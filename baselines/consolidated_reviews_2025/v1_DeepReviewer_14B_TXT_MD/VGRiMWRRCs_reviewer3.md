### Summary

This paper presents a novel approach to improve group robustness in machine learning models, particularly in the presence of spurious correlations. The authors propose a unified framework based on Empirical Bayes, which allows for the integration of various existing methods. Their key contribution is the "Learn from Known Unknowns" (LfKU) technique, which leverages the epistemic uncertainty of biased ERM models to perform selective reweighting during retraining. The method aims to improve group robustness without requiring explicit group annotations, thereby enhancing scalability and practicality. The authors demonstrate the effectiveness of their approach through extensive experiments on diverse datasets, showing improved worst-group accuracy and reduced reliance on hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel and unified perspective on group robustness by framing existing methods within an Empirical Bayesian framework. This offers a more principled understanding of how to address spurious correlations and improve model robustness.
2. The proposed LfKU method is innovative in its use of epistemic uncertainty to guide the retraining process. This allows for a more adaptive and efficient way to mitigate the impact of spurious correlations without the need for explicit group labels.
3. The authors conduct a comprehensive set of experiments across various datasets, demonstrating the effectiveness of their approach. The results show consistent improvements in worst-group accuracy, which is a critical metric for evaluating group robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on the Empirical Bayes framework assumes that the prior distribution over group assignments can be estimated from the data. However, in cases where group distributions are highly non-uniform or complex, this assumption may not hold, potentially affecting the performance of the method. Specifically, the method does not explicitly address scenarios where the group priors are multi-modal or where there are significant overlaps between groups, which could lead to inaccurate uncertainty estimates and suboptimal reweighting. The assumption of a smooth, learnable prior might be too restrictive for real-world datasets with complex group structures.
2. While the paper demonstrates empirical success, the theoretical analysis could be strengthened. A more rigorous theoretical foundation would help in understanding the conditions under which the proposed method is guaranteed to improve group robustness. The current theoretical justification lacks a clear connection between the proposed uncertainty-based reweighting and the actual improvement in worst-group performance. A more detailed analysis of how the uncertainty estimates relate to the spurious correlations would be beneficial.
3. The method's effectiveness is partly dependent on the quality of the epistemic uncertainty estimates from the ERM model. If the ERM model fails to capture meaningful uncertainty, the subsequent retraining process may not be effective. The paper does not explore the sensitivity of the method to different uncertainty estimation techniques or the potential for miscalibration of the uncertainty estimates. It is unclear how the method would perform if the ERM model produces overconfident or underconfident uncertainty estimates, and how these issues would impact the reweighting process.

### Suggestions

The paper would benefit from a more detailed discussion of the limitations of the Empirical Bayes framework, particularly in scenarios with complex group structures. The authors should explore alternative approaches for handling non-uniform or multi-modal group priors, such as using a mixture model for the prior or incorporating domain knowledge to guide the prior estimation. Furthermore, the paper should include a sensitivity analysis of the method's performance under different group prior distributions, including cases where the prior is significantly mis-specified. This would provide a more comprehensive understanding of the method's robustness and applicability in real-world settings. The authors could also consider incorporating techniques from robust Bayesian inference to mitigate the impact of inaccurate prior estimates.

To strengthen the theoretical foundation, the authors should provide a more rigorous analysis of the relationship between the proposed uncertainty-based reweighting and the improvement in worst-group performance. This could involve deriving bounds on the worst-group error or showing that the proposed method converges to a solution that minimizes the worst-group loss under certain conditions. The analysis should also address the potential for the reweighting process to introduce bias or instability, and provide guarantees on the convergence and generalization properties of the method. A more detailed theoretical analysis would provide a stronger justification for the proposed approach and enhance the paper's impact.

Finally, the paper should include a more thorough investigation of the sensitivity of the method to different uncertainty estimation techniques. The authors should explore the impact of using different evidential deep learning methods or other uncertainty quantification techniques on the performance of the proposed approach. The paper should also discuss the potential for miscalibration of the uncertainty estimates and how this could affect the reweighting process. The authors could consider incorporating techniques for uncertainty calibration to improve the reliability of the uncertainty estimates. A more detailed analysis of the uncertainty estimation process would provide a more complete picture of the method's strengths and limitations.

### Questions

1. How does the method perform when the group distributions are highly non-uniform or complex? Are there any modifications to the framework that could address such scenarios?
2. Can the authors provide more theoretical insights into why the proposed uncertainty-based reweighting leads to improved group robustness? Are there any guarantees on the convergence or generalization properties of the method?
3. How sensitive is the method to the quality of the epistemic uncertainty estimates? What happens if the ERM model fails to capture meaningful uncertainty?

### Rating

6

### Confidence

3

**********
