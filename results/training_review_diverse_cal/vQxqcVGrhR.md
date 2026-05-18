Here is my consolidated final review.

---

## Summary

DisEnvisioner proposes a two-stage tuning-free framework for single-image customized generation. The **DisVisioner** stage uses learned queries to separate image features into subject-essential and subject-irrelevant visual tokens via a cross-attention image tokenizer; the **EnVisioner** stage enriches the subject tokens into a more granular representation. The subject-irrelevant tokens are discarded at inference. Experiments on the DreamBooth dataset show competitive text-alignment (C-T 0.315) and the lowest internal variance (IV 0.026) among compared methods, with fast inference (1.96s).

---

## Strengths

1. **Novel disentangle-then-enrich pipeline with practical benefits.** The two-stage design (DisVisioner → EnVisioner) is well-motivated. The ablation in Fig. 7 (supplementary) confirms that single-stage training fails, and the $\lambda_s$/$\lambda_i$ sweep (supplementary Figs. 1–3) provides visual evidence that the two token types contribute independently to the generation. This is a clean architectural contribution.

2. **Competitive quantitative performance on editability and robustness.** In Table 1, DisEnvisioner achieves the highest text-alignment score (C-T 0.315 vs. next-best 0.295) and lowest internal variance (IV 0.026 vs. next-best 0.029). These two metrics directly reflect the paper's stated goals of better instruction following and resistance to subject-irrelevant factors.

3. **Strong qualitative results across diverse scenarios.** Figures 2, 3, 4 (qualitative comparisons) show that DisEnvisioner more faithfully follows editing prompts (e.g., changing background, posture, accessories) while maintaining subject identity compared to baselines. The qualitative advantage over IP-Adapter (which tends to copy the full image) and BLIP-Diffusion (which struggles with editability) is clear and consistent.

4. **Tuning-free and efficient.** At 1.96s per generation, DisEnvisioner is competitive with the fastest tuning-free baselines while delivering stronger editability, supporting practical applicability.

5. **Ablation studies validate key choices.** The paper systematically ablates token counts ($n_s$, $n_i$) and the two-stage training strategy, demonstrating that the optimal configuration ($n_s=n_i=1$) meaningfully separates subject from background in attention maps, while larger token counts lead to collapse.

---

## Weaknesses

### Fatal
None.

### Major

1. **The core disentanglement claim is insufficiently validated.** The paper's central technical claim—that DisVisioner achieves "accurate disentanglement of subject-essential attributes" into "mutually independent and orthogonal" tokens—rests on: (a) qualitative attention-map visualizations (Figs. 5–6), and (b) the indirect Internal Variance metric. No direct quantitative measurement of disentanglement is provided. The paper should report, for example:
   - Attention overlap with ground-truth subject masks (e.g., via open-vocabulary segmentation) to show the subject token fires primarily on the subject and the irrelevant token on the background.
   - Cosine similarity between subject and irrelevant token outputs to verify near-orthogonality empirically.
   
   Without such evidence, the reader cannot tell whether the method genuinely separates *attributes* (pose, lighting, texture) or simply learns a coarse subject/background spatial split while still entangling attribute information.

   Furthermore, the theoretical justification in Sec. 3.2 is technically inaccurate: "mutual independence and orthogonality are ensured by the SoftMax(·) function applied at spatial dimension." SoftMax normalizes attention weights across spatial positions *for each query independently*; it does not enforce orthogonality or statistical independence *between* the resulting token representations. Two queries could attend to entirely different spatial regions yet produce features that are highly correlated. This inaccuracy should be corrected.

2. **Quantitative comparisons lack robustness measures and the mRank weighting is under-justified.** The mRank metric weights C-I and D-I at 0.5 each while all other metrics receive weight 1.0, on the grounds that C-I and D-I are "two sub-indicators of image-alignment." This choice is defensible but the paper does not show whether the ranking is stable under alternative weighting schemes (e.g., unweighted average, equal weights for all five metrics). More critically, **no confidence intervals, standard deviations, or significance tests are reported** for any metric in Table 1. The reported differences—particularly in C-T (0.315 vs. 0.295) and IV (0.026 vs. 0.029)—are small and could fall within measurement noise. Bootstrapping over the 30 subjects would clarify whether these differences are reliable.

### Minor

1. **User study methodology is underspecified.** The supplementary describes a study with 69 users and 345 rounds where participants assign grades 0–5. However, the paper does not state whether (a) method identity was hidden from participants, (b) image order was randomized across participants, or (c) images were presented in a consistent format. The large gap between DisEnvisioner and baselines in the user study (scores ~30% higher) relative to automated metrics (~6–7% higher for C-T) is striking and raises questions that methodological transparency would resolve. Without blinding details, the user study's evidentiary value is limited.

2. **No discussion of failure cases or limitations.** The paper does not discuss scenarios where the method might underperform (e.g., subjects that are very small in the reference image, backgrounds containing objects semantically similar to the subject, extreme pose variation). A limitations section would strengthen credibility and guide future work.

3. **The augmentation set used in DisVisioner is unspecified.** Line 149 mentions "an augmentation set" applied to the reference image to prevent the model from simply copying the input, but the specific augmentations (types, intensities) are never listed. Given that this is a critical component for preventing trivial solutions, the paper should specify the augmentations and ideally provide an ablation on this choice.

### Trivial

- Training cost (GPU-hours) is not reported, though training steps (120k × 2), batch sizes (160, 40), and hardware (8×A800) are provided. This would be useful for practitioners.
- There is a minor inconsistency: the user study description says "5 rounds in total" but 69 users × 5 rounds = 345 rounds, which matches the stated total. Clarify whether each user did 5 rounds or the total was 5 rounds across all users.

---

## Nice-to-Haves

- A comparison with additional recent tuning-free methods (Subject-Diffusion, InstantBooth, PhotoMaker) would strengthen the evaluation, though the paper's selection of the most closely related baselines is defensible.
- Reporting mRank with multiple weighting schemes (unweighted average, Borda count) or reporting per-metric ranks separately would address concerns about the weighting choice.
- An ablation measuring the contribution of each stage in isolation (DisVisioner alone → text-to-image generation without EnVisioner) would help isolate the benefit of enrichment.

---

## Removed Points

These points from the reviewers were removed for the following reasons:

- **"The ablation on token numbers undermines the claim"** — The ablation shows an expected behavior (more tokens → more capacity → collapse) and the paper explicitly discusses this. The observation that the method requires limited tokens to work does not invalidate the empirical finding; it is a known property of bottleneck-style tokenizers. The paper's claims are about what the method does *at its optimal configuration*, not that it enforces separation under all configurations.
- **"Comparison to more recent methods is missing"** — The paper compares to five leading methods encompassing tuning-based and tuning-free categories. Adding every available method is scope creep; the existing comparison is adequate for a conference submission.
- **"The training data may not match test distribution"** — This is a generic concern applicable to nearly all learned methods and does not specifically undermine any claim in the paper. Training on cropped bounding boxes from OpenImages is a standard practice in this line of work.
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem") that lack specific evidence were filtered out.
- **Strength Finder's claim of "comprehensive user study"** was moved here because the user study has methodological gaps (no stated blinding/randomization) that weaken its evidentiary value; the weakness prevails over the strength per the review guidelines.

---

## Novel Insights

One interesting observation emerges from combining the critic's and strength finder's analyses: the paper's two-stage training (separating disentanglement from enrichment) is both its main architectural contribution and the source of its validation gap. The DisVisioner training objective is pure reconstruction—there is no explicit loss encouraging the two tokens to be *informationally* disjoint in attribute space (as opposed to spatially disjoint). This means the claimed "disentanglement of subject-essential vs. irrelevant *attributes*" (pose, lighting, texture, background semantics) is an emergent property of the capacity bottleneck plus separate query initialization, not of any explicit inductive bias. The fact that the method works well in practice despite this suggests that the reconstruction objective plus limited token count may be sufficient for attribute-level separation on the training distribution, but this should be explicitly tested rather than assumed. A future paper could add a mutual-information minimization term between the token representations and study whether it improves generalization to out-of-distribution poses or backgrounds.

---

## Suggestions

1. **Provide direct quantitative disentanglement evidence.** Compute the overlap (e.g., attention-weighted IoU) between each token's spatial attention map and ground-truth subject/background masks from an off-the-shelf segmentation model (e.g., SAM, Grounding-DINO) on held-out images. Also report cosine similarity between the two token representations averaged over a large set of images.

2. **Add confidence intervals to Table 1.** Bootstrap over the 30 DreamBooth subjects and report 95% CIs for C-T, C-I, D-I, and IV. This would clarify whether the reported differences are stable.

3. **Report mRank under alternative weighting schemes** (e.g., unweighted average of all five per-metric ranks) to show the ranking is not an artifact of the chosen weights.

4. **Specify the user study design more thoroughly.** State whether images were anonymized and randomized, and ideally report inter-rater agreement (e.g., Fleiss' kappa).

5. **List the augmentation set used in DisVisioner** and provide a brief ablation showing the effect of removing it.

6. **Add a limitations section** discussing when the method might fail (small subjects, cluttered backgrounds, out-of-distribution poses).

7. **Correct the claim about SoftMax ensuring orthogonality** in Sec. 3.2. The method achieves empirical separation through training, not through a property of the SoftMax function.

---

## Score and Decision

This paper proposes a well-motivated framework and shows competitive results on an important task. The qualitative advantages in editability are compelling. However, the paper's core novelty claim—that it achieves accurate, explicit disentanglement of subject-essential vs. irrelevant features—is not convincingly supported by the evidence provided. The theoretical justification contains an inaccuracy, no direct quantitative measurement of disentanglement is offered, and the quantitative results lack error bars. While the method likely works better than the baselines for the intended use case, the paper's framing significantly overstates what is demonstrated. The weaknesses are addressable but require non-trivial additional analysis, not just text revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>