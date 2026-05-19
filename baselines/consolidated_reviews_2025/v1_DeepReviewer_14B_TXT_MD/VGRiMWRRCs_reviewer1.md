### Summary

This paper proposes to address the group robustness problem by applying empirical Bayesian framework. The authors first show that previous group robustness methods can be seen as estimating the posterior distributions over group assignments and the model parameters. Then the authors propose to leverage the epistemic uncertainty from an ERM model to perform last layer retraining.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a good literature review of previous group robustness methods and summarizing them with the proposed empirical Bayesian framework. The writing is clear and easy to follow.

2. The experiments are comprehensive, including multiple datasets and tasks (image and text).

### Weaknesses

#### Some Related Works


#### comment

1. The connection between the proposed empirical Bayesian framework and the proposed method is weak. The authors only use the framework to summarize previous group robustness methods, but do not utilize it in the proposed method. Specifically, the framework is used to motivate the need for a method that leverages uncertainty, but the actual method directly uses the uncertainty of an ERM model without explicitly connecting it back to the Bayesian framework. The link between the posterior distribution over group assignments and the uncertainty used for reweighting is not clearly established. It seems that the framework is more of a high-level motivation rather than an integral part of the method's design and implementation.

2. The proposed method seems a bit ad-hoc, combining ERM, uncertainty estimation, and last layer retraining. Each of them already has many existing works, and the motivation for combining them is not clear. The paper does not provide a strong theoretical justification for why this specific combination should lead to improved group robustness. The connection between the uncertainty estimation and the reweighting strategy needs more clarification. It is unclear why the epistemic uncertainty from an ERM model would necessarily correspond to the minority groups. The method lacks a clear explanation of why this particular combination of techniques is expected to be effective, beyond the empirical results.

3. The proposed method is very similar to [1], which also uses evidential uncertainty to address group robustness. The authors should discuss the difference. The paper needs to clearly articulate how the proposed method differs from existing approaches that also leverage evidential uncertainty for group robustness. A more detailed comparison is needed to highlight the novel aspects of the proposed method.

4. The results are good, but the analysis is not sufficient. The authors should provide more in-depth analysis of when the method works and when it does not. The analysis should include a discussion of the limitations of the method and the conditions under which it may fail. The paper should also provide a more detailed analysis of the failure cases and the reasons behind them.

### Suggestions

The paper would benefit from a more rigorous connection between the proposed empirical Bayesian framework and the actual method. The authors should explicitly derive how the epistemic uncertainty from the ERM model relates to the posterior distribution over group assignments within the Bayesian framework. This could involve showing how the uncertainty estimates can be interpreted as a proxy for the posterior probability of a sample belonging to a minority group. A more detailed explanation of the theoretical underpinnings of the method is needed to justify the use of uncertainty for reweighting. The authors should also provide a more thorough discussion of the assumptions made and the limitations of the approach. This would strengthen the theoretical contribution of the paper and make the method less ad-hoc.

To address the concern about the method being a combination of existing techniques, the authors should provide a more detailed explanation of why this specific combination is expected to be effective. This could involve a theoretical analysis of how ERM, uncertainty estimation, and last layer retraining interact to improve group robustness. The authors should also discuss the potential limitations of this approach and the conditions under which it may not be effective. A more detailed comparison with alternative methods is needed to highlight the advantages of the proposed approach. This would help to justify the novelty and contribution of the method beyond simply combining existing techniques. The authors should also consider exploring alternative uncertainty estimation methods and comparing their performance with the proposed approach.

Finally, the paper needs a more thorough comparison with existing methods that use evidential uncertainty for group robustness. The authors should clearly articulate the differences between their method and these existing approaches, highlighting the novel aspects of their work. A more detailed analysis of the experimental results is also needed, including a discussion of the limitations of the method and the conditions under which it may fail. The authors should also provide a more detailed analysis of the failure cases and the reasons behind them. This would help to provide a more complete picture of the performance of the method and its limitations.

### Questions

1. How is the proposed method connected to the proposed empirical Bayesian framework, beyond just summarizing previous methods?

2. Why would the epistemic uncertainty of an ERM model correspond to the minority groups? The ERM model should be more confident on the majority group.

3. How is the proposed method different from [1]?

[1]  Robust Learning with Progressive Ensemble Label Smoothing based on Uncertainty

### Rating

3

### Confidence

4

**********
