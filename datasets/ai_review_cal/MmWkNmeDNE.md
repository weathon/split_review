- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 5, 5, 5, 6
Now I have a complete picture. Let me write the final consolidated review.

---

## Summary

This paper proposes using random matrix theory (RMT) as a zero-information null hypothesis to locate learned features in the weight matrices of pretrained transformers (BERT and Llama-8B). It shows that different matrix types (query, key, intermediate.dense vs. attention.output, value) exhibit distinct deviation patterns from the Marchenko-Pastur law, uses a Monte Carlo KS test on singular vectors to quantify these deviations, validates via activation-covariance overlap analysis, and conducts removal experiments to tie RMT deviations to functional importance. The paper also sheds light on the debate about small singular values by showing their importance emerges during fine-tuning.

## Strengths

- **Cross-architecture consistency of spectral patterns (BERT and Llama-8B):** Figures 1–2 demonstrate that query matrices consistently produce many spectral outliers while attention.output matrices remain close to the Marchenko-Pastur law, across both a ~110M and an ~8B parameter model. This structural regularity supports the claim of layer-type-specific feature learning beyond any single architecture.

- **Quantitative link between RMT deviations and learned features via activation covariance:** Section 5 (Figure 4) shows that singular vectors outside the MP bulk achieve maximal overlap with activation covariance eigenvectors above 0.5 in a 768-dimensional space, while vectors inside the bulk show near-zero overlap. This directly confirms that RMT-deviant regions encode data-driven features, using a clean, independent signal (activation data) that does not rely on downstream task performance.

- **Custom Monte Carlo KS test for singular vectors:** Section 4 derives a tailored null distribution for the KS statistic using synthetic Gaussian vectors, avoiding the bias of standard KS tables that assume independent entries. This is methodologically careful — the normalization constraint of singular vectors introduces correlations that would otherwise inflate false positives.

- **Fine-tuning experiment (Figure 7) provides clear evidence on the small-singular-value debate:** The before/after comparison is clean: removing the smallest 10% of singular values before fine-tuning has negligible effect (within error bars), but removing them after fine-tuning causes a significant accuracy drop. This specificity to decile 10 (not blocks 1–9) shows this is not a generic "model can adapt to any perturbation" artifact; it is concentrated on the smallest singular values.

- **Reproducibility:** The paper provides a Zenodo archive with pre-saved data, Jupyter notebooks, and SLURM scripts, enabling independent verification of all figures.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence. While some concerns warrant attention, none invalidate the main contributions.

### Minor

- **Pretrained p-values shown alongside fine-tuned removal results (Figure 6):** The insets in Figure 6 display p-values computed from the *pretrained* model's singular vectors, while the accuracy drops result from removing singular values from the *fine-tuned* model. The caption states "Values below this plateau suggest learned information during pretraining," confirming this mismatch. If fine-tuning changes the singular vectors, the pretrained p-values may correspond to different vectors than those being removed. The paper does not address whether singular vectors remain stable during fine-tuning or recompute p-values on the fine-tuned weights. This weakens the stated "good agreement" between RMT deviations and functional importance. *(However, note that the accuracy drops themselves stand as independent evidence of functional importance — the p-values are supporting context, not the primary result.)*

- **Ambiguity about the scope of fine-tuning:** The paper states: "we fine-tuned a pretrained BERT transformer using five different random seeds for initializing the model heads on the BoolQ dataset." It does not explicitly state whether *all* parameters are updated or only the classification head. Standard practice is full fine-tuning, and the paper's analysis of weight-matrix changes during fine-tuning (Section 7) only makes sense if the weights are updated. However, the 73.6% accuracy is lower than typical BERT-base BoolQ results (~77%), and the phrasing should be clarified to eliminate any ambiguity.

- **Generality of the activation covariance analysis:** The overlap analysis in Section 5 is performed only for BERT on the BoolQ dataset. Llama-8B is analyzed for its spectra (Figures 1–2) and p-values (Figure 3), but the activation-covariance validation is not extended to it. This limits the strength of the claim that RMT-deviant regions universally correspond to learned features across architectures.

- **Overclaim on "alignment":** The abstract and conclusion suggest that removing small singular values from an "already aligned transformer" could "compromise model alignment." The experiments are conducted on BoolQ (a question-answering dataset), not on any alignment benchmark. The paper cites Perez et al. (2022) to connect alignment degradation with performance changes, but this remains a speculative extrapolation beyond the experimental scope. The paper would be stronger if it either tested an aligned model directly or framed this as a speculation rather than a conclusion.

### Trivial

- **Averaging window size for p-values is not justified:** The paper uses a sliding window of 15 neighbors (Eq. 4) to smooth p-values. The choice is ad hoc; the paper does not discuss the singular-value-index correlation length or whether results are robust to this parameter.

## Nice-to-Haves

- Compare the MP distribution fitted to the spectral bulk against the fixed initialization variance (σ=1/√m) to assess how much of the apparent deviation is a shift in scale versus genuine structural change.
- Include a random-matrix control at the same dimensions and variance as the empirical bulk to quantify the expected finite-size fluctuations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's Criticism 1 (fine-tuning claim not supported):** The reviewer argues that the before/after removal experiment (Figure 7) is confounded by the network's ability to adapt during subsequent fine-tuning. This misunderstands the experimental design. The "remove before fine-tune" condition deliberately allows the network to re-encode information during fine-tuning; the comparison tests whether fine-tuning specifically makes small singular values important. The fact that the effect is concentrated on decile 10 (not blocks 1–9) shows this is not a generic "model can adapt" property. The related sub-criticism about "removal targets not being the same singular values" likewise misses the point — the experiment compares the smallest 10% at each stage, and the singular values naturally differ between stages, which is exactly what is being tested. **Removed: misunderstanding of the experimental design.**

- **Harsh Critic's decile spacing concern:** "The removal of deciles does not account for the fact that singular values are not evenly spaced; decile 1 may contain a few very large values while decile 10 contains many tiny values." The paper uses *equally sized* deciles (10% of the singular values each), which is the correct and standard approach. The spacing of the singular values within a decile is irrelevant to the experiment's design. **Removed: factually incorrect criticism.**

- **Harsh Critic's claim about "unfair comparison" and Section 3 MP parameter choice being a weakness:** The paper's choice of σ=1/√m is deliberate — it uses the initialization scale as a fixed reference to identify deviations, rather than fitting to the data. This is a valid methodological choice. The suggestion to fit the variance is a nice-to-have, not a weakness. **Demoted to Nice-to-Have.**

- **Strength Finder's claim #3 ("Removal experiments tie RMT deviations to functional importance"):** This is partially weakened by the p-value mismatch issue (kept as a Minor weakness above). The accuracy drops themselves remain valid evidence of functional importance, but the specific claim about agreement with RMT deviations is qualified by the mismatch. The strength is retained but with the caveat absorbed into the Minor weakness.

## Novel Insights

The most interesting observation from the review process is the tension between two analyses that the paper itself does not resolve: the p-values in Section 3/4 are computed on *pretrained* weights and convincingly show RMT deviations, while the removal experiments in Section 6 are on *fine-tuned* weights. The paper assumes continuity between these states without verifying whether the singular vectors change during fine-tuning. The fine-tuning experiment (Section 7) suggests that small singular values *acquire* importance during fine-tuning, which implies that the singular vectors *do* change — yet this is never directly measured. A direct comparison of the singular-vector p-values before and after fine-tuning would either confirm the validity of the comparison in Figure 6 or reveal a more nuanced picture.

## Suggestions

1. Explicitly state whether fine-tuning updates all parameters or only the classification head.
2. Recompute p-values on the fine-tuned weights for the removal experiment (Figure 6), or at minimum discuss whether singular vectors remain stable during fine-tuning.
3. Extend the activation-covariance overlap analysis to at least one Llama-8B layer to support cross-architecture generality.
4. Tone down claims about "alignment" to match the experimental scope (BoolQ), or add experiments on an aligned model.
5. Provide a brief justification or sensitivity analysis for the averaging window size of 15 neighbors.
