# Memory model

This document describes the meaning of shared records. It does not prescribe a database engine or claim that a server endpoint already exists.

## Space and source

A space is a stable sharing boundary established by verified identity and channel bindings. It survives local directory changes, application restarts, and model changes.

Provenance answers where a record came from: device, channel, chat, sender, source message, task, conversation, and observed time. Those values support attribution and deduplication. They do not split a linked space into a separate memory store for every sender or chat.

If a source field is unavailable, preserve that uncertainty. A model must not manufacture a platform identifier or claim an unverified account link.

## Record content

Keep explicit preferences, decisions, constraints, relevant messages, task progress, artifact references, and verified results. Preserve the distinction between user statements, external content, inference, and observed tool outcomes.

Task records should make continuation practical: what was requested, what has actually happened, what remains, where the artifacts are, and which claims are still unverified. A failed tool call remains a failure. An interrupted task is not complete because a summary exists.

Secrets, session tokens, device permissions, approval tickets, executable queues, and hidden model reasoning stay outside shared memory.

## Event identity and versions

Use host-issued event identity and an idempotency key that survives retries. Namespace platform message identifiers with their actual platform and binding so unrelated messages cannot collide.

An edit points to the version it supersedes. Concurrent edits preserve both branches until resolved. Device wall clocks provide context but do not prove causal order. Record an explicit user correction without erasing the earlier source.

## Synchronization states

| State | What it establishes |
| --- | --- |
| Local only | A durable local record exists; no shared service is linked |
| Waiting for account | Local work is available; verified remote association is missing |
| Pending | A local record is queued for upload |
| Syncing | A transfer is in progress |
| Server acknowledged | The service acknowledged specific events or a cursor |
| Read on target | The destination device actually retrieved the record |
| Conflict | Competing versions need resolution |
| Revoked | Current remote access has been denied or withdrawn |
| Error | An operation failed; its last confirmed state remains visible |

Keep the last confirmed cursor, acknowledgment time, pending count, and error details available. A connected socket or enabled toggle is not a synchronization receipt.

## Deletion and revocation

Starting a new chat clears the current view, not shared long-term memory. An explicit forgetting request creates a propagating deletion record or tombstone. Reconnecting devices must apply that record before exposing older cached content.

Deletion receipts should describe what was deleted locally, acknowledged remotely, and applied on other devices. They cannot prove that a person erased content already seen or copied outside the system.

Revoking a binding prevents subsequent authorized remote access through that binding. The host defines cache handling and offline behavior; the agent reports what can actually be verified.

## Group sharing and execution

Every admitted member of a linked group can use associated private-chat memory in that space. This policy should be visible during linking. It does not merge a member's unrelated private spaces into the group.

Reading a memory does not authorize acting on it. A recalled shell command, file path, or old approval is evidence about past work. Current actions still require the host's current execution authority and a valid target.
