### Summary

This paper studies the problem of estimating heterogeneous treatment effects when the feedback is delayed. The authors formulate the problem as a counterfactual regression problem, and propose a modified EM algorithm to estimate the potential outcomes and the response time. The authors provide theoretical guarantees on the identifiability of the causal estimands, and conduct experiments on both synthetic and real-world datasets to demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The problem of estimating heterogeneous treatment effects with delayed feedback is an important problem that has not been studied in the literature.
2. The authors provide theoretical guarantees on the identifiability of the causal estimands, which is a significant contribution to the field.
3. The authors conduct experiments on both synthetic and real-world datasets, which demonstrates the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well motivated. The authors do not provide a clear explanation of why estimating heterogeneous treatment effects with delayed feedback is important. The authors should provide more concrete examples of real-world scenarios where this problem is relevant, and explain why existing methods are insufficient to address this problem. For instance, in a medical setting, a delayed response could mean a patient's condition worsening or improving, which has significant implications for treatment decisions. The authors should elaborate on how their method addresses these specific challenges.
2. The authors do not provide a detailed comparison with existing methods for estimating heterogeneous treatment effects. The authors should discuss how their method differs from existing methods, and what advantages it has over these methods. For example, the authors should compare their method with methods that use survival analysis techniques, or methods that incorporate time-varying confounders, and explain why their approach is more suitable for the delayed feedback setting.
3. The authors do not provide a detailed discussion of the limitations of their method. The authors should discuss the assumptions that are required for their method to be valid, and the potential biases that could arise from these assumptions. For example, the authors should discuss the assumption of no unmeasured confounding, and how violations of this assumption could affect the results. The authors should also discuss the sensitivity of their method to the choice of hyperparameters, and provide guidance on how to select appropriate values for these parameters.

### Suggestions

The authors should begin by providing a more compelling motivation for their work. They need to articulate specific scenarios where delayed feedback in treatment effect estimation is a critical issue, and why existing methods fall short. For example, in a personalized medicine context, a delayed response could mean a patient's condition worsening or improving, which has significant implications for treatment decisions. The authors should provide concrete examples of how their method addresses these specific challenges, and why existing methods are insufficient. This should include a discussion of the limitations of current approaches and how the proposed method overcomes these limitations. The authors should also discuss the potential impact of their method on real-world applications, and how it could be used to improve decision-making in practice.

Furthermore, the authors need to provide a more thorough comparison with existing methods for estimating heterogeneous treatment effects. They should discuss how their method differs from existing methods, and what advantages it has over these methods. For example, the authors should compare their method with methods that use survival analysis techniques, or methods that incorporate time-varying confounders, and explain why their approach is more suitable for the delayed feedback setting. This comparison should not only focus on the theoretical differences but also on the practical implications of these differences. The authors should also discuss the computational complexity of their method compared to existing methods, and whether it is scalable to large datasets. A detailed comparison with existing methods would help to position the proposed method within the existing literature and highlight its unique contributions.

Finally, the authors should provide a more detailed discussion of the limitations of their method. They should discuss the assumptions that are required for their method to be valid, and the potential biases that could arise from these assumptions. For example, the authors should discuss the assumption of no unmeasured confounding, and how violations of this assumption could affect the results. The authors should also discuss the sensitivity of their method to the choice of hyperparameters, and provide guidance on how to select appropriate values for these parameters. The authors should also discuss the potential impact of the delayed feedback on the identifiability of the causal estimands, and how their method addresses these challenges. A thorough discussion of the limitations would help to provide a more balanced and realistic assessment of the proposed method.

### Questions

1. What is the motivation for studying the problem of estimating heterogeneous treatment effects with delayed feedback? Can you provide more concrete examples of real-world scenarios where this problem is relevant?
2. How does the proposed method compare with existing methods for estimating heterogeneous treatment effects? What are the advantages and disadvantages of the proposed method compared to existing methods?
3. What are the limitations of the proposed method? What assumptions are required for the method to be valid, and what are the potential biases that could arise from these assumptions?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
