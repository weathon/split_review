# Mitigating Emergent Robustness Degradation while Scaling Graph Learning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Although graph neural networks have exhibited remarkable performance in various graph tasks, a significant concern is their vulnerability to adversarial attacks. Consequently, many defense methods have been proposed to alleviate the deleterious effects of adversarial attacks and learn robust graph representations. However, most of them are difficult to *simultaneously* avoid two major limitations: (i) an emergent and severe degradation in robustness when exposed to very intense attacks, and (ii) heavy computation complexity hinders them from scaling to large graphs. In response to these challenges, we introduce an innovative graph defense method for unpredictable real-world scenarios by *designing a graph robust learning framework that is resistant to robustness degradation* and *refraining from unscalable designs with heavy computation*: specifically, our method employs a denoising module, which eliminates edges that are associated with attacked nodes to reconstruct a cleaner graph; Then, it applies Mixture-of-Experts to select differentially private noises with varying magnitudes to counteract the hidden features attacked at different intensities toward robust predictions; Moreover, our overall design avoids the reliance on heavy adjacency matrix computations, such as SVD, thus facilitating its applicability even on large graphs. Comprehensive experiments have been conducted to demonstrate the anti-degraded robustness and scalability of our method, as compared to popular graph adversarial learning methods, under diverse attack intensities and various datasets of different sizes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper develops a novel graph learning model that can handle very intense attacks and avoid heavy computation complexity. The model involves designing a new graph neural network (GNN) architecture the mixture of experts associated with differential noise. Extensive experiments are conducted to demonstrate that the proposed model can outperform many baseline methods against different attacks. Sufficient theoretical analysis is also provided.

### Strengths
+ It is new that the paper introduced the problem of performance degradation against intense attacks of existing models. Solving the problem is very important, especially for the data of high-risk applications. It is also interesting to consider improving computation efficiency. 

+ The paper developed a new model that leverages a mixture of experts to design a new graph neural network architecture, which is novel and interesting. The theoretical analysis of the proposed method is sufficient and solid. 

+ The authors have conducted sufficient experiments over multiple datasets with different intensity attacks. The proposed model outperforms many baseline methods. The improvements are significant.

### Weaknesses
 - It seems that the current manuscript mainly focused on the node attacks. How is the performance of the proposed method against other attacks? That is, more results and discussion regarding different attacks are suggested. 

- Besides a mixture of experts, there are other choices for improving GNN from an ensemble perspective. It is necessary to discuss the comparison between different methods and why the current design, i.e., MoE with differential private noise, is selected.

### Questions
Please see the weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a graph neural network resilient to adversarial attacks. This approach incorporates a denoising step and a novel message passing scheme that leverages a mixture of experts (trained for varying levels of noises). The superiority of the proposed method over baseline approaches is demonstrated across diverse adversarial attack scenarios.

### Strengths
S1. The paper is easy to follow well structured.

S2. The inclusion of a mixture of experts, each tailed for distinct noise levels, seems to be a novel and logical approach.

### Weaknesses
W1. The argument regarding the poor scalability of the existing method is not sufficiently convincing. For example, many extremely fast SVD algorithms have been developed for sparse graphs. It is essential for the authors to discern whether the scalability issue (e.g., O(N^2) complexity) is simply an implementation issue or it stems from fundamental limitations.

W2. It appears that the considered baselines were not specifically designed to address the attack scenarios under consideration (i.e., the injection of nodes). For instance, EvenNet is specifically designed for generalization to graphs with different degrees of homophily. Consequently, claiming superiority over them may not strongly support the effectiveness of the proposed method. The authors should consider evaluating their approach against state-of-the-art methods better aligned with the specified attack scenarios.

W3. The denoising performance of the proposed auto-encoder module is not compared with any baseline approach (e.g., Jaccard, SVD, etc).

### Questions
Q1. Please address W1

Q2. Please address W2

Q3. Could you provide details on how E_{r} is derived from the trained auto-encoder? Can it include new edges, or does it solely filter out some existing ones?

Q4. The results in Table 11 are not easy to understand. Can you please provide more specific details, including the numbers of TPs, TNs, FPs, and FNs?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on defending node injection attacks on graphs. The authors propose a pipeline called DRAGON to reconstruct a clean graph via combining denoise auto-encoder and DP-based mixture of experts. Extensive experiments are conducted to illustrate the advantage of the proposed method.

### Strengths
The problem is well motivated and important. The organization is clear, and the performance of the proposed method is promising.

### Weaknesses
1. Illustrations in some sections are not clear and easy to follow. For example in Section 4.2, the notations are not clearly introduced. Besides, the motivation of DPMoE is not well introduced. The authors should provide some intuitions/insights for leveraging Mixture-of-Experts, which I think is an important novelty of this work. But from this section, I do not get why MoE is useful though the authors empirically illustrate that in the experimental part.
2. Lemma 1 is very confusing. It is hard to understand what the authors are trying to state in this lemma and how it supports the method. The most confusing thing is that "Suppose a GNN f(·) containing DPMoE satisfies (ε,δ)-DP", how can this be supposed? I thought Lemma 1 was to prove that adding a DPMoE module to the model would make it DP, but the authors directly assume that. Besides, what does this mean "node v is robust to the features $h_v^{(l)}$"? This statement is too informal and the authors should characterize robustness in rigorous mathematical expressions.

### Questions
1. Why the deviation is in this form: $σ =\sqrt{p2ln(1.25/δ)/ε}$ in DPGC in section 4.2?
2. In Table 1 why adversarial training can hurt the robustness of DRAGON for most cases?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework DRAGON that is robust against Graph Injection Attack. 
The framework first adopts an edge denoising module implemented by an auto-encoder.
Then, a Differentially-Private Mixture-of-Experts (DPMOE) layer is used as a robust Graph Convolution layer.
Extensive experiements verify the effectiveness and efficiency of DRAGON.

### Strengths
1. The proposed framework holds siginificant perfromance superiority over defense baselines against various types of attacks.
2. The proposed framework is scalable to large graphs, like AMiner with more than 600,000 nodes.

### Weaknesses
1. The module of DRAGON is not first proposed in the paper, which slightly limits the novelty of the proposed framework.
2. It would be better if the presentation is more clear. For example, the notations in the lemma are not well introduced. The setting of the attack and defense is not included as well. 
3. The whole framework is quite complex and not in an end-to-end manner.
It includes quite a few hyperparameters, and choosing a propoer GNN backbone seems to matter, which would be a concern when applied to real-world scenarios.

Other concerns are listed in Questions.

### Questions
1. How is the auto-encoder trained? Is it trained on the clean graph or trained on the attacked graph? 
If the denoising module is trained on the attacked graph, why auto-encoder enjoys such a good performance in recovering clean graph structrue?
Including more discussion about the intuition why the denosing part is effective would be better. 
2. What the reuslts would be if the denoising module is compiled with other defense model?  For example, GATGuard + DMGAN. 
It looks like the two modules of DRAGON can be decoupled. 
3. It is amazing that DRAGON is so efficient. Dose the reported time in Table 18 include the training time of DMGAN?
4. DRAGON adopts other defense model as backbone, which could seems a little unfair. I wonder how DRAGON would perform when compiled with other basic GNNs like GCN? Is it sill competitive?
5. Why the baselines like GATGuard and EvenNet not coupled with AT?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
