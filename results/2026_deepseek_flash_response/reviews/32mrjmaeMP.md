## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless method for weight disentanglement in task arithmetic. The key insight is that representation drift regularization can be reformulated as a curvature matrix (GGN) approximation problem, enabling the use of KFAC to construct a regularizer that does not require sharing raw data between tasks. The method achieves constant O(1) complexity in the number of tasks via a Kronecker-factor merging heuristic, demonstrates strong performance on vision task addition/negation benchmarks (matching or exceeding the data-dependent τJp), and exhibits robustness to the α scaling coefficient.

## Strengths

- **Strong empirical results on vision task negation** where TAK (dataless) surpasses even the data-dependent τJp on ViT-B/32 and ViT-B/16 (Table 2), achieving lower target-task forgetting and higher control-task accuracy. This is a clean demonstration of the method's advantage in the harder setting.

- **The O(1) complexity in the number of tasks via accumulated Kronecker factors** (Eq. 8) is a genuine algorithmic contribution. Table 3 shows the gap from the idealized multi-task formulation is at most 0.8 points across three architectures/domains, validating the heuristic empirically.

- **Robustness to α scaling** eliminates the need for held-out tuning (Fig. 4a): TAK maintains stable accuracy across α ∈ [0, 2] while all other methods exhibit sharp peaks and declines. This is a practical advantage for real-world deployment where validation data may be unavailable.

- **Extensive ablations** validate design choices systematically: KFAC estimation with 128–256 examples suffices (Fig. 7a), compression reduces storage by 87% with ~1-point drop (Fig. 7b), and the regularizer can be applied every 16 steps with modest degradation (Fig. 8).

- **Low practical overhead**: KFAC precomputation takes ~4 minutes (Fig. 6b) and training time is about one-third that of the data-dependent τJp (Fig. 6a).

## Weaknesses

### Major

None.

### Minor

- **Overstated SOTA claim**: The abstract and introduction claim "state-of-the-art results in task addition and negation" without qualification. On language tasks (T5-base), TAK (78.7) lags behind τJp (81.3) by 2.6 points (Table 3a). On vision addition, TAK and τJp are essentially tied (e.g., 86.0 vs 85.6 on ViT-B/32). The claim should be calibrated: TAK achieves SOTA on vision task negation and is competitive on vision addition, while underperforming on language. This does not diminish the contribution but the framing should be precise.

- **No uncertainty quantification**: No standard deviations or confidence intervals are reported for any main result (Tables 1–3). While this follows the convention of the task-arithmetic literature (where cited baselines also report single scalars), it limits assessment of whether narrow margins (e.g., 86.0 vs 85.6 on ViT-B/32) are meaningful. Reporting variance across seeds for at least the core comparisons would strengthen the quantitative claims.

- **Kronecker merging heuristic lacks theoretical justification**: The merge in Eq. 8 replaces Σ(B_t ⊗ λ_t A_t) with (Σ B_t) ⊗ (Σ λ_t A_t) — these are not equal. The paper provides empirical validation (Table 3, gap 0.2–0.8 points) but no theoretical analysis. Given that the paper's O(1) complexity claim rests on this approximation, more discussion of when it might break down (or a justification beyond "empirically matches") would be helpful.

- **Squared-loss GGN substitution**: The derivation uses the GGN under squared loss (∇²c_n = I_C) rather than the actual training criterion (cross-entropy). The paper acknowledges this (Sec. 3.2) but does not discuss whether using cross-entropy curvature would affect regularization quality. A brief justification or empirical analysis would strengthen the methodological framing.

### Trivial

None.

## Nice-to-Haves

- An analysis of why KFAC underperforms τJp on language (e.g., is it the Kronecker approximation quality for Transformers, the squared-loss proxy, or the architecture?) would strengthen the paper even as a negative result.
- A sensitivity analysis over the overall regularization strength β (all experiments use a fixed β).
- Comparison with Fisher merging or RegMean for broader positioning.

## Removed Points

These points are flagged to be removed, treat them with caution:
- "Dataless framing is overclaimed" — The paper transparently states that KFAC factors are computed on training data and "after initial pre-computation does not require further data access" (line 83). This is standard terminology in privacy-preserving ML and the paper is clear about the initial requirement.
- "Diagonal GGN baseline insufficiently described" — The paper cites the original work (Porrello et al., 2025) and describes the baseline adequately as a coarse diagonal GGN approximation. Implementation details follow from the citation.
- "Missing related works" — Cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Rephrase "state-of-the-art" in the abstract and introduction to "state-of-the-art on vision task negation and competitive on task addition" or similar calibrated language.
- Add standard deviations from multiple seeds to at least the core comparison tables (Tables 1–2) for the main architectures.
- Add a brief discussion (or reference to appendix analysis) on why the squared-loss GGN substitution is appropriate for representation drift regularization.

## Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (score < 3.5): ATM (3.00), Collective Model Intelligence (3.40), Projected Subnetworks (2.00), Unified View Delta Parameters (2.33) — all rejected, clearly weaker than TAK.
- Middle anchors (3.5–7.5): τJp paper (6.00, Accept), Attention Only FT (6.25, Accept), Submodule Linearity (6.00, Accept), SuperMerge (4.33, Reject).
- Strong anchors (> 7.5): All on unrelated topics (Training on Test Task 8.00, DEPT 8.00, Transformers Reasoning 7.60, Watermarking 7.60).

**Initial bracket:** 5.0–7.0

**Round 2 — Narrowing within bracket:**
- τJp paper (1VwWi6zbxs.md) avg 6.00: Most directly comparable baseline. τJp requires external data; TAK solves this. TAK has broader experiments (language, ablations). TAK is slightly stronger overall.
- Uncertainty-Based Gradient Matching (D7KJmfEDQP.md) avg 6.00: Strong theory, thin experiments. TAK experiments more comprehensive.
- Mitigating Parameter Interference (eaTqsptDPL.md) avg 5.75: SAM-based, limited to vision. TAK stronger.
- NegMerge (bKQJzuBSRJ.md) avg 6.00: Rejected despite 6.0, limited technical depth.

**Final score positioning:** TAK compares favorably to the τJp paper (6.00), Attention Only FT (6.25), and Submodule Linearity (6.00) — all accepted. Its contribution (connecting drift to curvature, enabling dataless regularization, O(1) merging) is novel and well-supported. The weaknesses (SOTA overclaim, missing std devs) are fixable and do not threaten the core claims. Score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>