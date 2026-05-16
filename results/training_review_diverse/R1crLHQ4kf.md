Now I have a thorough understanding of the paper and have cross-checked all claims. Let me write the final consolidated review.

## Summary

This paper proposes a detection method for adversarial examples in end-to-end ASR systems by extracting six statistical characteristics (median, min, max, entropy, KL divergence, JSD) from the output probability distribution at each time step, aggregating them into scores, and feeding them into binary classifiers (Gaussian classifiers, ensembles, neural networks). Evaluated on three ASR architectures (wav2vec, LSTM, Transformer) across four languages and multiple attack types, the method achieves high AUROC on targeted attacks and outperforms noise flooding and temporal dependency baselines.

## Strengths

1. **Consistently high detection performance on targeted attacks**: The method achieves AUROC exceeding 99% on clean data and 98% on noisy data for C&W and Psychoacoustic attacks across all tested ASR models (Table 4). This directly supports the core claim, and the gap over baselines (NF, TD) is substantial (e.g., NN at 99.14% vs. TD at 82.00% on clean data).

2. **Broad and realistic experimental scope**: The evaluation covers three distinct ASR architectures (wav2vec-CTC, LSTM-LAS, Transformer), four languages (English, Chinese, German, Italian), multiple tokenizer sizes (32 to 21,128), and both clean and MUSAN-corrupted noisy conditions. This breadth meaningfully supports the claim of general applicability.

3. **Efficiency and model-agnostic design**: The detector adds only ~18.74 ms per sample on an A40 GPU and requires no model retraining, data preprocessing augmentation, or access to the ASR model's internal gradients—making it practical for real-time deployment with any ASR system that outputs token-level probability distributions.

4. **Transferability across attack types**: Detectors trained solely on C&W targeted attacks generalize to Psychoacoustic targeted attacks and achieve AUROC >90% for Kenansville untargeted attacks (Table 6), demonstrating robustness beyond their training attack distribution.

## Weaknesses

### Fatal
None.

### Major

1. **Missing direct experimental comparison with the most closely related prior work (Däubener et al., 2020)**. The paper correctly cites Däubener et al. (2020) and acknowledges they used two of the same characteristics (mean KL divergence, mean entropy) for detection in hybrid ASR systems, yet does not include a direct comparison. Adapting their uncertainty-based detector to E2E systems would be a straightforward baseline that isolates the added value of the additional characteristics (median, min, max, JSD) and the multi-lingual E2E evaluation. Without this, the claim of "surpassing the leading temporal dependency technique and the noise flooding method" compares against baselines that the paper itself describes as limited (NF: 10-word classification; TD: evadable by Zhang et al., 2020), rather than against the method with the most feature overlap.

2. **The neural network detector is trained on a critically small dataset with high overfitting risk**. The paper selects 200 samples total, uses 100 for testing, and the remaining ~100 for training the NN, fitting all Gaussian classifiers, and threshold selection. The NN has three layers of 72 hidden nodes each (~12K parameters) and is trained for 250 epochs on ~100 samples with no reported training/validation split, learning curves, or regularization. This makes the NN results (which the paper recommends as a top performer) potentially unreliable. The paper should at minimum report validation performance or cross-validated metrics.

### Minor

3. **No uncertainty quantification on any metric**. All AUROC and accuracy values are reported to two decimal places without confidence intervals, bootstrap estimates, standard deviations across multiple splits, or statistical significance tests. With 100 samples per class, a few misclassifications can shift AUROC by several points. While the very high AUROC values (99%+) are unlikely to reverse the qualitative conclusion (even a pessimistic lower bound would still exceed baselines), the absence of variance reporting undermines the precision implied by the reported numbers and makes comparative claims like "surpasses" unquantified.

4. **Contradiction in the genetic attack dismissal**. The paper reports AUROC as low as 46% for genetic attacks (near random) and dismisses this by stating genetic attacks are "characterized by noise, making them easily noticeable by human hearing." However, Table 3 reports a genetic attack SNR of 43.37 dB—not particularly low. No human listening test or perceptual analysis is provided. The paper's own data does not support the claim that genetic attacks are perceptually noisy, making this dismissal of a clear failure case unconvincing.

5. **Adaptive attack narrative conflates two distinct defenses**. When the proposed detection method degrades under adaptive attacks, the paper introduces filtering-based detection (low-pass filtering, spectral gating) as a salvage mechanism and presents it as "another avenue for preserving the system's robustness." While the paper does not explicitly claim filtering is part of the proposed method, the narrative structure presents this as a positive outcome of the analysis rather than acknowledging that the core proposed method is not robust to adaptive attacks. The filtering approach is a completely separate defense that could be applied regardless of the output-distribution classifiers, and the two are never evaluated as an integrated system.

### Trivial

6. **Notation inconsistency in adaptive attack formulation**. The loss term \(l_s^c(x)\) in Eq. 2 uses a superscript \(c\) that is not defined until the following paragraph, and its meaning shifts across classifier types.

## Nice-to-Haves

- An ablation study progressively adding characteristics (entropy alone, then KL divergence, then median, etc.) would isolate which features drive performance and whether the full set of 6 characteristics × 4 aggregation functions is necessary.
- Computational overhead comparison with baselines (NF and TD) to contextualize the reported 18.74 ms.
- Justification or ablation of the "equal number of tokens" target selection criterion, which may artificially limit attack difficulty.
- A dedicated limitations section acknowledging the small-sample evaluation and the vulnerability to adaptive attacks.

## Removed Points

- **Point about small sample size being a "structural issue" that "undermines reported quantitative claims":** Downplayed from Major to Minor. While the absence of confidence intervals is a real methodological gap, the AUROC values are so high (99%+) that even pessimistic confidence intervals (e.g., ±3%) would still place the method well above the baselines. The critique overstates the impact on the paper's core claims.
- **Criticism that "the paper should not be accepted" and "major revision" is needed:** The paper has real contributions (broad evaluation, novel combination of characteristics for E2E systems, adaptive attack analysis) that are not invalidated by the identified weaknesses. The severity of the recommendation does not match the actual damage to claims.
- **Generic strength from Strength Finder that "the idea is sensible" and "scope of evaluation is commendable":** These are superficial and lack specific citation. Moved here.
- **Strength about "robust secondary defense against adaptive attacks" showing a "practical fallback":** The 0.57% average gain with no confidence intervals is too weak to be a meaningful strength. The filtering defense is a separate method not evaluated as part of the proposed system.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a direct baseline adapting Däubener et al. (2020) to E2E systems using only mean entropy and mean KL divergence. This is the single most important experiment to substantiate the novelty.
2. Report bootstrapped 95% confidence intervals for all AUROC and accuracy values. With 100 samples, this is essential and trivial to compute.
3. For the NN classifier, either increase the training set size (e.g., use a larger held-out portion of the ASR test set) or report cross-validation performance with training curves showing no overfitting.
4. Restructure the adaptive attack section to clearly separate the failure of the proposed detection method from the independent filtering analysis. The filtering should be presented as a separate observation, not as evidence that the proposed method is robust.
5. Remove or substantiate the claim that genetic attacks are "characterized by noise" with perceptual evidence, or simply acknowledge that the method does not detect genetic attacks well.

## Score and Decision

The paper proposes a straightforward but well-motivated detection method, evaluated with impressive breadth across architectures, languages, and attack types. The high AUROC values on targeted attacks are genuinely promising. However, the evaluation has several gaps: the most directly related prior work is not compared experimentally, the NN results are potentially overfit, and quantitative claims lack statistical grounding. These are addressable in revision but limit the paper's current strength. The contribution is solid but not exceptional—the method is a sensible combination of known ideas (output distribution statistics for detection) with a broader E2E evaluation than prior work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>