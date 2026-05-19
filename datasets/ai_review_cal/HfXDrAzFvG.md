- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information needed. Let me construct the final review.

## Summary

This paper extends LipSDP — a semidefinite programming framework for computing certified Lipschitz bounds — to neural networks with GroupSort, MaxMin, and Householder activations, which are not slope-restricted and thus could not be handled by the original LipSDP. The core technical contribution is the derivation of novel quadratic constraints (Lemmas 1–2) that exploit the sum-preservation and 1-Lipschitz properties of these activations, leading to SDP conditions for ℓ₂ and ℓ∞ Lipschitz bounds covering feedforward, residual, and implicit architectures. Experiments on MaxMin networks show tighter bounds than the product-of-norms baseline and the naive residual-ReLU encoding approach.

## Strengths

- **Novel quadratic constraints for GroupSort and Householder activations (Lemmas 1–2).** The paper derives quadratic constraints based on sum-preservation and 1-Lipschitzness (Equations 6–9), enabling SDP-based Lipschitz analysis for activation functions that are not slope-restricted. This is the first extension of the LipSDP family beyond slope-restricted activations — a recognized open limitation.

- **Clean motivating example demonstrating the insufficiency of prior approaches (Section 3).** The paper shows that applying LipSDP to the residual-ReLU representation of a single MaxMin layer yields ρ = 2 (so an upper bound of √2 ≈ 1.414 on a known 1-Lipschitz function), concretely establishing why new quadratic constraints are necessary.

- **Unified SDP framework for ℓ₂ and ℓ∞ bounds across multiple architectures (Theorems 1–4).** The same quadratic constraints are extended to feedforward and residual networks and implicit models, with SDP conditions for both ℓ₂→ℓ₂ and ℓ∞→ℓ₁ Lipschitz estimation — a non-trivial unification that follows from the structure of the constraints.

- **Empirical validation showing substantial improvement over naive baselines (Table 1).** On deep MaxMin networks (up to 18 layers, 128 units), LipSDP-NSR gives bounds many orders of magnitude tighter than the matrix-product baseline (e.g., ℓ₂: 24,271 vs. 74,167 for 18×128; ℓ∞: 1.97×10⁵ vs. 2.79×10¹⁶ for the same model) and consistently outperforms LipSDP-RR (the residual-ReLU encoding) on deeper networks.

## Weaknesses

### Fatal
None.

### Major

- **Empirical validation is restricted to MaxMin (group size 2); GroupSort with larger groups and Householder are not tested.** The paper claims generality for GroupSort with arbitrary group sizes and Householder activations in the title, abstract, and throughout the text (e.g., "our work is the first one to extend LipSDP beyond slope-restricted activations, providing accurate Lipschitz bounds for neural networks with MaxMin, GroupSort, or Householder activations" — line 18). Yet every experiment in Table 1 uses only MaxMin (n<sub>g</sub>=2) activations. GroupSort with n<sub>g</sub>>2 and Householder are structurally distinct (sorting more than two elements; not a sorting operation at all), and the paper provides no experimental evidence that the SDP performs well for these cases. A single experiment with FullSort (n<sub>g</sub> = full width) or a learned Householder activation on a standard dataset would directly validate the claimed generality. This is the most significant gap in the paper — it is evidential rather than theoretical (the derivations are sound), but it meaningfully limits what can be claimed from the presented results.

### Minor

- **No ablation study supporting the S/P=0 simplification.** The paper states "Empirical tests indicate that the choice S=P=0 yields the same results as without this constraint" (line 297) and a similar claim for residual networks (line 482), but no supporting data is shown. A small ablation table (even for a few small networks) would confirm that the simplified SDP recovers the same ρ as the full parameterization.

- **SDP solve times are not reported.** The paper discusses scalability as a limitation and references structure-exploiting solvers, but does not report solve times for any of the models in Table 1. This information is directly relevant for assessing practical deployability, especially for the 18-layer, 128-unit case (~2300 neurons).

- **The sampling lower bound is described without the caveat that it is a heuristic, not a certificate.** The paper calls it "a lower bound on the true Lipschitz constant" (line 532) but it is computed by evaluating gradients on 200k random points, which can miss higher-Lipschitz directions. While this is a common practice in the literature, a brief clarification that this is an *empirical* rather than *certified* lower bound would improve precision.

### Trivial

- **The paper does not specify the number of random seeds or network instances used per architecture.** If only one instance per configuration was evaluated, results could be idiosyncratic; stating the replication protocol would strengthen reproducibility.

## Nice-to-Haves

- **Comparison against alternative Lipschitz estimation methods for general activations.** The paper could benchmark against general-purpose Lipschitz bounds such as LipMIP (Latorre et al., 2020) or semialgebraic approaches (Chen et al., 2020) to contextualize the SDP's tightness relative to methods outside the LipSDP family. This would strengthen the significance claim but is not required to validate the paper's core contribution (extending LipSDP).

- **Code release.** Making the SDP construction code available would aid reproducibility and adoption.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Proof sketches are too terse; Lemma 2 has no proof sketch."** The paper provides a proof sketch for Lemma 1 (GroupSort) in the main text (lines 213–237). Lemma 2 (Householder) states the result without a sketch, but full proofs would appear in the appendix (stripped by the parser). This is a presentation preference, not a substantive flaw. The paper is self-contained for users who accept the lemma statements.

- **"No comparison against Lipschitz estimation methods that do not require slope-restricted activations."** This is scope-creep. The paper's contribution is extending the LipSDP family; the natural baselines are LipSDP-RR (how existing LipSDP handles these activations) and the product bound. The paper compares against both, plus a sampling lower bound and FGL. Comparing against methods from a different paradigm (semialgebraic, MIP) is a nice-to-have, not a required baseline.

- **"The motivating example would be stronger if it used a trained network."** The single-layer example is sufficient to demonstrate the conservatism of the residual-ReLU representation. It correctly shows that LipSDP on the equivalent ReLU network cannot even certify the known 1-Lipschitz property of MaxMin — which is the exact motivation for the paper.

- **"Missing appendix content, missing proofs in appendix."** The appendix was stripped by the PDF parser; these exist in the original submission.

- **"Only one random seed" as a major concern.** This is noted as a trivial weakness above; it does not rise to the level of a structural issue.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least one experiment with GroupSort (n<sub>g</sub> > 2, e.g., FullSort) or a learned Householder activation** on a small CNN or MLP on MNIST/CIFAR-10, comparing LipSDP-NSR against the product bound and a sampling lower bound. This would directly support the paper's central generality claim.

2. **Provide a small ablation table** (as supplementary or in the main text) comparing ρ from the simplified SDP (S=P=0) against the full parameterization for a few representative networks, to substantiate the claim that the simplification is lossless.

3. **Report SDP solve times** for the largest models in Table 1 (e.g., 18-layer, 128-unit) so readers can assess practical deployability.

4. **Clarify the sampling bound** by noting it is an empirical/heuristic lower bound, not a certified one.
