### Summary

This paper proposes a formalization of the notion of generalizability in ML. The authors propose a framework to quantify generalizability, which is a concept that is often used but not well-defined. The authors propose a formal definition of generalizability as the probability that any two empirical studies approximating the same ideal study yield similar results. They then propose a method to estimate the size of an empirical study based on a desired generalizability threshold. The authors apply their framework to two case studies: a benchmark of categorical encoders and a benchmark of large language models (LLMs). They demonstrate how the proposed approach can be used to assess the generalizability of experimental studies and determine the minimum number of experiments needed to achieve generalizable results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper formalizes the concept of generalizability in ML, which is often used but not well-defined. This is an important contribution that can help researchers better understand and communicate the generalizability of their results.
- The paper provides a practical method for estimating the size of an empirical study based on a desired generalizability threshold. This can be useful for researchers who want to design more efficient and effective experiments.
- The paper applies the proposed framework to two case studies: a benchmark of categorical encoders and a benchmark of large language models (LLMs). This demonstrates the applicability of the framework to different types of machine learning problems.

### Weaknesses

#### Some Related Works


#### comment

 - The paper assumes that the experimental conditions are independent and identically distributed (i.i.d.). However, in many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper does not discuss the limitations of this assumption or how it may affect the results.
- The paper does not provide a clear definition of what constitutes an "experiment" in the context of machine learning. While the authors define an experiment as a mapping from a set of conditions to a ranking of alternatives, they do not provide a concrete example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network? The lack of clarity on this point makes it difficult to understand how the proposed framework can be applied in practice.
- The paper's approach to measuring generalizability relies on the assumption that the experimental conditions are independent and identically distributed (i.i.d.). However, in many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper does not discuss the limitations of this assumption or how it may affect the results.
- The paper does not provide a clear definition of what constitutes an "experiment" in the context of machine learning. While the authors define an experiment as a mapping from a set of conditions to a ranking of alternatives, they do not provide a concrete example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network? The lack of clarity on this point makes it difficult to understand how the proposed framework can be applied in practice.

### Suggestions

The paper would benefit from a more thorough discussion of the i.i.d. assumption and its potential limitations. The authors should acknowledge that the assumption of independent and identically distributed experimental conditions may not hold in many real-world scenarios. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper should also discuss how the proposed framework can be adapted to handle non-i.i.d. experimental conditions. One possible approach would be to explore the use of techniques from causal inference to account for potential dependencies between experimental conditions. Another approach would be to consider the experimental conditions as a sequence, rather than a set, and to use time-series analysis techniques to model the dependencies between conditions. Furthermore, the authors should provide a more concrete definition of what constitutes an "experiment" in the context of machine learning. While the authors define an experiment as a mapping from a set of conditions to a ranking of alternatives, they do not provide a clear example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network? Providing a concrete example would make it easier for readers to understand how the proposed framework can be applied in practice. The authors could also consider providing a more detailed discussion of how the proposed framework can be used to design experiments that are more likely to be generalizable.

To improve the practical applicability of the proposed framework, the authors should consider providing more guidance on how to choose the desired generalizability threshold. The paper mentions that the threshold should be chosen based on the specific goals of the study, but it does not provide any concrete examples or guidelines on how to make this choice. For instance, in the case of a benchmark of categorical encoders, what would be a reasonable generalizability threshold? How would one determine if the results of a benchmark are sufficiently generalizable for practical use? The authors could consider providing a sensitivity analysis to show how the estimated size of an empirical study changes as the generalizability threshold is varied. This would help readers understand the trade-offs between generalizability and the size of the empirical study. Furthermore, the authors should discuss the computational cost of estimating the size of an empirical study based on the proposed framework. The paper mentions that the estimation process involves sampling from the results of the experiments, but it does not provide any details on the computational complexity of this process. It would be helpful to know how the computational cost scales with the number of experimental conditions and the size of the ranking space. This information would be useful for researchers who want to apply the proposed framework to large-scale studies.

Finally, the paper should address the issue of missing values in the experimental results. The authors mention that they impute missing values by assigning the worst rank, but they do not provide any justification for this approach. It would be helpful to know if there are other ways to handle missing values, and if so, how these methods compare to the imputation approach used in the paper. For example, one could consider using multiple imputation techniques, which involve generating multiple plausible values for the missing data and then combining the results of the analyses performed on each imputed dataset. This approach can provide a more robust estimate of the uncertainty in the results. The authors should also discuss the potential impact of missing values on the estimated generalizability of the experimental study. If a large number of values are missing, it is possible that the estimated generalizability is not accurate. The authors should provide some guidance on how to assess the impact of missing values on the results.

### Questions

- How does the proposed framework handle the case where the experimental conditions are not independent and identically distributed (i.i.d.)? In many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. How does the framework account for potential dependencies between experimental conditions?
- Can the authors provide a concrete example of what constitutes an "experiment" in the context of machine learning? The paper defines an experiment as a mapping from a set of conditions to a ranking of alternatives, but it does not provide a clear example of how this definition applies to a specific machine learning task. For instance, in the case of training a neural network, what would be considered an "experiment"? Is it the choice of hyperparameters, the initialization of the weights, or the specific architecture of the network?
- How should the desired generalizability threshold be chosen in practice? The paper mentions that the threshold should be chosen based on the specific goals of the study, but it does not provide any concrete examples or guidelines on how to make this choice. For instance, in the case of a benchmark of categorical encoders, what would be a reasonable generalizability threshold? How would one determine if the results of a benchmark are sufficiently generalizable for practical use?
- How does the proposed framework handle missing values in the experimental results? The paper mentions that they impute missing values by assigning the worst rank, but they do not provide any justification for this approach. Are there other ways to handle missing values, and if so, how do they compare to the imputation approach used in the paper?
- What is the computational cost of estimating the size of an empirical study based on the proposed framework? The paper mentions that the estimation process involves sampling from the results of the experiments, but it does not provide any details on the computational complexity of this process. How does the computational cost scale with the number of experimental conditions and the size of the ranking space?

### Rating

6

### Confidence

3

**********
