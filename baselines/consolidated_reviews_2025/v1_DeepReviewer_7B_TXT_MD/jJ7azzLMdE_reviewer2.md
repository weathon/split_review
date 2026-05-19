### Summary

The paper introduces IoT-LLM, a framework designed to enhance the capabilities of Large Language Models (LLMs) for IoT task reasoning by integrating IoT sensor data and domain-specific knowledge. The framework comprises three key steps: IoT data simplification and enrichment, knowledge retrieval augmentation, and prompt configuration. The authors also present a new benchmark with five real-world IoT tasks to evaluate LLMs' performance in IoT reasoning. The results demonstrate that the IoT-LLM framework significantly improves LLMs' performance, achieving an average improvement of 65% across various tasks and LLMs.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-organized and clearly written, making it easy to follow and understand the proposed framework and its components.
- The authors provide a comprehensive evaluation of the IoT-LLM framework, including experiments across multiple LLMs and a new benchmark with five real-world IoT tasks.
- The paper addresses a critical gap in the literature by exploring the potential of LLMs in IoT task reasoning, which is an important area of research with practical applications.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed framework and potential areas for future research. For example, how does the framework handle noisy or incomplete IoT data, and what are the computational costs associated with the proposed approach?
- The paper could provide more insights into the specific challenges of IoT task reasoning and how the proposed framework addresses these challenges. For example, how does the framework handle the heterogeneity of IoT data and the complexity of real-world IoT systems?
- The paper could benefit from a more thorough comparison with existing approaches in the literature, highlighting the unique contributions and advantages of the proposed framework. For example, how does the IoT-LLM framework compare to other methods for integrating IoT data with LLMs, and what are the key differences in terms of performance and applicability?

### Suggestions

The paper would be significantly strengthened by a more thorough discussion of the limitations of the IoT-LLM framework. Specifically, the authors should address how the framework handles noisy or incomplete IoT data, which is a common challenge in real-world deployments. For instance, what mechanisms are in place to mitigate the impact of missing sensor readings or corrupted data points? Furthermore, the computational cost of the proposed approach should be analyzed in detail, including the time and resources required for data preprocessing, knowledge retrieval, and LLM inference. This analysis should consider the scalability of the framework to large-scale IoT deployments and provide insights into its practical applicability. A discussion of the trade-offs between performance and computational cost would also be valuable, allowing readers to assess the suitability of the framework for different use cases.

In addition to the limitations, the paper should provide a more in-depth analysis of the specific challenges of IoT task reasoning and how the proposed framework addresses them. The authors should elaborate on how the framework handles the heterogeneity of IoT data, which often involves diverse data types, varying units, and different sampling rates. For example, how does the framework ensure that the LLM can effectively process and integrate data from different sensors with varying levels of precision and resolution? Furthermore, the paper should discuss how the framework handles the complexity of real-world IoT systems, which may involve multiple interacting components and dynamic environments. The authors should provide examples of how the framework can be adapted to different types of IoT systems and tasks, highlighting its flexibility and robustness.

Finally, the paper should include a more comprehensive comparison with existing approaches in the literature. The authors should clearly articulate the unique contributions and advantages of the IoT-LLM framework, highlighting its performance and applicability compared to other methods for integrating IoT data with LLMs. For example, how does the proposed framework compare to existing methods that use rule-based systems or machine learning models for IoT task reasoning? The authors should also discuss the key differences in terms of performance, computational cost, and ease of implementation. A detailed comparison with relevant baselines would help to establish the novelty and significance of the proposed framework and provide a clearer understanding of its potential impact on the field.

### Questions

- How does the IoT-LLM framework handle noisy or incomplete IoT data, which is common in real-world scenarios?
- What are the computational costs associated with the proposed approach, and how does it scale to large-scale IoT deployments?
- How does the framework handle the heterogeneity of IoT data and the complexity of real-world IoT systems?
- How does the IoT-LLM framework compare to other methods for integrating IoT data with LLMs, and what are the key differences in terms of performance and applicability?

### Rating

6

### Confidence

3

**********
