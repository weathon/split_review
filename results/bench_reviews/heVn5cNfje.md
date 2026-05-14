Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper introduces High-Entropy Sum (HES), a training-free metric that measures reasoning-path quality by summing the entropy of only the top 0.5% highest-entropy tokens—the hypothesized "critical forking points" where the model must make non-trivial decisions. HES is used to guide data selection across three major training paradigms (SFT, RFT, and RL). The paper demonstrates that training on the top 80% of data ranked by HES (i.e., pruning the lowest 20%) consistently outperforms training on the full dataset, and that HES-based selection beats simple heuristics (length, difficulty, average entropy) across multiple domains (math, code, STEM) and model scales.

## Strengths

- **The HES metric is simple, cheap, and principled.** Computing HES requires only one forward pass of the training or a smaller proxy model, with no external reward models or human annotation. The insight that global averaging dilutes signal from critical reasoning forks is well-motivated by token-level entropy analysis (Figure 1 shows HES gives a 0.29 vs. 0.68 separation between correct/incorrect means, whereas average entropy gives 0.52 vs. 0.53).

- **Broad and consistent empirical validation.** The paper evaluates across three distinct training paradigms (SFT, RFT, RL), multiple model architectures (Qwen3-8B, DeepSeek-R1-Distilled-7B/1.5B), multiple domains (math, code, STEM), and seven challenging benchmarks. The core result—that pruning the bottom 20% by HES improves over the full dataset—holds consistently across all SFT settings (Tables 1–4), with gains of +2.75 (math), +2.13 (math, second model), +3.23 (code), and +1.06 (STEM) points. This consistency across varied settings is the paper's strongest evidence.

- **Small-to-large model transfer is convincingly demonstrated.** Using Qwen3-0.6B as a proxy to score data for training Qwen3-8B achieves 32.12% average accuracy, comparable to 31.14% from self-selection by the 8B model, while reducing inference cost by over an order of magnitude (Table 1). This is practically significant for large-scale data curation.

- **The asymmetric RL sampling strategy is a clean design.** Pairing highest-HES positive rollouts with random negatives (Pos-High, Neg-Rand) outperforms all alternatives including the full-batch baseline (21.30% vs. 20.63% average, Table 6), and the ablation showing that constraining negative diversity hurts performance (Pos-High, Neg-Low: 19.50%) provides a useful insight.

## Weaknesses

### Fatal
None.

### Major

- **Statistical significance is not established, and some effect sizes are small.** No confidence intervals, standard errors, or significance tests are reported anywhere. For benchmarks with ~30 problems (AIME24/25), a 2% difference is less than one problem out of 30, and the RL improvement (Pos-High, Neg-Rand vs. Full-Batch) is only 0.67 points (21.30% vs. 20.63%, Table 6)—an edge that could easily fall within evaluation noise. While reporting uncertainty is not yet universal practice in LLM benchmarking, the paper's central claims about HES's superiority would be substantially strengthened by confidence intervals, especially given that several key comparisons rest on narrow margins.

- **The RL results are the weakest pillar of the paper.** The 0.67-point average improvement over Full-Batch is small, and on individual benchmarks the pattern is mixed: Pos-High, Neg-Rand outperforms Full-Batch on only 5 of 8 benchmarks, and on HMMT25 it is actually worse (11.88 vs. 15.21). The paper's claim that this "significantly outperforms" the baseline is not supported without a statistical test. The 1.5B model also achieves fairly low absolute scores (e.g., AIME24 33.33%), raising the question of whether the RL setup is fully optimized, though the paper notes it matches the officially reported accuracy of DeepScaleR-1.5B-Preview.

- **HES's relationship with correctness is under-explored.** Figure 1 shows that incorrect responses have *higher* mean HES than correct ones (0.68 vs. 0.29), which the paper does not reconcile. While the method only applies HES within correct samples for SFT/RFT, and the empirical results validate that within-correct HES ranking works (Highest-HES-20% >> Lowest-HES-20%), the paper would benefit from explaining *why* a metric that seems to characterize incorrect reasoning also identifies the best correct reasoning. Some analysis of what high-HES correct vs. high-HES incorrect trajectories look like qualitatively would clarify this.

### Minor

- **The sensitivity analysis for the high-entropy token ratio is coarse.** Only four thresholds are tested (0.005, 0.05, 0.5, 1.0), and the claim that 0.005 is best is based on averaged scores without variance. Finer-grained exploration (e.g., 0.001, 0.01, 0.1) would make the robustness argument more convincing.

- **The "difficulty" baseline is implemented using a costly separate model** (Qwen2.5-Math-72B-Instruct for pass@32 scoring), which makes the comparison less clean. This doesn't weaken the paper's positive results (HES is both cheaper and better) but should be discussed as an uneven comparison that actually favors the paper's metric.

- **Preprocessing details for the 100k Open-Math-Reasoning subset are not specified**, affecting reproducibility. The sampling procedure (random? stratified?) should be stated.

- **The "Forking-Only" baseline (gradients on high-entropy tokens only) is included but not clearly motivated** relative to the data-selection framing. It achieves near-identical performance to Full-Dataset (32.51 vs. 32.61 in Table 1), which seems like a null result requiring interpretation.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment isolating whether the benefit of HES-based selection comes from removing genuinely harmful samples or from producing a more balanced difficulty distribution would strengthen the mechanistic claims.
- Combining HES with a diversity constraint in the global-pool RFT setting could recover the per-query advantage and is a natural extension.
- Qualitative examples of high-HES correct, low-HES correct, high-HES incorrect, and low-HES incorrect trajectories would help readers understand what HES captures.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The core assumption that higher HES among correct responses identifies more valuable training examples is not validated."** — This is factually incorrect. The paper's SFT experiments (Tables 1–4) directly validate this: Highest-HES-20% achieves 31.14% vs. Lowest-HES-20% at 14.90% (Table 1), a massive gap. The critic confuses the negative correlation between HES and correctness (incorrect samples have higher mean HES) with the claim about ranking within correct samples. These are different things.

2. **"The SFT result that Highest-HES-80% outperforms the full dataset is contradicted by its own tables."** — The critic claims improvements are "inconsistent in magnitude" and that random pruning might work as well. Table 1 shows Random-80% achieves 32.06% (worse than Full-Dataset at 32.61%), while Highest-HES-80% achieves 35.36% (better than Full-Dataset). The gains are consistently positive across Tables 1–4, and the random-pruning claim is directly refuted by the data.

3. **"The comparison to alternative data-selection methods is incomplete; better-performing or more principled baselines are omitted (LENS, DSIR)."** — LENS and DSIR are designed for instruction-tuning and pre-training data selection respectively, not for reasoning-path selection. The paper's baseline set (length, difficulty, entropy variants, random) covers the reasonable space. Demanding domain-mismatched baselines is scope creep.

4. **"The Forking-Only baseline ... paper does not discuss why this is relevant."** — The Forking-Only baseline is directly relevant. It is based on Wang et al. (2025), which the paper cites as inspiration, and tests whether token-level weighting (vs. data selection) is effective.

5. **Criticisms about formatting, missing appendix content, or missing references** — These are parser artifacts or knowledge gaps, not author errors.

## Novel Insights

The most interesting observation is the asymmetric importance of positive vs. negative sample selection in RL: using HES to curate positive trajectories while keeping negative diversity through random sampling outperforms all other combinations (Table 6). This suggests that not all selection decisions are symmetric—overly simplistic negative examples (Lowest-HES) harm the model's robustness because they fail to expose it to diverse failure modes. This is a non-obvious finding that extends beyond the core HES contribution and speaks to broader RL training design. The per-query vs. global-pool comparison in RFT (Table 5) is also insightful: per-query selection consistently outperforms global pooling, showing that maintaining query diversity matters even when using a strong quality metric. This tension between quality and diversity is a recurring theme in data selection, and the paper surfaces it clearly.

## Suggestions

1. **Add bootstrap confidence intervals** for the main comparisons (at least Tables 1 and 6). Even simple error bars over the 16 sampling paths per problem would significantly strengthen the claims about HES's superiority. The RL results in particular need this.

2. **Include qualitative analysis** of high-HES correct vs. low-HES correct trajectories (with token-level entropy annotations) to demonstrate what HES actually captures and to reconcile the apparent negative correlation with correctness shown in Figure 1.

3. **Strengthen the RL experiments** either by (a) running multiple random seeds to demonstrate that the 0.67-point improvement is reproducible, or (b) comparing against a stronger Full-Batch baseline that resolves the somewhat low absolute scores (e.g., AIME24 33.33%).

4. **Specify the 100k sampling procedure** for Open-Math-Reasoning and release the HES scores for the filtered datasets to aid reproducibility.

5. **Test combining HES with a diversity-aware selection strategy** in the global-pool RFT setting to see if the per-query advantage can be recovered through algorithmic means rather than engineering.

## Score and Decision

**Calibration Anchors (all from the human review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| KE43G03vI7 (entropy for efficient reasoning) | 3.50 | Weaker paper — narrower experiments, less clear contribution, on a different problem (overthinking reduction vs. data selection). Current paper is significantly stronger. |
| MDE6S92PJR (SELECT2REASON, long-CoT data selection) | 3.60 | Directly comparable task. SELECT2REASON uses a simpler heuristic (length+difficulty with LLM-as-judge); current paper introduces a more principled metric and broader evaluation. Current paper is stronger. |
| nXENWUSRMw (entropy-aware self-evolution) | 5.00 | Similar entropy theme but evaluated only on simpler benchmarks (GSM8K, SVAMP) with small models (1.8B). Current paper has harder benchmarks and broader scope. Comparable in quality. |
| SFXX5Pjl5K (EntropyLong, long-context data curation) | 5.50 | Accepted (Poster). Different task (long-context vs. reasoning), similar use of entropy for data curation. Comparable rigor and breadth. Current paper is of similar quality. |
| yKUbw7q1IA (data-efficient LLM pre-training) | 6.80 | Accepted (Poster). Much larger-scale study (22 methods, 220 pretraining runs). More thorough but addresses a different setting (pre-training vs. reasoning post-training). Current paper is narrower but well-executed. |
| VKGTGGcwl6 (LLMs lost in multi-turn conversation) | 8.00 | Accepted (Oral). Significantly stronger — large-scale evaluation, novel methodology, deep behavioral analysis. Current paper is not at this level. |

The paper under review falls below the 8.00-level work but is comparable to the 5.00–6.00 band. It has a clear, well-motivated contribution, comprehensive evaluation across three training paradigms, and consistent results. The primary weaknesses are the lack of statistical rigor (no confidence intervals), the relatively small RL improvement, and some under-explored analysis of what HES captures qualitatively. These are addressable limitations in a good paper, not fatal flaws. The paper meets the bar for a top venue.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**