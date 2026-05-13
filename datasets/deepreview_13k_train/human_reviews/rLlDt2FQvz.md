# N-ForGOT: Towards Not-forgetting and Generalization of Open Temporal Graph Learning

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Temporal Graph Neural Networks (TGNNs) lay emphasis on capturing node interactions over time but often overlook evolution in node classes and dynamic data distributions triggered by the continuous emergence of new class labels, known as the open-set problem. This problem poses challenges for existing TGNNs in preserving learned classes while rapidly adapting to new, unseen classes. To address this, this paper identifies two primary factors affecting model performance on the open temporal graph, backed by a theoretical guarantee:  (1) the forgetting of prior knowledge and (2) distribution discrepancies between successive tasks. Building on these insights, we propose N-ForGOT, which incorporates two plug-in modules into TGNNs to preserve prior knowledge and enhance model generalizability for new classes simultaneously. The first module preserves previously established inter-class connectivity and decision boundaries during the training of new classes to mitigate the forgetting caused by temporal evolutions of class characteristics. The second module introduces an efficient method for measuring distribution discrepancies with designed temporal Weisfeiler-Lehman subtree patterns, effectively addressing both structural and temporal shifts while reducing time complexity. Experimental results on four public datasets demonstrate that our method significantly outperforms state-of-the-art approaches in prediction accuracy, prevention of forgetting, and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper addresses the challenge of open temporal graph learning (OTGL), where temporal graph neural networks must adapt to continuously emerging new classes while preserving knowledge of existing classes. The method aims to balance preventing catastrophic forgetting while enabling generalization to new classes. The authors provide a theoretical analysis of the generalization error bounds.

### Strengths
Originality: The paper presents a novel perspective by jointly addressing forgetting and generalizability in temporal graphs, rather than treating them as separate problems. The LTDO module's use of temporal WL subtree patterns is particularly innovative.

Quality: The theoretical analysis is thorough, grounding the approach in PAC-Bayesian theory and providing a clear justification for the chosen architecture. The reduction in computational complexity from O(n²) to O(n) is significant.

Clarity: The paper is well-structured and clearly written. The problem motivation using real-world examples (like evolving cell phone characteristics) helps readers understand the practical implications.

Significance: The work addresses an important real-world challenge in temporal graph learning and provides a practical solution that could benefit various applications like social networks and e-commerce systems.

### Weaknesses
1. While the TICR module's preservation of decision boundaries is well-explained, there could be more discussion about potential trade-offs between maintaining old boundaries and adapting to new class characteristics.

2. The paper could better explain how the temporal WL subtree patterns are specifically designed to capture temporal information, as this seems crucial to the method's success.

3. The relationship between batch size and performance of the LTDO module deserves more analysis, as this could affect practical deployments.

### Questions
The computational complexity reduction is impressive - are there any trade-offs in terms of model accuracy when using the more efficient LTDO approach compared to traditional MMD-based methods?

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
N-ForGOT proposes a novel solution to Open Temporal Graph Learning (OTGL). Specifically, N-ForGOT consists of 2 plug-in modules: Temporal Interclass Connectivity Regularization Module (TICR), which mitigates catastrophic forgetting when new classes emerge in future timestamps, and Localized Temporal Graph Discrepancy Optimization (LTDO) that learns task-invariant representations, enhancing the generalizability for models across different tasks.

### Strengths
1. N-ForGOT achieves competitive empirical results and conducts a comprehensive empirical evaluation setting that consists of diverse real-world datasets and robust evaluation metrics that assess the generalizability and model’s robustness against forgetting.

2. Overall comprehensive presentation and reproducibility details, as the paper presents a clear diagram describing the method, pseudo-code for training realization, and detailed report of experimental settings, including hyperparameters and computational resources.

### Weaknesses
1. The mathematical notations are hard to follow in Section 4.1, as some notations are not associated with a formal definition or description.
In line 238:
>  … types for the class $i$ are denoted by $\mathbf{p}^{(i)} \sum_{j \in \mathcal{S}_i} g(x_j)$.
Before line 238, or after the definition of prototypes for a class, the definition of $\mathcal{S}_i$ is not found. Does $\mathcal{S}_i$ have the same definition as $\mathbf{S}_i$ defined in line 259? If so, I think authors should declare this and move the definition to the right behind (or before) the definition of prototypes for the class $i$ in line 238.

In line 241, what is the definition of $\mathbf{p}^{i}_j$?

In line 242, for the definition of $I(i, j)$: 
> … is an indicator function used to represent whether a category $n$ appears in a task $j$
Why does $I(i, j)$’s definition depend on $n, j$?

In lines 252-253: 
> … $\mathbf{p}_{k - 1}$ is obtained from the class prototype matrix …
What is the definition of $\mathbf{p}_{k - 1}$? Does it have the same meaning with the class prototype matrix $\mathbf{P}_{k}$ (defined in lines 239-240 but with a different index ($k - 1$ instead of $k$)? If so, authors should revise $\mathbf{p}_{k - 1}$ to $\mathbf{P}_{k - 1}$.

2. What is the role of the bounding risk (presented in Theorem 1)? Does the bounding inspire any component of N-ForGOT? Or do any implications from the bound motivate the proposed method? If so, the authors should state this in the paper.

3. As authors claim that TLDO helps cultivate task-invariant representations that are robust to structural and temporal shifts, I suggest authors present a plot or illustration that shows how the distributional shifts (computed by MMD) change from task-to-task. 

4. Are there any constraints for $\alpha$ and $\beta$ (defined in Eq. 9)? For better reproducibility, I suggest authors report these hyperparameters used for training N-ForGOT.

### Questions
Please see Weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes N-ForGOT, a framework for Temporal Graph Neural Networks (TGNNs) that addresses the open-set problem in dynamic graphs by preserving previously learned classes while adapting to new ones. This is achieved with two main modules: the Temporal Inter-Class Connectivity Regularization (TICR) for mitigating forgetting of prior knowledge, and the Localized Temporal Graph Discrepancy Optimization (LTDO) to manage distribution shifts across tasks. Empirical results show that N-ForGOT outperforms existing methods in prediction accuracy, minimizing forgetting, and enhancing generalizability across tasks.

### Strengths
S1: Clarify: The overall demonstration of open-set learning in dynamic graphs is very clear, in terms of two core challenges of distribution shifts and knowledge forgetting, also with clear motivation for the proposed continual learning mechanism.

S2: Method: Two modules, TICR module and LTDO module, help the model retain essential inter-class information, reduce forgetting and preserve learned knowledge over time, and manage distribution shifts across evolving tasks, sounds rational to me.

S3: Empirical Experiments & Good Structure: The method demonstrates effective performance on multiple benchmarks, with good logic and organized well.

### Weaknesses
See questions.

Q1: My understanding of the open-set setting is that it allows predictions on completely unseen classes. However, in the proposed method, it seems the model gradually learns across tasks by incorporating new classes over time. If the dataset consists of six tasks, does this mean the prediction space is limited to these six tasks and wouldn’t cover unknown classes beyond them? In the test set, are predictions also evaluated solely on the six classes seen during training? In this case, can we take it as the 'open-set'?

Q2: The paper mentions dynamic graph distribution shifts, but does this refer only to shifts in class labels over time? Are other types of distribution shifts, such as changes in features or interactions over time, also considered or defined in this work? And how these distribution shift issues are modeled and integrated into the proposed method?

### Questions
I do not have extensive expertise in this research area, but I have some general questions:

Q1: My understanding of the open-set setting is that it allows predictions on completely unseen classes. However, in the proposed method, it seems the model gradually learns across tasks by incorporating new classes over time. If the dataset consists of six tasks, does this mean the prediction space is limited to these six tasks and wouldn’t cover unknown classes beyond them? In the test set, are predictions also evaluated solely on the six classes seen during training? In this case, can we take it as the 'open-set'?

Q2: The paper mentions dynamic graph distribution shifts, but does this refer only to shifts in class labels over time? Are other types of distribution shifts, such as changes in features or interactions over time, also considered or defined in this work? And how these distribution shift issues are modeled and integrated into the proposed method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on temporal graph learning and proposes a method, named N-ForGOT, to address evolution in node classes and dynamic data distributions triggered by the continuous emergence of new class labels. Two specific modules are designed to address the corresponding problem. Experimental results on four public datasets demonstrate the effectiveness of the proposed method.

### Strengths
The studied problem is practical and interesting.

The authors provide a theoretical analysis of the generalization error bound.

The experimental results are promising.

### Weaknesses
The related works are not comprehensive.

Some symbols and statements are not clear.

### Questions
1.	Some recent works on graph continual learning are not included in the paper, such as [1][3].
2.	The authors are encouraged to discuss the differences between the studied problem and graph continual learning more clearly as the distribution shift and forgetting problem also exist in graph continual learning [2].
3.	More recent graph continual learning baselines are encouraged to be included for comparison,
4.	When learning a new task, is the data of previous tasks available and included for training? In graph continual learning, there is no access to data from previous tasks and classes.
5.	In line 243, should the category “n” be “i”?
6.	In line 349, there are some overlapping.
7.	Please revise line 420 to make it more clear.
8.	In 484, the figure should be Figure 4 and there should be margins between the caption of Figure 4 and the main text.
9.	Why are there learning rates for the model optimization in line 892?

[1] Niu C, Pang G, Chen L. Graph Continual Learning with Debiased Lossless Memory Replay[J]. arXiv preprint arXiv:2404.10984, 2024.
[2] Zhang, X., Song, D., & Tao, D. (2022). Cglb: Benchmark tasks for continual graph learning. Advances in Neural Information Processing Systems, 35, 13006-13021.
[3] Liu, Y., Qiu, R., & Huang, Z. (2023, December). Cat: Balanced continual graph learning with graph condensation. In 2023 IEEE International Conference on Data Mining (ICDM) (pp. 1157-1162). IEEE.

### Soundness
3

### Presentation
2

### Contribution
3
