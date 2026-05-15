I've thoroughly read and verified the paper. Let me now produce the final consolidated review.

---

## Summary

This paper introduces GS-VTON, an image-prompted 3D virtual try-on method built on 3D Gaussian Splatting. The key idea is to extend 2D VTON (IDM-VTON) to 3D by: (1) a reference-driven image editing approach that generates consistent multi-view edited images by sharing key/value attention features across views, (2) LoRA fine-tuning on these edited images to personalize the diffusion model, and (3) a "persona-aware" 3DGS editing step that blends self-attention features from the editing direction with those from the edited training set to maintain cross-view consistency. The paper also introduces 3D-VTONBench, a 60-subject benchmark for the task. Results are evaluated via a user study (25 participants, 625 responses) and qualitative comparisons against five text-prompted 3D editing methods and an internal baseline.

---

## Strengths

- **Addresses a genuine, underexplored problem.** The paper correctly identifies that naively applying 2D VTON models per-view in a 3D scene produces multi-view inconsistencies, and proposes targeted mechanisms (reference attention sharing, persona-aware attention blending) to enforce cross-view consistency. This problem framing is sound and well-motivated (Fig. 4, lines 42–45, 172).

- **Reference-driven image editing for consistent multi-view generation.** The approach of sharing key/value attention features from a reference view during simultaneous IDM-VTON denoising of multiple views (Eq. 5, lines 177–185) is a reasonable adaptation of temporal attention from video diffusion. The ablation (Fig. 9, lines 261–265) shows this component tangibly improves texture consistency with the garment.

- **Persona-aware 3DGS editing addresses a real remaining gap.** Even after LoRA fine-tuning, views far from the training set can be inconsistent. The attention blending (Eq. 6, lines 192–194) that mixes the current editing direction's attention with averaged attention from the edited multi-view set is a sensible solution. The ablation (Fig. 7, lines 256–257) confirms its necessity.

- **Efficiency is a practical strength.** The total pipeline takes ~30 min (LoRA) + ~25 min (editing) on a single V100 GPU (line 211), which is notably faster than NeRF-based alternatives. All hyperparameters are fixed across experiments, demonstrating practical robustness without per-scene tuning.

- **No resolution limitation.** Unlike methods constrained by Instruct-Pix2Pix (512×512), GS-VTON edits at the original scene resolution (line 209).

---

## Weaknesses

### Fatal
None. The paper's core claims—that GS-VTON produces multi-view consistent 3D VTON results—are supported by ablations and a user study. No error invalidates the central thesis.

### Major

- **No automatic metrics on the proposed benchmark.** The paper introduces 3D-VTONBench (60 subjects, lines 221) but reports **zero** repeatable automatic metrics (PSNR, SSIM, LPIPS, FID, CLIP score, or inter-view consistency metrics). The only quantitative evidence is a user study. This is a significant gap: (a) future work cannot compare against the reported results, (b) the user study is not reproducible, and (c) the benchmark's primary purpose—enabling quantitative evaluation—is left unfulfilled in this paper. While user studies are valid for subjective quality, automatic metrics are standard for a claim of "state-of-the-art."

- **Comparison set is predominantly text-prompted methods.** Five of six comparisons (GaussianEditor, IG2G, GaussCTRL, IN2N, Vica-NeRF) accept only text prompts. These methods operate at a fundamental disadvantage for image-detail tasks. While the paper acknowledges this ("Since these methods only accept text prompts as input," line 224), it weakens the "state-of-the-art" claim. The one directly comparable method (GaussianVTON) is excluded due to unavailable code (line 224)—understandable, but the evaluation would be substantially strengthened by at least discussing its reported results or attempting a re-implementation. The internal baseline (IDM-VTON per-view + LoRA + 3DGS) does partially address this concern, as it is an image-prompted approach.

- **ControlNet conditioning signal is underspecified.** The paper states the model is "adapted via a ControlNet-based stable diffusion inpainting model to condition the inpainting process on the input garment image" (line 194) and writes $\mathcal{C}(I_{\text{cloth}})$ (Eq. 10). However, ControlNet requires a specific conditioning modality (canny edge, depth map, pose skeleton, etc.). What signal is used to encode the garment image for ControlNet? How is the garment image preprocessed for this conditioning? This is a core implementation detail that is missing, making the 3DGS editing step's key mechanism opaque and the method difficult to reproduce.

### Minor

- **User study design has limitations.** The study asks participants only to select the "best" among five videos (winner-takes-all, line 229), rather than rating each method independently on a Likert scale. No inter-rater reliability metric (e.g., Fleiss' kappa) is reported, and no significance test is performed. Additionally, only 25 of the 60 benchmark subjects are evaluated, with no explanation of the selection criteria. These issues reduce but do not invalidate the evidence.

- **Missing sensitivity analysis for key hyperparameters.** The reference-driven editing fixes $n=4$ images and always uses the first image as reference (line 175, 180). The attention blending weight is fixed at $\lambda=0.55$ (line 194). No ablation or sensitivity study is provided for either. The paper mentions an appendix for the number of views (line 188), which the parser likely stripped, but the main paper does not address this.

- **2D-to-3D mask projection is not described.** The paper replaces GaussianEditor's LLM-based mask generation with human parsing (line 206), but does not explain how the 2D human parsing mask is projected to 3D Gaussians to identify which Gaussians correspond to the garment. This is a non-trivial step for a method built on 3DGS.

- **No runtime comparison.** The paper reports its own runtime (30+25 min, line 211) but does not compare against the runtime of any baseline method, making it hard to contextualize the efficiency claim.

### Trivial

- The LoRA circularity concern raised by one reviewer reflects a misunderstanding: LoRA fine-tuning on the already-edited images is standard personalization (akin to DreamBooth), not circular. The LoRA adapts the model to the specific garment-person appearance for use during 3DGS editing. The paper could clarify this motivation briefly.

---

## Nice-to-Haves

- Reporting automatic metrics on 3D-VTONBench (e.g., CLIP image similarity between rendered views and the garment image, inter-view LPIPS for consistency, FID).
- Adding a comparison with a naive per-view IDM-VTON → 3DGS reconstruction baseline (without LoRA), to isolate the value of the full pipeline vs. a simpler 3D reconstruction from 2D VTON outputs.
- Sensitivity analysis for $\lambda$ and $n$ across a few values, reported via a simple consistency metric.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No baseline that uses IDM-VTON independently on each view"** — Factually incorrect. The paper's baseline (Sec. 4.2, lines 236–238) does exactly this: "generating edited training image set $X_{\text{train}}$ individually via IDM-VTON." This criticism is removed.

- **"LoRA circularity"** — The reviewer claims training LoRA on images already edited by IDM-VTON is circular. This misunderstands the purpose: LoRA personalization (fine-tuning on the specific case) is standard practice (e.g., DreamBooth, RealFill). The LoRA adapts the model for consistent generation during 3DGS editing. Removed as a strawman.

- **Several formatting/reproducibility nitpicks** about undisclosed hyperparameters or missing trivial implementation details — removed per hard rules.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation gap (no automatic metrics, limited baselines) but do not propose fundamentally new technical insights about the method itself.

---

## Suggestions

1. **Report automatic metrics on 3D-VTONBench.** At minimum, report CLIP image-image similarity between rendered views and the garment image, and inter-view LPIPS (measuring consistency across neighboring views). This would significantly strengthen the quantitative evidence and make the benchmark useful for future work.

2. **Specify the ControlNet conditioning modality.** Clarify what control signal (image itself, depth, edge, or other) is used for the garment image in $\mathcal{C}(I_{\text{cloth}})$ and how it is preprocessed. This is critical for reproducibility.

3. **Describe how the 2D human parsing mask is projected to 3D Gaussians.** The paper says it generates a 2D image mask and uses it for local editing (line 206) but doesn't explain the 3D Gaussian labeling process.

4. **Add sensitivity analysis for $\lambda$ and $n$.** Even 2–3 values with a simple visual comparison would help establish robustness.

5. **Refine the user study.** Ask participants to rate each method independently (e.g., 1–5 Likert) rather than winner-takes-all, and report inter-rater agreement.

---

**Overall assessment:** The paper tackles a well-motivated problem with a sensible pipeline combining established techniques in a novel way. The method is efficient, resolution-flexible, and the ablations confirm that both proposed components (reference-driven editing, persona-aware attention blending) contribute meaningfully. The introduction of 3D-VTONBench is a positive contribution. However, the evaluation is notably incomplete: the benchmark is introduced but no automatic metrics are reported, and the comparison set skews toward text-prompted methods at an inherent disadvantage. The ControlNet conditioning detail is underspecified. These are substantial but not fatal. The paper would benefit from additional experiments but the core technical contribution is sound.

**Score and Decision:** 5.5/10 → Borderline. The paper has clear merit but the evaluation gaps prevent a strong accept. I lean toward **weak reject** at a top venue with encouragement to resubmit after adding automatic metrics and a stronger baseline comparison, or **weak accept** at a mid-tier venue if the authors can address the major concerns in a rebuttal.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>