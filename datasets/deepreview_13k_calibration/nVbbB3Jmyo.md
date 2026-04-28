# Degree-aware Spiking Graph Domain Adaptation for Classification

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Spiking Graph Networks (SGNs) have garnered significant interest from both researchers and industry due to their ability to address energy consumption challenges in graph classification. However, SGNs are typically inference under the same distribution of training dataset, which is difficult to satisfy in real applications. In this paper, we first propose the domain adaptation problem in SGNs, and introduce the novel framework named \textbf{De}gree-aware \textbf{S}piking \textbf{G}raph \textbf{D}omain \textbf{A}daptation for Classification (\method{}). To address this problem, we propose solutions in terms of three aspects: node distribution-aware personalized spiking representation, graph feature distribution alignment, and pseudo-label distillation. Firstly, we introduce the personalized spiking representation method that varies with node degrees. The difficulty of triggering a spike is determined by the node degree, allowing this personalized approach to capture more expressive information for classification. Then, we propose the graph feature distribution alignment module that is adversarially trained using membrane potential against a domain discriminator, efficiently maintaining high performance and low energy consumption in the case of inconsistent distribution. Additionally, we extract consistent predictions across two spaces to create reliable pseudo-labels, effectively leveraging unlabeled data to enhance graph classification performance. 
Extensive experiments on benchmark datasets validate the superiority of the proposed \method{} compared with baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a framework called DeSGDA to tackle the problem of domain adaptation in spiking graph neural networks. DeSGDA combines three key components: a degree-aware spiking representation that adapts spiking thresholds based on node degree, adversarial distribution alignment to minimize discrepancies between source and target domains, and pseudo-label distillation to improve model performance on unlabeled target data. The authors provide theoretical bounds on the generalization error of their framework and validate its effectiveness through extensive experiments on multiple benchmark datasets, demonstrating DeSGDA’s superiority over other baseline methods in terms of classification accuracy and energy efficiency.

### Strengths
1. The DeSGDA framework is a multi-faceted approach that includes personalized spiking representation, adversarial distribution alignment, and pseudo-label distillation.
2. The authors provide theoretical bounds on the generalization error for spiking graph domain adaptation.
3. The paper conducts extensive experiments on several benchmark datasets, comparing DeSGDA with a wide range of competitive baselines. This comprehensive evaluation demonstrates the model’s effectiveness and superiority over other methods.

### Weaknesses
1. This paper studies an A+B problem. The authors bring together two distinct challenges—spiking neural networks and domain adaptation—within the context of graph data. However, the novelty of this problem setup raises questions about the practical relevance and contribution of the paper, as such a scenario may be uncommon in real-world applications.
2. The authors mention in the Introduction that this problem may exist in Electroencephalography (EEG) data, however, they did not conduct experiments on such data. The datasets used in this paper are mainly protein, molecular, and chemical graphs, can the authors give explanations about what are the applicable scenarios on these data? especially given that, in these domains, accuracy often takes precedence over timeliness.
3. The adversarial learning on both source and target domains, and the pseudo-labeling strategy on target graphs are very familiar techniques in domain adaptation methods. The contribution is limited.
4. The methodology assumes that the node degree is a key factor for domain adaptation in spiking graph networks. More explanation on why “setting higher thresholds for high-degree nodes and lower thresholds for low-degree node” should be added.
5. In some real-world datasets, besides the degree, other structural or feature-based factors might impact the domain shift. Focusing heavily on degree-aware thresholds may overlook other graph properties.
6. The definition of V_th is not given.

### Questions
see above.

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
3

### Summary
This paper proposes the problem of spiking graph domain adaptation and introduce a novel framework DeSGDA. This framework enhances the adaptability and performance of SGNs through three key aspects: node degree-aware personalized spiking representation, adversarial feature distribution alignment, and pseudo-label distillation. DeSGDA enables more expressive information capture through degree-dependent spiking thresholds, aligns feature distributions via adversarial training, and utilizes pseudo-labels to leverage unlabeled data effectively.

### Strengths
1. The structure of the paper is clear and easy to follow.
2. This paper explores the spiking graph domain adaptation problem, which has been neglected in graph domain adaptation.
3. The paper conducts comprehensive experiments to demonstrate the performance of proposed method.

### Weaknesses
1. The novelty seems limited. The core idea of DeSGDA is three parts, i.e., node degree-aware personalized spiking representation, adversarial feature distribution alignment, and pseudo-label distillation. However, the second part is domain alignment[1] and the third part is pseudo-labeling[2, 3]. There are both popular ideas in domain adaptation. The technical contribution is a little weak.
2. The motivation of this paper is not clear. It is recommended that the authors further explain the purpose of using spiking graph neural networks in graph domain adaptation so that readers can understand the contribution of this paper.
3. The authors provide an energy efficiency analysis, which is commendable. Can the authors further compare the training time and memory of DeSGDA with graph domain adaption methods?

### Questions
1. From Tables 1 and 2 in the experimental section, the WL subtree method achieves better performance in many cases than the well-designed graph domain adaptation methods. Can the author explain why?
2. In Figure 3, the DeSGDA method is not found. Does SGNN in the figure represents DeSGDA?
3. What is the effect of directly replacing the spiking graph neural networks with commonly used graph neural networks, such as GIN and GCN, combined with adversarial feature distribution alignment and pseudo-label distillation?

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
4

### Summary
This paper introduces a novel framework named DeSGDA (Degree-aware Spiking Graph Domain Adaptation for Classification) for addressing cross-domain graph classification. DeSGDA tackles the domain adaptation challenge by employing three components: degree-aware personalized spiking representation, adversarial feature distribution alignment, and pseudo-label distillation. Extensive experiments on benchmark datasets demonstrate the superiority of DeSGDA compared to other state-of-the-art methods, highlighting its potential for deployment on low-power devices due to its energy-efficient design.

### Strengths
1. This paper is a pioneer work to address domain adaptation in spiking graph neural networks.
2. Degree-aware spiking neural networks (SNNs) is an interesting and effective idea, where the spiking threshold is customized based on node degrees. This degree-dependent approach enhances the model's ability to capture informative node representations, significantly improving its performance in varied domain settings.
3. The authors conduct extensive experiments across various datasets and different domain shift scenarios.
4. The paper provides the theoretical analysis to present DeSGDA's generalization capabilities for cross-domain graph classification.

### Weaknesses
 1. There shows many inconsistencies in the reported experimental results, which makes me much unconfident about the real performance of proposed method:
    - In Figure 2, the reported results for the "PROTEINS" dataset do not match those presented in Table 1, Table 9, or Table 12. Specifically, in Figure 2, P1-->P0 (GIN) performance is about 0.75~0.76. However, in Table 1, the performance is 84.6; in Table 9, the performance is 78.4; in Table 12, the performance is 84.3. Any of the data in the three tables is inconsistent with the results in Figure 2. There are also some other situations that do not match. This difference raises significant questions about the consistency of experimental results. Further clarification is must to confirm accuracy and reproducibility.
    - In Figure 3, there is no label corresponding to "DeSGDA".

 2. In this paper, the authors first make the assumption that  "Nodes with higher degrees have more neighbors, and the aggregation operation in Eq. 1 allows for more significant feature accumulation, making it easier for these nodes to trigger spikes compared to those with fewer neighbors. " This assumption is valid if a direct summation-based neighbor information aggregation is used. However, it remains unclear if this holds for other aggregation methods, such as GAT which is weighted average based on attention score, and GCN which is weighted average based on structural information. Further discussion on this assumption is needed.

3. I really appreciate the degree-aware personalized spiking representation design. However, this paper aims to tackle with the OOD problem. It shows limited technical contribution for graph domain adaptation. The adversarial learning and pseudo-labeling are both well-investigated method in existing DA works.

4. The experiments primarily focus on binary classification tasks using standard graph classification datasets. More complex experiment setting, e.g., multi-class scenarios rather than all binary classification, is welcome to fully assess the model’s capability.

5. The paper does not adequately explain why DeSGDA outperforms general graph domain adaptation methods, like DEAL, CoCo, and A2GNN. An analysis of how DeSGDA specifically enhance performance beyond standard graph DA approaches would better highlight its advantages.

6. Since the degree-aware component design is crucial  to the performance improvements of DeSGDA, it is recommended to provide specific theoretical analysis for this component to strengthen the core contribution. Of course, I understand that this is often not easy, just as a suggestion that the author can consider for future work.

### Questions
Please address my concerns in the weakness part.

Due to concerns about the inconsistency of the experimental results, I will initially give a neutral score. I will decide whether to raise (or lower) my score based on the author's responses during the discussion phase.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Spiking Graph Networks (SGNs) help reduce energy use in graph classification but fail with out-of-distribution data. This paper introduces a new framework, DeSGDA, for spiking graph domain adaptation. DeSGDA improves classification by using node degree-aware spiking signals, aligning feature distributions adversarially, and leveraging pseudo-labels from unlabeled data. Experiments show it outperforms other methods.

### Strengths
Problem Statement: The paper clearly articulates the domain adaptation problem in SGNs, providing a well-defined background, making it easy to understand. 

Innovation: The design of effective pseudo-labels tailored to different distributions is a clever approach.

Methodology: The methods employed are appropriate and rigorous, with a well-reasoned experimental design and a transparent data collection and analysis process.

Writing Quality: The writing is fluent, the structure is logical, and it is easy to read and comprehend.

### Weaknesses
The description in figure 1 is too simplistic.

### Questions
The paper is well written and I don't have any concerns.

### Soundness
4

### Presentation
4

### Contribution
4
