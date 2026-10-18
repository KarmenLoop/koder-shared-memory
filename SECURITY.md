# Security policy

## Reporting a concern

Please do not post credentials, private conversations, account identifiers, or a working exploit in a public issue.

Check this repository's Security tab for private vulnerability reporting. If it is enabled, use that channel. If it is not available, open a minimal issue asking a maintainer for a private reporting method. Keep sensitive details out of that request.

A useful private report explains the affected version, host integration, expected boundary, actual result, and a synthetic reproduction. Examples include cross-account memory access, a revoked binding retaining access, secret disclosure, or retrieved content granting execution authority.

## Scope

This repository distributes a skill and integration guidance. A defect in a host's identity, storage, connector, or synchronization implementation may need to be reported to that host's maintainers as well. Do not assume a skill text change can repair a server-side authorization defect.

We do not promise a response deadline or describe an unverified integration as secure. Fixes and published results should state the scope actually tested.
