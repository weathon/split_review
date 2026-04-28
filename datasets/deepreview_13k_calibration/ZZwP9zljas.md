# Effects of Random Edge-Dropping on Over-Squashing in Graph Neural Networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Message Passing Neural Networks (MPNNs) are a class of Graph Neural Networks (GNNs) that leverage the graph topology to propagate messages across increasingly larger neighborhoods. The message-passing scheme leads to two distinct challenges: over-smoothing and over-squashing. While several algorithms, e.g. DropEdge and its variants – DropNode, DropAgg and DropGNN – have successfully addressed the over-smoothing problem, their impact on over-squashing remains largely unexplored. This represents a critical gap in the literature as failure to mitigate over-squashing would make these methods unsuitable for long-range tasks. In this work, we take the first step towards closing this gap by studying the aforementioned algorithms in the context of over-squashing. We present novel theoretical results that characterize the negative effects of DropEdge on sensitivity between distant nodes, suggesting its unsuitability for long-range tasks. Our findings are easily extended to its variants, allowing us to build a comprehensive understanding of how they affect over squashing. We evaluate these methods using real-world datasets, demonstrating their detrimental effects. Specifically, we show that while DropEdge-variants improve test-time performance in short-range tasks, they deteriorate performance in long-range ones. Our theory explains these results as follows: random edge-dropping lowers the effective receptive field of GNNs, which although beneficial for short-range tasks, misaligns the models on long-range ones. This forces the models to overfit to short-range artefacts in the training set, resulting in poor generalization. Our conclusions highlight the need to re-evaluate various methods designed for training deep GNNs, with a renewed focus on modelling long-range interactions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the effect that randomly dropping edges (in different ways) has on over-squashing and more broadly on the propagation of information. The conclusion is that techniques like DropEdge have a negative effect on the sensitivity between distant nodes, but possibly a positive effect on closer nodes. This is shown both mathematically and through experiments.

### Strengths
The paper is well presented and well written. There is a good amount of literature review and context provided as well. The authors study different scenarios and overall provide a pretty detailed mathematical understanding of the topic they wish to study.

### Weaknesses
I believe that the main weakness is that the core claim of the paper is not surprising. It is clear in general that removing edges will decrease the sensitivity. In fact, the converse is a motivation for graph rewiring techniques — adding the smallest amount of edges to maximise the propagation of information.

From another point of view, I believe that this trade-off is clear also when contrasting over-squashing and over-smoothing. A large spectral gap means better sensitivity, but also means more smoothing. For this reason,  removing edges (which will likely lower the spectral gap) will have the effect of combatting over-smoothing, by reducing the connectivity (meaning global sensitivity is lowered).

I do believe that the work is well-written and quite thorough. For this reason I do not wish to be overly negative in my initial scoring, although I would need to be convinced during the rebuttal phase on the strength of the contribution.

It is also worth pointing out that there already are a number of works [e.g. 1, 2] that link the trade offs between over-smoothing to over-squashing.

[1] Revisiting Over-smoothing and Over-squashing Using Ollivier-Ricci Curvature. ICML 2023
[2] On the Trade-off between Over-smoothing and Over-squashing in Deep Graph Neural Networks. CIKM 2023

### Questions
Related to the weakness, I would appreciate if the authors could comment on why they believe the main claim to be a surprise to readers working in related areas? 

Could the authors comment on how the findings are different from works such as [1, 2] that already comment on the trade-off between over-squashing and over-smoothing, especially [2] connecting it to spectral quantities (see my comment in the weaknesses section above on  spectral gaps).

[1] Revisiting Over-smoothing and Over-squashing Using Ollivier-Ricci Curvature. ICML 2023
[2] On the Trade-off between Over-smoothing and Over-squashing in Deep Graph Neural Networks. CIKM 2023

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the impact of random edge-dropping techniques on the issue of over-squashing in GNNs, specifically in the context of message-passing neural networks (MPNNs). While previous studies have explored edge-dropping methods to address over-smoothing, this paper highlights that these methods can exacerbate over-squashing, thus hindering GNNs’ performance on long-range tasks. Through theoretical analysis and empirical validation, the authors demonstrate that edge-dropping methods reduce the sensitivity of distant nodes to each other, leading to limited message-passing across long distances. The results suggest that while random edge-dropping methods like DropEdge improve performance in short-range tasks, they deteriorate performance in long-range tasks due to overfitting to local structures.

### Strengths
- This work provides a fresh perspective by focusing on over-squashing, a less-explored limitation of edge-dropping techniques in GNNs

- The paper presents a comprehensive theoretical framework, supported by experiments that confirm the detrimental impact of edge-dropping on long-range node interactions.

- The paper provides clear explanations showing how random edge-dropping improves accuracy in short-range tasks but worsens performance in long-range tasks.

### Weaknesses
 - While the paper identifies limitations of random edge-dropping methods—which are not specifically designed to address over-squashing—it lacks a proposed solution or guidance on mitigating over-squashing for these methods.

- The choice of datasets could be improved. It may be beneficial for the authors to follow the experimental setup outlined in [1].

- Some relevant works are omitted: (1) SkipNode [2], which selectively skips nodes at each layer, and (2) DropMessage [3], which introduces a generalizable framework for dropout-based techniques in GNNs.

- The source codes and the used dasets should be provided to facilitate the reproducibility of this work. Please refer to https://anonymous.4open.science.

### Questions
Please see the weaknesses listed above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the effects of random edge-dropping algorithms, such as DropEdge and its variants (DropNode, DropAgg, and DropGNN), on over-squashing in MPNNs. Over-squashing occurs when information from exponentially growing neighborhoods is compressed into finite-sized node representations, limiting the ability to capture long-range interactions.

### Strengths
1. This paper is well written and easy to follow.
2. The paper provides a comprehensive analysis of different types of MPNNs.

### Weaknesses
1. I do not find the main experiments of the paper convincing. The authors categorize the experimental results in Table 2 into homophilic datasets and heterophilic datasets to verify that the experimental results align with the theoretical results. In fact, I think that the magnitude of the Spearman correlation values in Table 2 depends on the optimal dropping probability for that dataset, rather than the homogeneity of the dataset. In other homophilic datasets, such as PubMed and ogbn-arxiv, the optimal dropping probability is quite small, and I do not think the same conclusions as those in the paper can be reached.
2. The conclusions described in Lemma 3.2 and Theorem 3.1 of the paper lack quantitative descriptions, which makes the conclusions less compelling. Additionally, the paper does not discuss potential solutions; it only analyzes this phenomenon, which limits the contribution of the work.
3. The paper only discusses DropEdge and its variants. In fact, for graph random dropping methods, Dropout [1,2] is the most commonly used, while DropMessage [3,4] is the most advanced. The lack of exploration of such non-edge dropping methods significantly limits the applicability of this work.
4. The experimental section of the paper is insufficient as it only includes a limited set of node classification tasks. Other downstream tasks, such as link prediction and graph classification, are missing experimental results.

### Questions
Please refer to the points I mentioned in the weakness section.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the effects of DropEdge and other variants on over-squashing problem, by calculating the sensitivity theoretically and emperically.

### Strengths
- The motivation is quite clear and solid. 
- Overall the writing is pretty good and understandable.
- The paper's logic is sound, and the assumptions are reasonable. 
- The empirical study on sensitivity is well-designed and makes great sense.
- The experiments on real world datasets align well with the theory and intuition.

### Weaknesses
 - The proof in appendix A1 is not quite clear. Maybe explain more.
- There are some datasets on long range interaction (LRI) and over-squashing, say trees match and peptides datasets. They are missing from the experiments. 
- The contribution of the paper is marginal. The mainstream of solving over-squashing is by graph rewiring or graph transformers. This paper addresses DropEdge and variants cannot solve over-squashing, that's fine, but empirically that is already true, and no one uses it for LRI.

### Questions
See weakness. Can you explain more the derivation in A1?

### Soundness
3

### Presentation
3

### Contribution
2
