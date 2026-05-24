Now I have sufficient calibration data. Let me construct the final consolidated review.

## Summary

This paper proves that one-hidden-layer ReLU networks trained solely by permuting second-layer weights (keeping fixed initial values) can achieve universal approximation of one-dimensional continuous functions. The proof uses a four-pair step-matching construction and a linear reorganization method to eliminate unused parameters. Theorems cover equidistant initialization (with and without a learnable output linear layer) and extend to random initialization with a probabilistic guarantee. Experiments using the LaPerm heuristic algorithm validate the predicted O(n^{-1/2}) convergence rate in 1D and explore initialization effects and permutation patterns.

## Strengths

1. **First theoretical UAP guarantee for permutation-trained networks.** Theorem 1 proves that a ReLU network whose second-layer weights are only permuted (never changed in value) can approximate any continuous function on [0,1] to arbitrary accuracy. This is a genuinely novel result because all prior UAP theorems assume unconstrained parameter tuning. The construction — using four pairs of basis functions in a step-matching arrangement combined with linear reorganization of unused parameters — is clever and non-trivial. Every parameter must be used or accounted for, which is a harder constraint than standard UAP proofs face. (Theorem 1, Section III)

2. **Approximation rate analysis with numerical verification.** Section III-E derives an O(n^{-1/2}) L² convergence rate for the step-function approximator, and Figure 1 confirms this rate holds empirically for both L² and L∞ errors under equidistant and pairwise random initialization. Providing a rate (rather than just an existential guarantee) and validating it numerically is a clear strength uncommon in UAP papers. (Section III-D, Figure 1)

3. **Demonstration that initialization quality fundamentally matters under permutation constraints.** Experiments in Section IV-E show that Xavier and He initializations can catastrophically fail under permutation training while simple uniform randomizations succeed. This is a non-obvious insight specific to the permutation-training setting and directly supports the paper's claim that initialization plays a qualitatively different role here than in standard training. (Section 4.5, Figure "The performance of different initialization strategies")

4. **Honest treatment of high-dimensional limitations.** The paper transparently reports that the 1/2 convergence rate degrades in 2D and 3D (to ~1/6 in 3D), explicitly attributes this to the "preliminary eight-direction setting," and identifies finite-element methods as a plausible path forward. This candor appropriately scopes the theoretical contribution. (Section 4.4, Figures 2-3)

## Weaknesses

### Major

1. **Proof gap in Theorem 2 (UAP without the linear layer): residual-parameter handling is unsubstantiated.** When eliminating unused parameters in the pseudo-copy construction, the paper writes remaining parameters as paired constant-matching approximators plus a residual R(x). It then claims: *"Since the constant-matching construction has flexibility, {b̄_k}_{k=1}^4 can be small enough to ensure C_R ≤ Δh."* (lines 481-482) The biases {b̄_k} are determined by the equidistant initialization (a fixed grid on [0,1]); they are not chosen by the proof. If the residual consists of basis functions near 1, their squares sum to O(1) rather than O(Δh). The paper offers no argument for why the construction can always avoid this case. This gap does **not** affect Theorem 1 (which relies on linear reorganization with the learnable α,γ layer) but it means Theorem 2 is not properly established as written. The gap appears fixable (e.g., by ensuring n ≡ 1 (mod 8) or using a more careful allocation), but the current proof does not provide the needed reasoning.

2. **Theorem 3 (random initialization) proof is sketched rather than completed.** The proof (Section III-F) does not provide explicit bounds on the required width n and perturbation Δr to achieve probability 1-δ. The inclusion-exclusion expression for P_sub is given but never evaluated into a concrete width requirement. More critically, the perturbation argument (Eq. 22) that f_sub^NN approximates f_equi^NN with error < ε/4 is asserted without any continuity estimate: the network uses ReLU activations and the construction involves discrete matching of coefficients, so small perturbations could break the step-matching relations. The claim may be true, but the paper does not supply a rigorous justification. This is an evidential gap, not a fatal flaw — the idea that denser random samples approximate the equidistant case is intuitive — but it falls short of the standard of proof expected for a theorem.

### Minor

3. **Title overclaims the scope relative to the actual contribution.** The title "Neural Networks Trained by Weight Permutation are Universal Approximators" reads as a general result, but the theory is proven only for one-dimensional continuous functions with equidistant (or pairwise random) initialization and fixed first-layer weights w_i = ±1. The abstract is properly qualified ("approximate one-dimensional continuous functions"), but the title will mislead casual readers. The paper would be more accurately titled with a scope qualifier such as "One-Dimensional" or "for One-Dimensional Continuous Functions."

4. **Experiments do not directly test the existence guarantee.** The experimental section evaluates the LaPerm algorithm, which interleaves Adam free-updates with periodic permutations. The theory guarantees the *existence* of a permutation achieving the approximation (existential statement about the expressivity of the weight-constrained architecture). The experiments show that a heuristic algorithm can find such permutations in practice — which is a weaker and different claim. A controlled experiment that, for small n, enumerates permutations or directly searches for the optimal permutation would directly validate the existence theorem. The current experiments are not decoupled from the algorithm's convergence properties.

5. **No comparison with standard unrestricted training baselines.** The experiments do not include the approximation error achieved by the same architecture under standard gradient descent (full weight freedom). Without this baseline, the reader cannot judge whether the permutation constraint is a significant handicap, or how the O(n^{-1/2}) rate compares to what an unconstrained network of the same width achieves. Adding this comparison would contextualize the contribution.

6. **Error-rate derivation in Section III-D is presented as a heuristic estimate, not a formal theorem.** The derivation makes assumptions (e.g., that s = (b₂+b₃)/2 exactly, that Δs_l ~ O(d)) that are plausible but not rigorously justified, and the stacking analysis conflates the scaling factor L with the number of pseudo-copies. The paper is transparent about this being an estimate, which is fine, but it should be clearer that this is not a theorem-level bound.

### Trivial

7. The proof sketch of Lemma 1 (piecewise constant approximation) is very brief — "we assume f^* to be a polynomial function for simplicity" — though the construction is standard and the idea is clear.

8. The paper refers to "permutation-active patterns" and "learning behavior" (Section IV-F) in qualitative terms. These observations are interesting but the connection to the theoretical results is speculative and not quantitatively substantiated.

## Nice-to-Haves

- A direct test of the existence guarantee: for small width n, enumerate all possible permutations of the coefficient vector and measure the best achievable approximation error, comparing to the theoretical bound.
- A comparison with standard Adam/free training on the same architecture to contextualize the performance of permutation training.
- A brief discussion of whether Theorem 2 can be salvaged by ensuring n ≡ 1 (mod 8) to avoid the residual handling issue.

## Removed Points

These points from the input reviews are flagged for removal with justification:

1. **"Lemma 1 proof is incomplete / too sketchy."** — The construction described (covering the range with Δh-bins and picking level-crossing points) is a standard piecewise constant approximation. The one-line sketch is adequate for a conference paper; a full constructive proof would add length without insight. Removed as overly demanding.

2. **"The paper's theory does not cover arbitrary first-layer weights."** — This is correct but the paper explicitly states w_i = ±1 via homogeneity (line 93: "we consider a homogeneous case with w_i = ±1"). This is a standard simplification in ReLU network proofs. Not a weakness.

3. **"No demonstration that the theoretical construction could be realized in hardware."** — The paper discusses hardware motivation in the introduction but does not claim to implement it. Scoping the paper to the theoretical result is appropriate. Removed as scope creep.

4. **"Random initialization theorem should have explicit bounds."** — Retained as a minor weakness (#2 above) but downgraded from the harsh critic's "fatal / only sketched" characterization. The proof sketch conveys the core idea clearly; the issue is one of rigor rather than correctness.

5. **"The paper does not discuss whether the permutation training algorithm converges."** — The theory is about expressivity (existence of a permutation), not optimization. This is explicitly stated (line 791: "our proof does not rely on any specific algorithmic implementations"). Removed as misunderstanding.

6. **"The soft-mask comparison uses a non-standard proxy"** etc. — This criticism is about a different paper; it does not appear in the current paper.

7. **Strength Finder's generic claims** (e.g., "this paper addressed an important problem") — Removed. Only concrete, evidence-grounded strengths are retained.

8. **"Error rate derivation is not rigorous."** — Retained as minor weakness #6 but the harsh critic's framing as a serious gap is overblown; the paper presents it as an estimate, not a theorem.

## Novel Insights

None beyond the paper's own contributions. The most valuable observation emerging from the review is that Theorem 2's gap is localized to the mod-8 residual handling and appears eminently fixable — the core proof technique (four-pair construction + linear reorganization) is sound. The reviews do not surface a synthetic insight that the paper itself does not already articulate.

## Suggestions

1. **Fix the residual handling in Theorem 2.** Either: (a) ensure the construction always uses n ≡ 1 (mod 8) so the leftover bases are the first (smallest) four; (b) provide an explicit argument showing how the "flexibility of constant-matching construction" ensures the residual bases have small b̄_k values; or (c) restrict Theorem 2 to the case where n is a multiple of 8 plus 1.

2. **For Theorem 3, either complete the proof** with explicit Lipschitz-continuity estimates for the network output with respect to parameter perturbations and explicit bounds on n and Δr in terms of ε and δ, **or downgrade it to a conjecture/observation** and adjust the labeling accordingly.

3. **Qualify the title** to reflect the 1D scope, e.g., "One-Dimensional Universal Approximation for Permutation-Trained ReLU Networks."

4. **Add a free-training baseline** to the experiments for the same architecture to contextualize the performance.

5. **Run an enumeration experiment** for very small n (e.g., n=8, 12, 16) to directly validate the existence claim by exhaustive search over permutations.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Low band (<3.5): ZTvUT49JjL (3.40), KNQJtoPZmz (3.00), 2NwHLAffZZ (2.33), 6E8GCcCgxl (3.25) — papers with fundamental flaws or very weak contributions. Current paper is clearly stronger.
- Middle band (3.5–7.5): 5xwx1Myosu (6.50) — fixed random weights, only biases trained for UAP, only minor weaknesses; wOSYMHfENq (6.00) — UAP via BN-only training with fixed random weights, only minor weaknesses; 1Wi0Ys33Nm (6.25) — pseudo-iid for NNGP, minor weaknesses only; QjO0fUlVYK (6.00) — star domain conjecture, minor weaknesses only.
- High band (>7.5): 4xWQS2z77v (8.00) — loss landscape connectivity with critical widths; viftsX50Rt (8.00) — graph random features; EzjsoomYEb (8.00) — higher-order message passing.

**Initial bracket: 4.5–6.5.** The paper is well above weak anchors (~3) but has real gaps (Theorem 2) that the strongest middle-band anchors lack.

**Round 2 (Narrowing):**
- ihHeqPLRDk (4.75, Reject) — SincKAN, missing experimental details. The current paper has fewer fatal flaws but a genuine proof gap.
- y9Xp9NozPR (5.50, Accept) — low-rank attention expressivity, only minor weaknesses. Current paper is weaker due to proof gaps.
- QgwAYFrh9t (5.75, Accept) — learning hierarchical polynomials, only minor weaknesses. Current paper is weaker.
- PCTqol2hvy (6.25, Reject) — ResNet approximation bounds, major weakness in lower-bound reasoning but upper bounds solid. Current paper's proof gap is comparable in severity.

**Final placement:** The paper sits below the 5.50–6.50 anchors (which have no major weaknesses) and is comparable to PCTqol2hvy (6.25, Reject) in terms of structural issues, though with a different profile. It is above 4.75 anchors which had more fundamental experimental problems.

**Narrowing from the bracket:** Round 1 bracket was 4.5–6.5. Round 2 anchors at 4.75 (Reject), 5.50 (Accept), 5.75 (Accept), 6.25 (Reject) show the paper is closest to the 4.75–5.50 range. The paper is weaker than the 5.50 and 5.75 Accept papers (which had no major weaknesses) and slightly stronger than the 4.75 Reject paper (which had missing experimental details for its core empirical claims). The Theorem 2 gap is the decisive factor — it is a genuine mathematical gap, though localized and plausibly fixable.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>