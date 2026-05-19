### Summary

This paper studies the problem of algorithmic fairness from the perspective of the data generating process. The authors propose a framework that decouples the objectionable data generating components from the neutral ones by utilizing reference points and the associated value instantiation rule. The framework is motivated by John Rawls's advocacy for pure procedural justice.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper proposes a novel framework for algorithmic fairness from the perspective of the data generating process. The framework is motivated by John Rawls's advocacy for pure procedural justice.
3. The paper provides a comprehensive evaluation of the proposed framework on both simulated and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed framework relies on the assumption that the data generating process is known and can be accurately modeled. However, in practice, this may not always be the case, especially for complex systems with multiple interacting factors. The framework's reliance on a fully specified causal graph limits its applicability in scenarios where the underlying causal relationships are uncertain or only partially known. This is a significant limitation, as many real-world systems involve complex interactions and feedback loops that are difficult to capture in a static causal model. The paper should discuss the sensitivity of the proposed method to errors in the assumed causal structure.
2. The paper could benefit from a more detailed discussion of the practical implications of the proposed framework. For example, how can the framework be used to guide the design of fair algorithms in real-world applications? The paper lacks concrete examples of how the framework can be applied in practice, particularly in scenarios where the data generating process is complex and the causal relationships are not fully understood. The authors should provide more guidance on how to identify and address potential sources of unfairness in real-world datasets using their framework. It would be beneficial to include a case study demonstrating the application of the framework to a real-world problem, highlighting both the benefits and challenges of its implementation.

### Suggestions

The authors should consider exploring methods for handling uncertainty in the causal graph, such as using techniques from causal discovery or robust causal inference. This would enhance the practical applicability of the framework in scenarios where the data generating process is not fully known. Specifically, the authors could investigate how the framework performs when the causal graph is misspecified or when there are unobserved confounders. It would be valuable to analyze the sensitivity of the proposed method to different causal structures and to provide guidelines on how to mitigate the impact of errors in the assumed causal graph. Furthermore, the authors could explore the use of sensitivity analysis to assess the robustness of the framework to variations in the causal assumptions.

To improve the practical relevance of the framework, the authors should provide more concrete examples of how it can be applied in real-world scenarios. This could include a detailed case study demonstrating the application of the framework to a specific problem, such as loan approval or hiring decisions. The case study should highlight the steps involved in identifying objectionable components, configuring reference points, and evaluating the fairness of the resulting algorithm. The authors should also discuss the challenges of applying the framework in practice, such as the difficulty of obtaining accurate causal information and the computational cost of decoupling objectionable components. It would be beneficial to provide practical guidelines for practitioners on how to use the framework to design fair algorithms in real-world applications.

Finally, the authors should discuss the limitations of their approach in more detail, including the assumptions made about the data generating process and the potential for unintended consequences. For example, the authors should consider the possibility that decoupling objectionable components may lead to other forms of unfairness or that the framework may not be effective in all contexts. A more thorough discussion of the limitations would help to clarify the scope of the framework and to identify areas for future research. It would also be beneficial to compare the proposed framework with existing approaches to algorithmic fairness and to highlight its unique contributions and limitations.

### Questions

1. How does the proposed framework handle situations where the data generating process is unknown or partially known?
2. Can the framework be extended to handle dynamic or evolving data generating processes?
3. How does the proposed framework compare to existing approaches in terms of computational complexity and scalability?

### Rating

6

### Confidence

4

**********
