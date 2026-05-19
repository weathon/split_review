### Summary

This paper introduces a framework to address procedural fairness in algorithmic decision-making by focusing on the data generating process. The authors propose decoupling objectionable components from neutral ones in the data generation process to prevent disguised procedural unfairness. Inspired by John Rawls's concept of pure procedural justice, the framework uses reference points and a value instantiation rule to ensure fairness requirements are met during data generation, benefiting the least advantaged individuals. The paper includes experiments on simulated and real-world data to demonstrate the effectiveness of this approach.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

1. The paper introduces a novel perspective on procedural fairness by focusing on the data generating process, which is often overlooked in algorithmic fairness literature. The integration of Rawls's theory of justice provides a strong theoretical foundation for the proposed framework.

2. The paper is well-structured and clearly written. The authors provide a thorough explanation of the problem, the proposed solution, and the theoretical underpinnings. The use of diagrams and examples enhances the clarity of the presentation.

3. The proposed framework has significant implications for the design of fair algorithmic systems. By ensuring that the data generating process itself adheres to fairness principles, the framework can lead to more equitable outcomes in various applications, including hiring, lending, and criminal justice.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the practical challenges in implementing the proposed framework, such as identifying and classifying components of the data generating process as either objectionable or neutral. The authors should elaborate on the specific criteria or methods that could be used to make this distinction in real-world scenarios, where the data generation process is often complex and opaque. For instance, in a hiring scenario, how does one definitively separate attributes like 'years of experience' (potentially neutral) from 'educational background' (potentially objectionable due to socioeconomic factors) when both can influence the outcome?

2. The paper primarily focuses on the theoretical aspects of the framework. More empirical evidence demonstrating the effectiveness of the approach in diverse real-world settings would strengthen the paper's contributions. The current experiments, while illustrative, do not fully capture the complexities of real-world data and decision-making processes. The authors should consider expanding their empirical analysis to include more complex datasets and scenarios, such as those involving high-dimensional data or non-linear relationships.

3. The paper could explore the sensitivity of the framework to different configurations of reference points and the value instantiation rule. A more thorough analysis of how these choices impact the fairness and accuracy of the outcomes would provide valuable insights. For example, how does the selection of different reference points for a given protected attribute affect the final decision-making process? What are the trade-offs between different value instantiation rules in terms of fairness and utility?

### Suggestions

To address the challenge of identifying objectionable and neutral components, the authors should consider incorporating a more structured approach, perhaps drawing from existing feature selection or causal inference techniques. For example, they could explore methods for quantifying the degree of association between features and protected attributes, or use causal discovery algorithms to identify potential pathways of discrimination. This would provide a more principled way to determine which components of the data generating process should be considered objectionable. Furthermore, the authors could investigate the use of domain expertise and stakeholder input to guide the classification process, ensuring that the framework is both technically sound and socially relevant. This could involve developing a systematic protocol for eliciting and incorporating expert knowledge about the data generating process and its potential biases.

To strengthen the empirical validation of the framework, the authors should conduct experiments on more diverse and complex datasets. This could include datasets with high-dimensional features, non-linear relationships, and multiple interacting protected attributes. The authors should also consider evaluating the framework's performance in different application domains, such as healthcare or finance, to demonstrate its generalizability. In addition, the authors should compare the performance of their framework against existing fairness-aware algorithms, using a range of fairness metrics and performance measures. This would provide a more comprehensive assessment of the framework's strengths and weaknesses. Furthermore, the authors should explore the impact of different data preprocessing techniques on the framework's performance, such as feature scaling or imputation methods.

Finally, to address the sensitivity of the framework to reference point configurations and value instantiation rules, the authors should conduct a more thorough analysis of these parameters. This could involve systematically varying the reference points and instantiation rules and evaluating their impact on fairness and accuracy metrics. The authors should also explore the use of adaptive or data-driven methods for selecting these parameters, rather than relying on arbitrary choices. For example, they could investigate the use of optimization algorithms to find the optimal configuration of reference points and instantiation rules that maximize fairness while minimizing the loss of predictive accuracy. This would make the framework more robust and practical for real-world applications.

### Questions

1. How does the framework handle situations where the data generating process is unknown or partially known?

2. Can the framework be extended to handle dynamic or evolving data generating processes?

3. How does the proposed framework compare to existing approaches in terms of computational complexity and scalability?

4. What are the potential ethical implications of using reference points to modify the data generating process?

### Rating

6

### Confidence

4

**********
