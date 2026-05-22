Excellent. Now I have enough calibration context. Let me synthesize the final review.

## Summary of Bracketing and Calibration

**Round 1 bracket**: Based on initial search, I placed this paper between the weak anchors (~3) and strong anchors (~8), establishing a plausible range of 4–7.

**Round 2 narrowing**: I compared against ReNovo (6.50, Accept), RankNovo (5.50, Reject), DenoiseVAE (7.00, Accept), and RoCA (6.67, Accept) — all from proteomics or causal ML. CausalNovo is clearly stronger than RankNovo (better improvements, more thorough evaluation). It is comparable to ReNovo (both are de novo sequencing papers with good empirical results but some missing controls). It is slightly weaker than DenoiseVAE and RoCA due to the theoretical murkiness around the purification objective.

**Final score**: 6.5 — the paper is solid and above the acceptance threshold, slightly below the strongest anchors due to one murky theoretical component and one missing ablation control, but with stronger empirical breadth than its closest comparator ReNovo.

Now writing the review.

---

## Summary

CausalNovo introduces a model-agnostic framework for *de novo* peptide sequencing that learns causal representations (signal fragment ions) disentangled from non-causal noise peaks. It formalizes the task via a Structural Causal Model, derives independence and sufficiency principles, and implements them through a Causality Extraction Module (CEM) with contrastive and information-theoretic objectives. Experiments across three benchmark datasets and three strong baselines show consistent, substantial improvements (up to 12% in amino acid precision, up to 15.1% in PTM precision), supported by vulnerability analyses, NSR generalization studies, and attention interpretability evidence.

## Strengths

1. **Principled causal formulation grounded in the SCM framework.** The paper formalizes peptide sequencing using Reichenbach's Common Cause Principle, deriving two clear properties (independence and sufficiency) that directly motivate the CEM design and learning objectives. This goes well beyond ad-hoc robustness tricks and provides a reusable conceptual foundation for causal reasoning in proteomics.

2. **Consistent and substantial empirical gains across diverse settings.** CausalNovo improves all three baseline models (CasaNovo, AdaNovo, π-HelixNovo) across all three datasets, at amino acid, peptide, and PTM levels, with gains reaching +12.0% (amino acid precision on Seven-species) and +15.1% (PTM precision on Seven-species). The improvements are large, consistent, and observed without changing the underlying model architecture.

3. **Multiple converging lines of evidence for the claimed mechanism.** Beyond raw performance numbers, the paper provides vulnerability analyses (Figures 1, 3) showing CausalNovo-enhanced models degrade less under noise peak perturbation, NSR generalization (Figure 4) showing improved robustness at all noise levels, attention analysis (Table 7) showing the model actually attends to causal peaks more, and cross-species validation (Table 3) showing improved generalization. This multi-evidence approach convincingly supports the causal interpretation.

4. **Clean ablation study confirming each component's contribution.** Table 4 decomposes the full system and shows that independence, purification, and symmetric training each add measurable value. This counters the concern that performance gains are merely from added parameters.

## Weaknesses

### Major
- **The purification objective (maximizing I(z_s; Y)) lacks a fully coherent theoretical justification.** The paper states that this objective "can indirectly lead to the purification of z_c" because optimizing I(z_c; Y) alone could allow non-causal information to leak into z_c while reducing I(z_s; Y). The proposed response — maximizing I(z_s; Y) — would create competition between the two streams for predictive information. This is a plausible mechanism, but the paper's explanation is too brief and appears to contradict standard disentanglement practice where non-causal representations are *discouraged* from predicting the label. The authors either need to (a) provide a clearer theoretical argument (e.g., grounded in information bottleneck or redundancy reduction), (b) cite a formal result from Chen et al. (2022) that justifies this, or (c) honestly reframe this objective as a heuristic regularizer that helps empirically. The ablation shows it works, but the causal framing of this specific objective is not yet earned.

### Minor
- **No explicit control for the added parameters of the CEM.** The CEM adds 3 Transformer layers + an MLP to the baseline encoder's 9 layers. The ablation study (Table 4) compares "Baseline" (no CEM) against "Independence only" (CEM + contrastive loss), but does not test a control condition where a module of equivalent capacity is added *without* any causal objectives (e.g., trained with standard cross-entropy only). Without this control, some of the observed gains could in principle come from increased model capacity rather than the causal intervention. The vulnerability and attention analyses partially address this concern, but a clean capacity-control experiment would strengthen the paper significantly. (Note: This is a real gap but not fatal — the ablation shows that adding causal objectives on top of the CEM progressively improves performance, suggesting the causal intervention itself matters.)

- **No statistical significance or variance reporting.** The main results (Tables 1, 2) report single-run numbers without confidence intervals or standard deviations. Given the improvements are large and consistent across 3 baselines × 3 datasets, this is less concerning than it would be for marginal gains, but it remains a gap in reporting rigor.

### Trivial
- The explanation "However, it can reduce I(z_s; Y)" (Section 3.3) is grammatically ambiguous — it is unclear what "it" refers to.
- The increased training time (2.3×) is noted but a brief breakdown of which component causes the overhead would help.

## Nice-to-Haves
- A brief hyperparameter sensitivity analysis (temperature τ, replacement fraction α) would demonstrate robustness.
- Extending the framework to additional baseline architectures (e.g., InstaNovo, SearchNovo) would strengthen claims of model-agnosticity.
- Reporting results with the more realistic evaluation protocol (training on large external corpora, as used by ContraNovo/RankNovo) would increase real-world relevance.

## Removed Points
- **"The experimental design lacks a control for increased model capacity"** — kept but demoted to Minor. The reviewer's concern about a "structural gap" is overstated; the ablation already shows progressive improvements as causal objectives are added to the CEM, and the vulnerability/attention analyses provide direct causal evidence that extra capacity alone cannot explain.
- **"Missing error bars"** — kept but placed as Minor.
- Points about missing appendix content, missing related work references, and formatting issues — all removed per hard rules (parser artifacts, not verifiable).
- Strength Finder's generic claims about problem importance — removed as too generic.

## Novel Insights
None beyond the paper's own contributions. The strength of this paper is in its systematic application of a causal framework to *de novo* peptide sequencing rather than in a fundamentally new conceptual insight about causality or representation learning.

## Suggestions
1. **Clarify the purification objective.** Either provide a formal information-theoretic argument for why maximizing I(z_s; Y) "purifies" z_c (e.g., via a redundancy reduction or competition mechanism), or reframe it as a practical heuristic regularizer that empirically helps rather than claiming it follows directly from causal principles.
2. **Add a model capacity control experiment.** Include a baseline where the CEM architecture is added but trained only with standard cross-entropy (no independence or purification objectives). If this does not achieve the same gains, the case for causality is substantially stronger.
3. **Report variance across multiple runs** (at least 3 seeds) for the main tables to improve statistical credibility.

## Score and Decision

**Anchors retrieved (all rounds):**
- yIRtu2FJvY: 3.00 (round 1) — weak paper on VAE for variant effect prediction; clearly below this paper.
- qi5dkmEE91: 3.00 (round 1) — weak paper on motif explanations; below this paper.
- AvXrppAS2o: 3.00 (round 1) — weak paper on causal structure learning; below this paper.
- doBof19Ia4: 2.60 (round 1) — weak paper on RNA design; below this paper.
- ym7pr83XQr: 7.00 (round 1) — DenoiseVAE, strong paper on molecular pre-training; slightly above this paper due to cleaner theory.
- Z756zcjNcC: 4.50 (round 1) — Denoising Diffusion Causal Discovery; below this paper.
- 9htTvHkUhh: 6.33 (round 1) — RNA property prediction with geometric context; comparable but CausalNovo has stronger novelty.
- ZDaI3aSDTF: 3.67 (round 1) — weak RNA SSP paper; below this paper.
- zMPHKOmQNb: 8.00 (round 1) — very strong protein generation paper; above this paper.
- PdaPky8MUn: 8.00 (round 1) — strong paper on sequence models; above this paper.
- 0ctvBgKFgc: 8.00 (round 1) — strong protein structure generation; above this paper.
- 3cuJwmPxXj: 8.00 (round 1) — strong identifiable representation learning; above this paper.
- uQnvYP7yX9: 6.50 (round 2) — ReNovo, retrieval-based de novo sequencing; comparable but CausalNovo has broader experiments.
- 87B3zDRMjv: 5.50 (round 2) — RankNovo, reranking for de novo sequencing; below this paper.
- I2ZYngkRW6: 4.25 (round 2) — knowledge distillation for de novo sequencing; below this paper.
- 78tc3EiUrN: 6.00 (round 2) — MADGEN, MS-based molecular generation; comparable.
- Q0s6kgrUMr: 6.67 (round 2) — RoCA, causal/anticausal discovery; slightly above due to cleaner theory.
- lWXedJyLuL: 5.67 (round 2) — SIT, causal view of instruction tuning; below this paper.
- 1iuaxjssVp: 7.25 (round 2) — InvMSAFold, inverse folding; above this paper.

**Round 1 bracket:** 4–7 (plausible range after bracketing with weak ~3, middle ~4-7, strong ~8 anchors).

**Round 2 narrowing:** Compared against ReNovo (6.50) — CausalNovo has broader and more convincing experiments but similar weaknesses; RankNovo (5.50) — CausalNovo is clearly stronger; DenoiseVAE (7.00) and RoCA (6.67) — slightly stronger due to cleaner theoretical framing. This places CausalNovo at the upper end of the bracket.

**Final score:** 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>