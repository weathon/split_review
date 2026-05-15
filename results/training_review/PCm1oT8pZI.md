Now I have a thorough understanding of the paper, the reviews, and how the paper's evidence relates to the criticisms. Let me produce the final consolidated review.

## Summary

This paper proposes a backdoor-based watermarking method that requires no training data — using a single out-of-distribution (OoD) image as the sole data source for watermark injection. The method (1) constructs a surrogate dataset via strong augmentations of one OoD image, (2) poisons it with a trigger, and (3) fine-tunes the model with an adversarial weight perturbation (WP) objective designed to improve robustness against removal attacks. Experiments on CIFAR-10, CIFAR-100, and GTSRB across six trigger patterns and three removal attack types (fine-tuning, pruning, model extraction) demonstrate that the method achieves high OoD watermark success rates (e.g., 95.66% on CIFAR-10) and that the WP procedure substantially improves post-attack WSR (e.g., 19.94%→57.52% under RT-AL).

## Strengths

- **First data-free backdoor watermark using a single OoD image, eliminating any dependency on training data.** The paper explicitly identifies the gap — "watermark injection without training data is barely explored" (Introduction) — and delivers a method that constructs a surrogate dataset entirely from one OoD image via strong augmentations (Section 3.1). This contrasts with prior data-free methods like Li et al. (2022) that require training a generator over hundreds of epochs.

- **Remarkable sample and time efficiency: one image and ≤30 epochs suffice for injection.** Injection on CIFAR-10 converges in only 10 epochs (Section 4.1, Figure 1), and the entire process uses a single OoD image. The high OoDWSR (95.66% on CIFAR-10, Table 2) is achieved with <3% accuracy degradation, all without any original training data.

- **Weight perturbation (WP) demonstrably improves robustness across all three removal attacks.** Under the strongest attack (RT-AL) on CIFAR-10, WP raises OoDWSR from 19.94% to 57.52% for trojan_wm and from 12.81% to 24.19% for trojan_8x8 (Table 6). Suspect models consistently maintain OoDWSR far above non-watermarked baselines with p-values < 0.05 (Tables 2–3), confirming statistical ownership verification.

- **The paper provides a direct comparison showing OoD-injected watermarks are substantially more robust post-attack than i.i.d.-injected ones** (Table 4): after RT-AL, i.i.d. injection's WSR drops to ~4% while OoD injection retains 57.52% / 24.19% for the two tested triggers. This comparison, though asymmetric in data quantity (favoring the ID baseline), makes the robustness advantage more striking.

- **Comprehensive evaluation across three datasets, six trigger patterns, and three removal attack types**, including a study of how OoD source image choice affects watermark quality (Table 5), providing practical guidance (dense images > sparse images).

## Weaknesses

### Fatal
None. The paper's core claims — that a single OoD image suffices for watermark injection and that the WP procedure improves robustness — are supported by the experimental evidence. The high IDWSR (>90% on CIFAR-10, Table 2) on i.i.d. test images with triggers demonstrates that the watermark generalizes beyond the narrow OoD augmentation distribution, directly contradicting any claim that the results are merely overfitting artifacts.

### Major

- **Missing comparisons with existing data-free and OoD-based watermarking baselines.** The paper cites Li et al. (2022, data-free via generator) and Wang et al. (2022, OoD-based with PTYNet) as closely related prior work, yet provides no experimental comparison against them on the same datasets and attacks. Without these baselines, the claimed advantages in efficiency, robustness, and simplicity cannot be properly assessed. While the paper's focus on sample efficiency (single image) distinguishes it, a direct comparison — even a brief one — is needed to establish that the method is not merely competitive but superior or complementary to existing approaches.

- **The weight perturbation ablation conflates multiple components.** Table 6 compares "with WP" (uses Eq. 2: adversarial perturbation + KL divergence term) vs. "without WP" (uses Eq. 1: basic cross-entropy only). The improvement from ~20% to ~57% could stem from the adversarial perturbation, the KL term, the training schedule (first 5 epochs with WP), or their combination. No ablation isolates these factors, and no comparison to standard sharpness-aware minimization (SAM) or adversarial weight regularization is provided. This makes it unclear which specific design choice drives the robustness gain.

### Minor

- **No cross-OoD-image verification test.** The watermark is verified on surrogate data generated from the *same* OoD image used for injection. While the high IDWSR on i.i.d. test data shows the backdoor generalizes beyond narrow OoD augmentations, a direct test — verifying the watermark on surrogate data from a *different* OoD image — would strengthen the claim that a generalizable backdoor has been implanted. The paper tests different source images for injection (Table 5) but not for verification.

- **Non-watermarked model exhibits non-negligible OoDWSR for some triggers.** On CIFAR-10, the non-watermarked model has OoDWSR of 4.87% for trojan_wm (Table 2), well above random chance (10% for CIFAR-10, but 4.87% is also above zero). While suspect model OoDWSR (57.52% after attack) vastly exceeds this baseline, the elevated false-positive rate for certain triggers deserves discussion and a clear operational threshold for ownership claims.

- **No hyperparameter sensitivity analysis for γ and β.** The perturbation constraint γ is set to 0.1 or 0.05, and the KL trade-off β is fixed at 6 (Section 4), with no sensitivity sweep showing the accuracy–robustness trade-off. A small ablation would help practitioners understand the method's practical range.

### Trivial
None of substance beyond what has been addressed above.

## Nice-to-Haves

- **Component ablation for WP:** Isolating the effect of the KL term vs. the adversarial perturbation, and comparing against SAM or weight decay, would strengthen the paper's claims about the WP mechanism.
- **Larger surrogate datasets from multiple OoD images:** Combining patches from several OoD images could improve watermark generalization and further address overfitting concerns.
- **Quantitative metrics for OoD/ID distribution overlap** (e.g., MMD distance) to supplement the qualitative t-SNE visualization in Figure 3.

## Removed Points

The following points from the Harsh Critic were evaluated against the paper and removed for the stated reasons:

1. **"The ID vs OoD comparison is unfair because ID uses the entire training set"** — Removed per hard rules: the asymmetry favors the baseline (ID has more data). The paper uses this asymmetry intentionally to show that OoD injection is *more* robust despite having far less data. This criticism, if anything, strengthens the paper's result.

2. **"The evaluation cannot distinguish between genuine backdoor and overfitting to a narrow distribution"** — The paper already reports IDWSR >90% on i.i.d. test images with triggers, which directly refutes the pure-overfitting hypothesis. If the model were simply memorizing OoD augmentations, it would not generalize to i.i.d. data. The critic's own Section-by-Section notes acknowledge this as "surprising" and "contradict[ing] the overfitting hypothesis."

3. **"Missing appendix, missing proofs, absent references"** — Per hard rules, the parser strips these sections from all papers; they exist in the original submission.

4. **Formatting/style nitpicks, typo concerns, and requests for trivial implementation details** — Per hard rules, these are parser artifacts or out of scope for evaluation.

## Novel Insights

The paper's most interesting observation — that high IDWSR (>90%) emerges despite the model being fine-tuned *only* on OoD data — is noted by the critic but could be elevated. The t-SNE analysis in Figure 3 suggests that the OoD data lies close enough to the ID data distribution that the trigger learned on OoD samples transfers to ID samples. This raises an intriguing question for the watermarking community: if a backdoor can be injected without any in-distribution data while still activating on in-distribution inputs, then the traditional assumption that watermarking requires access to the original training distribution may be unnecessarily restrictive. The robustness differential (OoDWSR preserved after fine-tuning while IDWSR collapses, as seen for GTSRB in Table 2) further suggests that OoD watermarks exploit a fundamentally different kind of decision-boundary feature than i.i.d. watermarks — one that is less aligned with the fine-tuning objective and therefore harder to erase. The paper does not fully develop this explanation, but it is a promising direction for future work.

## Suggestions

1. **Add baseline comparisons** with Li et al. (2022) and/or Wang et al. (2022) on at least one dataset (e.g., CIFAR-10) under the same removal attacks. Even if these methods cannot be exactly replicated, reporting their published results under comparable settings would contextualize the contribution.

2. **Add a cross-OoD-image verification experiment:** inject a watermark using one OoD image (e.g., "City") and verify using a different OoD image (e.g., "Animals" or "Bridge"). If OoDWSR remains high, this directly addresses the generalization concern.

3. **Ablate the WP components:** compare (a) no WP, (b) WP without the KL term, (c) standard SAM, and (d) the full proposed method. This would isolate whether the robustness gain comes from the adversarial perturbation, the KL regularization, or their combination.

4. **Report a sensitivity analysis** for γ and β (even a 3-value sweep per parameter) to demonstrate that the method is not brittle to hyperparameter choice.

5. **Discuss the elevated non-watermarked OoDWSR** (4.87% for trojan_wm) and propose a concrete decision threshold for ownership claims that accounts for this false-positive rate.

## Score and Decision

**Originality:** 3.5/5 — The idea of using a single OoD image is genuinely novel within data-free watermarking, though the individual components (backdoor injection, weight perturbation) build on known techniques.

**Importance of research question:** 4/5 — Removing the need for training data has clear practical relevance for model protection in federated learning, third-party IP auditing, and foundation model scenarios.

**Claims well-supported:** 3/5 — The core claims (data-free feasibility, efficiency) are well-supported. The robustness claim is partially supported but weakened by missing baselines, incomplete WP ablation, and the lack of cross-OoD-image verification.

**Soundness of experiments:** 3.5/5 — Broad coverage of datasets/triggers/attacks is commendable, but the two missing baselines and the unablated WP comparison are noticeable gaps.

**Clarity of writing:** 4/5 — The method is clearly presented and the figures are helpful.

**Value to the research community:** 3.5/5 — Useful demonstration that single-image OoD watermarking is feasible; the robustness differential between OoD and i.i.d. watermarks is a genuinely interesting finding. However, the contribution would be stronger with the missing baselines and ablations.

**Overall:** This paper tackles a real problem and presents a clever, sample-efficient solution. The evidence supports the core feasibility claim, and the WP robustness improvement is demonstrated. However, the paper's reach is limited by the absence of comparisons to existing data-free methods and the incomplete WP ablation. These are addressable gaps rather than fatal flaws. With the suggested experiments, the paper could be significantly strengthened.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>