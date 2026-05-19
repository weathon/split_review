### Summary

This paper investigates the robustness of deep neural networks under varying degrees of distribution shifts. It highlights that models robust to moderate distribution shifts may not maintain robustness under higher degrees of shift and vice versa. The authors also examine the brittleness of large-scale pre-trained models, like CLIP, under different distribution shift degrees. The findings suggest that pre-trained models can be sensitive to even mild distribution shifts in downstream tasks. The paper advocates for a more comprehensive evaluation of OOD generalization across multiple degrees of distribution shifts to gain deeper insights and develop safer AI applications.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.

2. The motivation of the paper is sound and the problem of OOD generalization under different degrees of distribution shifts is interesting.

3. The paper conducts extensive experiments to validate the research questions.

### Weaknesses

#### Some Related Works

[1] Robust generalization under real-world distribution shifts.
[2] Spawrious: A systematic characterization of visual distribution shifts.

#### comment

1. The paper lacks novelty. The paper mainly investigates the robustness of ERM and DG methods under different distribution shifts, and the main finding is that the robustness to certain degrees of distribution shifts may tell little about the robustness to lower or higher degrees. However, this phenomenon is already observed in previous works [1,2]. The authors should provide a more detailed discussion of the differences between their work and these previous works, and highlight their unique contributions.

2. The paper lacks in-depth analysis of the research questions. For example, the paper concludes that the robustness of a model may be more brittle than we think. However, the paper does not provide a detailed analysis of the reasons behind this brittleness. What factors contribute to this phenomenon? What are the implications of this phenomenon for the development of robust models?

3. The paper lacks a discussion of the limitations of the study and future research directions.

### Suggestions

The paper would benefit significantly from a more rigorous comparison to existing literature, specifically addressing how the observed brittleness differs from previously documented phenomena. While the authors mention that their work considers a broader range of shift degrees, they need to articulate more precisely how this differs from the specific experimental setups and conclusions of works like [1,2]. For instance, do these prior works explicitly control for the degree of shift, or do they primarily focus on different types of shifts? A more detailed analysis of the experimental design differences is needed to justify the claim of novelty. Furthermore, the authors should clarify whether the observed non-monotonic behavior of ERM models across shift degrees has been previously reported, and if so, how their analysis provides new insights. A more thorough literature review and a more precise definition of the novelty of the contribution are crucial.

To strengthen the analysis, the authors should delve deeper into the underlying mechanisms causing the observed brittleness. The paper currently lacks a mechanistic explanation for why models trained on certain shifted datasets generalize poorly to others, even when the shifts are seemingly similar. For example, the authors could investigate the feature representations learned by the models under different shift degrees. Are there specific features that are robust to certain shifts but not others? Do the models learn different feature representations as the degree of shift increases? Techniques like feature visualization or ablation studies could be used to gain a better understanding of the learned representations. Furthermore, the authors should explore the role of spurious correlations in the training data and how these correlations might contribute to the observed brittleness. A more detailed analysis of the feature space and the learned representations is needed to provide a more complete picture of the phenomenon.

Finally, the paper should include a more thorough discussion of the limitations of the study and potential avenues for future research. The authors should acknowledge the limitations of their experimental setup, such as the specific datasets and types of distribution shifts considered. They should also discuss the potential impact of these limitations on the generalizability of their findings. For example, do the observed phenomena hold for other types of distribution shifts, such as those involving changes in style or texture? Furthermore, the authors should propose specific future research directions that could address the limitations of their study. This could include exploring new algorithms that are more robust to varying degrees of distribution shifts, or developing new evaluation metrics that can better capture the nuances of OOD generalization. A more detailed discussion of the limitations and future directions would significantly enhance the impact of the paper.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
