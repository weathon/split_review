# ZoomVLM: A Tuning-Free Framework for Efficient Video Understanding via Adaptive Zooming in Vision-Language Models

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Recent advances in vision-language models (VLMs) have led to impressive progress in video understanding. However, despite their promising performance, existing state-of-the-art (SOTA) solutions require an excessive number of tokens (e.g., up to 6,272 tokens in the Llava-OneVision model) to represent input videos, leading to a non-negligible bottleneck in inference efficiency. Motivated by findings in human perception, where individuals first focus on high-level overviews and then zoom into specific areas for detailed information, we hypothesize that a similar approach can enhance the inference efficiency of VLMs by reducing the number of tokens needed to represent videos. Based on this hypothesis, we propose ZoomVLM, a tuning-free, plug-and-play efficient video processing framework for video VLMs. ZoomVLM first generates an overview of the entire video and then adaptively zooms in and out on different parts based on the content being generated. Our key insight is that the attention distributions in the Large Language Model (LLM) within the VLM can provide sensible guidance on where to focus (by allocating more tokens) and where to discard (by dropping tokens) during inference. Specifically, ZoomVLM integrates two key components: (1) a Video Overview Augmenter, which enables cost-effective high-level understanding by augmenting downsampled video overview with a few high-resolution keyframes; and (2) an Adaptive Token Adjustment, which predicts the importance of different video parts in the upcoming generation process and adjusts the number of tokens allocated to each part according to their importance. Extensive experiments and ablation studies across two challenging open-ended video understanding benchmarks and four models validate that ZoomVLM effectively improves inference efficiency by reducing the number of tokens and boosting throughput in terms of the number of generated tokens per second without degradation in achievable accuracy. Specifically, when applying ZoomVLM to Llava-Next-Video-7B-DPO, ZoomVLM achieves a 30\% higher token generation rate with a 0.259 improvement in the Video Detail Description score.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents ZoomVLM, a novel framework aimed at enhancing the efficiency of vision-language models (VLMs) for video understanding. The authors address a critical issue: existing VLMs, particularly SOTA models like Llava-OneVision, require a high number of tokens, leading to slow inference and computational bottlenecks. Inspired by human perception strategies--where people focus on general overviews and selectively zoom into specific areas for details--ZoomVLM proposes a more selective token allocation approach to reduce token usage while maintaining performance.

### Strengths
1. Tuning-free and plug-and-play: Being tuning-free and plug-and-play, ZoomVLM can be seamlessly integrated with existing VLMs without the need for extensive modifications or retraining, facilitating broader adoption.
2. Efficient Token Usage. Selectively allocating tokens to the most important parts of a video is an intuitive motivation.
3. Well-structured presentation. The presentation of this paper is clear and easy to understand.

### Weaknesses
1. The motivation is somewhat unclear. The generation quality of Video Overview Augmenter is crucial, as it determines which parts of the video should be emphasized or ignored. However, due to spatial pooling and temporal sampling, the quality may be suboptimal, and this has not been validated through ablation studies.
2. There are concerns about its practicality. First, the Video Overview Augmenter increases inference costs for the same question compared to other methods. Second, the proposed method only achieves comparable performance compared to its counterparts.
3. Lack sufficient experimental support. It would be beneficial to include evaluations on other challenging video benchmarks, such as long video datasets, to validate effectiveness and enable a more comprehensive comparison.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on efficient video processing framework for video VLMs. It proposes a pipeline to first generates a high-level overview of the entire video and then adaptively zooms in on specific parts based on the content being generated. Experiments show effectiveness on the video detailed description dataset.

### Strengths
1. The efficient video compression for VLM is promising and useful for practical usage.
2. The course-to-fine design for video understanding is interesting and seems to be useful in caption.
3. Overall, the writing is clear and easy to follow.

### Weaknesses
1. From Figure 2, the proposed ZoomVLM utilizes LLM twice for image-level and token level selection. But the efficency in Table 1 is seems better for vanilla manner in Token/sec. Is the efficiency mainly from reduction in video tokens? Considering provide the whole inference time and time spent on each component (video overview generation, token adjustment, etc.) for clear comparison. It could be better to compare other metrics like memory usage or FLOPs.
2. The evalution in Video description is far from enough. The authors are recommended to conduct experiments on VideoMME [A] and EgoSchema [B], which could be more close to real-life scenes. Of course, it's better to provide some analysis or limitation on different benchmarks.
3. One of the main drawback in current pipeline could be the multi-round QA, which is more useful in practical applications. Because the Vanilla or Slowfast do no need to generate the token again for different round. Are the authors have any solutions or ideas to this tasks or potential optimizations for repeated queries on the same video? 
4. Because the video overview augmenter and adaptive token adjustment are all target to reduce reduent tokens, why not only keep the adaptive token adjustment with larger reduction rate? The authors are recommended to discuss any potential synergies or trade-offs between the two approaches.

[A] "Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis", arXiv:2405.21075, 2024

[B] "Egoschema: A diagnostic benchmark for very long-form video language understanding", NeurIPS, 2023

### Questions
My main concern focuses on the experiment part. Current experiments are not enought to support the general efficient framework for VLM.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes ZoomVLM, a tuning-free, plug-and-play efficient video processing framework for video VLMs. ZoomVLM integrates two key components: (1) a Video Overview Augmenter, which enables cost-effective high-level understanding by augmenting downsampled video overview with a few high-resolution keyframes; and (2) an Adaptive Token Adjustment, which predicts the importance of different video parts in the upcoming generation process and adjusts the number of tokens allocated to each part according to their importance.

The contributions are summarized as follows:
1. propose a tuning-free, plug-and-play efficient video processing pipeline for VLMs, dubbed ZoomVLM.
2. ZoomVLM integrates two key components to efficiently select necessary information by leveraging the attention distribution within the VLM: Video Overview Augmenter and Adaptive Token Adjustment.
3. Extensive experiments demonstrate significant improvements.

### Strengths
1. This paper observes a bottleneck in the practical application of current video VLMs, namely the excessive number of visual tokens, which severely affects inference speed. The paper attempts to address this issue with a tune-free approach, which is a good starting point.
2. The ablation experiments are quite comprehensive.

### Weaknesses
1. There should be a section that analyzes the efficiency of the method proposed in the paper, including how many tokens have been reduced, which KV caches can be reused or recalculated, the theoretical speedup ratio, etc. It would be best to include pseudo code for inference.
2. The results for Vanilla in Table 1 are significantly lower than the official results for the LLaVA-NeXT-Video series, and the authors do not explain the reason in the paper. Is it due to resolution, retraining, or some other factor, and the paper's results also fail to surpass the official results for the LLaVA-NeXT-Video series. This makes it difficult to believe in the effectiveness of the methods presented in the paper.
3. The paper only includes two benchmarks and llava series models, and more benchmarks and models could be added to enhance the credibility and trustworthiness of the method proposed, as perceived by the readers.

### Questions
1. The paper mentions resuming the generation process, but video tokens will undergo corresponding changes, such as concatenating $P_C$. In this scenario, can KV caches still be reused, and will the computational load increase?
2. In Equation 12, duplicating tokens does not introduce additional information; why would it be effective?

### Soundness
1

### Presentation
2

### Contribution
2
