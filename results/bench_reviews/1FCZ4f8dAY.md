Now I have all the evidence I need. Let me compose the final review.

---

## Summary

This paper develops a unified, invariant-theoretic characterization of equivariant polynomial (and analytic) functions mapping tensors to tensors under the orthogonal group O(d), the indefinite orthogonal group O(s,d-s) (including the Lorentz group), and the symplectic group Sp(d). The authors translate abstract results from classical invariant theory (isotropic tensors, Kronecker deltas, Levi-Civita symbols, and their generalizations) into explicit parameterizations (Corollaries 1–3) suitable for constructing machine learning models. They demonstrate the framework on three diverse applications: stress-strain tensor learning in materials science, path signature estimation for time series, and sparse vector estimation from theoretical computer science, consistently showing that the equivariant models outperform non-equivariant baselines.

## Strengths

- **Theoretically clean and general framework.** Theorem 1 and its generalizations (Theorem 2, Corollaries 1–3) provide explicit, constructive parameterizations of equivariant tensor functions for O(d), the Lorentz group O(s,d-s), and Sp(d) using isotropic tensors and contractions — without requiring Clebsch–Gordan decompositions, which are limited to low-dimensional SO(d)/O(d). The presentation is mathematically rigorous yet accessible to an ML audience, with clear definitions, examples, and complexity analysis.

- **Broad scope beyond O(d).** While prior equivariant tensor methods (e3nn, escnn) focus on O(d)/SO(d) for d=2,3, this paper extends the theory to the indefinite orthogonal and symplectic groups, which are directly relevant to special relativity and classical/quantum mechanics. Corollary 3 provides explicit parameterizations for these groups. This is a genuine generalization.

- **Diverse experimental validation.** The paper demonstrates its framework on three genuinely distinct problems from materials science, time series analysis, and theoretical computer science. The stress-strain experiment (Table 1) shows orders-of-magnitude improvement over MLP baselines (e.g., 4.057e-6 vs 1.586e-4 at n=5,000), and the path signature experiment (Table 2) shows similar gains. The sparse vector experiment (Table 3) is particularly insightful: it shows that learned equivariant models can outperform sum-of-squares methods when the theoretical assumptions of SoS are violated, illustrating a concrete advantage of the learning approach.

- **Practical recipes for low-order tensors.** Corollaries 1 and 2 reduce the exponential complexity of the general theorem to tractable forms for output ranks k′=1,2,3,4 and for symmetric matrices. The authors explicitly acknowledge the complexity limitations and target practically relevant settings, which is honest and appropriate.

## Weaknesses

### Fatal
None.

### Major
- **Unfair comparison to TFENN (stress-strain experiment, Table 1).** The authors compare against TFENN numbers taken directly from Garanger et al. (2024) without re-implementing the method under identical conditions. TFENN errors are reported as single numbers without variance, while the authors' results are averaged over 5 trials with standard deviations. Although the performance gap is very large (1–2 orders of magnitude), the paper's claim that "our equivariant model performs dramatically better than the other models" would be on firmer ground with a controlled reimplementation. The paper should at minimum discuss this limitation transparently.

- **Weak augmentation baselines.** In both the stress-strain experiment (line 282) and the path-signature experiment (line 303), the "augmented" MLP baselines use only 4 random transformations. For continuous groups like O(d) and the Lorentz group, 4 random transformations are far too few to achieve approximate equivariance; the large gap between the augmented MLP and the proposed model may largely reflect insufficient augmentation. The paper should run the augmented baseline with substantially more transformations (e.g., 50, 100) or compare against a canonicalization baseline to make the advantage of exact equivariance convincing.

### Minor

- **Shared-MLP implementation not fully characterized.** The paper states (line 303) that all functions q_{t,σ,J} in Corollary 1 are implemented as a "single, shared MLP." The theoretical parameterization requires a separate polynomial for each (t,σ,J) combination. The paper does not discuss whether this weight-sharing breaks universal representation, nor does it provide ablation experiments comparing shared vs. separate MLPs for small settings. Remark 1 invokes Stone-Weierstrass for polynomial approximation, but the gap between "separate polynomials per term" and "one shared MLP producing all coefficients" is not addressed.

- **Missing experimental details in main text.** Table 2 does not report the number of sampled points n used in the path-signature experiment, making the complexity of the method unassessable from the main paper. The notation "Discrete (24)" in the table — referring to equation (24) — is confusing without context. These details may be in the appendix but should be noted in the main text.

- **"Ours (Diag)" outperforms full model in some sparse-vector settings.** In Table 3, the variant that uses only row norms (i.e., invariant features) beats the full equivariant model in 5 out of 12 settings (e.g., Accept/Reject-Diagonal: 0.589 vs 0.465). This interesting ablation receives only a brief mention and deserves more discussion about when cross-products add noise rather than signal.

### Trivial
None beyond what was already moved to Removed Points.

## Nice-to-Haves

- A figure or pseudocode illustrating how the combinatorial sum in Corollary 1 is reduced to a neural computation (taking the matrix of inner products as input and outputting the tensor) would greatly improve understandability.
- For the sparse-vector problem, comparing against an E(n)-equivariant model or a dot-product attention model (which naturally respects O(d) symmetry) could provide stronger learned baselines.

## Removed Points

- **Criticism about "first work... at this level of generality" being overstated re: Clebsch-Gordan methods.** Removed because the paper already explicitly acknowledges (lines 72-73) that CG methods work for O(d) for d=2,3 and that the novelty lies in covering indefinite orthogonal and symplectic groups. The claim is appropriately scoped.

- **Criticism about missing appendix content or proofs being deferred.** Removed per instruction — appendix sections are stripped by the parser and exist in the original submission.

- **Claim that TFENN comparison uses "different evaluation metric."** The paper states the metric (squared Frobenius norm) and it is the same as reported in Garanger et al. (2024). The concern about reimplementation stands, but the metric claim is factually incorrect.

- **Pure formatting/style nitpicks and grammar issues.** Removed per instruction.

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own contributions. However, one observation worth noting from the sparse-vector experiment: the "Ours (Diag)" ablation (using only row norms) sometimes outperforming the full model suggests that in high-noise regimes the cross-product terms may actually harm performance — a finding that resonates with the broader phenomenon of "too much expressivity can hurt" in equivariant models when data is limited or noisy.

## Suggestions

1. Re-implement TFENN under identical training conditions (same data splits, metric, training regime) and report both methods with comparable statistics, or at least add a disclaimer about the uncontrolled comparison.
2. Run the augmented MLP baselines with substantially more transformations (50–100) to make the augmentation-vs-equivariance comparison fair.
3. Include an ablation comparing the shared-MLP architecture against separate-MLP versions for a small-scale setting to characterize the expressivity gap.
4. Add the value of n (number of sampled points) to the path-signature experiment description in the main text, and clarify the "Discrete (24)" label.

## Score and Decision

**Calibration Anchors** (all from the human reviews directory):

| Anchor Path | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/q95Hql3QBk.md` (Learned Polarization) | 2.00 | Pure theory with no experiments; the current paper has both theory and diverse experiments — substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/MQucws0B1g.md` (Symmetric Tensor Network) | 3.33 | Limited theory contribution, only one experiment; current paper has broader theoretical scope and more experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/uzHoja5T7x.md` (Learnable Augmentations) | 4.00 | Weak experiments, unclear method; current paper is much cleaner methodologically. |
| `/home/wg25r/review_agent/human_reviews_2026/HufTLkTOJh.md` (Antisymmetric Tensors) | 5.00 | Strong theory but toy experiments only; current paper has more realistic experiments and broader scope. |
| `/home/wg25r/review_agent/human_reviews_2026/anvRacYUHe.md` (Binary Forms) | 5.50 | Similar hybrid theory+experiments paper but only covers SO(3); current paper covers more groups and has more diverse applications — slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/HVKB5DM5n7.md` (Approximate Equivariance) | 6.50 | Solid method with good experiments; different focus (approximate vs exact). Current paper has cleaner theoretical contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/jz3d7nvtGz.md` (Any-Subgroup Equivariant) | 6.50 | Strong accepted paper with elegant idea and solid experiments; the current paper is more theoretical but similar in quality. |
| `/home/wg25r/review_agent/human_reviews_2026/VaS6xcDrTb.md` (SU(2) Rotation Estimators) | 8.50 | Exceptionally clean and well-executed; current paper has more experimental messiness but broader theoretical contribution. |

The paper provides a solid theoretical contribution — a unified parameterization of equivariant tensor functions across three classical Lie groups — backed by three diverse experimental demonstrations. The weaknesses (uncontrolled TFENN comparison, weak augmentation baselines, missing characterization of shared-MLP expressivity) are real but not fatal; they are fixable and do not undermine the core theoretical claims. Compared to the calibration anchors, the paper sits comfortably above purely theoretical works (2.0–4.0 range) and comparable to or slightly above mid-range theory+experiment papers (5.0–6.5). The experiments are more diverse than typical for this type of paper, though the experimental rigor has room for improvement.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>