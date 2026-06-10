## Summary

This paper proposes SparseCubes, a differentiable sparse mesh representation that stores geometric (25-dim) and texture (30-dim) features per cube, operating on only the <5% of cubes that contain mesh faces. A Sparse Cube Transformer with local windowed 3D self-attention (2³ and 4³ neighborhoods) enables processing at 256³ resolution—a leap that dense representations cannot support. The method is evaluated on anime character generation and general Objaverse objects, reporting a ~70% reduction in Chamfer Distance over Instant3D (the next-best method).

## Strengths

- **~70% reduction in Chamfer Distance over the best fine-tuned competitor (Instant3D) on anime characters (Table 1).** This is the strongest quantitative evidence that the sparse representation genuinely preserves fine geometric detail. The CD gap (~70% vs Instant3D) is large and directionally clear, and Instant3D was properly fine-tuned on the same 20K-character dataset. This is not an artifact of unfair comparison.

- **40× training speedup vs. dense cubes at 64³ resolution, enabling scaling to 256³ where dense cubes become infeasible (100×+ slowdown, 2× memory; Table 3).** The paper provides controlled empirical evidence that sparsifying to <5% of cubes does not degrade PSNR/SSIM while substantially improving CD, and that the sparse representation unlocks a resolution regime inaccessible to dense alternatives.

- **Local 3D windowed self-attention (2³ at 128³, 4³ at 256³) reducing memory/computation by >1000× (Section 3.2).** This architectural choice—confining self-attention to small 3D neighborhoods—is what makes the Sparse Cube Transformer practically trainable at high resolutions. The paper reports quantifiable savings (1000× at 128³, 10× speedup with 100× less memory at 256³ with "little loss in mesh and texture quality").

- **Joint geometry+texture embedding per cube (Section 3.1).** Unlike DMTet/FlexiCubes which require a separate implicit field for texture, SparseCubes bake a 30-dim texture feature directly into each cube. This allows geometry and texture to be optimized simultaneously in a single pass, avoiding the skew artifacts and over-smoothing documented in triplane-based methods (Fig. 1, Fig. 5).

- **Training efficiency: 3,800 A100 GPU hours total vs. LRM's 9,000 (Section 3.3).** A concrete system-level savings claim, complementary to the per-iteration savings.

- **Random displacement data augmentation addressing off-center characters (Section 3.3, Table 4).** The paper identifies a specific failure mode (positional embeddings for non-centered cubes are poorly optimized) and validates a simple fix.

## Weaknesses

### Fatal
None.

### Major

1. **Framing-evaluation mismatch: the paper claims "Text-to-3D" but the quantitative evaluation is on single-image-to-3D reconstruction from ground-truth images.** The title and abstract announce a text-to-3D method. Tables 1 and 2 explicitly evaluate single-image-to-3D reconstruction (Table 1 caption: "Comparisons on ground truth single image to 3D"). Quantitative text-to-3D evaluation—measuring text-3D alignment via CLIP score, user study, or any text-conditioned metric—is entirely absent. While qualitative text-to-3D results are shown (Fig. 4), the headline quantitative support is for a different task. This is fixable (reframe the paper or add quantitative text-to-3D evaluation) but as written, the paper overclaims relative to its evidence.

2. **Two of four baselines (DreamGaussian, InstantMesh) are used without fine-tuning on the domain-specific dataset, while the paper states "we fine-tune all the methods used for evaluation" (Table 1 footnote).** This is not fatal—the main 70% CD claim is against Instant3D (fine-tuned), and SDS-based methods like DreamGaussian cannot be trivially fine-tuned. But the comparison against DreamGaussian and InstantMesh is uninformative for the anime domain, and the footnote contradicts the preceding sentence's claim of equal treatment. The authors should explain why these methods could not be adapted, or remove them from the primary comparison.

### Minor

1. **Test set of 30 samples with no confidence intervals or standard deviations (Tables 1, 2).** With a small test set, the reported improvements (especially finer-grained PSNR/SSIM differences) could reflect sample variance. Reporting error bars or statistical significance would significantly strengthen the evaluation.

2. **The 50% storage reduction claim (abstract) is not quantified against any specific baseline.** The 95% computation reduction is explained (sparsity ratio → token reduction), but the 50% storage figure has no supporting experiment or explicit comparison target. What representation is this 50% relative to—dense cubes? Triplanes? 3D Gaussians?

3. **Several reproducibility details are underspecified.** (a) The threshold T in Eq. 1 (cube selection criterion) is not defined—it appears as `T > sum > 0` but T is never stated. (b) The neighboring-cube propagation (Section 3.1) does not specify connectivity (6-connectivity? 26-connectivity?), just "repeated twice to select each neighborhood and its neighborhood's neighborhoods." (c) The 20K anime character dataset is not sourced or described—critical for assessing domain bias and reproducibility. (d) The four input-view camera parameters are not specified.

4. **The multi-view diffusion model (central to text-to-3D) is described in a single sentence** as "similar to ImageDream, but with a higher resolution (512)" (line 50). While the paper's core contribution is the 3D representation, and the text-to-3D pipeline is an application, this component is given vanishingly little documentation given its role in producing inputs for the qualitative results.

5. **Ablation on data augmentation (Table 4) is performed at 64³ resolution**, but the main results use 256³. Whether the augmentation benefit transfers at full resolution is unverified.

### Trivial

None.

## Nice-to-Haves

- A direct efficiency comparison (FLOPs, memory, inference time) against actual competing methods (Instant3D/Triplane, LGM/3D Gaussians, InstantMesh/FlexiCubes) at their operating resolutions would strengthen the efficiency claims beyond the dense-vs-sparse-cube comparison in Table 3.
- Adding a surface-based metric (F-Score, Normal Consistency) would complement the Chamfer Distance for geometric evaluation.
- Reporting failure cases or categories of prompts/characters the method struggles with would improve the paper's honesty and usefulness.

## Removed Points

The following points from the inputs were removed under filtering rules:

- **"95% efficiency claim is a straw man because no serious method uses dense 256³ grids"** → REMOVED. This is factually inaccurate about the comparison target. DMTet and FlexiCubes operate on dense grids, so the comparison against dense cubes at the same resolution is the natural ablation. The paper's claim is about sparsity of the representation, not a cross-method efficiency sweep. The only missing piece is a direct cross-method efficiency comparison (moved to Nice-to-Haves).
- **"The multi-view diffusion model is a critical missing piece that prevents reproduction"** → DEMOTED from Major to Minor (Weakness 4). The paper's core contribution is the 3D representation/transformer, not the upstream diffusion model. Describing it briefly is standard for non-core pipeline components. The criticism is scope creep for the paper's stated contribution.
- **"RenderPeople evaluation table is missing (line 126)"** → REMOVED. The broken reference (`"Tab."` followed by a period) is a parser artifact. The original submission likely contained this table.
- **Various formatting/parser nitpicks** → REMOVED per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the method that the paper itself does not already contain.

## Suggestions

1. **Reframe the paper honestly.** Change the title and abstract to reflect that SparseCubes + Sparse Cube Transformer is evaluated primarily on multi-view/single-image-to-3D reconstruction, with text-to-3D demonstrated as an application. Alternatively, add quantitative text-to-3D evaluation (CLIP score, user study on text-3D alignment).

2. **Define T in Eq. 1.** State the threshold value used in experiments and justify it. If T=8 (surface-crossing criterion), say so explicitly.

3. **Specify the neighbor propagation connectivity** (6-connectivity vs. 26-connectivity) and cite or describe the 20K anime dataset source.

4. **Add standard deviations or confidence intervals** to Tables 1 and 2 given the small (N=30) test sets.

## Score and Decision

The paper presents a genuine technical contribution: SparseCubes is a sensible representation that enables higher-resolution 3D generation with demonstrable quality improvements, and the Sparse Cube Transformer's local windowed attention is a practical enabler. The quantitative evidence—particularly the 70% CD reduction and the 40× speedup over dense cubes—is directionally strong. However, the paper overclaims its text-to-3D framing in the title and abstract while quantitatively evaluating a different task, and several evaluation details (baseline fairness, statistical reporting, reproducibility parameters) need attention. These are fixable issues, but they prevent acceptance in the current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>