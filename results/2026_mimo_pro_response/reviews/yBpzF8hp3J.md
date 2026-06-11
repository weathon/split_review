Now I have all the information I need. Let me write the final review.

## Summary

This paper reframes differentially private set union through a "missing mass" objective (ℓ₁ and ℓ∞ variants), proves that the simple Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian data with matching lower bounds, and extends the framework via a distribution-free ℓ∞ guarantee to obtain new utility guarantees for DP top-k and k-hitting set in the unknown-domain setting. Experiments on six real-world datasets demonstrate that WGM-based methods are competitive with or outperform existing baselines.

## Strengths

- **First absolute utility guarantees for DP set union (Theorems 3.3, 3.5, 3.6):** Prior work (Desfontaines et al., 2022; Chen et al., 2025) only proved relative results (algorithm A dominates algorithm B). This paper proves the first absolute upper and lower bounds on missing mass, and the matching `(1/(εN))^{(s-1)/s}` scaling in the upper bound (Theorem 3.3) and lower bound (Theorem 3.5) demonstrates near-optimality of WGM up to logarithmic factors.

- **Distribution-free ℓ∞ missing mass guarantee (Theorem 3.6):** Unlike the ℓ₁ bound requiring (C,s)-Zipfian assumptions, this result imposes no distributional assumptions. This is the key technical enabler for the downstream top-k (Theorem 4.3) and k-hitting set (Theorem 4.5) guarantees, which are also distribution-free.

- **Novel utility guarantees for unknown-domain top-k and k-hitting set (Theorems 4.3, 4.5):** The modular two-phase approach (Algorithm 2: WGM for domain discovery with half the privacy budget, then a known-domain algorithm) yields the first utility guarantees for these problems in the unknown-domain setting, filling a gap where Durfee & Rogers (2019) had only k-relative error for top-k and prior submodular maximization work assumed known domains.

- **Empirical competitiveness despite simplicity (Figures 1–3):** Figure 1 shows WGM obtains MM within 5% of the much more expensive Policy Gaussian and Policy Greedy mechanisms. Figure 2 shows WGM-then-top-k outperforms all limited-domain baselines from Durfee & Rogers (2019). Figure 3 shows competitive k-hitting set performance even against baselines that use privileged domain information.

- **Matching lower bounds (Theorems 3.5, Corollaries 4.4, 4.6):** The lower bounds demonstrate that the k/ε dependence is unavoidable for algorithms satisfying Assumption 1, providing confidence in the tightness of the analysis.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 4.5's multiplicative factor (1 − 1/ε) is vacuous for ε ≤ 1.** The theorem states: `Hits(W, S) ≥ (1 − 1/ε) · Opt(W, k) − additive error`. For ε ≤ 1 (a standard privacy regime, and the one used in the experiments where ε = 1), the factor (1 − 1/ε) ≤ 0 renders the guarantee trivially true (since Hits ≥ 0). The paper does not acknowledge this gap. The underlying User Peeling Mechanism is based on the private greedy from Mitrovic et al. (2017), which achieves (1 − 1/e) ≈ 0.632 independent of ε in the known-domain setting, and the experiments (Figure 3) show the method works well at ε = 1, even outperforming the known-domain baseline on some datasets. This strongly suggests the issue is a proof artifact, but the stated guarantee is what a reader would rely on, and the gap between theory and practice is significant and unacknowledged.

- **Corollary 4.6 states the lower bound with the wrong inequality direction.** The corollary reads: `𝔼[Hits(W, S)] ≥ Opt(W, k) − Ω̃(k/ε)`. The surrounding text ("one must lose k/ε from the optimal value") indicates the intended meaning is that no algorithm can achieve better than Opt − Ω̃(k/ε), which should use ≤. As written with ≥, the result is either vacuous (if the Ω̃ term exceeds Opt) or trivially satisfied. This appears to be a typo in a key result that should be corrected.

### Minor

- **Set union experiments report only average MM without variance, unlike k-hitting set experiments.** The k-hitting set results (Section 5.3) explicitly report standard errors across 5 trials, but the set union results (Section 5.1) report only averages. This inconsistency makes it harder to assess the significance of the reported 5% gap between WGM and the policy mechanisms.

- **No practical guidance for choosing Δ₀.** While Lemma 3.1 bounds `max_i |W_i|` for Zipfian datasets, practitioners don't know the Zipfian parameters a priori. The experiments fix Δ₀ = 100 and Figure 1 shows significant sensitivity (Δ₀ = 1 performs poorly). A brief discussion or heuristic based on the theoretical analysis would strengthen practical applicability.

### Trivial
None.

## Nice-to-Haves
- A brief discussion of the ℓ₀ missing mass (p = 0) connection to existing cardinality-based results, bridging the old and new frameworks (mentioned in §2.3 but not explored).
- Confidence intervals for set union experiments to match k-hitting set reporting.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Nitpicks about formatting, typos, or parser artifacts (these are parser issues, not paper problems).
- Generic reproducibility concerns about hyperparameters (sufficient detail is provided for a theory paper).
- Criticisms about missing related works (cannot verify existence without external sources).

## Novel Insights
The key novel insight is the reframing from cardinality (ℓ₀) to missing mass (ℓ₁/ℓ∞) as the natural objective for DP set union. This is not merely a relabeling: the ℓ∞ variant enables distribution-free analysis (Theorem 3.6) that the cardinality objective cannot support, and this distributional freedom is precisely what makes the downstream extensions to top-k and k-hitting set possible without Zipfian assumptions. The matching upper/lower bounds demonstrate that WGM—a simple, scalable mechanism already deployed in practice—is near-optimal for this objective, resolving what was previously an open question about the quality of practical algorithms. The surprising finding that domain filtering via WGM can actually *help* downstream k-hitting set performance (outperforming the known-domain private baseline on some datasets, Figure 3) is an interesting practical insight.

## Suggestions
- Tighten or explicitly discuss the (1 − 1/ε) gap in Theorem 4.5 relative to the known-domain (1 − 1/e) result from Mitrovic et al. (2017).
- Fix the inequality direction in Corollary 4.6 (≥ should be ≤).
- Report standard errors for set union experiments (Section 5.1) to match the k-hitting set reporting style.
- Add a brief discussion on practical Δ₀ selection heuristics.

## Calibration Report

**Anchors retrieved:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | uxFme785fq (Nonlinear Inference for DP) | 2.50 | Weak DP paper, incremental; much weaker than this paper |
| 1 | TbOcySs6g8 (DP Synthetic Dataset Alignment) | 2.50 | Weak DP paper, flawed contribution; much weaker |
| 1 | WhIuLQWCWS (DP Federated k-Means) | 3.00 | Weak DP clustering paper; much weaker |
| 1 | nM2kuesKpC (D2P2-SGD) | 3.00 | Incremental optimizer paper; much weaker |
| 1 | S6Dn3uyM2p (DP One Permutation Hashing) | 4.60 | Straightforward DP extension; weaker |
| 1 | fj5SqqXfn1 (Privacy Accounting Pitfalls) | 5.00 | Important message but lacks rigor; weaker |
| 1 | yfZJdCijo6 (Max Coverage Turnstile Streams) | 5.25 | Streaming combinatorial paper; weaker |
| 1 | mkXi7O0fun (Data Value on Private Gradients) | 5.25 | Applied DP paper; weaker |
| 1 | 1DEEVAl5QX (Mini-batch Submodular Maximization) | 4.67 | Submodular optimization, no DP; weaker |
| 1 | vtCkb4KJxr (Adaptive Threshold Submodular) | 5.50 | Noisy submodular maximization; weaker |
| 1 | hVTaXJ0I5M (Privately Counting Partially Ordered) | 6.75 | Good DP theory, one mechanism; comparable but this paper is broader |
| 1 | fbqOEOqurU (Optimality of Matrix Mechanism) | 7.00 | Strong DP theory, tight characterization; comparable depth |
| 1 | FZS5m1cbFU (DP Range Subgraph Counting) | 5.67 | DP graph algorithm, rejected; weaker |
| 1 | 6tqgL8VluV (Guaranteed Error for Learned DB) | 6.00 | Different area; somewhat comparable in rigor |
| 1 | EUSkm2sVJ6 (Dataset Usage Cardinality Inference) | 7.60 | Different area, strong paper; somewhat comparable |
| 1 | f4gF6AIHRy (Submodular File Selection for LLMs) | 8.00 | LLM data selection; different area |
| 1 | A3YUPeJTNR (Hidden Cost of Waiting) | 8.00 | Prediction/allocation theory; different area |
| 1 | oZtt0pRnOl (DP Few-Shot ICL) | 8.00 | LLM + DP applied paper; different area |
| 1 | fMTPkDEhLQ (Tight Lower Bounds Hölder) | 8.00 | Optimization lower bounds; different area |
| 1 | PHg4rAXFVH (RTop-K GPU) | 3.40 | GPU implementation; irrelevant |
| 1 | yfZJdCijo6 (Max Coverage) | 5.25 | Streaming/sketching; weaker |

**Round-1 bracket:** The paper is clearly above the 4–5.5 reject range (straightforward extensions, lack of rigor) and comparable to "Privately Counting Partially Ordered Data" (6.75) and "Optimality of Matrix Mechanism" (7.00). It has broader scope than either of those papers (covering set union + top-k + k-hitting set) with matching bounds, but has the Theorem 4.5 (1−1/ε) issue. Bracket: **6.5–7.5**.

**Final score rationale:** The paper's core contribution—near-optimal missing mass guarantees for WGM with matching bounds—is strong and well-supported. The distribution-free ℓ∞ result is elegant and enables practical downstream applications. The k-hitting set analysis weakness and Corollary 4.6 typo are real but do not undermine the main contributions. The paper is comparable in quality to the "Optimality of Matrix Mechanism" paper (7.00), with broader practical scope but a weaker secondary result (k-hitting set). Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>