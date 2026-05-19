### Summary

This paper studies the generalization performance of pairwise learning under heavy-tailed gradient noise. The authors establish stability-based learning guarantees for non-convex pairwise learning, and extend their analysis to the corresponding minibatch case. The authors also provide the first stability-based near-optimal generalization and optimization bounds for non-convex pairwise learning with heavy tails.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper provides a thorough study on the generalization error of non-convex pairwise learning with heavy-tailed gradient noise. The authors establish stability-based learning guarantees for non-convex pairwise learning, and extend their analysis to the corresponding minibatch case. The authors also provide the first stability-based near-optimal generalization and optimization bounds for non-convex pairwise learning with heavy tails.

2. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Stochastic gradient descent on non-convex objectives over non-independent and non-identically distributed data.
[2] Stochastic gradient descent on population and minimax risks for nonconvex losses.
[3] Generalization error bounds for deep learning with heavy-tailed losses and unbounded data.
[4] Generalization error bounds for deep learning with heavy-tailed losses and unbounded data.

#### comment

1. The authors should provide a more detailed comparison with existing work on pairwise learning, such as [1,2,3,4]. Specifically, the paper should clarify how the proposed stability-based approach differs from existing generalization bounds for pairwise learning, particularly those that may not rely on stability. A more thorough discussion of the assumptions made in this paper compared to those in [1,2,3,4] is needed, especially regarding the nature of the loss function and the data distribution. For instance, are there specific scenarios where the stability-based bounds are expected to be tighter or more informative than the bounds derived in [1,2,3,4]?

2. The authors should provide a more detailed discussion on the technical novelty of the proposed approach. While the paper mentions the use of stability, it does not fully explain how this approach overcomes the limitations of existing techniques. For example, how does the stability analysis handle the non-convexity of the loss function, and what are the key technical challenges that are overcome in this process? A more detailed explanation of the mathematical tools and techniques used to derive the stability bounds would be beneficial.

### Suggestions

The paper would benefit from a more in-depth comparison with existing work on pairwise learning. The authors should explicitly highlight the differences in the assumptions made, the types of loss functions considered, and the data distributions assumed. For example, while [1,2,3,4] may not explicitly rely on stability, they often make assumptions about the loss function's properties (e.g., smoothness, boundedness) or the data distribution (e.g., bounded gradients). A detailed comparison should clarify whether the proposed stability-based approach offers advantages in specific scenarios, such as when the loss function is highly non-convex or when the data exhibits heavy-tailed behavior. The authors should also discuss the limitations of their approach compared to existing methods, and identify potential areas for future research.

To further clarify the technical novelty, the authors should provide a more detailed explanation of how the stability analysis is used to derive the generalization bounds. This should include a discussion of the key mathematical steps involved in the analysis, and how these steps differ from those used in previous work. For instance, the authors could elaborate on how the stability constants are derived and how they relate to the properties of the loss function and the data distribution. A concrete example of how the stability analysis is applied to a specific pairwise learning problem would also be helpful. The authors should also discuss the limitations of their approach, such as the assumptions made on the noise distribution and the learning rate schedule.

Finally, the authors should provide more intuition behind the derived bounds. While the paper presents the bounds, it does not fully explain why these bounds are expected to hold and what they signify in terms of the generalization performance of pairwise learning. A more detailed discussion of the factors that influence the tightness of the bounds, such as the learning rate, the batch size, and the properties of the loss function, would be beneficial. The authors should also discuss the practical implications of their results, such as how they can be used to guide the design of pairwise learning algorithms. This would help to make the paper more accessible and impactful to a wider audience.

### Questions

1. The authors should provide a more detailed comparison with existing work on pairwise learning, such as [1,2,3,4]. 

2. The authors should provide a more detailed discussion on the technical novelty of the proposed approach.

### Rating

6

### Confidence

3

**********
