### Summary

This paper proposes a method to estimate the full distribution of a language model given partial observations from the model API, enabling white-box detection methods to identify machine-generated text from proprietary models. The authors introduce Probability Distribution Estimation (PDE) and demonstrate its effectiveness across multiple proprietary models and languages, achieving high detection accuracy.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to enable white-box detection methods for proprietary LLMs, addressing a significant gap in the field.
2. The authors provide extensive experimental results, demonstrating the effectiveness of PDE across various models and languages.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on detection accuracy and does not thoroughly explore the practical implications of using PDE in real-world scenarios. For example, the computational cost of estimating the full probability distribution, especially with larger models, is not fully analyzed. While the authors mention that PDE reduces the number of generations needed for detection compared to black-box methods, a more detailed breakdown of the computational resources required (e.g., API calls, memory usage) would be valuable. Furthermore, the paper lacks a discussion on the latency introduced by the PDE estimation process, which is crucial for real-time applications. A comparison of the computational cost with other detection methods, including black-box approaches, would provide a more comprehensive understanding of the trade-offs involved.
2. The paper assumes that the partial observations from the model API are representative of the full probability distribution. However, this assumption may not always hold true, especially if the API only provides limited context or biased outputs. The paper does not address how the quality and quantity of the partial observations affect the accuracy of the estimated distribution. For instance, if the API only returns the most probable token, the estimation might be significantly skewed. The paper should include an analysis of the sensitivity of PDE to the quality and quantity of the partial observations, and discuss potential strategies to mitigate the impact of biased or limited API access.
3. While the paper demonstrates the effectiveness of PDE across different LLMs and languages, it does not explore the limitations of the approach in detail. For example, it is unclear how PDE performs on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable. The paper should include a discussion on the potential challenges of applying PDE to domains with limited training data for the proprietary models. Furthermore, the paper does not investigate the robustness of PDE against adversarial attacks that might manipulate the partial observations to mislead the estimation process. A more thorough analysis of the limitations and potential failure modes of PDE would provide a more balanced view of its applicability.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the PDE method. Specifically, the authors should provide a detailed breakdown of the resources required for the estimation process, including the number of API calls, memory usage, and latency. This analysis should compare the computational cost of PDE with that of other detection methods, including both black-box and white-box approaches. For example, the authors could measure the time taken to estimate the full distribution for different model sizes and compare it with the time taken by other methods to generate and evaluate multiple outputs. This would provide a more complete picture of the practical implications of using PDE in real-world scenarios, especially for resource-constrained environments. Furthermore, the authors should explore potential optimizations to reduce the computational cost of PDE, such as using more efficient estimation algorithms or parallelizing the computation.

To address the limitations of relying on partial observations from the API, the authors should conduct a more comprehensive analysis of how the quality and quantity of these observations affect the accuracy of the estimated distribution. This could involve experiments with different types of partial observations, such as varying the length of the context or the number of tokens provided. The authors should also investigate the sensitivity of PDE to biased or noisy partial observations, and discuss potential strategies to mitigate these effects. For example, they could explore techniques for weighting the partial observations based on their reliability or using robust estimation methods that are less sensitive to outliers. Additionally, the authors should discuss the implications of using different API access patterns, such as those that provide only a subset of the tokens or those that are subject to rate limiting. This would provide a more realistic assessment of the applicability of PDE in real-world scenarios.

Finally, the paper should include a more detailed discussion of the limitations of PDE and potential failure modes. This should include an analysis of how PDE performs on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable. The authors should also investigate the robustness of PDE against adversarial attacks that might manipulate the partial observations to mislead the estimation process. For example, they could explore scenarios where the API provides biased or misleading partial observations and evaluate how PDE responds to these attacks. Furthermore, the authors should discuss potential strategies to mitigate these risks, such as using multiple sources of partial observations or incorporating additional information about the model's behavior. A more thorough analysis of these limitations would provide a more balanced view of the applicability of PDE and guide future research in this area.

### Questions

1. How does the computational cost of PDE compare to other detection methods, especially in real-time applications?
2. How sensitive is PDE to the quality and quantity of the partial observations from the model API? What strategies could be used to mitigate the impact of biased or limited API access?
3. How does PDE perform on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable?

### Rating

5

### Confidence

4

**********
