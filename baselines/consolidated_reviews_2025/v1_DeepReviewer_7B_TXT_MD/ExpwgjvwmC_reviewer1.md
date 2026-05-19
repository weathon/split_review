### Summary

The paper proposes a new evaluation framework for AI/ML models called OMNIINPUT. Unlike traditional data-centric evaluation, OMNIINPUT is model-centric, evaluating models by examining their output distribution across the entire input space, rather than relying on pre-defined test sets. The framework uses an efficient sampler to generate representative inputs and assess model performance through precision and recall metrics, offering a more comprehensive understanding of model behavior, especially in open-world settings where models must handle unseen data.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed evaluation framework is novel and interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive discussion of related work, particularly in the areas of open-world evaluation and out-of-distribution (OOD) detection. A more thorough literature review would help contextualize the contributions and highlight the novelty of the proposed approach. Specifically, the paper should discuss how OMNIINPUT relates to existing methods that also aim to evaluate model performance beyond standard test sets, such as those using generative models or adversarial attacks. The current discussion does not adequately address the nuances of different approaches to open-world evaluation.
2. The paper does not provide a detailed analysis of the computational efficiency of the proposed sampler, especially in comparison to traditional data-centric evaluation methods. A more rigorous analysis of the computational complexity and resource requirements would be beneficial. The paper should include a breakdown of the time and memory costs associated with the sampling process, as well as how these costs scale with the size of the input space and the complexity of the model. Furthermore, a comparison with the computational costs of traditional evaluation methods is needed to justify the practicality of the proposed approach.
3. The paper does not provide a clear explanation of how the proposed precision and recall metrics are calculated in the context of the entire input space. The paper should provide a detailed mathematical formulation of these metrics, including how they are adapted to the continuous nature of the input space. The current description lacks the necessary detail to fully understand how these metrics are computed and interpreted in the proposed framework.
4. The paper does not provide a clear explanation of how the proposed precision and recall metrics are calculated in the context of the entire input space. The paper should provide a detailed mathematical formulation of these metrics, including how they are adapted to the continuous nature of the input space. The current description lacks the necessary detail to fully understand how these metrics are computed and interpreted in the proposed framework.
5. The paper does not provide a clear explanation of how the proposed precision and recall metrics are calculated in the context of the entire input space. The paper should provide a detailed mathematical formulation of these metrics, including how they are adapted to the continuous nature of the input space. The current description lacks the necessary detail to fully understand how these metrics are computed and interpreted in the proposed framework.

### Suggestions

The paper should include a more comprehensive discussion of related work, particularly in the areas of open-world evaluation and out-of-distribution (OOD) detection. This discussion should not only cite relevant papers but also provide a detailed comparison of the proposed method with existing approaches. For example, the paper should discuss how OMNIINPUT differs from methods that use generative models to generate diverse test cases or those that employ adversarial training to improve model robustness. A thorough literature review would help to contextualize the contributions of the paper and highlight the novelty of the proposed approach. The discussion should also address the limitations of existing methods and how OMNIINPUT addresses these limitations, providing a clear rationale for the proposed framework.

The paper needs to provide a more detailed analysis of the computational efficiency of the proposed sampler. This analysis should include a breakdown of the time and memory costs associated with the sampling process, as well as how these costs scale with the size of the input space and the complexity of the model. The paper should also compare the computational costs of OMNIINPUT with those of traditional data-centric evaluation methods. This comparison should be done in terms of both time and memory requirements, providing a clear understanding of the trade-offs between the two approaches. Furthermore, the paper should discuss the practical implications of these computational costs, including the feasibility of applying the proposed method to large-scale datasets and complex models. The analysis should also consider the impact of different sampling strategies on the computational efficiency of the method.

The paper should provide a detailed mathematical formulation of the precision and recall metrics used in the context of the entire input space. This formulation should clearly explain how these metrics are adapted to the continuous nature of the input space, including the use of binning or other techniques to discretize the input space. The paper should also provide a clear explanation of how the metrics are calculated for each bin and how these bin-specific metrics are aggregated to obtain the overall precision and recall values. The paper should also discuss the limitations of these metrics and how they might be improved in future work. The mathematical formulation should be precise and unambiguous, allowing other researchers to reproduce the results and build upon the proposed framework.

### Questions

1. How does the proposed OMNIINPUT framework compare with existing open-world evaluation methods in terms of computational efficiency and scalability?
2. How does the choice of the Wang–Landau (WL) algorithm sampler impact the accuracy and reliability of the evaluation results? Have you considered other sampling techniques, and if so, how do they compare?
3. How sensitive is the OMNIINPUT framework to the choice of hyperparameters, such as the number of bins used for calculating precision and recall?

### Rating

3

### Confidence

4

**********
