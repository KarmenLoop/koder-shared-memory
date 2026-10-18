# Validation

Validate the package and the host integration separately. Use a dedicated test space, synthetic content, and accounts and devices you are authorized to use. Do not publish real conversations or credentials as evidence.

## Local repository checks

```bash
python3 scripts/check_repository.py
python3 scripts/package_skill.py
```

The checks inspect required files, skill metadata, local documentation links, English-only content, and archive round-trip integrity. The package includes the skill, its UI metadata, the license, and the notice.

These checks do not call a model, inspect a personal account, install a connector, or prove cross-device behavior. Review the skill's decisions with realistic host tests as well as structural checks.

## Behavioral scenarios

| Scenario | Required observation |
| --- | --- |
| Desktop to WeChat private chat | The same fact and actual task state are retrieved with provenance |
| WeChat to Feishu private chat to another group member | Associated private context is available to the linked group member |
| Feishu group to WeCom private chat to another WeCom group member | All three entry points resolve the same authorized space |
| Computer A to phone to computer B | The target devices retrieve the actual source record; different local paths do not matter |
| Restart, reconnect, and model change | Space and task references remain stable |
| Two devices append or edit concurrently | Independent facts survive and competing versions remain visible |
| Offline write followed by reconnect and redelivery | Pending records survive restart and deduplicate on upload |
| Delete, then reconnect an old device | Older content does not reappear |
| Revoke a device or group binding | Later online reads and writes are denied under current policy |
| Same display name on an unrelated account | No account merge or unauthorized read occurs |
| Pending approval in another chat | Shared history does not transfer approval authority |
| Two devices configured for the same bot | Only the current host owner processes an inbound message; memory sync sends no duplicate reply |
| Long history or oversized tool output | Relevant context fits the actual model budget; original records remain available |
| Credentials in source content | Secrets are excluded from shared records and replies |

## Record useful evidence

For each scenario, record the host and skill versions, source and target entry points, space and event references, actual tool receipts, observed response, and pass, fail, or unverified status. Redact account and message identifiers before publishing them.

Keep these evidence levels distinct:

1. Repository and package checks.
2. A local host fixture with multiple clients.
3. Real messaging accounts and linked groups.
4. Different physical computers and phones.
5. A deployed service with restart, revocation, and recovery checks.

A mock client is not a physical-device test. An upload acknowledgment is not a remote read. A successful import is not complete platform support.

## Publishing integration results

Publish only the scope actually observed. Include failures and unverified scenarios. For a reproducible bug report, follow [CONTRIBUTING.md](../CONTRIBUTING.md) and the private-reporting guidance in [SECURITY.md](../SECURITY.md).
