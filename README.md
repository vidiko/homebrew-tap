# homebrew-tap

The Homebrew tap of the Vidiko organisation. It holds the Homebrew formulae
for VMAFx, the perceptual video quality library and toolkit, and for the tools
Vidiko builds on it.

```sh
brew install Vidiko/tap/vmafx
```

## The name

- **Meaning**: a Homebrew *tap* is a Git repository of formulae that
  `brew tap` adds next to the core formulae. Homebrew requires the repository
  name `homebrew-<name>`; `brew` then addresses it as `Vidiko/tap`.
- **Origin**: Vidiko is the organisation that succeeds VMAFx; new
  repositories of the project are created under it. The name *tap* is
  Homebrew's own term, from the beer-brewing vocabulary of the project.
- **Pronunciation**: HOME-brew tap (/ˈhoʊm.bruː tæp/).

## Status

Bootstrap. The repository carries its standards set-up (praetor) and licence;
the `vmafx` formula is written by the release job of
[VMAFx/vmafx](https://github.com/VMAFx/vmafx) after each release tag and is
not edited by hand.

## Development

```sh
make verify-all
```

runs the same gate as CI. Contribution rules are in
[CONTRIBUTING.md](CONTRIBUTING.md), agent rules in [AGENTS.md](AGENTS.md),
security reports in [SECURITY.md](SECURITY.md).

## Licence

homebrew-tap is licensed under the European Union Public Licence 1.2
([LICENSE](LICENSE)), the licence of VMAFx's own code. Licence and copyright
information for every file follows the [REUSE](https://reuse.software)
specification ([REUSE.toml](REUSE.toml), [LICENSES/](LICENSES/)).

<!-- praetor:readme-governance:start -->
[![HISS Adopted][praetor-hiss-badge]][praetor-hiss-agents]

Praetor manages this repository's declared governance policy. This managed
block records adoption state; it is not a verification certificate.

**Verification**: `make verify-all` runs the repository's configured
verification cascade.

**HISS Audit**: `praetorctl audit` enforces policy, generated-surface
integrity, and the debt ratchet.

**Context Sync**: `praetorctl compile-context --verify` verifies every
generated agent context against `AGENTS.md`.

**Debt Baseline**: `.standards-baseline.json` anchors the debt ratchet at
0 recorded infractions; audit forbids growth.

[praetor-hiss-badge]: https://img.shields.io/badge/Standards-HISS%20Adopted-blue
[praetor-hiss-agents]: https://github.com/vidiko/homebrew-tap/blob/HEAD/AGENTS.md
<!-- praetor:readme-governance:end -->
