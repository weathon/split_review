### Summary

The paper proposes a new method for fairness learning without sensitive attributes. Specifically, the authors employ a linear classifier to obtain confidence scores and split the dataset into high-confidence and low-confidence data. Then, the authors train two VAEs on these two data subsets respectively. The authors also propose a learnable noise module to extract essential information for predictions and a knowledge-sharing mechanism to share knowledge between two VAEs. The proposed method is evaluated on two datasets and two fairness metrics. The experiment results show that the proposed method outperforms existing methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The paper proposes a new method for fairness learning without sensitive attributes, which is an important topic in the fairness community.
- The paper provides a detailed analysis of the relationship between fairness and model confidence, which is interesting.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks the motivation of the proposed method. Why does the proposed method, which includes learnable noise and a knowledge-sharing mechanism, help improve fairness? Although the authors provide some explanations, they are insufficient. I would like to see more theoretical explanations or experimental evidence to support the proposed method.
- The paper lacks a discussion of the limitations of the proposed method.
- The authors only conduct experiments on two datasets and two fairness metrics. The experimental results may not be convincing.

### Suggestions

The paper would benefit from a more rigorous justification of the proposed method's effectiveness in mitigating bias. While the authors introduce a learnable noise module and a knowledge-sharing mechanism between two VAEs, the underlying reasons for their impact on fairness remain unclear. Specifically, the learnable noise is said to extract essential information, but it is not clear why this process would inherently lead to fairer predictions. A more detailed analysis, perhaps through ablation studies or visualizations of the learned noise patterns, could provide valuable insights. Furthermore, the knowledge-sharing mechanism, while intuitively appealing, lacks a theoretical grounding. It would be beneficial to explore how the exchange of information between the high-confidence and low-confidence VAEs affects the model's sensitivity to biased features. For example, does the mechanism encourage the high-confidence VAE to rely less on sensitive attributes by learning from the low-confidence VAE's more uncertain representations? Without a deeper understanding of these mechanisms, the proposed method appears somewhat ad-hoc.

To strengthen the paper, the authors should also address the limitations of their approach. For instance, the method's reliance on a confidence-based split might introduce biases if the confidence scores are themselves correlated with sensitive attributes. This could lead to a scenario where the high-confidence data primarily comes from one demographic group, while the low-confidence data comes from another. Such a situation could exacerbate existing biases rather than mitigate them. The authors should also discuss the computational cost of training two VAEs and the potential scalability issues for larger datasets. Furthermore, the choice of VAEs as the base model might limit the method's applicability to other model architectures. A discussion of these limitations would provide a more balanced and realistic assessment of the proposed method's practical value. The authors should also consider the sensitivity of their method to the choice of the confidence threshold and provide guidance on how to select this parameter in practice.

Finally, the experimental evaluation needs to be more comprehensive. While the authors evaluate their method on two datasets and two fairness metrics, this is not sufficient to demonstrate the generalizability of their findings. The authors should consider including a wider range of datasets with varying characteristics, such as different types of sensitive attributes and different levels of bias. They should also evaluate their method using a more comprehensive set of fairness metrics, including metrics that capture different aspects of fairness, such as equal opportunity and predictive parity. Furthermore, the authors should compare their method to a broader range of baselines, including more recent and state-of-the-art methods for fairness learning without sensitive attributes. This would provide a more robust and convincing evaluation of the proposed method's performance.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
