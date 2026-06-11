Now I have all the information needed. Let me produce the final review.

## Summary

This paper studies sparse support recovery when observations come from two sources with different noise levels (heteroscedastic Gaussian noise). It establishes sufficient conditions for information-theoretic recovery (Theorems 1, 2) and algorithmic recovery via the LASSO (Theorem 3) in two settings: *agnostic* (decoder does not know per-sample noise variances) and *informed* (decoder knows them). The central concept is the *Price of Quality* — the exchange rate between high- and low-quality samples in the sufficient condition. In the agnostic setting, the Price of Quality is uniformly bounded by 2; in the informed setting, it can grow arbitrarily large. For LASSO recovery, the phase transition depends only on total sample size and average noise, revealing an asymmetry between the information-theoretic and algorithmic thresholds.

## Strengths

1. **First explicit trade-off between high- and low-quality data for sparse recovery.** The sufficient conditions (Theorems 1, 2) factorize into α₁n₁ + α₂n₂ > n*, yielding a well-defined exchange rate γ = α₁/α₂ (the Price of Quality). Prior homogeneous-noise work (Wainwright, 2009; Reeves et al., 2019; Gamarnik & Zadik, 2022) had no notion of sample-quality trade-off because all observations had identical noise. This is a genuinely new quantity for the mixed-quality setting.

2. **Non-obvious bound γ < 2 in the agnostic setting.** Equation (14) gives γ ≃ 2 − σ₁²/σ₂² < 2 in the low-SNR₂ regime, showing that even when the low-quality observations are very noisy, one high-quality sample is worth at most two low-quality samples under the sufficient condition. This contrasts sharply with the informed setting, where γ can be arbitrarily large (Equation 20), highlighting the practical importance of knowing per-sample variance.

3. **Genuine technical extension of the LASSO phase transition to heterogeneous noise.** Theorem 3 extends Wainwright (2009) to the case where the noise covariance Σ is no longer a scalar multiple of the identity, which the paper notes "causes key steps of the classical proof to fail" (line 304). The paper overcomes this via QR decomposition and Haar-measure arguments on the orthogonal group (Lemma D.6) — a non-trivial technical advance that required tools from random-matrix theory not needed in the homogeneous-noise setting.

4. **Full two-sided characterization of the LASSO threshold with explicit λₚ.** Theorem 3 provides both necessary (26) and sufficient (27–28) conditions. Proposition 4.1 gives the exact noise-scaling condition (30) and an explicit λₚ (31) that satisfies the sufficient conditions. Prior LASSO analyses covered only the homogeneous-noise case, so the two-sided characterization with explicit regularization parameter is new.

5. **Identifies a fundamental asymmetry between information-theoretic and algorithmic thresholds.** The information-theoretic sufficient condition (Theorem 1) depends on the individual noise variances σ₁², σ₂², while the LASSO threshold (Theorem 3) is completely independent of them. The paper explicitly highlights this contrast (lines 337–338), offering insight beyond the individual results.

6. **Generalization to arbitrary invertible noise covariance.** Remark 3.4 provides extensions (22–23) for general Σ, demonstrating the analysis is not tied to the specific two-block-diagonal structure.

## Weaknesses

### Fatal
None.

### Major
- **Internal contradiction about sharpness of the informed information-theoretic threshold.** Remark 3.3 (line 251) states: *"Establishing full necessity in the heterogeneous setting remains an interesting direction for future work."* Yet the conclusion (line 340) states: *"the informed information-theoretic threshold and the LASSO threshold are sharp."* These statements are incompatible. If necessity has not been proved, the threshold cannot be called "sharp" in the standard sense (which requires both necessity and sufficiency). The LASSO threshold sharpness is correctly justified (Theorem 3 gives both directions), but the informed information-theoretic sharpness claim directly contradicts the more cautious statement in Remark 3.3. This must be resolved: either prove necessity for the informed setting and state it clearly, or modify the conclusion to correctly reflect that the informed information-theoretic condition is *conjectured* to be sharp but necessity is not yet established.

### Minor
- **The headline Price of Quality bound (γ ≤ 2) applies only to a sufficient condition acknowledged as potentially loose.** The paper is transparent about this (Remark 3.2): the agnostic condition comes from relaxing a cubic equation (37) whose exact solution would give a tighter characterization. In the homogeneous-noise case, solving the analogous equation recovers the sharp threshold; in the heterogeneous case, this optimization has not been carried out. The paper's hedging language is appropriate, but it does mean the most striking quantitative claim — that one high-quality sample is never worth more than two low-quality ones — rests on a condition the paper itself says is not tight. A tighter bound could change (or even eliminate) this bound.

- **The LASSO Theorem 3 sufficient condition requires λₚ to satisfy bounds involving σ²_avg, but the paper does not discuss how an agnostic decoder (who does not know σ₁², σ₂²) would choose such a λₚ in practice.** While the paper's contribution is a theoretical characterization, Proposition 4.1 gives an explicit λₚ formula (31) involving σ²_avg = (n₁σ₁² + n₂σ₂²)/n, yet provides no guidance on how an agnostic decoder would estimate this quantity. A brief remark about estimating σ²_avg from data (e.g., via residual variance estimation) would bridge the gap between the theoretical result and its practical interpretation.

### Trivial
None.

## Nice-to-Haves
- **Optimize the Chernoff exponent exactly in the agnostic setting.** The paper acknowledges the cubic equation (37) leads to a tighter bound. Solving this exactly would either validate or modify the γ ≤ 2 claim and is identified by the paper itself as the most impactful improvement.
- **Numerical illustrations.** Simulations showing the phase transition in (n₁, n₂) space — e.g., fixing total n and varying n₁/n₂ — would make the qualitative behavior of the Price of Quality concrete. Not required for a theory paper but helpful for intuition.
- **A brief conjecture about the informed LASSO.** Remark 4.2 explains why the proof fails (loss of Wishart structure), but no speculation about what the result might look like is offered. A brief discussion of whether the Price of Quality for the informed LASSO would resemble the information-theoretic informed case or the agnostic LASSO case would strengthen the narrative.

## Removed Points
*These points were flagged for removal; treat them with caution.*
- **Parser artifact in Eq. (12) vs. (9):** The harsh critic noted σ₁⁴ appears where σ₂² might be intended. This is a formatting artifact from PDF extraction, not an author error. (Removed per hard rules on formatting artifacts.)
- **Generalization formulae not derived in main text (Remark 3.4):** The formulae are sketched in the main text; full derivation is in the appendix, which is standard practice for theory papers. (Removed per relevance.)
- **No numerical illustrations as a weakness:** Downgraded to Nice-to-Have. Simulations are not required for theory papers. (Removed per soft rules.)
- **Informed LASSO absent as a weakness:** Downgraded to Nice-to-Have. The paper clearly explains why this is not addressed (Remark 4.2), making this a scope limitation, not a weakness. (Removed per soft rules.)

## Novel Insights
None beyond the paper's own contributions. The main insight surfaced by the review process is the internal contradiction between Remark 3.3 (line 251) and the conclusion (line 340) regarding sharpness of the informed information-theoretic threshold. The reviewers otherwise surface observations that the paper already addresses transparently — notably that the agnostic Price of Quality bound applies to a sufficient condition, which the paper explicitly discusses in Remark 3.2.

## Suggestions
1. **Resolve the sharpness contradiction:** Either prove necessity for the informed setting and state it clearly, or modify line 340 to correctly reflect that the informed information-theoretic threshold is *conjectured* to be sharp but necessity is not yet established.
2. **Add a brief practical discussion for Theorem 3:** Include a remark in Section 4 discussing how an agnostic decoder could estimate σ²_avg (e.g., via residual sum-of-squares estimation) to enable the λₚ selection required by Theorem 3 / Proposition 4.1.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `JXvEzl8YkS.md` (Regularised Jump Models) | 2.00 | R1 | Unrelated topic; much weaker paper |
| `Zap3nZhRIQ.md` (Non-differentiability & NN training) | 3.00 | R1 | Unrelated topic; weaker |
| `ZDoaLbOFaP.md` (Sparse Covariance NNs) | 3.00 | R1 | Unrelated topic; weaker |
| `vQIVbfTMzf.md` (Adapting to finite-sample) | 3.25 | R1 | Unrelated topic; weaker |
| `L0pMPCmEfN.md` (Splitted Wavelet) | 4.33 | R1 | Unrelated topic; weaker |
| `gVVoZtiQlt.md` (Phase Transition of Shuffled Regression) | 5.00 | R2 | Similar topic (phase transitions in regression), but that paper's analysis was described as heuristic/non-rigorous; this paper is clearly stronger with rigorous proofs |
| `sIcPMMhl9W.md` (Phase Transition of Shuffled Regression v2) | 5.80 | R2 | Same paper, similar comparison — our paper is more rigorous |
| `qcigbR1UYA.md` (Active Binary Testing) | 5.25 | R1 | Different topic; roughly similar tier |
| `ILqA09Oeq2.md` (Multi-view Clustering, Matrix-Tensor) | 6.20 | R1 | Comparable: pure theory paper with phase transitions; our paper has comparable theoretical depth |
| `qZwtPEw2qN.md` (Noisy Image Worth / Ambient Diffusion) | 6.80 | R1 | Somewhat similar theme (data quality trade-offs), but that paper had experiments + theory; our paper is comparable theoretically but lacks experiments |
| `NHhjczmJjo.md` (Transformers ICL Sparse Recovery) | 7.00 | R2 | Related topic (LASSO/sparse recovery); comparable contribution depth |
| `4xWQS2z77v.md` (Loss Landscape via Convex Duality) | 8.00 | R1 | Significantly stronger mature contribution |
| `hrqNOxpItr.md` (Cross-Entropy Inverts DGP) | 8.00 | R1 | Significantly stronger |

**Round 1 Bracket:** Between 5.0 and 7.0.
**Round 2 Narrowing:** Comparison with shuffled regression papers (5.00–5.80) confirms our paper is stronger (rigorous proofs vs. heuristic derivations). Comparison with the transformers ICL sparse recovery paper (7.00) shows our paper has comparable theoretical depth and fewer weaknesses, though it lacks experiments. The most natural comparison is the 6.20 multi-view clustering paper, which is a pure theory paper with phase transitions and similar evaluation profile.
**Final Score:** 6.5 — solid theoretical contribution with novel problem framing, non-trivial technical extensions, and one fixable internal contradiction. Above the heuristic-style papers (5.0–5.8), comparable to other rigorous theory papers (6.2), and slightly below papers with combined theory+experiments (6.8–7.0).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>