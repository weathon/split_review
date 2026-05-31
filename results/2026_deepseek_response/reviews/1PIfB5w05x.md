Now I have all the evidence I need. Let me write the final review.

## Summary
The paper studies sparse recovery when observations come from two sources with different noise levels (high-quality/low-variance, low-quality/high-variance). It provides sufficient conditions for information-theoretic recovery in agnostic and informed settings, introduces a "Price of Quality" quantifying how many low-quality samples replace one high-quality sample under these sufficient conditions, and extends the LASSO phase transition to the heterogeneous-noise agnostic setting, showing the threshold depends only on total sample size and average noise.

## Strengths
1. **First sufficient conditions for sparse recovery under heterogeneous noise (Theorems 1 and 2).** The paper provides explicit sample-size conditions of the form \(\alpha_1 n_1 + \alpha_2 n_2 > n^*\) and defines the Price of Quality \(\gamma\). The comparison between agnostic (\(\gamma \le 2\)) and informed (\(\gamma\) can diverge) settings yields genuine insight.

2. **Clean extension of the LASSO phase transition to heterogeneous noise (Theorem 3).** The proof shows that the signed-support recovery threshold for the LASSO is \(n_{\text{ALG}} = 2s\log(p-s)+s+1\) — identical to the homogeneous-noise case — with noise entering only through the average level \(\sigma^2_{\text{avg}}\). The proof overcomes the breakdown of Wishart structure via QR decomposition and Haar measure arguments, a nontrivial adaptation of Wainwright (2009).

3. **Proposition 4.1 closes the loop on noise scaling.** It provides the necessary and sufficient condition \(\sigma^2_{\text{avg}} = o\bigl(n/((1+s/\rho^2)\log(p-s))\bigr)\) for the LASSO result to hold, and constructs an explicit valid \(\lambda_p\).

4. **Well-motivated practical distinction.** The agnostic vs. informed decoder framing is grounded in concrete applications (web-scale text corpora vs. multi-site clinical trials), making the theoretical differences practically meaningful.

5. **Generalization to arbitrary noise structures.** Remark 3.4 extends the sufficient conditions beyond the two-source model to any invertible \(\Sigma\), showing the core ideas are not restricted to the high/low-quality dichotomy.

## Weaknesses

### Fatal
None.

### Major
1. **Typo in equation (12): the denominator should be \(\sigma_2^2\) not \(\sigma_1^4\).** The Price of Quality for the agnostic setting is derived from the sufficient condition (9), where the coefficient for \(n_1\) is \(\log(1 + \delta(2\sigma_2^2 - \sigma_1^2)s/(2\sigma_2^2))\). However, equation (12) writes the numerator argument as \(\delta(2\sigma_2^2 - \sigma_1^2)s/(2\sigma_1^4)\). The asymptotic analyses (13)–(14) implicitly use the correct form (with \(\sigma_2^2\)), not the one printed in (12). For instance, in the low-SNR₂ regime, (14) reports \(\gamma \simeq 2 - \sigma_1^2/\sigma_2^2\), which is consistent with the correct \(\gamma\) from (9) but not with the printed (12) (which would yield \(\gamma \simeq (2\sigma_2^2 - \sigma_1^2)\sigma_2^2/\sigma_1^4\)). This is a genuine typo that must be corrected.

### Minor
1. **The Price of Quality is a property of the sufficient condition, not necessarily of the problem.** The paper acknowledges this in Remark 3.2 but the repeated conclusion "one high-quality sample is never worth more than two low-quality samples" is stated without always reminding readers that this is only proven for the particular relaxed Chernoff bound of the specific estimator (8). The actual information-theoretic Price of Quality could be larger. The distinction is clear enough for an expert reader but could mislead a broader audience.

2. **The role of \(\delta\) (fraction of support errors) is not discussed.** The sufficient conditions (9) and (16) involve a free parameter \(\delta \in (0,1)\). As \(\delta \to 0\) the LHS goes to 0, making recovery impossible. The paper does not discuss how \(\delta\) should be chosen, whether it can be taken arbitrarily small while maintaining the condition, or what the implications are for exact (rather than approximate) support recovery. In contrast, the homogeneous-noise information-theoretic results (Reeves et al., 2019) give thresholds for exact recovery.

3. **The necessity condition (26) requires \((n_1\sigma_1^2 + n_2\sigma_2^2)/(\lambda_p^2 n^2)\) to have a limit.** This excludes some parameter sequences (e.g., where the ratio oscillates). The paper does not comment on whether this is a genuine restriction or a technical artifact.

4. **Theorem 3 requires \(n_1, n_2 = \omega(s)\).** The homogeneous case only requires \(n > s\) in some formulations. The paper does not discuss whether this stronger assumption is necessary or an artifact of the proof technique.

5. **No experimental validation.** Simulations validating the predicted Price of Quality behavior or showing the LASSO phase transition for heterogeneous noise would strengthen the paper. For a purely theoretical paper this is not fatal, but the absence is noticeable given that the information-theoretic results are only sufficient conditions whose tightness is unknown.

### Trivial
None.

## Nice-to-Haves
- An information-theoretic lower bound for the heterogeneous setting (even for a special case like \(\sigma_2 \to \infty\)) would anchor the sufficient conditions.
- A partial analysis of the LASSO in the informed setting (even an upper bound).
- A brief discussion comparing estimator (8) to other agnostic approaches (e.g., reweighting by observed labels as mentioned in Remark 3.2).

## Removed Points
- **"The proof sketches are too brief"** — Papers routinely defer proof details to appendices; this is standard practice.
- **"Missing related works on heteroscedastic regression"** — The paper already cites Buja et al. (2019) and discusses relevant literature.
- **"Equation (9)/(12) inconsistency is fatal"** — It is a typo, not an error that invalidates the paper; the asymptotic analyses, which are the substantive contribution, use the correct form.
- **Harsh critic's speculation that "the bound 'one high-quality sample is never worth more than two low-quality samples' is taken as fundamental"** — The paper repeatedly qualifies this as applying to the sufficient condition, not as a fundamental limitation (see Remark 3.2, Section 5).
- **Generic Strength Finder strengths** (e.g., "the problem is important") that do not cite specific technical content.
- **"Section-by-section notes"** about clarity — these are subjective observations without concrete actionable content.

## Novel Insights
The most striking observation that emerges from this review is the asymmetry between the information-theoretic and algorithmic thresholds with respect to data heterogeneity: the paper shows that under the LASSO, high- and low-quality samples contribute equally to the sample-size requirement (only average noise matters), whereas the information-theoretic sufficient conditions exhibit a "Price of Quality" bounded by 2 in the agnostic case. This suggests that the algorithmic (computational) threshold is more robust to heterogeneity than the information-theoretic threshold, echoing a pattern observed in other sparse recovery settings (sparse vs. dense designs). The informed setting results showing that \(\gamma\) can diverge further highlight that knowing per-sample noise variance can yield arbitrarily large gains at the information-theoretic level, but no analogous result exists yet for algorithmic recovery since the informed LASSO is not analyzed.

## Suggestions
1. **Fix the typo** in equation (12): replace \(\sigma_1^4\) with \(\sigma_2^2\) in the denominator.
2. **Add a brief discussion of \(\delta\)** — explain its role, whether it can be taken as a constant (e.g., \(\delta = 1/2\)), and how the results would change for \(\delta \to 0\) (exact recovery).
3. **Add a small simulation** (even in the appendix or a comments section) showing that the LASSO phase transition indeed depends only on \(n\) and \(\sigma^2_{\text{avg}}\) under heterogeneous noise, and ideally that the Price of Quality bound from the sufficient condition is not absurdly loose.
4. **Comment on the \(n_1,n_2 = \omega(s)\) assumption** in Theorem 3 — is this necessary or an artifact?
5. **Clarify the limit requirement** in condition (26) — is the limit assumption needed or can it be relaxed to \(\liminf\) / \(\limsup\)?

## Score and Decision

### Round 1 — Bracketing
The paper was compared against anchors in three bands:
- **Weak band (score < 3.5):** Papers at ~2.33–3.00 — these papers had severe flaws (incoherent claims, non-rigorous methods). Our paper is clearly stronger. Not in this band.
- **Middle band (3.5–7.5):** Shuffled Regression (5.00, 5.80), Flat Minima (5.67), Learn-to-Optimize Transformers (7.00), Multi-Index Models (6.00), Phase Transitions TMS (5.50). Our paper is competitive with these.
- **Strong band (>7.5):** Papers at 8.00 uniformly — exceptional theoretical contributions with complete execution. Our paper has more limitations (sufficient conditions only, typo, no experiments). Not in this band.

**Bracket: 5.0–7.0**

### Round 2 — Narrowing
Compared to specific anchors within the bracket:
- **Shuffled Regression (5.00, 5.80):** That paper's analysis is heuristic/physics-style; ours is fully rigorous. Our paper is stronger.
- **Flat Minima (5.67, Accept):** Comparable theoretical depth; ours has a broader scope (two related problems, two settings) but lacks experiments theirs had. Slightly stronger.
- **Phase Transitions TMS (5.50, Reject):** Limited to a toy model; our paper addresses a more general and well-motivated problem. Stronger.
- **Learn-to-Optimize Transformers (7.00, Accept):** Rigorous theory + experiments + practical relevance. Our paper lacks experiments and has the typo issue. Weaker.

### Final Score
Positioned relative to the round-2 anchors: our paper is clearly stronger than the Shuffled Regression (5.00/5.80) and Phase Transitions TMS (5.50) papers, comparable to or slightly stronger than Flat Minima (5.67), but weaker than the strong 7.00 anchor (which had experiments and no typos). The LASSO contribution is solid and well-executed; the information-theoretic contribution is honest about its limitations but has a clear typo. Overall, I place the paper at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>