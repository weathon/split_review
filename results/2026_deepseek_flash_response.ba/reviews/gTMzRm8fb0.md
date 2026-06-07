## Summary

This paper proposes **GoalRank**, a generator-only (one-stage) ranking framework for recommender systems. It provides a theoretical result (Theorem 1) showing that a sufficiently large single generator can achieve strictly smaller approximation error to the optimal ranking policy than any finite-mixture Multi-Generator–Evaluator system. To train such a model, the paper introduces a **group-relative optimization** principle: given a biased reward model, it constructs a reference policy by normalizing reward scores within groups of candidate lists, then trains the generator to minimize KL divergence to this reference policy. Experiments span offline benchmarks (ML-1M, Amazon-Book, Industry datasets) and a large-scale online A/B test on a platform with over half a billion daily active users.

## Strengths

- **Theorem 1 with explicit width-scaling construct (Section 3.1, lines 106–118):** The theorem proves the existence of a generator-only class with width ≥ kα + n whose policy space achieves strictly smaller KL approximation error to π* than any k-generator mixture, with error → 0 as n → ∞. This is a concrete, non-trivial theoretical guarantee with an explicit width requirement, not just a vague expressiveness claim.

- **Group-relative reference policy construction (Equation 4, lines 146–154):** The paper derives π^ref(l|ℬ) = exp((r̂(l)-r̄_ℬ)/σ_ℬ) / Σ exp(…) as a tractable surrogate for the oracle policy π* when only a biased reward model r̂ is available. This bridges the gap between the theoretical ideal (Equation 2) and a practical training objective (Equation 5) by exploiting within-group reward gaps.

- **Large-scale online A/B validation (Section 4.2, Table 4, lines 307–317):** GoalRank was tested on a platform serving "over half a billion daily active users" with eight traffic buckets (tens of millions of users each) over at least 14 days. Pure GoalRank outperforms the production MG-E baseline across all five business metrics (App Stay Time +0.149%, Watch Time +0.197%, Effective View +1.212%, Like +0.227%, Comment +0.802%). This is substantially stronger evidence than most papers at top venues provide.

- **Controlled ablation on group size revealing an inverted-U pattern (Table 2, lines 256–262):** Table 2 systematically varies |ℬ| from 3 to 100 and shows a clear optimum at 8–20, with degradation at both extremes (e.g., H@6: 62.88 at 3 → 69.95 at 8 → 63.50 at 100). This directly validates the trade-off predicted by Equation 3 and shows the method is not overly sensitive to this hyperparameter.

- **Bias robustness experiments (Table 3, lines 264–271):** Under noise injection λ ∈ {0.0, 0.2, 0.5}, GoalRank's H@6 drops gracefully from 69.93 to 63.77 — and even at λ=0.5 (half the reward signal is Gaussian noise), it still outperforms all baselines. This addresses a key theoretical concern (biased reward model) with empirical evidence.

## Weaknesses

### Major

- **Asymmetric evaluation confounds the paradigm comparison (Section 4.1.2, lines 232–236).** GoalRank trains its generator by *minimizing cross-entropy with π^ref*, which is derived directly from the reward model's scores (Equations 4–5). The generator therefore receives dense supervision from the reward model during training — this is distillation. The G-E baselines (PIER, NAR4Rec) use the same reward model *only as an evaluator at inference* to select among candidate lists; their generators are trained through their own objectives without access to the reward model's supervision. The paper states "all baselines share exactly the same evaluator (reward model) as GoalRank" — this is about the inference-time evaluator, not the training signal. The comparison therefore evaluates (a) a generator trained to mimic the reward model's preferences against (b) generators trained without that signal. This asymmetry plausibly accounts for a significant fraction of GoalRank's reported advantage, making the headline "generator-only paradigm outperforms G-E paradigm" inadequately supported. A fairer comparison would require either training G-E baselines' generators with the same distillation signal or ablating GoalRank's training to isolate the architectural advantage from the training-signal advantage.

- **MG-E baselines show anomalously low AUC (Table 1, lines 208–224).** The MG-E methods (G-3, G-20, G-100) exhibit remarkably poor AUC that is inconsistent with their other metrics and with common sense: on ML-1M, G-100 (100 generators!) gets AUC 76.48 while a simple DNN gets 86.87 and DLCM gets 89.35. On Industry, G-100 gets AUC 75.30 while RankMixer gets 91.03. On Book, G-100 gets AUC 77.36 while RankMixer gets 92.23. An ensemble of 100 generators should not produce substantially *worse* AUC than a single feedforward network. This pattern suggests either (a) the MG-E implementation is flawed, (b) the evaluation protocol (N=50, L=6, ground truth = last 6 interactions) is incompatible with how MG-E methods are designed to be evaluated, or (c) the reward model used as evaluator is configured in a way that disadvantages MG-E. In any case, the baselines do not appear to be operating at a credible strength, and the enormous reported gains (e.g., +17.12% H@6 on ML-1M, +25.39% on Industry, +47.73% on Book) cannot be interpreted without an explanation for this anomaly.

### Minor

- **The "evidence upper bound" claim is overstated (Abstract, lines 9, 34, 321; Section 3.2, lines 134–140).** The abstract, introduction, and conclusion claim the paper "derives an evidence upper bound of the one-stage optimization objective." What Section 3.2 actually shows (lines 134–140) is a standard manipulation: from the entropy-regularized objective (Eq 1), the maximum is τ log Z (the log-partition function), attained when KL(π‖π*)=0. This is textbook maximum-entropy RL (Ziebart 2010), not a novel bound. The paper frames this textbook result as a new theoretical contribution, which is misleading. The authors should either characterize what about this bound is new or remove the claim and describe the derivation accurately as standard.

- **Scaling experiments confound model size with data size (Figure 3, footnote 2, line 292).** The paper reports scaling laws on Industry-0.1B varying model size from 1M to 0.1B parameters, but footnote 2 states: "For very small models, training on the full dataset leads to unstable convergence. To ensure fair comparison, we proportionally sample the dataset for all models (including GoalRank) at the same parameter scale." This means model size and training data size are varied simultaneously. Any observed improvement with larger models could be due to more training data rather than increased model capacity. The flat scaling of baselines is also uninformative under this protocol.

- **No confidence intervals or standard deviations in main results (Table 1, line 226).** The paper states results are averaged over five independent runs but reports only point estimates. Given the massive reported gains (up to +47.73%), confidence intervals or standard deviations would help assess robustness.

- **Discrepancy between offline and online gains is not discussed (Table 1 vs. Table 4).** The paper reports 17–25% offline improvements (Table 1) but sub-1% online improvements (Table 4). This gap is not addressed anywhere. While some gap is expected (offline evaluation is an imperfect proxy), a difference of two orders of magnitude warrants discussion, as it affects how readers interpret the offline results.

### Trivial

- The group construction (line 180–184) introduces an auxiliary set of ranking policies M during training, meaning GoalRank depends on *multiple* generators during training, which somewhat undermines the "generator-only" framing, though it remains generator-only at inference.

## Nice-to-Haves

- For the scaling experiments, a clean ablation holding training data fixed while varying model size (even if only for a subset of sizes) would strengthen the scaling law claim considerably.
- Statistical tests (p-values or confidence intervals) for the online A/B results, beyond the "statistically significant" caption in Table 4.

## Removed Points

- "Evidence upper bound does not appear in the paper" — factually incorrect; the derivation appears in lines 134–140 (the bound τ log Z = sup_π{…}). However, the bound is standard, so the criticism is reframed as an overclaim issue (see Minor weakness above).
- "Gap between theory (π* via r*) and algorithm (π^ref via biased r̂)" — the paper acknowledges the bias in Section 3.2 and provides bias-robustness experiments (Table 3). A gap between ideal theory and practical approximation is standard in ML papers.
- "Missing related works" — cannot be verified without external sources.
- Formatting/style nitpicks, reproducibility nitpicks about hyperparameters, and other parser-artifact complaints.
- Several generic "one-size-fits-all" weaknesses from the harsh critic (e.g., requesting more datasets when the current set is adequate) — removed per filtering guidelines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the asymmetric evaluation.** Either train G-E baselines' generators with the same reward-model distillation signal (using π^ref as a target), or — alternatively — train a version of GoalRank *without* the distillation signal to isolate the value of the generator-only architecture from the value of the training signal. Without this, the central claim (generator-only > G-E) is confounded.

2. **Diagnose and explain the anomalous MG-E AUC.** The AUC values for MG-E methods (76–77 on ML-1M and Industry) are far below what even simple DNNs achieve (87–92). This needs to be explained or the baselines re-implemented. If the current setup genuinely degrades MG-E, that must be acknowledged as a limitation of the comparison.

3. **Remove or recharacterize the "evidence upper bound" claim.** The derivation in Section 3.2 is standard KL / maximum-entropy manipulation. Describe it accurately rather than marketing it as a novel bound.

4. **Add confidence intervals to Table 1** and discuss the offline/online performance gap.

5. **Disentangle model size from data size** in the scaling experiments, or at minimum acknowledge the confound explicitly.

## Score and Decision

**MY FINAL SCORE:** <score>5.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (< 3.5): e.g., *One to All* (3.0), *Prompt2Rec* (3.2) — simple recommendation papers without theory or online validation. GoalRank is clearly well above these.
- Middle band (3.5–7.5): *SUBER* (4.25), *PG-Ret* (4.0), *Preference Discerning* (4.0) — recommender papers with interesting ideas but clear flaws (no online validation, weak baselines). GoalRank is stronger than these in experimental rigor and has a real theoretical result.
- Strong band (> 7.5): e.g., *Rethinking Reward Modeling* (8.0), *Tight Lower Bounds* (8.0) — pure theory papers in a different genre. Not directly comparable but establish the ceiling.

**Round 2 (Narrowing):**
- *Embedding Collapse* (5.25, rejected) — identifies a phenomenon and proposes a solution, but marginal improvements and no online validation. GoalRank is somewhat stronger (online test, larger improvements) but has more significant evaluation concerns.
- *PreferDiff* (5.75, accepted) — adapts diffusion models for recommendation with a ranking loss. No online validation, limited novelty. GoalRank is comparable in strength: stronger experiments but more significant evaluation confounds.
- *MQL4GRec* (6.5, accepted) — multimodal generative recommendation with strong offline results but no online validation and limited novelty. GoalRank is weaker than this anchor due to the evaluation issues (asymmetric comparison, anomalous MG-E baselines) that undermine the core claims.

**Final bracket:** 5.0–6.0. Closer to Embedding Collapse (5.25) than to MQL4GRec (6.5) because the evaluation confounds and anomalous baselines are serious concerns that the paper shares with the weaker anchor. **Final score: 5.5** — the paper has genuine strengths (Theorem 1, online validation, ablation studies) but the asymmetric comparison and anomalous MG-E baselines prevent the central claims from being adequately supported.