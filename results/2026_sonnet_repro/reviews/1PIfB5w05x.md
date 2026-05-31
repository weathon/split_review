Now let me perform the calibration search to find comparable papers.Now I'll do Round 2 to narrow the bracket. Based on Round 1, the paper seems to sit in the 5–7 range. Let me narrow:Now I have enough information to write the full review. Let me synthesize everything.

---

## Summary

This paper studies sparse recovery when observations come from two heterogeneous noise sources — a small collection of high-quality measurements (variance $\sigma_1^2$) and a larger set of low-quality ones (variance $\sigma_2^2 > \sigma_1^2$). The authors establish sufficient sample-size conditions for information-theoretic support recovery in both an agnostic setting (Theorem 1) and an informed setting (Theorem 2), and introduce the **Price of Quality** (PoQ) $\gamma$ — the number of low-quality samples equivalent to one high-quality sample — as a unifying lens. They further prove (Theorem 3) that the LASSO recovery threshold in the heterogeneous agnostic setting matches the classical homogeneous threshold and depends on the noise only through its average $\sigma_{\text{avg}}^2$. The central finding is a striking dichotomy: the PoQ is bounded above by 2 in the agnostic IT setting, but can be arbitrarily large in the informed IT setting, while the algorithmic (LASSO) threshold is entirely blind to the data-quality split.

---

## Strengths

1. **Explicit, closed-form PoQ expressions in both settings (eqs. 12, 18).** The paper derives $\gamma$ as a ratio of Chernoff-exponent coefficients, characterizes its behavior in high-SNR (eq. 13), low-SNR (eq. 14), and mixed-SNR (eqs. 19–21) regimes, and uses this to prove a concrete bounded vs. unbounded dichotomy between the agnostic and informed cases.

2. **Theorem 3 (LASSO phase transition) is technically solid and somewhat surprising.** The result proves that the signed-support recovery threshold $n_\text{ALG} = 2s\log(p-s)+s+1$ and the regularization condition (eq. 28) are both independent of the individual noise levels $\sigma_1^2, \sigma_2^2$ — only $\sigma_\text{avg}^2$ appears. This equality of high- and low-quality samples at the algorithmic threshold is non-obvious and practically important. The proof, adapting Wainwright (2009) via a Gram–Schmidt decomposition of $X_S$ and Haar-measure arguments (Lemma D.6), is a genuine technical contribution to handle the non-scalar $\Sigma$.

3. **Proposition 4.1 complements Theorem 3 cleanly.** The necessary and sufficient condition on noise scaling (eq. 30) and the explicit construction (eq. 31) of a valid $\lambda_p$ tie the admissible noise regime to signal magnitude $\rho$, sparsity $s$, and dimension $p$, making the algorithmic result self-contained.

4. **Generalization to arbitrary noise structures (Remark 3.4).** The sufficient conditions (eqs. 22–23) extend to non-diagonal noise matrices $\Sigma$ via per-sample singular values. This substantially broadens the scope of the IT results beyond the two-block diagonal assumption.

5. **Transparency about limitations.** Remark 3.2 explicitly flags the relaxation step (replacing the cubic equation (37) with a closed-form bound), acknowledges that estimator (8) may not be optimal in the agnostic setting, and discusses the reweighted variant. Section 5 directly states that the agnostic IT condition is "sufficient but not proven tight." This honesty is a genuine strength.

---

## Weaknesses

### Fatal
None.

### Major

- **The PoQ ≤ 2 result lacks a matching lower bound, leaving open whether it is a fundamental information-theoretic quantity or an artifact of the analysis.** The paper's most prominent claim — "one high-quality sample is never worth more than two low-quality samples" — is a property of the sufficient condition derived by relaxing the Chernoff bound (replacing the cubic equation (37) with a closed-form). Remark 3.2 acknowledges that this relaxation may be loose, and also notes that estimator (8) may not be optimal. If a smarter agnostic decoder admitted a tighter sufficient condition with a PoQ substantially larger than 2, the bound would be an artifact of the specific estimator. The contrast between the bounded agnostic PoQ and the unbounded informed PoQ — which is the paper's central finding — therefore rests on an asymmetric evidentiary foundation: the informed side has an exact Chernoff optimization (Remark 3.3 explicitly notes this), while the agnostic side does not. This is a real gap. The paper handles it honestly in the body, but the abstract phrase "one high-quality sample is never worth more than two low-quality samples" is presented without the qualifier "under our sufficient condition" visible until later. Authors should either add a lower-bound argument or more prominently foreground the limitation in the abstract.

### Minor

- **Equation (12) appears inconsistent with equation (9).** The sufficient condition (9) for the agnostic setting has the n₁ coefficient $\log(1 + \delta(2\sigma_2^2 - \sigma_1^2)s / 2\sigma_2^2)$, but equation (12) writes the same numerator as $\log(1 + \delta(2\sigma_2^2 - \sigma_1^2)s / 2\sigma_1^4)$. Substituting the expression in (12) into the low-SNR asymptotic does not yield the claimed $\gamma \approx 2 - \sigma_1^2/\sigma_2^2$ in (14): that derivation only works if the denominator in the argument is $2\sigma_2^2$, as in (9). The inconsistency should be resolved and eq. (12) corrected to $2\sigma_2^2$ to match (9) and make (14) independently verifiable.

- **Informed LASSO threshold is unaddressed.** As the authors acknowledge (Remark 4.2), the phase transition for the informed LASSO remains open. Characterizing how high-quality and low-quality samples trade off algorithmically when the decoder knows the noise levels would complete the 2×2 table (IT/algorithmic × agnostic/informed) and substantially strengthen the paper's core contrast. This is acknowledged as future work but narrows the scope of the current contribution.

### Trivial
None beyond the equation inconsistency noted above.

---

## Nice-to-Haves

- **Numerical comparison of the relaxed vs. optimized Chernoff bound.** Even a single example with specific $\sigma_1^2, \sigma_2^2, s$ showing how much the agnostic IT sufficient condition (9) deviates from the true Chernoff-optimal bound would help readers assess whether the PoQ ≤ 2 finding is nearly tight or could be far from the truth.

- **Analysis of the reweighted estimator (Remark 3.2).** The paper proposes $\arg\min \sum_i Y_i^{-2}(Y_i - \langle x_i, \beta\rangle)^2$ as a potentially better agnostic estimator in low SNR. Even a partial sufficient condition for this variant — and comparison of its PoQ to that of estimator (8) — would either validate or challenge the PoQ ≤ 2 bound, turning "an interesting direction" into a concrete result.

- **Lower bound for at least one IT regime.** A matching (or partial) lower bound for the agnostic IT threshold in, say, the low-SNR limit would transform the PoQ ≤ 2 finding from "a property of the sufficient condition" into a genuine information-theoretic statement.

---

## Removed Points

*These points are flagged for removal — treat them with caution.*

- **Criticism that the PoQ ≤ 2 result is "fatal" or invalidates the paper** (from the harsh critic's framing as a structural flaw): Removed/demoted. The paper explicitly acknowledges the sufficient-condition limitation in Remark 3.2 and Section 5. The finding is correctly stated in the body; the concern is about abstract framing only, which is a presentational issue, not a fatal flaw.

- **Generic concern about missing related work**: Removed per hard rule (cannot verify from external sources).

- **Strength about "addressing an important problem"**: Removed as generic.

- **Strength about "first to study mixed-quality data"**: Retained only to the extent the paper itself claims it ("to the best of our knowledge, this paper is the first to…"), which is reported directly.

---

## Novel Insights

The most genuinely novel observation in this paper is the **algorithmic–informational dichotomy under data heterogeneity**: the information-theoretic threshold *does* distinguish between data qualities (the PoQ is nontrivial), but the LASSO threshold does not — it depends only on total sample size and average noise. This sharpens and extends a prior observation that the algorithmic threshold is "robust to changes in the problem setting" (Wang et al. 2010; Omidiran & Wainwright 2008; Gamarnik & Zadik 2022): not only is the LASSO threshold robust to design sparsity, it is also robust to noise heterogeneity in the agnostic setting. The Haar-measure technique for handling the non-scalar covariance in the LASSO proof is also a reusable technical contribution for future extensions to more complex noise structures.

---

## Suggestions

1. **Abstract**: Add the qualifier "under our sufficient condition" explicitly to the PoQ ≤ 2 claim in the first mention in the abstract, so readers who don't read the body are not misled about what has been proved.
2. **Equation (12)**: Correct the denominator from $2\sigma_1^4$ to $2\sigma_2^2$ and verify that equations (13)–(14) follow from the corrected expression.
3. **Tightness discussion**: Add even a brief asymptotic lower bound argument for one SNR regime to bound the looseness of the agnostic IT condition — this would substantially strengthen the paper's central claim.
4. **Reweighted estimator**: Develop Remark 3.2 slightly further by deriving the leading-order PoQ for the $Y_i^2$-reweighted estimator and comparing it to the 2 bound, even in an asymptotic regime.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to paper under review |
|---|---|---|---|
| vQIVbfTMzf.md | 3.25 | R1 (weak) | Robust estimation paper; weaker theoretical contribution, inconsistent scores |
| ZDoaLbOFaP.md | 3.00 | R1 (weak) | Covariance NN paper; different topic, much weaker theory |
| L0pMPCmEfN.md | 4.33 | R1 (mid) | Wavelet shrinkage; weak theory, borderline contribution |
| YvOq7jHT6R.md | 3.75 | R1 (mid) | Hard-thresholding paper; algorithmic focus, less rigorous theory |
| NHhjczmJjo.md | 7.00 | R1 (mid) | Transformer in-context sparse recovery; solid theory + experiments; stronger overall |
| H8OOlBjhkU.md | 5.00 | R1 (mid) | Sparse optimization with constraints; narrower contribution |
| fMTPkDEhLQ.md | 8.00 | R1 (strong) | Tight lower bounds, oracle complexity; more complete theory (tight bounds) |
| gVVoZtiQlt.md | 5.00 | R2 | Shuffled regression phase transition (message passing); similar flavor, weaker writing and less clean results |
| sIcPMMhl9W.md | 5.80 | R2 | Shuffled regression phase transition; comparable flavor, Reject; weaker results and less clear |
| wpXGPCBOTX.md | 6.75 | R2 | Sparsistency for inverse OT; Accept; similar type of contribution (new sufficient condition for sparsistency in extended setting) |
| nxnbPPVvOG.md | 5.67 | R2 | Gauss-Markov extension; Accept; similar scope, comparable completeness |
| Piod76RSrx.md | 5.50 | R2 | MI generalization bounds; different topic |
| TKRIRI9tQv.md | 5.00 | R2 | LASSO-type recovery under adversarial attacks; narrower, fewer novel insights |

**Round 1 bracket: 5–7.**

**Round 2 narrowing:** The most comparable papers are the sparsistency for inverse OT (6.75, Accept) and the shuffled regression phase transition (5.8, Reject). The paper under review is:
- **Better than** the shuffled regression paper: the LASSO result (Theorem 3) is technically cleaner, the writing is more organized, and the limitations are acknowledged more honestly.
- **Slightly below** the inverse OT sparsistency paper: that paper provides both sufficient conditions and finite-sample sparsistency, whereas this paper's agnostic IT condition lacks a matching lower bound. However, the LASSO result here is arguably a stronger and more surprising theorem than the iOT irrepresentability condition.
- **Comparable** to nxnbPPVvOG (5.67, Accept): similar scope (extending a classical result to a new setting with rigorous but incomplete analysis).

Given these comparisons, the paper sits at approximately **6.0**: above the shuffled regression reject (5.8) due to cleaner results and the strong LASSO contribution, below the iOT paper (6.75) due to the incomplete agnostic IT analysis. The work is a genuine first contribution to a well-motivated problem, with at least one very clean theorem and a novel conceptual framework, but does not fully close the information-theoretic gap that is at the heart of its main advertised claim.

**Axes evaluation:**
- *Originality*: Good — first to study the mixed-quality data setting for sparse recovery and introduce the PoQ framework.
- *Importance of research question*: Solid — heterogeneous data quality is practically relevant and understudied in this theoretical setting.
- *Claim support*: Moderate — Theorem 3 is well supported; Theorem 1's central implication (PoQ ≤ 2) lacks tightness.
- *Soundness of experiments*: N/A (pure theory paper); proofs appear sound.
- *Clarity of writing*: Good — clear structure, honest about limitations.
- *Value to community*: Good — Theorem 3 and the PoQ framework are likely to be cited and extended.

**Final score: 6.0. Borderline Accept.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>