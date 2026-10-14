"""Exercise the actual release resolver with public synthetic API replies; never publish."""

import json
import os
import pathlib
import subprocess
import tempfile


class ReleaseResolverProbe:
    """Own fixtures and execute the workflow's unchanged Bash with a local gh substitute."""

    def __init__(self):
        self.root = pathlib.Path(__file__).resolve().parents[3]
        workflow = (self.root / ".github/workflows/release.yml").read_text()
        block = workflow.split("        run: |\n", 1)[1]
        lines = []
        for line in block.splitlines():
            if line and not line.startswith("          "):
                break
            lines.append(line[10:] if line else "")
        self.script = "\n".join(lines)

    @staticmethod
    def release(tag, date="2026-10-01T00:00:00Z", **extra):
        return {"tag_name": tag, "published_at": date, "draft": False,
                "prerelease": False, **extra}

    def run(self):
        stable = self.release("v0.1.5")
        earlier = self.release("v0.1.2", "2026-09-01T00:00:00Z")
        cases = [
            ("empty", [], [], "schedule", "", "", 0, None),
            ("stable", [stable], [], "schedule", "", "", 0, "v0.1.5"),
            ("oldest-first", [stable, earlier], [], "schedule", "", "", 0, "v0.1.2"),
            ("existing-skipped", [stable, earlier], [earlier], "schedule", "", "", 0, "v0.1.5"),
            ("all-distributed", [stable], [stable], "schedule", "", "", 0, None),
            ("floor", [self.release("v0.1.1")], [], "schedule", "", "", 0, None),
            ("draft", [self.release("v0.1.5", draft=True)], [], "schedule", "", "", 0, None),
            ("prerelease", [self.release("v0.1.5", prerelease=True)], [], "schedule", "", "", 0, None),
            ("manual", [stable], [], "workflow_dispatch", "v0.1.5", "v0.1.5", 0, "v0.1.5"),
            ("manual-mismatch", [stable], [], "workflow_dispatch", "v0.1.4", "v0.1.5", 1, None),
            ("manual-incomplete", [stable], [], "workflow_dispatch", "v0.1.5", "", 1, None),
            ("manual-draft", [self.release("v0.1.5", draft=True)], [], "workflow_dispatch", "v0.1.5", "v0.1.5", 1, None),
            ("manual-existing", [stable], [stable], "workflow_dispatch", "v0.1.5", "v0.1.5", 0, None),
        ]
        evidence = self.root / "docs/audits/AUD-001-evidence"
        evidence.mkdir(parents=True, exist_ok=True)
        for name, canonical, distribution, event, source, tag, code, expected in cases:
            with tempfile.TemporaryDirectory(prefix="resolver-", dir=evidence) as folder:
                path = pathlib.Path(folder)
                (path / "fixtures.json").write_text(json.dumps({"canonical": [canonical],
                                                              "distribution": [distribution]}))
                stub = path / "gh"
                stub.write_text("""#!/usr/bin/python3
import json, sys
from pathlib import Path
fixtures = json.loads(Path('fixtures.json').read_text())
url = sys.argv[-1]
if '/releases/tags/' in url:
    tag = url.rsplit('/', 1)[-1]
    row = next((row for row in fixtures['canonical'][0] if row['tag_name'] == tag), None)
    if row is None:
        raise SystemExit(1)
    print(json.dumps(row))
else:
    print(json.dumps(fixtures['canonical'] if 'multi-chain-wallet-tools' in url else fixtures['distribution']))
""")
                stub.chmod(0o700)
                output = path / "outputs"
                env = {**os.environ, "PATH": f"{path}:/usr/bin:/bin", "GH_TOKEN": "public-fixture",
                       "GITHUB_REPOSITORY": "example/distribution", "GITHUB_OUTPUT": str(output),
                       "EVENT_NAME": event, "MANUAL_SOURCE_REF": source, "MANUAL_RELEASE_TAG": tag}
                result = subprocess.run(["/bin/bash", "-c", self.script], cwd=path, env=env,
                                        capture_output=True, timeout=10)
                values = dict(line.split("=", 1) for line in output.read_text().splitlines())
                assert result.returncode == code, (name, result.stderr.decode())
                assert values.get("publish") == ("true" if expected else "false"), (name, values)
                if expected:
                    assert values["source_ref"] == values["release_tag"] == expected, (name, values)
                print(json.dumps({"case": name, "exitCode": result.returncode,
                                  "outputs": values, "passed": True}))
        print(f"Passed {len(cases)} actual workflow resolver cases; no GitHub requests or publication.")


if __name__ == "__main__":
    ReleaseResolverProbe().run()
