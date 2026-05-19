### Summary

This paper studies the effect of chunking in continual learning, i.e., training on data chunks instead of the whole dataset. The authors show that chunking is responsible for a significant part of the performance drop in continual learning. They also show that the main reason for the performance drop is forgetting. To mitigate forgetting, the authors propose a simple method, per-chunk weight averaging, which improves performance under chunking and transfers to the full continual learning setting.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a novel analysis of the chunking problem in continual learning, which is an important aspect of the field that has been overlooked in previous work.
- The paper proposes a simple yet effective method to improve performance under chunking, which can be easily implemented and applied to various continual learning scenarios.
- The paper demonstrates the effectiveness of the proposed method on several benchmark datasets and shows that it transfers to the full continual learning setting.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only considers the class-balanced chunking setting, which may not be representative of real-world scenarios. In practice, the distribution of classes in each chunk may vary, and the proposed method may not generalize well to such cases. Specifically, the method's reliance on uniform averaging across chunks could be problematic when chunk sizes or class distributions are highly imbalanced, potentially leading to biased weight updates and suboptimal performance.
- The paper does not provide a theoretical analysis of the proposed method. While the empirical results are promising, a theoretical understanding of why per-chunk weight averaging works is missing. For instance, it is unclear how this method relates to existing optimization techniques or what guarantees it provides in terms of convergence or generalization. A theoretical framework would strengthen the paper's contribution and provide a deeper understanding of the method's behavior.
- The paper does not compare the proposed method with other existing methods for addressing the chunking problem. While the authors argue that current CL methods do not address the chunking problem, it is still important to compare the proposed method with other potential solutions, such as methods that explicitly model the chunk structure or use adaptive learning rates for each chunk. Without such comparisons, it is difficult to assess the relative merits of the proposed method.

### Suggestions

The paper makes a valuable contribution by highlighting the chunking problem in continual learning, but it could be strengthened by addressing the limitations mentioned above. First, the authors should investigate the performance of the proposed method under more realistic, class-imbalanced chunking scenarios. This could involve experimenting with different levels of class imbalance within each chunk and analyzing how the method's performance changes. Furthermore, the authors could explore modifications to the averaging process that take into account the size or class distribution of each chunk. For example, a weighted averaging scheme could be used, where chunks with more data points or more balanced class distributions are given higher weights. This would make the method more robust to variations in chunk characteristics and improve its applicability to real-world scenarios. The authors should also consider comparing their method with other potential solutions that explicitly address the chunking problem, such as methods that use adaptive learning rates for each chunk or methods that model the chunk structure. This would provide a more comprehensive evaluation of the proposed method and help to establish its relative merits.

Second, the authors should provide a theoretical analysis of the proposed method. This could involve relating the method to existing optimization techniques or providing guarantees in terms of convergence or generalization. For example, the authors could investigate whether the per-chunk weight averaging method can be viewed as a form of stochastic gradient descent with a specific learning rate schedule. They could also analyze the method's behavior in a simplified setting, such as linear regression, to gain insights into its convergence properties. A theoretical framework would not only strengthen the paper's contribution but also provide a deeper understanding of the method's behavior and limitations. This analysis should also explore the sensitivity of the method to the number of chunks and the size of each chunk, providing guidance on how to choose these parameters in practice.

Finally, the paper should include a more thorough comparison with existing continual learning methods, even if those methods do not explicitly address the chunking problem. While the authors argue that current CL methods do not address the chunking problem, it is still important to show how the proposed method compares to these methods in terms of performance. This comparison should include a range of CL methods, such as replay-based methods, regularization-based methods, and parameter isolation methods. This would help to contextualize the proposed method and demonstrate its advantages over existing approaches. The authors should also consider comparing their method with online learning algorithms, as the chunking problem shares similarities with online learning scenarios. This would provide a more comprehensive evaluation of the proposed method and help to establish its relative merits.

### Questions

- How does the proposed method perform in the class-imbalanced chunking setting?
- Can the authors provide a theoretical analysis of the proposed method?
- How does the proposed method compare to other existing methods for addressing the chunking problem?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
