# Enhancing Dataset Distillation with Concurrent Learning: Addressing Negative Correlations and Catastrophic Forgetting in Trajectory Matching

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Dataset distillation generates a small synthetic dataset on which a model is trained to achieve performance comparable to that obtained on a complete dataset. Current state-of-the-art methods primarily focus on Trajectory Matching (TM), which optimizes the synthetic dataset by matching its training trajectory with that from the real dataset. Due to convergence issues and numerical stability, it is impractical to match the entire trajectory in one go; typically, a segment is sampled for matching at each iteration. However, previous TM-based methods overlook the potential interactions between matching different segments, particularly the presence of negative correlations. To study this problem, we conduct a quantitative analysis of the correlation between matching different segments and discover varying degrees of negative correlation depending on the image per class (IPC). Such negative correlation could lead to an increase in accumulated trajectory error and transform trajectory matching into a continual learning paradigm, potentially causing catastrophic forgetting. To tackle this issue, we propose a concurrent learning-based trajectory matching that simultaneously matches multiple segments. Extensive experiments demonstrate that our method consistently surpasses previous TM-based methods on CIFAR-10, CIFAR-100, Tiny ImageNet, and ImageNet-1K.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses dataset distillation, aiming to create small synthetic datasets that enable models to achieve comparable performance to training on complete datasets. Due to convergence and stability challenges, Trajectory Matching methods typically match only segments of training trajectories, but they overlook negative correlations between different segments. The authors quantitatively analyze these correlations, finding that negative correlations can increase trajectory error and lead to catastrophic forgetting. To address this, they propose a concurrent learning-based TM approach that matches multiple segments simultaneously. Experiments show that this method outperforms previous approaches across various datasets.

### Strengths
1. This paper clearly identifies the problem, providing both theoretical and experimental analysis to demonstrate the existence of negative correlations between trajectory segments.

2. All the discussions in the paper are clear and straightforward.

3. The experiments contains all the necessary components with enough discussion

### Weaknesses
1. This paper includes a theoretical analysis of negative correlation; however, the theory presented in Section 4.1 primarily illustrates that training errors can accumulate across segments. While this is an important observation, it is not directly related to the negative correlation itself. A more detailed exploration of how these relate to negative correlation would strengthen the theoretical foundation of the proposed method. Specifically, the analysis does not provide a clear mechanism explaining why optimizing one segment's trajectory would negatively impact another. The theoretical framework should explicitly model the interaction between segments and demonstrate how concurrent optimization mitigates this negative interference. For example, a formal definition of the negative correlation between segments, and how it relates to the loss landscape, would be beneficial.

2. The novelty of the proposed approach appears to be somewhat limited. To mitigate negative correlation, the method simply trains multiple segments concurrently, which is a strategy commonly employed as a baseline in continual learning scenarios. While concurrent training is a valid approach, the paper does not sufficiently demonstrate why this specific method is superior to other potential solutions for addressing negative correlations in trajectory matching. The paper should explore alternative strategies or provide a more in-depth justification for the chosen approach. For instance, a comparison with methods that dynamically adjust segment weighting or employ gradient manipulation techniques could strengthen the argument for concurrent training.

3. The performance gains observed in the experiments are somewhat disappointing, particularly when considering the increased computational requirements associated with the proposed method. Given the additional complexity introduced, one would expect a more substantial improvement in performance to justify the costs involved (especially when compared to DATM). This raises questions about the effectiveness of the approach in real-world applications. The paper should provide a more detailed analysis of the computational overhead and demonstrate that the performance gains are not only statistically significant but also practically meaningful. For example, a breakdown of the training time and resource consumption compared to baseline methods would be helpful.

### Questions
See strengths and weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper analyzes the challenges of dataset distillation, i.e., negative correlation between different segments of a trajectory to match and catastrophic forgetting problem. To address this, the authors formulate trajectory matching as a continual learning problem and propose a method called Concurrent Training-based Trajectory Matching (ConTra). It employs multi-task learning to simultaneously match multiple segments, rather than sequential learning used in previous works. Experimental results show that ConTra consistently outperforms existing trajectory matching methods on various datasets, thus demonstrating its ability to minimize accumulated matching errors and achieve lossless condensation.

### Strengths
1.	The analysis on negative correlation between different trajectory segments is detailed and solid, enriching the discourse on continual learning.
2.	The idea of utilizing concurrent learning to tackle negative correlation is simple but novel.
3.	Extensive experiments on multiple datasets and downstream tasks are quite convincing.

### Weaknesses
1.	The paper needs to be further polished. There are numorous typos, such as line 140 ‘a expert’->’an expert’, line 457 ‘s the range’->’so the range’.
2.	It would be more intuitive if there is a figure to show the differences/advantages of your proposed ConTra compared to the previous TM methods. Specifically, a visual representation of how the concurrent training approach addresses the negative correlation issue would be beneficial. The current description relies heavily on textual explanation, which can be difficult to grasp without a clear visual aid.
3.	The paper does not test the proposed method using different distillation and evaluation model size. This is a critical omission, as the effectiveness of distillation methods can vary significantly depending on the model architectures used. The paper should include experiments that explore the performance of ConTra when distilling from larger to smaller models, and vice versa, as well as using models of similar size but different architectures. This would provide a more comprehensive understanding of the method's robustness and generalizability.

### Questions
1.	Is the proposed method sensitive to the model size used for distillation and evaluation? 
2.	Does the distillation training time decease when using concurrent learning compared to sequential learning?

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
This paper tackles the problem that matching between different segments of the training trajectory may be negatively correlated. Existing methods use Trajectory Matching (TM), which optimizes the synthetic dataset by matching its training trajectory with the real dataset. However, they overlook the negative correlation between different trajectory segments, leading to performance degradation. The authors propose a concurrent learning-based TM method that matches multiple segments simultaneously, reducing errors. With exhaustive experiments, their approach outperforms previous methods across several benchmark datasets.

### Strengths
[1] The writing of paper is good.

[2] The analysis of the negative correlation on accumulated trajectory error is comprehensive. For example, the author clearly specifies the accumulated error to initialization error and matching error. Afterwards, the authors calculate the correlation to validate the phenomenon.

[3] The proposed cocurrent training methods is reasonable. The experimental results validate the effectiveness of the proposed methods.

### Weaknesses
[1] The description of the accumulated trajectory error is not intuitive. The notations defined in Sec. 4.1 are complex and there is no graphic illustration of these notations. Specifically, the paper introduces terms like initialization error and matching error without clearly defining how these errors are computed or related to the overall accumulated trajectory error. A more detailed explanation with a visual aid would greatly improve understanding. The lack of clarity makes it difficult to assess the validity of the subsequent analysis.

[2] The explanation of the negative correlation is not clear, especially when the IPC is low. The paper states that reducing the matching error of one segment increases the error in other segments, but the underlying mechanism is not well-explained. The role of training dynamics, such as the learning rate or the optimization algorithm, in exacerbating this negative correlation is not explored. Furthermore, the claim that low IPC leads to more pronounced negative correlation requires more rigorous justification and experimental evidence. The paper should provide a more detailed analysis of how the information content of the synthetic dataset interacts with the observed negative correlation.

[3] The novelty of the concurrent training to tackle the problem is rather limited. While reasonable, the author only simply leverages the multitask learning to tackle the problem. The concurrent training approach, while effective, feels like a straightforward application of multi-task learning principles. The paper does not explore other potential solutions or discuss why this specific approach was chosen over other alternatives. Given that the improvement compared to previous state-of-the-art methods is not very significant, the contribution is not above the acceptance bar of ICLR.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
3

### Contribution
2
