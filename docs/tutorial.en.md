# KODER Shared Memory: from package to first handoff

English | [简体中文](tutorial.zh-CN.md) · [Project](../README.md)

This guide matches **v1.0.0**. It consolidates the practical path from [getting-started](getting-started.md), [integration](integration.md), and [faq](faq.md) into one install → practice → troubleshoot → update flow.

## 1. Before you begin

You need a Koder (or other) host that can:

- load skills, and
- expose persistent memory tools.

Cross-channel use also needs working chat connectors. Cross-device use needs a shared service and verified device association.

The skill package does **not** require its own model subscription. Your host, model provider, messaging platform, and storage service may have separate requirements or charges. This repository does not configure or purchase those services.

## 2. Build and import

From the repository root (Python 3.10+):

```bash
python3 scripts/check_repository.py
python3 scripts/package_skill.py
```

Import `dist/koder-shared-memory.skill.zip` through your host’s skill or resource importer. Exact UI controls vary by build.

If the host loads folders directly, install `skills/koder-shared-memory/` in its documented skill directory. Keep `SKILL.md` and `agents/openai.yaml` together. Do **not** copy credentials or runtime data into the package.

Enable the skill across every entry point you want to link. A project-only or conversation-only setting limits where it is available. Metadata alone does not guarantee default recall on every turn—wire per-turn recall into the host session flow when you need that behavior ([integration](integration.md)).

## 3. Check the host connection

Confirm the host can:

1. Resolve account, device, and memory space from **verified** identity.
2. Persist a record and retrieve it after restarting the application.
3. Map each linked channel to that same space.
4. Report synchronization status from **actual receipts**.
5. Load the skill for each turn, including desktop tasks and resumed conversations.

A successful import does **not** establish these capabilities.

## 4. First handoff (first task)

Use a **test space** and content intended for everyone in the linked group.

**On the desktop:**

> Remember that the demo review is on Thursday. The sample report is drafted, but the charts still need review.

**In a linked private chat:**

> What is left to do before the demo review?

**As another member of a linked group:**

> Pick up the demo review. What is ready, and what still needs work?

Verify retrieved source, task state, and **reply destination**. Then repeat on a second physical device and check that the source record was acknowledged and the receiving device actually retrieved it.

### Group visibility

The default allows every member of a linked group to use associated private-chat memory in that space. Explain this when linking. Use separate spaces for material that should not enter that shared scope.

## 5. Troubleshoot

- **Import succeeded but recall is empty:** Host may lack persistent tools, space binding, or per-turn loading—see [integration](integration.md).
- **Wrong chat answered:** Conversations stay independently routed; check reply destination, not only memory content.
- **Group saw private details unexpectedly:** Review linking disclosure and space separation ([faq](faq.md)).
- **Offline / pending sync:** Local work may continue; other devices cannot read changes until transferred. Report pending vs confirmed honestly.
- **File not on the other device:** Memory stores references; transfer needs a separately authorized resource path.
- **Another host (Hermes, etc.):** Portable Markdown helps, but compatibility is not established until required tools pass behavioral scenarios ([validation](validation.md)).

## 6. Update, roll back, or remove

1. Keep your own memory data and host config **outside** the skill package directory.
2. Download or rebuild a new verified package; install into a fresh skill location when the host refuses overwrite.
3. Close or refresh host sessions after switching versions.
4. To roll back, restore the previous skill folder and refresh discovery.
5. To remove, delete only the skill directory you installed; this package does not install a system service. Host-side memory stores and account bindings remain until you clear them through the host.

Read [CHANGELOG.md](../CHANGELOG.md) and [RELEASE.md](../RELEASE.md) before publishing or relying on a new package.

## 7. Integration substance (checklist)

| Responsibility | Observable result |
| --- | --- |
| Resolve space from verified bindings | Stable space identity and access scope |
| Retrieve with provenance | Records with versions and deletion filtering |
| Persist with event identity | Durable local write receipt |
| Synchronize | Idempotent acknowledgments; distinct uploaded / acknowledged / read states |
| Keep execution separate | No silent replay of queues or transferred approvals |

Full contract: [integration.md](integration.md) · [memory-model.md](memory-model.md).

[Project home](../README.md) · [简体中文教程](tutorial.zh-CN.md)
