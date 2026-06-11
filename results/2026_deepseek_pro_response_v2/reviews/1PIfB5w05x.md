Now let me write the final review.

## Summary

This paper studies sparse recovery when observations come from two sources with different noise variances (σ₁² and σ₂²). It distinguishes agnostic (decoder doesn't know per-sample variances) vs. informed (decoder knows them) settings, analyzing both information-theoretic recovery via MLE over the binary-sparse set and algorithmic recovery via the LASSO. The central concept is the "Price of Quality" (γ) — how many low-quality samples replace one high-quality sample while preserving a sufficient condition for recovery. Two headline findings: (i) in the agnostic information-theoretic setting, γ is bounded (γ ≤ 2); in the informed setting, γ can be arbitrarily large; (ii) for the LASSO in the agnostic setting, the recovery threshold depends only on the total sample size n and the average noise level σ²_avg — high- and low-quality samples contribute equally.

## Strengths

- **Theorem 3 establishes a full phase transition (necessary and sufficient) for LASSO signed-support recovery under heterogeneous noise, showing the threshold depends only on σ²_avg.** The necessity result (failure below n_ALG with probability → 1, eq. 26) and sufficiency result (success above n_ALG with appropriate λ_p, eqs. 27–28) together give a sharp characterization. The finding that the algorithmic threshold n_ALG = 2s log(p−s) + s + 1 matches the homogeneous-noise case and that the regularization condition (28) depends only on σ²_avg is surprising and well-substantiated.

- **The proof of Theorem 3 requires a non-trivial technical innovation.** As noted in the proof sketch (lines 304–305), the non-scalar diagonal Σ breaks the Wishart structure (X_S^T X_S) used in Wainwright (2009). The authors resolve this via a Gram–Schmidt (QR) decomposition of X_S and leverage properties of the Haar measure on the orthogonal group. This is a genuine technical contribution beyond straightforward adaptation.

- **Theorem 2 yields a closed-form sufficient condition for the informed setting with an exactly optimized Chernoff exponent.** Unlike Theorem 1 where a relaxation is needed, the informed MLE's rescaled loss (15) admits exact Chernoff optimization, producing condition (16). This enables sharp asymptotic analysis of γ across all SNR regimes (eqs. 19–21), including the striking γ → ∞ result in the low-SNR₂/high-SNR₁ regime.

- **Proposition 4.1 gives an explicit, constructive condition on noise scaling for LASSO recovery.** The result provides a necessary and sufficient condition (30) on σ²_avg for the existence of a valid λ_p, and explicitly constructs λ_p via (31). This makes Theorem 3's asymptotic conditions concretely realizable rather than purely existential.

- **The "Price of Quality" framework (γ, eq. 5) provides a clean, interpretable metric for comparing the two settings.** The asymptotic analysis across SNR regimes yields clear contrasts: bounded γ < 2 in the agnostic case vs. unbounded γ in the informed case.

- **The paper is transparent about its limitations.** Remark 3.2 acknowledges the non-tightness of the agnostic sufficient condition, Remark 4.1 notes the restriction to independent features, and Remark 4.2 explains the technical obstacle preventing extension of Theorem 3 to the informed setting.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Equation (12) contains a typo that makes it inconsistent with equation (9).** In (9), the coefficient of n₁ uses denominator 2σ₂²: log(1 + δ(2σ₂² − σ₁²)s/(2σ₂²)). But (12) defines γ with denominator 2σ₁⁴ in the numerator's log argument. The asymptotic expansions (13) and (14) are derived from the expression in (9), not (12) — for instance, (14) algebraically simplifies to 2 − σ₁²/σ₂² using (9)'s denominator, whereas using (12)'s σ₁⁴ would give (2σ₂² − σ₁²)σ₂²/σ₁⁴, which does not reduce to 2 − σ₁²/σ₂² in general. This is a clearly fixable typo, but it appears in one of the paper's most central displayed equations defining the Price of Quality.

- **The agnostic γ ≤ 2 bound comes from a sufficient condition that is explicitly acknowledged as non-tight (Remark 3.2), which somewhat weakens the agnostic-vs.-informed contrast that structures the paper's narrative.** The paper is honest about this — the Chernoff relaxation is disclosed and the cubic equation for the tight exponent is mentioned. However, the abstract and introduction present the γ ≤ 2 result as a headline finding without foregrounding the non-tightness caveat, which could mislead a reader who does not reach Remark 3.2. The contrast between a non-tight agnostic bound and a tight informed bound is less definitive than the paper's framing suggests.

### Trivial

None.

## Nice-to-Haves

- A simple simulation illustrating the Price of Quality — e.g., sweeping (n₁, n₂) and showing where recovery succeeds vs. fails, overlaid with the theoretical sufficient conditions — would help readers internalize the threshold behavior. Not required for a theory paper, but would increase impact.

- The agnostic estimator (8) computes MLE over the binary-sparse set, which is NP-hard. The paper could briefly note this computational infeasibility when introducing (8), to avoid confusion between the information-theoretic and algorithmic analyses.

- The generalization to arbitrary diagonal Σ in Remark 3.4 is stated without derivation. Even a brief sketch of how the proof extends would help.

- A few more sentences in the proof sketch for Theorem 3(i) explaining why heterogeneous noise does not create a "loophole" that lets LASSO succeed below n_ALG would strengthen reader confidence in the necessity direction.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 3 (Theorem 3(i) proof sketch too compressed; appendix stripped).** Removed per rules — the appendix exists in the original submission. The criticism that the reader "cannot assess whether the argument correctly handles the fact that the noise is no longer exchangeable" stems from the appendix being stripped by the parser, not from an author error. The full proof is in Appendix D.

## Novel Insights

The most striking insight emerging from this work is the asymmetry between how data heterogeneity affects information-theoretic vs. algorithmic recovery: the information-theoretic threshold is sensitive to the full (σ₁², σ₂²) structure (hence the Price of Quality varies between the agnostic and informed settings), while the algorithmic LASSO threshold collapses to depend only on the average noise σ²_avg — making high- and low-quality data effectively interchangeable for computational recovery. This is not just a technical curiosity; it suggests a broader principle that polynomial-time algorithms may be inherently more "robust" to distribution shift than optimal (exponential-time) decoders, which connects to the OGP literature on algorithmic hardness.

## Suggestions

- Fix the typo in equation (12): change σ₁⁴ to σ₂² in the denominator of the log argument to match equation (9) and the subsequent asymptotic expansions.
- In the abstract and introduction, make the non-tightness of the agnostic sufficient condition more prominent when presenting the γ ≤ 2 result (e.g., "under our sufficient condition, one high-quality sample is never worth more than two").
- Verify that equation (22) in Remark 3.4 — which uses σ_max(Σ)⁴ in the denominator analogously to (12) — is not affected by the same typo pattern.

---

## Calibration

**Round 1 (Bracketing):** Retrieved anchors across three bands. The paper sits above the weak band (2.33–3.25, all on unrelated topics) and the middle band (5.00–7.00), and below the strong band (7.60–8.00). Initial bracket: **6.5 – 7.5**.

**Round 2 (Narrowing):** Retrieved additional anchors inside the bracket for direct comparison.

Anchor-by-anchor comparison:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| vQIVbfTMzf | 3.25 | R1 | Heavy-tailed robust estimation — far weaker, not comparable |
| 2NwHLAffZZ | 2.33 | R1 | Gradient-based learning linearization — far weaker |
| Zap3nZhRIQ | 3.00 | R1 | Non-differentiability in NNs — far weaker |
| ZDoaLbOFaP | 3.00 | R1 | Sparse covariance NNs — far weaker |
| gVVoZtiQlt | 5.00 | R1 | Shuffled regression phase transition — our paper is stronger |
| sIcPMMhl9W | 5.80 | R1/R2 | Shuffled regression (variant) — our paper is stronger |
| FT4gAPFsQd | 6.00 | R2 | Pruning deep networks — our paper is stronger |
| fuoM5YDBX4 | 6.00 | R2 | Transformer group-sparse classification — our paper is stronger |
| wpXGPCBOTX | 6.75 | R1/R2 | Sparsistency for iOT — our paper is clearer and more original |
| RsJwmWvE6Q | 6.75 | R2 | Optimal sketching — incremental improvement; ours is more original |
| NHhjczmJjo | 7.00 | R1/R2 | Transformers in ICL sparse recovery — has more substantive issues (non-standard assumptions, existence vs. training gap); ours is cleaner |
| fbqOEOqurU | 7.00 | R2 | Matrix mechanism optimality — close follow-up to prior work, dense; ours is better motivated |
| Tzh6xAJSll | 7.60 | R1 | Scaling laws for associative memories — both theory and experiments, cleaner presentation; ours is below this |
| 4xWQS2z77v | 8.00 | R1 | Loss landscape of regularized NNs — far stronger |
| et5l9qPUhm | 8.00 | R1 | Strong model collapse — far stronger |
| fMTPkDEhLQ | 8.00 | R1 | Tight lower bounds — far stronger |

The paper is clearly above the 7.00 cluster (NHhjczmJjo, fbqOEOqurU) — it has fewer substantive issues and is more original and better motivated. It sits below Tzh6xAJSll (7.60) — that paper combines theory with extensive experiments and has cleaner presentation. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>