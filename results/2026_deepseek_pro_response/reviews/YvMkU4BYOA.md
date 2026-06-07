Now I have a clear picture. Let me finalize.

**Round 1 bracket**: XBIC sits between ~4.5 and ~6.0. It is clearly better than the kernel selection paper (4.40, too incremental) but weaker than the meta-learning Bayesian causal discovery paper (6.00, more theoretical depth).

**Round 2 narrowing**: Compared against:
- **ljZFM2mhbR (5.00, Reject)**: DAG-SHAP — Shapley + causal graphs, similar topical space. Novel idea, decent experiments, but lacks theoretical guarantees and requires known DAG. XBIC is comparable: reverses the direction (Shapley→discovery), has more extensive experiments (10 networks, 700 runs), but has its own evaluation flaw (random PDAG orientation). Roughly similar level.
- **Lxst78Rrwj (5.00, Reject)**: Distributional invariance for causal discovery. Novel heuristic, extensive experiments, but downsampling lacks theoretical guarantee. XBIC is comparable — similar gap in theoretical justification.
- **3n6DYH3cIP (5.60, Accept)**: Extendable BN structure learning. Has theoretical lemmas, strong runtime gains. XBIC is weaker — lacks equivalent theoretical grounding.
- **jE6VXUhxq9 (6.25, Reject)**: Causal discovery with deterministic relations. Has both theory and extensive experiments. XBIC is clearly weaker.

XBIC lands at **5.0**. The novel conceptual reversal and extensive empirical validation are genuine strengths, but the random PDAG orientation issue significantly undermines the PC/GES comparisons, and the Shapley→causal link is heuristic rather than theoretically grounded. These two issues prevent the paper from reaching the 5.5+ range where the more rigorous anchors sit.

---

## Summary

This paper proposes XBIC, a modification of the BIC score for discrete causal discovery that soft-weights the complexity penalty using Shapley values from per-node XGBoost classifiers. The idea is that if feature Xⱼ is more predictively important for Xᵢ than vice versa, the edge Xⱼ → Xᵢ receives a reduced penalty during hill-climbing search, thereby helping break ties within Markov equivalence classes. The method is evaluated on 10 benchmark discrete Bayesian networks across 7 sample-size regimes (700 runs), showing consistent improvements in directed-edge F₁ over BIC hill-climbing (+5.6%), GES (+9.6%), and PC (+20.9%).

## Strengths

- **Novel conceptual reversal: using explanations to aid causal discovery.** Prior work at the causality–explainability interface uniformly assumes a known or partially known causal graph to constrain or reinterpret Shapley explanations (Frye et al. 2020; Heskes et al. 2020; Wang et al. 2021). XBIC inverts this paradigm by using local Shapley attributions computed when the graph is *unknown* to inform structure learning itself (Section 2.2, lines 48–53; Section 2.3, lines 56–58). This opens a genuinely underexplored direction and is clearly distinguished from adjacent Shapley-guided work such as CAGE (Breuer et al. 2024, global explanations), CD-RCA (Yokoyama et al. 2024, time-series diagnosis), and ReX (Renero et al. 2025, continuous-only pruning).

- **Principled BIC extension that preserves asymptotic consistency.** The XBIC score (Equation 2, lines 107–113) factors the penalty as (log N / 2) × [dim(G) / exp(w·SHAP(G))]. For bounded SHAP(G), this still grows as O(log N), preserving large-sample consistency. When w = 0 or SHAP(G) = 0, XBIC reduces exactly to BIC (line 113; consistency remarks lines 155–159), providing a clean theoretical safety net — the method never does worse than BIC when directional evidence is absent.

- **Extensive empirical validation.** The evaluation spans 10 benchmark discrete BNs (6–76 nodes) from the bnlearn repository covering medical, cell biology, insurance, weather, wastewater, transport, and software domains (Table 1, lines 177–188), tested across 7 geometrically-spaced sample-size regimes with 10 repetitions each (700 total runs). The per-network per-sample-size F₁ delta table (Table 2) and aggregate results (Table 4) provide fine-grained evidence. Gains are confirmed by adjusted Friedman and Wilcoxon signed-rank tests (lines 241–242).

- **Natural ablation via the w parameter.** Setting w ∈ {1, 2, 3} (with w = 0 recovering BIC) provides a built-in ablation. Figure 2 and Table 4 show the precision–recall tradeoff: larger w increases recall at some precision cost, consistent with the mechanism of a softer complexity penalty admitting more edges.

- **Honest treatment of computational cost.** The paper transparently reports wall-clock runtimes (Table 5) showing XBIC is substantially slower than BIC-HC, and flags when GES failed to complete within a 7-day limit. The runtime discussion and parallelization notes are forthright.

## Weaknesses

### Fatal

None.

### Major

- **The Shapley-value-to-causal-direction link is assumed rather than justified.** The method takes Shapley values from predictive XGBoost models trained on observational data and treats their magnitude as evidence for causal edge direction. The paper offers no theoretical or conceptual argument for why predictive attribution asymmetry should track causal asymmetry. A feature Xⱼ can be highly predictive of Xᵢ for reasons unrelated to a direct causal edge Xⱼ → Xᵢ (reverse causation, confounding, associational patterns). The abstract calls XBIC a "principled enhancement" (line 9), and the paper frames the Shapley signal as "directional evidence" (lines 19–20), yet the warrant for this mapping is never established. The limitation acknowledged in the Conclusions — "formal analysis of the weighting mechanism (e.g., bounds and convergence properties) is an important direction" (line 313) — asks for convergence bounds on a mechanism whose basic validity has not been argued. The empirical results are suggestive but do not fill this conceptual gap. The paper would be stronger if it either provided such justification (even under restricted conditions) or explicitly framed XBIC as a heuristic.

- **Random orientation of PDAG edges makes the PC and GES comparisons unreliable.** The paper states (Section 4.1, line 190): "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." PC and GES deliberately leave edges undirected when direction cannot be resolved from the data — this is correct behavior, not a failure. Randomly orienting those edges injects noise into the baseline's output and artificially depresses its directed-edge metrics. The reported +20.9% F₁ improvement over PC and +9.6% over GES are almost certainly inflated by this choice. A fair comparison would evaluate directed-edge metrics only on edges the baseline actually orients, use an SHD variant that treats undirected edges as a separate category, or at minimum report metrics on the PDAG output directly. The paper does report SHD for the GES comparison (Section 4.5) but does not report SHD for PC at all — an omission that is hard to reconcile with the centrality of PC to the headline claims. Note: this issue does **not** affect the BIC-HC comparison, since hill climbing returns a fully directed DAG.

### Minor

- **Small absolute gains relative to computational cost.** Table 4 reports an absolute F₁ improvement over BIC of 0.04 (for w=2). Meanwhile, Table 5 shows XBIC is 25–200× slower than BIC-HC (e.g., Asia: 0.39s → 74.78s; Hailfinder: 36s → 1904s). The paper acknowledges the runtime cost but defers serious grappling with this cost-benefit ratio to future work. For a ~50× average slowdown yielding a 0.04 absolute F₁ gain, a more explicit discussion of when this trade-off is worthwhile would strengthen the paper.

- **Reversals at large sample sizes are not discussed.** Table 2 shows that for several networks at larger sample sizes, XBIC underperforms BIC (e.g., Win95pts at 8M²: Δ = -0.09; Hepar2 at 4M²: Δ = -0.02). These are notable because Shapley evidence should become more reliable with more data, yet XBIC loses ground to standard BIC in exactly these regimes for some networks. The paper discusses small-sample limitations (lines 206–208, 284–285) but does not address or explain these large-sample reversals.

- **Absolute value in SHAP(G) gives equal weight to negative and positive attributions.** Equation 3 defines SHAP(G) = Σ |Φ̄_{j→i}|, meaning negative Shapley values (which indicate features that hurt prediction) receive the same penalty reduction as positive ones. Whether negative attributions should count as "directional support" is unclear and unexamined. This is a specific design choice that could affect results.

- **Absolute baseline F₁ values are not reported.** Table 2 shows only deltas and Table 4 shows relative and absolute improvements, but the baseline absolute F₁ values are never given. Without knowing whether BIC achieves 0.3 or 0.8 F₁, the 5.6% relative improvement is hard to calibrate. Reporting absolute numbers would aid interpretation.

### Trivial

- The paper does not report PC SHD numbers anywhere, even though SHD is reported for the GES comparison (Section 4.5). Since PC's PDAG output would interact differently with SHD computation than with directed-edge F₁, this omission leaves the PC comparison incomplete.

## Nice-to-Haves

- **Skeleton-vs-orientation decomposition.** The paper never reports how much of the F₁ gain comes from better skeleton recovery versus better orientation of a given skeleton. Since the paper's motivation is specifically about orienting edges within equivalence classes (Section 1), this decomposition would directly test the core claim. Comparing XBIC against BIC-HC on the same skeleton (e.g., fixing the skeleton to the ground truth and comparing orientation accuracy) would isolate the value of the Shapley signal.

- **Comparison on oriented edges only.** For PC, restricting evaluation to edges the baseline actually orients (rather than randomly completing its PDAG) would provide a fairer and more informative comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Confidence threshold insensitivity being uninformative.** The harsh critic suggested that τ-insensitivity might mean the filter does little work. The paper already addresses this directly: "suggesting the filter mainly reduces SHAP evaluations without materially affecting accuracy" (line 195). The paper's interpretation is honest and reasonable. Removed.

- **GES selection bias from filtering to completed runs.** The paper explicitly states the filtering is "favorable" to GES (line 278) and compares head-to-head on the same subset. The transparency here is adequate. Removed.

- **Missing related work on cause-effect pairs using regression error asymmetry / additive noise models.** These methods are designed for continuous data; the paper is explicitly about discrete data. The related work section adequately covers adjacent Shapley-guided approaches (CAGE, CD-RCA, ReX). Removed.

- **Mismatch between global SHAP computation and local search scoring.** The SHAP values are computed once globally and summed over edges in the candidate graph during search. This is a reasonable design — the SHAP values estimate directional evidence, and the search finds the DAG whose edges best align with that evidence. There is no genuine mismatch requiring discussion. Removed.

- **Formatting nitpicks, typos, parser artifacts.** These are not author errors. Removed.

## Novel Insights

The paper inverts the prevailing direction in causality–explainability research: rather than using known causal structure to produce better explanations, it uses explanations (Shapley values) to discover causal structure. This conceptual reversal is genuinely novel and opens a fresh research direction. However, the paper does not develop the theoretical underpinnings of why this reversal should work, leaving it as an empirically-motivated heuristic.

## Suggestions

- Reframe the paper to be explicit that XBIC is a heuristic (removing "principled enhancement" unless theoretical justification is added), and treat the empirical results as evidence that the heuristic is effective on benchmark discrete BNs.
- Re-run the PC and GES comparisons using a fair metric: either restrict directed-edge evaluation to edges the baselines actually orient, or use an SHD variant that handles undirected edges appropriately. Report PC SHD alongside the existing GES SHD results.
- Report absolute baseline F₁ values alongside deltas so readers can calibrate the magnitude of improvements.
- Discuss and analyze the cases where XBIC underperforms BIC at large sample sizes (e.g., Win95pts at 8M²).
- Provide even a partial theoretical analysis of when predictive attribution asymmetry should track causal direction (e.g., under faithfulness plus specific functional-form conditions common in discrete BNs).

## Score and Decision

**Anchor comparison summary:**
- **i5JfdnCob7 (4.40, Reject)**: Kernel selection for score-based causal discovery. Too incremental, thin experiments. XBIC is clearly stronger with its novel reversal and 700-run evaluation.
- **ljZFM2mhbR (5.00, Reject)**: DAG-SHAP. Similar Shapley-causal topic, requires known DAG, lacks theoretical guarantees. XBIC is comparable — reverses the direction (more creative), has more extensive experiments, but has its own evaluation flaw (random PDAG orientation).
- **Lxst78Rrwj (5.00, Reject)**: Distributional invariance for causal discovery. Novel heuristic with theoretical gaps. XBIC is comparable in novelty and theoretical depth.
- **3n6DYH3cIP (5.60, Accept)**: Extendable BN structure learning. Has theoretical lemmas and strong runtime gains. XBIC is weaker — lacks equivalent theoretical grounding.
- **eeJz7eDWKO (6.00, Accept)**: Meta-learning Bayesian causal discovery. More theoretical depth and cleaner evaluation. XBIC is weaker.
- **jE6VXUhxq9 (6.25, Reject)**: Causal discovery with deterministic relations. Theory + extensive experiments. XBIC is clearly weaker.

XBIC has a genuinely novel conceptual reversal and extensive experiments, but the random PDAG orientation issue undermines the PC/GES comparisons and the Shapley→causal link lacks theoretical justification. The paper lands at the same level as the DAG-SHAP and distributional invariance anchors — interesting ideas with significant gaps that prevent acceptance at a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>