# PPLLaVA: Varied Video Sequence Understanding With Prompt Guidance

- Decision: Reject
- Avg Score: 4.80
- Scores: 6, 6, 3, 6, 3

## Abstract
The past year has witnessed the significant advancement of video-based large language models. However, the challenge of developing a unified model for both short and long video understanding remains unresolved. Most existing video LLMs cannot handle hour-long videos, while methods custom for long videos tend to be ineffective for shorter videos and images. In this paper, we identify the key issue as the redundant content in videos. To address this, we propose a novel pooling strategy that simultaneously achieves token compression and instruction-aware visual feature aggregation. Our model is termed Prompt-guided Pooling LLaVA, or PPLLaVA for short. Specifically, PPLLaVA consists of three core components: the CLIP-based visual-prompt alignment that extracts visual information relevant to the user's instructions, the prompt-guided pooling that compresses the visual sequence to arbitrary scales using convolution-style pooling, and the clip context extension designed for lengthy prompt common in visual dialogue. Moreover, our codebase also integrates the most advanced video Direct Preference Optimization (DPO) and visual interleave training. Extensive experiments have validated the performance of our model. With superior throughput and only 1024 visual context, PPLLaVA achieves better results on image benchmarks as a video LLM, while achieving state-of-the-art performance across various video benchmarks, excelling in tasks ranging from caption generation to multiple-choice questions, and handling video lengths from seconds to hours.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new model that can handle short and long videos with state-of-the-art performance under comparable model sizes. By using DPO's fine-tuning strategy, the proposed PPLLaVA is able to outperform selected baseline models. This is achieved by incorporating three components: the CLIP-based visual-prompt alignment that extracts visual information relevant to the user’s instructions, the prompt-guided pooling that compresses the visual sequence to arbitrary scales using convolution-style pooling, and the clip context extension designed for lengthy prompt common in visual dialogue.

### Strengths
1. The paper's motivation is interesting: applying pooling based on the text-frame similarity is reasonable. This is effective on removing redundant video frames conditioned on the user prompt input.
2. The author also proposes methods to handle long user inputs.
3. The final results are promising.

### Weaknesses
1. How the capability of CLIP affects the model performance is not discussed. Since the method relay on CLIP to remove redundant video frames, its accuracy could be the bottleneck of the method. Will a stronger text-image matching encoder further improve the model's performance? I believe adding this type pf discussion to the paper will make it stronger.

### Questions
Please refer to the weakness section: Will a stronger text-image matching encoder further improve the model's performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel pooling method to enhance video large language models (LLMs) by enabling token compression and prompt-aware feature extraction. The approach can be summarized as follows:
- Prompt-Relevant Visual Feature Extraction: The method begins by identifying visual features relevant to the prompt through a fine-grained visual-prompt alignment.
- 3D Token Compression: Leveraging prompt-vision alignment, the authors employ a 3D convolutional kernel to compress tokens to a specified 3D size, adjusting the output stride accordingly.
- Asymmetric Positional Embedding: To further enhance the model's capabilities, the authors introduce asymmetric positional embedding extensions to expand the capacity of text encoding.

The proposed method achieves a significant compression rate and supports both short and long token inputs. In comparison to Q-Former, the authors argue that their approach offers greater flexibility and adaptability.

Extensive experiments across a variety of datasets demonstrate promising performance improvements with this method.

### Strengths
- This paper begins with a clear analysis of video LLMs and highlights limitations in existing pooling techniques, effectively motivating the proposed approach.
- The proposed method, which comprises three key components, is technically sound and well-justified, addressing the identified challenges.
- The training strategy is particularly interesting, utilizing detailed video captions as proxies for video content and performing DPO with feedback from the language model serving as a reward signal.
- Experimental results demonstrate substantial performance improvements, supporting the effectiveness of the proposed approach.
- The paper includes detailed analysis, providing insights into the efficiency and performance gains of the model, with evidence suggesting that DPO plays a critical role in achieving the final results.
- The paper is well-written and easy to understand.

### Weaknesses
 - The diagrams could benefit from more detailed captions to enhance clarity. For example, Figure 2 requires additional context to quickly convey the relationship between [TOK] and the 3D blue rectangle, as this took some time to interpret.
- The fairness of the comparisons is questionable, as many previous works do not utilize DPO in their training. This difference may give the proposed method an advantage, making it challenging to assess its improvements solely based on the new pooling technique. Furthermore, the specific impact of DPO is not clearly isolated, making it difficult to determine the exact contribution of the proposed pooling method versus the DPO training strategy. The paper would benefit from a more rigorous ablation study that isolates the effects of DPO and the new pooling method.


### Questions
- Since the proposed method builds on the image-domain LLaVA, would it be feasible to adapt this approach to existing video LLMs directly? It would be interesting to understand any potential challenges or modifications required for integration with current video-specific models.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a novel method named PPLLAVA, which is based on Video LLM. my concerns are as below.
1. The authors claim that the method is for long video, however, I cannot see the comparison of performances when applying the method to long/short videos. Also, how to define "long video"? 1 hour long?
2. I think LLAVA is for images, instead of video. While if the authors want to apply LLAVA to videos, why not do like this: a. locate the related frames; b. VQA on frames. I cannot see the necessity of the three steps way.
3. The authors seems want to satisfy the user's needs/reply to user's questions. What if the questions are open-ended questions without an answer?
4. why we need "Prompt-Guided Pooling"? I cannot see the necessity of prompt here.

### Strengths
The paper is well-written, with clear pipeline, framework, and experimental results.

### Weaknesses
As can be found in the summary. I cannot see why the approach should be applied to videos instead of image-level applications. The authors claim that the method is for long video, however, I cannot see the comparison of performances when applying the method to long/short videos. Also, how to define "long video"? 1 hour long? I think LLAVA is for images, instead of video. While if the authors want to apply LLAVA to videos, why not do like this: a. locate the related frames; b. VQA on frames. I cannot see the necessity of the three steps way. The authors seems want to satisfy the user's needs/reply to user's questions. What if the questions are open-ended questions without an answer? why we need "Prompt-Guided Pooling"? I cannot see the necessity of prompt here.

### Questions
Will the method also be applied to image-level applications? is video necessary?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed PPLLAVA, a video-LLM based on a prompt-guide pooling strategy. The core idea is to conduct text query/prompt-dependent pooling for video features before putting them into LLM. The authors conduct extensive experiments to show the effectiveness of the proposed method. The proposed PPLLAVA outperforms other training-free/training-based video-LLM at a similar model scale.

### Strengths
(1) this paper conducts extensive experiments to show the effectiveness of the proposed methods.

(2) pooling redundant tokens based on visual-text similarity is an efficient solution to capture query-related information in a video with large redundancy.

(3) The design of extending the CLIP content window is smart enough to adapt CLIP to a longer context with minimal modification.

### Weaknesses
(1) one thing I'm a bit confused about is the video captioning setting when adapting this prompt-guided pooling strategy. As the caption prompts are not as diverse as that question answering, holistic captioning should be affected unless the user is querying a specific object-related caption. I would suggest some experiments on video caption benchmarks, e.g. activitynet caption or newer DREAM-1K, to further support the strong video understanding ability claim.

(2) it seems the paper missed some related baseline methods, see LongVA [1], and Kangaroo [2]. It should be helpful to include a more comprehensive analysis and comparison with those methods, even if some of them achieve better performance on some datasets. 

(3) My other big concern is the novelty side. While I understand this paper did a good job of validating their idea/design with extensive experiments and ablations, comparing some zero-shot baseline like PLLAVA/LLaVA-NeXT-Video, the big boost of the performance might come from fine-tuning on 1.3M multimodal data and the prompt-guided pooling seems a bit incremental from my personal perspective. So I am a bit worried that if we conduct the same level of training with a stronger LLM backbone that has a long content window, the model can learn this query-related attention itself, so the proposed core idea, prompt-guided pooling, seems sub-optimal. 

(4) A potential solution might be to fine-tune zero methods that conduct their token merging idea with the same data and show the performance difference.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel approach to video understanding by leveraging prompt guidance to enhance the performance of video language models (VLMs). The methodology focuses on reducing video redundancy and extracting key content to enhance the performance of VLMs. It uses CLIP-based visual-prompt alignment to extract relevant visual information and compresses visual sequences using convolution-style pooling. Direct Preference Optimization (DPO) was also used to improve its performance. In experiments, PPLLaVA demonstrated good results on both long and short video benchmarks, and achieves over an 80% compression rate.

### Strengths
1. The paper introduces methods for video understanding by leveraging prompt guidance through the use of CLIP-based visual-prompt alignment and convolution-style pooling.
2. PPLLaVA shows versatility by performing well on both long and short video benchmarks, demonstrating robust performance for varied video sequence understanding. This adaptability is crucial for handling diverse video lengths and complexities, making it a robust solution for varied video sequence understanding5.
3. PPLLaVA uses Direct Preference Optimization (DPO) to reduce hallucinations in video-based dialogue and also applies CLIP Context Extension to expand text encoding capacity.

### Weaknesses
1. PPLLaVA does not show leading results compared to some training-free compression methods like SLOWFAST-LLAVA[1], on benchmarks such as MSVD and MSRVTT. Specifically, while the method demonstrates good performance on some benchmarks, its performance on MSVD and MSRVTT is not competitive with SLOWFAST-LLAVA, indicating a potential weakness in handling certain types of video data or tasks.
2. The use of Direct Preference Optimization (DPO) and Proximal Policy Optimization (PPO) lacks innovation. Also, LLaVA-Next-Video also achieve great accuracy improvements using above methods, but this paper does not highlight any unique advantages of these methods within PPLLaVA. The application of DPO and PPO, while beneficial, does not represent a novel contribution, and the paper fails to articulate any specific advantages or modifications of these methods within the PPLLaVA framework compared to existing implementations in other models.

### Questions
1. The method seems similar to the involution kernel[1]. What are the  differences between the two? 
2. Have any ablation studies been conducted using regular 3D convolution for pooling instead of prompt-guided methods? 
3. In Table 5, why is the context length for average pooling set to 576 instead of 1024?
4. Can PPLLaVA  extend to multimodal **generative** models?

[1] Involution: Inverting the Inherence of Convolution for Visual Recognition

### Soundness
3

### Presentation
3

### Contribution
2
