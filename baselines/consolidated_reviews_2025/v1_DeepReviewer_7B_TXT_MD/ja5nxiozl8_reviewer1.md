### Summary

This paper formalizes the concept of experimental studies and their results by introducing a mathematical framework that quantifies generalizability. The authors propose using the Maximum Mean Discrepancy (MMD) to measure the similarity between the results of different experimental conditions, and then define generalizability based on the probability that any two empirical studies approximating the same ideal study yield similar results. The paper also presents an algorithm to estimate the number of experiments required to achieve a desired level of generalizability. The framework is then applied to two case studies: a benchmark of categorical encoders and a benchmark of large language models (LLMs), demonstrating how the proposed approach can be used to assess the generalizability of experimental studies and determine the minimum number of experiments needed to achieve generalizable results.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper provides a novel mathematical framework for quantifying the generalizability of experimental studies, which is a significant contribution to the field of machine learning. The authors define generalizability in a formal way, using the concept of probability and Maximum Mean Discrepancy (MMD) to measure the similarity between the results of different experimental conditions. This formalization allows for a more rigorous and quantifiable assessment of generalizability compared to existing approaches. The paper also presents an algorithm to estimate the number of experiments required to achieve a desired level of generalizability, which is a practical contribution that can be used by researchers to design more efficient and effective experiments. The authors apply their framework to two case studies: a benchmark of categorical encoders and a benchmark of large language models (LLMs), demonstrating the applicability of their approach to different types of machine learning problems.

### Weaknesses

#### Some Related Works


#### comment

The paper's approach to measuring generalizability relies on the assumption that the experimental conditions are independent and identically distributed (i.i.d.). However, in many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper does not discuss the limitations of this assumption or how it may affect the results. Additionally, the paper does not provide a clear definition of what constitutes an "experiment" in the context of machine learning. While the authors define an experiment as a mapping from a set of conditions to a ranking of alternatives, they do not provide a concrete example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network? The lack of clarity on this point makes it difficult to understand how the proposed framework can be applied in practice.

### Suggestions

The paper would benefit from a more thorough discussion of the i.i.d. assumption and its potential limitations. The authors should acknowledge that the assumption of independent and identically distributed experimental conditions may not hold in many real-world scenarios. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper should also discuss how the proposed framework can be adapted to handle non-i.i.d. experimental conditions. One possible approach would be to explore the use of techniques from causal inference to account for potential dependencies between experimental conditions. Another approach would be to consider the experimental conditions as a sequence, rather than a set, and to use time-series analysis techniques to model the dependencies between conditions. Furthermore, the authors should provide a more concrete definition of what constitutes an "experiment" in the context of machine learning. While the authors define an experiment as a mapping from a set of conditions to a ranking of alternatives, they do not provide a clear example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network? Providing a concrete example would make it easier for readers to understand how the proposed framework can be applied in practice. The authors could also consider providing a more detailed discussion of how the proposed framework can be used to design experiments that are more likely to be generalizable.

### Questions

1. How does the proposed framework handle the case where the experimental conditions are not independent and identically distributed (i.i.d.)? In many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. How does the framework account for potential dependencies between experimental conditions?
2. Can the authors provide a concrete example of what constitutes an "experiment" in the context of machine learning? The paper defines an experiment as a mapping from a set of conditions to a ranking of alternatives, but it does not provide a clear example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network?
3. The paper assumes that the experimental conditions are independent and identically distributed (i.i.d.). However, in many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. How does the proposed framework account for potential dependencies between experimental conditions?
4. The paper defines generalizability as the probability that any two empirical studies approximating the same ideal study yield similar results. However, it is not clear how this definition relates to the goal of machine learning, which is to find a model that generalizes well to unseen data. How does the proposed framework connect the concept of generalizability to the goal of machine learning?

### Rating

5

### Confidence

3

**********
