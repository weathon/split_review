Here is my final consolidated review, synthesized after cross-checking the paper against all reviewer claims.

---

## Summary

This paper proposes modeling TD errors in deep RL with the Generalized Gaussian Distribution (GGD) instead of the standard Gaussian, adding a β-head (shape parameter) to capture kurtosis and tail behavior. The authors augment the actor-critic loss with risk-averse weighting (ω^RA = Q^β_t) and a Batch Inverse Error Variance (BIEV) regularization term. Experiments on MuJoCo and discrete control tasks with SAC and PPO show that GGD-based variants consistently outperform variance-network (Gaussian NLL) baselines, with more stable parameter estimation.

## Strengths

1. **Novel and well-motivated application of GGD to TD error modeling.** The paper identifies a real limitation of Gaussian error assumptions in TD learning—heavy tails that evolve during training—and provides empirical evidence of non-normality (Figure 1). Replacing the Gaussian with a GGD that adapts per-sample tail behavior is a principled and computationally lightweight idea (one extra head).

2. **Consistent empirical gains over variance-network baselines across multiple settings.** In all six MuJoCo environments (SAC, Figure 2) and across both continuous and discrete control tasks (PPO, Figure 5), GGD variants match or exceed their variance-head counterparts. The improvements are particularly visible where variance heads degrade performance (e.g., HalfCheetah-v4, Hopper-v4), suggesting the method is more robust.

3. **More stable parameter estimation.** Figure 3 shows that the coefficient of variation of β estimates is consistently lower and more stable than that of variance estimates, supporting the claim that the GGD head yields more reliable uncertainty estimates than a Gaussian variance head.

4. **Theoretical scaffolding.** The connection to second-order stochastic dominance (Theorem 2) provides a principled basis for the risk-averse weighting scheme, and the discussion of kurtosis-induced bias in variance estimation (Proposition 1) correctly identifies a genuine statistical issue in variance-network training.

## Weaknesses

### Major

1. **Missing standard SAC/PPO baselines (without any uncertainty head).** The paper compares GGD variants exclusively against variance-network (GD) baselines. It acknowledges (Figure 2, line 315) that variance heads *degrade* performance in several environments relative to what one would expect. Since the abstract and title claim "significant performance improvements" broadly, the reader cannot tell whether GGD is recovering performance lost by the variance head or truly improving over standard SAC/PPO (which use plain MSE loss and no variance head). Standard SAC/PPO are the de facto reference practitioners will care about, and their omission weakens the practical significance claims.

2. **The α=1 simplification is not adequately justified.** The paper fixes the GGD scale parameter α=1 and models only β. The claim that "moments influenced by α can also be represented by β" (Remark 2.3) is unsupported: with α=1, variance = Γ(3/β)/Γ(1/β), coupling scale and shape so that one cannot independently control spread and tail behavior. Real TD error distributions may require both. The paper mentions an ablation study on integrating the α head (line 356, deferred to appendix), which suggests the authors are aware of the issue, but the main text offers no evidence (or a rigorous counterargument) that α is dispensable. This limitation undercuts the claim to be modeling the *generalized* Gaussian—the method uses a one-parameter subclass, not the full GGD family.

### Minor

3. **Theorem 1 is imprecisely framed.** The paper states "The NLL of GGD is well-defined for β∈(0,2]" and cites positive-definiteness of the characteristic function. In fact, the GGD PDF is a valid density (positive, integrates to 1) for *all* β>0, so the NLL is well-defined as a loss function for any β>0 regardless. The positive-definiteness property discussed is about characteristic functions, not about the NLL being valid. The practical method is unaffected, but the theoretical framing is misleading.

4. **The risk-averse weighting using β as a multiplicative weight (ω^RA_t = Q^β_t) needs better justification.** The GGD NLL already contains β in the exponent (|δ|^β) and in log terms. Weighting by β across the batch on top of this is a separate mechanism that the paper motivates via stochastic dominance (Theorem 2), but the interaction between the likelihood structure and the batch-level weighting is not analyzed. The critic's concern about "double usage" is reasonable—the paper should explain why the likelihood's own β-dependence is insufficient.

5. **BIEV notation (V[δ_t]) is underspecified.** The paper defines ω^BIEV_t = 1/(V[δ_t] + ξ) but does not explicitly state whether V[δ_t] is the variance of TD errors across the 5 ensemble members (the natural reading from the BIV analogy) or something else. The context (V[Q^μ_t] in BIV, the ensemble size of 5, Bessel's correction discussion) makes the across-ensemble interpretation clear, but a precise definition would improve reproducibility.

6. **No trace plots or summary statistics of learned β values.** The paper claims β estimates "mostly converge within [0,2]" (line 52) and shows only coefficients of variation (Figure 3), which give no information about the actual value range or trajectories of β during training. Without this, the claim about convergence and alignment with Theorem 1's range is not verifiable from the presented data.

7. **No quantitative goodness-of-fit measures for TD error distributions.** Figure 1 shows fitted PDFs qualitatively, but the claim of "substantial deviations from Gaussian" would be substantially strengthened by quantitative measures (e.g., estimated kurtosis, log-likelihood ratios vs. Gaussian, Kolmogorov-Smirnov statistics) across multiple environments and algorithms.

### Trivial

None.

## Nice-to-Haves

- Adding standard SAC/PPO baselines would immediately strengthen the practical significance claims.
- A single-critic (or 2-critic, as in standard SAC) ablation would clarify whether the benefit of GGD is contingent on the ensemble of 5 critics.
- Brief trace plots of β during training (in the main text or appendix) would support the claim about convergence within (0,2].
- Statistical significance tests or confidence intervals on final performance would help assess which differences are meaningful given seed variance.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after cross-checking against the paper:

- **Criticism that BIEV is "ill-defined" and "not reproducible":** Removed. The notation V[δ_t] naturally inherits the same interpretation as V[Q^μ_t] (variance across the ensemble), which is explicitly described as "empirical variance" with Bessel's correction over the ensemble of 5. The per-sample subscript t rules out the batch-variance misinterpretation. The method is operational as described.
- **Criticism that the MBBE theory is disconnected from BIEV:** Downgraded from a claimed structural flaw to a minor observation. Proposition 3 is used to motivate why better variance estimation matters, and BIEV applies the insight by using error variance rather than value variance. The connection is plausible, not proven, which the paper acknowledges.
- **Criticism about ablation studies being deferred to the appendix:** Removed per hard rule (the parser strips appendix content; the ablation study exists in the original submission).
- **Criticism about the 5-ensemble setup not being standard:** Removed. All methods use the same ensemble; comparisons are fair. Asking for single-critic results is a reasonable extension but not a flaw in the current comparison.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Removed for lacking specific content or conflicting with verified weaknesses.

## Novel Insights

The cross-reviewer synthesis surfaces a tension that neither reviewer fully articulates: the paper's two main technical innovations—modeling kurtosis via β and regularizing via BIEV—pull in opposite directions. The β head explicitly models heavy tails and assigns higher weight to less spread-out samples (risk-averse), while BIEV down-weights high-variance samples for epistemic robustness. These are both forms of sample reweighting, but they operate on different signals (β vs. δ variance). Understanding when these mechanisms reinforce, trade off, or conflict would deepen the contribution. The paper does not analyze this interaction.

## Suggestions

1. Add standard SAC (MSE loss, no variance head) and standard PPO as baselines to all main learning curves. This is the single change that would most strengthen the paper.
2. Either add an α head and show whether it helps, or provide a rigorous theoretical or empirical argument (not just a claim) that fixing α=1 is harmless. The ablation study in the appendix should be reported in the main text.
3. Clarify the definition of V[δ_t] in the BIEV weight by writing, e.g., "the empirical variance of the TD error δ_t across the K=5 ensemble critics" or adding a sentence of pseudocode.
4. Replace or supplement Theorem 1's discussion: state clearly that the GGD PDF is valid for all β>0, and reposition the positive-definiteness reference as a property of the characteristic function (which may be relevant to a different theoretical claim).
5. Report at least a summary of learned β values (mean ± std across seeds, or trace plots) to substantiate the claim about convergence within (0,2].

## Score and Decision

The paper introduces a sensible and well-motivated technique with consistent empirical support across multiple domains and algorithms. However, two issues prevent stronger endorsement: (a) the absence of standard SAC/PPO baselines leaves the practical significance claims incompletely supported, and (b) the α=1 simplification is asserted without rigorous justification. These are addressable but non-trivial gaps. The theoretical framing of Theorem 1 is imprecise, though the method itself is unaffected.

**Score: 6.0 / 10** — A solid technique with clear promise, but with significant evidential gaps that must be closed before the contribution can be fully assessed.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>