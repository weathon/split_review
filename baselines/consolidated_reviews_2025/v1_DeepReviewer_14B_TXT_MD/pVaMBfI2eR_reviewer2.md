### Summary

This paper addresses the challenge of domain shift in federated learning by proposing a novel method called Federated Dual Prompt Tuning (Fed-DPT). The paper leverages prompt learning and pre-trained vision-language models to improve domain adaptation in decentralized data. The proposed method outperforms existing approaches on three benchmarks, demonstrating its effectiveness in domain-aware federated learning.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a novel method called Federated Dual Prompt Tuning (Fed-DPT) that addresses the challenges of domain shift in federated learning. The method leverages prompt learning and pre-trained vision-language models to improve domain adaptation in decentralized data.

2. The paper provides a comprehensive overview of the challenges in federated learning, including domain shift and limited communication efficiency. It also discusses the limitations of existing approaches and the need for a more effective solution.

3. The paper is well-written and organized, making it easy to follow the proposed method and its evaluation. The authors provide a clear explanation of the problem, the proposed solution, and the experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that each client represents a specific domain, which may not always be the case in real-world scenarios. In practice, clients may have data from multiple domains, and the proposed method may not be effective in such cases. Specifically, the method's reliance on distinct prompts for each client-domain combination could lead to an explosion in the number of prompts required, making it impractical for scenarios where clients have even slightly overlapping domain distributions. The paper does not address the challenge of how to handle clients with mixed-domain data, which is a significant limitation.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is important to understand the computational requirements of the method, especially in resource-constrained environments. The paper lacks a breakdown of the computational cost associated with prompt generation, optimization, and inference. This makes it difficult to assess the practical feasibility of the method, especially when compared to simpler federated learning approaches.

3. The paper does not discuss the potential privacy concerns associated with the proposed method. In federated learning, privacy is a major concern, and it is important to address any potential privacy risks. The paper does not analyze how the prompt tuning process might leak information about the local client data through the shared prompts. A more thorough analysis of the privacy implications is needed, especially considering the sensitivity of data in federated learning settings.

### Suggestions

The paper should address the limitations of the proposed method in handling clients with mixed-domain data. One potential solution is to explore techniques for learning domain-invariant prompts or to develop a mechanism for dynamically selecting or generating prompts based on the specific domain distribution of each client's data. This could involve incorporating domain classification techniques or using a meta-learning approach to adapt prompts to different domain distributions. Furthermore, the paper should investigate the impact of the number of domains and the degree of overlap between domains on the performance of the proposed method. A more detailed analysis of the method's robustness to varying domain distributions is needed to demonstrate its practical applicability.

To address the lack of computational complexity analysis, the paper should provide a detailed breakdown of the computational cost associated with each step of the proposed method. This should include the cost of prompt generation, optimization, and inference. The analysis should also compare the computational complexity of the proposed method with that of existing federated learning approaches. It would be beneficial to provide a theoretical analysis of the computational complexity, as well as empirical results on the computational time and memory usage of the method. This analysis should consider the impact of the number of clients, the size of the model, and the number of prompts on the overall computational cost. Such an analysis would allow readers to better understand the practical feasibility of the method in resource-constrained environments.

Finally, the paper needs to include a thorough analysis of the privacy implications of the proposed method. The authors should investigate whether the prompt tuning process could leak information about the local client data through the shared prompts. This could involve analyzing the sensitivity of the prompts to changes in the local data and exploring techniques for mitigating any potential privacy risks. The paper should also discuss the potential for using differential privacy or other privacy-preserving techniques to protect the privacy of the client data. A more rigorous analysis of the privacy implications is essential to ensure the responsible deployment of the proposed method in real-world federated learning settings.

### Questions

1. How does the proposed method handle clients with data from multiple domains? What are the limitations of the method in such cases?

2. What is the computational complexity of the proposed method? How does it compare to existing federated learning approaches?

3. What are the potential privacy concerns associated with the proposed method? How can these concerns be addressed?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
