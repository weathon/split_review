Now I have enough to construct the final consolidated review. Let me finalize it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- Strength 1 — specific evidence from paper
- ...

## Weaknesses
### Fatal
...

### Major
...

### Minor
...

### Trivial
...

## Nice-to-Haves
...

## Removed Points
...

## Novel Insights
...

## Suggestions
...

## Score and Decision

Let me now produce the complete review.

One more check on what the paper says about the ReX paper and whether the distinction is clearly drawn.

I've verified everything needed. Let me write the final review.

Key decisions:
1. The uniform penalty control experiment is the most important gap - Major
2. PDAG evaluation issue - Major
3. No diagnostic test of Shapley directional assumption - Minor
4. Modest absolute improvements - Minor
5. GES subset issue - Minor
6. PC Hailfinder runtime anomaly - Trivial (minor observation)

I'll make the score 5.0 - borderline, with potential but significant gaps.Here is my consolidated meta-review.

## Summary

XBIC augments the BIC score for discrete Bayesian network structure learning by soft-weighting the complexity penalty with edge-specific Shapley values. The idea is that when a candidate parent contributes strongly to predicting its child, the penalty for adding that edge is reduced, providing directional preference within Markov-equivalence classes. Evaluated on ten benchmark networks across seven sample-size regimes (700 runs), XBIC reports oriented-edge F₁ improvements of +5.6% over hill-climbing BIC, +20.9% over PC, and +9.6% over a GES variant.

## Strengths

1. **Novel integration of feature attributions into a score-based causal discovery objective.** Using local Shapley values to modulate the BIC penalty is a creative and underexplored direction. The paper cleanly formulates this as a drop-in modification (Equation 2) that reverts to standard BIC when no directional signal is present (SHAP(G)=0 or w=0), making adoption straightforward in existing BIC-based pipelines.

2. **Extensive and systematic empirical evaluation.** The study covers 10 benchmark networks (6–76 nodes), 7 sample-size regimes, and 700 total runs (Table 4, Section 4.3). Results are reported against three baselines (BIC-HC, PC, GES) with statistical significance tests (adjusted Friedman + Wilcoxon). The hyperparameter search over w values and the τ sensitivity analysis (F₁ varies <1% for τ∈[0.7, 0.95]) are well-executed.

3. **Transparent handling of the Shapley+search pipeline.** The paper describes the three-stage pipeline (per-node classifiers, attribution aggregation, score-based search with caching) clearly, provides Algorithm 1 and Algorithm 2, and characterizes computational costs (Table 5). Code and data splits are released.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control condition: a uniform penalty reduction could explain the gains.** The paper never compares XBIC against a BIC variant with a uniformly scaled penalty (e.g., BIC with penalty coefficient α < 1, or AIC). The Shapley-weighted penalty in Equation 2 is  dim(G)/exp(w·SHAP(G)), which for any fixed graph amounts to dim(G)·c(G) with c(G) a graph-specific shrinkage factor. Figure 2 shows that larger w increases recall while sometimes decreasing precision—exactly the pattern one would expect from a uniformly softer penalty. Without testing whether a standard criterion with a uniformly reduced penalty (e.g., BIC with penalty α·log N/2 for α<1) achieves comparable or identical results, the core claim—that the directional Shapley signal is responsible for the improvements—is unsupported. Paper Section 4.3 and Table 4 report the headline numbers but no such control appears.

2. **PDAG-to-DAG conversion introduces a bias favoring XBIC against PC and GES.** The paper states (line 194): "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." Randomly orienting undirected edges from PC/GES injects noise that artificially lowers their precision and F₁, since XBIC always outputs a fully directed DAG. This is particularly problematic for the 20.9% improvement over PC (Table 4), which is the largest reported gain. The correct approach would separate skeleton recovery (which is fair to all methods) from orientation accuracy (evaluated only on edges that are directed in each output). The paper's evaluation conflates both, making the PC and GES comparisons not credible as reported.

### Minor

3. **No diagnostic evidence that Shapley asymmetry encodes causal direction.** The paper's core premise—that the aggregate Shapley difference between X_j→X_i and X_i→X_j reflects the true causal direction—is asserted intuitively (line 131: "Intuitively, if |φ̄_{1→2}| ≫ |φ̄_{2→1}|, the edge X₁→X₂ has stronger directional support") but never tested in isolation. Shapley values from a predictive classifier capture arbitrary statistical associations (confounded, chained, etc.) with no guarantee of pointing toward true causal parents. No case study on simple identifiable motifs (e.g., a chain X→Y→Z or a confounder X←Z→Y) demonstrates that the asymmetry correctly identifies the true direction. Without this, the mechanism by which XBIC improves orientation remains opaque.

4. **Modest absolute improvements tempered by uneven performance.** The headline relative improvement over BIC is 5.6%, but the absolute F₁ increase is 0.04 (Table 4). Several networks show negligible or near-zero improvement (e.g., Hepar2 BIC-deltas are all ≤0.01 across sample sizes; Water BIC-deltas ≤0.07; Asia and Survey show fluctuations around zero). The improvement is concentrated in a subset of medium-sized networks (e.g., Insurance +8–10%, Sachs up to +20% at some sample sizes). The paper is transparent about these patterns (line 210) but the overall practical significance of a 0.04 absolute F₁ gain needs more candid discussion.

5. **GES comparison on a selected, non-representative subset.** Only 175 out of 700 runs are used for the GES comparison because GES timed out on larger/denser networks (Section 4.5). The paper acknowledges this and frames the filtering as "favorable for GES," but the subset is clearly biased toward smaller/sparser cases, limiting the generality of the GES comparison. The extreme variability in Figure 3 (SHD differences from −30 to +20 on networks with ~50 edges) also suggests the comparison may be driven by a few outlier runs.

### Trivial
- PC's runtime on Hailfinder (15,923 seconds, Table 5) is an extreme outlier (~52× its runtime on comparably sized networks) with no explanation, raising a possible implementation or configuration issue.

## Nice-to-Haves
- A random-Shapley baseline (replacing Shapley values with random edge weights matched on magnitude) would cleanly test whether the directional signal, rather than any edge-level weighting, drives improvements.
- Reporting skeleton F₁ and orientation F₁ separately, and for PC/GES computing orientation metrics only on edges that are directed in their output, would make the comparison fairer and more informative.
- A diagnostic scatter plot showing Shapley asymmetry ratios vs. ground-truth parent direction (on a simple synthetic model) would strengthen the core claim.

## Removed Points

These points from the original reviews were evaluated against the paper and excluded from the main weaknesses for the stated reasons:

- **Criticism about insufficient distinction from ReX (Renero et al., 2025):** The paper explicitly states ReX is for continuous data with constraint pruning, while XBIC is for discrete score-based search (Section 2.3, lines 60–62). The distinction is sufficiently clear.
- **Criticism about the consistency remark being misleading:** The paper's consistency remark (line 159–163) is about asymptotic order (O(log N)), which is technically correct. The overfitting concern is a reasonable caution but the paper's empirical results do not show catastrophic overfitting. Removed as the paper's statement is accurate for what it claims.
- **Speculation about τ sensitivity on individual networks:** The reviewer speculates some networks may be sensitive to τ without evidence. The paper reports aggregate F₁ variation <1%. Removed as speculative.
- **Formatting and presentation nitpicks:** Parser artifacts, not author errors.

## Novel Insights

The key insight from the reviews is that the paper's experimental design does not isolate the mechanism it claims to demonstrate. There are two independent confounds. First, the penalty reduction from XBIC's Shapley weighting could be approximated by a uniform penalty scaling (e.g., AIC or BIC with α<1), which would require no directional signal at all. Second, the comparison against PC and GES is contaminated by the random-orientation procedure for converting their PDAG outputs to DAGs. Together, these gaps mean the paper's headline numbers (+5.6% over BIC, +20.9% over PC) may overstate or misattribute the contribution of the directional Shapley signal. A cleaner evaluation would: (a) include a uniform-penalty baseline (BIC with reduced α), (b) replace Shapley values with random weights as a negative control, and (c) report skeleton vs. orientation metrics separately—especially for PDAG-outputting baselines. Without (a) and (b), the improvements could be explained by a trivial penalty adjustment rather than by the claimed causal-directional guidance.

## Suggestions

1. **Add a uniform-penalty control baseline.** Compare XBIC(w=2) against BIC with penalty coefficient α·log N/2 for several α<1 (e.g., α∈{0.5, 0.7, 0.9}). If these achieve similar F₁, the Shapley signal is not the active ingredient.
2. **Report skeleton and orientation metrics separately.** For all methods, report undirected skeleton F₁ (which is fair across all methods) and, for PC/GES, compute orientation accuracy only on edges that are directed in their output.
3. **Add a diagnostic experiment on a simple known motif** (e.g., a three-variable chain or confounder) showing that Shapley asymmetries correctly identify the true direction. Also run XBIC with random edge weights replacing Shapley values as a negative control.

## Score and Decision

**Overall assessment:** The paper introduces a creative idea (Shapley-modulated BIC for discrete causal discovery) and provides a thorough empirical evaluation across diverse networks. However, two significant experimental gaps prevent the current evidence from fully supporting the claimed mechanism: (1) no control for a uniform penalty reduction, which could reproduce the gains without requiring directional signal; (2) a biased evaluation protocol for PDAG-outputting baselines that inflates the reported improvements. The absolute F₁ improvement over the strongest competitor (BIC-HC) is modest (0.04). The paper would benefit substantially from targeted controls and diagnostic experiments before the claims can be considered fully supported.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>