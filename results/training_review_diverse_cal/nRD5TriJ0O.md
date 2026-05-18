Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper studies active learning on heterophilic graphs, where standard graph active learning (GAL) methods designed for homophilic graphs fail. It identifies that previous GAL methods select isolated nodes whose induced subgraph misrepresents the true homophily distribution, and proposes the "Know Your Neighbors" (KyN) principle: label nodes together with their neighbors to give GNNs a correct view of the graph's homophily structure. KyN partitions the graph via METIS, represents each subgraph using a Jordan center plus neighbor-mean embedding, and samples subgraphs via ℓ₁ Lewis weights. The method shows strong empirical results across six heterophilic graph datasets and scales to graphs with millions of nodes.

## Strengths

- **Identifies and empirically demonstrates a genuine failure mode of prior GAL methods on heterophilic graphs.** Section 3.1 and Figure 2 show that previous GAL methods produce training sets whose local homophily distributions are left-skewed (homophilic-looking) on the heterophilic Roman-empire dataset, directly contradicting the ground-truth right-skewed distribution. Table 1 confirms these methods often fail to outperform random sampling, with gaps as large as 10.4% on Roman-empire and 5.6% on Minesweeper. This diagnosis is novel and well-supported.

- **Proposes an intuitive and effective principle ("Know Your Neighbors") that directly addresses the identified failure mode.** The observation that isolated labeled nodes produce artificially homophilic training subgraphs is clean and the solution — label entire subgraphs so every selected node has labeled neighbors — is conceptually simple yet empirically effective. Theorem 3.2 formally motivates why knowing more neighbors improves homophily estimation.

- **Comprehensive empirical validation across diverse heterophilic graphs and budgets.** KyN achieves the best accuracy on all six datasets across three labeling budgets (5C, 10C, 20C), with improvements of up to 12.1% over prior methods. Results are averaged over 10 runs with standard deviations reported. The method also works with heterophilic GNN backbones (FAGCN, M2M-GNN, Table 2) and scales to snap-patents (>2M nodes, Table 3), where prior methods time out.

- **Efficient runtime and robustness to the core hyperparameter.** Figure 4 shows KyN is an order of magnitude faster than FeatProp on Roman-empire and Amazon-ratings. Figure 5 demonstrates stable accuracy across a wide range of the number-of-groups hyperparameter c, with practical guidance for choosing c ≈ |V|/C.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical guarantee does not match the actual training procedure, creating a significant overclaim.** Theorem 3.6 proves a relative-error coreset guarantee for the loss function L(β) = −Σ_{i=1}^{c} ln p(y_i | R_{G_i}, β), which is a **subgraph-level** loss where each subgraph G_i contributes exactly one term with one label y_i. However, the actual GNN training performed in the experiments is **node-level** classification: every node in the selected subgraphs is labeled and contributes its own cross-entropy term, yielding many more loss terms than the number of sampled subgraphs. The paper never defines what y_i represents in the theorem (label of the Jordan center? majority label of the subgraph?) and never addresses the gap between the subgraph-level objective the theory covers and the node-level objective actually minimized during training. The abstract and conclusion repeatedly claim a "solid theoretical guarantee" for KyN, but this guarantee applies to a different problem than the one being solved. The paper should either (a) adapt the method so the training objective matches the theoretical one, (b) explicitly state that the theory applies to a simplified proxy and the full method is heuristic, or (c) provide a rigorous argument bridging the two objectives.

### Minor

- **Missing ablations to isolate the core "label subgraphs" insight from the auxiliary design choices.** The method has several components: METIS partitioning, Jordan-center representation, and Lewis weights sampling. The paper mentions "More detailed component analysis" (Section 5.2) but the actual ablation content does not appear in the extracted text (likely in the full paper). Crucially, the simplest baseline that tests the core principle — **random partition sampling with label-all** (i.e., randomly select a few METIS clusters and label every node in them) — is absent. Without this baseline, a skeptical reader cannot tell whether the primary performance gain comes from the "label entire subgraphs" insight (which could be implemented trivially) or from the Lewis weights sampling and Jordan-center representation specifically. Including this baseline would both strengthen and honestly bound the contribution.

- **Theorem 3.2 (Hoeffding bound for homophily estimation) is presented as a formal justification but provides no actionable guidance for the algorithm design.** The theorem states that labeling more neighbors of a node improves local homophily estimation — a property that follows directly from Hoeffding's inequality and does not connect to the specific choices in KyN (METIS partitioning, Jordan-center representation, or Lewis weights). The paper does not derive a required number of neighbors, a stopping criterion, or any design consequence from the bound. This is a minor overreach rather than a flaw, since heuristic motivation is common, but the paper's framing of it as a "theoretical justification" oversells the bound's role.

- **The analysis of why prior GALs fail could be sharpened.** Section 3.1 shows that prior GAL-selected training sets have homophilic local homophily distributions. The paper attributes this to isolated nodes (where the node itself is the only labeled neighbor, forcing h_t=1). However, it does not test whether the selected nodes might also *inherently* have homophilic neighborhoods (i.e., the nodes themselves tend to be in same-label dense regions). A simple control — labeling the immediate neighbors of GAL-selected nodes and recomputing the distribution — would distinguish these two mechanisms. The current analysis is still valid but would be stronger with this dissection.

### Trivial

- The paper states that "the results are similar on any multi-layer linear GNNs" without support; this claim is too broad for a single experiment with a one-layer encoder.
- The runtime comparison (Figure 4) reports end-to-end time but does not break down how much is spent on METIS partitioning, Lewis weight computation, and GNN training, which would help practitioners understand scalability to larger graphs.

## Nice-to-Haves

- Include a "prior GAL method + label neighbors" baseline: take an existing GAL (e.g., AGE or FeatProp), then additionally label the one-hop neighbors of each selected node. This would directly test whether the "know your neighbors" principle can be retrofitted onto existing methods, clarifying whether the contribution is the principle itself or KyN's specific sampling mechanism.
- Provide an explicit derivation or citation explaining how the multi-class cross-entropy loss is cast as a (1, ln2, ln2)-nice hinge function (Definition 3.5 operates on a single scalar, while CE operates on a logit vector). This is currently claimed without support and would help readers evaluate the theoretical contribution.

## Removed Points

These points were raised by reviewers but do not hold up against the actual paper or are excluded per review guidelines.

- **Criticism about CE as nice hinge function being unsubstantiated (removed per Hard Rules):** The paper states "We reformulate the CE loss to show it is also a (1, ln2, ln2)-nice hinge function." If this reformulation was presented in the appendix (stripped by the parser), the criticism amounts to missing appendix content, which per guidelines should be removed. The underlying concern is legitimate but cannot be adjudicated from the extracted text alone.
- **Proposition 3.1 direction criticism (removed as factually incorrect):** The reviewer claimed the inequality shows D is a consequence of high accuracy rather than a necessity condition. The inequality D ≤ (1/n)Σ(1−Acc_i) + (1−Acc) correctly gives the contrapositive: if D is large, accuracy is bounded away from 1 (since RHS must be large). This is the standard mathematical meaning of necessity. The paper's interpretation is correct.
- **GraphPart similarity as a weakness (removed as inflated):** KyN differs from GraphPart in multiple substantial ways (Jordan-center representation, Lewis weight sampling vs. FeatProp within partitions), which the reviewer acknowledges. The claim that improvements are "modest" is not supported by the reported results (up to 12.1% on Roman-empire; even the smallest improvement of 1.9% is meaningful for active learning). The conceptual similarity of "partition then sample" does not make the methods equivalent.
- **Missing related works (removed per guidelines):** The reviewer did not specifically mention missing related works, but per guidelines, I do not have external sources to confirm such omissions.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a key meta-insight: the paper's core contribution — recognizing that isolated labeled nodes distort homophily perception in heterophilic GAL — is practically separable from its specific implementation. The strongest version of this paper would first establish that any method that labels entire subgraphs outperforms prior GAL (via a simple random-partition baseline), then layer the Lewis weights sampling on top. This would cleanly separate the conceptual contribution (the "know your neighbors" principle) from the algorithmic contribution (Lewis-weighted subgraph sampling), making both easier to evaluate. The current paper conflates these two layers, and the theoretical analysis adds confusion rather than clarity because it addresses a different loss than the one optimized.

## Suggestions

1. **Either fix the theory or honestly caveat it.** The most impactful change would be to restructure Section 3.3 to clearly state: "The coreset guarantee applies to a subgraph-level classification loss L(β) = −Σ ln p(y_i|R_{G_i}, β) where y_i is the label of the Jordan center node; in practice we train a node-level classifier on all nodes within selected subgraphs, which is a related but distinct objective. The theoretical analysis provides principled motivation but the full method's effectiveness is evaluated empirically." This honesty would not diminish the empirical contribution, which is strong enough to stand alone.

2. **Add the random-partition label-all baseline.** This is the single most informative ablation: randomly sample k METIS clusters and label all nodes in them. If this baseline performs near KyN, the main contribution is the "label subgraphs" insight rather than the Lewis weights. If it performs substantially worse, the Lewis weights are validated. Either outcome is informative.

3. **Clarify what y_i represents in Theorem 3.6** and acknowledge the gap between the subgraph-level coreset objective and the node-level training objective. Even a brief paragraph explaining the relationship would resolve the current ambiguity.

4. **Break down the runtime** into METIS partitioning, Lewis weight computation, and GNN training components so practitioners can assess scalability for their use case.

## Score and Decision

This paper identifies a genuine and previously overlooked problem (active learning on heterophilic graphs), provides an insightful diagnosis of why prior methods fail, and proposes an effective empirical solution. The empirical results are strong and consistently demonstrated across multiple datasets, budgets, and backbones. However, the paper significantly overclaims its theoretical contribution: the advertised "solid theoretical guarantee" applies to a subgraph-level loss that does not match the node-level training actually performed, and the paper never acknowledges this gap. The missing ablation baseline (random partition sampling) makes it difficult to assess which component drives the gains. These are addressable issues — the core idea is sound — but they prevent acceptance in the current form.

**Score:** 5.5  
**Decision:** Reject (borderline; the core idea is promising and the empirical results are strong, but the theoretical overclaim and missing ablations require substantial revision)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>