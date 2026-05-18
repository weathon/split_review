Here is my consolidated review:

---

## Summary

The paper proposes the NetInfoF framework for measuring and exploiting "network usable information" (NUI) in node-attributed graphs. It introduces (1) a set of five derived node embeddings capturing structure, features, and propagated information; (2) a measurement score \(2^{-H(Y|X)}\) that lower-bounds accuracy and can be computed without model training; and (3) a compatibility matrix \(\mathbf{H}^*\) that adjusts node similarity for link prediction, handling both homophily and heterophily. The method achieves strong empirical results: winning 11/12 real-world link prediction datasets and all three OGB link prediction benchmarks, with linear scalability and far fewer parameters than GNN baselines.

## Strengths

- **Strong and comprehensive link prediction performance**: NetInfoF wins 11 of 12 real-world datasets (Table 2) and achieves the highest average rank against six GNN baselines spanning homophily and heterophily graphs. It also outperforms GCN, SAGE, and SlimG on all three OGB link prediction benchmarks (Table 3) while using only 1,280 parameters — 218× fewer than GCN/SAGE.

- **Only method robust across all six synthetic graph scenarios**: On a controlled taxonomy of 3 feature types (random/global/local) × 2 structure types (diagonal/off-diagonal), NetInfoF achieves average rank 1.0 while every baseline fails on at least one scenario (synthetic link prediction table). This provides rigorous evidence that the method does not rely on homophily assumptions.

- **Practical scalability**: Lemma 3 proves the model complexity is linear in \(|\mathcal{E}|\), and Figure 4 empirically confirms linear scaling on graphs up to millions of edges. Three speed-up techniques (warm start, coefficient selection, edge reduction) make the method practical for large graphs.

- **Ablation validates design choices**: The ablation study (Table 4) shows that both the compatibility matrix and the negative-edge optimization are individually necessary, with the full \(\mathbf{H}^*\) consistently outperforming ablated variants across all 12 datasets.

- **Closed-form compatibility matrix handling heterophily and negative edges**: Lemmas 1–2 provide exact solutions for the compatibility matrix, which rectifies the limitation of linear GNNs on link prediction. The interpretable structure (diagonal for homophily, off-diagonal for heterophily) is a practical advantage.

## Weaknesses

### Major

- **Significant gap between claimed "theoretical guarantee" and the actual contribution**: Theorems 1 and 2 are repeatedly advertised as a "theoretical guarantee" (abstract, introduction, conclusions, Table 1). In reality, Theorem 1 (\(2^{-H(Y)} \leq \max_y p_y\)) follows directly from \(H(Y) \geq -\log \max_y p_y\), and Theorem 2 is its conditional extension. Both are elementary consequences of the definition of entropy. While the *use* of these inequalities as a practical measurement tool has merit, the paper frames them as a key intellectual contribution, which is an overstatement. The "theoretical guarantee" label inflates what is a simple mathematical observation into a claimed structural advantage over other methods.

- **The measurement module does not answer the paper's central motivating question**: The paper opens by asking whether GNNs will perform better than MLPs on a given graph, yet (a) the NUI score measures information in the authors' own *derived embeddings*, not a method-agnostic quantity, and (b) the real-world experiments contain **no comparison to an MLP or feature-only baseline** at all. The paper compares only against other GNNs (GCN, SAGE, GAT, H²GCN, GPR-GNN, SlimG). Without a feature-only baseline, the reader cannot assess whether the method answers its motivating question. The score may be useful for practitioners deciding whether to train a GNN, but the paper does not demonstrate this use case.

- **Unremoved authorial annotations in the manuscript**: The abstract contains leftover editing notes: `\xiangsx{What are graph tasks? ...}`, `\james{... I cannot understand ...}`, and `\christos{YES! lets give our best few numbers!}` (lines 6, 8, 13, 18, 19). These are not parser artifacts; they are internal comments that were never removed. While this does not affect the science, it indicates the manuscript was submitted in an unfinished state and undermines confidence in the thoroughness of the work.

### Minor

- **Node classification results placed entirely in the appendix despite "general" being a headline advantage**: The paper lists "general" (handling both link prediction and node classification) as its first advertised advantage and describes the node classification method in Section 5. However, it explicitly states "the experiments for node classification are in Appendix [app:nc_real] because of space limit" (line 592). Given that generality across tasks is a primary claimed advantage, relegating all results to the appendix weakens the support for this claim in the main paper.

- **No analysis of failure cases or relative weaknesses**: The method loses on PubMed (GPR-GNN wins 66.3 vs. 59.7), and on some datasets the margins over baselines are modest. The paper does not analyze why the method underperforms on PubMed specifically, which would strengthen the contribution by revealing the method's limitations and guiding future work.

- **Lack of MLP / feature-only baseline**: As noted above, the complete absence of a simple MLP or logistic regression baseline (using only node features) from the main experiments means the paper cannot demonstrate whether adding graph structure through NetInfoF actually improves over a non-graph approach. This directly relates to the paper's framing and should be addressed.

### Trivial

- **The time complexity notation \(d^4|\mathcal{E}|\) in Lemma 3 suggests a quartic dependence on embedding dimension \(d\)** when in practice \(d\) is small (e.g., 128) and bounded. The paper should clarify that the complexity is effectively linear because \(d\) is a constant hyperparameter, and the \(d^4\) factor comes from the closed-form matrix operations, which dominate only for very large \(d\).

## Nice-to-Haves

- Include a summary table or figure of node classification results in the main paper (even one representative dataset per category) to directly support the "general" claim.
- Add a simple MLP or logistic regression baseline trained on node features alone, to contextualize whether and when the graph structure is actually helpful.

## Removed Points

These points were flagged but removed after verification against the paper:

- **"Synthetic experiments are crafted to favor the proposed method"** (Harsh Critic Issue 5): The synthetic experiments are a controlled validation covering all 6 scenarios in a systematic taxonomy. This is standard practice for sanity checks and does not constitute circular reasoning. The paper makes no claim that synthetic experiments replace real-world evaluation; they serve as controlled verification that the method works across diverse conditions.
- **"Hyperparameter details not in the main text"**: The paper references the appendix for these details. The instructions for this review stipulate that missing appendix content should not be penalized.
- **"Missing related works"**: As per review instructions, this cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension between the paper's substantive empirical contribution (a fast, interpretable, high-performing link prediction pipeline) and its inflated framing (claiming a "theoretical guarantee" and a tool that answers the GNN-vs-MLP question that it does not actually resolve). This gap between what the paper does well and what it claims to do is the central issue that any revision must address.

## Suggestions

1. **Tone down the theoretical claims substantially.** Move Theorems 1–2 to a brief background paragraph or appendix. Remove "theoretical guarantee" from the key advantages list. The method's practical strengths (speed, parameter efficiency, interpretability, strong empirical results) are sufficient grounds for the paper's contribution.
2. **Either add an MLP/feature-only baseline to the main experiments or reframe the motivating question.** If the paper cannot include a full baseline comparison, change the opening question from "will GNNs perform better than MLPs?" to "how much task-relevant information does this graph contain?" which the NUI score actually addresses.
3. **Remove all authorial annotations** (`\xiangsx{}`, `\james{}`, `\christos{}`) from the manuscript before resubmission. A clean manuscript is a basic expectation for publication.
4. **Move at least a summary of node classification results** (one table or concise paragraph) into the main paper, or downgrade the "general" claim to acknowledge that the primary focus is link prediction.
5. **Add a brief discussion of the PubMed failure case** to demonstrate understanding of the method's limitations and build credibility.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>