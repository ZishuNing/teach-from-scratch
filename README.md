# teach-from-scratch

一个从零教到会用的 Agent Skill。像老师一样，先用具体例子讲清一件事，再顺着学习者的理解引入机制和术语；理解系统时从最小情形逐步搭起它，不从最终架构和名词清单开始。

支持中文及用户使用的其他语言，可直接对话教学，也可维护分多次学习的 HTML 课程。

## 使用方式

把本仓库中的 `teach-from-scratch/` 目录复制或链接到支持 Agent Skills 的客户端技能目录，例如 `~/.agents/skills/` 或 `~/.claude/skills/`。不要把仓库根目录当成技能目录。

在支持斜杠命令的客户端中使用：

```text
/teach-from-scratch 从零教我事件系统。我会一点 C++，先讲懂，再带我写一个最小版本。
```

支持自动匹配技能的客户端也可以直接表达学习意图，实际触发方式取决于客户端。示例：

```text
带我一步步看懂这个仓库的缓存实现，先不搭环境。
上次讲到角色掉血怎么通知血条，接着那个例子往下讲。
我还是不懂引用，换一个小例子，带我逐行看发生了什么。
```

## 教学方式

- 先接住目标和已有基础；缺少关键条件才问一两个问题，不要求先填完整配置问卷。
- 给简短路线后尽早开讲。近处细化，远处保留里程碑，允许随理解调整，不把完整课程审批当起点。
- 同一个例子串起白话、术语和机制；不固定七段格式，不为每节课制造失败或强制悬念。
- 新内容先示范，再渐进练习。卡住时换具体例子、补中间步骤，不只是把原话说得更长。练习可跳过。
- 区分已备课、已讲过和已验证；文件生成不等于用户学会，示例的预期输出不等于实际运行结果。

原有四个档位 `simplified-paper`、`full-paper`、`skeleton`、`full` 继续兼容，但不要求用户先理解英文配置。讲解深度、动手方式与节奏可以分别调整。

## 文件与续课

持续课程在用户确认的课程目录中维护 `BUILD-PLAN.md` 和 `steps/*.html`；样式、可查参考和偏好笔记按需建立。普通追问不创建一套课程文件。已有课件的路径、编号、链接和历史记录保留，不要求迁移重做。

技能本身没有外部写作技能或在线服务依赖。HTML 默认使用本地资源，简单练习使用可展开的思路与答案，不强制搭建测验系统。

核心入口是 [SKILL.md](teach-from-scratch/SKILL.md)，其余资料按需加载：

- [教学示例](teach-from-scratch/references/TEACHING-EXAMPLES.md)：自然讲法、听不懂时怎么换讲法、怎样给反馈。
- [学习方式与深度](teach-from-scratch/references/GEARS.md)：旧档位兼容和中途调整。
- [计划格式](teach-from-scratch/references/BUILD-PLAN-FORMAT.md)：路线、暂停位置与验证记录。
- [课件要求](teach-from-scratch/references/STEP-FORMAT.md)：可读性、离线使用、导航和交互。

## 维护与验证

在仓库根目录运行结构回归检查，无第三方 Python 依赖：

```sh
python -m unittest discover -s tests -v
```

[教学回归场景](tests/scenarios.md) 用于检查真实授课输出。结构测试只能发现元数据、链接和包装问题，不能证明讲解自然或学习有效；评估语气与教学行为时应按场景实际试讲，不把静态检查当作教学效果评测。

## 致谢与许可

最初的逐步教学思路受 [mattpocock/skills 的 teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) 启发；早期写作规则参考了 [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)。本技能不再要求运行时加载这些外部技能。

MIT，见 [LICENSE](LICENSE)。
