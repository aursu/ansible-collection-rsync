# Changelog

All notable changes to `aursu.rsync` are documented here.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2026-09-22

### Fixed

- **The collection declared no dependencies at all, while the role calls two.**
  `roles/rsync` uses `community.crypto.openssh_keypair` and
  `ansible.posix.authorized_key`, and `galaxy.yml` listed neither - so installing this collection
  from Galaxy pulled nothing, and the role had no modules to call. It worked only where the
  consuming project happened to list both itself, which is how it went unnoticed.

- **`roles/rsync/meta/main.yml` carried a role tag Galaxy rejects.** Role tags must be lowercase
  letters and digits only; `file-transfer` contains a hyphen. Now `filetransfer`.

- **`manage_dir: yes`** rather than `true`, and trailing whitespace in three files. Cosmetic, but
  they were what stood between this collection and a blocking lint.

### Added

- **CI.** `test` runs the unit tests, compiles the plugins, and runs a **blocking** `ansible-lint`;
  `release` publishes to Galaxy on a `v*` tag, gated by
  `.github/scripts/release_preflight.py`, which refuses a tag that disagrees with `galaxy.yml` and
  a version Galaxy already holds - both unrecoverable once uploaded.

  `.ansible-lint` warn-lists the pre-existing stylistic rules by name, including
  `command-instead-of-module` and `no-changed-when`, which are deliberate here: the role shells out
  to `rsync` because the `synchronize` module cannot express the `-e "ssh -i <key>"` it needs for
  its generated per-target key. `load-failure` and `syntax-check` are tagged `unskippable` and
  cannot be warn-listed away, which is what makes blocking safe.

- **`build_ignore`**, keeping `.github`, `.pytest_cache` and `dist` out of the published artifact.
