# IMEX-Reg: Implicit-Explicit Regularization in the Function Space for Continual Learning

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Continual learning (CL) remains one of the long-standing challenges for deep neural networks due to catastrophic forgetting of previously acquired knowledge. Although rehearsal-based approaches have been fairly successful in mitigating catastrophic forgetting, they suffer from overfitting on buffered samples and prior information loss, hindering generalization under low-buffer regimes. Inspired by how humans learn using strong inductive biases, we propose \textbf{IMEX-Reg} to improve the generalization performance of experience rehearsal in CL under low buffer regimes. Specifically, we employ a two-pronged implicit-explicit regularization approach using contrastive representation learning (CRL) and consistency regularization. To further leverage the global relationship between representations learned using CRL, we propose a regularization strategy to guide the classifier toward the activation correlations in the unit hypersphere of the CRL. Our results show that IMEX-Reg significantly improves generalization performance and outperforms rehearsal-based approaches in several CL scenarios. It is also robust to natural and adversarial corruptions with less task-recency bias. Additionally, we provide theoretical insights to support our design decisions further.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach called IMEX-Reg, tailored for low memory buffer scenarios. In addition to several other techniques such as EMA, the approach utilizes contrastive representation learning and applies regularization to both the classification outputs and projection outputs. The motivation behind the approach stems from the fact that contrastive embeddings lie on the hypersphere, which improves training stability and classification performance. The experiment shows that the proposed method outperforms the baselines under the low memory buffer settings and shows the effectiveness of the proposed techniques in the ablation study.

### Strengths
1. The motivation is clear and the paper is well-written
2. It outperforms the baselines

### Weaknesses
1. The contribution of the paper is merely incremental as using contrastive learning and regularization on function space have been extensively studied before [1, 2, 3]. Imposing a regularization on the contrastive projected outputs along with the classification outputs improves the performance is not surprising. The specific combination of contrastive learning, EMA, and regularization, while presented as novel, appears to be a straightforward application of existing techniques. The paper lacks a thorough justification for why this particular combination is significantly better than other possible combinations or existing methods.
2. The method introduces many hyper-parameters (e.g., alpha, beta, lambda in Eq.7), but there was no study of how these hyper-parameters affect the model performance. The absence of a sensitivity analysis for these hyper-parameters makes it difficult to assess the robustness and generalizability of the proposed method. The optimal values of these parameters may be highly dependent on the specific dataset and task, limiting the practical applicability of the method without extensive tuning.
3. The authors argue that their method has advantages over existing replay methods. However, rehearsal-free methods such as [3, 4] already significantly outperform the proposed method. For instance, [3] achieves 87.8% accuracy on Seq-CIFAR10 and 47.1% on Seq-TinyImageNet without the need to save any samples. The comparison to replay-based methods is not compelling, as the state-of-the-art in rehearsal-free methods already achieves much higher performance. The paper fails to adequately address why a replay-based method is still relevant given the advancements in rehearsal-free techniques.

### Questions
1. Based on a paper under review, [5] achieves 74+% in Seq-CIFAR10 with a buffer size of 200 in ResNet-18. The authors may compare their method with [5]
2. Why is this method robust to natural corruption? An important discussion aligned with robustness to data distribution (or corruption) is covered in [6].

Misc.
Please use \` rather than ' for \`SGD' and \`Joint' on page 6


[5] Learnability and algorithm for continual learning \
[6] A multi-head model for continual learning via out-of-distribution detection

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper studies an interesting topic, continual learning, which aims to learn a series of tasks without forgetting. In order to the generalization performance of the memory-based methods, this paper introduces to employ contrastive representation learning (CRL) and consistency regularization. The experiment results show that the proposed approach achieve good results in continual learning.

### Strengths
1. The main idea seems interesting.
2. This paper studies an interesting topic.

### Weaknesses
1. The notations are hard to follow. For example, x and y should be bold because they are matrixes.
2. The parameters of the shared model and classifier are not defined.
3. Eq.1 is not clear to me. What is the actual network for f and g? Why is h not used in Eq.1?
4. In the text below Eq.2, you said z = h(f(.)). However, z is not defined in Eq.2. The input and output patterns for the models f, g and h are unclear.  
5. Why introduce the existing Conjecture 1? Does this theory connect with your actual design?
6. Why the classifier can create the function spaces?
7. The proposed approach is based on the existing technology, and the overall novelty is small.
8. The proposed approach still requires the task information, which can not be used in more realistic continual learning settings such as task-free continual learning.
9. The methodology section is hard to follow. A lot of notations are not defined clearly and the proposed approach is not novel enough.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper develops IMEX-Reg as a new method to tackle catastrophic forgetting in continual learning settings.  IMEX-Reg  is inspired by the nervous system mechanisms and combines contrastive representation learning with consistency regularization. It aligns the classifier with CRL representations in the unit hypersphere. Empirical results are offered to demonstrate that IMEX-Reg improves the model generalization and leads to SOTA performance compared to the baselines. IMEX-Reg is also resilient to adversarial data issues and reduces bias towards recent tasks. The approach is also supported by theoretical justifications.

### Strengths
1. CL is still an active research area and the proposed approach is a new method for this purpose.

2. The paper reads well and can be followed straightforwardly.

3. Section D in the Appendix is informative and offers insights about the weaknesses and future potentials for the proposed research.

### Weaknesses
1. Continual learning in the context of the used baselines is a mature field with many existing works. However, the method does not provide a significant performance boost over the existing state-of-the-art, and the gains are not consistently substantial across all settings to warrant a strong contribution. While the method achieves SOTA results, the margin of improvement is not always large enough to justify the complexity of the approach.

2. Theoretical justifications of the paper are not novel and mostly are reiterating previous results. Doing so is OK but does not offer any new theoretical contributions. The theoretical analysis, while present, does not provide a deep, novel understanding of why the proposed method works so well, and it relies on existing theoretical frameworks.

3. Some aspects of the algorithm are not studied extensively. Specifically, the sensitivity of the method to the hyperparameters, including \alpha, \beta, and \lambda, is not thoroughly investigated. The paper lacks a detailed ablation study to understand the contribution of each component of the proposed method, and how the interplay between contrastive learning and consistency regularization affects the final performance.

### Questions
1. The connection between the proposed approach and the nervous system is very loose and emphasis on this aspect is overstated. What is the reason behind this emphasis without providing much evidence to support it?

2. It is important to study the effect of \alph, \beta, and \lambda on the performance. How the user should tune them? A study should be offered for this purpose. If the performance is sensitive with respect to the values of these hyperparameters, then it is essential to provide a solution for selecting the optimal values.

3. There are other common settings to study CL using CIFAR100, e.g., using 20 tasks each with 5 classes. I think adding experiments for these settings is also helpful to demonstrate how well the method scales when there are more tasks.

4. Having learning curves in CL is common and allows for studying the dynamic of learning. I think providing them in addition to the tables is helpful.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
