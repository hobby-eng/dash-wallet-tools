# Security

Report suspected vulnerabilities privately through GitHub's security-advisory interface for this repository. Do not include real recovery phrases, private keys, viewing keys, or wallet exports in a report.

## Tool boundaries

- **Key Derivation Tool:** intended for a disconnected computer. Verify the checksum before use and independently verify valuable derived addresses.
- **Activity Viewer:** intentionally connects to public providers and accepts only public addresses, identities, public keys, and Orchard viewing capabilities. Providers can observe IP address, timing, and queried public identifiers.
- **PSBT & Multisig Inspector:** intended for a disconnected computer. It reviews supported public transaction/policy data and can decrypt BIP38 locally, but does not sign, finalize, fund, query UTXOs, persist data, or broadcast transactions.
- **Discovery Scanner:** separates Seed phrase and Public keys modes, each with Single and Batch input. Secret derivation and watch-only child derivation run in a sandboxed opaque-origin vault whose CSP blocks network and workers; a separate worker handles fixed read-only network operations using derived public lookups. Public keys and viewing capabilities cannot spend funds but remain privacy-sensitive. A compromised browser, extension, operating system, or modified HTML remains outside that boundary.

The tools do not construct, sign, or broadcast transactions. Provider data and indexed history have the trust limitations documented in the canonical source repository. This project has not received an independent cryptographic security audit.

Verify release files with `sha256sum -c SHA256SUMS` and use a clean browser profile or dedicated device for sensitive recovery work.
