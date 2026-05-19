### Summary

This paper proposes a novel approach to scaling LLM inference for code generation. The authors frame code generation as a black-box optimization problem and introduce a tree-search algorithm called SCATTER, which is composed of three key components: SCATTER, FOREST, and SCOUT. SCATTER enhances exploration by enabling the LLM to propose diverse solution improvements, FOREST improves exploitation by sharing feedback and experiences across search branches, and SCOUT utilizes global insights to guide the search process. The authors provide a theoretical analysis demonstrating how these techniques avoid local optima during optimization. The method is evaluated on five code generation benchmarks, including HumanEval, MBPP, APPS, CodeContests, and Leetcode, and shows significant performance improvements over existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach to code generation by framing it as a black-box optimization problem and introducing a tree-search algorithm that combines exploration and exploitation. This is a significant departure from traditional methods and offers a fresh perspective on how to improve code generation with LLMs.
- The paper provides a theoretical analysis to support the effectiveness of the proposed techniques, demonstrating how they avoid local optima during optimization. This adds credibility to the proposed method and provides a solid foundation for future research.
- The method is evaluated on five code generation benchmarks, including HumanEval, MBPP, APPS, CodeContests, and Leetcode, and shows significant performance improvements over existing methods. The empirical results are compelling and demonstrate the effectiveness of the proposed approach.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its components. The figures and tables are well-designed and help to illustrate the key concepts and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for practical applications. While the authors mention faster convergence, a detailed breakdown of the time and resources required for each component (SCATTER, FOREST, and SCOUT) is needed. This should include a comparison with existing methods, not just in terms of overall runtime but also in terms of memory usage and the number of API calls to the LLM. For example, the authors could provide a table showing the average time per iteration, the total number of tokens processed, and the API call count for SCATTER compared to baseline methods on each benchmark. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be beneficial to analyze how the computational cost scales with the size of the code generation task, such as the length of the input prompt or the complexity of the desired output.
- The paper does not compare the proposed method with some recent state-of-the-art methods, such as DeepSeek-Coder and CodeGen. While the paper compares against several baselines, the field has rapidly advanced, and the absence of comparisons with models like DeepSeek-Coder and CodeGen is a significant gap. These models have demonstrated strong performance on code generation tasks, and their inclusion would provide a more comprehensive understanding of SCATTER's relative performance. The authors should consider evaluating SCATTER on the same benchmarks used by these models, or at least provide a discussion of how SCATTER might perform relative to these models based on their reported results. This would help to contextualize the contribution of the proposed method and highlight its strengths and weaknesses compared to the current state-of-the-art. Additionally, it would be valuable to analyze the performance of SCATTER on more complex code generation tasks, such as those involving multi-file projects or intricate dependencies, to better understand its limitations and potential for real-world applications.
- The paper does not discuss the limitations of the proposed method, such as its performance on more complex code generation tasks. While the authors mention that SCATTER is not designed for tasks that require external tools or libraries, a more thorough analysis of its performance on more complex code generation tasks is needed. For example, the authors could discuss how SCATTER might perform on tasks that require advanced programming concepts, such as concurrency, multithreading, or networking, which are not explicitly addressed in the current evaluation. Furthermore, it would be beneficial to analyze the method's sensitivity to the choice of hyperparameters and the impact of different LLMs on its performance. This would provide a more complete picture of the method's capabilities and limitations and help guide future research in this area. The authors should also discuss potential avenues for future work, such as how to extend SCATTER to handle more complex code generation tasks or how to improve its performance on tasks that require external tools or libraries.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost of the proposed SCATTER method. While the authors mention faster convergence, a more granular breakdown of the time and resources required for each component (SCATTER, FOREST, and SCOUT) is needed. This should include a comparison with existing methods, not just in terms of overall runtime but also in terms of memory usage and the number of API calls to the LLM. For example, the authors could provide a table showing the average time per iteration, the total number of tokens processed, and the API call count for SCATTER compared to baseline methods on each benchmark. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be beneficial to analyze how the computational cost scales with the size of the code generation task, such as the length of the input prompt or the complexity of the desired output. This analysis should also consider the impact of different LLMs on the computational cost, as the performance of the method may vary depending on the underlying model. A more thorough analysis of the computational aspects would significantly strengthen the paper's practical relevance.

To further enhance the paper, the authors should include comparisons with more recent state-of-the-art methods in code generation, such as DeepSeek-Coder and CodeGen. While the paper compares against several baselines, the field has rapidly advanced, and the absence of comparisons with these models is a significant gap. These models have demonstrated strong performance on code generation tasks, and their inclusion would provide a more comprehensive understanding of SCATTER's relative performance. The authors should consider evaluating SCATTER on the same benchmarks used by these models, or at least provide a discussion of how SCATTER might perform relative to these models based on their reported results. This would help to contextualize the contribution of the proposed method and highlight its strengths and weaknesses compared to the current state-of-the-art. Additionally, it would be valuable to analyze the performance of SCATTER on more complex code generation tasks, such as those involving multi-file projects or intricate dependencies, to better understand its limitations and potential for real-world applications. This analysis should also consider the impact of different LLMs on the performance of SCATTER, as the effectiveness of the method may vary depending on the underlying model.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. While the authors mention that SCATTER is not designed for tasks that require external tools or libraries, a more detailed analysis of its performance on more complex code generation tasks is needed. For example, the authors could discuss how SCATTER might perform on tasks that require advanced programming concepts, such as concurrency, multithreading, or networking, which are not explicitly addressed in the current evaluation. Furthermore, it would be beneficial to analyze the method's sensitivity to the choice of hyperparameters and the impact of different LLMs on its performance. This would provide a more complete picture of the method's capabilities and limitations and help guide future research in this area. The authors should also discuss potential avenues for future work, such as how to extend SCATTER to handle more complex code generation tasks or how to improve its performance on tasks that require external tools or libraries. This would provide a more comprehensive understanding of the method's strengths and weaknesses and help guide future research in this area.

### Questions

- How does the proposed method compare with some recent state-of-the-art methods, such as DeepSeek-Coder and CodeGen?
- What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

4

**********
