# PLLaVA: Parameter-efficient LLaVA Extension from Image to Video Understanding

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Vision-language pre-training has significantly elevated performance across a wide range of image-language applications. Yet, the pre-training process for video-related tasks demands exceptionally large computational and data resources, which hinders the progress of video-language models. This paper investigates a straightforward, highly efficient, and resource-light approach to adapting an existing image-language pre-trained model for dense video understanding. Our preliminary experiments reveal that directly fine-tuning pre-trained image-language models with multiple frames as inputs on video datasets leads to performance saturation or even a drop. Our further investigation reveals that it is largely attributed to the bias of learned high-norm visual features.  Motivated by this finding, we propose a simple but effective pooling strategy to smooth the feature distribution along the temporal dimension and thus reduce the dominant impacts from the extreme features. The new model is termed Pooling LLaVA, or PLLaVA in short.  PLLaVA achieves new state-of-the-art performance on modern benchmark datasets for both video question-answer and captioning tasks. Notably, on the recent popular Video ChatGPT benchmark, PLLaVA achieves a score of 3.25 out of 5 on average of five evaluated dimensions. On the latest multi-choice benchmark MVBench, PLLaVA achieves 58.1\% accuracy on average across 20 sub-tasks, 14.5\% higher than GPT4V (IG-VLM).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents PLLaVA, a parameter-efficient adaptation of LLaVA (Large Language and Vision Assistant) to extend its capabilities from image to video understanding. The authors highlight the challenges associated with directly fine-tuning image-language models on video data, such as performance degradation due to bias in visual features with high norms. To address these challenges, PLLaVA introduces an adaptive pooling strategy along the spatial and temporal dimensions to smooth feature distributions and reduce the influence of extreme feature values. This strategy aims to mitigate performance saturation commonly seen when directly using image models for video tasks. The authors also propose a post-training optimization technique to combine image-based and video-tuned model weights through weighted model merging of image-based VLM and video fine-tuned VLM. Experimental results show that PLLaVA achieves competitive or superior performance compared to existing models on several video-related benchmarks, including Video ChatGPT, MSVD-QA, MSRVTT-QA, MVBench, and ActivityNet-QA.

### Strengths
1. **Study of Feature Downsampling**: The authors provide a detailed study on the effect of feature downsampling in spatial and temporal dimensions, as well as model merging tuning. This could be valuable for practitioners who need to fine-tune related parameters for their specific applications.

2. **Post-Training Optimization**: The post-training optimization technique to mix weights from image and video domains is an interesting approach that helps retain image understanding while incorporating temporal dynamics. This allows PLLaVA to balance generalization capabilities between images and videos.

3. **Performance on Benchmarks**: The model shows measurable improvements over previous state-of-the-art models on multiple benchmarks. The improvements on MVBench are particularly notable, indicating PLLaVA's ability to better capture temporal dependencies, which is a key challenge in video-language understanding.

4. **Scalability**: The paper provides evidence that PLLaVA scales effectively across different model sizes (7B, 13B, 34B), maintaining or improving performance as parameters increase. This demonstrates its scalability without significant performance degradation.

### Weaknesses
1. **Presentation Issues**: The presentation of this work is difficult to follow, primarily due to several issues:

   1. **Concepts Without Explanation**: Several core concepts are introduced without sufficient explanation. For example, `AdaptStructurePooling`, which is crucial to the proposed approach, lacks a clear description of how it is implemented. The paper does not specify the exact pooling operation used (e.g., average, max, or learned pooling) or the kernel sizes and strides applied in the spatial and temporal dimensions. This lack of detail makes it hard to assess the computational cost and potential impact on feature representation.
   2. **Logical Gaps**: There are several instances where claims are made without adequate examination. For instance, from L320 to L340, the authors mention that spiky input makes the output of the Softmax function less stable. However, there is no clear explanation of why this leads to tokens with high norms, which is claimed to be the effect of having inputs with spiky distributions. The paper does not provide a mathematical or empirical justification for this claim, leaving the reader to speculate on the underlying mechanisms. Specifically, the connection between softmax instability and the emergence of dominant token embeddings is not clearly established.
   3. **Confounding Conclusions**: In Section 4.2 on pooling layer design, the authors state that "pooling along the temporal dimension always downgrades model performance." However, in the following paragraph, they assert that "pooling over more video frames improves model efficiency and makes it more robust to user inquiries." This appears either conflicting or lacking context, making it unclear whether pooling is recommended or not. The paper fails to clarify the specific conditions under which temporal pooling is detrimental versus beneficial, and does not provide a clear explanation of how the number of frames used for pooling affects the model's performance and robustness.

2. **Technical Novelty**: Pooling or downsampling is already a widely adopted technique in feature engineering for visual language models. While the detailed parameter tuning is useful, the paper lacks a clear differentiation of how these results contribute to new techniques or novel insights. The paper does not adequately explain how the specific combination of spatial and temporal pooling, along with the post-training optimization, constitutes a novel contribution beyond existing methods. The novelty of the approach is further diminished by the lack of a clear comparison with other adaptive pooling techniques.

3. **Complexity of Post-Training Optimization**: The process of tuning the mix ratio between image and video-trained weights is dataset-dependent, which could limit the practical adoption of the model. Providing more detailed guidance on selecting the mix ratio would make this approach more accessible to practitioners. The paper does not provide a systematic approach for determining the optimal mix ratio, and the lack of a clear methodology makes it difficult to reproduce the results or apply the technique to new datasets.

### Questions
1. **Post-Training Optimization Practicality**: Can the authors provide more detailed guidelines on how to effectively determine the mix ratio between image-based and video-trained weights during post-training optimization? This would help practitioners replicate the results without excessive trial and error.

2. **Data Quality Influence**: How does the quality of video-text datasets influence PLLaVA's performance? Would using higher-quality datasets or specific data augmentation strategies reduce issues related to dominant token norms and improve overall model performance.

### Soundness
3

### Presentation
2

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
This paper proposes an efficient approach to adapting pre-trained image-language models for dense video understanding. The authors conducted several initial studies to analyze the limitations of applying image-based MLLMs directly to video. Initial experiments revealed that simply fine-tuning these models on video data could lead to performance issues. To address this, the authors propose a temporal pooling strategy that smooths feature distribution across time, reducing the impact of extreme feature values. They also introduce a post-training model merging technique that mitigates forgetting in large language models during multi-modal fine-tuning due to low-quality video-text data. PLLaVA demonstrates strong performance across various video benchmarks.

### Strengths
The paper is well-written, covering the motivation, methodology, and experiments. The authors first analyze the issues and challenges in directly applying image MLLMs to video understanding and then propose a simple pooling operation and post-training strategy to address these issues. They also provide extensive ablation studies to demonstrate the effectiveness of the design. Finally, this approach shows strong performance across various benchmarks.

### Weaknesses
1. Comparing PLLaVA with the 4-Frame method in the initial failure analysis does not seem fair if PLLaVA uses 16 frames, which includes more video content to inform the answer. Recent studies show that using more frames can significantly improve the results [1][2]
2. The author mentioned that adding 249K data from VideoChat2 to train Video-ChatGPT does not continue to improve the model; on the contrary, the performance worsens. However, this outcome may also be influenced by the quality or distribution of the 249K data, as recent papers have shown that data quality and data mixture strategies can significantly impact model performance. Showing the performance of Video-ChatGPT trained on this 249K data alone could help verify this conclusion.
3. Lack the explanation of the x/y axis for Figure 2(a) and is there a direct correlation between norm distribution and model performance?
4. The post-optimization steps seem a bit counterintuitive. Does this mean that fine-tuning makes the alignment between vision and text even worse? How does this compare with unfreezing the LLM during fine-tuning?
5. Missing a few baseline methods such as [1][2][3]

### Questions
1. Could you elaborate more on how the 4 frames are selected? It is possible that the performance worsens as more data samples are trained due to a mismatch between the selected frames and the text content. This could lead to irrelevant frames being selected, which in turn results in increased training and bigger misalignment between vision and text.
2. Is there any training involved in the post-optimization process? If so, what training data is used?
3. What is the possible reason for the performance drop when the spatial pooling shape is 20 and its increase back when the shape is 24 in Figure 5(a)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on video undersdtanding. It analyzed current drawback for Vision-Language Model on video training and proposed to extend Vision-Language Model to support video with pooling operations. Experiments prove effectiveness on several video datasets.

### Strengths
1. This work proposes to extend current Vision-Language Model to support video, which is important and promising.
2. Extensive experiments on video-based benchmarks prove the effectiveness.
3. The overall method is simple and easy to follow.

### Weaknesses
It is interesting to find training with pooling can help video training. However, there could be some concerns regarding this paradigm that need to be solved. 

1. Whether this phenomenon is caused by the low-quality video training data? Because most of the visual tokens in video dataset could be redundant for simple video caption. A suggestion is to use high-quality data for model training, like LLaVA-Video [A] data. Specifically, the redundancy of visual tokens could be due to the high frame rate and minimal motion between consecutive frames in many video datasets. This could lead to the pooling operation effectively acting as a form of noise reduction, rather than a true feature aggregation. The authors should investigate this by using datasets with more dynamic scenes and lower frame rates to see if the same phenomenon persists.

2. Whether the pooling strategy harms the performance on image? It's good to find the authors counduct extensive experiments for video. However, the performance on image-based settings is still not clear. Considering add image-based experiments to make it more clear. The concern is that the pooling operation, optimized for temporal redundancy in videos, might lead to a loss of spatial detail when applied to images. This could be particularly problematic for tasks requiring fine-grained visual understanding. It is important to evaluate the impact of this pooling on image-based tasks, such as image classification or object detection, to ensure the method's general applicability. 

3. What's the baseline used in the experiments? Considering add experiments over the baseline to make the improvement more clear. The current experiments lack a clear comparison with a strong baseline that uses a similar architecture but without the pooling operation. This makes it difficult to isolate the specific contribution of the pooling strategy. It is crucial to include a baseline that is trained on the same data and with the same architecture, except for the pooling, to accurately measure the improvement. 

4. LLaVA-Next-Video 34b in Table 4 should also be added in Table 2 and 3.

### Questions
More studied are recommended to futher varified the proposed strategy. Please refer to the questions on the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The proposed approach PLLaVA adapts image vision-language models (VLMs) for video understanding tasks in a parameter-efficient way. The authors introduce an adaptive pooling strategy that smooths out feature distributions across the temporal dimension. This method termed Pooling LLaVA, prevents issues like dominant feature tokens, which can degrade model performance and leads to improvements in video-language tasks such as video question answering (QA) and video captioning. The authors test PLLaVA’s performance compared to state-of-the-art models across multiple benchmarks, including MVBench, VideoMME and Video-ChatGPT.

### Strengths
* The approach allows image-based VLMs to be adapted for video tasks using adaptive pooling. This avoids computation costs associated with training entirely new models for video data. 
* The analysis of pooling applied to spatial vs temporal dimensions (Sec. 4.2) is interesting. 
* The analysis demonstrating the issue of dominant tokens (high-norm visual feature tokens that skew performance during model fine-tuning) is novel and provides new insight for VLMs. However, the pooling approach concluded from this analysis is not new. 
* PLLaVA is tested on a wide range of video-related tasks and benchmarks. The approach is reported to perform reasonably well overall.

### Weaknesses
 * The novelty seems to be limited in the proposed approach since the main contribution is spatial pooling instead of temporal pooling and the application of LoRA weight aggregation. 
* The main source of improvement seems to be coming from fine-tuning the LLaVA-Next image model on videos. What are the technical improvements over the LLaVA-Next model? 
* Within the same parametric complexity models (e.g., 7B), the PPLaVA approach performs lower than the competing models like IG-VLM. 
* It is unclear how the model handles complex temporal dynamics inherent in video tasks. E.g., tasks that involve intricate motion understanding or multi-event reasoning. Can the authors provide specific examples of how PLLaVA handles long temporal dependencies in complex video scenes? 
* Although the empirical results show that pooling helps alleviate the problem of dominant tokens, the theoretical explanation behind why spatial pooling works is somewhat lacking. The provided justification is generic for spatial and temporal pooling, and the explaination on softmax distributions and sharp/balanced token distributions seems quite generic, not justifying why specifically spatial pooling is better. 
* The writing needs to be significantly improved. Several details are not clear. There are some typos as well: e.g., Fig. 4 "Adaptative" --> "Adaptive".
* Eq. 2, AdaptStructPooling is not properly defined. How is this pooling function implemented, how is it different from the pooling operations implemented in VideoChatGPT (I understand the only difference seems to be pooling on the spatial dimension)? Isn't the problem of dominant high-norm visual tokens already addressed by VideoChatGPT with their average pooling?
* Section 3.4, it is unclear how the Post Optimization approach differs from LoRA? Its also similar to distillation where a model weights are used to guide the adapted model weights (e.g., in continual learning). This needs to be clarified and clearly explain. 
* Can you elaborate on how PLLaVA’s pooling strategy impacts its ability to handle long-term temporal reasoning?Using the tests on tasks involving longer videos, kindly explain how did the performance compare to short clips?
* The pooling strategy is designed to alleviate the issue of dominant tokens, but how does it affect specific visual features? For example, does the pooling lead to a loss of finer details in complex scenes with many objects or fast-moving elements?
* Table 4, authors compare PLLaVA with its most similar counterpart, LLaVA-Next-Video, however its not clear specifically what changes are leading to the improvement over LLaVA-Next-Video? An ablation on this model will help clarify.

### Questions
* Eq. 2, AdaptStructPooling is not properly defined. How is this pooling function implemented, how is it different from the pooling operations implemented in VideoChatGPT (I understand the only difference seems to be pooling on the spatial dimension)? Isn't the problem of dominant high-norm visual tokens already addressed by VideoChatGPT with their average pooling?
* Section 3.4, it is unclear how the Post Optimization approach differs from LoRA? Its also similar to distillation where a model weights are used to guide the adapted model weights (e.g., in continual learning). This needs to be clarified and clearly explain. 
* Can you elaborate on how PLLaVA’s pooling strategy impacts its ability to handle long-term temporal reasoning?Using the tests on tasks involving longer videos, kindly explain how did the performance compare to short clips?
* The pooling strategy is designed to alleviate the issue of dominant tokens, but how does it affect specific visual features? For example, does the pooling lead to a loss of finer details in complex scenes with many objects or fast-moving elements?
* Table 4, authors compare PLLaVA with its most similar counterpart, LLaVA-Next-Video, however its not clear specifically what changes are leading to the improvement over LLaVA-Next-Video? An ablation on this model will help clarify.

### Soundness
2

### Presentation
2

### Contribution
2
