# Contributing

Thanks for helping make context easier to carry between places people work.

## Useful contributions

We welcome clearer skill instructions, realistic continuation examples, documentation fixes, and host integration reports backed by actual results. Changes should preserve default sharing within linked spaces and the separation between memory access and execution authority.

For a bug, describe what you expected, what happened, your host and skill versions, and the entry points involved. Include the smallest synthetic reproduction you can provide. For an integration report, distinguish a local fixture from real platform accounts and physical-device testing.

## Make a change

1. Fork the repository and create a focused branch.
2. Change the skill or documentation and keep related guides consistent.
3. Run `python3 scripts/check_repository.py` and `python3 scripts/package_skill.py`.
4. Describe the behavior change, checks performed, and remaining limits in your pull request.

Use natural American English throughout the public repository. Prefer concrete examples and observable results over broad capability claims. Keep the main skill self-contained so hosts can import it without needing every documentation file.

## Handle data carefully

Use synthetic messages and sample files. Do not submit private chats, API keys, account exports, personal databases, or internal workspaces. Report security issues through [SECURITY.md](SECURITY.md).

By submitting a contribution, you agree that your contribution may be distributed under this repository's [Apache License 2.0](LICENSE). Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
