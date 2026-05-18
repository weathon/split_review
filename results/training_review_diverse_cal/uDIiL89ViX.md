Now I have a thorough understanding of the paper and can verify each claim against the actual content. Let me compose the final consolidated review.

## Summary

This paper asks whether dictionary learning can extract unknown, biologically-meaningful concepts from unsupervised microscopy foundation models — extending mechanistic interpretability beyond text and natural images into a domain where prior knowledge is sparse. The authors show that sparse features learned from a masked autoencoder's intermediate representations correlate with cell types, genetic perturbation types, and functional gene groups. They propose Iterative Codebook Feature Learning (ICFL), a decoder-only dictionary learning approach that avoids "dead features" without auxiliary regularization, and combine it with PCA whitening on a control dataset as a form of weak supervision. Experiments demonstrate that both ICFL and PCA improve feature selectivity compared to TopK sparse autoencoders, and that the learned features approach the selectivity of handcrafted CellProfiler features (Pearson r=0.71). Qualitative analysis validates biological plausibility at the token level for selected features.

## Strengths

- **First demonstration of dictionary learning for concept discovery in microscopy foundation models.** The paper extends mechanistic interpretability tools to a scientific domain (cellular microscopy) where concepts are unknown a priori, unlike prior work on text, games, or natural images. This opens a new application direction for sparse dictionary learning. The key evidence is that learned features correlate with cell type, genetic perturbation type, and functional gene groups (Figures 2d–f, Table 3), and are validated by token-level heatmaps aligning with known biology (Figures 4–5, Section 7).

- **ICFL eliminates dead features naturally.** Table 1 reports that ICFL produces zero dead features (out of 8192) during training, while TopK SAEs yield 236 dead features under identical conditions. This is a concrete algorithmic advantage stemming from the design choice of not backpropagating through z during decoder updates (Section 4).

- **PCA whitening on a control dataset substantially improves feature quality.** Figure 2a shows a clear drop in linear probing accuracy when PCA whitening is omitted (e.g., from ~0.8 to ~0.6 on siRNA tasks), and Figure 2b confirms that the benefit of PCA whitening is larger than the effect of sparsity. This provides clear evidence that the preprocessing step serves as effective weak supervision (Section 5).

- **Learned features nearly match handcrafted CellProfiler features in selectivity.** Figure 3e shows that the top average selectivity scores per label for ICFL are close to those of 964 expert-designed CellProfiler features, with a Pearson correlation of 0.71 between the two (Figure 3g). This grounds the unsupervised features against the current standard in microscopy image analysis.

- **Qualitative analysis confirms biological plausibility.** Section 7 demonstrates that feature directions align with known biology: a feature for adherens junction knockouts highlights disrupted cell-cell adhesion (Figure 4), and features for OPA-1 (mitochondrial), ALG-3 (ER), and TSC-2 (membrane) mutations show channel-specific correlations consistent with known protein functions (Figure 5). These token-level heatmaps provide concrete validation that the learned concepts are interpretable and domain-relevant.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric comparison with TopK SAEs weakens the selectivity superiority claim.** The paper uses the same fixed hyperparameters (learning rate 5e-5, sparsity K=100) for both TopK and ICFL and states that "changing the learning rate has a limited impact" (line 65) without showing an ablation specific to this setting. Since TopK SAEs are known to be sensitive to learning rate and sparsity choices (Gao et al., 2024), and the cited observation about learning rate insensitivity comes from language model experiments, it is unclear whether TopK was given a fair hyperparameter search. This concern also applies to the dead-feature comparison in Table 1. Without evidence that TopK was reasonably tuned for this domain, the claim of "consistently higher selectivity" (Section 6.1) rests on a potentially uneven playing field.

- **ICFL components are not ablated, making it unclear what drives improvement.** The paper does not systematically ablate the key design choices of ICFL: the effect of the number of iterations J, the per-iteration sparsity k, the random resets for decorrelation, or a comparison with a single-pass version (matching TopK's encoder but using the same decoder learning). Without these ablations, it is impossible to attribute the observed improvements to the iterative matching pursuit mechanism specifically, as opposed to the decoder-only training, the random resets, or simply the higher effective model capacity. The sparsity ablation in Figure 2b is general and does not address ICFL-specific components.

### Minor

- **No computational cost comparison.** ICFL's iterative matching pursuit is likely significantly slower than a single forward pass through a TopK encoder. A brief runtime comparison (e.g., tokens/second or training wall-clock time) would help practitioners decide which method to use and is notably absent. This gap is relevant because ICFL's advantage in selectivity may come at a substantial computation cost.

- **Systematic quantification of interpretable features is limited.** The qualitative analysis (Section 7) is compelling but covers only a handful of hand-picked features. Table 3 provides feature counts at selectivity thresholds (0.3, 0.15, 0.1), but these thresholds are not motivated and a cumulative distribution of max selectivity across all 8192 features would be more informative. The paper does not characterize what fraction of features have clear biological interpretations, leaving open the question of how many learned features are actually useful for scientific discovery versus noise.

### Trivial
None.

## Nice-to-Haves

- Numeric tables reporting mean and max selectivity with bootstrapped confidence intervals or error bars alongside the figures would make the ICFL-vs-TopK comparison more concrete, especially given that the figures (2d–f) are the primary evidence for the selectivity claim.
- A cumulative distribution plot of max selectivity across all 8192 features (instead of arbitrary thresholds) would more informatively characterize the learned dictionary.
- For the CellProfiler comparison, the thresholding procedure (matching average non-zero count) is reasonable but the paper could run a sensitivity analysis on the choice of α.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Quantitative comparisons whose actual numerical values are not visible"* — The figures and tables exist in the original submission; their absence is a PDF-parser artifact. The paper contains Table 1 (dead features), Table 3 (feature selectivity counts), and Figures 2–5 (plots/visualizations), which are standard presentation formats.
- *"ICFL algorithm should be presented as a full pseudocode block"* — Algorithm 1 is referenced in the original submission (line 30); it is stripped by the parser, not absent from the paper. The textual description (lines 30–33) provides a reasonably complete specification: select top-k columns by alignment, solve for z on selected columns, compute residual, repeat J times, sum z^(t).
- *"Other sparse dictionary learning methods (k-SVD, ISTA, LISTA) not considered"* — This evaluates the paper against the wrong class of expectations. The paper's goal is to show that DL works for microscopy concept discovery, benchmarking against the relevant SOTA (TopK SAEs) and the domain standard (CellProfiler). A comprehensive survey of DL algorithms would be a different paper.
- *"PCA whitening — similar ideas are common in high-throughput biology"* — The paper acknowledges this by citing Kraus et al. (2024) (line 63) and presents PCA whitening as a technique they use, not as a novel invention. This criticism misreads the paper's claim.
- *"Selectivity score does not account for strength of activation"* — The paper uses the standard definition from Hubel & Wiesel (1968) and Madan et al. (2022), based on binary activation rates. Both ICFL and TopK produce sparse z with most entries zero, so the comparison is consistent. The CellProfiler comparison uses a separate quantile-thresholding procedure that the paper describes transparently.
- *"Selectivity thresholds (0.3, 0.15, 0.1) are arbitrary"* — Using a small set of thresholds to summarize feature counts is standard practice. A cumulative distribution (suggested as a nice-to-have) would be more informative but the current approach is not a weakness.
- *"The paper would benefit from a clearer discussion of when PCA whitening might remove biologically relevant variance"* — The paper applies PCA whitening on a control dataset (unperturbed HUVEC cells) precisely to downweight variance directions that do not correspond to biological perturbations. This is a reasonable design choice and the logic is stated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the work that the paper itself does not already articulate.

## Suggestions

1. **Run a hyperparameter sensitivity analysis for TopK SAEs** (learning rate, sparsity K) in this domain and show that the comparison is fair. Alternatively, present the results as "ICFL under fixed hyperparameters achieves X; TopK after tuning achieves Y" — whichever is the honest comparison.
2. **Ablate ICFL components**: compare full ICFL vs. a single-pass variant (J=1), vary J and k independently, and test without random resets. This would pin down what drives the improvement.
3. **Report wall-clock training time** or tokens/second for both ICFL and TopK to help practitioners assess the trade-off.
4. **Add a cumulative distribution plot** of max selectivity across all features (or the fraction of features with selectivity > threshold as a continuous curve) to replace or supplement Table 3.
5. **Provide numeric summaries** (mean ± std) of the selectivity scores for both methods in a table alongside Figures 2d–f.

## Score and Decision

The paper makes a solid contribution by demonstrating that dictionary learning can extract biologically-meaningful concepts from unsupervised microscopy foundation models, and the qualitative validation is genuinely convincing. The proposed ICFL algorithm and PCA whitening preprocessing show clear benefits. However, the central quantitative comparison with TopK SAEs is weakened by the absence of hyperparameter tuning for the baseline and the lack of component ablations for ICFL. These are real gaps but not fatal — the core contribution (DL works for microscopy concept discovery) does not depend on ICFL being strictly better than TopK, and the CellProfiler comparison provides an independent anchor. The paper is well-positioned for acceptance after addressing these methodological gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>