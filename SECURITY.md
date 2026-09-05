# Security

Report suspected vulnerabilities privately through GitHub's security-advisory interface for this repository. Do not include real recovery phrases, private keys, viewing keys, or wallet exports in a report.

## Tool boundaries

- **Key Derivation Tool:** intended for a disconnected computer. Verify the checksum before use and independently verify valuable derived addresses.
- **Activity Viewer:** intentionally connects to public providers and accepts only public addresses, identities, public keys, and Orchard viewing capabilities. Providers can observe IP address, timing, and queried public identifiers.
- **Discovery Scanner:** accepts mnemonic material while online. Secret derivation runs in a sandboxed opaque-origin vault whose CSP blocks network and workers; a separate worker handles fixed read-only network operations. A compromised browser, extension, operating system, or modified HTML remains outside that boundary.

The tools do not construct, sign, or broadcast transactions. Provider data and indexed history have the trust limitations documented in the canonical source repository. This project has not received an independent cryptographic security audit.

Verify release files with `sha256sum -c SHA256SUMS` and use a clean browser profile or dedicated device for sensitive recovery work.
