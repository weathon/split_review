### Summary

This paper proposes a formalization of the concept of generalizability in machine learning. The authors propose a definition of generalizability as the probability that any two empirical studies approximating the same ideal study yield similar results. They then propose a method to estimate the number of experiments needed to obtain generalizable results. The authors apply their framework to two case studies: a benchmark of categorical encoders and a benchmark of large language models (LLMs).

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The problem is well-motivated and the proposed solution is novel. The paper includes two case studies, which demonstrate the applicability of the proposed framework to different types of machine learning problems.

### Weaknesses

#### Some Related Works


#### comment

The paper assumes that the experimental conditions are independent and identically distributed (i.i.d.). However, in many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. For example, in a study of a machine learning algorithm, the choice of hyperparameters may be dependent on the specific dataset being used, which violates the i.i.d. assumption. The paper does not discuss the limitations of this assumption or how it may affect the results.

### Suggestions

The paper's core contribution lies in formalizing generalizability, but the practical applicability of the proposed framework is limited by the i.i.d. assumption. To enhance the paper, the authors should explore methods to relax this assumption. One approach could be to investigate the use of techniques from causal inference, which are designed to handle dependencies between variables. For instance, they could consider using instrumental variables or propensity score matching to account for potential confounding factors that arise when experimental conditions are not independent. This would significantly broaden the applicability of the framework to more realistic scenarios.

Furthermore, the paper could benefit from a more detailed discussion of how the choice of kernel impacts the estimation of generalizability. While the authors mention that different kernels capture different aspects of the results, they do not provide concrete guidance on how to select an appropriate kernel for a given task. A more thorough analysis of the properties of different kernels, such as their sensitivity to noise and their ability to capture different types of relationships, would be valuable. For example, the authors could explore the use of kernel methods that are specifically designed for non-i.i.d. data, or they could investigate the use of adaptive kernel selection techniques that automatically adjust the kernel parameters based on the characteristics of the data.

Finally, the paper should include a more comprehensive evaluation of the proposed framework. While the two case studies are a good starting point, they do not fully demonstrate the robustness and generalizability of the approach. The authors should consider evaluating their framework on a wider range of datasets and tasks, including those with more complex dependencies between experimental conditions. They should also compare their approach to existing methods for assessing generalizability, such as those based on cross-validation or bootstrapping. This would provide a more rigorous assessment of the strengths and limitations of the proposed framework and would help to establish its practical value.

### Questions

How does the proposed framework handle the case where the experimental conditions are not independent and identically distributed (i.i.d.)? In many real-world scenarios, the experimental conditions may not be i.i.d., and this assumption may not hold. How does the framework account for potential dependencies between experimental conditions?

### Rating

8

### Confidence

3

**********
