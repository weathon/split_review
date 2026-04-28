# Retraining-Free Merging of Sparse Mixture-of-Experts via Hierarchical Clustering

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Sparse Mixture-of-Experts (SMoE) models represent a significant breakthrough in large language model development. These models enable performance improvements without a proportional increase in inference costs. By selectively activating a small set of parameters during task execution, SMoEs enhance model capacity. However, their deployment remains challenging due to the substantial memory footprint required to accommodate the growing number of experts. This constraint renders them less feasible in environments with limited hardware resources. To address this challenge, we propose Hierarchical Clustering for Sparsely activated Mixture of Experts (HC-SMoE), a task-agnostic expert merging framework that reduces SMoE model parameters without retraining. Unlike previous methods, HC-SMoE employs hierarchical clustering based on expert outputs. This approach ensures that the merging process remains unaffected by routing decisions. The output-based clustering strategy captures functional similarities between experts, offering an adaptable solution for models with numerous experts. We validate our approach through extensive experiments on eight zero-shot language tasks and demonstrate its effectiveness in large-scale SMoE models such as Qwen and Mixtral. Our comprehensive results demonstrate that HC-SMoE consistently achieves strong performance, which highlights its potential for real-world deployment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a retraining free experts merging approach which employs a hierarchical clustering strategy. The authors claim that using expert outputs as the similarity metric for clustering is more effective compared with using router logins or weights employed by prior works. The experimental results reveal the proposed approach gains more performance improvements compared with existing methods across various benchmarks.

### Strengths
1. An output based similarity metric of expert clustering is proposed, which is more effective than previous works.
2.The experimental results compared with the previous methods are very good.

### Weaknesses
There is a lack of theoretical analysis on the performance of expert clustering using different similarity metrics.

### Questions
I am wondering the results or analysis for more extreme expert reduction scenarios, such as reducing to 25% or 10% of the original experts. This would give insight into how the method performs under more aggressive compression.

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
4

### Summary
This work introduces Sparse Mixture-of-Experts (SMoE) models, which improve large language model performance without significantly increasing inference costs by activating only a subset of parameters. However, their high memory requirements hinder deployment. To address this, the authors propose Hierarchical Clustering for Sparsely activated Mixture of Experts (HC-SMoE), a task-agnostic framework that reduces SMoE parameters without retraining.

### Strengths
- HC-SMoE offers a practical solution for reducing parameters without the need for retraining, simplifying the implementation process.

- The task-agnostic nature of HC-SMoE allows for broader applicability across different language tasks, enhancing its versatility.

- The comprehensive experiments conducted on eight zero-shot language tasks provide strong empirical evidence of HC-SMoE's effectiveness in large-scale models like Qwen and Mixtral.

### Weaknesses
 - While this work demonstrates competitive accuracy, it lacks a comprehensive assessment of efficiency metrics, such as speedup and memory usage. Given that efficiency is a key contribution, this aspect of the experimental results is essential.

- A theoretical analysis of the effectiveness of expert merging and HC-SMoE would enhance the understanding of the method's performance.

- Although HC-SMoE is validated on eight zero-shot language tasks, its effectiveness may vary in more complex tasks or domains, potentially limiting its broader applicability.

### Questions
Please refer to the Weakness.

### Soundness
3

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
3

### Summary
This paper proposed a new expert merging framework, named Hierarchical Clustering for Sparsely activated Mixture of Experts (HC-SMoE), to reduce SMoE model parameters without retraining. The proposed method is simple but effective, and the experiments demonstrated the efficacy of the proposed method.

### Strengths
* The proposed method is simple but effective, 
* The paper is very easy to follow.
* The experiments are comprehensive and the results are very promising.

### Weaknesses
 * The motivation of using the "Hierarchical" clustering is not clear to me. I cannot intuitively get the idea of why hierarchical clustering is better than simple K-means clustering, although the results confirmed that K-means clustering is less effective. Besides, the paper proposed to use a "hard" hierarchical clustering, and I am wondering if it is more effective to use "soft" hierarchical clustering or simply "soft" clustering without hierarchies. 
* The choice of the calibration dataset. I did not see any ablation study about the choice of the calibration dataset, and I think the performance of the proposed method should highly depend on the calibration dataset. If the calibration dataset is not comprehensive enough, e.g., not covering enough domain specific data, the clustering may not be very informative, which may lead to poor performance. For example, if we want the LLM to perform well on a law-related or medical-related tasks, can you also rely on the same calibration dataset used in the experiments?
* Some minor issues:
  * In Fig. 1, why you did not compare the methods on 14B model?
  * Section 3.2.1 presents the method of similarity metric but contains a lot of discussions about related work.
  * In line 299/300, is alpha_i fixed or not? If it is fixed, will it also suffer from the issue that you mentioned in line 199-203 about frequency-based method?
  * In Table 4, the best performance of 'ARC-c' should be the Average linkage using the Weight setting, right?

### Questions
Please refer to my question above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Hierarchical Clustering for Sparsely Activated Mixture of Experts (HC-SMoE), a task-agnostic framework for merging experts within an SMoE model. HC-SMoE aims to reduce the model's parameters without requiring retraining. Experiment results on a series of benchmarks show its effectiveness.

### Strengths
1) Pruning experts in MoE models can indeed reduce the difficulty of deployment.
2) The paper is easy to follow, and the ablation study is comprehensive.
3) The experimental results on Qwen and Mixtral are convincing.

### Weaknesses
1) O-prune [1] requires enumerating all possible combinations of experts, resulting in significant time overhead. I would like to know how HC-SMoE compares to other approaches in terms of runtime and resource consumption.
2) O-prune [1] also conducts experiments on domain-specific tasks (e.g., GSM8K, Math). I am interested in the performance of HC-SMoE on these datasets.

### Questions
See Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
