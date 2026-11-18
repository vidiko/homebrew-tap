---
description: Homebrew tap of the Vidiko organisation: formulae for VMAFx.
---

# homebrew-tap

The Homebrew tap of the Vidiko organisation holds formulae for VMAFx, the
perceptual video quality library and toolkit, and the tools Vidiko builds on
it ([README](../README.md)).

```sh
brew tap Vidiko/tap
brew install Vidiko/tap/vmafx
```

There is no formula yet; the install command will work after the first final
VMAFx release's formula pull request merges
([ADR-3387][adr-3387]).

## How a formula arrives

The VMAFx release job generates the formula and opens a pull request on the
tap. The tap's required checks run before the pull request merges. An
identical formula already in the tap is left alone; release candidates are
not published to the tap
([ADR-3387][adr-3387]).

## The name

A Homebrew *tap* is a Git repository of formulae that `brew tap` adds next to
the core formulae. Homebrew requires the repository name `homebrew-<name>`;
`brew` addresses this one as `Vidiko/tap`
([Homebrew Taps](https://docs.brew.sh/Taps)).

Vidiko is the organisation that succeeds VMAFx; new project repositories are
created under it. *Tap* is Homebrew's own term from its beer-brewing
vocabulary. Pronunciation is **HOME-brew tap** (/ˈhoʊm.bruː tæp/).

## Where to go next

| Page | What it covers |
| :--- | :--- |
| [README](../README.md) | The tap, installation and release process. |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution and verification. |
| [decision records](adr/README.md) | The tap's architectural decisions. |

[adr-3387]: https://github.com/VMAFx/vmafx/blob/master/docs/adr/3387-homebrew-tap-publish.md
