Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes Add-it, a training-free method for inserting objects into images using pretrained diffusion models (FLUX). The core technical contributions are: (1) a weighted extended-attention mechanism that balances information from the source image, the target image, and the text prompt in MMDiT blocks; (2) a structure transfer step that aligns the target image's global structure with the source; and (3) a subject-guided latent blending mechanism that preserves fine background details. Additionally, the paper introduces the "Additing Affordance Benchmark" — a new evaluation protocol with manually annotated bounding boxes to measure object placement plausibility. Results show strong performance across automatic metrics, human evaluations (preferred in ~80% of head-to-head comparisons), and a large affordance gap (0.828 vs. next best 0.474) on the proposed benchmark.

## Strengths

- **State-of-the-art training-free object insertion.** Add-it consistently outperforms or matches both training-free (Prompt-to-Prompt, SDEdit) and supervised (InstructPix2Pix, MagicBrush, EraseDraw) baselines across multiple benchmarks (Tables 1, 2). Human preference studies show it is favored in ~80% of comparisons on real images (EmuEdit) and ~83–90% on generated images, providing strong evidence beyond automatic metrics.

- **Principled analysis and control of attention dynamics.** The paper identifies a concrete phenomenon — that naively extending attention to include source tokens causes the source to dominate, suppressing prompt-driven changes — and introduces a root-solver-based mechanism to balance attention across source, target, and text (Figure 5). The ablation on γ (Figure 5A) cleanly demonstrates the trade-off between inclusion and affordance, and the "Auto" setting empirically finds a sweet spot.

- **Novel affordance benchmark addressing an evaluation gap.** The paper constructs the first dedicated benchmark for object placement plausibility with manually annotated insertion regions. While the metric itself merits further validation (see weaknesses), the benchmark directly targets a shortcoming of existing CLIP-based protocols and represents a useful resource for the community.

- **Comprehensive ablation analysis.** Figures 5–7 isolate the contribution of each component (weight scale, structure transfer timing, latent blending) with clear visual evidence. The analysis of how structure transfer at different timesteps (Figure 6) and blending (Figure 7) affect the final output provides solid internal validation for the design choices.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The affordance metric needs stronger validation.** The paper reports Add-it at 0.828 vs. the best baseline at 0.474 — a dramatic gap. The protocol relies on Grounding-DINO detection within a finite set of manually annotated bounding boxes. Several unaddressed concerns weaken the metric's credibility: (a) a finite box set may penalize correct placements outside annotated regions; (b) Grounding-DINO may systematically miss objects added by certain methods due to appearance artifacts; (c) no inter-annotator agreement is reported for the bounding-box annotations; (d) no correlation with human judgments of placement plausibility is shown. While the human preference results (~80% favorability) indirectly support that Add-it places objects better, the paper's headline affordance claim (47% → 83%) rests on a metric whose validity is not fully established. The authors should report human ratings on the same images and/or show per-image failure analysis for the metric.

- **Baseline reimplementations on FLUX are insufficiently documented.** Prompt-to-Prompt and SDEdit are re-implemented on FLUX.1-dev for fair comparison, but these methods were designed for SD's cross-attention architecture, not FLUX's MMDiT blocks. The paper provides no details on how attention maps are injected in multi-stream vs. single-stream blocks, and no validation that the reimplementations match the quality of the originals on their intended models. If the reimplementations are suboptimal, comparisons on the Additing Benchmark and Affordance Benchmark are artificially favorable to Add-it. The authors should at minimum provide implementation details or side-by-side comparisons on a common setup.

- **User study details are underspecified.** The paper reports that Add-it was "preferred in ~80% of cases" but does not specify the number of raters, number of pairwise comparisons per condition, the rating interface, or any measure of inter-rater agreement or confidence intervals. These details are necessary to assess the reliability of the human evaluation.

- **Missing implementation details in main text.** The root-solver algorithm (type, tolerance, per-head or per-block, recomputation per timestep), Grounding-DINO confidence threshold for the Inclusion metric, and the blending timestep T_blend are not specified in the main text and are deferred to the appendix (which was stripped from the reviewed version). These should be stated in the main paper or made easily accessible.

- **Ablations are qualitative rather than quantitative across the full benchmark.** The structure transfer and latent blending ablations (Figures 6, 7) are illustrated with single examples. Reporting quantitative impact (inclusion, affordance, CLIP scores) on the full benchmark with/without each component would strengthen the contribution claims.

- **No comparison against dedicated object-insertion methods.** The baselines are predominantly instruction-based editors (InstructPix2Pix, MagicBrush, EraseDraw) and general editing methods (P2P, SDEdit). Methods specifically designed for object insertion (e.g., AnyDoor, DreamEdit, Paint-by-Example, or inpainting-based approaches) are not included. While the existing baseline set is reasonable, including at least one dedicated method would better contextualize the contribution.

- **Error bars are absent from all metric tables.** Tables report point estimates without confidence intervals or standard deviations. Given benchmark sizes of 100–200 images, variance matters and should be reported.

### Trivial

- The paper states "ensures perfect reconstruction of the source image, since σ₀ = 0" for the real-image pipeline (Section 3.5). This is technically accurate but the source image is being used as a reference in the attention mechanism, not being "reconstructed" as an output — the phrasing could be clarified.

## Nice-to-Haves

- A controlled experiment comparing the random-noise pipeline against a proper inversion on a small set of generated images (where the true noise is known) to quantify the quality gap between synthetic and real-image performance.
- Provide the code for the affordance benchmark evaluation protocol to facilitate adoption and verification by the community.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **The critic's claim that the real-image pipeline makes EmuEdit comparison "questionable" and "the evidence may not support" SOTA on real images.** Removed because: (1) Table 2 shows Add-it achieves the highest CLIP_dir (0.101) and Inclusion (81%) on EmuEdit despite using a simpler inversion — the empirical evidence supports the claim; (2) the asymmetry (simpler inversion vs. baselines' trained pipelines) favors the baselines, not Add-it, so this is not a valid criticism of unfair comparison. The paper's own acknowledgment of this as a limitation is retained in Minor.
- **The critic's claim about CLIP_im for Erasedraw being an unaddressed issue.** Removed because the paper explicitly addresses this: "This result is not surprising given that in 35% of the cases Erasedraw did not add an object to the image (indicated by the Inclusion metric), artificially boosting the image similarity score."
- **The critic's framing that the T_blend and mask extraction details being "impossible to judge" because they're in the appendix.** Removed because the appendix is present in the original submission — the parser stripped it. The authors do reference implementation details.
- **Strength Finder strength #5 framed as "Robust handling of real images without complex inversion."** Tempered: the approach is simple and works empirically but is acknowledged by the paper as less effective than on generated images. Retained in Strengths with more measured language.
- **Generic "important problem" framing from Strength Finder.** The strengths listed are all specific and evidence-backed; no generic strengths need removal.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is the tension between the dramatic affordance gap (0.828 vs. 0.474) and the relatively modest gaps on CLIP-based metrics. This suggests that existing CLIP-based evaluation protocols for insertion tasks are indeed insufficient to capture placement plausibility, and that the affordance benchmark, despite its validation concerns, is addressing a real and previously unmeasured dimension. The attention-distribution analysis (Figure 5B) also provides a rare quantitative look into how MMDiT blocks balance multi-source information — a level of detail that is still uncommon in the FLUX/SD3 literature and could inform future training-free editing methods.

## Suggestions

1. **Validate the affordance metric** by running a human study on the same benchmark images asking raters to judge placement plausibility, and report the correlation between the automatic score and human judgments. Also report inter-annotator agreement for the bounding-box annotations.
2. **Document the baseline reimplementations** — provide the specific strategy for injecting attention maps in FLUX's dual-block architecture (multi-stream vs. single-stream), and ideally show a comparison confirming the reimplementations produce comparable quality to the originals.
3. **Report user study details** (number of raters, comparisons, confidence intervals or error bars) and add error bars or standard deviations to all metric tables.
4. **Add quantitative ablations** on the full benchmark for each component (structure transfer, blending, weighting) rather than single examples.

## Score and Decision

The paper makes a genuine contribution: a training-free method that achieves strong results on a practically important task, supported by a careful analysis of attention dynamics and a new evaluation benchmark targeting a real gap in existing protocols. The weaknesses are all addressable and none threaten the core claim (the method works well and outperforms baselines). The human preference data, the attention analysis, and the consistent improvement across multiple metrics provide convergent evidence.

**Score: 8.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>