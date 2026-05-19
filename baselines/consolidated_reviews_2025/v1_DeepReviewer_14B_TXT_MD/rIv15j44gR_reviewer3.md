### Summary

The paper studies the problem of estimating heterogeneous treatment effects in the presence of delayed feedback. The authors formalize the problem by considering the potential response time of different treatments, and prove the identifiability of the eventual potential outcome and potential response times under certain assumptions. They propose a principled learning approach called CFR-DF, which extends counterfactual regression to delayed feedback outcomes. The effectiveness of the proposed method is validated through extensive experiments on both synthetic and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important and practical problem in treatment effect estimation, which is often overlooked in existing studies.
2. The authors provide a clear and rigorous theoretical analysis of the problem, including identifiability results and a principled learning approach.
3. The proposed method is evaluated through extensive experiments on both synthetic and real-world datasets, demonstrating its effectiveness in various scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes binary outcomes, which may limit its applicability in real-world scenarios where outcomes can be continuous or multi-valued. Specifically, the method does not account for scenarios where the outcome is a continuous measure of improvement, or where multiple outcomes are of interest simultaneously. This restriction to binary outcomes may not be suitable for many practical applications, such as in healthcare or economics, where outcomes are often more nuanced.
2. The paper does not provide a detailed discussion of the computational complexity of the proposed method. It is unclear how the method scales with the size of the dataset, and whether it is feasible to apply it to large-scale datasets. The analysis should include a breakdown of the time complexity of each step in the CFR-DF algorithm, and discuss the memory requirements for storing intermediate results. Without this, it is difficult to assess the practical applicability of the method for large datasets.
3. The paper does not discuss the potential impact of unobserved confounders on the estimation of treatment effects. While the authors mention the assumption of no unmeasured confounders, they do not elaborate on how violations of this assumption might affect the results. A discussion of sensitivity analysis or robustness checks would be valuable. Specifically, the paper should address how the presence of unobserved variables that influence both treatment assignment and the outcome could bias the estimated treatment effects, and what steps could be taken to mitigate this bias.

### Suggestions

The authors should consider extending their framework to handle continuous and multi-valued outcomes. This could involve adapting the counterfactual regression approach to model continuous response variables, potentially using techniques from regression analysis or generalized linear models. For multi-valued outcomes, the authors could explore methods that model each outcome dimension separately or jointly, depending on the relationships between the outcomes. This would significantly broaden the applicability of the proposed method to a wider range of real-world problems. Furthermore, the authors should provide a more detailed analysis of the computational complexity of their method. This should include a breakdown of the time complexity of each step in the CFR-DF algorithm, as well as a discussion of the memory requirements for storing intermediate results. The analysis should consider the impact of dataset size on the computational cost, and discuss potential strategies for improving scalability, such as parallelization or approximation techniques. This would help to clarify the practical limitations of the method and guide its application to large-scale datasets. Finally, the authors should include a more thorough discussion of the potential impact of unobserved confounders on the estimation of treatment effects. This should include a discussion of sensitivity analysis or robustness checks that could be used to assess the robustness of the results to violations of the unconfoundedness assumption. The authors could also explore methods for addressing unobserved confounding, such as instrumental variables or control function approaches. This would provide a more complete picture of the limitations of the proposed method and guide its application in real-world settings where unobserved confounding is likely to be present.

### Questions

1. Can the proposed method be extended to handle continuous or multi-valued outcomes?
2. How does the computational complexity of the proposed method scale with the size of the dataset?
3. How sensitive are the results to violations of the unconfoundedness assumption?

### Rating

6

### Confidence

4

**********
