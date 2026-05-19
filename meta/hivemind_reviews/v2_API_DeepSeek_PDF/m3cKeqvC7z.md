## Summary
# Final Review Report

## Summary

This paper presents a systematic empirical investigation of Mamba-based architectures for 3D volumetric medical image segmentation. Rather than proposing a single novel architecture, the authors design controlled experiments to isolate three design factors: (1) whether Mamba layers can replace Transformer layers in a U-shaped encoder-decoder under matched conditions, (2) whether Mamba's long-range dependency modeling enhances multi-scale representation learning, and (3) whether complex multi-directional scanning strategies are necessary for 3D medical data. The study evaluates models on three public benchmarks—AMOS (15 abdominal organs), TotalSegmentator (117 structures), and BraTS 2021 (brain tumor subregions)—using Dice score and FLOPs as primary metrics.

The main findings are: (a) UlikeMamba (Mamba-based U-Net) achieves competitive or better Dice scores than UlikeTrans (Transformer-based U-Net) at lower computational cost, especially when 1D depthwise convolutions are replaced with 3D convolutions; (b) a proposed multi-scale Mamba block (MSv4) yields the largest gains on TotalSeg (the most complex benchmark); and (c) Tri-scan (three-direction scanning) outperforms single-scan and dual-scan strategies but at increased computational cost. The integrated model (UlikeMamba 3dMT) shows favorable accuracy-to-efficiency trade-offs against nnUNet, CoTr, UNETR, SwinUNETR, and U-Mamba on two of three datasets.

**Strengths:** The controlled experimental design is a methodological improvement over prior work that mixes architectural changes. The three-part investigation structure is clear and reader-friendly. Evaluation on three large, diverse benchmarks adds credibility.

**Core weaknesses:** (1) No statistical variance reported—all results are single-run Dice scores, making it impossible to assess significance of observed gaps. (2) The final model comparison omits TotalSeg (the most challenging dataset), leaving the "new benchmark" claim only partially supported. (3) Tri-scan's advantage is confounded with increased model capacity. (4) Several causal claims about mechanism (e.g., "3D DWConv preserves spatial coherence") lack diagnostic evidence. (5) Novelty claims cannot be fully verified without external literature comparison (deferred to manual verification).

## Strengths
**S1. Systematic controlled-experiment design.** The paper's main strength is its three-part analytical framework that isolates architectural factors (Mamba vs. Transformer backbone, multi-scale fusion design, scanning strategy) under a controlled U-shaped backbone. This is a meaningful methodological improvement over prior Mamba-based segmentation papers, which typically combine multiple modifications without isolating their individual contributions. The study design enables cleaner attribution of observed gains to specific design choices.

**S2. Large-scale, diverse evaluation.** The use of three public benchmarks (AMOS, TotalSegmentator, BraTS) covering different anatomical regions (abdomen, whole-body, brain), modalities (CT, multi-sequence MRI), and task complexities (3 to 117 classes) provides broad empirical coverage. The inclusion of TotalSegmentator (1,228 scans, 117 structures) as a challenging multi-class benchmark is particularly valuable for testing the generalizability of architectural findings.

**S3. Clear, well-structured presentation.** The paper is organized around three explicit research questions, each with a dedicated analysis section containing experimental design, results, and interpretation. Figures and tables are informative and well-labeled. The supplementary material provides detailed architectural configurations that support reproducibility.

**S4. Practical comparative framing.** By building both Mamba-based (UlikeMamba) and Transformer-based (UlikeTrans) variants from the same U-shaped template and integrating both into the nnUNet framework, the paper provides a fairer comparison than most prior work. The inclusion of computational efficiency metrics (FLOPs, parameters) alongside accuracy metrics is useful for practitioners.

**S5. Honest acknowledgment of trade-offs.** The paper acknowledges that simpler scanning methods often suffice and that Tri-scan incurs higher computational costs. This balanced reporting is commendable and contrasts with the more promotional tone sometimes found in architecture papers.

## Weaknesses
**W1. No statistical variance reporting (Critical).** All quantitative results in Tables 1-3 report single Dice scores without standard deviations, confidence intervals, or significance tests. The observed differences between models are often small (e.g., Tri-scan 89.77 vs. Single-scan 89.45 on AMOS, a 0.32-point gap). Without multi-seed variance estimation, the reader cannot distinguish systematic improvement from random run-to-run variation. This undermines the reliability of all comparative claims.

**W2. Missing final comparison on TotalSeg (Major).** Section 7 evaluates the integrated UlikeMamba 3dMT only on AMOS and BraTS. TotalSeg—the most challenging benchmark with 117 classes—is excluded from the final comparison despite showing the largest MSv4 improvements in earlier experiments. This omission weakens the headline claim that the model "sets a new benchmark."

**W3. Tri-scan confounded with capacity (Major).** Tri-scan uses three separate SSM layers (one per scanning direction) versus Single-scan's one SSM layer. The observed gains (+0.48 average Dice) may be partly or entirely due to increased model capacity rather than multi-directional scanning. No matched-capacity control is provided.

**W4. Causal mechanism claims without diagnostic evidence (Major).** The paper asserts that DWConv 3D "preserves spatial coherence" and that MSv4 "excels at capturing multi-scale features," but these are mechanistic claims supported only by final accuracy numbers. No internal representation analysis (feature visualization, spatial consistency metrics, or controlled ablations) is provided to validate the proposed explanations.

**W5. Limited novelty assessment without external literature verification.** Due to retrieval constraints (Retrieval-Disabled Mode), novelty and positioning claims relative to the broader literature cannot be independently verified. The paper's claim that prior work "primarily demonstrates Mamba's feasibility without fully exploring its broader potential" needs external validation. Manual literature review is required to determine whether the specific analytical dimensions examined here are indeed unexplored.

**W6. Overclaiming in abstract and contribution framing.** The abstract uses hype language ("transformative force," "sets a new benchmark") that exceeds the evidence provided. Contribution 3 is a performance-only claim ("sets a new benchmark"), which the review guidelines advise against treating as a standalone contribution. The paper's genuine value is its systematic analysis; the SOTA framing is a distraction.

**W7. Related Work organized as a flat list.** Section 2 provides one-sentence summaries of 12+ papers grouped into two coarse categories (hybrid/pure), without explicit comparison axes or clear identification of the specific gaps that each prior work leaves open.

**W8. No limitations section.** The paper lacks a dedicated limitations paragraph or section. Critical limitations—single-run results, dataset scope (CT/MRI only), Tri-scan's computational overhead, and unknown generalization to other modalities—are not self-acknowledged.

## Key Issues
The following five issues are ranked by combined severity, research-value impact, and validity risk. These represent the most critical barriers to publication in the current form.

### Issue 1: Single-run results without statistical grounding (Severity: Critical)
**Location:** Tables 1, 2, 3; Sections 4.3, 5.2, 6.2
**Evidence:** All reported Dice scores are single values without standard deviation or confidence intervals. Comparisons of ~0.3–1.0 Dice points (e.g., Tri-scan vs Single-scan on AMOS: 89.77 vs 89.45) are presented as definitive advantages.
**Root cause:** The paper does not report performing multi-seed experiments or significance tests.
**Risk:** Core comparative claims (Mamba > Transformer, MSv4 > other schemes, Tri-scan > Single-scan) may not be statistically significant. The entire empirical contribution could be undermined if gains are within noise.
**Fix:** Re-run key comparisons with ≥3 seeds, report mean ± std, and apply paired significance tests vs the strongest baseline. If compute constraints prevent full re-runs, explicitly state this limitation and use cautious comparative language.

### Issue 2: TotalSeg excluded from final model comparison (Severity: Major)
**Location:** Section 7, Figure 4, Page 10
**Evidence:** UlikeMamba 3dMT results shown only for AMOS and BraTS. No TotalSeg comparison despite TotalSeg being the paper's most complex and most-improved benchmark.
**Root cause:** Unknown—possibly computational constraints or incomplete experimentation.
**Risk:** The central "new benchmark" claim is supported by only 2/3 benchmark datasets. This gap is especially conspicuous because TotalSeg showed the largest gains for the proposed MSv4 and Tri-scan components.
**Fix:** Add TotalSeg results to the final comparison. At minimum, report UlikeMamba 3dMT Dice on TotalSeg and compare to the strongest baseline from Table 2. If TotalSeg evaluation is infeasible, clearly scope the "new benchmark" claim to only AMOS and BraTS.

### Issue 3: Tri-scan advantage confounded with model capacity (Severity: Major)
**Location:** Section 6, Table 3, Page 8-9
**Evidence:** Tri-scan uses 3 separate SSM layers (one per direction) versus Single-scan's 1 SSM layer. Parameters increase from 24.30M to 26.38M. No matched-capacity Single-scan baseline is provided.
**Root cause:** The experimental design does not control for the confound between scanning direction multiplicity and parameter count.
**Risk:** The claimed benefit of multi-directional scanning may be an artifact of increased capacity. The paper's analytical conclusion ("Tri-scan preserves comprehensive spatial relationships") is not supported without a controlled ablation.
**Fix:** Add a matched-capacity Single-scan control (expand hidden dimension to match Tri-scan's total SSM parameters) or a "pseudo Tri-scan" (same direction through 3 separate SSM layers). Report whether the performance advantage persists.

### Issue 4: Causal mechanism claims without diagnostic evidence (Severity: Major)
**Location:** Sections 4.3 (DWConv 1D vs 3D), 5.2 (MSv4 multi-scale), Page 5-7
**Evidence:** The paper claims DWConv 3D "preserves spatial coherence" and MSv4 "excels at capturing both fine-grained details and global context." These are mechanistic claims supported only by final accuracy metrics, not by internal representation analysis.
**Root cause:** The study is designed as a black-box comparison without intermediate feature analysis. The claimed internal mechanisms are post-hoc explanations.
**Risk:** Alternative explanations (capacity increase, regularization, gradient dynamics) could account for the observed gains. The paper's analytical contribution relies on the validity of these mechanism explanations.
**Fix:** Either (a) add diagnostic evidence (feature visualization, spatial autocorrelation analysis, or a control experiment isolating the mechanism), or (b) replace causal language with correlational statements (e.g., "Mamba 3d achieves higher Dice, consistent with improved spatial modeling").

### Issue 5: Abstract and contribution overclaiming (Severity: Major)
**Location:** Abstract, Contribution 3, Page 1-2
**Evidence:** Abstract calls Mamba "a transformative force" and states the model "sets a new benchmark." Contribution 3 is a performance-only SOTA claim.
**Root cause:** The paper attempts to position itself as a breakthrough architecture paper when its true strength is a systematic empirical analysis.
**Risk:** The overclaiming invites reviewer skepticism and sets an evidence bar (multi-run statistics, cross-validation, deployment metrics) that the paper does not meet. This could lead to rejection despite the valid analytical contributions.
**Fix:** Rewrite abstract and contributions to reflect the paper's analytical nature. Replace "sets a new benchmark" with "demonstrates competitive accuracy-to-efficiency ratios through systematic analysis of Mamba design choices." Remove "transformative force" and similar promotional language.

## Actionable Suggestions
### Suggestion 1: Add multi-seed variance and significance testing (Must)
**Target:** Tables 1, 2, 3; Sections 4-6
**Action:** Re-run all baseline comparisons with at least 3 random seeds. Report results as mean ± std in all tables. Add a note in each table caption: "Results reported as mean ± std over 3 runs." For the main comparisons (UlikeTrans SRA vs UlikeMamba 3d, MSv4 vs baselines, Tri-scan vs Single-scan), perform a paired t-test or Mann-Whitney U test and mark statistically significant improvements ($p<0.05$) with an asterisk.
**Expected benefit:** All comparative claims become interpretable and scientifically defensible. Without this change, the paper's core empirical evidence is at risk of being dismissed.
**Cost:** Moderate. Each model takes 250K iterations × 3 seeds = 750K iterations per condition. Priority: P0.

### Suggestion 2: Complete the final comparison with TotalSeg (Must)
**Target:** Section 7, Figure 4, Page 10
**Action:** Evaluate UlikeMamba 3dMT on TotalSeg test set and add results to Figure 4 or a companion table. At minimum, compare against the best TotalSeg baseline from Table 2 (UlikeMamba 3d with MSv4: 84.50 Dice). If evaluating all baselines on TotalSeg is too expensive, report at least UlikeMamba 3dMT's TotalSeg Dice with a note that the gain over the best baseline is preliminary.
**Expected benefit:** Central claim becomes fully supported across all three benchmark datasets. Eliminates a conspicuous evidence gap.
**Cost:** High if all baselines need re-evaluation; Low if only UlikeMamba 3dMT is run. Priority: P0.

### Suggestion 3: Add capacity-matched control for Tri-scan (Must)
**Target:** Section 6, Table 3
**Action:** Design a "Single-scan-large" variant where single-direction SSM hidden size is increased so total SSM parameters approximately match Tri-scan (target: ~26.4M parameters). Alternatively, create a "pseudo Tri-scan" that runs the same direction through three separate SSM layers without changing scanning direction. Report results on the same three datasets.
**Expected benefit:** Resolves the capacity confound and supports or refutes the claim that multi-directional scanning per se is beneficial.
**Cost:** Moderate (two additional runs per dataset). Priority: P1 (before Section 6 can be published).

### Suggestion 4: Provide diagnostic evidence for mechanism claims (Must)
**Target:** Sections 4.3 and 5.2
**Action:** For the DWConv 1D vs 3D comparison, add a simple diagnostic: compute the spatial autocorrelation of intermediate feature maps (e.g., average pairwise correlation between a voxel and its 3×3×3 neighborhood) for both Mamba 1d and Mamba 3d. If Mamba 3d produces higher local autocorrelation, the "spatial coherence preservation" claim gains direct evidence. For MSv4, compute per-class Dice on TotalSeg for small (<1000 voxels) vs large (>10000 voxels) structures and show that MSv4 primarily improves the small-structure Dice.
**Expected benefit:** Transforms post-hoc speculation into evidence-backed mechanism analysis.
**Cost:** Low. Priority: P1.

### Suggestion 5: Rewrite abstract and contribution claims (Must)
**Target:** Abstract, Introduction (Page 1-2)
**Action:** Replace promotional language ("transformative force," "sets a new benchmark") with bounded claims. Rewrite Contribution 3 to emphasize the validation insight rather than SOTA positioning. (See the detailed rewrite in Page 1-2 annotations.)
**Expected benefit:** Aligns the paper's claims with its evidence. Reduces reviewer skepticism about overclaiming.
**Cost:** Low (text editing only). Priority: P0.

### Suggestion 6: Restructure Related Work as comparison table (Nice-to-have)
**Target:** Section 2, Page 3
**Action:** Replace the flat paper-by-paper list with a structured comparison table organized by axes: (1) scanning strategy, (2) convolution dimension, (3) multi-scale handling, (4) benchmarks evaluated, (5) controls vs Transformer baseline. Add a column showing what each prior work analyzed versus what remains open.
**Expected benefit:** Immediately communicates the gap this paper fills. Strengthens novelty positioning.
**Cost:** Low. Priority: P2.

### Suggestion 7: Add dedicated Limitations section (Nice-to-have)
**Target:** Conclusion, Page 10
**Action:** Insert a "Limitations" paragraph after the main conclusion. Address: (a) single-run results, (b) dataset scope (CT/MRI only; no ultrasound, PET, or low-data regimes), (c) Tri-scan computational overhead, (d) untested generalization to out-of-distribution data, (e) reliance on nnUNet pipeline.
**Expected benefit:** Improves scientific rigor and reviewer confidence. (See detailed rewrite in the Page 10 Conclusion annotation.)
**Cost:** Low. Priority: P1.

### Suggestion 8: Clarify flattening strategy and scanning details (Nice-to-have)
**Target:** Section 4.1 (Mamba-based network), Page 4
**Action:** Specify the flattening order used before SSM processing (e.g., depth-major, then height, then width). Clarify whether Tri-scan uses a different flattening order per direction or simply permutes the axes before the same flattening procedure.
**Expected benefit:** Improves reproducibility.
**Cost:** Low. Priority: P2.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current Introduction (Page 1-2) follows this arc:
1. P1: Volumetric segmentation definition + CNN limitation + Transformer alternative
2. P2: Mamba SSM introduction + prior Mamba vision works + multi-scan strategies
3. P3: Prior Mamba segmentation works (U-Mamba, SegMamba, SwinUMamba) + gap statement
4. P4-P6: Three research questions previewed as bullet-point-style paragraphs
5. P7: Three contribution claims

**Identified issues:** (a) P2 conflates Mamba's general vision adoption (ViM, VMamba) with medical image segmentation—these could be separated. (b) The gap statement in P3 ("primarily demonstrate Mamba's feasibility") is too vague—it does not specify what analysis dimensions are missing. (c) The three research questions are previewed in the introduction but also appear as section headings—some redundancy. (d) Contribution 3 is a performance-only SOTA claim.

### Recommended Storyline (Option A — Analytical Focus)

**Target:** Emphasize the paper's strength as a systematic empirical analysis, not a new architecture.

**Abstract Outline (S1-S5):**
- **S1 (Problem):** 3D medical image segmentation requires long-range dependency modeling, where Transformers are effective but computationally heavy.
- **S2 (Gap):** Mamba-based State Space Models offer linear-complexity alternatives, but prior work integrates Mamba into specific hybrid architectures without isolating which design factors drive performance.
- **S3 (What we do):** We conduct a controlled three-part investigation isolating (i) Mamba vs. Transformer backbone, (ii) multi-scale fusion design, and (iii) scanning strategy under matched U-shaped encoder-decoder conditions.
- **S4 (Key results):** Mamba with 3D depthwise convolutions matches or exceeds Transformer accuracy at lower FLOPs. A multi-scale Mamba block (MSv4) yields largest gains on complex multi-class segmentation. Tri-scan provides marginal improvements over single-scan at 15% higher cost.
- **S5 (Significance bounded):** These findings provide evidence-based guidance for deploying Mamba in volumetric segmentation and identify specific design choices that matter most.

**Introduction Outline (P1-P5):**
- **P1 (Stakes):** 3D medical segmentation context, why long-range dependencies matter.
- **P2 (CNN → Transformer evolution):** CNN limitations, Transformer promise, Transformer's computational barrier for 3D data.
- **P3 (Mamba as alternative + prior work gap):** Introduce SSM/Mamba as linear-complexity alternative. Review prior Mamba segmentation works (U-Mamba, SegMamba, SwinUMamba). Explicit gap: "These works validate feasibility but combine Mamba with task-specific modifications, leaving three open questions: ..."
- **P4 (Three questions + approach):** List the three questions. State: "To answer these, we build matched U-shaped Mamba and Transformer baselines, systematically vary DWConv dimension, multi-scale fusion, and scanning strategy, and evaluate on three public benchmarks."
- **P5 (Contributions):** Three analytical contributions (not performance claims). End with: "Our findings provide a design foundation for future Mamba-based volumetric segmentation research."

### Alternative Storyline (Option B — Architecture-Focused)

If the authors prefer to retain a stronger architecture-focus, restructure as:
- Title: "UlikeMamba: Systematic Analysis and Design of Mamba Networks for 3D Medical Image Segmentation"
- P1: Problem + CNN/Transformer context
- P2: Introduce Mamba + identify unresolved design questions
- P3: Present UlikeMamba architecture as a testbed for studying these questions
- P4: Three investigations (as now)
- Contribution list stays analytical, with Contribution 3 framed as "Cumulative validation of identified design principles"

### Recommended Title Revision

Current: "What Can Mamba Do for 3D Volumetric Medical Image Segmentation?"

Problem: The title is engaging but vague—it does not communicate the paper's analytical contribution.

Better options:
- Option A (analytical): "Mamba vs. Transformer for 3D Medical Segmentation: A Systematic Analysis of Architecture Design Choices"
- Option B (architecture + analysis): "UlikeMamba: Systematic Analysis and Design of Mamba Networks for 3D Medical Image Segmentation"
- Option C (shorter): "Three Questions for Mamba in 3D Medical Image Segmentation"

### Three Alignment Checks

| Check | Current Storyline | Option A (Recommended) |
|---|---|---|
| Problem alignment | Good: Mamba efficiency vs. Transformer cost | Same, but stronger gap specification |
| Variable alignment | Fair: 3D DWConv appears late in Intro | Better: DWConv dimension mentioned alongside Mamba introduction |
| Contribution-evidence alignment | Weak: Contribution 3 claims SOTA without TotalSeg | Stronger: All contributions are analytical, supported by controlled experiments |

## Priority Revision Plan
The revision plan is organized into three priority tiers. P0 items are publication-critical and must be addressed before acceptance. P1 items substantially improve rigor and confidence. P2 items are quality-of-presentation enhancements.

### P0: Must-Address Before Acceptance

| Item | Issue | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P0-A | Single-run results (W1, Issue 1) | Re-run ≥3 seeds for key comparisons, report mean±std, add significance tests | Core empirical claims become interpretable | 2-3 weeks |
| P0-B | TotalSeg missing from final comparison (W2, Issue 2) | Evaluate UlikeMamba 3dMT on TotalSeg and add to Fig. 4 | Central "new benchmark" claim becomes fully supported | 1-2 weeks |
| P0-C | Tri-scan capacity confound (W3, Issue 3) | Add matched-capacity Single-scan control experiment | Tri-scan advantage claim becomes rigorous | 1 week |
| P0-D | Abstract/contribution overclaiming (W6, Issue 5) | Rewrite abstract and Contribution 3 per annotation guidance | Claim-evidence alignment improves; reduces reviewer skepticism | 1 day |
| P0-E | Missing Limitations section (W8) | Add dedicated Limitations paragraph to Conclusion | Scientific rigor and self-awareness demonstrated | 0.5 day |

### P1: Substantial Improvement

| Item | Issue | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P1-A | Causal mechanism claims without evidence (W4, Issue 4) | Add feature autocorrelation analysis for DWConv 1D vs 3D + per-class Dice breakdown for MSv4 | Transforms speculation into evidence-backed mechanism analysis | 1-2 weeks |
| P1-B | Related Work as flat list (W7) | Reorganize as comparison table or structured paragraphs | Stronger gap communication and novelty positioning | 2-3 days |
| P1-C | Flattening strategy not specified (W8, related) | Add one sentence on flattening order in Section 4.1 | Reproducibility improved | 0.5 day |
| P1-D | Scanning analysis hypothesis untested (related to W4) | Acknowledge the "structural priors" hypothesis as untested and suggest how to verify it | Analytical honesty improved | 0.5 day |

### P2: Quality Enhancement

| Item | Issue | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P2-A | MSv4 fusion mechanism not ablated (minor) | Add small ablation comparing MSv4 vs alternative fusion strategies | Analytical completeness improved | 1 week |
| P2-B | Hyperparameter sensitivity not explored (minor) | Add note that nnUNet auto-configuration was used consistently | Robustness awareness improved | 0.5 day |
| P2-C | Title vagueness (storyline issue) | Revise title to reflect analytical contribution | Reader engagement and expectation alignment | 0.5 day |

### Revision Sequence (Recommended Order)

```
Week 1-2: P0-A (multi-seed runs) + P0-B (TotalSeg evaluation) — these are the longest experiments, start first
Week 2-3: P0-C (Tri-scan control) + P1-A (diagnostic analysis) — runs in parallel with above
Week 3:   P0-D (rewrite abstract/contributions) + P0-E (limitations) + P1-B (Related Work restructure) — text edits
Week 3-4: P1-C + P1-D + P2-A/B/C — remaining polish items
```

### Expected Quality After Full P0-P1 Completion

- All empirical comparisons: mean±std with significance markers → claims become statistically grounded
- Central SOTA claim: supported by all three benchmarks → evidence gap closed
- Tri-scan analysis: confound resolved → analytical conclusion supported or refuted
- Causal mechanism claims: backed by diagnostic evidence → analytical depth increases
- Presentation: bounded claims, clear limitations, structured related work → improved reviewer confidence

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 (Sec 4) | Mamba vs Transformer under matched U-shape backbone | UlikeMamba (1d/3d) vs UlikeTrans (vanilla/SRA) on AMOS, TotalSeg, BraTS | Dice, FLOPs, Params | UlikeMamba 3d outperforms UlikeTrans SRA (87.45 vs 85.97 avg Dice) at lower FLOPs (46.03 vs 64.47 G) | C1 (Mamba can replace Transformers) | Single-run results; DWConv 3d mechanism not validated; vanilla UlikeTrans OOM prevents fair comparison |
| E2 (Sec 5) | Multi-scale Mamba blocks improve representation learning | UlikeTrans SRA + MSv1/2/3; UlikeMamba 3d + MSv1/2/3/4 on 3 datasets | Dice, FLOPs, Params | MSv4 achieves highest avg Dice (88.01); gains largest on TotalSeg (+1.90) | C2 (Mamba enhances multi-scale learning) | No per-class analysis; MSv4 fusion mechanism not ablated; no capacity-matched baseline |
| E3 (Sec 6) | Multi-directional scanning improves spatial capture | UlikeMamba 3d with Single/Dual-forward-backward/Dual-forward-random/Tri-scan | Dice, FLOPs, Params | Tri-scan highest avg Dice (87.93); Single-scan competitive (87.45) | C3 (scanning strategy analysis) | Capacity confound (Tri-scan uses 3× SSM); "structural priors" explanation untested |
| E4 (Sec 7) | Integrated model outperforms strong baselines | UlikeMamba 3dMT vs nnUNet, CoTr, UNETR, SwinUNETR, U-Mamba on AMOS, BraTS | Dice, FLOPs (Fig 4) | UlikeMamba 3dMT competitive Dice (89.95 AMOS, 90.60 BraTS) with lowest FLOPs (93.09G) | C3 (combined model as benchmark) | TotalSeg not evaluated; single-run; FLOPs-only efficiency metric (no throughput/memory) |

### Research-Theme Gap Diagnosis

| Knowledge Claim | Current Evidence Strength | Gap | Required Action |
|---|---|---|---|
| "Mamba can replace Transformers" (C1) | Level 1 (single-run Dice on 3 datasets) | No variance estimation; no deployment metrics; DWConv 3d mechanism unvalidated | Multi-seed runs + diagnostic analysis |
| "MSv4 enhances multi-scale learning" (C2) | Level 2 (single-run Dice with 4 schemes) | No per-class analysis; fusion mechanism not ablated; capacity not controlled | Per-class breakdown + fusion ablation |
| "Tri-scan is beneficial" (C3) | Level 1 (single-run Dice, confounded) | Capacity confound unaddressed; "structural priors" hypothesis untested | Capacity-matched control + verification on non-medical data |
| "Combined model sets new benchmark" (C3) | Level 1 (2/3 datasets, single-run) | TotalSeg missing; FLOPs-only efficiency metric | TotalSeg evaluation + throughput/memory reporting |

### Proposed Research Experiments (P0/P1/P2)

#### Experiment P0-A: Multi-Seed Variance and Significance Testing
- **Target Claim:** All comparative claims (C1, C2, C3)
- **Hypothesis:** Observed improvements are statistically significant (p < 0.05) over baselines
- **Minimal Design:** Run UlikeTrans SRA, UlikeMamba 3d, UlikeMamba 3d+MSv4, and UlikeMamba 3dMT with 3 random seeds each on all 3 datasets. Report mean ± std.
- **Controls/Baselines:** Same models as already implemented; keep all hyperparameters fixed across seeds
- **Metrics:** Dice (mean ± std), paired t-test p-value vs strongest baseline
- **Success Criterion:** At least 2 of 3 datasets show significant (p<0.05) improvement of UlikeMamba 3dMT over strongest baseline
- **Estimated Cost:** ~3-4 GPU-weeks (12 models × 250K iters × 3 seeds)
- **Expected Paper-Quality Gain:** All empirical claims become scientifically interpretable

#### Experiment P0-B: TotalSeg Final Evaluation
- **Target Claim:** C3 (combined model benchmark)
- **Hypothesis:** UlikeMamba 3dMT maintains its advantage on 117-class TotalSeg
- **Minimal Design:** Evaluate UlikeMamba 3dMT on TotalSeg test set. Compare to best TotalSeg baseline from Table 2 (UlikeMamba 3d with MSv4: 84.50 Dice)
- **Controls/Baselines:** Same preprocessing/inference pipeline as earlier TotalSeg experiments
- **Metrics:** Dice (per-class and average)
- **Success Criterion:** UlikeMamba 3dMT average Dice ≥ 84.50 (matches or exceeds MSv4 baseline)
- **Estimated Cost:** ~1 GPU-week
- **Expected Paper-Quality Gain:** Central "new benchmark" claim fully supported across all 3 benchmarks

#### Experiment P0-C: Tri-scan Capacity-Matched Control
- **Target Claim:** C3 (Tri-scan advantage is due to multi-directional scanning)
- **Hypothesis:** Single-scan with matched parameter count does not match Tri-scan performance
- **Minimal Design:** Create "Single-scan-large" with SSM hidden dimension expanded so total params ≈ 26.4M. Evaluate on AMOS and TotalSeg.
- **Controls/Baselines:** Compare to Tri-scan and original Single-scan (24.3M) from Table 3
- **Metrics:** Dice, FLOPs, Params
- **Success Criterion:** Single-scan-large achieves significantly lower Dice than Tri-scan (or the gap substantially narrows)
- **Estimated Cost:** ~1 GPU-week
- **Expected Paper-Quality Gain:** Resolves critical confound; conclusion about multi-directional scanning becomes evidence-backed

#### Experiment P1-A: Diagnostic Analysis for DWConv 1D vs 3D
- **Target Claim:** C1 (3D DWConv preserves spatial coherence)
- **Hypothesis:** Mamba 3d feature maps show higher local spatial autocorrelation than Mamba 1d
- **Minimal Design:** Extract intermediate feature maps (ES2 stage) from both models on 50 validation samples. Compute average pairwise correlation between each voxel and its 3×3×3 neighborhood.
- **Metrics:** Spatial autocorrelation coefficient (higher = better coherence)
- **Success Criterion:** Mamba 3d shows significantly higher autocorrelation than Mamba 1d (p < 0.05)
- **Estimated Cost:** 0.5 GPU-day (no training needed; use already-trained models)
- **Expected Paper-Quality Gain:** Mechanism claim transitions from speculation to evidence-backed

### ASCII Diagram — Experiment Upgrade Plan

```text
Experiment Upgrade Plan (P0/P1/P2 sequencing)
┌─────────────────────────────────────────────────────────────────┐
│  TODAY'S MANUSCRIPT (single-run, 2/3 benchmarks, confounded)    │
└──────────────────────┬──────────────────────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ P0-A     │ │ P0-B     │ │ P0-C     │
    │ Multi-   │ │ TotalSeg │ │ Capacity- │
    │ seed     │ │ Final    │ │ matched   │
    │ runs     │ │ Eval     │ │ control   │
    └────┬─────┘ └────┬─────┘ └────┬─────┘
         │            │            │
         └────────────┼────────────┘
                      ▼
          ┌──────────────────────┐
          │ P1-A: Diagnostic     │
          │ (spatial coherence   │
          │  verification)       │
          └──────────┬───────────┘
                     ▼
          ┌──────────────────────┐
          │ P2: Quality polish   │
          │ (ablation, title,    │
          │  hyperparameter note)│
          └──────────────────────┘
                     ▼
          ┌──────────────────────────────────┐
          │ REVISED MANUSCRIPT                │
          │ - Statistical grounding           │
          │ - All 3 benchmarks                │
          │ - Capacity confound resolved      │
          │ - Mechanism evidence              │
          │ - Bounded claims + limitations    │
          └──────────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Score Rationale (research value and novelty prioritized):**
- The paper's controlled experimental design and three-part investigation structure represent a genuine methodological improvement over prior Mamba segmentation works (+2.0 for systematic contribution).
- However, the absence of any statistical variance reporting (single-run Dice throughout) fundamentally limits the interpretability of all comparative claims (-1.5). The missing TotalSeg evaluation leaves the headline result incomplete (-0.5). The Tri-scan capacity confound weakens a core analytical conclusion (-0.5). Overclaiming in abstract and contribution framing (-0.5) further reduces confidence. The inability to verify novelty claims against external literature (Retrieval-Disabled Mode) means novelty assessment is deferred (-0.5).

- The paper has a solid core idea (systematic Mamba vs. Transformer analysis) but the experimental execution is not yet publication-ready in its current form.

**Post-Revision Target: [6.5, 7.5] / 10**

**Target Rationale:** If the P0 items are fully addressed (multi-seed runs, TotalSeg evaluation, Tri-scan capacity control, rewritten claims, limitations section) and at least P1-A (diagnostic analysis) is completed, the score should reach the 6.5-7.5 range. This assumes: (a) multi-seed results confirm at least 2 of 3 key comparisons are statistically significant, (b) TotalSeg evaluation supports the integrated model's advantage, and (c) the Tri-scan control shows residual benefit beyond capacity. Novelty verification against external literature (manual verification) could further adjust this range upward or downward.

**Scoring Breakdown:**

| Dimension | Current Score (0-10) | Weight | Weighted Contribution |
|---|---|---|---|
| Research Value / Contribution | 6.0 | 30% | 1.80 |
| Novelty (deferred verification) | 5.0 | 25% | 1.25 |
| Validity / Soundness | 4.5 | 25% | 1.13 |
| Reproducibility / Clarity | 6.5 | 20% | 1.30 |
| **Final Score** | **5.5** | 100% | **5.48 ≈ 5.5** |