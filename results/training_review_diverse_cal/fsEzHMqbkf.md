Now I have thoroughly verified the paper content. Let me produce the final consolidated review.

## Summary

The paper introduces the Conditional Density Ratio (CDR) score for post-hoc out-of-distribution detection. Instead of marginalizing conditional distributions over classes (as done by energy score and GEM), CDR leverages the ratio of a class-conditional generative model p(z|y) and a discriminative classifier p(y|z) to estimate marginal densities without marginalization. A key component is an automatic temperature-tuning procedure that requires no OOD samples. Two instantiations are explored: CDR_Maha (using Mahalanobis-based Gaussian estimates) and CDR_KDE (using kernel density estimation). Experiments on CIFAR and ImageNet benchmarks show competitive performance.

## Strengths

1. **Principled theoretical framing that avoids the constant-partition-function assumption.** The paper explicitly identifies that the energy score is only a valid density estimator when the partition function remains constant (Section 3.2, lines 99–100), and shows that CDR avoids this issue by not marginalizing. This is a genuine theoretical advance over prior post-hoc methods like the energy score and GEM.

2. **Robustness to classifier quality, supported by quantitative evidence.** When the ID dataset shifts from CIFAR-10 (high classifier accuracy) to CIFAR-100 (lower accuracy), the average AUROC of the Energy score drops from 91.99% to 77.20%, while CDR_Maha only decreases from 97.41% to 95.66% (Section 4.1, lines 169–170). This demonstrates that CDR's dual use of generative and discriminative information confers meaningful robustness.

3. **Hyperparameter-free automatic temperature scaling without OOD data.** Algorithm 1 and the surrounding discussion (lines 109–123) describe a principled two-step temperature selection procedure using only in-distribution validation data. Figure 4 validates that the automatically selected temperatures are near-optimal in terms of AUROC. This is practically valuable for the realistic setup where OOD samples are unavailable.

4. **Generality across density estimators and learning paradigms.** The CDR framework is instantiated with both a parametric Mahalanobis estimator and a non-parametric KDE estimator, and is extended to self-supervised learning (Table 4). Both variants perform competitively across a wide range of benchmarks.

5. **Addresses an under-explored but realistic post-hoc setup.** The paper explicitly targets the scenario where only pretrained model weights and a small number of ID validation samples are available—no training data, no OOD samples (Section 1, Problem Setup, line 17). This fills a practical gap that prior work often overlooks.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric baseline comparison clouds attribution of gains.** The paper sets temperatures to 1 for all baseline methods (MSP, Energy, Mahalanobis distance, GEM) while applying tuned temperatures \(T_\phi, T_\psi\) to CDR (lines 142, 155). The paper itself calls temperature scaling "a crucial component" (abstract, line 79) and shows that CDR without it performs substantially worse (Figure 3). Since temperature scaling is known to benefit these baselines as well (Liang et al., 2017 for MSP; temperature is structurally part of the Energy score), the reported gains cannot be cleanly attributed to the CDR formulation versus simply having a tuned temperature. **This is the most significant weakness.** The paper's central empirical claim—that CDR "achieves competitive performance"—would be considerably strengthened by comparing against baselines that are also temperature-tuned on the same validation data using a similar search procedure. Without this, the magnitude of CDR's advantage over the next-best method is uncertain.

### Minor

2. **Missing ablation of the temperature tuning loss design.** The loss for \(T_\phi\) (lines 120–123) combines a separation term and a regularization term \(\mathcal{R}\) that penalizes scale differences between the two log-densities. While the motivation for \(\mathcal{R}\) is explained (line 117), the paper provides no ablation showing whether both terms are necessary or how performance changes without \(\mathcal{R}\). This makes it unclear whether the full complexity of the loss is warranted.

3. **Unverified theoretical claim about the partition-function assumption.** The paper argues that CDR avoids the constant-partition-function assumption that limits the energy score (Section 3.2, lines 99–100). This is a theoretically sound observation, but no experiment demonstrates a case where this assumption actually harms the energy score in practice and CDR succeeds because of avoiding it. The claim remains motivational but untested.

4. **Small validation sample size for ImageNet.** The paper uses only 25 samples per class (25,000 total for 1000 classes) on ImageNet to estimate the full covariance matrix and tune temperatures (line 146). This raises reliability concerns, particularly for the KDE variant and the covariance estimate. A sensitivity analysis varying the number of validation samples would strengthen confidence in the results.

5. **No comparison of CDR_KDE vs. CDR_Maha trade-offs.** The paper notes that CDR_KDE is "more robust" but "comes at the cost of increased computational requirements" (lines 169–173). However, no quantitative analysis of the computational cost vs. performance trade-off is provided to help practitioners choose between the two variants.

### Trivial

None.

## Nice-to-Haves

- A controlled toy experiment where the densities are known exactly, comparing CDR against marginalization-based methods under misspecification, would ground the empirical success and make the theoretical claims more compelling.
- The paper acknowledges the assumption that \(p(z)\) adequately represents \(p(x)\) (line 200–201) as a limitation. A brief experiment varying feature extractor quality to illustrate when this assumption breaks would further strengthen the discussion.

## Removed Points

- **"Additional Ablations not reported":** The paper mentions "Additional Ablations" (line 191). The parser strips appendix content from all papers; these ablations exist in the original submission. Removed per hard rule about missing appendix content.
- **"Temperature tuning method risks being overfitted to specific experiments":** This is speculative and unsupported by evidence. The paper already shows results across multiple datasets and models. Removed as an unsubstantiated claim.

## Novel Insights

The most interesting finding to emerge from the reviews—not fully foregrounded in the paper itself—is the structural insight that CDR can be decomposed into an average generative conditional ratio (GCR) plus the energy score (Equation 2), and that the GCR acts as a "corrective" term that is near-zero for inlier samples. This decomposition provides an intuitive explanation for why CDR works: it corrects the energy score with a term that is small when the two conditional models agree (as they should for in-distribution data) and diverges when they disagree (as they might for OOD samples). This perspective suggests CDR could be viewed less as a new density estimator and more as a principled ensembling of two existing detection signals.

## Suggestions

1. **Augment Tables 1–3 with temperature-tuned baselines.** This is the single highest-impact change. If the baselines also benefit from temperature tuning (even using the same validation set and a grid search), the comparison becomes fairer and the contribution of CDR's formulation—separate from temperature tuning—can be properly assessed. If the gap persists, the paper's claims become much stronger.

2. **Ablate the regularization term \(\mathcal{R}\)** from the \(T_\phi\) optimization loss to demonstrate its necessity and isolate which component of the tuning loss drives performance.

3. **Add a sensitivity analysis** varying the number of validation samples per class for ImageNet to establish how robust CDR is to limited data.

## Score and Decision

Overall assessment: The paper presents a conceptually appealing framework with a solid theoretical motivation and a practically useful automatic temperature-tuning method. The empirical results are impressive, but the core weakness—the asymmetric baseline comparison where CDR benefits from tuned temperatures while baselines do not—prevents clean attribution of the reported gains and limits the strength of the central claim. The contribution is real and the paper is well-executed otherwise, but this issue must be addressed before the empirical conclusions can be fully trusted.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>