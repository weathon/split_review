### Summary

The paper proposes a formalization of experimental studies in machine learning, aiming to quantify the generalizability of such studies. The authors define an experimental study as a set of experiments comparing alternatives under different conditions, with a focus on allowed-to-vary factors that determine the scope of generalizability. They introduce the concept of an ideal study, which represents an exhaustive exploration of all possible experimental conditions, and contrast it with empirical studies, which are limited samples of the ideal. The paper proposes a quantifiable definition of generalizability based on the similarity of results from different empirical studies approximating the same ideal study. This generalizability is measured using the probability that the distance between the results of two studies, as quantified by a kernel-based metric, is below a certain threshold. The authors develop an algorithm to estimate the number of experiments required to achieve a desired level of generalizability, based on a linear relationship between the logarithms of sample size and the quantile of the distance metric. The paper includes case studies on categorical encoders and large language models, demonstrating the application of the proposed framework and the estimation of the number of experiments needed for generalizable results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel formalization of experimental studies in machine learning, providing a clear mathematical framework for defining and quantifying generalizability. This is a significant contribution to the field, as it addresses the critical issue of whether experimental results can be expected to hold under different conditions.

2. The paper proposes a practical algorithm for estimating the number of experiments required to achieve a desired level of generalizability. This is a valuable tool for researchers, as it provides guidance on how to design experiments that are both efficient and likely to produce generalizable results.

3. The paper includes case studies on real-world machine learning problems, demonstrating the applicability of the proposed framework. The analysis of categorical encoders and large language models provides concrete examples of how the framework can be used to assess the generalizability of experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper relies on the assumption that the experimental conditions are independent and identically distributed (i.i.d.), which may not always hold in practice. The authors acknowledge this limitation but do not provide a detailed discussion of its implications or potential solutions. Specifically, the i.i.d. assumption is a strong one, and violations could arise from various sources, such as temporal dependencies in data collection, or correlations between different experimental factors. The paper does not address how the proposed framework would be affected by such dependencies, nor does it offer any guidance on how to detect or mitigate them. This lack of discussion limits the practical applicability of the framework in real-world scenarios where the i.i.d. assumption is unlikely to hold perfectly.

2. The paper's focus on ranking-based results may limit its applicability to other types of experimental outcomes. While the authors propose a kernel-based metric for measuring the distance between results, the core of the framework is built around the idea of ranking alternatives. This may not be suitable for experiments where the primary outcome is a continuous variable, such as accuracy or loss, or where the results are more complex, such as confusion matrices or ROC curves. The paper does not adequately explore how the framework could be extended to handle these types of outcomes, which limits its generality.

3. The paper does not provide a detailed analysis of the computational complexity of the proposed algorithm for estimating the number of experiments. While the authors mention that the algorithm is efficient, they do not provide a formal analysis of its time and space complexity. This is a significant omission, as the computational cost of the algorithm could be a limiting factor in its practical application, especially for large-scale experiments. A detailed analysis of the algorithm's complexity, including its dependence on the number of alternatives, experimental conditions, and the desired level of generalizability, would be necessary to assess its scalability.

### Suggestions

The paper makes a valuable contribution by formalizing the concept of generalizability in machine learning experiments. However, several aspects could be improved to enhance its practical applicability and theoretical rigor. First, the assumption of independent and identically distributed (i.i.d.) experimental conditions needs further scrutiny. The authors should explore the impact of relaxing this assumption, perhaps by considering scenarios where experimental conditions are sampled from a non-i.i.d. distribution. For instance, they could investigate how temporal dependencies or correlations between experimental factors affect the generalizability metric and the estimation of the required number of experiments. This could involve incorporating techniques from time series analysis or causal inference to model the dependencies between experimental conditions. Furthermore, the authors should provide practical guidance on how to assess the validity of the i.i.d. assumption in real-world experiments and suggest methods for mitigating the effects of its violation. This would significantly enhance the robustness and applicability of the proposed framework.

Second, the paper should broaden its scope to include a wider range of experimental outcomes beyond rankings. While rankings are a common outcome in comparative studies, many experiments in machine learning involve continuous variables or more complex results. The authors could explore how their framework can be adapted to handle these types of outcomes. For example, they could investigate the use of different distance metrics that are suitable for continuous variables, such as the Earth Mover's Distance or the Wasserstein metric. They could also explore how to extend the framework to handle more complex results, such as confusion matrices or ROC curves, by defining appropriate distance metrics for these types of data. This would significantly increase the generality and applicability of the proposed framework. Additionally, the authors should provide concrete examples of how their framework can be applied to different types of experimental outcomes, demonstrating its versatility.

Finally, the paper needs a more detailed analysis of the computational complexity of the proposed algorithm. The authors should provide a formal analysis of the time and space complexity of the algorithm, including its dependence on the number of alternatives, experimental conditions, and the desired level of generalizability. This analysis should be supported by empirical evidence, demonstrating the scalability of the algorithm for different problem sizes. Furthermore, the authors should discuss potential optimizations that could be used to improve the efficiency of the algorithm, such as parallelization or approximation techniques. This would make the proposed framework more practical for large-scale experiments and would allow researchers to better assess the computational cost of applying the framework to their specific problems.

### Questions

1. How does the proposed framework handle cases where the experimental conditions are not independent and identically distributed (i.i.d.)? Are there any extensions or modifications that can be made to handle such cases?

2. Can the framework be extended to handle other types of experimental results beyond rankings, such as continuous variables or more complex results? If so, how would the generalizability metric need to be adapted?

3. What is the computational complexity of the proposed algorithm for estimating the number of experiments? How does it scale with the number of alternatives and experimental conditions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
