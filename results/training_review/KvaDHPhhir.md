Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces SketikZ, a dataset of 3,231 hand-drawn sketch–reference diagram–TikZ code triples collected using paper, whiteboard, and tablet tools, filling a genuine gap in paired sketch-to-code data. The authors also present ImgTikZ, a 6.7B-parameter code-specialized VLM (DeepSeek Coder + SigLIP) fine-tuned on large corpora (RenderTikZ, AugTikZ, ImgAugTikZ) with a multi-candidate inference strategy using a learned image-similarity selector (D-SigLIP). The system achieves subjective evaluation scores competitive with GPT-4o and Claude 3.5 Sonnet, despite being an order of magnitude smaller.

## Strengths

- **Novel dataset addressing an underexplored task.** SketikZ provides 3,231 triples (sketch, reference diagram, TikZ code) collected across three real-world tools (paper, whiteboard, tablet) with realistic noise (lighting, background, distortion). This fills the critical gap the paper correctly identifies: the lack of paired sketch-to-code data for training and evaluation (Section 3.2, Figure 4, Table 3).

- **Two data augmentation strategies with demonstrated effectiveness.** AugTikZ (GPT-3.5–generated code variations, 556K samples) and ImgAugTikZ (synthetic sketch-like image noise) are shown to improve performance: Table 4 shows clear degradation when removing each, and Table 5 shows ImgAugTikZ reduces the performance gap from rendered to sketch inputs (image similarity drop from 12.5% to 6.97%). These strategies are practical and likely transferable to other image-to-code tasks.

- **Multi-candidate generation with a learned visual selector is a useful methodological contribution.** Using D-SigLIP (fine-tuned SigLIP) for candidate selection is novel for image-to-diagram conversion. Figure 8 shows D-SigLIP selection continues improving with more candidates while CLIP plateaus at K=5, providing clear evidence that a well-tuned visual selector matters. The motivation — that code-level loss alone is insufficient for visual quality — is sound and supported by the low correlation between code similarity and human ratings (0.365).

- **Per-tool diagnostic analysis.** Table 6 breaks down performance across paper, whiteboard, and tablet inputs, showing that paper and whiteboard sketches cause a 7.10% drop in image similarity and 14–28% decline in character similarity. This granular analysis helps the community target specific robustness challenges.

- **Useful correlation analysis linking automatic and subjective metrics.** The reported Pearson correlations (alignment vs. image similarity: 0.759, vs. code similarity: 0.365, vs. character similarity: 0.592) provide concrete evidence motivating the use of image-level objectives — a finding that generalizes beyond this task.

## Weaknesses

### Fatal
None.

### Major

1. **Potential training–test overlap is not addressed, threatening all reported numbers.**  
   The test set is derived from DaTikZ (Belouadi et al., 2023) — itself sourced from arXiv figures (Section 3.2). The training data includes RenderTikZ, also collected from arXiv source files, plus "existing pairs of TikZ code and images" (Table 1, No. 8). The paper presents **no verification** that test-set TikZ codes or rendered images are absent from any training corpus. Given that both DaTikZ and RenderTikZ share an arXiv provenance, contamination is plausible. If even a fraction of test codes appear in training, all test-set metrics (CSR, ImageSim, Alignment, Quality) are inflated. This is a standard deduplication check (and a cheap one to run) that the authors must provide.

2. **The headline comparison conflates data exposure, training, and inference — the claim of "comparable to GPT-4o" lacks proper disentanglement.**  
   ImgTikZ is fine-tuned on a large corpus of TikZ code and uses multi-candidate generation (K=20) with a learned D-SigLIP selector. GPT-4o, Claude 3.5, and LLaVA-Next are evaluated **zero-shot** with only simple iterative generation (max 5 attempts, no selection). This means the comparison attributes the gap to "the model" when it actually reflects a combination of (a) TikZ-domain fine-tuning, (b) data augmentation, and (c) the inference strategy. The paper's central claim would be better framed as "a specialized small-VLM system can match larger general models" rather than an architecture-level comparison. The ablation studies help partially, but the headline framing remains imprecise.

### Minor

3. **D-SigLIP is used both as the candidate selector and as the evaluation metric for ImageSim.**  
   The selection criterion (maximize similarity between sketch and generated image via D-SigLIP) and one of the main automatic metrics (ImageSim, also via D-SigLIP) are not independent. This mechanically inflates ImageSim for ImgTikZ-MCG compared to baselines that do not use selection. The human evaluation (Alignment) is independent and partially mitigates this concern, but the ImageSim numbers should be interpreted with this in mind, and the paper should acknowledge this circularity explicitly.

4. **No uncertainty quantification for any reported result.**  
   All automatic metrics (CSR avg, ImageSim, CodeSim, CharSim) and subjective scores (Alignment, Quality) are reported as point estimates without confidence intervals, standard deviations, or bootstrap ranges. The test set is only 323 samples, so variance could be meaningful. Without this information, it is unclear whether observed differences (e.g., ImgTikZ-MCG Alignment 3.24 vs. GPT-4o 3.04) are statistically meaningful. This is especially important for CSR avg, which could vary across generation seeds.

5. **AugTikZ quality is not analyzed.**  
   556K TikZ codes were generated by GPT-3.5, but the paper does not report what fraction compile successfully or produce semantically/visually valid diagrams. Low-quality synthetic data could add noise rather than signal. While the ablation (Table 4) shows removing AugTikZ (along with ImgAugTikZ) hurts performance, a standalone analysis of AugTikZ quality would strengthen the contribution.

6. **Individual contribution of AugTikZ is not independently ablated.**  
   Table 4 compares (a) removing ImgAugTikZ and (b) removing *both* ImgAugTikZ and AugTikZ. The individual effect of AugTikZ alone (without also removing ImgAugTikZ) cannot be determined from these ablations. The effect can be inferred by comparing (a) and (b), but a direct "w/o AugTikZ only" ablation would be cleaner.

### Trivial

- Table 5 caption is fragmented in the text (line 186), likely a PDF extraction artifact; the original submission presumably has a clean table.
- Line 97: "Iterative genetaion" has a clear typo ("genetaion").

## Nice-to-Haves

- Test whether multi-candidate generation (K=20 with D-SigLIP selection) also improves GPT-4o/Claude 3.5 performance. This would dramatically strengthen the claim about the specialized model by isolating the effect of training from the effect of inference strategy.
- Report results over multiple random seeds for CSR avg to estimate variance.
- Provide representative failure-mode examples (e.g., text rendering errors, overlapping elements) common to all models, helping readers understand task difficulty.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Unfair comparison setup invalidates the headline claim."* — While the comparison conflates factors, the paper is making a system-level claim (specialized small system vs. large general models). This is a valid practical comparison; the criticism overstates the severity. The point is retained in weakened form as Major Weakness #2 above.

- *"The use of iterative generation for baselines vs. multi-candidate for ImgTikZ is unfair."* — ImgTikZ-IG (iterative generation, same inference as baselines) is also presented and still outperforms baselines on most metrics. So the comparison is not purely driven by inference strategy. The criticism is partially addressed by the paper's own design.

- *"Rouge-1 for character similarity is coarse."* — Rouge-1 is a standard metric for text overlap. Calling it "coarse" is a subjective methodological preference, not a genuine weakness.

- *"Subjective evaluation details are non-standard."* — Using 5 annotators per sample with median-of-3 averaging and Krippendorff's α = 0.761 (alignment) is standard and well-documented practice for crowdsourced evaluation.

## Novel Insights

The most interesting observation emerging from these reviews is the general tension this paper surfaces: the goal of training a *code-specialized* VLM is undermined by the fact that code-level loss correlates poorly with visual output quality (r=0.365 with human alignment). The paper's multi-candidate inference addresses this at test time, but the fact remains that the training objective and the evaluation goal are misaligned. This suggests a broader lesson for image-to-code tasks: it may be more productive to train with a visual discriminator (or reinforcement learning from visual feedback) than to rely solely on next-token prediction of code. The paper's D-SigLIP selector is a step in this direction, but only at inference time.

## Suggestions

1. **Run and report a deduplication check** between test-set TikZ codes/images and all training datasets (RenderTikZ, AugTikZ, No. 8, DaTikZ source). Report exact overlap numbers or confirm zero overlap.

2. **Rephrase the headline claim.** Instead of "comparable to GPT-4o," say "a specialized 6.7B VLM system — combining TikZ-domain fine-tuning, data augmentation, and multi-candidate selection — achieves results competitive with larger zero-shot models such as GPT-4o and Claude 3.5 Sonnet."

3. **Add an experiment showing multi-candidate selection applied to a baseline** (e.g., GPT-4o with K=20 and D-SigLIP selection). Even one setting would help isolate what the fine-tuning contributes vs. what the inference strategy contributes.

4. **Report confidence intervals** (e.g., bootstrapped 95% CI) for all automatic metrics and at least standard deviation for subjective scores.

5. **Add an ablation for AugTikZ alone** (w/o ImgAugTikZ) to parallel the w/o-ImgAugTikZ-only condition already reported.

6. **Analyze AugTikZ quality**: report compilation rate and sample visual validity for the 556K GPT-3.5 generated codes.

7. **Acknowledge the D-SigLIP circularity** (selector = evaluator) explicitly in the paper and note that human evaluation provides the independent signal.

## Score and Decision

The paper has genuine and useful contributions: a much-needed dataset (SketikZ), practical augmentation strategies, and a novel inference-time selection method. The core weaknesses — potential data contamination and conflation of multiple factors in the headline comparison — are serious but addressable through verification and more precise framing. The dataset alone is a valuable contribution to the community, and the methodological insights (augmentations, D-SigLIP selector) are solid. I recommend acceptance contingent on the authors addressing the deduplication check and better scoping their claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>