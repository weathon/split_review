- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 3, 8
Now I have a thorough understanding of the paper. Let me compose the final review.

---

## Summary

OneFit introduces a self-supervised garment simulation framework that replaces mesh-specific learning with a function-based patch representation. The key idea is to decompose a garment mesh into patches via ACVD clustering, fit a differentiable n-jet function (PolyFit) to each patch, and learn patch deformations by modifying jet coefficients conditioned on body pose. Training on 6 garment types produces a model that generalizes to unseen garment styles and mesh resolutions, and inference runs at 250+ fps — substantially faster than prior work.

---

## Strengths

1. **Novel function-based garment representation (PolyFit).** Representing garment patches as parametric n-jet functions (Section 3.1) is a principled departure from mesh-specific approaches. It enables analytical computation of metric tensors and Jacobians (Section 3.2), which supports exact enforcement of inextensibility constraints rather than relying on mesh-based approximations. The PCA+STN pipeline to maximize bijectivity of the jet fit is technically well-motivated.

2. **Clear and significant speed advantage.** Table 5 reports OneFit at 3.9 ms/frame (~256 fps) without post-processing and ~6 ms/frame with it, outperforming GAPS (22.9 ms), SNUG (57.2 ms), and HOOD (973.6 ms) by a large margin. This is a concrete, well-measured contribution that is independently valuable for real-time applications.

3. **Empirical evidence of cross-garment generalization.** Table 1 quantitatively shows that a model trained on 6 garments drastically reduces collision ratio (ε_c) on unseen garment types compared to a single-garment model. Figures 5–6 further show visual generalization across garment intra-class and inter-class variations. This supports the claim that local patch-level learning transfers across garment shapes.

4. **Fine-tuning efficiency demonstrated.** Table 2 shows that fine-tuning a multi-garment OneFit model on a new garment (jumpsuit) reduces collision vertices below 2% in 1 hour — a 3× savings over training from scratch. This is practically significant and supports the garment-agnostic claim.

5. **Scalability to varying mesh resolutions.** Figure 4 shows consistent draping across meshes of different vertex counts with stable inference time (Table 5), confirming the mesh-agnostic property of the function-based representation.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative comparison to baselines on deformation quality.** All comparisons to GAPS, SNUG, NCS, and HOOD are visual (Figures 7, 8). Critical metrics such as collision depth, stretch error (edge-length preservation), or Chamfer distance to a reference are reported only for OneFit's own configurations (Table 1) but never for baselines. The claim of being "at par with GAPS" (Section 4.2) is therefore unsubstantiated. Without quantitative evidence, the paper's central quality claim — that the function-based approach matches existing methods while being faster — is only partially supported. Timing data alone does not establish comparable drape fidelity.

2. **Mesh reconstruction from deformed patches is not described.** The paper outputs per-patch deformations *S* and mentions "dense mesh vertices" for sampling, but never specifies how individual deformed parametric patches are assembled back into a coherent, watertight garment mesh. The boundary loss (ℒ_boundary) encourages alignment, but the actual reconstruction pipeline (e.g., how sampled points from different patches are connected, how the original mesh topology is preserved or adapted) is absent. This is a significant methodological gap that affects reproducibility and even basic understanding of the method.

### Minor

1. **The post-processing procedure for collision removal is never defined.** The paper repeatedly invokes "a computationally inexpensive post-processing" and reports it takes 1–2 ms, but its nature — whether gradient-based push, Laplacian smoothing, or an explicit collision resolution — is not disclosed. Since post-processing is used to handle unseen garments (a central use case), this omission makes the reported quality and timing results for that setting unverifiable.

2. **Variable-K patch representation handling is underspecified.** The paper states "K varies for each garment" (Section 3) and describes per-patch MLP encoding, but the crucial architectural detail of how the variable-length set of patch embeddings is aggregated into the joint embedding Z (Section 3: "Z = concatenate(Z_{G_T}, Z_B)") is ambiguous. If Z_{G_T} is a set of per-patch feature vectors, concatenation with Z_B requires a pooling or aggregation step that is not specified. While the empirical results demonstrate the method works, the missing architectural detail is a reproducibility concern.

3. **Positional encoding details are too vague.** The paper uses positional encoding to incorporate "its center position and its relative offsets from body joints" (Section 3). It does not specify which body joints are used (all SMPL joints? a subset?), how offsets are computed relative to each patch, or how this encoding is integrated into the MLP. This is a critical detail for the claimed generalization across garments — if the method relies on encoding distances to specific body joints, the choice of joints matters.

4. **PolyFit hyperparameters are insufficiently reported.** The paper pre-trains PolyFit on synthetic functions and fine-tunes on Cloth3D patches, but does not report: the number of points per patch used for fitting, how patch size (number of constituent mesh vertices) is determined by the ACVD clustering, or the error thresholds considered "acceptable" for the jet fit. Table 3 reports fitting errors without context for what values are good or bad.

### Trivial
None.

---

## Nice-to-Haves

- Ablate the impact of different PolyFit pre-training variants (single-function-family vs. multi-family) on final draping quality, not just on fitting error (Table 3). This would strengthen motivation for the pre-training step.
- Report training time on comparable hardware to baselines (e.g., single GPU vs. 4 A100s) to substantiate the "computationally superior" training claim.
- Clarify the relationship between the per-patch analytic inextensibility loss ℒ_inext and the mesh-based ℒ_mesh_inext — why both are needed, and whether the mesh edge dependency of ℒ_mesh_inext limits mesh-agnosticism in practice.

---

## Removed Points

These points from the original reviews were removed with brief justification:

- *"The garment-agnostic claim is not supported by the method's design, and the paper never explains how a model trained on one set of patch topologies can be applied to garments with fundamentally different patch layouts."* — Overstated. The paper does describe per-patch processing with positional encoding, and provides empirical evidence (Table 1, Figures 5, 6) that the method works across garment types. The mechanism (variable-K handled by per-patch independent processing with spatial encoding) is outlined, though not fully detailed. The architectural aggregation detail is kept as a Minor weakness above; the claim that the method "never explains" how it works is factually incorrect given the described pipeline and shown results.

- *"The paper claims the model is 'self-supervised' — this is correct. However, the boundary loss and mesh inextensibility loss rely on the template mesh's edge list, which is a fixed structure; this is not a self-supervised component in the sense of being derived from physics, but rather a geometric prior."* — Semantic nitpick. Using geometric priors without ground-truth supervision is standard practice in self-supervised learning; the term is used correctly by the field's conventions.

- *"L_mesh_inext requires access to the template mesh edges — this means a specific edge connectivity is implicitly assumed. For a truly mesh-agnostic model, this dependence on a specific edge set is a limitation. The paper acknowledges that 'mesh-specific' methods are undesirable, yet OneFit here still uses mesh edges from the template garment."* — The paper uses both ℒ_inext (analytic, mesh-agnostic) and ℒ_mesh_inext (mesh-based). The mesh-agnostic claim is about the representation, not about every auxiliary loss. The ablation (Table 4) shows ℒ_mesh_inext is needed but does not invalidate the mesh-agnostic representation claim.

- *"The evaluation provides no quantitative comparison to baselines on deformation quality."* — Retained as Major weakness #1 (valid). The removal here is not needed.

- *"The PolyFit error threshold for 'acceptable' fitting is not established."* — Retained as Minor weakness #4 (valid but minor).

- *"The paper claims the model is 'mesh-agnostic' yet OneFit here still uses mesh edges from the template garment."* — Already addressed above.

---

## Novel Insights

The most striking observation from the synthesis is that the harsh critic's central attack — that the garment-agnostic claim is unsupported — is not actually supported by the paper's content. The paper provides both quantitative (Table 1, Table 2) and qualitative (Figures 5, 6) evidence of generalization to unseen garments, and the mechanism (per-patch local processing with body-aware positional encoding) is architecturally designed for variable-K inputs. The real weakness is not that the method fails to generalize, but that the paper underspecifies key components of its own pipeline (mesh reconstruction, post-processing, variable-K aggregation), making reproducibility difficult. The second major gap — no quantitative baseline comparison — is a more traditional evaluation weakness. Interestingly, neither reviewer fully articulated the tension between the paper's genuine speed contribution and the evaluation gap: even if OneFit produced slightly lower-quality drapes than GAPS, its 65× speedup would still be a meaningful contribution, but the paper needs to establish *how much* quality is being traded for that speed. The current presentation sidesteps this trade-off entirely.

---

## Suggestions

1. **Add a quantitative comparison table.** At minimum, report collision percentage/depth, edge-length stretch error, and Chamfer distance to a PBS reference for OneFit and all baselines (GAPS, SNUG, NCS, HOOD) on a shared held-out test set. This single addition would substantially strengthen the paper.

2. **Explicitly describe the mesh reconstruction pipeline.** Add a clear step-by-step description (or a diagram) showing how the set of deformed parametric patches (S := {O, φ_S}) is converted into the final output garment mesh — including how points are sampled, how boundary alignment is enforced in practice, and how the original mesh connectivity is used or adapted.

3. **Specify the post-processing procedure.** Even a brief description (e.g., "we perform gradient-based push along body surface normals with Laplacian smoothing for 1–2 ms per frame") would make the results reproducible and the timing claim verifiable.

4. **Clarify the variable-K aggregation mechanism.** Specify how the per-patch embeddings (Z_{G_T}) are combined: is there a global pooling operation (max/mean)? A set transformer? A simple concatenation followed by a global MLP? This detail is needed for reproducibility.

5. **Report the positional encoding in detail.** Specify which body joints are used for the "relative offsets" and how they are computed for each patch (e.g., nearest joint, weighted by distance to all joints, etc.).

---
