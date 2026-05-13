# Multimodal Instruction Tuning with Hybrid State Space Models

- Decision: Reject
- Scores: 3, 3, 5, 3, 3

## Abstract
Handling lengthy context is crucial for enhancing the recognition and understanding capabilities of multimodal large language models (MLLMs) in applications such as processing high-resolution images or high frame rate videos. The rise in image resolution and frame rate substantially increases computational demands due to the increased number of input tokens. This challenge is further exacerbated by the quadratic complexity with respect to sequence length of the self-attention mechanism. Most prior works either pre-train models with long contexts, overlooking the efficiency problem, or attempt to reduce the context length via downsampling (e.g., identify the key image patches or frames) to decrease the context length, which may result in information loss. To circumvent this issue while keeping the remarkable effectiveness of MLLMs, we propose a novel approach using a hybrid transformer-MAMBA model to efficiently handle long contexts in multimodal applications. Our multimodal model can effectively process long context input exceeding 100k tokens, outperforming existing models across various benchmarks. Remarkably, our model enhances inference efficiency for high-resolution images and high-frame-rate videos by about 4 times compared to current models, with efficiency gains increasing as image resolution or video frames rise. Furthermore, our model is the first to be trained on low-resolution images or low-frame-rate videos while being capable of inference on high-resolution images and high-frame-rate videos, offering flexibility for inference in diverse scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a multi-modal Large Language Model (LLM) framework that integrates a hybrid state space model called Jamba. The framework is designed to handle multi-modal tasks involving language and vision inputs, such as images and videos. The overall structure is similar to the LLaVA (Large Language and Vision Assistant) architecture, consisting of a vision encoder, an MLP adapter, and an LLM network. In this case, the LLM backbone is JamBA, as opposed to LLaMA in LLaVA.

### Strengths
The paper is well-written and easy to understand, making it accessible to a wide audience.

The use of State Space Models (SSMs) to reduce inference costs is a reasonable and potentially beneficial approach.

### Weaknesses
1. The reviewer is concerned with the novelty of this paper. As far as the reviewer can tell, the only contribution and modification made in this paper is replacing a decoder-only LLM with a state-space LLM. The claimed advantage of MMJAMBA, such as computational efficiency and the "train-on-short-infer-on-long" method are rooted in the state-space LLM, not from the novel design of MMJAMBA. Other than the different choice of LMM, everything else remains canonical to standard LMMs. For example, an MLP adapter, multi-stage training, existing training datasets and benchmarks, etc. There are limited contributions or insights to make stat-space LMM work better.

2. The comparison of MMJamba to other 13B LMMs is unfair. JAMBA LLM is a 52B MoE model with 12B active. It's performance would fall between a 52B and a 12B model.

3. The performance advantage of "train-on-short-infer-on-long" is sort of overclaimed. The performance goes up on some benchmarks indeed, but goes down or remains about the same on others. Overall, the reviewer would consider it as "maintaining similar performances across different resolutions".

### Questions
Why use Jamba instead of pure SSM structure.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MMJAMBA, a multimodal large language model (MLLM) designed to efficiently process long context inputs, such as high-resolution images and high-frame-rate videos. It addresses the computational challenges posed by the quadratic complexity of self-attention in transformers by integrating Mamba layers, which are part of a hybrid state space model architecture. The authors propose a "train-on-short-infer-on-long" strategy, which allows the model to be trained on low-resolution inputs for efficiency and perform inference on high-resolution inputs for enhanced performance. The model compares favorably against other SoTA methods in image and video understanding, both in terms of computation and performance.

### Strengths
1. The hybrid transformer-Mamba architecture effectively manages long context inputs, significantly improving inference efficiency while maintaining competitive accuracy.
1.  The "train-on-short-infer-on-long" method reduces training complexity and computational cost, making it practical for training large LMMs and on high-resolution images and long videos.
1. The model demonstrates adaptability to various resolutions and frame rates, showcasing flexibility in handling diverse multimodal tasks.

### Weaknesses
1. The novelty is really limited. I don’t see anything particularly unique in the architecture or training methods. The use of a hybrid state space model, while effective for long sequences, is not a novel application in itself, especially given its prior use in other sequence modeling tasks. The specific adaptation to multimodal data, while a contribution, lacks a significant architectural innovation that would differentiate it from existing approaches. The 'train-on-short-inference-on-long' strategy, while practically useful, is also not a fundamentally new training paradigm.
2. The presentation of results in Table is a bit hasty, with no necessary bolding, equalization, etc. The lack of clear visual cues in the tables makes it difficult to quickly assess the significance of the results. Specifically, without bolding the best results or providing a clear indication of statistical significance, the reader has to spend more time to interpret the data. This lack of attention to detail in presentation detracts from the overall impact of the experimental results.
3. Ablation study is missing. Without an ablation study, it's difficult to understand the contribution of each component of the proposed method. For example, it is not clear how much the hybrid state space model contributes compared to other sequence models, or how the 'train-on-short-inference-on-long' strategy affects the performance compared to standard training. This lack of analysis makes it hard to isolate the key factors driving the observed improvements.

### Questions
1. In terms of writing, Tab 7 is never referenced in the paper. Also, what's the different points the authors want to make between the "Resolution" and "Training Recipe" subsections of Sec 6 Analysis?

1. Any comparisons with existing LMMs with state-space LMMs?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a MLLM that leverages a hybrid transformer-MAMBA architecture to efficiently process long input contexts. The contributions of this study are: it introduces the MMJAMBA model optimized for lengthy contexts from high-resolution inputs, a "train-on-short-infer-on-long" strategy for improved training and inference efficiency. Experimental validation demonstrates stronger performance against both open-source and proprietary models.

### Strengths
The use of a SSM architecture to enhance the modeling efficiency for long contexts and tokens in MLLM is intuitively motivated.

Overall, the experimental section of the study appears to be thorough and solid, both in terms of content and effort. It also confirms that the proposed model indeed improves both efficiency and performance.

### Weaknesses
1. Problems with resolution. Typically, we use the dynamic resolution as the key to address such limitations. Since dynamic resolution not only addresses the limitation of increasing resolution, it can also handle any aspect ratio of the image. This paper just employs the AnyRes as an engineering trick to improve the performance. The authors fail to acknowledge that dynamic resolution methods, such as those used in Qwen2-VL, offer a more principled approach by adapting the input resolution during processing, which inherently handles varying aspect ratios and reduces computational overhead. The use of AnyRes, while effective, is presented as a core contribution rather than an implementation detail, which is misleading.

2. This paper claims their motivation originates from the long-video understanding. While their experiments in Table 3 did not support their claims. The authors did not present any advantages of their method of inference speed or performances in long video understanding. For example, VideoMME has a long-video split, the comparison should be conducted on this split. Meanwhile, Figure 2 just shows the scalability of the proposed model on handling increasing resolution, there is no such proof that supports the proposed model is more suitable for video understanding, because this paper has nothing to do with temporal aggregation or cross-frame gathering. In addition, according to Figure 2, this model has a similar inference latency with LLaVA-NeXt-13B while the resolution is in the range of [672,2688]. The paper lacks a clear demonstration of how the proposed architecture is specifically advantageous for long-video processing. The experiments do not address the core challenges of long-range temporal dependencies and efficient processing of extended video sequences. The comparison with LLaVA-NeXt-13B in Figure 2, showing similar latency, further weakens the claim of improved efficiency for video understanding.

3. In Table 7, the authors show that their model can outperform their baseline models of LLaVA-NeXt-7B and LLaVA-NeXt-13B. In my opinion, with the resolution increasing from 1344 to 2688, their baseline models show poor performances because of memory limitation. As for the proposed model, similarly, there is an obvious performance drop as increasing the resolution from 672 to 1344 and from 1344 to 2688. The authors' claim should refer to their model can improve the performance by increasing the resolution. Therefore, it's unconvincing that the proposed model can address limitations in increasing the resolution problem. The performance degradation of the proposed model with increasing resolution, as observed in Table 7, directly contradicts the claim that it effectively addresses resolution limitations. The fact that both the baseline and the proposed model exhibit performance drops at higher resolutions suggests that the issue is not fundamentally resolved, but rather mitigated to some extent. The authors should have focused on a more robust solution rather than just pushing the limits of resolution.

4. The method section just follows the common practice in the community. I can not find any novelty.

### Questions
1. Do the authors intend to open-source the code and meta-data?

2. In Figure 2, why did the authors only compare with LLAVA-NEXT? Have other models been compared as well?

3. How is the resolution on the X-axis of Figure 2 calculated?

4. Have the authors compared efficiency in video modeling? It seems that the reviewer has only seen a comparison of efficiency in image modeling.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a multimodal instruction tuned model utilizing the hybrid state space model  to effectively process long context input brought up by the higher resolutions of the images and more frames of the videos, thereby enhancing multimodal visual comprehension and recognition. A train-on-short-inference-on-long strategy is also introduced. Extensive experiments on 12 benchmarks validate the efficacy of the proposed method.

### Strengths
1. The topic on processing high-resolution images or high frame rate videos is crucial, which makes the motivation necessary.
2. Extensive experiments are conducted to validate the efficacy of the proposed method.
3.  "Train-Short-Inference-Long" is interesting.

### Weaknesses
1. The novelty is really limited. I don’t see anything particularly unique in the architecture or training methods.
2. The presentation of results in Table is a bit hasty, with no necessary bolding, equalization, etc.
3. Ablation study is missing.

### Questions
1. My main concern is the novelty of the method in this paper. Can the authors elaborate on the crucial improvements in the architecture or training method?
2. The necessary ablation experiments are required.

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
This paper aims to address the limitations of existing vision-language models in computational burdens from increasing resolution and video frame rates. They find some problems with VLMs in training long-vision token sequences. The paper does not reveal why multimodal instruction tuning specifically requires such hybrid model architectures between Transformers and state space models. They did present some good experimental results on image and video zero-shot understanding benchmarks. However, the reviewer can not find the technical novelty of this paper. Please see the comments below:

### Strengths
This paper shows some good results compared with baseline models. This paper contains both image and video understanding results, which provides a better evaluation compared with existing models.

### Weaknesses
1. Problems with resolution. Typically, we use the dynamic resolution as the key to address such limitations. Since dynamic resolution not only addresses the limitation of increasing resolution, it can also handle any aspect ratio of the image. This paper just employs the AnyRes as an engineering trick to improve the performance.

2. This paper claims their motivation originates from the long-video understanding. While their experiments in Table 3 did not support their claims. The authors did not present any advantages of their method of inference speed or performances in long video understanding. For example, VideoMME has a long-video split, the comparison should be conducted on this split. Meanwhile, Figure 2 just shows the scalability of the proposed model on handling increasing resolution, there is no such proof that supports the proposed model is more suitable for video understanding, because this paper has nothing to do with temporal aggregation or cross-frame gathering. In addition, according to Figure 2, this model has a similar inference latency with LLaVA-NeXt-13B while the resolution is in the range of [672,2688]. 

3. In Table 7, the authors show that their model can outperform their baseline models of LLaVA-NeXt-7B and LLaVA-NeXt-13B. In my opinion, with the resolution increasing from 1344 to 2688, their baseline models show poor performances because of memory limitation. As for the proposed model, similarly, there is an obvious performance drop as increasing the resolution from 672 to 1344 and from 1344 to 2688. The authors' claim should refer to their model can improve the performance by increasing the resolution. Therefore, it's unconvincing that the proposed model can address limitations in increasing the resolution problem.

4. The method section just follows the common practice in the community. I can not find any novelty.

### Questions
1. Does this paper take the LLaVA-NeXt-13B as the baseline and naively re-train the models with additional SSM blocks?

2. Performance improvement by dropping the last block of vision transformers (Page 15 Appendix A.1) seems important to the proposed model. It's a trick to improve the performance while it's not ablated in the experiments.

3. Should we use the SSM for increasing resolution or video frame rate? I think dynamic resolution in Qwen2-VL is powerful enough and their corresponding 13B model shows much better results compared with this paper.

### Soundness
2

### Presentation
1

### Contribution
1
