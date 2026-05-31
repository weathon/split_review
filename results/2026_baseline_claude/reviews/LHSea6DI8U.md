Now I have read the complete paper. Let me write the review.

---

## Summary

STBP is a continual spatio-temporal forecasting framework that bridges strong ST backbone design with continual learning. It comprises: (1) a Frequency-Domain Network (FreNet) for stable, drift-resilient temporal representations, (2) a Dual-Stream Linear Graph Attention (DLGA) module that reduces spatial attention complexity from O(N²) to O(N), and (3) an expandable contextual pattern bank of per-node trainable parameters that incrementally grows as the graph expands. After an initial joint training stage, the backbone is frozen and only the pattern bank is updated, mitigating catastrophic forgetting while supporting graph topology growth. Experiments on three streaming spatio-temporal datasets (two traffic, one air quality) consistently place STBP above state-of-the-art continual baselines, with particularly large MAE reductions on traffic datasets.

---

## Strengths

- **Large and consistent empirical gains on traffic datasets.** STBP reduces average MAE by 21.44% (PEMS-Stream) and 21.93% (CA-Stream) over the strongest baseline (EAC). These margins hold across all horizons (3/6/12 steps) and all three metrics (MAE/RMSE/MAPE), as shown in Table 1. The few-shot experiment (Table 2, 10% training data) also shows clear superiority (~16% MAE improvement over EAC on PEMS-Stream).

- **Efficient and scalable design.** The linear attention approximation in DLGA is well-motivated and empirically validated: Figure 8 confirms O(N) vs. O(N²) GPU memory growth on the toy dataset. STBP achieves its accuracy improvements with minimal additional training time over EAC, making the accuracy-efficiency trade-off highly favorable.

- **Coherent and principled architecture.** The separation of concerns—backbone handles distributional drift and dynamic spatial correlations; pattern bank handles node heterogeneity and catastrophic forgetting—is clearly articulated and reflected in the ablation results. Each removed component (DLGA, FreNet, pattern bank) causes meaningful degradation (Figure 4).

- **Interpretable pattern bank.** The t-SNE visualizations (Figures 3 and 6) show that the pattern bank autonomously clusters nodes by behavioral similarity without supervision. The case study demonstrates that new nodes added in later incremental stages are naturally assigned to appropriate existing clusters, providing some mechanistic justification for the design.

---

## Weaknesses

### Fatal
None.

### Major

1. **Frozen backbone creates an unexamined brittleness.** The backbone is trained only at stage τ=1 and then frozen permanently. No analysis examines what happens when the initial data is unrepresentative (e.g., few nodes, short time span, or atypical distribution). If initial coverage is poor, all subsequent stages inherit a systematically biased backbone—a particularly problematic failure mode for the application domain (growing urban infrastructure where early data may come from a small sensor network). The paper does not ablate or even acknowledge this dependency.

2. **Marginal gains on AIR-Stream weaken cross-domain generalization claims.** On the meteorological dataset, MAE improvement over EAC is only 2.35% (24.21→23.64), and RMSE improvements at horizon 6 (EAC: 39.63, STBP: 39.81) and horizon 12 (EAC: 44.65, STBP: 44.97) are actually slight regressions. The paper claims STBP "outperforms state-of-the-art baselines in both forecasting accuracy and scalability" without qualification, yet the air quality results do not uniformly support this. A more nuanced discussion of why the approach generalizes differently across domains—or whether air quality's irregular spatial patterns interact poorly with DLGA's adjacency-matrix-free approach—is needed.

### Minor

1. **Gating design unjustified.** The prompt-based gating in Eq. 5 (H'_τ = P_τ^(1) · h_θ(H_τ · (1 + P_τ^(0)))) is presented without motivation for this specific multiplicative form. No ablation over alternative gating designs (additive, cross-attention, DiT-style shift-scale) is provided, making it unclear whether this particular form is essential or incidental.

2. **Ablation table is approximate.** Figure 4 conveys ablation results only as a bar chart with approximate values (~15, ~20, etc.). Exact numbers are not given in text or a companion table, making it impossible to precisely compare variants or check statistical significance.

3. **Parameter growth accounting is incomplete.** The total parameters introduced per incremental stage equal 3 × (N_τ − N_{τ-1}) × d. No quantification is given of how many new parameters are added in practice (e.g., per 100 new nodes) or how this compounds across the full PEMS-Stream timeline (2003–2017, hundreds of incremental stages). While linear growth is claimed to be "lightweight," the cumulative size warrants reporting.

### Trivial
None worth noting.

---

## Nice-to-Haves

- Sensitivity analysis on which incremental stage the backbone is frozen (e.g., freeze at τ=2 or τ=3) would clarify the robustness to early-stage data quantity.
- Reporting exact numbers in the ablation figure (or a companion table) would improve reproducibility.
- A brief analysis of cluster stability over incremental periods (do existing cluster assignments change?) would strengthen the interpretability narrative.

---

## Novel Insights

The most genuinely novel insight is the **dual-stream design** in DLGA (Eq. 9): the pattern bank contributes a second key stream in the linear attention computation, allowing stored node-level knowledge to directly modulate spatial correlation estimation rather than being injected only as an additive prompt. This formulation maintains O(N) complexity while enabling the attention module to reason jointly about current input patterns and accumulated historical knowledge. Combined with the insight that freezing the backbone and expanding only a node-indexed parameter matrix is sufficient to prevent catastrophic forgetting—without any replay or regularization—the paper demonstrates that architectural separation (general vs. node-specific parameters) can be a cleaner and cheaper solution than gradient-based forgetting mitigation for this class of problems.

---

## Suggestions

- Conduct at least one experiment varying when the backbone is frozen (τ=1 vs. τ=2 vs. τ=3) to characterize sensitivity to cold-start coverage.
- Investigate why STBP underperforms EAC at specific AIR-Stream RMSE horizons; if the issue is tied to sensor characteristics or irregular spatial topology, a domain-specific discussion would strengthen the paper.
- Report the absolute parameter counts per incremental period alongside training time, to give practitioners a complete picture of overhead.
- Consider reporting a "full retrain" oracle baseline (train on all historical + current data) to contextualize the gap between continual and offline learning on these datasets.

---

## Score and Decision

STBP presents a well-engineered and empirically well-validated solution to a genuinely important problem. The traffic-domain results are large and robust; the efficiency story is compelling; the design is coherent. The primary concern—frozen-backbone brittleness and uneven performance on air quality—does not invalidate the core contribution but does limit the generality claim. This is a solid, above-average contribution to the CSTF field, appropriate for acceptance with minor revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>