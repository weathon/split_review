- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5
Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces diffusion Thompson sampling (dTS), a framework that uses a pre-trained diffusion model as a prior over action parameters in contextual bandits. The key algorithmic contribution is an efficient posterior approximation that enables fast sampling and updating — becoming exact when the diffusion model and reward likelihood are both linear. The paper provides a Bayes regret bound for linear instances and evaluates dTS on synthetic and semi-synthetic problems (Swiss roll, MovieLens), showing consistent improvements over LinTS, LinUCB, GLM-TS, and other baselines.

## Strengths

- **First Bayes regret bound for diffusion-model–based Thompson sampling in contextual bandits** (Theorem 4.1, Eq. 13). Under linear rewards and linear diffusion link functions, the bound quantifies how the hierarchical latent structure affects regret, and the paper provides a sparsity-aware variant (Proposition 4.2) that yields cleaner dependence. This is a genuine theoretical advance over Hsieh et al. (2023), who studied only multi-armed bandits without guarantees.

- **Closed-form exact posteriors under linear diffusion and linear rewards** (Section 3.1). The paper shows that when both the diffusion link functions and the reward model are linear, the posterior remains a diffusion model with updated parameters. This exact tractability motivates the efficient approximation for the non-linear case and enables the theoretical analysis.

- **Robustness to reward-model misspecification** (Fig. 2, second and fourth columns). dTS variants that use the correct diffusion prior but the *wrong* reward distribution (linear-Gaussian instead of logistic-Bernoulli) still outperform baselines with the correct reward model but no diffusion structure (GLM-TS, UCB-GLM). This provides compelling evidence that capturing latent action correlations can matter more than an exact reward specification.

- **Comprehensive empirical validation.** Experiments span linear/non-linear diffusion, linear/logistic rewards, varying dimensions (d=5,20), action spaces (K=10–5×10⁴), diffusion depths (L=2–40), pre-training sample sizes, and prior misspecification. The Swiss roll and MovieLens experiments demonstrate that dTS works even when the true data-generating process is not a diffusion model.

## Weaknesses

### Fatal
None.

### Major

- **The Bayes regret bound suffers from exponential dependence on the number of diffusion layers L, severely limiting its practical relevance.** The bound in Theorem 4.1 contains the term σ_MAX^{2ℓ}, which grows exponentially with layer index ℓ. For a realistic diffusion model with L=40 (as used in the Swiss roll experiment, Fig. 4b), σ_MAX^{2L} would be astronomically large unless the per-layer variances are tiny — making the bound vacuous for exactly the models that drive the empirical results. The paper discusses this (Section 4.1, "Why the bound increases with L?") and provides illustrative mitigation scenarios (decreasing variances, rapid dimension reduction), but these are special cases, not generic. The bound's looseness for practical depths is a structural limitation of the analysis, not merely a notational one. This weakens the theoretical contribution considerably: the bound provides conceptual insight but cannot explain the regime where dTS performs well empirically.

### Minor

- **The derivation of the recursive posterior approximation formulas (Eqs. 11–12) is not shown.** The paper states the recursive formulas for Ḡ_{t,ℓ} and B̄_{t,ℓ} without explaining how they follow from the hierarchical model when the link functions f_ℓ are non-linear. While the equations are explicitly written, a reader trying to implement or extend dTS would need to reconstruct the derivation. The paper references an appendix experiment validating the approximation, but the derivation itself is missing. This is a reproducibility concern.

- **The computational efficiency framing is somewhat misleading.** The paper contrasts dTS's O((L+K)d³) complexity against O(K³d³) for maintaining a full joint posterior — a straw-man baseline that no sensible algorithm would use. The natural computational comparison is LinTS (O(Kd³)), which the paper acknowledges but only *after* leading with the K³ comparison. dTS's real advantage over LinTS is *statistical* (sharing information across actions via the latent structure), not computational. The paper should reframe this discussion to avoid overstating the computational claim.

- **No comparison to other structured bandit approaches.** Methods such as latent-factor Thompson sampling, clustering bandits, or hierarchical Bayesian models that also exploit cross-action correlations are not discussed or compared. While the paper focuses on diffusion models as a specific framework, a discussion of how dTS relates to these alternatives would better contextualize the contribution.

### Trivial
None.

## Nice-to-Haves

- A wall-clock time comparison between dTS and LinTS for varying K would cleanly separate the computational and statistical claims.
- Including a small 1D/2D experiment in the main paper comparing the approximate posterior against an MCMC gold standard (rather than deferring to an appendix) would strengthen the reader's confidence in the approximation for non-linear f_ℓ.
- The bound's exponential L-dependence could be explicitly marked as an analysis artifact (e.g., "a limitation of our analysis technique") to prevent over-interpretation.

## Removed Points

- *"The paper provides no evidence that the approximation is faithful: no comparison to an exact (or MCMC-based) posterior, no diagnostic of approximation error."* — **Removed** because the paper states (line 122) that "3 provides an experiment demonstrating that this approximation closely matches the exact posterior in that setting," referencing an appendix that exists in the original submission. The claim of "no evidence" is factually incorrect. The broader algorithmic concern about the derivation being underspecified is retained above as a Minor weakness.

- *Strength: "Computational efficiency compared to naive joint posterior maintenance"* — **Removed** because this strength conflicts with the verified weakness that the computational framing is overstated. The weakness wins per the filtering rules.

- *"The bound itself says that, ceteris paribus, regret grows exponentially with depth. This is a structural weakness of the analysis: it suggests the bound is extremely loose (since practical diffusion models with L=40 would have completely vacuous terms unless variances are tiny)… The paper does not adequately confront this."* — This criticism is **partially removed** in its stronger form. The *fact* of exponential dependence is kept as a Major weakness, but the sub-claim that the paper "does not adequately confront this" is weakened: the paper does discuss the L-dependence (lines 149–155, Section 4.1), explains why it arises, and provides mitigating scenarios. The retained weakness acknowledges the discussion but notes it does not resolve the underlying looseness.

- *"The 'joint posterior' comparison is a straw man."* — **Partially removed.** The paper *does* acknowledge LinTS's computational efficiency and frames dTS's advantage as primarily statistical. The retained weakness (above) reflects this nuance: the framing could be clearer, but it is not a straw man.

- *Removed strengths from Strength Finder:* "Computational efficiency compared to naive joint posterior maintenance" — conflicting with the verified weakness. Also removed generic phrasing from strengths that are too vague to anchor.

## Novel Insights

The reviewers' perspectives reveal a paper with solid contributions (novel algorithm, strong empirical results, non-trivial theoretical analysis) whose main weakness is a mismatch between its theoretical and empirical strengths. The regret bound is a genuine technical achievement — it is the first such bound for diffusion-model-based TS in contextual bandits — but its exponential L-dependence means it cannot explain the regime where dTS actually excels (deep, non-linear diffusion models). Meanwhile, the empirical evaluation is the paper's strongest asset: the misspecification experiments (Fig. 2) and the widening gap with K (Fig. 3a) convincingly demonstrate that latent structure matters more than exact reward specification, which is an interesting finding in its own right. The paper is best understood as an empirical/algorithmic contribution supported by a partially-tight theoretical analysis, not as a fully resolved theoretical treatment.

## Suggestions

1. Add a brief derivation or intuition for the recursive formulas (Eqs. 11–12) — even a sentence explaining the algebraic steps — to improve reproducibility.
2. Reframe the "computational benefits" paragraph to lead with the *statistical* advantage over LinTS and present the O(K³d³) comparison as a secondary illustration of what is avoided, not a primary selling point.
3. In the regret bound discussion, explicitly state the bound's looseness for deep models as a limitation of the analysis technique, and characterize conditions under which it is tighter (building on the already-present sparsity/dimension-reduction discussion).
