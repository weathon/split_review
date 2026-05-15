Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes "troenpy" (the expectation of −log(1−p(x)), i.e., the self-information of the complement event) as a conceptual dual of Shannon entropy that measures certainty/commonness rather than uncertainty/surpriseness. It uses troenpy to derive a class-sensitive term weighting scheme called Positive Class Frequency (PCF), combines it with IDF to form TF-PI, and further introduces Expected Class Information Bias (ECIB) features based on information-theoretic odds ratios. Experiments on seven text classification datasets show that TF-PI consistently reduces kNN classification error by an average of 22.9% over TF-IDF, and that adding ECIB and binary term features further improves logistic regression.

## Strengths

- **Consistent and substantial empirical improvement over TF-IDF.** Across all seven datasets, TF-PI uniformly outperforms TF-IDF in the kNN setting, with an average 22.9% error reduction and a maximum of 53.4% on R8 (Figure 1, Section 6). The improvement is also uniform when switching from kNN to logistic regression. This is the paper's strongest empirical evidence.

- **Computationally efficient.** The proposed weighting and features require only a single linear-time pass over the data, in contrast to optimal-transportation methods (HOFTT, WFR) that incur higher computational costs (Section 6, Word Moving Distance Methods). This practical advantage is clearly stated.

- **Novel ECIB features provide additional gains.** Adding the Expected Class Information Bias features (information-theoretic odds ratios using both entropy and troenpy) and binary term features yields further error reduction beyond TF-PI alone in a logistic regression setting (Figure 2, Section 6). The features are conceptually clean and computationally cheap.

- **Evaluation across diverse datasets with two classifiers.** The paper uses seven standard benchmarks of varying sizes and domains, and evaluates with both kNN and logistic regression, providing reasonable breadth.

## Weaknesses

### Fatal
None. The core empirical finding (TF-PI beats TF-IDF consistently) is supported by the experimental data.

### Major

- **Missing ablation: the claimed advantage of troenpy over entropy is not tested.** The PCF weighting uses troenpy, but the paper never compares PCF against an analogous entropy-based weighting (NCF) on the same class-label distributions. The paper merely states that "entropy based NCF is not suitable for weighting" and defers justification to a separate publication (line 89: *"We will illustrate and explain this phenomenon elsewhere"*). Without this ablation, the reader cannot determine whether the improvement comes from troenpy specifically or from incorporating class-label distribution information in any form. This weakens the paper's central attribution claim.

- **Limited baselines for a supervised term weighting paper.** The only comparisons are TF-IDF (an unsupervised baseline) and HOFTT (an optimal-transport method). Many well-established supervised term weighting schemes exist — chi-square weighting, information gain weighting, Delta-IDF, and odds-ratio weighting among others — that also incorporate class labels. Without comparisons to these, the claim that troenpy-based weighting is superior to alternative class-sensitive methods is unsupported. The paper's reference to Delta-IDF as inspiration (Section 4) makes its absence as a baseline particularly noticeable.

- **No measures of statistical significance or variance.** All results are reported as point estimates (error rates) without standard deviations, confidence intervals, or statistical tests across the 50 random splits. Given that some improvements are modest (e.g., Twitter, BBCsports), the reader cannot assess whether these differences are reliable.

### Minor

- **Theoretical framing of troenpy as a "novel" or "dual" quantity is oversold.** The paper defines PI(x) = −log(1−p(x)) and notes that PI(x) = NI(not x). Troenpy is therefore the expected self-information of the complement event — a simple transformation of the same probabilities, not a fundamentally new information measure with its own coding theorem or operational interpretation. While this does not invalidate the practical weighting scheme, it means the paper's theoretical contribution is modest. The paper would benefit from toning down the language about "complementing classical Shannon information theory."

- **ECIB feature motivation and analysis is thin.** The paper states that ECIB features are "inspired by Delta-IDF" but provides no intuition for why the troenpy-based version (PCF-CIB) should differ meaningfully from the entropy-based version (NCF-CIB), nor any analysis of when one is preferable. The formulas involve nested logs with many terms (C_i, n, n_w, n_{iw}) whose combined effect on classification is opaque.

- **WFR results excluded without full details.** The paper mentions that WFR results are "comparable" but excludes them because of "version mismatch" and "slightly different sampling procedure" (Section 6). This is transparent but incomplete; providing the specific discrepancies would help the reader assess whether the comparison is fair.

### Trivial
None.

## Nice-to-Haves

- Comparison with entropy-based PCF (NCF) on the same datasets to isolate the troenpy effect.
- Inclusion of at least one additional supervised baseline (e.g., Delta-IDF, chi-square weighting) for the kNN setting.
- Error bars or standard deviations on the reported error rates.
- A concrete example or small case study showing troenpy weighting qualitatively different from entropy weighting on real terms.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Denominator in ECIB formula can become zero or negative (Harsh Critic, Sec-by-Sec).** The critic claims 1+C_i−n_{iw} could be ≤ 0 if n_{iw} > C_i+1. This is factually wrong: n_{iw} is the count of class-i documents containing word w, and C_i is the total count of class-i documents, so n_{iw} ≤ C_i by definition, and 1+C_i−n_{iw} ≥ 1 > 0. The second denominator 1+n−C_i−n_w+n_{iw} is similarly always positive. **Removed: factually incorrect.**

- **Criticism about missing Legendre transform, variational principle, dual optimization (Harsh Critic, Issue 1).** The paper uses "dual" in the conceptual sense of "opposite measure" (entropy measures surpriseness, troenpy measures commonness), not in the formal optimization-theoretic sense. Demanding variational principles or Legendre transforms for a practical weighting paper is beyond scope. **Removed: scope creep / not standard for this type of paper.**

- **Criticism about HOFTT being "not contemporary" (2019).** Four years is a reasonable timeframe for a paper published after 2023. **Removed: not substantive.**

- **Request for theoretical properties of troenpy (bounds, convexity, connection to Rényi entropies).** The paper's primary contribution is an empirical weighting scheme, not a new information theory textbook. **Removed: scope creep / nice-to-have, not a weakness.**

- **Various formatting/style nitpicks and "typos" (from parser artifacts).** **Removed per hard rule: parser artifacts.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself misses; the key concern (troenpy vs. entropy ablation) is already implicitly recognized by the paper's deferral of the entropy-based justification to future work.

## Suggestions

1. **Perform the critical ablation:** Replace troenpy with entropy in the PCF definition and compare the resulting weighting under identical conditions. If entropy-based weighting performs comparably, the paper's novelty rests on the ECIB features and the overall class-sensitive weighting framework, not on troenpy.
2. **Add at least two supervised baselines** (e.g., Delta-IDF, information gain weighting) to contextualize the reported improvements.
3. **Report standard deviations or confidence intervals** for all error rates across the 50 random splits, and use a paired test to validate "significant error reduction" claims.
4. **Tone down the theoretical claims** about "complementing Shannon information theory" and instead focus the contribution on the practical weighting scheme.
5. **Clarify the WFR exclusion** by listing which datasets had version mismatches and what the sampling differences were.

## Score and Decision

The paper provides a practically effective class-sensitive term weighting scheme with strong and consistent empirical results across seven datasets. Its main weaknesses are the missing ablation (troenpy vs. entropy), limited baselines, and no error bars — all addressable in a revision. The theoretical framing is oversold but does not undermine the empirical contribution. I assign a borderline score reflecting that the paper needs substantive additional experiments to fully support its claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>