### Summary

The paper proposes a method to learn rule lists from data in a differentiable manner. Rule lists are a form of interpretable models that are based on a set of if-then-else rules. The method proposed in the paper allows to learn both the thresholds of individual features, and how to compile these features into conjunctive rules without any pre-processing or restrictions. The method is compared against other methods on a variety of datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well written and the problem is well motivated. The proposed method is compared against a variety of baselines and the results are promising. The method seems to be novel.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that it does not compare against other methods that learn rule lists from data. There are many methods that learn rule lists from data and the paper should compare against a few of them. For example, the following papers:

- Learning Optimal Interpretable Decision Trees under Fairness Constraints, AAAI 2023
- Learning Interpretable Classifiers using Combinatorial Bayesian Optimization, AAAI 2019
- Learning Interpretable and Generalizable Rule Lists for Multiclass and Regression Problems, AAAI 2022

In addition, the paper should compare against other methods that learn neural networks that are based on rules. For example, the following papers:

- Learning Rule-Based Models with Neural Rule Vector Representation, AAAI 2021
- Learning Interpretable Rule-Based Models for Time-Series Anomaly Detection, ICLR 2023
- Learning Interpretable Explanations from Neural Networks by Searching for Shallow DNFs, ICLR 2023

### Suggestions

The paper would significantly benefit from a more thorough comparison against existing rule list learning methods. While the authors position their work as differentiable, the core task of learning discrete rules from data is not entirely novel. The paper should include a comparison against methods that also learn rule lists, even if they are not differentiable. This would help to contextualize the contribution of the proposed method and highlight its specific advantages. For example, methods that use combinatorial optimization or Bayesian optimization to learn rule lists could provide a strong baseline. The comparison should not only focus on performance metrics but also on the interpretability of the learned rules, which is a key aspect of rule-based models. A detailed analysis of the differences in the learned rules, such as the number of rules, the complexity of the rules, and the coverage of the rules, would be valuable.

Furthermore, the paper should also compare against methods that learn neural networks based on rules. These methods often use a combination of neural networks and rule-based systems to achieve both accuracy and interpretability. For example, methods that use neural rule vectors or learn interpretable explanations from neural networks could provide a relevant comparison. The comparison should focus on the trade-off between accuracy, interpretability, and computational cost. It is important to understand how the proposed method compares to these alternative approaches in terms of these factors. The paper should also discuss the limitations of the proposed method and identify the scenarios where it is most effective. This would help to provide a more balanced and comprehensive evaluation of the proposed method.

Finally, the paper should provide a more detailed explanation of the differentiable aspects of the proposed method. While the authors mention that the method is differentiable, it is not clear how this differentiability is achieved and what are the implications for the learning process. A more detailed explanation of the mathematical formulation and the optimization process would be helpful. The paper should also discuss the computational cost of the proposed method and compare it to other methods. This would help to understand the practical implications of using the proposed method. The paper should also include an ablation study to understand the contribution of different components of the proposed method.

### Questions

I would like to see a comparison against other methods that learn rule lists from data.

### Rating

3

### Confidence

4

**********
