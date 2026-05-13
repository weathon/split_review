# Build Roadmap for Automated Feature Transformation: A Graph-based Reinforcement Learning Approach

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Feature transformation tasks aim to generate high-value features by combining existing ones through mathematical operations, which can improve the performance of downstream machine learning models.
Current methods typically use iterative sequence generation, where exploration is guided by performance feedback from downstream tasks.
However, these approaches fail to effectively utilize historical decision-making experiences and overlook potential relationships between generated features, thus limiting the flexibility of the exploration process.
Additionally, the decision-making process lacks the ability to dynamically backtrack on efficient decisions, which hinders adaptability and reduces overall robustness and stability.
To address these issues, we propose a novel framework that uses a graph to track the feature transformation process, where each node represents a transformation state.
In this framework, three cascading agents sequentially select nodes and mathematical operations to generate new nodes.
This strategy benefits from the graph structure’s ability to store and reuse valuable transformations, and it incorporates backtracking via graph pruning techniques, allowing the framework to correct inefficient paths.
To demonstrate the effectiveness and flexibility of our approach, we conducted extensive experiments and detailed case studies, demonstrating superior performance across a variety of datasets.
This strategy leverages the graph structure's inherent properties, allowing for the preservation and reuse of sight-seen and valuable transformations. 
It also enables back-tracking capabilities through graph pruning techniques, which can rectify inefficient transformation paths.
To validate the efficacy and flexibility of our approach, we conducted comprehensive experiments and detailed case studies, demonstrating superior performance in diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces an automated feature transformation framework designed to enhance downstream machine learning model performance. The TCTO framework leverages a reinforcement learning-based graph structure to maintain a roadmap of feature transformations, enabling efficient exploration and backtracking of transformation pathways. TCTO uses a multi-agent reinforcement learning approach, clustering and encoding transformation states to strategically apply feature transformations. Experiments on multiple datasets demonstrate TCTO's performance over existing methods by improving robustness and flexibility in feature generation.

### Strengths
1. While mostly clear, certain sections (e.g., cascading agent decision process) could benefit from additional details.

2. The framework is well-supported by experimental evidence showing its adaptability across different datasets and improvement in downstream model performance.

3. TCTO introduces a novel approach to automated feature engineering by employing a transformation-centric methodology with a graph-based roadmap, overcoming limitations of existing feature transformation methods.

4. The approach’s ability to backtrack and optimize feature transformations dynamically makes it highly applicable in real-world ML tasks where feature diversity and stability are crucial.

### Weaknesses
1. While mostly clear, certain sections (e.g., cascading agent decision process) could benefit from additional details.

2. The framework is well-supported by experimental evidence showing its adaptability across different datasets and improvement in downstream model performance.

3. TCTO introduces a novel approach to automated feature engineering by employing a transformation-centric methodology with a graph-based roadmap, overcoming limitations of existing feature transformation methods.

4. The approach’s ability to backtrack and optimize feature transformations dynamically makes it highly applicable in real-world ML tasks where feature diversity and stability are crucial.


1. While effective on a range of datasets, it is unclear how well TCTO scales with extremely high-dimensional data or very large datasets, as the pruning strategy may require fine-tuning in these cases.

2. The cascading decision-making process is intricate, and further simplification or additional visuals might aid understanding.

3. The reward structure combines performance and complexity, but further discussion on how these metrics are weighted could improve transparency and replicability of the model’s efficacy.

### Questions
1. Could the authors elaborate on how they determined the weights for performance and complexity in the reward function? More detail on this could clarify the balance between the two objectives.

2。 How does TCTO perform on high-dimensional datasets with over 10,000 features? Is the pruning strategy sufficient to maintain stability without compromising feature diversity?

3. Were there any specific scenarios where TCTO’s backtracking mechanism was particularly beneficial in terms of model performance or feature diversity?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors present TCTO, a graph-based reinforcement learning framework designed for automated feature transformation. The approach addresses limitations in current methods, such as the lack of historical insight utilization and insufficient flexibility in transformation exploration. By constructing a transformation roadmap with nodes representing feature states, TCTO leverages a cascading multi-agent system to dynamically select transformations, reuse effective paths, and prune inefficient ones. The experimental results demonstrate that TCTO outperforms existing methods in generating high-quality features, suggesting its potential to enhance feature engineering in machine learning tasks.

### Strengths
This paper has several notable strengths. Firstly, the authors present a well-motivated framework that addresses clear gaps in current automated feature transformation methods, such as the need for effective historical data utilization and robust backtracking. The proposed TCTO framework is innovative in its use of a graph-based roadmap and cascading multi-agent reinforcement learning, which enhance the flexibility and adaptability of the transformation process. Additionally, the authors provide a comprehensive experimental evaluation across diverse datasets, which convincingly demonstrates TCTO’s superior performance compared to traditional methods. This solid empirical foundation supports the framework's potential for broad applicability in feature engineering for machine learning tasks.

### Weaknesses
While this paper offers a promising framework, it has some weaknesses. Firstly, the explanation of the cascading multi-agent system and its decision-making processes could benefit from more clarity and detail, as the current description may be challenging for readers to fully grasp without additional context. Specifically, the interaction between the agents, the reward structure guiding their actions, and the precise mechanism by which they explore the transformation space are not sufficiently elaborated. Additionally, the computational complexity of TCTO is not thoroughly analyzed, especially regarding scalability to larger datasets, which may impact its practical applicability. The paper lacks a rigorous analysis of how the graph structure and the cascading agent approach affect runtime and memory usage as the number of features and data points increases. Finally, while the experimental results are extensive, the paper could further strengthen its claims by providing more insight into specific scenarios or datasets where TCTO may struggle, thereby clarifying the framework’s limitations and potential areas for improvement. For example, it would be beneficial to understand how TCTO performs on datasets with varying degrees of feature correlation or different underlying data distributions.

### Questions
1.How does the computational complexity of TCTO scale with larger datasets, and are there any strategies to mitigate potential performance bottlenecks?
2.Are there scenarios or specific types of datasets where TCTO’s performance may be limited, and if so, what adjustments might be necessary to enhance its adaptability?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper deals with the automated generation of features. The generation process consists of several steps, which are represented as a graph. The graphs are to be optimized using multi-agent reinforcement learning.

### Strengths
* It can be seen (among other things from the large number of specific illustrations) that a lot of effort was put into preparing the paper

### Weaknesses
 * I find the text very badly written. Examples follow. The novelty and benefits of the method are hard for me to understand.
* It seems to me that there is too much material for a conference paper, the number of pages is simply not enough to present it in a convincing way.

Details, examples and further comments:
* I don't think “roadmap” is a suitable term, “schedule” or "sequence" would probably be better.
* The title sounds strange. Wouldn't "Optimization of transformation sequences for automated feature generation“ be better?
* The abstract uses terms that are incomprehensible:
mathematical feature-feature crossing
the roadmap of feature transformation
* „Feature transformation task aims to generate high-value features and improve the performance of downstream machine learning tasks using the mathematical feature-feature crossing” needs to be reformulated.
* "Classic machine learning is highly dependent on the structure of the model, the activation function" cannot be said in this way, it seems to refer exclusively to neural networks and not to classical machine learning in general.
* A reference should be given for "a cascading multi-agent reinforcement learning (MARL) algorithm", because it is not generally known what “cascading multi-agent reinforcement learning” is.
* “we present an innovative framework” -> “we present a novel framework”
* In the loss function, Equation 8, the square is probably missing. 
* "In this study, we introduce TCTO, an automated feature transformation framework. Our method emphasizes a transformation-centric approach, in which a transformation roadmap is utilized to systematically track and manage feature modifications." should be reworded. What is the information content? What should be expressed?
* I think that the Abstract and Conclusion need to be completely rewritten.

### Questions
* How were the small uncertainties in Table 1 achieved? How often were the experiments repeated?

### Soundness
2

### Presentation
2

### Contribution
3
