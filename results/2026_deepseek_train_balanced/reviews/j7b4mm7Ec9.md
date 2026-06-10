Here is my final consolidated review:

---

## Summary

This paper analyzes limitations of lightweight deep watermarking models by decomposing the MSE decoding loss into three components — deflation, inflation, and regularization — and argues that only the deflation component directly reduces decoding error while the others "consume model parameters" without helping accuracy. It proposes two remedies: a Detachable Projection Head (PH) that absorbs decoding-irrelevant gradients during training and is discarded at inference, and a Decoding-Oriented surrogate loss (DO) that limits inflation loss to bits near the decision boundary. The paper also introduces a five-module conceptual framework and instantiates a model with only 16.59K parameters that achieves competitive or superior robustness (99.36% average accuracy) against substantially larger prior models.

## Strengths

- **Formal decomposition of MSE into functionally interpretable components (Equation 3, Section 2.2).** The paper analytically partitions MSE into $\mathcal{L}_{deflation}$, $\mathcal{L}_{inflation}$, and $\mathcal{L}_{regularization}$, showing that only $\mathcal{L}_{deflation}$ directly penalizes decoding errors. This provides a principled lens for understanding why surrogate losses may be wasteful for lightweight models — a diagnosis absent from prior watermarking literature.

- **Ablation study (Table 5, Section 4.4) empirically validates the diagnosis.** Training with $\mathcal{L}_{deflation}$ alone outperforms the full MSE loss on robustness, while $\mathcal{L}_{inflation}$ and $\mathcal{L}_{regularization}$ in isolation yield near-zero accuracy. This directly supports the paper's central claim that the non-deflation components are detrimental in the lightweight setting.

- **Extreme parameter reduction with competitive performance (Table 1, Table 2).** The model uses 16.59K parameters total (2.2% of HiDDeN's 454.40K, 0.05% of CIN's 36M) and achieves 99.36% average accuracy against combined noise, outperforming all baselines including much larger models. This is a genuine engineering contribution.

- **Comparison against knowledge distillation baselines (Table 3, Section 4.2).** The paper shows that PH and DO outperform KD-based compression of the same architecture across all distortions, establishing that direct loss modification is more effective than distillation for this setting.

## Weaknesses

### Fatal
None.

### Major

1. **Critical experimental details are omitted, undermining reproducibility and comparison.** The paper never states which dataset was used, what image resolution was employed, what message length $L$ was, or any training hyperparameters (learning rate, batch size, number of epochs, optimizer, scheduler). The balancing weights $\lambda_1$ and $\lambda_2$ for both PH and DO are never given values, and the key DO hyperparameter $\epsilon$ (safe distance) is never specified or analyzed. Without these details, the reported results cannot be reproduced, verified, or meaningfully compared against future work. This is a fundamental omission for an empirical paper claiming SOTA performance.

2. **Section 4.3 evaluates a Gaussian+median filter proxy but claims robustness against specific diffusion-based purification attacks (PRGAI, DiffPurE).** The paper acknowledges that "utilizing a diffusion model as a noise layer is impractical" and instead uses a composite of Gaussian noise and median filtering to "simulate this type of attack." The results are then reported as "nearly perfect robustness against the PRGAI attack" and specific accuracy numbers for "the DiffPurE attack" (Section 4.3, lines 193-195). Gaussian noise followed by median filtering is not a diffusion-based purification pipeline — it lacks iterative denoising, score-function estimation, or any characteristic of diffusion-based purification. The evaluation does not support the claimed conclusions about robustness against diffusion-based attacks. This is a disconnect between evidence and claims.

### Minor

3. **The central "parameter consumption" claim (Section 2.2, line 67) is asserted without direct evidence.** The paper states that inflation and regularization losses "inevitably occupy some model parameters, particularly limiting the performance of lightweight models." The ablation study (Table 5) shows that removing these components improves performance — this is consistent with the claim but does not demonstrate that parameters are specifically "consumed" by those loss components (e.g., via gradient analysis, parameter sensitivity, or effective capacity measurements). The practical result stands, but the stated mechanism remains a conjecture.

4. **The five-module framework (Section 3.2) is claimed as a contribution but never empirically validated.** The paper decomposes the encoder/decoder into IP, MP, FF, NWIP, and ME modules, and the conclusion claims that "ablation studies reveal effective module selection strategies for different distortions." However, no experiment in the paper selectively removes or ablates these modules. The framework is described and then never operationalized. As presented, it is a taxonomy, not an empirically supported contribution.

5. **The Detachable Projection Head mechanism (Section 3.1) is functionally described but not rigorously analyzed.** The paper asserts that the projection head absorbs "decoding-irrelevant optimization directions" during training, but offers no analysis (e.g., gradient norm comparison, parameter sensitivity) to substantiate this specific claim. The explanation is plausible but unsubstantiated relative to alternative interpretations (e.g., the PH simply provides extra capacity that matters during training).

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis for the DO method's $\epsilon$ hyperparameter, which the paper acknowledges requires manual tuning.
- Reporting variance or confidence intervals across multiple runs for accuracy and PSNR.
- Clarification of the input resolution used for FLOPs computation, which the paper reports but cannot be interpreted without this context.

## Removed Points

*These points were flagged for removal during filtering; treat them with caution.*

- **Criticism that KD comparison is a "straw man."** The harsh critic claimed that KD addresses a different problem, making the comparison uninformative. This is incorrect — both KD and PH/DO are valid approaches for obtaining lightweight models, and the comparison is informative. Removed as an invalid criticism.
- **Strength that five-module framework "enables selective compression by distortion type."** The Strength Finder attributed empirical validation to the framework that the paper does not actually provide (no module-level ablation is performed). Moved here because it overclaims what the paper demonstrates.
- **Criticism that the paper's observation about surrogate loss mismatch "is not novel."** The high-level observation about surrogate loss gaps is standard, but the specific decomposition into three components for the watermarking MSE loss and the ablation supporting each component's role is novel. The criticism in this framing was removed as overly dismissive of a genuine analytical contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective on the work that the paper itself does not already articulate.

## Suggestions

1. Add a complete experimental specification: dataset, image resolution, message length, all hyperparameters (with values), and the $\epsilon$ value used in DO experiments. Include variance or confidence intervals for all reported metrics.
2. Either evaluate against actual diffusion-based purification pipelines (even a single configuration) or reframe Section 4.3 to honestly describe the evaluation as robustness against a Gaussian+median composite noise layer — removing all claims about PRGAI and DiffPurE specifically.
3. Either validate the five-module framework with actual module-level ablation experiments, or downgrade its status from a claimed contribution to a descriptive taxonomy.
4. Provide direct evidence for the "parameter consumption" claim, or reframe the paper's motivation around the supported observation that $\mathcal{L}_{deflation}$ alone suffices with careful stabilization.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>