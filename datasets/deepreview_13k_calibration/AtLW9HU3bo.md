# Discovering the question-critical moments: Towards building event-aware multi-modal large language models for complex video question answering

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Recently, Multi-modal Large Language Models (MLLM) have demonstrated impressive capabilities in image-language reasoning tasks like Image Question Answering. However, naively transferring them to complex Video Question Answering (VideoQA) tasks suffers from unsatisfactory causal-temporal reasoning capabilities. Existing methods simply concatenate the uniformly sampled frame representations to obtain the video representation, which either results in a quite large number of visual tokens and is thus resource-demanding, or is distracted by the redundancy of question-irrelevant contents. In light of this, we introduce E-STR, extending MLLM to be Event-aware for Spatial-Temporal Reasoning in complex VideoQA tasks. Specifically, we propose a differentiable question-critical keyframes retriever to adaptively select the question-critical moments in the video serving as the key event for spatial-temporal reasoning, and a general context encoder to encode the unselected parts for preserving the general contexts of the video. To facilitate the acquisition of spatial-temporal representations, we also incorporate lightweight adapters within the frozen image encoder. Extensive experiments on three large-scale benchmarks, including NExT-QA, Causal-VidQA, and STAR, all of which are notable for complex causal-temporal reasoning within long videos containing multiple objects and events, show that our method achieves better performance than existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Existing Multimodal Large Language Models (MLLM) still suffer from complex video question answering (VideoQA) tasks. Currently, they typically uniformly sample sparse frames and simply concatenate them to represent the entire video. However, as long and complex videos typically contain multiple events, the sparse frame sampling strategy may lead to a deficiency of essential information. To this end, they propose an event-aware spatial-temporal reasoning method E-STR. It retrieves the question-critical event before feeding the visual features into the frozen LLMs.

### Strengths
+ The motivation is very clear and natural. Meanwhile, the proposed method is also very straightforward.

### Weaknesses
 + Although the proposed method can improve the performance of baseline InstructBLIP, it is still hard to demonstrate the results are same as the initial motivation. For example, the sampled events are really important ones.

+ The main contribution of this paper is proposing an event-aware spatial-temporal reasoning strategy for VideoQA. It is still unclear how the proposed framework (cf. Figure 3) can realize "event-aware" reasoning.

+ Based on the results in Table 4, the simple concat-32 baseline already achieves 71.1 in @All metric, which already beat all the listed state-of-the-art baselines in Table 1 (InstructBLIP with 69.5). It would be better to have more explanations about the results? Otherwise, it seems that the compared baselines are not strong enough.

### Questions
Based on the results in Table 4, the simple concat-32 baseline already achieves 71.1 in @All metric, which already beat all the listed state-of-the-art baselines in Table 1 (InstructBLIP with 69.5). It would be better to have more explanations about the results? Otherwise, it seems that the compared baselines are not strong enough.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to address the task of complex video question answering. To reduce the complexity of previous methods, this paper introduces a two-step approach. Specifically, it first designs a moment adapter to retrieve the question-related frames. Then, it associates corresponding critical information with the general contexts of the unselected part to predict the answer. Besides, it also incorporates lightweight adapters within the frozen image encoder. Experiments are conducted on three datasets.

### Strengths
1. The motivation of this paper is straightforward and easy to follow.
2. This paper is well-written and easy to read.
3. Supplementary file is provided.

### Weaknesses
1. The novelty is limited. This paper proposes a two-step approach which first retrieves the question-related moment and then achieves reasoning. This process is similar to the coarse-to-fine approach in many temporal grounding methods, for example, but not limited to, “Scanning Only Once: An End-to-end Framework for Fast Temporal Grounding in Long Videos”. Since the motivation is straightforward, the newly introduced technical designs are not new and not exciting. Therefore, I believe that the novelty is incremental.

2. Missing some relevant references. Since the main approach is coarse-to-fine, the authors should add and compare more related methods to discuss their differences.

3. Experiments are not fair. This paper proposes a two-step approach, directly comparing it with other one-step approaches is unfair. Although this work brings large improvements, it also leads to higher running time and GPU cost. Therefore, the authors should re-implement other two-step approaches from other tasks into the current task for comparison.

4. The efficiency comparison in Table 4 is not convincing. In general, a two-step approach will cost much time and GPU memory. The authors should provide a detailed analysis of each component of the proposed method to demonstrate its efficiency.

### Questions
Please see the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces E-STR, which aims to handle complex VideoQA tasks involving long videos with multiple objects and events. E-STR incorporates a question-critical keyframes retriever to adaptively select key events for spatial-temporal reasoning, along with a context encoder to preserve general video context.

### Strengths
1) The paper proposes a reasonable method to handle the complex VideoQA task by keyframe retrieval, which can effectively compress the long video (32->6). The idea of context encoder is innovative, which seems different from other similar works.
2) A series of experiments on complex VideoQA benchmarks have demonstrated the superiority of the method.
3) The article has a clear structure, logical writing, and is easy to understand.

### Weaknesses
1) The retrieval-based approach is not entirely new, as many existing works [1]-[3] utilize this idea for the VideoQA task. The article lacks a detailed comparison and analysis of these works. For example, in MIST, a similar keyframes-obtaining method based on attention maps is proposed, and SeViLA[1] introduces prompting LLM to get keyframes. Why does the paper choose a 1d CNN to find keyframes, and what is its advantage? What’s more, the results seem not as good as SeViLA in the NExT-QA and STAR datasets, what about the reasons?
2) Simply adapting the InstructBLIP to VideoQA tasks already achieves relatively strong performances (63.2->69.5), thus the performance gains seem to rely on the pre-trained MLLM (69.5->72.8). Besides, the contributed GCE & ST seem to have weak performance gain in Tab. 5.
3) The paper aims to handle long video reasoning. STAR only contains videos of 12s on average. More complex benchmarks like AGQA v2 (large-scale compositional reasoning), and ActivityNet-QA (longer videos of 180s on average) are worth evaluating.
4) Need further qualitative results to prove the effectiveness of the method. 
5) Limitations are not discussed.

### Questions
1) Why remain the "spatial" frame feature for question retrieval, does it keep complete video content? What's the difference between the "spatial frame feature" and the "spatial-temporal frame feature" (ST feature)? Why are the dimensions of these two features not consistent?
2) What are the differences between the proposed ST feature adapter and the current Adapter-based works, esp. the ST-Adapter (Pan et al. 2022)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author focused on better-resolving video question answering. Among various approaches, the authors focus primarily on long videos. Although the topic and the focus sound interesting, it is hard to understand the main difference compared to the previous works and how each model is constructed in what manner.

### Strengths
First, the author well-presented the problem, and I do not doubt this part. Also, the experiment seems very well designed with multiple datasets. From my end, the justifications in Figure 4 help me understand why the author set each parameter. Last but not least, I did not find any grammatical issues.

### Weaknesses
It is very hard to catch what are the main differences between previous approaches. Also, it is almost impossible to understand how each module introduced in Section 3 is constructed, even with Figure 3. As a result, it is tough to find a clear link before Section 4 and after Section 4. Specifically, the authors claim novelty in handling long-term video, stating that prior VideoQA methods do not focus on causal and temporal inference. However, many early VideoQA works [1,2,3], including the Co-Mem baseline, employed spatial/temporal attention mechanisms to address causality. Given that this work also relies on attention, the distinction is unclear. The manuscript lacks a detailed theoretical analysis to justify its approach over existing attention-based methods. Furthermore, while the authors mention Transformer-based models that sample frames, they do not adequately explain why these methods work well despite not having explicit attention-based frame samplers, nor do they provide a comparison with such models like MERLOT [4,5]. The construction of components in Section 3 is unclear. For instance, the relationship between  $X_{L}$ and $X_{l}$ is not well-defined, and the origins of $V_{ST}$, $V_{Key}$, $E_{S}$, and $E_{Q}$ are not explained. The equations, especially the Argmax in Eq.(2), lack sufficient context to understand how these are computed. Figure 3(a) is too small and lacks crucial details, making it difficult to replicate the work. The lack of clarity in Section 3 makes it difficult to connect the method to the experimental results in Sections 4 and 5.

### Questions
A. First and foremost, the authors sell their approach as somewhat new in handling long-term video. For instance, the first sentence in 3rd paragraph of the Intro (there are a couple more, e.g., the last paragraph of the Intro and the first paragraph of Related work) treats pioneer video QA tasks/methods do not focus more on causal and temporal inference. However, even from the beginning of VideoQA (Jang et al., 2017b) (I would like to cite some additional work in this thread [1,2,3]), they tackle causality with spatial/temporal attention mechanism (for instance, the oldest baseline Co-Mem (Gao et al., 2018) also uses attention). Considering this work is also mainly based on attention mechanisms, I missed the main difference between these lines of work. The author may want to say that those works are not based on the Transformer model, and it should be true for some old approaches, as those works appeared even before the Transformer was presented, but it is only valid for some of the baselines. Instead of mainly focusing on presenting numbers, I would request to present a detailed analysis with a theoretical explanation, and I do believe this will strengthen this manuscript. Along with this, I also wonder how and why the authors think some Transformer-based approaches that sample a few frames from the vision side (e.g., MERLOT [4,5]) work reasonably well on VideoQA, even though some of those models do not have an explicit attention-based frame sampler. Comparison with those models would also be appropriate.

B. Along with A, it is almost impossible to understand how each component presented in Section 3 is constructed. I guess X_{L} comes from X_{l} in Equation (1), but I failed to find any clue for V_{ST}, V_{Key}, E_{S}, E_{Q}. The only equation I can see afterward is an Argmax in Eq.(2); it is impossible to guess how to compute those. I also failed to see any symbols from tiny Figure 3 (a) (The author should write the main paper self-contained within the page limit). I don't think any reader can easily replicate this work without such details.

Due to A and B, I feel Sections 1-3 and 4-5 are disconnected, and thus, it is hard to fully digest the experiment results; it seems the experiment itself is reasonably designed, by the way. To this end, it is hard to give acceptance from my end as of now. I suggest the authors (aggressively) revise Sections 1-3 to sound more coherent with Section 4~5.


*** References ***

[1] Zhu et al., Uncovering the Temporal Context for Video Question Answering, IJCV 2017.

[2] Mun et al., MarioQA: Answering Questions by Watching Gameplay Videos, in ICCV 2017.

[3] Kim et al., DeepStory: Video Story QA by Deep Embedded Memory Networks, in IJCAI 2017.

[4] Zellers et al., MERLOT: Multimodal Neural Script Knowledge Models, in NeurIPS 2021.

[5] Zellers et al., MERLOT Reserve: Neural Script Knowledge through Vision and Language and Sound, in CVPR 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
