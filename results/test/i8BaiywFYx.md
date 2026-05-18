Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper proposes a symmetrization method for multi-class loss functions: subtracting the per-class average of a loss to obtain its symmetric component (Proposition 4.1). Applying this to cross-entropy yields a multi-class unhinged loss, which the authors prove is the unique convex, non-trivial, non-increasing symmetric loss under permutation invariance (Theorem 5.1). Building on this, they introduce SGCE (symmetric GCE) and α-MAE — loss functions that interpolate between the unhinged loss and MAE — and demonstrate competitive empirical performance on CIFAR-10/100, CIFAR-10N/100N, and WebVision under various noise types.

## Strengths

- **Principled symmetrization framework (Proposition 4.1)**: The paper provides a clean, general decomposition of any multi-class loss into a symmetric component and a class-insensitive term, offering a systematic way to generate symmetric (hence noise-robust) losses from arbitrary base losses. This is more general than the normalization approach of Ma et al. (2020).

- **Uniqueness of the multi-class unhinged loss (Theorem 5.1)**: The paper proves that the multi-class unhinged loss is the unique convex symmetric loss under natural conditions (non-increasing, permutation-invariant, non-trivial), extending the binary result of van Rooyen et al. (2015) to the multi-class setting. The permutation-invariance assumption is a key enabler for this extension.

- **Novel loss functions SGCE and α-MAE**: These losses smoothly interpolate between the multi-class unhinged loss and MAE using a single hyperparameter, enabling practitioners to trade off between the unhinged loss's gradient-strengthening of clean examples and MAE's gradient-attenuation of potentially corrupted examples. α-MAE is shown to resolve MAE's underfitting issues on CIFAR-100.

- **Linear approximation insight (Section 5.2)**: The observation that any symmetric loss is locally equivalent to the multi-class unhinged loss at equal-component points (Proposition 5.2), and that CE is locally unhinged around such points, provides a unified explanation for why CE can exhibit some noise robustness with early stopping.

- **Strong empirical validation**: The experiments cover symmetric noise (40%–80%), asymmetric noise, and natural noise (CIFAR-10N/100N), comparing against seven prior robust loss functions. α-MAE in particular achieves consistently top results on the realistic noisy benchmarks CIFAR-10N/100N.

- **Practical handling of unboundedness (Section 7.2)**: The paper addresses the numerical instability of the unbounded unhinged loss through Euclidean normalization and batch normalization, demonstrating which works better under different learning rate schedules.

## Weaknesses

### Fatal
None.

### Major
None. The core claims — the symmetrization method, the uniqueness result, the derived loss functions, and the empirical competitiveness — are all soundly supported. The issues below are substantive but do not invalidate the contribution.

### Minor

- **Overclaimed "superior performance" in the abstract**: The abstract claims "superior performance over previous state-of-the-art robust loss functions on standard benchmarks." However, the paper's own results (Table 1) show that SGCE is sometimes outperformed by ANL-CE (e.g., on CIFAR-100 with 80% symmetric noise). The conclusion more accurately uses "competitive performance." The abstract's phrasing is an overstatement that should be tempered. This does not undermine the paper's value — the results are strong — but the claim should match the evidence.

- **Gap between theory and practice due to normalization (Section 7.2)**: The theoretical guarantees (symmetry, uniqueness of the unhinged loss) are established for losses defined on the raw score vector z. However, the practical implementation requires Euclidean or batch normalization of the score vector to prevent unbounded values. The paper does not discuss whether the symmetric loss property, the uniqueness result, or the noise-robustness guarantee holds for the normalized scores, or whether normalization introduces unintended consequences. This disconnect weakens the claim that the empirical results directly validate the theory.

- **Proposition 5.3 bound is too loose to be practically meaningful**: The bound in Proposition 5.3 depends on c^(2(l-1)), which is exponential in network depth. For networks beyond a few layers (e.g., ResNet-34 used in experiments), this term makes the bound astronomically large, providing no meaningful constraint. The paper does not acknowledge this limitation or discuss whether the bound has any practical relevance for the architectures used.

- **Missing hyperparameter sensitivity analysis**: Hyperparameters (q for SGCE, α for α-MAE) were tuned on 80% symmetric noise and applied unchanged to all other noise settings (asymmetric, lower symmetric rates, natural noise). While this is a defensible choice to avoid overfitting, the paper does not report how sensitive the results are to these hyperparameter choices across different noise regimes. A simple sensitivity plot would significantly strengthen the empirical case.

- **Clarity on baseline comparison protocol**: The paper states that weight decay was tuned separately for each loss function, whereas Ye et al. (2023) did not. This introduces a confound: reported gains may partly reflect better weight decay tuning rather than the loss function itself. The paper should explicitly state whether all baseline numbers were recomputed using the same tuned-weight-decay protocol, and if so, report the tuned weight decay values for each baseline. Currently this is ambiguous.

- **Incremental theoretical novelty**: Theorem 5.1 extends the known binary unhinged uniqueness result (van Rooyen et al., 2015) to the multi-class case under the additional invariance-to-permutations assumption. This is a correct and useful extension, but the conceptual gap from binary to multi-class is modest once the permutation invariance condition is imposed. The paper positions this as a central result, which exaggerates its novelty relative to prior work.

### Trivial

- Only SGCE (not α-MAE) is reported in the WebVision results (Table 3). Including α-MAE would be informative, though the omission is not a flaw in the existing results.

## Nice-to-Haves

- A direct ablation comparing GCE vs. SGCE and MAE vs. α-MAE while holding all other training details fixed, to isolate the effect of symmetrization from the interpolation hyperparameter.
- A brief theoretical or empirical comment on how Euclidean/batch normalization affects the symmetry property of the loss, even if only approximate.
- Sensitivity analysis of the hyperparameters (q, α) across different noise regimes.
- Discussion of the computational cost (gradient computation differences) of the proposed losses versus standard alternatives.

## Removed Points

The following criticisms were removed per the review guidelines:

- **"The symmetrization method is mathematically trivial"**: This is a qualitative judgment about novelty, not a factual error. The paper does not claim the formula is complex; it claims it is principled. However, the related point about the incremental nature of the theoretical contributions is retained as a minor weakness (see above). The "trivial" framing is removed.
- **Criticism that the paper should symmetrize the hinge loss**: This is a suggestion to extend the paper in a different direction, not a flaw in what the paper actually does. Scope-creep requests are removed per guidelines.
- **Criticism that Proposition 5.2 "formalizes what one would expect"**: This is a subjective opinion about obviousness. The proposition is mathematically correct and non-trivial to prove; the objection is aesthetic, not substantive.

## Novel Insights

The reviewer's most valuable observation is the tension between the clean theoretical framing (symmetry in raw z-space) and the practical normalization step. This identifies a genuine gap — the paper's theory operates on unnormalized scores while its experiments use normalized ones — that is worth flagging but does not invalidate the paper. The symmetrization method's generality (applicable to any base loss) and the local-to-unhinged approximation result (Proposition 5.2) remain the paper's strongest conceptual contributions beyond its own claims.

## Suggestions

1. **Temper the abstract's claim**: Replace "superior performance" with "competitive performance" or "state-of-the-art or competitive performance" to match the evidence in Tables 1–4.
2. **Clarify the baseline comparison**: Explicitly state whether all baselines were recomputed with tuned weight decay, and report the tuned weight decay values used.
3. **Add hyperparameter sensitivity results**: A figure or table showing accuracy as a function of q/α for different noise rates would strengthen the empirical case.
4. **Discuss the normalization gap**: Add a brief discussion (even a paragraph) addressing whether and how the theoretical guarantees degrade or hold after score normalization. If the normalized losses remain symmetric in the normalized space, state this explicitly.
5. **Acknowledge the limitation of Proposition 5.3**: Note that the bound depends exponentially on depth and is loose for deep networks, making it primarily a conceptual guarantee rather than a tight practical bound.

## Score and Decision

The paper presents a clean theoretical framework for symmetrizing loss functions, proves a meaningful uniqueness result for the multi-class unhinged loss, derives two new loss functions (SGCE and α-MAE) that perform competitively across diverse noise benchmarks, and provides thorough experimental validation. The issues identified — overclaiming in the abstract, a theory-practice gap from normalization, looseness of one theoretical bound, and some missing analyses — are all addressable in revision and do not undermine the core contribution. The paper makes a solid contribution to the robust loss function literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>