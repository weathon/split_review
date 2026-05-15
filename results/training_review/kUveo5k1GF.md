Here is my consolidated final review:

## Summary

This paper studies bias in equilibrium propagation (EP) when applied to non-symmetric dynamical systems. It provides a theoretical decomposition isolating two sources of gradient bias — finite nudge amplitude and Jacobian asymmetry — and proposes a novel "homeostatic loss" that penalizes the skew-symmetric part of the Jacobian at the fixed point, without requiring perfect weight symmetry. The authors demonstrate that combining generalized holomorphic EP (hEP) with this homeostatic loss dramatically improves performance on CIFAR-10 (60.4% → 84.3% top-1 accuracy) and achieves 31.4% top-1 on ImageNet 32×32 with only a small gap from the symmetric case.

## Strengths

1. **Clean theoretical isolation of bias sources.** Equations (11) and (12) provide a precise relationship between the hEP error vector, the RBP error vector, and the skew-symmetric part of the Jacobian (A). This decomposition cleanly separates finite-nudge bias from asymmetry bias, which prior work had conflated. The relation `dudβ = J^{-1}J^T δ` and its first-order expansion `dudβ = δ - 2S^{-1}Aδ + o(S^{-1}Aδ)` are important framing contributions.

2. **A genuinely novel loss targeting Jacobian symmetry, not weight symmetry.** The homeostatic loss `L_homeo = E[‖Jε‖² − εᵀJ²ε]` is designed to minimize ‖A‖² without enforcing any particular weight structure. The paper verifies this theoretically (the loss equals 2‖A‖²_F as shown via the trace identities in Section 3.4) and empirically (the symmetry measure `‖S‖/(‖S‖+‖A‖)` increases during training). The demonstration that this loss works even in an architecture where symmetric feedback is impossible (Figure 3e–h) is a clean control that confirms the loss's generality beyond reciprocal weight connections.

3. **Large performance improvements on real benchmarks.** The CIFAR-10 jump from 60.4% to 84.3% top-1 accuracy with the homeostatic loss is striking. The gap to the symmetric hEP baseline (88.6%) is only 4.3%, meaning the method recovers most of the performance lost due to asymmetry. The CIFAR-100 results (35.2% → 53.8% top-1) follow the same pattern. These are substantive empirical contributions given that prior asymmetric EP approaches failed on CIFAR-10 entirely (as the paper notes).

4. **Continuous-time formulation suitable for physical substrates.** Section 3.2 provides a time-continuous estimate of both `dudβ` and the gradient itself (Eqs. 8–10), eliminating the need for separate free/nudged phases. The continuous-time experiment (Table 1, 17.3% error vs. 14.3% with N=6) shows it works reasonably well, which is valuable for neuromorphic hardware realizations.

## Weaknesses

### Fatal
None.

### Major

1. **The full oscillatory hEP method is not demonstrated at scale.** The ImageNet 32×32 results (Table 2) use "True dudβ" (automatic differentiation), not the oscillatory Cauchy-integral estimation (N=2, N=4) that the paper presents as the method for removing finite-nudge bias without weight symmetry. The oscillatory hEP is only shown on Fashion MNIST (Table 1) and on CIFAR-10 with N=2 (81.4% vs. 84.3% with True dudβ). The paper's claim that "our strategy allows training deep dynamical networks without perfect weight symmetry on ImageNet 32×32" is technically true of the *combination* of hEP + homeostasis, but the oscillatory *estimation* component of hEP was not evaluated at scale. The CIFAR-10 N=2 result suggests the gap would be small, but this is a meaningful gap between the paper's strongest claim and the provided evidence.

2. **Missing hyperparameter and ablation for the homeostatic loss.** The paper never specifies how the homeostatic loss `L_homeo` is weighted relative to the task loss (no λ coefficient is reported). Without this, the reported gains (60.4% → 84.3%) could depend critically on an unstated hyperparameter. Furthermore, the two terms in `L_homeo` — `E[‖Jε‖²]` (Jacobian norm minimization) and `−E[εᵀJ²ε]` (trace maximization) — are never ablated separately. We cannot tell whether the improvement comes from symmetry improvement specifically, or from the Jacobian norm term acting as a generic regularizer (e.g., improving conditioning). This is the most significant experimental gap.

### Minor

1. **Limited experimental details for reproducibility.** The CIFAR-10, CIFAR-100, and ImageNet experiments do not report data augmentation, batch size, learning rate schedule, optimizer hyperparameters, or weight decay. This makes independent reproduction unnecessarily difficult. These details are standard to include even in a main paper (or appendix, which appears absent from the PDF).

2. **The first-order expansion lacks stated validity conditions.** Equation (12) — `dudβ = δ − 2S⁻¹Aδ + o(S⁻¹Aδ)` — is presented without discussing when the Neumann series converges (i.e., when `‖S⁻¹A‖ < 1`). While the `o()` notation makes the statement technically correct as a formal expansion, the paper would benefit from acknowledging this condition, especially since the magnitude of A relative to S is central to the paper's claims.

3. **No direct gradient-error measurement.** The paper relies on cosine similarity between error vectors (δ and dudβ) as the main diagnostic for bias. While cosine similarity is a meaningful proxy (gradients are `dF/dθᵀ·error_vector`, shared across methods), a direct measurement of gradient error — e.g., `‖g_hEP − g_RBP‖/‖g_RBP‖` as a function of ‖A‖ — would strengthen the causal claim that asymmetry reduction drives performance improvement. The current evidence is correlational (homeostasis → symmetry ↑, cosine ↑, accuracy ↑).

### Trivial

- The description of the two loss terms as "should be minimized" / "should be maximized" (Section 3.4) could be clarified to emphasize that the overall loss is a *difference*, so these are not independent objectives. (The text is technically correct — in `L = term1 − term2`, minimizing L means minimizing term1 and maximizing term2 — but a reader could misread it.)
- Table 2 shows "—" for hEP w/o homeostasis on ImageNet. While this is standard notation, explicitly stating "training did not converge" or "accuracy < 10%" would be more informative.

## Nice-to-Haves

- Ablation of the two terms in `L_homeo` separately, to confirm the performance gain is attributable to symmetry improvement (the `−E[εᵀJ²ε]` term) rather than pure Jacobian norm shrinkage.
- A direct measurement of `‖A‖/‖J‖` dynamics during training with and without homeostasis (the symmetry measure in Figure 3 is already useful; eigenvalue spectra would add further insight).
- Application of the oscillatory hEP (N=2 or N=4) with homeostasis to CIFAR-100 to demonstrate that the *complete* method (not just exact-gradient hEP) scales beyond MNIST-scale.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The central mathematical justification for the homeostatic loss is not provided."** — The paper states the identity `‖A‖² = ½tr(JᵀJ) − ½tr(J²)` (line 218) and defines `L_homeo = E[‖Jε‖² − εᵀJ²ε]`. The step from the expectation to the trace (`E[εᵀMε] = tr(M)` for standard Gaussian ε) is standard. The derivation is implicitly present; the paper could add one more line of algebra for clarity but this is not a "structural" flaw.

- **"Table 1 lacks symmetric baseline."** — Table 1's purpose is to validate that hEP estimation matches ground-truth automatic differentiation. A symmetric baseline is irrelevant to this question.

- **"Section 3.1 extension is mathematically trivial."** — This is a subjective opinion, not a factual weakness.

- **"Table 2 does not show ImageNet results without homeostasis."** — The "—" is standard notation for methods that failed to train. The paper explicitly notes (line 41–42, 353) that asymmetric EP fails on larger datasets without homeostasis.

- **"The homeostatic loss is missing a critical hyperparameter"** — This is kept as a major weakness but the reviewer's phrasing (that the results "could be arbitrarily dependent on an unstated hyperparameter") overstates the case. The 60.4%→84.3% gap is so large that it is unlikely to be artifact of fine-tuning; however, the missing λ is still a genuine reproducibility gap.

## Novel Insights

The reviewer's observation that the paper's strongest scaling claim (ImageNet) relies on the exact-gradient variant rather than the oscillatory hEP is an insightful catch that identifies a genuine gap between claim and evidence. Conversely, the reviewer's assertion that the homeostatic loss derivation is missing is itself incorrect — the mathematical steps are present in the paper, albeit compactly. The most constructive insight from the reviews is that the paper should have ablated the two terms of the homeostatic loss separately, as this would directly address whether performance gains come from symmetry improvement or generic regularization, and would make the causal story complete.

## Suggestions

1. Add a hyperparameter λ (or equivalent) for the homeostatic loss weight to all experiments, and report its value. Include a sensitivity sweep on CIFAR-10.
2. Ablate the two terms of `L_homeo` separately: (i) full loss, (ii) `E[‖Jε‖²]` only, (iii) social `−E[εᵀJ²ε]` only. Show that the full loss outperforms either term alone, confirming synergy.
3. Demonstrate the oscillatory hEP (N=2) with homeostasis on CIFAR-100 or ImageNet 32×32 to close the gap between the claimed full method and the demonstrated results. If this is computationally prohibitive, clearly state this as a limitation rather than implying the full method scales.
4. Add standard training details (optimizer, learning rate schedule, batch size, data augmentation) for all experiments in the main paper or appendix.
5. Optional but strengthening: add a direct gradient-error measurement (`‖g_hEP − g_RBP‖/‖g_RBP‖` across training steps) with and without homeostasis.

## Score and Decision

The paper makes genuine contributions: it provides the first clean decomposition of finite-nudge vs. asymmetry bias in generalized EP, proposes a novel and well-motivated homeostatic loss that targets Jacobian symmetry rather than weight symmetry, and demonstrates large empirical improvements on CIFAR-10/100 and ImageNet 32×32. The weaknesses are real — the full oscillatory method is not shown at scale, the loss weighting hyperparameter is missing, and ablations are absent — but none are fatal. The core theoretical and algorithmic contributions are solid, and the experimental gaps are addressable with moderate revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>