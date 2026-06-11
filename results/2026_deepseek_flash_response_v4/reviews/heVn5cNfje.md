## Summary

The paper proposes High-Entropy Sum (HES), a training-free metric for data selection in LLM reasoning training. HES sums only the entropy of the top 0.5% highest-entropy tokens per reasoning sample, focusing on critical "forking points" rather than averaging across all tokens. The metric is validated across SFT, RFT, and RL paradigms on multiple model families (Qwen3, DeepSeek-R1-Distilled) and three domains (math, code, STEM), demonstrating consistent improvements or matching of full-dataset performance with less data. The core insight—that token-level entropy aggregation should be selective rather than uniform—is well-motivated and practically impactful.

## Strengths

- **Novel and well-motivated metric.** The insight that traditional entropy-based metrics dilute signal by averaging over all tokens is empirically validated: Figure 1 shows HES separates correct from incorrect samples with a 0.39 gap in normalized means, vs. 0.01 for Avg Entropy of All Tokens and 0.30 for Entropy Sum. The intuition that forking tokens (high-entropy decision points) carry disproportionate signal is grounded in the nature of long-CoT reasoning.

- **Comprehensive experimental validation across three training paradigms.** The paper evaluates HES on SFT (Tables 1–4, with two model families and three domains), RFT (Table 5, per-query and global-pool settings), and RL (Table 6, with asymmetric sampling ablations). This breadth—rare in data selection papers—directly supports the claim that HES is a *unified* metric.

- **Pruning lowest-HES data consistently improves over full-dataset training.** Highest-HES-80% surpasses Full-Dataset on Qwen3-8B (35.36% vs 32.61%), DeepSeek-R1-Distilled-7B (32.35% vs 30.22%), Code domain (39.51% vs 36.28%), and STEM domain (45.48% vs 44.42%). This counter-intuitive result—removing the worst 20% of data improves performance—is strong evidence that HES identifies genuinely harmful samples rather than merely ordering by a correlate.

- **Small-to-large model transfer works effectively.** Using Qwen3-0.6B as a proxy to score data for Qwen3-8B achieves 32.12% AVG, comparable to the 8B's self-selection (31.14%), with over an order of magnitude less inference cost. This directly supports practical deployability.

- **Sensitivity analysis confirms robustness across hyperparameters.** The token ratio of 0.005 and data selection ratios around 20%/80% consistently deliver best or near-best performance across all domains (Figures 3–4), showing the method does not require careful tuning.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification despite small-margin comparisons.** The paper reports only average pass@1 over 16 sampling paths without confidence intervals, error bars, or statistical significance tests. Several key comparative margins are small enough to fall within evaluation noise: HES vs Entropy Sum (ES) is 0.22 points (31.14 vs 30.92, Table 1); HES vs Length is 0.47 points (Table 1); Pos-High,Neg-Rand vs Full-Batch is 0.67 points (Table 6). Without variance estimates, the reader cannot distinguish genuine improvement from sampling noise. This is the most significant limitation because the paper's central thesis is comparative—HES is claimed to be a *better* signal than existing metrics—and several strong baselines (ES, Length) are separated by fractions of a point. The paper would benefit from bootstrapped confidence intervals or similar, at minimum for the aggregate AVG column.

- **Missing baseline comparisons in RFT experiments.** The RFT experiments (Table 5) compare HES against Random, Length, and Difficulty but omit Entropy Sum (ES) and Average Entropy (AvgE)—two of the key entropy baselines from the SFT experiments where HES's margins were already small (0.22–0.47 points). Since the SFT results are the strongest evidence that HES beats ES/AvgE, the absence of these baselines in RFT weakens the claim that HES is a uniformly superior metric. Including them would validate whether the advantage replicates across paradigms.

### Minor

- **Temperature used for computing token entropies for HES is not specified.** The paper specifies a generation temperature of 0.6 for evaluation (line 151) but does not state whether this temperature (or another) was used when computing the token-level entropies that form the HES scores. Since temperature scaling changes logit distributions and therefore entropy values, this is a reproducibility detail that should be provided.

- **RL findings validated only on a 1.5B model.** The RL experiments use DeepSeek-R1-Distilled-Qwen-1.5B, which achieves ~20% absolute accuracy. While following the DeepScaleR setup is a reasonable design choice given compute constraints, the paper does not discuss whether the asymmetric sampling strategy (Pos-High, Neg-Rand) transfers to larger models where baseline performance is substantially higher. A note on expected generalizability would strengthen the claims.

### Trivial
None.

## Nice-to-Haves

- A correlation analysis between HES and response length within correct solutions would further address the natural concern that longer responses mechanically produce more high-entropy tokens, even though the Length baseline comparison already partially mitigates this.
- Including perplexity as a baseline (closely related to AvgE but more standard in the data selection literature) would round out the baseline set.
- The Forking-Only baseline (32.51 AVG, competitive with Full-Dataset at 32.61) is an interesting result that the paper does not discuss; a brief note would be informative context.

## Removed Points

These points were raised in reviews but are not included as weaknesses in the main review for the reasons stated:

- **"Random-20% beats Full-Dataset in Table 2 undermines the full-dataset baseline"** — The margin (30.38 vs 30.22, a 0.16-point difference) is negligible and well within evaluation noise. The paper's key claim (HES-80% at 32.35 outperforms Full-Dataset at 30.22 by 2.13 points) is unaffected.

- **"Figure 1 relationship between HES and quality is more nuanced than presented"** — The paper clearly explains its conditional use of HES (high HES among correct solutions indicates higher learning value). Figure 1's finding that incorrect solutions have higher HES is used to demonstrate discriminative power, and the SFT/RFT/RL sections all specify that HES is applied conditionally within correct-solution pools or with separate positive/negative handling.

- **"Forking-Only baseline is competitive"** — This is an interesting observation but not a weakness. The paper does not claim HES is the only effective approach; it claims HES is a better *selection metric*.

- **"Perplexity baseline missing"** — The paper includes AvgE, which is closely related to perplexity. This is a minor omission that falls under nice-to-have.

- **"RL uses a smaller model"** — Weakened to a minor weakness above, as it is a practical limitation acknowledged by following the DeepScaleR setup.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the lack of uncertainty quantification and missing baselines as the primary gaps but do not add unexpected synthetic observations.

## Suggestions

1. **Add uncertainty quantification.** Bootstrap confidence intervals over the 16 sampling paths for the AVG column, at minimum for the key comparison tables (1, 2, 6). This is the single highest-leverage improvement.

2. **Include ES and AvgE baselines in the RFT experiments (Table 5).** The RFT setting is the missing link in the otherwise thorough baseline comparison chain.

3. **Specify the temperature used for HES entropy computation** in Section 3.1.

4. **Soften comparative language** in claims where margins are under 1 point and no significance test is available (e.g., "shows a clear advantage over simpler heuristics like length" → "shows a consistent advantage").

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| qUJsX3XMBH (Rethinking Data Selection at Scale) | 4.40 | R1, low band | Negative-result paper; HES is clearly stronger (novel proposal, broad eval) |
| cijO0f8u35 (Scaling Relationship on Learning Math Reasoning) | 5.25 | R1, mid band | Limited to GSM8K only; HES has broader evaluation |
| 1hQKHHUsMx (What Kind of Pretraining Data) | 6.75 | R1, mid band | More sophisticated analysis (influence functions) but very narrow scope (80 queries); comparable quality |
| BTKAeLqLMw (DEITA — What Makes Good Data for Alignment) | 6.33 | R2, upper band | Requires costly GPT-4 for scoring; HES is training-free and covers more paradigms |
| FAfxvdv1Dy (STAFF: Speculative Coreset Selection) | 6.50 | R2, upper band | Similar quality; stronger baselines but less paradigm coverage than HES |
| I5p1Gm8GFS (3DS: Decomposed Difficulty Data Selection) | 5.75 | R2, lower band | Domain-specific (medical); HES has broader scope |
| SpTzsQjgxF (Rule-Based Rating and Selection) | 5.75 | R2, lower band | Requires LLM-generated rules; HES is simpler and more direct |

**Bracket rationale:** Round 1 placed the paper between 5.5 and 7.0. Round 2 narrowed this by comparing against anchors at 5.75, 6.33, and 6.50. The paper is above the 5.25–5.75 range (novelty and breadth) and comparable to the 6.33–6.50 range, but the lack of uncertainty quantification and missing RFT baselines prevent it from reaching the cleaner 7+ level.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>