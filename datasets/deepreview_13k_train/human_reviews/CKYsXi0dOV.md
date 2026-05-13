# BLIP-3-Video: You Only Need 32 Tokens to Represent a Video Even in VLMs

- Decision: Reject
- Scores: 5, 8, 6, 6

## Abstract
We present xGen-MM-Vid (\modelname): a multimodal language model for videos, particularly designed to efficiently capture temporal information over multiple frames. \modelname takes advantage of the `temporal encoder' in addition to the conventional visual tokenizer, which maps a sequence of tokens over multiple frames into a compact set of visual tokens. This enables \modelname to use much fewer visual tokens than its competing models (e.g., 32 vs. 4608 tokens). We explore different types of temporal encoders, including learnable spatio-temporal pooling as well as sequential models like Token Turing Machines. We experimentally confirm that \modelname obtains video question-answering accuracies comparable to much larger state-of-the-art models (e.g., 34B), while being much smaller (i.e., 4B) and more efficient by using fewer visual tokens. The project website is at {\small \url{https://www.salesforceairesearch.html}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents BLIP-3-Video, which introduces a "temporal encoder" alongside a conventional visual tokenizer, allowing it to significantly reduce visual tokens (32 tokens compared to thousands in other models). The study explored various temporal encoders, including learnable spatio-temporal pooling and sequential models like token turning machines (TTM). Detailed experiments showed that different encoder types had a noticeable impact on performance, particularly in handling complex video scenarios. Experimental results show that BLIP-3-Video achieved video question-answering accuracies comparable to much larger state-of-the-art models while being smaller and more efficient.

### Strengths
1. An impressive tradeoff between efficiency and accuracy on the MSVD-QA benchmark.
2. Extensive explorations on temporal encoders to reduce visual tokens.
3. The paper is well written and easy to follow.

### Weaknesses
1. Novelty: The primary weakness is the insufficient novelty. As detailed in Section 2.2, the only improvements to TTM include (1) time-stamped positional encodings and (2) a 'grouped' TTM temporal encoder. These minor changes, while potentially beneficial, do not represent a significant conceptual leap or a fundamentally new approach to temporal modeling. The time-stamped positional encodings, for instance, are a straightforward extension of existing positional encoding techniques, and the 'grouped' TTM, while showing performance gains, is essentially a parameterization change rather than a novel architectural component. The core mechanism of TTM remains largely unchanged, thus limiting the overall novelty of the work.

2. Evaluation Benchmarks: The evaluated benchmarks are unconvincing for assessing Video LMMs. The model was only evaluated on MSVD-QA, MSRVTT-QA, ActivityNet-QA, TGIF-QA, and NExT-QA, which are not so ideal for testing LMMs. These benchmarks primarily focus on relatively simple video understanding tasks, such as question answering about object presence or basic actions. They do not adequately assess the model's ability to handle more complex video reasoning, such as understanding temporal relationships, event causality, or nuanced interactions. The authors may consider newer benchmarks like VideoMME and MVBench, which are proposed for assessing Video LMMs, to provide a more comprehensive evaluation of the model's capabilities.

### Questions
1. What novel designs does this method introduce compared to TTM? Are there ablation studies for these designs?

2. The model utilizes the VideoChatGPT instruction set. Why hasn't it been evaluated on that benchmark?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces BLIP-3-Video, a multimodal vision language model which demonstrates strong performance on video understanding with high token accuracy. BLIP-3-Video uses as few as 16~32 tokens to encode an entire video sequence, which is highly efficient to other video VLMs, enabled by the incorporation of a temporal encoder. BLIP-3-Video achieves competitive accuracy on various video question-answering benchmarks while having smaller model parameters.

### Strengths
- The temporal encoder which aggregates visual tokens across frames in a highly efficient manner results in computational efficiency of training the model.
- Extensive ablation study in the temporal encoder design validates the design choice while also demonstrating the flexibility in the design of temporal encoder. 
- Competitive performance on various video question-answering benchmarks, despite its smaller size.

### Weaknesses
 - The model proposed in the paper utilizes 8 frames per video which are uniformly sampled. This approach might not work for tasks that inherently require more than 8 frames to understand the video. If this method could scale up, an explanation of why that might be would be helpful. Specifically, the paper does not address the potential limitations of uniform sampling, which may miss crucial temporal details in videos with complex or rapidly changing scenes. For instance, in a video of a complex action like a gymnastics routine, uniformly sampling 8 frames might not capture the critical moments of the routine, such as the take-off, mid-air movements, or landing. This could lead to a loss of important information that is necessary for accurate video understanding.
- The experiments of the paper focuses on video question-answering benchmarks only, and this limited experimentation may not capture the model's ability in other video-based tasks. Further evaluation on other video tasks, such as temporal understanding would demonstrate the applicability of this approach to more general and diverse video-related tasks. The lack of evaluation on tasks that require fine-grained temporal understanding, such as action recognition or temporal segmentation, is a significant limitation. These tasks would more thoroughly test the model's ability to capture and utilize temporal information, which is critical for many real-world applications.

### Questions
- The (video part of the) training of this model is on video captioning data and video question-answering datasets. If the downstream task were to change to a more complex task, like temporal reasoning, would the model require more tokens or would 16~32 still be sufficient? i.e. is there enough visual information encoded in the 16~32 tokens?
- In addition, if the downstream task requires remembering multiple details and nuanced events over a long diverse scenario, how would this approach perform? Is there a built-in mechanism that prevents information loss during token pooling?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an efficient Video LLM, coined as BLIP-3-Video, by incorporating extra modules to transform dense video tokens into sparse tokens (e.g., # can be 32). Specifically, the authors use a sequential transformer (so called token turing machine) on top of frame-wise image tokens and perceiver-resampler to produce limited 32 tokens. Diverse video QA benchmarks show the competitive performance of BLIP-3-Video on video question answering tasks. The authors also test the captioning ability of BLIP-3-Video.

### Strengths
This paper investigates an important topic, how to efficiently & effectively understand videos by LLMs, which is underexplored so far. This paper proposes the BLIP-3-Video to understand videos with just 32 tokens (in LLMs) based on Phi-3, and it outperforms both parameter-heavy or visual-token-heavy models (as shown in Fig 1) on QA and captioning benchmarks. Additionally, this paper presents a compelling finding (somewhat): a video can be effectively represented by just 32 tokens in LLMs for QA and captioning tasks. I think this research line is promising and can benefit several downstreaming tasks, e.g., captioning for text-to-video generation.

### Weaknesses
Although this is overall a good paper, several concerns are here:
1. The presentation of the main method (Sec 2.2) somwhat presents confusion: Does BLIP-3-Video both use spatio-temporal attentional pooling and TTM? Is there a perceive resampler before temporal encoder in BLIP-3-Video (cannot be infered from Figure 2)?

2. Compressing a video into 32 tokens is a compelling and exciting idea. However, I am worried that spatial-temporal details will be missing through compression, which is crucial for some detailed reasoning in LLMs. More evaluation of BLIP-3-Video on diverse tasks beyond captioning and MCQ are encouraged.
(also, as the compression is not text query guided, the compression is solely dominated by the visual information itself. That is to say, 32 tokens per a video are fixed under different text query, which might not be appropriate in general)

3. Relating with the weakness 1, extra modules introduced besides the visual encoder (SigLIP) and LLM sound too complicated. If I understand correctly, there are a perceiver-resampler and a temporal encoder (attention pooling or TTM). My idea is naive and simple, can we just finetune a perceiver-resampler in BLIP-3 into a temporal encoder, rather than just compressing tokens per frame? Given the strong performance of cross attention layers in the perceiver resampler, this seems to be a missing but promising ablation study in this paper.

### Questions
1. Can one BLIP-3-Video model produce 32 and 128 tokens on demand as a hyper parameter? Or they are different models trained individually?

2. What does text encoder in Fig 2 mean? The text tokenizer?

### Soundness
3

### Presentation
2

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
The paper introduces BLIP-3-Video, a novel multimodal language model designed for video understanding that efficiently captures temporal information across frames. A key innovation is the integration of a 'temporal encoder' that maps a sequence of tokens from multiple frames into a compact set of visual tokens, allowing BLIP-3-Video to operate with significantly fewer visual tokens compared to its competitors. The model explores various temporal encoders, including learnable spatio-temporal pooling and sequential models like Token Turing Machines. Experiments demonstrate that BLIP-3-Video achieves comparable video question-answering accuracies to much larger models, while being more efficient and smaller in size due to its reduced token usage. The paper also details the model's architecture, training recipe, and experimental results, highlighting the effectiveness of the temporal encoder in representing videos for question-answering tasks with a small number of tokens.

### Strengths
- **Originality**: It introduces an innovative temporal encoder that significantly reduces the number of visual tokens needed to represent videos, offering a new approach to efficiency in video understanding models.

- **Quality**: The model is thoroughly evaluated against state-of-the-art benchmarks, demonstrating competitive performance. The ablation studies are providing insightful analyses into the model's components.

- **Clarity**: The paper is well-organized, with clear explanations and visual aids that effectively convey complex information, making the technical content accessible to readers.

- **Significance**: BLIP-3-Video's efficiency in handling video data with fewer resources.

### Weaknesses
 - **Diversity of Datasets**: The experiments primarily rely on a limited set of public benchmarks for evaluation. Expanding the evaluation to include a more diverse range of benchmarks, particularly those with varying lengths and complexities of videos, could provide a more comprehensive assessment of the model's generalizability and robustness. The current benchmarks, while standard, do not fully capture the nuances of real-world video understanding tasks, especially those involving longer temporal dependencies and more complex scene dynamics. For instance, the model's performance on datasets with significant camera motion, occlusions, or rapid scene changes remains unclear.

- **Scalability Analysis**: While the paper demonstrates the model's efficiency, there is a lack of analysis on how the model scales with increasing video length and complexity. Future work could benefit from exploring the model's performance as it processes longer videos, which is crucial for real-world applications. The paper does not provide sufficient detail on the computational cost associated with processing longer videos, such as the increase in memory usage or inference time. Furthermore, the impact of longer videos on the performance of the temporal encoder, particularly its ability to maintain relevant information over extended periods, is not explored.

- **Comparison with State-of-the-Art**: Although comparisons are made with other models, the paper could benefit from a more detailed analysis comparing the trade-offs between BLIP-3-Video and the state-of-the-art models in terms of accuracy, computational resources, and inference time. The current comparisons are limited to overall accuracy metrics, without a thorough analysis of the computational efficiency, such as FLOPs or memory footprint, and inference latency. A more granular analysis of these trade-offs would be beneficial for understanding the practical implications of using BLIP-3-Video in resource-constrained environments.

- **Implementation Details**: Some aspects of the model's implementation, such as the specific choices made in the architecture of the temporal encoder, could be elaborated upon with more technical depth. This additional detail would aid other researchers in understanding the design decisions and potentially replicating or improving upon them. The paper lacks a detailed description of the specific parameters and configurations used in the temporal encoder, such as the number of layers, hidden units, and activation functions. This lack of detail makes it difficult to fully understand the model's inner workings and replicate the results.

### Questions
1. **Temporal Encoder Generalization**: A smaller number of visual tokens is particularly important for understanding longer videos. However, this paper only tested on a few simple short video benchmarks. Please provide test results on video benchmarks of different lengths and scenarios, such as VideoMME, MVBench, etc.

2. **Scalability Concerns**: How does the model's performance and efficiency scale with longer videos, and have you observed any limitations in terms of the number of frames the model can effectively process?

3. **Model Interpretability**: The paper mentions the use of different types of temporal encoders. Are there any plans to provide insights into how these encoders make decisions?

4. **Comparison with Other Efficient Models**: How does BLIP-3-Video compare with other recent models that also focus on efficiency, such as those employing knowledge distillation or sparse attention mechanisms? Could the authors provide some insights into the trade-offs involved? Please provide persuasive evidence from experimental studies.

5. **Novelty**: Compared to LLaMA-VID, where is the core novelty of this paper? Although the experimental results show that 32 tokens achieved better performance on four short video benchmarks, this standard will change with different video lengths, video scenarios, and the complexity of question answering. The scalability and generalizability of this method are questionable. Perhaps a more effective mechanism for accommodating more frames and selecting key information for video question answering from a large number of visual tokens is worth exploring, rather than determining the specific numerical value of a visually overfitted token on a few benchmarks. Similar architectures have been explored enough in a series of works such as Video-LLaVA, LLaVA-VID, LLaVA-NEXT, and so on.

### Soundness
2

### Presentation
2

### Contribution
1
