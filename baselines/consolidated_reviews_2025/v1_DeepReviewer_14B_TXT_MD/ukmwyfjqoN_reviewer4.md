### Summary

This paper proposes a recurrent bottleneck mixer network (ReBotNet) for real-time video enhancement. The authors combine the advantages of recurrent setup and bottleneck models to effectively capture temporal dependencies in the video while reducing the computational complexity and memory requirements. The experimental results on multiple video enhancement datasets show that the proposed method outperforms state-of-the-art methods in terms of computational efficiency while matching or outperforming them in terms of visual quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a novel and efficient architecture, ReBotNet, that achieves state-of-the-art results in real-time video enhancement.
2. The authors curate two new video enhancement datasets, PortraitVideo and FullVideo, which emulate practical video enhancement scenarios.
3. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only compare their method with a few previous works. It is suggested to compare with more recent methods to show the superiority of the proposed method.
2. The authors claim that the proposed method is able to perform real-time video enhancement. It is suggested to show the real frames processed by the proposed method to verify the claim.
3. There are some typos in the paper. For example, "the the" in line 346. The authors are suggested to carefully proofread the paper.

### Suggestions

The paper would benefit from a more thorough comparison against a wider range of state-of-the-art video enhancement techniques. While the current comparisons provide a baseline, the field is rapidly evolving, and including more recent methods, especially those that focus on similar low-latency scenarios, would strengthen the claims of the proposed method's superiority. Specifically, the authors should consider including methods that utilize transformer-based architectures or other advanced techniques that have shown promising results in recent literature. This would provide a more comprehensive evaluation of the proposed method's performance and its advantages over existing approaches. Furthermore, a more detailed analysis of the computational complexity and memory footprint of the proposed method compared to these recent methods would be beneficial.

To further validate the real-time performance claim, the authors should provide a more detailed analysis of the latency characteristics of their method. While the authors mention the inference time, a more granular breakdown of the processing time for each stage of the network would be beneficial. This would help to identify potential bottlenecks and provide a more comprehensive understanding of the method's real-time capabilities. Furthermore, it would be useful to show the method's performance on a variety of hardware platforms, including those with limited computational resources, to demonstrate its practical applicability. The inclusion of frame rate plots, as suggested, is a good start, but should be complemented with a more detailed analysis of the latency distribution and the impact of different input resolutions on the processing time.

Finally, the authors should ensure that the paper is thoroughly proofread to eliminate any typos or grammatical errors. While the identified typo is a minor issue, it can detract from the overall quality of the paper. A careful review of the text, including the figures and tables, is necessary to ensure that the paper is clear, concise, and free of errors. The authors should also ensure that all the claims made in the paper are supported by sufficient evidence and that the experimental results are presented in a clear and consistent manner. This will help to improve the credibility of the paper and make it more accessible to the wider research community.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
