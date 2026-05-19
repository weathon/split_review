### Summary

The paper proposes a method for learning rule lists in an end-to-end differentiable manner. The method learns the discretization of continuous features, the combination of features into conjunctive rules, and the order of the rules in a single differentiable framework. The method uses soft approximations of threshold functions and a novel differentiable logical conjunction to alleviate vanishing gradients. The method also learns a rule priority that is grounded into a strict ordering at the end of training. The paper evaluates the method on several real-world datasets and compares it with other methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper proposes a novel and interesting method for learning rule lists in an end-to-end differentiable manner. The method addresses the limitations of existing methods and offers several advantages, such as not requiring pre-discretization of continuous features, learning the discretization of features and the combination of features into conjunctive rules without any pre-processing or restrictions, and learning the rule order differentiably. The paper evaluates the method on several real-world datasets and compares it with other methods, showing that the method achieves superior performance in terms of F1 score. The paper also provides a detailed analysis of the results and discusses the limitations of the method.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide any theoretical analysis of the proposed method, such as convergence guarantees, complexity bounds, or generalization properties. This limits the understanding of the method's behavior and performance and makes it difficult to compare it with other methods theoretically. The paper also does not address the issue of missing values in the data, which is a common problem in real-world applications. The paper should discuss how the method handles missing values or propose some strategies to deal with them. The paper also does not provide any user study or case study to demonstrate the interpretability and usefulness of the learned rule lists for human users. The paper should provide some examples of how the rule lists can be used to support decision making or explain phenomena in different domains and how users perceive them.

### Suggestions

The lack of theoretical analysis is a significant weakness. While empirical results are strong, a theoretical foundation would greatly enhance the paper's impact and credibility. Specifically, the paper should explore the convergence properties of the proposed optimization algorithm. It would be beneficial to analyze whether the temperature annealing schedule guarantees convergence to a stable rule list, and if so, under what conditions. Furthermore, a complexity analysis of the proposed method, in terms of the number of features, rules, and data points, would be valuable. This would help to understand the scalability of the method and compare it with other approaches. Finally, some theoretical guarantees on the generalization performance of the learned rule lists would be highly desirable, perhaps by relating the complexity of the rule list to its generalization error. Such analysis would provide a more complete understanding of the method's behavior and limitations.

Regarding missing values, the paper should explicitly address how the proposed method handles them. Simply ignoring missing values or treating them as a separate category might not be optimal in many scenarios. The authors could explore imputation techniques or modify the model to directly handle missing values. For example, the soft binning function could be adapted to output a probability distribution over the bins, rather than a single bin, when the input value is missing. This would allow the model to learn which bins are more likely given the missing value. Alternatively, the model could learn separate rules for missing and non-missing values. The paper should also discuss the impact of missing values on the performance and interpretability of the learned rule lists. A thorough analysis of different missing value handling strategies would significantly improve the practical applicability of the method.

Finally, the paper needs to provide more evidence for the interpretability and usefulness of the learned rule lists. While the paper claims that rule lists are interpretable, it does not provide any empirical evidence to support this claim. The authors should conduct user studies to evaluate how easily humans can understand and use the learned rule lists. For example, they could ask users to predict the outcome for a given instance based on the rule list, or to explain the reasoning behind a prediction. The paper could also include case studies in specific domains, where the learned rule lists are used to support decision making or explain phenomena. These case studies should include qualitative analysis of the learned rules and their impact on the decision making process. This would provide a more compelling argument for the interpretability and usefulness of the proposed method.

### Questions

How does the proposed method ensure the stability and robustness of the learned rule lists, especially when dealing with noisy or high-dimensional data? How sensitive is the method to the choice of hyperparameters, such as the temperature parameters and the regularization strength?
How does the proposed method compare with other interpretable machine learning models, such as decision trees, random forests, or explainable boosting machines, in terms of accuracy, interpretability, and computational cost?
How can the proposed method be extended to handle more complex rule structures, such as rule sets, decision trees, or decision graphs, that can capture more diverse and non-sequential patterns in the data?

### Rating

6

### Confidence

4

**********
