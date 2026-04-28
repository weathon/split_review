# Interpolating Video-LLMs:  Toward Longer-sequence LMMs in a Training-free Manner

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Advances in Large Language Models (LLMs) have inspired various strategies for integrating video modalities. 
A key approach is Video-LLMs, which incorporate an optimizable interface linking sophisticated video encoders to LLMs. 
However, due to computation and data limitations, existing Video-LLMs are typically pre-trained to process only short videos, limiting their broader application for understanding longer video content. Additionally, fine-tuning Video-LLMs to handle longer videos is cost-prohibitive.
Consequently, it is essential to explore the interpolation of Video-LLMs under a completely training-free setting. In this paper, we first identify the primary challenges in interpolating Video-LLMs: \raisebox{-1.1pt}{\ding[1.1]{182\relax}} the video encoder and modality alignment projector are fixed, preventing the integration of additional frames into Video-LLMs, and \raisebox{-1.1pt}{\ding[1.1]{183\relax}} the LLM backbone is limited in its content length capabilities, which complicates the processing of an increased number of video tokens.
To address these challenges, we propose an \textbf{INT}er\textbf{P}olation method for Video-LLMs (\intp-Video-LLMs). We introduce a video token rearrangement technique that circumvents limitations imposed by the fixed video encoder and alignment projector. Furthermore, we introduce a training-free LLM context window extension method to enable Video-LLMs to understand a correspondingly increased number of visual tokens. 
We analyze the deployment costs of \intp-Video-LLM, and find its efficiency bottleneck is on its KV cache cost. Accordingly, we introduce a training-free KV-cache compression mechanism that reduces memory overhead during inference. 
\intp-VideoLLM not only supports the processing of longer video sequences but also optimizes memory usage during inference---all achieved without the need for additional training. 
In practice, whereas pre-trained Video-LLaVA~\citep{lin2023video} models are configured to process just 8 frames, \intp~allows these models to comprehend 32 frames.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the task of adapting a Video-LLM, pre-trained on short videos, to handle long videos without additional training. It identifies key challenges related to the fixed video encoder, modality projector, and the limited context window size of the LLM. To address these issues, the authors propose a video token rearrangement technique and an extension method for the LLM's context window to accommodate a greater number of visual tokens. Additionally, they introduce a KV-cache compression mechanism to minimize memory usage during inference. These innovations enable the proposed INTP-Video-LLaVA model to process videos with up to 32 frames.

### Strengths
1. **Innovation and Relevance:** The paper introduces a novel training-free approach to extend the input video length compatibility for Video-LLMs. This contribution is significant and addresses a timely issue in the field. 

2. **Clarity and Coherence:** The paper is commendably well-structured and it is easy to follow.

3. **Insightful Analysis:** The paper offers a thorough explanation of the challenges associated with video encoder limitations, LLM context window size constraints, and KV-cache management during inference in current Video-LLMs. This analysis is particularly valuable for the community, providing insights that can guide future research and development.

### Weaknesses
1. The applicability of the proposed training-free techniques across a range of Video-LLMs is a critical aspect to assess. The paper, however, presents experimental results solely for Video-LLaVA. It is recommended that the authors expand their experiments to include additional Video-LLMs to demonstrate the broader applicability of the techniques.

2. The paper lacks certain crucial experiments. An ablation study examining the impact of the video token rearrangement techniques and the efficacy of every design choice of the RoPE interpolation methods is recommended. Such studies would provide a more comprehensive understanding of the contributions of these specific aspects to the overall performance.

### Questions
My primary concern is the scope of the experimental section. It is recommended that the authors expand their experimental analysis to encompass a variety of Video-LLMs and conduct ablation studies for each design decision. This would offer a more thorough understanding of the findings for the readers. Please find more details in Weaknesses.

### Soundness
3

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
5

### Summary
Overall, this papre presents INTP, an training-free method aiming to improve video LMMs on longer video evaluation. In general, two strategies are proposed in this paper:
(1) With a fixed length video encoder, it sends alternative frames to bypass the frame length limit for the video encoder. With this, it allows up to 128 frames as input for the `INTP`-VideoLLaVA.
(2) It uses off-the-shelf NTK extrapolation to allow the short context LLM to allow more frames.

Though this paper is technically solid, it does not provide enough contribution to this field, and sadly I cannot recommend acceptance to this paper in its current form. Please see the weaknesses part for more details and try to improve it.

### Strengths
1. This paper is well-written.
2. The experiments are abundant and solid, providing results from 8 to 128 frames.
3. The presentation is well.

### Weaknesses
1. For performance, the improvement is marginal. Though we should not expect huge improvements on training-free methods, VideoLLaVA is already a very poor performer

2. NTK interpolation is an off-the-shelf strategy for LLM context extension (almost default for most). Therefore, the part discussing rope and NTK seems a bit trivial with limited contributions. Similarly, the strategy for video encoder is SPECIFIC to video models with a video encoder, which is not common for now.

3. As the extension has already gone to 128 frames, I would advise to evaluate on some longer video benchmarks, e.g. VideoMME-Long, MLVU, LongVideoBench. Maybe this may better emphasize the effect of the method.

### Questions
Please see my weaknesses.

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the problem of long sequence LLMs. The authors point out that the challenge lies in : video encoder and modality alignment projector are fixed, preventing the integration of additional frames into Video-LLMs, and the LLM backbone is limited in its content length capabilities, which complicates the processing of an increased number of video tokens. The authors introduce a video token rearrangement technique that circumvents limitations imposed by the fixed video encoder and alignment projector. Furthermore, a training-free LLM context window extension method is proposed to enable Video-LLMs to understand a correspondingly increased number of visual tokens.

### Strengths
1. The paper proposes a video token rearrangement technique that bypasses the restrictions imposed by the fixed video encoder and alignment projector. 
2. A training-free Video-LLM context window extension method is proposed to ensure that the interpolated Video-LLM can handle any number of video frames.
3. The presentations are good.

### Weaknesses
1. The chosed baselines are not complete. For example, PLLaVA, Video-LLaMA 2, Flash-VStream are not included.
2. Table 2 should include the #frames of each model.
3. Some others works about LLM sequence extension should be discussed and analysised. For example, LongVA: Long Context Transfer from Language to Vision.
4. Lack some benchmark evaluations: VideoMME, MoVQA, MVBench, etc.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a interpolation method for extending Video-LLMs to process longer video sequences under training-free setting, called INTP-Video-LLMs. The approach leverages a video token rearrangement technique and a training-free LLM context window extension method to bypass the limitations of existing Video-LLMs, which typically only process short video clips. Furthermore, a training-free key-value (KV) cache compression mechanism is introduced to optimize memory usage during inference. The proposed INTP-Video-LLMs can comprehend longer video sequences (up to 32 frames) without additional training, and experimental results indicate that this approach provides a significant improvement in both video processing capabilities and inference efficiency.

### Strengths
- The motivation for the proposed INTP-Video-LLM is clear and fundamental. The Introduction is well-crafted, making it easy to grasp the paper's concept.
- The proposed methods allow existing Video-LLMs to process longer video (i.e. more video frames) **in a training-free manner**, effectively addressing computational constraints.
- The paper comprehensively considers and analyzes whether the proposed **Video Tokens Rearrangement** and **Interpolating Video-LLM Backbone** will lead to additional computational overhead.
- The **memory optimization** via KV-cache compression ensures that extended video sequences can be processed with minimal memory overhead, making the approach feasible for practical deployment.

### Weaknesses
 - The paper points out the existing limitations in the temporal consistency of encoders and projectors, but the description of the video token rearrangement method is unclear. It is not explained why rearrangement would help maintain consistency, and a more thorough explanation is needed.
- Near Figure 2, at line 234, it describes “we obtain two subsequences, $X_{v,1}$ and $X_{v,1}$,” where $X_{v,1}$ appears twice. Is this a typographical error?
- In Section 3.4.1, the authors analyze the inference cost and propose 2-bit quantization of the KV cache to reduce storage overhead during inference. However, the potential performance degradation due to quantization is not discussed in detail. It would be beneficial to include an analysis of the trade-offs between reduced storage and potential accuracy loss.
- In the ablation study (Section 4.3), the authors compare the performance of using different numbers of frames in Video QA tasks. However, it is unclear what the individual contributions of each module are to the final performance. A detailed breakdown of the impact of each module would provide more insight into their effectiveness.

### Questions
Q1. The authors perform 2-bit quantization of the KV cache to reduce storage overhead during the inference process of the video LLM. However, does quantizing the stored KV result in performance degradation?

Q2. Could you provide a more detailed description of the video tokens rearrangement process (e.g., in the form of pseudocode) as well as an analysis of the effectiveness of this method?

### Soundness
3

### Presentation
2

### Contribution
2
