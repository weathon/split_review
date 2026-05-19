### Summary

This paper presents a new conformal prediction framework for structured prediction tasks. The authors propose a general method for constructing prediction sets in structured output spaces, such as directed acyclic graphs (DAGs), which can represent complex relationships between labels. The framework provides coverage guarantees and is evaluated in three domains: integer prediction, hierarchical image classification, and interval-based question answering.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an interesting and important problem in uncertainty quantification for structured prediction tasks. 
- The proposed framework is general and could potentially be applied to a wide range of structured prediction problems. 
- The authors provide theoretical coverage guarantees for their method.

### Weaknesses

#### Some Related Works

[1] PAC-Bayes Conformal Prediction with Hierarchical Label Structures
[2] Conformal Prediction with Conditional Guarantees

#### comment

 - The paper lacks a comparison with existing methods for uncertainty quantification in structured prediction. For example, how does the proposed framework compare to methods like the one proposed by Ghosh et al. (2024) [1]?
- The authors do not discuss the computational complexity of solving the integer program in Equation (4). For larger DAGs, this could be computationally expensive. The paper lacks a detailed analysis of the computational cost associated with solving the integer program, especially as the size of the DAG increases. This is a critical aspect that needs to be addressed for practical applications.
- The paper does not discuss any heuristics or approximations that could be used to scale the method to larger DAGs. The absence of a discussion on scaling strategies limits the applicability of the proposed method to real-world scenarios involving large structured output spaces. The authors should explore and discuss potential heuristics or approximation techniques to make the method more practical.
- The authors do not discuss the sensitivity of the method to the choice of the scoring function g(x, y). The performance of the method could be highly dependent on the choice of the scoring function, and this aspect needs to be investigated. The paper should include an analysis of how different scoring functions affect the performance of the proposed framework.
- The paper does not discuss the potential for extending the framework to other types of structured prediction problems, such as natural language generation or code generation. The scope of the paper is limited to the three evaluated domains. The authors should discuss the potential and challenges of extending the framework to other structured prediction tasks, such as natural language generation or code generation, to demonstrate the generality of the approach.
- The paper does not discuss the potential for extending the framework to other types of structured output spaces, such as hypergraphs or other complex structures. The current framework is limited to DAGs. The authors should explore the possibility of extending the framework to other structured output spaces, such as hypergraphs, to broaden its applicability.

### Suggestions

The paper would benefit from a more thorough comparison with existing uncertainty quantification methods in structured prediction. Specifically, the authors should compare their approach with methods that provide coverage guarantees, such as the one proposed by Ghosh et al. [1]. This comparison should include an analysis of the strengths and weaknesses of each method, as well as a discussion of the scenarios where each method performs best. Furthermore, the authors should consider comparing their method with other relevant approaches in the literature, such as the method proposed by Mohri et al. [2], to provide a more comprehensive evaluation of their framework. This would help to better position the proposed method within the existing landscape of conformal prediction techniques.

To address the computational concerns, the authors should provide a detailed analysis of the computational complexity of solving the integer program in Equation (4). This analysis should include a discussion of how the runtime scales with the size of the DAG and the number of nodes. Additionally, the authors should explore and discuss potential heuristics or approximation techniques that could be used to scale the method to larger DAGs. For example, they could consider using greedy algorithms or other optimization techniques to find approximate solutions to the integer program. The paper should also include an empirical evaluation of these heuristics to demonstrate their effectiveness and limitations. This would make the method more practical for real-world applications involving large structured output spaces.

Finally, the authors should investigate the sensitivity of the method to the choice of the scoring function g(x, y). This analysis should include an evaluation of how different scoring functions affect the coverage and efficiency of the prediction sets. The authors should also discuss the potential for extending the framework to other types of structured prediction problems and structured output spaces. This would demonstrate the generality and versatility of the proposed approach. For example, they could explore the challenges and potential solutions for applying their method to natural language generation or code generation tasks, as well as to more complex structured output spaces such as hypergraphs. This would significantly enhance the impact and applicability of the paper.

### Questions

- How does the proposed framework compare to existing methods for uncertainty quantification in structured prediction, such as the one proposed by Ghosh et al. (2024) [1]?
- What is the computational complexity of solving the integer program in Equation (4), and how does it scale with the size of the DAG?
- Are there any heuristics or approximations that could be used to scale the method to larger DAGs?
- How sensitive is the method to the choice of the scoring function g(x, y)?
- Can the framework be extended to other types of structured prediction problems, such as natural language generation or code generation?
- Can the framework be extended to other types of structured output spaces, such as hypergraphs or other complex structures?

### Rating

5

### Confidence

4

**********
