Now I have sufficient anchors to finalize. Let me compile the final review.

## Summary

KOALA proposes an adversarial example detector based on disagreement between two complementary similarity metrics — KL divergence and a thresholded L0-based distance — in a nearest-prototype classifier. When the two metrics predict different classes, the input is flagged as adversarial. The paper provides a formal proof (Theorem 1) that under norm-bounded perturbations and sufficient inter-class prototype separation, no perturbation can simultaneously fool both metrics, guaranteeing detection. The method requires only clean-image fine-tuning of a pretrained encoder. Experiments are conducted on ResNet-18/CIFAR-10 and CLIP ViT-B/32 on Tiny-ImageNet.

## Strengths

- **Formal theoretical framework distinguishing the method from prior empirical detectors**: Theorem 1 and its decomposition into Propositions 2-4 provide an explicit incompatibility proof between the conditions for fooling KL-based and L0-based classifiers. The core idea — mutual exclusivity of the two prediction-stability bands under a shared perturbation budget — is conceptually elegant and novel for adversarial detection. Most prior detectors (LID, MagNet, feature squeezing) lack such formal guarantees.

- **Empirical validation of the theorem on compliant samples**: Table 1 shows that on the theorem-compliant subset, KOALA achieves perfect recall (1.0) across both datasets and both perturbation budgets, while non-compliant samples show substantially lower F1 (e.g., 0.53 vs. 1.0 for ResNet/CIFAR-10 at ε=2/255). This cleanly separates compliant from non-compliant performance and provides evidence that the theory's conditions are predictive.

- **Clean-image-only fine-tuning preserves standard accuracy**: Table 3 shows KL+L0 fine-tuned ResNet-18 achieves 94.78% clean accuracy vs. 95.16% for the baseline — a negligible 0.38pp drop — while improving adversarial accuracy (57.32% vs. 45.5% under PGD ε=2/255). The method requires no adversarial examples during training, making it lightweight compared to adversarial training approaches.

- **Cross-architecture evaluation reveals architecture-dependent behavior**: Testing on both ResNet-18/CIFAR-10 and CLIP ViT-B/32/Tiny-ImageNet reveals that the optimal metric configuration is architecture-dependent (KL+L0 is best for ResNet; L0-only is best for CLIP), attributed plausibly to CLIP's cosine-contrastive pretraining. This provides practical guidance beyond a single setup.

## Weaknesses

### Fatal

None.

### Major

- **Non-standard detection evaluation conflates detection with classification accuracy**: The confusion matrix definition in Section 4.2 (lines 187-191) counts an attacked input as a True Positive even when the detector fails to flag it (â=0), as long as the classifier happens to be correct (ŷ=y*). An undetected attack only counts as a False Negative when it is also misclassified. This systematically inflates recall because every attack the model withstands — whether KOALA detected it or not — boosts the numerator without affecting the denominator. The headline precision of 0.94 and recall of 0.81 (abstract, line 9) are therefore uninterpretable as standard detection metrics. This affects every detection result in Tables 1 and 2, making it impossible for a reader to assess actual detection performance.

- **No comparison to any existing adversarial detector**: The related work (Section 2) extensively catalogs detection methods — LID, MagNet, feature squeezing, NIC, Mahalanobis detector — yet the experiments only compare KOALA against alternative metric combinations within its own framework (Tables 2-4). There is no head-to-head comparison against any prior detector. Without this, the claim of "strong detection performance" (line 34) has no external reference point.

### Minor

- **Theorem-compliance partitioning uses post-hoc information**: Determining whether a sample is "theorem-compliant" requires knowing which adversarial class the attack targets (the condition checks |c_i* - ĉ_i| > threshold). This information is unavailable at test time. While the experiment validly tests the theory under its own conditions, practical significance is limited — only ~10% of CLIP/Tiny-ImageNet samples are compliant, and they cannot be identified at inference.

- **Gap between existence proof and fixed-τ implementation**: The proof sketch (Prop. 4) argues that "we can always find a threshold τ" that forces incompatibility, but the detector uses a single fixed τ=0.75 for all samples. The relationship between the existence argument and the fixed implementation is not addressed.

- **No evaluation against adaptive attacks**: An attacker aware of KOALA's detection mechanism could explicitly optimize perturbations to minimize disagreement between KL and L0 predictions. This is the most important stress test for a detection method and is absent.

- **No sensitivity analysis for key hyperparameters**: The parameters τ=0.75 and φ=0.5 are stated without ablation, despite τ being central to the theoretical argument.

- **Limited attack budget**: Only ℓ∞ perturbations with ε ∈ {2/255, 4/255} are tested. Testing at standard larger bounds (e.g., 8/255 for CIFAR-10) would more seriously stress the method.

### Trivial

- **Table 4 caption error**: The caption (line 272) states "The KL+L0 objective demonstrates superior adversarial accuracy," which appears to be a copy-paste from Table 3. Table 4 actually shows KL+L0 at 26.50% while L0-only achieves 53.31% and KL-only achieves 60.02% under PGD ε=2/255. The body text (lines 274-277) correctly discusses this.

## Nice-to-Haves

- Report standard detection metrics (TPR at fixed FPR, AUROC) separately from the joint detection+classification metric, so readers can assess actual detection performance.
- Analyze what fraction of clean samples satisfy the theorem's structural condition for all possible adversarial target classes, to characterize the practical scope of the guarantee.
- Report computational cost of computing KL and L0 distances to all m class prototypes relative to standard inference.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The L0 metric is not standard L0"**: The paper explicitly defines the L0-based metric in Eq. (2) as a thresholded count of outlier coordinates relative to the mean absolute deviation. The definition is clear and the design choice is reasonable. Not a valid weakness.
- **"Prior work lacking proof of correctness is overstated"**: This is a framing/rhetorical choice in the introduction. It does not affect the paper's technical contribution and is not a substantive weakness.
- **"KL+L0 underperforms on CLIP, contradicting the core contribution"**: The paper already acknowledges and discusses this in the body text (lines 274-277), attributing it to CLIP's pretraining geometry. The caption error (covered above) is the real issue.
- **"Assumption A3 is not mild"**: This is a judgment about assumption strength that goes beyond what can be verified from the paper alone. The assumption is stated and its implications can be discussed, but labeling it as not mild without proof is speculative.

## Novel Insights

The core theoretical insight — that KL divergence and L0-based distance induce mutually exclusive prediction-stability bands under a shared perturbation budget — is genuinely novel for adversarial detection. The proof strategy of showing that the energy required to flip the L0 prediction leaves insufficient residual energy to satisfy the KL-flip alignment condition provides a principled framework for designing disagreement-based detectors beyond the specific metrics used here. This is the paper's most valuable contribution.

## Suggestions

- Redefine the evaluation to report standard detection metrics (TPR/FPR, AUROC) that measure whether attacks are flagged independent of classification correctness. The current joint metric can be retained as a secondary measure.
- Add comparisons to at least 2-3 established detectors (e.g., LID, Mahalanobis, feature squeezing) on the same models and attacks, so readers can assess whether KOALA's detection performance is competitive.
- Report what the detection rate would be under the standard confusion matrix definition (TP = attacked AND detected) to give readers a clear picture of actual detection performance.
- Test against an adaptive attack that explicitly minimizes KL-L0 prediction disagreement.

## Calibration

**Round 1 bracket**: 4.0–6.0. KOALA sits clearly above the weak band (2.0–3.0 papers lack formal theory or have weak empirical validation) and below the strong band (7.5+ papers like GNNCert at 8.0 have mature, well-validated contributions with strong empirical results).

**Round 2 narrowing**: Compared KOALA against anchors in the 4.0–6.5 range:
- **POT** (4.60): Prototype-based OOD detection. Has comparisons to baselines but uses test-set information in its method. KOALA has stronger theory but weaker empirical validation. KOALA is comparable — slightly better on theory, slightly worse on empirical.
- **SPADE** (5.50): Formal guarantees for OOD/adversarial detection using extreme value theory. Has baseline comparisons across multiple architectures. KOALA has a more interesting theoretical angle (mutual exclusivity of stability bands) but substantially weaker empirical validation (flawed metrics, no baselines). KOALA is below SPADE.
- **MirrorCheck** (5.50): Adversarial detection for VLMs. Compares to baselines, includes adaptive attack analysis, solid empirical validation. KOALA has stronger theory but significantly weaker empirical validation. KOALA is below MirrorCheck.
- **DDAD** (6.20): Strong theory + strong empirical validation with SOTA comparisons. KOALA is clearly below DDAD.
- **Eigenvalue framework papers** (5.33, 5.50): Purely theoretical frameworks for understanding adversarial examples. KOALA has both theory and empirical validation, but the empirical part has structural issues. Roughly comparable.

**Final score**: 4.5. The theoretical contribution (mutual exclusivity of KL and L0 stability bands) is genuinely interesting and novel. However, the empirical validation has structural issues — the evaluation metrics conflate detection with classification accuracy, and there are no comparisons to existing detectors — that prevent the empirical claims from being assessed as stated. The paper would benefit substantially from fixing the evaluation framework and adding baseline comparisons.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>