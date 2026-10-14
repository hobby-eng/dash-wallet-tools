# AUD-002 distribution follow-up

This follow-up uses the existing distribution checkout at HEAD `a4c9075d5b0a3cca9eedd9963a345a02352cd23d`, with the pre-existing unpublished workflow change preserved. The source fingerprint in the report identifies the exact reviewed bytes. AUD-001 and its retained evidence remain historical.

From this repository root, run the unchanged local resolver harness through the shared capture service:

```sh
python3 ../multi-chain-wallet-tools/docs/audits/AUD-028-harnesses/capture.py . 2 rerun-resolver python3 docs/audits/AUD-001-harnesses/resolve.py
```

The harness executes the actual release workflow Bash against 13 public synthetic API replies with a local `gh` substitute. It makes no GitHub requests and publishes nothing. Its temporary fixtures are removed when each case ends; the new command record and log are retained only in ignored `AUD-002-evidence/`. A mismatch exits nonzero; success reports 13 cases. Python 3, Bash and jq must already be installed.

Upstream fixes and four Dash Community HTML pages are verified once in multi-chain-wallet-tools AUD-029. This distribution record references that source fingerprint and preserves original upstream finding IDs without inventing distribution findings or claiming a release is accepted. MnemoCode remains an explicitly unreleased owner handover.

The shared generator and validator are `../multi-chain-wallet-tools/docs/audits/AUD-029-harnesses/report.py` and `validate.py`, executed from the upstream repository. They need both repositories' final snapshots and current command evidence. They bind reports to all 32 canonical procedure checks and unchanged baseline reports. No browser, artifact download, launcher execution, paid CI, commit, signing or publishing is performed.
