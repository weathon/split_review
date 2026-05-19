- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

The paper proposes DIAGNOSIS, a method to detect unauthorized data usage in text-to-image diffusion models. The key idea is to "coat" protected images with a stealthy warping function before release, then check whether a model trained on those images reproduces the warping pattern in its outputs. The authors define two types of memorization (unconditional and trigger-conditioned), train a binary signal classifier to detect the warping, and use a statistical hypothesis test to decide if unauthorized usage occurred. Experiments on Stable Diffusion v1/v2 and VQ Diffusion with LoRA, DreamBooth, and standard training report 100% detection accuracy across many settings.

## Strengths

- **Novel approach combining dataset watermarking with diffusion model memorization.** The idea of planting a detectable artifact through steering memorization is well-motivated and distinct from prior work on sample-level memorization. The paper provides a formal definition (Definition 1) and a clean pipeline (coating → classifier training → hypothesis testing).

- **100% detection accuracy with a large memorization-strength gap.** In Table 1, the method achieves 0 false positives and 0 false negatives across all fine-tuning settings. The memorization strength averages 91.2% for unauthorized models vs. only 5.1% for legitimate models — a large separation that makes the detection threshold reliable.

- **Robust performance under multi-source partial-data scenarios.** Table 3 shows 100% detection even when the infringer collects only 25% of training data from the protected set, with distributional differences (non-overlapping classes) across data sources. This is a realistic and challenging scenario.

- **Small impact on generation quality.** For unconditional memorization, the FID increase from 208.38 (standard) to 218.28 is modest. Visual examples (Fig. 1–4) support the claim that the warping is stealthy.

- **Works across multiple models and fine-tuning methods.** The method is demonstrated on Stable Diffusion v1/v2 and VQ Diffusion with LoRA, DreamBooth, and standard training, supporting the claim of broad applicability.

## Weaknesses

### Fatal
None.

### Major

1. **Testing prompts are sampled from the training set, conflating element-level and sample-level memorization.** The memorization strength is approximated using prompts sampled from the protected dataset (Section 3.3: *"The set I can be obtained by sampling a set of the text prompts in the protected dataset"*). Because these prompts were seen during training, the model could simply be reproducing specific warped training images (sample-level memorization) rather than learning the warping function as a general transformation (element-level memorization). The paper claims element-level memorization as a core conceptual contribution, but does not test with held-out prompts or cross-domain prompts to isolate the mechanism. This leaves the central conceptual claim unsupported and raises the question of whether the method would work when the infringer uses different captions than those in the protected dataset.

2. **Cross-method robustness is not evaluated.** The paper claims the method is *"independent of the model used in the unauthorized training or fine-tuning process"* (Section 1). However, every experiment matches the training method used by the infringer to the method assumed by the protector (e.g., both use LoRA). No experiment tests scenarios where the protector coats data assuming LoRA but the infringer uses DreamBooth, or vice versa. Without such cross-method evaluation, the claimed model-agnostic independence is not supported, and the method's robustness to realistic variation in the infringer's training protocol is unknown.

### Minor

3. **Comparison to prior work is narrow and lacks detail.** Only one baseline (Yu et al., 2021) is compared, with very sparse implementation details. The paper reports 50% accuracy for the baseline vs. 100% for DIAGNOSIS (Table 5), but does not describe how the adaptation was performed, what hyperparameters were used, or whether the baseline was given a comparable experimental setup. A broader comparison would strengthen the claim of superiority.

4. **Small evaluation scale limits the strength of the perfect-accuracy claim.** Detection accuracy is measured on only 20 models per class (40 total) in each Table 1 setting. With 40 binary classification trials, the 95% confidence interval for 100% accuracy ranges from roughly 91% to 100%. While the large memorization-strength gap mitigates this concern, explicitly reporting confidence intervals or using more seeds would improve statistical rigor.

5. **FID degradation for trigger-conditioned memorization with the trigger is notable.** The FID increases from 208.38 (standard) to 239.03 (trigger-conditioned with trigger). The paper asserts stealthiness based on visual examples but does not provide a quantitative perceptual metric (e.g., LPIPS) or a human evaluation study to substantiate this claim.

### Trivial

None.

## Nice-to-Haves

- Test detection with held-out prompts (e.g., from a different dataset distribution) to distinguish element-level from sample-level memorization.
- Evaluate cross-method detection (e.g., protector assumes LoRA, infringer uses DreamBooth) and cross-model detection (e.g., classifier trained on SD v1 applied to a VQ Diffusion model).
- Add experiments testing whether the signal classifier transfers across domains (train on coated Pokemon images, test on generated CUB-200 images).
- Compare to a simple baseline such as an invisible watermark embedded in the protected images.
- Report false positive rate (β) and detection thresholds consistently across all experiments, not only in the ablation (Table 6).

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"No justification for τ=0.05 and γ=0.05"** — The paper explicitly states these follow Li et al. (2023b). This is adequate justification.
- **"The adaptive infringer is not summarized in the main text"** — The paper points to Appendix A.4 for this discussion. The appendix was stripped by the parser; this is not an author error.
- **"Missing related works"** — Cannot be verified without external sources.
- **"The hypothesis testing is reused without adaptation"** — Adopting a well-established statistical test is standard practice.
- **"No discussion of natural images resembling warping"** — The warping is a specific geometric transformation (Nguyen & Tran, 2021); this concern is speculative.
- **"No evaluation of detection time or computational cost"** — Useful but not a core evaluation requirement for a method paper.
- **"No human perceptual study of stealthiness"** — Not standard for this type of evaluation; visual examples and FID are accepted proxies.
- **Strength Finder generic claims** (e.g., "the paper targets an important problem") — These are too generic to retain as substantive strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Design a controlled experiment using held-out prompts (from outside the training set) to test whether the model applies the warping function to unseen captions. This would directly support or refute the element-level memorization claim.
2. Add cross-method experiments: coat data assuming LoRA, but have the infringer use DreamBooth (and vice versa). Also vary hyperparameters (learning rate, number of steps, LoRA rank) to test robustness.
3. Provide more detail about the Yu et al. (2021) adaptation: how was the fingerprint encoder trained, what data was used, were hyperparameters tuned? Consider adding at least one additional baseline (e.g., a simple backdoor trigger injected into the diffusion model).
4. Report 95% confidence intervals for the detection accuracy, or increase the number of random seeds to 50+ per class.
5. Include a quantitative perceptual metric (LPIPS, SSIM) for the warped images and the generated images to substantiate the stealthiness claim beyond FID.
