# DeepSeek Flash / Opus / Human Metric 报告

生成时间：2026-05-21

## 文件和 full review 路径

### DeepSeek flash

- score 文件：`/home/wg25r/split_review/results/sweep_v1_905prompts/scores.csv`
- full review 目录：`/home/wg25r/split_review/results/sweep_v1_905prompts/reviews/`
- 单篇 full review 路径模板：`/home/wg25r/split_review/results/sweep_v1_905prompts/reviews/{paper_id}.md`
- log：`/home/wg25r/split_review/results/sweep_v1_905prompts/merge.log`
- 结果规模：392 行 score，391 个 unique paper；`ZNAY3ivd62` 在 score 表里重复一次。

### Opus

- score 文件：`/home/wg25r/split_review/results/2026_opus.csv`
- full review 目录：`/home/wg25r/split_review/results/2026_opus/`
- 单篇 full review 路径模板：`/home/wg25r/split_review/results/2026_opus/{paper_id}.md`
- 结果规模：251 个 paper。

### Human

- ratings 文件：`/home/wg25r/review_agent/iclr2026_new/ratings.csv`
- full human review 目录：`/home/wg25r/review_agent/iclr2026_new/human_reviews/`
- 单篇 human review 路径模板：`/home/wg25r/review_agent/iclr2026_new/human_reviews/{paper_id}.md`
- paper 文本目录：`/home/wg25r/review_agent/iclr2026_new/papers/`
- 单篇 paper 文本路径模板：`/home/wg25r/review_agent/iclr2026_new/papers/{paper_id}.txt`

## 全量集合 metric

注意：DeepSeek flash 和 Opus 的全量集合不是同一个集合。DeepSeek flash 是 392 行 score，Opus 是 251 个 paper，所以全量数字只能看各自 run 的表现，不能当作严格 A/B。

| 系统 | Papers | Spearman raw | Spearman rounded | Pearson raw | MAE raw | Bias pred-gt | Decision acc | AUROC | AUPRC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DeepSeek flash | 392 | 0.6242 | 0.5593 | 0.6563 | 1.5791 | +1.2692 | 66.8% | 0.7901 | 0.7056 |
| Opus | 251 | 0.6707 | 0.6670 | 0.6560 | 1.1913 | +0.4658 | 75.3% | 0.8348 | 0.7674 |

## Human baseline

Human baseline 是在对应模型集合上重新计算的，所以 DeepSeek flash 集合和 Opus 集合的 human 数字略有不同。

### 在 DeepSeek flash 的 392 行集合上

| Human baseline | Spearman | Pearson | MAE |
|---|---:|---:|---:|
| panel-to-reviewer | 0.5751 | 0.6179 | 1.4851 |
| reviewer-to-reviewer | 0.4771 | 0.4988 | 1.6906 |
| subgroup-to-subgroup | 0.6064 | 0.6616 | 1.2491 |

### 在 Opus 的 251 篇集合上

| Human baseline | Spearman | Pearson | MAE |
|---|---:|---:|---:|
| panel-to-reviewer | 0.5906 | 0.6218 | 1.5285 |
| reviewer-to-reviewer | 0.4893 | 0.5059 | 1.7228 |
| subgroup-to-subgroup | 0.6284 | 0.6707 | 1.2733 |

## Opus 和 DeepSeek flash 重叠集合

严格比较应该看重叠 paper。当前已有重叠导出：

- Opus overlap：`/home/wg25r/split_review/results/overlap_905prompts_vs_opus/opus_overlap.csv`
- DeepSeek flash overlap：`/home/wg25r/split_review/results/overlap_905prompts_vs_opus/deepseek_905_overlap.csv`
- 重叠规模：249 篇。

| 系统 | Spearman | Pearson | MAE | Bias pred-gt | AUROC | Decision acc |
|---|---:|---:|---:|---:|---:|---:|
| Opus | 0.6738 | 0.6568 | 1.1941 | +0.4643 | 0.8380 | 75.5% |
| DeepSeek flash | 0.6373 | 0.6588 | 1.5867 | +1.2477 | 0.8140 | 68.7% |

## 读法

DeepSeek flash 的相关性不差：全量集合 Spearman raw 是 0.6242，高于同集合的 panel-to-reviewer human baseline 0.5751，也略高于 subgroup-to-subgroup baseline 0.6064。但是它的高分 bias 很明显，pred-gt 平均偏高 +1.2692，MAE 也高到 1.5791。

Opus 的核心优势不是 Pearson，而是排序、校准和决策更稳。在全量集合上 Opus Spearman raw 是 0.6707，MAE 是 1.1913，bias 只有 +0.4658，decision accuracy 是 75.3%。在 249 篇重叠集合上，Opus 也比 DeepSeek flash 有更高 Spearman、更低 MAE、更低 bias、更高 AUROC 和更高 decision accuracy。

所以目前判断是：DeepSeek flash 有一定 ranking 能力，问题主要不是完全不会评，而是分数尺度和接受倾向偏高；这个 bias 可以后处理校准，但 review 内容质量和最终 decision 仍然需要结合 full review 文件逐篇看。

## Paired bootstrap 显著性

在 Opus 和 DeepSeek flash 的 249 篇重叠集合上，按 paper 成对 bootstrap 20,000 次，比较 Opus - DeepSeek 的差值：

| 指标 | 差值 | 95% CI | 结论 |
|---|---:|---:|---|
| Spearman | +0.0365 | [-0.0372, +0.1108] | 不显著 |
| Pearson | -0.0019 | [-0.1025, +0.0924] | 不显著 |
| AUROC | +0.0239 | [-0.0272, +0.0749] | 不显著 |
| Decision acc | +0.0683 | [-0.0080, +0.1446] | 边缘趋势 |
| MAE | -0.3927 | [-0.5066, -0.2730] | Opus 显著更好 |
| absolute bias | -0.7833 | [-0.9048, -0.6711] | Opus 显著更好 |

因此，Opus 的 raw 优势主要显著体现在 calibration / MAE / bias。Spearman 和 AUROC 虽然更高，但这个 overlap 样本下不能说显著。

## 线性校准后的 MAE

在同一 249 篇 overlap 上做线性回归校准 `pred_score -> gt_avg_score`：

| 系统 | raw MAE | in-sample calibrated MAE | leave-one-out calibrated MAE |
|---|---:|---:|---:|
| Opus | 1.1941 | 1.1101 | 1.1211 |
| DeepSeek flash | 1.5867 | 1.1614 | 1.1703 |

校准公式：

- Opus: `calibrated = 0.9851 * pred_score - 0.3931`
- DeepSeek flash: `calibrated = 1.2388 * pred_score - 2.5775`

校准后，DeepSeek flash 的 MAE 从 1.5867 降到 1.1703，和 Opus 的 1.1211 很接近。说明 DeepSeek flash 的主要 raw 问题是高分 bias / scale，而不是完全没有 ranking signal。

## Human one-vs-rest 对比

在同一 249 篇 overlap 上，human one-vs-rest baseline：

| Human baseline | Spearman | Pearson | MAE |
|---|---:|---:|---:|
| one-vs-rest | 0.5955 | 0.6251 | 1.5258 |

paired bootstrap vs human one-vs-rest：

| 系统 | 指标 | model-human diff | 95% CI | 结论 |
|---|---|---:|---:|---|
| Opus | Spearman | +0.0783 | [+0.0018, +0.1584] | 勉强显著更高 |
| DeepSeek flash | Spearman | +0.0418 | [-0.0381, +0.1254] | 不显著 |
| Opus | raw MAE | -0.3317 | [-0.4880, -0.1733] | 显著更好 |
| DeepSeek flash | raw MAE | +0.0609 | [-0.1191, +0.2442] | 不显著 |
| Opus | LOO calibrated MAE | -0.4047 | [-0.5579, -0.2489] | 显著更好 |
| DeepSeek flash | LOO calibrated MAE | -0.3555 | [-0.5073, -0.2000] | 显著更好 |

最终读法：Opus 和 DeepSeek flash 的 ranking 都在 human one-vs-rest 附近或更高；只有 Opus 的 Spearman 勉强显著高于 human。线性校准后，两者 MAE 都显著好于 human one-vs-rest。
