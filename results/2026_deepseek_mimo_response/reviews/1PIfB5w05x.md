Now I have enough calibration data. Let me write the final review.

## Summary
This paper studies sparse signal recovery when observations arrive from two sources with different noise levels. It introduces the "Price of Quality" γ — the number of low-quality samples needed to replace one high-quality sample for the sufficient recovery condition. The main findings are: (1) in the agnostic setting (decoder ignores noise structure), γ is uniformly bounded by 2; (2) in the informed setting (decoder knows per-sample variances), γ can grow unboundedly; (3) the LASSO threshold in the agnostic setting depends only on average noise σ²_avg, not individual noise levels — a sharp, necessary-and-sufficient result achieved via a novel proof technique using QR decomposition and Haar measure analysis.

## Strengths
- **Sharp agnostic/informed contrast demonstrates a genuine structural phenomenon.** The Price of Quality γ ≤ 2 in the agnostic setting (equation 14) vs. γ → ∞ in the informed setting (equation 20) provides a clean, interpretable demonstration that decoder knowledge of noise structure qualitatively changes the relationship between data quality and recovery. This is supported by closed-form asymptotic expressions in all three SNR regimes (equations 13–14, 19–21). The contrast is robust: the informed result is sharp (exact Chernoff optimization, Remark 3.3), so even if the agnostic bound is loose, the qualitative conclusion that knowing noise variances provides a dramatic advantage holds.

- **Theorem 3 is a sharp, necessary-and-sufficient LASSO phase-transition result with a genuinely novel proof technique.** The LASSO threshold matching the homogeneous case (equations 26–27), depending only on n and σ²_avg (equation 28), is striking and non-obvious — the proof extends Wainwright (2009) to heterogeneous noise by applying QR decomposition and analyzing the resulting orthogonal matrix via the Haar measure on the orthogonal group (line 304, Lemma D.6), overcoming the loss of Wishart structure when Σ is no longer scalar.

- **Generality beyond the two-source model.** Remark 3.4 shows the sufficient conditions extend to arbitrary invertible Σ (equations 22–23), demonstrating the results capture a structural phenomenon about heterogeneous noise rather than being artifacts of a toy two-source setup.

- **Honest characterization of tightness.** Remark 3.2 transparently acknowledges the agnostic sufficient condition is not expected to be sharp, explains the source of looseness (relaxation of a cubic equation in the Chernoff exponent, equation 37), and contrasts with the sharp informed setting and sharp LASSO results. This builds trust and clearly identifies which results are tight and which are not.

## Weaknesses

### Fatal
None.

### Major
- **The agnostic Price of Quality bound γ ≤ 2 is a property of the sufficient condition, not necessarily of the problem, which limits its interpretive value.** Remark 3.2 explicitly acknowledges: "optimizing (37) would similarly lead to a tighter characterization here, though we do not pursue this direction." The headline claim "one high-quality sample is never worth more than two low-quality samples" (abstract, Section 1.2.1, Section 5) follows from this potentially loose bound. If the sufficient condition is substantially loose, the true price of quality in the agnostic setting could differ significantly. The informed contrast (γ → ∞) is genuinely sharp (exact Chernoff optimization), but the agnostic half of the story's definitiveness is limited. This doesn't invalidate the paper — the authors are transparent, the structural insight (bounded vs. unbounded) is likely genuine, and the LASSO result provides additional evidence — but it is the paper's most significant limitation and warrants explicit discussion of what γ values are actually achievable.

### Minor
- **No numerical simulations to assess tightness.** Even for a theory paper, phase-transition simulations (varying n₁, n₂ for fixed p, s, σ₁², σ₂² and plotting recovery probability) would substantially strengthen the paper. An empirical phase boundary plotted against the theoretical sufficient condition would immediately clarify the agnostic bound's looseness and make the results much more tangible. This is the single highest-leverage improvement available.

- **The informed-setting MLE (equation 15) is combinatorial over s-sparse supports.** The paper does not discuss the computational intractability of this estimator, meaning the dramatic γ → ∞ result has no known algorithmic realization. While this is standard for information-theoretic results, a brief remark noting this limitation and its implications would strengthen the paper. Remark 4.2 discusses the informed LASSO as future work but does not speculate about whether the price of quality there would be bounded or unbounded — even a conjecture would help frame the gap.

### Trivial
None.

## Nice-to-Haves
- The structural observation that in the low-SNR agnostic regime, γ = 2 − σ₁²/σ₂² ∈ (1, 2) regardless of the noise gap (equation 14) could be stated more explicitly as a clean result.
- A conjecture on the informed LASSO's price of quality would help frame the open problem identified in Remark 4.2.

## Removed Points
- Harsh Critic's concern about SNR notation in equation (7) using β instead of β* — not an actual issue; β* is defined as the signal and the formula is correct for binary signals where E∥Xβ*∥₂² = ns.
- "Missing related works" points — cannot verify external references; removed per policy.

## Novel Insights
The paper's most novel insight is the qualitative difference between how information-theoretic and algorithmic thresholds adapt to data heterogeneity. The IT threshold distinguishes high- and low-quality data (via the Price of Quality γ), while the LASSO threshold treats them identically depending only on σ²_avg. This parallels observations by Wang et al. (2010) and Omidiran & Wainwright (2008) about sparse designs, where the algorithmic threshold is also more "robust" to changes in problem structure than the IT threshold. The Price of Quality framework provides the first clean quantitative lens for this qualitative observation, and the paper demonstrates it extends to a new dimension of problem heterogeneity.

## Suggestions
- Add a small set of simulations showing empirical phase transitions vs. theoretical sufficient conditions, especially for the agnostic setting. This would directly address the paper's main open question.
- State the γ ∈ (1, 2) observation for the low-SNR agnostic regime more explicitly.
- Add a brief remark about the computational intractability of the informed MLE and speculate on the informed LASSO price of quality.

## Calibration Report

**Anchors retrieved:**

*Round 1:*
- ZDoaLbOFaP.md (3.00, weak) — Sparse Covariance Neural Networks; topically unrelated, rejected
- S3zKrEQpRr.md (3.00, weak) — GNN noisy channels; unrelated
- vQIVbfTMzf.md (3.25, weak) — Adapting to regimes; unrelated
- zqXANcFO9T.md (1.67, weak) — Decentralized learning; unrelated
- wpXGPCBOTX.md (6.75, middle) — Sparsistency for inverse optimal transport; related theory paper, accepted
- NHhjczmJjo.md (7.00, middle) — Transformers in-context sparse recovery; directly related, accepted
- sIcPMMhl9W.md (5.80, middle) — Shuffled regression phase transition; related theory, rejected
- gVVoZtiQlt.md (5.00, middle) — Same paper, rejected
- fMTPkDEhLQ.md (8.00, strong) — Tight lower bounds; strong theory, accepted
- WJaUkwci9o.md (8.00, strong) — Self-improvement; unrelated
- hrqNOxpItr.md (8.00, strong) — Cross-entropy; unrelated
- 5t57omGVMw.md (8.00, strong) — Linear system solver; unrelated

*Round 2:*
- qZwtPEw2qN.md (6.80, lower) — Noisy image scaling laws; related (heterogeneous noise), accepted
- qcigbR1UYA.md (5.25, lower) — Active binary testing; somewhat related, rejected
- ILqA09Oeq2.md (6.20, lower) — Multi-view clustering performance gaps; related theory, accepted
- 4vzGQcVUG8.md (6.50, lower) — Weak-to-strong generalization; related theory, accepted
- fMTPkDEhLQ.md (8.00, upper) — Tight lower bounds; strong theory
- 4xWQS2z77v.md (8.00, upper) — Loss landscape; strong theory, accepted
- wISvONp3Kq.md (7.33, upper) — Sparse GLMs; related (sparse methods), accepted
- hiHZVUIYik.md (7.33, upper) — Path-norm toolkit; less related

**Round 1 bracket:** Between 6.0 and 8.0. The paper clearly exceeds the rejected shuffled regression paper (5.80) in clarity and contribution sharpness, but falls short of the strong 8.0 theory papers.

**Round 2 narrowing:** Between 6.5 and 7.5. The paper is above the multi-view clustering (6.20) and weak-to-strong (6.50) papers — it has a sharper central result and cleaner narrative. It is comparable to the sparsistency/iOT paper (6.75) and the noisy image scaling paper (6.80), likely slightly above both due to the stronger narrative arc and the LASSO result being both necessary and sufficient. It is comparable to but not clearly above the transformers sparse recovery paper (7.00) or the sparse GLMs paper (7.33).

**Final score rationale:** The paper's Price of Quality framework is a genuine novel contribution, the LASSO result is sharp and technically impressive, and the agnostic/informed contrast is clearly presented. The main limitation is the acknowledged looseness of the agnostic bound and the absence of simulations. Comparing against anchors: it sits above the 6.5–6.8 papers (cleaner contribution, sharper results) and at approximately the level of the 7.00 sparse recovery paper, but below the 7.33 sparse GLMs paper which has both theory and experiments. Score: 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>