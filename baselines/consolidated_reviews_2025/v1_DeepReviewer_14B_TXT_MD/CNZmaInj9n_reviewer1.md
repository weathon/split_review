### Summary

This paper studies the problem of computing Shapley values of features for predicting a label with a machine learning model, given a specific dataset. This problem is known to be computationally challenging, and many sampling-based algorithms have been proposed for efficient approximation. This paper unifies several popular algorithms (semigalue, random order value, and least square value) by showing that they are essentially different mean estimators embedded in a common framework. Based on this observation, this paper further proposes a new algorithm SimSHAP, which learns a function that maps an input data point to the Shapley values of the features for this data point, via least squares regression. SimSHAP is shown to be more efficient than the prior method FastSHAP, while maintaining similar accuracy.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

This paper provides a unified view of several existing methods for Shapley values estimation, which could be helpful for future development of more efficient algorithms. The proposed algorithm SimSHAP is more efficient than the prior method FastSHAP, while producing more accurate results on several datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The unified framework in Section 2.3 is not very clear. In particular, the unified stochastic estimator is defined in Definition 2 as $\phi^{uni}=T\tilde\phi+b$, but it is not clear what $\tilde\phi$ is and what the goal of defining the unified estimator in this form is. It is not clear to me why the formulation of the unified estimator is useful, and why the specific forms of the semivalue, random order value, and least square value algorithms are preferred. It would be helpful if the authors could provide more insights on this.
2. The proposed algorithm SimSHAP is essentially a variant of the least square value algorithm, with the difference being that SimSHAP does not perform the normalization in the end to ensure efficiency. This is mentioned in the paper, but it is not clear to me that why this difference is important and how it leads to a better performance in practice. In particular, it is not clear to me why the removal of the normalization step leads to a better performance in practice.

### Suggestions

The paper would benefit from a more detailed explanation of the unified framework introduced in Section 2.3. Specifically, the role of $\tilde\phi$ within the definition of the unified stochastic estimator, $\phi^{uni}=T\tilde\phi+b$, needs further clarification. It is unclear how $\tilde\phi$ relates to the sampled subset values and how this formulation helps in understanding the relationship between different Shapley value estimation methods. The authors should elaborate on the intuition behind expressing different algorithms as variations of mean estimators within this framework. Furthermore, a more in-depth discussion is needed on why the specific forms of the semivalue, random order value, and least square value algorithms are preferred within this unified view. Providing concrete examples of how these algorithms map to the unified framework would greatly enhance the reader's understanding and the overall contribution of the paper.

Regarding the SimSHAP algorithm, the paper should provide a more thorough justification for omitting the normalization step present in FastSHAP. While the authors mention that SimSHAP does not require the computation of $v(\mathbf{N})$ and a subsequent normalization step, the practical implications of this omission are not fully explored. It is crucial to explain why enforcing the efficiency constraint through normalization is problematic in practice, and how the unconstrained formulation of SimSHAP avoids these issues. A more detailed analysis of the trade-offs between the constrained and unconstrained approaches would be beneficial. For instance, the authors could discuss the potential impact on the accuracy and stability of the estimated Shapley values when the efficiency constraint is not strictly enforced. Furthermore, a more detailed explanation of why the unconstrained formulation leads to a better performance in practice is needed.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed approach. While the experimental results demonstrate that SimSHAP performs well on the tested datasets, it is important to acknowledge potential scenarios where the algorithm might not be as effective. For example, the authors could discuss the sensitivity of SimSHAP to the choice of the sampling strategy or the architecture of the learned function. Additionally, a more detailed comparison with other state-of-the-art Shapley value estimation methods, beyond FastSHAP, would provide a more complete picture of the strengths and weaknesses of the proposed algorithm. This would help the reader understand the specific contexts in which SimSHAP is most applicable and where alternative methods might be more suitable.

### Questions

See the questions in the "weakness" section.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
