### Summary

This paper studies the generalization of preference optimization under noisy feedback. The authors provide generalization guarantees for a broad family of preference optimization losses such as DPO, IPO, SLiC, etc. The analysis provides the basis for a general model that describes how the generalization decays with the noise rate. Empirical validation on contemporary LLMs confirms the practical relevance of the findings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis seems to be correct and solid.
3. The findings are of great significance for the development of robust AI systems.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis is based on the assumption that the sample embeddings are from a hyperspherical distribution with unit norm. This assumption is crucial for the proof, but it may not hold in real-world scenarios. Specifically, while L2 normalization is common, it doesn't guarantee a perfect hyperspherical distribution, and deviations from this assumption could impact the validity of the derived generalization bounds. The analysis should discuss the sensitivity of the results to violations of this assumption.
2. The paper lacks a discussion of the limitations of the proposed approach. For example, the analysis focuses on a specific type of noise (random label flipping) and it is unclear how the results would generalize to other types of noise, such as systematic biases in human feedback or adversarial examples. Furthermore, the analysis does not explicitly address the impact of different model architectures or training procedures on the derived bounds.

### Suggestions

The paper should include a more detailed discussion of the hyperspherical distribution assumption and its potential impact on the results. Specifically, the authors should explore the sensitivity of their theoretical findings to deviations from this assumption. This could involve analyzing how the generalization bounds change when the embeddings are not perfectly normalized or when the distribution deviates from the von Mises-Fisher distribution. For instance, the authors could consider adding a section that discusses the robustness of their results to different types of embedding distributions, perhaps by introducing a parameter that quantifies the degree of deviation from the hyperspherical assumption. This would provide a more comprehensive understanding of the applicability of their theoretical framework in real-world scenarios.

Furthermore, the paper should expand its discussion of the limitations of the proposed approach. The current analysis focuses on random label flipping, but real-world noise is often more complex. The authors should discuss how their results might be affected by other types of noise, such as systematic biases in human feedback or adversarial examples. For example, they could explore how the generalization bounds would change if the noise was not uniformly random but instead correlated with certain features of the input or the model's predictions. Additionally, the authors should consider the impact of different model architectures and training procedures on their derived bounds. It would be beneficial to discuss whether the bounds are specific to certain types of models or training methods, or if they are more generally applicable. This would help to clarify the scope and limitations of their theoretical analysis.

Finally, the paper should provide more concrete guidance on how to apply their theoretical findings in practice. While the theoretical analysis is valuable, it would be helpful to provide practical recommendations for how to use the derived bounds to improve the robustness of preference optimization algorithms. For example, the authors could discuss how to choose the appropriate hyperparameters or how to detect and mitigate the effects of noisy feedback. This would make the paper more accessible to practitioners and increase its impact on the field. The authors could also consider providing a case study or example to illustrate how their theoretical results can be used to guide the development of more robust preference optimization algorithms.

### Questions

Please see weaknesses.

### Rating

6

### Confidence

3

**********
