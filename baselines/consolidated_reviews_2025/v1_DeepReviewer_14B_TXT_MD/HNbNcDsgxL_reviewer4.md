### Summary

The paper introduces Delta, a novel approach to mitigate hallucinations in large language models (LLMs) during inference. Delta leverages contrastive decoding by masking portions of the input prompt and comparing the output distributions of the original and masked inputs. This method effectively reduces hallucinations without requiring model retraining or additional training data. The authors evaluate Delta on context-rich question-answering benchmarks, demonstrating significant improvements in exact match and F1 scores. However, they note that Delta's effectiveness is limited in tasks without explicit contextual information, such as CommonsenseQA and MMLU.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to mitigating hallucinations in LLMs using contrastive decoding with masked inputs. This is a creative application of existing techniques to a new problem.
2. The method is evaluated on a variety of question-answering benchmarks, providing a comprehensive assessment of its effectiveness across different types of context-rich tasks.
3. The paper demonstrates that Delta can improve the performance of LLMs on tasks with explicit contextual information, showing its potential for practical applications in QA systems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead introduced by the Delta method. Understanding the trade-offs between performance gains and computational costs is crucial for practical applications.
2. The paper could benefit from a more in-depth discussion of the limitations of the Delta method, particularly in scenarios where contextual information is limited or absent. While the paper acknowledges this limitation, it does not delve into the underlying reasons why Delta struggles in these scenarios.
3. The paper could explore the potential of combining Delta with other methods for reducing hallucinations in LLMs. A comparative analysis with existing techniques would provide a more comprehensive understanding of Delta's strengths and weaknesses.

### Suggestions

To address the lack of computational analysis, the authors should include a detailed breakdown of the inference time for the Delta method. This should include the time taken for the initial forward pass, the masking step, the second forward pass, and the contrastive decoding process. The analysis should also explore how these times scale with input sequence length and the number of masking iterations. Furthermore, it would be beneficial to compare the computational cost of Delta with other methods for reducing hallucinations, such as those based on knowledge retrieval or fact verification. This would provide a clearer understanding of the trade-offs between performance gains and computational overhead. The authors could also investigate techniques to optimize the implementation of Delta to reduce its computational footprint, such as using more efficient masking strategies or parallelizing the forward passes.

To enhance the discussion of limitations, the authors should provide a more detailed analysis of why Delta struggles in scenarios with limited or absent contextual information. This could involve examining the types of questions or contexts where Delta is likely to fail. For example, the authors could analyze the performance of Delta on different subsets of the CommonsenseQA and MMLU datasets, identifying specific question types or knowledge domains where the method is less effective. This analysis should also explore the underlying reasons for these limitations, such as the method's reliance on contextual cues for contrastive decoding. The authors could also investigate potential modifications to the Delta method that might improve its performance in these scenarios, such as incorporating external knowledge sources or using a different contrastive decoding strategy. Furthermore, the authors should consider exploring the impact of different masking strategies on the performance of Delta, such as varying the masking ratio or using different masking patterns. This could provide insights into how to optimize the method for different types of tasks and datasets.

Finally, the authors should explore the potential of combining Delta with other methods for reducing hallucinations in LLMs. This could involve conducting a comparative analysis with existing techniques, such as knowledge retrieval, fact verification, or adversarial training. The analysis should highlight the strengths and weaknesses of each method and discuss how they might complement each other. For example, the authors could investigate whether combining Delta with a knowledge retrieval method could improve its performance on tasks with limited contextual information. They could also explore whether using Delta as a pre-processing step for other hallucination reduction methods could enhance their effectiveness. The paper should also discuss the potential challenges and limitations of integrating Delta with other approaches, such as increased computational complexity or the need for additional training data. This would provide a more comprehensive understanding of the potential of Delta and its place within the broader landscape of hallucination mitigation techniques.

### Questions

1. How does the computational overhead of the Delta method compare to other methods for reducing hallucinations in LLMs?
2. Are there any specific types of hallucinations that Delta is particularly effective or ineffective at addressing?
3. How does the performance of Delta vary across different LLM architectures and sizes?
4. What are the potential challenges and limitations of implementing Delta in real-world applications?

### Rating

5

### Confidence

3

**********
