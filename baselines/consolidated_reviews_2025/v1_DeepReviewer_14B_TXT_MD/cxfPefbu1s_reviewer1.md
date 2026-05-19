### Summary

The paper introduces a novel framework for algorithmic fairness that emphasizes procedural fairness by addressing "disguised procedural unfairness" in the data generating process. The authors draw inspiration from John Rawls's concept of "pure procedural justice" to argue that automated decision-making processes should be fair not only in their outcomes but also in their underlying procedures. The key innovation is a method that decouples objectionable components of the data generating process from neutral ones, using reference points and a value instantiation rule to ensure that predictions are based only on neutral components. This approach aims to prevent inadvertent alterations to neutral aspects of the data generating process while ensuring the greatest benefit to the least advantaged individuals. The authors demonstrate their framework through theoretical analysis and empirical experiments on both simulated and real-world datasets, showing its effectiveness in achieving procedural fairness.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The paper introduces an innovative framework for algorithmic fairness by focusing on procedural fairness within the data generating process, drawing inspiration from John Rawls's concept of "pure procedural justice." This approach shifts the focus from outcome-based fairness to ensuring fairness in the underlying procedures, which is a fresh perspective in the field of algorithmic fairness. The concept of "disguised procedural unfairness" highlights a subtle yet significant issue that has been previously overlooked. The framework's method of decoupling objectionable components from neutral ones using reference points and a value instantiation rule is a novel technical contribution. The paper provides a rigorous theoretical foundation for its framework, with clear definitions and formalisms that support its claims. The use of causal graphs and causal inference techniques demonstrates a deep understanding of the underlying processes and adds robustness to the proposed approach. The empirical evaluation is comprehensive, with experiments conducted on both simulated and real-world datasets. The choice of datasets, including the UCI Adult dataset, allows for a practical demonstration of the framework's effectiveness. The experiments are well-designed to illustrate the problem of disguised procedural unfairness and to validate the proposed solution. The results are clearly presented and provide evidence for the framework's ability to improve fairness without compromising neutral components of the data generating process. The paper's focus on maintaining the integrity of neutral components while addressing objectionable ones is a significant contribution. Most existing fairness methods alter the neutral parts of the data generating process along with the problematic parts. This paper introduces a method that avoids this issue, leading to a more precise and fair outcome.

### Weaknesses

#### Some Related Works


#### comment

The paper's reliance on having a correct causal graph is a significant limitation. In many real-world scenarios, the true causal relationships between variables are unknown or difficult to ascertain. The framework's effectiveness is heavily dependent on the accuracy of the specified causal graph. Any errors in the causal structure could lead to incorrect identification of objectionable and neutral components, potentially undermining the fairness goals. Specifically, the method's reliance on a fully specified DAG means that it cannot directly handle situations where causal relationships are uncertain, latent, or involve feedback loops. This limits its applicability in complex, real-world settings where causal structures are often partially known or disputed. The paper does not provide a detailed discussion of the computational complexity of the proposed framework. Implementing causal inference techniques, especially on large-scale datasets with complex causal graphs, can be computationally intensive. The process of decoupling objectionable components and configuring reference points may add additional computational overhead. The lack of a formal analysis of the time and space complexity makes it difficult to assess the scalability of the method for practical applications. It is unclear how the framework would perform with high-dimensional data or very large causal graphs, which are common in many real-world datasets. 
While the paper introduces the concept of "disguised procedural unfairness" and provides a linear example, the intuitive understanding of this concept could be further enhanced. A more detailed and accessible explanation of how procedural unfairness manifests in real-world scenarios would be beneficial. The current example, while illustrative, does not fully capture the nuances of how seemingly neutral processes can inadvertently perpetuate unfairness. The paper could benefit from a more thorough discussion of how to identify and define "objectionable components" in practice. The framework relies on the user to specify which parts of the data generating process are problematic. However, the criteria for making this distinction are not always clear-cut, and different stakeholders may have varying perspectives on what constitutes an objectionable component. The paper does not provide a systematic methodology for this crucial step, which could lead to subjective or inconsistent applications of the framework.

### Suggestions

To enhance the practical applicability of the proposed framework, the authors should address the limitations imposed by the requirement of a fully known causal graph. One approach could be to explore methods for handling uncertainty in causal structures, such as using probabilistic causal models or techniques for causal discovery. This would allow the framework to be applied in scenarios where the true causal relationships are not fully known or are subject to uncertainty. Furthermore, the authors should provide a more detailed analysis of the computational complexity of their method. This should include a formal analysis of the time and space complexity, as well as an empirical evaluation of the framework's performance on large-scale datasets. This would help to assess the scalability of the method and identify potential bottlenecks. The authors could also consider exploring approximations or optimizations to improve the computational efficiency of the framework, especially for high-dimensional data or complex causal graphs. 

To improve the clarity and practical relevance of the concept of "disguised procedural unfairness," the authors should provide more concrete examples and a more detailed explanation of how it manifests in real-world scenarios. This could include case studies or examples from specific domains, such as lending, hiring, or healthcare. These examples should illustrate how seemingly neutral processes can inadvertently perpetuate unfairness and how the proposed framework can address these issues. Additionally, the authors should provide a more systematic methodology for identifying and defining "objectionable components." This could involve developing a set of criteria or guidelines for making this distinction, as well as a process for engaging with stakeholders to understand their perspectives on what constitutes an objectionable component. This would help to ensure that the framework is applied consistently and fairly across different contexts.

Finally, the authors should consider expanding the experimental evaluation to include a wider range of datasets and scenarios. This could include datasets with more complex causal structures, as well as datasets from different domains. This would help to demonstrate the generalizability of the framework and its ability to address diverse fairness challenges. The authors should also compare their framework to a wider range of existing fairness methods, including those that do not rely on causal assumptions. This would provide a more comprehensive evaluation of the framework's strengths and weaknesses and help to position it within the broader landscape of algorithmic fairness research.

### Questions

How does the framework perform when the causal graph is only partially known or estimated from data? 
Can the authors provide a more detailed analysis of the computational complexity of their framework? 
What are the guidelines for practitioners to identify and define "objectionable components" in real-world scenarios? 
How does the framework handle situations where different stakeholders have conflicting views on what constitutes an objectionable component? 
Are there any trade-offs between achieving procedural fairness and other fairness notions, such as statistical fairness? 
How does the proposed framework compare to other causal fairness methods when the causal graph is uncertain or partially known?

### Rating

5

### Confidence

3

**********
