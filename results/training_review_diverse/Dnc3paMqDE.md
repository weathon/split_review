Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes DeepSPF, a rotation-equivariant encoder backbone for point cloud processing that combines Spherical Patch Fields (SPF) — a patch-wise representation based on Spherical Gaussians — with a Patch Gaussian Layer (PG-Layer) that learns adaptive patch sizes and enables deeper networks. The method is evaluated on Scan-to-CAD tasks (registration, retrieval, completion) on ModelNet40, ShapeNet, and Scan2CAD, showing consistent improvements when replacing standard encoders (e.g., PointNet) in existing pipelines.

## Strengths

- **Novel patch-wise rotation-equivariant representation (SPF) that captures both local and global information.** Unlike prior global spherical representations (e.g., SGPCR), SPF maps a point cloud to multiple spherical patches with graph-based inter- and intra-relationships. The ablation in Table 1 validates this: the patch-graph component alone (condition E) reduces rotation RRMSE from 0.049 (SGPCR) to 0.039 on zero-intersection ModelNet40.

- **PG-Layer enables adaptive patch sizes and deeper networks while preserving the SG mathematical form.** The differentiable radial component V(r) allows the network to automatically adjust spherical patch sizes, and the formulation preserves the original SG structure to support multiple successive convolutional layers (unlike prior SGConv which deformed the representation). The ablation confirms that adding V(r) (condition V) further reduces RRMSE from 0.036 to 0.028.

- **Consistent improvements across three Scan-to-CAD tasks using a single backbone as a drop-in replacement.** DeepSPF is shown to improve registration (DeepGMR + DeepSPF RRMSE 0.031 vs. original DeepGMR 0.078 on zero-intersection data, Tables 1-2), retrieval (Top-1 error reduced from 0.081 to 0.067, Table 4), and completion (F-score from 0.582 to 0.641 for seen categories, Table 5) — all without increasing model parameters relative to comparable methods.

- **Plug-and-play compatibility with existing decoder architectures.** The paper shows DeepSPF can replace PointNet in DeepGMR and PCN pipelines, improving results without modifying the decoder or loss functions, demonstrating practical utility.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to Vector Neurons (VN) on registration and retrieval tasks.** The Related Work section states "we show improvements over VN due to acquiring local and global information," but VN is only compared on point cloud completion (Table 5: VN-PCN). On the main tasks of registration (Tables 1-2) and retrieval (Table 4), VN-based methods are absent. Since VN is the most directly comparable SO(3)-equivariant point network, this omission undermines the claim of "significant improvements" over the equivariant state of the art. The paper either needs to include VN comparisons on these tasks or temper its claims.

- **The rotation-equivariance proof rests on an unsubstantiated approximation (R_ν ≈ R_p).** Section 3.2 attempts to prove that SPF is SO(3)-equivariant, but the central step (Eq. 9–11) assumes that the rotation applied to the spherical sampling grid approximates the rotation applied to the point cloud (R_ν ≈ R_p), and similarly μ(ν) ≈ μ(p). The paper provides no justification for why this approximation holds, how tight it is, or under what conditions it breaks. Since rotation-equivariance is the paper's central theoretical claim, this gap is significant. An empirical demonstration of equivariance (e.g., measuring feature consistency under random rotations) would partially remedy this, but the theoretical foundation as presented is incomplete.

### Minor

- **No statistical significance or uncertainty estimates.** All quantitative results are reported as single numbers without error bars, confidence intervals, or multi-run statistics. Some claimed improvements are narrow (e.g., Scan2CAD recall 21.1%→22.0% in Table 3; Chamfer distance reductions of a few hundredths). Without variance information, it is unclear whether these gains are reproducible or within training noise.

- **Key implementation details omitted.** The number of PG-Layers per SA layer (m), the initial radii for each SA layer, the latent dimensionality A_n, and the number of spheres per sampled point (C, except in a figure caption) are not specified in the implementation section (4.2). These are necessary for reproducibility; the paper defers to the configurations of baseline works, but since the encoder changes, hyperparameters may not transfer directly.

- **The λ_G ≈ λ_H ≈ 2λ_R assumption in PG-Layer is stated without justification.** Section 3.3 (line 139) asserts this approximation to conclude that the PG-Layer output matches the SPF form. No analysis or experiment is provided to show this approximation holds during training or preserves the SG structure for deeper layers.

- **Notation ambiguity and underspecification in SPF formulation.** The edge function (Eq. 3) uses "max_{j,i,o∈K}" without clarifying whether the max is over neighbor indices or feature dimensions. The notation |ν| as an index set for argmax (Eq. 5-6) is inconsistent with its earlier use as a cardinality. The architectural form of the learnable parameters θ and φ (e.g., MLP layers, dimensions) is not specified.

- **Ablation is confined to the SGPCR decoder framework.** While Table 1's ablation (E, U, V conditions) isolates the contributions of the patch graph, Legendre polynomials, and adaptive radii, it is only tested within the SGPCR pipeline. It is unclear whether the same relative improvements transfer to other decoder architectures (e.g., DeepGMR, DeepUME).

- **Limited completion baselines.** Table 5 compares against PCN (2018) and VN-PCN, but not against more recent completion methods (e.g., PointTr, SnowflakeNet, SeedFormer). The paper acknowledges this in passing (line 244), but the claim of a "30% reduction in Chamfer Distance" would be more impactful with comparison to modern baselines.

### Trivial

- The notation |ν| is used inconsistently — both as a cardinality/line number and as an index set — which can confuse readers trying to follow the derivations.

## Nice-to-Haves

- **Direct visualization of adaptive patch behavior.** The paper claims that PG-Layer automatically learns to adjust patch sizes based on information density, but provides no direct evidence. Showing learned radii overlaid on example point clouds before and after training would substantially strengthen this claim.
- **Runtime/memory analysis.** The method uses FPS and k-NN graph construction per patch. The conclusion notes this as a limitation, but including actual runtime measurements would help practitioners assess trade-offs.
- **Code release.** Given the complexity of the method, releasing an implementation would significantly improve reproducibility and adoption.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No release plan for code/models"** and any questioning of existence/availability of cited methods: Per the hard rules, criticisms about release status of the paper's own code or about the existence of any cited entity are removed. The paper appropriately cites all baselines.
- **"Ambiguity in the scan-to-CAD pipeline"**: The paper describes the pipeline adequately in Section 4.5 — scans are encoded using the same DeepSPF encoder, and retrieval is performed by comparing latent vectors to pre-computed ShapeNet encodings via cross-covariance and SVD.
- **"Strength: theoretical derivation of rotation-equivariance"**: Conflicts with the verified weakness that the proof relies on unsubstantiated assumptions. Per the rule that weakness wins when a strength and weakness disagree, this strength is removed.
- **"PG-Layer is never ablated independently of SPF"**: The ablation in Table 1 tests conditions E (patch graph), U (Legendre), and V (adaptive radii), which collectively constitute the PG-Layer. The components are decoupled; what is not tested is the benefit of the PG-Layer _as a whole_ versus SPF without any convolution, but this is a fine-grained distinction beyond what is standard for ablation.
- **Demand for newer completion baselines (PointTr, SnowflakeNet, SeedFormer) beyond what the paper's encoder-focused scope requires**: The paper explicitly scopes its completion evaluation to encoder comparisons ("to provide a fair comparison between encoder structures, we restrict ourselves to PointNet-based networks"). Criticizing the absence of specialized completion methods is scope creep; the paper frames this as a demonstration of the encoder, not a completion SOTA claim.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core value — a patch-wise, adaptive spherical representation for rotation-equivariant point cloud processing — while identifying the main gaps (incomplete equivariance proof, missing VN comparisons on key tasks) that the authors would need to address in revision.

## Suggestions

1. **Include VN-based encoders in registration and retrieval experiments.** VN-PointNet can be plugged into the same DeepGMR/SGPCR decoders used in Tables 1-2 and 4, providing a direct and fair comparison. This is the single most impactful addition the authors could make.
2. **Strengthen the equivariance argument.** Either (a) replace the hand-wavy R_ν≈R_p approximation with a rigorous derivation, or (b) provide an empirical experiment showing that SPF features are approximately equivariant (e.g., by measuring feature consistency under random input rotations — a standard practice in equivariance papers).
3. **Report error bars or multi-run statistics** for all main results, especially where margins are narrow.
4. **Specify all architectural hyperparameters** in the main paper or supplement: m (PG-Layers per SA layer), initial radii per SA layer, A_n (latent dimensions), and C (sphere sampling count).

## Score and Decision

The paper proposes a technically interesting and empirically promising approach. The strengths — novel patch-wise spherical representation, adaptive radius learning, consistent task improvements — are genuine and supported by evidence. However, two major weaknesses prevent acceptance in this form: (1) the central theoretical claim of rotation-equivariance rests on an unjustified approximation, and (2) the strongest equivariant baseline (Vector Neurons) is omitted from the two main evaluation tasks, undercutting comparative claims. These are addressable with revision, but they are substantive gaps, not minor presentation issues.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>