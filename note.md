# 这次 DeepSeek / Opus prompt 对比的教训

## 先确认 prompt 版本，不要凭印象判断

一开始我们以为 Opus 跑出来的 prompt 和当前 `prompts/` 差不多，但检查 `905381a` 后发现不是这样：

- `merger.md` 和 `neutral_reviewer.md` 基本一致。
- `cal_with.md` 不一样：`905381a` 是多轮 bracketing / narrowing calibration，当前版本是更单次、直接的 calibration。
- `harsh_critic.md` 不一样：`905381a` 更强调按 paper 自身类别判断、软性 lens、完整分数范围；当前版本更像结构化 checklist。

教训：如果要解释模型结果差异，第一步应该 checkout / diff 实际 prompt，而不是先假设“prompt 一样”。

## 比较指标必须对齐共同样本

三个结果集样本数不同：

- 旧 prompt DeepSeek `results/sweep_v1/scores.csv`: 99 篇。
- 905381a prompt DeepSeek `results/sweep_v1_905prompts/scores.csv`: 97 篇。
- Opus `results/2026_opus.csv`: 251 篇。

直接比较全量 Spearman 可以看趋势，但严谨结论要看共同 paper 子集。三者共同 97 篇上：

| 结果集 | Spearman |
|---|---:|
| 旧 prompt DeepSeek | 0.5480 |
| 905381a prompt DeepSeek | 0.6779 |
| Opus | 0.6814 |

教训：共同样本上的 Spearman 才能说明 prompt 改动本身的影响。905381a prompt 基本把 DeepSeek 的排序能力拉到了 Opus 水平。

## 高相关和高分 bias 是两件事

905381a prompt 的 DeepSeek 有明显高分 bias：

- mean pred 明显高于 mean gt。
- low-score bin 的 MAE 很大。
- 很多弱 paper 仍然被打到 5 到 6 分附近。

但它的 Spearman 很高，说明排序能力已经明显改善。这个区别很重要：

- Spearman 高：review / ranking signal 有用。
- 分数偏高：可以后处理校准，比如线性校准、isotonic calibration、按 bin 校准或 threshold 调整。

教训：不要因为分数 bias 就否定 prompt。先看 ranking signal 是否足够强；如果 corr 高，bias 可以作为后处理问题处理。

## 只看分数不够，review 内容也要看

review 内容显示旧 prompt DeepSeek 和 905381a prompt DeepSeek 的差异不只是分数：

- 旧 prompt 更容易把弱 paper 说成“有一些问题但整体可接受”。
- 905381a prompt 更常做 anchor comparison 和分数区间 narrowing，因此排序更稳定。
- 但 DeepSeek 仍会在部分样本上过度相信 paper 的正面贡献，尤其是低分 paper，会把 structural flaw 降级成 fixable issue。

典型例子：

- `KAZpuq2W4Y`: Opus 给 4.0 reject；905381a DeepSeek 仍给 5.5 accept，说明它没有像 Opus 那样把关键技术/证据问题压到 reject 区间。
- `BDNctVKwuD`: 旧 prompt 6.5，905381a 降到 5.5，但 Opus 是 4.5。方向对了，但低分压不够。
- `lbLAgGF8OO`: 旧 prompt 4.0，905381a 5.5，Opus 6.5。905381a 更接近 Opus，因为它把 parser artifact 和真实 paper flaw 分开了。
- `Iq1fNZus2W`: 905381a DeepSeek 给 6.0 accept，但 Opus 给 4.0 reject。这说明 prompt 改好后仍有模型能力/判断差异，不是所有问题都能靠 prompt 解决。

教训：分数指标告诉我们整体趋势，review 内容告诉我们错在哪里。两者要一起看。

## 这次最有用的实验结论

905381a prompt 对 DeepSeek 是有效的：

- 旧 prompt DeepSeek 在共同 97 篇上 Spearman 只有 0.5480。
- 905381a prompt DeepSeek 到 0.6779。
- Opus 同样 97 篇是 0.6814。

因此当前优先级应该是：

1. 保留 905381a prompt 方向，因为它显著提高 rank correlation。
2. 不急着为了 bias 大改 prompt；高分 bias 可以单独校准。
3. 后续 prompt 修改如果要做，应该非常小心，只针对低分区 anchor / fatal flaw 压分，不要破坏已经变好的 Spearman。

## 操作上的教训

- 不要创建“DeepSeek 专用 prompt”并在 prompt 正文里写模型名；这会混入不必要变量。
- 改 prompt 前先备份当前 `prompts/`。
- 跑新实验时输出到新目录，不覆盖旧结果。
- 有缺失样本时不要 silently fallback，也不要把失败样本补成空结果。
- 分析时明确区分：
  - prompt 差异
  - model 能力差异
  - score calibration/bias
  - parser artifact
  - benchmark sample mismatch

## Opus / DeepSeek / Human 的最终比较

后续把 DeepSeek flash 和 Opus 对齐到 249 篇 overlap 后，结论变得更清楚：

| 系统 | Spearman | Pearson | raw MAE | Bias | AUROC | Decision acc |
|---|---:|---:|---:|---:|---:|---:|
| Opus | 0.6738 | 0.6568 | 1.1941 | +0.4643 | 0.8380 | 75.5% |
| DeepSeek flash | 0.6373 | 0.6588 | 1.5867 | +1.2477 | 0.8140 | 68.7% |

paired bootstrap 显示：

- Spearman 差值 Opus - DeepSeek 是 +0.0365，95% CI [-0.0372, +0.1108]，不显著。
- AUROC 差值 +0.0239，95% CI [-0.0272, +0.0749]，不显著。
- Decision accuracy 差值 +0.0683，95% CI [-0.0080, +0.1446]，双侧不显著但有趋势。
- MAE 差值 -0.3927，95% CI [-0.5066, -0.2730]，显著，Opus 更好。
- absolute bias 差值 -0.7833，95% CI [-0.9048, -0.6711]，显著，Opus 更好。

也就是说，Opus raw 结果显著更稳，主要体现在 calibration / bias / MAE；ranking 上 Opus 更高，但这个 overlap 样本下不能说显著。

## 线性校准后的结论

在同一 249 篇 overlap 上做 `pred_score -> gt_avg_score` 的线性校准：

| 系统 | raw MAE | in-sample calibrated MAE | leave-one-out calibrated MAE |
|---|---:|---:|---:|
| Opus | 1.1941 | 1.1101 | 1.1211 |
| DeepSeek flash | 1.5867 | 1.1614 | 1.1703 |

校准公式：

- Opus: `calibrated = 0.9851 * pred_score - 0.3931`
- DeepSeek flash: `calibrated = 1.2388 * pred_score - 2.5775`

校准后 DeepSeek 的 MAE 大幅接近 Opus，LOO calibrated MAE 只差约 0.0492。这说明 DeepSeek 的主要 raw 缺陷是高分 bias / scale，不是完全没有排序信号。

## 相比 human one-vs-rest

在同一 249 篇 overlap 上，human one-vs-rest baseline 是：

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

最终判断：

- Opus 和 DeepSeek flash 的 ranking 都接近或略高于 human one-vs-rest；只有 Opus 的 Spearman 在 bootstrap 下勉强显著高于 human。
- 线性校准后，两者 MAE 都显著好于 human one-vs-rest。
- Opus 仍然是更好的 raw evaluator，因为它不需要强校准就有低 MAE / 低 bias。
- DeepSeek flash 更像是有可用 ranking signal 但分数尺度偏高的 evaluator；如果下游只关心 calibrated score，差距会明显缩小。
