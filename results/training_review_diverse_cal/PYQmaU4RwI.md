Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes *troenpy*, defined as \(-\sum p(x)\log(1-p(x))\), as a "dual" of Shannon entropy that measures certainty/commonness rather than surprise/uncertainty. It then derives a Positive Class Frequency (PCF) weighting scheme for supervised document classification and additional Expected Class Information Bias (ECIB) features. The key empirical claim is that the TF-PI weighting (PCF×IDF) outperforms both TF-IDF and an optimal-transport-based method (HOFTT) across seven benchmark datasets in kNN classification, with an average 22.9% error reduction claimed.

## Strengths

1. **Novel information-theoretic quantity with practical potential**: The paper defines troenpy as the expectation of \(-\log(1-p(x))\), a conceptually interesting complement to Shannon entropy. The observation that PI\((x) = \text{NI}(\bar{x})\) is correctly noted, and the intuition of measuring "commonness" versus "surprise" is clear.

2. **Consistent empirical improvement over TF-IDF across seven datasets**: In the kNN setting, the TF-PI weighting shows visibly lower error rates than TF-IDF on all seven datasets (Figure 1). The reported 22.9% average error reduction, with 53.4% on R8, suggests the PCF weighting captures useful label-distribution information that TF-IDF ignores.

3. **ECIB and BTF features provide additional gains in logistic regression**: The logistic regression experiments (Figure 2) show that adding the ECIB or BTF features, individually or jointly, further reduces error rates on most datasets. This demonstrates that the proposed odds-ratio-style features have practical value beyond the weighting scheme itself.

4. **Linear computational complexity**: The paper correctly notes that PCF, ECIB, and BTF can all be computed in a single pass over the data with linear time complexity, contrasting favorably with the expensive Sinkhorn iterations required by optimal-transport-based methods like HOFTT.

## Weaknesses

### Major

1. **Troenpy is undefined for deterministic distributions (structural mathematical flaw)**: Troenpy is defined as \(-\sum p(x)\log(1-p(x))\). For any outcome with \(p=1\), the term becomes \(-1\cdot\log(0)=\infty\). In the document classification setting, if a term appears only in documents of a single class, the conditional label distribution given term presence is deterministic, making \(\text{PCF}_1 = \infty\). The weighting scheme \(\text{PCF}_1 - \text{PCF}_*\) then inherits this infinity. The paper explicitly adds "+1" smoothing to IDF for the analogous \(d=0\) case (Section 3.1), but provides no smoothing whatsoever for PCF/troenpy. This is not a pathological edge case — in real text data, many class-specific terms have all their occurrences in a single class. The problem is structural in the definition, not an implementation detail. The paper neither acknowledges nor addresses this, and it is unclear how the reported results were obtained without numerical instability.

2. **No numerical results tables — empirical claims are unverifiable from figures alone**: The paper reports all experimental results exclusively as bar charts (Figures 1 and 2). No numerical error rates, standard deviations, or confidence intervals are provided anywhere in the text or figures. For the four datasets where 50 random train-test splits are used, no measure of variability is given. The claimed "22.9% average error reduction" and individual dataset improvements cannot be independently verified, compared across conditions, or assessed for statistical significance. This is a critical omission for a paper whose central argument is empirical.

3. **Limited baseline comparisons insufficient to support broad superiority claims**: The paper's main comparison is against TF-IDF, a half-century-old unsupervised weighting scheme. Only one modern baseline (HOFTT) is included, and the paper acknowledges that a more recent method (WFR) is comparable to the proposed approach. No comparisons are made against other label-aware weighting methods such as delta-TFIDF, information-gain-based term weighting, chi-square weighting, or odds-ratio weighting — despite the paper's own ECIB features being odds-ratio-based. Without these comparisons, it is unclear whether the improvement over TF-IDF is specific to the PCF formulation or is simply the benefit of incorporating label information, which many existing methods also do.

### Minor

1. **The "dual" framing lacks theoretical substance**: The paper motivates troenpy as a "natural dual" of entropy purely by analogy (replacing \(-\log p\) with \(-\log(1-p)\)). No information-theoretic properties of this duality are established — no discussion of convexity, additivity, chain rules, or how troenpy relates to existing information measures like KL divergence or mutual information. The practical weighting scheme may be valuable, but the theoretical framing as a "dual of Shannon information" is overstated relative to what is actually shown.

2. **NCF defined but dismissed without evidence**: Negative Class Frequency (entropy-based) is formally defined in Section 3.2 but immediately dismissed as "not suitable" with a reference to future work. No empirical evidence is provided showing why the entropy-based version fails. This leaves an incomplete picture.

3. **The WFR admission undercuts the claimed superiority over OT methods**: The paper states that TF-PI outperforms HOFTT, but immediately notes that a more recent method (WFR) is "comparable" and that results were not included due to "version mismatch" and "different sampling procedures." Without direct comparison to WFR under identical conditions, the claim of superiority over optimal-transport-based methods remains unsubstantiated for the strongest competitor.

### Trivial

1. The speculative explanation for the BBC error increase ("very small test sample size") in Section 6 is offered without any quantitative support.
2. The fixed K=7 in kNN is used without any sensitivity analysis or justification that this setting is fair across all weighting schemes.

## Nice-to-Haves

- An ablation study comparing PCF alone, IDF alone, and PCF×IDF to isolate each component's contribution.
- Sensitivity analysis for the fixed K=7 in kNN.
- Computational complexity comparison (wall-clock time) between the proposed methods and baselines.
- A discussion of how the infinite-troenpy issue could be resolved (e.g., Laplace smoothing before computing troenpy, or using \(\log(1-p+\epsilon)\)).

## Removed Points

These points were flagged by reviewers but do not survive cross-verification against the paper:

1. **"'Negative Information' and 'Positive Information' are non-standard and confusing"** — The paper explicitly states it uses these names "for showing the duality nature later" (line 28). This is a deliberate authorial choice, not an error. It is standard practice in papers to introduce new terminology for new concepts. Removing as factually inaccurate criticism of a deliberate choice.

2. **"ECIB features definition not clearly justified"** — The paper provides a complete derivation of both CIB-NCF and CIB-PCF starting from delta-IDF (Section 4.1, including the full equations 4-5). While the justification could be expanded, it is not absent or confusing. Downgrading from the reviewer's framing.

## Novel Insights

None beyond the paper's own contributions.

## Evaluation

**Originality**: The concept of troenpy as \(-\sum p\log(1-p)\) is genuinely new to the best of my knowledge. However, the paper does not establish any nontrivial theoretical properties of this quantity — it remains a heuristic functional form rather than a well-characterized information measure.

**Importance of research question**: Effective term weighting for supervised text classification is a practically important problem. The paper addresses a real need.

**Claims support**: The central claim — that TF-PI outperforms TF-IDF — is directionally supported by the figures, but the lack of numerical results makes rigorous verification impossible. The mathematical flaw (infinite values for deterministic distributions) casts doubt on the definition's soundness. Claims of superiority over optimal-transport methods are weakened by the admission that WFR is comparable.

**Soundness of experiments**: The experimental setup is reasonable (seven datasets, kNN and logistic regression), but the absence of numerical tables, error bars, and standard deviations means the experiments cannot be properly assessed. The baseline selection is too narrow to support the paper's broader claims.

**Clarity of writing**: The paper is generally well-structured and the intuition is communicated clearly. Notation is consistent within the paper.

**Value to community**: If the mathematical flaw is resolved and rigorous numerical results are provided, the PCF weighting scheme and ECIB features could be of practical value. In its current form, the contribution is not reliably usable.

## Score and Decision

The paper presents a genuinely novel idea with clear practical potential. However, two issues prevent acceptance in the current form: (1) a structural mathematical flaw — troenpy is undefined for deterministic distributions, which are common in the intended application — with no smoothing mechanism provided, unlike the explicit "+1" smoothing in the paper's own IDF formulation; and (2) the complete absence of numerical results, making the paper's central empirical claims unverifiable. These are fundamental weaknesses for a paper whose contribution is both theoretical and empirical. The remaining issues (limited baselines, thin theoretical justification) are less severe but also need attention.

The core ideas show promise, and the paper could become a solid contribution after substantial revision addressing the mathematical definition and providing full numerical results with proper baselines. In its present form, however, it does not meet the bar for publication.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>