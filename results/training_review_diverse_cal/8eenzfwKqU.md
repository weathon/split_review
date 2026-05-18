Now I have all the information I need. Let me write the consolidated review.

## Summary

GS-VTON proposes a 3D virtual try-on pipeline built on 3D Gaussian Splatting. The method consists of three key innovations: (1) fine-tuning a 2D VTON diffusion model (IDM-VTON) with LoRA on multi-view images for personalization, (2) a reference-attention mechanism during multi-view editing to improve cross-view consistency, and (3) a persona-aware 3DGS editing process that blends attention features from the edited training set into the editing pipeline. The paper also introduces 3D-VTONBench, a benchmark of 60 human subjects for 3D VTON evaluation. User studies and qualitative comparisons against five text-driven 3D editing methods show favorable results.

## Strengths

- **Novel pipeline integrating 2D VTON priors into 3DGS**: The paper proposes a well-motivated approach to extend pre-trained 2D VTON diffusion models (IDM-VTON) to 3D via LoRA fine-tuning on multi-view edited images. This directly addresses the limitation that text prompts cannot capture garment-specific details. (Section 3.2, Eq. 3–4)

- **Reference-driven multi-view image editing for consistency**: The technique of concatenating reference-view attention features (keys and values) during the simultaneous denoising of multiple views is a sensible way to reduce the multi-view inconsistency that arises when editing images individually. (Section 3.2, Eq. 5–6, Figure 4)

- **Persona-aware 3DGS editing**: The blending of self-attention outputs from the editing direction with those from the original edited training set (Eq. 7) helps maintain cross-view consistency during 3DGS optimization. The qualitative ablation (Figure 6) confirms the importance of this component. (Section 3.3)

- **First dedicated 3D VTON benchmark**: 3D-VTONBench fills a genuine gap — prior benchmarks focused on 2D VTON or general-scene editing. (Section 4, opening paragraph)

- **User study with clear preference margin**: 25 volunteers (625 responses) evaluated realism, garment similarity, and overall quality, and the proposed method was preferred by a large margin over five baselines. (Figure 5, Section 4.1)

- **Practical robustness**: The method uses fixed hyperparameters across all experiments and supports editing at the original scene resolution (unlike many 3D editing methods limited to 512×512). (Section 3.4)

## Weaknesses

### Major

- **No objective quantitative metrics on the proposed benchmark**: The paper introduces 3D-VTONBench as a contribution and claims it enables "comprehensive qualitative and quantitative evaluations," but the only quantitative evaluation is a user study. While user studies are valuable, they are subjective and limited (25 volunteers). Standard objective metrics are missing. Specifically, **CLIP image similarity** between the rendered garment region and the input garment image (averaged across viewpoints) and **multi-view consistency scores** (e.g., pairwise LPIPS between rendered views, or variance of CLIP features across views) are both feasible without ground truth and would directly substantiate the paper's central claims about fidelity and consistency. The absence of such metrics is the single most significant gap in the experimental evaluation.

- **Comparison set excludes the most directly related method**: All five baselines (GaussianEditor, IG2G, GaussCTRL, IN2N, Vica-NeRF) are text-driven general 3D editing methods, not designed for VTON. GaussianVTON — the only other 3D VTON method — is mentioned in the related work but not compared against, with the explanation that "their code is not publicly available" (line 224). While this is a practical constraint, the paper's claim of "a new state-of-the-art for 3D virtual try-on" is weakened without at least a detailed discussion of GaussianVTON's reported results, a side-by-side qualitative comparison using the same input data, or a more thorough contextualization of differences.

### Minor

- **Limited hyperparameter analysis**: The key blending parameter λ (defaulting to 0.55 in the persona-aware 3DGS editing) is not ablated — only a "with/without" comparison is shown. Similarly, the choice of the *first* of four randomly selected images as the reference in reference-driven editing is not justified or tested for sensitivity (e.g., what happens if the reference is an extreme viewpoint?). These design choices would benefit from even a small quantitative or qualitative analysis.

- **No failure case quantification**: The limitations section (line 279) honestly acknowledges difficulties with long hair intersecting clothing and severe self-occlusion, but no failure cases are shown or quantified. A reader cannot assess how frequently these issues arise or how severe they are in practice.

### Trivial

- None that survive filtering — presentation issues are handled below in Removed Points.

## Nice-to-Haves

- An analysis of how the number of training images *n* (default 4) or the number of random binary masks *K* during LoRA fine-tuning affects quality would strengthen the reproducibility and understanding of the method.
- Explicit runtime comparisons with baselines (beyond the reported 30+25 minutes for the method itself) would help contextualize the method's efficiency.
- CLIP-based garment similarity and multi-view consistency metrics (noted above as a major gap) are the highest-priority additions.

## Removed Points

These points from the reviews are flagged for removal but preserved here for completeness:

- **Criticism about missing PSNR/SSIM/LPIPS between rendered views and ground truth**: For a VTON task, there is no ground-truth image of the person wearing the target garment, making pixel-wise metrics infeasible. The underlying concern (lack of objective metrics) is valid and has been addressed in the Major section above, but the specific demand for PSNR/SSIM/LPIPS reflects a misunderstanding of the task setup.

- **Criticism about \ToDo{} commands and misspelled section label** (`sec:personalized_inpaiting`): These are likely formatting artifacts or minor author oversights. Per policy, such formatting/style nitpicks are removed from the main review.

- **Criticism about insufficient detail on inpainting mask generation**: The paper states it uses "a 2D human parsing model and a human pose estimation model to generate the image mask" (line 206–207), which is a sufficient level of detail for a methods paper.

- **Criticism about lack of analysis of mask ratio/number of masks K in LoRA fine-tuning**: The paper follows RealFill, a cited work, for these details. This is standard practice and does not constitute a meaningful weakness.

## Novel Insights

None beyond the paper's own contributions. The three reviews converge on the same central issues (lack of standard metrics, limited comparisons) without offering novel interpretations of the method itself.

## Suggestions

1. **Add objective metrics on 3D-VTONBench.** Compute CLIP image similarity between the rendered garment region and the input garment image (averaged across all available viewpoints). Compute a multi-view consistency score, such as pairwise LPIPS between renderings of the same scene or the variance of CLIP features across views. These require no ground truth and directly measure the paper's claimed improvements.
2. **Strengthen the comparison with GaussianVTON.** Even without their code, provide a detailed side-by-side qualitative comparison using identical inputs, and discuss where the two methods differ architecturally and where each excels.
3. **Ablate λ and the reference selection strategy.** A simple sweep over 3–5 values of λ and a comparison of different reference image choices (e.g., frontal vs. profile) would substantially strengthen the experimental rigor.
4. **Show representative failure cases** to give readers a realistic understanding of the method's robustness beyond the brief limitations paragraph.

## Score and Decision

The paper presents a plausible, well-motivated pipeline with clear technical contributions and fills a genuine gap with the 3D-VTONBench benchmark. However, the experimental evaluation is insufficient to support the claimed state-of-the-art status in a convincing way. The absence of any standard objective metrics, the comparison only against text-driven methods that are not designed for VTON, and the limited ablation of key design choices mean the paper's central claims are not yet adequately validated. Major revision is required to bring the experimental evidence to the level expected for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>