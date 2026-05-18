Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper investigates the mechanism behind adversarial transferability, proposing that trained models behave as ensembles of submodels capturing different features. It introduces Neuronal Activation Orthogonality (NAO) and Averaged NAO (ANAO) as metrics to quantify how much different inputs activate overlapping vs. distinct neurons (operationalized via weight gradient magnitudes). The paper shows that adversarial examples activating more diverse (orthogonal) submodels transfer better, and that data transformations help avoid inefficient perturbations. Based on these insights, the authors propose AdaAES, which combines random transformations (rotation, resized padding, block shuffle) with momentum and ANAO-based candidate selection. Experiments across five surrogate and twelve target models show competitive attack success rates.

## Strengths

- **Novel mechanistic perspective on transferability**: The paper moves beyond experience-based heuristics to propose that models function as ensembles of submodels capturing different features, and that activating more of these submodels improves transferability. This reframing is grounded in the empirical observation (Figure 1a) that different benign inputs activate largely orthogonal sets of neurons in CNNs.

- **Introduction of principled metrics (NAO/ANAO)**: The paper formalizes a way to quantify neuron activation overlap via normalized gradient orthogonality (Eqs. 4, 5). While the choice of gradient magnitude as a proxy for "activation" is debatable (see Weaknesses), the metrics themselves are well-defined and enable quantitative analysis that was previously lacking.

- **Strong empirical validation connecting mechanism to practice**: The controlled noise experiment (Table 1) shows that, within a given noise type, lower mANAO (more diverse neuron activation) correlates with higher attack success rates. Figure 5 further shows a monotonic relationship between transformation count, decreasing mANAO, and increasing ASR. This directly links the proposed mechanism to practical attack design.

- **Competitive empirical results across diverse architectures**: AdaAES achieves the highest or near-highest attack success rates across twelve target models spanning CNNs (ResNet, DenseNet, Inception, VGG) and vision transformers (ViT, PiT, Visformer, Swin), using five different surrogate models (Tables 5–9). The experiments cover a more diverse set of target architectures than many prior works.

- **Clean ablation study isolating component contributions**: Table 4 cleanly separates the contributions of noise augmentation, transformation-based gradient averaging, and ANAO-based candidate selection, showing that all three components contribute to the final result.

## Weaknesses

### Fatal
None.

### Major
1. **Unvalidated mapping from gradient magnitude to feature-level neuron activation.** The paper uses the magnitude |∇θ| of the gradient of a weight w.r.t. the objective as a measure of "neuron activation" (line 60). This quantity captures first-order sensitivity of the loss to that weight — not the neuron's output activation, firing pattern, or feature selectivity. While gradient-based importance measures have precedent in the literature (Bi et al., 2024), the paper does *not* validate that lower ANAO (gradient orthogonality) actually corresponds to more orthogonal *feature representations* in the internal activations of the model. The paper's mechanistic story depends on this mapping, but experiments probing intermediate representations (e.g., CKA, probing classifiers, or activation similarity on layer outputs) are absent. Without such validation, the claimed mechanism (activating more submodels → better transferability) remains a plausible but unsubstantiated interpretation of a correlational observation about gradients. The empirical performance of AdaAES is not invalidated by this concern, but the paper's central explanatory claim is weaker than stated.

### Minor
2. **Non-monotonic relationship between ANAO and transferability is under-explained.** The core narrative is that lower ANAO (more orthogonal neuron activation) is better. However, Table 2 shows a non-monotonic pattern: at 1 iteration, using 1 rotation *increases* mANAO relative to no transformation (according to the paper's description on lines 130–131), while ASR also increases. This means there are regimes where higher ANAO coincides with better results. The paper provides a reasonable dual-mechanism explanation (avoiding inefficient perturbations via transformation averaging + activating more submodels), but the two mechanisms are not disentangled experimentally, and the reader is left unclear about what direction of ANAO change is beneficial under what conditions. The paper would benefit from an experiment that isolates these two effects.

3. **Comparative methods are not clearly identified in the text.** The paper states it compares against "7 adversarial attacks" (line 208) but only names MI-FGSM and DEM explicitly, referring to the rest as "other advanced methods proposed recently." The reader should not need to decode table images to know which methods are being compared. If the comparison includes BSR, DeCowA, L2T, or ADNA (cited as related work), this should be stated explicitly. If it does not include them, the paper should explain why.

4. **No variance or confidence intervals for the main results.** The experiments use a 1000-image subset of ImageNet, which is standard in this area, but all results are reported as point estimates without error bars. Given the relatively small sample size, reporting variance across multiple random subsets or multiple runs would help assess the reliability of the reported improvements.

### Trivial
5. DEM is referenced in the experiments (line 208) without being defined or expanded. Readers unfamiliar with this attack must infer it from context.
6. The hyperparameter selection for transformations relies on comparing mANAO values, which risks circularity when the same metric is used both to justify the method and to set its parameters.

## Nice-to-Haves
- A validation experiment (e.g., CKA on internal layer activations, or a probing classifier) showing that gradient orthogonality (low ANAO) actually corresponds to orthogonal feature representations in the model's hidden states.
- An experiment explicitly decoupling the "avoiding inefficient perturbations" effect from the "activating more submodels" effect, e.g., by comparing candidate selection via ANAO vs. via a non-ANAO criterion (e.g., random selection, largest loss).
- Naming all seven comparative methods explicitly in the text (Section 4.3) rather than leaving five of them to be inferred from table images.
- Reporting confidence intervals or standard deviations for the main attack success rates.

## Removed Points
These points were evaluated against the paper and found to be inaccurate, misinformed, or reflecting parser artifacts rather than actual issues:
- *"The term 'activating more neurons' is used interchangeably to mean both 'activating a larger number of distinct neurons' and 'activating neurons that are more similar'."* — The paper consistently uses lower ANAO to mean more orthogonal (different) neurons. There is no confusion in usage; the paper settles on the diversity interpretation throughout.
- *"The ensemble interpretation is stated as a finding but is actually a speculation."* — The paper hedges appropriately ("may be viewed as," line 29) and provides empirical evidence (ANAO distributions, Figure 1a) consistent with this interpretation. It is presented as a plausible mechanistic hypothesis grounded in observations, not as an established fact.
- *"Several figures are low-resolution" and "mathematical notation has formatting issues."* — These are parser artifacts from PDF extraction, not author errors.
- *"The paper argues that activating more neurons improves transferability, but... the claimed mechanism cannot be read off from these numbers."* — The paper provides a coherent dual-mechanism explanation in Section 3.3 (avoiding inefficient perturbations + activating more submodels). The reviewer's cross-noise-type comparison in Table 1 ignores the paper's explicit caveat "given a specific noise type."

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a validation experiment (CKA or probing) comparing gradient-based ANAO against activation-based similarity measures to ground the mechanistic claim.
2. Clearly name all comparative methods in the experiment section (Section 4.3) rather than leaving them implicit in table images.
3. Disentangle the "avoid inefficient perturbations" and "activate more submodels" mechanisms with a controlled experiment that varies the selection criterion independently.
4. Add error bars (e.g., bootstrap confidence intervals) for the main attack success rate results.

## Score and Decision
The paper makes a genuine contribution by proposing a mechanistic framework for understanding adversarial transferability, introducing novel metrics (NAO/ANAO), and demonstrating a practical attack that performs competitively across diverse architectures. The weaknesses — most notably the unvalidated mapping from gradient magnitude to feature-level activation — are real but not fatal: the empirical results stand on their own, and the mechanistic interpretation remains a plausible hypothesis that can be tested in future work. The paper is above the acceptance threshold but would benefit from the suggested revisions to strengthen its central claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>