Now I have all the information needed to write a verified, consolidated review.

## Summary

This paper proposes NeMal, a pipeline combining large language models, a fine-tuned Stable Diffusion text-to-image model, and preference-based filtering to generate synthetic marine images at scale, along with MarineSynth — a dataset of over 4 million text-image pairs across 2,332 marine conceptions. The key empirical result is that combining few-shot real data (5 images per class) with synthetic data from the pipeline achieves 57.25% classification accuracy, essentially matching the Oracle model trained on all 9,400 real images (57.83%). The paper also demonstrates the synthetic data's utility for coral reef segmentation (via pseudo-labels from CoralSCOP) and vision-language model fine-tuning.

## Strengths

- **First large-scale synthetic marine dataset with demonstrated downstream utility**: MarineSynth (4M+ images, 2,332 conceptions) is an order of magnitude larger and more diverse than prior simulator-based marine datasets. Table 1 provides a clear comparison showing NeMal uniquely supports pure synthetic data, domain-specific generation, and task-agnostic use simultaneously, unlike NEIL/NELL or DreamDA.

- **Few-shot + synthetic data matches real-data Oracle**: The strongest empirical finding (Table 2) — 5-shot real data + ChatGPT + Alt-text synthetic data achieves 57.25% vs. Oracle's 57.83% on the IND test set — convincingly demonstrates that synthetic data can dramatically reduce human collection and labeling effort for classification.

- **Systematic ablation of text prompt sources with clear design guidance**: Table 2 separately evaluates BLIP2 captions, Alt-texts, and ChatGPT prompts across in-distribution (IND), out-of-distribution (OOD), and challenging (CLG) test sets, revealing that combining ChatGPT and Alt-texts achieves the best overall accuracy (53.66% vs. 46.37% for ChatGPT alone). This offers actionable guidance for future synthetic dataset construction.

- **Cross-task generalization demonstrated**: Beyond classification, the paper shows synthetic data helps coral reef segmentation (SAM-F improving from 72.94 to 79.22 IoU with 1 point prompt, Table 4) and VLM fine-tuning (LLaVa1.5 improving from 76.4% to 80.7%, Table 5), supporting the task-agnostic claim.

- **Preference-based image picking validated**: Figure 5 (right) shows increasing the number of synthesis trials *m* from 1 to 4 improves downstream accuracy, confirming the practical value of the human-feedback-based binary selector trained on 100K volunteer judgments.

## Weaknesses

### Fatal
None.

### Major

- **Fine-tuning data for SD1.5 is not specified, creating a reproducibility gap**: Section 3.1.3 states: "We first construct our internal marine text-image data based on our marine conception list for fine-tuning." No details are given about the number of images, their sources (beyond the conception list), how they were captioned, what quality filters were applied, or the training hyperparameters. Since the entire pipeline depends on the domain-adapted T2I model, this omission prevents reproduction and comparison. This is the paper's most consequential flaw.

### Minor

- **"Never-ending" framing is inflated relative to the evidence**: The title and central framing trade on "never-ending" learning, but every experiment is a single-pass generation with clear saturation (Figure 5, left, and the paper's own statement: "the top-1 classification accuracy converges, proving that we cannot unlimitedly promote the classification accuracy"). The paper does acknowledge this upper bound (§5, Fig. 2) and defines "never-ending" in terms of the pipeline's throughput capacity rather than unbounded improvement (line 171). However, the discrepancy between the headline claim and the demonstrated convergence remains a significant overstatement that should be corrected.

- **No confidence intervals or error bars on any experimental result**: Table 2 (classification), Table 4 (segmentation), and Table 5 (VLM) all report point estimates without standard deviations, confidence intervals, or any measure of uncertainty. Given the stochasticity in T2I generation, model training, and few-shot data draws (e.g., the critical 5-shot result), this makes it impossible to assess whether reported differences are statistically significant.

- **CoralSCOP's own test-set performance is not reported in the segmentation experiment (§4.3)**: The paper uses CoralSCOP to generate pseudo-labels for synthetic coral images, then trains SAM-F, DeepLabV3, and SegFormer on those pseudo-labels. How well CoralSCOP itself performs on the 400 real coral test images is never reported. If CoralSCOP already achieves high IoU, the improvement from training on its pseudo-labels may largely reflect distillation rather than a novel benefit of synthetic data. Reporting this baseline would clarify the contribution.

### Trivial
None that affect the evaluation.

## Nice-to-Haves

- **Synthetic image quality metrics**: Adding FID/KID scores between MarineSynth and real marine images would help quantify the distribution gap and contextualize the classification results. The paper currently uses downstream accuracy as the sole quality proxy.
- **Pseudo-label quality analysis for segmentation**: A small human evaluation of CoralSCOP's pseudo-labels on a sample of synthetic coral images would strengthen the segmentation experiment.
- **Second marine classification dataset**: Testing on an additional marine recognition benchmark (e.g., ROV transect data) would strengthen the generalization claim beyond Sea-animal.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh Critic's point about segmentation baseline**: The claim that "this comparison does not establish whether the synthetic data is *useful* for coral segmentation, because it conflates two effects" — The comparison is vanilla SAM (no coral training, 72.94 IoU) vs. SAM-F (trained on synthetic coral, 79.22 IoU). The improvement IS demonstrably from the synthetic data. The requested baseline of "SAM-F fine-tuned on real coral images" would answer a different question (synthetic vs. real data) that is outside the paper's scope (which aims to show synthetic data can replace real collection/labeling). Removed as factually incorrect reasoning. Only the valid sub-point about CoralSCOP's own unreported performance is kept above.

2. **Harsh Critic's complaint about QA dataset not being released**: "The constructed QA dataset is not released (only mentioned)" — This criticizes release status. Rule: REMOVE criticisms about release status of items described in the paper.

3. **Harsh Critic's comment that 12 volunteers providing 100K preferences is "downplayed as minimal"** — The paper transparently reports 12 marine biologist volunteers and 100K image pairs. This is a descriptive nitpick, not a genuine weakness.

4. **Harsh Critic's request for "person-hours" breakdown** — Overly specific implementation detail, not standard to report.

5. **Strength Finder claim 1 about "first never-ending marine learning system"** — While Table 1 supports this, the "never-ending" framing is itself a verified weakness, and the strength conflicts with the verified weakness. Per rules: "when a strength and weakness disagree, the weakness wins." Moved here.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's "never-ending" framing and its own experimental evidence of saturation. The paper explicitly acknowledges an upper bound (Fig. 2, §5) and shows convergence in Fig. 5, yet the title and abstract maintain the "never-ending" claim. This is not a fatal contradiction — the paper defines never-ending as pipeline throughput capacity, not unbounded improvement — but it reveals a mismatch between how the system is marketed and what the evidence supports. The reviews collectively point out that the paper's strongest contribution is not the "never-ending" framing but rather the concrete demonstration that a single-pass synthetic data pipeline, when combined with very few real images (5-shot), can match a full-data Oracle model. This is the result that future work should build on.

## Suggestions

1. **Specify the SD1.5 fine-tuning data in full**: Report the number of images, sources, captioning method, filtering criteria, training hyperparameters, and compute used. This is essential for reproducibility.
2. **Tone down the "never-ending" framing**: Rephrase the title and abstract to reflect what is actually demonstrated — e.g., "scalable synthetic data generation for marine vision" — and reserve "never-ending" for a discussion of the pipeline's theoretical capacity rather than a claimed property validated by experiments.
3. **Add confidence intervals or standard deviations** to all main results, especially the few-shot classification comparisons.
4. **Report CoralSCOP's direct test-set performance** on the 400 real coral images used in §4.3 to clarify the segmentation experiment.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>