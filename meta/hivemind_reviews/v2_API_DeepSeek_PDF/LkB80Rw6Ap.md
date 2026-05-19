## Summary
# Final Review Report

## Summary

This paper proposes Curvature-Constrained Message Passing (CCMP), a framework that modifies MPNN aggregation to propagate messages selectively along edges partitioned by Ollivier or Augmented Forman curvature. The authors introduce a curvature-constrained homophily measure ($\beta^+$, $\beta^-$) and several CCMP variants using positive/negative curvature masks with one-hop or two-hop propagation. Experiments on 11 node classification datasets show that CCMP outperforms base GCN/GAT on 6 of 7 heterophilic benchmarks and is competitive with existing rewiring methods (SDRF, FOSR, DIGL) on homophilic datasets.

**Strengths**: The core idea — using discrete curvature as a hard mask for message propagation rather than as soft attention or graph rewiring — is elegant and architecture-agnostic. The empirical evaluation is broad (11 datasets, 2 backbones, 4 baselines). The spectral gap analysis provides a mechanistic link to over-squashing mitigation.

**Weaknesses**: The contribution framing is insufficiently differentiated from prior curvature-based GNN work (Ye et al., 2019). The homophily analysis has interpretative inconsistencies. CCMP configuration choices are dataset-specific without a principled selection rule, raising concerns about over-tuning. The results section overclaims without statistical significance testing. Writing quality issues (typographical errors, vague abstract, generic introduction) reduce clarity.

**Novelty verdict**: Deferred — external literature verification was not available in this run. Based on manuscript evidence alone, the incremental advance over Ye et al. (2019) curvature attention and Topping et al. (2022) curvature-rewiring is plausible but requires systematic comparison to assess residual novelty. See Novelty Verification section for details.

## Strengths
1. **Elegant and general idea**: Using discrete edge curvature as a hard mask to partition message propagation channels (positive vs. negative curvature, one-hop vs. two-hop) is a conceptually clean approach. The framework is architecture-agnostic and can be applied to any MPNN backbone (demonstrated with GCN and GAT) without modifying the internal aggregation kernel.

2. **Broad empirical evaluation**: The paper evaluates on 11 datasets (7 heterophilic, 4 homophilic) with 2 backbone architectures and 4 competitive baselines (DIGL, SDRF, FOSR, FA). This is a thorough coverage that exceeds many concurrent works in the curvature-for-GNNs subarea. Reporting results over 100 random splits with standard deviations provides reasonable statistical grounding.

3. **Mechanistic analysis via spectral gap**: The paper goes beyond accuracy reporting by analyzing the normalized spectral gap before and after CCMP. This provides a direct link between the proposed method and the over-squashing mitigation claim, which many rewiring papers lack. The observed spectral gap increase (5%–87% across datasets) is a meaningful diagnostic signal.

4. **New homophily measure**: The curvature-constrained homophily ($\beta^+$, $\beta^-$) reveals structure invisible to global edge homophily $\beta$. For example, on Roman-empire, $\beta^- = 0.48$ vs $\beta = 0.29$, showing that negatively curved edges carry more same-label signal than the global average — a finding that directly motivates curvature-guided propagation. On Actor, $\beta^+ = 0.73$ vs $\beta = 0.32$, a striking 41-point absolute difference.

5. **Computational efficiency advantage**: CCMP does not modify the graph structure, avoiding the $\mathcal{O}(n^2)$ edge-addition cost of methods like FOSR. The one-hop variant reduces graph size by removing negative-curvature edges, cutting computational cost by 10–40% on large graphs (Squirrel, Actor, Roman-empire) without sacrificing performance.

## Weaknesses
1. **Insufficient differentiation from prior curvature-based GNN work** (Major). The paper does not clearly distinguish CCMP from Ye et al. (2019) Curvature Graph Network, which also uses Ollivier curvature for node classification. The difference (hard mask vs. soft attention) is mentioned cursorily in related work but never explicitly articulated as a design advantage. Without this distinction, the novelty claim is ambiguous.

2. **Dataset-specific configuration tuning without principled selection rule** (Major). Appendix A.3 shows that each dataset uses a different CCMP variant (e.g., negative one-hop for Squirrel, positive one-hop for Actor, two-hop negative for Texas). The paper does not report a validation procedure for configuration selection or analyze sensitivity to mis-specified configurations. This raises concerns about over-tuning and generalizability.

3. **Homophily analysis contains interpretative inconsistencies** (Major). Table 1's "Max Homophilic Gain" column reports relative improvements up to 131% (Actor), which is inflated by a small denominator ($\beta = 0.32$). The text claim that "using positively curved edges does not improve homophily" on heterophilic datasets is contradicted by Table 1 (e.g., $\beta^+ = 0.44 > \beta = 0.31$ for Texas). The 2-hop analysis claim is similarly inconsistent with the data.

4. **Results overclaimed without statistical testing** (Major). The paper states "CCMP outperforms the original adjacency matrix by 14.24% and 16.55%" without significance tests. Per-dataset analysis (Table 4) shows that on Chameleon, CCMP actually underperforms the base GCN. The spectral gap improvement is reported only as a range (5%–87%) without per-dataset breakdown. The conclusion uses "empirically proving" — inappropriate causal language for observational benchmark results.

5. **Missing reproducibility details** (Moderate). No hardware/software specifications are provided. Ollivier curvature computation takes up to 836 seconds for Squirrel, but it is unclear whether this is one-time preprocessing or repeated per run. The 2-hop neighborhood definition for curvature is ambiguous (does the curvature constraint apply to the entire path or individual edges?).

6. **Writing quality issues** (Moderate). The abstract is vague without concrete numbers. The first introduction paragraph is a generic literature survey that delays the paper's motivation. There are typographical errors ("wich" for "which", "beetween" for "between"). The CCMP method section (Section 3.4) describes architectural variants in prose without algorithmic pseudocode, reducing clarity.

7. **Limited scope of over-squashing evaluation** (Moderate). Over-squashing mitigation is measured only indirectly via spectral gap changes. No direct over-squashing benchmarks (e.g., Long Range Graph Benchmark, Tree-NeighbourMatch tasks from Alon & Yahav, 2021) are used. The claim of over-squashing mitigation would be stronger with such task-level validation.

## Key Issues
### Ranked Core Defect Board (Top 6 by Severity × Impact)

| Rank | Issue | Severity | Validity Risk | Evidence Map | Fixability |
|------|-------|----------|---------------|--------------|------------|
| 1 | Dataset-specific CCMP configs without selection principle | Major | High — undermines generalizability claim | Appendix A.3 shows per-dataset configs; no validation procedure reported | Fixable — add held-out config selection + sensitivity analysis |
| 2 | Results overclaimed without significance testing | Major | High — "14.24% improvement" averaged over datasets including one where CCMP loses (Chameleon) | Tables 4-5; Page 9 lines 24-26 | Fixable — report per-dataset deltas + significance tests |
| 3 | Insufficient differentiation from Ye et al. (2019) | Major | Medium — novelty claim is ambiguous | Page 3 lines 13-16 mention Ye et al. without explicit comparison | Fixable — add 2-3 sentence differentiation paragraph |
| 4 | Homophily analysis inconsistencies | Major | Medium — core contribution (C1) has contradictory statements | Table 1 vs Page 5 lines 46-49; "Max Homophilic Gain" column | Fixable — correct interpretation, replace relative gain with absolute delta |
| 5 | Over-claim in conclusion ("empirically proving") | Major | Medium — language over-reaches evidence | Page 9 line 44 | Fixable — replace with "demonstrating" or "providing evidence" |
| 6 | Missing over-squashing benchmarks | Moderate | Medium — core claim (C3) lacks direct task validation | Page 9 lines 33-36; spectral gap only indirect evidence | Fixable — add LRGB or Tree-NeighbourMatch results |

## Actionable Suggestions
### S1: Add explicit differentiation from Ye et al. (2019) Curvature Graph Network (Must)
**Location**: Page 3 — Section 2.2 (Graph Curvature), after describing Ye et al.
**Action**: Add 2-4 sentences explaining the key difference: Ye et al. uses Ollivier curvature as a continuous attention weight modulating edge messages within a fixed graph topology, whereas CCMP creates structurally disjoint propagation channels (N+ vs N−) that can be composed across layers. CCMP requires no learned curvature parameters and can be applied to any MPNN backbone without modifying its internal kernel.
**Expected Benefit**: Resolves novelty ambiguity and clarifies contribution boundary.

### S2: Replace "Max Homophilic Gain" with absolute delta (Must)
**Location**: Page 5 — Table 1 and surrounding text.
**Action**: Replace the relative "Max Homophilic Gain" column with absolute gain: $\Delta\beta = \max(\beta^+-\beta, \beta^--\beta, \text{2-hop}\beta^+-\beta, \text{2-hop}\beta^--\beta)$. For Actor, this changes from 131% (relative) to 0.41 (absolute). Add a note that relative gains can be misleading when $\beta$ is small.
**Expected Benefit**: Corrects misleading impression and improves scientific objectivity.

### S3: Correct homophily interpretation paragraph (Must)
**Location**: Page 5 — lines 46-51.
**Action**: Replace the sentence "For heterophilic datasets, using positively curved edges does not improve homophily" with "For heterophilic datasets, both $\beta^+$ and $\beta^-$ exceed the global $\beta$, but $\beta^-$ is typically higher (e.g., Roman-empire: $\beta^-=0.48$ vs $\beta^+=0.40$ vs $\beta=0.29$)." Also correct the 2-hop analysis to reflect per-dataset patterns rather than a blanket statement.
**Expected Benefit**: Eliminates contradiction between text and Table 1.

### S4: Report per-dataset spectral gap changes (Must)
**Location**: Page 9 — lines 33-36.
**Action**: Replace "the normalized spectral gap increases from 5% to 87% on these datasets" with a table showing per-dataset $\lambda_2$ before/after CCMP. Include dataset name, original $\lambda_2$, CCMP $\lambda_2$, relative change (%). For the 5% case (Roman-empire), discuss why the gain is small and whether over-squashing is still meaningfully reduced.
**Expected Benefit**: Strengthens the over-squashing mitigation claim with transparent evidence.

### S5: Add configuration selection principle and sensitivity analysis (Must)
**Location**: Page 8 — Section 4.3 or Appendix A.3.
**Action**: Either (a) fix a selection rule based on dataset properties (e.g., β threshold), or (b) report a cross-validation procedure where configuration is selected on validation split. Add a sensitivity table showing performance of all CCMP variants on 2-3 representative datasets to demonstrate the cost of mis-configuration.
**Expected Benefit**: Addresses over-tuning concerns and establishes generalizability.

### S6: Add statistical significance tests (Must)
**Location**: Page 9 — Section 4.4.
**Action**: For each dataset, report a paired t-test or Mann-Whitney U test comparing CCMP against the best baseline. Flag results where $p > 0.05$ as not statistically significant. Report per-dataset improvement as absolute delta (percentage points) not relative percentage.
**Expected Benefit**: Converts subjective "outperforms" claims to statistically grounded conclusions.

### S7: Add over-squashing benchmark results (Nice-to-have)
**Location**: Page 9 — Section 4.4 or Appendix.
**Action**: Evaluate CCMP on at least one standard over-squashing benchmark (e.g., Tree-NeighbourMatch from Alon & Yahav, 2021, or the Long Range Graph Benchmark). Compare against base GCN and SDRF. Report accuracy and convergence behavior.
**Expected Benefit**: Directly validates the core over-squashing mitigation claim.

### S8: Add reproducibility details (Nice-to-have)
**Location**: Page 7-8 — Section 4.3.
**Action**: Add: (1) hardware specification (GPU/CPU), (2) software framework (PyTorch Geometric version), (3) curvature computation library and settings, (4) clarification that curvature is one-time preprocessing.
**Expected Benefit**: Enables independent verification and comparison.

### S9: Fix writing issues (Nice-to-have)
**Location**: Throughout.
**Action**: 
- Fix typos: "wich" → "which" (Page 1), "beetween" → "between" (Page 4).
- Add pseudocode or algorithm block for CCMP (Section 3.4).
- Replace "empirically proving" with "demonstrating" or "providing evidence for" (Page 9).
- Add concrete numbers to abstract.
**Expected Benefit**: Improves professional presentation quality.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows: Background (GNNs work well) → Heterophily challenge → Over-smoothing + Over-squashing → Curvature as solution → Contributions. The problem is that the first paragraph (9 citations in 13 lines) delays the core motivation. The curvature-rewiring link is introduced only in the last sentence of page 1, meaning a reader must get through 40 lines of text before understanding the paper's specific focus.

### Alignment Checks

- **Problem alignment**: The stated challenge (over-squashing) directly matches the proposed solution (curvature-constrained propagation to reduce bottlenecks). ✓
- **Variable alignment**: "Curvature," "positive/negative edges," and "homophily" appear in both introduction and method. ✓
- **Contribution-evidence alignment**: The abstract claims "outperforms existing rewiring methods" — this is supported by Tables 4-5 for heterophilic datasets but not for homophilic datasets where CCMP is comparable or worse than DIGL. Partial match.

### Recommended Storyline (Option A — Best)

A problem-first, curvature-centric arc:

**Paragraph 1** (New): *Problem hook* — Open with: "Message-passing GNNs are fundamentally limited by the over-squashing bottleneck: as information from exponentially growing receptive fields is compressed into fixed-size vectors, long-range interactions are lost." Establish stakes by citing Alon & Yahav (2021) immediately. No generic GNN background.

**Paragraph 2** (New): *Curvature link* — "Recent work has shown that over-squashing concentrates on edges with negative curvature, which act as structural bottlenecks." Briefly introduce Ollivier and Forman curvature. Reference Topping et al. (2022) and Figure 1.

**Paragraph 3** (New): *Gap* — "Existing solutions either rewire the graph (SDRF, FOSR, DIGL), incurring computational cost and altering graph properties, or use curvature only as soft attention weights (Ye et al., 2019), which does not prevent information from flowing through bottleneck edges." This explicitly contrasts CCMP with prior work.

**Paragraph 4** (New): *Proposed method + contributions* — "We propose Curvature-Constrained Message Passing (CCMP), which partitions edges by curvature sign and restricts message propagation to selected curvature classes. This framework requires no graph modification, is architecture-agnostic, and can be applied with one-hop or two-hop strategies." List contributions with concrete numbers.

### Alternative Storyline (Option B) — Taxonomy/Classification Arc

**Paragraph 1**: Classify existing over-squashing solutions into three families: (a) graph rewiring, (b) global context (master node, expanders), (c) curvature-aware propagation. State that (c) is the least explored.

**Paragraph 2**: Identify sub-families of curvature-aware methods: curvature-as-attention (Ye et al.) vs curvature-as-mask (this paper). Argue that masking is more flexible.

**Paragraph 3**: Present CCMP as the first systematic curvature-masking framework.

**Paragraph 4**: Contributions.

### Abstract Outline (Recommended)

S1 — Problem: "Graph Neural Networks suffer from over-squashing, where exponentially growing information is compressed into fixed-size node representations, limiting long-range interaction modeling."

S2 — Gap: "Existing rewiring methods modify graph topology at high computational cost, while curvature-aware attention still allows bottleneck edges to propagate noise."

S3 — Method: "We propose Curvature-Constrained Message Passing (CCMP), an architecture-agnostic framework that partitions edges by curvature sign and restricts message propagation to selected curvature classes."

S4 — Key Result: "On 7 heterophilic benchmarks, CCMP improves GCN/GAT accuracy by 6–32 percentage points (14% on average) and outperforms SDRF, FOSR, and DIGL on 6 of 7 datasets."

S5 — Significance: "CCMP increases the spectral gap by up to 87%, confirming over-squashing mitigation without graph modification."

### Introduction Outline (Paragraph-by-Paragraph)

**P1** (New — Problem Hook, ~6 sentences):
- Sentence 1: "Message-passing GNNs iteratively aggregate neighbor information to learn node representations."
- Sentence 2: "However, stacking layers causes each node to compress information from an exponentially growing receptive field into a fixed-size vector — a phenomenon known as over-squashing [Alon & Yahav, 2021]."
- Sentence 3: "Over-squashing severely limits GNNs' ability to model long-range dependencies, which are critical in heterophilic graphs where distant nodes carry predictive signal."
- Sentence 4: (Transition) "Recent work has linked over-squashing to edge curvature: negatively curved edges act as structural bottlenecks that impede information flow [Topping et al., 2022]."

**P2** (New — Gap, ~5 sentences):
- Sentence 1: "Existing approaches mitigate over-squashing by rewiring the graph — adding or removing edges to reduce bottlenecks."
- Sentence 2: "Methods like SDRF and FOSR iteratively adjust the adjacency matrix based on curvature or spectral gap, while DIGL uses PageRank-based diffusion."
- Sentence 3: "However, rewiring modifies the original graph structure, incurs significant computational cost, and may alter task-relevant connectivity patterns."
- Sentence 4: "Ye et al. (2019) use curvature as attention weights, but this still allows information to propagate through bottleneck edges, just with reduced weight."

**P3** (New — Proposed Method, ~4 sentences):
- Sentence 1: "We propose a fundamentally different approach: instead of modifying the graph, we control which edges participate in message propagation by partitioning them according to curvature sign."
- Sentence 2: "Our CCMP framework defines curvature-specific neighborhoods (N+ for positively curved edges, N− for negatively curved edges) and composes them across layers."
- Sentence 3: "This preserves the original graph structure while providing direct control over information flow through bottleneck regions."
- Sentence 4: (Optional) Figure 2 illustrates the difference between standard MPNN and CCMP propagation patterns.

**P4** (Contributions, bullet list as currently written but with sharper wording — see S1 in Actionable Suggestions).

## Priority Revision Plan
### P0 — Must-fix before resubmission (publication-critical)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | Differentiate from Ye et al. (2019) | Add 2-4 sentence differentiation paragraph (Section 2.2) | Resolves novelty ambiguity; prevents desk rejection | Low |
| P0.2 | Correct homophily misinterpretation | Fix text claims in Section 3.3 to match Table 1; replace "Max Homophilic Gain" with absolute delta | Eliminates factual contradictions | Low |
| P0.3 | Add configuration selection rule | Add validation procedure + sensitivity analysis (Section 4.3 / Appendix A.3) | Addresses over-tuning concern; establishes generalizability | Medium |
| P0.4 | Add per-dataset spectral gap table | Replace range with per-dataset λ₂ before/after (Section 4.4) | Strengthens over-squashing claim | Low |
| P0.5 | Revise conclusion language | Replace "empirically proving" with "demonstrating"; remove unsupported future claims | Aligns language with evidence strength | Low |
| P0.6 | Add significance tests | Report t-test p-values for CCMP vs best baseline on each dataset (Section 4.4) | Converts subjective claims to statistical evidence | Medium |

### P1 — Important for rigor

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Add over-squashing benchmarks | Evaluate on Tree-NeighbourMatch or LRGB | Directly validates core contribution | Medium-High |
| P1.2 | Clarify 2-hop neighborhood definition | Formalize N+2(i) in Section 3.4 with set notation | Enables reproducibility | Low |
| P1.3 | Add pseudocode for CCMP variants | Algorithm block in Section 3.4 | Improves clarity and reproducibility | Low |
| P1.4 | Add hardware/software specifications | One sentence in Section 4.3 | Enables fair comparison | Low |

### P2 — Quality improvement

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Fix abstract | Add concrete numbers (datasets, accuracy gain, spectral gap increase) | Improves first impression | Low |
| P2.2 | Restructure introduction | Follow Option A storyline (Problem → Curvature → Gap → Solution) | Improves narrative flow | Medium |
| P2.3 | Fix typos | "wich" → "which", "beetween" → "between" | Professional polish | Low |
| P2.4 | Add computational cost discussion | Compare CCMP preprocessing vs SDRF/FOSR per-iteration cost | Positions efficiency advantage | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | CCMP vs base GCN/GAT on homophilic datasets (Table 3) | 4 homophilic datasets (Cora, Citeseer, Photo, Computers); GCN/GAT backbones; 100 random splits | Accuracy ± std | CCMP comparable to base; DIGL slightly better on homophilic | C2 (CCMP applicable to any MPNN) | CCMP does not outperform DIGL on homophilic; not discussed |
| E2 | CCMP vs baselines on heterophilic datasets with GCN (Table 4) | 7 heterophilic datasets; GCN backbone; 4 baselines (DIGL, FA, SDRF, FOSR) | Accuracy ± std | CCMP wins on 6/7 datasets; CCMPa best overall | C3 (performance gain on heterophilic) | No statistical significance tests; Chameleon lost to FOSR |
| E3 | CCMP vs baselines on heterophilic datasets with GAT (Table 5) | Same as E2 but GAT backbone | Accuracy ± std | Same pattern as E2; CCMP wins on 6/7 | C3 (architecture-agnostic) | Same limitation as E2 |
| E4 | Curvature-constrained homophily analysis (Table 1) | 11 datasets; β+, β−, 2-hop variants; Ollivier curvature | β, β+, β−, 2-hop β+, 2-hop β− | β+ ≥ β on homophilic; β− > β on heterophilic | C1 (new homophily measure) | Interpretation inconsistencies; "Max Homophilic Gain" misleading |
| E5 | Spectral gap analysis (Page 9) | 3 datasets (Squirrel, Actor, Roman-empire) | Normalized spectral gap change | 5%–87% increase after one-hop CCMP | C3 (over-squashing mitigation) | Reported only as range; no per-dataset values |
| E6 | Computational cost analysis (Page 9) | 3 datasets (Squirrel, Actor, Roman-empire) | Graph size reduction; cost reduction | 10–40% cost reduction | C3 (efficiency) | No wall-clock time comparison with baselines |
| E7 | Curvature computation time (Table 2) | 11 datasets | Ollivier time; AF-Forman time | 1–836 seconds | Practical feasibility | No hardware specification; unclear if one-time cost |

### Research-Theme Gap Diagnosis

1. **Over-squashing task validation**: The paper relies entirely on spectral gap as a proxy for over-squashing mitigation. No direct over-squashing tasks (e.g., Tree-NeighbourMatch from Alon & Yahav, 2021) are evaluated. This limits the strength of Claim C3.

2. **CCMP variant selection**: The paper uses dataset-specific configurations without a principled selection rule. This weakens the claim that CCMP is a general-purpose framework.

3. **Baseline fairness on homophilic datasets**: CCMP underperforms DIGL on homophilic datasets (Table 3). The paper attributes this to DIGL adding positively curved edges, but provides no curvature analysis of DIGL's edges to support this claim.

4. **Ablation of curvature type**: CCMPO (Ollivier) vs CCMPa (Augmented Forman) are compared but the paper does not explain when one is preferred or why they produce different results (e.g., on Cora, CCMPO=87.34 vs CCMPA=85.60 with GCN).

5. **Generalization to deeper architectures**: The paper uses only 2-layer GNNs. Over-squashing is most relevant for deeper models (4-8 layers). The conclusion's suggestion of "very deep GNN models" is unsupported.

### Proposed Research Experiments

**P0 Experiment: Over-squashing benchmark validation**
- **Target Claim**: C3 — "CCMP attenuates over-squashing"
- **Hypothesis**: CCMP improves accuracy on the Tree-NeighbourMatch task (Alon & Yahav, 2021) by enabling better long-range information propagation.
- **Minimal Design**: Evaluate CCMP on Tree-NeighbourMatch with 4 layers. Compare against GCN, GCN+SDRF, GCN+FOSR.
- **Controls**: Same hidden dimension (64), optimizer (Adam, lr=0.001), 5 random seeds.
- **Metrics**: Accuracy, convergence epoch, sensitivity to tree depth.
- **Success Criterion**: CCMP achieves >5% absolute improvement over base GCN and is competitive with SDRF/FOSR.
- **Estimated Cost**: 2-3 GPU-hours.
- **Expected Quality Gain**: Directly validates the core over-squashing claim (currently supported only by spectral gap proxy).

**P1 Experiment: Configuration sensitivity analysis**
- **Target Claim**: C2 — "CCMP offers different variants for flexible propagation"
- **Hypothesis**: Dataset homophily level (β) predicts the optimal CCMP variant.
- **Minimal Design**: Run all 8 CCMP variants (positive/negative × one-hop/two-hop × Ollivier/Forman) on 3 datasets with varying β (Cora β=0.84, Texas β=0.31, Actor β=0.32). Report full 8×3 matrix.
- **Controls**: Same GCN backbone, hyperparameters fixed across variants.
- **Metrics**: Accuracy, rank correlation between β and optimal variant.
- **Success Criterion**: A clear pattern emerges (e.g., negative curvature preferred when β < 0.4).
- **Estimated Cost**: 3-5 GPU-hours.
- **Expected Quality Gain**: Replaces arbitrary dataset-specific configs with a principled selection rule. Addresses over-tuning concern.

**P2 Experiment: Deeper GNN evaluation**
- **Target Claim**: C3 — over-squashing mitigation
- **Hypothesis**: CCMP's advantage over baselines increases with number of layers.
- **Minimal Design**: Evaluate CCMP vs GCN vs SDRF on 3 heterophilic datasets (Texas, Wisconsin, Cornell) with {2, 4, 6, 8} layers.
- **Controls**: Residual connections for deeper models; same hidden dim (32); dropout tuned per depth.
- **Metrics**: Accuracy vs depth curve; performance drop rate.
- **Success Criterion**: CCMP shows slower accuracy degradation as depth increases compared to GCN.
- **Estimated Cost**: 5-8 GPU-hours.
- **Expected Quality Gain**: Validates the claim that CCMP reduces over-squashing in deeper architectures (currently only tested with 2 layers).

**ASCII Diagram — Experiment Upgrade Plan**

```text
Experiment Upgrade Plan (P0/P1/P2 Sequencing)
                      
    Current evidence     │     Proposed experiments
                         │
  C3: Over-squashing     │  P0: Tree-NeighbourMatch (direct task)
      mitigation         │  P2: Depth sweep 2→8 layers
         ↓               │       ↓
    Spectral gap proxy   │  Direct over-squashing validation
      (indirect)         │
                         │
  C2: Flexible CCMP      │  P1: 8 variants × 3 datasets
      variants           │       ↓
         ↓               │  Config selection rule + sensitivity
    Per-dataset configs  │  Generalizability established
      (no selection rule)│
                         │
  C1: Homophily measure  │  Correction of interpretation
      β+, β−             │       ↓
         ↓               │  Clear, consistent analysis
    Inconsistent text    │
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 5.5 / 10

**Rationale**: The paper presents a clean, architecture-agnostic idea (curvature-constrained message passing) with broad empirical evaluation across 11 datasets. However, the contribution is partially overlapping with prior curvature-based GNN work (Ye et al., 2019; Topping et al., 2022), and the incremental advance (hard mask vs soft attention/rewiring) is not explicitly differentiated. The evaluation has significant methodological weaknesses: dataset-specific configuration tuning without a principled selection rule, missing statistical significance tests, overclaimed results (averaging across datasets including one where CCMP loses), and interpretation inconsistencies in the homophily analysis. Writing quality issues further reduce clarity.

**Score breakdown**:
- **Novelty**: 5/10 — The concept of curvature-guided propagation is not entirely new; CCMP's specific contribution (hard partitioning vs soft attention/rewiring) is plausible but requires explicit differentiation. (Deferred — external verification unavailable.)
- **Research Value**: 6/10 — The curvature-constrained homophily measure and spectral gap analysis provide useful diagnostic tools. The architecture-agnostic nature is valuable for practitioners.
- **Validity/Soundness**: 5/10 — Configuration selection concerns, missing significance tests, and homophily interpretation errors weaken empirical validity.
- **Reproducibility**: 4/10 — Missing hardware/software specs, ambiguous 2-hop neighborhood definition, no pseudocode, and dataset-specific configurations reduce reproducibility.
- **Writing/Presentation**: 5/10 — Abstract is too vague; introduction is generic; typos present; no algorithm pseudocode.

**Post-Revision Target**: [6.5, 7.5] / 10

**Conditions**: This target is achievable if the authors:
1. Add a clear differentiation paragraph distinguishing CCMP from Ye et al. (2019) (P0.1)
2. Fix homophily interpretation inconsistencies and replace "Max Homophilic Gain" with absolute delta (P0.2)
3. Add a configuration selection rule with sensitivity analysis (P0.3)
4. Report per-dataset spectral gap changes and significance tests (P0.4, P0.6)
5. Revise overclaimed language in conclusion (P0.5)
6. Add over-squashing benchmark validation (P1.1)

Without these corrections, the score would remain below 6.0/10 primarily due to unresolved novelty ambiguity and validity concerns about configuration over-tuning.