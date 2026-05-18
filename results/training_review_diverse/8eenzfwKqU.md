Now I have a thorough understanding of the paper. Let me craft the final consolidated review.

---

## Summary

GS-VTON introduces an image-prompted 3D virtual try-on method built on 3D Gaussian Splatting. The pipeline has two main components: (1) a personalized diffusion model via LoRA fine-tuning with reference-driven multi-view editing to address inconsistency in 2D VTON outputs, and (2) a persona-aware 3DGS editing mechanism that blends editing-direction attention features with averaged features from the edited image set to maintain cross-view consistency. The paper also introduces 3D-VTONBench, a benchmark with 60 subjects in varied poses and garments. Evaluation includes a user study (25 volunteers, 625 responses), qualitative comparisons against five text-prompted 3D editing methods, and ablation studies.

## Strengths

- **Novel technical approach for image-prompted 3D VTON:** The method tackles a genuine gap — existing 3D editing pipelines accept only text prompts, which lose garment detail. The reference-driven image editing (Eq. 4, Sec. 3.2) simultaneously edits multi-view images while sharing reference attention features to reduce inconsistency, and the persona-aware attention blending (Eq. 6, Sec. 3.3) further regularizes cross-view consistency during 3DGS editing. These two mechanisms are well-motivated and technically coherent.

- **New benchmark (3D-VTONBench):** The paper provides the first dedicated benchmark for 3D VTON with 60 subjects in diverse poses and garments (Sec. 4). This fills a genuine gap, as existing 3D human datasets focus on SMPL-based modeling or general scenes rather than VTON evaluation.

- **User study demonstrates strong preference:** With 25 volunteers and 625 pairwise responses across realism, garment similarity, and overall quality, the user study (Sec. 4.1, Fig. 5) shows GS-VTON significantly outperforms all five text-prompted comparison methods. This provides real human-judgment evidence of the method's effectiveness.

- **Practical efficiency:** LoRA fine-tuning (~30 min) and 3DGS editing (~25 min) on a single V100 GPU with fixed hyperparameters across all experiments (Sec. 3.4) makes the method accessible and robust without per-scene tuning.

## Weaknesses

### Major

- **No standard automatic metrics on the introduced benchmark:** The paper claims to introduce 3D-VTONBench for "comprehensive qualitative and quantitative evaluations" (Sec. 4) and asserts state-of-the-art performance, yet reports no standard automatic metrics (e.g., FID, LPIPS, PSNR, CLIP similarity, or multi-view consistency scores) on this benchmark. The only quantitative results are from user studies. While user studies are valuable, they do not provide reproducible, protocol-based evaluation. The benchmark is described in one paragraph with minimal detail (60 subjects, various poses/garments — no resolution, capture setup, ground-truth availability, or evaluation protocol). This gap is the paper's most serious weakness: the central claim of state-of-the-art performance is not backed by standard, reproducible quantitative evidence.

- **Primary comparison is structurally biased toward the proposed method:** All five comparison methods (GaussianEditor, IG2G, GaussCTRL, IN2N, Vica-NeRF) accept only text prompts, while GS-VTON accepts a garment image — a fundamentally richer condition. The paper mitigates this by generating text prompts via ChatGPT, but the modality asymmetry remains. The ablated baseline in Sec. 4.2 (Image → IDM-VTON → LoRA → 3DGS without consistency modules) is an image-prompted comparator but is only compared qualitatively. A quantitative comparison against this image-prompted baseline (or another reasonable image-prompted competitor) is needed to fairly isolate the benefit of the proposed consistency mechanisms.

- **No quantitative measure of multi-view consistency:** The paper's core motivation is that 2D VTON models produce inconsistent multi-view images, and the proposed components solve this. Yet no quantitative metric of inconsistency is provided (e.g., pairwise LPIPS/SSIM variance across views before vs. after reference-driven editing, or rendered-view consistency of the final 3D scene). The ablation studies show qualitative improvements, but the central empirical claim about consistency reduction is unquantified.

### Minor

- **Hyperparameter sensitivity unreported:** The balancing weight λ=0.55 in Eq. (9) and loss weights λ₁=10, λ₂=15 in Eq. (10) are given without any sensitivity analysis. A brief sweep would strengthen confidence that the method is not brittle to these choices.

- **Benchmark description lacks detail for reproducibility:** The description of 3D-VTONBench (one paragraph, Sec. 4) is too sparse — no information about capture setup, resolution, number of views per subject, whether ground-truth garment-aligned views exist, or how it differs structurally from existing human datasets (THuman, MultiGarmentNet, CAPE). A reader cannot gauge the benchmark's difficulty or suitability.

- **Conceptual comparison with GaussianVTON missing:** GaussianVTON (Chen et al. 2024) is cited but not compared (code unavailable). A brief conceptual discussion of how the two approaches differ — since both use 3DGS for VTON — would help position the contribution.

### Trivial

- None.

## Nice-to-Haves

- Add a controlled image-prompted baseline: edit each view independently with IDM-VTON, then train a 3DGS scene without any consistency modules, and report quantitative metrics against the proposed method.
- A single-sweep sensitivity plot for λ ∈ {0.3, 0.5, 0.55, 0.7, 0.9} in the appendix.
- Expand the 3D-VTONBench description with capture protocol, view counts, and resolution.
- Include a conceptual comparison with GaussianVTON to clarify differences.

## Removed Points

- **"Method description is convoluted" and "pipeline figure not visible":** The method is clearly structured into subsections (3.1–3.4) with well-defined components. The figure-not-visible complaint is a parser artifact. Neither is a valid weakness in the original submission.
- **"Fairness of comparison — need an external image-prompted baseline":** The paper already includes this baseline (Sec. 4.2, the ablated pipeline using IDM-VTON individually with no consistency modules), albeit only qualitatively. The underlying concern (lack of quantitative comparison) is retained in Major, but the claim that no such baseline exists is incorrect.
- **"LoRA trained on only 4 images, how does it generalize?":** The paper explicitly acknowledges this limitation in Sec. 3.3 and references the appendix (stripped by parser) for additional analysis. The concern is registered but already addressed by the authors.
- **Formatting/style nitpicks, "typos", "grammar":** Parser artifacts in the extracted text, not present in the original submission.

## Novel Insights

The reviews surface a fundamental tension in the paper: the technical contributions (reference-driven attention sharing for multi-view editing, persona-aware attention blending for 3DGS) are well-designed and address a real problem, but the evaluation framework does not match the strength of the claims. The harsh critic's core critique — that without automatic metrics the SOTA claim is unsubstantiated — is the single issue that would need to be resolved for the paper to be accepted. Interestingly, the user study design (25 × 5 comparisons = 125 per dimension) actually provides reasonable statistical power for pairwise preference, but the modality-asymmetry confound means the user study primarily validates that *images are better than text* rather than that the specific technical innovations drive the improvement. A within-modality comparison (ablated image-prompted baseline vs. full method) in the user study would have been more informative.

## Suggestions

1. **Add automatic metrics on 3D-VTONBench.** The most impactful improvement: define an evaluation protocol (e.g., hold-out views or leave-one-out), report CLIP similarity between rendered garment region and garment image, LPIPS between rendered views for consistency, and FID on rendered views. This directly addresses the paper's most serious weakness.
2. **Quantitatively compare against the ablated baseline** (Image → IDM-VTON individually → LoRA → 3DGS) using the same metrics above, plus in the user study. This isolates the contribution of the two proposed components on fair footing.
3. **Provide a quantitative consistency measure** (e.g., average pairwise LPIPS across multi-view edited images with vs. without reference-driven editing) to directly support the core motivation.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>