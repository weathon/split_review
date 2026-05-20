Now I have all the information I need to produce the consolidated review.

## Summary

The paper proposes Precision Reject Curves (PRC) and Recall Reject Curves (RRC) as alternatives to standard Accuracy Reject Curves (ARC) for evaluating reject options in classification, motivated by the fact that accuracy is misleading on imbalanced data. The PRC and RRC are formally defined as straightforward extensions of the ARC formulation. The paper demonstrates these curves on synthetic Gaussian data, two benchmark datasets (Tecator, Haberman), and a real medical dataset (Adrenal) using three prototype-based classifiers (RSLVQ, GMLVQ, LGMLVQ) with two certainty measures.

## Strengths

- **Well-motivated gap in prior work**: The paper correctly identifies that accuracy-reject curves are standard but can be misleading for imbalanced data, and formally defines precision- and recall-reject curves to fill this gap (Section 1, lines 28–30; Section 5, lines 167–169). The motivation is clear and the problem is genuinely important for safety-critical applications.

- **Clear, usable formal definitions**: PRC and RRC are defined with precise mathematical equations (Eq. 3 and 4, lines 174–181) that directly extend the ARC formulation. These definitions are immediately usable by practitioners without requiring additional implementation guidance.

- **Demonstration on real medical data**: The Adrenal dataset (lines 202–205) grounds the contribution in a concrete high-stakes application where correct evaluation of reject options genuinely matters for clinical decision-making.

## Weaknesses

### Fatal
None.

### Major

1. **Positive class is never specified for any experiment.** Precision and recall are class-dependent metrics — their values depend critically on which class is treated as "positive." The paper reports precision/recall results for Tecator (36%/64%), Haberman (26.5%/73.5%), and Adrenal (68.4%/30.6%) but never states which class is positive for any of them. Without this information, the reader cannot interpret the reported precision and recall values, and the entire experimental section is unverifiable. This is a basic reporting requirement.

2. **No quantitative results reported anywhere.** All experimental findings are described in purely qualitative language: "performance decreases," "PRCs and RRCs perform differently," "accuracy overestimates the performance," "precision is in the same range as accuracy." No tables of numbers, no area-under-curve values, no effect sizes, no standard deviations from the 10-fold repeated CV (which is mentioned but never summarized quantitatively). The paper's central claim — that PRC/RRC provide "more accurate insights" — cannot be assessed without quantitative evidence.

3. **No controlled demonstration that ARC leads to a wrong conclusion.** The paper's core assertion is that ARCs are "unsuitable" and "misleading" for imbalanced data. The experiments only show that PRC/RRC produce different values from ARC — which is mathematically guaranteed for any metric other than accuracy. The paper never provides a concrete scenario (e.g., two classifiers with similar ARCs but different PRCs/RRCs, or a threshold selection task where ARC suggests good performance but PRC/RRC reveal problems on the minority class) that demonstrates ARC leading to a genuinely wrong decision that PRC/RRC corrects.

### Minor

1. **Gaussian data experiment does not test the imbalanced-data motivation.** The synthetic Gaussian data is balanced (line 193: "equally distributed over classes"), serving only as a validation that PRC/RRC can match a Bayesian baseline. The paper's main motivation is imbalanced data, but this experiment tests a different regime.

2. **No explicit comparison to existing alternatives.** The paper cites Pillai (2011) on F1-reject curves (line 170) and Hanczar (2019) on alternative evaluation methods (line 42), and argues that F1-curves would not add insight beyond PRC/RRC because precision and recall develop similarly (line 239). However, an explicit experimental comparison with F1-reject curves or the receiver-operator approach of Hanczar (2019) would substantially strengthen the case that the proposed method offers new value.

3. **Claims are somewhat overstated relative to the evidence.** The conclusion states that "the ARC may be misleading, while PRC and RRC provide meaningful comparisons" (line 254). With only qualitative evidence and no controlled demonstration of ARC leading to an incorrect conclusion, this claim outpaces what the experiments establish.

### Trivial
None.

## Nice-to-Haves

- A controlled synthetic experiment with imbalanced data where two classifiers have similar ARCs but different PRCs/RRCs, directly illustrating the claimed advantage.
- Reporting area under each reject curve (or key precision/recall/accuracy values at standardized rejection rates) with standard deviations.
- A concrete use case on the Adrenal data: "If we require at least 90% recall on the minority class, what rejection rate does each model achieve according to RRC vs. ARC?"

## Removed Points

- **"Section 3 (Prototype-based classification) is overly long"** — Pure presentation/style preference; not a substantive weakness.
- **"Figures are not provided in the text"** — Parser artifact; the original submission contains figures.
- **Complaints about missing appendix content** — Parser strips appendices; they exist in the original submission.
- **Generic formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The harsh critic's observation that no experiment demonstrates ARC leading to a wrong conclusion which PRC/RRC corrects is the most penetrating insight. While the paper treats "accuracy overestimates performance" (different numeric values) as equivalent to "ARC is misleading," these are not the same claim. A practitioner might reasonably counter that accuracy, precision, and recall measure different things, so of course they differ — the contribution requires showing that this difference matters for a concrete decision (e.g., threshold selection, model comparison). The missing positive-class specification compounds this: even the qualitative descriptions cannot be properly interpreted.

## Suggestions

1. **Specify the positive class** for every dataset in the experiments, and justify the choice (typically the minority class of interest, e.g., malignant tumours for Adrenal, non-survival for Haberman).
2. **Add a controlled synthetic experiment** with imbalanced 2D data, comparing two classifiers with similar ARCs but different PRCs/RRCs to concretely demonstrate the claimed advantage.
3. **Report quantitative results**: at minimum, tabulate precision, recall, and accuracy at key rejection rates (0%, 20%, 40%) with standard deviations from the repeated CV.
4. **Tone down the central claim** to match the evidence: "PRC and RRC provide complementary information to ARC" rather than "ARC is unsuitable/misleading."
5. **Include explicit comparison** to the F1-reject curve (Pillai 2011) as a baseline.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| 2LhCPowI6i (Self-Supervised Pseudodata Filtering) | 2.33 | Weaker than the current paper — its core method has more fundamental issues. The current paper has a sounder idea. |
| yiQCeXdPvs (DIRECT Active Learning) | 3.75 | Similar tier — both papers have reasonable ideas undermined by insufficient/incomplete experimental validation. Current paper is slightly cleaner conceptually. |
| 0kvrymILfy (Selective Recalibration) | 5.25 | Stronger — has quantitative results and theoretical analysis. Current paper lags well behind in experimental rigor. |
| S1IbZssS5a (Label Noise for Imbalanced) | 5.50 | Stronger — extensive experiments across many datasets. Current paper's experimental breadth and rigor are substantially weaker. |
| HvkXPQhQvv (SSME) | 6.00 | Much stronger — thorough experiments across multiple domains with quantitative evidence. Current paper is far from this bar. |
| 6vtGG0WMne (Regulating Imbalanced Models) | 4.50 | Stronger — has quantitative experimental results and comparison to baselines. Current paper lacks these. |

The paper's idea is sensible and the definitions are clear, but the experimental validation is fundamentally insufficient: no quantitative results, no specification of which class is positive for precision/recall, and no controlled demonstration that the proposed curves actually provide new insight beyond what ARC already offers. Compared to calibration anchors in the 4–6 range, this paper's evidence base is markedly weaker. The contribution is intuitive but remains unsubstantiated.

**MY FINAL SCORE: 3.5**

**MY FINAL DECISION: Reject**