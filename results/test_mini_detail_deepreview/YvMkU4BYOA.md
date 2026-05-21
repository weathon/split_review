Now I have a solid understanding of the calibration landscape. Let me write the final consolidated review.

## Summary

This paper introduces XBIC, a score-based method for discrete causal discovery that augments the BIC score with edge-specific Shapley values derived from per-node XGBoost classifiers. The key idea is to soft-weight BIC's complexity penalty: edges with strong directional Shapley support (i.e., when $|\bar{\phi}_{j\rightarrow i}|$ is large) are penalized less, while edges with weak support revert to the standard BIC penalty. The method is evaluated on 10 benchmark discrete Bayesian networks (6–76 nodes) across 7 sample-size regimes totaling 700 runs, reporting consistent but modest improvements in oriented-edge $F_1$ over BIC-HC (5.6% relative), PC (20.9%), and a GES variant (9.6%).

## Strengths

- **First integration of local Shapley values into a score-based discrete causal discovery objective.** The paper is the first to directly use local feature attributions as a directional penalty modulation in a BIC-style score for purely discrete data. The three-stage pipeline (per-node classifier → Shapley aggregation → hill-climbing with XBIC score) is clearly described and novel.

- **Extensive and consistent empirical evaluation.** The paper evaluates on 10 benchmark networks spanning 6–76 nodes and 7 sample-size regimes with 10 repetitions each (700 total runs). Table 4 aggregates the results, showing XBIC (w=2) achieves 5.6% relative $F_1$ improvement over BIC, 20.9% over PC, and 9.6% over GES. The pattern of improvement is consistent across networks and sample sizes (Table 2).

- **Drop-in design with safe fallback.** XBIC reduces exactly to BIC when $w=0$ or $\text{SHAP}(G)=0$ (Section 3). The paper notes that the penalty still scales as $O(\log N)$, preserving BIC's large-sample consistency properties. This makes XBIC a backward-compatible modification that practitioners can adopt within existing BIC-based pipelines.

- **Sensitivity analysis of key hyperparameters.** The paper examines the confidence threshold $\tau$ (varying 0.7–0.95 changes $F_1$ by <1%) and the Shapley weight $w$ (Figure 2 shows precision–recall trade-offs), providing practical guidance and demonstrating robustness.

- **Transparent runtime reporting.** Table 5 reports wall-clock times for all methods across all networks, and the paper discusses parallelization opportunities for the front-loaded attribution phase.

## Weaknesses

### Major

- **Missing justification that predictive Shapley asymmetry encodes causal direction.** The paper's core claim is that if $|\bar{\phi}_{1\to2}| \gg |\bar{\phi}_{2\to1}|$, then $X_1\to X_2$ has "stronger directional support" (Section 3.2, line 131). But the Shapley values are computed from a purely predictive classifier $p(X_i \mid X_{\setminus i})$ that captures any statistical association, not causal direction. The paper offers no argument, toy example, or theoretical analysis establishing that predictive Shapley asymmetry should systematically align with the true causal orientation. The only related work cited (Frye et al. 2020) assumes a *known* causal graph, which is not available here. This gap is structural: if the mapping is unjustified, the score modification is an expensive heuristic whose success on the tested benchmarks may not generalize. The paper's limitations section (Section 5) does not mention this issue.

### Minor

- **Large computational cost relative to modest gains.** XBIC takes 74 seconds on Asia (6 nodes, 8 edges) vs. 0.39 seconds for BIC-HC (~190× slower); on Hailfinder (56 nodes) it takes 1904 seconds vs. 36 seconds for BIC-HC (~52× slower). The absolute $F_1$ improvement over BIC across all runs is 0.04 (Table 4). While the paper acknowledges runtime and discusses parallelization, the "drop-in upgrade" framing downplays a 50–200× slowdown for a 4-percentage-point absolute $F_1$ gain. This is a practical limitation that most readers would weigh heavily.

- **Missing absolute $F_1$ values and variance for baselines.** Table 2 reports only $F_1$ deltas relative to baselines, and Table 4 reports only the improvement. The reader cannot assess whether BIC itself is performing well or poorly on these networks, nor can they evaluate the spread of results. Figure 2 shows confidence intervals for precision/recall on 3 networks, but the main results table has no variance information.

- **GES comparison conditioned on completed runs.** Section 4.5 explains that GES exceeded the 7-day limit on many settings; the comparison is restricted to the subset where GES completed. The paper notes this is "favorable filtering for GES," and XBIC still wins on this subset. However, the reported SHD improvements (6–32%) may hold only on the easier instances, and the paper does not analyze how the filtered subset differs from the full data.

- **No analysis of whether the Shapley penalty biases search toward denser graphs.** The paper notes that larger $w$ increases recall at the cost of precision (consistent with a softer penalty), but does not examine whether the method systematically favors denser graphs. A plot of graph size (number of edges) vs. true positive rate for XBIC vs. BIC would clarify this.

### Trivial

- The $F_1$ deltas in Table 2 are presented without confidence intervals or significance markers, making it difficult to assess which entries are meaningful vs. noise.
- Figure 3 (SHD difference scatter plot) would be more informative as a box plot or aggregated table.

## Nice-to-Haves

- A synthetic toy example (e.g., a simple 3-variable chain vs. confounder) demonstrating that Shapley asymmetry aligns with the true causal direction would significantly strengthen the paper's core thesis.
- A comparison to MMHC or other discrete-specific hybrid algorithms would provide a stronger empirical baseline.
- An analysis of whether the Shapley values change meaningfully when classifiers are trained on bivariate inputs (rather than all other variables) could help understand whether the signal is diluted by many competing features.
- Reporting the test statistics, p-values, or a critical difference diagram for the adjusted Friedman + Wilcoxon test would support the significance claims.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"No comparison to MMHC"** – The paper explicitly scopes out MMHC in Section 4.1 ("MMHC targets large sparse graphs and is not the focus here"). This is a scope choice, not a missing comparison.
- **"No error bars in Table 2"** – Figure 2 does include confidence intervals for precision/recall on representative networks. The criticism is partially valid but the paper does provide some variance information.
- **"Figure 3 is misleadingly favorable"** – The figure is a simple line plot of SHD differences, most of which are below zero. The presentation is clear, not misleading. The critic's suggestion of a box plot is a reasonable alternative but not a flaw.
- **"The paper does not discuss related work on causal asymmetry from predictive models"** – Per instructions, I cannot comment on missing related work as I lack external sources to confirm existence.
- **"The non-confident instances may be where directional information is most useful"** – This is speculative and not grounded in any analysis the paper could have done.
- **"No comparison to MMHC"** (repeated from Strength Finder) – Already addressed.
- Several generic strengths from the Strength Finder (e.g., "addressed an important problem") are removed as they are superficial or apply to any paper in this area.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface the tension between the paper's empirical claims and its missing foundational justification, which the paper itself does not fully engage with.

## Suggestions

1. **Add a synthetic demonstration** of the core claim. A simple 3-variable chain ($X \to Y \to Z$) vs. confounder ($X \leftarrow H \to Y$) experiment where the Shapley asymmetry is computed and shown to align with the true direction would provide the missing justification. This is the single most important addition.

2. **Report absolute $F_1$ and SHD** for all methods (including variance) in a supplementary table, so readers can assess the baseline performance and effect sizes directly.

3. **Tone down the "drop-in upgrade" framing** in the abstract and conclusion. "Drop-in within the familiar BIC framework" is accurate, but the computational overhead is substantial. A more precise framing would acknowledge the cost upfront.

4. **Add a graph-size analysis** showing whether XBIC systematically learns denser graphs than BIC, and how this interacts with the Shapley weight $w$.

## Score and Decision

**Round 1 bracket (3.5–7.5):** The paper is clearly stronger than weak anchors at ~3.0–3.25 (e.g., D$^3$PM, which had unclear methods and poor theoretical grounding) and clearly weaker than top-tier anchors at ~8.0 (e.g., Signature Kernel CI tests for stochastic processes). The round 1 bracket placed the paper between 4.0 and 6.5.

**Round 2 narrowing (4.0–6.0):** The most comparable anchor is **DAG-SHAP** (5.0), which similarly uses Shapley values in a causal context and suffers from a missing theoretical justification. The XBIC paper has broader and more rigorous empirical validation than DAG-SHAP, but also has a higher cost-to-benefit ratio concern. **PIT** (4.25) is a more incremental algorithm paper with limited comparison; XBIC is stronger in novelty and scope. **Extendable Structure Learning** (5.6) has strong empirical results and some theoretical backing but more limited novelty; XBIC is comparable in quality. **TICL** (5.5) has mixed reviews and a similar profile of novel idea with some gaps.

**Final score:** 5.0. The paper has a genuinely novel idea, clear presentation, and extensive experiments. However, the missing justification for the core mapping from Shapley asymmetry to causal direction undermines the contribution's foundations, and the large computational cost relative to modest gains limits practical impact. The paper is a reasonable borderline submission that would benefit from addressing the foundational gap before the final version.

**Anchor summary:**
- **D$^3$PM** (3.25, R1): Weak theory, unclear method. XBIC is substantially stronger.
- **PIT** (4.25, R1): Incremental PC improvement, limited comparison. XBIC has more novel contribution.
- **DAG-SHAP** (5.0, R2): Comparable Shapley+causal theme, similar missing-theory concern, but less extensive evaluation. XBIC is slightly stronger empirically.
- **TICL** (5.5, R2): Test-time learning for causal discovery, mixed reviews. Comparable quality.
- **Extendable Structure Learning** (5.6, R2): Strong empirical results, theoretical lemmas. Comparable.
- **DrBO** (6.5, R2): Bayesian optimization for DAG learning, strong method and results. XBIC is weaker than this.
- **Signature Kernel CI** (8.0, R3): Top-tier theoretical contribution. XBIC is not at this level.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>