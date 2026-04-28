# Understanding When and Why Graph Attention Mechanisms Work via Node Classification

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 3

## Abstract
Despite the growing popularity of graph attention mechanisms, their theoretical understanding remains limited. This paper aims to explore the conditions under which these mechanisms are effective in node classification tasks through the lens of Contextual Stochastic Block Models (CSBMs). Our theoretical analysis reveals that incorporating graph attention mechanisms is *not universally beneficial*. Specifically, by appropriately defining *structural noise* and *feature noise* in graphs, we show that graph attention mechanisms can enhance classification performance when structural noise exceeds feature noise. Conversely, when feature noise predominates, simpler graph convolution operations are more effective. Furthermore, we examine the over-smoothing phenomenon and show that, in the high signal-to-noise ratio (SNR) regime, graph convolutional networks suffer from over-smoothing, whereas graph attention mechanisms can effectively resolve this issue. Building on these insights, we propose a novel multi-layer Graph Attention Network (GAT) architecture that significantly outperforms single-layer GATs in achieving *perfect node classification* in CSBMs, relaxing the SNR requirement from $ \omega(\sqrt{\log n}) $ to $ \omega(\sqrt{\log n} / \sqrt[3]{n}) $. To our knowledge, this is the first study to delineate the conditions for perfect node classification using multi-layer GATs. Our theoretical contributions are corroborated by extensive experiments on both synthetic and real-world datasets, highlighting the practical implications of our findings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper provides a theoretical study of graph attention mechanisms (GATs) through the lens of Contextual Stochastic Block Model (CSBM) on node classification tasks. It presents an analysis of when structure noise outweighs feature noise, graph attention mechanisms offer an advantage over simple graph convolutional operations. Additionally, the paper explores well-known over-smoothing problem and demonstrates that multi-layer GATs can mitigate this problem under certain condition related to signal-to-noise ratio (SNR). Lastly, the authors proposes a multi-layer GAT architecture that achieves better performance of perfect node classification with relaxed SNR requirement

### Strengths
The paper investigates when graph attention mechanisms (GATs) outperform simpler graph convolutional networks (GCNs) in node classification tasks by analyzing the balance between two types of noise: structure noise and feature noise. Specifically, the authors identify that GATs are beneficial when structure noise is higher than feature noise. It, to certain extend, provides an actionable rule-of-thumb that the decision to use GATs or GCNs should be informed by the relative levels of structure and feature noise in the graph data. 

The paper explores the over-smoothing problem, a well-known challenge in graph neural networks (GNNs) where increasing the network depth leads to node representations becoming indistinguishable. It provides a refined definition of over-smoothing in GNNs, incorporating a formal measure of node similarity. The authors argue that GATs can mitigate over-smoothing, especially in high signal-to-noise ratio (SNR) scenarios. This structured approach to studying over-smoothing adds to the understanding of how attention-based models can maintain informative node representations over deeper layers. The paper also presents a synthetic experiment regarding the claim

### Weaknesses
Much of the paper builds directly on the study by Fountoulakis et al. (2023), which also analyzed graph attention mechanisms in noisy settings. While the paper provides an extension to multi-layer GATs and refines SNR requirements, these contributions are largely incremental and do not significantly advance the foundational insights established in previous work. The core idea of analyzing the interplay between structure and feature noise, and its impact on GAT performance, is already present in the prior work, making the novelty of this paper somewhat limited.

The paper’s reliance on the Contextual Stochastic Block Model (CSBM) framework and assumptions limits its applicability to real-world graphs, which often have more complex and varied structures. The CSBM, while useful for theoretical analysis, makes strong assumptions about the graph's community structure and the distribution of node features. This strong dependence on CSBM makes it challenging to generalize the findings to other types of graph data, reducing the paper's practical value. For example, real-world graphs often exhibit power-law degree distributions and heterophily, which are not captured by the basic CSBM model used in this paper.

The experimental section is relatively narrow, relying heavily on synthetic data generated from CSBMs and only including three standard, small real-world datasets (Cora, Citeseer, and Pubmed). The lack of diverse and larger datasets limits the empirical validation of the findings and raises questions about their robustness in more complex, real-world settings. The chosen datasets are also relatively old and may not reflect the challenges posed by modern graph datasets. Furthermore, the experiments do not explore the sensitivity of the results to variations in CSBM parameters or different noise models, which would be crucial for assessing the robustness of the theoretical claims.

### Questions
Given that graph attention mechanisms (GATs) are no longer state-of-the-art in graph deep learning, how do you see the practical relevance of your findings for more recent models, such as Graph Transformers or advanced message-passing networks? Could your theoretical insights be extended or adapted to these contemporary architectures?

How would you suggest practitioners apply your findings in real-world scenarios, where graphs often do not conform to CSBM and the noise characteristics may be less controlled or well-defined? Are there specific graph properties or types of datasets where your approach would be most applicable?

Perfect node classification, as discussed in your paper, is a rigorous but often impractical benchmark since real-world graph data rarely allow for flawless classification, especially in noisy settings. Could you clarify how your findings on perfect node classification translate to more realistic, imperfect classification tasks? Are there insights from your work that could help improve performance on standard metrics used in practical graph learning applications?

The experimental section primarily focuses on synthetic CSBM data and three small real-world datasets. Given the assumptions in your theoretical analysis, have you considered evaluating your approach on larger and more complex datasets or on datasets with varied noise characteristics? How do you anticipate your findings will generalize to such settings?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies properties of graph attention mechanisms in the context of node classification in the contextual stochastic block model (CSBM). The authors derive several theoretical results. First, when compared with the simple graph convolution operation, graph attention can either be beneficial or not beneficial, depending on the level of structure noise in the graph and the level of feature noise in node features. This complements prior study of graph attention in a similar setting. Second, under assumptions of sufficiently small feature noise and sufficiently dense graph connectivity, the authors show that graph attention can effectively avoid the issue of over-smoothing, up to order n layers where n is the number of nodes in the graph. Third, the authors show that a multi-layer graph attention network can achieve perfect node classification, up to a signal threshold that is much smaller than what is required by a single-layer graph attention network. The authors empirically valid their theoretical claims over both synthetic data and semi-synthetic data (i.e. real-world networks with synthetic node features).

### Strengths
- The paper is reasonably well-written and easy to follow.
- The results in this paper extend our understanding of graph attention to multi-layer settings. In particular, the separation between simple graph convolution and graph attention in terms of over-smoothing is intuitive and interesting.

### Weaknesses
 - Given prior work on the analysis of single-layer graph attention [1] and the combination of simple graph convolution with graph attention in a multi-layer architecture [2], the current work does not offer a strikingly new perspective. The technical results are not surprising.

- The assumptions on p, q, SNR are kind of strong. For example, Assumption 1 requires both p and q to be log^2 n / n. There are also gaps in SNR in Corollary 1. I understand that prior work also rely on similar assumptions. This paper does not offer an improvement in terms of the parameter regimes (i.e., ranges of p, q, and SNR) required to analyze graph attention.

- The authors should cite [2] and compare with the results in [2] both theoretically and empirically. In [2], a combination of GCN and GAT is proposed and the authors show that the required SNR to achieve perfect node classification in CSBM can be significantly reduced. It seems that if one assumes both p and q are constants, then Corollary 2 in [2] is much stronger than Theorem 4 in this paper. The authors should discuss this.

- Minor:
  - Line 57, CSBM has been used as a data model analyze the performance of various GNNs, I believe that this is mostly due to the simplicity of CSBM. I don't think I should agree with the claim that CSBM is "a powerful tool ... to model real graph data". The authors should either revise this claim or provide justifications for such a claim.
  - Line 148, the authors use one-dimensional features throughout this paper. They should comment here if and how their results generalize to higher-dimensional features.
  - Line 226, I don't think Assumption 1 covers most practical graph data. On the contrary, a lot of graph data in practice are sparse and may not even be homophilic. I would suggest the authors change the word "most" to "many" at the minimum, and provide some context.
  - Line 317, and line 327, typo: F_noise and S_noise should be swapped.
  - Line 493, the authors used t = [0, 0.5, 0.5, 5] for GAT*. This is different from what is considered in Appendix J, where the first L layers have t = 0. The authors should explain why t = 0.5 was chosen for both the 2nd and the 3rd layers.

### Questions
Please see my comments above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper analyzes the graph attention mechanism by CSBMs, revealing that graph attention mechanisms can enhance classification performance when structure noise exceeds feature noise. Conversely, simpler graph convolution operations are more effective when feature noise predominates. Then, the authors design a new GAT that outperforms traditional GAT.

### Strengths
***Strengths***
- The paper is theoretically sound.

- The proposed method is easy to follow.

### Weaknesses
 ***Weaknesses***

- The main finding—that GAT performs better with higher structural noise and fails with predominant feature noise—seems intuitive. Recent research on graph heterophily also indicates that when structure is heterophilic (i.e., noisy as described here), GAT models tend to fail.

- The paper analysis is based on artificially generated datasets, how to judge whether GAT is suitable in the real application?

- The proposed method can be seen as hard attention, which is a discontinuous function, and I think the gradient cannot be returned. I hope the author gives further explanation to dispel my concerns.

- Many recent GT models lack in comparison[1,2,3].

- The readability of the paper is not good.

minor problem：
homogeneous -> homophilic? in line235.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
