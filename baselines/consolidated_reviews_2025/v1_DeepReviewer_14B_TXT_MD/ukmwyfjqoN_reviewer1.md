### Summary

In this paper, the authors propose an efficient video enhancement framework, named Recurrent Bottleneck Mixer Network (ReBotNet), for practical applications such as video calls and live streaming. ReBotNet employs a dual-branch architecture to learn spatiotemporal features and improve temporal consistency. The authors also curate two new datasets, PortraitVideo and FullVideo, to evaluate the proposed method. Experimental results demonstrate that ReBotNet outperforms existing approaches with lower computations, reduced memory requirements, and faster inference time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a novel and efficient architecture, ReBotNet, that achieves state-of-the-art results in real-time video enhancement.
2. ReBotNet outperforms existing approaches with lower computations, reduced memory requirements, and faster inference time.
3. The authors curate two new video enhancement datasets, PortraitVideo and FullVideo, which emulate practical video enhancement scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only compare their method with a few previous works. It is suggested to compare with more recent methods to show the superiority of the proposed method.
2. The authors claim that the proposed method is able to perform real-time video enhancement. It is suggested to show the real frames processed by the proposed method to verify the claim.
3. There are some typos in the paper. For example, "the the" in line 346. The authors are suggested to carefully proofread the paper.

### Suggestions

The paper would benefit from a more comprehensive comparison against state-of-the-art video enhancement techniques. While the authors demonstrate improvements over the selected baselines, the field is rapidly evolving, and inclusion of more recent methods, particularly those leveraging advanced architectures or training strategies, would strengthen the claims of superiority. Specifically, the comparison should include methods that focus on similar low-latency scenarios, as this is a key aspect of the proposed approach. A more thorough analysis of the trade-offs between performance and computational cost would also be valuable, perhaps by including a wider range of methods with varying complexities. This would help to better contextualize the contribution of ReBotNet within the broader landscape of video enhancement research.

To further validate the real-time performance claim, the authors should provide a more detailed analysis of the latency characteristics of their method. While the authors mention the inference time, a more granular breakdown of the processing time for each stage of the network would be beneficial. This would help to identify potential bottlenecks and provide a more comprehensive understanding of the method's real-time capabilities. Furthermore, it would be useful to show the method's performance on a variety of hardware platforms, including those with limited computational resources, to demonstrate its practical applicability. The inclusion of frame rate plots, as suggested, is a good start, but should be complemented with a more detailed analysis of the latency distribution and the impact of different input resolutions on the processing time.

Finally, the authors should ensure that the paper is thoroughly proofread to eliminate any typos or grammatical errors. While the identified typo is a minor issue, it can detract from the overall quality of the paper. A careful review of the text, including the figures and tables, is necessary to ensure that the paper is clear, concise, and free of errors. The authors should also ensure that all the claims made in the paper are supported by sufficient evidence and that the experimental results are presented in a clear and consistent manner. This will help to improve the credibility of the paper and make it more accessible to the wider research community.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
