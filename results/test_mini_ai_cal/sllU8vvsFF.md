Now I have thorough calibration data. Let me compile the final review.

## Round 1 Bracketing

**Initial bracket: 3.5–5.5** (between weak anchors ~3.0 and strong 6.0 anchors).

## Round 2 Narrowing

Most comparable anchors found: CDM (4.75), Ouroboros3D (5.00), Fourier123 (3.50), Part321 (4.80). All are in 3D / single-image-to-3D territory.

**Final determination after comparing against these anchors:** LRM has a more significant architectural contribution (first large-scale transformer for direct image-to-3D) than Fourier123 (SDS loss modification) and arguably larger scale than CDM. However, its experimental evaluation is **substantially weaker** than ALL of these anchors — zero quantitative results, only one baseline (qualitative), zero ablations. This places it below CDM (4.75) and Ouroboros3D (5.00), and roughly alongside or slightly above Fourier123 (3.50) because the contribution novelty is higher even though the evaluation deficiency is comparable.

Let me write the review.

---

## Summary

This paper proposes LRM, a transformer-based encoder-decoder architecture that takes a single image of an object and directly regresses a triplane-NeRF representation, trained end-to-end on ~1 million objects from Objaverse and MVImgNet. The model uses a DINO ViT image encoder and a transformer decoder with cross-attention and camera-conditioned adaptive layer norm (adaLN) to project 2D image features onto a 3D triplane. It achieves 5-second inference on a single A100 GPU and shows impressive qualitative reconstruction results across diverse inputs.

## Strengths

- **First large-scale transformer for direct single-image-to-3D reconstruction.** The paper scales model capacity (500M parameters) and training data (~1M objects) far beyond prior work. This is a genuine step forward in the data-driven 3D reconstruction paradigm, analogous to the GPT-style scaling narrative the paper invokes. (Evidence: Abstract, Section 1, lines 30–31.)

- **End-to-end training with simple reconstruction losses, no 3D-specific regularization or per-shape optimization.** The model is trained by minimizing MSE + LPIPS on novel views (Section 3.4, Eq. 1), without score distillation, multi-stage pipelines, or delicate regularizers. This design choice directly enables scalability. (Evidence: Section 3.4, lines 28–29.)

- **Five-second inference on a single A100 GPU.** The paper provides a detailed timing breakdown (1.14s feed-forward, 1.14s point query, 1.91s mesh extraction), making a strong case for practical applicability. (Evidence: Abstract, Section 4.2, line 190.)

- **Use of DINO image features with explicit justification.** The paper explains why DINO's structural/texture features are preferable to CLIP or ResNet for the reconstruction task (Section 3.1, lines 79–81), and retains the full patch-wise feature sequence rather than only the [CLS] token — a design choice supported by the task requirements.

- **Camera modulation via adaLN is a principled architectural choice.** Conditioning the transformer layers on normalized camera parameters (Section 3.2) reduces the optimization complexity of the image-to-triplane mapping and is clearly explained.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative results in the main paper.** The paper mentions acquiring 50 unseen Objaverse shapes and 50 unseen MVImgNet videos "to numerically study the design choices" (lines 168–169), but presents **zero** numerical metrics (no PSNR, SSIM, LPIPS, Chamfer distance, or F-score) anywhere in the main text. Claims of "high-quality reconstruction" and "highly generalizable" are supported exclusively by qualitative visualizations. For a paper presenting itself as a large-scale breakthrough, this is a fundamental evidential gap — the reader cannot judge whether the method is actually better than existing approaches, or whether the examples shown are cherry-picked. The quantitative evaluation that was promised is simply absent from the paper as presented.

- **Minimal and purely qualitative baseline comparison.** Only one concurrent method (One-2-3-45) is compared, and the comparison is entirely qualitative (Figure 3). Several relevant baselines discussed in the related work — PixelNeRF, MCC, GINA-3D — are not evaluated. Without quantitative comparison to at least 2–3 prior methods on a shared test set, the paper cannot convincingly demonstrate superiority over existing approaches.

- **No ablation studies.** The architecture contains several non-trivial design choices: DINO vs. other feature extractors, adaLN camera modulation vs. concatenation, cross-attention mechanism, number of transformer layers, triplane resolution, LPIPS loss weight. None are ablated. This makes it impossible to determine which components actually contribute to performance, a standard expectation for a method paper.

### Minor

- **Fixed camera assumption during inference limits the claimed generality.** The paper acknowledges this in the limitations (lines 215–216), stating that inference uses "a set of fixed camera intrinsics and extrinsics (same as our Objaverse training data)." This means any input image with different field-of-view, distance, or orientation will have mismatched camera parameters, potentially causing distorted reconstructions. The impact is larger than suggested — the model's practical applicability to arbitrary in-the-wild images is constrained. Furthermore, there is no analysis of how sensitive the results are to deviations from the assumed camera.

- **The claim "ours does not depend on a canonical pose of the object" (line 89) requires clarification.** During training, the model does handle varying camera inputs via the camera feature conditioning. However, during inference, a fixed normalized camera is assumed (line 190), meaning the method *does* depend on the canonical camera assumption at test time. While the claim is technically about the model architecture's capability, the practical inference procedure contradicts the spirit of the statement. The paper should clarify this distinction.

- **Resource requirements are high (128 A100 GPUs, 3 days) with no discussion of reproducibility implications.** This is not a flaw in the method itself, but it affects the practical impact and reproducibility for other research groups.

### Trivial
None.

## Nice-to-Haves

1. **Add a quantitative evaluation table in the main text** with standard metrics (PSNR, SSIM, LPIPS for appearance; Chamfer distance, F-score for geometry) on the held-out Objaverse and MVImgNet sets described in lines 168–169.
2. **Compare quantitatively against at least two baselines** (e.g., PixelNeRF, MCC, Zero-1-to-3 → One-2-3-45 pipeline) on the same test images. Explain how multi-view or per-shape-optimization methods are adapted fairly.
3. **Ablate key design choices** — e.g., DINO vs. CLIP vs. ResNet features, with/without adaLN, reducing transformer layers, varying triplane resolution — on a smaller training subset to demonstrate each component's contribution.
4. **Analyze camera parameter sensitivity.** Show how reconstruction quality degrades when the assumed camera FoV or distance is off by 10%, 20%, 50%.

## Removed Points

These points were flagged by reviewers but removed or downgraded after cross-checking against the paper:

- **"Cannot be independently verified" / "not yet released" concerns** — Removed per hard rules. The paper cites Objaverse, MVImgNet, DINO, etc.; these are publicly available. Citations suffice.

- **"The method assumes Lambertian objects and cannot handle view-dependent effects"** — Kept in the paper's own acknowledged limitations (line 215), which is transparent. Moved to Minor as a limitation noted by the authors themselves, but not a flaw in a paper that scopes itself to Lambertian reconstruction.

- **"Missing related works"** — Not included per policy; I cannot verify the existence of works not cited in the paper.

- **"Missing appendix content, proofs, references"** — Removed per hard rules; the parser strips supplementary content which exists in the original submission.

- **"Comparison is limited and favors baselines if anything"** — The paper's single baseline comparison with One-2-3-45 is purely qualitative and uses the same images from One-2-3-45's paper/demo page to avoid cherry-picking. The comparison, if anything, is unfair to the proposed method (using lower-quality input images meant for the competitor). Retained as a weakness but scoped accurately.

- **Pure formatting/style nitpicks about typos, punctuation, line breaks** — Removed per hard rules; these are parser errors, not author errors.

- **Strength Finder strengths about "addressing an important problem" or "targeting an interesting question"** — Removed as generic/superficial. Only concrete, evidence-grounded strengths were retained.

## Novel Insights

None beyond the paper's own contributions. The key tension — a genuinely novel and large-scale architecture that produces impressive qualitative results, paired with an evaluation that lacks any quantitative evidence — is evident from reading the paper itself and is accurately captured in the reviews.

## Suggestions

1. **Add a quantitative results table** (PSNR, SSIM, LPIPS, Chamfer distance, F-score) comparing LRM against at least 2–3 baselines on a held-out subset of Objaverse and/or Google Scanned Objects. This is the single highest-leverage change.
2. **Ablate the three most important design choices on a small-scale experiment:** (a) DINO vs. CLIP image encoder, (b) with vs. without adaLN camera modulation, (c) number of transformer decoder layers.
3. **Clarify the camera assumption story.** Explicitly state in a single place: "During training, the model receives ground-truth camera parameters; during inference, a fixed canonical camera is assumed (position [0,-2,0], FoV based on Objaverse rendering setup)." This resolves the apparent contradiction with the "does not depend on a canonical pose" claim.
4. **Add a camera-sensitivity analysis** showing reconstruction metrics as the assumed camera deviates from ground truth by varying degrees.

## Score and Decision

I have completed two rounds of calibration. Let me report the anchors.

**Round 1 (Bracketing) anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 9Qptgv0Eyw.md (PtychoFormer) | 3.40 | R1 | Different topic (ptychographic phase retrieval); paper had quantitative results but different domain |
| 2H6KhX1kJr.md (FPTT) | 3.00 | R1 | Different topic (world modeling); comparable evaluation rigor |
| NLRo4qhg6t.md (HIWE) | 3.00 | R1 | Different topic (NeRF encoding); paper had quantitative evaluation |
| 2HdZPEQUig.md (Interpreter) | 3.00 | R1 | Different topic (video segmentation); paper had quantitative results |
| TwBY17Hgiy (3D regularizer) | 6.00 | R1 | 3D-aware regularizer with triplanes; **stronger evaluation** (quantitative results, ablations, baselines) |
| 1CIUkpoata (6D pose) | 6.00 | R1 | 6D pose estimation; **stronger evaluation** (quantitative on YCB-V, baselines, ablations) |
| U6hEOZlDf5 (Pose estimation) | 6.00 | R1 | Relative pose; **stronger evaluation** (multiple datasets, ablations, robustness analysis) |
| u1cQYxRI1H (IC-Light) | 10.00 | R1 | Illumination editing; far stronger evaluation; not directly comparable |
| di52zR8xgf (Data-type ID) | 8.00 | R1 | Far stronger evaluation; not directly comparable |

**Round 2 (Narrowing) anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 385gQZuuuR (CDM, single-image 3D) | 4.75 | R2 | **Stronger evaluation** than LRM: has quantitative results on ShapeNet/Co3D, ablation studies, baseline comparisons. LRM has more novel contribution but much weaker evaluation. |
| Nx6Bb5uxfI (E3D, 3D detection) | 4.40 | R2 | Different task; paper truncated but has quantitative results. |
| bjkQTInGes (Ouroboros3D, image-to-3D) | 5.00 | R2 | **Much stronger evaluation** than LRM: PSNR/SSIM/LPIPS on GSO benchmark, multiple baselines (LGM, InstantMesh, VideoMV, SyncDreamer, TripoSR), ablation studies. LRM's contribution is different (direct reconstruction vs. diffusion+reconstruction loop). |
| C0HDYvGwol (3D-Adapter) | 5.60 | R2 | **Much stronger evaluation**: quantitative results across multiple tasks, multiple baselines, ablations. |
| FL6112vyty (DirectTriGS) | 5.00 | R2 | Different approach (3D Gaussian Splatting generation); paper has quantitative evaluation. |
| v5JrYUdMxc (Fourier123, image-to-3D) | 3.50 | R2 | Has quantitative results on GSO, ablations, baselines. LRM has more novel contribution but equally poor evaluation overall. |
| jdFoxDnBwY (Part321) | 4.80 | R2 | 3D part detection; has ablation studies, quantitative results on 2D segmentation with baselines. |
| PoL2joPZQ4 (MVLight) | 4.25 | R2 | Multi-view diffusion for relighting; has quantitative evaluation and baseline comparisons. |
| lGDmwb12Qq (Sampling-Gaussian) | 4.67 | R2 | Stereo matching; has quantitative evaluation across multiple datasets. |

**Comparison reasoning for final score:** LRM's architectural contribution — a large-scale transformer that directly regresses a triplane-NeRF from a single image with simple reconstruction losses — is more novel than Fourier123's SDS modification or CDM's diffusion regularization, and arguably more impactful than Ouroboros3D's joint training framework. However, the paper's evaluation is dramatically weaker than all comparable anchors: **zero quantitative metrics, only one baseline (qualitative), zero ablations**. Papers in the 4.75–5.00 range (CDM, Ouroboros3D) all provide quantitative results, baseline comparisons, and ablation studies. LRM falls below this bar. The method's genuine novelty and impressive qualitative results prevent it from sinking to the lowest scores, but the evidential gap is severe enough that the paper cannot be accepted in its current form. I calibrate it at 4.0, below CDM (4.75) but above Fourier123 (3.50) due to the larger contribution scope.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>