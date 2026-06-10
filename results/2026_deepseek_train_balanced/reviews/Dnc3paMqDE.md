## Summary

DeepSPF proposes a learnable, patch-wise SO(3)-equivariant representation for point clouds, targeting Scan-to-CAD tasks (registration, retrieval, completion). The method introduces Spherical Patch Fields (SPF) — which replace a single global sphere with multiple local spherical patches via furthest point sampling — and the Patch Gaussian Layer (PG-Layer), a convolutional module designed to preserve the Spherical Gaussian form for deeper stacking. The backbone is evaluated by plugging it into existing methods (DeepGMR, PCN, SceneCAD) across synthetic and real-world benchmarks.

## Strengths

- **Patch-wise spherical representation is a concrete architectural improvement over prior single-sphere approaches.** Prior work (Salihu & Steinbach, 2023) uses one global SG for the entire point cloud, losing local structure. SPF (Eq. 2–6) generates multiple spherical patches via FPS, processes inter-patch and intra-patch relations through a graph-based edge function, and encodes local-to-global information. This is a verifiable design advance.

- **Differentiable radial component V(r) enabling adaptive patch sizes is novel.** The paper introduces a learnable spherical volume term V(r) = 4/3 π r³ (Eq. 7) that can adjust each patch's radius during training, allowing the model to smoothly transition between local and global receptive fields. This capability is not present in fixed-patch or single-sphere baselines.

- **Ablation study with three controlled conditions (E, U, V) provides structured empirical analysis.** The ablation in Table 1 isolates the contributions of the patch-graph, Legendre-polynomial low-frequency analysis, and adaptive resizable patches, with the text reporting progressive improvements in rotation error. This allows readers to attribute gains to specific design choices.

- **Evaluation across three distinct S2C tasks with multiple datasets.** The paper demonstrates that swapping DeepSPF into existing pipelines (DeepGMR, PCN, SceneCAD) yields improvements on registration (ModelNet40 with zero-intersection/additive noise, Scan2CAD), retrieval (ShapeNet), and completion (ShapeNet), spanning both synthetic and real-world benchmarks.

## Weaknesses

### Fatal

None.

### Major

- **The rotation-equivariance proof is incomplete; the key step is assumed rather than derived.**  
  Section 3.2 (Eq. 9–11) grounds the equivariance claim on the assumption \(R_\nu \approx R_p\) — that the rotation applied to the spherical sampling directions is approximately the rotation applied to the point cloud. The paper does not derive this relationship from the construction; it is stated without justification. Line 102: "assuming a random rotation \(R_p\) on the point cloud \(\mathbf{p}\), we obtain information in respect to the inverse rotation \(R_\nu \approx R_p\) on the sphere." For a proof of equivariance, the correspondence between these rotations must follow from the geometry of the representation, not be imposed externally. As written, the argument is circular and does not establish the claimed theoretical guarantee. The same assumption \(R_\nu \approx R_p\) also appears in the PG-Layer derivation (Eq. 13–14), compounding the issue.

- **The PG-Layer's central claim — preserving the SG form to enable deeper networks — depends on an unsubstantiated assumption and is not empirically validated.**  
  The derivation in Eq. (13)–(14) relies on the assumption \(\lambda_G \approx \lambda_H \approx 2\lambda_R\) (line 139). The paper provides no justification for why these lobe sharpness parameters should satisfy this relation; it is imposed to make the algebraic closure work. Moreover, the paper claims that prior work (Salihu & Steinbach, 2023) prevents deep stacking because its convolution deforms the SG form. Section 3.4 states that each SA layer contains \(m\) PG-Layer modules, yet no experiment ablates \(m\) (e.g., 1 vs. 2 vs. 3 layers) or compares performance when using the prior SG convolution at depth > 1. The main claimed advantage over prior work is stated but neither mathematically grounded nor experimentally demonstrated.

- **The claim "without increasing the number of parameters compared to similar state-of-the-art methods" (conclusion, line 250) is made without supporting evidence.**  
  The paper reports no parameter counts for DeepSPF or the baselines it replaces (PointNet, VN-PointNet) in any experiment. Given that SPF adds FPS, spherical sampling, graph-based edges, Legendre polynomial projections, and per-patch radii, a parameter count comparison is necessary to substantiate this claim.

### Minor

- **No variance or confidence intervals are reported for any experimental result.**  
  The paper reports single values (e.g., "improvements in rotation error," "up to 17% in Top-1 error") without standard deviations, confidence intervals, or significance tests. For a comparison-heavy evaluation across three tasks, readers cannot assess whether the reported gains are reliable or within the noise margin. This is standard practice at top venues for empirical papers.

- **No runtime or computational cost comparison is provided.**  
  DeepSPF introduces FPS sampling, spherical sampling at each FPS point (C samples), graph construction over K neighbors, and Legendre polynomial computation. The conclusion acknowledges the FPS complexity but does not quantify it. For a method proposed as a "versatile and easily integrable backbone," reporting inference time and memory relative to replaced encoders (PointNet, VN-PointNet) is directly relevant.

- **No sensitivity analysis for key hyperparameters.**  
  The number of FPS samples \(f_{no}\) and spherical samples \(C\) appear in Eq. (2) and Section 3.4, but no experiment varies these or justifies the chosen values. The retrieval evaluation (Section 4.5) uses an indirect pipeline (registration-trained latent space → cross-covariance → SVD → Chamfer Distance) following prior work protocols, but the paper does not discuss why simpler latent-space similarity (e.g., cosine distance) would not suffice, leaving it unclear whether improvements stem from the representation or the retrieval protocol.

- **The depth-enabling claim not ablated.** As noted in Major, the paper never compares performance of 1 vs. multiple PG-Layers, or compares against the prior SG convolution stacked. This limitation belongs here because the ablation is missing, not because the claim is disproven.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment comparing 1-layer SPF vs. 2-layer with prior SGConv vs. 2-layer with PG-Layer to directly validate the "enabling deeper networks" claim.
- Characterization of the equivariance approximation error bound when \(R_\nu \neq R_p\), or empirical measurement of equivariance error under random rotations.
- Reporting of variance and parameter counts would substantially strengthen the empirical contribution.

## Removed Points

*The following points from the inputs were removed with justification:*

- **Criticism that evaluation tables being embedded as images is a weakness** — This is a parser artifact; the original submission would contain proper tables. Removed per Hard Rules on formatting.
- **Criticism that the paper conflates rotation variance with zero point-to-point correspondence** — The paper's introduction (lines 20–22) lists them as three *separate* issues rather than conflating them. The reviewer misread the structure. Removed as factually wrong.
- **Criticism about tangled notation and underspecified terms (Eq. 3–6)** — The equations are garbled in the extracted text, likely a parser artifact. The original rendering in the PDF may be clear. Removed per Hard Rules on formatting artifacts.
- **Strength Finder's claim that PG-Layer derivation is supported by evidence** — Verified against the paper: the derivation relies on unjustified assumptions (\(\lambda_G \approx \lambda_H \approx 2\lambda_R\), \(R_\nu \approx R_p\)). This strength conflicts with a verified weakness and is removed per protocol.
- **Strength Finder's framing "the most important piece of evidence is the ablation study"** — While the ablation is a strength, the claim is somewhat overstated given the vague numerical descriptions ("improves," "reduction"). Weakened by incorporation into the more measured assessment above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the disconnect between the paper's ambitious theoretical framing and the thinness of its actual mathematical justification — a pattern worth noting but not a novel insight per se.

## Suggestions

1. **Rewrite the equivariance proof.** Either provide a rigorous derivation that shows \(R_\nu \approx R_p\) follows from the geometric construction (e.g., that FPS-sampled patches rotate with the point cloud), or empirically bound the equivariance error. Without this, the central selling point of the method is unsubstantiated.

2. **Validate the PG-Layer depth claim with controlled experiments.** Compare (a) 1-layer SPF, (b) 2-layer with prior SGConv, and (c) 2-layer with PG-Layer, showing that (c) improves while (b) degrades. If this is infeasible, soften the claim.

3. **Add a table of parameter counts** for DeepSPF vs. every replaced encoder (PointNet, VN-PointNet) across all experiments, to verify the stated claim about not increasing parameters.

4. **Report standard deviations or confidence intervals** for the main comparisons in Tables 1–5.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>