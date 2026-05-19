### Summary

The paper proposes a method for estimating heterogeneous treatment effects (HTEs) with delayed feedback. The authors first formalize the problem and prove the identifiability of the causal estimands. They then propose a principled learning approach, called CFR-DF, to simultaneously predict potential outcomes and potential response times. The authors conduct extensive experiments on both synthetic and real-world datasets to demonstrate the effectiveness of their proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The problem of estimating heterogeneous treatment effects with delayed feedback is important and interesting.
3. The authors provide theoretical proofs of the identifiability of the causal estimands.
4. The authors propose a principled learning approach, called CFR-DF, to simultaneously predict potential outcomes and potential response times.
5. The authors conduct extensive experiments on both synthetic and real-world datasets to demonstrate the effectiveness of their proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed discussion of the limitations of the proposed method.
2. The paper does not provide a detailed discussion of the computational complexity of the proposed method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed CFR-DF method. Specifically, the authors should address scenarios where the assumptions underlying the method might be violated, such as when the treatment effect is not consistent across different subgroups or when the delay in feedback is not uniform across individuals. For example, if the treatment effect varies significantly within a stratum defined by a key covariate, the method's ability to accurately estimate HTE could be compromised. Furthermore, the authors should discuss the sensitivity of the method to the choice of hyperparameters and the potential impact of model misspecification. A more detailed analysis of these limitations would provide a more balanced and realistic assessment of the method's applicability. It would also be beneficial to explore the performance of the method under different levels of confounding, as this is a common challenge in causal inference.

Additionally, the paper should include a more detailed analysis of the computational complexity of the CFR-DF method. While the authors mention that the method is computationally efficient, they do not provide a formal analysis of the time and space complexity of the algorithm. It would be beneficial to include a discussion of how the computational cost scales with the number of individuals, the number of covariates, and the size of the dataset. This analysis should also consider the computational cost of the counterfactual regression component and the delayed feedback component. Furthermore, the authors should discuss the practical implications of the computational complexity, such as the feasibility of applying the method to large-scale datasets. A more detailed analysis of the computational complexity would help readers understand the practical limitations of the method.

Finally, the authors should consider including a more detailed discussion of the practical challenges associated with applying the CFR-DF method in real-world settings. For example, they should discuss the potential impact of unobserved confounding variables on the accuracy of the method and the strategies for mitigating this impact. They should also discuss the challenges associated with collecting and preprocessing the data required by the method, such as the measurement of treatment assignment, outcomes, and response times. A more detailed discussion of these practical challenges would help readers understand the limitations of the method and the conditions under which it is most likely to be effective. It would also be useful to explore the performance of the method under different levels of data quality, such as missing data or measurement error.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
