Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Add-it, a training-free method for inserting objects into images using pretrained diffusion models (specifically FLUX). The key technical contribution is a weighted extended-attention mechanism that balances attention from three sources—the source image, the target image, and the text prompt—via an automatic root-finding scheme. The method is complemented by a noising-based structure transfer step and a Subject-Guided Latent Blending mechanism to preserve background details. The paper also introduces a new "Additing Affordance Benchmark" for evaluating object placement plausibility. Without any task-specific fine-tuning, Add-it achieves state-of-the-art results across multiple benchmarks, with human preference exceeding 80% against both training-free and supervised baselines, and an affordance score of 0.828 (nearly doubling the best prior method at 0.474).

## Strengths

- **Novel weighted extended-attention mechanism with automatic balancing achieves a step-change improvement in affordance.** The paper identifies and explicitly models the three-way attention competition (source, target, prompt) in MMDiT blocks and introduces a root-finding procedure to balance them. This yields 0.828 affordance vs. 0.474 for the best prior method (Prompt2Prompt, Table 1), directly supporting the central claim that attention balancing is critical for natural object placement.

- **State-of-the-art results on both real and generated image benchmarks, validated by human preference.** Add-it achieves the best CLIP_dir (0.101), CLIP_out (0.322), and Inclusion (81%) on the Emu Edit benchmark (Table 2) despite using no training. Human evaluations (Figures 1A–B) show the method is preferred in ~80% of cases against supervised baselines and ~90% against zero-shot methods, providing strong independent validation of output quality.

- **Introduction of the Additing Affordance Benchmark fills a genuine evaluation gap.** Prior evaluation protocols lacked a systematic way to measure placement plausibility. The benchmark of 200 manually annotated images with a detection-based protocol reveals that prior methods severely underperform (best: 0.474), while Add-it achieves 0.828 (Table 1). Human preference studies further corroborate the metric's relevance.

- **Comprehensive ablation study isolating each component.** Figure 3 (attention balancing), Figure 5 (structure transfer timestep sweep), and Figure 6 (latent blending) each isolate a design choice with quantitative or clear qualitative evidence. The ablation of γ over a range of values with affordance and inclusion curves (Figure 3A) convincingly shows why the automatically chosen γ is optimal.

- **Practical noising-based approach for real images circumvents FLUX's inversion difficulties.** Rather than requiring a costly or unreliable inversion, the method uses a simple forward-noising strategy (Section 3.5) that guarantees perfect reconstruction at t=0 while still enabling the extended-attention pipeline. This is a pragmatic engineering contribution.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by evidence across multiple benchmarks and human evaluations. The issues listed below are addressable and do not invalidate the contribution.

### Minor

- **The attention balancing analysis (Figure 3B) is shown on a small validation set, and the transfer of γ from prompt-query optimization to all attention queries is not fully characterized.** The root-finding objective uses prompt queries Qₚ specifically (balancing A_source and A_target defined via Qₚ), but the resulting γ is applied to all queries (including Q_target) in the full attention computation. The paper argues empirically that this works (benchmark results confirm this), but the analysis of why this transfer holds—and whether there are failure cases where it does not—is limited to the small set shown in Figure 3B. A broader characterization of the chosen γ distribution across diverse scenes would strengthen the generality claim.

- **The structure-transfer timestep t_struct=933 is fixed after a single ablation sweep, without analysis of content-dependent variation.** The ablation in Figure 5 shows a clear tradeoff, but the optimal timestep may depend on scene complexity or object properties. The paper does not investigate whether this fixed choice causes systematic failures in particular settings (e.g., highly cluttered vs. sparse scenes). Given that this is a single hyperparameter, a brief analysis of its sensitivity across scene types would be informative.

- **The real-image performance gap is acknowledged but not analyzed.** The paper states that results on real images are less effective than on generated images and attributes this to FLUX inversion (Section 6). However, the forward-noising approach used for real images (Section 3.5) produces noisy latents by a different process than the natural reverse-diffusion path for generated images. The paper does not examine how this distribution mismatch affects the attention balancing or the structure transfer. While the method still achieves SOTA on real images, diagnosing this gap could lead to further improvements.

- **The affordance metric's robustness to detector failure modes is not discussed.** The metric relies on Grounding-DINO for object detection, and it is unclear how detection failures are handled (e.g., a missed detection would likely lower the score rather than inflate it, but this is not specified). Additionally, the metric checks bounding-box location but does not explicitly account for object scale or orientation plausibility within the bounding box. The paper reports human evaluations that independently support the method's quality, but the affordance metric's design choices could be documented more completely. (The paper states that construction details are in the appendix, which was not available for review.)

- **Computational cost (runtime, GPU memory) is not reported.** The method runs two parallel denoising processes plus SAM-2 segmentation. A brief wall-clock and memory comparison against baselines would help practitioners assess the practical overhead of the "training-free" advantage.

### Trivial

- A hyperparameter summary table listing all parameters (T_blend, t_struct, attention layers for aggregation, Otsu thresholds, SAM-2 sampling details) concisely would improve reproducibility. The paper references the appendix for these details, but a compact table in the main text would be helpful.

## Nice-to-Haves

- Characterizing the distribution of automatically chosen γ values across diverse image scenes (indoor, outdoor, cluttered, simple) to confirm the root-finding consistently balances attention.
- Comparing attention distributions between the generated-image and real-image cases to diagnose the source of the performance gap noted in Section 6.
- Validating the affordance metric with a human correlation study on a subset of the benchmark outputs.
- A brief discussion of how the approach might adapt to other MMDiT-based architectures (e.g., SD3) or to U-Net-based diffusion models.

## Removed Points

The following points from the reviews were removed per filtering rules:

- **Criticism that the auto-balancing is validated only on a small set "without broader validation."** — Partially misreads the paper. The "small validation set" mention in the caption of Figure 3 applies specifically to panel B (attention distribution visualization), not to the overall method validation, which uses the full benchmarks (200-image Affordance Benchmark, 100-image Additing Benchmark, Emu Edit benchmark). The benchmark results provide substantial indirect validation of the balancing mechanism.

- **Criticism that the affordance benchmark details (annotator agreement, construction) are absent.** — The paper explicitly states these details are in the appendix (\cref{sec:affordance_extra_details}), which was stripped by the parser.

- **Criticism about implementation details and hyperparameters being absent.** — The paper states "further details can be found in \cref{sec:implementation_details}" (stripped appendix).

- **Criticism that Grounding-DINO non-detection would "inflate affordance scores."** — Without evidence, this attribution is speculative. If Grounding-DINO fails to detect an object, the object is not counted as correctly placed, which would lower the affordance score rather than inflate it. The direction of the potential bias is the opposite of what the reviewer assumes.

- **Weakness about missing SAM-2 refinement step ablation.** — An interesting experiment but not necessary to validate the core contribution, and the method's results are strong without it.

## Novel Insights

The most interesting observation emerging from this review is that the paper's strongest contribution—the attention-balancing mechanism—is simultaneously the most validated (through benchmark results) and the least deeply understood (the transfer of γ from prompt-query optimization to full attention is accepted on empirical grounds rather than principled analysis). The 0.828 affordance score is so far ahead of the next best (0.474) that the result is not in doubt, but the mechanism's success raises a natural follow-up question: why does balancing two scalar quantities derived from Qₚ alone yield the correct balance for all queries and all tokens? This is a distinct and unanswered research question. Relatedly, the large gap between Add-it and all baselines on affordance (0.828 vs. 0.474 for the best prior work) versus the more moderate gap on CLIP-based metrics suggests that existing evaluation protocols systematically miss the affordance dimension—the paper's benchmark is itself a contribution that future work should adopt.

## Suggestions

1. Add a brief analysis of the distribution of automatically chosen γ values across the full Affordance Benchmark, partitioned by scene type or image complexity, to demonstrate the root-finding's robustness.
2. Include a short discussion of how the forward-noising real-image pipeline affects the attention distributions compared to the generated-image case, to clarify the acknowledged performance gap.
3. Document how Grounding-DINO detection failures are handled in the affordance metric (e.g., are they counted as incorrect placement or excluded?), even briefly in the main paper.
4. Add a runtime and GPU memory comparison against the main baselines (InstructPix2Pix, EraseDraw, Prompt2Prompt) to contextualize the "training-free" advantage.
5. Include a hyperparameter summary table in the main text (or supplement the pointer to the appendix with a brief table).

## Score and Decision

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>