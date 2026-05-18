Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper introduces Kernel Banzhaf, a linear-regression-based estimator for Banzhaf values. Its core contribution is Theorem 3.2, which establishes that Banzhaf values for any set function are the exact solution to a specific least-squares problem over all $2^n$ subsets. The paper then subsamples this regression problem via uniform leverage-score sampling (with paired sampling) to produce a practical estimator, provides theoretical sample-complexity guarantees, and empirically demonstrates superior accuracy over Monte Carlo and MSR baselines across eight datasets.

## Strengths

**1. Novel and clean linear regression formulation.** Theorem 3.2 establishes for the first time that Banzhaf values for *general* set functions are the solution to an unweighted least-squares problem where $\mathbf{A}$ has rows $\frac{1}{2}\mathbf{z}^\top$ and $\mathbf{b}$ is $v(\mathbf{z})$. This goes beyond prior work that only covered binary simple set functions (Hammer & Holzman, 1992) and is the essential theoretical foundation for the entire algorithm. The proof is elementary (lines 94–112) and correct.

**2. Strong and consistent empirical accuracy.** In Figure 2, Kernel Banzhaf (with and without paired sampling) achieves lower $\ell_2$-norm error than MC and MSR across all eight datasets and all sample sizes. These comparisons use exact Banzhaf values computed via the tree algorithm of Karczmarz et al. (2022), which is a more rigorous evaluation than prior work's convergence-only metrics. The paper also shows superior robustness to additive noise (Figure 3) and better numerical conditioning (Figure 5).

**3. Principled experiment design with ground-truth evaluation.** Unlike prior work that only measured convergence, the paper computes exact Banzhaf values for tree-based models (via Karczmarz et al., 2022) and directly measures $\ell_2$-norm error. This makes the empirical claims substantially more credible.

## Weaknesses

### Fatal

None.

### Major

**1. Unsubstantiated theoretical guarantee for Algorithm 1 with paired sampling.** Theorem 3.3 is stated as applying to Algorithm 1, which uses paired sampling (each $\mathbf{z}$ and its complement $\bar{\mathbf{z}}$ are included together). The paper explicitly acknowledges (line 157) that this "requires completely reproving it from scratch because of the incorporation of paired sampling" — and then does not provide that proof, nor even a sketch of why the standard leverage-score analysis (which assumes independent draws) holds for deterministically paired rows. The claim that Theorem 3.3 applies to the actual algorithm is therefore unsubstantiated. The paper should either (a) provide the proof for the paired-sampling case, (b) state the theorem only for the unpaired variant (which is already evaluated as "Kernel Banzhaf (Excluding Pairs)" in the experiments), or (c) clearly demote this to a conjecture.

**2. Inconsistency between Theorem 3.3 and the proof of Corollary 3.4.** Theorem 3.3 states $\|\mathbf{A}\hat{\phi}-\mathbf{A}\phi\|_2 \leq (1+\epsilon)\|\mathbf{A}\phi-\mathbf{b}\|_2$. The proof of Corollary 3.4 (line 190) uses the assumption $\|\mathbf{A}\hat{\phi}-\mathbf{A}\phi\|_2^2 \leq \epsilon\|\mathbf{A}\phi-\mathbf{b}\|_2^2$. Squaring Theorem 3.3 gives $(1+\epsilon)^2$, not $\epsilon$ — these are different. The corollary would claim $\|\hat{\phi}-\phi\|_2^2 \leq \epsilon\gamma\|\phi\|_2^2$, but the actual bound that follows from Theorem 3.3 is at most $(1+\epsilon)^2\gamma\|\phi\|_2^2$. This is not a typo; it affects the quantitative guarantee. The paper must reconcile this mismatch — either Theorem 3.3 should state $\epsilon$ instead of $1+\epsilon$ (which would align with standard leverage-score results), or the Corollary proof needs revision.

These two theoretical issues together mean that the paper's central theoretical claims — a $(1+\epsilon)$-type residual bound from Theorem 3.3 (unproven for the paired algorithm) and the $\ell_2$-norm error bound in Corollary 3.4 (inconsistent with Theorem 3.3 as stated) — are not currently sound. The theoretical contribution of the paper is significantly weakened as a result.

### Minor

**3. Neural network evaluation is not shown.** The paper states (line 213) that it also evaluates on neural networks using small datasets where Equation 2 gives exact Banzhaf values, but no results are presented in the main paper. While the tree-model experiments are the primary evaluation (because exact Banzhaf values require a specialized algorithm), showing at least one neural-network result would substantially strengthen the claim of general applicability.

**4. The $\mathbf{K}$ matrix definition is unnecessarily confusing.** The paper defines $\mathbf{K} = (\mathbf{A}^\top\mathbf{A})^{-1/2}\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}(\mathbf{A}^\top\mathbf{A})^{1/2}$, which is non-symmetric in general. However, due to Observation 3.1 ($\mathbf{A}^\top\mathbf{A} = 2^{n-2}\mathbf{I}$), the factors are scalars and $\mathbf{K} = \tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$, which is symmetric. The paper should either note this simplification or define $\mathbf{K}$ in the standard symmetric form $(\mathbf{A}^\top\mathbf{A})^{-1/2}\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}(\mathbf{A}^\top\mathbf{A})^{-1/2}$ to avoid confusion — especially since Figure 5 compares condition numbers across Kernel Banzhaf, KernelSHAP, and Leverage SHAP, and the latter two do *not* have $\mathbf{A}^\top\mathbf{A} \propto \mathbf{I}$.

### Trivial

- The "larger magnitude, and hence high variance" justification for MSR's weakness (line 233) is intuitive but the paper does not formalize why regression avoids this issue beyond the condition-number argument.
- The additive Gaussian noise model (Figure 3) is a standard but artificial proxy. This does not weaken the results but a brief discussion of limitations would be appropriate.

## Nice-to-Haves

- A discussion of why the Banzhaf regression avoids the variance issues of MSR beyond appealing to condition numbers would strengthen the methodological story.
- A note on whether the normalized error metric (dividing by $\|\phi\|_2^2$) is comparable across Banzhaf and Shapley regimes, since Banzhaf and Shapley values have different intrinsic scales.
- A lower bound discussion that goes beyond the $\Omega(n)$ argument for linear set functions to better support the claimed near-optimality.

## Removed Points

- *"The matrix K is non-symmetric ... condition number of a non-symmetric matrix captures different geometry"* — Removed because $\mathbf{A}^\top\mathbf{A} = 2^{n-2}\mathbf{I}$ (Observation 3.1), so both factors are scalar and $\mathbf{K} = \tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$, which is symmetric. The reviewer missed this simplification.
- *"The noise is artificial"* complaint beyond what is kept above — Additive Gaussian noise is a standard stress test; the paper's finding that Kernel Banzhaf degrades more gracefully is still meaningful.
- *"Missing related works"* — This would require external knowledge I cannot verify.
- *"Formatting/style nitpicks"* — Standard removal per instructions.
- *"Not yet released / cannot be independently verified"* complaints about any cited method — Per instructions, cited entities are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The core insight — that Banzhaf values are solutions to an unweighted least-squares problem over $\{-1/2, 1/2\}$-valued rows — is already the paper's main intellectual contribution and is correctly identified as such.

## Suggestions

1. **Fix the Theorem 3.3 / Corollary 3.4 inconsistency.** The simplest fix is to change Theorem 3.3's $(1+\epsilon)$ to $\epsilon$ (which matches the standard leverage-score sampling guarantee and aligns with the Corollary proof), with the understanding that $\epsilon$ is then the relative error on the residual norm. Alternatively, revise Corollary 3.4 to correctly propagate $(1+\epsilon)^2$.

2. **Either prove the paired-sampling guarantee or restate Theorem 3.3 for the unpaired variant.** The paper should not claim a theoretical guarantee for an algorithm when the analysis framework does not apply and the proof is not provided. One clean option: state Theorem 3.3 for the unpaired version (which inherits the standard uniform leverage-score analysis), present paired sampling as a heuristic enhancement with empirical support, and note that a rigorous analysis of paired sampling is left as future work.

3. **Show at least one neural-network result.** Even a small-scale experiment ($n \leq 12$, where brute-force enumeration is feasible) with a neural network would directly support the claim of general applicability and address the most natural concern about the evaluation scope.

## Score and Decision

This paper has a novel and correct core idea (the linear regression formulation of Banzhaf values, Theorem 3.2) and strong empirical results demonstrating practical superiority over existing Banzhaf estimators. However, the theoretical contribution — a central selling point — has two concrete problems: (a) Theorem 3.3 is claimed for the paired-sampling algorithm without proof, and (b) the Corollary 3.4 proof is inconsistent with Theorem 3.3 as stated. These issues are fixable (reparameterizing Theorem 3.3 and either proving or scaling back the paired-sampling guarantee), but in their current form they mean the paper's theoretical claims are not internally consistent or fully substantiated. The empirical work is sufficiently strong that the paper still has real value, but the theoretical gaps prevent acceptance at the level claimed. A major revision addressing these issues could make this a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>