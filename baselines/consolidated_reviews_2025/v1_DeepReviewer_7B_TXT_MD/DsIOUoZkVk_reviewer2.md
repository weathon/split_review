### Summary

This paper studies the problem of inferring the similarity between unpaired modalities using contrastive learning. The authors provide a theoretical analysis of multimodal contrastive learning and show that directly comparing representations of unpaired modalities can recover the same likelihood ratio as directly comparing the representations. They also introduce a Monte Carlo approximation method to improve the practical application of these insights. The paper validates its theoretical claims through experiments on both synthetic and real-world datasets, including language-conditioned reinforcement learning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel theoretical foundation for understanding and utilizing unpaired multimodal data, which is a significant contribution to the field of multimodal learning.

2. The authors present a clear and well-structured argument, supported by rigorous mathematical derivations.

3. The paper includes a variety of experiments that effectively validate the theoretical claims, demonstrating the practical applicability of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a theoretical analysis, it lacks a detailed discussion on the practical implications of the assumptions made. Specifically, the assumption of conditional independence given the intermediate modality (Assumption 1) is not thoroughly examined in terms of its real-world validity and potential impact on the results. The paper should include a more in-depth analysis of scenarios where this assumption might be violated and how such violations could affect the performance of the proposed method. For instance, in complex real-world datasets, the relationship between modalities might be highly non-linear and conditional dependencies could be significant, potentially leading to inaccurate similarity measures. The authors should provide concrete examples of such scenarios and discuss the limitations of their approach in these cases.

2. The paper could benefit from a more detailed comparison with existing methods for multimodal learning, particularly those that address unpaired data. The current comparison is limited, and a more thorough analysis would help to clarify the advantages and disadvantages of the proposed approach. For example, the paper should discuss how the proposed method compares to techniques that use adversarial training or other forms of representation alignment for unpaired data. A more comprehensive comparison would also include a discussion of the computational complexity and scalability of the proposed method compared to existing approaches, which is crucial for practical applications.

### Suggestions

The paper would significantly benefit from a more rigorous exploration of the conditional independence assumption (Assumption 1). The authors should delve deeper into the scenarios where this assumption is likely to hold and where it is likely to fail. For instance, in a multimodal setting involving text, images, and audio, the relationship between the image and the text might be conditional on the specific object being described, and the text and audio descriptions might also be conditionally dependent given the object. The authors should provide concrete examples of such scenarios and discuss how violations of this assumption could lead to inaccurate similarity measures. Furthermore, the paper should explore potential methods for relaxing this assumption or adapting the proposed approach to handle more complex dependencies between modalities. This could involve incorporating techniques from causal inference or developing more sophisticated models that can capture conditional dependencies. A more thorough analysis of this assumption is crucial for understanding the practical applicability of the proposed method.

In addition to a more detailed analysis of the conditional independence assumption, the paper should include a more comprehensive comparison with existing methods for multimodal learning, particularly those that address unpaired data. The current comparison is limited and does not fully clarify the advantages and disadvantages of the proposed approach. The authors should discuss how their method compares to techniques that use adversarial training or other forms of representation alignment for unpaired data. This comparison should include a discussion of the computational complexity and scalability of the proposed method compared to existing approaches. For example, the authors could compare their method to techniques that use contrastive learning with unpaired data, highlighting the differences in terms of the learned representations and the computational cost. A more thorough comparison would also include a discussion of the robustness of the proposed method to different types of data and task settings, as well as its sensitivity to hyperparameter choices. This would help to better position the proposed method within the broader landscape of multimodal learning and provide a more complete understanding of its strengths and weaknesses.

Finally, the paper should provide more practical guidance on how to apply the proposed method in real-world scenarios. The authors should discuss how to assess the validity of the conditional independence assumption in practice and provide recommendations for how to adapt the method when this assumption is violated. This could involve developing diagnostic tools or providing guidelines for selecting appropriate hyperparameters. The paper should also discuss the limitations of the proposed method and provide recommendations for future research. For example, the authors could discuss the potential for extending their method to handle more than three modalities or to incorporate other types of data, such as sequential data. This would help to make the paper more useful for practitioners and encourage further research in this area.

### Questions

1. How sensitive is the proposed method to violations of the conditional independence assumption (Assumption 1)? Could you provide more insights into the practical implications of this assumption and how it might affect the performance of the method in real-world scenarios?

2. Could you elaborate on the computational complexity of the proposed Monte Carlo approximation method? How does it scale with the size of the dataset and the dimensionality of the representations?

### Rating

6

### Confidence

3

**********
