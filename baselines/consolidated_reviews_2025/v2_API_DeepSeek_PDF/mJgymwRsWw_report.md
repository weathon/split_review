## Summary
# Final Review Report

## Summary

This paper presents **Active Probabilistic Drug Discovery (APDD)**, a framework that formulates early drug discovery as an active probabilistic learning problem. APDD combines three steps: (1) probabilistic clustering of a molecular library using MPC on Morgan fingerprint substructure similarity, (2) selective molecular docking of representative molecules using Vina-GPU+, and (3) active learning querying with context probability refinement to select molecules for wet-lab validation. The method is evaluated on 90 targets from DUD-E and LIT-PCBA datasets, plus a simulated 1.4M-molecule large-scale virtual library.

**Strengths**: The core idea — using probabilistic clustering to propagate wet-lab feedback across structurally similar molecules without per-target model retraining — is practically motivated and intuitively appealing. The evaluation across 90 targets (79+11) is broad compared to many drug screening papers. The cost savings (median ~80% in docking, ~75% in wet experiments on well-behaved targets) are substantial if reproducible.

**Major weaknesses**: (1) The only baseline is exhaustive Vina docking (VE), which does not represent state-of-the-art screening methods. (2) The core probabilistic assumption — that Tanimoto similarity equals co-binding probability — is unvalidated. (3) Cost savings are reported as unconditional averages, while individual targets show enormous variance and several LIT-PCBA targets require *more* wet experiments than VE. (4) The large-scale experiment uses artificially pooled DUD-E decoys, not a realistic library. (5) Formula notation errors (Eq. 3) and missing symbol definitions (Eq. 4) reduce reproducibility. (6) The conclusion makes unsupported claims about eliminating lead optimization.

**Overall**: The paper presents a promising framework with a meaningful empirical scope, but suffers from overclaiming, insufficient baseline comparisons, and methodological gaps that prevent strong conclusions. With targeted revisions — especially adding baselines, validating key assumptions, and bounding claims — this work could make a solid contribution to the drug screening literature.

## Strengths
**S1 — Practical, well-motivated framework design.** The core idea of APDD — using probabilistic clustering to propagate limited wet-lab feedback across structurally similar molecules — addresses a real bottleneck in drug discovery: how to prioritize molecules for docking and experimental testing when both computational and wet-lab budgets are limited. The three-component pipeline (clustering, selective docking, active refinement) is clearly structured and each component serves a distinct purpose.

**S2 — Broad empirical evaluation across 90 targets.** The evaluation on 79 DUD-E targets and 11 LIT-PCBA targets is substantially broader than many drug screening papers that test on only a handful of proteins. This scope allows the paper to analyze performance variance across target families, library sizes, and docking score qualities — an analysis that, if properly reported, provides useful practical insights.

**S3 — Novel probability-aware active learning objective.** The expected recall improvement formulation (Eq. 2-5) goes beyond simple uncertainty sampling or diversity sampling by explicitly modeling how wet-lab feedback propagates through cluster probabilities. This probabilistic refinement mechanism is the most technically distinctive aspect of the work and represents a genuine methodological contribution to active learning for screening.

**S4 — Transparent reporting of failure cases.** The paper acknowledges that when Vina-GPU+ scores are uninformative (narrow range, AUC < 0.5), APDD does not outperform exhaustive docking and can require more wet experiments (KAT2A, PKM2, MAPK1 cases in Table 2). This transparency, while currently underemphasized, is scientifically honest and valuable.

**S5 — Scalability demonstration with 1.4M molecules.** Although the large-scale experiment has caveats, the demonstration that APDD can be applied to a million-scale library without computational breakdown is a useful proof-of-concept that the clustering + selective docking pipeline scales beyond typical benchmark sizes.

## Weaknesses
**W1 — Overclaimed cost savings without statistical rigor.** The Abstract and Introduction report "average reduction of 80% in computational docking expenses and 70% in wet experimental costs" without any variance or confidence bounds. Per-target WLE per(%) ranges from 1.5% to 100% on DUD-E, making the average a poor summary statistic. On several LIT-PCBA targets, APDD requires more wet experiments than VE (KAT2A: +20.6%, PKM2: +30.9%, MAPK1: +189.8%).

**W2 — Insufficient baseline comparison.** The sole baseline is Vina Enumeration (exhaustive docking of all molecules). Missing comparisons include: (a) standard clustering-based screening (e.g., UMAP + centroid docking), (b) random molecule selection at equal budget, (c) existing active learning methods for drug screening, and (d) simpler clustering alternatives. Without these, the contribution of each APDD component cannot be isolated.

**W3 — Unvalidated core probability assumption.** Equation (1) defines Tanimoto similarity on Morgan fingerprints as a direct probability estimate for co-binding to the same target. This conceptual leap is neither calibrated against empirical co-binding data nor compared against alternative similarity metrics. The claim that it is "validated using statistics from Lit-PCBA/DUD-E/PubChem datasets" is unsupported by any results in the paper.

**W4 — Formula errors and missing definitions.** Equation (3) contains a notation error using `P(d_j=1|...)` where `d_j` is not defined as an event variable. Equation (4) uses symbols P_i, P_j, S_ij without prior definition. The conditional independence assumption for multi-modal fusion (Section 4.2) is unstated and unvalidated. These issues reduce reproducibility and reader confidence.

**W5 — Unrealistic large-scale evaluation.** The 1.4M-molecule experiment pools decoys from all DUD-E proteins as "inactive molecules for each target," which does not represent a realistic virtual screening library. Additionally, only 5 proteins are tested, showing high variance (0.6% to 22.2% WLE reduction) that limits generalizability.

**W6 — Redundant structure and weak narrative.** Section 3 (Formulation) largely repeats content from the Introduction. The Related Work section is a narrative list of platforms rather than a comparative methodological analysis. The Introduction over-relies on a single citation (Wei et al. 2023 cited 6 times). The Conclusion makes an unsupported claim about "eliminating the need for lead optimization."

**W7 — Missing ablation studies.** The paper does not isolate the contribution of: (a) MPC vs simpler clustering (k-means, hierarchical), (b) the active learning query vs random selection within top clusters, (c) the isotonic regression calibration vs direct score ranking, or (d) the probability refinement vs one-shot selection.

**W8 — No code or data release.** The paper states "The code and data will be freely available upon acceptance" without a repository or supplement. Combined with incomplete formula notation and missing experimental details, this significantly lowers reproducibility.

## Key Issues
### Issue 1 (Critical): Unvalidated co-binding probability assumption
**Severity: Major | Validity Risk: High | Fixability: High**

The paper equates Tanimoto similarity on Morgan fingerprints (Eq. 1) with the probability that two molecules bind to the same protein target. This is the foundational assumption on which the entire clustering and probability propagation pipeline rests. If this mapping is inaccurate, the cluster assignments, posterior updates, and active learning gains are all unreliable. The paper claims validation using Lit-PCBA/DUD-E/PubChem datasets but presents zero calibration curves, correlation statistics, or error analyses. **Required fix**: Provide calibration data showing empirical co-binding frequency vs Tanimoto similarity bins, with correlation coefficients and calibration error metrics.

### Issue 2 (Major): Single baseline comparison
**Severity: Major | Validity Risk: High | Fixability: Medium**

APDD is compared only against exhaustive Vina enumeration (VE). Without comparisons against standard clustering-based screening (e.g., UMAP + centroid docking), random selection, or existing active learning methods for drug discovery, the paper cannot attribute its gains to any specific component. The claimed "82% reduction" could be achieved by any method that docks fewer molecules — including random subsampling. **Required fix**: Add at least two baselines: (a) random molecule selection at equal docking budget, (b) a standard clustering-based method (e.g., k-means or UMAP with centroid docking and no active refinement).

### Issue 3 (Major): Overclaimed and underqualified cost savings
**Severity: Major | Validity Risk: Medium | Fixability: High**

The Abstract and Introduction report 80%/70% average cost savings without variance, confidence intervals, or the crucial caveat that on several LIT-PCBA targets APDD actually performs worse. The individual per-target WLE per(%) shows enormous spread (1.5%–100% on DUD-E), and three LIT-PCBA targets exceed 100% (APDD uses more experiments than VE). The paper's framing is systematically optimistic. **Required fix**: (a) Replace averages with medians and report 5th-95th percentile ranges. (b) Clearly state the fraction of targets where APDD underperforms VE. (c) Add a conditional statement: "APDD reduces costs when docking scores have reasonable discriminative power (AUC > 0.6, score spread > 2 kcal/mol)."

### Issue 4 (Major): Formula errors and incomplete derivations
**Severity: Major | Reproducibility Risk: High | Fixability: High**

Equation (3) uses `P(d_j=1|...)` where the event variable `d_j` is undefined (should be `e_j`). Equation (4) uses P_i, P_j, S_ij without definition. The conditional independence assumption for multi-modal fusion (Section 4.2) is stated but never justified or tested. These issues prevent independent reproduction of the core algorithm. **Required fix**: (a) Correct Eq. (3) notation. (b) Define all symbols in Eq. (4) before or immediately after its presentation. (c) Add a derivation appendix showing the steps from the independence assumption to the fusion formula.

### Issue 5 (Major): Unrealistic large-scale evaluation
**Severity: Major | Generalizability Risk: High | Fixability: Medium**

The 1.4M-molecule experiment (Section 5.4) pools DUD-E decoys across targets rather than using a commercially relevant compound library. Only 5 proteins are tested, showing high variance (WLE per(%) from 0.6% to 22.2%). The claim about "potential of APDD in real world drug discovery applications" is unsupported by this setup. **Required fix**: (a) Test on at least 20 proteins. (b) Use a realistic decoy library (e.g., ZINC or ChEMBL inactives) rather than pooled DUD-E decoys. (c) Add a comparison against random selection at equal docking budget.

### Issue 6 (Moderate): Missing ablation studies
**Severity: Minor | Insight Risk: Medium | Fixability: Medium**

The paper does not isolate which component drives cost savings: MPC clustering, selective docking, isotonic regression calibration, or the active learning query. **Required fix**: Add ablations that replace (a) MPC with k-means clustering, (b) the active learning query with random selection within top clusters, and (c) the isotonic regression with raw score ranking.

### Issue 7 (Moderate): Conclusion overselling
**Severity: Minor | Narrative Risk: Medium | Fixability: High**

The Conclusion claims APDD "aims to eliminate the need for lead optimization," which is unsupported by any experiment in the paper. The conclusion also lacks any limitation discussion or future work directions. **Required fix**: Replace with a concise summary of validated findings, explicit limitations (docking quality dependency, single baseline, unvalidated probability assumption), and three concrete next steps.

## Actionable Suggestions
### S1 — Calibrate and validate the Tanimoto-as-probability assumption (Must)
**Target**: Section 4.1, Equation (1)

**Action**: Add a calibration figure showing empirical co-binding frequency against Tanimoto similarity bins (0-0.1, 0.1-0.2, ..., 0.9-1.0) computed from the Lit-PCBA/DUD-E/PubChem datasets you claim to have used. Report Spearman correlation between similarity and co-binding frequency, mean absolute calibration error (MACE), and reliability diagram. If calibration is poor, replace Eq. (1) with a learned mapping using isotonic regression (as done for docking scores in Section 4.2).

### S2 — Add two baselines (Must)
**Target**: Section 5.2 (Performance Comparison)

**Action**: Add the following baselines at equal docking budget:
1. **Random sampling**: Randomly select molecules for docking and testing with the same budget.
2. **Clustering baseline**: Use k-means or UMAP-based clustering (as in Hernández-Hernández & Ballester, 2023), dock cluster centroids, then test top centroids. This isolates the benefit of probabilistic vs deterministic clustering.
Report relative efficiency gain over each baseline separately. This is a moderate-effort addition with high scientific impact.

### S3 — Correct formula notation and add derivations (Must)
**Target**: Sections 4.2-4.3, Equations (3)-(5)

**Actions**:
- Eq. (3): Replace `P(d_j=1|d_i, s_ij, d_j)` with `P(e_j=1|d_i, s_ij, d_j)` throughout.
- Eq. (4): Before presenting the formula, define: `P_i = P(e_i=1)`, `P_j = P(e_j=1)`, `S_ij = P(e_ij=1)`.
- Eq. (4): Provide a short derivation in an appendix showing how the law of total probability and assumed independence yield the expression.
- Multi-modal fusion (Section 4.2): Add a caveat: "This formula assumes conditional independence of score modalities given the binding label, which may not hold in practice. We recommend validating the calibration of fused probabilities against a held-out set before deployment."

### S4 — Replace unconditional cost claims with bounded statistics (Must)
**Target**: Abstract, Introduction (contribution paragraph), Conclusion

**Action**: 
- Replace "average reduction of 80%/70%" with "median reduction of X%/Y% (interquartile range: [A,B]/[C,D]) across 79 DUD-E targets."
- Add sentence: "On 3 of 11 LIT-PCBA targets where docking scores had limited dynamic range or AUC < 0.5, APDD required comparable or slightly more wet experiments than exhaustive docking."
- Add bounded phrasing: "These results suggest APDD is most effective when docking scores provide reasonable discriminative power."

### S5 — Add component ablation (Nice-to-have)
**Target**: After Section 5.2 (new subsection)

**Action**: Compare APDD against itself with key modules replaced:
1. Replace MPC clustering with k-means clustering (same number of clusters).
2. Replace active learning query with random selection from top clusters.
3. Replace isotonic regression calibration with raw Vina score ranking.
Report wet-lab and docking cost for each ablation on a subset of 10 representative DUD-E targets.

### S6 — Improve large-scale evaluation (Nice-to-have)
**Target**: Section 5.4

**Action**: 
- Use a realistic decoy library (e.g., ZINC15 or a DUD-E independent subset) instead of pooled DUD-E decoys.
- Test on at least 20 proteins.
- Add a random-selection baseline for comparison.

### S7 — Add limitation paragraph and remove unsupported conclusion claim (Must)
**Target**: Section 6 (Conclusion)

**Action**: 
- Remove the unsupported claim about "eliminating the need for lead optimization."
- Add a Limitations subsection covering: dependency on docking score quality, single-baseline design, unvalidated Tanimoto calibration, and the artificial large-scale setup.
- Add a Future Work subsection with 3 concrete directions: (1) multi-modal docking score integration, (2) validation on in-house or commercial libraries, (3) extension to lead-optimization-stage properties (ADMET prediction).

## Storyline Options + Writing Outlines
The current introduction has a weak narrative arc: it starts too broad (textbook-style description of drug discovery), relies on repetitive citations, and does not clearly establish the research gap until the formulation in Section 3 (which largely repeats the introduction). Below are two alternative storylines.

### Storyline Option 1 (Recommended): Problem-Driven Structure

**Abstract Outline (4-sentence structure)**:
- **S1 (Problem)**: "Identifying active molecules that bind to target proteins is a critical bottleneck in early drug discovery, with compound libraries containing millions of candidates yet typical hit rates of only 10-35%."
- **S2 (Gap)**: "Existing approaches either dock all molecules at high computational cost or use active learning methods that require target-specific retraining and many wet-lab assays."
- **S3 (Method)**: "We propose APDD, which frames drug screening as an active probabilistic learning problem: molecules are clustered by substructure similarity, representative molecules are docked, and the limited wet-lab results propagate through cluster probabilities to refine predictions."
- **S4 (Result)**: "On 90 targets from DUD-E and LIT-PCBA, APDD achieves target recall with a median 75-80% reduction in docking and wet-lab costs compared to exhaustive docking on well-predicted targets, while matching screening accuracy."
- **S5 (Bounded claim)**: "Gains depend on docking score quality; on targets with poor score discrimination, APDD performance matches or slightly trails exhaustive docking."

**Introduction Outline (6-paragraph structure)**:

- **P1 — Practical stakes**: Open with the concrete bottleneck — screening large molecular libraries is slow and expensive, hit rates are low, and docking scores correlate poorly with experimental activity. State the central question: given limited computational and wet-lab budgets, which molecules should we dock and test?
  
- **P2 — Prior approaches and their gaps**: Review three existing paradigms: (a) exhaustive docking (accurate but expensive), (b) clustering-based screening (reduces cost but cannot learn from feedback), (c) active learning with ML models (requires target-specific retraining). Conclude that none combine probabilistic clustering with active feedback propagation.

- **P3 — Our formulation**: Frame the solution as an active probabilistic learning problem, leveraging the observation that active molecules are scarce and clustered in chemical space. Preview the three APDD components (clustering, selective docking, active refinement with feedback propagation) and explain why probabilistic clustering is key.

- **P4 — Method sketch**: Briefly describe MPC clustering on Morgan fingerprints, representative molecule selection via substructure similarity maximization, Vina-GPU+ docking, isotonic regression for probability calibration, and the expected-recall-gain query strategy.

- **P5 — Empirical preview**: Summarize the evaluation (90 targets, two benchmarks) and key results (cost reduction on most targets, exceptions where docking quality is poor). Preview the large-scale simulation.

- **P6 — Contributions**: List three contributions: (C1) the probabilistic active learning formulation, (C2) the APDD algorithm with expected-recall-gain query, (C3) empirical evaluation showing cost savings conditional on docking quality.

### Storyline Option 2: Method-First Structure

Intro P1-P2: Same as Option 1.
Intro P3: Jump directly into APDD's methodological novelty — the expected recall improvement objective and probabilistic refinement — then show how it differs from prior active screening.
Intro P4: Ground the method in the drug discovery domain (clustering, docking). 
Intro P5: Evaluation and contributions.

This structure is better for a methods-focused venue but risks losing drug-discovery domain readers.

### Selected Storyline: Option 1

Option 1 is recommended because it builds the narrative from a practical bottleneck, which is more accessible to the interdisciplinary audience of ICLR. The key narrative improvement is making the research gap explicit (P2) before presenting the solution (P3), which the current manuscript does not do.

### Alignment Checks

| Check | Current | Option 1 |
|-------|---------|----------|
| Problem alignment | Weak — intro describes drug discovery broadly | Strong — opens with concrete bottleneck |
| Variable alignment | Moderate — "clustering" appears in intro but "probabilistic clustering" is not distinguished | Strong — explicit link between intro motivation and method components |
| Contribution-evidence | Weak — intro claims 80%/70% savings without caveats | Strong — bounded claims match empirical limitations |

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P0.1 | Eq. (3) notation error + undefined symbols in Eq. (4) | Correct formulas, add symbol definitions and derivation | Low (1 hour) | High — enables reproducibility |
| P0.2 | Overclaimed cost savings without variance/caveats | Replace averages with medians + IQR; add conditionality statement in Abstract, Intro, Conclusion | Low (2 hours) | High — corrects misleading framing |
| P0.3 | Unvalidated Tanimoto-as-probability assumption | Add calibration figure (co-binding frequency vs similarity) | Medium (1-2 days for analysis, half-page figure) | High — validates core assumption |
| P0.4 | Single baseline comparison | Add random sampling and clustering baseline (k-means/UMAP) | Medium (3-5 days for implementation and evaluation) | High — enables attribution of gains |
| P0.5 | Conclusion overselling | Remove "eliminate lead optimization"; add Limitations and Future Work subsections | Low (2 hours) | Medium — improves credibility |

### P1 — Important (Should fix for strong acceptance)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P1.1 | Missing limitation on docking quality | Add paragraph in Results and Abstract: "APDD reduces costs when docking scores have AUC > 0.6 or score spread > 2 kcal/mol" | Low (1 hour) | Medium |
| P1.2 | Repetitive Section 3 | Merge Section 3 into Introduction, remove standalone section | Low (1 hour) | Low-Medium — improves density |
| P1.3 | Incomplete Related Work | Restructure around methodological axes (clustering, active learning, score fusion) rather than platform descriptions | Medium (4-6 hours) | Medium — improves positioning |
| P1.4 | Multi-modal fusion claims without demonstration | Add caveat that multi-modal fusion was not used in current experiments, and provide single vs multi-modal comparison on a subset | Medium (2-3 days) | Medium — clarifies scope |

### P2 — Quality Improvement (Nice-to-have)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P2.1 | Missing ablation studies | Add ablations (MPC vs k-means, active vs random selection, calibrated vs raw scores) on 10 representative targets | High (1-2 weeks) | High — enables component attribution |
| P2.2 | Large-scale evaluation caveats | Replace pooled DUD-E decoys with realistic library; test on more proteins | High (1-2 weeks) | Medium — strengthens scalability claim |
| P2.3 | No code/data release | Upload anonymized code repository and processed data | Medium (3-5 days) | High — enables reproduction |
| P2.4 | Introduction too reliant on single citation | Diversify citations, reduce Wei et al. 2023 repeats | Low (< 1 hour) | Low — cosmetic |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: Overclaimed results without variance]
    -> [Fix: replace averages with medians+IQR, add conditionality]
    -> [Expected impact: honest, defensible claims]

[Problem: Core probability assumption unvalidated]
    -> [Fix: add Tanimoto calibration figure + metrics]
    -> [Expected impact: validates foundational claim or forces revision]

[Problem: Only one baseline]
    -> [Fix: add random sampling + clustering baselines]
    -> [Expected impact: enables gain attribution, strengthens conclusions]

[Problem: Formula errors (Eq. 3, Eq. 4)]
    -> [Fix: correct notation, add symbol definitions + derivations]
    -> [Expected impact: reproducibility restored]

[Problem: Conclusion oversells]
    -> [Fix: replace with validated findings + limitations + future work]
    -> [Expected impact: credible, bounded contribution statement]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/protocol) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-----------------------|---------|-------------|----------------|-------------------|
| E1 | DUD-E screening (79 targets) — does APDD reduce cost vs VE? | 79 DUD-E targets, APDD (MPC clustering + selective docking + active refinement) vs VE (exhaustive docking) | WLE count, Docking count, per(%) | Median ~82% docking reduction, ~75% WLE reduction | C2 (method efficiency) | Only one baseline; no confidence intervals; per-target variance unreported |
| E2 | LIT-PCBA screening (11 targets) | 11 LIT-PCBA targets, same protocol as E1 | WLE count, Docking count, per(%) | Average ~85% docking reduction, ~40% WLE reduction | C2 (method efficiency) | 3 targets show APDD worse than VE; small sample (n=11) |
| E3 | Molecule clustering analysis | Active molecule distribution analysis for 4 DUD-E + 4 LIT-PCBA targets | R_k (active molecule ratio), P_k (cluster purity) | DUD-E: active molecules perfectly separated (P_k=1.0). LIT-PCBA: P_k ranges 0.35-0.76 | C1 (cluster assumption) | Only 8 proteins analyzed; DUD-E purity perfect possibly due to benchmark design |
| E4 | Large-scale simulation (5 targets, 1.4M molecules) | 5 DUD-E proteins, pooled decoys from all DUD-E as inactives | WLE count, Docking count, per(%) | APDD uses 20% of VE resources on average | C2 (scalability) | Pooled DUD-E decoys unrealistic; only 5 proteins; no random baseline |
| E5 | Multi-modal fusion (described but not implemented) | — | — | — | Not tested | Described in Methods but not used in any experiment |

### Research-Theme Gap Diagnosis

The experimental validation leaves three critical gaps:

1. **Attribution gap**: Without ablations (E5) or multiple baselines, it is impossible to determine whether APDD's gains come from clustering (reducing the number of molecules to dock), probability calibration (better ranking), or the active learning query (better selection for wet-lab). The current design is a black-box comparison.

2. **Validation gap**: The foundational assumption (Tanimoto similarity = co-binding probability, used in E1-E4) is never directly validated. If this assumption is wrong, all experiments inherit bias.

3. **Generalization gap**: E4 uses artificial decoy pooling, not a realistic diverse library. E3's cluster purity analysis is limited to 8 proteins. The method's performance on truly novel targets (not in DUD-E/LIT-PCBA) is unknown.

### Proposed Research Experiments

#### P0 — Calibration Validation

| Field | Value |
|-------|-------|
| Target Claim | C1 (cluster assumption) |
| Hypothesis | Tanimoto similarity on Morgan fingerprints correlates with empirical co-binding frequency |
| Minimal Design | Compute Tanimoto similarity for all molecule pairs from 10 DUD-E proteins. Bin similarities (0-0.1, ..., 0.9-1.0). For each bin, compute fraction of pairs that share the same activity label (both active or both inactive vs mixed). |
| Controls/Baselines | Compare against ECFP4 Tanimoto, MACCS Tanimoto, and random baseline (0.5 expected co-binding rate) |
| Metrics | Spearman ρ, mean absolute calibration error, reliability diagram |
| Success Criterion | Monotonic increasing relationship with ρ > 0.6 and calibration error < 0.1 |
| Est. Cost/Time | 2-3 days computation, half-page figure |
| Paper-Quality Gain | Validates (or disproves) the foundational assumption; high scientific impact |

#### P0 — Baseline Addition

| Field | Value |
|-------|-------|
| Target Claim | C2 (APDD efficiency) |
| Hypothesis | APDD outperforms both random selection and standard clustering-based screening at equal budget |
| Minimal Design | On 20 DUD-E targets: (a) Random: randomly select molecules for docking + testing at same budget as APDD. (b) UMAP+centroid: cluster molecules with UMAP, dock centroids, test top-scoring centroids. (c) K-means+centroid: same with k-means. |
| Controls/Baselines | APDD, VE, random, UMAP+centroid, k-means+centroid |
| Metrics | WLE count, docking count, recall rate at each budget |
| Success Criterion | APDD achieves target recall with significantly fewer WLE than all baselines (paired Wilcoxon p < 0.05) |
| Est. Cost/Time | 5-7 days implementation + computation |
| Paper-Quality Gain | Enables gain attribution; addresses the most critical baseline weakness |

#### P0 — Formula Correction + Derivation

| Field | Value |
|-------|-------|
| Target Claim | C2 (method clarity and reproducibility) |
| Action | Correct Eq. (3) notation. Define all symbols for Eq. (4). Add 1-page derivation appendix showing Eq. (4), Eq. (5), and the multi-modal fusion formula from first principles. |
| Est. Cost/Time | 1-2 hours |
| Paper-Quality Gain | Enables independent reproduction; increases technical credibility |

#### P1 — Ablation Study

| Field | Value |
|-------|-------|
| Target Claim | C2 (component attribution) |
| Hypothesis | Both MPC clustering and active learning query contribute to APDD's efficiency, with clustering having larger impact |
| Minimal Design | On 10 DUD-E targets: compare (a) APDD-full, (b) APDD with k-means instead of MPC, (c) APDD with random selection instead of active query, (d) APDD without isotonic regression (raw score ranking) |
| Controls/Baselines | APDD-full as reference |
| Metrics | Delta in WLE count, docking count, and recall vs APDD-full |
| Success Criterion | MPC clustering contributes >= 30% of total WLE reduction vs VE; active query contributes >= 10% |
| Est. Cost/Time | 5-7 days |
| Paper-Quality Gain | Identifies which component drives gains; enables targeted improvement |

#### P1 — Large-Scale Realistic Evaluation

| Field | Value |
|-------|-------|
| Target Claim | C2 (scalability) |
| Hypothesis | APDD maintains cost savings on a realistic large library |
| Minimal Design | Use ZINC15 or ChEMBL inactive molecules as decoys (rather than pooled DUD-E). Test on 20 proteins. Add random-selection baseline. |
| Controls/Baselines | VE, random selection at equal budget |
| Metrics | WLE count, docking count, recall |
| Success Criterion | APDD uses < 50% of VE's resources on > 15/20 proteins |
| Est. Cost/Time | 1-2 weeks |
| Paper-Quality Gain | Stronger evidence for real-world applicability |

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0 — Must, before resubmission):
    [Calibration validation] -> [validate Tanimoto assumption]
    [Baseline addition: random + clustering] -> [gain attribution]
    [Formula correction + derivations] -> [reproducibility]

Stage 2 (P1 — Should, within 2 weeks):
    [Ablation study: MPC vs k-means, active vs random] -> [component contribution]
    [Realistic large-scale evaluation] -> [generalizability evidence]

Stage 3 (P2 — Nice-to-have, before final submission):
    [Code/data release] -> [community reproduction]
    [Multi-modal fusion demonstration] -> [framework completeness]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale**: The paper presents a practically motivated framework (APDD) with a broad empirical evaluation across 90 targets. The expected-recall-gain query strategy and probabilistic refinement mechanism are technically interesting. However, the score is constrained by (a) the single insufficient baseline that prevents gain attribution, (b) the unvalidated core probability assumption (Tanimoto = co-binding probability), (c) overclaimed cost savings in Abstract/Introduction/Conclusion that ignore substantial variance and failure cases, (d) formula errors (Eq. 3) and missing symbol definitions (Eq. 4) that reduce reproducibility, and (e) a conclusion that makes unsupported claims about eliminating lead optimization. The paper's research value is moderate: the framework structure is novel but the evidence for its superiority over simpler alternatives is not established.

**Scoring dimensions**:
- **Research value**: 6/10 — Practical problem, meaningful scope, but unanswered attribution questions reduce impact
- **Novelty**: 6/10 — Probabilistic clustering + active learning for drug screening is relatively novel, but the claim strength is limited by missing comparisons
- **Validity**: 4/10 — Core assumption unvalidated, cost claims overstated, formula errors present
- **Reproducibility**: 4/10 — Missing code, incomplete formula notation, undefined symbols
- **Writing quality**: 5/10 — Redundant structure (Section 3), over-reliance on single citation, conclusion overselling

**Post-Revision Target**: [6.5, 7.5] / 10

This target assumes that all P0 actions are completed: (1) Tanimoto calibration validation, (2) addition of random and clustering baselines, (3) formula corrections and derivations, (4) bounded, honest cost statistics with confidence intervals, (5) conclusion rewritten with limitations and future work. If P1-P2 items (ablation study, realistic large-scale evaluation, code release) are also completed, the upper bound of 7.5 is achievable.