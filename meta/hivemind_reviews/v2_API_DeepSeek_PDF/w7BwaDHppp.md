## Summary
# Final Review Report

## Summary

This paper addresses the problem of novel view synthesis in **unbounded neural radiance fields** — scenes where cameras point in any direction and content exists at arbitrary distances. Existing NeRF methods use fixed, scene-independent mapping functions (inverted-sphere and contract mappings) that allocate representation capacity in a pre-determined way, causing poor rendering of distant objects especially when cameras are far from the scene origin.

The authors make three contributions:
1. **Geometric analysis via stereographic projection**: A unified framework decomposing existing mappings into inverse stereographic projection + orthogonal projection, revealing that prior methods map onto cylindrical or paraboloidal manifolds whose shape is independent of scene content.
2. **p-norm adaptive mapping**: A mapping function whose manifold shape is controlled by a p-norm parameter, with automatic p-value selection via RANSAC on COLMAP point clouds. Small p allocates more capacity to distant regions; large p focuses on near regions.
3. **Angular ray parameterization**: A complementary sampling strategy that maintains even sample spacing in the deformed embedding space, preventing over/under-sampling when the mapping function non-linearly distorts space.

Experiments across three datasets (mip-NeRF 360, Tanks and Temples, Free Dataset) and four NeRF backbones (DVGO, TensoRF, iNGP, NeRF) show consistent improvements over contract and inverted-sphere baselines, with the largest gains when cameras are far from the scene origin (e.g., +11.25 dB PSNR for iNGP on mip-NeRF 360 ×2).

**Novelty assessment (deferred — external literature verification unavailable in this run):** The core idea — adaptive manifold shaping via p-norm — appears to be novel within the NeRF unbounded-scene literature reviewed in the paper. However, without external search (Retrieval-Disabled Mode), I cannot confirm whether related methods in other volumetric representation domains have explored similar adaptive mappings. Authors should verify novelty against concurrent works on learnable coordinate transformations for neural fields.

## Strengths
1. **Well-motivated geometric analysis**: The paper's use of stereographic projection to unify the analysis of inverted-sphere and contract mappings is a genuine conceptual contribution. By showing that both prior methods correspond to fixed manifolds (cylinder and paraboloid) in a 4D embedding space, the authors provide a clear visual and mathematical explanation for why these mappings fail under camera shift.

2. **Clean formulation of adaptive mapping**: The p-norm parameterization elegantly interpolates between different manifold shapes, and the geometric intuition (convex surface for near focus, concave surface for distant focus) is intuitive and well-communicated through Figures 1 and 10.

3. **General integration with multiple backbones**: The method is demonstrated across four different NeRF frameworks (DVGO, TensoRF, iNGP, NeRF) representing both MLP-based and voxel/grid-based approaches, showing that the mapping is framework-agnostic and widely applicable.

4. **Comprehensive evaluation across camera shift conditions**: The ×1, ×2, ×4, ×8 experimental design systematically tests the method's robustness to camera displacement, which directly targets the claimed advantage. The ablation study (Table 2) separates the effects of the p-norm mapping from the angular ray parameterization.

5. **Honest limitation discussion**: The conclusion explicitly acknowledges failure modes (extreme camera displacement, near-object undersampling) that readers can use to assess applicability to their own settings.

## Weaknesses
The following weaknesses are ordered by severity and impact on research validity.

1. **[Major] Missing statistical significance and variance reporting (Page 7 - Section 5.1, Table 1)**
   All quantitative results are reported as point estimates without variance, confidence intervals, or multi-seed statistics. Many improvements over the contract baseline are small (e.g., DVGO on mip-NeRF 360 ×1: +0.5 dB PSNR; TensoRF on Free: +0.3 dB PSNR). Without error bars, the reader cannot determine whether these gains are statistically reliable or within the noise of random seed variation. This is a critical reproducibility gap for a paper making SOTA claims.

2. **[Major] RANSAC p-value selection criterion is heuristic without rigorous justification (Page 2 - Introduction, Page 6 - Section 4.3)**
   The criterion "maximize Euclidean distance between randomly sampled projected point pairs" is based on the hypothesis that "points should be evenly distributed in the whole space." This hypothesis is plausible but not validated. The paper does not show that the max-distance heuristic correlates with optimal rendering quality, nor does it compare against alternative criteria (e.g., maximizing embedding-space volume, maximizing entropy). Without this validation, the adaptivity claim is only weakly supported.

3. **[Major] Related work lacks comparative taxonomy (Page 3 - Section 2.2)**
   The section catalogs prior methods as a sequential list without organizing them by decision-relevant axes (e.g., fixed vs. adaptive mapping, MLP-compatible vs. grid-compatible, foreground-background separation strategy). This makes it difficult for readers to independently assess where the paper's novelty lies relative to existing approaches. The concluding claim of a "universal" mapping function is overstated since the method requires per-scene p-value estimation.

4. **[Major] Algebraic derivation of contract mapping has skipped steps and dimension mismatch (Page 5 - Section 4.2)**
   The derivation from contract mapping (Eq. 3) to the paraboloidal manifold (Eq. 7-8) omits the intermediate step showing how ∥x_b∥ relates to 1/∥x∥, making it harder to follow. More critically, the derivation uses R^4 vectors throughout (Eq. 4-5), but the original contract mapping operates in R^3. The R^3-to-R^4 embedding is never specified, creating an ambiguity that affects reproducibility.

5. **[Minor] Angular ray parameterization (Eq. 10, Page 7) has a vector dimension ambiguity**
   The angle definition θ = ∠(x - Q, o - Q) mixes 3D world points (x, o) with a 4D projection center Q = (0,0,0,1), and the limiting argument for θ_max is imprecise (d - Q vs. d). This needs clarification to ensure correct implementation.

6. **[Minor] Conclusion overclaims "state-of-the-art" without qualification (Page 9 - Section 6)**
   The SOTA claim is not bounded by dataset, setting, or comparison scope. Some ×1 results show marginal improvement or regression, so the SOTA statement should be qualified.

7. **[Minor] Iterative p-value estimation has circular dependency and no convergence criterion (Appendix D, Page 15)**
   The iterative refinement uses NeRF-rendered depths to re-estimate p, but those depths depend on the initial p, creating a potential circular dependency. No convergence threshold is specified, and the computational cost of retraining is not reported.

8. **[Minor] Noise/sparsity robustness analysis is under-specified (Appendix E, Page 16)**
   The noise model (distribution, parameters) is not specified, and absolute point counts for the sparsity experiment are not reported, limiting reproducibility of these robustness findings.

## Key Issues
### Issue 1: No statistical significance or variance reporting (Severity: Major, Validity Risk: High)

**Location:** Page 7-8, Section 5.1, Table 1  
**What:** All results are single-point estimates.  
**Why it matters:** Without variance, small gains (e.g., +0.3-0.5 dB) cannot be distinguished from noise. The iNGP ×2 case shows a dramatic 11 dB gain, but most comparisons are much smaller.  
**Required fix:** Report mean ± std over ≥3 seeds; add significance tests.

### Issue 2: RANSAC p-selection criterion lacks validation (Severity: Major, Research-Value Risk: High)

**Location:** Page 2 (introduction), Page 6 (Section 4.3)  
**What:** The "max pairwise distance" heuristic for p selection is unvalidated.  
**Why it matters:** The entire adaptive benefit depends on this step. If the heuristic is suboptimal, the claimed advantage is undermined.  
**Required fix:** Compare RANSAC-p against grid-search optimal p on ≥3 scenes; report p values for all scenes.

### Issue 3: Derivation gap and dimension ambiguity in mapping analysis (Severity: Major, Reproducibility Risk: Medium)

**Location:** Page 5, Section 4.2  
**What:** Contract mapping derivation skips an algebraic step; R^3-to-R^4 embedding is unspecified.  
**Why it matters:** The geometric analysis is the paper's core analytical contribution. If the derivation is unclear, the contribution's foundation is weakened.  
**Required fix:** Add the missing substitution step; explicitly state the 4D embedding of 3D points.

### Issue 4: Related work lacks comparative organization (Severity: Major, Novelty-Positioning Risk: Medium)

**Location:** Page 3, Section 2.2  
**What:** Methods are listed chronologically without a comparative taxonomy.  
**Why it matters:** Readers cannot easily assess the paper's position in the field.  
**Required fix:** Restructure as a taxonomy with axes: mapping type (fixed/adaptive), backend type, foreground-background strategy.

### Issue 5: Angular ray parameterization has dimension/formula ambiguity (Severity: Minor, Reproducibility Risk: Medium)

**Location:** Page 7, Section 4.4, Eq. (10)  
**What:** Angle definition mixes 3D and 4D vectors; limiting argument for θ_max is imprecise.  
**Why it matters:** Implementation errors are possible if the formula is used as-is.  
**Required fix:** Clarify the 4D embedding for all vectors in Eq. (10).

## Actionable Suggestions
### S1 (Must): Add statistical significance and variance reporting
**Target:** Table 1 (Page 8), all result paragraphs  
**Action:** Rerun all experiments with ≥3 random seeds and report mean ± std. Add a paired significance test (e.g., Wilcoxon signed-rank) between Ours and Contract for each backbone-dataset pair.  
**Expected benefit:** Readers can distinguish statistically reliable gains from noise.  
**Acceptance criterion:** Table 1 shows "24.30 ± 0.15" style entries; at least one significance claim per dataset.

### S2 (Must): Validate RANSAC p-selection against grid search
**Target:** Section 4.3 (Page 6), Ablation Table 2 (Page 9)  
**Action:** For 3+ scenes, compare the RANSAC-selected p against the optimal p obtained by brute-force grid search over p ∈ {0.5, 0.7, 1.0, 1.1, 1.5, 2.0, 3.0}. Report the selected p values for all scenes as a supplementary table.  
**Expected benefit:** Directly validates the RANSAC heuristic as a reliable proxy for optimal p.  
**Acceptance criterion:** RANSAC-p yields PSNR within 0.5 dB of optimal-p for each scene.

### S3 (Must): Clarify dimension ambiguity in mapping derivation and angular parameterization
**Target:** Section 4.2 (Page 5, Eq. 4-8) and Section 4.4 (Page 7, Eq. 10)  
**Action:** (a) Add the missing algebraic step in the contract mapping derivation. (b) Explicitly state: "For a 3D point x = (x1, x2, x3), we embed it as x' = (x1, x2, x3, 0) before computing ∥x' - Q∥_p with Q = (0,0,0,1)." (c) Revise Eq. (10) using padded vectors.  
**Expected benefit:** Eliminates reproducibility ambiguity.  
**Acceptance criterion:** A reader can implement the mapping directly from the derivation.

### S4 (Nice-to-have): Restructure related work as comparative taxonomy
**Target:** Section 2.2 (Page 3)  
**Action:** Organize prior methods by (a) mapping type (fixed/adaptive), (b) backend (MLP/voxel/grid), (c) foreground-background strategy. Add a short taxonomy table.  
**Expected benefit:** Stronger novelty positioning; easier for readers to see the paper's contribution.  
**Acceptance criterion:** Each prior method is explicitly classified along the proposed axes.

### S5 (Nice-to-have): Add mechanistic analysis of capacity allocation
**Target:** Section 5.1 results analysis (Page 8)  
**Action:** For a representative scene, plot the effective sampling density in embedding space for contract vs. p-norm mapping. Show that p-norm allocates more capacity near scene content.  
**Expected benefit:** Provides causal evidence for the claimed mechanism (capacity allocation), not just correlational performance gains.  
**Acceptance criterion:** A figure showing spatial density comparison with an associated PSNR-per-region breakdown.

### S6 (Nice-to-have): Specify iterative p refinement convergence criterion and cost
**Target:** Appendix D (Page 15)  
**Action:** Report (a) the convergence threshold for p (e.g., |Δp| < 0.05), (b) number of iterations to convergence, (c) total training time.  
**Expected benefit:** Enables reproducibility and practical assessment.  
**Acceptance criterion:** Convergence criterion and iteration count reported.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: NeRF background → bounded volume limitation
- P2: Prior unbounded-scene solutions (NeRF++, mip-NeRF 360)
- P3: Stereographic projection analysis → failure of fixed manifolds
- P4: Key insight (p-norm adaptivity) + RANSAC
- P5: Angular ray parameterization motivation
- P6: Experiment preview

**Issue:** The problem statement (P1) and related work (P2) are split across two paragraphs before the analytical contribution is introduced in P3. The reader must wait until P3 to understand the paper's unique angle (manifold shape analysis).

### Recommended Storyline (Candidate A)

Restructure into a tighter 4-paragraph arc:

- **P1 (Problem + Gap):** NeRFs need bounded volumes → unbounded scenes break this → prior mappings are fixed and scene-independent → core gap: no mechanism for per-scene capacity allocation.
- **P2 (Analytical Insight + Solution Intuition):** We show via stereographic projection that prior mappings correspond to fixed manifolds → our key insight: manifold shape should adapt to scene geometry → p-norm enables this adaptivity.
- **P3 (Technical Approach):** p-norm mapping function → RANSAC-based p selection → angular ray parameterization for consistent sampling.
- **P4 (Evidence + Contribution Summary):** Integrated into four backbones → consistent gains, largest under camera shift → summary of contributions.

### Abstract Outline (Complete)

**S1 — Problem and domain:** "Neural radiance fields (NeRFs) achieve high-quality novel view synthesis for bounded scenes, but their reliance on a pre-defined bounded volume limits performance on unbounded scenes where content exists at all distances."

**S2 — Prior work gap:** "Existing mapping functions for unbounded scenes (inverted-sphere, contract) use fixed, scene-independent manifold shapes that allocate representation capacity in a pre-determined way, causing poor rendering of distant objects when cameras are far from the scene origin."

**S3 — Proposed method:** "We present a p-norm-based adaptive mapping function that shapes its manifold according to scene geometry, with automatic p-value selection via RANSAC on COLMAP point clouds, and an angular ray parameterization that maintains even sample spacing in the deformed embedding space."

**S4 — Key results:** "Integrated into four NeRF backbones (DVGO, TensoRF, iNGP, NeRF), our method achieves consistent improvements across three datasets, with the largest gains (up to +11 dB PSNR) when cameras are far from the scene origin."

**S5 — Bounded implication:** "These results demonstrate that adaptive manifold shaping is a principled and effective strategy for handling unbounded scenes without expanding computational cost."

### Introduction Outline (Complete)

**P1 — Problem (Problem alignment check: ✓)**  
Role: Establish the bounded-volume limitation as the fundamental challenge.  
Claim: Prior NeRF methods assume a bounded volume → fails for unbounded scenes → naive solutions (volume expansion) are computationally prohibitive.  
Transition: "The key bottleneck is that existing coordinate-mapping functions for handling unbounded space do not adapt to scene content."

**P2 — Gap + Analytical Insight (Variable alignment check: ✓)**  
Role: Show that prior mappings (inverted-sphere, contract) have fixed manifold shapes → provide geometric derivation → show this causes capacity allocation that is invariant to scene geometry.  
Claim: Stereographic projection reveals cylinder and paraboloid manifolds → both pay more attention to near objects regardless of actual scene distribution.  
Transition: "This observation leads to the central question: can we design a mapping function whose manifold shape adapts to the scene geometry?"

**P3 — Solution + Key Idea**  
Role: Present p-norm mapping as the answer to the above question.  
Claim: p-norm generalizes the mapping shape → small p → distant focus, large p → near focus → RANSAC automatically selects p from COLMAP point cloud.  
Transition: "The adaptive mapping requires a corresponding ray parameterization that respects the non-linear distortion of the embedding space."

**P4 — Angular Parameterization + Method Summary**  
Role: Introduce angular ray parameterization and preview experimental evidence.  
Claim: Angular sampling ensures even spacing in deformed space.  
Transition: "We validate this approach across four backbones and three datasets..."

**P5 — Contribution Summary**  
Role: List clear, bounded contribution claims.  
Claim 1: First geometric unification of existing NeRF unbounded-scene mappings via stereographic projection.  
Claim 2: Adaptive p-norm mapping with automatic scene-specific p selection.  
Claim 3: Angular ray parameterization for consistent sampling under non-linear embedding.  
Claim 4: Consistent experimental gains demonstrated across frameworks and datasets.

## Priority Revision Plan
| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| **P0** | Missing variance/significance (Table 1) | High (rerun experiments) | Critical — validity of all quantitative claims | Rerun 3 seeds, report mean±std, add significance test |
| **P0** | RANSAC p-selection validation | Medium | High — core claim | Compare vs grid-search on 3+ scenes |
| **P1** | Derivation gap + dimension ambiguity (Eq. 4-10) | Low | Medium — reproducibility | Add missing steps, specify 4D embedding |
| **P1** | Related work restructuring | Low | Medium — novelty positioning | Convert to taxonomy format |
| **P2** | Angular ray param precision (Eq. 10) | Low | Low — implementation clarity | Clarify vector dimensions |
| **P2** | Conclusion SOTA claim bounding | Low | Low — defensive writing | Qualify to bounded claim |
| **P2** | Iterative p refinement details | Low | Low — reproducibility | Add convergence criterion and cost |
| **P2** | Noise/sparsity experiment details | Low | Low — reproducibility | Specify noise model and absolute counts |

### Execution Roadmap

```text
Stage 1 (1-2 days): Claim & notation fixes
  ├── Tighten SOTA wording in abstract/conclusion
  ├── Fix derivation gaps (Eq. 4→8 step, dimension notes)
  └── Clarify Eq. (10) angular ray param vectors

Stage 2 (1 week): Core evidence strengthening
  ├── Rerun all experiments with 3 seeds + std
  ├── Add RANSAC-p vs grid-search validation
  └── Add significance tests for main results

Stage 3 (before next submission): Presentation & robustness
  ├── Restructure related work as taxonomy
  ├── Add mechanistic analysis figure (sampling density)
  ├── Report p values per scene in supplementary
  └── Add convergence criterion for iterative p refinement
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (data/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|------|---------|-------------|-----------------|-------------------|
| E1 | Main comparison (Table 1) | 3 datasets × 4 backbones × 2 camera shift levels (×1, ×2) × contract/inv-sphere/F2-NeRF baselines | PSNR, SSIM, LPIPS | Ours > baseline in most conditions | Adaptive mapping improves rendering | No variance, single seed |
| E2 | Ablation (Table 2) | Bicycle scene, ×1/×2/×4/×8, p-norm vs contract, angular vs normalized ray param | PSNR, SSIM, LPIPS | Both components contribute, p-norm mapping is primary | p-norm mapping + angular param are both beneficial | Only one scene tested |
| E3 | RANSAC p-selection (Section 4.3) | COLMAP point cloud, max-distance heuristic | p values reported (indirect) | RANSAC-p produces near-opt results in ablation | RANSAC is a viable p-selection heuristic | No direct comparison to grid-search optimal p |
| E4 | Iterative p refinement (Appendix D) | Single scene, NeRF-based depth rendering for re-estimation | PSNR, SSIM | Iteration converges to optimal p | SfM errors can be corrected iteratively | No convergence criterion, high compute cost |
| E5 | Noise/sparsity robustness (Appendix E) | Bicycle scene, synthetic noise/sparsity injection | p values, PSNR | RANSAC robust to noise/sparsity | Method works with imperfect SfM | Noise model underspecified, only 1 scene |

### Research-Theme Gap Diagnosis

1. **New knowledge (partial):** The geometric analysis (stereographic projection as unified framework) is a genuine new perspective. However, the adaptive mapping provides incremental gains (0.3-1.0 dB in most ×1 cases) — the core new knowledge is analytical rather than performance-driven.

2. **Reproducibility (weak):** Missing variance, unclear 4D embedding, ambiguous angular parameterization formula, and unspecified convergence criteria for iterative refinement reduce reproducibility.

3. **Impact on practice (moderate):** The method can be plugged into any existing NeRF pipeline that uses coordinate-based mapping, which is valuable. However, the benefit is largest in the ×2 regime, which may not be the primary use case for many practitioners.

### Proposed Research Experiments

#### P0 Experiment: Multi-seed variance + significance testing
- **Target Claim:** "Our method outperforms contract mapping"  
- **Hypothesis:** Gains are statistically significant at p<0.05  
- **Minimal Design:** Rerun all Table 1 entries with 3 random seeds per configuration. Report mean ± std. Apply paired Wilcoxon signed-rank test between Ours and Contract per dataset×backbone.  
- **Controls:** Same seed initializations across methods  
- **Metrics:** PSNR mean±std, p-value  
- **Success Criterion:** >80% of comparisons show p<0.05  
- **Estimated Cost:** ~3× current compute (3 seeds × same training)  
- **Expected Gain:** Critical — validates all quantitative claims

#### P1 Experiment: RANSAC-p vs grid-search validation
- **Target Claim:** "RANSAC effectively selects near-optimal p"  
- **Hypothesis:** RANSAC-p is within 0.5 dB PSNR of grid-search optimal p  
- **Minimal Design:** For 3 scenes (bicycle + 2 diverse scenes), brute-force search p ∈ {0.5, 0.7, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.0, 2.5, 3.0}. Compare RANSAC-p against grid-search optimal p.  
- **Controls:** Same NeRF backbone (recommend iNGP due to sensitivity), same training budget  
- **Metrics:** PSNR gap (optimal - RANSAC)  
- **Success Criterion:** Mean gap < 0.5 dB  
- **Estimated Cost:** 11 p-values × 3 scenes × 1 backbone = 33 additional training runs  
- **Expected Gain:** High — directly validates the core adaptivity mechanism

#### P2 Experiment: Capacity allocation visualization
- **Target Claim:** "The mapping allocates capacity according to scene geometry"  
- **Hypothesis:** p-norm mapping produces more uniform sampling density around scene content than contract mapping  
- **Minimal Design:** For one scene, render depth maps, compute effective sampling density (samples per unit volume) in embedding space for both mappings. Visualize as a 2D histogram.  
- **Controls:** Same number of total samples  
- **Metrics:** Sampling density entropy, spatial distribution plots  
- **Success Criterion:** Higher entropy (more uniform distribution) for p-norm mapping  
- **Estimated Cost:** No new training needed — post-hoc analysis of existing models  
- **Expected Gain:** Medium — provides mechanistic evidence for the claimed advantage

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Must) ─── Multi-seed variance + significance
  └── Gate: All Table 1 entries with std
      └── If passed → solidifies quantitative claims

P1 (Must) ─── RANSAC-p vs grid-search validation
  └── Gate: p value comparison across 3 scenes
      └── If passed → validates adaptivity mechanism

P2 (Nice-to-have) ─── Capacity allocation visualization
  └── Gate: Sampling density entropy analysis
      └── If passed → provides mechanistic explanation
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale:* The paper presents a genuinely interesting geometric analysis (stereographic projection unification) and a clean adaptive mapping formulation. However, the quantitative evidence has a critical gap: no variance reporting or significance testing. The core adaptivity mechanism (RANSAC p-selection) lacks direct validation against optimal p. These issues prevent full confidence in the empirical claims. The novelty position is promising but cannot be fully verified without external literature search (Retrieval-Disabled Mode in this run). The research value — a generalizable plug-in mapping for unbounded NeRF scenes — is meaningful and the method is clearly applicable across multiple backbones.

**Post-Revision Target: [7.5, 8.0] / 10**

*Prediction rationale:* If the authors address the P0 items (multi-seed variance, RANSAC-p validation, derivation clarity), the paper's empirical credibility would be substantially strengthened. The analytical contribution (stereographic projection analysis) is already solid and would support a higher score once the experimental evidence is properly grounded. The upper bound of 8.0 reflects the incremental nature of the gains in standard (×1) settings — the method is a clear improvement in the ×2 regime but provides only modest gains in the ×1 setting, which limits the breadth of impact.

### Scoring Breakdown

| Dimension | Score (0-10) | Weight | Rationale |
|-----------|-------------|--------|-----------|
| Research Value / Contribution | 7 | 30% | Novel geometric analysis + adaptive mapping; practical plug-in value |
| Novelty / Originality | 7 | 25% | Stereographic projection analysis is novel; p-norm mapping is a natural extension; full novelty verification deferred |
| Methodological Soundness | 6 | 20% | Formulation is clean; but missing validation of core adaptivity mechanism |
| Empirical Evidence | 5 | 15% | No variance/significance; small gains in ×1 setting; single-scene ablation |
| Reproducibility / Clarity | 6 | 10% | Dimension ambiguity in derivations; well-written overall |
| **Weighted Total** | **6.5** | 100% | |