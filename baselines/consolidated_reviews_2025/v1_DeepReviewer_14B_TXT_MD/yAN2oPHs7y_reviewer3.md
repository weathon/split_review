### Summary

The authors propose a new method for learning rule lists. The proposed method is a differentiable relaxation of the rule list learning problem. The method is end-to-end and unifies the learning of predicates, their assembly into rules, and the final order of the rule list into a single architecture. The method does not require pre-discretization of continuous features. The authors evaluate the proposed method on several datasets and compare it with other methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well written and easy to follow. The proposed method is novel and interesting. The authors provide a thorough evaluation of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

The proposed method is limited to the rule list model, which may lack expressiveness and could be less effective on complex tasks. The method currently only supports binary classification, limiting its applicability to a subset of machine learning tasks.

### Suggestions

The primary limitation of the proposed method lies in its reliance on a rule list model, which inherently restricts its expressiveness. While rule lists offer interpretability, they may struggle to capture complex relationships present in many real-world datasets. For instance, consider a scenario where the target variable is influenced by a combination of features that interact in a non-linear or non-conjunctive manner. A rule list, by its sequential and conjunctive nature, might require an exponential number of rules to approximate such relationships, leading to reduced performance and interpretability. Exploring alternative, more expressive models that can still maintain a degree of interpretability, such as decision sets or fuzzy rule-based systems, could be a valuable direction for future research. These models might offer a better trade-off between accuracy and interpretability for complex tasks.

Furthermore, the current restriction to binary classification significantly limits the applicability of the proposed method. Many real-world problems involve multi-class classification, and extending the method to handle such scenarios is crucial for broader adoption. A naive approach, such as one-vs-rest, might not be optimal, as it could lead to a large number of rules and potentially reduce interpretability. A more sophisticated approach would involve learning a set of rules that can directly handle multiple classes, possibly by introducing a hierarchical structure or by using a different rule language that can express multi-class relationships more efficiently. The authors should consider exploring such extensions to make the method more versatile and applicable to a wider range of problems. This would involve careful consideration of how to define the rule antecedents and consequents for multi-class scenarios.

Finally, the paper would benefit from a more detailed analysis of the computational complexity of the proposed method. While the authors mention that the method is end-to-end, they do not provide a clear understanding of how the computational cost scales with the number of features, rules, and data points. This is important for assessing the practicality of the method, especially for large datasets. A theoretical analysis of the time and space complexity, along with empirical evaluations on datasets of varying sizes, would provide valuable insights into the scalability of the method. Additionally, a comparison of the computational cost with other rule-based learning methods would help to position the proposed method in terms of its efficiency.

### Questions

How does the proposed method handle continuous features? Is it through binning? If so, how many bins are typically used?
What is the computational complexity of the proposed method? How does it scale with the number of features and the length of the rule list? It would be helpful to compare the training time with other baselines.
In the experiments, how is the rule list length chosen? What criteria should be used to determine the optimal length of the rule list?
How can the proposed method be extended to handle missing values in the dataset?

### Rating

6

### Confidence

3

**********
