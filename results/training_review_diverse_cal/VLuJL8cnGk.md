Here is the consolidated meta-review:

---

## Summary

This paper proposes a method for single-image novel view synthesis (NVS) that combines a pretrained 3D-based NVS model (Zero123++) for weak viewpoint guidance with a 3D-free inference-time optimization pipeline (HawkI-style). A viewpoint regularization loss aligns the optimized text embedding with an angle-embedding derived from the target azimuth/elevation. The method requires no 3D training data and aims to handle complex, in-the-wild scenes with backgrounds — an area where object-centric 3D-based methods struggle.

## Strengths

1. **Effective integration of 3D priors into a 3D-free pipeline.** The method uses Zero123++ only to produce a weak guidance image, then feeds this into a 3D-free inference-time optimization. This hybrid design is clearly motivated and well-described (Section 4, Figure 1). It allows camera control on complex scenes without 3D training data — a genuinely useful combination.

2. **Viewpoint regularization loss with clear ablation support.** The regularization term \(L_{\text{reg}} = \| e_{\text{view}} - e_{\text{target}} \|^2\) explicitly injects angular information into the CLIP embedding space. The ablation study (Table 2, Figure 5) shows consistent improvements across all seven metrics and all viewpoints when this loss is added — e.g., LPIPS on HawkI-Syn \((30^\circ, 30^\circ)\) improves from 0.5867 to 0.5661, CLIP score from 28.54 to 29.96. This is the paper's most concrete technical contribution.

3. **Consistent CLIP-score and DINO improvements over strong baselines.** On both HawkI-Syn and HawkI-Real across four viewpoints (Table 1), the proposed method achieves the highest CLIP score (text-to-image alignment including viewpoint) and the highest or tied-highest DINO score on every entry. For example, on HawkI-Real \((30^\circ, 270^\circ)\): CLIP 30.55 vs. next-best 29.05; DINO 0.4126 vs. next-best 0.3530. These text-based metrics directly measure viewpoint accuracy and are not subject to the evaluation-reference ambiguity that affects the pixel-level metrics.

4. **Diagnostic analysis motivating the design.** Section 3 provides two controlled experiments showing (a) removing the guidance image causes CLIP to produce inconsistent viewpoints even with angle text, and (b) using an incorrect guidance image causes the model to follow the guidance regardless of text. These observations ground the design choice of using an accurate 3D-based prior alongside text-based regularization.

5. **Qualitative generalization to complex scenes.** Results on HawkI-Real (Figures 3, 4) show the method preserving background details (Seine River in the Eiffel Tower scene, rock textures in waterfall) where baselines like Zero123++ focus on the main object. This supports the claim that the hybrid approach benefits from both scene-complexity handling (3D-free) and camera control (3D-based).

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguous/misleading evaluation reference for LPIPS, PSNR, and SSIM.** The paper defines LPIPS as measuring similarity "between the generated and input images" (Section 5.2) — i.e., against the *source* image, not a ground-truth target view. For novel-view synthesis, a method that genuinely changes the viewpoint will naturally have large pixel- and perceptual-level differences from the source. So lower LPIPS (claimed "better") could actually indicate less viewpoint change, and higher PSNR/SSIM could as well. The same issue affects CLIP-I (also explicitly against the "input image") and potentially PSNR/SSIM (computed against "reference images," which is never defined). **This means LPIPS, PSNR, SSIM, and CLIP-I as presented are not measuring NVS quality in the standard sense.** The CLIP Score and DINO metrics remain valid because they measure text alignment and semantic consistency rather than pixel-level similarity to the source. However, the paper's quantitative claims that rely on LPIPS (including the headline number in the abstract) are significantly weakened. The authors should either (a) compute these metrics against ground-truth target views for HawkI-Syn (which, as a synthetic dataset, has them), or (b) clearly define and frame these metrics as measuring *content preservation* rather than NVS quality, and acknowledge that they cannot distinguish correct viewpoint changes from incorrect ones.

2. **Numerical error in the abstract.** The abstract claims: "our model outperforms the lowest-performing model by **0.1712 in LPIPS** (HawkI-Syn $(-20^\circ, 210^\circ)$ in Table~2)." For that table entry, the LPIPS values are 0.5740 (with regularization) vs. 0.5860 (without) — a difference of **0.012**, not 0.1712. The relevant LaTeX label (`table-evaluation2`) does not exist in the paper (the labels are `table-evaluation1` and `table-evaluation-ablation`). This is a factual error that must be corrected.

### Minor

3. **Computational cost not quantified.** The method runs 1000 + 500 + 500 + 250 = 2250 iterations of diffusion-model optimization per scene/viewpoint. The paper calls this "rapid" (Section 4) but provides no wall-clock time. Baselines (Zero123++, Stable Zero123) are feed-forward and run in seconds. While the paper acknowledges this limitation in the Conclusion, the "rapid" claim is unsubstantiated, and the computational asymmetry should be explicitly discussed in the comparison.

4. **No error bars or confidence intervals.** Only 10% of each dataset is used (line 180), and results are reported as point estimates without standard deviations. Many of the gaps between methods are small (e.g., LPIPS 0.5661 vs. 0.5694), making significance unclear. This is particularly problematic given the evaluation-reference ambiguity, as small absolute differences could be noise.

5. **The analysis in Section 3 is informal.** The claim that "CLIP struggles with 3D comprehension" is supported by a single qualitative experiment (Figure 1) showing inconsistent views when the guidance image is removed. This does not isolate CLIP's role from other components (e.g., the diffusion prior). Similarly, the incorrect-guidance experiment (Figure 2) shows the model follows the guidance image, which is expected behavior. These analyses motivate the method adequately but are anecdotal rather than rigorous.

### Trivial

- The abstract references `\ref{table-evaluation2}` which is not a defined label in the paper (only `table-evaluation1` and `table-evaluation-ablation` exist). All such references need to be corrected.
- The paper states "3D-based methods such as HawkI enable precise camera control" (line 28) but HawkI is a 3D-free method, not a 3D-based method — this appears to be a wording error (Zero123++ is the 3D-based method used).

## Nice-to-Haves

- **Ablation on guidance model choice.** The paper uses only Zero123++ for guidance. Testing alternatives (e.g., a different 3D NVS model, or a non-3D augmentation-based guidance image) would strengthen the claim that the specific choice matters.
- **View-consistency metrics across generated viewpoints.** For real data without ground truth, evaluating consistency across generated views of the same scene (e.g., via Free3D-style consistency metrics or LPIPS between different generated views) would provide additional evidence.
- **User study for real-world images.** A perceptual study on HawkI-Real could compensate for the lack of ground-truth target views.

## Removed Points

- *"The novelty is modest"* (Harsh Critic): This is a judgment about incremental contribution, not a verified weakness. Many papers combine existing components, and the paper's regularization loss and analysis are concrete contributions. Removed as subjective and not a verified flaw.
- *"The quantitative evaluation is fundamentally flawed / all metrics are computed against the input"* — downgraded from the critic's "fatal" framing to Major. The CLIP Score and DINO metrics are not subject to this issue and show consistent improvements. The evaluation reference ambiguity primarily affects LPIPS, PSNR, SSIM, and CLIP-I — not the full set of metrics. Additionally, all baselines are compared under the same protocol, so relative ordering for content preservation is still meaningful.
- *"Results may be noisy with only 10% of data"* — moved to Minor. This is standard practice in some NVS papers and doesn't invalidate the results; error bars would improve confidence but are not a fatal omission.
- *"Strength Finder's generic strengths"* — filtered out generic phrasing. The five strengths listed above are the non-generic, evidence-backed ones from the Strength Finder.

## Novel Insights

The most interesting observation across the reviews is that the evaluation-reference ambiguity exposes a deeper tension in how NVS evaluation is conducted when ground-truth target views are unavailable. The paper's LPIPS-against-source metric — while problematic for measuring viewpoint accuracy — does capture *content preservation*, which is a real desideratum for NVS (you want to change the viewpoint without losing the identity of the scene). The CLIP score separately captures viewpoint accuracy. The paper conflates these two dimensions under a single umbrella of "NVS quality," but the reviewer correctly identified that they are distinct. A clearer conceptual separation in the paper — "content preservation" metrics vs. "viewpoint accuracy" metrics — would resolve most of the confusion.

## Suggestions

1. **Re-compute LPIPS, PSNR, and SSIM against ground-truth target views for HawkI-Syn**, where ground truth is available. For HawkI-Real, either explicitly frame these metrics as measuring content preservation (not viewpoint accuracy), or replace them with view-consistency metrics across generated outputs.

2. **Fix the 0.1712 number in the abstract** to match the actual table values, and fix all LaTeX label references that point to non-existent labels.

3. **Report wall-clock time** for the full inference pipeline to substantiate (or qualify) the "rapid" claim, and explicitly acknowledge the computational asymmetry with feed-forward baselines.

4. **Add standard deviations or confidence intervals** to the quantitative tables, especially for entries where the gap between methods is small.

5. **Clarify the reference image used for each metric** in a single, unambiguous sentence in the evaluation section. Currently the paper mixes "input images," "reference images," "reference counterparts," and "ground-truth structures" without defining which is which.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>