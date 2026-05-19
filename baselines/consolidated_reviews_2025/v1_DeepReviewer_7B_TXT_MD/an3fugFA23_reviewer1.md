### Summary

This paper proposes a method called Probability Distribution Estimation (PDE) to enable white-box detection methods to identify machine-generated text from proprietary LLMs. PDE estimates the full probability distribution of an LLM given partial observations from the model API, allowing existing white-box detection techniques to be applied to proprietary models. The authors demonstrate that PDE significantly improves detection accuracy across five LLMs and seven languages, achieving an average accuracy of 95% on XSum dataset.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to enable white-box detection methods for proprietary LLMs by estimating the full probability distribution from partial observations. This addresses a significant gap in the field where most existing detection methods rely on black-box techniques or outdated white-box methods that only work with open-source models.

2. The authors conduct extensive experiments across five different proprietary LLMs (GPT-3.5, GPT-4, Claude, Gemini, and ChatGPT) and seven languages, providing strong empirical evidence for the effectiveness of PDE. The results show consistent improvements over baseline methods, particularly for the latest LLMs like GPT-4 and Gemini, demonstrating the practical relevance of the proposed approach.

3. The paper is well-organized and clearly explains the technical details of PDE and its application to white-box detection methods. The authors provide a thorough description of the estimation algorithms used (Geometric, Zipfian, and MLP models) and the experimental setup, making it easy for readers to understand and potentially replicate the work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on detection accuracy and does not thoroughly explore the practical implications of using PDE in real-world scenarios. For example, the computational cost of estimating the full probability distribution, especially with larger models, is not fully analyzed. While the authors mention that PDE reduces the number of generations needed for detection compared to black-box methods, a more detailed breakdown of the computational resources required (e.g., API calls, memory usage) would be valuable. Furthermore, the paper lacks a discussion on the latency introduced by the PDE estimation process, which is crucial for real-time applications. A comparison of the computational cost with other detection methods, including black-box approaches, would provide a more comprehensive understanding of the trade-offs involved.

2. The paper assumes that the partial observations from the model API are representative of the full probability distribution. However, this assumption may not always hold true, especially if the API only provides limited context or biased outputs. The paper does not address how the quality and quantity of the partial observations affect the accuracy of the estimated distribution. For instance, if the API only returns the most probable token, the estimation might be significantly skewed. The paper should include an analysis of the sensitivity of PDE to the quality and quantity of the partial observations, and discuss potential strategies to mitigate the impact of biased or limited API access.

3. While the paper demonstrates the effectiveness of PDE across different LLMs and languages, it does not explore the limitations of the approach in detail. For example, it is unclear how PDE performs on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable. The paper should include a discussion on the potential challenges of applying PDE to domains with limited training data for the proprietary models. Furthermore, the paper does not investigate the robustness of PDE against adversarial attacks that might manipulate the partial observations to mislead the estimation process. A more thorough analysis of the limitations and potential failure modes of PDE would provide a more balanced view of its applicability.

### Suggestions

To enhance the practical relevance of the paper, the authors should provide a more detailed analysis of the computational cost associated with PDE. This should include a breakdown of the resources required for the estimation process, such as the number of API calls, memory usage, and latency. A comparison of these costs with those of other detection methods, including both black-box and white-box approaches, would be beneficial. Furthermore, the authors should investigate strategies to optimize the PDE estimation process for efficiency, such as using more efficient estimation algorithms or parallelizing the computation. This would make the approach more feasible for real-world applications, especially those with limited computational resources. The authors could also explore the trade-off between the accuracy of the estimated distribution and the computational cost, providing guidelines for selecting the appropriate estimation method based on the available resources.

To address the limitations of using partial observations, the authors should conduct a more thorough analysis of how the quality and quantity of these observations affect the accuracy of PDE. This could involve experiments with different types of partial observations, such as varying the length of the context or the number of tokens provided. The authors should also investigate the sensitivity of PDE to biased or noisy partial observations, and discuss potential strategies to mitigate these effects. For example, they could explore techniques for weighting the partial observations based on their reliability or using robust estimation methods that are less sensitive to outliers. Additionally, the authors should discuss the implications of using different API access patterns, such as those that provide only a subset of the tokens or those that are subject to rate limiting. This would provide a more comprehensive understanding of the limitations of PDE and its applicability in real-world scenarios.

Finally, the paper should include a more detailed discussion of the limitations of PDE and potential failure modes. This should include an analysis of how PDE performs on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable. The authors should also investigate the robustness of PDE against adversarial attacks that might manipulate the partial observations to mislead the estimation process. This could involve experiments with different types of adversarial attacks, such as those that introduce noise or bias into the partial observations. Furthermore, the authors should discuss potential strategies to mitigate these risks, such as using robust estimation methods or incorporating additional information about the model's behavior. A more thorough analysis of these limitations would provide a more balanced view of the applicability of PDE and guide future research in this area.

### Questions

1. How does the computational cost of PDE compare to other detection methods, especially in real-time applications? Could you provide a more detailed breakdown of the resources required for the estimation process?

2. How sensitive is PDE to the quality and quantity of the partial observations from the model API? What strategies could be used to mitigate the impact of biased or limited API access?

3. How does PDE perform on less common or highly specialized domains, where the probability distributions of proprietary models might be less predictable? Are there any specific challenges or limitations in these scenarios?

### Rating

5

### Confidence

4

**********
