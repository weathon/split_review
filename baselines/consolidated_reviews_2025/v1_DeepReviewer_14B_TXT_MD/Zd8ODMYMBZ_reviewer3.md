### Summary

This paper introduces FAVICOMP, a training-free evidence compression method designed to enhance retrieval-augmented generation (RAG) in large language models (LMs). FAVICOMP makes retrieved evidence more familiar to the target model by integrating parametric knowledge during evidence compression. The method employs ensemble decoding to combine token logits from both the compression model and the target model, ensuring that the generated context is both relevant and familiar to the target model. Experimental results demonstrate that FAVICOMP outperforms recent evidence compression baselines across multiple open-domain QA datasets, with accuracy improvements of up to 23.91% while maintaining high compression rates.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel training-free evidence compression method, FAVICOMP, which effectively balances parametric and non-parametric knowledge in large language models (LLMs). This approach is particularly innovative in its use of ensemble decoding to integrate knowledge from both the compression model and the target model, ensuring that the generated context is both relevant and familiar to the target model. The method's ability to make retrieved evidence more "familiar" to the target model is a unique contribution that addresses a significant challenge in retrieval-augmented generation (RAG) systems.

2. The paper is well-structured and clearly written, making it accessible to a broad audience. The authors provide a thorough explanation of the motivation behind FAVICOMP, detailing the limitations of existing methods and how their approach addresses these issues. The methodology is presented in a logical sequence, with clear definitions and illustrations that aid in understanding the proposed framework.

3. The authors conduct extensive experiments across multiple open-domain QA datasets, demonstrating the effectiveness of FAVICOMP. The results show significant improvements in accuracy, with up to 23.91% increase compared to recent evidence compression baselines. The paper also includes ablation studies and analyses of compression rates, providing a comprehensive evaluation of the method's performance. The empirical findings are robust and well-supported, highlighting the practical benefits of FAVICOMP in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of FAVICOMP. While the method shows promising results, it is important to acknowledge potential drawbacks or scenarios where it might not perform as well. For example, the paper does not explore the sensitivity of the method to the choice of compression model, which could be a significant factor in its overall performance. Additionally, the computational overhead of the ensemble decoding process, while mentioned, is not thoroughly analyzed in terms of its impact on real-time applications. A more in-depth analysis of these limitations would provide a more balanced view of the method's capabilities.

2. The paper could provide more insights into the selection of the ensemble coefficient α. While the authors mention that α controls the balance between the compression model and the target model, the process of choosing the optimal value of α is not clearly explained. The paper lacks a detailed analysis of how different values of α affect the performance across various datasets and tasks. It would be beneficial to include a sensitivity analysis that demonstrates the impact of α on the final results, along with guidelines for selecting an appropriate value for different scenarios. This would enhance the practical applicability of the method and provide users with a better understanding of how to fine-tune the model for their specific needs.

### Suggestions

To address the limitations regarding the sensitivity of FAVICOMP to the choice of compression model, the authors should conduct a more thorough investigation into how different compression models affect the overall performance. This could involve experimenting with a range of compression models, including both smaller and larger models, and analyzing the resulting accuracy and compression rates. The analysis should also consider the trade-offs between compression efficiency and the quality of the generated context. For instance, a smaller compression model might offer faster processing times but could potentially lead to a loss of crucial information, while a larger model might retain more information but at the cost of increased computational overhead. The authors should provide a detailed discussion of these trade-offs and offer recommendations on how to select an appropriate compression model based on the specific requirements of the task. Furthermore, the paper should include a more detailed analysis of the computational overhead associated with the ensemble decoding process. This analysis should go beyond simply stating that the method is slower than other approaches and should instead provide a breakdown of the time spent on different stages of the process, such as evidence retrieval, compression, and ensemble decoding. The authors should also explore potential optimizations that could reduce the computational cost of the method, such as parallelizing the decoding process or using more efficient algorithms. This would make the method more practical for real-time applications and would enhance its overall appeal.

To improve the practical applicability of FAVICOMP, the authors should provide a more detailed analysis of the ensemble coefficient α. This analysis should include a sensitivity study that demonstrates how different values of α affect the performance of the method across various datasets and tasks. The authors should also provide guidelines for selecting an appropriate value of α based on the characteristics of the task and the desired balance between parametric and non-parametric knowledge. For example, they could explore whether a higher value of α is more suitable for tasks that require more reliance on the target model's internal knowledge, while a lower value of α might be better for tasks that require more reliance on the retrieved evidence. The authors should also investigate whether the optimal value of α varies across different datasets and tasks and provide recommendations on how to determine the best value for a given scenario. This would make the method more user-friendly and would allow practitioners to fine-tune the model for their specific needs. Additionally, the authors should consider providing a default value for α that works well across a range of tasks, which would serve as a starting point for users who are not sure how to choose the optimal value.

### Questions

1. How does the performance of FAVICOMP vary with different sizes of the target model? The paper mentions using a 13B target model, but it would be interesting to see how the method performs with smaller or larger models. This could provide insights into the scalability of the approach and its applicability to different computational resources.

2. Can the authors provide more details on the computational overhead of FAVICOMP compared to other methods? While the paper mentions that the method is slower, it would be helpful to have a more quantitative comparison of the time and resources required for different stages of the process, such as evidence retrieval, compression, and ensemble decoding.

### Rating

6

### Confidence

4

**********
