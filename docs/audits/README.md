# Audit records

Numbers are local to this repository. Markdown and JSON companions describe the same snapshot. Reports follow the canonical [audit standard](../../../multi-chain-wallet-tools/docs/audits/AUDIT_STANDARD.md), [template](../../../multi-chain-wallet-tools/docs/audits/AUDIT_TEMPLATE.md), [procedure](../../../multi-chain-wallet-tools/docs/FULL_AUDIT_GUIDE.md) and [schema](../../../multi-chain-wallet-tools/docs/audit-report.schema.json); their exact hashes are recorded in each report.

1. [AUD-001](AUD-001-2026-10-12.md) · [JSON](AUD-001-2026-10-12.json) — 2026-10-12; distribution workflow/document review and 13 release-selection fixtures; inherited runtime/build findings retain their IDs in the paired upstream AUD-028
2. [AUD-002](AUD-002-2026-10-12.md) · [JSON](AUD-002-2026-10-12.json) — 2026-10-12; 13 distribution resolver cases and upstream remediation bound to AUD-029, with no publication or release acceptance

Evidence stays in ignored `AUD-001-evidence/`. Reproducible local fixtures are in `AUD-001-harnesses/`. This audit does not authorize committing, publishing or accepting unresolved upstream assets.

## Publication privacy

Published machine-owner paths use `/home/user/...`; report time zone is explicitly UTC (+00:00). Historical records retain their original instants and date precision. Privacy-only metadata does not rerun checks or change findings, counts, source or artifact hashes. Each paired record retains its pre-edit document hashes and original document bindings as provenance; updated document bindings identify publication bytes only. Raw local evidence remains unchanged. See the [privacy metadata harness](../../../multi-chain-wallet-tools/docs/audits/AUD-030-harnesses/privacy-README.md) for the repeatable rebind-only step after document formatting.
