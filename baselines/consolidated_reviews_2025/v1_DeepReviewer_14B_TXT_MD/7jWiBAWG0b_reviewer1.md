### Summary

This paper studies the algorithmic stability and generalization properties of pairwise SGD in non-convex settings with heavy-tailed gradient noise. The authors derive stability and generalization bounds that improve upon previous results by eliminating the bounded gradient assumption. They also establish sharper error bounds under a gradient dominance condition and extend their analysis to minibatch pairwise SGD, providing stability-based near-optimal bounds that align with empirical observations.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a comprehensive theoretical framework for non-convex pairwise SGD under heavy-tailed noise, addressing a significant gap in learning theory.

2. By removing the bounded gradient assumption, the results are more broadly applicable to practical scenarios with heavy-tailed noise.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical results, while novel, may be challenging for practitioners to apply directly due to their complexity. The derived bounds, while mathematically sound, involve multiple nested terms and constants that are difficult to estimate or interpret in real-world scenarios. This makes it hard to translate the theoretical insights into practical guidelines for hyperparameter tuning or algorithm design. For example, the constants hidden within the big-O notation may have a significant impact on the actual performance, but these are not explicitly addressed, limiting the practical utility of the results.

2. The paper could benefit from empirical validation of the theoretical bounds through experiments on real-world datasets. The absence of empirical validation makes it difficult to assess the practical relevance of the derived bounds. It is unclear how well these bounds capture the behavior of pairwise SGD in realistic settings, and whether the assumptions made in the analysis hold in practice. Without empirical evidence, the theoretical findings remain somewhat abstract and their practical impact is hard to gauge.

### Suggestions

To enhance the practical applicability of the theoretical results, the authors should consider providing more concrete guidance on how to estimate or bound the constants involved in their derived bounds. This could involve exploring specific examples or case studies where the bounds can be explicitly calculated or approximated. Furthermore, the authors could investigate the sensitivity of their bounds to different parameter settings and provide recommendations on how to choose parameters to achieve the best possible performance. For instance, they could explore the relationship between the heavy-tailed parameter and the convergence rate, and provide practical guidelines on how to select this parameter based on the characteristics of the dataset. This would make the theoretical results more accessible and useful for practitioners.

In addition to providing more practical guidance, the authors should conduct a thorough empirical evaluation of their theoretical bounds using real-world datasets. This would involve implementing pairwise SGD with heavy-tailed noise and comparing the observed performance with the predicted bounds. The experiments should cover a range of datasets with varying characteristics, such as different levels of noise and dimensionality, to assess the robustness of the theoretical findings. The authors should also explore the impact of different hyperparameter settings on the performance of pairwise SGD and compare these results with their theoretical predictions. This empirical validation would provide valuable insights into the practical relevance of the theoretical bounds and help to identify potential limitations or areas for improvement.

Finally, the authors should consider providing a more detailed discussion of the limitations of their theoretical analysis and potential directions for future research. This could include exploring alternative assumptions or analysis techniques that could lead to more practical bounds. For example, they could investigate the possibility of deriving bounds that are less sensitive to the constants hidden within the big-O notation, or explore the use of different stability measures that may be more suitable for pairwise learning. This would help to further advance the field and provide a more complete understanding of the behavior of pairwise SGD in non-convex settings with heavy-tailed noise.

### Questions

1. How do the theoretical bounds derived in the paper translate to practical performance improvements in real-world pairwise learning tasks?

2. Can the authors provide specific examples or case studies where their stability and generalization bounds offer tangible benefits over existing methods?

### Rating

6

### Confidence

3

**********
