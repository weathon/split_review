## Summary
# Final Review Report

## Summary

This paper proposes MEGA (Memory-Efficient 4D Gaussian Splatting), a compression framework for 4DGS-based dynamic scene representation. The method introduces two main technical contributions: (1) a DC-AC color decomposition that replaces the high-dimensional 4D spherical harmonics (144 parameters per Gaussian) with a per-Gaussian 3-parameter DC component plus a lightweight MLP-based AC color predictor, and (2) an entropy-constrained Gaussian deformation technique that expands each Gaussian's spatiotemporal action range while using an opacity-based entropy loss to prune redundant Gaussians. Combined with FP16 storage and zip delta compression, MEGA achieves approximately 190x and 125x storage reduction on the Technicolor and Neural 3D Video datasets respectively, relative to the original 4DGS, while maintaining comparable rendering quality and real-time speeds.

The paper addresses a practically relevant problem (the massive storage requirements of 4DGS) and the proposed solutions are technically sound in their high-level design. However, several critical issues reduce the overall reliability: (1) the opacity entropy loss is mathematically incomplete (asymmetric, missing the (1-o)log(1-o) term, which undermines the claimed binary-opacity push), (2) quaternion deformation via element-wise multiplication (Eq. 5) is geometrically invalid without explicit normalization, (3) the Neu3DV results show measurable PSNR degradation that is underreported, and (4) several comparative claims (particularly against STG) lack statistical significance testing. Novelty verification is deferred due to unavailability of external literature search in this run.

## Strengths
1. **Clear problem motivation.** The paper identifies a genuine practical limitation of 4DGS — the massive storage requirements (up to 7.79 GB per scene) — which is a real barrier to deployment. The motivation is well-supported with concrete numbers and a clear use case (AR/VR headsets).

2. **Elegant core idea.** The DC-AC color decomposition is conceptually clean and well-executed. Borrowing the DC/AC analogy from electrical engineering to separate steady-state color from temporal-viewpoint variations provides an intuitive framework for understanding the compression strategy.

3. **Strong empirical compression ratios.** The reported 190x and 125x storage reductions on two standard benchmarks are impressive. The per-scene breakdown in Table 4 confirms the method consistently reduces storage by orders of magnitude across all five Technicolor scenes.

4. **Comprehensive ablation study.** Table 3 systematically ablates each component (DAC, deformation, L_opa) across four scenes from two datasets, allowing readers to attribute the contribution of each module. The "w/ DAC+Deformation" row showing increased Gaussian count without L_opa, and the full method achieving dramatic reduction, provides a clear causal picture.

5. **Real-time rendering maintained.** Despite the aggressive compression, rendering speed remains competitive (83 FPS on Technicolor, 77 FPS on Neu3DV), which is important for practical applications.

## Weaknesses
1. **Mathematically incomplete opacity entropy loss (Page 7, Eq. 6).** The opacity entropy loss is defined as L_opa = (1/N) Σ(-o_j log(o_j)), which is only half of the standard binary entropy H(p) = -p log p - (1-p) log(1-p). This asymmetric formulation pushes opacity toward 1 but does not equally penalize intermediate values. The paper's claim that this loss "encourages the spatial opacity of each Gaussian to approach one or zero" is incorrect in its current form; only the "approach one" direction is enforced by the loss. The "approach zero" behavior relies entirely on the separate pruning step, which is a different mechanism.

2. **Geometrically invalid quaternion deformation (Page 6, Eq. 5).** The deformation predictor outputs are applied via element-wise multiplication to the 4D quaternion parameters (q_l, q_r). Element-wise multiplication of quaternions does not correspond to valid rotation composition and does not preserve unit-norm constraints. Unless explicit normalization is applied after each deformation step, the rotation representation becomes geometrically invalid, potentially introducing rendering artifacts. The paper does not mention any such normalization.

3. **Underreported quality regression on Neu3DV (Page 8-9, Table 2).** The text claims "preserving similar visual quality" on the Neu3DV dataset, but average PSNR drops from 31.57 (4DGS) to 31.49 (MEGA), with per-scene degradations of up to -0.92 dB (Flame Steak: 33.19→32.27). This PSNR regression is not statistically evaluated (no variance, no significance test), so the claim of "preserved quality" is not adequately supported.

4. **SOTA claim lacks statistical rigor (Page 8, Sec 4.2).** The paper claims "our MEGA records a 0.22dB gain in visual fidelity over the state-of-the-art (SOTA) Gaussian-based method STG." A 0.22 dB PSNR difference without any confidence intervals or multi-seed variance cannot be established as significant. The term "state-of-the-art" for STG is also used without comparative evaluation across all relevant settings.

5. **Missing technical justification for key design choices.** (a) The stop-gradient operators in Eq. (3)-(4) are introduced without explanation of why geometry gradients must be blocked from the color/deformation predictors. (b) The sigmoid saturation issue when c_dc grows large is not discussed. (c) The 8x per-Gaussian compression ratio (Page 3) is presented as a standalone number without clarifying that the total 190x compression is the product of multiple effects (per-Gaussian compression × Gaussian count reduction × FP16 × zip).

6. **Related work "inapplicability" claim is overstated (Page 4).** The paper asserts that existing 3DGS compression methods "may be inapplicable to or unsuitable for 4DGS" without providing technical reasoning for each method family (pruning, SH distillation, VQ, entropy models). Several of these techniques are general enough to be adapted, and the lack of analysis weakens the gap statement.

## Key Issues
The following five issues are the most critical defects affecting the paper's validity and research value, ranked by severity and impact.

### Issue 1 (Critical): Asymmetric Opacity Entropy Loss Cannot Enforce Binary Opacity

**Location:** Page 6, Eq. (6); Page 7, Eq. (7)
**Severity:** Critical | **Fixability:** Easy

**Evidence:** Eq. (6) defines L_opa = (1/N) Σ(-o_j log(o_j)). The standard binary entropy is H(p) = -p log p - (1-p) log(1-p). The missing term -(1-o_j) log(1-o_j) means the loss only penalizes opacity values that are not close to 1, not values that are not close to 0.

**Impact:** The paper claims this loss "encourages the spatial opacity of each Gaussian to approach one or zero." But the asymmetric loss only pushes toward one. The push toward zero relies on a separate pruning mechanism (threshold-based removal), which is a different operation. This undermines a core claimed contribution of the entropy-constrained deformation.

**Fix:** Replace Eq. (6) with the full binary entropy: L_opa = (1/N) Σ[-o_j log(o_j) - (1-o_j) log(1-o_j)]. Alternatively, explicitly acknowledge that the current formulation is asymmetric and explain why the (1-o)log(1-o) term is intentionally omitted (e.g., to avoid numerical instability for near-zero opacities).

### Issue 2 (Major): Quaternion Deformation via Element-Wise Multiplication

**Location:** Page 6, Eq. (4)-(5)
**Severity:** Major | **Fixability:** Medium

**Evidence:** Eq. (5) transforms rotations as q^{t,v}_l = q_l × m^{t,v}_{ql}, where × denotes element-wise multiplication. Valid quaternion rotations require unit-norm quaternions, and composition requires the Grassmann product, not element-wise multiplication.

**Impact:** Without explicit re-normalization, the rotated quaternions may not represent valid rotations. This introduces a geometric error that potentially degrades rendering quality and creates artifacts that are not attributable to the compression mechanism.

**Fix:** Replace element-wise multiplication with quaternion multiplication (⊗) and add explicit L2 normalization. Alternatively, output delta rotations in the tangent space of the quaternion manifold and apply exponential-map updates.

### Issue 3 (Major): Quality Regression on Neu3DV Underreported

**Location:** Page 8, Table 2; Page 9, Sec 4.2 description
**Severity:** Major | **Fixability:** Easy

**Evidence:** Average PSNR drops from 31.57 (4DGS) to 31.49 (MEGA). Per-scene: Flame Steak 33.19→32.27 (-0.92 dB), Coffee Martini 27.98→27.84 (-0.14 dB), Flame Salmon 28.86→28.48 (-0.38 dB). The text claims "preserving similar visual quality" without reporting these decreases.

**Impact:** A reader relying on the abstract and conclusion could incorrectly assume the method is uniformly lossless, whereas it actually trades off some rendering quality for storage in several scenes. This weakens the credibility of the paper's central claim.

**Fix:** Report the average PSNR delta and per-scene breakdown. Replace "preserving similar visual quality" with "comparable perceptual metrics (LPIPS) with a marginal average PSNR decrease of 0.08 dB."

### Issue 4 (Major): SOTA Claim Without Statistical Significance

**Location:** Page 8, Sec 4.2
**Severity:** Major | **Fixability:** Medium

**Evidence:** The paper claims a 0.22 dB gain over STG as evidence of "state-of-the-art" status. No variance/confidence intervals are reported for any method. The Technicolor per-scene breakdown (Table 4) shows STG outperforming MEGA on Fabien (35.61 vs 34.89) and Painter (35.73 vs 36.73, within 1 dB). Without multi-seed statistics, the significance of the average 0.22 dB advantage cannot be assessed.

**Impact:** If challenged by a reviewer, this claim could undermine confidence in the entire experimental evaluation. Many submissions now require multi-seed variance reporting.

**Fix:** Report results as mean ± std over ≥3 random seeds. Add a paired significance test (e.g., Wilcoxon signed-rank) for the comparison against the strongest baseline.

### Issue 5 (Major): Insufficient Mechanistic Explanation for Participation Ratio Gain

**Location:** Page 3, Sec 1 (Introduction); Page 6, Fig 4
**Severity:** Major | **Fixability:** Medium

**Evidence:** The paper shows participation ratio improving from ~6% to ~75% (Fig 4a) but does not explain the mechanism. The deformation predictor modifies µ_4D, s_4D, q_l, q_r but not explicitly the temporal decay width W or the opacity σ(t). How does changing the 4D geometry increase the temporal window?

**Impact:** Without mechanistic explanation, the dramatic participation gain appears as a black-box result rather than a principled design. This reduces the paper's scientific value.

**Fix:** Add an analysis paragraph explaining whether the deformation indirectly affects the temporal slicing (by changing V/W in µ_3D(t)) or whether the effect is achieved through post-slicing geometry changes that keep more Gaussians above the σ(t) > 0.05 threshold.

## Actionable Suggestions
### S1 (Must): Correct the Opacity Entropy Loss
**Location:** Page 6, Eq. (6); Page 7, Eq. (7)
**Action:** Replace the asymmetric loss with the full binary entropy.
**Revised Eq. (6):** 
$$L_{\text{opa}} = \frac{1}{N}\sum_{j=1}^{N}\bigl[-o_j\log(o_j) - (1-o_j)\log(1-o_j)\bigr]$$
Alternatively, if the asymmetric form is intentional, add an explicit justification: "We omit the -(1-o)log(1-o) term because low-opacity Gaussians are removed by the pruning step, and the asymmetric loss focuses optimization on keeping high-opacity Gaussians at peak contribution."

### S2 (Must): Fix Quaternion Deformation
**Location:** Page 6, Eq. (4)-(5)
**Action:** Replace Eq. (5) with proper quaternion operations.
**Revised Eq. (5):** 
$$\mu^{t,v}_{4D} = \mu_{4D} \odot m^{t,v}_{\mu_{4D}}, \quad s^{t,v}_{4D} = s_{4D} \odot m^{t,v}_{s_{4D}}$$
$$q^{t,v}_l = \text{normalize}\bigl(q_l \otimes m^{t,v}_{q_l}\bigr), \quad q^{t,v}_r = \text{normalize}\bigl(q_r \otimes m^{t,v}_{q_r}\bigr)$$
where $\otimes$ is quaternion multiplication and $\odot$ is element-wise multiplication. Add a sentence confirming that the output quaternions are L2-normalized before use in the covariance matrix.

### S3 (Must): Report Quality Trade-offs Honestly
**Location:** Abstract, Page 8 Sec 4.2, Page 10 Conclusion
**Action:** 
- In the Abstract, replace "maintains comparable rendering speeds and scene representation quality" with "maintains comparable rendering speeds; quality is preserved on LPIPS metrics though marginal PSNR decreases are observed on Neu3DV."
- In Sec 4.2, add a sentence: "On Neu3DV, average PSNR is 31.49 dB compared to 4DGS's 31.57 dB (-0.08 dB), with per-scene variation from +0.35 dB (Cook Spinach) to -0.92 dB (Flame Steak)."
- In the Conclusion, replace "more than a hundredfold reduction...while maintaining high-quality reconstruction" with "more than a hundredfold reduction; on Technicolor this is achieved with improved PSNR, while on Neu3DV comparable LPIPS is maintained with a marginal PSNR trade-off."

### S4 (Must): Add Statistical Significance Reporting
**Location:** Page 8, Sec 4.2, Table 1, Table 2
**Action:** Report all main result metrics as mean ± std over at least 3 random seeds. Add a significance test (e.g., paired t-test or Wilcoxon signed-rank) for the primary comparison (MEGA vs 4DGS and MEGA vs STG). In the text, qualify the STG comparison: "MEGA achieves a 0.22 dB higher average PSNR than STG, though this difference is within one standard deviation and further significance testing is needed."

### S5 (Nice-to-have): Clarify Participation Ratio Mechanism
**Location:** Page 3 (Introduction), Page 6 (Fig 4)
**Action:** Add an analysis paragraph explaining how the deformation predictor increases the participation ratio. Specifically, clarify whether the effect comes from: (a) modifying V/W in the linear motion term µ_3D(t), (b) changing the 4D positions to increase the temporal decay width σ(t), or (c) making Gaussians larger in 3D space so they remain visible even with low temporal opacity. Provide a mathematical derivation or at least an empirical analysis.

### S6 (Nice-to-have): Improve Notation Clarity
**Location:** Page 4, Eq. (1)-(2); Page 5, Eq. (3)
**Action:** 
- Explicitly state V ∈ R^{3×1} and W ∈ R after Eq. (1).
- Define the final rendered opacity as o · σ(t) where o is the learned spatial opacity.
- Explain the stop-gradient operator rationale in Eq. (3): "sg(·) prevents the AC color predictor from affecting geometry optimization through gradient feedback, which we found empirically stabilizes training."

### S7 (Nice-to-have): Bound the "8× Compression" Claim
**Location:** Page 3
**Action:** Add a clarifying sentence: "This 8× refers to the per-Gaussian attribute storage ratio. The total model compression of 190× is the combined effect of per-Gaussian compression, Gaussian count reduction (via deformation and pruning), half-precision storage, and lossless zip compression."

## Storyline Options + Writing Outlines
### Abstract Outline

The current Abstract is functional but ends with hype ("setting a new standard"). Recommended revision:

**S1 (Problem):** "4D Gaussian Splatting (4DGS) achieves high-fidelity dynamic scene rendering but requires millions of Gaussians, each with 161 parameters, leading to storage costs of several GB per scene."

**S2 (Gap):** "The 4D spherical harmonics coefficients (144 of the 161 parameters) are the dominant storage factor and exhibit considerable redundancy. Additionally, each Gaussian's limited temporal action range forces the model to use excessive numbers of Gaussians."

**S3 (Method):** "We propose a memory-efficient framework (MEGA) with two key innovations: (a) a DC-AC color decomposition that replaces 4D SH coefficients with a 3-parameter per-Gaussian DC component and a lightweight MLP-based color predictor, and (b) an entropy-constrained Gaussian deformation that expands the spatiotemporal range of each Gaussian while pruning redundancies via opacity-based regularization."

**S4 (Results):** "On the Technicolor and Neural 3D Video datasets, MEGA achieves approximately 190x and 125x storage reduction respectively compared to 4DGS, while maintaining real-time rendering speeds (77-83 FPS). Quality is preserved on LPIPS metrics, with marginal PSNR variation across scenes."

**S5 (Implication, bounded):** "This work demonstrates that careful per-Gaussian color compression combined with deformation-based pruning is a promising direction for compact dynamic scene representation."

### Introduction Outline

**Current storyline diagnosis:** The introduction has four paragraphs: (P1) NeRF→3DGS→4DGS evolution, (P2) storage problem, (P3) MEGA solution, (P4) contributions. The main weakness is that P1 is purely descriptive and does not foreshadow the storage problem, creating a discontinuity at P2's "However."

**Recommended storyline (Candidate A — Problem-first):**

**P1 (Stakes & Gap):** "Dynamic scene reconstruction from multi-view video is critical for VR/AR applications. 4D Gaussian Splatting has emerged as a leading approach due to its real-time rendering and photorealistic quality. However, its practical deployment is severely limited by massive storage requirements: a single scene can exceed 7 GB, making it impractical for resource-constrained devices. The primary culprit is the 4D spherical harmonics representation, which consumes 144 out of 161 parameters per Gaussian and contains significant redundancy."

**P2 (Prior attempts & remaining gap):** "While 3DGS compression has been extensively studied through pruning, SH distillation, and quantization, these methods are designed for static scenes and do not address the unique challenges of 4DGS: the temporal dimension in SH coefficients and the low temporal utilization of individual Gaussians. Direct application of grid-based SH replacement causes severe quality degradation (Table 3)."

**P3 (Proposed solution):** [Current text, largely acceptable but tighten wording.]

**P4 (Contributions):** [Current text, but remove "among the first" and rephrase as technical contributions.]

**Alternative Candidate B (Insight-first):** Lead with the DC/AC analogy as the motivational hook, then derive the problem from that perspective. Risk: readers may not understand the 4DGS context before seeing the insight.

**Selected recommendation:** Use Candidate A (Problem-first), which follows standard ICLR narrative conventions and ensures readers understand the stakes before encountering technical details.

### Title Suggestion

Current: "MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes"
Suggested: "MEGA: Compressing 4D Gaussian Splatting via DC-AC Color Decomposition and Entropy-Constrained Deformation"
Rationale: Adds specificity about the two core technical contributions.

### Key Paragraph Revision (Introduction P1-P2 transition)

**Current:** P1 ends with "achieving photorealistic visual quality." P2 starts with "However, 4DGS requires millions of Gaussians..."

**Mentor Revised Version for P1 ending:** "By directly optimizing a collection of 4D Gaussians, 4DGS effectively captures both static and dynamic scene elements, achieving photorealistic visual quality at real-time frame rates. However, this high fidelity comes at a steep storage cost: a single scene can require over 13 million Gaussians and 7 GB of memory, arising from the high-dimensional per-Gaussian attributes—particularly the 4D spherical harmonics coefficients with 144 parameters each."

## Priority Revision Plan
### P0 (Must-do before resubmission)

| Priority | Item | Location | Effort | Impact |
|----------|------|----------|--------|--------|
| P0 | Fix asymmetric opacity entropy loss (Eq. 6) | Page 6-7 | 1 hour | Critical: core claim validity |
| P0 | Fix quaternion deformation (Eq. 5) | Page 6 | 2 hours | Critical: geometric correctness |
| P0 | Revise Neu3DV quality claim | Abstract, Sec 4.2, Conclusion | 1 hour | Major: factual accuracy |
| P0 | Add multi-seed variance to main tables | Table 1, Table 2 | 8 hours | Major: statistical rigor |

### P1 (Strongly recommended)

| Priority | Item | Location | Effort | Impact |
|----------|------|----------|--------|--------|
| P1 | Add participation ratio mechanism explanation | Page 3, Fig 4 | 4 hours | Major: mechanistic clarity |
| P1 | Revise Related Work "inapplicable" claim | Page 4 | 2 hours | Major: literature positioning |
| P1 | Clarify 8x vs 190x compression accounting | Page 3 | 1 hour | Minor: reader clarity |
| P1 | Remove "new benchmark" from Conclusion | Page 10 | 0.5 hour | Minor: hype reduction |
| P1 | Add stop-gradient rationale for Eq. (3)-(4) | Page 5-6 | 1 hour | Minor: reproducibility |

### P2 (Quality improvements)

| Priority | Item | Location | Effort | Impact |
|----------|------|----------|--------|--------|
| P2 | Add dimension annotations for V, W | Page 4, Eq. (1) | 0.5 hour | Minor: notation clarity |
| P2 | Define opacity composition rule (o·σ(t)) | Page 4 | 0.5 hour | Minor: notation clarity |
| P2 | Add title with technical specificity | Page 1 | 0.5 hour | Minor: discoverability |
| P2 | Restructure introduction P1-P2 transition | Page 2 | 2 hours | Minor: narrative flow |

### Revision Sequence

1. **Fix mathematical errors first (P0):** Eq. (6) entropy loss and Eq. (5) quaternion deformation. These are correctness issues that could invalidate core claims if challenged.

2. **Revise claims and reporting (P0):** Neu3DV quality regression, multi-seed variance, STG SOTA comparison. These affect the paper's credibility with reviewers.

3. **Add missing analysis (P1):** Participation ratio mechanism, Related Work justification.

4. **Polish narrative (P1-P2):** Remove hype language ("new benchmark"), improve transitions, clarify notation.

### Expected Impact After Full Revision

- **Validity risk:** Reduced from high to low after P0 fixes (entropy loss, quaternion deformation, statistical rigor)
- **Reviewer confidence:** Significantly improved by honest reporting of quality trade-offs and variance
- **Research value:** Core contribution remains strong; revisions primarily improve defensibility and reproducibility

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main Technicolor comparison (Table 1) | 5 scenes, full-res 2048×1088, 50 frames | PSNR, DSSIM1/2, LPIPS, FPS, Storage | MEGA: 33.57 PSNR, 32.45 MB; 4DGS: 32.07 PSNR, 6107 MB | C1 (DAC), C2 (deformation), C3 (compression) | No variance/seeds; DSSIM inconsistency across methods |
| E2 | Main Neu3DV comparison (Table 2) | 6 scenes, half-res, 300 frames | Same as E1 | MEGA: 31.49 PSNR, 25.05 MB; 4DGS: 31.57 PSNR, 3128 MB | C3 (compression ratio) | PSNR regression not reported; per-scene variance large |
| E3 | Per-scene breakdown (Table 4, Appendix) | Same as E1+E2, per-scene | Same as E1 | Confirms consistent compression; speed varies per scene | C3 | Trains scene: MEGA slower than 4DGS (28 vs 40 FPS) |
| E4 | Ablation: DAC vs grid (Table 3) | Birthday, Fabien, Flame Steak, Sear Steak | PSNR, DSSIM1, N, Params | DAC outperforms grid-based SH replacement; deformation alone increases N | C1, C2 | Limited to 4 scenes; no DSSIM2/LPIPS |
| E5 | Ablation: DAC+Deformation+L_opa (Table 3) | Same as E4 | Same as E4 | Full method: 0.91M Gs, 18.48M params (Birthday); 4DGS: 13M Gs, 2093M params | C2 | Flame Steak full method PSNR drops (33.19→32.27) |
| E6 | Participation ratio analysis (Fig 4a) | Birthday scene | Participation % vs time step | 4DGS: ~6%; MEGA: ~75% | C2 | Only 1 scene; no per-scene breakdown |
| E7 | Gaussian count during training (Fig 4b) | Birthday scene | #Gaussians vs iterations | L_opa suppresses uncontrolled densification | C2 | Only 1 scene |
| E8 | Qualitative comparison (Fig 5-7, Appendix) | Theater, Painter, Birthday, Trains, Cut Roasted Beef, Sear Steak | Subjective visual quality | MEGA preserves details, fewer artifacts | C1, C2, C3 | No user study; single-frame examples |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's primary novel knowledge is that (a) a simple 3-parameter DC component + small MLP can effectively replace 144-parameter 4D SH for color, and (b) deformation-based temporal range expansion can dramatically increase Gaussian utilization. Both findings are empirically demonstrated but the second lacks mechanistic explanation (see Key Issue 5).

2. **Reproducibility gap:** Missing variance/seeds, incomplete opacity definition (o·σ(t) not specified), and the unresolved quaternion deformation issue (Eq. 5) limit reproducibility.

3. **Impact-on-practice gap:** The paper establishes strong compression ratios but does not analyze runtime memory (peak GPU memory), deployment constraints (mobile/edge), or rendering latency distribution. The Trains scene showing lower FPS than 4DGS suggests the speed advantage is not universal.

### Proposed Research Experiments

#### P0 Experiments (Must-add before resubmission)

| Exp | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-----|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| EX1 | C3 (quality preservation) | MEGA preserves quality within 1σ of 4DGS | Run 4DGS and MEGA with 5 seeds on 2 Technicolor + 2 Neu3DV scenes | Same seeds, same hardware | PSNR mean±std, LPIPS, significance (p<0.05) | No significant difference at p<0.05 | 16 GPU hours | Statistical rigor for main claim |
| EX2 | C2 (deformation mechanism) | Deformation increases temporal window W or changes V/W ratio | Compare σ(t) distribution before/after deformation on Birthday | Fixed Gaussian count | Histogram of W values, temporal opacity profiles | Measurable shift in W distribution | 4 GPU hours | Mechanistic understanding |
| EX3 | C1 (DAC vs SH) | DAC quality comparable to 4DGS at matched Gaussian count | Train MEGA (DAC only, no deformation/pruning) vs 4DGS with same N | Same N, same optimizer | PSNR, LPIPS | MEGA within 0.5 dB of 4DGS at same N | 8 GPU hours | Isolate DAC contribution |

#### P1 Experiments (Strongly recommended)

| Exp | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-----|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| EX4 | C3 (generalization) | MEGA compresses other dynamic NeRF methods | Apply DAC+L_opa to K-Planes or HexPlane | Original method as baseline | Storage, PSNR | Comparable quality with 50%+ storage reduction | 12 GPU hours | Broader impact |
| EX5 | C2 (opacity distribution) | L_opa produces bimodal opacity distribution | Plot opacity histogram of MEGA vs w/o L_opa | Same scene, same N | Opacity histogram entropy | Bimodal separation in opacity values | 2 GPU hours | Validate "binary states" claim |
| EX6 | C3 (deployment) | MEGA fits within mobile GPU memory | Measure peak GPU memory at inference | 4DGS as baseline | Peak GPU memory, FPS | <2 GB peak memory at 1080p | 4 GPU hours | Practical relevance |

#### P2 Experiments (Quality improvements)

| Exp | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-----|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| EX7 | C2 (robustness) | Deformation predictor generalizes to unseen timestamps | Hold out 20% of frames during training, evaluate on held-out | Full-training baseline | PSNR on held-out vs full | <1 dB drop on held-out | 8 GPU hours | Temporal generalization evidence |
| EX8 | C1 (color ablation) | AC predictor redundancy varies by scene | Replace AC MLP with linear layer | Full MLP baseline | PSNR, Params | Identify scenes where AC MLP is necessary | 4 GPU hours | Design insight |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5 / 10

**Rationale:** The paper addresses a genuine and well-motivated problem (4DGS storage) with a technically clean core idea (DC-AC color decomposition). The empirical results demonstrate substantial compression ratios on standard benchmarks. However, the score is reduced by: (a) two mathematical correctness issues (asymmetric entropy loss, geometrically invalid quaternion deformation) that directly affect core claims, (b) underreported quality regression on the Neu3DV dataset that gives a misleading impression of lossless compression, (c) lack of statistical significance testing for comparative claims, and (d) insufficient mechanistic explanation for the key participation-ratio improvement. Novelty cannot be fully assessed due to the unavailability of external literature search in this run, so novelty-based scoring is deferred pending manual verification. The paper's research value as a compression technique is clear, but the current presentation and mathematical rigor issues prevent a higher score.

**Post-Revision Target:** [6.5, 7.5] / 10

**Conditional on:** (1) Correcting the asymmetric entropy loss to full binary entropy, (2) fixing the quaternion deformation with proper normalization, (3) honestly reporting Neu3DV quality trade-offs, (4) adding multi-seed variance and significance tests, and (5) providing mechanistic analysis for the participation ratio improvement. If all P0 and P1 items in the Priority Revision Plan are satisfactorily addressed, the paper could achieve a score in the 6.5-7.5 range, reflecting a solid contribution with some remaining minor limitations.