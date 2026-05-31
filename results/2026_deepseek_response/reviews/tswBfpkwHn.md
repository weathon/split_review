Now let me craft the final consolidated review and calibration report.

## Calibration Summary

**Round 1 — Bracketing:**
- Low (avg < 3.5): Mamba normalization study (3.00), Mamba Neural Operator (3.00) — clearly weaker than our paper.
- Middle (3.5–7.5): In-context vs In-weight Learning (6.50), How Do Transformers Learn ICL Beyond Simple Functions (6.50), Training Nonlinear Transformers for CoT (6.50), Mamba SSMs Lyapunov-Stable (4.67).
- High (7.5+): Context-Parametric Inversion (8.00), When can transformers reason (7.60), Scaling Laws for Associative Memories (7.60) — broader-impact or more general results.

**Initial bracket: 5.0–7.0**

**Round 2 — Narrowing:**
- Lower anchors: JoMA (5.75), Provable ICL Mixture of Linear Regressions (5.00, Reject), Better Understanding of ICL (5.00). Our paper is clearly above 5.00 reject-level papers — it has a stronger contribution (first Mamba ICL training analysis) and validation.
- Upper anchors: How Transformers Learn ICL Beyond Simple Functions (6.50, Accept), Training Nonlinear Transformers for CoT (6.50, Accept), How Transformers Implement Induction Heads (6.20, Reject). The 6.50 CoT paper is structurally similar (one-layer analysis, training dynamics, synthetic experiments, distribution-shifted generalization) and was accepted. Our paper is comparable but has more restrictive sufficient conditions and the conical-hull assumption, putting it slightly below.

**Final score: 6.0** — solid Accept, clearly above 5.00 reject-level theoretical papers, comparable to but slightly below the 6.50 accepted theoretical ICL papers due to the interdependence of sufficient conditions and the conical-hull scope restriction on the central robustness claim.

---

## Summary

This paper presents the first theoretical analysis of training dynamics and ICL generalization for one-layer Mamba models on binary classification tasks with additive outliers. It formally shows that Mamba's gating mechanism enables robustness to outlier fractions approaching 1, while a comparable one-layer linear Transformer can only tolerate α < 1/2. The analysis also provides a mechanistic decomposition: the linear attention layer selects examples sharing the query's relevant pattern, while the nonlinear gating suppresses outliers and induces an exponential local bias. Experiments on synthetic data support the theoretical predictions.

## Strengths

1. **First theoretical analysis of Mamba training dynamics for ICL with outliers** — Theorem 1 provides explicit convergence and sample complexity guarantees, and Theorem 2 proves ICL generalization under distribution-shifted outliers. This is a genuine "first" in the literature and extends beyond prior Transformer-focused analyses.

2. **Provable robustness characterization with comparison** — Theorem 2 (Condition c) and Theorem 4 (Condition c) formally establish that Mamba tolerates α → 1 while a one-layer linear Transformer tolerates only α < 1/2. This gap is new, and the experiments in Figure 2 validate the threshold experimentally across three different outlier labeling functions.

3. **Mechanistic characterization** — Corollary 1 proves attention concentrates on same-pattern examples; Corollary 2 proves gating suppresses outliers (gating → poly(M₁)⁻¹) and induces exponential decay with index distance. These predictions are verified in 3-layer Mamba experiments (Figures 3–4), showing the theory captures phenomena that persist in deeper models.

4. **Honest presentation of failure modes** — Table 1 explicitly shows Mamba's vulnerability when outliers are closest to the query (CQ: 82.73% vs FQ: 99.73%), and the paper discusses this as a direct consequence of Corollary 2's local bias. Remark 6 clarifies the scope of comparison with linear Transformers.

## Weaknesses

### Major

None.

### Minor

1. **The conical-hull restriction on test outlier generality** — Theorem 2 Condition (a) requires test outliers to belong to 𝒱' = {v : v = Σ λᵢvᵢ* + u, Σ λᵢ ≥ L > 0, u ⟂ training patterns}. This means test outliers must contain a *positive* linear combination of training outlier patterns, plus an orthogonal component. The paper's phrasing "unseen outliers" is technically correct (they need not be identical to training outliers) but the restriction is strong: an outlier pattern orthogonal to all training outlier patterns is not covered. The paper states this assumption (Section 3.1 P1, Theorem 2, Remark 3) but could more prominently flag how much generality is lost compared to the intuitive "unseen" reading.

2. **Interdependent sufficient conditions not checked against experiments** — Theorem 1 imposes many simultaneous bounds (batch size, outlier magnitude window with lower AND upper bound, prompt length bounded above by pₐ⁻¹poly(M₁^{κₐ}) and below by (1-pₐ)⁻¹log M₁). The paper does not verify whether the experimental parameters (e.g., κₐ=2, β=3, V=3, pₐ=0.6) actually satisfy these conditions. A brief sanity check or worked example would help readers gauge whether the theoretical regime is vacuous or reasonably inhabited.

3. **Structured initialization of W_B, W_C** — The first d diagonal entries are set to δ ∈ (0,0.2], departing from standard random initialization. The paper does not discuss whether this is necessary or whether the analysis would hold under random initialization. This matters for practitioners wanting to know if the theory applies to default training setups.

4. **Ambiguous notation in Theorem 1 Condition (iii)** — The expression "pₐ⁻¹poly(M₁^{κₐ})" in the upper bound on l_tr is ambiguous: poly(M₁^{κₐ}) could be read as a polynomial in M₁^{κₐ}, which grows exponentially in κₐ. Clarification would help readers understand the bound's practical implications.

### Trivial

- The lower bound in Theorem 1 Condition (ii), Vβ⁻⁴ ≲ κₐ, simplifies to roughly V ≲ κₐ since β ≥ 1, which could be stated more directly.

## Nice-to-Haves

- A high-level proof sketch in the main text (the paper refers to Appendix A but provides no intuition about how the gating dynamics learn to detect outliers via the update equations).
- Discussion of whether the gating can suppress *any* sufficiently large-norm outlier pattern beyond the conical hull, or whether the mechanism is inherently subspace-limited.
- Note that the experiments in Figure 2 use α up to 0.8 while Theorem 2 Condition (c) with pₐ=0.6, l_tr=l_ts=20 gives α < 0.6. The empirical robustness beyond the sufficient condition is interesting but unremarked.

## Removed Points

- **Comparison baseline is a stripped-down architecture (Harsh Critic #2):** The paper consistently specifies "one-layer single-head linear Transformer" throughout and includes Remark 6 explicitly clarifying the scope. The claim is precise and not misleading.
- **Mamba training conditions are "extremely narrow":** The paper itself states these are sufficient conditions, which is standard for first-pass theoretical analysis. The conditions are not unusually restrictive for this literature (cf. Li et al. 2024a, Huang et al. 2023, the CoT paper at 6.50).
- **Multi-layer CQ experiment as a weakness:** The paper presents this as an honest finding and discusses it as a direct consequence of its own theory. This is a strength of the analysis, not a weakness.
- **"Proof sketch in main text"** is a nice-to-have. The paper mentions Appendix A for proofs, which is standard.
- **"Empirical validation of training difficulty":** The paper's theory already characterizes the trade-off; not running an additional experiment on convergence speed is a minor omission at worst.
- **Missing related works concern:** Removed per hard rules — I cannot verify which works exist.
- **Formatting/style nitpicks and typing issues:** Removed per hard rules — these are parser artifacts.

## Novel Insights

The central insight is that Mamba's gating mechanism serves a dual role: it drives gating values to poly(M₁)⁻¹ for outlier-containing inputs (suppressing them) while simultaneously inducing an exponential local bias (1/2^{j-1}) toward examples close to the query. This explains both Mamba's superior robustness to high outlier fractions and its vulnerability to outliers placed nearest the query — a concrete failure mode verified in Table 1. The convergence analysis reveals a fundamental trade-off: the gating that enables robustness also makes Mamba harder to train (Θ(l_tr) more iterations) than a comparable linear Transformer, yet the benefit in outlier tolerance (α → 1 vs α < 1/2) is substantial. This provides a principled explanation for empirical observations in Park et al. (2024).

## Suggestions

1. Add a brief paragraph clarifying what the conical-hull assumption (Theorem 2 Condition (a)) excludes and stating that generalization to completely novel outlier directions orthogonal to the training subspace is not covered.
2. Include a short sanity check (or appendix note) showing that the experimental parameters plausibly satisfy the theoretical sufficient conditions, or acknowledge the gap.
3. Clarify the "poly(M₁^{κₐ})" notation in Theorem 1 Condition (iii) — state explicitly whether this means polynomial in M₁ with degree scaling in κₐ (which would grow exponentially) or something else like poly(M₁)^{κₐ}.
4. Discuss whether the structured initialization (diagonal δ ∈ (0,0.2]) is necessary or whether the analysis can accommodate standard random initialization.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>