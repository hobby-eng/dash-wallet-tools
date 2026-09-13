# Dash Community Wallet Tools

Independent Dash-focused distribution of four standalone browser utilities:

- **Dash Community Key Derivation Tool** — offline derivation for Dash Core, Platform Payments, Platform Identity keys, Purpose48 multisig cosigner material, and Orchard.
- **Dash Community Activity Viewer** — read-only Core, Platform Payment, Identity, and Orchard inspection.
- **Dash Community Discovery Scanner** — BIP39 candidate and watch-only discovery with an isolated, network-disabled Secret Vault and a separate read-only Network Worker.
- **Dash Community PSBT & Multisig Inspector** — offline Dash Core PSBT/Script review, public message verification, BIP38 decryption, and test P2SH multisig/watch-only policy construction.

Each release contains self-contained HTML files intended to be downloaded and opened directly with `file://`. No installation or hosted web application is required. The visual treatment follows the official Dash BrandBook and Brand Guidelines.

## Verify a download

Download all release assets into one directory, then run:

```bash
sha256sum -c SHA256SUMS
```

Each release also includes `verification-record.json`, which records the canonical source revision, pinned toolchain, performed check groups, and artifact hashes. Tagged release assets receive GitHub build-provenance attestations from this repository. Verify an individual file online with GitHub CLI:

```bash
gh attestation verify Dash_Community_Key_Derivation_Tool.html -R hobby-eng/dash-wallet-tools
```

## Safety boundaries

The Key Derivation Tool and PSBT & Multisig Inspector are intended for offline use and block runtime network access. The Activity Viewer is connected but rejects private wallet material. The Discovery Scanner has separate Seed phrase and Public keys modes, each with Single and Batch input. Seed discovery necessarily accepts secret material while online, confines it to the network-disabled vault, and sends only validated public lookups to the network worker.

The Inspector does not sign, finalize, fund, query UTXOs, or broadcast transactions. None of the four tools creates or broadcasts recovery transactions. Use a clean device for sensitive recovery work, independently verify valuable results in a maintained Dash wallet, and move recovered funds to a new wallet. Read [SECURITY.md](SECURITY.md) before using valuable wallet data.

## Provenance

This repository is an independent Dash Community release surface, not a source fork. Application, cryptographic, build, documentation, and verification sources remain canonical in [hobby-eng/multi-chain-wallet-tools](https://github.com/hobby-eng/multi-chain-wallet-tools). Every release identifies the exact canonical source tag and commit and is rebuilt with that source repository's pinned Docker toolchain. The workflow verifies the exact Dash-only bundle before publication; Multi-Chain artifacts are excluded.

This is an independent hobby project and is not endorsed by Dash Core Group or other upstream projects. See [ATTRIBUTION.md](ATTRIBUTION.md).

## Releasing

Maintainers run **Build and publish Dash Community release** manually only after the matching canonical Multi-Chain tag workflow succeeds, with:

- `source_ref`: the immutable `v<version>` tag in `hobby-eng/multi-chain-wallet-tools`;
- `release_tag`: the same `v<version>` value for this repository.

The workflow requires both inputs to match, performs the complete canonical build, verifies the exact Dash-only asset set and checksums, loads the curated Dash release notes from the canonical source tag, generates provenance attestations, and publishes the release.
