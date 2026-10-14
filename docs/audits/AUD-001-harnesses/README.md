# AUD-001 distribution harness

This harness belongs to the Dash distribution audit at commit `a4c9075d5b0a3cca9eedd9963a345a02352cd23d` plus the working-tree source identified in the paired report. It tests the actual first resolver Bash block from `.github/workflows/release.yml` with synthetic stable, draft, prerelease, already-distributed, below-floor and manual-request API replies.

`resolve.py` replaces only `gh` with a local fixture command and uses the installed `jq`. Thirteen cases assert exit status and exact outputs. It contacts no GitHub endpoint, creates no release and changes no project source. Temporary fixture files exist only in the ignored evidence directory and are removed by the harness.

From the Dash repository root:

```sh
python3 docs/audits/AUD-001-harnesses/resolve.py
python3 ../multi-chain-wallet-tools/docs/audits/AUD-028-harnesses/capture.py . 1 fresh-resolver python3 docs/audits/AUD-001-harnesses/resolve.py
```

The shared [command recorder](../../../../multi-chain-wallet-tools/docs/audits/AUD-028-harnesses/capture.py) owns serialization, memory monitoring, source binding, UTC logs and original evidence retention. Its hash is pinned in AUD-001. Expected output is thirteen `passed: true` records and a summary; any incorrect workflow decision raises an assertion and exits nonzero. Compilation, actual runners, attestations, publishing, executable browser behavior and canonical artifacts are not established by these fixture tests.

Evidence stays local in ignored `../AUD-001-evidence/`; the report and harness are separate reviewable files. No commit or publication is authorized by the audit.
