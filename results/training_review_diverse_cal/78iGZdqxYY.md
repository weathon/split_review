Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes Mirage, a model-agnostic graph distillation algorithm for graph classification. The key insight is that message-passing GNNs decompose graphs into computation trees, and these trees often follow a skewed (power-law) frequency distribution. Mirage exploits this by mining frequently co-occurring computation tree patterns (itemsets) and training the GNN on these patterns rather than on the full graph dataset. This avoids the need to train a model on the full data during distillation (a limitation of prior gradient-matching approaches) and makes the distilled dataset independent of the target GNN architecture and hyperparameters.

## Strengths

- **Model-agnostic distillation that avoids full-dataset training:** Unlike existing gradient-matching methods (DosCond, KIDD) that require training a GNN on the original data to extract gradients, Mirage distills the dataset by mining frequent computation trees using only the data itself. The entire pipeline is CPU-bound and architecture-independent, directly addressing the "counter-objective design" limitation of prior works (Sections 1.2, 3.2–3.3).

- **Consistent top-2 ranking across diverse datasets and architectures:** In Table 1, Mirage achieves either best or second-best AUC-ROC in all 17 dataset–architecture combinations (8 first-place finishes), spanning GCN, GAT, and GIN across molecular, protein, and social network domains. This is the highest number of top rankings among all baselines, demonstrating that being unsupervised to original training gradients does not hurt accuracy.

- **Simultaneous compression and efficiency advantages:** Table 2 shows Mirage achieves the highest compression in 5 of 7 datasets, with average compression ≈4× better than DosCond and ≈5× better than KIDD. Figure 1 documents that Mirage is ≈150× faster than DosCond and ≈500× faster than KIDD, despite using only CPU instead of GPU. This triple advantage (accuracy, compression, speed) is a clear core strength.

- **Power-law distribution insight with empirical validation:** The paper identifies and visualizes the skewed frequency distribution of computation trees (Figure 2), noting that in ogbg-molhiv the most frequent tree alone has normalized frequency 0.32. This observation is the foundation of the distillation strategy and is shown to hold across multiple real-world datasets.

- **Sufficiency experiment demonstrating information retention:** Figure 3 shows that when model weights from full-dataset training are frozen, the loss difference between running the model on Mirage's distilled set and on the full set rapidly approaches zero. This empirically demonstrates that the frequent tree patterns capture the essential characteristics needed for learning.

## Weaknesses

### Fatal

None. The first reviewer's central claim — that the training procedure is unspecified — is inaccurate. Section 3.4 (lines 323–324) clearly states: each frequent tree set serves as a surrogate for a graph; the GNN computes root embeddings of each tree via message passing (per Observation 1, the representation of a node can be computed from its computation tree); these root embeddings are combined using the graph-level Combine function (Eq. 4). The reviewer's questions about "how trees are assembled into an input graph" reflect a misreading — they are not assembled; trees are processed individually by the GNN and their root embeddings are pooled. The description, while concise, is conceptually complete.

### Major

None. The paper's claims are well-supported by the experiments. The weaknesses below are refinements, not structural flaws.

### Minor

- **Frequency threshold θ not reported for individual datasets:** The paper defines θ (Section 3.5) and notes it controls distilled dataset size, but does not report which specific θ values were used for each dataset in the experiments. Since compression ratio is a headline result, the absence of this information and the lack of a sensitivity analysis (accuracy vs. distilled size as θ varies) makes it difficult to assess how sensitive the reported compression advantage is to this parameter choice.

- **Multi-class AUC-ROC for IMDB-M not clarified:** IMDB-M has three classes, but AUC-ROC is conventionally defined for binary classification. The paper reports AUC-ROC for this dataset without specifying whether one-vs-rest macro-averaging or another multi-class extension was used. This should be clarified for reproducibility.

- **KIDD evaluation on non-GIN architectures:** As the paper acknowledges (Section 4.2), KIDD only supports GIN, so evaluations on GAT and GCN use KIDD's GIN-distilled data. This is noted but not discussed as a potential disadvantage for KIDD that could inflate Mirage's relative advantage on non-GIN architectures. Mentioning this caveat explicitly would improve fairness of the comparison.

- **Algorithm reference in omitted appendix:** The main text (line 324) references Algorithm alg:dd_training without providing its content. While the narrative description is sufficient for understanding, including a concise pseudocode sketch in the main text would improve clarity and self-containedness.

### Trivial

- **Computation tree size distribution:** The paper analyzes complexity as O(z × δ^L) and notes L ≤ 3 is typical, but does not provide empirical verification of actual tree sizes or the time spent on decomposition. A brief empirical note would strengthen the efficiency claims.

## Nice-to-Haves

- Reporting the *number of training examples* (frequent itemsets vs. synthetic graphs) produced by each method, in addition to byte-size compression, would allow readers to compare training budgets more directly.
- A sensitivity analysis for θ (compression ratio vs. accuracy trade-off) across one or two datasets would place the reported compression advantage on firmer ground.
- Clarifying whether the frequent tree sets are mined separately per class (the text implies this with "We mine the frequently co-occurring trees from each class separately") would remove any ambiguity.

## Removed Points

- **"Unclear and potentially flawed training procedure" as a fatal weakness:** The harsh critic claimed the training procedure is unspecified and that this undermines the paper. This is incorrect — Section 3.4 clearly describes sampling tree sets, computing root embeddings per tree, and combining them via the graph-level Combine function. The description is sufficient. This point is removed as it misunderstands the paper.

- **"Not apples-to-apples byte comparison":** The critic claimed that because Mirage's distilled data is a set of tree patterns rather than synthetic graphs, the byte comparison may not be fair. This is not a valid concern — byte size is a direct measure of storage cost regardless of data format, and is the standard metric used across distillation literature. Removed.

- **"Missing appendix/algorithm pseudocode" as a fatal weakness:** The critic treated the absence of the algorithm from the main text (it is in the appendix) as a critical gap. The parser strips appendix content; the narrative description in the main text (Section 3.4) is sufficient for understanding the method. This is at most a minor clarity suggestion.

## Novel Insights

The most interesting observation emerging from this review is that the paper's core advantage — being unsupervised to training gradients — is simultaneously its strongest selling point and the source of its most interesting limitation. The sufficiency experiment (Figure 3) demonstrates that frequent tree patterns retain enough information to drive the loss to near-zero when the full-dataset weights are frozen; but this does not automatically guarantee that training from scratch on these patterns will recover the same decision boundary. The fact that Mirage nonetheless achieves competitive accuracy (Table 1) suggests that the inductive bias of message-passing GNNs aligns naturally with the frequency-skew of computation trees — an alignment that is not theoretically guaranteed and deserves deeper investigation. A second insight: the surprisingly strong performance of the Random(sum) baseline (Table 1) reveals that the choice of graph-level pool function interacts non-trivially with distillation, and that SumPool may preserve discriminative node-count information that MeanPool washes out. This is a finding the paper itself identifies but does not fully exploit in its design.

## Suggestions

1. Report the specific θ values used for each dataset and include a brief sensitivity analysis (accuracy vs. compressed size) for at least one dataset.
2. Clarify the multi-class AUC-ROC metric used for IMDB-M (one-vs-rest macro-averaging or similar).
3. Add a concise pseudocode sketch of the training loop in the main text (or in a clearly marked public repository if page limits are strict).
4. Discuss the caveat that KIDD results on non-GIN architectures use GIN-distilled data as a limitation, not just a procedural note.

## Score and Decision

The paper presents a genuinely novel approach to graph distillation with a well-motivated idea, solid empirical validation across multiple architectures and datasets, and significant practical advantages in compression and efficiency. The weaknesses are minor and addressable. The contribution is timely and the paper is clearly written.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>