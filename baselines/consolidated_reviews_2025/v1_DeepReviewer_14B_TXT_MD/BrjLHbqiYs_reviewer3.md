### Summary

This paper proposes a method to quantify the interactions between modalities in a semi-supervised setting, where only labeled unimodal data and unlabeled multimodal data are available. The authors derive lower and upper bounds on the amount of multimodal interactions using information-theoretic measures. The paper also discusses the implications of these bounds for estimating multimodal model performance, guiding data collection, and selecting appropriate multimodal models for various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a precise information-theoretic definition of multimodal interactions and derives lower and upper bounds to quantify these interactions in a semi-supervised setting. This theoretical analysis contributes to a deeper understanding of multimodal interactions.
2. The authors demonstrate how the theoretical results can be used to estimate multimodal model performance, guide data collection, and select appropriate multimodal models for various tasks. This has practical implications for multimodal learning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes finite sample spaces for features and labels, which may limit its applicability to real-world datasets that are often continuous and high-dimensional. The authors propose discretization as a solution, but the effectiveness of this approach depends on the chosen discretization method and the inherent structure of the data. The paper lacks a discussion on how the choice of discretization impacts the tightness of the derived bounds, and whether the bounds remain meaningful after discretization.
2. While the bounds are theoretically sound, their practical utility in guiding data collection and model selection needs further empirical validation. The paper does not provide clear guidelines on how to interpret the bounds in practice, and how the magnitude of the bounds relates to the actual benefits of using multimodal models. For example, it is unclear what range of values for the lower and upper bounds would indicate a strong synergy between modalities, and what range would suggest that a unimodal approach is sufficient. The paper also lacks a systematic evaluation of how the bounds perform across different datasets and tasks.

### Suggestions

The paper should provide a more detailed analysis of the impact of discretization on the derived bounds. Specifically, the authors should investigate how different discretization methods (e.g., equal-width, equal-frequency, k-means clustering) affect the tightness of the lower and upper bounds. It would be beneficial to include experiments that compare the bounds obtained using different discretization strategies and analyze the sensitivity of the bounds to the choice of discretization parameters. Furthermore, the authors should discuss the theoretical implications of discretization on the information-theoretic measures used to derive the bounds. For example, how does discretization affect the mutual information and other information-theoretic quantities used in the analysis? A more rigorous treatment of this aspect would strengthen the theoretical foundation of the proposed method.

To enhance the practical utility of the bounds, the authors should provide clear guidelines on how to interpret the bounds in the context of multimodal learning. This could involve defining ranges of values for the lower and upper bounds that indicate different levels of synergy between modalities. For instance, what range of values for the lower bound would suggest that a multimodal approach is likely to be beneficial, and what range would indicate that a unimodal approach is sufficient? The authors should also investigate the correlation between the magnitude of the bounds and the actual performance gains achieved by multimodal models. This could involve conducting experiments on a variety of datasets with different characteristics and analyzing how the bounds correlate with the improvement of multimodal models over unimodal baselines. Such an analysis would provide practitioners with a better understanding of how to use the bounds to guide data collection and model selection.

Finally, the paper should include a more comprehensive empirical evaluation of the proposed bounds across a wider range of datasets and tasks. This evaluation should include datasets with varying degrees of modality synergy and different types of multimodal interactions. The authors should also compare the performance of the proposed bounds with existing methods for quantifying multimodal interactions, if any exist. This would help to establish the advantages and limitations of the proposed approach and provide a more complete picture of its practical applicability. Furthermore, the authors should investigate the robustness of the bounds to different types of noise and perturbations in the data. This would help to assess the reliability of the bounds in real-world scenarios.

### Questions

1. How does the choice of discretization method affect the accuracy of the bounds, and are there recommended approaches for discretizing high-dimensional data?
2. What are the computational requirements for calculating the bounds, and how do they scale with the size of the dataset and the dimensionality of the modalities?
3. How does the proposed approach compare with existing methods for quantifying multimodal interactions in a semi-supervised setting, if any exist?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
