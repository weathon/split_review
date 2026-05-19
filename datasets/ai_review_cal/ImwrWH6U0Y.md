- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper presents the first comprehensive empirical study of how curriculum learning (CL) affects privacy risks through membership inference attacks (MIA) and attribute inference attacks (AIA). It evaluates four CL methods (bootstrapping, transfer learning, baseline curriculum, anti-curriculum) across 9 datasets and 3 architectures, finding that CL makes models slightly more vulnerable to MIA — but with a *disparate* and substantially larger impact on difficult samples. The paper also proposes a new difficulty-calibrated MIA (Diff-Cali) that achieves better TPR at low FPR, and evaluates four defenses under CL. The core contributions are the isolation of data ordering vs. repetition effects on privacy, the documentation of disparate vulnerability by difficulty level, and the mechanistic explanation via memorization analysis.

---

## Strengths

- **Isolates the effects of data ordering vs. data repetition on privacy**: By comparing bootstrapping, anti-curriculum, and baseline curriculum, the paper separates the contribution of meaningful ordering from fixed repetition. Finding 2 (Section 5.1) explicitly states that "data ordering plays a bigger role," supported by consistent accuracy gaps across Tables 1–2 and Figure 2. Prior privacy work did not decompose these factors.

- **Provides a principled memorization explanation using KNN-Shapley**: Section 5.2 uses the formal memorization definition (Equation 3) and KNN-Shapley (Figures 5–7) to show that CL forces stronger memorization of difficult samples, making them more vulnerable. This goes beyond merely reporting attack accuracy and ties the finding to a theoretically grounded metric.

- **Proposes Diff-Cali attack that improves TPR at low FPR**: The difficulty-calibrated MIA achieves meaningfully higher true-positive rates at false-positive rates below \(10^{-4}\) compared to standard NN-based attacks (Figure 8, Table 4). This addresses a regime emphasized by Carlini et al. (2021) as critical for practical threat assessment.

- **Comprehensive evaluation across multiple dimensions**: The study covers 9 datasets (image and tabular), 4 CL methods, 3 model architectures, 6 attack variants, and 4 defenses. The 5-repeat experimental protocol with reported standard deviations provides confidence that core findings (e.g., disparate impact on difficult samples) are not artifacts of a single setup.

---

## Weaknesses

### Fatal

None. The paper's core contributions (documenting CL's disparate privacy impact on difficult samples, isolating ordering vs. repetition effects, providing a memorization-based explanation) are supported by evidence across multiple datasets and architectures. No weakness verifiable from the paper invalidates these central claims.

### Major

- **The DPSGD defense evaluation uses an unrealistic privacy regime that limits its informativeness**: DPSGD is evaluated with \(\varepsilon = 124{,}496\) and a batch size that preserves comparability with other training settings. This configuration provides essentially no meaningful privacy guarantee (\(\varepsilon\) this large is indistinguishable from no DP) and destroys target model accuracy (to ~16–17% on CIFAR100). The paper acknowledges the large \(\varepsilon\) and mentions that tuning could improve the tradeoff (line 579), but the conclusion "None of the studied defenses can significantly drop the MIA accuracy while maintaining the target model accuracy" is misleading when applied to DPSGD — the DPSGD configuration tested was not one that any practitioner would deploy. The defense evaluation's core value is in the comparison of Memguard, MixupMMD, and Advreg under CL, and the interesting finding that DPSGD reverses CL's disparate impact (Figure 9, lines 634–636). However, the DPSGD accuracy/utility numbers as reported do not inform the practical privacy-utility frontier. The authors should either redo the DPSGD evaluation with tuning that achieves a realistically meaningful \(\varepsilon\) (e.g., < 10), or explicitly reframe the DPSGD section to focus solely on the reversal of disparate impact rather than claiming it fails to maintain accuracy.

### Minor

- **No formal statistical significance tests for key comparisons**: The paper claims "statistical significance" (line 201) based solely on small standard deviations. While the reported standard deviations (typically < 0.01) strongly suggest the differences are real, a proper test (e.g., paired t-test or bootstrap confidence intervals) would strengthen the claims, particularly for the small overall MIA accuracy increases (0.01%–2.46%) where formal significance testing would clarify which differences are reliable.

- **AIA evaluation is limited in scope and signal**: Only 3 datasets are used for AIA, and the attack accuracy for Place100/60 (0.107 and 0.173) is barely above random chance, making it difficult to draw strong conclusions about CL's impact on AIA vulnerability. The paper briefly discusses this (line 566) but should report baseline accuracy (e.g., majority-class prediction) and discuss whether ceiling/floor effects limit the analysis.

- **Lack of comparison with LiRA**: The paper acknowledges this limitation (line 648) and explains the dataset splitting constraint, which is reasonable. But since LiRA is a current SOTA MIA, the paper would be stronger with at least a small-scale comparison or a more detailed justification of why the key conclusions would hold regardless.

- **Small overall MIA accuracy increases de-emphasized relative to disparate impact finding**: The paper's framing still leads with "CL makes models more vulnerable to MIA" in the abstract and conclusion, but the absolute increases (0.01%–2.46%) are small. The disparate impact finding (up to 4.23% gap) is both larger and more novel. The paper already emphasizes this in the body but could better align its abstract and conclusion with this insight.

### Trivial

- The justification for using top-3 (black-box-top3) NN-based attack as the primary MIA method (line 226) is brief. A sentence explaining why top-3 was chosen over top-1 or full posterior would improve reproducibility.

---

## Nice-to-Haves

- Provide baseline accuracy (majority-class prediction) for AIA datasets to contextualize the low attack accuracy on Place100/60.
- Include a brief justification for the choice of black-box-top-3 over top-1 or full posterior for the NN-based attack.
- Consider including loss trajectory-based MIAs (e.g., LZBZ22) for completeness — though this is beyond the paper's stated scope.

---

## Removed Points

These points are flagged to be removed from the review; treat them with caution.

- **Criticism that Diff-Cali cannot be evaluated because the method description is in a stripped `\input{advanced_attack}` file**: Per the hard rules, weaknesses about missing appendix content are removed — the parser strips these sections from all papers; they exist in the original submission. The paper's Section 5.3 provides substantial evaluation details. *Reason for removal: hard rule about stripped appendix content.*

- **Criticism about missing LiRA details**: The paper explicitly addresses this limitation (line 648–649). *Reason for removal: the paper already addresses this.*

- **Criticism about pacing function details being insufficient**: The paper describes "varied exponential pacing" with steps and cites Hacohen & Wolf (2019), which provides the precise formula. *Reason for removal: the paper provides sufficient detail and citation.*

- **Claim that MIA improvements are "within the noise of random seed variation"**: The paper reports standard deviations from 5 repeats that are extremely small (e.g., 0.0000–0.0222), demonstrating consistency across runs. The claim is not supported by the data in the paper. *Reason for removal: factually incorrect given the reported standard deviations.*

- **Strength Finder's generic claim about "comprehensive evaluation"**: Kept as it is supported by specific evidence (9 datasets, 4 CL methods, 3 architectures, etc.). Not removed.

---

## Novel Insights

The most novel insight emerging from synthesizing these reviews is that the paper's key finding is not that CL increases privacy risk (the increase is small), but that it *redistributes* risk: difficult samples become substantially more vulnerable while easy samples are barely affected. This disparate impact finding is well-supported, has a plausible causal mechanism (memorization via repeated ordering), and has practical implications — a practitioner using CL should be aware that the privacy cost is not uniform. The KNN-Shapley analysis further strengthens this by showing the effect is specific to difficulty, not just data value.

---

## Suggestions

1. **Redo the DPSGD evaluation** with a configuration that achieves \(\varepsilon < 10\) and reasonable model accuracy (within 5% of undefended), or explicitly reframe the DPSGD section to focus on the reversal of disparate impact (which is an interesting finding independent of the absolute \(\varepsilon\) value).

2. **Recenter the narrative** in the abstract and conclusion to lead with the disparate impact finding (difficult samples become substantially more vulnerable) rather than the small overall MIA increase. The paper largely does this in the body but the high-level framing still emphasizes the overall increase.

3. **Add formal significance tests** (paired t-tests or bootstrap CIs) for the key comparisons (CL vs. normal, easy vs. difficult groups).

4. **Add AIA baseline accuracy** to contextualize the near-random results for Place100/60.

---
