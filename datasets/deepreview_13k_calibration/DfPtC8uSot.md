# Bounding the Expected Robustness of Graph Neural Networks Subject to Node Feature Attacks

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
Graph Neural Networks (GNNs) have demonstrated state-of-the-art performance in various graph representation learning tasks. Recently, studies revealed their vulnerability to adversarial attacks. In this work, we theoretically define the concept of expected robustness in the context of attributed graphs and relate it to the classical definition of adversarial robustness in the graph representation learning literature. Our definition allows us to derive an upper bound of the expected robustness of Graph Convolutional Networks (GCNs) and Graph Isomorphism Networks subject to node feature attacks. Building on these findings, we connect the expected robustness of GNNs to the orthonormality of their weight matrices and consequently propose an attack-independent, more robust variant of the GCN, called the Graph Convolutional Orthonormal Robust Networks (GCORNs). We further introduce a probabilistic method to estimate the expected robustness, which allows us to evaluate the effectiveness of GCORN on several real-world datasets. Experimental experiments showed that GCORN outperforms available defense methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors have provided theoretical as well as empirical study of vulnerability of GNNs to adversarial attacks. The concept of "Expected Adversarial Robustness" for GNNs is introduced and studied in relation to conventional adversarial robustness. An upper bound of this robustness concept is derived and proved for the networks which is independent of the model or attack. Based on these results, GCORN is introduced which is a training method to improve robustness of graph networks by controlling the norm of weight matrices, encouraging their orthonormality. Empirical analysis is conducted to illustrate the effectiveness of GCORN in comparison to other defense baselines.

### Strengths
**Originality**: This work introduces and studies the concept of expected robustness of graph networks and sounds very novel. Not only strong theoretical foundation is provided, methods are proposed to empirically calculate the robustness. Furthermore based on findings, a novel method to improve robustness is introduced. The theoretical and empirical claims speak to the novelty of the work.

**Quality**: The paper is characterized by its rigorous theoretical exploration and empirical analysis, which collectively elevate its overall quality. The experimental results strongly support the theoretical claims.

**Clarity**: The concepts in the paper are clear and well organized. The narrative flow keeps the reader engaging and this clarity in presentation makes the complex subject matter accessible and comprehensible.

**Significance**: I think this work provides significant insights to the robustness of GNNs and will be useful for the research community. The GCORN method is effective, has good theoretical foundation and adds a new benchmark for training robust GNNs.

### Weaknesses
A few typos:
Section 4.3 encourages -> encourage
Algorithm 1: Second for loop line# 3 $X +Z$ should be $X_i + Z_i$?

### Questions
see weaknesses

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper ,the authors theoretically define the concept of expected robustness to evaluate the robustness of GNNs, extending beyond the traditional "worst-case" adversarial robustness, and derive an upper bound of the expected robustness of GCNs and GINs. They propose a modification to the GCN architecture called the Graph Convolutional Orthogonal Robust Network (GCORN) that aims to improve robustness against node feature perturbations by promoting the orthogonality of weight matrices, effectively controlling the norm of these matrices to mitigate the impact of such attacks. The authors employ an iterative orthogonalization process that also benefits learning convergence by mitigating vanishing and exploding gradients. They ensure that the complexity of their approach remains manageable and does not excessively increase with larger graph sizes. Furthermore, they develop a probabilistic and model-agnostic method for empirical evaluation of GNN robustness. Unlike existing metrics, this proposed method applies to a variety of attack types and does not require the knowledge of specific attack schemes. They present experimental results to demonstrate the superior robustness of GCORN compared to baseline models, using various real-world datasets. The findings suggest that GCORN is a promising modification to enhance GNNs' robustness to adversarial feature perturbations without significant trade-offs in performance.

### Strengths
Originality: The paper introduces a new theoretical framework for defining and quantifying the concept of "Expected Adversarial Robustness" for GNNs, which is a deviation from the traditional worst-case scenario evaluation that dominates the field. Their GCORN model demonstrates an innovative approach to mitigating the impact of adversarial attacks on GNNs by leveraging the orthogonality of weight matrices, a concept that has not been extensively explored in the context of GNNs. The development of a model-agnostic, probabilistic method for evaluating GNN robustness is a creative combination of existing ideas that significantly enhances the security assessment of graph models against a wider range of adversarial strategies.
Quality: The quality of the paper is high as it thoroughly examines the proposed concepts from both theoretical and empirical perspectives. It provides a rigorous mathematical formulation of the problem and strong theoretical foundations for the methods proposed.
Clarity: The paper is well-written and organized in a manner that strategically guides the reader through both the theoretical and practical aspects of the work. Definitions and theoretical findings are clearly presented and sufficiently detailed, making them accessible to readers with a foundational understanding of the domain. 
Significance: The Expected Adversarial Robustness framework gives practitioners a more nuanced understanding of model vulnerability in realistic scenarios beyond the worst-case adversarial examples.
In summary, the paper showcases original conceptual developments, high-quality theoretical work, clarity in its exposition, and significant contributions to the field of graph representation learning, particularly addressing adversarial robustness in GNNs.

### Weaknesses
While the paper presents significant contributions to the stability and robustness of GNNs against feature-based adversarial attacks, there are certain areas where it could potentially be improved to reinforce its claims and widen its applicability:
1. Computational Cost: The estimation of a GNN’s expected robustness involves a sampling-based approach, which indeed can be computationally intensive as it requires generating and evaluating numerous perturbed versions of the input graph, especially when it comes to large datasets. The computational cost is not only related to the number of samples but also to the size of the graph and the complexity of the GNN model itself. The paper does not provide a detailed analysis of how the computational cost scales with these factors, which is crucial for practical applications.
2. The robustness measure might vary significantly with each estimation due to sampling, leading to inconsistency and making it difficult to compare with other models. The paper lacks a rigorous analysis of the variance of the robustness estimate and how this variance impacts the reliability of the results. Without a clear understanding of the statistical properties of the estimator, it is difficult to assess the significance of the reported robustness improvements.
3. The paper lacks the comparison between the theoretical upper bound of the expected robustness and its empirical estimates. The authors have provided a theoretical upper bound for the expected adversarial robustness of GNNs and introduced an empirical method to estimate this robustness; however, the paper does not explicitly show how closely the empirical results align with the theoretical bound. This comparison is essential to validate the theoretical findings and to understand the practical implications of the proposed bound. It is unclear whether the bound is tight enough to be useful in practice.
4. Attack Models and Benchmarks: It appears that the attack models used to evaluate robustness are largely selected from existing and potentially well-known strategies. Exploration of the effectiveness of GCORN against emerging or more sophisticated adversarial models could further substantiate the claimed robustness. Furthermore, including newer or well developed defense mechanisms would be advantageous for our understanding of GCORN’s effectiveness. The paper does not address the potential for adaptive attacks, where the adversary is aware of the defense mechanism and can design attacks to circumvent it. This is a significant limitation, as real-world adversaries are often adaptive.

### Questions
1. How to determine the number of samples required to obtain an accurate empirical estimation of the robustness? Is there a theoretical guarantee (such as a bound on the estimation error with high probability) that the estimated value is close enough to the true expected robustness?
2. A comparison between the theoretical upper bound of the expected robustness and its empirical estimates should be provided in order to show how closely the empirical results align with the theoretical bound and the effectiveness of the theoretical bound.
3. It is encouraged to include experiments with more sophisticated adversarial models and comparisons with other defense methods.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new formalization of the notion of expected robustness for GNN and introduce some theoretical guarantees on this quantity. It also uses the insights coming from the bound in the case of GCN to propose a robust alterntive under the form of GCORN. The paper also validates the relevance of their approach empirically.

### Strengths
* The paper is well structured and easy to read
* The paper proposes a clear and general framework for adversarial robustness on graphs
* The paper derives some theoretical bounds for expected adversarial robustness and leverage this formulation to propose some simple but efficient improvement based on orthonormalisation with the GCORN model
* In the case of MPNN, the paper provides both bounds for node features attacks and structural attack
* It also validates that his approach work in practice

### Weaknesses
 * The paper considers only a few attacks to validate his approach. Even if these attacks makes sense (PGD / Nettack are good standards for this type of tests), it would have been interesting to try additional ones. Specifically, the evaluation could benefit from including attacks that target different aspects of the graph structure or node features, such as those that focus on edge rewiring or feature perturbation with different magnitudes. This would provide a more comprehensive understanding of the robustness of the proposed method.
* The gain of robustness of GCORN over GCN is interesting but it's not clear how it compares to other defense methods (for instance is GCORN w adversarial training still better than GCN with adversarial training). It is important to benchmark GCORN against a wider range of defense strategies, including those that use adversarial training, to properly assess its relative performance. The paper should also explore whether combining GCORN with adversarial training leads to further improvements in robustness.
* It is unclear to me how tight is the bound from theorem 4.1/4.2 ; this part could be stated more clearly in the experiment section. The paper should include a more detailed analysis of the tightness of the derived bounds, possibly by plotting the theoretical bound alongside the empirical robustness for different datasets and attack parameters. This would help to better understand the practical relevance of the theoretical results.

### Questions
* Do you have some table summarizing the tightness of the bound in the experiments you ran ?
* You focus mainly on the cases where alpha, beta=(0,1) or (1,0). Do you have some insights on the more general case of mixed attacks (structural and feature based) ? Are some results holding in that case ? (combination of 4.1 and 4.2 ?)

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the robustness of GNNs under adversarial attacks to node features in attributed graphs. The authors establish the upper bound for the expected robustness of GCNs under the node feature perturbations, and generalize to GIN as well as structural attacks. The bound also motivates a solution called Graph Convolutional Orthogonal Robust Networks (GCORNS), that adopts  orthogonal projections of the weight matrices of GNNs to reduce the upper bound (and to improve the robustness). Moreover, the authors also propose an estimation method of the proposed robustness measure. Then they conduct experiments to demonstrate the improved robustness of GCORN method.

### Strengths
- The proposed robustness measure is new;

- The proposed method is somehow interesting;

- The presentation and organization are clear;

### Weaknesses
(-) The scope seems to be limited;

(-) Some baselines have not been compared with.

(-) The improvements seem to be incremental and limited;



### Questions
1. The scope seems to be too limited:
a. If the scope is as claimed as focusing on adversarial attacks on node features, what are the practical scenarios? Are there any realistic cases for the studied attack?

b. As already been shown by the authors, there is a natural connection between structural attacks and the attribute attacks, why not study the more general attacks? 

c. The work also neglects a rich literature in the line of graph injection attack, where the adversary will inject new nodes and optimize the injected nodes’ features to perform the attack [1,2,3,4]. It is also worth discussing the connections of the proposed robustness measure with respect to injection attacks, as well as the recently emerging backdoor attacks [5,6].

2. There are already multiple new robustness measures proposed [3,7] which have not been discussed in the paper.

3. Some baselines have not been compared with, including [8,9,10]. Can GCORNS outperform them? 

b. Besides, why table 1 and table 2 adopt different baselines? 

c. Can a heuristic solution like weight decay achieve the same functionality as GCORNS?

d. Can GCORNS be incorporated to more GNN backbones other than GCN?

e. Would GCORNS work for large graphs?

4. The improvements seem to be limited when with slightly more powerful attacks. For example, in Table 1, with Nettack, GCORN underperform AirGNN in ogbg-arxiv, and RGCN in PubMed. In Table 2, with structural attacks, GCORN underperform previous methods in even more cases.


**References**

[1] TDGIA: Effective Injection Attacks on Graph Neural Networks, KDD’21.

[2] Single Node Injection Attack against Graph Neural Networks, CIKM’21.

[3] Understanding and Improving Graph Injection Attack by Promoting Unnoticeability, ICLR’22.

[4] Let Graph be the Go Board: Gradient-free Node Injection Attack for Graph Neural Networks via Reinforcement Learning, AAAI’23.

[5] Unnoticeable Backdoor Attacks on Graph Neural Networks, WWW’23.

[6] On Strengthening and Defending Graph Reconstruction Attack with Markov Chain Approximation, ICML’23.

[7] Revisiting Robustness in Graph Machine Learning, NeurIPS’22.

[8] Graph Structure Learning for Robust Graph Neural Networks, KDD’20.

[9] Elastic graph neural networks, ICML’21. 

[10] EvenNet: Ignoring Odd-Hop Neighbors Improves Robustness of Graph Neural Networks, NeurIPS’22.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
