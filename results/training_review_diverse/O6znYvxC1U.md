Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

## Summary

This paper studies BNNs in asymptotic limits (linear-width and sublinear-width) and establishes connections between kernel theory (the spectral universality assumption / SUA) and the renormalisation theory from statistical mechanics. The core contributions are: (1) novel integral formulas (Theorems 3.3 and 3.4) for BNN predictor statistics under the SUA, expressed via the limiting spectral measure of the empirical kernel matrix; (2) a necessary and sufficient condition (Theorem 3.5) linking the applicability of renormalisation theory to nonlinear BNNs with the correctness of the SUA; and (3) a proposal for estimating predictor statistics in the sublinear-width regime where renormalisation theory breaks down.

## Strengths

- **Novel bridge between SUA and renormalisation theory for BNNs.** Theorem 3.5 is the first result (to my knowledge) that formally characterises when the renormalisation theory of Li & Sompolinsky (2021) extends to nonlinear BNNs, connecting it to the spectral universality assumption from kernel theory. The "if and only if" framing — though the condition is strong — is a clean conceptual contribution that clarifies the relationship between two previously separate lines of work.

- **Integral formulas for BNN predictors in two asymptotic regimes.** Theorem 3.4 provides explicit integral expressions for the mean and variance of a trained BNN predictor under the SUA, applicable in both the linear-width and sublinear-width limits. These formulas offer a new way to think about BNN inference that avoids explicit posterior computation.

- **The paper identifies the sublinear-width regime as a distinct setting where the sublinear scaling P ∝ N·N₀ causes renormalisation theory to break down.** Section 3.4 correctly diagnoses the failure mode (degenerate limiting spectral measure) and proposes a spectral-estimation approach that is a reasonable direction, even if the empirical validation is still preliminary.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 3.3's eigenvalue-eigenfunction independence claim is not justified.** The proof sketch (lines 71–73) argues that because the spectral measure converges to a nonrandom deterministic limit, "the eigenvalues can be sampled independently from the eigenfunctions." This does **not** follow logically. Convergence of the empirical spectral distribution (a P-dimensional joint distribution of eigenvalues) to a deterministic limiting measure does **not** imply that the eigenvalues are independent draws from that measure, nor does the spectral measure becoming nonrandom imply independence between eigenvalues and eigenvectors. The argument "since the spectral measure no longer depends on Θ, the eigenvalues can be sampled independently from the eigenfunctions" is a non sequitur. Baker (1977) concerns convergence of empirical eigenvalues to Mercer eigenvalues under a fixed data distribution — it does not address the joint eigenvalue-eigenvector distribution in a random feature model where both Θ and the data are random. This gap is structural: the independence assumption is central to the derivation of the integral formulas in Theorem 3.4, which treat Λ and Φ as independent and integrate over them with a product measure. Without a proper justification, the theoretical edifice is fragile.

- **Experimental validation is far too thin to support the claimed practical contribution.** The paper claims a "novel technique for estimating the predictor statistics of a trained BNN" that is "applicable to the sublinear-width regime where the predictions of the renormalisation theory are inaccurate" (abstract). The supporting experiment (Figure 2) consists of a single synthetic dataset (linear teacher, Gaussian data, P=200, N₀=40) with a single ReLU hidden layer. There are no quantitative error metrics (RMSE, log-likelihood, calibration), no error bars or measures of variability, no comparison to the renormalisation theory that is being superseded, and no test on a real dataset in the sublinear regime. The variational inference baseline used as "ground truth" is itself an unverified approximation. For a claimed methodological advance, this level of validation is insufficient to convince.

- **The theoretical framing of Theorem 3.5 is mismatched with its practical implications.** The condition — "for any orthogonal Φ, there exists Θ such that φ(Θ,X)ᵀ φ(Θ,X) = ΦΛΦᵀ" — amounts to requiring that the random feature map's Gram matrix can realise **any** orthogonal decomposition. For any finite-width nonlinear network with a fixed activation function, this is almost certainly false: the set of attainable Gram matrices is a low-dimensional manifold. The paper acknowledges this indirectly ("in the spiked kernel case...we anticipate that the spectral universality assumption would fail") but does not squarely state the implication: the theorem effectively says renormalisation theory **does not** hold for realistic nonlinear BNNs except in trivial limiting cases. The paper frames this as an "extension" (Section 3.3 title, Contribution 2), which an honest reader would find misleading. The result is interesting as a *negative* characterisation, but the mismatch between presentation and logical content is a weakness.

### Minor

- **The likelihood notation in Section 2 is confusing and appears to contain an error.** The paper writes $p(\mathbf{y} | \mathbf{X}, \Theta, \mathbf{W}^L) \sim \mathcal{N}(\mathbf{y}, \phi(\Theta,\mathbf{X})^T \mathbf{W}^L \mathbf{W}^{L^T} \phi(\Theta,\mathbf{X}))$, where the first argument to $\mathcal{N}$ appears to be the data vector $\mathbf{y}$ rather than the network output. If this is conventional $\mathcal{N}(\text{mean}, \text{covariance})$ notation, the mean should be the model prediction $f(\mathbf{X})$, not the observations. This may be a parser artifact or a typo, but it propagates to the theoretical development and should be clarified.

- **The derivation of the limiting spectral measure in Section 3.1 is stated without sufficient justification.** The paper claims the limiting spectral measure of $\mathbf{K}_\Theta^{P,N,N_0}(\mathbf{X},\mathbf{X})$ in the linear-width regime is $\rho_{MP}^\alpha \boxtimes^L \rho_{\mathrm{NNGP}}^{\alpha_0}$, attributed as "a direct corollary of Theorem 2" in El Harzli et al. (2024). The induction step — successively applying the linear-width limit to hidden-layer widths while keeping interior widths infinite — is described in one sentence and the reasoning is not fully spelled out. The paper mentions it follows "the approach in Lee et al. (2018) where infinite limits are taken sequentially," but the sequential limiting procedure for multiple layers is delicate and the paper does not discuss potential issues.

- **Experimental details are insufficient for reproducibility.** The paper does not specify: how the integral formulas (Eq. 2 and 3) were computed numerically, the number of Monte Carlo samples used, the variational inference setup (architecture, prior scales, inference algorithm, hyperparameters) for the Pyro baseline, or how the Marchenko-Pastur fixed-point equation was solved numerically. The MNIST experiment uses "large width $\hat{N}=10000$ to estimate the NNGP kernel matrix" — but does not state the hidden-layer width used for the actual BNN in that experiment.

- **The practical advantage of the sublinear-width approach over alternatives (e.g., variational inference) is not argued or demonstrated.** The method replaces one computational problem (training a BNN via VI) with another (diagonalising large random matrices and estimating spectral measures). The paper does not discuss computational complexity, wall-clock time, or accuracy trade-offs. The claim that "in many applications of BNNs, where the training datasets are relatively small, this computational difficulty becomes less significant" is vague.

### Trivial
None.

## Nice-to-Haves

- A real-dataset experiment in the sublinear-width regime with quantitative metrics (RMSE, log-likelihood, calibration), error bars, and comparison to both the renormalisation theory and variational inference baselines.
- A more explicit discussion of the practical implications of Theorem 3.5: the paper would benefit from stating directly that the condition is essentially never satisfied for finite-width nonlinear networks, and reframing the result as a **negative** characterisation that explains why deviations from renormalisation theory are expected.
- Pseudocode or an algorithmic description of how the integral formulas are computed in practice.
- A discussion of computational complexity: how does the spectral estimation scale with P, N, and N₀?

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about MNIST experiment not testing the linear-width regime:** The reviewer claims the MNIST experiment "does not test the linear-width regime but rather approximates the NNGP limit." This is incorrect. The experiment uses the NNGP kernel (estimated via large width) as the **input** to the Marchenko-Pastur computation, which is precisely how the linear-width regime theory operates. The experiment is appropriate for testing the claim that the integral formulas match the renormalisation theory predictions in the linear-width regime.

- **Criticism about dimensional inconsistency of N(Φᵀy, Λ) in Theorem 3.4:** The reviewer claims "Φᵀy is M-dimensional while Λ is M×M" is dimensionally inconsistent. For a multivariate Gaussian N(μ, Σ), μ ∈ ℝ^M and Σ ∈ ℝ^{M×M} is **dimensionally consistent**, not inconsistent.

- **Criticism about absent proofs in appendix:** The reviewer notes proofs are absent and the appendix was stripped. Per the review rules, the parser strips appendix content from all papers; it exists in the original submission. The substantive point about the proof sketch being too brief is kept as a Major weakness under the independence claim.

- **Criticism about verifying the referenced theorem of El Harzli et al. (2024):** The complaint "Without being able to verify the referenced theorem" is a reviewer knowledge gap, not a paper error. The cited work exists. The substantive point about insufficient reasoning is retained as a Minor weakness.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the necessary and sufficient condition in Theorem 3.5, combined with the near-impossibility of satisfying it for nonlinear networks, implies that the renormalisation theory of Li & Sompolinsky (2021) is fundamentally limited to linear networks in any practical sense. This reframes the paper's Contribution 2 from "extending renormalisation theory to nonlinear BNNs" to "characterising why it cannot extend except in degenerate cases." This negative characterisation is arguably the paper's most interesting result, though the paper itself does not emphasise it. The reviews also collectively highlight that the paper's theoretical ambition (bridging kernel theory, random matrix theory, and statistical mechanics) outstrips the rigor of the derivations and the strength of the experimental validation, which is a common pattern in interdisciplinary theory papers that attempt to connect multiple technical languages.

## Suggestions

1. **Fix the eigenvalue-eigenfunction independence gap.** Either provide a rigorous argument (e.g., appealing to asymptotic freeness or the structure of the random feature Gram matrix) or restate Theorem 3.3 as an approximation rather than a convergence result. Without this, the theoretical core is not credible.

2. **Reframe Theorem 3.5 honestly.** The paper should openly state that the necessary and sufficient condition is so strong that it is essentially never satisfied for nonlinear networks, making the result a *negative* characterisation. This is still a useful contribution — it explains why renormalisation theory's empirical success is limited to specific settings — but the current framing as an "extension" is misleading.

3. **Substantially expand the experimental section.** At minimum, add: (a) a real dataset experiment in the sublinear-width regime, (b) quantitative metrics with uncertainty quantification (error bars across random seeds), (c) a direct comparison between the proposed method and the renormalisation theory predictions in the sublinear regime to demonstrate the improvement claimed in the abstract.

4. **Add an algorithmic description.** Provide pseudocode for how the integral formulas (Eq. 2 and 3) are computed in practice, including how the spectral measure is estimated and how the Marchenko-Pastur fixed-point equation is solved.

5. **Clarify the likelihood notation.** The Gaussian likelihood definition in Section 2 should be corrected/re-written to avoid confusion about whether the mean is the network output or the data.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>