# Mining-Evaluation-Skills 安装与使用指南

> 一个面向矿业专业人士的 AI Skill，覆盖资源量估算、品位-吨位分析、经济可行性（PEA/PFS/FS）、
> 风险评估，以及 NI 43-101 / JORC / CRIRSCO 等国际标准的合规报告生成。
>
> **仓库地址：** https://github.com/Hap-hub/mining-evaluation-skills
>
> ## 📬 Contact Me

- WeChat: **happyhey**
- Email: cnheyong@email.com
- Linkedin: https://www.linkedin.com/in/heyonghy
- GitHub: https://github.com/hap-hub

---

## 目录

- [这是什么](#这是什么)
- [Skill 结构](#skill-结构)
- [快速获取](#快速获取)
- [一、在 Codex 中安装](#一在-codex-中安装)
- [二、在 Claude 中安装](#二在-claude-中安装)
  - [方式 A：Claude.ai 网页版](#方式-aclaudeai-网页版)
  - [方式 B：Claude Code（CLI）](#方式-bclaude-codecli)
- [三、在 Obsidian Claudian 中安装](#三在-obsidian-claudian-中安装)
- [四、国产大模型配置方法](#四国产大模型配置方法)
- [使用示例](#使用示例)
- [常见问题](#常见问题)

---

## 这是什么

`mining-evaluation-skills` 是一个符合 [Agent Skills 开放标准](https://github.com/Hap-hub/mining-evaluation-skills) 的技能包，核心是一份 `SKILL.md` 说明书，外加参考知识库、计算脚本和报告模板。任何支持该标准的 AI 平台（Claude、Codex、Obsidian Claudian 等）都能加载它。

加载后，当你提出矿业评估相关问题时，AI 会**自动触发**该 Skill，无需手动调用。它能做：

- 项目合规性检查（QA/QC、资源量分类比例、缺项识别）
- 品位-吨位曲线 / 边界品位（cut-off grade）敏感性分析
- NPV / IRR / 回收期财务测算
- 按国际标准（NI 43-101 / JORC / CRIRSCO / CBRR / GKZ / SAMREC）生成技术报告 + 投资人摘要（Markdown / Word）
- 覆盖 13 种金属专项知识（铜/金/镍/锂/钴/铅锌/铌钽/稀土/钼/钨/白钨/锆/钛）
- 中英文智能切换（中文矿业术语已重修，减少误用）

---

## Skill 结构

```
mining-evaluation-skills/
├── SKILL.md                        # 技能说明书（含 YAML frontmatter：name / description）
├── README.md
├── CHANGELOG.md
├── references/                     # 知识库：AI 触发时查阅
│   ├── resource-estimation.md
│   ├── economic-feasibility.md
│   ├── risk-assessment.md
│   ├── reporting-standards.md
│   ├── esg-sustainability.md
│   ├── terminology-glossary-zh.md  # 中文矿业术语表（已重修易混术语）
│   └── metals/                     # 13 种金属专项资料
│                                   #   铜/金/镍/锂/钴/铅锌/铌钽/稀土
│                                   #   + 新增：钼/钨/白钨/锆/钛
├── scripts/                        # 仅在提供真实数据时运行（Python 标准库）
│   ├── grade_tonnage_calculator.py
│   ├── financial_model.py
│   └── resource_classification_checklist.py
└── assets/templates/               # 报告骨架模板
    ├── resource_estimation_report.md
    ├── pea_pfs_fs_summary.md
    └── risk_assessment_matrix.md
```

> `SKILL.md` 的 frontmatter 中 `name: mining-evaluation-skills`，这是各平台识别技能的唯一标识。

---

## 快速获取

三个平台都需要先把仓库拉到本地。任选一种：

```bash
# 方式 1：git clone（推荐，便于更新）
git clone https://github.com/Hap-hub/mining-evaluation-skills.git

# 方式 2：下载 zip 后解压
#   打开 https://github.com/Hap-hub/mining-evaluation-skills
#   Code → Download ZIP → 解压
```

仓库里还提供了一个打包好的 `mining-evaluation-skills.skill` 文件，供 Claude.ai 网页版直接上传使用（见下文）。

---

## 一、在 Codex 中安装

Codex CLI 支持开放的 `SKILL.md` 标准，会自动发现 skills 目录中的技能。

1. 在你的项目根目录创建 skills 目录，并把整个技能文件夹放进去：

   ```bash
   mkdir -p .agents/skills
   git clone https://github.com/Hap-hub/mining-evaluation-skills.git \
     .agents/skills/mining-evaluation-skills
   ```

   > 说明：不同版本的 Codex 约定目录可能是 `.agents/skills/`。若你的 Codex 使用其他约定（如 `~/.codex/skills/`），把 `mining-evaluation-skills` 整个文件夹放到对应目录即可——关键是保证 `SKILL.md` 位于该文件夹根部。

2. 确认目录结构正确：

   ```
   .agents/skills/mining-evaluation-skills/SKILL.md   ← 必须存在
   ```

3. 重启 Codex 会话。之后直接提问矿业评估问题，Codex 会自动加载该 Skill。

---

## 二、在 Claude 中安装

### 方式 A：Claude.ai 网页版

最简单，无需命令行。

1. 打开 **Settings → Capabilities**，确保 **Code execution（代码执行）** 已开启（脚本计算依赖它）。
2. 进入 **Settings → Capabilities → Skills**（或 Customize → Skills）。
3. 点击 **Upload skill / +**，上传仓库里的 `mining-evaluation-skills.skill` 文件。
4. 在列表中**勾选启用**该 Skill。
5. 之后在对话中提出矿业问题，Claude 会自动触发它（无需手动 @）。

### 方式 B：Claude Code（CLI）

适合团队共用、可版本化管理。

1. 在项目根目录放置技能：

   ```bash
   mkdir -p .claude/skills
   git clone https://github.com/Hap-hub/mining-evaluation-skills.git \
     .claude/skills/mining-evaluation-skills
   ```

   > 如需**全局**对所有项目生效，改放到用户级目录：`~/.claude/skills/mining-evaluation-skills`

2. 确认 `.claude/skills/mining-evaluation-skills/SKILL.md` 存在。
3. 重启 Claude Code 会话，Skill 会被自动发现。用 `/` 或直接提问即可触发。

---

## 三、在 Obsidian Claudian 中安装

Claudian 基于 Claude Code 运行在你的 Obsidian 仓库（vault）内，因此复用 Claude Code 的技能发现机制：技能放在 **vault 根目录下的 `.claude/skills/`** 中。

1. 在 Obsidian 仓库根目录打开终端（vault 根即 `.obsidian`、`.claude` 所在目录），执行：

   ```bash
   mkdir -p .claude/skills
   git clone https://github.com/Hap-hub/mining-evaluation-skills.git \
     .claude/skills/mining-evaluation-skills
   ```

   最终结构应为：

   ```
   <你的 vault>/
   ├── .obsidian/
   └── .claude/
       └── skills/
           └── mining-evaluation-skills/
               └── SKILL.md          ← 必须存在
   ```

2. 在 Claudian 对话框中**重新开启一个会话**（或重载插件），让它重新扫描技能目录。
3. 验证：在 Claudian 里问一句「有一个铜矿项目 Inferred 占 40%，能上 PFS 吗？」，若回复引用了 NI 43-101 / JORC 规则，说明已成功加载。

> 提示：
> - `.claude/skills/` 中的技能不会污染你的笔记，Obsidian 默认隐藏点号开头的目录。
> - 若脚本类计算（品位-吨位 / NPV）不生效，确认运行 Claudian 的环境中已安装 Python 3（脚本仅用标准库，无需额外依赖）。

---

## 四、国产大模型配置方法

如果你希望在国内网络环境或国产模型服务上使用本 Skill，推荐采用 **OpenClaw + OpenAI Compatible API** 的路径：OpenClaw 作为模型无关的宿主，底层模型配置为 DeepSeek 或 Z.ai（GLM）。Skill 仍按上文方式放在 `.claude/skills/mining-evaluation-skills/` 中，模型只负责执行和生成。

### 方式 A：OpenClaw + DeepSeek

1. 在 DeepSeek 控制台创建 API Key。
2. 在 OpenClaw 的模型设置中新增或选择 **OpenAI Compatible** 类型。
3. 填入以下配置：

   ```text
   Provider / Type: OpenAI Compatible
   Base URL: https://api.deepseek.com
   API Key: 你的 DeepSeek API Key
   Model: deepseek-chat（或你在 DeepSeek 控制台已启用的模型）
   ```

4. 保存后重新开启 OpenClaw 会话，并用一个矿业评估问题测试 Skill 是否自动触发。

### 方式 B：OpenClaw + Z.ai（GLM）

1. 在 Z.ai 控制台创建 API Key，并确认你使用的是普通 API 还是 GLM Coding Plan。
2. 在 OpenClaw 的模型设置中新增或选择 **OpenAI Compatible** 类型。
3. 按你的账户类型填入端点：

   ```text
   Provider / Type: OpenAI Compatible
   Base URL: https://api.z.ai/api/paas/v4/              # 普通 API
   Base URL: https://api.z.ai/api/coding/paas/v4        # GLM Coding Plan
   API Key: 你的 Z.ai API Key
   Model: 你的 GLM 模型代码，例如 glm-4.5 或 glm-5.2
   ```

4. 如果 OpenClaw 提供上下文窗口设置，按所选 GLM 模型的官方说明填写；如果出现 401 / 403，优先检查 API Key 类型、订阅计划和 Base URL 是否匹配。

> 提示：国产模型配置只改变底层推理模型，不改变 Skill 的安装位置。若 Skill 未触发，先检查 `.claude/skills/mining-evaluation-skills/SKILL.md` 是否存在，再重启 OpenClaw / Claudian 会话。

---

## 使用示例

安装完成后，无需手动调用，直接自然语言提问：

**合规检查**

> 有一个铜矿项目，资源量 2300 万吨，平均品位 0.65% Cu，完成 27 个钻孔，
> QA/QC 通过率 95%，品位分布 60% Indicated / 40% Inferred。
> 请评估现在有什么风险，报告框架怎么搭。

**数据计算**（上传一张钻孔 CSV 表）

> 用这份锂矿数据做品位-吨位分析，边界品位从 0.3% 到 1.8% Li₂O，帮我找最经济的开采边界。

**报告生成**

> 用 NI 43-101 标准，帮我生成一份镍矿资源评估章节，输出 Word。

---

## 常见问题

**Q：三个平台的目录约定为什么不同？**
A：技能标准本身只要求「一个含 `SKILL.md` 的文件夹」。不同宿主约定的扫描路径不同——Codex 常用 `.agents/skills/`，Claude Code / Claudian 用 `.claude/skills/`，Claude.ai 网页版则直接上传 `.skill` 打包文件。放对位置、保证 `SKILL.md` 在文件夹根部即可。

**Q：装好了但没触发？**
A：① 确认 `SKILL.md` 路径正确；② 重启会话让宿主重新扫描；③ 提问尽量包含矿业关键词（品位、吨位、NI 43-101、PEA/PFS/FS、资源量分类等）。

**Q：脚本报错？**
A：脚本仅在你提供真实数据（如 Excel/CSV）时运行，且需要干净的表格格式。请确认运行环境有 Python 3，并检查数据列名与格式。

**Q：老用户如何升级到新版本（新增金属 / 标准）？**
A：
- **Claude Code / Codex / Claudian（CLI）**：进入技能目录 `git pull` 覆盖，重启会话自动发现新版本：
  ```bash
  cd .claude/skills/mining-evaluation-skills   # 或对应平台路径（Codex 为 .agents/skills/…）
  git pull
  ```
- **Claude.ai 网页版**：进 Settings → Customize → Skills，**先删掉旧的** `mining-evaluation-skills`，再上传新版 `.skill` 文件并重新勾选启用。

**Q：跨国标准 / 苏系储量分类（GKZ）能直接照搬吗？**
A：不能盲信。GKZ 的 A/B/C1/C2 与西方 Measured/Indicated/Inferred **并非一一对应**（例如 C2 该对 Inferred 还是更低，业内仍有争议）。Skill 给的是**起点而非结论**，跨标准披露务必让当地 QP / 有资质人员复核。

**Q：新增金属的计价系数、回收率能当精确数字用吗？**
A：不能。文档中金属的计价系数、回收率均为**定性范围与常见口径**，具体项目须以实际选冶试验和购销合同为准。

---

## 免责声明

本 Skill 用于**辅助**矿业评估，不能替代人工判断。最终的经济可行性结论仍须由合格人士（QP）或投资委员会签署。所有生成报告均附带免责声明。跨标准披露、金属计价与回收率参数均需人工复核。

**仓库：** https://github.com/Hap-hub/mining-evaluation-skills · 欢迎提 Issue / Fork / Star ⭐

