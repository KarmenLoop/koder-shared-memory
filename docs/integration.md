# Host integration

The skill runs on top of host capabilities. It does not implement identity, a database, a transport, or chat-platform authentication. The names below describe responsibilities, not an HTTP API or a list of tool names to invent.

## Load it at the right boundaries

Load the skill in CLI, desktop, editor, private-chat, and group-chat session initialization. Preserve it when a task resumes, a model changes, or a connector reconnects. Installations scoped to one project or conversation cannot provide the default behavior across all entry points.

Hosts that support `agents/openai.yaml` may use its implicit-selection policy. For memory to apply on every turn, make the per-turn recall and persistence behavior part of the host's session flow. Selection metadata alone is insufficient.

## Required capabilities

| Responsibility | Input from the trusted host | Observable result |
| --- | --- | --- |
| Resolve space | Verified account, tenant, device, channel binding, and admitted sender | Stable space identity and current access scope |
| Retrieve | Space, task or conversation references, query, and bounded result budget | Relevant records with provenance, versions, and deletion filtering |
| Persist | Attributed content, event identity, task references, and actual result state | Durable local write receipt |
| Synchronize | Locally committed events and the last acknowledged cursor | Idempotent acknowledgments and incremental remote records |
| Report status | Local and remote receipts | Pending count, confirmed cursor, last confirmation time, and current failure or conflict |
| Revoke or delete | A currently authorized binding or content operation | Enforced access change or a deletion record that propagates |

Document concrete tool names, fields, limits, and failure codes in your host. Expose credentials only through the host's protected authentication mechanism.

## Identity and bindings

Use the existing account authority. A model API key is not a user identity. Link channels through an authenticated owner flow, and verify platform events before allowing a sender to access a space. A direct message from an unknown person does not establish ownership.

Use one default space across linked entry points. Retain channel, group, sender, and device identifiers as provenance. Explicitly separate spaces stay separate. For a group, apply the documented policy that admitted members may access associated private-chat memory in that linked space.

Never infer an account association from a display name, a typed email address, a group title, or a local path.

## Keep execution separate

Each request keeps its own reply route, live thread, cancellation state, and approvals. Shared records may explain what a task has already done. They must not grant execution rights, transfer a pending approval, or replay an executable queue.

If the same bot is configured on multiple devices, use the host's existing current-owner or lease mechanism for inbound processing. A standby device may receive memory without sending a second reply. Memory event deduplication does not replace inbound-message deduplication or tool-effect control.

## Persistence and synchronization

Commit locally before upload. Retain pending events across restarts. Reuse event identities after uncertain network results. Merge incremental remote updates without overwriting independent concurrent records.

Treat uploaded, acknowledged, and read on a destination device as distinct states. Validate remote payloads and current access before merging them. Keep credentials, approval tickets, and execution authority outside the sync stream.

An offline device cannot promise immediate awareness of a remote revocation. Report that limit accurately. Once revocation is known, stop subsequent remote access and follow host policy for cached data.

## Context and artifacts

Retrieve relevant material into the real model budget. Store the full history outside the prompt. Preserve actual tool receipts and original artifacts when summarizing.

A local absolute path on device A is not a usable file reference on device B. Use the host's resource-transfer system when file availability is required. Do not report file delivery based only on a memory record.

## Integration acceptance

Use the scenarios in [Validation](validation.md). Record which host version, connectors, accounts, device types, and service versions were actually tested. Publish a narrow status when only a subset works; the complete sharing policy remains the target.
