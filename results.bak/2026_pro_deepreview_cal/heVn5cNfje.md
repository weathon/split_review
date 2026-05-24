Now I have a clear picture. Let me synthesize the final review.

---

## Summary
This paper introduces the High-Entropy Sum (HES), a training-free metric that sums only the top 0.5% highest-entropy tokens in a reasoning path, designed to capture critical "forking" points that indicate reasoning complexity. The authors validate HES as a data selection signal across three training paradigms — SFT, RFT, and RL — showing that HES-guided selection consistently outperforms random selection and other heuristic baselines. In SFT, training on the top 80% HES-ranked data surpasses full-dataset performance by pruning harmful low-quality samples; in RFT, HES beats length and difficulty baselines; and in RL, an asymmetric sampling strategy (high-HES positives + random negatives) outperforms full-batch training despite using half the data.

## Strengths
- **Broad, consistent empirical validation across paradigms and domains.** HES is evaluated in SFT (two datasets, two model families, plus Code and STEM domains), RFT (per-query and global-pool settings, k=2/4/8), and RL (GRPO with multiple curation strategies). Gains are consistent throughout — e.g., Highest-HES-80% SFT on Open-Math-Reasoning achieves 35.36% vs. full-dataset 32.61% (Table 1), Pos-High/Neg-Rand RL achieves 21.30% vs. Full-Batch 20.63% (Table 6). This breadth of evidence is a genuine strength.

- **Training-free and computationally cheap.** HES requires no auxiliary model training — it is computed directly from the generating model's token-level entropy during inference. The small-proxy-model transfer experiment (0.6B model selecting data for 8B training, Table 1, 32.12% vs. 31.14% self-selection) demonstrates practical cost savings of >10×.

- **Rich ablation of entropy variants.** Table 1 compares HES_relative, HES_absolute, AvgHE, AvgE, and total entropy sum, with HES_relative consistently best. The sensitivity analysis (Figures 3–4) shows robustness to both the data selection ratio and the high-entropy token percentile.

- **The finding that pruning low-HES data boosts performance beyond the full dataset is notable and practically valuable.** In SFT, Top-80% HES consistently exceeds Full-Dataset performance across all domains (Tables 1–4), and Lowest-HES-20% severely degrades it (14.90% vs. 32.61%). This asymmetry is well-demonstrated and actionable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Motivational gap between Figure 1 and the actual usage of HES.** Figure 1 shows that *incorrect* responses have substantially higher mean HES (0.68) than *correct* ones (0.29). The text interprets this as HES being able to "distinguish high- and low-quality samples," but in all subsequent experiments, HES is used exclusively within pools of already-verified-correct data, where higher HES is treated as better. The leap from "HES separates correct from incorrect (with incorrect higher)" to "higher-HES correct samples are better training data" is asserted without direct evidence. The empirical results support the usage, but Figure 1 as presented motivates the opposite direction. A within-correct-only HES distribution analysis would close this gap cleanly.

- **No statistical variability reported.** All tables report single-point averages (average@16) without standard deviations, confidence intervals, or error bars. While single-run reporting is common in LLM training due to computational cost, the paper makes comparative claims (e.g., "Highest-HES-20% outperforms the full-dataset baseline") where even modest variance could affect interpretation. The consistency across settings provides informal robustness, but formal reporting would strengthen the evidence.

- **RL HES computation is underspecified.** Section 4.3 describes generating 32 rollouts and computing HES for positive/negative selection, but does not specify whether HES is computed from the current policy at each training step, a frozen reference model, or the initial checkpoint. Given that policy updates change token-level entropy distributions, this detail matters for reproducibility and fairness of the comparison.

- **Overstated framing around "obviating reward models."** The abstract and conclusion claim HES "obviates the need for costly external reward models" and provides a "training-free reward signal." HES does not predict correctness or serve as a reward — in RFT, answer verification (matching) is still required, and in RL, binary correctness rewards are still used. HES is a *quality-ranking heuristic within correctness-verified pools*, not a replacement for reward models. The paper would benefit from more precise language: HES *reduces reliance on process-level reward models* for data selection, rather than obviating them entirely.

### Trivial
- The RL description (line 195) says "select half with the highest HES from the pool of successful trajectories" and "randomly sample half failures" — it would be clearer to specify "half of each pool."
- Sensitivity analysis (Figures 3–4) is limited to SFT; extending one such analysis to RFT or RL would improve confidence in hyperparameter robustness across paradigms.

## Nice-to-Haves
- Including one or two annotated reasoning traces with token-level entropies overlaid and HES values would make the "forking points" concept more concrete.
- A brief hypothesis for why Medium-Difficulty underperforms severely (Table 1, 23.29% vs. Random-20% 25.89%) would add insight.
- An explicit analysis of HES distribution *within correct-only samples* would address the Figure 1 motivational gap.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic claim that "the claim HES obviates reward models is overstated" is partially removed as a fatal-level criticism.** The claim is indeed somewhat overstated, but it is retained above as a Minor weakness rather than a fatal flaw because the paper is clear throughout that HES is used within correctness-verified pools, and the phrase reasonably refers to *process-level* reward models rather than outcome verification.

- **Harsh Critic claim of a "potential circularity concern" in RL as a major issue is removed.** The paper does not explicitly specify HES computation details for RL, but in standard practice, token entropy is computed from the generating model's log-probabilities at generation time, which is the natural interpretation. This is retained as a Minor documentation gap rather than a methodological flaw.

- **Strength Finder claim about "rigorous ablation of entropy-based variants" is retained** because it is directly supported by Table 1's 12-method comparison.

- **Strength Finder claim about "clear theoretical motivation grounded in prior work" is retained** — the paper builds on the forking tokens concept from Wang et al. (2025) and provides an intuitive entropy-based operationalization.

- **Harsh Critic's "no qualitative examples" point is moved to Nice-to-Haves** — it would strengthen the paper but is not a weakness.

- **Harsh Critic's "missing baseline with learnable selection methods" is removed.** The paper already compares against difficulty-based methods (which use external models), length, and multiple entropy variants. Adding a learned selection method would be scope creep — the paper's contribution is precisely that a training-free metric can be competitive, and the existing baselines are adequate to demonstrate this.

- **All formatting/typographical criticisms are removed** per the hard rules.

## Novel Insights
The reviewers' input converges on an interesting point not fully developed in the paper: HES may be less a measure of "reasoning quality" per se and more a measure of reasoning *path complexity/density* — how many non-trivial decisions the model had to navigate. This distinction matters because complexity and correctness are orthogonal (incorrect paths can be complex too, as Figure 1 shows). Framing HES as a complexity metric that, when filtered through correctness verification, identifies *complex-yet-correct* reasoning paths would resolve the Figure 1 tension and provide a more precise conceptual foundation.

## Suggestions
- Rephrase the contribution to state that HES is a *complexity metric* for reasoning paths, and that within correctness-verified pools, higher complexity correlates with higher training value. This would resolve the Figure 1 direction problem.
- Add an explicit within-correct-only HES distribution analysis to directly support the claim that higher-HES correct samples are better training data.
- Report standard deviations or bootstrapped confidence intervals for at least the main SFT result tables, even if only in an appendix.
- Clarify in Section 4.3 whether RL HES is computed from the current policy or a fixed reference model.
- Tone down "obviates the need for costly external reward models" to "reduces reliance on process-level reward models for data selection."

## Score and Decision

**Calibration anchor comparison:**
- `qUJsX3XMBH` (avg 4.40, Round 1): "Rethinking Data Selection at Scale" — finds methods fail to beat random; HES is clearly stronger with consistent positive results.
- `Fty0wTcemV` (avg 6.00, Round 1): "DELIFT" — comparable data selection method with submodular functions; HES has broader paradigm coverage (3 vs. 1) and is training-free.
- `BTKAeLqLMw` (avg 6.33, Round 2): "DEITA" — data selection for instruction tuning using GPT-4 scores; HES is broader, more self-contained, and evaluated on harder reasoning benchmarks.
- `FAfxvdv1Dy` (avg 6.50, Round 2): "STAFF" — speculative coreset selection; comparable novelty level; HES is training-free and broader in scope.
- `3NnfJnbJT2` (avg 7.00, Round 2): "GIO" — gradient-based data selection with information-theoretic grounding; GIO is stronger due to theoretical depth and polished presentation.
- `f4gF6AIHRy` (avg 8.00, Round 1): "DiSF" — submodular file selection for pretraining with theoretical guarantees; clearly stronger.

The HES paper is empirically thorough, practically useful, and simple — placing it above DEITA (6.33) and STAFF (6.50), but below GIO (7.00) which has comparable empirical breadth plus stronger theoretical grounding. The minor weaknesses (Figure 1 motivation gap, no error bars, overclaiming) prevent it from reaching the 7.0+ tier.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>