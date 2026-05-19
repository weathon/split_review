### Summary

This paper proposes a metric called model kinship to measure the similarity between LLMs and uses it to guide model merging.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method incurs almost no additional computational cost while achieving good performance.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not well-motivated. The authors fail to provide a reasonable explanation for why model kinship should be a good indicator for model merging. Specifically, the paper lacks a theoretical justification for why the proposed kinship metric, based on weight differences, would correlate with successful merging. The authors should provide a more rigorous argument, potentially drawing from existing theories on model parameter spaces and transfer learning.
- The performance improvement achieved by the proposed method is very marginal. For example, in Table 2, the improvement is only 0.41% (69.13 vs. 68.72). The authors should clarify whether this difference is statistically significant and provide a more detailed analysis of the practical implications of such a small gain. It is unclear if this minor improvement justifies the complexity introduced by the kinship-based selection process.
- The authors only conduct experiments with a limited set of models and benchmarks. For example, they only use Mistral-based models and a single benchmark (Avg.) to evaluate model merging performance. This raises concerns about the generalizability of the findings. The authors should demonstrate the effectiveness of their method across a wider range of model architectures and datasets to ensure that the observed results are not specific to the chosen models and tasks.

### Suggestions

The paper would benefit significantly from a more robust theoretical foundation for the proposed model kinship metric. The authors should explore existing literature on model parameter spaces, transfer learning, and feature representations to provide a clear rationale for why the similarity of weight differences should be a good indicator for model merging potential. For instance, they could investigate whether the proposed metric correlates with the alignment of feature spaces or the compatibility of learned representations. A deeper analysis of the underlying mechanisms that drive successful model merging would strengthen the motivation for using model kinship. Furthermore, the authors should consider exploring alternative metrics for measuring model similarity, such as those based on activation patterns or gradient flow, and compare their effectiveness with the proposed weight-based metric.

To address the marginal performance gains, the authors should conduct a more rigorous statistical analysis of their results. This should include reporting confidence intervals or p-values to determine the significance of the observed improvements. Additionally, they should provide a more detailed analysis of the practical implications of the performance gains. For example, they could investigate whether the proposed method leads to improvements in specific downstream tasks or applications. It would also be beneficial to explore the sensitivity of the method to different hyperparameter settings and to analyze the computational overhead introduced by the kinship-based selection process. The authors should also consider comparing their method with other model merging techniques to provide a more comprehensive evaluation of its effectiveness.

Finally, the authors need to significantly expand the scope of their experimental evaluation. This should include using a wider range of model architectures, such as different transformer variants or models with different sizes. They should also evaluate their method on multiple benchmarks, including datasets with different characteristics and complexities. This would help to demonstrate the generalizability of the proposed method and ensure that the observed results are not specific to the chosen models and tasks. Furthermore, the authors should consider exploring the impact of different training strategies on the effectiveness of model kinship. For example, they could investigate whether the proposed method works equally well for models trained with different optimization algorithms or learning rates.

### Questions

- In Table 1, the authors conclude that model kinship alone is insufficient for predicting whether a model can achieve generalization gains through merging. If this is the case, what is the motivation for using model kinship for guiding model merging? 
- In Figure 3a, the proposed method does not show any advantage over the greedy method. In Figure 3b, the proposed method even performs worse than the greedy method in Generation 4. 
- In Table 2, the performance improvement is very marginal. For example, 69.13 vs. 68.72. Is it statistically significant?

### Rating

3

### Confidence

3

**********
