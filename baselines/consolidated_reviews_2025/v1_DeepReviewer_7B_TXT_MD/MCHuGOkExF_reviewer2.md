### Summary

This paper proposes a new approach to code generation with LLMs, called SCATTER, which frames code generation as a black-box optimization problem within the code space. The method includes three key components: SCATTER, which enhances exploration by enabling LLMs to propose diverse solution improvements; FOREST, which improves exploitation by sharing feedback and experiences across search branches; and SCOUT, which utilizes global insights to guide the search process. The authors demonstrate that SCATTER outperforms existing methods on five code generation benchmarks, including HumanEval, MBPP, APPS, CodeContests, and Leetcode, achieving significant performance improvements and faster convergence. The paper also provides a theoretical analysis to support the effectiveness of the proposed techniques.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach to code generation by framing it as a black-box optimization problem, which is a fresh perspective that has not been explored in previous work.
- The paper provides a comprehensive evaluation of the proposed method on five code generation benchmarks, demonstrating its effectiveness and scalability.
- The paper includes a theoretical analysis to support the effectiveness of the proposed techniques, which adds to the credibility of the work.
- The paper is well-written and easy to understand, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for practical applications.
- The paper does not compare the proposed method with some recent state-of-the-art methods, such as DeepSeek-Coder and CodeGen.
- The paper does not discuss the limitations of the proposed method, such as its performance on more complex code generation tasks.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the SCATTER method. While the authors mention faster convergence, a detailed breakdown of the time and resources required for each component (SCATTER, FOREST, and SCOUT) is needed. This should include a comparison with existing methods, not just in terms of overall runtime but also in terms of memory usage and the number of API calls to the LLM. For example, the authors could provide a table showing the average time per iteration, the total number of tokens processed, and the API call count for SCATTER compared to baseline methods on each benchmark. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be beneficial to analyze how the computational cost scales with the size of the code generation task, such as the length of the input prompt or the complexity of the desired output. 

To strengthen the paper's evaluation, it is crucial to include comparisons with more recent state-of-the-art methods in code generation. While the paper compares against several baselines, the field has rapidly advanced, and the absence of comparisons with models like DeepSeek-Coder and CodeGen is a significant gap. These models have demonstrated strong performance on code generation tasks, and their inclusion would provide a more comprehensive understanding of SCATTER's relative performance. The authors should consider evaluating SCATTER on the same benchmarks used by these models, or at least provide a discussion of how SCATTER might perform relative to these models based on their reported results. This would help to contextualize the contribution of the proposed method and highlight its strengths and weaknesses compared to the current state-of-the-art. Additionally, it would be valuable to analyze the performance of SCATTER on more complex code generation tasks, such as those involving multi-file projects or intricate dependencies, to better understand its limitations and potential for real-world applications.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors mention that SCATTER is not designed for tasks that require external tools or libraries, a more thorough analysis of its performance on more complex code generation tasks is needed. For example, the authors could discuss how SCATTER might perform on tasks that require advanced programming concepts, such as concurrency, multithreading, or networking, which are not explicitly addressed in the current evaluation. Furthermore, it would be beneficial to analyze the method's sensitivity to the choice of hyperparameters and the impact of different LLMs on its performance. This would provide a more complete picture of the method's capabilities and limitations and help guide future research in this area. The authors should also discuss potential avenues for future work, such as how to extend SCATTER to handle more complex code generation tasks or how to improve its performance on tasks that require external tools or libraries.

### Questions

- How does the proposed method compare with some recent state-of-the-art methods, such as DeepSeek-Coder and CodeGen?
- What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********
