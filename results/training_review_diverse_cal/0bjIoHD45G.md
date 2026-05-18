I now have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper identifies "implicitly categorical features" (numerical features that behave categorically) as an underappreciated cause of the performance gap between deep learning and tree-based methods on tabular data. It proposes two preprocessing interventions — Categorical Feature Detection (ICF) using simple statistical tests to identify and explicitly encode such features, and Learned Fourier Features (LFF) to mitigate neural networks' bias toward overly-smooth solutions. The combined method (F|C) is evaluated on 68 datasets from an established benchmark (Grinsztajn et al., 2022), with a random search choosing between ICF and LFF per run. Results show ResNet+F|C matches or surpasses XGBoost on classification tasks and narrows the gap on regression tasks.

## Strengths

- **Novel identification of an overlooked cause of the DL/tree gap**: The paper pinpoints a specific, concretely diagnosable data property — numerical features whose relationship with the target is better captured through categorical encoding — and demonstrates its impact on multiple datasets (e.g., eye movements in the Introduction). This insight goes beyond prior aggregate analyses (Grinsztajn et al.) by proposing explicit detection methods.

- **Large-scale empirical evaluation**: The benchmark spans 68 datasets combining classification and regression tasks, with ~51,000 runs total. The budget plots (Figure 2) show consistent improvement of ResNet+F|C over both base ResNet and MLP across all four task types, supporting the core claim that the preprocessing helps.

- **Complementarity demonstrated through ablation**: Figure 5 separates ResNet+F and ResNet+C runs and shows each component dominates on different datasets (e.g., ICF on eye movements, LFF on year). This validates the dual-motivation design and shows the components are not redundant.

- **Performance profiles provide a nuanced picture**: Figure 3's performance profiles complement the budget plots and honestly show that XGBoost retains advantages across much of the performance spectrum, with lines converging near τ=0.97. The paper discusses the apparent contradiction with the budget plots, demonstrating intellectual honesty about the method's behavior.

- **Simple, practical detection methods**: The use of chi-squared, ANOVA, and mutual information tests is transparent, computationally cheap, and requires no additional training — making the approach easy to apply in practice.

## Weaknesses

### Fatal

None.

### Major

- **ICF identification pipeline is critically underspecified for reproducibility**. The paper does not document: (a) the number of bins used for discretizing continuous features, (b) the binning strategy (uniform quantile vs. fixed-width), (c) the range of p-value thresholds explored during hyperparameter search, (d) whether thresholds are dataset-specific or global, or (e) what "low cardinality" threshold is used to automatically treat features as categorical. Lines 63–65 and 72 mention thresholds and low-cardinality handling as hyperparameters, but the actual search space is never reported. Without these details, the method cannot be reproduced, and the reader cannot assess whether the detection is principled or ad hoc. This is the most consequential weakness in the paper.

### Minor

- **The ablation separating ICF and LFF is limited to a cherry-picked subset of datasets**, specifically "a selection of datasets with the highest gap between the best and the runner-up model" (Section 5.4). The paper does not report aggregate performance of ResNet+F and ResNet+C separately across the full benchmark. While the paper's main claim is about the combined F|C method, a full-benchmark decomposition would substantially strengthen the evidence that both components contribute broadly and clarify whether one dominates the other on average.

- **The "spiking" phenomenon (Section 5.3) is framed almost entirely as a strength ("proper encoding is critical") rather than acknowledged as a limitation.** The method's advantage over XGBoost is concentrated in outlier runs where the random search happens to find a good encoding. The paper acknowledges this (Section 5.2 discusses performance profiles showing XGBoost retains advantages across most of the performance spectrum), but the headline claims in the abstract and conclusions are calibrated to the best-run results. Reporting median or lower-quantile normalized performance (e.g., 80th percentile) would clarify whether the method offers reliable gains or only occasional breakthroughs. This is a real limitation for practitioners deciding whether to adopt the method.

- **No error bars or confidence intervals are provided for the budget plots (Figure 2).** Given the high variance implied by the spiking behavior (Figure 4), reporting variability across the 15 simulations (e.g., standard deviation or interquartile range) is important for assessing how much of the observed advantage is robust versus driven by outliers.

- **The hyperparameter search space for the ICF/LFF-specific parameters (bin count, p-value thresholds, Fourier embedding size M, etc.) is not documented anywhere in the paper.** The paper states "150 random seeds over the hyperparameter space" (Section 4) but never specifies what that space contains. This compounds the reproducibility concern from the Major weakness above.

### Trivial

None. The presentation is generally clear and the paper is well-structured.

## Nice-to-Haves

- A sensitivity analysis on bin count and p-value threshold on a few representative datasets would strengthen confidence that the ICF detection is robust rather than sensitive to arbitrary choices.
- Reporting what fraction of the 68 datasets exhibit the "spiking" pattern would give readers a clearer picture of how broadly the phenomenon applies.
- Discussing the connection to Periodic Activation Functions (Gorishniy et al., 2022) more explicitly — the paper mentions similarity (line 96) but does not compare against them experimentally.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Comparison set too narrow (FT-Transformer, TabPFN, NODE, etc.)** — The paper follows the established Grinsztajn et al. benchmark and targets comparison specifically with XGBoost, the best-performing method in that benchmark. Demanding comparisons against a broad set of modern tabular DL architectures would expand the paper beyond its stated scope. The paper's own baseline choices (MLP, 1D-convolutional ResNet, XGBoost) are defensible given its focus on preprocessing for simple backbones.

2. **Missing LightGBM/CatBoost comparison** — The paper's claim is specifically about "closely match[ing] or surpass[ing] XGBoost" (abstract). Comparing against other tree-based methods would be nice but is not required to support the stated claim.

3. **"The paper mixes two conceptually distinct interventions" as a structural criticism** — The paper explicitly presents these as two separate components addressing two different diagnosed causes. Presenting them separately and then combining them is standard methodology. The ablation already separates them.

4. **Criticism about whether the benefit is larger for ResNet vs MLP regarding rotational variance** — This is an interesting analysis question but not required to support the paper's main claims, and the paper's scope does not promise such an analysis.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main insights are about methodological rigor and presentation choices that the paper could improve, not new scientific observations about the phenomenon itself.

## Suggestions

1. **Document the full hyperparameter search space** for ICF detection (binning strategy and count, p-value threshold ranges, low-cardinality threshold) and LFF (embedding size M range, learning rates). This is essential for reproducibility.

2. **Report aggregate performance of ResNet+F and ResNet+C separately across the full benchmark** (not just the top-8 runs on selected datasets) to fully validate the dual-component design.

3. **Add median normalized performance or other robust statistics** to the budget plots to complement the mean-of-best metric and address the spiking concern.

4. **Include error bars or confidence bands** on the budget plots to convey variability across the 15 simulations, especially given the high-variance behavior.

5. **Explicitly discuss the spiking behavior as a limitation** (not just a feature) and advise practitioners on how many random search iterations might be needed to reliably find good encodings.

## Score and Decision

The paper makes a genuinely novel and interesting contribution by identifying implicitly categorical features and proposing a practical, interpretable approach to address them. However, the experimental evaluation has significant reproducibility gaps (the ICF pipeline is underspecified, the hyperparameter search space is undocumented) and the headline results are tempered by the spiking phenomenon — the method's advantage is concentrated in outlier runs rather than being consistent. These issues do not invalidate the paper's core insight but prevent it from fully supporting its more ambitious claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>