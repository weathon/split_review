Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes *syre*, a simple method that adds a static random bias to model parameters along with weight decay to provably remove reflection symmetries from the loss function. The authors prove that this breaks the coupling between symmetric solutions and weight decay minimizers, preventing low-capacity traps. They characterize the symmetry-breaking strength theoretically and demonstrate the method across diverse settings including supervised learning, VAEs, self-supervised learning, and continual learning.

## Strengths

1. **Provable removal of all reflection symmetries with a simple additive bias (Theorem 1)**: The paper proves that with probability 1, adding a static bias + weight decay removes all reflection symmetries from the loss function without requiring knowledge of them. This is a clean theoretical result with a one-line code change.

2. **Theoretical characterization of symmetry-breaking strength (Theorem 3 / Corollary)**: The paper proves that at any symmetric point, the gradient in the symmetry-breaking direction is Ω(γσ₀), giving a quantitative bound. Theorem 4 extends this to general finite groups, showing the gradient scales with rank(I−V̄). This goes beyond an existence proof and provides guidance for hyperparameter choices.

3. **Empirical demonstration across diverse high-stakes settings**: The method is shown to prevent neural collapse in supervised FCNs (Figure 4/5), mitigate posterior collapse in VAEs (Figure 6), improve last-layer representations in SimCLR (Table 1, from 22.2%→32.5%), and maintain plasticity in continual learning (Figures 7, 8). The breadth of applications makes a convincing case that symmetry-induced collapse is a genuine practical problem.

4. **Handling of uncountably many symmetries via anisotropic weight decay (Theorem 2)**: By using a diagonal matrix D with distinct entries, the method extends to rotation and double rotation symmetries common in transformers and SSL, reducing the possible symmetries to at most finitely many.

5. **SSL results isolate symmetry as a concrete mechanism**: Table 1 shows syre removes 0% low eigenvalues (vs. 70% in vanilla) and recovers roughly 42-50% of the performance gap between last and penultimate layers. This provides mechanistic insight into why last-layer representations underperform in SSL.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baseline comparisons in several practical experiments**: The VAE (Section 6.4), SSL (Table 1), and continual learning CNN (Figure 7) experiments compare syre primarily against vanilla training, without controlling for the fact that syre adds both a static bias AND weight decay. **The VAE experiment is particularly problematic**: it compares vanilla training (no weight decay) against syre (with γ=1000 weight decay), conflating weight decay effects with symmetry removal. The 4-layer FCN (Figure 4) and RL (Figure 8) experiments do control for weight decay, which is good, but the paper would be substantially stronger if additional ablations separated the effect of "removing symmetries" from "adding regularization." Comparisons against increased weight decay, larger initialization variance, or dropout in the main application experiments (not just the synthetic benchmark of Figure 3) would clarify whether the proposed mechanism drives the gains. This is the paper's most significant weakness.

2. **The VAE experiment (Section 6.4) confounds weight decay with syre**: The reconstruction images compare "No weight decay" (vanilla) against "γ=1000" (syre). Since syre always includes weight decay, the improved rank and reconstruction loss could be partially or entirely due to weight decay alone. The paper notes that "only the encoder has weight decay," but this is not a controlled comparison. Given that this is one of the paper's primary application demonstrations, this is a meaningful gap that needs to be addressed.

### Minor

1. **Proposition 2's claim about discrete GD/SGD**: The proposition states that for all time steps *t* under GD or SGD, there exists a lower-dimensional model matching the forward pass. The paper's justification ("despite the discretization error") does not rigorously establish that this holds for discrete GD/SGD, only for gradient flow. For finite step sizes, discretization error can (and often does) move parameters out of the symmetric subspace. The claim should be qualified or more carefully argued.

2. **Theory-dynamics gap**: The paper proves that symmetric points are no longer stationary under ℓᵣ (Corollary to Theorem 3), but does not analyze escape dynamics from *near-symmetric* points. The gradient component in the symmetry-breaking direction is Ω(γσ₀), which at recommended values (σ₀ = 0.01/√d, γ ≈ 10⁻³–10⁻²) gives γσ₀ ≈ 3×10⁻⁶ for d=1024. While the experiments show the method works in practice, the paper does not discuss how quickly the model escapes near-symmetric attractors or whether there is a regime where γσ₀ is too small to matter within a practical number of steps. A scaling analysis or numerical experiment on escape times would bridge this gap.

3. **Missing confidence intervals / run counts for the 4-layer FCN experiment (Figure 4/5)**: The ResNet experiment reports 10 trials with standard deviation, and the RL experiment averages over 5 seeds, but the 4-layer FCN on MNIST does not state the number of runs. Explicitly reporting variability would strengthen this result.

4. **Limited discussion of continuous symmetries**: Theorem 2 handles rotation/double-rotation symmetries via anisotropic weight decay (diagonal D), but the paper does not discuss whether continuous Lie groups beyond those covered by the framework could pose limitations in practice. The paper acknowledges this implicitly (Theorem 2 requires distinct diagonal entries of D) but does not discuss the scope of this restriction.

### Trivial
- The synthetic benchmark's "degree of symmetry" metric (thresholding |vᵢᵀw| < cₜₕ) is threshold-dependent, though this is acceptable for a controlled benchmark.
- The SSL "50%" claim is a rough estimate (the gap reduction is ~42% numerically) and should be stated with slightly more precision.

## Nice-to-Haves
- An ablation of σ₀ in the VAE and continual learning experiments would help practitioners calibrate the trade-off between symmetry removal and optimization.
- An experiment showing a case where *syre* hurts performance (too much symmetry removal causes overfitting) would strengthen the paper's honesty and help define the method's operating regime, as the conclusion mentions this possibility but does not demonstrate it.
- Comparison against dropout or increased weight decay in the main application experiments (beyond the synthetic benchmark) would substantially strengthen the causal claim that symmetry removal drives the improvements.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"No methods are known to enable full escape" is too strong**: The critic misreads this statement. The paper claims no method is known to *provably remove all reflection symmetries from the loss function without knowledge of them*, which is a different claim from "no method helps with escape." The paper's context and the cited related work support this precision. **Removed** — misreading by reviewer.

- **Assumption 1 not argued for**: The paper explicitly states "This assumption is satisfied by common neural networks with standard activations" and provides a footnote with a pathological counterexample (linear objective). The critic's demand for a more formal argument is not a genuine weakness given the paper's explicit acknowledgment. **Removed** — paper provides sufficient justification.

- **Theorem 4 proof speculation**: The critic speculates about potential issues in the (appendix-stripped) proof of Theorem 4. Per the hard rules, missing appendix content is a parser artifact and not a paper weakness. **Removed** — parser artifact.

- **Degree of symmetry measure is arbitrary**: The measure is defined specifically for the controlled benchmark in Figure 3 and is a standard design choice for synthetic problems. No single metric is universal, and the paper makes no claim otherwise. **Removed** — design nitpick.

- **SSL 50% figure is not a clean causal estimate**: The paper is appropriately cautious ("can explain about 50%") and the estimate is reasonable given the experimental design. The critic overstates the imprecision. **Removed** — the paper's language is already appropriately hedged.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Fix the VAE experiment**: Run a controlled comparison where both vanilla and syre use the same weight decay (or where weight decay is added to the vanilla baseline). This is essential for the VAE experiment to cleanly support the paper's claims.
2. **Add a few controlled baseline comparisons**: Even adding 1-2 additional baselines (e.g., doubled weight decay, dropout on the projection head in SSL) would substantially increase confidence that the improvements come from symmetry removal rather than generic regularization.
3. **Add a numerical escape-time experiment**: On a small model where the symmetric subspace is known, show that syre reduces the time to escape compared to vanilla training, with varying γσ₀. This would bridge the theory-dynamics gap.
4. **Qualify Proposition 2**: Clarify that the claim holds exactly for gradient flow and approximately for discrete GD/SGD, rather than claiming it holds "for all time steps t under GD or SGD" without caveat.

## Score and Decision

The paper makes a theoretically sound and practically simple contribution to an important problem. The core idea — adding a static bias to break loss symmetries — is novel and well-motivated. The theoretical analysis is the paper's strongest asset, providing provable guarantees. The experimental breadth is good, covering multiple training paradigms where collapse is known to occur. However, the VAE experiment's uncontrolled comparison and the general lack of alternative baselines in the main experiments weaken the empirical validation. With revisions to address these issues (particularly fixing the VAE comparison and adding a few controlled baselines), the paper would be a solid contribution.

**MY FINAL SCORE: <pineapple>7.0</pineapple>**

**MY FINAL DECISION: <orange>Accept</orange>**