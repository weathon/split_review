Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces "troenpy," defined as the expected value of \(- \log(1-p)\), proposed as a dual of Shannon entropy that measures certainty/commonness rather than surprisal. Using troenpy, the authors develop a supervised term weighting scheme, Positive Class Frequency (PCF), which leverages label distribution information. PCF is combined with IDF to form TF-PI weighting, and the paper also proposes Expected Class Information Bias (ECIB) features based on odds-ratios of information quantities. Experiments on 7 text classification datasets with kNN and logistic regression show that TF-PI outperforms TF-IDF (22.9% average error reduction) and the optimal-transport-based HOFTT method, with linear-time computation.

## Strengths

- **Novel information-theoretic quantity (troenpy)** — The paper formally defines Positive Information \(\text{PI}(x) = -\log(1-p(x))\) and its expectation troenpy (Eq. 2–4), establishing a quantity that is demonstrably dual to Shannon entropy (\(\text{PI}(x) = \text{NI}(\bar{x})\)). This is a genuinely new concept distinct from entropy, extropy, and other known generalizations.

- **Principled label-aware weighting that yields substantial empirical gains** — The PCF weighting (derived from troenpy of class-conditional label distributions) combined with IDF produces TF-PI, which uniformly outperforms TF-IDF across all 7 datasets in a fixed kNN (k=7) setting with an average 22.9% error reduction and up to 53.4% on R8 (Section 6, Figure 1).

- **Effective ECIB features with further improvements** — The odds-ratio-based Expected Class Information Bias features (Eq. 5–6) are shown to individually outperform binary term features on 6 of 7 datasets in logistic regression, and their combination with TF-PI yields additional error reduction (Section 6, Figure 2 description).

- **Linear-time computational complexity** — The paper explicitly notes that all proposed weightings and features are computable in a single data pass (linear complexity), in contrast to optimal-transport methods like HOFTT and Sinkhorn-based algorithms which are computationally expensive (Abstract, Section 6).

## Weaknesses

### Fatal
None.

### Major

- **Missing supervised term weighting baselines** — The paper compares TF-PI only to unsupervised TF-IDF and to HOFTT (an optimal-transport method that is not a weighting scheme). Supervised term weighting methods (e.g., TF-RF, delta-TFIDF, supervised IDF variants) are a well-established area that also uses label distribution information. The paper itself cites Delta-IDF (Section 4) as inspiration for ECIB but does not include it or any other supervised weighting as a baseline. Without these comparisons, the reader cannot determine whether the advantage of TF-PI comes from the specific troenpy formulation or simply from the use of label information, which any supervised weighting would provide. This is the most significant weakness in the empirical evaluation.

### Minor

- **No ablation isolating PCF vs. IDF contributions** — The paper combines PCF and IDF multiplicatively without showing the individual contribution of each. An ablation comparing PCF alone, IDF alone, and PCF×IDF would clarify whether the improvement comes from the label-based weighting, the IDF term, or their interaction. Similarly, the paper does not compare PCF weighting to simpler alternatives such as using class-prior ratios or class-conditional probabilities directly.

- **Missing statistical significance reporting** — For the four datasets evaluated with 50 random train/test splits, results are reported as single error numbers without confidence intervals, standard deviations, or significance tests. This makes it impossible to assess the variability or reliability of the claimed improvements.

- **No comparison of ECIB to Delta-IDF** — Since Delta-IDF is cited as direct inspiration for the ECIB features (Section 4), a natural and informative comparison would be to include Delta-IDF as a baseline in the logistic regression experiments. Without this, the added value of the troenpy-based formulation over the prior method is unclear.

- **Missing basic dataset statistics** — The paper does not report vocabulary size, average document length, class balance, or other standard dataset characteristics, making it difficult to judge the difficulty and nature of each classification task (Section 5.1).

- **Overclaim: "such label distribution information has never been made use of before"** — This statement (Section 3, final paragraph) is inaccurate; supervised term weighting methods have made use of label distribution information for decades. The paper would benefit from a more measured claim.

### Trivial

- The explanation for limited improvement on Twitter/BBCsport ("extreme polarity … less common description words") is speculative and not supported by analysis (Section 6).
- The t-SNE visualization (Figure 3) is qualitative and provides only weak supplementary evidence.

## Nice-to-Haves

- A systematic discussion positioning PCF/ECIB relative to existing supervised term weighting methods would help readers understand the contribution.
- Reporting the actual error rates (in a table) for the logistic regression experiments would be more informative than describing bar chart colors qualitatively.
- An explicit limitation section discussing when PCF may not help (e.g., with powerful classifiers like logistic regression, the gap between TF-PI and TF-IDF narrows) would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **HOFTT comparison inconsistency** (Harsh Critic #3): The critic claims the paper says "TF-PI outperforms HOFTT on all datasets but then notes that on R8 this requires additional 2B features." Reading the paper carefully (Section 6), the text says "HOFTT performs poorly compared with the TF-PI weighting on all dataset except on R8 dataset, on which it is also outperformed by TF-PI employing the additional 2B features." This is consistent — the paper accurately notes the R8 exception and honestly reports that 2B features are needed there. No inconsistency.

- **Figure 2 not provided** (Harsh Critic #3): The figure IS in the original PDF submission as an embedded image; its absence is a text-extraction artifact. The paper's qualitative description is standard practice.

- **Arbitrary definitions / lack of theoretical grounding** (Harsh Critic #2, much of it): The paper provides reasonable motivation. The duality is formalized: \(\text{PI}(x) = \text{NI}(\bar{x})\) and troenpy = \(\mathbb{E}[\text{PI}]\) vs. entropy = \(\mathbb{E}[\text{NI}]\). The weighting \(\text{PCF}_1 - \text{PCF}_*\) is naturally interpretable as the change in label-certainty when conditioning on term presence. The multiplicative combination PCF×IDF follows the same pattern as TF-IDF (combining term-level and label-level signals). These are not heuristic leaps — they are standard analogical reasoning from information theory.

- **"Why not condition on term absence?"** / **"Why not a ratio?"** — The paper explains its choice clearly. Alternative formulations are open questions, not flaws.

- **Troenpy extreme-probability behavior** — This is a niche mathematical property that is not relevant to the paper's applied contribution.

- **Smoothing not mentioned in definition** — The \(1+\) smoothing IS explicitly present in the equations (Eq. 5–6).

- **Formatting/style/copyediting nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The reviews surface a clear gap between the paper's conceptual contribution and its empirical validation. The troenpy concept is genuinely novel and the duality with entropy is clean, but the experimental design does not isolate whether the observed gains come from troenpy specifically or merely from using label information in any form. The harsh critic correctly identifies the missing supervised baselines as the central issue, while the strengths show that the core idea has promise. The paper would be substantially strengthened by a targeted experiment: compare TF-PI against at least one existing supervised weighting (e.g., delta-TFIDF or TF-RF) to demonstrate that the troenpy formulation adds value beyond the general principle of label-conditioned weighting.

## Suggestions

1. **Add at least two supervised term weighting baselines** (e.g., TF-RF, delta-TFIDF) to the kNN experiments. This is the single most important change to substantiate the claim that troenpy-based weighting offers a genuine advance.

2. **Report means and standard deviations** (or confidence intervals) for the 50-repeat experiments. Add a simple significance test (e.g., paired t-test) comparing TF-PI to each baseline.

3. **Include an ablation** comparing PCF alone, IDF alone, and PCF×IDF to show the marginal contribution of each component.

4. **Add a table of dataset statistics** (vocabulary size, document counts per class, average length) for reproducibility and context.

5. **Tone down the claim** about "never been made use of before" to something like "not commonly used in standard TF-IDF-style weighting."

## Score and Decision

The paper introduces a genuinely new information-theoretic quantity (troenpy) with a clean duality to entropy, and the proposed TF-PI weighting shows consistent improvement over TF-IDF and a modern optimal-transport method on multiple datasets. However, the lack of comparison to any existing supervised term weighting baseline is a significant gap — without it, the evaluation cannot distinguish between an advance attributable to troenpy specifically and one attributable simply to using label information. The paper's central empirical claim is therefore incompletely supported. This is addressable in revision but is too large a gap for the current version.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>