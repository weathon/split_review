# Towards Bridging Generalization and Expressivity of Graph Neural Networks

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
Expressivity and generalization are two critical aspects of graph neural networks (GNNs). While significant progress has been made in studying the expressivity of GNNs, much less is known about their generalization capabilities, particularly when dealing with the inherent complexity of graph-structured data.
In this work, we address the intricate relationship between expressivity and generalization in GNNs. Theoretical studies conjecture a trade-off between the two: highly expressive models risk overfitting, while those focused on generalization may sacrifice expressivity. However, empirical evidence often contradicts this assumption, with expressive GNNs frequently demonstrating strong generalization. We explore this contradiction by introducing a novel framework that connects GNN generalization to the variance in graph structures they can capture. This leads us to propose a $k$-variance margin-based generalization bound that characterizes the structural properties of graph embeddings in terms of their upper-bounded expressive power. Our analysis does not rely on specific GNN architectures, making it broadly applicable across GNN models. We further uncover a trade-off between intra-class concentration and inter-class separation, both of which are crucial for effective generalization. Through case studies and experiments on real-world datasets, we demonstrate that our theoretical findings align with empirical results, offering a deeper understanding of how expressivity can enhance GNN generalization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work present a practical framework for analyzing the generalization property of GNNs via their expressivity. The main result is an extension of previous works to graph representation learning. The theoretical results are accompanied by case studies and experimental verifications to demonstrate the tightness of the proposed bound.

### Strengths
1. The proposed framework is empirically effective to estimate the generalization of GNNs. The bound is given by the regularity and expressivity of the graph encoder itself, which are accessible measures in practice. This method has the potential to assess the generalization of real-world models.

2. The presentation of the paper is clean and easy to follow.

### Weaknesses
1. The verification and discussion are limited to MPNNs. Empirically, higher-order information and/or attention mechanism are widely adopted to enhance GNNs. While the results in this work are applicable to these models in a straightforward way, it does not provide insights how these architectures improve the B/S constants in the bound. Specifically, the analysis does not delve into how different message aggregation schemes, such as those used in k-WL or attention mechanisms, quantitatively affect the expressivity term (S) and the bound's overall tightness. The paper lacks a detailed discussion on how the choice of aggregation function impacts the separation of graph embeddings and the resulting generalization bound. For example, while k-WL is known to be more expressive than 1-WL, the paper does not explore how this increased expressivity translates into a tighter bound, or if the increase in expressivity is offset by other factors in the bound. This limitation restricts the practical applicability of the framework to a narrower class of GNNs, as many state-of-the-art models incorporate more complex aggregation strategies.


### Questions
Is it possible to do a priori analysis on how a specific message aggregation scheme, e.g., k-WL or attention, can quantitively influence the terms in the bound?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the generalization of graph neural networks. The paper is based on three technical tools. The first one is margin bound, which is common in deriving generalization bound. The second is the Wasserstein distance, which is implicitly linked to the Lipschitzness property of a neural network. The third one, which is the major novelty in this paper, it to bridge between a continuous GNN to a discrete graph embedding that has more separation power, such as 1-WL or homomorphism vectors. Combining the three types of techniques yields a meaningful generalization bound. The authors gave a concrete case showing that how improved expressivity benefits/harms generalization, which is quite interesting. They also conduct experiments to support the theory.

### Strengths
Overall the theoretical result is sound and help gain better understanding for how expressivity is related to generalization in GNNs. The paper is clearly written, with rigorous math notations and theorems. While not checking the proof, I feel the results are correct and make sense to me. The concrete example is quite interesting and makes this paper potentially useful in practice.

### Weaknesses
One major weekness of this paper is that, similar to most of the previous generalization papers, the bound given by this paper is quite sophisticated, intractable to compute, and potentially lose. It may be hard to draw the conclusion that this **upper bound** indeed reflects the real case. Another weakness is the readability. The authors did not explain the insights behind this bound clearly. I think it's not intuitive to understand why generalization error can be bounded by the discrete classifier with better separation power. What does the better separation power play a role in the bound? Also, why do the authors rely on Wasserstein distance? I should acknowledge that I am not an expert in generalization theory, but it would be nice to make the paper friendly to the expressivity community as well.

### Questions
See the comments above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors in this paper study the connection between expressivity and generalization ability of GNNs in the graph classification task. They first show that the generalization ability of a graph encoder can be upper bounded by that of graph more encoders with higher expressivity . After that, they establish generalization bounds for GNNs from a optimal transfer viewpoint. Concretely, the derived bound contain the Wasserstein distance of embeddings between two random subsets sampled from training nodes within the same class. In this way, the generalization ability of GNNs in the graph classification task can be depicted by the concentration of intra-class embeddings and the separation of inter-class embeddings. Finally, the authors also provide empirical bounds that adopting sampling to computed the Wasserstein distance and verify their theoretic results on real-world datasets. The experimental results generally support their derived bounds.

### Strengths
The problem studied in this paper is pivotal in the theory of GNNs, i.e., revealing the connection between expressivity and generalization ability of GNNs. This paper makes a non-trivial progress in this problem, and the derived results are convinced and sound. As for the generalization bounds for GNNs in graph classification task, the derived results extend previous results (Chuang et al. 2021) to graph data, which also provides a new perspective to understand the generalization ability of GNNs. And, the experimental results show that the numerical values of the derived empirical bounds are significant sharper than that of VC bounds.

### Weaknesses
- The derived generalization bounds for GNNs contain the Lipschitz constants of graph encoders. These constants could be easily evaluated for shallow models, e.g., GCN with two or three layers, yet it may be difficulty to evaluate for more complex GNNs such as graph transformer [1,2]. Specifically, while the paper mentions that the Lipschitz constant of the decoder can be easily computed, the Lipschitz constant of the encoder itself is not directly addressed. The paper should clarify how these constants can be practically estimated or bounded for complex architectures, especially when the encoder involves multiple non-linear transformations and message passing steps. The lack of a clear methodology for estimating these constants limits the practical applicability of the derived bounds.
- The derived bounds do not take the optimization into consideration and thus could not reflect the impact of optimization algorithms on generalization ability. It has been shown that the training trajectory could also affect the generalization ability of models [3]. Although this observation is not yet verified for GNNs, I believe that improving the generalization bounds by involving the analysis of training dynamics could be a promising direction. The current bounds are static and do not account for the dynamic nature of the training process, which could lead to overly pessimistic or optimistic estimates of the generalization performance. For instance, different optimizers or learning rate schedules might lead to different generalization behaviors, which are not captured by the current analysis.

### Questions
Q1: In the experiments you only compare your bounds with VC bounds. It is encouraged to also compare with PAC-Bayesian bounds presented in (Ju et al. 2023).

Q2: Providing some examples to illustrate some definitions could help the readers better understand their meanings, e.g., the definitions of homomorphism and graph invariant in Section 3. You could add some figures to demonstrate these definitions more intuitively.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper theoretically studies the relationship between the generalization of GNN and the expressive power of GNN in terms of the variance of graph structures. This work especially shows a trade-off between intra-class concentration and inter-class separation, which is the key insight into the generalization gap. Some experiments are conducted to support the theory.

### Strengths
1. Some theoretical results seem solid and strong.
2. The problem to study is very interesting and important to the community to bridge the gap between the generalization and expressive power of GNN.

### Weaknesses
1. The theoretical proof is not complete. The proof of Corollary 4.5 and Proposition 5.2 are missing.
2. The paper is full of equations. Section 3 is not easy to follow when introducing so many terminologies with any examples. 
3. The practical insights are limited. Section 6 is quite confusing. This section shows that different graphs can lead to opposite effects on inter-class separation by the expressive power. Then, what should we do in practice based on this knowledge? Moreover, Section 6 seems irrelevant to intra-class concentration. Then, is the case study of Section 6 meaningful enough?
4. Results in Table 2 look weak. I cannot see that the proposed bound is better than VC bound in simulating the trend of accuracy or loss gap. The trends in the generalization gap are not clear, with many datasets showing a nearly constant gap across different layers. For example, in PROTEINS, SIDER, and MUTAG, the generalization gap appears relatively stable, and the VC bound is also constant, and smaller than the proposed bound in PROTEINS and MUTAG. This raises concerns about the practical utility of the proposed bound.

Minor: 1. at the end of line 482, it shall be "Figure 2(b)" instead of "Figure 2(a)"?
2. Please resize Figure 2 to make it look nicer.

### Questions
In Figure 2 (a), why not show both the loss gap and the bound for each dataset? In Figure 2 (b), why not show both $W_1$ and $Lip(f)$ for each dataset?

### Soundness
2

### Presentation
2

### Contribution
3
