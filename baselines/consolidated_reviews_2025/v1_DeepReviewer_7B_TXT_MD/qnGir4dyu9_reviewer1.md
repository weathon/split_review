### Summary

This paper proposes a video editing framework, which consists of two stages: video-to-paragraph and paragraph-to-video. In the first stage, a video is converted into a paragraph, and in the second stage, the paragraph is used for video editing. The authors propose a multi-granular spatiotemporal pooling strategy to generate well-structured paragraphs. The proposed framework can perform various video editing tasks, including removing, adding, and changing objects. The authors also collect a new dataset, VPLM, which contains video descriptions and object masks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed framework is versatile and can perform various video editing tasks, including removing, adding, and changing objects.
2. The authors propose a new dataset, VPLM, which contains video descriptions and object masks. The dataset will be helpful for future research.
3. The authors conduct extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed framework is not novel. The framework mainly consists of two stages: video-to-paragraph and paragraph-to-video. The first stage is similar to Video-ChatGPT, and the second stage is similar to VideoComposer.
2. The authors do not provide any failure cases of the proposed method. It is important to understand the limitations of the proposed method.
3. The authors do not discuss the limitations of the proposed method.

### Suggestions

The paper's primary weakness lies in its lack of novelty, as the proposed framework closely resembles existing approaches. While the authors combine a video-to-paragraph stage with a paragraph-to-video stage, both components are conceptually similar to existing methods like Video-ChatGPT and VideoComposer, respectively. The video-to-paragraph stage, which uses a multi-granular spatiotemporal pooling strategy, needs more justification for its novelty compared to existing video captioning techniques. The paper should clearly articulate the specific differences and advantages of their approach over existing methods, rather than simply stating that it is different. For example, the authors should provide a detailed comparison of their pooling strategy with other pooling methods used in video captioning, highlighting the unique aspects of their approach and why it is better suited for generating detailed paragraphs. Furthermore, the paper should discuss the specific challenges of video captioning that their method addresses and how it overcomes these challenges compared to existing techniques.

In addition to the lack of novelty, the paper lacks a thorough discussion of its limitations. The authors should provide a detailed analysis of the scenarios where the proposed method might fail, including specific examples of failure cases. This analysis should go beyond simply stating that the method might fail in complex scenes or with ambiguous descriptions. The authors should discuss the potential sources of error in each stage of the framework, such as the video-to-paragraph stage and the paragraph-to-video stage, and how these errors might propagate through the pipeline. For example, the authors should discuss how the multi-granular spatiotemporal pooling strategy might fail to capture subtle details in the video, or how the paragraph-to-video stage might fail to accurately translate the generated paragraph into a realistic video. This discussion should also include an analysis of the limitations of the dataset, VPLM, and how these limitations might affect the performance of the proposed method. The authors should also discuss the computational cost of their method and how it compares to existing approaches.

Finally, the paper should provide a more detailed analysis of the experimental results. While the authors present quantitative results, they should also provide a qualitative analysis of the generated paragraphs and videos. This analysis should include a discussion of the strengths and weaknesses of the generated outputs, and how they compare to the ground truth. The authors should also discuss the impact of different parameters on the performance of the proposed method, and how these parameters can be tuned to achieve optimal results. For example, the authors should discuss the impact of the number of superpixels used in the multi-granular spatiotemporal pooling strategy, or the impact of the size of the object masks on the quality of the generated videos. This analysis should also include a discussion of the limitations of the evaluation metrics used in the paper, and how these metrics might not fully capture the quality of the generated outputs. The authors should also discuss the potential for future work, such as extending the framework to handle more complex video editing tasks or incorporating user feedback into the generation process.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

4

**********
