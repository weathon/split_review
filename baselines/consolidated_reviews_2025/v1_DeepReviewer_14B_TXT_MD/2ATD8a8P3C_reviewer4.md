### Summary

This paper proposes a framework for conformal prediction in structured prediction settings, where the output space is complex and requires more interpretable prediction sets. The authors address the challenge of providing coverage guarantees in such settings by adapting existing conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels. They demonstrate how their approach can be applied in domains where the prediction sets can be represented as a set of nodes in a directed acyclic graph (DAG), such as hierarchical labels in image classification. The paper provides theoretical guarantees for both marginal and PAC coverage and evaluates the approach empirically on three tasks: predicting integers represented by a list of MNIST digits, hierarchical image classification using ImageNet, and question answering on the SQuAD dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel framework for conformal prediction in structured prediction settings, which is a generalization of existing conformal prediction methods to more complex output spaces. The authors provide a theoretical foundation for their approach, including marginal and PAC coverage guarantees.

2. The paper is well-organized, with a clear problem formulation, detailed description of the proposed algorithms, and thorough experimental evaluation. The authors provide clear definitions and notations, making the paper easy to follow.

3. The proposed framework has the potential to significantly improve the interpretability and reliability of predictions in structured prediction settings. By providing coverage guarantees, the approach can help users understand the uncertainty associated with the predictions and make more informed decisions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison with existing methods for structured prediction, which makes it difficult to assess the advantages and disadvantages of the proposed framework. Specifically, the paper lacks a comparison with methods that also aim to provide uncertainty quantification in structured prediction, such as those based on Bayesian approaches or ensemble methods. A more thorough comparison should include metrics beyond coverage, such as the size of the prediction sets and computational cost, to fully understand the trade-offs.

2. The experimental evaluation is limited to three tasks, which may not be sufficient to demonstrate the generalizability of the proposed framework to other structured prediction settings. The chosen tasks, while diverse, do not fully explore the range of challenges present in structured prediction. For example, tasks involving sequential data or more complex hierarchical structures could reveal limitations of the proposed approach. The paper should include experiments on a wider variety of datasets and tasks to better assess its robustness.

3. The paper does not discuss the computational complexity of the proposed algorithms, which could be a concern in practice, especially for large-scale structured prediction problems. The integer programming approach, while effective, may not scale well to very large DAGs or complex structured output spaces. A detailed analysis of the time and space complexity, along with empirical evaluations of runtime on different problem sizes, is needed to understand the practical limitations of the proposed framework.

### Suggestions

To address the lack of comparative analysis, the authors should include a more comprehensive comparison with existing structured prediction methods that provide uncertainty quantification. This should include methods that use Bayesian approaches, ensemble methods, or other conformal prediction techniques tailored for structured outputs. The comparison should not only focus on coverage but also on other relevant metrics such as the average size of the prediction sets, computational cost, and calibration error. For example, the authors could compare their method against a Bayesian approach that provides posterior distributions over the structured outputs, or an ensemble method that aggregates predictions from multiple models. This would provide a more complete picture of the strengths and weaknesses of the proposed framework.

To improve the generalizability of the proposed framework, the authors should expand their experimental evaluation to include a wider variety of structured prediction tasks. This should include tasks with different types of structured output spaces, such as sequential data, more complex hierarchical structures, or tasks with a larger number of possible outputs. For example, the authors could evaluate their method on tasks such as natural language generation, protein structure prediction, or graph-based prediction problems. This would help to demonstrate the robustness and versatility of the proposed framework. Furthermore, the authors should analyze the performance of their method under different levels of data scarcity and noise, as these factors can significantly impact the quality of the prediction sets.

Finally, the authors should provide a detailed analysis of the computational complexity of their proposed algorithms. This should include both theoretical analysis of the time and space complexity, as well as empirical evaluations of the runtime on different problem sizes. The authors should also discuss potential strategies for improving the scalability of their approach, such as using approximate integer programming techniques or parallelization. This would help to make the proposed framework more practical for large-scale structured prediction problems. The authors should also provide guidelines on how to choose the parameters of their algorithm, such as the size of the DAG, to balance the trade-off between accuracy and computational cost.

### Questions

1. How does the proposed framework compare to existing methods for structured prediction in terms of performance and computational cost?

2. Can the proposed framework be applied to other structured prediction settings beyond the three tasks considered in the paper? What are the limitations of the proposed approach?

3. What is the computational complexity of the proposed algorithms, and how can it be improved for large-scale structured prediction problems?

### Rating

6

### Confidence

3

**********
