# Causality-Inspired Spatial-Temporal Explanations for Dynamic Graph Neural Networks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Dynamic Graph Neural Networks (DyGNNs) have gained significant popularity in the research of dynamic graphs, but are limited by the low transparency, such that human-understandable insights can hardly be drawn from their predictions. Although a number of existing research have been devoted to investigating the interpretability of graph neural networks (GNNs), achieving the interpretability of DyGNNs is pivotally challenging due to the complex spatial-temporal correlations in dynamic graphs. To this end, we propose an innovative causality-inspired generative model based on structural causal model (SCM), which explores the underlying philosophies of DyGNN predictions by identifying the trivial, static, and dynamic causal relationships. To reach this goal, two critical tasks need to be accomplished including (1) disentangling the complex causal relationships, and (2) fitting the spatial-temporal explanations of DyGNNs in the SCM architecture. To tackle these challenges, the proposed method incorporates a contrastive learning module to disentangle trivial and causal relationships, and a dynamic correlating module to disentangle dynamic and static causal relationships, respectively. A dynamic VGAE-based framework is further developed, which generates causal-and-dynamic masks for spatial interpretability, and recognizes dynamic relationships along the time horizon through causal invention for temporal interpretability. Comprehensive experiments have been conducted on both synthetic and real-world datasets, where our approach yields substantial improvements, thereby demonstrating significant superiority.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a causal approach to improving the interpretability of GNNs. The authors have integrated a contrastive learning module that distinguishes between non-causal and causal relationships, enhancing the clarity of the model's decision-making process. Additionally, a dynamic correlating component is employed to differentiate dynamic from static causal relationships, providing a nuanced understanding of changes over time. Furthermore, the authors utilize a VGAE-based model to generate causal-and-dynamic masks, which contribute to spatial interpretability. This model also captures dynamic relationships across temporal scales through causal inference, thereby boosting the model's ability to interpret temporal data.

### Strengths
(1) The composition and articulation of the paper are logical and coherent. The use of a causality-driven approach to enhance the out-of-distribution generalization capabilities of dynamic GNNs is intriguing.

(2) Introducing research on temporal distribution shift in sequential processes is important and may provide valuable insights for subsequent studies.

### Weaknesses
 (1) The paper's presentation appears problematic, particularly in the description of the backdoor adjustment. While simplified results are provided in the main text, the specific derivation process is absent and should be relegated to the appendix. Additionally, the computational intensity of introducing temporal masks, which could be exacerbated by the incorporation of contrastive learning (VGAE is known to be computationally demanding), is not addressed. The authors should include complexity descriptions to inform the reader. However, these issues are not discussed in the paper.

(2) The proposal of 4 loss functions can be unfriendly to network training. If even one parameter is improperly tuned, it could lead to significant instability or even failure in network training. The authors should systematically discuss parameter selection techniques or guidelines to aid those who follow in this line of work.

(3) There is a lack of related experiments: although experiments are conducted, there is a shortage of benchmarks in this field. It is recommended that the authors refer to [1] to add more experiments to validate the effectiveness of their DyGNN, such as including the Ogbn-Arxiv dataset. Additionally, an ablation study replacing VGAE-like models is crucial to help others understand the contribution of each model component.

(4) Related work is missing from the paper, especially concerning spatio-temporal related work [5], generalization/extrapolation on graphs, and causality learning [2-4]. The authors should consider these areas to provide a more comprehensive context for their research.

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach for interpretability in dynamic graph neural networks. The proposed framework is demonstrated on both synthetic and real-world datasets. The experimental results show that the proposed method outperforms the baselines (all baselines are for explaining static graph neural networks). Another contribution is that the paper constructs a new synthetic benchmark dataset for dynamic graph interpretability tasks.

### Strengths
The proposed framework is the first work for interpretability in dynamic graph neural networks. This is a significant contribution. The paper is well organized and clearly described. The method is technically sound. The experiments are comprehensive and the results show the effectiveness of the proposed method. The new constructed benchmark dataset is a good addition to the research domain.

### Weaknesses
Minors: 
In Figure 1, the text is too small.

### Questions
In table 2, the best performance for OrphicX is obtained by DTree-Grid?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a causality-inspired generative model to explain DyGNN predictions by identifying the trivial, static, and dynamic causal relationships. To experimentally evaluate the proposed approach, synthetic dynamic datasets are generated and provided. Evaluations on both synthetic datasets and real-world datasets demonstrate superior performance.

### Strengths
Originality: this paper is aimed at explaining dynamic graphs by proposing a causal inspired framework. Existing works on the explanation of GNNs are on static graphs. This paper instead focuses on dynamic graphs. Disentangling spatial and temporal relationships can be very challenging. This paper explicitly constructs a structural causal model by considering trivial relationships and causal relationships (consisting of static relationships and dynamic relationships) to solve this problem, which is interesting.

### Weaknesses
The presentation can be improved. It is hard for me to follow the paper well. For example, in the Introduction section, it is hard to straightforwardly understand the spatial interpretability and temporal interpretability. Illustrations can help readers understand better. Besides, it is not easy for me to understand the challenges for implementing the SCM (third paragraph in the Intro). Correspondingly, I didn’t see how the proposed approach addresses the challenges in the fourth paragraph.

The significance of the proposed approach is not clear. It is hard to judge the performance improvement achieved by DyGNNExplainer since other baselines are all for static graphs.

### Questions
In Table 2, for Node classification task, OrphicX performs better than DyGNNExplainer on DTree-Grid dataset but is not bolded?

Can you compare your model on static graphs to state-of-the-art explainers?

How sensitive the model is to the hyper parameters in Equation 15? What’s the computational complexity of solving Equation 15?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims at interpreting the Dynamic Graph Neural Networks (DyGNNs), and proposes an innovative causality-inspired
generative framework based on structural causal model (SCM), which explores the underlying philosophies of DyGNN predictions by identifying the trivial, static, and dynamic causal relationships. This work actually identifies the subgraph via a masking mechanism.

### Strengths
S1. The research motivation of this paper is clear. The existing studies on the interpretability of Dynamic Graph Neural Networks are still limited, thus it is meaningful to bridge such gap.
 
S2. The description of the existing challenges to the interpretability of DyGNNs is interesting. The authors argue that the first challenge lies in the approach to disentangling the complex causal relationships as no explicit information is available for the identification of trivial, dynamic, and static relationships.

### Weaknesses
W1. I'm confused about this sentence, 'Hence, our ultimate objective is to define a generative model', in Section 2.1. Throughout the whole paper, DyGNNExplainer is a representational model.

W2. Equation 1 should be described in detail. Since causal relationships ($C$) consist of dynamic ($D$) and static ($S$) relationships, there should exist $P(S) = P(C) - P(D)$. I guess this equation is derived from it, but I can't see the logical derivation.

W3. This paper still has not well addressed the interpretability issue of DyGNNs. The authors only provide evidence in performance improvements and static interpretability ('house' motif in BA-Shapes). We can not observe specific causal relationships in dynamic graphs from provided results. Besides, the baselines are interpretability methods conducted on static graphs, and the datasets are not classic dynamic graph datasets, such as traffic and citation network datasets. Thus, this proposed solution does not satisfy the expectation that exploring the interpretability of dynamic graph.

W4. Some important literature is missing, e.g., CauSTG for capturing invariant relations targets temporal shifts in ST graphs [1] and CaST for discovering via Structural Causal Model (SCM) with back-door and front-door adjustment [2]. The authors should distinguish the distinctions between the proposed DyGNNExplainer and  (CauSTG, CaST), especially the CaST.


### Questions
1. In Equation 7, $e$ is not defined in this paper, and the implementation of  $s( \cdot , \cdot )$ is also not provided. 

2. Does $||A||$ operate by summing all elements of $A$ in Equation 14? Besides, does Equation 14 exist error? To satisying the sparsity requirement of causal and dynamic causal graph set, whether Equation 14 should be replaced by $\frac{{||A_t^C|{|_1} + ||A_t^S|{|_1}}}{{||{A_t}|{|_1}}}$?

3. In Table 2, OrphicX achieves the best performances on DTree-Grid (96.1). But, you bold your work DyGNNExplainer (94.2 < 96.1).

4. $\Theta $ should be replaced by $\Psi $ in the last line of Section 2.

5. How to interpret the 'dynamic' in DyGNNExplainer? Can the datasets in experiments support the augment raised in this paper, as it seems there are no dynamic graph in experiments?

6. Distinguish the distinctions between this work and CaST.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
