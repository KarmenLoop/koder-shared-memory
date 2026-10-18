# Getting started

## Before you begin

You need a KODER build that can load skills and expose persistent memory tools. Cross-channel use also needs working chat connectors. Cross-device use needs a shared service and a verified device association.

The skill package does not require a model subscription of its own. Your host, model provider, messaging platform, and storage service may have separate requirements or charges. This repository does not configure or purchase those services.

## Build and import the package

From the repository root:

```bash
python3 scripts/check_repository.py
python3 scripts/package_skill.py
```

The second command creates `dist/koder-shared-memory.skill.zip`. Import it through the skill or resource importer in your KODER build. Exact controls vary by build; this guide does not assume a particular settings screen or undocumented command.

If your host loads folders directly, install the `skills/koder-shared-memory/` folder in its documented skill directory. Keep `SKILL.md` and `agents/openai.yaml` together. Do not copy credentials or runtime data into the package.

## Check the host connection

Confirm that the host can:

1. Resolve the current account, device, and memory space from verified identity.
2. Persist a record and retrieve it after restarting the application.
3. Map each linked channel to that same space.
4. Report synchronization status from actual receipts.
5. Load the skill for each turn, including desktop tasks and resumed conversations.

If a capability is missing, keep the working local path available and report the missing integration. A successful import does not establish these capabilities.

## Try a first handoff

Use a test space and content intended for everyone in the linked group.

On the desktop:

> Remember that the demo review is on Thursday. The sample report is drafted, but the charts still need review.

In a linked private chat:

> What is left to do before the demo review?

As another member of a linked group:

> Pick up the demo review. What is ready, and what still needs work?

Verify the retrieved source, task state, and reply destination. Then repeat on a second physical device and check that the source record was acknowledged and the receiving device actually retrieved it.

## Understand group visibility

This skill's default allows every member of a linked group to use associated private-chat memory in that space. Explain this when linking the group. Use explicitly separate spaces for material that should not enter that shared scope.

Continue with [Host integration](integration.md), [Memory model](memory-model.md), or the [Validation guide](validation.md).
