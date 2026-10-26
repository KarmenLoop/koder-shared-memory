# KODER Shared Memory

[English](README.md) | 简体中文 · **v1.0.0**

[![Format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-2563eb)](skills/koder-shared-memory/SKILL.md)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-16a34a)](LICENSE)
[![Release](https://img.shields.io/github/v/release/KarmenLoop/koder-shared-memory)](https://github.com/KarmenLoop/koder-shared-memory/releases)

**可移植技能：在已关联的对话与设备间保留经批准的工作上下文——动手前先回忆，边做边保存真实结果，执行权仍由宿主掌握。**

规定智能体应回忆什么、保存什么，以及如何处理更正和未完成任务。为 [Koder](https://karmenloop.com) 编写；其他宿主若能提供身份、存储、检索与同步，也可适配。本仓库提供**规则与接入契约**，不提供托管记忆服务、聊天连接器或同步守护进程。

[下载](https://github.com/KarmenLoop/koder-shared-memory/releases/latest) · [中文教程](docs/tutorial.zh-CN.md) · [English tutorial](docs/tutorial.en.md) · [技能入口](skills/koder-shared-memory/SKILL.md) · [Apache 2.0](LICENSE)

---

## 为什么做这个

任务可能从私聊开始，再到群聊或桌面继续。没有共享规则时，智能体要么忘掉决定，要么在错误设备上静默重放命令。本技能约定如何携带相关决定、限制、偏好与进度——同时保持**对话各自路由**，并把**执行权与记忆可见性分开**。

关联账号、渠道或设备后，使用对应记忆空间。关联群组可能让成员接触该空间的关联私聊记忆；宿主必须在关联前向所有者解释。

---

## 一览

| | |
| --- | --- |
| **安装内容** | 可移植技能包（`SKILL.md` + 元数据），ZIP 或目录加载 |
| **版本** | **1.0.0**（`VERSION`，首发） |
| **依赖** | 能加载技能并提供持久记忆工具的宿主；打包需 Python **3.10+** 标准库 |
| **打包网络** | 本地检查与打 ZIP **不**连接模型或消息账号 |
| **预期入口** | 飞书 / 企业微信私聊与群聊 · 微信私聊 · 桌面 CLI/应用/编辑器 · 已关联设备 |
| **许可** | [Apache License 2.0](LICENSE) |
| **不含** | 托管同步服务、平台登录适配器、自动命令重放 |

---

## 是 / 不是

| 是 | 不是 |
| --- | --- |
| 跨渠道 / 跨设备上下文的技能与契约 | 云端记忆 SaaS 或同步守护进程 |
| 工作前回忆；保存事实与实际结果 | 静默再次授权或重放执行队列 |
| 已披露的关联群私聊记忆策略 | 偷偷合并无关账号或空间 |
| 来源、版本、冲突、删除、同步回执 | 打包检查等于真实平台同步已通 |
| 面向 Koder、可适配其他宿主的 Markdown 技能 | 不接宿主流程也能保证每轮默认回忆 |

---

## 覆盖范围

- 工作前检索相关决定、约束与任务状态。
- 随工作保存重要决定和实际结果（含失败、取消、未完成）。
- 在已验证的私聊、群组和桌面入口使用同一空间；跨设备用稳定引用。
- 关联群组成员可使用该空间的关联私聊记忆（须事先披露）。
- 在模型上下文窗口内只取相关材料与有限摘要，完整记录持久保存。
- 执行仍由宿主管理：记住某个动作 ≠ 再次授权或在别的设备重放。

## 平台要求（接入要求，非已测矩阵）

| 入口 | 预期范围 | 宿主需提供 |
| --- | --- | --- |
| 飞书 | 私聊、群聊 | 验证渠道关联、入站消息与记忆工具 |
| 企业微信 | 私聊、群聊 | 同上 |
| 微信 | 私聊 | 可用连接器与记忆工具 |
| 桌面 | CLI、应用、编辑器、代码、文件、浏览器等已授权活动 | 每条执行路径加载技能并可访问记忆 |
| 其他电脑/手机 | 相同关联空间 | 验证设备关联与真实同步 |

表格描述接入要求，不表示某版 Koder 已安装并测试全部连接。技能只能记录宿主经授权观察或导入的工作。

---

## 下载与导入

```sh
git clone https://github.com/KarmenLoop/koder-shared-memory.git
cd koder-shared-memory
python3 scripts/check_repository.py
python3 scripts/package_skill.py
```

用当前 Koder 版本的技能或资源导入器导入 `dist/koder-shared-memory.skill.zip`。直接加载目录的宿主可用 `skills/koder-shared-memory/`。打包不安装依赖、不连接模型、个人资料或消息账号。

在需要关联的各入口启用；仅项目或仅对话设置会限制可用范围。完整步骤见[中文教程](docs/tutorial.zh-CN.md)。

### 第一次交接

确认宿主能解析可信空间、读写持久记忆并报告**实际**同步状态，再用其支持的登录流程关联账号和设备。保存一个小测试决定，在私聊取回，再由关联群组另一位成员检索；分别核对来源、可见范围与原对话回复位置。

身份、存储、渠道或同步尚未接通时，不应把「技能导入成功」称为跨工具/跨设备可用。

### 分享哪些内容

| 可纳入空间 | 保持在空间之外 |
| --- | --- |
| 相关对话、明确偏好、决定和任务进度 | 密码、API 密钥、令牌和会话秘密 |
| 已验证工具结果、失败、取消、产物引用与版本 | 活跃审批票据、设备权限、自动重放执行队列 |
| 可用的来源、作者、渠道、设备和任务引用 | 隐藏推理、无关账号和未关联空间内容 |

共享记忆不自动传文件。特别留意群组可见性：本策略允许关联群成员使用关联私聊记忆。

---

## 状态与文档

本包包含英文技能、宿主要求、记忆契约、验收场景、贡献说明和本地打包工具。结构、链接和归档检查不证明真实消息平台或第二台实体设备同步成功。

| 文档 | 用途 |
| --- | --- |
| [中文教程](docs/tutorial.zh-CN.md) · [English](docs/tutorial.en.md) | 导入、第一次交接、排查、升级、卸载 |
| [开始使用](docs/getting-started.md) · [宿主接入](docs/integration.md) | 英文细则 |
| [记忆模型](docs/memory-model.md) · [验收](docs/validation.md) · [FAQ](docs/faq.md) | 契约与边界 |
| [变更](CHANGELOG.md) · [发布](RELEASE.md) | 版本 |

中文入门、交接与限制以本页和中文教程为准；技术契约正文目前以英文文档为准。

---

## 常见问题

### 导入技能会登录我的聊天账号吗？

不会。连接器、登录与验证绑定由宿主提供。

### 是否包含云端记忆服务？

不包含。跨设备同步需要宿主侧可用的同步服务。

### 关联群里的人都能看到私聊记忆吗？

对该关联空间中的**关联私聊记忆**可以——关联前必须披露。无关空间仍分开。

### 共享记忆等于把电脑控制权给群吗？

不等于。记忆可见性与执行权分开。

### 软可发现性

与仓库实质相符的检索表述：**智能体共享记忆技能**、**飞书企业微信微信跨渠道上下文**、**关联群私聊记忆策略**、**可移植 SKILL.md 记忆契约**、**不静默重放命令的宿主接入**。避免堆砌关键词。

---

## 贡献、许可与联系

贡献见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)；求助见 [SUPPORT.md](SUPPORT.md)；安全见 [SECURITY.md](SECURITY.md)。不要上传私聊、凭据或客户资料。

采用 [Apache License 2.0](LICENSE)，按条款可使用、修改与分发（含商业用途）；保留声明并标出修改。许可只覆盖本仓库文件，不覆盖 Koder 运行时、第三方连接器或模型服务。保留 [NOTICE](NOTICE)。

[GitHub Issues](https://github.com/KarmenLoop/koder-shared-memory/issues) · Star 自愿。
