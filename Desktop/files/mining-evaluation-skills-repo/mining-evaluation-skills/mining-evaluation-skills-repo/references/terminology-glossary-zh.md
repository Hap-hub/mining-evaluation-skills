# 中英矿业术语对照表 / Chinese-English Mining Terminology Glossary

General-purpose translation of mining terms often produces phrasing that "sounds right but is subtly wrong" — several terms get merged or swapped in ways that change technical/legal meaning. This file exists to prevent that. When responding in Chinese on topics covered here, use the terms below rather than a literal re-translation of the English reference files.

## 品位相关术语（Grade / Cut-off terminology）— 三个最容易混用的词

这三个词在中文语境里经常被互换使用，但含义并不相同，使用时应严格区分：

- **边界品位 (boundary grade)**：用于圈定矿体范围的最低品位标准，是地质圈矿意义上的下限，不直接等同于经济意义上的可采下限。
- **截止品位 (cut-off grade)**：经济意义上"值不值得开采"的最低品位标准，随成本、金属价格、回收率变动而变化（对应 `references/resource-estimation.md` 里的 cut-off grade 公式）。这是英文语境里绝大多数场景应该对应的词。
- **最低工业品位 (minimum mining/industrial grade)**：中国矿产资源储量规范体系里的特定术语，通常指在给定技术经济条件下，可以作为工业矿床开采的最低平均品位要求，历史上带有一定的规范/审批色彩，和西方语境里纯粹由成本-价格模型推导出的 cut-off grade 并不总是同一件事。

**使用原则**：翻译或解释英文 "cut-off grade" 时，默认对应"截止品位"，不要用"边界品位"或"最低工业品位"替代，除非用户明确在讨论中国矿产资源规范体系下的具体审批语境。

## 资源量 vs. 储量（Resource vs. Reserve）

这是法律意义上有实质差别的一对术语，不是同义词：

- **矿产资源量 (Mineral Resource)**：基于地质证据，认为有合理经济开采前景的矿产富集体，尚未扣除采矿/选冶/经济/市场/法律/环境/社会/政府等"修正因素 (modifying factors)"。
- **矿产储量 (Mineral Reserve)**：在矿产资源量的基础上，应用修正因素后，认定为经济可采的部分。只有 Measured / Indicated（探明/控制）级别的资源量才能转化为储量；**推断资源量 (Inferred Resource) 不能直接转化为储量**。

在中文输出中，遇到英文原文使用 "Resource" 或 "Reserve" 时，应准确对应"资源量"或"储量"，不要因为语感顺口而混用；这个区分直接影响披露是否合规（见 `references/reporting-standards.md`）。

## 资源量分类（CRIRSCO confidence categories）— 标准中文表述

- **Measured Resource → 探明资源量**（有时也译"测定资源量"，"探明"是行业更通行的表述）
- **Indicated Resource → 控制资源量**
- **Inferred Resource → 推断资源量**
- **Proved Reserve → 探明储量**
- **Probable Reserve → 概略储量** / 也常见"可信储量"，两种译法在业内并存，行文时选定一种并保持全文一致，避免一稿多译。

## 可行性研究阶段（PEA / PFS / FS）

- **PEA (Preliminary Economic Assessment) → 概略经济评价 / 预可行性前评价**——注意不要和 PFS 混淆，中文里"预可行性"一词有时被误用来指代 PEA，实际上"预可行性研究"对应的是 PFS。
- **PFS (Pre-Feasibility Study) → 预可行性研究**
- **FS (Feasibility Study) → 可行性研究**

**易错点**：中文"预可行性"四个字，字面上很容易被套用到 PEA 身上（因为 PEA 也在 FS"之前"），但行业标准对应关系是 PEA≠预可行性研究，PFS=预可行性研究。翻译或解释时务必按上面三行的对应关系走，不要按字面直觉推断。

## 品位-吨位曲线与敏感性分析

- **品位-吨位曲线 (grade-tonnage curve)**：不要简化为"品位曲线"或"吨位曲线"，两个维度都要保留在术语里，因为这条曲线的核心信息就是两者的反比关系（见 `references/resource-estimation.md`）。
- **敏感性分析 (sensitivity analysis)**：在矿业经济评价语境下，通常特指对 NPV/IRR 等指标相对于价格、成本、汇率等变量的敏感度分析，翻译时不要泛化为一般意义上的"风险分析"（那是 risk assessment，见 `references/risk-assessment.md`），二者在这个领域里指代不同的分析类型。

## 使用建议

如果用户在对话中使用了上述容易混淆的中文术语（例如把"截止品位"说成"边界品位"），礼貌地在回复中使用正确术语并简单说明区别，而不是原样沿用用户的措辞——这是这份 skill 存在的意义之一：把术语用对，而不是迎合可能不准确的表述。
