- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have a comprehensive understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes LIMANS, a linear model of the adversarial noise space where adversarial perturbations are expressed as a linear combination of universal dictionary atoms (D) with example-specific coding vectors (v). The model bridges specific and universal attacks by controlling the number of atoms M: M=1 gives a universal perturbation, while M=500 (still much smaller than the input dimension 3,072) approaches the success rate of specific attacks like AutoAttack. Two stochastic algorithms — Simple-LIMANS (parameter-free) and Regularized-LIMANS (with a tunable regularization parameter) — are presented for learning the dictionary and coding vectors.

## Strengths

- **A principled linear model that demonstrably interpolates between universal and specific attacks**: Figure 2 provides the strongest evidence in the paper. With M=500 atoms, LIMANS achieves fooling rates approaching state-of-the-art specific attacks on CIFAR-10 while optimizing only 500 variables per example instead of 3,072, directly supporting the central claim of reconciling universality and efficiency. The trend as M varies from 1 to 500 cleanly demonstrates the interpolation behavior.

- **Empirical confirmation of a low-dimensional adversarial manifold**: The fact that M=500 (≈16% of the input dimension) suffices to match AutoAttack on CIFAR-10 validates the hypothesis that the adversarial noise space lies in a low-dimensional subspace. This is a meaningful empirical finding independent of any comparison issue.

- **Competitive transferability across diverse classifier architectures**: Tables 2 and 3 show that LIMANS transfers across vanilla classifiers (e.g., from ResNet50 to MobileNet reaching 96.0% FR) and also between vanilla and robust classifiers. The paper explicitly acknowledges dependence on target classifier difficulty and that transferability can hold even when source performance is not maximal — this nuance strengthens rather than weakens the analysis.

- **Two scalable algorithms with different trade-offs**: Simple-LIMANS requires no hyper-parameter tuning (parameter-free), while Regularized-LIMANS provides finer control via λ. Both are presented with clear pseudocode, and the practical suggestion to start with Simple-LIMANS and refine with Regularized-LIMANS is sensible.

## Weaknesses

### Fatal

None.

### Major

- **Detection-robustness comparison against non-adaptive baselines limits the strength of the claim.** The paper claims LIMANS is "more robust to existing adversarial example detectors" and "surpasses these specific attacks" based on Table 1, where baselines are off-the-shelf PGD, FGSM, and AutoAttack — none designed or adapted to evade detection. It is well known that unmodified PGD/FGSM/AutoAttack produce easily detectable perturbations. The paper provides no discussion of this asymmetry. To support a claim that the *model itself* confers detection evasion, the comparison should either include detection-aware variants of the baselines (e.g., PGD with a detection-loss term) or at minimum acknowledge this limitation. The current framing implies a property of the method that the experimental design cannot isolate. (Verifiable from Section 4.2, Table 1 — the paper states "The proposed LIMANS attack surpasses these specific attacks" without caveat about baseline adaptation.)

- **The claim of "visually inspectable atoms that help understand DNN flaws" is stated as a contribution but not substantiated.** Figure 3 visualizes five atoms for VGG11 and robust ResNet-18, noting they "show structure" and are "reminiscent of certain Fourier decompositions." However, no analysis connects these atoms to classifier decision boundaries, gradient information, specific failure modes, or class-wise behavior. The phrase "helps to better understand the DNN flaws" appears in the contribution list (Section 1) and the abstract but receives neither empirical nor theoretical backing. A visualization showing structured patterns is not the same as a method that provides insight into DNN flaws. (Verifiable from the contribution list on line 23: "visually inspectable, helps to better understand the DNN flaws" — and the only supporting evidence in Section 4.2 is the qualitative description in lines 132-138.)

- **Transferability results lack reporting of computational cost, making the comparison incomplete.** LIMANS involves a training phase that optimizes the dictionary over thousands of examples (with many forward-backward passes across minibatches), plus per-example coding vector optimization at inference. The baselines (VNI-FGSM, NAA, RAP) require a small fixed number of gradient evaluations per example. The paper does not report the total number of gradient evaluations, wall-clock time, or any computational budget for LIMANS relative to baselines. Without this information, a reader cannot assess whether the transferability advantage stems from the model's structure or from asymmetric computation. This is a methodological gap, not a fatal flaw — the comparison is not invalid, but it is incomplete. (Verifiable from Section 4.1 and Tables 2-3: resource descriptions mention only hardware, not per-method compute.)

### Minor

- **Claim of "almost comparable performance" with AutoAttack is overstated for the source classifier.** On CIFAR-10 diagonal entries (source→same target), the paper's LIMANS underperforms AutoAttack by a notable margin (text reports this implicitly; e.g., VGG→VGG gap). The paper labels this "almost comparable," which overstates the match. A more precise characterization would strengthen credibility.

- **No discussion of how gradient normalization in Simple-LIMANS (Equation 4) affects learned atom directions.** In Simple-LIMANS, the adversarial noise is normalized to exactly δp before projection, which rescales Dv(i) when ‖Dv(i)‖p ≠ δp. This changes the direction of the perturbation through norm-dependent scaling. The paper does not discuss whether this interferes with learning meaningful atom directions or biases the dictionary in any way.

- **No variance or statistical significance reporting.** All fooling rates and RAUD scores are reported as single values without confidence intervals, standard deviations, or multiple-seed results. Given that some comparisons are close, the significance of differences is unclear.

### Trivial

None.

## Nice-to-Haves

- Reporting the computational cost (gradient evaluations or wall-clock time) for LIMANS training + inference vs. each baseline would allow readers to assess the trade-off.
- An analysis connecting individual dictionary atoms to classifier behavior (e.g., which classes are most affected, correlation with gradient directions) would substantiate the visual-inspection claim.
- Including ℓ∞ results analogous to Figure 2 in the main text (currently deferred to supplementary) would improve self-containedness.

## Removed Points

> These points are flagged to be removed, treat them with caution. They are not included as weaknesses in the main review.

- **"Detector details absent from main text"** (Harsh Critic Point 4): The paper explicitly cites supplementary material for detector choices ("More details about this metric and the considered detector choices are given in the supplementary material"). Since the parser strips supplementary sections from all papers, this criticism reflects a parsing artifact, not an author error. *Removed per Hard Rules.*

- **"Pure formatting/style nitpicks"**: None present.

- **"Transferability comparison is staged / 100× compute speculation"**: The critic's framing ("If LIMANS uses 100× more compute... the comparison is staged") is speculative and not grounded in reported data. The core concern (missing compute reporting) is retained as a Major weakness above, but the speculative "staged" characterization is removed.

- **Strength about visual inspection providing "interpretable insight into classifier flaws"**: This conflicts with the verified weakness that the claim is unsupported. Per the Hard Rules, "when a strength and weakness disagree, the weakness wins." The strength is removed; the weakness is retained in Major.

- **"AutoAttack not designed for transferability"**: This is raised as a concern but the paper does include AutoAttack as a reasonable reference point for comparison, and its inclusion as a baseline is common practice. The paper does not over-rely on this comparison.

## Novel Insights

The Harsh Critic's most valuable observation is the asymmetric comparison in the detection-robustness evaluation — a point that runs deeper than a missing ablation. The paper presents LIMANS as more robust to detectors, but the baseline attacks are not evaluated against detection *by design*. This is not a small oversight: it means the paper's claim about robustness is supported by evidence that cannot distinguish between "LIMANS is inherently harder to detect" and "the baselines selected are trivially detectable." The Strength Finder does not surface this asymmetry. The core modeling contribution (linear dictionary model) and the strongest empirical result (interpolation via M in Figure 2) are genuine, and the transferability results are competitive even accounting for the caveats. The paper's weakest points are the gap between its stated contributions and the evidence supplied for two of them (detection robustness and visual interpretability). The method itself is sound and the central claim is supported.

## Suggestions

1. **Reframe or strengthen the detection-robustness evaluation.** Either (a) rerun the RAUD comparison with detection-aware variants of PGD and AutoAttack (e.g., incorporating a detection loss into the attack objective) so that the comparison tests the model structure rather than the lack of baseline adaptation, or (b) substantially qualify the claim to acknowledge that the current comparison does not control for whether baselines are optimized for evasion.

2. **Report computational cost for the transferability comparison.** Provide the number of gradient evaluations per example (or wall-clock time) for LIMANS (training amortized + inference) and for each baseline. A brief discussion of the computation-performance trade-off would address the fairness concern.

3. **Either substantiate the visual inspection claim or demote it.** If atoms are meant to "help understand DNN flaws," provide analysis: which classes are most affected by each atom? How do atoms correlate with gradient directions? If such analysis is not possible, remove this from the contribution list and present Figure 3 as an exploratory observation.

4. **Add variance estimates.** Report fooling rates over multiple runs or seeds, especially where LIMANS and baselines produce close numbers.
