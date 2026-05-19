- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 3, 3, 5
Now I have a thorough understanding of the paper content. Let me construct the consolidated review.

## Summary

The paper proposes ETC (Exploiting Temporal Capabilities of Spatial Attention), a text-to-video framework that removes all additional temporal attention layers and instead relies solely on the spatial attention of a pre-trained text-to-image diffusion model. Videos are processed by stitching frames into a spatial grid, and the model uses a novel Spatial-Temporal Mixed Embedding (ME) to distinguish intra-frame and inter-frame features along with a Triple-Data Driven Training (TDT) strategy. The central claim is that this design achieves competitive or better video quality while requiring only ~1% of the training data used by prior SOTA methods.

## Strengths

1. **Novel and well-motivated architectural simplification.** The idea of removing temporal attention layers entirely and relying on spatial attention for both spatial and temporal modeling is a clean departure from the dominant paradigm of adding temporal modules. The experimental observation (Figure 2) showing that a spatial-only model (W/O-TA) converges faster and produces recognizable videos after only 500 finetune steps, while the model with newly-initialized temporal layers (W-TA) remains blurry, provides genuine empirical support for the thesis.

2. **Spatial-Temporal Mixed Embedding (ME) is effective and documented.** The ablation in Table 2 shows that ME reduces the frame-boundary segmentation error rate from ~17% to 0%, and improves FVD on MSR-VTT. The design is clearly specified (Equation 2–3), and the generalization experiments (Figure 6) demonstrate that after only 1K finetune steps, the model can produce high-resolution (512×320) and long (256-frame) videos, indicating ME's scalability.

3. **Triple-Data Driven Training (TDT) is a practical contribution.** The ablation (Table 2) confirms that incorporating label-image and caption-image data alongside video data improves both FVD (9.0→8.4) and CLIP score (0.282→0.290). This is a concrete strategy for reducing dependence on expensive text-video paired data, which is a genuine practical concern.

4. **Competitive zero-shot results across multiple benchmarks.** On MSR-VTT and UCF-101, ETC (0.9B parameters) achieves competitive FVD scores relative to four strong baselines despite using substantially less training data. The inference speed of 1.92 FPS (~3× faster than LVDM) is a tangible efficiency advantage.

## Weaknesses

### Fatal
None.

### Major
1. **The theoretical justification in the main text is oversimplified to the point of being misleading.** The paper claims that spatial attention and the combination of spatial+temporal attention both produce "linear mappings" (Section 3, lines 68–69: "remains a linear combination of the input data"), and therefore one can substitute for the other. This characterization ignores the softmax nonlinearity inherent in self-attention, which is not a linear operation. The equations presented (χ_s and χ_st) are simplified forms that do not actually represent how attention computes outputs. While the full proof is deferred to Appendix B.2 (which was stripped during parsing), the main text's framing of attention as "linear" is inaccurate and undermines confidence in the theoretical component of the paper. The experimental observation (Figure 2) stands on its own as empirical motivation, but the paper should either present a rigorous theoretical treatment or drop the claim of a formal proof.

2. **The central data-efficiency claim lacks a controlled comparison.** The paper contrasts ETC (trained on a filtered subset of ~100K WebVid videos + ImageNet + JDB images) against baselines (LVDM, VideoCrafter, VideoCrafter2, ModelScope) trained on full video datasets with millions of samples and temporal modules trained from scratch. This comparison confounds two variables: (a) the spatial-only architectural design and (b) the training data size and filtering. To rigorously demonstrate that the spatial-only design is the cause of the data savings, a controlled experiment where a strong baseline (e.g., VideoCrafter2) is retrained on the same 100K filtered dataset would be needed. Without it, the impressive headline numbers (49% FVD improvement, 99% data reduction) may partially reflect dataset filtering, model scale differences, or other factors rather than the removal of temporal layers per se. The dataset-size ablation (Figure 7) is useful but only tests ETC's own sensitivity, not the relative advantage over baselines on small data.

3. **The quantitative results table (Table 1) is presented as an image without numerical values reproducible in text.** The paper reports competitive FVD/CLIP scores and a "49% average FVD improvement" but the reader cannot verify the exact numbers, per-dataset breakdowns, or which baseline the 49% is averaged over. Confidence intervals or error bars are not reported for any metric. Given that the main quantitative claims are central to the paper's contribution, the specific numerical results should be included in accessible text form with measures of variability.

### Minor
1. **The temporal-to-spatial stitching strategy itself is not ablated against alternatives.** The paper ablates ME and TDT (Table 2) but never compares the core stitching-based arrangement against other plausible ways to feed video into a spatial-only model, such as channel concatenation, batch-style processing with grouped attention, or processing frames independently with a post-hoc temporal blend. This makes it unclear whether the stitching strategy specifically is essential to the results.

2. **Several hyperparameters and design choices are unreported.** The parameter Θ in the ME sine/cosine embedding (Equation 2) is not defined. The video filter threshold α (Equation 4, described as "selecting a threshold ratio α") is not specified, making it impossible to reproduce the dataset filtering. The exact composition of the Triple-Data mixture (sampling ratios among caption-image, label-image, and caption-video sources) is not given. These omissions hinder reproducibility.

3. **The user study description contains a minor inconsistency.** The text states both that "ETC and VideoCrafter2 performed similarly, with VideoCrafter2 slightly outperforming ETC" and that "our results are the best among several different models, but similar to videocrafter2" (line 187). If VC2 slightly outperforms ETC, calling ETC "the best" is imprecise. This is a wording issue, not a methodological flaw, but it should be cleaned up.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment where a standard temporal-attention baseline is retrained on the same filtered 100K dataset (and ideally the same image data) would directly isolate the benefit of removing temporal layers from the benefit of data filtering and selection. This is the single most impactful addition.
- Reporting inference memory footprint and total per-video generation time alongside FPS.
- A failure analysis showing examples of the 17% incorrect-segmentation error rate without ME and how ME resolves them.

## Removed Points
The following points from the reviewer inputs were removed with justification:

- **"Theoretical proof is entirely invalid / unsound"** — *Removed as stated.* The criticism about softmax nonlinearity in attention is valid and has been reincorporated as a Major weakness above. However, the claim that the argument is "not derivations from actual attention" is partly based on the appendix (B.2) being absent due to parser stripping. The final review retains a precise version of this concern.
- **"Qualitative results table is garbled OCR"** — Removed. The table is an embedded image, standard in ML papers; garbled text is a parser artifact, not a paper flaw.
- **"Reproducibility: FPS embedding described vaguely ('three linear layers')"** — Removed. Describing a learnable module as "three linear layers" with channel quadrupling and reduction is sufficiently specific for a conference paper.
- **"Missing related works"** — Removed per instructions (cannot confirm existence of external sources).
- **"Baseline equal sampling of 10k videos is ambiguous"** — Removed. This is a standard evaluation practice and the description is clear enough.
- **"Strength about theoretical demonstration"** — Removed from strengths. The theoretical argument as presented in the main text is weak; the paper's genuine strength is the experimental observation, not the theory.
- **"Strength about user study"** — Retained but qualified. The user study shows comparable preference, which is a real supporting result.
- **"Multiple reproducibility nitpicks"** — Merged and narrowed to the specific missing parameters (Θ, α, data mixture ratios) that are genuinely absent from the main text.
- **"Strength about TDT"** — Retained. The ablation does confirm TDT's benefit.
- **"Criticism about Figure 2 not proving spatial attention replaces temporal well at convergence"** — Removed. The figure shows convergence behavior (loss curves) and early generation quality; it is presented as a motivating observation, not a proof of convergence parity. The reviewer overstates what the figure claims.
- **"Criticism that the paper does not control for baselines having seen test distributions"** — Removed. Zero-shot evaluation is standard; baselines' training sets are well-documented and do not include MSR-VTT/UCF-101 by default.

## Novel Insights
None beyond the paper's own contributions. The two reviews align on the core tension: the paper's central idea (spatial-only attention for video) is interesting and the empirical results are promising, but the evidence for the specific data-efficiency claim is weakened by an uncontrolled comparison. This is not a contradiction or an artifact of the reviewing process—it is a faithful characterization of the paper's current evidentiary state.

## Suggestions
1. **Run a controlled small-data baseline.** Retrain a standard T2V model (e.g., VideoCrafter2 without its pretrained temporal module, or LVDM) on the exact same filtered 100K WebVid subset used for ETC, and compare FVD/CLIP. This is the single experiment that would most directly support the paper's central claim about temporal module removal enabling data efficiency.
2. **Provide exact numerical results in the main text (not only as an image table).** Include per-dataset FVD with confidence intervals and specify which baselines/subset the "49% average improvement" is computed over.
3. **Define Θ and report the α threshold** used in the video filter. Specify the sampling proportions among the three data sources in TDT.
4. **Ablate the stitching arrangement** against channel concatenation or independent frame processing with token-level temporal blending.
5. **Re-frame the theoretical argument** as an empirical observation/informal intuition rather than claiming a formal proof, unless the appendix contains a rigorous treatment that addresses the softmax nonlinearity.
