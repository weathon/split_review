## Summary
XBIC augments BIC's complexity penalty with edge-specific Shapley evidence drawn from per-node XGBoost classifiers trained on observational discrete data. For each candidate DAG, aggregate |SHAP| values across its edges reduce the penalty term, biasing the hill-climbing search toward edges with strong predictive attribution. The method is evaluated on ten benchmark discrete Bayesian networks across seven sample-size regimes (700 runs), reporting consistent F₁ gains over BIC-HC (+5.6%), GES (+9.6%), and PC (+20.9%).

---

## Strengths

- **Graceful fallback**: The design is such that XBIC exactly recovers BIC when w=0 or when no confident instances pass the threshold filter (SHAP(G)=0). This property means the method cannot catastrophically degrade below the BIC baseline in low-signal settings, which is practically desirable.

- **Empirical breadth**: The evaluation spans 10 networks (6–76 nodes, multiple domains), 7 sample-size schedules scaled to M², 10 repetitions per cell, and three values of w, for a total of 700 runs. Statistical comparisons use Friedman + Wilcoxon signed-rank tests with p < 0.05, which is appropriate for this kind of multi-condition benchmark.

- **Drop-in modification**: XBIC can replace the BIC score inside any existing hill-climbing skeleton with no change to the search procedure itself, lowering the adoption barrier significantly.

---

## Weaknesses

### Fatal
None that fully invalidate all results. The empirical improvements are real on the reported benchmarks.

### Major

**1. The core directional mechanism is not theoretically justified, and a concrete counter-argument exists.** The paper's fundamental claim is that $|\bar{\phi}_{j\rightarrow i}| > |\bar{\phi}_{i\rightarrow j}|$ signals causal direction $X_j\rightarrow X_i$. But these quantities are Shapley values from two *different* predictive models: $f_i$ (predicting $X_i$ from $X_{\setminus i}$) and $f_j$ (predicting $X_j$ from $X_{\setminus j}$). The asymmetry between these depends on *marginal entropy*, not only causal structure. For discrete variables, $H(X_i|X_j) - H(X_j|X_i) = H(X_i) - H(X_j)$, meaning whenever $X_j$ has a more diffuse marginal distribution than $X_i$, the model $f_i$ will tend to be more confident and produce larger Shapley contributions—regardless of causal direction. This confound is not mentioned, not controlled for, and could systematically favor one direction over another for marginal-distribution reasons rather than causal ones. The paper notes that formal analysis is a future direction, but this is not a minor gap; it is central to whether the method is principled or a coincidentally working heuristic.

**2. The claimed benefit (orientation within equivalence classes) is never directly measured.** The paper's stated goal is to "resolve edge directions within Markov-equivalence classes." However, the reported metric—oriented-edge F₁—conflates skeleton errors (missing/extra edges) with orientation errors. A missing edge that BIC and XBIC both miss counts the same way. To actually demonstrate that XBIC improves *orientation* within the equivalence class, one would need to (a) identify which edges are in the skeleton of the true CPDAG and are undirected there, and (b) measure orientation accuracy on that subset. Without this breakdown, the improvements in Table 2 may mostly come from skeleton changes driven by the penalty modification, not from better orientation within equivalence classes.

**3. Inconsistent results across networks undermine the generality claim.** Table 2 shows XBIC underperforms BIC for Win95pts at the two largest sample sizes (−0.00 and −0.09), and for Asia shows negative deltas at medium-to-large samples (e.g., −0.12 at 2M², −0.02 at 4M², −0.02 at 8M²). Hepar2 shows 0.00 improvement against BIC at almost every sample size across the entire table. These are not sampling fluctuations—Hepar2 is a 70-node medical network, and the systematic non-improvement there is unexplained. The aggregate gain hides these cases.

### Minor

**4. Hyperparameter w has no principled selection criterion.** The paper sweeps w ∈ {1,2,3} and reports w=2 as the best across all 700 runs, but in practice, a user needs to pick w without access to ground truth. The paper does not describe a cross-validation or model-selection strategy, leaving the practical pipeline underspecified.

**5. Computational overhead is severe.** Table 5 shows XBIC is 50–200× slower than BIC-HC across networks (e.g., 0.39 s vs 74.78 s for Asia; 9.30 s vs 523.52 s for Alarm). The paper acknowledges this and notes parallelization, but for networks of even moderate size this cost is substantial for practitioners.

### Trivial

- Three footnote URLs (code repository, Optuna, release) are redacted in the submitted version, but this is expected for anonymized submissions.

---

## Nice-to-Haves

- An ablation that keeps the skeleton fixed (e.g., uses the oracle skeleton from the true DAG) and applies XBIC only to orientation would cleanly isolate the claimed contribution to Markov-equivalence resolution.
- A controlled synthetic experiment where causal asymmetry is known analytically (e.g., bivariate discrete additive noise model) to show that $|\bar{\phi}_{j\rightarrow i}|$ vs. $|\bar{\phi}_{i\rightarrow j}|$ indeed favors the true direction—and to characterize when it does not.
- SHD broken down into missed edges, extra edges, and wrong directions would clarify which component XBIC actually improves.

---

## Novel Insights
The paper's genuinely novel element is that per-node predictive models (trained marginally over all other variables) can produce asymmetric attributions that, when used to soft-weight BIC's penalty, push hill-climbing toward empirically better-oriented structures in discrete Bayesian networks. This is a pragmatic, practically accessible idea—classifiers and TreeSHAP are standard tools, and piping their outputs into score modification is architecturally clean. However, whether the asymmetry carries causal information or merely reflects marginal entropy differences or sample-size effects is left open, making the contribution more empirical than principled.

---

## Suggestions

- Establish (even empirically on synthetic examples) that $|\bar{\phi}_{j\rightarrow i}| > |\bar{\phi}_{i\rightarrow j}|$ reliably predicts the true causal direction when controlling for marginal entropy differences. This would greatly strengthen the paper.
- Report orientation accuracy separately from skeleton recovery (e.g., fraction of correctly oriented edges among skeleton-present edges) to directly validate the stated goal.
- Describe and evaluate a practical w-selection procedure (e.g., leave-one-network-out, or validation on a held-out sample).
- Include MMHC as a baseline even for some networks, as it is a standard hybrid algorithm for discrete BNs and is explicitly mentioned in the text.

---

## Score and Decision

The paper proposes a pragmatic, usable modification of BIC that empirically shows real improvements on established benchmarks. The evaluation is appropriately broad and the fallback property is appealing. However, the core directional mechanism lacks theoretical justification, and a specific entropy-asymmetry confound can explain the Shapley asymmetry without invoking causality. The evaluation metric does not directly measure the claimed contribution (orientation within equivalence classes), and improvements are inconsistent across several major benchmark networks. These are substantive issues that weaken confidence in the generality and principled nature of the method.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>