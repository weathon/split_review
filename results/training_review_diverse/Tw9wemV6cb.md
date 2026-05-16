Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes BTI-DBF, a backdoor trigger inversion method that reverses the usual paradigm: instead of attempting to extract backdoor features directly (which requires scanning all classes and guessing the trigger form), it decouples *benign features* using only local benign samples. A feature mask is learned such that benign features suffice for correct classification, then a generator produces poisoned samples that match benign samples on benign features but diverge on the complementary (backdoor) features. Two downstream defenses (fine-tuning-based removal and input pre-processing) are built on this BTI module. Experiments on CIFAR-10, GTSRB, and ImageNet against six attacks show strong defense results and dramatic efficiency gains.

## Strengths

- **Novel and principled paradigm shift.** Rather than trying to approximate unknown backdoor features—a fundamentally hard problem—the paper inverts the logic by decoupling benign features, for which defenders have direct local samples. This is conceptually clean and well-motivated (Section 3.2.1), and the ablation study (Table 4) confirms that the feature decoupling component is responsible for the gains.

- **State-of-the-art defense effectiveness.** Tables 2 and 3 show that both BTI-DBF (U) (backdoor removal) and BTI-DBF (P) (pre-processing) achieve ASR < 10% with BA drop < 5% across all six attacks on three datasets. All baseline defenses fail (ASR > 10% or excessive BA drop) in at least one setting, directly supporting the claim that the defenses reach state-of-the-art performance.

- **Dramatic efficiency gain.** Figure 4 reports BTI-DBF completes trigger inversion in 60 seconds on CIFAR-10—more than 20× faster than Unicorn and more than 3× faster than the most efficient baseline (Pixel). This efficiency follows directly from the design: because the method does not scan all potential target classes, the cost is independent of the number of classes.

- **Quantitative reliability improvement.** Table 1 shows BTI-DBF achieves nearly 10× smaller feature distance (FD) under BadNets compared to Pixel, and 100% detection success rate (DSR) in almost all cases, whereas all baselines drop below 50% DSR on some attacks.

- **Robustness to adaptive attacks.** Table 6 shows that defenses maintain high BA (>91%) and low ASR (<6%) under Adap-Blended (which reduces latent separation) and a custom Adaptive BadNets (which makes backdoor features also useful for benign classification).

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by evidence; the weaknesses below are addressable gaps in presentation and evaluation breadth, not structural flaws.

### Minor

- **FD metric lacks transparency for baseline comparison.** The paper measures feature distance (FD) between recovered and ground-truth poisoned samples in the feature space of the backdoored model's convolutional layers (S_a). However, it does not specify *how* baseline methods' outputs (e.g., masks + trigger patterns from NC, THTP, Pixel) are converted into poisoned samples for this comparison—e.g., whether a standard mask+trigger formulation is applied uniformly across methods. Without this detail, readers cannot assess whether the large FD gap reflects genuine superiority or an uneven comparison protocol. This is a necessary experimental clarification.

- **DSR metric is non-standard and needs justification.** Detection Success Rate (DSR)—whether feeding generated poisoned samples to the model consistently yields the target-class label—is used as a primary reliability metric. This is not the standard way BTI methods like NC are evaluated; they are typically assessed by whether the recovered trigger *causes* a class flip to the target, not by majority-vote prediction on generated samples. The finding that "there are methods with small distances ... but they cannot find the target label correctly" suggests the metric conflates two capabilities. Reporting complementary standard metrics (e.g., trigger pattern similarity, attack success rate of recovered triggers) alongside DSR would strengthen the evaluation.

- **No standard deviations for defense results.** Tables 2, 3, and 6 report ASR and BA as point estimates without standard deviations or confidence intervals. Given the small local dataset size (5% of training data), variance across runs could be nontrivial. This is important for assessing the reliability of the claimed superiority over baselines.

- **Feature separation assumption not deeply validated.** The method assumes that benign features suffice for correct prediction and that the remaining (backdoor) features lead to wrong predictions. While the ablation (Table 4) and adaptive attacks (Adap-Blended, which reduces latent separation) provide partial validation, an explicit diagnostic—e.g., measuring model accuracy when only the complement (1−m) features are used—would more directly confirm the assumption holds for the diverse attacks tested.

- **Efficiency claim for larger datasets not shown.** The paper states "This efficiency advantage is even more pronounced in datasets with more classes (e.g., GTSRB and ImageNet)" (Section 4.2), but Figure 4 reports efficiency only on CIFAR-10. The efficiency advantage on CIFAR-10 is already clear, but the stronger claim about larger datasets is unsupported.

### Trivial

- Some implementation details are deferred: how the mask *m* in Eq. (1) is optimized (gradient-based optimization with clamping to [0,1] is implied but not stated); how the hyperparameter *τ* in Eq. (2) is set and whether it is sensitive; and the specific schedule for the iteration-based enhancement (alternating updates of generator and defense target). These are standard details that would improve reproducibility but do not affect the paper's validity.

## Nice-to-Haves

- A more systematic adaptive evaluation: the two adaptive attacks tested (Adap-Blended and Adaptive BadNets) are relevant, but additional adaptive strategies—e.g., an attack that directly fools the mask optimization in Eq. (1) by making backdoor features also contribute to correct classification on local benign samples containing the true backdoor pattern—would further strengthen the robustness claims.

- Visualizing the learned mask *m* overlaid on feature maps to show it focuses on class-discriminative regions would deepen understanding of what benign features the method captures.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- The criticism that FD is "biased" because it uses the same feature extractor (S_a) that BTI-DBF optimizes against is overstated. Feature-space methods (FeatureRE, Unicorn) also optimize in this space; for input-space methods (NC, THTP, Pixel), the feature space is a legitimate evaluation space for measuring similarity of recovered triggers to ground truth. The paper does not unfairly handicap baselines—rather, the missing detail about *how* baselines are applied for FD calculation is the real issue (already captured above).

- The criticism that DSR is "unusual" and effectively invalid is too strong. While DSR is non-standard, it measures a practically relevant property (can the BTI identify which class is targeted?). The issue is that it should be supplemented with standard metrics, not that it is wrong.

- The call for hyperparameter analysis of *τ* and mask optimization details as a "significant gap" is downgraded: these are standard experimental details whose omission is common in conference papers and addressable in supplementary material.

## Novel Insights

The most interesting observation from the reviews is the tension between the BTI evaluation metrics (FD and DSR) and the downstream defense results. The reviewer correctly notes that FD and DSR have fairness/justification concerns, yet the downstream defense results (Tables 2, 3) independently validate that BTI-DBF's inverted triggers are practically useful—they enable both fine-tuning and pre-processing defenses to succeed where baselines fail. This creates an elegant "proof by utility" that partially insulates the paper from the metric concerns: even if the FD/DSR comparison were imperfect, the downstream results confirm the triggers are high-quality. The paper could lean into this more explicitly.

## Suggestions

1. **Clarify the FD evaluation protocol:** Specify exactly how each baseline method's outputs are converted to poisoned samples for feature distance calculation. Use a uniform procedure (e.g., the standard mask+trigger formulation from each method's original paper) and state this explicitly.

2. **Add standard BTI metrics:** Report trigger pattern similarity (e.g., pixel-space correlation or SSIM) and attack success rate of recovered triggers (i.e., does the recovered trigger cause misclassification to the target class?) alongside FD and DSR.

3. **Report variance:** Add standard deviations for Tables 2, 3, and 6 (or confidence intervals) to account for variability due to the small local dataset.

4. **Validate the feature separation assumption directly:** Measure the model's accuracy when using only the complement features (1−m) on benign samples. If accuracy is near zero, the assumption holds strongly.

5. **Show efficiency on GTSRB or ImageNet** to support the claim that the advantage scales with class count.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>