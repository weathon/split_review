- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

Mirage proposes a model-agnostic graph distillation method for graph classification. Instead of the gradient-matching paradigm used by existing methods (DosCond, KIDD), Mirage decomposes each graph into computation trees (the local rooted trees an L-layer MP-GNN sees), mines frequently co-occurring tree sets using FPGrowth, and trains GNNs directly on sampled tree-set batches. The key insight is that computation tree frequency distributions are highly skewed (power-law), so a small collection of frequent co-occurring trees can serve as an effective surrogate training set. The method requires no training on the full dataset and is independent of GNN architecture (tested on GCN, GAT, GIN) and hyperparameters.

## Strengths

1. **Genuinely novel, principled approach to graph distillation.** Existing distillation methods (DosCond, KIDD) are all gradient-matching approaches that require training on the full dataset and are architecture-specific. Mirage's shift to compressing the computation data itself — via frequent co-occurring computation tree mining — is a fundamentally different and well-motivated paradigm. Section 4.1–4.3 carefully justifies the approach from message-passing principles.

2. **First architecture-agnostic graph distillation validated across multiple GNN families.** Table 3 evaluates Mirage on GAT, GCN, and GIN — 17 dataset–architecture combinations — while prior work DosCond and KIDD only evaluate on a single architecture. This is a direct empirical demonstration of the claimed model-agnostic property.

3. **Consistent top-1 or top-2 performance across all 17 settings.** In Table 3, Mirage achieves the highest number of top-1 wins (8 of 17) and never falls below second place in any combination. This is achieved alongside the strongest compression (4–5× smaller than DosCond/KIDD on average, Table 4) and dramatically faster distillation (~150× vs DosCond, ~500× vs KIDD, Figure 2), all on CPU.

4. **Credible handling of the Random(sum) phenomenon.** The paper identifies that Random(sum) (random graph selection + sum pooling) can be surprisingly strong, explains the mechanism (sum pooling preserves differences in node/label counts between classes), and includes it as a baseline — an improvement over prior work that only reported the weaker Random(mean). The paper's own results still dominate Random(sum) overall.

5. **Empirical evidence for the skewed distribution motivating the approach.** Figure 1 (powerlaw) provides direct evidence that computation tree frequency distributions follow a power law across datasets, supporting the core premise. Section 5.4 further provides a sufficiency experiment showing loss convergence between full-dataset and distilled training.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained duplicate table with inconsistent numerical values.** Lines 498–526 contain a second full-results table (without caption or explanation) that reports substantially different values for key entries compared to the main Table 3. For example, on ogbg-molhiv the Full Dataset AUC-ROC values differ dramatically:
   - Main table: GAT=73.71, GCN=75.93, GIN=78.66
   - Duplicate table: GAT=66.34, GCN=64.78, GIN=65.13
   Mirage's own numbers also differ (e.g., DD GAT: 76.08±0.63 in main vs 72.96±2.78 in duplicate). This is a serious inconsistency that must be resolved — it is unclear which set of results is authoritative, and the presence of two different full-dataset baselines for the same dataset undermines trust in either table.

2. **Training procedure with tree sets is underspecified.** Section 4.4 states that the GNN is trained on sampled "frequent tree sets" rather than graphs, using the Combine function on root embeddings. However, the paper does not specify: how batches are constructed from tree sets, whether the GNN architecture is modified to accept tree-set inputs (and if so, how), what batch sizes are used, or how the Combine function is applied in practice (does it replace the graph-level readout?). Algorithm alg:dd_training is referenced but appears only in the stripped appendix. Without these details, the training protocol cannot be reproduced, and it is unclear whether the comparison to baselines training on full graphs is "apples-to-apples" in terms of the learning procedure.

3. **Values of the frequency threshold θ are not reported.** The threshold θ directly controls the size and content of the distilled dataset (Section 4.3). The paper states θ "may be selected based on the desired distillation size" but never reports the values used for any dataset. This is a critical hyperparameter for reproducibility and for understanding the trade-off between compression and accuracy.

### Minor

4. **Ablation isolating the mining component is missing.** The comparison against Random(sum) selects random *graphs*, not random *tree patterns*. A baseline that selects random tree patterns (instead of frequent co-occurring ones) would directly measure whether the FPGrowth mining step adds value beyond the tree decomposition itself. Without this, it is unclear whether the performance is driven by the mining or simply by the tree representation.

5. **KIDD is evaluated on non-GIN architectures outside its intended setting.** The paper acknowledges (Section 5.2) that KIDD only supports GIN, and for GAT/GCN experiments KIDD's GIN-distilled dataset is reused. This handicaps KIDD in those settings. The results are still informative but should be interpreted with this caveat, and the paper could have noted this more prominently when drawing comparisons.

6. **Sufficiency experiment (Section 5.4) partially addresses from-scratch training but only on one dataset (ogbg-molhiv, Figure 6b).** The main frozen-model experiment (Figure 6a) measures whether a *pre-trained* model's loss on tree patterns matches its loss on full data, which does not directly demonstrate that training from scratch on tree patterns alone converges to the same accuracy. The paper includes one from-scratch loss curve for ogbg-molhiv, which helps, but this should be extended to more datasets.

### Trivial

7. The claim that Mirage is "more than 30 times faster on average" than full-dataset training references a table (tbl:fulltraintime) that does not appear in the extracted paper. While this may be in a stripped appendix, the claim is unsubstantiated in the main text.

## Nice-to-Haves
- A sensitivity analysis of the θ threshold across datasets would strengthen the paper's understanding of the compression–accuracy trade-off.
- Reporting confidence intervals via bootstrapping on the accuracy results (instead of only standard deviations) would strengthen the statistical claims.
- A discussion of how the tree-set sampling probability (proportional to frequency) interacts with class balance would be helpful.

## Removed Points

These points from the reviews were removed; they are listed here for reference only and should not be weighted in the evaluation.

- **"Output of distillation not clearly defined / comparison to baselines invalid"** (Harsh Critic): The paper defines the answer set in Problem 2 (Eq. 14) and describes its use in Section 4.4. The distilled output is a collection of frequent tree sets, which is a different *kind* of distilled data than synthetic graphs — but the accuracy comparison is still valid (both produce a representation used to train a GNN classifier) and the byte-size comparison is legitimate (both measure storage footprint). The claim of "invalid comparison" is an overstatement; the issue is one of underspecification, not invalidity.

- **"Sufficiency experiment is fundamentally flawed"** (Harsh Critic): The paper's Sufficiency section (5.4) includes both a frozen-model experiment AND a from-scratch training comparison on ogbg-molhiv (Figure 6b). The critic's claim that the paper lacks a from-scratch comparison is incorrect.

- **"Paper overstates full-dataset training as a fatal flaw of existing methods"** (Harsh Critic): This is a subjective judgment about presentation, not a technical weakness. The paper's characterization is a reasonable critique of the gradient-matching paradigm.

- **"Time complexity not empirically validated"** (Harsh Critic): Minor nitpick; the time comparison against baselines (Figure 2) provides sufficient empirical validation of efficiency.

- **"Missing related works"** (implied): Per instructions, I cannot comment on missing related works without external confirmation.

- **Pure formatting/style nitpicks** (various): Removed per instructions.

- **Generic strengths about "importance of the problem"** (Strength Finder): Removed — these are superficial and sycophantic without specific evidence.

## Novel Insights

The most interesting observation that emerges from reading the two reviews together is the *tension between novelty and specificity*. The harsh critic identifies genuine underspecification in how the distilled tree sets are used for training, but simultaneously the strength finder recognizes that this underspecification is a natural consequence of the method's novelty — there is no established template for "training on frequent co-occurring tree sets" that the authors could have followed. The more interesting question (not raised by either reviewer) is whether the Combine function applied to tree root embeddings (as a stand-in for graph-level readout) changes the effective hypothesis class the GNN is optimizing over, and whether this could explain both Mirage's strong performance and the surprising competitiveness of Random(sum). If the tree-set aggregation acts similarly to a learned pooling kernel, the mining step may matter less than the representation itself — a hypothesis the authors could test by comparing tree-set training against standard graph training on the same architecture.

## Suggestions

1. **Resolve the duplicate table inconsistency.** Clarify which table is the correct set of results, explain what the second table represents (e.g., a different experimental condition, an older ablation), or remove it entirely.
2. **Provide a complete specification of the training procedure with tree sets.** Either include Algorithm alg:dd_training in the main paper (perhaps in a short form) or provide pseudo-code describing how tree sets are batched, how the Combine function is applied, and how the GNN's readout is modified.
3. **Report the θ values used per dataset** in the experimental setup, and ideally include a sensitivity analysis.
4. **Add an ablation comparing frequent tree patterns to randomly selected tree patterns** (matched for set size) to directly isolate the contribution of the mining step.
5. **Extend the from-scratch sufficiency comparison to additional datasets** beyond ogbg-molhiv.
