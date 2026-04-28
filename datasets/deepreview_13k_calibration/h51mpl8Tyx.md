# BANGS: Game-theoretic Node Selection for Graph Self-Training

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 5, 8, 6, 6

## Abstract
Graph self-training is a semi-supervised learning method that iteratively selects a set of unlabeled data to retrain the underlying graph neural network (GNN) model and improve its prediction performance. While selecting highly confident nodes has proven effective for self-training, this pseudo-labeling strategy ignores the combinatorial dependencies between nodes and suffers from a local view of the distribution.
To overcome these issues, we propose \ourmodel, a novel framework that unifies the labeling strategy with conditional mutual information as the objective of node selection. Our approach---grounded in game theory---selects nodes in a combinatorial fashion and provides theoretical guarantees for robustness under noisy objective. More specifically, unlike traditional methods that rank and select nodes independently, \ourmodel considers nodes as a collective set in the self-training process. Our method demonstrates superior performance and robustness across various datasets, base models, and hyperparameter settings, outperforming existing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the problem of graph self-training, which is a main strategy in semi-supervised graph learning. The study specifically addresses the combinatorial dependencies between nodes for pseudo-label selection. To tackle this challenge, the authors propose a novel framework that unifies the labeling strategy with conditional mutual information to guide the selection of pseudo-labels. Unlike traditional approaches that provide a sorted list of labels, the proposed method forms a node set for graph self-training. The proposed method is validated on many real-world datasets.

---
After rebuttal, I raise my rating from 5 to "6: marginally above the acceptance threshold."

### Strengths
This paper introduces a new direction in graph self-training by integrating conditional mutual information into the pseudo-labeling process. The proposed method may have the potential to improve the effectiveness of semi-supervised learning on graphs, particularly in scenarios where node dependencies play a significant role. The empirical studies are solid.

### Weaknesses
1. One main concern is the rationale behind forming a node set for graph self-training from a submodular optimization perspective. The paper argues that pseudo-labels should be evaluated and fed into the model as a set, contrasting with most existing self-training strategies that evaluate each pseudo-label individually. The justification of the traditional strategy is that adding pseudo-labels to the training set satisfies submodularity, allowing for the use of a greedy strategy to achieve an optimal solution.

Does submodular optimization apply to the formation of the node set in this paper? Why this approach is advantageous?

2. In the experiments, the number of pseudo-labels $k$ is fixed. This setting may not be fair for comparisons across different methods. Allowing each baseline to obtain an optimal number of pseudo-labels as they required would provide a more equitable evaluation and potentially yield more insightful results.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the problem of graph self-training and argue that the combinatorial dependencies between nodes have a very strong relationship with the pseudo-labeling strategy which has been ignored now. To overcome this problem. this paper propose a novel framework that unifies the labeling strategy with conditional mutual information as the objective of node selection. This method grounded in game theory selects nodes in a combinatorial fashion and provides theoretical guarantees for robustness under noisy objective.

### Strengths
The structure of this article is clear and easy to understand. The experiments are detailed, and the analysis of the results is also quite clear. Moreover, the code has been made publicly available.

### Weaknesses
1. The motivation of the article is unclear and not strong enough. The core work of self-training is to select suitable nodes and assign pseudo-labels. This article focuses on the combinatorial dependencies in node selection; however, the impact of such information on the model's performance is not discussed in depth and lacks supporting experiments. Specifically, while the paper introduces a k-Bounded Banzhaf value, it does not sufficiently demonstrate why this specific measure is superior to other possible measures of node importance in the context of self-training. The paper needs to provide more direct evidence that considering these combinatorial dependencies leads to a significant improvement in the quality of pseudo-labels and, consequently, the performance of the model.

2. Furthermore, I do not see self-training as an interesting research direction; it seems more like a variant of data augmentation to me. Assigning labels to some nodes based on existing information intuitively seems difficult to understand, as it does not clearly lead to new information. The core issue is that the pseudo-labels are derived from the model's own predictions, which could reinforce existing biases or errors. The paper does not adequately address how this approach avoids the problem of confirmation bias and how it can truly lead to the discovery of new, useful information that is not already present in the labeled data.

### Questions
1. The article has designed a k-Bounded Banzhaf value to measure the marginal contribution of  a node. Does it still satisfy the properties of the Banzhaf value, such as symmetry, additivity, and so on?
2. In Section 3.2 of the paper, the ground-truth utility function and the noisy utility function are mentioned. How is the ground-truth utility function calculated?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors addressed the limitations in graph self-training by introducing a comprehensive framework that systematically tackles the node selection problem using a novel formulation with mutual information. The proposed BANGS is a game theory-based method with the
utility function based on feature propagation.

### Strengths
The writing is clear. 

The discussion is comprehensive.

### Weaknesses
The novelty of the studied problem is limited - the authors studied the node selection problem using a novel formulation with mutual information.

The paper relies on a lot on (Wang & Jia, 2023) technically. It would be good to demonstrate the authors' unique contribution in the context of (Wang & Jia, 2023) - is it a straightforward extension of the referenced work?

### Questions
Given the improvement, how significant is the problem solved?

Is this work straightforward extension of the referenced work of (Wang & Jia, 2023)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
To address the issue that existing pseudo-labeling strategy ignores the combinatorial dependencies between nodes, this paper introduces a framework that unifies the labeling strategy with conditional mutual information as the objective of node selection, instead of predicting pseudo labels.

### Strengths
1. It is interesting to introduce techniques from the co-operative game theory into graph self-tranining, taking into acount the combinatorial.
2. The paper is well-organized and literature review is conducted well.
3. The paper provides a theoretical analysis of the proposed method.

### Weaknesses
1. Considering the reported standard deviation of the experimental results, the improvements on some datasets appear to be marginal, such as on the Flickr dataset.
2. Experiments are conducted only on homophilic graph datasets. It would be better if the performance of the method on heterophilic graph datasets could be provided, such as Cornell, Texas, and Wisconsin [1].

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new node selection method for graph self-training. The authors leverage PPR-based feature propagation to estimate a utility function aimed at information gain. To address node interdependencies in graph-structured data, the authors employ Banzhaf values, allowing for combinatorial modeling of node influence during the node selection phase.

### Strengths
- The paper's motivation is clear and well-presented.
- The introduction of Banzhaf values to incorporate node interdependencies is novel and unique.
- BANGS is grounded in a profound theoretical foundation, which makes the proposed method more solid.

### Weaknesses
 **W1.** BANGS requires a confidence calibration model, which further increases the computational costs. Additionally, the authors do not provide a running time analysis on the Flickr, a large-scale dataset; the results are selectively reported on small- or medium-sized datasets. Although the method is theoretically well-founded, its practical utility seems to be limited due to the high computational burden. The lack of a detailed computational analysis, especially on larger graphs, makes it difficult to assess the scalability of the proposed approach. The authors should provide a more thorough analysis of the computational complexity, including the time and memory requirements, as the Banzhaf value calculation can be particularly expensive.

**W2.** The most concerning part is the marginal empirical performance. This is particularly noticeable in the ablative study, where the performance gap between Conf (Cal) and BANGS (Uncal) is minimal. Since the calibration model is not this paper's contribution, it is difficult to acknowledge the method's distinct efficacy. This calls into question about whether the high computational complexity of BANGS justifies the gains. Furthermore, the use of calibration model is somewhat hidden from the reader, only becoming clear in the experimental setting paragraph. For a paper that emphasizes empirical performance, it is critical to clearly identify the impactful components in the main text. The ablation study should more clearly demonstrate the isolated impact of the Banzhaf-based selection strategy, as the current results suggest that the performance gains are primarily due to the calibration model, rather than the proposed selection method.

**W3.** The authors’ claim that "previous approaches all suffer from independent selection" (in introduction) may be overstated. For instance, CaGCN [1] propagates node confidence across the graph structure, reflecting combinatorial interactions through multi-hop neighbor consideration during calibration.

### Questions
**Q1.** CaGCN is not considered a SOTA calibration model. Could the authors compare the performance between BANGS and GATS [2]? While GATS does not include a self-training experiment, it could likely be adapted to a pseudo-labeling framework, similar to CaGCN.

**Q2.** Comparison with consistency regularization approaches, such as [3], is highly recommended, as the current baselines are all pseudo-labeling methods.

### Soundness
3

### Presentation
3

### Contribution
2
