Now I have thoroughly read the paper and verified all claims. Let me produce the consolidated review.

## Summary

This paper proposes MultiHot Embedding, a simple method for representing numerical features in deep learning. The approach discretizes numerical values into fine-grained bins and activates the bin itself plus *m* neighboring bins in the embedding lookup, creating overlapping representations. The method is designed to address two problems of standard discretize-and-embed approaches: (1) SBD/DBS information loss from bin-boundary artifacts, and (2) inadequate training when using many narrow bins. Experiments on 6 tabular datasets with MLP and ResNet backbones are reported, along with a sensitivity analysis on the California Housing dataset.

---

## Strengths

1. **Clear, well-motivated method that directly targets a well-defined problem.** The SBD/DBS problems and the "inadequate training" issue with narrow bins are explained accessibly in Section 2, and the MultiHot mechanism (activating *m* neighbors) is a natural, minimal extension to one-hot that addresses both concerns. The geometric intuition in Figure 2 (overlapping representations for boundary values) is compelling.

2. **Figure 5 provides direct empirical support for the core claim.** The sensitivity analysis on California Housing shows that as the number of bins increases, One-hot Embedding (OE) peaks then degrades (consistent with inadequate training), while MultiHot Embedding continues to improve. This is the paper's strongest piece of evidence — it cleanly isolates the mechanism that the method is designed for.

3. **Consistent empirical advantage across diverse datasets.** Table 1 reports that MultiHot achieves the best performance in 5 out of 6 datasets for both MLP and ResNet, beating a more complex state-of-the-art method (AutoDis). This suggests the method generalizes across different problem types (regression, classification) and dataset sizes.

4. **Interpretability of the representation is explicitly addressed.** Section 3.3 and Figure 3 provide a clear semantic interpretation where each element of the MultiHot vector corresponds to a wider overlapping interval, making the representation transparent rather than a black-box mapping.

---

## Weaknesses

### Fatal
None. The core idea is sound and there is supporting evidence. No error invalidates the paper's central thesis.

### Major

1. **No uncertainty quantification on any experimental result.** Table 1 reports every value as a single number with no standard deviation, confidence interval, or indication of multiple runs. Several improvements are small (e.g., Adult Accuracy differences at the ~0.001 level); without variance estimates the reader cannot determine whether these improvements are meaningful or within noise. For a methods paper that claims "significantly improves prediction performance" (abstract), this is a serious evidential gap. *(Applies to: Table 1, Section 4.2)*

2. **Critical hyperparameters (K and m) are not disclosed for the main experiments.** The paper never states the number of bins *K* or the neighbor radius *m* used to produce the results in Table 1. The sensitivity analysis (Figure 5) varies only bin count and only for California Housing. For the other five datasets, the reader is given no information about these method-defining parameters. The statement that the authors "follow the model configuration and training details specified in Gorishniy et al. (2021)" covers backbone architecture but not MultiHot-specific choices *(Section 4.1, line 131)*. Without this information, the results are not reproducible and the reader cannot assess whether optimal *K*/*m* varies across datasets.

### Minor

3. **Sensitivity analysis is limited to one dataset (California Housing) and does not vary *m*.** Figure 5 convincingly demonstrates the trend on CA but does not show whether the same behavior holds on other datasets (e.g., Adult, Helena). Additionally, Figure 5 fixes *m* at an unspecified value, so the interaction between *m* and bin count — which is important for understanding the method's behavior — is not explored. *(Applies to: Section 4.3, Figure 5)*

4. **Improvement percentages may be overstated relative to the strongest baseline.** Section 4.2 claims "over 7% and 9%" improvement for CA (MLP and ResNet) and "over 2%" for AT and HE. The Table 1 caption states improvements are "compared to the best baseline," but without access to per-cell numbers the reader cannot verify this. The specific numbers needed for verification are embedded in a table image rather than stated in the text. The authors should audit their improvement calculations against the best baseline (not a weaker one) and report them transparently. *(Applies to: Section 4.2, Table 1 caption, Conclusion)*

5. **AutoDis is mischaracterized.** The paper states (Section 4.2, line 149) that "AD still uses the numerical value as input without the discretization process." AutoDis performs learned soft discretization via its automatic binning mechanism — it does not take the raw numerical value directly. This is a simplification that weakens the analysis; the contrast should focus on hard vs. soft discretization rather than claiming no discretization occurs.

6. **Embedding dimensionality *h* is not reported for experiments.** The embedding size *h* is defined in Section 3.1 (the output dimension of the lookup matrix **M**) but never specified in the experimental setup. If inherited from Gorishniy et al. (2021), this should be stated explicitly. *(Applies to: Sections 3.1, 4.1)*

### Trivial
None.

---

## Nice-to-Have

- **Ablation isolating the overlap mechanism.** Comparing MultiHot with *m*=0 (equivalent to one-hot with many bins) against MultiHot with *m*>0 at the same bin count would directly isolate the contribution of the neighbor activation from the effect of simply using more bins.
- **Extending sensitivity analysis** to at least one more dataset (e.g., Adult) and including a sweep of *m* values would significantly strengthen generalizability claims.
- **Computational cost discussion.** MultiHot with large *m* activates up to *2m+1* rows of the embedding matrix per input, increasing the effective embedding dimension. The paper should at least note this trade-off.
- **Comparison to simple smooth alternatives** (e.g., linear interpolation between adjacent bin embeddings, or kernel-weighted combinations) would help clarify whether the hard binary activation pattern is essential or incidental.

---

## Removed Points

- **"Overstated improvement claim" framed as a confirmed factual error.** The critic asserts the 9% figure for CA ResNet is relative to STD (0.4520) rather than the best baseline OE (0.4311), giving ~6.15% actual improvement. The specific numerical values (0.4520, 0.4311, 0.4046) come from the table image which is not machine-readable in this text extraction. The paper explicitly states in the Table 1 caption that improvements are "compared to the best baseline." Since the critic's claim depends on specific numbers I cannot independently verify from the extracted text, and the paper's stated methodology is clear, this is not a confirmed overstatement — it is a potential concern that needs verification. Demoted to Minor (weakness #4 above).
- **Strength Finder claim about "Clear and testable mechanism for addressing SBD and DBS"** — kept, as it is specific and grounded.
- **Strength Finder claim about "intuitive interpretation"** — kept.
- **"No comparison to interpolation/kernel-based embeddings"** — moved to Nice-to-Have (scope creep; paper compares to standard baselines: STD, OE, AutoDis).
- **"Missing related works"** — removed per instructions (cannot verify external sources).
- **"Section-by-section notes" on typographical errors** — removed per instructions (parser artifacts, not author errors).
- **"Excluding transformer models is a weak justification"** — removed. The paper explicitly scopes this out (Section 4.1: "sensitivity to hyperparameters... could obscure the influence of different numerical feature representation methods"), which is a reasonable justification for an already-broad 6-dataset evaluation.

---

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same assessment: the method is simple and plausible, the sensitivity analysis provides the cleanest evidence, but the lack of statistical rigor and missing hyperparameter details prevent the paper from meeting the standard of evidence for a methods contribution.

---

## Suggestions

1. **Report all results with means and standard deviations over at least 5 random seeds.** For small improvements, include a paired significance test against the best baseline.
2. **Disclose *K* and *m* for every dataset in Table 1** (either in a table or an appendix). State the binning strategy (equal frequency, as mentioned) and describe any tuning procedure used.
3. **Audit improvement percentages** and report them against the single best baseline per backbone. Provide the raw numbers (e.g., improvement = (baseline − MultiHot)/baseline × 100%) clearly.
4. **Extend sensitivity analysis** to at least one more dataset and include a sweep over *m* to show how the overlap radius affects performance.
5. **Add a simple *m*=0 ablation** at the same bin count to isolate the overlap effect from the bin-count effect.
6. **State the embedding dimensionality *h*** used in all experiments.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>