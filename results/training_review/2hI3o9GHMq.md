Now I have a thorough understanding of the paper and can verify each claim. Let me write the consolidated review.

## Summary

This paper proposes Self-Matrix Factorization (SMF), a non-negative matrix factorization method augmented with a self-expressive term that jointly learns object embeddings and object similarities from association data alone. The key idea is to add a term that reconstructs each row of the data matrix using other rows weighted by the dot products of their embeddings (via \(WW^\top\)), intending to preserve linear manifold structure. The method is evaluated on three real-world datasets (MovieLens, Drug-SE, ModCloth) and compared against NMF, HCCF, and SLIM, showing improvements in both missing-association prediction (RMSE, precision@K) and embedding quality (class separation via Z-scores).

## Strengths

- **Novel integration of self-expressive learning into matrix factorization**: The second term in Eq. 2, which reconstructs rows of \(X\) using other rows weighted by \(WW^\top\), is a principled extension of subspace clustering ideas into the NMF framework. Unlike prior work that requires manually curated similarities, SMF learns similarities and embeddings jointly from the association matrix itself. The paper clearly articulates this as its core novelty (Section 3).

- **Consistent empirical superiority in predicting missing associations**: SMF achieves lower RMSE than NMF and SLIM across all three datasets (e.g., 15 % lower RMSE than NMF on ModCloth, ≥65 % lower than SLIM on all datasets). In the top-K precision evaluation, SMF achieves the best precision in 7 out of 10 settings (Figure 2). These results are based on 30 runs with reported variance, providing statistical grounding.

- **Higher-quality embeddings that encode unseen object attributes**: SMF embeddings yield significantly larger Z-scores for intra- vs. inter-class separation than NMF and HCCF across all datasets and attribute groupings (Figure 3), including users by gender, movies by genre, drugs by ATC hierarchy levels, and clothes by type. The analysis uses a two-sample t-test and covers multiple runs, showing SMF achieves statistical significance in ≈99 % of experiments vs. 41 % for NMF and 87 % for HCCF.

- **Robustness to hyperparameters**: The sensitivity analysis on MovieLens (Section 4.1) shows that SMF maintains stable performance across a wide range of hyperparameter values, with only the α weight on zeros causing predictable task-dependent variation. This reduces practical tuning burden.

## Weaknesses

### Fatal
None.

### Major

- **No theoretical justification for the claimed manifold-preserving property, only intuition.** The paper asserts that minimizing the self-expressive term "will favour reconstructing each row using only rows representing the objects in the same subspace" (Section 3), but this claim is supported only by informal reasoning and a toy illustration (Figure 1). The coefficient matrix \(T \circ (WW^\top)\) is dense, low-rank, and symmetric — there is no analysis showing it enforces sparsity or subspace selectivity. The empirical evidence in Section 4.2 (Z-scores, t-tests) provides indirect validation that SMF embeddings encode attributes, but the paper does not establish a formal link between the loss function and the claimed manifold-preserving mechanism. Since this mechanism is the core novelty, the lack of formal analysis weakens the theoretical contribution.

- **Missing ablation isolating the self-expressive term.** The paper attributes SMF's gains to the novel self-expressive term (\(\lambda_{se}\)), but never runs an ablation that removes this term while keeping the weighting scheme (\(P\) matrix) and elastic-net regularization identical. Without comparing SMF to a version with \(\lambda_{se}=0\) (while retaining the weighted-zero scheme and regularizers), it is impossible to quantify how much of the improvement comes from the novel term vs. from the weighting scheme and regularization that are not present in standard NMF. This is a standard experimental control that should have been conducted.

- **Scalability is prohibitive and unaddressed in practice.** The stated per-iteration complexity is \(O(n^2 m)\) (Section 3). For the ModCloth dataset (\(n=32\,089, m=5\,419\)), this is \(\sim 5.6 \times 10^{12}\) operations per iteration. No wall-clock time, number of iterations to convergence, or practical runtime is reported for any dataset. While the paper references an appendix for computational details (which exists in the original submission), the main paper does not discuss whether the method converges in a feasible number of iterations or whether approximations (e.g., mini-batching) are possible. This makes it difficult to assess whether SMF is practical beyond small-scale settings.

### Minor

- **Embedding dimension mismatch in the cosine-similarity evaluation.** In the clustering analysis (Section 4.2), SMF and NMF use embedding dimensions of \(k=5\)–\(15\) (varying by dataset), while HCCF uses a fixed dimension of \(64\) (Table 1). Cosine-similarity-based metrics are known to be sensitive to dimensionality due to concentration of measure, which could systematically affect the comparability of Z-scores across methods. This is a methodological confound in the HCCF comparison. (Note: the SMF-vs-NMF comparison uses identical dimensions and is unaffected, so the core results remain robust.)

- **AUROC mentioned but not reported.** The paper notes that "AUROC and AUPRC are also useful metrics" (Section 4.1) but only reports AUPRC in the hyperparameter sensitivity analysis, not in the main model comparison. AUROC is never presented. While the paper argues that precision@K is more practically relevant for recommendation tasks — a reasonable position — the omission of a complete set of standard metrics weakens the evidence somewhat.

### Trivial
None.

## Nice-to-Haves

- **Visualizations of the learned similarity matrix \(WW^\top\)**: A heatmap or nearest-neighbor analysis showing whether the learned coefficients group objects by ground-truth attributes would directly test the manifold-preserving claim.
- **t-SNE/PCA projections of embeddings** colored by attributes for qualitative assessment of clustering.
- **Hyperparameter search space for baselines** (NMF, HCCF, SLIM): the paper only reports sensitivity analysis for SMF.

## Removed Points

These points were raised in the reviews but are removed per the verification guidelines. They are included here for transparency in case they are useful.

1. **"No empirical support for manifold-preserving claim"** — The paper provides extensive empirical support in Section 4.2 (Z-scores, t-tests, Figure 3). This criticism is factually incorrect. The paper lacks *theoretical* justification but does provide empirical evidence.

2. **Criticism about missing appendix details** (computational time, number of iterations) — The paper references an appendix that exists in the original submission. Per guidelines, parser-stripped appendix content should not be treated as missing.

3. **"ModCloth precision@K dismissal is inconsistent with RMSE evaluation"** — There is no inconsistency. RMSE evaluates numerical reconstruction of held-out values; precision@K evaluates ranking of all items. The sparsity issue that makes precision@K uninformative does not affect RMSE in the same way.

4. **Criticism about AUPRC not being reported** — The paper uses AUPRC in the hyperparameter sensitivity analysis (Section 4.1) and explains why precision@K is the more relevant metric for the recommendation task (Section 5). The main claim about AUROC omission is retained as a minor weakness above.

## Novel Insights

The most interesting observation from the reviews is that SMF's embedding quality advantage is **most pronounced precisely where NMF struggles most** — on the Drug-SE ATC hierarchy, NMF achieves statistical significance in only 3–13 % of runs, while SMF achieves 100 %. This suggests the self-expressive mechanism may be particularly valuable when the latent structure is hierarchical or fine-grained, a hypothesis worth exploring in future work. Additionally, the fact that SMF outperforms NMF even when both use the same embedding dimensions (k=5–15) provides a cleaner signal that the improvement comes from the self-expressive constraint, not from model capacity.

## Suggestions

1. **Add a proper ablation study**: Train SMF with \(\lambda_{se}=0\) while keeping the \(P\) matrix weighting and elastic-net regularization identical to the full SMF. Report RMSE, precision@K, and Z-scores to isolate the contribution of the self-expressive term.
2. **Report runtime/convergence**: For at least one dataset, report the number of iterations to convergence and wall-clock time per iteration. This is essential for assessing practical applicability.
3. **Control for embedding dimension in the clustering evaluation**: Either run HCCF with the same small k as SMF/NMF, or run SMF/NMF with k=64, and compare Z-scores. This would address the potential confound in the cosine-similarity metric.
4. **Report AUROC for the main comparison** to complete the evaluation picture, even if precision@K is the primary metric.
5. **Analyze the learned \(WW^\top\) matrix**: Provide visualizations (heatmaps, sparsity patterns, nearest-neighbor relationships) to directly demonstrate whether the learned similarity structure aligns with ground-truth attributes.

## Score and Decision

The paper proposes a genuinely novel approach to jointly learning embeddings and similarities in matrix factorization, supported by strong and consistent empirical results across diverse real-world datasets. The embedding evaluation (Figure 3) is particularly compelling, showing that SMF reliably and substantially improves the encoding of unseen object attributes. However, the paper lacks a formal analysis of its central theoretical claim, omits a critical ablation study, and does not address the practical scalability of the \(O(n^2 m)\) algorithm. These weaknesses are real but addressable — they do not invalidate the core contribution but do reduce the overall strength of the submission.

**Score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>