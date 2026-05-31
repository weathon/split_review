## Summary

This paper proposes a temporal graph neural network (TGNN) framework for detecting lead-lag relationships in financial markets. It reformulates the problem as temporal link prediction on dynamic graphs (nodes = assets, directed edges = lead-lag relationships), assembles a custom dataset of 37 stocks and commodities with 5 years of daily data enriched with financial indicators and sentiment, and benchmarks six state-of-the-art TGNN architectures plus a sequential LSTM baseline. GraphMixer (GM), a simple MLP-based model, consistently outperforms all attention-based TGNNs across both a positive+negative and a positive-only scenario. A new variant, GM-TNF, integrates time-varying node features but does not surpass the vanilla GM.

---

## Strengths

- **Natural problem formulation.** Recasting lead-lag detection as temporal link prediction on dynamic graphs is well-motivated: assets are naturally nodes, and directed predictive relationships are naturally edges. The formulation also enables modelling the whole network simultaneously rather than pairwise-only approaches.

- **Comprehensive experimental design.** Eight models, two scenarios (positive+negative vs. positive-only), three feature groups, five repeated runs for variance estimation, plus Friedman/Conover statistical significance tests constitute a thorough evaluation that goes well beyond most application benchmark papers.

- **Feature ablation reveals meaningful patterns.** The finding that description embeddings alone outperform embeddings+prices for most architectures—while GM uniquely benefits from all features—provides an actionable insight about feature utility in lead-lag modelling and is consistent with the graph construction rule: temporal edges encode return thresholds, so redundant price features add noise rather than signal.

- **Dual-scenario evaluation.** Explicitly separating "bullish-only" from "bidirectional" lead-lag is a useful contribution given the definitional ambiguity in the literature, and results show stable model rankings across both conditions.

---

## Weaknesses

### Fatal

None that entirely invalidate the contribution, but one issue below rises close.

### Major

1. **Potential feature-label entanglement (data leakage).** Lead-lag edge labels are defined by whether both assets' percentage returns exceed ε=5% on consecutive days. The "Embeddings + Prices" feature group includes the closing price at time *t* for both source and destination nodes. Given access to p_t and p_{t-1} (via VWAP or historical price features), models could implicitly compute r_t and r_{t-1} and partially deduce edge labels from the features. The paper does not include an analysis demonstrating that the models learn genuine predictive patterns rather than partially recovering the labelling rule from the same price data used to construct the graph. Notably, adding prices *hurts* most models (Table 3), which could indicate this signal is either redundant or corrupting, but the question deserves explicit analysis (e.g., testing features that are constructed purely from information preceding the edge timestamp).

2. **No comparison with domain-standard baselines.** The paper explicitly dismisses Granger causality and cross-correlation methods as "complex adaptations," yet these are the canonical tools practitioners use for lead-lag detection with exactly 37 assets. Even a simple pairwise cross-correlation threshold baseline or VAR-based Granger causality could be implemented at negligible cost and would give reviewers a reference point for whether the TGNN advantage over LSTM (AP 0.79 vs 0.51) is large or modest in absolute terms. The claim that such comparisons would require "hybrid approaches that differ substantially from established methods" is not convincing given the modest scale of the dataset.

3. **Very small, proprietary dataset limits generalizability.** The benchmark consists of only 37 nodes and daily observations, which is extraordinarily small for a graph learning task. With 37 nodes the maximum degree is 36, and R@10 reaching 0.99 (Table 1) is not a demanding retrieval task when only ~36 candidates exist. Conclusions about which TGNN architecture is superior on such a small graph may not transfer to realistic financial networks with hundreds or thousands of assets. The paper would be substantially stronger with even one additional dataset of different scale or sector composition.

4. **No economic/financial utility evaluation.** The paper claims practical relevance for "informed trading strategies," but no out-of-sample trading simulation, cumulative return, Sharpe ratio, or portfolio analysis is conducted. AP and AAUC are proper ranking metrics but provide no evidence that predicted lead-lag links translate into economically significant signals. For a paper that repeatedly motivates the work through financial applications, this gap is significant.

### Minor

1. **The GM-TNF variant is marginal.** GM-TNF is presented as a contribution, but the modification amounts to augmenting node features with a one-hop mean aggregation over a temporal window—a standard trick—and it consistently underperforms vanilla GM. Its inclusion as a distinct model creates some confusion about the hierarchy of contributions.

2. **ε=5% threshold is extreme for daily data.** A 5% single-day return is a tail event in most markets. The resulting graph is necessarily sparse and dominated by high-volatility episodes. The paper acknowledges this trade-off but does not quantify how the resulting graph statistics compare to those of the broader benchmark TGL tasks, making it harder to calibrate how unusual the task is.

3. **Validation protocol asymmetry.** Models are selected on the positive+negative dataset and then evaluated "as-is" on the positive-only dataset, bypassing standard validation for the second scenario. The paper acknowledges this but does not adequately justify it; optimising separately for each scenario would give a fairer comparison.

### Trivial

None beyond parser-related formatting (equations, figure alt-text).

---

## Nice-to-Haves

- A simple Granger causality or cross-correlation threshold baseline, even run on a subset of asset pairs, to anchor performance numbers against established methods.
- A trading simulation or portfolio backtest to translate AP gains into economic value.
- An experiment on a second, larger financial dataset (e.g., S&P 500 subset) to test generalizability of architecture rankings.
- Explicit analysis confirming that the "Embeddings + Prices" feature group does not allow models to recover labels from price data alone (e.g., ablating prices at the labelling time step vs. preceding steps).

---

## Novel Insights

The most genuinely novel observation is the dual-scenario (bidirectional vs. bullish-only) lead-lag formulation, which exposes an overlooked definitional gap in the literature and shows that model rankings are stable across the two interpretations. The confirmation that GraphMixer—built entirely from permutation-invariant MLPs without attention mechanisms—outperforms all TGNN architectures in a financial temporal graph setting adds further cross-domain evidence to the Cong et al. (2023) finding that architectural complexity does not automatically translate to better performance. The feature ablation revealing that adding price features tends to hurt most models but benefits GM exclusively is an interesting model-specific finding, though its causal explanation (that GM's token-mixing strategy integrates price information more effectively) remains speculative.

---

## Suggestions

1. Add a Granger causality pairwise baseline to provide an interpretability anchor; even a simple implementation would significantly strengthen the paper's positioning.
2. Conduct a separate model selection run for the positive-only scenario to eliminate the validation asymmetry.
3. Compute a graph informativeness sanity check: train a model that only receives source-node return at t-1 and destination-node return at t as features (i.e., the exact label conditions). If this trivially achieves high AP, then feature-label entanglement is a real issue that must be controlled.
4. Include at least one larger-scale experiment or an additional financial benchmark to substantiate claims about TGNN rankings for financial graphs in general.
5. Provide at minimum a simple return-based analysis on test-period predictions to illustrate economic relevance.

---

## Score and Decision

The paper occupies a legitimate niche—introducing a TGNN benchmark for financial lead-lag detection—and the experimental work is thorough. However, the combination of a very small dataset, the absence of domain-standard baselines, the unaddressed feature-label entanglement concern, and no economic evaluation represents a substantial gap between the paper's practical claims and its empirical support. The methodological ML contribution is incremental (GM-TNF is minor; the other models are adapted from existing work). The paper reads closer to a workshop or domain-venue submission than a main ICLR contribution.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>