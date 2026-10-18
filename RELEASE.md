# Releasing a skill package

This guide is for maintainers with publishing access to `KarmenLoop/koder-shared-memory`.

## Prepare the version

Update `VERSION`, the skill's `metadata.version`, and `CHANGELOG.md` together. Use a version that reflects changes to the skill and its contract; it does not describe the release state of the KODER runtime or connectors.

Review public claims, group visibility, license notices, and documentation links. Confirm that the publication contains no private data or internal workspace material.

## Validate and package

```bash
python3 scripts/check_repository.py
python3 scripts/package_skill.py
```

Keep the generated `dist/manifest.json` with the release. It records the archive digest and the size and digest of each packaged file. Verify the archive with the target host's importer when reporting host compatibility.

## Publish

Commit the reviewed source, push it to the intended repository, and create a version tag and GitHub Release that point to that exact commit. Attach:

- `dist/koder-shared-memory.skill.zip`
- `dist/manifest.json`

Write release notes in English. Explain what changed, what was actually checked, and which host or platform scenarios remain unverified. Do not present a skill-only release as a deployed synchronization service.

After publication, verify the repository owner, public visibility, default branch, license detection, release tag, and downloadable assets. Compare the uploaded archive digest with the local manifest.

## Correct a published problem

Keep an accurate changelog. Prefer a new version for changed content rather than silently replacing a tagged package. If sensitive material was exposed, follow the private reporting process in [SECURITY.md](SECURITY.md) and address the exposure before preparing another release.
