## Summary

This paper proposes a method to estimate the nonlinear coherence (a frequency-domain causality metric) between the input and output of a nonlinear dynamical system from noisy measurements, using only an imperfect forward model and a small amount of data (10 frames). The key idea is to exploit the structural property of a broad class of second-order nonlinear ODEs (Eq. 2) where the reverse mapping from output back to input is simpler than the forward mapping. By learning a frequency-dependent combination parameter K(f) that blends the noisy measurement with the model prediction, and using a tiny CNN to map the combined signal back to the input, the method derives the nonlinear coherence via an algebraic relationship between K and the noise-to-model-error ratio.

## Strengths

1. **Novel method that estimates nonlinear coherence without a perfect forward model.** The paper correctly identifies that existing methods "generally rely on a perfect forward model" (line 55), whereas this approach needs only an approximate model. The simulations demonstrate this across three different nonlinearity types: even when the forward CNN captures only 65–94% of the response, the method estimates the coherence with reasonable accuracy (Sections 4.1–4.3).

2. **Exploits a genuine structural insight about the reverse mapping of a broad ODE class.** The observation that for systems of the form in Eq. (2), the mapping from y back to x is simpler than the forward mapping because "there is no nonlinear mixing of terms in time in the reverse direction" (lines 69–70) is clever and well-motivated. This insight is what enables the method to use a remarkably small CNN (5 layers, kernel width 7, 5 features, only 778 parameters) across all test cases (line 105).

3. **Validated on a real experimental dataset with strong nonlinearity.** The experimental setup (Section 5) — a cantilever with magnets and rubber tip causing uncharacterized rattling, where the linearized response captures only 45% and a CNN captures just 74% — provides the most compelling evidence. The method tracks the true nonlinear coherence across three noise levels (Figure 9), demonstrating practical applicability where no other method could produce this estimate without a perfect model.

4. **Extremely data-efficient.** The method consistently uses only 10 frames of data (lines 160, 172, 194, 202, 221), which is a concrete practical advantage for feasibility assessment in applications like active noise reduction.

## Weaknesses

### Major

1. **The λ-selection mechanism is an unprincipled heuristic at the core of the estimation pipeline.** The paper's theoretical derivation (Eqs. 7–8) shows that the optimal K minimizes E[|Ŷ−Y|²] and depends on the ratio of noise to model-error power. The claim is that training the architecture to predict x from ŷ (with λ=0, minimizing only L_x) should yield this optimal K because "the architecture will implicitly estimate the ratio of errors" (line 96). However, the paper then concedes that "in practice, λ=0 does not yield the optimal K" (line 98) — the estimated K is "usually smaller than the true value" (line 152). The proposed fix (introducing λ and tuning it via a heuristic threshold of 0.01 on validation loss, with 100-epoch training increments) has no theoretical justification. The paper itself states this "worked well empirically" and calls for "an interpretable method for setting λ" (lines 237–238). A practitioner applying this method to a new system has no principled way to know whether the estimated coherence is accurate, because the mechanism that makes it work is not grounded. This is the most significant weakness.

2. **No quantitative error metrics.** The paper makes strong claims of "excellent prediction" and "excellent accuracy" (lines 172, 209, 232, 246) based entirely on visual inspection of coherence curves in four figures. There are no reported quantitative error measures (e.g., mean absolute error or mean squared error between predicted and true coherence, integrated over frequency) for any of the 12 conditions (4 systems × 3 noise levels). Without numerical metrics, it is impossible to assess whether the claimed performance is robust or coincidental, and cross-paper comparison is not possible.

3. **No uncertainty quantification.** With only 10 frames of data, spectral estimates have inherently high variance, and the additional variance from training a CNN on such limited data compounds this. Yet no confidence intervals, error bars, variance across trials, or bootstrap estimates are reported. This is particularly concerning because the method involves a stochastic training procedure with multiple hyperparameters (λ threshold, training schedule, learning rate).

### Minor

4. **Insufficient baselines and ablations.** The paper compares its estimate against the forward CNN prediction and the linear coherence (shown in Figure 4, line 172), but these do not demonstrate that the method's specific machinery is necessary. Missing ablations include: fixing K to a constant value (e.g., K=0.5), fixing K based on a global SNR estimate, or testing whether simpler reverse mappings (e.g., linear regression) could achieve similar results. Such baselines would strengthen the claim that the proposed architecture's complexity is warranted.

5. **Artificial noise in the experimental validation weakens the demonstration.** While the paper explains that mechanical noise would be correlated with the input and thus artificial post-processing noise is used (line 221), this means the "true" nonlinear coherence is known by construction (it is the coherence between the noise-free signal and the artificially noised signal). The method's main claimed advantage is distinguishing model error from noise in settings where the true coherence is *not* known. A demonstration with genuinely physical, uncorrelated noise would be stronger, though the practical difficulty is acknowledged.

### Trivial

- None

## Nice-to-Haves

- A sensitivity analysis of the λ threshold (0.01) and training schedule (100 epochs per λ step) across a range of values would help assess robustness.
- Reporting quantitative comparison metrics (e.g., integrated absolute error) for all test cases would substantially strengthen the evaluation.
- Code release would significantly improve reproducibility and adoption.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No meaningful baselines are compared"** — Partially removed. The paper *does* show linear coherence as a comparison (line 172: "the linear coherence between x and y_n (solid green line)"). However, the absence of ablations (fixing K, alternative estimation schemes) is retained as a minor weakness.
- **"Major omission: paper never uses analytical structure of reverse mapping"** — Removed. The paper says the reverse mapping is "relatively simple" (line 69), not known in closed form. Using a small CNN to learn it is an appropriate methodological choice, not an omission.
- **"Reproducibility statement empty"** — Removed. Per review policy, these sections are stripped by the parser and exist in the original submission.
- **"Forward model training details not specified"** — Partially removed. The paper does specify kernel width, layers, features, epochs, and learning rate for each case. However, the split of 10 frames between forward model training and main method training is unclear.
- **"Scope creep" criticisms about neuroscience/economics applicability** — Removed. The paper scopes its claims to the system class in Eq. 2, which is appropriate. The conclusion's mention of "structural dynamics to neuroscience" is a standard aspirational statement.
- **Strength: "Explicitly identifies and discusses the key limitation"** — Removed. Generic/superficial; most papers discuss their limitations.

## Novel Insights

The most interesting observation from the reviews is that the paper's central methodological challenge — λ selection — mirrors the very problem the method aims to solve: distinguishing signal from noise in an unsupervised way. The paper effectively replaces the original problem (estimating nonlinear coherence without a perfect model) with a proxy problem (finding λ where the validation loss starts rising). This reformulation is practically useful but the lack of a principled connection between the two problems is the paper's deepest flaw. An alternative framing that connects λ to a meaningful statistical quantity (e.g., a regularization strength tied to an estimated noise level) could transform this from a heuristic into a well-founded method.

## Suggestions

1. **Add quantitative error metrics** for every test case and noise level. A simple table with integrated MAE or MSE between predicted and true coherence would dramatically strengthen the evidence.
2. **Add uncertainty quantification** via bootstrap or multiple runs with different noise realizations to show confidence bands around the coherence estimates.
3. **Include ablation studies** — e.g., fixing K=0.5, fixing K based on global SNR, or using a linear reverse mapping — to justify the method's specific machinery.
4. **Provide a principled justification or sensitivity analysis for λ selection.** At minimum, show how the coherence estimate varies with λ near the chosen threshold across multiple test cases.
5. **Clarify the data split.** Specify how the 10 frames are allocated between forward model training and the main method's training/validation.

## Score and Decision

**Score:** 4.5

**Decision:** Reject

The paper presents a genuinely novel and clever idea with promising qualitative results, including on a real experimental system. However, at ICLR standards, a methods paper requires either stronger theoretical grounding or more rigorous empirical validation. The λ-selection mechanism is a heuristic with no principled justification, the evaluation lacks any quantitative error metrics or uncertainty quantification, and the baselines are insufficient to establish that the specific method is necessary rather than merely sufficient. These gaps combine to make the contribution — while interesting — not yet convincing enough for acceptance at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>