## Summary

Jigsaw++ proposes a two-stage generative framework for object reassembly. The first stage learns a complete shape prior by mapping raw point clouds to RGB images (via a coordinate-to-color bijection), then feeding those rendered images into LEAP (an image-to-3D model with a DINOv2 backbone) and training a rectified-flow generator on the resulting latents. The second stage — called "retargeting" — fine-tunes this model on paired data consisting of (latent derived from a partial/inaccurate assembly, ground-truth complete shape), enabling reconstruction of complete objects from the output of any existing assembly method.

---

## Strengths

1. **Consistent and substantial quantitative improvements across multiple baselines and datasets.** In Table 1, Jigsaw++ reduces Chamfer distance from 10.5→4.5 (×10⁻²) over Jigsaw on Breaking Bad and from 53.6→42.6 over DGL on PartNet-tables, with precision gains of 3–37 percentage points. These improvements hold across three assembly methods (SE(3), Jigsaw, DGL) and two datasets, demonstrating generality.

2. **Robustness to missing pieces is clearly demonstrated.** With 20% of pieces randomly removed (Table 2, left), performance degrades minimally (CD 1.8→2.0, precision 61.0%→59.5%, recall 59.4%→59.4%). This directly addresses a key real-world limitation of prior assembly methods, which assume most fragments are available.

3. **Novel technical approach to leveraging 2D pretraining for 3D shape generation.** The point-cloud-to-RGB mapping (Sec. 4, lines 115–128) provides a principled way to feed geometric data into image-based models trained on massive 2D datasets, potentially overcoming 3D data sparsity. The design supports arbitrary input/output point counts, circumventing a common constraint in point-cloud generators.

4. **Explicit documentation of failure modes.** The paper identifies three concrete failure categories (size, dataset coverage, topology) with visual examples (Fig. 4), providing a clear roadmap for future work.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative comparison against shape completion or conditioned 3D generation methods.**  
   The paper defines its task as reconstructing a complete 3D shape from a partially assembled point cloud — a problem closely related to point cloud completion. Although the paper acknowledges "generative shape completion which is highly relative to our task" (line 58) and provides a *qualitative* figure showing AdaPoinTr, LION, and SDEdit "failing" (Fig. 1), it never reports quantitative results for any completion baseline. The main tables (Table 1) compare only (assembly method) vs. (assembly method + Jigsaw++). Without knowing how Jigsaw++ performs relative to reasonable alternatives for the same prediction task (e.g., a conditional diffusion model trained on partial→complete pairs, or a completion network adapted to handle misaligned inputs), the paper's central claim of superiority is unsubstantiated. The paper is not merely a "plug-in" for assembly methods — it makes claims about reconstruction quality that require competitive evaluation.

2. **The point-cloud-to-RGB mapping — the paper's core technical enabler — receives no validation.**  
   The mapping converts each 3D coordinate (x,y,z) ∈ [0,1]³ into an RGB color (r,g,b) and renders these as images, which are then fed into LEAP/DINOv2 (lines 115–128). The paper offers no analysis showing that DINOv2 features — trained on natural images with semantic texture and appearance — behave meaningfully on these synthetic color-coded renderings, where "color" is a direct encoding of spatial position. There is no ablation comparing this mapping to a point-cloud-native generative model (e.g., training a rectified-flow model directly on 3D latents without the image bridge), no experiment measuring whether the rendered images preserve geometric fidelity, and no quantitative analysis of the domain gap. Because the entire generative pipeline depends on this mapping working, its lack of validation is a significant gap.

3. **Severe reproducibility gaps.** The paper provides no architecture sizes, no hyperparameters (learning rate, batch size, optimizer, training iterations, number of gradient steps in retargeting), no compute requirements, no inference time, and no specification of the rendering pipeline beyond "following camera settings from Kubric-ShapeNet" (line 154). The number of camera poses, image resolution, and how rasterization handles depth/occlusion are not described. These omissions make the work effectively irreproducible as presented.

### Minor

1. **Retargeting is standard supervised fine-tuning presented as a novel strategy.**  
   The "retargeting" phase (Sec. 5) takes the partially assembled input, reverse-samples through the ODE, applies Langevin dynamics (Eq. 5), and then *fine-tunes the velocity field on paired data* (x₀, x₁) where x₁ is the ground-truth complete object (Eq. 6, lines 184–188). The objective (Eq. 6) is the standard rectified-flow loss applied to these pairs. The identification of the distribution-shift problem (latents from partial inputs fall in low-likelihood regions) is a genuine insight, but the solution — adjust the latent and fine-tune on supervised pairs — is a straightforward two-stage training procedure, not a fundamentally new algorithmic concept.

2. **The "category-agnostic" claim is partially contradicted by the experimental setup.**  
   The abstract and introduction highlight "learning a category-agnostic shape prior." On Breaking Bad, categorical information is indeed not used. However, on PartNet, the paper states: "We independently trained the model on three subsets [chairs, tables, lamps]" (line 203). This means the model receives category information during training on PartNet. While the method can in principle be category-agnostic (as Breaking Bad shows), the headline claim is weakened by the PartNet experiments relying on per-category models.

3. **The downstream assembly improvement experiment relies on ground-truth matching, not an actual algorithm.**  
   Table 2 (right) shows that using the Jigsaw++ prior during Jigsaw's global alignment stage reduces MAE(R) from 36.3°→17.8°. However, the matching is computed "by finding the closest point from the ground truth position of each point to the generated shape" (lines 270–271). The paper candidly acknowledges it "encountered challenges in finding an algorithm that effectively utilizes the complete shape prior" (line 268). This experiment demonstrates that the prior *could* be useful, not that it *is* useful with any practical algorithm.

### Trivial
None.

---

## Nice-to-Haves

- Adding quantitative comparisons against shape completion baselines (e.g., AdaPoinTr, LION, a conditional rectified-flow model trained directly on partial→complete pairs without the image bridge) would substantially strengthen the evaluation.
- An ablation study that replaces the point-cloud-to-RGB mapping with a point-cloud-native generator (or validates DINOv2 features on the renderings) would validate the paper's central technical claim.
- Providing implementation details (architecture, hyperparameters, rendering specifics) is necessary for reproducibility.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"SE(3) is a weak baseline making the comparison stacked"** — The paper also compares against Jigsaw (a strong 2023 baseline) and shows significant improvement (CD 10.5→4.5). The inclusion of SE(3) as an additional baseline is standard practice. Removed as it mischaracterizes the evaluation.

- **"No code release mentioned"** — Removing per hard rule: reproducibility concerns rooted in doubt about existence of artifacts are not valid criticisms.

- **"Table formatting issues (duplicated columns)"** — Parser artifact, not an author error. Removed per hard rule.

- **"Point cloud generation with varying point counts is already solved" / generic concern about prior art coverage** — The paper correctly notes that most point-cloud generators use a fixed number of points. Removed as factually inaccurate.

- **Strength Finder's claim that improvements happen "all without category-specific training"** — This is incorrect for PartNet (per-category training). Removed as it conflicts with verified facts.

- **Strength Finder's generic strengths about "addressing an important problem"** — Removed per filtering discipline (generic/superficial).

---

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's claimed "category-agnostic" design and its actual experimental protocol. The Breaking Bad results (no category info) genuinely support the claim, but the PartNet results rely on per-category models, and the model fails on unseen categories (documented as a limitation). This suggests that the "category-agnostic" property is not inherent to the method but depends on the training data coverage — the 2D pretraining (DINOv2 via LEAP) may help with generalization within a category distribution, but does not automatically confer cross-category generalization without in-distribution training data. This is a more honest characterization than the paper's framing.

---

## Suggestions

1. Add quantitative comparisons against at least 2–3 shape completion baselines (e.g., AdaPoinTr, LION, a simple conditional diffusion model) on the same task, using the same metrics. This is the single most important strengthening the paper needs.
2. Validate the point-cloud-to-RGB mapping: either (a) show that DINOv2 features on these renderings correlate with geometric proximity in 3D space, or (b) ablate by training a point-cloud-native rectified-flow model and comparing performance.
3. Release full implementation details: architecture, hyperparameters, training schedule, rendering parameters (number of camera poses, resolution), and compute budget.
4. Clarify the retargeting protocol: how many gradient steps, on what data splits, and compare against an end-to-end baseline trained directly on (partial assembly, complete object) pairs without the two-stage approach.
5. Tone down the "category-agnostic" claim or provide explicit cross-category generalization experiments (e.g., train on chairs+tables and test on lamps).

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>