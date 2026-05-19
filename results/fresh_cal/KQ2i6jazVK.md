Now let me write the final consolidated review.

## Summary

This paper introduces LIMR, a method that learns implicit skeletal representations (bones, skinning weights, rigidity coefficients) jointly with explicit 3D shape from monocular video, without category-specific priors or 3D supervision. The key algorithmic contribution is the SIOS$^2$ (Synergistic Iterative Optimization of Shape and Skeleton) algorithm that alternates between refining the skeleton via physical constraints (bone length constancy, optical flow similarity) and optimizing the 3D reconstruction model. The method is evaluated on DAVIS and PlanetZoo datasets using 2D keypoint transfer accuracy, and qualitatively on multi-view sequences against BANMo.

## Strengths

1. **Category-agnostic skeleton learning with consistent 2D improvement over strong baselines**: Table 1 shows LIMR achieves 80.2% 2D keypoint transfer accuracy on DAVIS, outperforming LASR (71.9%) and ViSER (74.1%) by clear margins — and 69.9% on PlanetZoo vs. LASR's 66.9% — without using any category-specific template. These are concrete, reproducible numbers on standard benchmarks.

2. **Dynamic Rigidity (DR) loss is a principled improvement over ARAP**: The DR loss weights edge-length consistency by rigidity coefficients computed from skinning-weight entropy (Eq. 2), allowing joint regions more deformation while keeping rigid parts stiff. Table 1 shows DR contributes a consistent 1.7% improvement on both DAVIS and PlanetZoo, and the ablation is cleanly isolated.

3. **Part refinement via one-hot skinning weights addresses a real failure mode**: Section 3.2 describes freezing all parameters except limb parts after initial training. Figure 4 provides clear qualitative evidence that this resolves limb collapse/reconstruction failures in *camel* and *zebra* that both LASR and BANMo exhibit. This is a specific, well-motivated design choice with visible results.

4. **Mesh-contraction-based skeleton initialization avoids K-means artifacts**: Figures 5.2 and 5.3 show that the Laplacian contraction initialization yields bones distributed more plausibly across the body, whereas LASR's K-means initialization concentrates bones in the torso. This is a concrete improvement over prior work's approach.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim of 3D reconstruction improvement via Chamfer Distance is not quantitatively supported in the main paper.** Contribution (5) states: "LIMR improves 3D reconstruction performance with respect to ... 3D Chamfer Distance in the range of 7.9%–14% over state-of-the-art methods." However, no table or figure in the main paper reports 3D Chamfer Distance. The only quantitative metric in the main text is 2D keypoint transfer accuracy (Table 1). The paper references "Tab.\ref{ama}" (appendix) for multi-view comparison with BANMo and mentions "around 12%" improvement — but a quantitative claim of this specificity and prominence (it is listed as a bullet contribution) must be verifiable from the main paper. Relying entirely on the appendix for the metric that operationalizes the paper's central claim is a significant overclaim relative to presented evidence. This is not a methodological flaw — the data presumably exists — but it is a serious presentation gap that undermines the paper's ability to substantiate its own advertised contribution.

2. **The skeleton initialization procedure is underspecified.** Section 3.1 states "Given a mesh M = {X, E}" the Laplacian contraction is applied to obtain the initial skeleton. However, the mesh itself begins as a "simple sphere" (stated in Limitations). How the sphere is transformed into a mesh with sufficient structure for meaningful contraction — and at what point during training the contraction is first applied — is not described. The contraction of a near-spherical mesh into a meaningful skeleton is non-obvious and the paper provides no details or analysis of this critical initialization step. This affects reproducibility.

### Minor

1. **The skeleton refinement threshold sensitivity analysis is narrow and the merging heuristic has a known failure mode.** The paper only tests $t_o$ from 0.85 to 0.99, finding marginal differences in that range. The merging condition — two bones moving similarly — could merge functionally distinct bones that happen to co-move (e.g., both forelegs of a trotting quadruped). This failure mode is not discussed or tested. The paper acknowledges sensitivity but does not bound the problem.

2. **Repeated sentence in Section 3 (Method).** Lines 61-62 contain the exact same sentence twice consecutively: "The implicit representations are optimized using physical constraints such as bone length being consistent and optical flow directions being similar in the same semi-rigid parts across time (Sec. 3.1)." This appears to be a copy-paste artifact.

3. **Single-run evaluation without variance reporting.** Table 1 reports no error bars or standard deviations. While single-run evaluation is common in this line of work, the absence of any statistical characterization leaves concerns about result stability unaddressed.

### Trivial
None (parser artifacts excluded).

## Nice-to-Haves

- A summary of the BANMo multi-view comparison (Tab.\ref{ama}) should be brought into the main paper, even if as a small table, to directly support the Chamfer Distance claim.
- The paper could explicitly describe the initialization timeline: at which training step is the first mesh contraction applied, and how many vertices does the mesh have at that point?
- A brief discussion or experiment on the forelegs-co-motion failure case (when two functionally distinct bones move identically) would improve the completeness of the skeleton refinement analysis.

## Removed Points

The following points from the inputs were removed with justifications:

- **ViSER missing PlanetZoo numbers (harsh critic claim 3 — "dashes are insufficient")**: REMOVED. The paper explicitly explains that ViSER is sensitive to large camera motion and reports dashes with explanation. Reporting dashes with justification is standard practice.

- **BANMo not compared on single video (harsh critic)**: REMOVED. The paper explains BANMo requires multi-view input and cannot produce good results from a single short video. This is a fair scope-based exclusion.

- **RigNet comparison is "different task" (harsh critic)**: REMOVED. The paper uses RigNet as a reference for skeleton quality (comparison of physical plausibility, not task performance), which is appropriate for the diagnostic section.

- **"Optical flow warping ignores 3D rotation" (harsh critic Section-by-Section)**: REMOVED. This is a speculative concern about an approximation the paper does not claim to be exact. The method aggregates 2D flow onto bones via skinning weights, which is a standard approach in this literature.

- **"Degenerate solutions for DR loss" (harsh critic Section-by-Section)**: REMOVED. The claim that the loss landscape admits degenerate uniform-weight solutions is speculative and not supported by evidence. The paper's empirical results (Table 1) show DR consistently helps, suggesting the optimization does not collapse to this degenerate case.

- **All generic/speculative concerns from the harsh critic's "Strengthening the Paper on Its Own Terms"**: REMOVED as they are either covered by the weaknesses above or are speculative.

- **Strength Finder's Strength #6 (optical flow warp)**: REMOVED. This describes a standard implementation detail, not a distinctive contribution.

## Novel Insights

The harsh critic correctly identifies the central structural problem — a mismatch between what the paper claims (specific 3D Chamfer Distance numbers) and what the main paper demonstrates — but this is best understood as an overclaim/presentation issue rather than a fatal methodological flaw. The strength finder surfaces a complementary observation: the paper's actual strongest evidence is the clean 2D keypoint transfer results across two datasets with a proper ablation that isolates the DR loss contribution. Taken together, the reviews reveal that the paper has a solid empirical core (2D results, DR loss, part refinement) packaged with an over-ambitious 3D framing that the main-paper evidence does not fully support. The most productive path for the authors is to either (a) bring the Chamfer Distance table into the main text to back the claim, or (b) reframe the contribution around what is actually demonstrated — consistent improvement in 2D articulation consistency and qualitative 3D quality.

## Suggestions

1. **Move the 3D evaluation (Tab.\ref{ama}) into the main paper.** The Chamfer Distance numbers currently relegated to the appendix should appear as a main table, even if small. The paper advertises these numbers in the contributions — they must be verifiable in the main text.

2. **Clarify the initialization timeline.** Describe when and how the sphere-to-mesh transition occurs relative to the mesh contraction step. A brief note or diagram would resolve the current ambiguity.

3. **Add a brief discussion of the co-moving-bones failure case** in the skeleton refinement analysis to acknowledge the limitation of the flow-similarity merging heuristic.

4. **Remove the repeated sentence** in Section 3 (lines 61-62).

## Score and Decision

This paper makes genuine contributions: a category-agnostic implicit skeleton learning method, the Dynamic Rigidity loss, and the part refinement technique, all supported by solid 2D keypoint transfer results and clean ablations. The main weakness is a significant presentation gap — the paper's most prominent quantitative claim (7.9–14% Chamfer Distance improvement) is stated in the contributions but not backed by a main-text table, only by an appendix reference. This is fixable (move the table into the main text) and does not invalidate the method. The method section has one underspecified step (initialization from sphere via mesh contraction) that should be clarified. Overall, the paper represents a solid contribution that after reasonable revision would be ready for publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>