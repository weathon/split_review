# GPromptShield: Elevating Resilience in Graph Prompt Tuning Against Adversarial Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The paradigm of ``pre-training and prompt fine-tuning", with its effectiveness and lightweight characteristics, has rapidly spread from the language field to the graph field. Several pioneering studies have designed specialized prompt functions for diverse downstream graph tasks based on various graph pre-training strategies. These prompts concentrate on the compatibility between the pre-training pretext and downstream graph tasks, aiming to bridge the gap between them. However, designing prompts to blindly adapt to downstream tasks based on this concept neglects crucial security issues. By conducting covert attacks on downstream graph data, we find that even when the downstream task data closely matches that of the pre-training tasks, it is still feasible to generate highly misleading prompts using simple deceptive techniques. In this paper, we shift the primary focus of graph prompts from compatibility to vulnerability issues in adversarial attack scenarios. We design a highly extensible shield defense system for the prompts, which enhances their robustness from two perspectives: Direct Handling and Indirect Amplification. When downstream graph data exhibits unreliable biases, the former directly combats invalid information by adding mixed multi-defense prompts to the input graph's feature space, while the latter employs a training strategy that circumvents invalid part and amplifies valid part. We provide a theoretical derivation that proves their feasibility, indicating that unbiased prompts exist under certain conditions on unreliable data. Extensive experiments across various adversarial attack scenarios indicate that the prompts within our shield defense system exhibit enhanced resilience and superiority. Our work explores new perspectives in the field of graph prompts, offering a novel option for downstream robust prompt fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to graph prompt tuning focused on robustness in adversarial attack scenarios. It proposes a highly extensible shield defense system with a hybrid multi-defense prompt and robust prompt tuning strategy, demonstrating theoretical feasibility. Extensive experiments in few-shot scenarios under various adversarial attacks show that their strategies significantly enhance prompt tuning resilience in downstream biased tasks. The use of feature-based prompts allows real-time adjustments, and the paper highlights the effectiveness of their methods in both adaptive and non-adaptive attack scenarios.

### Strengths
The proposed mixed multi-layer defense strategy in this paper demonstrates technical innovation by combining various defense mechanisms, such as feature-based prompting and real-time adjustments. This approach significantly enhances the system’s tolerance to adversarial attacks, offering a fresh perspective on the research of graphic prompting adjustment systems.

### Weaknesses
One weakness of the paper is the absence of a comparative analysis with existing systems or defense strategies against adversarial attacks. 

The paper primarily focuses on theoretical analysis and experimental validation in controlled settings. However, the lack of real-world implementation or case studies hinders the practical applicability assessment of the proposed method. To enhance the relevance and impact of the research, future work could involve implementing the system in real-world scenarios and evaluating its performance in practical applications.

The evaluation section of the paper might benefit from a more comprehensive selection of evaluation metrics to assess the proposed method’s performance accurately. Specifically, incorporating additional metrics such as computational efficiency, scalability, or user experience aspects could provide a more holistic evaluation of the system’s capabilities and limitations. Including a diverse set of evaluation criteria would offer a more thorough understanding of the method’s strengths and weaknesses.

The paper could further strengthen its impact by discussing the generalizability of the proposed method to different types of adversarial attacks or diverse datasets. Providing insights into how the approach could be adapted or extended to address a broader range of security challenges would enhance the paper’s contribution to the field.

### Questions
Refer to the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores enhancing the robustness of graph prompt-tuning methods against adversarial attacks in graph neural networks (GNNs). It identifies a vulnerability in current prompt-based methods, which are highly susceptible to adversarial alterations. The proposed solution is a "shield defense system" that enhances robustness through two strategies: Direct Handling and Indirect Amplification. Direct Handling customizes multi-defense prompts based on node-specific attributes, targeting biased nodes introduced by attacks, while Indirect Amplification leverages few-shot learning and selectively focuses on untainted information, thereby circumventing the misleading data introduced by adversaries. Theoretical validation demonstrates that this approach can maintain unbiased outputs despite adversarial perturbations. Experimental results show that the defense system enhances resilience under various attack scenarios, outperforming existing prompts in maintaining accuracy and robustness.

### Strengths
The idea and structure is easy to follow.

### Weaknesses
1. Some of the tables are confusing, for example, the table 1. Pre-Training Strategies & Prompts appear simultaneously in the top left corner. Should we design the table in a better way or use other charts to represent these results?
2. Section 2 Related work, if there is no more subsection 2.1, is not necessary.
3. The whole framework should have a figure to clearly show the stages of prompt design and robust optimization strategies

### Questions
1. Why other methods' results are getting close to the proposed methods in 10-shot experiments? Is it possible that other methods will outperform the proposed methods with even more shots?
2. Adding the figures to represent prompt design and robust optimization strategies stages could be better.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a robust graph prompt learning method based on adversarial training to defend Graph Neural Networks (GNNs) against adversarial attacks. The method begins by identifying nodes typically targeted in these attacks, such as low-degree nodes, nodes with low central similarity within multi-hop subgraphs, and nodes linked to adversarially perturbed edges. Next, the approach fine-tunes three distinct types of graph prompts, each corresponding to one of the targeted node types. The objective of the prompt tuning process is to ensure: (1) smoothness in node embeddings within multi-hop subgraphs across the three types of graph prompts, (2) consistency between prompt-enhanced and unprompted node embeddings, and (3) smoothness across embeddings from different types of prompts. Finally, the study applies this method to multiple graph prompt learning models, evaluating its defense effectiveness against non-adaptive attacks and its performance in combination with other defense strategies for adaptive and graph poisoning attacks.

### Strengths
First of all, this is an interesting work in investigating robust graph prompt tuning to increase the stability of GPL against potential graph poisoning attacks. Especially, if the test graph structure is intentionally manipulated, this method offers a solution to suppress the impact of the poisoning efforts over the decision of GPL.

### Weaknesses
There are several points that need to be strengthened: 

1/ This work only focuses on node classification-oriented GPL and does not discuss graph poisoning attacks targeting at manipulating node attributes. It is not clear if the proposed robust prompt tuning method can be applied to edge or graph level learning tasks and can be adapted to both node- and edge-manipulation based attacks. I am asking this as GPL is a multi-task system that can transfer knowledge between different types of GNN learning tasks (node, edge and graph classification). From this perspective, the evaluation in this study is not sufficient. Extending the coverage over more graph datasets and GNN learning tasks should be considered. I'd recommend the author refer to the dataset choice and learning task configurations in [1]. 

2/ The theoretical proof in Section 4.3 is not associated with the main claim (robust prompt tuning) in this work. This theoretical analysis should be dedicated to explain how the robustness is improved via the proposed tuning approach. However, the link between Section 4.3 and the algorithmic design is unclear in the current submission. 

3/ The ablation study may also need to consider one situation: what if every node belonging to the three types (low degree, low central similarity and out-of-distribution nodes) has the same graph prompting function ? Besides, which types of the nodes should be given more weights in the robust tuning process, or they are handled equally in adversarial attacks ? 

4/ What are out-of-distribution nodes in a graph? Citing the paper (Li et al) is not enough. Further discussion regarding what these nodes are and why they are concerned in adversarial attacks should be involved. 

5/ How do you choose the threshold values $\tau_{degree}$ and $\tau_{sim}$ ? Are they set empirically, or is there any protocol to choose adaptively in different GNN adversarial attack scenarios ? Similarly, how do you choose $\tau_{tune}$ in Eq.15 ? Does it mean you completely exclude the subgraphs if the embeddings of nodes in these subgraphs meet the condition in Eq.15? Will it also bring harm to the utility of the trained GPL as it excludes information from the training process. 

6/ As an adversarial training method, it is not surprised to see the proposed defensive graph prompts can mitigate one attack method when they are trained to be resilient to this attack. I am wondering if the proposed method has the transferability. In particular, if it is trained with the perturbed graph using one of the attack methods (MetaAttack, Heuristic attack, Random attack, DICE) can be also resilient to the other three attacks.

### Questions
Please check the question raised in the comments concerning the weakness of this study.

### Soundness
3

### Presentation
3

### Contribution
3
