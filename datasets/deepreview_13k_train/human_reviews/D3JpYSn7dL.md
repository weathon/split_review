# An Instance-Level Framework for Multi-tasking Graph Self-Supervised Learning

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
With hundreds of graph self-supervised pretext tasks proposed over the past few years, the research community has greatly developed, and the key is no longer to design more powerful but complex pretext tasks, but to make more effective use of those already on hand. There have been some pioneering works, such as AutoSSL and ParetoGNN, proposed to balance multiple pretext tasks by global loss weighting in the pre-training phase. Despite their great successes, several tricky challenges remain: (i) they ignore instance-level requirements, i.e., different instances (nodes) may require localized combinations of tasks; (ii) poor scalability to emerging tasks, i.e., all task losses need to be re-weighted along with the new task and pre-trained from scratch; (iii) no theoretical guarantee of benefiting from more tasks, i.e., more tasks do not necessarily lead to better performance. To address the above issues, we propose in this paper a novel multi-teacher knowledge distillation framework for instance-level Multi-tasking Graph Self-Supervised Learning (MGSSL), which trains multiple teachers with different pretext tasks, then integrates the knowledge of different teachers for each instance separately by two parameterized knowledge integration schemes (MGSSL-TS and MGSSL-LF), and finally distills it into the student model. Such a framework shifts the trade-off among multiple pretext tasks from loss weighting in the pre-training phase to knowledge integration in the fine-tuning phase, making it compatible with an arbitrary number of pretext tasks without the need to pre-train the entire model from scratch. Furthermore, we theoretically justify that MGSSL has the potential to benefit from a wider range of teachers (tasks). Extensive experiments have shown that by combining a few simple but classical pretext tasks, the resulting performance is comparable to the state-of-the-art competitors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of graph self-supervised learning and presents a multi-teacher knowledge distillation framework. Specifically, it trains multiple teachers with different pretext tasks, then integrates the knowledge of different teachers for each instance separately by two parameterized knowledge integration schemes (MGSSL-TS and MGSSL-LF), and finally distills it into the student model.

### Strengths
1.	The paper is clearly motivated and well-written.
2.	Theoretical analysis is provided to show that the proposed method has the potential to benefit from more teachers.

### Weaknesses
1.	Experiments on other downstream tasks (e.g. node clustering, link prediction, and partition prediction as in AutoSSL and ParetoGNN) are missing.
2.	It seems better to add the discussion and comparison on related works about graph knowledge distillation and recent self-supervised graph learning.
a.	Quantifying the Knowledge in GNNs for Reliable Distillation into MLP, ICML2023.
b.	Extracting Low-/High- Frequency Knowledge from Graph Neural Networks and Injecting it into MLPs: An Effective GNN-to-MLP Distillation Framework, AAAI2023.
c.	Knowledge Distillation Improves Graph Structure Augmentation for Graph Neural Networks, NeurIPS2022.
d.	Decoupled Self-supervised Learning for Graphs, NeurIPS2022.
e.	Graph Self-Supervised Learning with Accurate Discrepancy Learning, NeurIPS2022.
f.	GraphMAE: Self-Supervised Masked Graph Autoencoders, KDD2022.
3.	Typo: In the line2 of page6, “…this paper proposes two…” is miswritten as “…this paper propose stwo…”.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach in graph self-supervised learning called Multi-teacher Knowledge Distillation Framework for Instance-level Multitasking Graph Self-Supervised Learning (MGSSL). MGSSL uses multiple teachers for 
different tasks, integrating their knowledge for each instance, and distills it into a student model. This method shifts from loss weighting in pre-training to knowledge integration in fine-tuning, allowing compatibility with numerous tasks without retraining from scratch. Theoretical justifications are provided, and extensive experiments show that MGSSL's performance is comparable to state-of-the-art methods by combining simple classical tasks.

### Strengths
+ The proposed multi-teacher knowledge distillation framework for instance-level multitasking graph self-supervised learning (MGSSL) is a novel approach. It addresses the limitations of existing methods by focusing on instance-level requirements and scalability to new tasks.

+ The paper successfully identifies and tackles key challenges in the field: the need for localized combinations of tasks for different instances, poor scalability to emerging tasks, and the lack of theoretical guarantees for performance improvement with more tasks.

+ Providing theoretical justification for the potential of MGSSL to benefit from a wider range of teachers (tasks) adds credibility and depth to  the research.

+ The extensive experiments and the resulting performance being comparable to state-of-the-art competitors lend strong empirical support to the proposed method.

### Weaknesses
 - While the paper introduces a novel framework, a more thorough evaluation of the scalability and computational costs of the proposed framework, especially in large-scale settings, would significantly strengthen the work. Specifically, it would be beneficial to see a comparative analysis of the computational overhead introduced by MGSSL when applied to datasets of varying sizes and complexities. For instance, how does the training time and memory usage scale with the number of nodes and edges in the graph? How does the number of teachers impact these metrics? Providing benchmarks on standard large-scale graph datasets, such as those in the Open Graph Benchmark, would offer valuable insights into the practical applicability of MGSSL.

- The author only compares their work with AutoSSL [1] in Table 1. Since AutoSSL [1] is a work from 2021, I suggest that the author should compare their work with more recent studies, such as ParetoGNN [2]. Comparing MGSSL to a wider range of state-of-the-art methods, including those published in recent top-tier conferences, would provide a more comprehensive understanding of its performance and advantages. This would further enhance the quality of the paper by demonstrating the competitiveness of MGSSL in the current research landscape.

### Questions
Please see my comments in Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents the MGSSL, which is a a novel multi-teacher knowledge distillation framework for instance-level Multi-tasking Graph SSL. This framework conducts knowledge integration in the fine-tuning phase, distilling the knowledge from multi-teacher models to the student models, which achieves an instance-level integration module. The authors provided sufficient theory to prove this framework can benefit from a wider range of teachers, and the experimental part also achieved competitive results.

### Strengths
My opinions towards the strengths of this papers are:
   + Originality. This paper proposes the idea of integrating knowledge in the fine-tuning phase, and thus achieved a breakthrough at the instance-level requirements for the first time.
   + Quality. This paper has clear method description, sufficient experiments, and competitive results.
   + Clarity. The figures of the methods plus theoretical proof clearly expressed the method of the paper. 
   + Significance. A framework theoretical guideline brings new ideas to solve Graph Self-Supervised Learning problems.

### Weaknesses
First of all, the authors say that they integrate knowledge from multiple teacher models to the student models. I wonder what specific type of knowledge is being integrated into the student models. For instance, are these high-frequency or low-frequency components of knowledge, and how are they measured in the context of this multi-tasking framework?  I think the knowledge may be the common knowledge from the multiple teacher models, but this is not explicitly stated. The authors may present more analysis on the nature of the integrated knowledge, perhaps with a quantitative breakdown of the different knowledge components being transferred.

Second, I find the paper not easy to follow, particularly due to the density and complexity of the symbols used. The symbols maybe complex for me to understand. As a result, I suggest the authors to simplify and well structure the used symbols. A table summarizing all symbols and their meanings would significantly improve readability.

### Questions
My two concerns are as the Weaknesses part. Pls refer to Weaknesses.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper designs a multi-tasking graph self-supervised learning framework to improve downstream graph learning performance. Different from the conventional multi-tasking SSL, it proposes a multi-teacher KD framework with an instance-level knowledge integration module, with the parameterized knowledge distillation module, which can output instance-wise knowledge combination weights. The proposed approach suggests a significant performance improvement over other single-pretext tasks, e.g., vanilla MTL, AutoSSL, and ParetoGNN.

### Strengths
1. This paper is well-written and provides sufficient empirical observations of combining multiple self-supervised tasks.
2. The experiment for node classification is conducted over a broad datasets and the improvement is significant.
3. Some theoretic results can be directly supported by the empirical results.
4. The proposed method with weighing different teachers for each node is novel.

### Weaknesses
1. The main concern is the experiments in this paper are only related to the classification task in a multi-tasking setting, while the proposed method is task-irrelevant. Although the some vision tasks are involved in the appendix, the graph-related tasks, such as node clustering and link prediction, should be investigated. It is crucial to demonstrate the versatility of the proposed framework across diverse graph learning scenarios. The absence of experiments on tasks like node clustering and link prediction raises questions about the method's general applicability beyond classification. Specifically, it's unclear how the instance-level knowledge integration would perform in tasks where the objective isn't directly tied to class labels, such as community detection or predicting missing links between nodes. This limitation undermines the claim of task-irrelevance.
2. The Eq. (4) is quite misleading. The proposed distillation is in an offline fashion, and the optimality of teacher has already in the objective. As a result, the constraint is a little bit unnecessary. Also, the parameters for optimization are not clearly presented in the objective. The formulation of the knowledge distillation process needs clarification. The objective function in Eq. (4) appears to be optimizing for a student model given a fixed teacher. However, the text implies that the teacher is an ensemble of models, and the weights for this ensemble are also learned. This discrepancy needs to be addressed. Furthermore, the specific parameters that are being optimized within the objective function need to be explicitly defined. It is not clear how the weighting function is optimized in conjunction with the student model parameters. The lack of clarity on the optimization process makes the method difficult to understand and reproduce.

### Questions
1. In page 2, you claim “Secondly, balancing multiple tasks by loss weighting during the pre-training phase makes it hard to scale the pre-trained model to emerging tasks. To incorporate new tasks, it requires to re-pretrain a new model from scratch.” Is it an over- pessimistic claim for the existing methods? Which may implicit exaggerate the contribution of the proposed method.
2. How do you perform vision task in Appendix 10? Please provide more details for the graph construction. Maybe you can discuss the performance difference between different methods to build the graph.
3. Is there more evidence for Figure 4? From Guidance 1, the integrated teacher probability is as close as possible to the true Bayesian probability. What is the specific reason for the failure of the other two schemes?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
