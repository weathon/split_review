I have now carefully read the paper and all reviewer inputs. Let me now produce the consolidated review.

---

## Summary

This paper proposes DRMGuard, the first defense framework specifically designed for detecting and mitigating backdoor attacks in deep regression models (DRMs) in the image domain. The core contribution is identifying that backdoored DRMs exhibit a distinctive feature-space property — the Ratio of Angle Variance (RAV) is consistently ≪ 1 for poisoned inputs, meaning the angles between feature vectors and the linear layer's weight vectors are highly concentrated. This observation is used to formulate a reverse-engineering optimization problem with a feature-space regularization term, enabling backdoor detection without enumerating continuous target vectors. Experiments on two regression tasks (gaze estimation, head pose estimation), four datasets, and four backdoor attacks show that DRMGuard achieves 95% identification accuracy and perfect 1.000 ROC-AUC, substantially outperforming adapted classification defenses.

## Strengths

- **Novel problem and key theoretical insight**: The paper correctly identifies that existing backdoor defenses fail for DRMs because (1) the continuous output space makes target vector enumeration impossible, and (2) all neurons contribute to the output (no argmax), so sparse-neuron defenses are ineffective. The derivation of the RAV metric (Section 3.3, Eq. 4) and the empirical demonstration that RAV ≪ 1 across four attacks on two datasets (Table 1, Figure 2) constitute a genuine and well-supported contribution.

- **Principled optimization framework**: The reverse-engineering objective (Equation 8) is well-motivated by the RAV observation. The feature-space regularization term $r_f$ directly encodes the identified property, making the optimization tractable where classification-based methods fail. The ablation study (Table 5) confirms that removing the feature-space regularization term (FSRT) causes complete failure (50% accuracy — all models classified as backdoored).

- **Strong empirical results against adapted baselines**: DRMGuard achieves ROC-AUC scores of 1.000 across all four attacks on MPIIFaceGaze, while the best adapted defense (FeatureRE) reaches only 0.599 and Neural Cleanse 0.379 (Table 3). Identification accuracy is 95% on MPIIFaceGaze and 87.5% on average across four datasets (Table 1). The mitigation results also show DRMGuard outperforming ANP, Fine-pruning, and Fine-tuning (Table 6).

- **Adaptive attack analysis**: The paper explicitly constructs an adaptive attack that targets the RAV property (adding a loss term to force RAV ≈ 1). This attack still cannot reduce DRMGuard's identification accuracy (95%), and the attack itself degrades (AE rises from 1.51 to 5.71, Table 7), suggesting the RAV property is a fundamental characteristic of backdoor behavior in DRMs.

## Weaknesses

### Fatal
None.

### Major

- **Momentum Reverse Trigger (MTR) is critically underspecified**: The MTR is shown by ablation to be indispensable — without it, all benign models are flagged as backdoored (Table 5, Acc drops to 50%). Yet the paper describes it in a single sentence: "assign different weights to different regions to balance the attention of the DRM on the image" (Section 3.4). No algorithm, equation, or architectural detail is provided. A commented-out line in the source (line 189) hints at a gradient-based attention map, but this is absent from the submission. Since MTR is a key enabler of the method's success, **the paper is not reproducible without a proper specification of this component.**

- **Baseline adaptations are insufficiently described, weakening the comparative claims**: The paper adapts Neural Cleanse and FeatureRE to regression by "taking the potential target vector $y_t$ as the optimization variable" (Section 4.1), with no further detail. For Neural Cleanse — which relies on enumerating discrete classes and detecting outliers — it is unclear how candidate target vectors are sampled in the continuous space. For FeatureRE — whose sparsity assumption the paper itself argues does not hold for DRMs — a simple adaptation is unlikely to be faithful. The paper's claim of "significantly outperforming" these baselines must be interpreted in light of this gap. While showing that naive adaptations fail is still useful evidence, the evaluation would be strengthened by either (a) a more careful adaptation, (b) explicit discussion of why these are the best possible adaptations, or (c) additional baselines more naturally suited to the setting (e.g., autoencoder-based outlier detection in feature space).

- **Architecture of the generative model $G_\theta$ is not specified**: The paper uses a generative model $G_\theta$ to reverse-engineer triggers for both input-independent and input-aware attacks (Section 3.2), but never describes its architecture (Is it a U-Net? An autoencoder? What are its dimensions, optimizer, training iterations?). This is essential for reproducibility.

### Minor

- **Small evaluation set for identification**: The identification accuracy is computed on only 20 models (10 benign + 10 backdoored) per condition. A single false positive yields 95%, and the perfect 1.000 AUC is achieved with just 20 data points — the confidence interval for this value is wide. Results are consistent across multiple attacks and datasets, which partially mitigates this concern, but bootstrapped confidence intervals or additional models (e.g., 30–50 per condition) would substantially strengthen the statistical reliability.

- **Detection threshold $\epsilon$ is set without justification or sensitivity analysis**: The identification metric $\mathcal{I}(f)$ uses $\epsilon = 0.03$ (Section 3.5). No ablation or analysis is performed on this value, even though $\lambda_1$, $\lambda_2$, and $p$ are ablated. Since $\epsilon$ directly governs the false-positive/false-negative trade-off, the paper should at minimum show that results are stable across a range of $\epsilon$ values (e.g., 0.01, 0.03, 0.05).

- **Limited architectural diversity**: All experiments use ResNet18 as the feature extractor $F$. The paper claims generalization "to different architectures" (Section 6) but provides no evidence. Testing at least one additional architecture (e.g., VGG, MobileNet) would support this claim.

- **Mitigation comparison lacks statistical testing**: The paper reports AE and DAE for DRMGuard (15.36, 3.29) vs. Fine-tuning (13.96, 4.32) as single values per method (Table 6), claiming "significantly larger" and "much smaller." Without variance estimates or statistical tests across multiple runs, the significance of these differences is not established.

### Trivial
None.

## Nice-to-Haves

- Report computational cost (GPU hours per model) for training $G_\theta$, as this affects practical deployability.
- Clarify whether Fine-pruning's pruning ratio and other baseline hyperparameters were tuned for the regression task or used with defaults.
- Discuss whether the RAV property could be circumvented by an adaptive attack that preserves low AE while achieving RAV ≈ 1 (the current adaptive attack trades off attack success for evasion).
- A more thorough discussion of limitations beyond the benign dataset requirement would strengthen the paper (e.g., reliance on the specific architectural decomposition $F + H$, applicability to other modalities).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism that the paper should test on 50 models per condition** — The defense paper norm is 10–20 models; 50 is an unusually high bar. However, the broader concern about statistical fragility (no CIs, no replication) is kept in Minor.
2. **Criticism that the RAV observation is "only verified on four attacks"** — The paper covers both input-independent and input-aware attacks, which is the standard taxonomy. This is adequate coverage.
3. **Criticism about missing related works** — Not verifiable; the paper adequately covers the relevant defense literature (NC, FeatureRE, ANP, Fine-pruning).
4. **Criticism about missing appendix or proofs** — These exist in the original submission; the parser strips appendix content.
5. **Strength Finder's claim about "DRMGateway"** — This appears to be a typo by the strength finder; the paper uses DRMGuard correctly.

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the RAV property is presented as a *defender's advantage* (backdoored models are more constrained in feature space), yet the adaptive attack analysis shows that an attacker who tries to break this property suffers reduced attack efficacy. This suggests there may be a fundamental trade-off between attack effectiveness and evasion of RAV-based detection — a claim the paper gestures at but does not formalize. If this trade-off is provable, it would be a stronger result than any individual defense. This observation goes beyond the paper's own framing and could motivate future theoretical work.

## Suggestions

1. **Fully specify the MTR**: Provide the exact equation, algorithm, or pseudo-code for how attention weights/region weights are computed and applied in the optimization. This is the single most important change for reproducibility.

2. **Specify the $G_\theta$ architecture**: Describe the generative model's architecture, optimizer, learning rate, training iterations, and any other relevant details.

3. **Justify or ablate $\epsilon$**: Add a sensitivity analysis over $\epsilon$ values (e.g., 0.01, 0.03, 0.05) to show the detection performance is stable, or explain the principled basis for choosing 0.03.

4. **Improve baseline adaptation description**: Either (a) describe the adaptation of NC and FeatureRE in more detail (how target vectors are sampled in continuous space, how statistical outlier detection is performed), (b) include additional baselines more suited to the regression setting, or (c) temper comparative claims to acknowledge the limitations of the adaptations.

5. **Increase evaluation set or add confidence intervals**: Either train more models per condition (e.g., 30) or provide bootstrapped confidence intervals for the identification accuracy and AUC scores.

6. **Test at least one additional architecture** (e.g., VGG, MobileNet) to support the generality claim beyond ResNet18.

## Score and Decision

The paper tackles an important and underexplored problem — backdoor defense for deep regression models — with a novel and well-motivated approach. The core insight (RAV-based feature space constraint) is sound and supported by theoretical derivation and empirical evidence across multiple attacks, tasks, and datasets. The method demonstrably outperforms adapted classification defenses.

However, the paper has significant reproducibility gaps: the MTR component (essential for correct operation) and the generative model $G_\theta$ are not described in sufficient detail. Additionally, the baseline adaptations are poorly documented, making the comparative claims harder to evaluate. These are fixable in a revision and do not invalidate the core contribution.

**Overall assessment**: The contribution is real and the evidence for the main claims is credible, but the paper requires major revisions to meet reproducibility standards and to substantiate the comparative evaluation. I recommend acceptance pending these revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>