### Summary

This paper proposes a new method called Scattered Forest Search (SFS) to improve code generation with LLMs by framing it as a black-box optimization problem. The key ideas are:

- SFS contains three core techniques:
  - Branch Scatter: Dynamically varies input prompts during tree search to generate more diverse solutions.
  - Forest Search: Performs tree search from multiple random seed solutions.
  - Branch Scout: Shares feedback across search branches to improve exploration.

- The method is motivated by optimization theory and analyzed using Markov chain theory.

- Experiments on five code generation benchmarks (HumanEval, MBPP, APPS, CodeContests, Leetcode) show significant improvements over state-of-the-art methods in terms of accuracy, scalability, and solution diversity.

- The method is simple to implement, requires no additional training data, and scales efficiently.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

Originality:

- Novel framing of code generation as a black-box optimization problem
- Innovative techniques for improving exploration and exploitation in tree search
- Creative combination of ideas from optimization theory and LLMs


Quality:

- Solid theoretical analysis using Markov chain theory
- Comprehensive experimental evaluation on multiple benchmarks
- Thorough ablation studies and analysis


Clarity:

- Clear problem definition and motivation
- Well-written explanation of the proposed method
- Effective use of figures and tables


Significance:

- Significant improvements over state-of-the-art methods
- Practical and easy-to-implement approach
- Potential for broad applicability to other code generation tasks

### Weaknesses

#### Some Related Works


#### comment

 - The method has many hyperparameters that require tuning.
- The method is relatively complex, involving multiple interacting components.
- The paper only uses gpt-3.5 for experiments. It would be interesting to see how the method performs with other LLMs, especially open-source ones.

### Suggestions

The paper introduces an interesting approach by framing code generation as a black-box optimization problem and proposes the Scattered Forest Search (SFS) method. However, the practical application of SFS could be challenging due to the number of hyperparameters that need to be tuned. The paper should provide more guidance on how to select these hyperparameters, perhaps by including a sensitivity analysis or a discussion of how the optimal values might vary across different tasks or LLMs. For example, the exploration parameter in the UCT formula, the number of seed solutions, and the parameters for branch scatter and branch scout all need to be carefully chosen. Without clear guidelines, it may be difficult for practitioners to effectively use the proposed method. Furthermore, the interaction between these components adds to the complexity, making it hard to isolate the impact of each individual technique. A more detailed analysis of how these components interact and influence the overall performance would be beneficial.

While the paper presents a comprehensive experimental evaluation, it is limited by its reliance on a single LLM, gpt-3.5. The performance of optimization methods can vary significantly across different LLMs due to differences in their architecture, training data, and inherent capabilities. It is crucial to evaluate the proposed method on a wider range of LLMs, including open-source models like Llama or Mistral, to assess its generalizability and robustness. This would also help to understand how the method performs with models that have different strengths and weaknesses. For instance, some models might be better at generating diverse code snippets, while others might be better at refining existing code. The paper should also explore how the hyperparameters of SFS might need to be adjusted for different LLMs. This would provide a more complete picture of the method's applicability and limitations.

Finally, the paper should also consider the computational cost of the proposed method. While the paper claims that SFS scales efficiently, it does not provide a detailed analysis of the computational resources required for different problem sizes and LLMs. A comparison of the computational cost of SFS with other state-of-the-art methods would be valuable. This would help practitioners to make informed decisions about whether to use SFS for their specific applications. Furthermore, the paper should discuss the potential for parallelizing the different components of SFS to reduce the overall runtime. This would be particularly important for large-scale code generation tasks.

### Questions

- How does the performance of SFS vary with different LLMs?
- How does the performance of SFS vary with different tasks?
- How does the performance of SFS vary with different hyperparameters?
- How does the performance of SFS vary with different problem sizes?

### Rating

6

### Confidence

3

**********
