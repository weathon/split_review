### Summary

This paper proposes a novel approach to scaling LLM inference for code generation by framing it as a black-box optimization problem. The authors introduce SCATTER, a tree search method that enhances exploration and exploitation in the code space. The method consists of three key components: SCATTER, which improves solution diversity; FOREST, which shares feedback and experiences across search branches; and SCOUT, which utilizes global insights to guide the search. The authors provide a theoretical analysis to support their approach and demonstrate significant performance improvements over existing methods on several code generation benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel perspective by framing code generation as a black-box optimization problem, which is a fresh and promising approach.
2. The proposed SCATTER method, with its three components (SCATTER, FOREST, and SCOUT), is well-designed and addresses the exploration-exploitation trade-off in code generation.
3. The paper provides a theoretical analysis to support the effectiveness of the proposed method, which adds credibility to the approach.
4. The empirical results demonstrate significant performance improvements over existing methods on several code generation benchmarks, highlighting the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for practical applications. While the authors mention faster convergence, a detailed breakdown of the time and resources required for each component (SCATTER, FOREST, and SCOUT) is needed. This should include a comparison with existing methods, not just in terms of overall runtime but also in terms of memory usage and the number of API calls to the LLM. For example, the authors could provide a table showing the average time per iteration, the total number of tokens processed, and the API call count for SCATTER compared to baseline methods on each benchmark. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be beneficial to analyze how the computational cost scales with the size of the code generation task, such as the length of the input prompt or the complexity of the desired output.
2. The paper does not compare the proposed method with some recent state-of-the-art methods, such as DeepSeek-Coder and CodeGen. While the paper compares against several baselines, the field has rapidly advanced, and the absence of comparisons with models like DeepSeek-Coder and CodeGen is a significant gap. These models have demonstrated strong performance on code generation tasks, and their inclusion would provide a more comprehensive understanding of SCATTER's relative performance. The authors should consider evaluating SCATTER on the same benchmarks used by these models, or at least provide a discussion of how SCATTER might perform relative to these models based on their reported results. This would help to contextualize the contribution of the proposed method and highlight its strengths and weaknesses compared to the current state-of-the-art. Additionally, it would be valuable to analyze the performance of SCATTER on more complex code generation tasks, such as those involving multi-file projects or intricate dependencies, to better understand its limitations and potential for real-world applications.
3. The paper does not discuss the limitations of the proposed method, such as its performance on more complex code generation tasks. While the authors mention that SCATTER is not designed for tasks that require external tools or libraries, a more thorough analysis of its performance on more complex code generation tasks is needed. For example, the authors could discuss how SCATTER might perform on tasks that require advanced programming concepts, such as concurrency, multithreading, or networking, which are not explicitly addressed in the current evaluation. Furthermore, it would be beneficial to analyze the method's sensitivity to the choice of hyperparameters and the impact of different LLMs on its performance. This would provide a more complete picture of the method's capabilities and limitations and help guide future research in this area. The authors should also discuss potential avenues for future work, such as how to extend SCATTER to handle more complex code generation tasks or how to improve its performance on tasks that require external tools or libraries.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the proposed SCATTER method. While the authors mention faster convergence, a detailed breakdown of the time and resources required for each component (SCATTER, FOREST, and SCOUT) is needed. This should include a comparison with existing methods, not just in terms of overall runtime but also in terms of memory usage and the number of API calls to the LLM. For example, the authors could provide a table showing the average time per iteration, the total number of tokens processed, and the API call count for SCATTER compared to baseline methods on each benchmark. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be beneficial to analyze how the computational cost scales with the size of the code generation task, such as the length of the input prompt or the complexity of the desired output. This analysis should also consider the impact of different LLMs on the computational cost, as the performance of the method may vary depending on the underlying model. A more detailed analysis of the computational aspects would significantly strengthen the paper's practical relevance.

To further enhance the paper, the authors should include comparisons with more recent state-of-the-art methods in code generation, such as DeepSeek-Coder and CodeGen. While the paper compares against several baselines, the field has rapidly advanced, and the absence of comparisons with models like DeepSeek-Coder and CodeGen is a significant gap. These models have demonstrated strong performance on code generation tasks, and their inclusion would provide a more comprehensive understanding of SCATTER's relative performance. The authors should consider evaluating SCATTER on the same benchmarks used by these models, or at least provide a discussion of how SCATTER might perform relative to these models based on their reported results. This would help to contextualize the contribution of the proposed method and highlight its strengths and weaknesses compared to the current state-of-the-art. Additionally, it would be valuable to analyze the performance of SCATTER on more complex code generation tasks, such as those involving multi-file projects or intricate dependencies, to better understand its limitations and potential for real-world applications. This analysis should also consider the impact of different LLMs on the performance of SCATTER, as the effectiveness of the method may vary depending on the underlying model.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. While the authors mention that SCATTER is not designed for tasks that require external tools or libraries, a more detailed analysis of its performance on more complex code generation tasks is needed. For example, the authors could discuss how SCATTER might perform on tasks that require advanced programming concepts, such as concurrency, multithreading, or networking, which are not explicitly addressed in the current evaluation. Furthermore, it would be beneficial to analyze the method's sensitivity to the choice of hyperparameters and the impact of different LLMs on its performance. This would provide a more complete picture of the method's capabilities and limitations and help guide future research in this area. The authors should also discuss potential avenues for future work, such as how to extend SCATTER to handle more complex code generation tasks or how to improve its performance on tasks that require external tools or libraries. This would provide a more comprehensive understanding of the method's strengths and weaknesses and help guide future research in this area.

### Questions

Please see the weakness.

### Rating

8

### Confidence

4

**********
