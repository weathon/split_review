### Summary

This paper proposes a video-to-video editing framework that supports multiple editing operations, such as object removal, addition, and modification. The framework consists of two stages: video-to-paragraph and paragraph-to-video. In the first stage, a video is converted into a paragraph, and in the second stage, the paragraph is used to edit the video. The authors propose a multi-granular spatiotemporal pooling strategy to generate well-structured paragraphs. The proposed framework can perform various video editing tasks, including removing, adding, and changing objects. The authors also collect a new dataset, VPLM, which contains video descriptions and object masks. The paper presents extensive experiments to validate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed framework is versatile and can perform various video editing tasks, including removing, adding, and changing objects.
- The authors propose a new dataset, VPLM, which contains video descriptions and object masks.
- The paper presents extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed framework is not novel. The framework mainly consists of two stages: video-to-paragraph and paragraph-to-video. The first stage is similar to Video-ChatGPT, and the second stage is similar to VideoComposer.
- The authors do not provide any failure cases of the proposed method. It is important to understand the limitations of the proposed method.
- The authors do not discuss the limitations of the proposed method.

### Suggestions

The paper would benefit from a more detailed analysis of the novelty of the proposed approach. While the authors claim a novel framework, the two-stage approach of video-to-paragraph and paragraph-to-video is not entirely new, and the paper needs to clearly articulate the specific differences and advantages of their method compared to existing approaches like Video-ChatGPT and VideoComposer. A more thorough discussion of the architectural differences, particularly in the video-to-paragraph stage, is needed. For example, the paper should elaborate on how the multi-granular spatiotemporal pooling strategy differs from other video captioning techniques and why it is particularly suitable for generating detailed paragraphs for video editing. Furthermore, the paper should provide a more in-depth comparison of the paragraph-to-video stage with VideoComposer, highlighting the specific mechanisms that enable more precise video generation based on the generated paragraphs. This would help to clarify the unique contributions of the proposed framework.

To address the lack of failure cases, the authors should include a more comprehensive analysis of the limitations of their method. This should include a detailed discussion of scenarios where the proposed framework might fail, such as complex scenes with multiple objects, occlusions, or unusual viewpoints. The paper should also discuss the limitations of the dataset, VPLM, and how these limitations might affect the performance of the proposed method. For example, the paper should analyze the types of video content included in the dataset and how well it represents real-world scenarios. Furthermore, the paper should discuss the potential biases in the dataset and how these biases might affect the generalizability of the proposed method. A more thorough analysis of these limitations would provide a more balanced and realistic assessment of the proposed framework.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of the computational cost of the framework, the sensitivity of the method to hyperparameter settings, and the potential for error accumulation during the video-to-paragraph and paragraph-to-video stages. The paper should also discuss the potential for the method to generate artifacts or inconsistencies in the edited videos. Furthermore, the paper should discuss the limitations of the evaluation metrics used in the paper and how these metrics might not fully capture the quality of the edited videos. A more thorough discussion of these limitations would provide a more complete and nuanced understanding of the proposed framework.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
