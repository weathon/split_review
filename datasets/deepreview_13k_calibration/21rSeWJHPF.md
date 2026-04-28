# Balanced Ranking with Relative Centrality: A multi-core periphery perspective

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Ranking of vertices in a graph for different objectives is one of the most fundamental tasks in computer science. It is known that traditional ranking algorithms can generate unbalanced ranking when the graph has underlying communities, resulting in loss of information, polarised opinions, and reduced diversity (Celis, Straszak \& Vishnoi [ICALP 2018]).

In this paper, we focus on *unsupervised ranking* on graphs and observe that popular centrality measure based ranking algorithms such as PageRank may often generate unbalanced ranking here as well. We address this issue by coining a new approach, which we term *relative centrality*. Our approach is based on an iterative graph-dependent local normalization of the centrality score, which promotes balancedness while maintaining the validity of the ranking.

We further quantify reasons behind this unbalancedness of centrality measures on a novel structure that we propose is called multi-core-periphery with communities (MCPC). We also provide theoretical and extensive simulation support for our approach towards resolving the unbalancedness in MCPC.

Finally, we consider graph embeddings of $11$ single-cell datasets. We observe that top-ranked as per existing centrality measures are better separable into the ground truth communities. However, due to the unbalanced ranking, the top nodes often do not contain points from some communities. Here, our relative-centrality-based approach generates a ranking that provides a similar improvement in clusterability while providing significantly higher balancedness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is motivated by the observation that traditional ranking algorithms can produce unbalanced rankings, and it aims to promote balancedness in centrality estimation. It first defines the concept of relative centrality and then proposes an iterative, graph-dependent local normalization of the centrality score. Empirical studies are provided to demonstrate the effectiveness of the proposed concepts.

### Strengths
S1. The paper aims to promote balancedness in nodes’ centrality ranking, using community detection as a concrete application scenario. I find this focus interesting.

S2. The paper proposes a multi-core-periphery structure with communities (MCPC) to quantify unbalancedness in centrality measures.

### Weaknesses
W1. The illustrative example in Figure 3 is unclear to me. The blue nodes in Figure 3(a) have more in-neighbors in Figure 3(b), but the out-degrees of the in-neighbors are also larger than those in Figure 3(b). Can we trivially conclude that the blue nodes in Figure 3(b) have smaller PageRank scores than those in Figure 3(a)?

W2. Following W1, if the answer is no, the core idea of defining the MCPC structure requires further clarification. Otherwise, the advantages of MCMC over traditional centrality measures (e.g., PageRank) seem marginal.

W3. The paper does not theoretically demonstrate the superiority of clusters detected by the proposed method over previous approaches, which limits the paper’s contributions.

### Questions
Could you provide further clarifications on W1 and W2 listed above?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new approach for achieving balanced rankings in graphs that have community structures. It addresses the problem of unbalanced rankings produced by traditional centrality measures. The authors introduce a structural concept called Multi-Core Periphery with Communities (MCPC), which combines both community and core-periphery structures. They propose "relative centrality" and develop a ranking algorithm that produces more balanced results than common centrality methods. The paper includes a theoretical analysis of ranking imbalances with MCPC structure and shows how their relative centrality approach resolves this issue. The paper demonstrates that their method improves clustering accuracy while achieving greater ranking balance compared to existing methods.

### Strengths
1. The paper introduces the concept of "relative centrality" and proposes a new structural assumption called Multi-Core Periphery with Communities (MCPC), which combines community structure and core-periphery structure.

2. The paper provides theoretical analysis of their proposed methods, including proofs of unbalancedness with MCPC structure and how their relative centrality approach overcomes this issue.

3. The paper demonstrates the usefulness of their balanced ranking algorithm on real-world data, specifically in improving the inference of community structure in single-cell RNA sequencing data.

4. The authors compare their method against several popular centrality measures and provide extensive simulations on real-world datasets.

### Weaknesses
1. The paper focuses primarily on directed graphs, which may limit the applicability of the methods to certain types of networks.

2. While the authors mention some existing work on multi-core structures, they don't provide a comprehensive comparison with these methods.

3. The paper briefly addresses the computational complexity of M-Rank for k-regular directed graphs in Section 3.2, but lacks analysis for other approaches, such as N2-Rank and RN-Rank. Providing additional clarification or a more comprehensive complexity analysis, especially for larger or irregular graphs, would enhance the paper's practical relevance for large-scale network applications.

4. Although the authors tested their method on 11 diverse single-cell datasets, these datasets are relatively small—only the TM dataset reaches 54K data points, with others below 16K. The superior results on Onion approach on the TM dataset in Table 2 raise questions about the scalability of the MCPC method on larger datasets. Besides, the PR for Onion is higher (.98) than RN-Rank (.87), yet RN-Rank is incorrectly highlighted in bold, which should be corrected. Evaluating the method on more larger datasets (e.g., millions of data points) could strengthen the paper’s contribution.

5. While the PR scores are high for RN-Rank and N2-Rank, the Purity metric is consistently lower than traditional centrality measures across most datasets in Table 2. The paper would benefit from a more in-depth discussion of this trade-off between Preservation Ratio and Purity, including potential ways to improve Purity scores while maintaining a high Preservation Ratio.

### Questions
1. How does the computational complexity of the proposed relative centrality algorithms compare to traditional centrality measures?

2. Can the MCPC structure and relative centrality concepts be extended to undirected graphs or weighted networks?

3. How does the performance of the proposed methods change as the number of communities in the graph increases?

4. How does the proposed method handle dynamic or temporal networks where the structure may change over time?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper argues against global centrality measures such as PageRank for ranking nodes and suggests using relative centrality instead. As the name suggests, relative centrality measures centrality of a node relative to its neighborhood. The paper shows that relative centrality on Louvain community detection algorithm produces better clusters (as measured by preservation ratio of top 20% points and purity score).

### Strengths
The paper has a limitations section. Kudos to the authors for being honest about the technical limitations of their study.

### Weaknesses
 - I have no objection to adding another centrality measure to the long list of node centrality measures. However, the results would have been more convincing if the experiments had been conducted for recommender systems rather than for community detection.

- The authors may find these references related to their work:

Sotiris Tsioutsiouliklis, Evaggelia Pitoura, Panayiotis Tsaparas, Ilias Kleftakis, and Nikos Mamoulis. 2021. Fairness-Aware PageRank. In Proceedings of the Web Conference, pp. 3815–3826. https://doi.org/10.1145/3442381.3450065

Kijung Shin, Tina Eliassi-Rad, Christos Faloutsos. 2016. CoreScope: Graph Mining Using k-Core Analysis - Patterns, Anomalies and Algorithms. In Proceedings of the IEEE International Conference on Data Mining, pp. 469-478. https://ieeexplore.ieee.org/document/7837871

- The captions for Figures 10 to 20 should be more informative. As is, they only list the name of the dataset.

### Questions
Ranking is often used in recommender systems. The authors point this out in the first sentence of the introduction. Why did they not compare relative centrality for recommending nodes instead of using it for community detection?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the task of **unsupervised ranking on graphs** and aims to generate **balanced ranking**, where the top-ranked nodes contain a reasonable fraction of nodes from each community on the graph.

The authors propose a novel notion called **relative centrality**, which better preserves balancedness across different communities. Based on relative centrality, the authors propose several new approaches to iteratively update the centrality scores, which can be subsequently used for node ranking and graph clustering.

On the other hand, the authors propose a novel structural assumption for the underlying graphs, called **multi-core-periphery with communities (MCPC)**. Based on this, the authors define a stochastic block model and show that typical centralities are unbalanced under this model. Finally, experiments on 11 single-cell datasets are conducted to show that the proposed methods achieve higher balancedness while maintaining similar clustering quality.

### Strengths
1. The goal of computing balanced ranking for vertices on graphs is a meaningful and interesting problem.
2. The proposed assumption of multi-core-periphery structure is a natural combination of the community structure and the core-periphery structure, and the intuitions are conveyed nicely through Figures 2 and 3.
3. The proposed methods and conducted experiments are generally described in detail.

### Weaknesses
1. I am not sure if this work is interesting to the ICLR community. This paper deals with unsupervised ranking, which can be regarded as unsupervised learning, but it may not fall into the scope of "representation learning," which is "generally referred to as deep learning" as indicated on the official website of ICLR 2025. This paper may be more suitable for some venues on data mining or network science, for example.
2. The theoretical analysis seems limited and not supportive for the balancedness of the proposed methods. The analysis relies on several simplifications: for example, the number of underlying communities is $2$, the size of all the cores and peripheries are the same, and $t=1$ in Theorem 3.6. The authors do claim that the analysis can be extended, but do not provide further explanations. On the other hand, although Theorem 3.6 and Lemma A.7 verify that the relative centrality scores of core vertices are close to $1$ and larger than those of periphery vertices, this does not imply that the induced ranking is balanced, since the scores in one community may be all larger than those in other communities. The theoretical results do not provide a clear guarantee that the top-ranked nodes will contain a proportional representation from each community, which is the stated goal of the paper.
3. The paper is messy and needs significant improvement in presentation and layout. First, there lacks a detailed section on related work, making it hard to judge the contribution of this paper and its relevance to the ICLR community. Although Section 2.1 discusses some related work, it is brief and only concerns part of the contributions of the paper. Second, the text for the proposed assumption, methods, and analysis are not structured nicely, which is somewhat confusing. In particular, the order of the main text is not consistent with the contributions outlined in Section 1.1. Finally, there are numerous writing issues that affect the readability of the paper, as listed below.
4. Some background concepts are not explained clearly. For example, the meaning of the single-cell data, the metrics of NMI and purity, and the "onion" baseline are not introduced clearly enough. The paper assumes a level of familiarity with these concepts that may not be universal, particularly within the ICLR community. A more thorough explanation of these concepts is needed to make the paper accessible to a broader audience.
5. The experiments only focus on single-cell datasets, which is limited. More experiments on other types of networks (e.g., social networks) are expected, and the number of tested single-cell datasets can be reduced. The lack of diversity in the experimental data limits the generalizability of the findings and makes it difficult to assess the robustness of the proposed methods across different network structures.

Minor issues:

1. Most (if not all) citations in this paper should use `\citep{}` instead of `\cite{}`, so that the author names are placed in the parentheses. Also, the authors should cite the published version instead of the arXiv version of some papers.
2. Line 163: "community structure" -> "core-periphery structure".
3. Line 287: here the notation $k$ is ambiguous since it has a different meaning in Line 286.
4. Line 352: "$N_{G}(v_{j})$" -> "$N_{G}(v_{i})$". Also, here the term "neighborhood" should be specified as "in-neighborhood" or "out-neighborhood".
5. Line 762: "upper bounded" -> "lower bounded".
6. There are some grammatical issues or typos:
	1. Lines 22-23;
	2. Line 74: "for e.g.," -> "e.g.,";
	3. Line 130: "behind of" -> "behind";
	4. Line 180 and other occurrences: "w.r.t" -> "w.r.t.";
	5. Line 264: remove "is defined";
	6. Lines 419 and 1012: remove repetition of "look at";
	7. Line 463: remove "to";
	8. Lines 75 and 270: add space before left parentheses;
	9. Lines 192-193: the parentheses are not matched;
	10. the hyphens in compound words should be used correctly and consistently. For example, it should be "centrality-measure-based" in Line 17 and "Core-Periphery structure" in the caption of Figure 2(b).
7. I recommend to beautify the layout of the paper:
	1. the captions of Figure 4 are hard to read;
	2. the annotation in Lines 352-353 are separated across lines;
	3. Table 1 and Figure 5 are placed weirdly;
	4. there should be punctuations around multiline math expressions;
	5. math expressions are not aligned nicely, and the ones at the top of page 15 are aligned terribly;
	6. the font of notations in math expressions is inconsistent in many places (e.g., $k$, $\mathrm{deg}(\cdot)$, and $o(\cdot)$ in Lines 849-856);
	7. the text font changes in Lines 1332-1346.

### Questions
1. Could you provide more justifications for the relevance of this work to the ICLR community? For example, you can give some relevant papers published in ICLR or similar conferences/journals and add discussions to the paper.
2. The quantities in Table 1 are magical to me. Could you explain them?
3. Could you explain "single-cell RNA seq data" in more detail? Why do you focus on directed graphs as stated in Line 80? What about for undirected graphs?

### Soundness
2

### Presentation
3

### Contribution
3
