### Summary

This paper proposes a method called APPLe to address the issue of visual variance within a category by constructing multiple prompts for each class, which are referred to as class prototypes. The authors introduce an adaptive attention mechanism to assign higher scores to representative prototypes and lower scores to flawed ones. Additionally, a prototype decorrelation loss is designed to reduce the probability of co-occurrence of multiple prototypes. Experimental results demonstrate that APPLe can consistently improve performance on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for constructing multiple prompts for each class is not clearly articulated. The authors should explain why a single prototype is insufficient to capture the visual variance within a category. Specifically, the paper lacks a clear explanation of how the proposed method addresses the inherent ambiguity in visual representations, and why a single prototype would be inadequate for this. The paper should elaborate on the limitations of a single prototype and provide a more detailed analysis of the scenarios where multiple prototypes are necessary.
2. The proposed method lacks novelty. The authors should clearly explain the differences between the proposed method and existing approaches. It is unclear how the adaptive attention mechanism and prototype decorrelation loss contribute to improved performance compared to existing methods. The paper needs to provide a more detailed comparison with related work, highlighting the unique aspects of the proposed method and its advantages over existing techniques. The authors should also discuss the limitations of their approach and potential areas for improvement.
3. The authors should provide a more detailed analysis of the experimental results to demonstrate the effectiveness of the proposed method. The paper should include a more in-depth analysis of the experimental results, including a discussion of the statistical significance of the observed improvements. The paper should also provide a more detailed analysis of the performance of the proposed method on different datasets and under different experimental conditions. The paper should also discuss the limitations of the experimental evaluation and potential areas for improvement.

### Suggestions

The paper needs to provide a more detailed explanation of the motivation behind using multiple prompts for each class. The authors should clearly articulate why a single prototype is insufficient to capture the visual variance within a category. For example, they could discuss the limitations of a single prototype in representing the diverse appearances of objects within the same class, such as variations in pose, lighting, and background. The authors should also provide a more detailed analysis of the scenarios where multiple prototypes are necessary and how they address the inherent ambiguity in visual representations. This could include a discussion of the types of visual variance that are captured by each prototype and how the adaptive attention mechanism assigns weights to different prototypes based on the input image. Furthermore, the authors should provide a more detailed analysis of the limitations of a single prototype and how their approach overcomes these limitations.

The paper should also provide a more detailed comparison with existing approaches, highlighting the unique aspects of the proposed method and its advantages over existing techniques. The authors should clearly explain how the adaptive attention mechanism and prototype decorrelation loss contribute to improved performance. For example, they could discuss how the adaptive attention mechanism differs from other attention mechanisms used in vision-language models and how the prototype decorrelation loss differs from other regularization techniques. The authors should also discuss the limitations of their approach and potential areas for improvement. This could include a discussion of the computational cost of the proposed method and how it compares to other methods. The authors should also discuss the potential for extending their method to other vision-language tasks and datasets.

The paper should include a more detailed analysis of the experimental results, including a discussion of the statistical significance of the observed improvements. The authors should also provide a more detailed analysis of the performance of the proposed method on different datasets and under different experimental conditions. This could include a discussion of the performance of the proposed method on different types of images and how it handles different levels of visual variance. The authors should also discuss the limitations of the experimental evaluation and potential areas for improvement. This could include a discussion of the potential for future work to further improve the performance of the proposed method.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
