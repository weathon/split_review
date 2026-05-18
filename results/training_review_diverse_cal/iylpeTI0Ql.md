Now I have all the evidence needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces Zero-Shot Noisy Test-Time Adaptation (ZS-NTTA), a practical setting where a vision-language model must adapt to a target stream containing out-of-distribution (noisy) samples at test time. It presents a rigorous analysis showing that noisy samples dominate adaptation gradients (by ~10×), explaining why existing TTA methods underperform a frozen baseline. The paper then proposes AdaND, which decouples detection from classification: the classifier (CLIP) is kept frozen, and a lightweight linear-layer noise detector is trained online using ZS-CLIP's pseudo-labels, with Gaussian noise injection to handle clean streams. AdaND achieves strong empirical results (e.g., 8.32% Acc_H improvement over TTA methods on ImageNet) with efficiency nearly identical to frozen CLIP.

## Strengths

1. **Rigorous analysis of why TTA methods fail under noisy samples.** The paper designs three adaptation pipelines (GT, Normal, All-update) and provides gradient analysis (Figure 4) showing that noisy samples produce gradients ~10× larger than clean samples, causing overfitting. Score distribution visualizations (Figure 3) further demonstrate that Tent's adaptation raises noisy-sample scores, eroding distinguishability. This evidence chain directly supports the paper's central diagnosis. This is the paper's strongest contribution.

2. **AdaND achieves strong ZS-NTTA performance with near-zero overhead.** On ImageNet, AdaND improves Acc_H by 8.32% over the best TTA method (Tables 2, 3) while maintaining runtime and GPU memory nearly identical to frozen ZS-CLIP and substantially below Tent, SoTTA, and TPT (Table 4). The combination of meaningful gains and negligible compute cost directly supports the method's practical value.

3. **Effective handling of both noisy and clean data streams via Gaussian noise injection.** Ablations (Table 6) show that without Gaussian injection, the detector collapses on clean streams (Acc_H drops from 91.76 to 35.52); with injection, it performs well on both. Robustness holds across noise types and injection frequencies (Tables 15, 16), validating the design choice.

4. **Introduction of a standardized ZS-NTTA benchmark.** The paper constructs 44 ID-OOD dataset pairs from established OOD detection benchmarks (Sec. 3.1) and defines clear metrics (Acc_S, Acc_N, Acc_H). This provides a reproducible evaluation protocol that addresses a gap in prior noisy-TTA work.

5. **Comprehensive ablation and robustness experiments.** The paper demonstrates insensitivity to hyperparameters (queue size, threshold length, warm-up steps) across datasets (Tables 20–22) and consistent performance under varying noise ratios (0%–75%) and random sample orders (Tables 17–19).

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained mechanism by which the detector surpasses its teacher.** AdaND's linear detector is trained on ZS-CLIP's pseudo-labels, which have ~28% error in detection (ZS-CLIP Acc_N = 72.08 on ImageNet, Table 3), yet achieves 91.90 Acc_N — a 20-point gain. The paper provides no analysis of pseudo-label quality, no comparison of AdaND vs. ZS-CLIP score distributions, no discussion of how a linear layer trained on ~28%-noisy labels can systematically *correct* the teacher's mistakes rather than regress toward them, and no synthetic experiment or theoretical argument to explain the improvement. The ablation in Table 6 confirms the detector *matters*, but does not explain *why* it helps so dramatically. This is a significant gap: the method's entire advantage over the frozen baseline hinges on this unexplained improvement. While the empirical results survive reproducibility skepticism (they are demonstrated across many datasets), the lack of mechanistic understanding weakens the paper's credibility.

2. **Asymmetric comparison in the Zero-Shot OOD Detection task (Table 5).** AdaND is evaluated under a protocol that allows online adaptation on the test stream (training a detector from the test data), while all comparator methods (Energy, MaxLogit, MCM, CLIPN, NegLabel) are evaluated in the standard static setting — no adaptation, no access to test-time information. The paper presents this as a straightforward head-to-head ("Our approach demonstrates competitive performance compared to state-of-the-art OOD detection methods") without acknowledging the protocol asymmetry. The 9.40% FPR95 improvement may partly reflect this advantage rather than a fundamentally better detector. The paper should either include adaptation-based OOD baselines (e.g., Tent adapted for OOD, or methods discussed in the reference to Fan et al. 2024) or explicitly re-frame the section as *test-time adapted* OOD detection with a clear statement of the comparison's limitations.

### Minor

1. **No quantification of pseudo-label noise the detector must overcome.** The paper reports ZS-CLIP's Acc_N as 72.08 on ImageNet, implying ~28% error in the training signal for AdaND. Reporting the fraction of pseudo-labels that match ground-truth labels would directly quantify the noise level and make the reported improvement more interpretable. This is easy to compute from existing experiment infrastructure.

2. **No oracle upper bound for the detector.** An ablation training the detector on ground-truth labels (only possible on benchmarks) would establish an upper bound and clarify how much of the performance gap is due to the linear layer's capacity vs. the quality of the training signal.

### Trivial

- None that survive filtering (formatting artifacts are parser issues, not author errors).

## Nice-to-Haves

- Provide a brief intuitive or theoretical argument for why a linear layer on frozen CLIP features can achieve better binary separation than the MCM score (which is itself a linear function of features via cosine similarity). A small synthetic experiment with known separability would be illuminating.
- Discuss why Gaussian noise in feature space serves as an effective OOD proxy — does its distribution empirically match that of real OOD features? The empirical success suggests it does, but a brief comment would strengthen intuition.
- Show that pseudo-label accuracy evolves (or does not degrade) over the course of adaptation, particularly after the stage switch. The paper states pseudo-labels come from ZS-CLIP throughout (Sec. 4.1), so the self-training concern raised by one reviewer does not apply — but tracking label accuracy over time would be informative.

## Removed Points

These points were flagged by one or more reviewers but are removed or downgraded for the reasons below:

1. **Self-training / confirmation bias after stage switch (Harsh Reviewer).** The reviewer claimed that after switching to AdaND for detection, "the detector's own outputs determine what is used as pseudo-labels for future training." The paper explicitly states the opposite (Sec. 4.1): "we use the detection results from ZS-CLIP as pseudo-labels in test-time **throughout the process**." Pseudo-labels are always from ZS-CLIP, not the detector's own outputs. The paper also acknowledges (line 201) that using detector outputs as pseudo-labels hurts performance. This criticism is based on a misreading and is removed.

2. **"The paper should also cover additional tasks/domains" style criticisms.** None of the reviewers made such points; no action needed.

## Novel Insights

The single most novel observation that emerges from the reviews (beyond the paper's own contributions) is the unresolved puzzle at the heart of the method: how does a linear layer trained on ~28%-noisy pseudo-labels improve detection accuracy from 72% to 92%? This is not a refutation of the paper — the empirical evidence across many datasets is strong — but it marks a clear gap between the method's empirical success and the paper's explanatory depth. The gradient analysis (Figure 4) explains *why existing methods fail*, but no corresponding analysis explains *why AdaND succeeds*. Bridging this gap would meaningfully elevate the paper.

## Suggestions

1. **Analyze the detector's learning dynamics.** Show the accuracy of ZS-CLIP's pseudo-labels vs. ground truth over the data stream, and plot what fraction of ZS-CLIP's detection errors AdaND corrects. Compare AdaND vs. ZS-CLIP score distributions side-by-side on representative dataset pairs.
2. **Re-frame the ZS-OOD detection section.** Acknowledge the protocol difference explicitly and either add adaptation-based baselines or rename the task to "test-time adapted OOD detection."
3. **Add an oracle ablation.** Train AdaND on ground-truth detection labels to establish an upper bound and isolate the effect of pseudo-label noise.
4. **Provide intuition for the linear layer's advantage over MCM scores.** The MCM score is essentially a softmax over cosine similarities to text embeddings. A binary linear layer has more flexibility to reorient the decision boundary in feature space. A brief explanation or small-scale synthetic demonstration would help.

## Score and Decision

**Overall assessment:** The paper identifies a genuine and practical problem, provides a convincing analysis of why existing TTA methods fail, and proposes a simple, efficient method with consistently strong empirical results across 44 dataset pairs. The benchmark and analysis are contributions in their own right. However, the paper is weakened by (1) a key unexplained result — how a detector trained on noisy pseudo-labels outperforms its teacher by 20 points — that lacks mechanistic analysis, and (2) an asymmetric OOD detection comparison that is presented as a direct head-to-head. These are real issues but not fatal: they concern completeness and framing rather than correctness. The empirical results are reproducible and demonstrated at scale.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>