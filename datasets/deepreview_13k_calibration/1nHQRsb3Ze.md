# Auxiliary Classifiers Improve Stability and Efficiency in Continual Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Continual learning is crucial for applications in dynamic environments, where machine learning models must adapt to changing data distributions while retaining knowledge of previous tasks. Despite significant advancements, catastrophic forgetting — where performance on earlier tasks degrades as new information is learned — remains a key challenge. In this work, we investigate the stability of intermediate neural network layers during continual learning and explore how auxiliary classifiers (ACs) can leverage this stability to improve performance. We show that early network layers remain more stable during learning, particularly for older tasks, and that ACs applied to these layers can outperform standard classifiers on past tasks. By integrating ACs into several continual learning algorithms, we demonstrate consistent and significant performance improvements on standard benchmarks. Additionally, we explore dynamic inference, showing that AC-augmented continual learning methods can reduce computational costs by up to 60\% while maintaining or exceeding the accuracy of standard methods. Our findings suggest that ACs offer a promising avenue for enhancing continual learning models, providing both improved performance and the ability to adapt the network computation in environments where such flexibility might be required.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to target catastrophic forgetting in continual learning as the problem statement. They
Introduce auxiliary classifiers (ACs) as a mechanism to improve performance in continual learning. The study provides analysis using linear probes and then proposes adding classifiers to intermediate layers, leveraging the fact that earlier layers of neural networks exhibit more stability. The results are shown with different Methods, naive fine-tuning , replay-based and regularizer based CL methods.

### Strengths
- Catastrophic forgetting is a key challenge in continual learning and this paper aims to address this critical issue
- The use of linear probing to assess accuracy at different network layers is interesting and offers insights
- The paper is well-organized and generally easy to follow

### Weaknesses
 - The paper’s objective is bit ambiguous. It’s unclear whether the goal is to fully mitigate catastrophic forgetting or simply to offer additional accuracy sources through auxiliary classifiers. Because, forgetting still occurs, with the method seemingly redistributing accuracy rather than eliminating forgetting. This distinction needs clarification, particularly around Line 190, where the claim that the method is "less prone to forgetting" may need more evidence. The paper should more clearly articulate whether the aim is to reduce forgetting or simply to improve overall accuracy by leveraging multiple classifiers, as these are distinct goals with different implications for continual learning.

- Previous studies have already shown that early layers capture more generic features, while later layers capture task-specific semantics, so just early layers alone are often insufficient for reliable predictions. Further, though the paper incorporates auxiliary classifiers across layers, this approach introduces computational overhead. The lack of consistent patterns in the ablation studies also leaves it unclear how to optimally position these classifiers for a more efficient solution. The paper needs to address the computational cost of adding multiple classifiers and provide a more systematic analysis of how their placement impacts performance, rather than relying on inconsistent ablation results. It is also unclear if the improvements are due to the additional parameters or the method itself.

- The motivation to introduce auxiliary classifiers (ACs) stems from empirical analysis, but the results show inconsistent patterns across different continual learning methods. For instance, in replay-based methods, weights remain relatively stable even without ACs, suggesting that the benefits of ACs may not be as universal as claimed. This raises the question of whether adding classifiers could be unnecessary overhead for certain methods. The paper should investigate why ACs provide varying benefits across different continual learning methods and consider whether the added complexity is justified for all methods, especially those that already exhibit good stability.

- LP works on frozen networks, however the hypothesis in Line 253, aims to train all classifiers, and the criteria changes. Training multiple classifiers concurrently may impact the final classifier's performance by diluting its specificity and potentially reducing network plasticity. Hence the training and the final classifier accuracy and the patterns learnt to make the prediction, can get affected ? The paper should analyze how training multiple classifiers concurrently affects the final classifier's performance and whether it leads to a reduction in network plasticity or a dilution of task-specific learning.

- Empirical analysis could be more detailed. There’s limited discussion on the scalability of this method to larger networks or more extended task sequences. The claim of reduced forgetting (Line 190) would benefit from testing on longer task sequences (>10)  and more complex (deeper) architectures. Also does the phase of training play a part, during initial epochs vs near the end of the final epochs for a task? The paper should include experiments on larger networks and longer task sequences to validate the scalability of the method. Additionally, the impact of the training phase on the effectiveness of ACs should be investigated.

- Other accuracy criteria such as stability and plasticity or forward/backward transfer is not provided which are important for assessing the method's full impact on continual learning.

- Will this work when classes overlap, say in domain incremental learning?

### Questions
- Figure 1 is not clear, the colors blend together. In general few figures need improvement.
- Can you explain LP analysis? The classifiers at each layer are trained after the whole network is trained on all tasks and frozen?
- Line 187, is this claim correct? There are no analysis for longer tasks (more than 10)
- Can we visualize a pattern of which classifiers are being used? With multiple ACs, how is the final classifier’s predictive power affected?  Could this architecture reduce overall network plasticity?
- Line 471 -  The lack of a clear impact from varying AC numbers and positioning is surprising. This makes it difficult to form a clear intuition about the impact. Thoughts on this ablation?
- While replay and regularization methods are considered in results, parameter isolation methods such as PNN.. are not considered. Also, such as DER ++ (logit replay) are not considered?
- Line 283 - was any other criterion tried before choosing maximum confidence? 
- How is threshold calculated for dynamic inference? Does it depend on arch or complexity of data or tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the stability of intermediate neural network layers and addresses the catastrophic forgetting problem in continual learning (CL) by utilizing features from these layers to train auxiliary classifiers (ACs). The proposed approach is novel and aims to enhance the robustness of existing CL methods.

### Strengths
**Originality:** The focus on leveraging intermediate layer features to train ACs as a means to combat catastrophic forgetting is an innovative contribution to the field.  
**Quality:** The experimental results demonstrate that the proposed ACs significantly improves the performance of current CL methods, validating the effectiveness of the approach.  
**Clarity:** The paper is well-organized and easy to follow.

### Weaknesses
1. The paper lacks a detailed analysis of time complexity and computational overhead. Specifically, how much additional time and memory are required for training and inference with the introduced ACs? This is a significant concern, as the practicality of the proposed method may be limited by increased resource requirements.  
2. The description of how to train the ACs is unclear. Are the same strategies used for training all classifiers? What is the architecture of each classifier?  
3. The choice of static inference, where the classifier with the maximum probability is selected, lacks further analysis and justification. More explanation is needed on this decision-making process.  
4. In Figure 5, what does the x-axis labeled "cost" represent? Additionally, what value of $\lambda$ was used in the reported results for dynamic inference?

### Questions
1. What is the distribution of the final selected classifiers during inference? 
2. The paper observes only six intermediate layers; it would be interesting to know if similar results apply to other layers as well.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigated the stability of intermediate neural network layers during continual learning, where early network layers tend to be more stable. The authors then proposed to integrate auxiliary classifiers (ACs) into intermediate layers and ensemble them for improving continual learning. The authors then provided extensive experiments to demonstrate the effectiveness of the proposed ACs.

### Strengths
1. This paper is essentially well-organized and easy to follow.

2. The proposed ACs seem to be easy to implement and provide significant improvements over a range of continual learning baselines.

3. The proposed ACs may also reduce the computation through dynamic inference.

### Weaknesses
1. The authors claimed that “no work has yet explored the use of intermediate classifiers in the continual learning setting”. However, there are at least two papers focusing on using multiple ACs in continual learning. [1] proposed to use multiple side classifiers on the top of regularization-based methods. [2] added multiple ACs to the intermediate outputs and integrated their outputs for online continual learning.

2. The entire work is essentially based on the observations that the intermediate outputs behave differently and may outperform the final outputs in some cases. Is it possible to provide some mechanistic explanation for this phenomenon? Also, the advantages of intermediate outputs in unique accuracy (Figure 3) seem to be marginal for continual learning baselines. I'm not sure this is the main reason for the improved performance of the ACs.

3. The authors claimed that the dynamic inference can reduce the computation. Does this mean training costs and/or testing costs? From my understanding, the proposed ACs still need to train the entire model while skip some layers for inference.

4. The experiments are mainly performed with ResNet-based architectures. Do the proposed ACs also apply to the intermediate outputs of transformer-based architectures?

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
