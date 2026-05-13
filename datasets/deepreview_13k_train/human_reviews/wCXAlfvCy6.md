# LongVILA: Scaling Long-Context Visual Language Models for Long Videos

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Long-context capability is critical for multi-modal foundation models, especially for long video understanding. We introduce LongVILA, a full-stack solution for long-context visual-language models \qinghao{by co-designing the algorithm and system. For model training, we upgrade existing VLMs to support long video understanding by incorporating two additional stages, {\em i.e.}, long context extension and long video supervised fine-tuning.
However, training on long video is computationally and memory intensive. We introduce the long-context Multi-Modal Sequence Parallelism (MM-SP) system that efficiently parallelizes long video training and inference, enabling 2M context length training on 256 GPUs without any gradient checkpointing.
LongVILA efficiently extends the number of video frames of VILA from 8 to 2048, improving the long video captioning score from 2.00 to 3.26 (out of 5), achieving 99.8\% accuracy in 6,000-frame (more than 1 million tokens) video needle-in-a-haystack. LongVILA-7B demonstrates strong accuracy on the VideoMME benchmark, {\em i.e.}, 61.8\% with subtitle. Besides, MM-SP is $2.1 \times$ - $5.7 \times$ faster than ring style sequence parallelism and $1.1 \times$ - $1.4 \times$ faster than Megatron with a hybrid context and tensor parallelism. Moreover, it seamlessly integrates with Hugging Face Transformers.
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel long-context Multi-Modal Sequence Parallelism (MM-SP) system specifically designed to enhance the performance of Vision-Language Models (VLMs) when processing extended contexts, increasing the window size from 8 to 1024 frames. The authors demonstrate how their approach can effectively manage and leverage longer input sequences, aiming to address limitations in current VLMs regarding video processing capabilities.

### Strengths
- The introduction of MM-SP is a significant contribution to the field, as it creatively combines techniques for managing long-context sequences in a multi-modal setting. This approach addresses a gap in existing models that struggle with extensive video inputs.

### Weaknesses
 - The evaluation primarily utilizes a single benchmark (VideoMME), which may not sufficiently demonstrate the capabilities of the proposed system in handling long videos. It would be beneficial to incorporate additional benchmarks focused on long video analysis, such as those introduced in recent works (e.g., arXiv:2406.09367 and arXiv:2406.14129) to validate the robustness of the findings.
- While the authors mention the ability to process 1024 frames, the results are only provided for 256 frames (Figure 2(a)). It would strengthen the paper to include performance metrics for 512 and 1024 frames across the discussed benchmarks to fully substantiate the claims made.

### Questions
- If the authors were to mix the stage 3 with stage 5 at the end, which is stage 1-2-4-(3&5), what anticipated effects on performance or learning dynamics might arise? Would the integration lead to any synergies or drawbacks?
- How would the performance change if context extension were prioritized by using a long-window LLM first, followed by stages 4-1-2-3-5?
- How would the performance change if you conbine these two stratgies, which is 4-1-2-(3&5)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces LongVILA, a comprehensive framework aimed at enhancing long-context video understanding capabilities in multi-modal foundation models. To optimize model training for long videos, LongVILA introduces two pivotal stages: long context extension and long video supervised fine-tuning. Considering the computational and memory challenges associated with training on long videos, the authors present the long-context Multi-Modal Sequence Parallelism (MM-SP) system. This system significantly improves training efficiency, enabling the processing of context lengths up to 2 million on 256 GPUs without relying on gradient checkpointing. The results demonstrate a remarkable increase in performance metrics, with the long video captioning score rising from 2.00 to 3.26 and achieving 99.5% accuracy in video needle-in-a-haystack tasks. Additionally, LongVILA shows strong performance on the VideoMME benchmark, with scores of 57.5% and 60.6% without and with subtitles, respectively. Overall, LongVILA presents a significant advancement in the realm of long-context visual-language models, providing both theoretical contributions and practical solutions to the challenges posed by long video understanding.

### Strengths
* The paper is well-written and easy to understand. The figure illustration and captions are informative.
* The authors provide a full-stack design for long-context Vision-Language Models, including both training curriculum and system implementation. These contributions are significant in the multimodal foundation model community.
* The proposed model, LongVILA, presents strong performance on VideoMME and other long video understanding tasks.
* The Multi-Modal Sequence Parallelism design can greatly reduce the memory cost in both training and inference.

### Weaknesses
 * The authors do not seem to provide performance metrics on general video understanding benchmarks, such as the Perception Test [A] or EgoSchema [B], after improving long video understanding capabilities. It is worth noting whether the performance on general benchmarks is affected after enhancing long-context capabilities.
* The proposed Multi-Modal Sequence Parallelism design is interesting and effective. However, it is not clear whether the source code will be released, which will be beneficial to the community.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes LongVILA, a solution for long-context visual-language models. The authors incorporate two additional stages, i.e., long context extension and long video supervised fine-tuning. A long-context multi-modal sequence parallelism system is proposed to efficiently parallelize long video training and inference.

### Strengths
1. This paper implements a five-stage training curriculum: multi-modal alignment, large-scale pre-training, short supervised fine-tuning, context extension for LLMs, and long supervised fine-tuning.
2. An efficient and user-friendly framework (multi-modal sequence parallelism) is proposed to support training and inferencing
memory-intensive long-context VLMs.
3. The presentations are good.

### Weaknesses
1. I suggest the authors to involve more baselines in Table 3. For example, PLLaVA, Flash-VStream, Video-LLaMA-2.
2. This paper has not reported results on some (long) video QA benchmarks, for example, MoVQA, ActivityNet-QA, Ego-Schema, MV-Bench. I suggest the authors to include them.
3. Is there any model complexity analysis? For example, #Params, GFLOPs.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
