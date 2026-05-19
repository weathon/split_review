## Summary
# Final Review Report

## Summary

This paper proposes LayerDAG, a generative model for Directed Acyclic Graphs that combines autoregressive generation with discrete diffusion models. The core technical insight is a **layerwise tokenization** of DAGs: rather than generating nodes one at a time (as in D-VAE) or in fixed-size sets (as in GraphPNAS), LayerDAG decomposes a DAG into a *unique* ordered sequence of bipartite graphs, where each layer corresponds to a set of incomparable nodes and their incoming edges from previous layers. Directional dependencies across layers are modeled through autoregression, while logical dependencies within each layer are captured via D3PM-based discrete diffusion. The method also introduces a layer-index-based denoising schedule that allocates more diffusion steps to deeper layers.

The paper targets a practically important application domain: generating synthetic DAGs for system and hardware benchmarking, where collecting real execution-traced DAGs is expensive and risks IP leakage. Experiments span a synthetic dataset (LP) with hard logical constraints and three real-world datasets (TPU Tile, HLS, NA-Edge). The central evaluation paradigm is *surrogate-based*: generated DAGs are used to train ML surrogate models (BiMPNN, Kaggle-solution), whose prediction accuracy on real test DAGs serves as a proxy for generation quality.

**Key findings:**

- On the LP synthetic dataset, LayerDAG achieves 20% absolute higher validity than baselines (Table 1).
- On three real-world benchmarks, surrogate models trained on LayerDAG-generated DAGs consistently achieve higher Pearson correlation and lower MAE than those trained on baseline-generated DAGs (Table 3).
- In the challenging label-extrapolation setting (TPU Tile, 5th quantile), LayerDAG achieves Pearson = 0.22 where all baselines score near zero or negative (Table 4).
- The layer-index-based denoising schedule offers better quality-efficiency trade-offs than a constant schedule (Figure 2).

**Core strengths:** The layerwise tokenization is a principled and elegant solution to the node-ordering problem in DAG generation. The hybrid autoregressive-diffusion architecture is well-motivated by the dual challenge of directional and logical dependencies. The application to large-scale (up to ~400 nodes) flow graphs for system benchmarking is novel and practically relevant.

**Core weaknesses:** The "first" claim for autoregressive diffusion DAG models needs scoping. The generalization results (Table 4) show positive but modest gains (Pearson ~0.2 vs real-data ~0.8), and the paper overclaims this in the introduction. The surrogate-based evaluation, while pragmatic, is an indirect quality signal. The conclusion lacks a limitations section. Several methodological details (conditional independence assumption, adaptive edge prior sensitivity, layer partition definition precision) need clarification.

## Strengths
**S1. Principled layerwise tokenization.** The core idea of partitioning a DAG into uniquely ordered bipartite-graph layers based on longest-path distance is elegant and well-motivated. It resolves the node-ordering ambiguity that plagues prior autoregressive DAG models (D-VAE, GraphPNAS) while preserving the inductive bias of partial-order structure. The claim of permutation invariance (Proposition 3.1) follows naturally from this design.

**S2. Targeted hybrid architecture.** The combination of autoregression (for cross-layer directional dependencies) and discrete diffusion (for intra-layer logical dependencies) is a sensible architectural choice. The paper makes a clear argument for why each component is needed — autoregression handles the sequential nature of DAG layers, while diffusion captures complex attribute-edge interactions within the incomparable node sets of each layer — and validates this through ablation (OneShotDAG without autoregression, LayerDAG (T=1) without multi-step refinement).

**S3. Practical application framing.** The paper targets a genuine and high-impact practical problem: generating synthetic DAGs for computing-system benchmarking without exposing proprietary workload information. The three real-world datasets (TPU Tile, HLS, NA-Edge) cover diverse hardware platforms and are appropriately sized (thousands of graphs, up to ~400 nodes). The surrogate-ML evaluation paradigm, while indirect, is a pragmatic response to the infeasibility of direct hardware measurement.

**S4. Strong empirical results on synthetic data.** On the LP dataset (Table 1), LayerDAG achieves 56-96% validity across constraint levels, consistently outperforming baselines by 20% absolute or more under strict constraints. This convincingly demonstrates that the hybrid architecture can learn hard logical rules from data.

**S5. Outperforms baselines in the challenging extrapolation setting.** In the label generalization experiment (Table 4), LayerDAG is the only method that achieves a positive Pearson correlation in both extrapolation (0.22) and interpolation (0.19) settings, while all baselines hover near zero or negative. This suggests that the autoregressive-diffusion combination provides genuine, though preliminary, generalization benefits.

**S6. Computational efficiency analysis.** The layer-index-based denoising schedule (Section 3.4, Figure 2) and its evaluation provide useful practical guidance for users who need to balance generation quality against computational budget. The linear schedule consistently outperforms the constant schedule, validating the intuition that deeper layers need more denoising steps.

**S7. Open-source implementation.** The code is publicly available on GitHub, supporting reproducibility and future comparisons.

## Weaknesses
### W1. Claim-evidence inconsistency on generalization (Major)
**Page 3 — Introduction (experiment overview):** The introduction states "LayerDAG demonstrates a superior generalization capability" but the results section (Page 10 — Section 5.3) describes the same result as "modest for practical usage." The actual numbers (Pearson = 0.22 vs. real-data upper bound 0.81) support the "modest" characterization, not "superior." This inconsistency undermines reader trust and should be resolved by aligning the introduction's claim with the actual evidence.

### W2. Novelty claim needs scoping (Major)
**Page 3 — Introduction (paragraph 6):** The paper states "our work is the first to use autoregressive diffusion models for DAG generation" without sufficient scoping. While the specific *layerwise tokenization + diffusion-per-layer* combination is novel, the broader category of "autoregressive diffusion models" has prior art (ARDMs, Hoogeboom et al. 2021a; EDGE, Chen et al. 2023; GRAPHARM, Kong et al. 2023). The paper cites these in Related Work but does not clearly delineate what differentiates LayerDAG from them. The "first" claim should be scoped to the specific technical contribution (layerwise bipartite-graph tokenization with per-layer discrete diffusion) rather than the broad "autoregressive diffusion for DAGs."

### W3. Surrogate-based evaluation limitation not acknowledged (Major)
**Page 9 — Evaluation (section 5.2):** The ML-surrogate evaluation paradigm is clever and practical, but the paper does not acknowledge its fundamental limitation: generation quality is assessed indirectly through how well generated DAGs train *another model*. This creates a double dependency — poor surrogate training could mask good generation, and vice versa. Without even a small-scale direct validation on hardware (e.g., synthesizing a handful of generated DAGs on FPGA), the evaluation chain remains uncalibrated.

### W4. Missing limitations discussion in conclusion (Major)
**Page 10 — Conclusion:** The conclusion is only one paragraph and does not follow the standard structure of (1) validated findings, (2) bounded limitations, (3) future directions. There is no discussion of limitations despite several being identifiable from the paper (surrogate evaluation, computational cost of multi-step diffusion, error propagation from node-count prediction). This omission weakens the paper's scientific completeness.

### W5. Incomplete permutation invariance justification (Minor)
**Page 6 — Section 3.3:** The permutation invariance argument claims that BiMPNN layers are permutation equivariant and pooling is permutation invariant, therefore LayerDAG is permutation invariant. However, the argument does not explicitly connect the *set-based processing* within each layer (transformer without positional encodings) to the invariance claim. Since the layerwise partition is unique, invariance only needs to hold *within* each layer, and the set-based processing ensures this — but this connection should be made explicit.

### W6. Imprecise layer partition definition (Minor)
**Page 4 — Section 3.1:** The definition "V(l+1) ⊂ V \ V(≤l) to be the set of nodes whose predecessors are in V(≤l)" is ambiguous: it could be read as requiring *any* predecessor in V(≤l), when the correct interpretation (consistent with the longest-path characterization) requires *all* predecessors to be in V(≤l). The definition should be tightened for clarity.

### W7. Conditional independence assumption undiscussed (Minor)
**Page 5 — Section 3.2 (autoregressive generation):** The factorization P(G) = ∏ P(|V|) · P(X | |V|) · P(A | X) assumes conditional independence among node count, attributes, and edges. This is a strong modeling assumption that is not discussed. If the node count prediction is incorrect, subsequent attribute and edge generation will be conditioned on wrong sizes, creating error propagation.

### W8. Adaptive edge prior sensitivity unanalyzed (Minor)
**Page 15 — Appendix A:** The adaptive edge prior min(|V(≤l)|, din) / |V(≤l)| depends on the predicted layer size |V(≤l)|. If the autoregressive size prediction is inaccurate, the edge prior shifts in ways not accounted for. No ablation study or sensitivity analysis is provided for this component.

## Key Issues
The following ranked error board presents the top-priority issues ordered by severity and research-value impact.

### Ranked Error Board

| Rank | Issue | Severity | Validity Risk | Research-Value Impact | Fixability | Confidence |
|------|-------|----------|--------------|----------------------|------------|------------|
| 1 | Claim-evidence inconsistency on generalization (W1) | Major | Medium — does not invalidate claims but erodes trust | High — introduction overstates core finding | High — simple rewording needed | High |
| 2 | Surrogate evaluation limitation unacknowledged (W3) | Major | Medium — evaluation chain is indirect | High — affects how results should be interpreted | High — add limitation paragraph | High |
| 3 | Missing limitations in conclusion (W4) | Major | Low — does not affect validity | Medium — completeness issue | High — one-paragraph addition | High |
| 4 | Novelty claim needs scoping (W2) | Major | Medium — risk of novelty rejection if unqualified | High — affects contribution perception | Medium — requires careful rewording + literature context | High |
| 5 | Conditional independence assumption undiscussed (W7) | Minor | Low — standard design choice | Medium — affects understanding of failure modes | High — add one-sentence discussion | High |
| 6 | Imprecise layer partition definition (W6) | Minor | Low — can be resolved by context | Low | High — tighten wording | High |
| 7 | Incomplete permutation invariance justification (W5) | Minor | Low | Low | High — add explicit connection | High |
| 8 | Adaptive edge prior sensitivity unanalyzed (W8) | Minor | Low — likely impact is small | Low | Medium — add ablation or discussion | Medium |

**Key Takeaway:** No fatal flaws were identified. The core technical contribution (layerwise tokenization + hybrid autoregressive-diffusion generation) is sound and empirically validated. The main weaknesses are in *presentation* (claim-evidence inconsistency, missing limitations) and *completeness* (undiscussed assumptions, unacknowledged evaluation limitations). All issues are fixable within a standard revision cycle.

## Actionable Suggestions
### Suggestion A (Priority: Must) — Align claim-evidence on generalization
**Affected areas:** Page 3 — Introduction (experiment overview paragraph), Page 10 — Section 5.3 (label generalization)

**Problem:** The introduction claims "superior generalization capability" while the results section calls the same findings "modest for practical usage."

**Action:** Replace "superior generalization capability" with a qualified statement in the introduction, e.g.: "LayerDAG demonstrates positive correlation (Pearson = 0.22) in the challenging extrapolation setting where all baselines fail to achieve positive correlation, though absolute performance remains modest compared to real-data upper bounds."

### Suggestion B (Priority: Must) — Add limitations section to conclusion
**Affected area:** Page 10 — Conclusion

**Problem:** The conclusion is one paragraph without limitations or future work.

**Action:** Restructure the conclusion into three parts: (1) one sentence summarizing validated findings, (2) 2-3 sentences on bounded limitations (surrogate evaluation, multi-step diffusion cost, error propagation from size prediction), (3) 1-2 sentences on future work priorities.

**Mentor Revised Version:** (Provided in the Conclusion annotation on Page 10)

### Suggestion C (Priority: Must) — Scope the novelty claim
**Affected area:** Page 3 — Introduction paragraph 6

**Problem:** "First to use autoregressive diffusion models for DAG generation" is too broad and risks contradiction with prior hybrid models (ARDMs, EDGE, GRAPHARM).

**Action:** Replace with a scoped claim: "To our knowledge, this end, we propose the first DAG generation model that combines autoregressive layerwise tokenization with per-layer discrete diffusion, enabling joint modeling of directional dependencies across layers and intra-layer logical dependencies that prior autoregressive or diffusion-only approaches cannot capture simultaneously." Then explicitly state in the Related Work section how LayerDAG differs from ARDMs, EDGE, and GRAPHARM (e.g., "Unlike EDGE and GRAPHARM, which perform one denoising step per edge generation, LayerDAG performs multi-step refinement within each autoregressive layer generation.")

### Suggestion D (Priority: Must) — Acknowledge surrogate evaluation limitation
**Affected area:** Page 9 — Evaluation section 5.2

**Problem:** The surrogate-based evaluation is presented as the primary evaluation method without acknowledging its indirect nature.

**Action:** Add the following sentence after the evaluation description: "We note that ML-based surrogate evaluation provides an indirect measure of generation quality; the ultimate benchmark would be direct measurement on the target hardware platform. However, such direct evaluation is often infeasible due to access constraints, making surrogate evaluation a practical alternative commonly adopted in system optimization literature [citations]."

### Suggestion E (Priority: Nice-to-have) — Tighten layer partition definition
**Affected area:** Page 4 — Section 3.1

**Problem:** The set definition for V(l+1) is ambiguous.

**Action:** Replace "the set of nodes whose predecessors are in V(≤l)" with "the set of nodes v ∈ V \ V(≤l) such that *all* predecessors of v are in V(≤l), and at least one predecessor is in V(l)." This matches the longest-path characterization and ensures uniqueness.

### Suggestion F (Priority: Nice-to-have) — Discuss conditional independence assumption
**Affected area:** Page 5 — Section 3.2 (autoregressive generation)

**Action:** Add: "This factorization assumes conditional independence among node count, attributes, and edges given preceding layers. While simplifying training, it implies that node-count prediction errors propagate without correction to subsequent attribute and edge generation."

### Suggestion G (Priority: Nice-to-have) — Add significance testing
**Affected area:** Page 8-9 — Tables 1 and 3

**Action:** Add statistical significance indicators (e.g., bold with p < 0.05 under paired bootstrap across seeds) to Tables 1 and 3 for key comparisons, especially where margins are small (Table 3, TPU Tile and NA-Edge results).

### Suggestion H (Priority: Nice-to-have) — Strengthen permutation invariance argument
**Affected area:** Page 6 — Section 3.3

**Action:** Add an explicit connection: "Permutation invariance holds because (i) the layerwise partition is unique, and (ii) within each layer, node attributes are processed by a transformer without positional encodings and edges are predicted from set-based node representations — both are permutation-invariant operations when conditioned on the preceding layers."

### Suggestion I (Priority: Nice-to-have) — Restructure Related Work
**Affected area:** Page 7 — Related Work (Section 4)

**Action:** Reorganize around 2-3 explicit comparison axes: tokenization strategy (node-wise / set-wise / layer-wise), dependency modeling approach (autoregressive / diffusion / hybrid), and scalability regime (small NAS graphs vs large flow graphs). Use the three-axis framing provided in the annotation on Page 7.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: DAG definitions and domain applications (literature catalog)
- P2: Why collecting real DAGs is hard (motivation)
- P3: Three benefits of DAG generative models
- P4: Challenges of generating DAGs (directional + logical dependencies)
- P5: LayerDAG approach description
- P6: Comparison with prior work + novelty claim
- P7: Experiment preview

**Diagnosis:** The current structure is information-complete but not optimally ordered for reader engagement. The primary issue is that the specific *research gap* (what existing methods cannot do) is not clearly stated until P6, which is too late. A more effective arc would establish the gap earlier and build tension toward the solution.

### Storyline Option A (Recommended)

**Arc:** Problem → Gap → Solution → Evidence → Contribution

- **P1 (Stakes):** DAGs are critical for system benchmarking, but collecting real DAGs is costly and risks IP leakage. (Combine current P1 motivation with P2 data challenge — cut the domain list to 2-3 key examples.)

- **P2 (Gap):** Existing DAG generative models face three limitations: (i) they impose artificial ordering on incomparable nodes (D-VAE, GraphPNAS), (ii) they lack expressive joint modeling of nodes and edges within a set (GraphPNAS), and (iii) they are limited to small graphs (≤24 nodes). These limitations prevent modeling strong directional and logical dependencies at scale.

- **P3 (Idea):** We propose LayerDAG, which decomposes a DAG into a unique sequence of bipartite graphs. Directional dependencies are modeled through autoregression across layers; logical dependencies within each layer are captured via discrete diffusion.

- **P4 (Evidence preview):** On synthetic DAGs with hard constraints, LayerDAG achieves up to 20% higher validity. On three real-world benchmarks, surrogate models trained on LayerDAG-generated DAGs consistently outperform those trained on baseline-generated DAGs. In the challenging extrapolation setting, LayerDAG is the only method achieving positive correlation.

- **P5 (Contributions):** Explicitly list 3 contributions: (C1) layerwise tokenization that respects partial-order structure, (C2) hybrid autoregressive-diffusion framework for joint directional-logical dependency modeling, (C3) scalable generation of flow graphs up to ~400 nodes for system benchmarking.

**Alignment checks:**
- Problem alignment: The stated challenge (collecting real DAGs is hard) matches the proposed solution (generating synthetic DAGs). ✓
- Variable alignment: "Layerwise tokenization", "bipartite graph", "autoregressive", "diffusion" appear as method variables. ✓
- Contribution-evidence alignment: C1 is validated by validity results (Table 1), C2 by ablation studies, C3 by TPU Tile/HLS/NA-Edge results (Tables 3-4). ✓

### Storyline Option B (Application-First)

**Arc:** Application Scenario → Technical Challenge → Solution → Impact

Focus the introduction on the system benchmarking application (TPU, FPGA, edge devices) from the start, positioning DAG generation as an enabling technology for hardware-software co-design. This option is better for a systems/hardware audience.

### Storyline Option C (Method-First)

**Arc:** Technical Problem → Insight → Method → Validation

Focus on the ordering problem in DAG generation (non-unique topological orderings) as the central technical challenge. Lead with the permutation invariance issue, then introduce layerwise tokenization as the resolution. This option is better for a graph-generation/ML audience.

### Abstract Outline

**S1 (Problem + Domain):** "Directed acyclic graphs (DAGs) are essential for modeling workloads in computing-system benchmarking, but collecting large-scale real DAGs is costly and risks intellectual-property leakage."

**S2 (Prior Limitation):** "Existing DAG generative models impose artificial ordering on structurally incomparable nodes and are limited to small graphs (≤24 nodes for neural architecture search), preventing them from capturing the strong directional and logical dependencies in larger flow graphs."

**S3 (Method):** "We propose LayerDAG, which decomposes DAG generation into a sequence of bipartite graphs — one per layer of the partial order — modeling directional dependencies via autoregression and intra-layer logical dependencies via discrete diffusion."

**S4 (Key Result):** "On a synthetic DAG dataset with hard logical constraints, LayerDAG improves validity by up to 20% absolute over baselines. On three real-world benchmarks (TPU, FPGA, edge devices) with up to 400 nodes, surrogate models trained on LayerDAG-generated DAGs consistently outperform those trained on baseline-generated DAGs."

**S5 (Bounded Implication + Code):** "LayerDAG also shows positive correlation (Pearson = 0.22) in the challenging label-extrapolation setting where all baselines fail. Code is available at https://github.com/Graph-COM/LayerDAG."

### Introduction Outline (Following Storyline Option A)

**P1 (Stakes):** Open with DAGs as critical for system benchmarking. Highlight the cost and IP challenges of collecting real DAGs. End with: "This motivates generative models that can produce realistic, large-scale synthetic DAGs."

**P2 (Gap):** State the three limitations of prior work: (i) node-ordering imposition violates partial-order structure, (ii) limited expressiveness for set-level dependencies, (iii) capped at small graphs. End with: "These limitations become critical when generating DAGs with strong directional and logical dependencies at practical scales."

**P3 (Idea):** Introduce layerwise tokenization and the hybrid autoregressive-diffusion architecture. Use Fig. 1 as the visual anchor. Keep technical details to a minimum; focus on the *why* rather than the *how*.

**P4 (Evidence Preview):** Present the four research questions (Q1-Q4) and key outcomes. Use specific numbers sparingly; focus on the pattern of results.

**P5 (Contributions):** Three-item bullet list covering C1, C2, C3 as defined above.

## Priority Revision Plan
### P0 — Publication-Critical (must address before resubmission)

| # | Task | Effort | Impact | Reference |
|---|------|--------|--------|-----------|
| 1 | Align introduction generalization claim with results (Pearson = 0.22 is "modest," not "superior") | 1 hour | High — fixes claim-evidence inconsistency (W1) | Suggestion A |
| 2 | Scope "first to use autoregressive diffusion" with precise technical qualifiers | 1 hour | High — reduces novelty-rejection risk (W2) | Suggestion C |
| 3 | Add limitations paragraph to conclusion | 1 hour | Medium — scientific completeness (W4) | Suggestion B |
| 4 | Acknowledge surrogate evaluation as indirect signal | 30 min | Medium — transparency (W3) | Suggestion D |

### P1 — High Priority

| # | Task | Effort | Impact | Reference |
|---|------|--------|--------|-----------|
| 5 | Tighten layer partition definition (V(l+1)) for precision | 30 min | Medium — reproducibility (W6) | Suggestion E |
| 6 | Discuss conditional independence assumption | 15 min | Medium — technical completeness (W7) | Suggestion F |
| 7 | Add explicit connection between set-based processing and permutation invariance | 15 min | Low — completeness (W5) | Suggestion H |

### P2 — Quality Improvements (if time permits)

| # | Task | Effort | Impact | Reference |
|---|------|--------|--------|-----------|
| 8 | Restructure Related Work along comparison axes | 2-3 hours | Medium — readability | Suggestion I |
| 9 | Add significance indicators to Tables 1, 3 | 1-2 hours | Medium — statistical rigor | Suggestion G |
| 10 | Add ablation/analysis of adaptive edge prior sensitivity | 1-2 days | Low-Medium — technical depth | Suggestion I (appendix) |
| 11 | Implement Storyline Option A for introduction rewrite | 3-4 hours | Medium — narrative quality | Storyline Options |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: Claim-evidence inconsistency (W1)]
    -> [Fix: Replace 'superior' with 'positive but modest' in intro]
    -> [Expected impact: Aligned narrative, increased trust]

[Problem: Novelty claim overreach (W2)]
    -> [Fix: Scope 'first' claim to layerwise tokenization + per-layer diffusion]
    -> [Expected impact: Reduced novelty-rejection risk]

[Problem: Missing limitations (W4)]
    -> [Fix: Add 3-part conclusion: findings + limitations + future work]
    -> [Expected impact: Scientific completeness]

[Problem: Indirect evaluation unacknowledged (W3)]
    -> [Fix: Add caveat sentence about surrogate evaluation]
    -> [Expected impact: Methodological transparency]

[Problem: Imprecise definitions (W6, W7)]
    -> [Fix: Tighten V(l+1) definition, discuss assumptions]
    -> [Expected impact: Improved reproducibility]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 (Sec 5.1) | Can LayerDAG learn hard logical constraints from data? | LP synthetic dataset, ρ ∈ {0,0.5,1}; compare vs D-VAE, GraphRNN, GraphPNAS, OneShotDAG | Validity (↑), W1-L, MMD-\|V(l)\| | LayerDAG achieves 56-96% validity, +20% absolute vs baselines | C1 (layerwise tokenization captures constraints) | Only tests binary attribute balance; other constraint types untested |
| E2 (Sec 5.2) | Can LayerDAG perform conditional generation matching real data distributions? | TPU Tile (6,301 graphs), HLS (2,062), NA-Edge (2,000); surrogate ML evaluation with BiMPNN | Pearson (↑), MAE (↓), W1-L, MMD-\|V(l)\| | LayerDAG achieves best Pearson/MAE on all 3 datasets | C2 (hybrid AR+diffusion enables conditional gen) | Surrogate evaluation is indirect; no direct hardware validation |
| E3 (Sec 5.3) | Can LayerDAG generalize to unseen label regimes? | TPU Tile, 5-quantile split; 5th (extrapolation) and 4th (interpolation) held out | Pearson, MAE, W1-L, MMD-\|V(l)\| | Only LayerDAG achieves positive Pearson (0.22 extrapolation, 0.19 interpolation) | C3 (generalization to OOD labels) | Gains are modest vs real data (Δ=0.6); single dataset tested |
| E4 (Sec 5.4) | Does layer-index-based denoising schedule improve quality-efficiency trade-off? | LP (ρ=0), TPU Tile, HLS; linear vs constant schedule | Ratio of max validity/Pearson vs ratio of max time | Linear schedule consistently outperforms constant | Layer-index-based schedule claim | Only tested on 3 datasets; theoretical justification thin |
| E5 (Appendix D) | Can LayerDAG generate valid node attributes? | Extended LP (3 binary attributes, ρ=0); D-VAE vs GraphRNN vs LayerDAG | Balance validity, attribute validity, full validity, W1-L, MMD-\|V(l)\|, MMD-attribute | LayerDAG achieves best on all metrics | Attribute generation quality | Only 2 baselines compared; small-scale dataset |

### Research-Theme Gap Diagnosis

The current experimental evaluation covers Q1-Q4 comprehensively but leaves three research-value gaps:

1. **Direct validation gap (New Knowledge):** All real-world evaluations rely on ML-surrogate models. While practical, this means the paper has not directly demonstrated that generated DAGs, when executed on actual hardware, produce realistic performance metrics. This limits the *impact on practice* dimension of research value.

2. **Failure-mode analysis gap (Reproducibility):** The paper reports average-case performance but does not systematically analyze *when* LayerDAG fails. For example, are DAGs with many layers (L > 20) more likely to violate constraints? Are certain attribute combinations systematically missed? Understanding failure modes is critical for practical deployment.

3. **Scalability boundary gap (Robustness):** The paper demonstrates generation up to ~400 nodes (TPU Tile max). It does not test whether performance degrades at larger scales (e.g., 1000+ nodes) or whether there is a practical upper bound on the number of layers the autoregressive process can handle before error accumulation degrades quality.

### Proposed Research Experiments

#### P0 Experiments (High Priority, Before Resubmission)

**Exp P0-1: Direct hardware validation on a small subset**
- **Target Claim:** LayerDAG generates DAGs with realistic hardware performance.
- **Hypothesis:** Generated DAG performance, when measured on actual hardware, correlates with real DAG performance at a level comparable to the surrogate evaluation.
- **Minimal Design:** Select 50 generated DAGs and 50 real DAGs from the HLS dataset. Implement them on FPGA; measure LUT usage. Compare measured vs predicted values.
- **Controls:** Same compilation flow for generated and real DAGs.
- **Metrics:** Pearson correlation between measured and predicted LUT usage.
- **Success Criterion:** Pearson > 0.8 within generated-DAG set; no systematic bias in error distribution.
- **Estimated Cost/Time:** 2-4 weeks (requires hardware access and implementation expertise).
- **Expected Paper-Quality Gain:** High — would transform the evaluation from indirect to direct, substantially strengthening the practical-impact claim.

**Exp P0-2: Failure-case analysis**
- **Target Claim:** LayerDAG reliably generates valid DAGs across diverse conditions.
- **Hypothesis:** Generation failures (invalid DAGs) are concentrated in specific regimes (e.g., many layers, extreme attribute configurations).
- **Minimal Design:** For the LP dataset, stratify generated DAGs by L and |V(l)|; compute validity per stratum. For real datasets, analyze which generated DAGs have the largest surrogate prediction errors.
- **Controls:** Compare against baseline failure distributions.
- **Metrics:** Validity as a function of L and layer size; error distribution quantiles.
- **Success Criterion:** Clear characterization of failure modes; identification of 1-2 actionable improvement directions.
- **Estimated Cost/Time:** 1-2 weeks (computational analysis only).
- **Expected Paper-Quality Gain:** Medium — would improve reproducibility and practical guidance.

#### P1 Experiments (Next Revision)

**Exp P1-1: Adaptive edge prior ablation**
- **Target Claim:** The adaptive edge prior (Appendix A) improves generation quality.
- **Hypothesis:** A fixed edge prior (constant probability) produces worse validity and graph statistics.
- **Minimal Design:** Compare LayerDAG (adaptive prior) vs LayerDAG (fixed prior, set to average edge density in training data) on LP (ρ=0) and TPU Tile.
- **Metrics:** Validity, W1-L, MMD-|V(l)|.
- **Success Criterion:** Adaptive prior achieves >5% validity improvement.
- **Estimated Cost/Time:** 1 week.
- **Expected Paper-Quality Gain:** Medium — adds ablation depth for a claimed innovation.

**Exp P1-2: Larger-scale stress test**
- **Target Claim:** LayerDAG scales to larger DAGs than tested.
- **Hypothesis:** LayerDAG maintains reasonable validity at 500+ nodes with moderate layer counts.
- **Minimal Design:** Create a synthetic dataset with 500-1000 nodes (using a known generative process). Train and evaluate LayerDAG on this dataset.
- **Metrics:** Validity, generation time scaling, memory usage.
- **Success Criterion:** Validity > 50% at 500+ nodes with generation time growing sub-quadratically in node count.
- **Estimated Cost/Time:** 2-3 weeks.
- **Expected Paper-Quality Gain:** Medium — would strengthen the scalability claim (C3).

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Before Resubmission)
├── P0-1: Direct hardware validation (HLS → FPGA measurement)
│   └── Expected: Transformative — indirect → direct evaluation
├── P0-2: Failure-case analysis (stratify validity by L, |V(l)|)
│   └── Expected: Reproducibility + practical guidance

P1 (Next Revision)
├── P1-1: Adaptive edge prior ablation
│   └── Expected: Ablation depth for claimed component
├── P1-2: Larger-scale stress test (500-1000 nodes)
│   └── Expected: Scalability boundary characterization

P2 (Future Work)
├── P2-1: Continuous node attributes via hybrid diffusion
├── P2-2: Comparison with direct measurement on all three platforms
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Scoring Rationale (research value + novelty prioritized):**

The paper earns a 6.5 based on the following assessment:

- **Research Value (7/10):** The problem of generating realistic synthetic DAGs for system benchmarking is genuinely important and well-motivated. The three real-world datasets (TPU, FPGA, edge devices) demonstrate practical relevance. The surrogate-based evaluation framework, while indirect, is a pragmatic approach to a difficult measurement problem. However, the absence of direct hardware validation and the modest generalization results (Pearson = 0.22 vs 0.81 upper bound) temper the practical-impact claim.

- **Novelty (6.5/10):** The layerwise tokenization is a principled and novel contribution to DAG generation. The hybrid autoregressive-diffusion architecture is well-conceived. However, the "first" claim for autoregressive diffusion models for DAGs needs careful scoping (ARDMs, EDGE, GRAPHARM explore adjacent territory). The permutation invariance argument, while valid, builds on known properties of BiMPNN and set pooling. The overall novelty is solid but incremental — a well-executed combination of existing building blocks rather than a fundamentally new paradigm.

- **Validity/Soundness (7/10):** The method is technically sound, the proof-of-concept diffusion implementation (D3PM) is appropriate, and the ablation studies (OneShotDAG, T=1) convincingly isolate the contributions of autoregressive and diffusion components. The main validity concerns are the indirect evaluation (surrogate models) and the claim-evidence inconsistency on generalization.

- **Reproducibility (6/10):** The method description is mostly complete, and code is publicly available. However, imprecise definitions in the layer partition (Sec 3.1), the undiscussed conditional independence assumption, and missing hyperparameters for the diffusion process (number of steps T_min, T_max, hidden dimensions) reduce reproducibility. The GitHub repository availability is a strong positive.

- **Presentation (6/10):** The paper is well-structured with clear figures. However, the introduction overclaims ("superior generalization"), the related work is a literature list rather than a structured comparison, and the conclusion lacks limitations. Abstract language could be tighter.

**Post-Revision Target: [7.0, 7.5] / 10**

If the P0 and P1 revision items are fully addressed:
- Claim-evidence inconsistency resolved (+0.3)
- Novelty claim properly scoped (+0.2)
- Limitations added to conclusion (+0.1)
- Surrogate evaluation limitation acknowledged (+0.1)
- Direct hardware validation on a subset (P0-1) (+0.2)
- Failure-case analysis added (P0-2) (+0.1)

The maximum achievable score after a thorough revision is approximately 7.5/10, bounded by the inherent limitations of the surrogate evaluation paradigm and the modest generalization numbers, which no amount of rewriting can change.

---

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|-----------------|-------|
| 1 | 2 | Covered | Abstract + Intro P1 |
| 2 | 4 | Covered | Intro P2, P3, P4, P5 (4 paragraphs) |
| 3 | 2 | Covered | Intro P6, P7 |
| 4 | 1 | Covered | Methodology 3.1 (layer partition) |
| 5 | 1 | Covered | Methodology 3.2 (autoregressive factorization) |
| 6 | 1 | Covered | Methodology 3.3 (permutation invariance) |
| 7 | 1 | Covered | Related Work |
| 8 | 1 | Covered | LP results (Table 1) |
| 9 | 1 | Covered | Conditional generation evaluation |
| 10 | 2 | Covered | Label generalization + Conclusion |
| 15 (Appendix A) | 1 | Covered | Adaptive edge prior discussion |
| 16-18 (Appendices C-F) | 0 | Skipped | Dataset construction details, experiment details — these are supplementary descriptions that do not affect core claims. No substantive issues found. |

**Total: 17 annotations across 12 pages. Main-body substantive paragraphs all covered. Appendix D-F skipped as non-substantive supplementary material.**

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Real DAGs are expensive/IP-sensitive to collect]
    |
    v
[C1: Layerwise tokenization (unique bipartite-graph sequence)]
    |--- Evidence: LP validity (Table 1): +20% absolute over baselines
    |--- Evidence: Permutation invariance (Prop 3.1)
    |
    v
[C2: Hybrid AR+Diffusion for DAG generation]
    |--- Evidence: Ablation (OneShotDAG < LayerDAG (T=1) < LayerDAG)
    |--- Evidence: Conditional gen (Table 3): best Pearson/MAE on 3 datasets
    |
    v
[C3: Scalable generation for system benchmarking (up to ~400 nodes)]
    |--- Evidence: TPU Tile (max 394 nodes), HLS (max 356), NA-Edge (max 339)
    |--- Evidence: Label generalization (Table 4): positive Pearson where baselines fail
    |
    v
[Gap: Indirect surrogate evaluation; modest extrapolation gains]
    |--- Risk: No direct hardware validation
    |--- Risk: Pearson = 0.22 vs real 0.81 in extrapolation
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Related Work: DAG and Graph Generative Models
├── Branch 1: Node-wise Autoregressive Models
│   ├── Leaf 1.1: Undirected graphs — GraphRNN, DeepGMG
│   └── Leaf 1.2: Directed DAGs — D-VAE (topological ordering)
│       Common limitation: impose artificial order; one node per step
│
├── Branch 2: Set-wise Autoregressive Models
│   ├── Leaf 2.1: Undirected graphs — GRAN (constant-size node sets)
│   └── Leaf 2.2: Directed DAGs — GraphPNAS (constant-size sets, Bernoulli mixture)
│       Common limitation: fixed token size; less expressive set modeling
│
├── Branch 3: Diffusion Models
│   ├── Leaf 3.1: Continuous diffusion — Niu et al., GDSS
│   ├── Leaf 3.2: Discrete diffusion — DiGress, GraphMaker
│   └── Leaf 3.3: Conditional diffusion — DiffusionNAG (attributes only, fixed structure)
│       Common limitation: no directional dependency modeling
│
└── Branch 4: Hybrid Autoregressive-Diffusion Models
    ├── Leaf 4.1: Time series — TimeGrad
    ├── Leaf 4.2: General graphs — EDGE, GRAPHARM (one diffusion step per edge)
    └── ─── Leaf 4.3: This paper — LayerDAG (multi-step diffusion per layer)
        Key difference from Leaf 4.2: multi-step refinement within each autoregressive step
```