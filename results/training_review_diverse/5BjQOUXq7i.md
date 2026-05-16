I now have all the information I need. Let me synthesize the final review.

## Summary

RegMix formulates data mixture selection for LLM pre-training as a regression task: it trains 512 small proxy models (1M params, 1B tokens each) on random mixtures sampled via Dirichlet distributions, fits a LightGBM regressor to predict validation loss from mixture weights, then simulates millions of mixtures to identify the optimal one, which is averaged across the top-100 and used to train a 1B-parameter model for 25B tokens. The paper validates rank invariance across a 1000× model-size and 25× token-count gap (Spearman ρ=97.12%), shows RegMix matches DoReMi's average downstream performance at 10% of the compute, and reveals that web corpora (Pile-CC) correlate more strongly with downstream performance than Wikipedia.

## Strengths

1. **Direct empirical validation of rank invariance across 1000× model-size and 25× token-count gaps**: Table 1 shows LightGBM achieves Spearman ρ=97.12% when predicting the rank of 1B-parameter/25B-token models from data learned on 1M-parameter/1B-token proxy models. This is the paper's central claim and it is directly supported with clean evidence.

2. **10× compute reduction while matching downstream performance of DoReMi**: RegMix uses 3.5×10¹⁸ FLOPs to find the mixture (vs. 3.7×10¹⁹ for DoReMi) yet achieves the same 48.6% average downstream score (Table 2). The 512 proxy models can be trained in parallel, making the practical advantage even larger.

3. **Non-obvious finding that web corpora (Pile-CC) correlate better with downstream performance than Wikipedia**: Figure 2(a) shows Pile-CC validation loss has near-1.0 correlation with HellaSwag, while Wikipedia exhibits much weaker correlation. This challenges common practice and provides actionable guidance for data curation.

4. **Actionable insight that increasing the number of proxy models is more effective than increasing tokens per model under a fixed FLOPs budget**: Section 4.2 shows 512 models × 0.2B tokens outperforms 128 models × 0.8B tokens. This gives practitioners a concrete resource-allocation rule.

5. **Robustness demonstrated via out-of-distribution validation**: Even when Pile-CC is excluded from the training corpus entirely, RegMix still finds a mixture that outperforms human and DoReMi baselines on Pile-CC validation loss (Figure 3 right).

6. **Revelation of complex, non-intuitive domain interactions via regression coefficients**: Figure 4 shows, e.g., PhilPapers positively contributing to all other domains — a pattern that would be difficult for human experts to anticipate, motivating automated approaches.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair DoReMi comparison weakens the "match or surpass" claim**: DoReMi's domain weights are taken from the original paper and re-normalized across the available 17 domains, which the authors acknowledge "may result in sub-optimal performance." Because this re-normalization likely disadvantages DoReMi, the claim of matching or surpassing DoReMi is not on fully equal footing. The paper would be substantially stronger if DoReMi were run in the exact same 17-domain setup, or if the original unnormalized weights and the effect of re-normalization were reported.

2. **Rank invariance validated only up to 1B parameters**: While the 1M→1B (1000×) scaling demonstration is impressive, 1B parameters remains small relative to the 7B+ models that the paper motivates as its target application. Pearson's r also drops to 94.36% at the 1B scale (vs. 98.57% at 1M), hinting at possible degradation. Without evidence — even a single experiment at 3B or 7B, or at an intermediate 350M–600M scale, or a more detailed discussion of why invariance should persist — the method's applicability to modern LLM scales remains an assumption. This is the paper's most significant open question.

### Minor

1. **Target domain selection guideline is under-specified**: The paper chooses Pile-CC as the optimization target because it correlates best with downstream tasks (justified empirically), but does not provide a general, principled recipe for selecting the target domain when applying the method to a new corpus with an unknown validation set. The OOD experiment is a good robustness check but doesn't resolve the *a priori* selection question.

2. **No ablation or justification for averaging top-100 mixtures**: The paper selects the top-100 simulated mixtures and averages them (Section 3.4) without sensitivity analysis or ablation. Why 100 rather than 1, 10, or 500? How much does this averaging affect downstream results?

3. **Hyperparameters for LightGBM not disclosed**: The central regression model is described only as "LightGBM." No parameters (learning rate, num_leaves, subsample, etc.) or tuning procedure are given, which slightly harms reproducibility.

4. **No wall-clock time or hardware comparison**: The FLOPs comparison is informative but coarse. The 512 proxy models can be trained in parallel (an advantage mentioned in the paper), but the practical GPU-hours vs. DoReMi is not reported, making it harder for practitioners to assess the real-world savings.

5. **The "transcend scaling laws" claim is overstated**: The paper argues that data mixture effects "transcend scaling laws" by showing that a simple log-log linear relationship between domain weight and loss does not hold for most domains. However, recent data mixing scaling law work (Ye et al., Ge et al., both cited in the paper) uses more complex functional forms that do not assume log-log linearity. The claim should be tempered to say that a *simple* log-log linear model is insufficient, rather than implying all scaling law approaches are transcended.

6. **Proxy model vs. token count analysis only evaluates regression accuracy, not final downstream performance**: Section 4.2 shows that more proxy models improve regression prediction accuracy, but does not directly test whether the final 1B model's downstream performance also benefits more from more proxy models vs. more tokens. The connection is indirect.

### Trivial

1. The "1000× larger and 25× longer" phrasing (abstract and introduction) cleanly describes parameter and token scaling, but it could be slightly clarified to distinguish parameter count scaling from token count scaling on first reading.

## Nice-to-Haves

- Running DoReMi in the exact 17-domain setup would eliminate the re-normalization concern entirely and make the compute comparison ironclad.
- A single experiment at an intermediate scale (e.g., 350M or 600M parameters on the predicted mixture vs. a human baseline) would strengthen the rank invariance generalization.
- A brief discussion of how to select the target validation domain *a priori* would make the method more directly usable — e.g., using a small holdout subset of the final evaluation tasks, or showing that averaging over multiple target domains also works.
- Reporting the Dirichlet α range sensitivity (0.1–5.0) as an ablation would strengthen the method description.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Figure 1 "slightly misleading" phrasing about 1000×/25×**: The critic's note that this is "slightly misleading" is not a real weakness — the paper states the numbers factually (1M→1B = 1000×, 1B→25B tokens = 25×) with a clarifying footnote about non-embedding parameters. This is a presentation nitpick, not a substantive concern.
- **Criticism about Dirichlet hyperparameter range (0.1–5.0) not being justified**: While a sensitivity analysis would be nice, the paper explains the purpose (construct sparse and near-uniform distributions to cover extreme weights). This falls below the threshold for inclusion as a weakness in a paper already demonstrating strong empirical validation.
- **"It would be informative to know whether RegMix significantly outperforms DoReMi on individual tasks"**: The paper already reports standard deviations and Cohen's d tests against the Human baseline. The comparison against DoReMi is constrained by the re-normalization issue (already listed as a major weakness), but the raw means and stds are reported for all methods. This is a wishlist item, not a weakness.

## Novel Insights

The review process surfaces two insights that go beyond the paper's own contributions. First, the regression-based framing itself is noteworthy because it decouples the mixture-search problem from training dynamics monitoring: by learning a *surrogate model* of loss as a function of mixture weights, the approach replaces expensive sequential search (DoReMi's 100B-token proxy) with an embarrassingly parallel design. Second, the paper's discovery that Pile-CC (generic web text) is a better indicator of downstream performance than Wikipedia is striking precisely because it contradicts a widely held belief in the community — and the regression coefficients (Figure 4) further show that domain interactions are non-monotonic and unintuitive, which is a genuine empirical finding that challenges how data curation is typically done.

## Suggestions

1. Run DoReMi in the exact 17-domain setup (or at minimum, report the original DoReMi weights and the effect of re-normalization) to make the comparison fair and the compute advantage ironclad.
2. Add a brief ablation or justification for the top-100 averaging cutoff — even a sentence explaining that performance plateaus beyond ~100 would help.
3. Temper the "transcend scaling laws" language to acknowledge that more complex (non-log-log-linear) scaling law formulations exist.
4. Consider including a small-scale experiment at an intermediate model size (350M–600M params) to extend the rank invariance evidence.

## Score and Decision

The paper presents a clean, well-motivated approach to a practically important problem. The core contribution — treating data mixture selection as regression on proxy model results with empirical validation of rank invariance — is sound and backed by careful experimentation. The two most significant weaknesses (unfair DoReMi comparison and limited scale of rank invariance validation) are genuine but addressable: the DoReMi issue can be resolved by running DoReMi in the same setup, and the scale concern can be partially addressed with intermediate-scale experiments or a more careful discussion of scaling behavior. Neither weakness invalidates the paper's central claims. The empirical findings about web data and domain interactions are valuable independent contributions. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>