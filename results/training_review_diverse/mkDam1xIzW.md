Now I have all the information I need to produce the final consolidated review. Let me carefully apply the rules to each point raised by the reviewers.

---

## Final Consolidated Review

## Summary

This paper introduces Probabilistic Geometric Principal Component Analysis (PGPCA), a generalization of PPCA that models data distributed *around* a nonlinear manifold (rather than exactly *on* it) by incorporating a local distribution coordinate system. The authors derive an EM algorithm where the M-step updates for the loading matrix C and noise variance σ² reduce to PPCA-like closed forms through a summary matrix Γ(q), and they introduce both Euclidean (EuCOV) and geometric (GeCOV) distribution coordinate systems. Experiments on simulated loop/torus manifolds and real mouse head-direction neural data show that PGPCA achieves higher log-likelihoods than PPCA/FA and can distinguish between coordinate systems via likelihood comparison.

## Strengths

1. **Principled generalization of PPCA to nonlinear manifolds with explicit noise modeling**: PGPCA replaces PPCA's Euclidean-space mean with a manifold φ(z) and incorporates a local orthonormal coordinate system K(z) (Eq. 1), explicitly modeling data that deviates from the manifold with both structured deviation (via C) and isotropic noise (σ²). Setting φ(z)=0 and K(z)=I exactly recovers standard PPCA (Section 3.1), making this a proper generalization rather than an ad-hoc extension. This directly addresses a gap left by prior nonlinear PPCA extensions (PPGA, Torus PPCA) that require data to lie precisely *on* the manifold.

2. **Analytical EM algorithm with closed-form M-step in the style of PPCA**: The paper derives a compact form for the ELBO (Eq. 13) where all information about the nonlinear manifold and distribution coordinate is summarized into a single matrix Γ(q). This enables closed-form updates for C (via eigendecomposition of Γ(q)) and σ² (Eqs. 14‑15) that mirror PPCA's structure, with empirical convergence within ~40 iterations (Figure 2C). The fact that the PPCA solution structure emerges despite the nonlinear manifold is a nontrivial theoretical insight.

3. **Introduction of geometric vs. Euclidean distribution coordinates with empirical differentiation**: The paper constructs a geometric coordinate system (GeCOV) aligned with the manifold's tangent and normal spaces, and shows that in both simulations (paired t-test p < 1.7e‑12, Figure 2B) and real neural data (Figures 4B, 4D), the correct coordinate system yields reliably higher log-likelihoods. This provides a principled way to test which coordinate system better captures the data distribution — a capability no prior PPCA extension offers.

4. **Robust empirical validation across multiple manifold types and settings**: The method is tested on 1D loops (in ℝ² and ℝ¹⁰), a 2D torus, and real neural data from two mice, with both given and learned manifold-state distributions p(z). PGPCA consistently outperforms PPCA and FA in log-likelihood (Table 2), and the learned distributions visually match the true ones (Figure 2A).

## Weaknesses

### Fatal
None.

### Major

1. **"Hypothesis testing" framing is substantially overstated throughout the paper.** The abstract, introduction, Section 4, and conclusion repeatedly describe PGPCA as performing "hypothesis testing" to distinguish distribution coordinates. What is actually done is fitting two models (GeCOV vs. EuCOV) and comparing their log-likelihoods — this is model comparison, not hypothesis testing in the formal statistical sense. There is no null distribution, no test procedure with known sampling properties for the coordinate-selection decision on a new dataset, and no correction for model complexity. While paired t-tests are reported for the *simulation* setting (comparing repeated draws), this confirms empirical reliability of the likelihood ordering, not a formal test procedure. The pervasive use of "hypothesis testing" for what is likelihood-based model selection is misleading and should be rephrased to "model comparison" or "coordinate selection via log-likelihood."

2. **The geometric coordinate system (GeCOV) is not formally defined.** The paper claims to "derive" GeCOV and Figure 1 illustrates the idea (tangent/normal vectors for a loop; two tangent vectors plus a normal for a torus), but no formal mathematical definition is provided. For reproducibility, the paper should specify how K(z) is constructed from the manifold's tangent space — e.g., via the Jacobian of φ or an orthonormal basis of the normal bundle. A reader cannot implement or evaluate GeCOV based on the current description.

### Minor

3. **No evaluation of sensitivity to manifold estimation quality.** PGPCA takes the manifold φ as given, and in any real application φ must be estimated from data. The paper mentions fitting methods (TDA, splines) only in passing and does not investigate how errors in φ propagate into log-likelihoods, parameter estimates, or coordinate selection. In the neural data analysis, a "fitted loop manifold in ℝ¹⁰" is shown but no details are given about the fitting method, hyperparameters, or reliability of the fit. While this doesn't invalidate the method, it is a significant gap: PGPCA's advantage over PPCA depends on having a good manifold, and users need guidance on when the manifold is "good enough." A minimal sensitivity analysis (e.g., perturbing the true manifold or comparing manifolds fit with different methods) would substantially strengthen the paper.

4. **Neural data results lack uncertainty quantification.** Figures 4B and 4D show that GeCOV yields higher log-likelihood than EuCOV for two example mice, but no error bars, cross-validation confidence intervals, or significance tests are reported. Table 2 reports single values per dataset. It is unclear whether the observed differences are meaningful relative to variability in the fitting procedure or across animals. The paper mentions six mice were recorded but only shows two — reporting results across all six with some measure of uncertainty would be needed to support the claim robustly.

5. **The derivation from Eq. (12) to Eq. (13) is condensed, and the critical step is asserted rather than derived.** While the key result (the compact form of ℒ₁ᴹ with Γ(q)) is stated and used to obtain the M-step updates, the algebraic manipulation that transforms the position-dependent covariance Ψ(z) into the PPCA-like form is not shown in the main text. This makes it difficult for readers to verify the derivation or understand why the PPCA structure emerges. Since this is the theoretical core of the EM algorithm, more exposition is warranted.

6. **The discretization parameter M (number of landmarks for p(z)) is not reported for any experiment, and sensitivity to M is not explored.** The paper introduces M landmarks to discretize p(z) but never states what value of M was used in simulations or neural data analyses, nor how results depend on this choice. For scaling to higher-dimensional manifolds, this is a practical concern.

### Trivial
None.

## Nice-to-Haves

- **Comparison to a nonlinear latent-variable model** (e.g., a VAE or GP-LVM) would help contextualize PGPCA's value relative to methods that learn nonlinear structure jointly rather than taking a pre-fitted manifold. This is not required to validate PGPCA's core claim (which is about generalizing PPCA, not outperforming all nonlinear methods), but would sharpen the contribution.
- **Direct visualization of the learned p(z)** for the simulation in Figure 3, comparing estimated vs. true manifold-state distribution, would make the "learning p(z)" claim more concrete than log-likelihood comparisons alone.
- **An ablation with a deliberately incorrect manifold** would demonstrate that PGPCA's higher log-likelihood is driven by genuine geometric structure rather than artifacts of the fitting procedure.

## Removed Points

- **"The derivation of Γ(q) is not presented in the readable portion"** — The derivation is presented in condensed form: Eq. (12) gives the expansion, Eq. (13) gives the compact result with Γ(q). While the intermediate algebra is not fully expanded, the key formulas are present. Further, the full derivation likely appeared in the appendix (which was stripped by the parser). This criticism is removed as it overstates the absence.
- **"The evaluation lacks comparison to a reasonable nonlinear baseline"** — The paper's core claim is generalizing PPCA to incorporate a known manifold; PPCA (not GP-LVM or VAE) is the natural and directly informative baseline. The paper explains why GP-LVM targets a different setting. This is scope creep rather than a genuine weakness and is moved here.
- **"The paper claims PGPCA can learn the data distribution both around and on the manifold as a solved problem"** — The paper demonstrates this via log-likelihood comparisons and Figure 3, and learning p(z) is an explicit part of the EM algorithm. The claim is supported, though direct visualization of p(z) would strengthen it (moved to Nice-to-Haves).

## Novel Insights

The most interesting observation emerging from the review process is the tension between the paper's claim of performing "hypothesis testing" and what the method actually provides. PGPCA's real strength is not formal hypothesis testing but rather a principled likelihood-based model comparison framework for distribution coordinate selection — this is genuinely useful (especially for neural data where geometric structure is of scientific interest) and should be presented as such rather than dressed in statistical language that invites skepticism. A second insight is that the paper's EM derivation, if fully spelled out, reveals an elegant reduction: by incorporating the manifold and coordinate information into Γ(q), the PPCA solution structure is preserved even in the nonlinear case, which means PGPCA inherits PPCA's theoretical guarantees (uniqueness of the M-step solution, monotonic convergence of the EM algorithm) without requiring new proof machinery. This structural inheritance is the paper's deepest intellectual contribution and deserves more emphasis.

## Suggestions

1. **Rephrase all instances of "hypothesis testing" to "model comparison" or "coordinate selection via log-likelihood."** If the authors wish to retain the term, they should provide a concrete test procedure (e.g., a parametric bootstrap or likelihood-ratio test with known null distribution) and validate it.

2. **Provide a formal mathematical definition of GeCOV** — e.g., as the orthonormal basis formed by the d tangent vectors of the manifold (via the Jacobian of φ or the Frenet frame) plus (n−d) normal vectors derived from the manifold's normal bundle.

3. **Add a sensitivity analysis for manifold quality:** perturb the true manifold in simulations or compare manifolds fit with different methods/hyperparameters, and show how PGPCA's log-likelihood and coordinate selection degrade.

4. **Report uncertainty for neural data results:** show log-likelihood differences across all six mice with error bars, and consider reporting results across cross-validation folds or bootstrap samples.

5. **State the value of M** used in each experiment and include a brief sensitivity check for this parameter.

## Score and Decision

The paper proposes a principled and valuable extension of PPCA to data distributed around nonlinear manifolds. The core idea is sound, the EM algorithm is clever, and the empirical results are consistent with the claims. The main issues — overclaimed "hypothesis testing," missing formal definition of GeCOV, and absent sensitivity analysis — are addressable in a revision and do not undermine the core contribution. The paper represents a genuine methodological advance for probabilistic dimensionality reduction in neuroscience and beyond.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>