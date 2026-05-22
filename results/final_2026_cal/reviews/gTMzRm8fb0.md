Now I have all the information needed to write the consolidated review.

## Calibration Report

**Round 1 bracket:** Low band (<3.5) had irrelevant or weak papers (FwVL5ckUdF at 3.33, dI5GvUg7ps at 2.50). Middle band (3.5–7.5) had relevant papers including PR6oISgk90 (ReRe, 6.0, Reject), JlwYkFm91F (DNR, 5.5, Accept Poster), cuzWopwoZG (Diversity, 4.67, Accept Poster), VWyPsYaSg2 (GR vs DR, 4.0, Withdrawn). High band (7.5+) returned only unrelated papers (kernel functions, matrix sign, LLM conversations, RL, transduction). Initial bracket: **5.5–8.0**.

**Round 2 narrowing:** Focused within (5.5, 8.0) and (4.0, 8.0) for recommendation/ranking papers. Read anchors in full: PR6oISgk90 (6.0, Reject — weaker; no theory, no online A/B), JlwYkFm91F (5.5, Accept Poster — weaker theory, smaller margins, similar online ambiguity), eDh0K9YNoL (4.5, Reject — unclear method, proprietary-only evaluation). GoalRank is clearly stronger than all three.

**Comparison reasoning:** GoalRank has (a) a genuine theoretical guarantee, (b) a principled training objective, (c) extensive offline experiments on three datasets, (d) an industrial online A/B test, and (e) scaling experiments. These go beyond what the ~5.5–6.5 recommendation anchors offer. Weaknesses (training-signal confound in framing, offline-online gap) are real but not fatal — they do not undermine the core claim that GoalRank as a complete method outperforms existing approaches. Final score: **7.0**.

---

## Summary

This paper proposes GoalRank, a generator-only ranking framework that replaces the two-stage Generator–Evaluator (G-E) paradigm with a single large generator trained via group-relative optimization. The paper makes three contributions: (1) a theoretical guarantee (Theorem 1) that for any finite (M)G-E system there exists a generator-only model with strictly smaller approximation error to the optimal policy, with error vanishing as model size grows; (2) a group-relative optimization principle that uses a reward model to construct a reference policy over groups of candidate lists, yielding a tractable cross-entropy training objective; and (3) an instantiation of these ideas in GoalRank, validated through offline experiments on three datasets (ML-1M, Amazon-Book, Industry) and a large-scale online A/B test on a short-video platform with hundreds of millions of daily active users.

## Strengths

- **Theoretical guarantee (Theorem 1).** The paper proves that a single sufficiently large generator-only model can achieve strictly smaller KL-divergence to the optimal ranking policy than any finite mixture of generators with an evaluator, and that the error tends to zero as model width/depth grows. This is a formal existence result that goes beyond empirical comparisons and provides a principled motivation for the generator-only paradigm. The proof uses a universal approximation argument over the probability simplex induced by the evaluator's selection.

- **Principled derivation of group-relative optimization.** Section 3.2 starts from an entropy-regularized oracle policy (Boltzmann distribution over lists) and shows how a biased reward model can still yield a valid reference policy via group-relative normalization (Equation 4), provided reward gaps within the group are sufficiently large. The resulting cross-entropy loss (Equation 5) connects the theoretical ideal directly to a practical algorithm. This is a clean and well-motivated objective.

- **Consistent and large-margin improvements across all settings.** On ML-1M, GoalRank improves H@6 by +17.12% and MAP@6 by +15.43% over the best baseline (Table 1). On the Industry dataset the gains reach +25.39% H@6 and +29.63% MAP@6. The online A/B test (Table 4) shows statistically significant improvements on all five business metrics (e.g., +0.149% App Stay Time, +1.212% Effective View, +0.802% Comment rate) when replacing the production MG-E system. These results are concrete and replicated across datasets.

- **Demonstration of scaling laws.** Figure 3 shows that GoalRank's performance rises steadily as model size increases from 1M to 0.1B parameters, while DNN, RankMixer, PIER, and MG-E all plateau. This directly supports Theorem 1's limit result and distinguishes GoalRank from prior approaches that do not benefit from larger capacity. The contrast is sharp and scientifically interesting.

- **Systematic ablation on group size and reward-model bias.** Table 2 identifies moderate group sizes (8–20) as optimal, balancing sample sufficiency against bias amplification. Table 3 shows that even with injected noise λ=0.5, GoalRank still outperforms all baselines. These experiments validate the design choices and confirm robustness to practical imperfections.

## Weaknesses

### Major
- **Offline comparison conflates training signal with paradigm.** The offline experiments compare GoalRank (trained with the reward model as its supervision signal via group-relative optimization) against baselines (trained with standard ranking objectives). While the paper states that "all baselines share exactly the same evaluator (reward model) as GoalRank," this refers to inference-time use for G-E/MG-E baselines, not training signal. The paper's framing emphasizes "can the generator-only paradigm outperform?" (Section 3.1), but the offline experiments do not isolate paradigm from training objective. A cleaner comparison would include a generator-only baseline trained with the same reward-model supervision (e.g., via distillation). The online A/B test is a fairer head-to-head comparison and mitigates this concern, but the offline evidence for the paradigm claim specifically is confounded.

### Minor
- **Large offline-online performance gap is not discussed.** Offline improvements on the Industry dataset range from +20% to +48%, while online gains are 0.1%–1.2%. The paper does not acknowledge or explain this discrepancy. While online and offline metrics are not directly comparable (different N, L, evaluation criteria), the magnitude of the gap warrants discussion about what the offline metrics capture and what they miss relative to real user behavior. This is especially relevant given that the Book dataset's offline gains (4–5%) are much closer to the online range.

- **Theory-practice connection is indirect.** Theorem 1 guarantees *existence* of a generator-only model with smaller approximation error, but does not guarantee that the group-relative objective (Equation 5) converges to that model. The derivation of the training objective from an evidence upper bound is reasonable, but the link between the existence guarantee and the practical algorithm is inferential rather than rigorous. This weakens the claim that the theory "explains" the empirical results.

- **Group construction relies on auxiliary policies.** GoalRank's group construction (Section 3.3) uses an auxiliary set of ranking policies M (heuristic and lightweight neural methods) to generate diverse candidate lists. The quality and diversity of GoalRank's training signal therefore depends on these auxiliary policies, whose performance and selection criteria are not thoroughly analyzed. An ablation isolating the contribution of specific auxiliary policies would strengthen the paper.

### Trivial
- The reward model bias experiment (Table 3) uses only λ ∈ {0.0, 0.2, 0.5}. Testing λ > 0.5 would more thoroughly probe robustness.
- The scaling experiment uses proportionally sampled data at small model sizes "to ensure fair comparison" (footnote 2), but the impact of this subsampling on the observed scaling trend is not analyzed.

## Nice-to-Haves
- Including a generator-only baseline trained with reward-model distillation (e.g., using the same reference policy as training targets) would cleanly isolate whether the paradigm or the training signal drives gains.
- A more detailed analysis of what drives the offline-online gap — e.g., comparing the distribution of offline proxy rewards vs. online metric deltas — would increase confidence in the offline evaluation methodology.

## Removed Points
- "Omits critical architectural details of the generator" — These details are deferred to appendices (C, D.2), which are stripped by the parser. The paper also commits to releasing code. Not a valid criticism given paper format constraints.
- "Omits how generators in MG-E are trained" — Same issue; details are in truncated appendices.
- "Formatting/style nitpicks" and "typos" — These are parser artifacts, not author errors.
- "Missing related works" — Cannot verify without external sources.
- Strength Finder's generic strengths about "the paper addressed an important problem" — Dropped as too generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The key intellectual move — proving that a single larger generator can strictly dominate any finite mixture of small generators with an evaluator, and then deriving a practical training objective that leverages a reward model in a group-relative way — is already clearly articulated by the authors. The review process did not surface any additional novel interpretation.

## Suggestions

1. Add a discussion of the offline-online gap, ideally with analysis of how offline proxy metrics relate to online business metrics, and whether the gap reflects evaluation fidelity or fundamental differences in the operating regime.
2. Include a controlled experiment where a generator-only baseline (e.g., a DNN or RankMixer) is trained with the same reward-model supervision (via distillation or direct KL minimization) to isolate paradigm from training signal.
3. Clarify in Section 3.1 that Theorem 1 is an existence guarantee, not a convergence guarantee for the specific training objective — and state how the group-relative derivation bridges this gap.
4. Add ablation over contributions of individual auxiliary policies in the group construction.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>