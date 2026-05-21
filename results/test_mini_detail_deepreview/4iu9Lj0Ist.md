Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper establishes the first theoretical framework connecting certified machine unlearning with continual learning. It models a two-stage process where a continual learning algorithm (ℓ₂-regularized retraining) sequentially learns tasks, and an unlearning mechanism removes specific tasks upon request. The paper decomposes the post-unlearning excess risk into two components — continual learning excess risk and unlearning loss — and adapts two certified unlearning approaches (gradient-based via natural forgetting, and Hessian-based) to this setting, providing theoretical upper bounds. Experiments on MNIST with a linear model illustrate the trade-offs between the two objectives.

## Strengths

1. **First theoretical formulation of certified unlearning in continual learning.** The paper introduces a principled decomposition of post-unlearning excess risk into continual-learning excess risk and unlearning loss (Eqs. 5-7). This decomposition enables joint analysis of two objectives that are typically studied in isolation. The two-stage diagram (Fig. 1) and the mathematical modeling of the sequence of unlearning requests (Section 2.2) provide a clean foundation that the authors explicitly identify as lacking in prior work.

2. **Explicit theoretical guarantees for two adapted algorithms.** Theorem 4.1 (natural forgetting) and Corollary 5.3 (Hessian-based) each provide explicit upper bounds on post-unlearning excess risk that combine the common continual-learning bound ℰ^{-S_≤t}(λ) from Theorem 3.1 with method-specific unlearning loss terms. This structure makes the interplay between forgetting (controlled by λ) and certifiability (controlled by the sensitivity bound γ_t) explicit and analyzable.

3. **Analysis of second-order advantage and unlearning sequence effects.** Proposition 5.2 gives a second-order approximation bound (depending on squared model differences) that is provably tighter than the first-order bound when errors are below 1. Proposition 5.1 and Lemma 5.4 analyze how the order of unlearning requests affects the approximation error, and Section 5.3 proposes a storage-reduction strategy that combines natural forgetting with selective Hessian corrections, reducing storage to O(max inter-arrival distance × d²).

## Weaknesses

### Major

1. **Notational errors in Theorem 3.1 (excess risk bound).** The bound in Eq. (8) contains terms of the form ρ^{τ_j − τ_j} = 1 multiplied by ‖w_{τ_j}^* − w_{τ_j}^*‖ = 0, and ρ^{τ_k} Σ_{i=2}^k ‖w_{τ_i}^* − w_{τ_i}^*‖ = 0 on the next line. The first double sum Σ_{i=1}^k Σ_{j=2,j≠i}^k ρ^{τ_j−τ_j}‖w_{τ_j}^* − w_{τ_j}^*‖ is identically zero regardless of the data. This suggests a transcription error (likely intended to involve ρ^{τ_j−τ_i}‖w_{τ_j}^* − w_{τ_i}^*‖ or similar). For a theory paper whose contribution rests on formal bounds, such errors in the main theorem statement severely undermine reader confidence. The bound cannot be verified or used as stated.

2. **Incorrect claim about the λ=0 limiting behavior.** Section 4 states that "the unlearning loss' upper bound γ_t(S_{1:t}) approaches zero for λ = 0 and ρ → 0." However, γ_t = (L/λ) Σ Σ ρ^{t−s−n} (Eq. 9). As λ → 0, L/λ → ∞, so the bound does not approach zero — the limit is of the indeterminate form ∞·0 and is not guaranteed to be small. The bound as written is actually problematic at λ=0 because of the 1/λ factor. This is a meaningful gap in the theoretical analysis, and the paper provides no discussion of the range of λ for which the bound is valid.

3. **Experiments do not satisfy the theory's core assumption.** The theory requires μ-strong convexity (Assumption 2.1), but the experiments use cross-entropy loss on a linear softmax model, which is convex but not strongly convex without explicit regularization beyond the ℓ₂ proximal term. The paper notes that it "relax its assumption … to show the more general results under a non-strongly convex setting" but provides no theoretical result for this case. The conclusion then states that "Experiments on MNIST validate our theory" — this is overstated given the assumption mismatch. The experiments are at best suggestive, not validating.

4. **Unlearning model outperforming retraining baseline unexplained.** Table 1 reports that at λ=30, the Hessian-based unlearned model achieves 71.59% test accuracy while the "perfect retraining" model achieves only 71.05%. Since the unlearning algorithm is designed to *approximate* retraining, outperforming it requires explanation (e.g., implicit regularization from the approximate update or noise). The paper offers none ("since it does not rely on forgetting" is not an explanation for *why* it beats the gold standard). This undermines the claim that the algorithm closely approximates retraining.

### Minor

5. **"Gradient-based" framing for Algorithm 1 is imprecise.** The paper states it "adapt[s] gradient-based certified unlearning" and cites Neel et al. (2021), but Algorithm 1 performs no gradient steps for unlearning — it simply adds noise to the current continual learning model w_t, leveraging the natural forgetting from the ℓ₂-regularized updates. The paper itself acknowledges skipping the R_A step, but the framing in the introduction and abstract ("adapt gradient-based unlearning") remains misleading. Algorithm 1 is more accurately described as a Gaussian mechanism applied to the output of a continual learning algorithm.

6. **No uncertainty quantification in experiments.** No error bars, confidence intervals, or multiple-seed results are reported for any experimental number (Fig. 2, Table 1). For a 30-task split of 60k MNIST samples with random task construction and random unlearning sequences, single-run results provide limited evidence.

7. **Derivation of Hessian update (Eq. 13) is sketched but not fully spelled out.** The transition from the Taylor expansion (Eqs. 11-12) to the final update (Eq. 13) is described at a high level. The correction terms for handling unlearning sequence interference are stated without explicit derivation. While the appendix (removed) may contain details, the main text would benefit from a more transparent account of how (13) follows from the expansion.

### Trivial

8. The bound in Theorem 3.1 references ‖w_{τ_i}^*‖ in one term (first line of Eq. 8) but these norms are not defined in terms of any regularization — it is unclear what norm is used and how this term was derived from the ℓ₂-regularized update.

## Nice-to-Haves

- A brief proof sketch in the main text explaining how the forgetting factor ρ = λ/(μ+λ) emerges from the ℓ₂-regularized update would improve readability.
- Comparison to a naïve noise-only baseline (Gaussian mechanism without leveraging forgetting structure) would clarify the value added by the theoretical analysis.
- A discussion of limitations: the assumption of strong convexity, the restriction to ℓ₂-regularized continual learning, the linear model experiments.

## Removed Points

These points were raised by reviewers but are removed or demoted for the following reasons:

- **Claim that experiment contradicts theory (unlearning loss decreases with λ while theory predicts increase):** Removed. The bound in Eq. (9) has both decreasing (1/λ) and increasing (ρ^{…}) factors; the paper does not claim monotonicity. The critic's assertion that "the bound on the unlearning loss should increase" is not supported by the formula itself. The experimental trend (slight decrease from ~0.10 to ~0.08 for natural forgetting) is weak and not clearly in contradiction with any stated theoretical claim.

- **Claim about storage cost not accounting for model differences:** Removed. The paper explicitly states "O(td² + 2td) for storing the Hessian, model updates, and historical unlearning corrections." The 2td term accounts for model differences and corrections.

- **Claim that Theorem 3.1 missing appendix / proof stripped:** Removed per instruction — appendix stripping is a parser artifact, not an author error.

- **Claim about missing related works:** Removed — cannot confirm existence of unmentioned works.

- **Claim that ε,δ definition departs from standard unlearning without justification:** Removed. The definition (Def. 2.1) follows the standard Gaussian-mechanism formulation (Guo et al., 2019; Neel et al., 2021). The comparison of distributions over training+unlearning randomness vs. fixed retrained model is a design choice that is adequately described.

- **Pure formatting/style nitpicks, typo complaints:** Removed per instructions.

## Novel Insights

Beyond the paper's own contributions, the most striking observation is that the paper's core theoretical contributions (Theorem 4.1, Proposition 5.1) each contain the same structural tension: the bounds involve both ρ^{…} (which grows with λ) and 1/λ (which shrinks with λ), meaning the optimal λ for unlearning is neither λ → 0 nor λ → ∞ but some intermediate value determined by the task heterogeneity. This trade-off is structurally novel and provides a genuine insight — that the ℓ₂ regularization strength in continual learning plays opposing roles for learning (preventing forgetting) and unlearning (enabling certification). The notational errors in Theorem 3.1 and the λ=0 claim problem, however, mean that the quantitative bounds cannot be taken at face value and require correction before the trade-off can be reliably analyzed.

## Suggestions

1. **Correct Theorem 3.1.** Fix the indices: ρ^{τ_j−τ_j} should almost certainly be ρ^{τ_j−τ_i} or similar, and ‖w_{τ_j}^* − w_{τ_j}^*‖ should be ‖w_{τ_j}^* − w_{τ_i}^*‖ (or appropriate task-pair distances). The fact that two terms vanish identically in the current formulation must be addressed.

2. **Address the λ→0 issue.** Either remove the claim about the bound approaching zero at λ=0, or replace it with a careful limit analysis showing that lim_{λ→0} γ_t exists and is finite (which would require showing that ΣΣρ^{…} → 0 faster than 1/λ → ∞, which is not obvious).

3. **Run experiments that satisfy strong convexity** (e.g., add explicit ℓ₂ regularization to make the objective strongly convex and report μ), or re-frame the experimental section as illustrative rather than "validating the theory." The current framing overclaims.

4. **Explain the λ=30 result** in Table 1 where the unlearned model beats retraining. Even a brief remark about implicit regularization from the Hessian approximation or noise would help.

5. **Report error bars** (at least 3-5 random seeds) for all experimental numbers, and include the exact unlearning sequences used.

## Score and Decision

**Round 1 bracket:** After reviewing the paper and calibrating against similar papers, I initially bracket the paper between 4.0 and 6.0. The weakest anchors (avg 2.5-3.0) are heuristic unlearning papers without theoretical foundations; the middle anchors (avg 4.5-6.6) are theory papers with some flaws; the strong anchors (avg 8+) have clean theory and extensive experiments. This paper has genuine theoretical contributions but also clear errors in its central theorems.

**Round 2 narrowing:** I examined four anchors in depth for direct comparison:

- **UnCLe (avg 5.75, reject):** Most topically similar work on continual learning + unlearning, but heuristic/empirical without formal guarantees. The current paper has stronger theoretical ambition and formal bounds, placing it slightly above UnCLe in novelty. However, UnCLe has no notational errors in its stated results, while this paper has verifiable errors in Theorem 3.1.

- **"Efficient and Generalizable Second-Order..." (avg 6.00, accept):** Hessian-based certified unlearning paper with clean theoretical analysis. The current paper adds the continual learning dimension (a genuine advance) but has less polished theory and clear errors, making it weaker overall.

- **"The Utility and Complexity..." (avg 6.60, accept):** Strong theoretical paper with rigorous analysis. The current paper is substantially weaker — not due to the problem novelty but due to presentation issues and errors in the main theorems.

- **"Primal-Dual Continual Learning" (avg 5.00, reject):** Continual learning theory paper with some notational issues and limited experiments. Comparable quality level to the current paper, but the current paper tackles a more novel problem (unlearning + continual learning), giving it an edge in originality.

The paper is closest to the 5.0-5.75 range. It has a clear novelty advantage over UnCLe (5.75) due to theoretical contributions, but the errors in Theorem 3.1 and the λ=0 claim are genuine issues that a reviewer would weigh against acceptance. I place it slightly below UnCLe's 5.75 but above the 5.00 anchor, settling at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>