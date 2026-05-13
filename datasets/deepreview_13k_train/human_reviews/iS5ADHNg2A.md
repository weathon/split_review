# Deceptive Fairness Attacks on Graphs via Meta Learning

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
We study deceptive fairness attacks on graphs to answer the following question: \textit{How can we achieve poisoning attacks on a graph learning model to exacerbate the bias deceptively?} We answer this question via a bi-level optimization problem and propose a meta learning-based framework named \method. \method~is broadly applicable with respect to various fairness definitions and graph learning models, as well as arbitrary choices of manipulation operations. We further instantiate \method~to attack statistical parity and individual fairness on graph neural networks. We conduct extensive experimental evaluations on real-world datasets in the task of semi-supervised node classification. The experimental results demonstrate that \method~could amplify the bias of graph neural networks with or without fairness consideration while maintaining the utility on the downstream task. We hope this paper provides insights into the adversarial robustness of fair graph learning and can shed light on designing robust and fair graph learning in future studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper first defines deceptive fairness attacks on graphs, which is a new type of threat model that is compatible with many of the existing settings. Then the paper proposes FATE, a framework that models this problem via a bi-level optimization treatment, and offers a solution using meta-learning. Finally, the paper empirically confirmed the effectiveness of their framework on real-world datasets in the task of semi-supervised node classification.

### Strengths
1. Very clear motivation and problem formulation
2. Extensive experimental results and clear explanations.
3. Theoretical analysis is necessary and appears to be correct.

### Weaknesses
The terminology of "deceptiveness" may be confusing and is not clearly explained, from an intuitive level, in the manuscript. Specifically, while the paper mentions that the attacks should be imperceptible, it does not fully articulate what constitutes imperceptibility in the context of graph data. It's unclear whether this refers to the magnitude of edge perturbations, the number of modified edges, or some other measure. Furthermore, the connection between maintaining downstream task performance and the "deceptiveness" of the attack could be more explicitly defined. It is not immediately obvious why a drop in performance would necessarily make an attack less deceptive, as an attacker might still achieve their fairness goals even with some performance degradation.

### Questions
What's the intuition behind the method being "meta-learning"? It appears that this is not a typical treatment of meta-learning in graph representation learning.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper Deceptive Fairness Attacks on Graphs via Meta Learning, the authors delve into the realm of deceptive fairness attacks on graph learning models, aiming to amplify bias while simultaneously maintaining or improving utility in downstream tasks. They formalize this challenge as a bi-level optimization problem, where the upper level seeks to maximize the bias function according to a user-defined fairness definition, and the lower level aims to minimize a task-specific loss function.

To address this challenge, the authors introduce FATE, a meta-learning based framework designed to poison the input graph using the meta-gradient of the bias function with respect to the input graph. FATE is rigorously evaluated and compared with three baseline methods: Random, DICE-S, and FA-GNN, across three real-world datasets in the context of binary semi-supervised node classification with binary sensitive attributes.

FATE distinguishes itself through two strategies: edge flipping (FATE-flip) and edge addition (FATE-add), as opposed to other baseline methods which only perform edge addition, and consistently outperform the baseline methods in fairness attacks. Unlike some baseline methods that sometimes fail to attack individual fairness, FATE maintains its effectiveness, amplifying bias while achieving the highest micro F1 scores in node classification. This dual success highlights FATE's deceptiveness, as it can increase bias while simultaneously enhancing or maintaining model performance.

### Strengths
1. Clear Structure and Argumentation: The paper is well-organized, providing a clear and compelling argument for the importance of studying deceptive fairness attacks in graph learning models. 
2. Robust Experimental Design: The experimental design is of high quality, with all mathematical symbols and notations meticulously explained.
3. Transparent Results Presentation: Results are presented clearly and concisely, with visual aids and detailed explanations that make the findings accessible and easy to understand, showcasing the effectiveness of the FATE framework.
4. Problem Novelty: The proposed work focuses on adversarial robustness of fair graph learning, which needs more exploration.

### Weaknesses
It is noted the below are minor weaknesses:
1. Grammatical Typos: There are minor grammatical errors present, such as in Section 6.1 on page 6, where the phrase "It randomly deleting edges..." should be corrected to "It randomly deletes edges...". 
2. Incomplete Introduction of Fairness Definitions: In Section 2B, when algorithmic fairness definitions are introduced, the paper provides English definitions but omits corresponding mathematical definitions. Including these mathematical definitions would enhance clarity, especially as the individual fairness definition is important when analyzing results. The lack of mathematical formulation makes it difficult to precisely understand the bias function and how it is being optimized in the bi-level optimization problem.
3. Inconsistent Organization: The paper utilizes a letter-based organization in some sections and a numerical organization in others. For instance, in Section 4, ideas are laid out numerically but then referred to using letters (A, B,...). This inconsistency makes it harder to follow the flow of the paper and connect the different parts of the methodology.

### Questions
1. Can more be discussed on the potential other bias functions besides statistical parity? 
2. Do the authors believe this attack scenario is reasonable in real-world settings? Although an example is provided of a banker and has been used in prior work, but it feels somehow contrived and would look forward to perhaps more realistic settings where the attackers have more restricted access (e.g., visibility of the existing graph and only able to construct and connect new nodes, etc.).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates deceptive fairness attacks on graph learning, introducing a meta-learning-based framework, FATE. Designed with broad applicability, FATE targets biases in graph neural networks. Using real-world datasets for semi-supervised node classification, the authors demonstrate FATE's ability to amplify biases without compromising downstream task utility. This emphasizes the covert nature of these attacks. The study hopes to spotlight adversarial robustness in fair graph learning, guiding future endeavours towards creating robust and equitable graph models. The paper is a commendable exploration of the crossroads of fairness, adversarial attacks, and graph learning.

### Strengths
The topic of this paper is attacking the fairness of GNNs by a poisoning attack setting, which is valuable for building trustworthy GNNs. The method in this paper is easy to follow. In the experimental evaluations, the authors attempt to provide deep analysis upon validating the effectiveness of the proposed method, which is great for the audience to obtain insights and understanding of the vulnerability of GNN fairness.

### Weaknesses
1.Limited novelty. The limitation of existing works is weak (section 2-c). For limitation 1, this paper still only attacks one fairness concept when generating the adversarial graph. For limitation 2, the operation space depends on the practicality of the attack. For limitation 3, the specially designed module for maintaining performance is not presented in this paper. Authors are suggested to revise this part to highlight the contribution of this paper.

2.Inaccurate/Unclear statements. For the budget limitation in the “capability of the attacker”, please be aware that the ||.||_{1,1} (according to the common definition of matrix norm) focuses on the maximum number of perturbations among nodes and cannot reflect the number of total perturbations. The definition of d(G,\tilde G) should also include the changes on X. In the 4-c, the \hat{y_(i,1)} discussing the sensitive attributes is repeated with that defining the label in 4-B.

3.The design for keeping the performance of GNNs is not presented in the equation (1). Authors are suggested to discuss why the proposed method can achieve the performance goal, as presented at the beginning of this paper.

4.The operation in equation 6 should be explained with more details to show how to handle different connection statuses and gradient statuses. Moreover, the flip and add operations should also be explained to show how they happen.

5.For definition 1, authors are suggested to explain why the conclusion from IID assumption can be used in the graph data, where nodes are non-IID. Moreover, according to the definition of CDF, the integral starts from -infinity. Authors are suggested to revise related symbols or statements in section 4.

6.In section 5, authors are suggested to explain that L_s is the Laplacian matrix of S, avoiding the confusion of audience who are not familiar with fairness.

7.Limited evaluation. It is worth noting that the surrogate model is SGC while the target model is GCN, and they almost have extremely similar architecture. Authors are suggested to evaluate the effectiveness of the proposed method on other target GNN architectures (e.g., GAT, GraphSAGE) to follow the attack setting of this paper (section 3.1, attackers have only access to the graph data).

8.Evaluation metric. It is worth noting that the fairness of GNNs is at the cost of performance. Although it is great to see the fairness deduction with limited performance cost. However, FA-GNN works well in a lot of cases. Considering that both fairness and model performance is the design of this paper, authors are suggested to compare the (\delta SP)/(\delta Acc) to evaluate the bias increment on unit acc cost.

9.Confusing analysis on the effect of the perturbation rate. I understand that the authors attempt to show insights on the adversarial graph. However, it is hard to digest the operation (delete or add) on the same/different label/attribute. The discussion in Figure 1-b is also confusing. I suppose that detailed explanations of what exactly happened on each bar will make a more clear discussion. Authors are suggested to revise the paragraphs related to figures 1 and 2.

10.According to the effectiveness table results, authors are suggested to explain why the proposed method can improve the performance of GNNs.

11.On the “Effect of the perturbation rate” in section 6.2. Intuitively, more perturbations will make the learned parameters farther from that learned from the original graph. Thus, the availability scope of the learned adversarial graph will be limited by the perturbations, i.e., the higher budget will result in more unexpected behaviours of GNN trained on the poisoned graph. Authors are suggested to revise and discuss it in this paper, which is the limitation of the gradient-based attack method.

### Questions
Refer to the weakness part.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper "Deceptive Fairness Attacks on Graphs via Meta Learning" proposes a meta-learning approach for exacerbating demographic bias in the prediction of a given, unknown, victim model operating on the input graph; It is based on the optimization of a surogate model to define edges (or features to modify). It shows that their approach is able to manipulate edges and features  of the graph so that the performance of different victim models remains constant while the bias is increased.

### Strengths
Very interesting approach and results. 

Looks theoretically sound.

### Weaknesses
The paper sometimes lacks of carity, with some defintions not given (e.g., Y never defined in sec 2) or only in the appendix. In fact I had to go many times in the appendix to understand the core concepts of the approach, which is not very comfortable for the reader. I feel the formalization of the problem/method should include some separated notation for the victim and the surogate model, cause it was a bit confusing. Maybe what we want is that we are good for any victim model from a given distribution of victims ? Setting the problem like this would made the problem easier to understand from my point of view. Results are very hard to follow as some notation are not specified at all (e.g., Ptb which is the perturbation budget but we have to infer it) and every important details as the evaluation metrics are only given in the appendix (I understand the choice for a lack of space but only give some words on it (e.g. simply say delta sp is the bias) and refer to the corresponding section in the appendix would be helpful. Also please better specify the experimental questions you are inspecting in each section of the experimental part, because we can be a little lost at the first read.

### Questions
1. I wish the paper could have inspected some possible ways to prevent such attacks. The approach announce that the goal is to better understand. Ok, but what can we do, that would be positive, from the outcomes of the model ? Would it be possible to give some insights for good ways to defend from such attacks ? 

2. The considered bias is not fully defined in sec 4, for instance for the instantiation 1: you give the way you estimate both pdf but finally what is the score considered ? an mse, a kl, or what ?  Also, would it be possible to consider a targeted attack that would favor a specific population ? 

3. Would it be possible to specify more deeply $\nabla_{\cal G} \Theta^{(T)}$ ? is it equal to $ \epsilon \nabla_{\cal G} \nabla_\Theta l({\cal G}, Y,\Theta,\theta)|_{\Theta^{(T-1)}}$, with $\epsilon$ the step size of update of the surogate ? 

4. I have difficulties to well understand the recursive definition of (3) and its connection with (2). Could you clarify please ?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
