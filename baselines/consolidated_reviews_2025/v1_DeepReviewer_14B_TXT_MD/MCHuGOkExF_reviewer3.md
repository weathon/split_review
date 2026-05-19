### Summary

This paper introduces a new approach to scaling LLM inference for code generation, framing it as a black-box optimization problem within the code space. The authors propose the Scattered Forest Search (SFS) method, which employs optimization-inspired techniques to enhance exploration and solution diversity. The key techniques include branch scatter, forest search, and branch scout, which dynamically vary input prompts, perform tree search from multiple seed solutions, and share feedback across search branches, respectively. Theoretical analysis is provided to illustrate how these methods avoid local optima during optimization. Extensive experiments on HumanEval, MBPP, APPS, CodeContests, and Leetcode benchmarks demonstrate significant performance improvements over state-of-the-art methods, including better accuracy, faster convergence, and greater solution diversity. The method is simple, parameter-free, and does not require additional training data, making it practical for large-scale deployments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to scaling LLM inference for code generation by framing it as a black-box optimization problem, which is a fresh perspective in the field.

2. The proposed Scattered Forest Search (SFS) method is innovative, combining techniques like branch scatter, forest search, and branch scout to enhance exploration and solution diversity.

3. The paper provides a solid theoretical foundation for the proposed methods, using Markov chain theory to analyze the conductance and mixing times, which strengthens the credibility of the approach.

4. The experimental evaluation is comprehensive, covering multiple benchmarks (HumanEval, MBPP, APPS, CodeContests, and Leetcode) and demonstrating significant performance improvements over state-of-the-art methods.

5. The method is practical and easy to implement, as it is parameter-free and does not require additional training data, making it suitable for large-scale deployments.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method. While the authors mention that SFS may not be suitable for all types of code generation tasks, a more in-depth analysis of the scenarios where SFS might underperform would be valuable. Specifically, the paper lacks a discussion on how the method might struggle with tasks requiring complex, multi-step reasoning or those that involve intricate control flow. It would be beneficial to see an analysis of how the method's performance degrades as the complexity of the required algorithm increases, or if there are specific types of programming problems where the search strategy is less effective.

2. The paper could provide more insights into the computational cost of the proposed method compared to other search techniques. While the authors claim that SFS scales efficiently, a more detailed analysis of the computational resources required, such as time and memory, would be helpful for practitioners. The paper should include a breakdown of the time spent on each component of the SFS method (e.g., branch scatter, forest search, branch scout) and compare it to the computational cost of baseline methods. This would allow for a more informed decision about the practical applicability of the method.

3. The paper could explore the generalization ability of the proposed method to other domains beyond code generation. While the current results are impressive, it would be interesting to see if the techniques could be applied to other optimization problems in different fields. The paper should discuss the potential challenges and adaptations required to apply SFS to other domains, such as combinatorial optimization problems or natural language processing tasks. This would broaden the impact of the work and demonstrate the versatility of the proposed approach.

### Suggestions

To address the limitations regarding the types of code generation tasks where SFS might underperform, the authors should include a more detailed analysis of the method's behavior on problems requiring complex reasoning and control flow. This could involve evaluating SFS on benchmarks that specifically test these capabilities, such as those involving algorithmic problem-solving with multiple nested loops or conditional statements. The authors should also analyze the search trajectories of SFS on these complex problems to identify where the method struggles. For example, do the branch scatter and scout techniques fail to generate diverse enough solutions, or does the forest search get stuck in local optima? A more granular analysis of the method's performance on different types of code generation tasks would provide a more complete picture of its strengths and weaknesses. Furthermore, the authors could consider incorporating techniques to explicitly encourage the generation of diverse control flow structures, such as using prompts that emphasize specific programming patterns or using a reward function that favors solutions with more complex control flow.

To provide a more detailed analysis of the computational cost, the authors should include a breakdown of the time spent on each component of the SFS method. This should include the time spent on branch scatter, forest search, and branch scout, as well as the time spent on evaluation. The authors should also compare the computational cost of SFS to that of baseline methods, such as simple sampling or tree search, on the same hardware. This comparison should include not only the total time but also the memory usage. The authors could also explore techniques to reduce the computational cost of SFS, such as using more efficient data structures or parallelizing the search process. This would make the method more practical for large-scale deployments. Additionally, the authors should provide a more detailed analysis of how the computational cost scales with the size of the code space and the number of iterations.

To explore the generalization ability of SFS to other domains, the authors should consider applying the method to a few representative problems in other fields. This could include combinatorial optimization problems, such as the traveling salesman problem or the knapsack problem, or natural language processing tasks, such as text summarization or machine translation. The authors should discuss the potential challenges and adaptations required to apply SFS to these domains. For example, how would the branch scatter and scout techniques be adapted to non-code domains? Would the evaluation function need to be modified? The authors should also analyze the performance of SFS on these other domains and compare it to existing methods. This would demonstrate the versatility of the proposed approach and broaden its impact.

### Questions

1. How does the performance of SFS vary with different LLMs? Have you tested the method with other models besides GPT-3.5, and if so, how does the performance compare?

2. How does the performance of SFS vary with different tasks? Have you evaluated the method on tasks other than code generation, and if so, how does it perform?

3. How does the performance of SFS vary with different hyperparameters? Have you conducted a sensitivity analysis to understand how the performance changes with different settings of the hyperparameters?

4. How does the performance of SFS vary with different problem sizes? Have you evaluated the method on problems of varying complexity, and if so, how does the performance scale with the size of the problem?

### Rating

6

### Confidence

3

**********
