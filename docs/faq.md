# Frequently asked questions

## Does importing the skill connect my chat accounts?

No. The host supplies connectors, sign-in, and verified bindings. The skill explains how to use the capabilities that are actually available.

## Does this include a cloud memory server?

No. It includes the behavior and integration contract. Cross-device synchronization requires a working host service.

## Can everyone in a linked group use private-chat memory?

Yes, for associated private-chat memory in that linked space. This is the intended default and should be disclosed when linking the group. Unrelated spaces stay separate.

## Will a new chat erase everything?

No. A new chat resets the current conversation view. Explicit forgetting uses the host's shared deletion mechanism.

## Can I keep working offline?

If the host supports local persistence, local work can continue and remain pending for synchronization. Other devices cannot read changes until they are actually transferred.

## Does shared memory give a group control of my computer?

No. Memory visibility and execution authority are separate. Current operations remain subject to the host's permissions and approval rules.

## Will every file be copied to every device?

No. Memory stores artifact references and relevant context. File transfer requires a separately authorized, working resource path.

## Will this remember activity KODER never observed?

No. An application must be connected, or its work must be imported through an authorized capability, before KODER can persist that context.

## Is this compatible with Hermes or another agent?

The skill uses a portable Markdown format. Another host can adapt it, but compatibility is not established until that host exposes the required tools and passes the behavioral scenarios.

## Can I use and modify it commercially?

The files in this repository are distributed under the [Apache License 2.0](../LICENSE). Other runtimes, platforms, connectors, and services retain their own terms.
