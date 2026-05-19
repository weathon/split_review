### Summary

This paper addresses the issue of delayed feedback in estimating heterogeneous treatment effects (HTEs), where the impact of a treatment may not be immediately apparent and can be obscured by the timing of observed outcomes. The authors propose a novel method, CFR-DF (Counterfactual Regression with Delayed Feedback), which incorporates both the treatment effect on the outcome and the timing of the response. They provide theoretical proofs of identifiability for both the outcome and response time under specific assumptions. The method is validated through experiments on both synthetic and real-world datasets, demonstrating its effectiveness in improving HTE estimation accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to HTE estimation that explicitly accounts for delayed feedback, a common issue in many real-world applications.
2. The authors provide rigorous theoretical proofs of identifiability for both the outcome and response time, which adds credibility to their proposed method.
3. The paper is well-organized and clearly written, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's theoretical contributions are not entirely novel, as the proofs rely heavily on existing frameworks. The core identifiability results, while adapted to the delayed feedback setting, do not introduce significant new mathematical techniques or insights. The proofs, while technically sound, largely follow standard causal inference arguments, and the adaptation to delayed feedback appears to be a straightforward extension rather than a substantial theoretical advancement.
2. The experimental evaluation is limited in scope, with a focus on relatively simple synthetic datasets and a few real-world examples. The synthetic data generation process, while including a delay parameter, does not fully capture the complexity of real-world delayed feedback scenarios. The real-world datasets used, while relevant, do not provide a comprehensive assessment of the method's robustness across diverse settings. The lack of comparison with more recent state-of-the-art methods in delayed treatment effect estimation further limits the evaluation's impact.

### Suggestions

To strengthen the theoretical contribution, the authors should explore more sophisticated mathematical tools or provide a more in-depth analysis of the identifiability conditions. For example, they could investigate the sensitivity of their results to violations of the assumptions, or explore alternative identification strategies that might be more robust or efficient. Furthermore, they could consider extending their framework to incorporate more complex forms of delayed feedback, such as non-Markovian effects or time-varying confounders. This would involve developing new theoretical results that go beyond the current identifiability proofs. The authors should also consider providing a more detailed discussion of the limitations of their theoretical framework and the potential impact of these limitations on the practical application of their method.

To improve the experimental evaluation, the authors should include a wider range of synthetic datasets with varying degrees of complexity and different types of delayed feedback. They should also consider using more realistic simulation scenarios that better reflect the challenges of real-world applications. Furthermore, the authors should compare their method with a broader range of state-of-the-art methods in delayed treatment effect estimation, including those that explicitly model time-varying confounders or use different identification strategies. This would provide a more comprehensive assessment of the method's performance and its advantages over existing approaches. The authors should also provide a more detailed analysis of the method's sensitivity to hyperparameter choices and provide guidance on how to select appropriate values for these parameters.

Finally, the authors should consider providing a more detailed discussion of the practical implications of their method and its potential applications in real-world settings. This should include a discussion of the computational complexity of their method and its scalability to large datasets. They should also discuss the potential challenges of applying their method in practice, such as the need for accurate estimation of the delay parameter and the potential impact of unobserved confounders. By addressing these practical considerations, the authors can make their work more accessible and useful to a wider audience.

### Questions

1. How does the proposed CFR-DF method handle potential violations of the assumptions, such as unobserved confounders or violations of the positivity assumption?
2. Could the authors provide more details on the computational complexity of the CFR-DF method and its scalability to large datasets?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
