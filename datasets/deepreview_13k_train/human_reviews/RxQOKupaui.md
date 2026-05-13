# Towards Optimal Adapter Placement for Efficient Transfer Learning

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Parameter-efficient transfer learning (PETL) aims to adapt pre-trained models to new downstream tasks while minimizing the number of fine-tuned parameters.
Adapters, a popular approach in PETL, inject additional capacity into existing networks by incorporating low-rank projections, achieving performance comparable to full fine-tuning with significantly fewer parameters.
This paper investigates the relationship between the placement of an adapter and its performance. We observe that adapter location within a network significantly impacts its effectiveness, and that the optimal placement is task-dependent. To exploit this observation, we introduce an extended search space of adapter connections, including long-range and recurrent adapters. We demonstrate that even randomly selected adapter placements from this expanded space yield improved results, and that high-performing placements often correlate with high gradient rank. Our findings reveal that a small number of strategically placed adapters can match or exceed the performance of the common baseline of adding adapters in every block, opening a new avenue for research into optimal adapter placement strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work investigates efficient strategies for placing adapters in transfer learning, specifically within the context of parameter-efficient transfer learning (PETL). A key finding is that the location of adapters within a network significantly impacts effectiveness, and the optimal placement depends on the specific task. By adapting pre-trained models to new tasks with minimal parameter adjustments, this study emphasizes maximizing effectiveness through strategic adapter placement rather than uniformly adding adapters across network layers.

### Strengths
1. The designs for the adapter in Equation 2 and the recurrent searching graph appear solid. It seems that using the recurrent approach is more effective than the parallel sequential or long-range approach.

2. Based on experiments, a single, well-placed adapter can significantly improve performance compared to the linear probe.

### Weaknesses
I think the paper could benefit if the author addresses the following question related to multiple adapters and the corresponding search and replacement algorithms:

1. How many adapters would achieve optimal performance? From Section 5.2, it appears that the authors aim to use multiple adapters with random search to improve transfer learning quality, yet it remains unclear how many adapters are necessary to achieve robust performance coverage. Based on Figure 6 and the GGA section, performance appears to continue increasing as more adapters are added. While I understand that the optimal number of adapters is task-dependent, is there a mathematical formalization that explicitly demonstrates how many adapters are sufficient? It seems that GGA is largely observational and based on gradient analysis. Is it possible that adding too many adapters could lead to an over-parameterized model, potentially causing a drop in accuracy?


2. The authors suggest that GGA is effective with a few adapters (as shown in Figure 6, where 12 GGA-based adapters achieve similar or higher performance). I believe it would be beneficial if the authors provided comparisons of computational complexity and memory usage for these methods. Specifically, what is the training complexity compared to the compressed approach in this paper? Calculating gradients may introduce additional time and memory costs, as it requires retaining the graph during training. Additionally, what is the inference complexity? For instance, to reach the same accuracy, full fine-tuning does not incur additional costs associated with adapters (which could treated as upper bound). How does GGA compare with other approaches in terms of these factors?

### Questions
Related to question 1 in terms of weaknesses, the authors suggest that the placement of adapters significantly impacts performance. In the case of multiple adapters, as shown in Figure 6, using the same number of adapters (e.g., 6, 12, 24) results in varied performance. The only difference is the placement of these adapters, while other conditions remain the same.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the impact of adapter placement within pre-trained neural networks on their transfer learning performance. Besides, the paper introduces an extended search space for adapter placement, including long-range and recurrent adapters, and proposes a method to identify optimal placements using gradient rank as a predictor of adapter performance. The experiments across datasets and model scales demonstrate that strategically placed adapters can match or exceed the performance of uniformly distributed adapters.

### Strengths
* The motivation is clear and the adapter placement is worth researching.
* The proposed Gradient Guided Adapters (GGA) algorithm is interesting.

### Weaknesses
 * The recurrent adapters require two forward processes, further deteriorating the efficiency of pre-trained models.
* Results in table 1 lack the comparison with related works.
* The paper lacks a clear and actionable conclusion. While the findings are interesting, it remains unclear how these results can be directly applied to practical scenarios.
* The GGA algorithm shows promise, but it only works on the use of a limited number of adapters. This limitation is problematic given that adapters are usually lightweight and commonly stacked layer-wise in practical. As a result, the applicability of GGA in real-world scenarios is severely constrained.
* The significance of reducing adapter parameters is not well-justified, given that adapters are already much smaller than the pre-trained model. Whether an adapter has 1M or 10M parameters does not drastically change its feasibility for single-GPU fine-tuning.
* The dataset-specific nature of adapter placement is not a novel finding, and the paper does not explore potential generalizable patterns that could emerge from this observation.

### Questions
The GGA algorithm shows promise, but it only works on the use of a limited number of adapters. This limitation is problematic given that adapters are usually lightweight and commonly stacked layer-wise in practical. As a result, the applicability of GGA in real-world scenarios is severely constrained.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates optimal adapter placement strategies in Parameter Efficient Transfer Learning (PETL) for deep neural networks. The authors introduce an extended search space for adapter connections, including long-range and recurrent adapters, which allows the adapters to exploit non-local information. They demonstrate that the placement of adapters is critical for the overall model performance and that strategically placed adapters can outperform standard uniform adapter placements. Additionally, they propose a gradient rank-based metric to identify optimal adapter locations efficiently.

### Strengths
1. The authors introduced a novel extension of the adapter placement search space, including long-range and recurrent adapters, which go beyond traditional uniform placement. This provides more flexibility and improves fine-tuning results.

2. The proposed gradient rank metric offers a practical and computationally efficient method for predicting the best adapter placements a priori, significantly reducing the computational cost of fine-tuning large models.

3.  The method shows that even with a small number of well-placed adapters, performance can match or exceed the standard uniform approach, highlighting the method's efficiency.

### Weaknesses
1. **Dataset Limitation**: While the paper demonstrates the method's effectiveness on several datasets, the reviewer is curious about its performance on larger and more diverse datasets, such as ImageNet. Testing on such datasets would better illustrate the method's scalability and generalization capabilities. Specifically, the paper should explore how the proposed gradient-based adapter placement strategy performs when the pre-training and fine-tuning datasets have significant domain shifts, as this is a common challenge in transfer learning scenarios.

2. **Adapter Complexity**: Introducing long-range and recurrent adapters increases overall model complexity. However, the paper does not fully explore the trade-offs between this complexity and the performance gains. The reviewer is curious if the added complexity of long-range and recurrent adapters could lead to instability during training or inference, particularly in large-scale applications. It is important to analyze the computational overhead of these complex adapters, including the increased memory footprint and the impact on training and inference times, compared to simpler adapter architectures.

3. **Task-Specific Adapter Placement**: The method's reliance on task-specific adapter placement strategies may limit its practicality for general-purpose applications. The reviewer wonders if there is potential to reduce the task-specific nature of adapter placement, making the method more widely applicable without requiring custom placement strategies for each task. A more thorough investigation into the transferability of adapter placements across different tasks and datasets is needed. It would be beneficial to understand how the optimal placements change when the task or dataset is significantly different from those used in the experiments.

### Questions
see weakness above

### Soundness
4

### Presentation
4

### Contribution
3
