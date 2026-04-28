# Enhancing Mutual Information Estimation in Self-Interpretable Graph Neural Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Graph neural networks (GNNs) with self-interpretability are pivotal in various high-stakes and scientific domains. The information bottleneck (IB) principle holds promise to infuse GNNs with inherent interpretability. In particular, the graph information bottleneck (GIB) framework identifies key subgraphs from the input graph $G$ that have high mutual information (MI) with the predictions while maintaining minimum MI with $G$. The major challenge is dealing with irregular graph structures and gauging the conditional probabilities for evaluating MI between these subgraphs and $G$. Existing methods for estimating the MI between graphs often present distorted and loose estimations, thereby undermining model efficacy. In this work, we propose a novel framework GEMINI for training self-interpretable graph models, which tackles the key challenge of graph MI estimations. We construct a variational distribution over critical subgraphs, based on which an efficient MI upper bound estimator for graphs is built. Besides the proposed theoretical framework, we devise a practical instantiation of different modules in GEMINI. We compare GEMINI thoroughly with both self-interpretable GNNs and post-hoc explanation methods on eight datasets with both interpretation and prediction performance metrics. Results reveal that GEMINI outperforms state-of-the-art self-interpretable GNNs on interpretability and achieves comparable prediction performance compared with mainstream GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a novel approach for approximating the Graph Information Bottleneck (GIB). Their method focuses on modeling the distribution of arbitrary subgraphs and graphs, while also bypassing the need to model the prior of subgraphs. Experimental results seem to demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-written, with the authors providing a thorough derivation of the proposed GIB approximation and presenting a clear step-by-step explanation of their method.

2. The authors employ the CLUB technique to circumvent the need for modeling the prior of subgraphs. This approach appears to relax the assumptions made in previous methods, enhancing the flexibility and applicability of the proposed approach.

### Weaknesses
1. The model architecture in this paper bears a resemblance to GSAT, and it would be advantageous if the authors could explicitly delineate the key distinctions between the two. Furthermore, the experimental results suggest a notable enhancement over GSAT despite their similar model architectures. The paper lacks a detailed explanation of how the proposed method addresses the limitations of GSAT, particularly in the subgraph matching step, which is crucial for calculating the conditional probability p(G_sub|G). Without a clear explanation of how this is handled differently, the claimed improvements are difficult to assess. Providing inference codes for model reproduction would greatly facilitate the validation of these results and contribute to the paper's overall reproducibility and transparency.

2. The authors assert that the proposed method can generate sparse subgraphs even without the need for sparse regularization. However, it is evident that L_sp is introduced as a subgraph term to regulate graph sparsity. In the ablation study, the authors argue that this term is essential, which appears to be inconsistent with their initial claim in the introduction. The paper should clarify the specific role of L_sp and how it interacts with the GCLUB regularization to achieve sparsity. The current presentation suggests a contradiction in the claims regarding the necessity of explicit sparsity regularization.

### Questions
1. See the comments above.

2. What is the benefit of modeling arbitrary subgraphs and graphs? Since G_{sub}^1 should be sampled from G_1 and should not be related to G_2.

3. Why is the MI upper bound approximation proposed in the method better than previous methods?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The Graph Information Bottleneck framework significantly enhances the self-interpretability of Graph Neural Networks. However, current approaches in estimating the mutual information between graph explanations and their original forms frequently yield distorted and imprecise estimations, ultimately compromising the effectiveness of the model. In response to these limitations, this paper introduces a novel framework called GEMINI to address these challenges.

### Strengths
+ They utilize a MI upper bound estimator based exclusively on the conditional probability distribution.
+ They introduce a variational distribution and its suitable instantiation for the conditional probability distribution.
+ Extensive experiments demonstrate the effectiveness of the proposed framework.

### Weaknesses
-	They employ established MI estimator theory, which appears easily extendable to the graph domain. In my view, it seems they have not drawn particularly interesting conclusions or specific designs for graphs. I have some reservations about the novelty of the proposed framework.
-	The experimental results are not convincing enough. SOTA explainers for GNNs should be set as baselines. Moreover, the proposed model did not exhibit a significant improvement compared to these baselines.
-	The paper's writing and organization require enhancements. For instance, it is challenging for readers to discern the corresponding relationships between the limitations and the contributions.

### Questions
Please refer to the weaknesses.

- They employ established MI estimator theory, which appears easily extendable to the graph domain. In my view, it seems they have not drawn particularly interesting conclusions or specific designs for graphs. I have some reservations about the novelty of the proposed framework.
- The experimental results are not convincing enough. SOTA explainers for GNNs should be set as baselines. Moreover, the proposed model did not exhibit a significant improvement compared to these baselines.
- The paper's writing and organization require enhancements. For instance, it is challenging for readers to discern the corresponding relationships between the limitations and the contributions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The goal of the paper is to evaluate the mutual information (MI) between an input graph and a key subgraph. To tackle this problem, the authors propose a novel framework called GEMINI, which trains self-interpretable graph models and addresses the challenge of distorted and imprecise estimations in graph MI estimation research. The authors construct a variational distribution over the critical subgraph and create an effective MI upper bound estimator. The proposed method is shown to be effective according to empirical results.

### Strengths
1. This paper is well-organized and well-written. The authors provide sufficient details about their work and easy to understand. 

2. Estimating the mutual information between the input graph and the subgraph is both important and challenging.

### Weaknesses
1. This work closely follows GSAT[1]. Its main theoretical contribution is the addition of the information bottleneck (IB) upper bound loss $L_{GCLUB}$ to the objective of GSAT[1], which is based on the idea of variational CLUB[2].

2. Does the proposed model's ability to remove the spurious correlation come from the framework of GSAT? Can GEMINI provide a theoretical guarantee for the removal of spurious correlations?

3. Some of the numerical results reported in Table 1 and Table 2 are quite different from those reported in GSAT. The differences are particularly noticeable with the numbers that involve MNIST-75sp in Table 1 and those associated with SPMotif in Table 2, relating to GIN and GSAT. It would be helpful if the authors could provide further details about their implementations and explanations for these differences.

### Questions
1. On page 3, in the last sentence before Eq.3, should it be a “lower” bound of $I(G_{sub};Y)$?

2. I cannot find the curve of GSAT in the second subfigure of Fig. 2(d). Is it missing or unavailable?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Existing self-interpretable Graph Neural Networks (GNNs) built upon Graph Information Bottleneck (GIB) suffer from the burdensome of mutual information estimation. To address this issue, this work proposes a novel framework for self-interpretable GNNs with an enhanced technique for mutual information estimation, namely GENIMI. Experiment results indicate the proposed GENIMI enjoys improved predictive and interpretable performance.

### Strengths
This paper is well-written and easy to follow. The motivation for improving the mutual information estimation in the GIB framework is clear and crucial. Empirical results show that the proposed GEMINI enjoys competitive performances of GNN prediction and interpretability.

### Weaknesses
However, the reviewer is concerned with some theoretical details.

1. For the predictive term in Eqn. 3, the appropriate formula derivation is: $I(G_{sub};Y)=E_{p(G_{sub},Y)}\log{\frac{p(Y|G_{sub})}{p(Y)}}\geq E_{p(G_{sub},Y)}q_{\omega}(Y|G_{sub})+H(Y)$. The current derivation in the paper lacks a rigorous justification for the transition from the mutual information to the variational lower bound. Specifically, the Jensen's inequality application and the introduction of the variational distribution $q_\omega$ need to be explicitly shown and explained.

2. Does $p_{\phi}(G_{sub}|G)$ and $q_{\theta}(G_{sub}|G)$ share the same subgraph generator? If so, what is the intuition behind using $q_{\theta}(G_{sub}|G)$ to approach $p_{\phi}(G_{sub}|G)$? The paper does not clearly articulate the relationship between the subgraph generator $g_\phi$ and the distributions $p_\phi$ and $q_\theta$. It is unclear how the parameters of $g_\phi$ influence the distributions, and why a separate neural network $q_\theta$ is needed to approximate $p_\phi$ instead of directly working with the output of $g_\phi$. Furthermore, the paper lacks a detailed explanation of how the two GNNs within $q_\theta$ are structured and how they contribute to the probability calculation.

### Questions
The authors are encouraged to address the concerns in Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
