# Dash Community Wallet Tools

Independent Dash-focused distribution of three standalone browser utilities:

- **Dash Community Key Derivation Tool** — offline derivation for Dash Core, Platform payments, Platform Identity keys, and Orchard.
- **Dash Community Activity Viewer** — read-only Core, Platform, Identity, and Orchard inspection.
- **Dash Community Discovery Scanner** — seed-phrase and watch-only public-key discovery with an isolated, network-disabled secret vault and a separate read-only network worker.

Each release contains self-contained HTML files intended to be downloaded and opened directly with `file://`. No installation or hosted web application is required.

## Verify a download

Download all release assets into one directory, then run:

```bash
sha256sum -c SHA256SUMS
```

The Key Derivation Tool is intended for offline use. The Activity Viewer is network-enabled but rejects private wallet material. The Discovery Scanner has separate Seed phrase and Public keys modes, each with Single and Batch input. Seed-phrase discovery necessarily accepts secret material while online, confines it to the network-disabled vault, and sends only derived public lookups to the network worker. Use a clean device and move recovered funds to a new wallet. Read [SECURITY.md](SECURITY.md) before using valuable wallet data.

## Provenance

This repository is an independent Dash Community release surface, not a source fork. Application, cryptographic, build, and verification sources remain canonical in [hobby-eng/multi-chain-wallet-tools](https://github.com/hobby-eng/multi-chain-wallet-tools). Every release identifies the exact canonical source commit and is rebuilt with that repository's pinned Docker toolchain. Only the verified Dash Community bundle is published here; Multi-Chain artifacts are excluded.

This is an independent hobby project and is not endorsed by Dash Core Group or other upstream projects. See [ATTRIBUTION.md](ATTRIBUTION.md).

## Releasing

Maintainers run **Build and publish Dash Community release** manually with:

- `source_ref`: an immutable commit or tag in `hobby-eng/multi-chain-wallet-tools`;
- `release_tag`: the matching `v<package.json version>` tag for this repository.

The workflow performs the complete canonical build, verifies the exact Dash-only asset set, generates provenance attestations, and publishes the release.
