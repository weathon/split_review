Now I have all the information needed. Let me synthesize the final consolidated review.

## Summary

This paper addresses three limitations in subspace inference for Bayesian neural networks: subspace construction, evaluation, and inference efficiency. It proposes (1) block-averaging (BA) as a subspace construction method that better approximates the full SGD trajectory than the existing tail-trajectory method at the same memory cost, (2) Bayes factor and evidence-ratio metrics for directly evaluating subspace quality, and (3) randomized quasi-Monte Carlo importance sampling (RQMC-IS) for efficient posterior predictive inference in low-dimensional subspaces. Experiments on UCI regression and CIFAR classification show that BA consistently outperforms TT, and that RQMC-IS achieves competitive predictive accuracy with fewer forward passes than MCMC or VI.

## Strengths

- **Block-averaging demonstrably improves subspace quality at equal memory cost.** Table 1 quantifies this via angular distances: BA with M=20 has ~23° to the full-trajectory (FT) subspace vs. ~80° for TT. Tables 4–6 show BA yields better test log-likelihood and classification accuracy on UCI and CIFAR datasets. This is a clear, practical improvement over the existing TT baseline.

- **The evaluation framework (Bayes factor and evidence ratio) provides principled, direct subspace quality assessment.** Figures 3 and Tables 3a/3b consistently show strong evidence favoring BA over TT across synthetic and UCI data. While these are standard Bayesian quantities, their application to *subspace evaluation* before performing inference is a sensible contribution that the community has overlooked.

- **RQMC-IS is computationally efficient for low-dimensional subspaces.** Table 2 shows RQMC-IS with N=1024 achieves RMSE 0.031, competitive with VI (0.024) and better than ESS (0.038), while using far fewer forward passes. Theorem 2 provides a theoretical convergence guarantee (O(N^{-1+ε})), though subject to smoothness conditions.

- **Identifies the overlooked induced-prior issue.** Section 3.2 correctly points out that existing subspace inference methods manually choose the prior on z without accounting for the correspondence between p_W(w) and p_Z(z). This is a principled correction in the subspace inference pipeline.

## Weaknesses

### Fatal
None.

### Major
- **The CIFAR experiments lack the FT baseline, weakening the central claim in the most challenging setting.** The paper acknowledges FT is infeasible on CIFAR, but this means the strongest experiments compare only BA vs. TT without any reference to the gold standard. The inference that BA≈FT on CIFAR relies on extrapolation from lower-dimensional synthetic/UCI results. A reader cannot rule out that BA and TT are both poor relative to an alternative construction method on CIFAR. This is the most significant limitation.

- **The inference cost comparison (Table 2) oversimplifies the computational burden of MCMC and VI.** Measuring cost purely by number of forward passes ignores ESS burn-in (which can be substantial) and VI gradient evaluations. Treating every ESS forward pass as equally informative for prediction inflates its effective cost, while treating VI's 5K forward passes as directly comparable to RQMC-IS's 1K ignores that VI also requires gradient backpropagation. A fairer comparison would report wall-clock time or effective sample size.

### Minor
- **The novelty of block-averaging is overstated.** BA is a straightforward averaging operation — partitioning a trajectory into M blocks and taking the mean of each. The paper calls it "novel" without establishing why this specific downsampling is theoretically superior to alternatives (e.g., systematic thinning, stratified selection) or analyzing what properties of the trajectory are preserved or lost. The contribution is empirical, not methodological.

- **The Bayes factor and evidence-ratio metrics are standard Bayesian model comparison tools applied to a new context, not novel metrics.** The paper claims "there are currently no metrics designed to directly evaluate how well the subspace represents the data-relevant portions of the full parameter space," but applying textbook marginal-likelihood ratios to subspaces is a natural translation rather than a novel invention. The contribution lies in recognizing their applicability, not in creating new methodology.

- **The induced prior p_Z(z) used in experiments is never explicitly specified.** The paper criticizes prior work for manually choosing the prior on z (Section 3.2) and correctly argues that the induced prior from p_W(w) should be used, but it never states what p_Z(z) is in its own SNIS/RQMC-IS estimators (Equation 9 uses p_Z(Z_i) without definition). The observation that projected weights have empirical mean 0 and covariance I_k (line 178) suggests N(0,I_k), but this is an empirical observation about the proposal, not a specification of the prior. This is a reproducibility gap.

- **No sensitivity analysis for the number of blocks M or subspace dimensionality k.** All experiments fix M=20, and k is not stated in the main text. The paper provides no guidance on how to choose these hyperparameters or evidence that performance is robust to their values.

- **Missing comparison with other subspace construction methods.** The related work mentions random subspaces (Li et al., 2018), last-layer subspaces (Kristiadi et al., 2020), and sparsity-based methods (Daxberger et al., 2021b), but the experiments compare BA only against TT and (where feasible) FT. Including even one alternative construction method would better establish whether BA is generally superior.

- **Theoretical convergence guarantees (Theorem 2) may not hold for neural network likelihood surfaces.** The O(N^{-1+ε}) rate requires smoothness conditions on the integrand p_Z(D'|z)p_Z(D|z)p_Z(z)/q(z). The paper does not verify whether these hold for the highly non-convex likelihood surfaces of neural networks, making the rate more aspirational than guaranteed in practice.

### Trivial
None.

## Nice-to-Haves
- An analysis of *why* BA approximates FT better (e.g., showing eigenvectors of BA covariance converge to those of FT under ergodicity assumptions on the SGD trajectory).
- Showing that the Bayes factor/evidence ratio metrics can be computed cheaply enough to *guide* subspace selection before performing full inference.
- Including a wall-clock time comparison for the inference methods rather than only counting forward passes.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Circularity of Bayes factor evaluation* (Harsh Critic, Issue 2): The critic claimed that computing Bayes factors requires inference, creating circularity. This is incorrect — the Bayes factor is a prior predictive quantity, not a posterior quantity. Computing ∫ p_Z(D|z) p_Z(z) dz does not require posterior inference.
- *Assumptions not stated in main text for Theorem 2*: The paper references Assumption 3 and 4, which are in the appendix (stripped by the parser). The substantive point about smoothness not holding for neural networks is preserved above.
- *k not stated / VI implementation details missing*: These details are likely in the appendices (B, C, D) which the parser strips.
- *Strength Finder's generic strengths* ("this paper addressed an important problem"): Removed for lacking specific content.
- *Demand for comparison with non-PCA subspace methods as a core weakness*: The paper scopes itself to PCA-based trajectory subspaces; demanding random/last-layer/sparse baselines is a wishlist item, not a flaw.

## Novel Insights

The most interesting observation — not made explicitly by the paper — is that block-averaging works well because it acts as a variance-reduced estimate of the trajectory covariance. The tail trajectory uses the last M raw points, which are highly correlated and capture only the terminal oscillation region of SGD. Block-averaging, by contrast, spreads M representative points across the entire trajectory, effectively performing stratified sampling of the trajectory's covariance structure. This explains why BA's eigenvectors resemble FT's (Table 1) while TT's are nearly orthogonal: BA's block centers decorrelate the trajectory samples. This insight suggests that any trajectory sub-sampling strategy that reduces autocorrelation (e.g., systematic thinning with a gap, or selecting points at quantiles of the loss) might achieve similar benefits — an avenue the paper does not explore but that would be a natural follow-up.

## Suggestions

1. **Downgrade novelty claims in framing.** Present BA as "an effective practical alternative to TT" rather than "novel." The empirical evidence speaks for itself.
2. **Specify the prior p_Z(z) explicitly.** State whether it is N(0, I_k) — induced from a N(0, I_d) prior on w via the orthogonal projection — or something else. This is essential for reproducibility.
3. **Add an ablation on M and k** in the main paper or appendix, showing sensitivity (or insensitivity) of BA performance to these choices.
4. **Acknowledge the cost comparison caveats explicitly.** Add a sentence noting that ESS typically requires warm-up iterations not counted here, and that VI requires gradient computations whose cost differs from forward-pass-only methods.
5. **Include at least one alternative subspace baseline** (e.g., random subspace) on the UCI experiments to broaden the comparison.

## Score and Decision

The paper presents solid empirical contributions to subspace inference for BNNs. The core claims are supported by evidence, the experiments are reasonably thorough, and the weaknesses (overclaimed novelty, missing FT baseline on CIFAR, simplified cost comparison) are addressable with framing revisions rather than fatal. The paper provides practical value to the subspace inference community and the results are reproducible in principle once the prior on z is clarified.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>