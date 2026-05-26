Now I have all the information needed. Let me compile the final consolidated review.

## Calibration Report

**All anchors retrieved:**

| Path | Avg Score | Round/Bucket | Comparison |
|------|-----------|--------------|-----------|
| `OdoS6cH8MP` | 2.00 | r1-topic-low | Data valuation paper; much weaker, unclear contribution |
| `z3DMFpaP6m` | 3.00 | r1-topic-low | Entropy metric paper; abstract/weak experiments vs. HES paper's concrete results |
| `EOPLy80bBm` | 3.00 | r1-topic-low | Data pruning survey with theoretical errors; HES paper is stronger |
| `t15cWqydys` | 3.00 | r1-topic-low | Decoding-free selection paper; less relevant, lower quality |
| `diKRhKs5yl` | 5.25 | r1-topic-mid | FEEDER — demo pre-selection; comparable scope, computational concerns, Reject |
| `Fty0wTcemV` | 6.00 | r1-topic-mid, r2 | DELIFT — data-efficient FT across 3 stages; comparable, Accepted |
| `I5p1Gm8GFS` | 5.75 | r1-topic-mid, r2 | 3DS — data selection for medical domain; weaker domain scope, Reject |
| `UoWslU6hsX` | 4.33 | r1-topic-mid | LLM success prediction; less relevant, smaller contribution |
| `SpTzsQjgxF` | 5.75 | r2 | Rule-based data selection; similar missing-baselines issue, Reject |
| `qUJsX3XMBH` | 4.40 | r2 | "Random selection is all you need"; found most methods ≈ random, Reject |
| `V9oT5Jmxpu` | 6.00 | r2 | GraphFilter — quality+diversity selection; comparable, Reject |
| `f4gF6AIHRy` | 8.00 | r1-topic-high | Dimensional collapse/pre-training; much stronger paper, Accept |
| `E2RyjrBMVZ` | 4.17 | r1-weakness-variance | Quantifying variance in benchmarks; Reject, but RL-specific |
| `f37TVPH62h` | 4.33 | r1-weakness-variance | Compound returns in RL; Reject, different subfield |
| `3NnfJnbJT2` | 7.00 | r1-weakness-HES | GIO — gradient info optimization; stronger method+experiments, Accept |
| `HhfcNgQn6p` | 5.50 | r1-weakness-HES | Statistical theory of data selection; Accept, more theoretical |

**Round-1 bracket:** 4.5 – 6.0. **What low-band anchors failed at:** weak or flawed methodology, unclear contributions, insufficient experimental validation. The HES paper does **not** share those failures — its contribution is clear and its SFT experiments are strong. The weakness-anchored (variance) hits at 4.17–4.33 are RL-specific papers; the data-selection literature (DELIFT, 3DS, FEEDER) routinely reports single-seed results. After narrowing, the paper sits between DELIFT (6.00, Accept) and 3DS/FEEDER (5.25–5.75, Reject) — making a clearer contribution than the latter but sharing their missing-baselines and no-variance limitations.

---

## Summary

This paper proposes High-Entropy Sum (HES), a training-free metric that sums the entropy of the top 0.5% highest-entropy tokens in a reasoning trajectory, and uses it to select training data for SFT, RFT, and RL. The core idea is well-motivated: in long-CoT reasoning, most tokens are predictable, so global metrics like average entropy dilute the signal from critical forking points. HES focuses on those forks. The SFT results are the strongest part of the paper — training on just the top 20% of HES-ranked data matches full-dataset performance, and the top 80% consistently surpasses it. The metric transfers across model scales (0.6B → 8B) and generalizes to code and STEM domains. RFT and RL results are positive but more modest.

## Strengths

1. **Simple, well-motivated, and empirically validated metric.** HES is clearly defined and motivated by the observation that long-CoT reasoning paths have a small number of high-entropy "forking tokens" that carry most of the information. Figure 1 provides direct evidence that HES cleanly separates correct and incorrect samples (normalized means 0.29 vs. 0.68), while average entropy does not (0.52 vs. 0.53). This discriminative ability is the foundation of the paper's claims.

2. **Strong SFT results across models, datasets, and domains.** Training on the top 80% of HES-ranked data consistently outperforms the full dataset on Qwen3-8B (35.36% vs. 32.61% average) and DeepSeek-R1-Distilled-7B (32.35% vs. 30.22%). The Lowest-HES-20% ablation (14.90% vs. Random-20% at 25.89%) confirms that HES identifies genuinely harmful low-quality data. These effects are replicated on code and STEM domains, supporting generality.

3. **Computationally efficient with practical small-to-large transfer.** Using a 0.6B proxy model to score data for 8B training achieves comparable results to self-selection (32.12% vs. 31.14%) at a fraction of the inference cost. This is a practically valuable finding for large-scale data curation.

4. **RL ablation reveals a nuanced insight about negative sample diversity.** The finding that constraining negative rollouts to low-HES hurts performance (Pos-High,Neg-Low: 19.50%, Pos-Rand,Neg-Low: 19.76% vs. Full-Batch: 20.63%), while random negatives with high-HES positives works best (21.30%), is an interesting and non-obvious result with practical implications for RL training recipe design.

## Weaknesses

### Major

1. **No statistical uncertainty reported for any result.** All numbers are single-seed point estimates (pass@1 averaged over 16 samples per problem). The RL improvement (21.30 vs. 20.63, a 0.67-point gain) and many RFT margins (1–2 points) are small enough that they could fall within noise. Without confidence intervals, multiple seeds, or significance tests, the reliability of these smaller improvements cannot be assessed. This is a standard expectation in empirical ML work and is particularly important when claims of superiority hinge on narrow margins. The SFT results are large enough to be robust to this concern, but for RFT and RL the evidence would be substantially strengthened by variance estimates.

2. **Missing competitive baselines from the same line of work.** The SFT and RFT experiments compare HES against simple heuristics (length, difficulty, average entropy) and random sampling. More recent training-free selection methods — DSIR, D4, perplexity-based importance sampling (Marion et al., 2023) — are discussed in the related work but never compared against. While the paper's focus on entropy-based metrics is clear, the absence of these established data-selection baselines weakens the claim that HES is the most effective training-free metric. Adding even one such baseline would significantly strengthen the evaluation.

### Minor

1. **"Unified" framing is slightly overclaimed.** The paper presents HES as a single metric that works uniformly across SFT, RFT, and RL. However, in RL the selection strategy is asymmetric: HES is used only for positive rollouts, while negatives are selected randomly. The paper itself shows that using HES to select negatives hurts performance. This is not a fully unified approach in the sense that the same rule applies everywhere. The metric itself is unified, but the selection policy is not. The narrative should be tempered accordingly.

2. **HES-quality relationship is presented in a confusing way.** Figure 1 shows that incorrect trajectories have *higher* HES than correct ones. The paper then uses HES to select high-quality *correct* solutions, assuming higher HES among correct samples indicates higher training value. This is a coherent position (HES measures complexity, not correctness; complex correct solutions are more informative), but the paper does not explicitly articulate this reasoning. The presentation in Figure 1 (which frames HES as distinguishing "high- and low-quality samples") creates unnecessary confusion. The SFT-Lowest-HES ablation empirically supports the interpretation, but a clearer conceptual explanation would help.

3. **RFT and RL results are modest.** The RFT gains over random are consistently 1–2 points, and the RL improvement is 0.67 points over Full-Batch on a 1.5B model. These results are positive but hardly transformative, and the paper's claims sometimes overstate their significance (e.g., "significantly surpassing existing training-free selection methods" in the abstract, when the RL comparison is against random and simple heuristics).

4. **Duplicated paragraph.** The paragraph beginning "HES shows robust performance in both Per-Query and Global Pool settings" appears verbatim twice (lines 232 and 234) in the RFT results section. This is clearly a copy-paste error.

### Trivial

- The sensitivity analysis (Figures 3-4) shows that the optimal data selection ratio varies noticeably across tasks (e.g., ~0.2 for AIME 2024 vs. ~0.8 for HMMT 2025), yet the paper claims "peak performance is almost consistently achieved when using approximately 20% or 80% of the data." This generalization is rougher than the data supports.
- No "Limitations" section is present; the paper does not self-criticize or discuss failure modes.
- Forking-Only baseline in SFT (gradient masking) is orthogonal to data selection and could be moved to appendix.

## Nice-to-Haves

- **Analyze what HES actually selects qualitatively.** Showing examples of high-HES vs. low-HES correct solutions (length, diversity, reasoning steps) would help readers understand what the metric captures beyond simple proxies like length.
- **RL experiments on a larger model (7B+).** The RL results are only on 1.5B; testing at larger scale would increase confidence.
- **More principled selection ratio rule.** The optimal ratio differs across tasks; a rule based on the HES distribution (rather than a fixed percentage) could improve robustness.

## Novel Insights

None beyond the paper's own contributions. The key insight — that focusing on a small number of high-entropy tokens in long reasoning trajectories yields a better quality metric than global averages — is the paper's main contribution. The finding that negative sample diversity matters more than negative quality in RL is a secondary insight.

## Suggestions

1. Add at least 2–3 seeds with standard deviations for the main SFT, RFT, and RL comparisons. For the RL results in particular, this is essential to establish that the improvements are not noise.
2. Add at least one competitive training-free baseline (DSIR or perplexity-based selection) to the SFT and RFT comparisons to better position HES in the existing landscape.
3. Clarify the HES-quality logic explicitly: HES measures reasoning complexity/uncertainty; among correct solutions, higher complexity provides more learning signal; this is distinct from the fact that incorrect solutions also have high HES (because the model struggles).
4. Temper the "unified" language to reflect that the selection strategy is adapted per paradigm (asymmetric in RL).
5. Remove the duplicated paragraph.

## Score and Decision

<score>5.5</score>
<decision>Accept</decision>