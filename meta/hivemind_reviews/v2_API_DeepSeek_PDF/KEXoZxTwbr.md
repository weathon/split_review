## Summary
# Final Review Report

## Summary

The paper proposes MIRReS, a two-stage inverse rendering framework that jointly reconstructs explicit triangle-mesh geometry, spatially-varying PBR materials, and environment lighting from multi-view images. Stage 1 extracts a coarse mesh via neural SDF (NeuS2/InstantNGP). Stage 2 refines vertex positions through trainable offsets and optimizes material and lighting parameters using physically-based multi-bounce path tracing (up to 3 bounces) with Monte Carlo integration. Reservoir-based spatio-temporal importance resampling (ReSTIR) is used for direct illumination to reduce variance at low sample counts.

The core technical contributions are: (1) a two-stage mesh optimization that decouples coarse SDF-based initialization from fine-grained vertex-offset refinement with fixed topology, (2) integration of physically-based multi-bounce path tracing into the inverse rendering optimization loop, and (3) application of reservoir sampling for variance reduction in direct lighting estimation during optimization.

The paper presents experiments on the TensoIR synthetic dataset (4 scenes) and the OWL real-world dataset (4 scenes), comparing against TensoIR, NVdiffrec-MC, and GS-IR. Results show improvements across geometry (CD, N-MAE), albedo, relighting, and novel view synthesis metrics.

**Overall assessment**: The paper addresses a relevant problem in inverse rendering and the two-stage pipeline is technically sound. However, several concerns reduce confidence in the stated contributions: (1) the multi-bounce path tracing contribution is weakened by gradient detachment for indirect rays (gradients do not flow through secondary bounces), (2) quantitative results lack variance reporting, making statistical significance unclear, (3) novelty claims about "state-of-the-art" and "first" cannot be verified without external literature retrieval (deferred), and (4) several methodological details (fixed-topology limitation, dataset-specific modifications) are under-discussed.

## Strengths
1. **Clear problem framing and practical motivation.** The paper identifies a concrete limitation of existing inverse rendering methods: they either use implicit representations (density fields, radiance fields) that are incompatible with standard graphics pipelines, or they use mesh-based representations but suffer from topological instability during optimization. The two-stage solution (SDF-based coarse extraction + vertex-offset refinement) is a reasonable architectural choice that directly addresses this issue.

2. **Physically-based rendering integration.** Incorporating multi-bounce path tracing into the inverse rendering optimization loop is technically non-trivial. The paper demonstrates that physically-based rendering provides more accurate forward-rendered images than radiance-field-based indirect illumination, which in turn improves the optimization signal for material decomposition. The decomposition results (Fig. 6) show notably reduced baked-in illumination artifacts compared to TensoIR and GS-IR, which is visually compelling.

3. **Reservoir sampling for inverse rendering.** While ReSTIR is well-known in real-time rendering (Bitterli et al. 2020), applying it within an inverse rendering optimization pipeline is a relatively novel engineering contribution. The ablation study (Table 4) shows that reservoir sampling contributes ~0.6 dB to albedo PSNR and ~2.2 dB to relighting PSNR, demonstrating practical benefit.

4. **Comprehensive evaluation on multiple datasets.** The paper evaluates on both synthetic (TensoIR) and real (OWL) datasets with multiple metrics (PSNR, SSIM, LPIPS for albedo, relighting, NVS; CD and N-MAE for geometry). This multi-dataset, multi-metric evaluation strengthens the evidence for the method's effectiveness.

5. **Acknowledged limitations.** The limitations section (Appendix C) candidly discusses the reliance on initial coarse mesh quality and the gradient detachment issue for indirect rays. This transparency is appreciated and helps readers assess the method's scope.

## Weaknesses
1. **Gradient detachment undermines multi-bounce contribution claim (Major).** The paper detaches gradients for indirect (non-primary) rays (Section 4.2, Page 7). This means multi-bounce path tracing only improves the forward-rendered image quality, but the material/geometry gradients do not flow through secondary bounces. Contribution claim C2 ("multi-bounce path tracing to provide more accurate estimation of indirect illumination") is thus accurate for rendering quality but misleading for optimization—the physical accuracy helps the loss computation, not the gradient signal. This distinction is not clearly stated in the contribution list or abstract.

2. **Missing statistical significance (Major).** All quantitative results (Tables 2, 3, 4) report single-point metrics without standard deviations, confidence intervals, or significance tests. Given the modest margins in some metrics (e.g., ~2 dB albedo PSNR over GS-IR, ~0.6 dB from reservoir ablation), the reader cannot assess whether improvements are statistically reliable. This is particularly important for the Chamfer Distance metric where values are small (0.056 vs 0.073) and sensitive to mesh extraction parameters.

3. **Novelty claims cannot be externally verified (Deferred).** Due to the Retrieval-Disabled Mode in this review run, external literature verification was not possible. Claims of "state-of-the-art" (Abstract, Contribution C1) and "first inverse rendering framework that supports multi-bounce raytracing" (Page 3, preceding Table 1) require manual verification against prior work. Notably, path-space differentiable rendering methods [Li et al. 2018; Zhang et al. 2020; Jakob et al. 2022] also handle multi-bounce transport, and the claimed "first" status needs qualification regarding the specific technical scope (mesh-based, 3-bounce, gradient-detached setting).

4. **Unstable experimental protocol across datasets (Minor).** The OWL experiments use a different initialization (dataset-provided NeuS mesh instead of NeuS2) and an extra learnable parameter (metallic channel). These differences make it difficult to assess whether the method generalizes consistently or whether performance on OWL benefits from dataset-specific tuning.

5. **Fixed-topology refinement limits geometry correction (Minor).** Stage 2 refines vertex offsets without changing mesh topology. This means topological errors from Stage 1 (incorrect connectivity, disconnected parts) cannot be corrected. The paper acknowledges this indirectly through the "initial coarse geometry" limitation but does not discuss the topology constraint explicitly or quantify its impact.

6. **Albedo-light scaling ambiguity (Minor).** The scaling procedure for albedo (per-channel global scalar for TensoIR, exposure scaling for OWL) is noted but not discussed as a limitation. This procedure compensates for an unresolved ambiguity between albedo intensity and light intensity, meaning the intrinsic decomposition is only up to a global scale factor.

7. **Abstract overclaims (Minor).** The abstract states "state-of-the-art decomposition performance" and "enabling efficient gradient-based optimization with low sample counts" without mentioning the gradient detachment limitation or the specific evaluation conditions. A more bounded abstract would better serve readers.

## Key Issues
### Issue 1: Gradient Detachment for Multi-Bounce Path Tracing (Severity: Major)
- **What**: Gradients of indirect (non-primary) rays are detached during backpropagation (Section 4.2, Page 7). Multi-bounce path tracing only affects forward rendering, not gradient-based material/geometry optimization through secondary bounces.
- **Why it matters**: The paper's second contribution claim ("multi-bounce path tracing to provide more accurate estimation of indirect illumination") implies that the physical accuracy directly improves material optimization. In reality, the improvement comes indirectly through more accurate loss computation in the rendered image, not through gradient flow across bounces. This distinction is never made explicit, and the contribution list in the introduction does not qualify this limitation.
- **Fix path**: (1) Add an explicit paragraph in Section 4.2 explaining the gradient detachment decision and its implications. (2) Qualify contribution claim C2 to state: "multi-bounce path tracing provides more accurate forward-rendered indirect illumination, which improves the loss signal for material optimization; gradients of indirect rays are detached due to memory constraints." (3) Add an ablation in the appendix comparing gradient-detached vs. gradient-checkpointed (or reparameterized) multi-bounce optimization on a single scene to quantify the information loss.

### Issue 2: Missing Statistical Significance in All Quantitative Results (Severity: Major)
- **What**: Tables 2, 3, and 4 report single-point metric values without variance, standard deviations, or significance tests. The ablation study (Table 4) has a single configuration point per condition.
- **Why it matters**: Without variance information, readers cannot assess whether observed differences (e.g., 0.6 dB albedo PSNR gain from reservoir sampling, 23.3% CD reduction) are statistically reliable or within noise range. This is especially critical for the CD metric (0.056 vs 0.073) which can vary significantly with mesh extraction parameters.
- **Fix path**: (1) Run all experiments with at least 3 random seeds and report mean ± std. (2) Add pairwise significance tests (paired bootstrap or Wilcoxon) between the proposed method and the strongest competitor for main metrics. (3) For mesh metrics (CD, N-MAE), report the mesh extraction parameters and the sensitivity of results to those parameters.

### Issue 3: Unverifiable Novelty Claims (Severity: Major, Deferred)
- **What**: The paper claims "state-of-the-art" (Abstract, C1) and "first inverse rendering framework that supports multi-bounce raytracing" (Page 3).
- **Why it matters**: These strong claims require external literature verification that is unavailable in this review run (Retrieval-Disabled Mode). Path-space differentiable rendering methods (e.g., Li et al. 2018, Jakob et al. 2022) also handle multi-bounce transport, and the specific scope of the "first" claim (mesh-based, 3-bounce, gradient-detached) must be precisely defined.
- **Fix path**: (1) Replace "first inverse rendering framework that supports multi-bounce raytracing" with a scoped claim: "To our knowledge, the first mesh-based inverse rendering method to integrate physically-based multi-bounce path tracing (up to 3 bounces) with differentiable mesh optimization for joint geometry-material-lighting estimation." (2) Replace "state-of-the-art" in abstract with "competitive" or "improved" and bound the claim to the evaluated datasets and protocols.

### Issue 4: Inconsistent Experimental Protocol Across Datasets (Severity: Minor)
- **What**: OWL experiments use (a) a different initial mesh (dataset-provided NeuS instead of NeuS2) and (b) an additional metallic parameter not present in the TensoIR experiments.
- **Why it matters**: These inconsistencies make cross-dataset conclusions harder to interpret. If the OWL initialization is higher quality, the advantage might partly come from initialization rather than the method itself.
- **Fix path**: (1) Add an ablation on the TensoIR dataset using the OWL initialization protocol to verify consistency. (2) Report the quality metrics of the initial coarse mesh for both datasets to quantify initialization effects.

## Actionable Suggestions
### S1: Clarify gradient detachment in method and contributions (Must)
- **Action**: Add one paragraph in Section 4.2 explaining that gradients of indirect rays are detached and why (memory constraints). Explicitly state that multi-bounce path tracing improves forward rendering quality and thus the optimization loss signal, but does not propagate gradients through secondary bounces.
- **Location**: End of Section 4.2, before the "Note" sentence.
- **Mentor Revised Version**:
  "Note that gradients of indirect (non-primary) rays are detached during backpropagation to limit GPU memory usage. This means the multi-bounce path tracing improves the forward-rendered image quality and the resulting photometric loss, but the material and geometry parameters at secondary intersection points are not directly optimized through indirect-ray gradients. Extending gradient flow to all bounces is a promising direction for future work using gradient checkpointing or reduced-budget approaches."
- **Also update**: Abstract, Contribution C2, and Conclusion to reflect this qualification.

### S2: Add variance reporting and significance tests (Must)
- **Action**: Re-run experiments with at least 3 random seeds and report mean ± std in Tables 2, 3, and 4. Add a supplementary table with pairwise p-values (paired bootstrap or Wilcoxon signed-rank) comparing Ours vs. the strongest competitor per metric.
- **Location**: Tables 2, 3, 4 and a new supplementary table in the appendix.
- **Expected benefit**: Provides statistical reliability assessment and strengthens the empirical contribution.

### S3: Bound novelty and SOTA claims (Must)
- **Action**: Replace "state-of-the-art" in Abstract with "competitive" or "improved performance on evaluated benchmarks." Replace "first inverse rendering framework that supports multi-bounce raytracing" with a precisely scoped claim.
- **Location**: Abstract, Page 3 (before Table 1), Contribution C1.
- **Mentor Revised Version** (Page 3):
  "To our knowledge, MIRReS is the first mesh-based inverse rendering method to integrate physically-based multi-bounce path tracing (up to 3 bounces) with differentiable vertex-offset optimization for joint geometry-material-lighting estimation."
- **Expected benefit**: Eliminates vulnerability to literature verification and improves scientific defensibility.

### S4: Add topological limitation discussion (Nice-to-have)
- **Action**: Add 2-3 sentences in the Limitations section discussing the fixed-topology refinement constraint: incorrect topology from Stage 1 cannot be corrected in Stage 2, and this is distinct from the "fine detail" limitation already discussed.
- **Location**: Appendix C, after the sentence about "areas with high specularity or fine details."
- **Mentor Revised Version**:
  "Additionally, because Stage 2 refines vertex positions without changing mesh connectivity, topological errors in the coarse mesh (e.g., incorrect genus, disconnected components) cannot be corrected during refinement. Enhancing Stage 2 to support topological changes, for example through remeshing or adaptive subdivision, remains an open challenge."

### S5: Report initial mesh quality metrics (Nice-to-have)
- **Action**: Add a table reporting the quality of the initial coarse mesh (CD vs. ground truth, vertex count, number of connected components) for all scenes, to help readers understand how much of the final quality is attributable to the initial SDF extraction vs. the Stage 2 refinement.
- **Location**: Appendix, either in Section A or as a supplementary table.

### S6: Standardize experimental protocol (Nice-to-have)
- **Action**: For the TensoIR dataset, run an additional experiment using the OWL initialization protocol (NeuS mesh of similar quality to dataset-provided mesh) to verify that the method's gains do not depend on dataset-specific initialization choices.
- **Alternative**: Explicitly state that the OWL dataset's provided NeuS mesh was used for practical reasons and provide quantitative comparison of initial mesh quality between NeuS2 and the dataset-provided NeuS mesh.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Problem definition + prior implicit methods (NeRF/SDF) + their limitations + TensoIR + two inherent disadvantages.
- P2: Proposed solution (MIRReS) + contrast with NVdiffrec-MC + three key technologies + contribution list.

**Strengths of current arc**: Clearly identifies two technical gaps (implicit representation vs. mesh, radiance-field indirect vs. PBR indirect). The contrast with NVdiffrec-MC is relevant.

**Weaknesses**: P1 reads as a literature list (7+ citations) that buries the key insight. The "two inherent disadvantages" claim is framed as applying to "these implicit methods" collectively, but TensoIR already uses explicit second-bounce ray marching, partially blurring the distinction. The contribution list contains performance claims rather than capability claims.

### Alternative Storyline Candidates

**Candidate A (Problem-Gap-Solution-Impact)**:
- P1: **Problem & Stakes** — Inverse rendering is essential for graphics pipelines but ill-posed. The industry standard output is triangle meshes with PBR materials, yet most inverse rendering methods produce implicit representations (NeRF, SDF, 3DGS) that cannot be directly used in game engines or CAD software.
- P2: **Gap** — Existing mesh-based inverse rendering (NVdiffrec-MC) suffers from topological instability during optimization because end-to-end mesh refinement (DMTet) creates self-intersections and holes that break multi-bounce path tracing. Prior implicit methods (TensoIR) sample secondary rays but rely on radiance-field caching rather than physically-based rendering, leading to baked-in illumination artifacts.
- P3: **Solution** — We propose MIRReS, a two-stage pipeline that (1) first extracts a coarse mesh from a neural SDF (NeuS2), then (2) refines vertex positions via stable offset optimization while jointly optimizing PBR materials through multi-bounce path tracing. This decoupling prevents topological drift while enabling physically-based indirect illumination.
- P4: **Evidence Preview** — Experiments on synthetic and real datasets show improved decomposition accuracy (CD: 0.056, N-MAE: 3.305), particularly in scenes with complex shadows and inter-reflections.
- P5: **Contributions** — [List three precise claims as revised in S3].

**Candidate B (Capability-Focused)**:
- P1: **Industry Compatibility Gap** — Graphics pipelines require triangle meshes, but modern inverse rendering methods produce neural fields or point clouds. We aim to produce directly usable mesh+PBR assets.
- P2: **Technical Challenge** — Direct mesh optimization from images is unstable; DMTet-based methods produce topological artifacts. Multi-bounce path tracing on unstable meshes is intractable.
- P3: **Two-Stage Solution** — Our key insight is to separate geometry initialization (SDF-based, globally consistent) from refinement (vertex-offset-based, locally stable). This enables physically-based multi-bounce path tracing during optimization.
- P4: **Key Technical Components** — (a) Vertex-offset refinement with fixed topology ensures ray-mesh intersection reliability; (b) Multi-bounce path tracing provides physically accurate indirect illumination for the rendering loss; (c) Reservoir sampling reduces Monte Carlo variance, enabling low-SPP optimization.
- P5: **Results & Limitations** — [Result summary + explicit limitations preview].

**Recommended: Candidate A**, as it creates a clearer narrative through-line from industry need to technical gap to solution design to evidence.

### Abstract Outline (Revised)

(S1) **Domain & Problem**: "Inverse rendering from multi-view images typically produces implicit neural representations incompatible with standard graphics pipelines."
(S2) **Gap**: "Existing mesh-based methods suffer from topological instability during optimization, preventing reliable multi-bounce path tracing for indirect illumination."
(S3) **Solution**: "We propose MIRReS, a two-stage framework that first extracts a coarse mesh via neural signed-distance fields, then jointly refines vertex positions and optimizes PBR materials through physically-based multi-bounce path tracing (up to 3 bounces)."
(S4) **Key Technique**: "Reservoir-based spatio-temporal importance resampling reduces Monte Carlo variance in direct lighting estimation, enabling stable optimization at 32 samples per pixel."
(S5) **Result (bounded)**: "On the TensoIR synthetic dataset and OWL real dataset, MIRReS achieves improved geometry, albedo, and relighting quality compared to prior implicit and mesh-based methods under the evaluated settings. The output mesh and materials are directly usable in standard graphics engines."

### Introduction Outline (Revised, Candidate A)

**P1 — Problem & Stakes** (1 paragraph, ~10 sentences)
- Opening: Define inverse rendering and its ill-posed nature.
- Industry requirement: Triangle meshes + PBR materials are the universal standard.
- Current limitation: Most methods produce neural implicit representations (NeRF, SDF, 3DGS).
- Consequence: Even when geometry can be extracted via marching cubes, the lack of explicit mesh during optimization prevents direct path tracing and limits material accuracy.
- **Anchor**: Cite industry-standard pipelines (game engines, CAD) as the practical motivation.

**P2 — Gap Analysis** (1 paragraph, ~12 sentences)
- Mesh-based prior work: NVdiffrec-MC uses DMTet for mesh optimization.
- Failure mode: DMTet's end-to-end refinement produces topological errors (holes, self-intersections).
- Impact: These errors make multi-bounce path tracing intractable (recursive error accumulation).
- Implicit indirect illumination: TensoIR uses radiance-field caching for indirect light, leading to baked-in shadows.
- **Key gap**: No existing method combines stable mesh optimization with physically-based multi-bounce indirect illumination.

**P3 — Proposed Solution** (1 paragraph, ~10 sentences)
- Overview of two-stage design: SDF→coarse mesh→vertex-offset refinement.
- Why this works: Fixed topology + dual-loss supervision (radiance field + PBR) prevents drift.
- Multi-bounce path tracing: Up to 3 bounces, directly on mesh, with gradient detachment for non-primary rays.
- Reservoir sampling: ReSTIR for direct illumination reduces variance at low SPP.
- **Bridge**: "We detail each component in the following sections."

**P4 — Contributions** (1 paragraph, brief)
- Three precise claims (as revised in S3) with scoped language.
- Explicit mention that gradient detachment applies to indirect rays.

## Priority Revision Plan
### P0 — Publication-Critical (must fix before acceptance)

| Priority | Item | Evidence | Action | Expected Benefit | Effort |
|---|---|---|---|---|---|
| P0.1 | Clarify gradient detachment for indirect rays | Section 4.2, Page 7; Contribution C2; Abstract | Add explanation paragraph in Section 4.2; qualify C2 and Abstract wording | Prevents misleading readers about multi-bounce contribution; improves scientific accuracy | Low (text edit) |
| P0.2 | Bound SOTA and "first" claims | Abstract; Page 3 (Table 1 preceding text); Contribution C1 | Replace with scoped claims as described in S3 | Eliminates vulnerability to literature verification challenge | Low (text edit) |
| P0.3 | Add variance/std to all quantitative results | Tables 2, 3, 4 | Re-run experiments (>=3 seeds); report mean±std; add significance tests | Provides statistical reliability; major review robustness | Medium (compute) |

### P1 — High Impact (should fix before camera-ready)

| Priority | Item | Evidence | Action | Expected Benefit | Effort |
|---|---|---|---|---|---|
| P1.1 | Discuss topological limitation of vertex-offset refinement | Section 3.2; Limitations (Appendix C) | Add paragraph about fixed-topology constraint | Fully discloses method's scope boundaries | Low (text edit) |
| P1.2 | Standardize OWL/TensoIR experimental protocol | Section 5.2 (OWL paragraph) | Add ablation on TensoIR with OWL-style initialization; report initial mesh quality | Strengthens cross-dataset generalization evidence | Medium (experiment) |
| P1.3 | Fix Eq. (8) notational ambiguity | Page 6, Eq. (8) | Replace ≡ f(ω_i) notation with explicit integrand definition | Improves readability and precision | Low (text edit) |
| P1.4 | Revise conclusion for accuracy | Page 10, Conclusion | Replace "multi-importance sampling" with correct description; add limitations summary | Ensures conclusion reflects validated findings only | Low (text edit) |

### P2 — Quality Improvement (nice-to-have)

| Priority | Item | Evidence | Action | Expected Benefit | Effort |
|---|---|---|---|---|---|
| P2.1 | Add initial mesh quality metrics | N/A | Report CD/N-MAE of coarse mesh vs ground truth per scene | Helps attribute gains to pipeline components | Low (analysis) |
| P2.2 | Per-scene metric variance | Appendix B | Add per-scene mean±std to supplement aggregated results | Provides finer-grained reliability assessment | Medium (analysis) |
| P2.3 | Ablation on metallic parameter | Section 5.2 | Run TensoIR evaluation with metallic channel to test cross-scene necessity | Clarifies whether metallic is dataset-specific | Low (experiment) |
| P2.4 | Discussion of albedo-light scaling ambiguity | Section 5.1 | Add paragraph explaining scaling procedure as a limitation | Improves transparency about decomposition ambiguity | Low (text edit) |

```text
ASCII Diagram — Revision Strategy Roadmap
[P0.1: Gradient detachment clarification]
    -> [Add explanation in Section 4.2 & qualify C2/Abstract]
    -> [Expected: prevents misleading interpretation of multi-bounce contribution]

[P0.2: Bound SOTA/first claims]
    -> [Replace with scoped wording in Abstract, Page 3, C1]
    -> [Expected: eliminates vulnerability to literature verification]

[P0.3: Variance & significance]
    -> [Re-run experiments (3+ seeds), report mean±std, add p-values]
    -> [Expected: provides statistical reliability for all metric claims]

[P1.1: Topological limitation]
    -> [Add paragraph in Limitations about fixed-topology constraint]
    -> [Expected: fully discloses method's scope]

[P1.2: Standardize protocol]
    -> [Run TensoIR ablation with OWL-style initialization]
    -> [Expected: strengthens cross-dataset generalization evidence]

[P2.1-P2.4: Quality improvements]
    -> [Add analysis, per-scene variance, metallic ablation, scaling discussion]
    -> [Expected: improves transparency and fine-grained evaluation]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 (Table 2) | Full method vs baselines on TensoIR dataset (geometry, albedo, relighting, NVS) | 4 scenes (Lego, Ficus, Hotdog, Armadillo); compared with NVD-MC, TensoIR, GS-IR | CD, N-MAE, PSNR, SSIM, LPIPS | Ours best on all metrics (CD: 0.056, N-MAE: 3.305, Albedo PSNR: 32.348, Relighting PSNR: 32.363) | C1 (General decomposition/relighting quality) | No variance/std; single seed only; GS-IR CD = N/A (incomparable) |
| E2 (Table 3) | Full method vs baselines on OWL real dataset (relighting, NVS) | 4 scenes (Antman, Tpiece, Gamepad, Porcelain Mug); NeuS initialization + metallic channel | PSNR, SSIM, LPIPS | Ours best on all metrics (Relighting PSNR: 28.827, NVS PSNR: 38.223) | C1 | Different initialization than TensoIR experiment; added metallic channel confounds comparison |
| E3 (Table 4) | Ablation: reservoir sampling + multi-bounce path tracing | TensoIR dataset (aggregate); 2x2 design | Albedo PSNR, Relighting PSNR | Full model best (34.348/33.788); reservoir contributes ~0.6 dB to albedo, multi-bounce ~1.8 dB | C2 (multi-bounce), C3 (reservoir) | Single configuration point per condition; no interaction analysis; no variance |
| E4 (Fig. 7, Appendix) | Ablation: indirect illumination | Hotdog scene (qualitative) | Visual comparison (albedo) | Indirect illumination reduces baked-in specular in albedo | C2 | Qualitative only; single scene |
| E5 (Fig. 8, Appendix) | SPP sensitivity (4 to 64) | Hotdog scene; 4 configurations | NVS PSNR | "ReSTIR full" best across all SPP; 32 SPP is optimal | C3 | Single scene; no direct analysis of SPP vs. training convergence |
| E6 (Fig. 9, Appendix) | Ablation: neural radiance field rendering | Qualitative comparison | Normal maps, NVS | Joint radiance+PBR better than PBR-only | Mesh refinement design choice | Qualitative only; no metric reported |

### Research-Theme Gap Diagnosis

1. **New knowledge**: The paper demonstrates that mesh-based two-stage optimization with multi-bounce path tracing improves decomposition quality. However, the gradient detachment for indirect rays means the mechanism behind the improvement is partially attributed to better forward-rendered loss rather than better gradients—this distinction is not analyzed.

2. **Reproducibility**: The paper provides network architecture details and training losses in the appendix, which supports reproducibility. The main concern is the lack of variance reporting and the use of custom CUDA kernels for LBVH and reservoir sampling, which may be difficult to reproduce without the exact code.

3. **Impact on practice/understanding**: The practical value (direct mesh output for graphics pipelines) is clearly stated. However, the computational cost (~4.5 hours on a single RTX 4090) and reliance on NeuS2/InstantNGP for stage 1 mean the method is not yet a lightweight solution.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|---|
| P0.3 | All claims (variance) | Observed gains are statistically significant | Re-run all main experiments (TensoIR + OWL) with 3 random seeds | Same hyperparameters; vary only random seed | Mean±std for all metrics; pairwise p-values vs strongest baseline | Gains remain >= 1 std above second-best for main metrics | ~3x compute time (~13.5 hrs GPU) | Major: enables statistical reliability assessment |
| P1.2 | C1 (protocol consistency) | Method gains are not initialization-dependent | Run TensoIR experiment with NeuS initialization (same protocol as OWL) instead of NeuS2 | Compare NeuS2-init vs NeuS-init on TensoIR | CD, N-MAE, Albedo PSNR | Metrics within 5% of original TensoIR results | ~4.5 hrs GPU | Medium: validates cross-dataset protocol consistency |
| P2.2 | C1 (per-scene analysis) | Improvements are consistent across scenes | Report per-scene mean±std metrics for Tables 2 and 3 | N/A (re-analysis of existing runs with seeds) | Per-scene PSNR/SSIM/LPIPS with std | All scenes show positive delta over baselines | ~2 hrs analysis | Medium: provides finer-grained reliability |
| P2.3 | C2, C3 (metallic ablation) | Metallic channel does not affect non-metallic scene results | Run TensoIR scenes with additional metallic channel | Compare original TensoIR results (no metallic) vs TensoIR+metallic | Albedo PSNR, Relighting PSNR | No significant change in non-metallic scenes; improvement in scenes with specular | ~4.5 hrs GPU | Low-Medium: clarifies necessity of metallic parameter |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

Stage P0 (Before resubmission):
    [P0.3: Multi-seed variance analysis]
        -> [Re-run main experiments with 3 seeds]
        -> [Report mean±std + pairwise p-values]
        -> [Gate: Gains must exceed 1 std above second-best]

Stage P1 (Before camera-ready):
    [P1.2: Protocol consistency ablation]
        -> [Run TensoIR with NeuS initialization (OWL-style)]
        -> [Compare vs original NeuS2-init results]
        -> [Gate: Metrics within 5%]

Stage P2 (Quality improvements):
    [P2.2: Per-scene variance] -> [P2.3: Metallic parameter ablation]
        -> [Verify consistency and necessity]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale**: The paper addresses a relevant problem (inverse rendering with industrial-grade mesh output) and presents a technically solid two-stage pipeline. The multi-dataset evaluation is comprehensive and the visual results are compelling. However, the score is constrained by:

- **Novelty (weight: high)**: The individual components (two-stage mesh refinement, multi-bounce path tracing, reservoir sampling) are individually known techniques. The main novelty is their integration into a cohesive pipeline. Gradient detachment for indirect rays reduces the technical depth of the multi-bounce contribution. External literature verification is deferred, so novelty conclusions are provisional. **Effective novelty score: 5/10**.

- **Research value (weight: high)**: The practical value (direct mesh+PBR output for graphics pipelines) is clear and well-motivated. The two-stage design is a practical solution to a known instability problem. **Research value score: 7/10**.

- **Validity/Soundness (weight: high)**: The main concern is the lack of statistical significance in all quantitative results. Without variance reporting, the reliability of reported gains is uncertain. The gradient detachment issue is not transparently communicated in the main claims. **Validity score: 6/10**.

- **Reproducibility (weight: medium)**: Architecture details and losses are provided. Custom CUDA kernels for LBVH and reservoir sampling may hinder exact reproduction without code release. **Reproducibility score: 6/10**.

- **Presentation (weight: medium)**: Generally well-written with clear figures. The introduction could be more focused. Some equations have notational issues (Eq. 8). **Presentation score: 7/10**.

### Post-Revision Target: [7.5, 8.0] / 10

If the following P0/P1 items are addressed:
1. **Gradient detachment clarification** (P0.1): Accurate communication restores trust in contribution claims.
2. **Bounded SOTA/first claims** (P0.2): Eliminates vulnerability to literature verification.
3. **Variance reporting and significance tests** (P0.3): Enables statistical reliability assessment.
4. **Topological limitation discussion** (P1.1): Full disclosure of scope boundaries.

The paper would be a solid contribution at a top venue. The achievable score range reflects the remaining uncertainty from unverifiable novelty claims (which require manual literature search) and the inherent limitations of fixed-topology refinement and gradient detachment that are design constraints rather than fixable issues.