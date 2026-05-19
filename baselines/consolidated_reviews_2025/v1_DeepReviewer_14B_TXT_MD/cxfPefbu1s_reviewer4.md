### Summary

The paper addresses the problem of "disguised procedural unfairness" in algorithmic decision-making, where neutral components of the data-generating process are inadvertently altered while trying to mitigate bias. The authors propose a framework inspired by John Rawls's theory of "pure procedural justice" to decouple objectionable data-generating components from neutral ones. The framework uses reference points and a value instantiation rule to ensure fairness without affecting neutral components. The paper demonstrates the effectiveness of the proposed approach through theoretical analysis and empirical experiments on both simulated and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel perspective on algorithmic fairness by focusing on the data-generating process rather than solely on the prediction model. This approach addresses a critical gap in the literature, as it considers the entire decision-making pipeline rather than just the final outcome.
2. The proposed framework is grounded in a well-established philosophical theory (Rawls's theory of justice), providing a strong theoretical foundation for the approach.
3. The paper provides a clear and detailed explanation of the proposed framework, including the concepts of reference points and the value instantiation rule. The authors also provide a thorough analysis of the framework's properties and limitations.
4. The empirical evaluation is comprehensive, with experiments conducted on both simulated and real-world datasets. The results demonstrate the effectiveness of the proposed approach in achieving procedural fairness while maintaining the integrity of neutral components.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the data-generating process can be accurately represented by a causal graph. In practice, obtaining a complete and accurate causal graph can be challenging, especially in complex real-world scenarios. The method's reliance on a fully specified causal graph, including all relevant confounders and mediators, is a significant limitation. The authors should acknowledge that in many real-world applications, the causal structure is either unknown or only partially known, which could severely limit the applicability of their proposed framework. The paper should also discuss the sensitivity of their method to errors in the causal graph, such as missing edges or incorrect directionality, and how these errors might impact the fairness of the resulting algorithm.
2. The paper could benefit from a more detailed discussion of the computational complexity of the proposed framework. While the authors mention that the framework is scalable, they do not provide a formal analysis of its computational requirements. The paper should include a discussion of the time and space complexity of the algorithm, particularly in relation to the size of the causal graph and the number of data points. Furthermore, it would be beneficial to compare the computational cost of the proposed method with existing fairness techniques, especially when dealing with large-scale datasets and complex causal structures. The authors should also discuss the practical implications of these computational costs, such as the feasibility of applying the method in real-time decision-making scenarios.

### Suggestions

The authors should explicitly address the limitations of their approach when the causal graph is not fully known or is misspecified. They could explore methods for handling uncertainty in the causal structure, such as using techniques from causal discovery or robust causal inference. For example, they could investigate how their framework performs when using a partially observed causal graph or when the graph is learned from data. Furthermore, the authors should discuss the potential impact of errors in the causal graph on the fairness of the resulting algorithm. It would be beneficial to provide a sensitivity analysis that shows how the performance of the method degrades as the causal graph becomes more inaccurate. This would help to understand the robustness of the proposed framework in real-world settings where the causal structure is often uncertain. The authors should also consider incorporating methods for validating the assumed causal graph, such as using statistical tests or expert knowledge.

To address the computational concerns, the authors should provide a more detailed analysis of the time and space complexity of their algorithm. This analysis should consider the impact of the size of the causal graph and the number of data points on the computational cost. It would be helpful to provide a breakdown of the computational cost of each step in the algorithm, such as the identification of objectionable components, the configuration of reference points, and the value instantiation. Furthermore, the authors should compare the computational cost of their method with existing fairness techniques, especially those that do not rely on causal assumptions. This comparison should consider both the theoretical complexity and the practical runtime performance. The authors should also discuss the practical implications of these computational costs, such as the feasibility of applying the method in real-time decision-making scenarios or when dealing with very large datasets. They could also explore potential optimizations to reduce the computational burden of their approach.

Finally, the authors should consider expanding their discussion on the practical implications of their work. While the theoretical framework is well-developed, the paper could benefit from a more detailed discussion of how the proposed approach can be applied in real-world scenarios. This could include a case study or a more detailed example that illustrates the steps involved in applying the framework to a specific problem. The authors should also discuss the challenges of implementing their approach in practice, such as the difficulty of obtaining a complete and accurate causal graph and the computational cost of the algorithm. Furthermore, the authors should discuss the ethical implications of their work, such as the potential for unintended consequences or the need for transparency and accountability in the use of their framework.

### Questions

1. How does the proposed framework handle situations where the data-generating process is unknown or partially known? Are there any methods to address this issue?
2. Can the framework be extended to handle dynamic or evolving data-generating processes? How would the reference points and value instantiation rule be adapted in such scenarios?
3. How does the proposed framework compare to existing approaches in terms of computational complexity and scalability? Are there any specific optimizations that can be applied to improve the efficiency of the framework?
4. What are the potential ethical implications of using reference points to modify the data-generating process? How can these implications be addressed?

### Rating

6

### Confidence

3

**********
