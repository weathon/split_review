# Temporal Reasoning Transfer from Text to Video

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 6, 6, 8

## Abstract
Video Large Language Models (Video LLMs) have shown promising capabilities in video comprehension, yet they struggle with tracking temporal changes and reasoning about temporal relationships.
While previous research attributed this limitation to the ineffective temporal encoding of visual inputs, our diagnostic study reveals that video representations contain sufficient information for even small probing classifiers to achieve perfect accuracy.
Surprisingly, we find that the key bottleneck in Video LLMs' temporal reasoning capability stems from the underlying LLM's inherent difficulty with temporal concepts, as evidenced by poor performance on textual temporal question-answering tasks.
Building on this discovery, we introduce the \textbf{T}extual \textbf{T}emporal reasoning \textbf{T}ransfer (\textbf{T3}). 
T3 synthesizes diverse temporal reasoning tasks in pure text format from existing image-text datasets, addressing the scarcity of video samples with complex temporal scenarios. 
Remarkably, \emph{without using any video data}, T3 enhances LongVA-7B's temporal understanding, yielding a 5.3 absolute accuracy improvement on the challenging TempCompass benchmark, which enables our model to outperform ShareGPT4Video-8B trained on 28,000 video samples.
Additionally, the enhanced LongVA-7B model achieves competitive performance on comprehensive video benchmarks. For example, it achieves a 49.7 accuracy on the Temporal Reasoning task of Video-MME, surpassing powerful large-scale models such as InternVL-Chat-V1.5-20B and VILA1.5-40B. 
Further analysis reveals a strong correlation between textual and video temporal task performance, validating the efficacy of transferring temporal reasoning abilities from text to video domains.\footnote{Project page: \url{https://video-t3.io}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the limitations of video LLMs in temporal reasoning, which involves tracking objects or events in a sequence of video frames. The authors discover and point out the deficiencies stemming from the limitations of LLM processing. Inspired by this, the authors present a text-based framework which can be used to finetune the LLM part of the video LLM, which can result in improved temporal understanding from text-only data. This approach enables smaller models to outperform larger, video-trained models on benchmarks such as TempCompass and Video-MME.

### Strengths
- Interesting approach to tackle temporal understanding of Video LLMs, that the LLM fails to understand the temporal behavior of the text prompts. 
- Utilizing only text data proposes an efficient and scalable framework, although the gains are questionable for larger models.
- The performance gains are quite significant

### Weaknesses
 - The biggest limitation of this work lies in the scope of the temporal concepts, but not simply because they were not covered in the paper. For example, consider rotation, direction, counting the number of a certain event, and relative velocity of an object relative to another object. There are some temporal concepts that cannot be represented in discrete sentences - for example, how would you describe the number of rotations of a diver in the form of text? How would you describe that one person is running faster than the other one without giving out the information explicitly?
- The above concern also brings up the question of whether the success of this approach is largely due to how video LLMs are tested on current video benchmarks: given a few discrete frames, the models are asked to answer a question. For example, a good video LLM would solve problems in "Order" when given a frame of book cover, die, school bus and then split-screen (example in figure 4). If the vision encoder encodes this information but the output quality is bottlenecked by the LLM, this method would improve the model. However, it is unclear whether this method will apply to questions that require virtually the entire video frames to be answered.

### Questions
- Are the temporal-oriented questions generated from a different distribution from the answer choice distribution of the video benchmarks? For example, are the orders in which the objects appear in the temporal-oriented questions not in the benchmark datasets? Does this still improve the performance when the training data is manipulated to be strictly out-of-distribution to the benchmark data?
- What is the performance of the fine-tuned video LLMs on the existing video benchmarks, when they are only provided the text part of the question? 
- If there is an analysis of the number of data points provided and the performance gain, it could provide a better insights to the validity of this approach.

The first two questions were critical in my rating decision.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tried to use text-only reordering style data to fine-tune MLLM to enhance the temporal ordering performance.

### Strengths
1. Show that visual features contain necessary information for order understanding task.
2. Writing is clear.

### Weaknesses
1. Why choosing LongVA? LongVA is only trained on images and text, therefore, evaluating and improving LongVA but evaluating on video understanding is not proper. Because everything is zero-shot manner. Instead, choosing backbones like LLaVA-onevision, phi-3.5-vision, or Qwen2-VL is proper. Those models have videos as the training data. If authors still show that there is clear improvement with their text-only ordering data, then the claim can be supported. 
2. Probing visual features is unfair. For LLM (decoder only), authors did not fine-tune. For visual encoder features, authors fine-tuned. Since the task diversity is limited, therefore, overfitting to this fixed task is not hard. This also explains that a LSTM can overfit this task. The interesting thing should be: if you use LSTM after LLM features, can LSTM also overfits? 
3. The empirical part of this paper demonstrate one thing: using text-only ordering data can improved relatively small LLM backbones. A more foundational question is: since large LLM can already solve the ordering task pretty well, is authors’ approach just a temporary  solution? Can authors’ approach improves Qwen-2-VL-72B?
4. Evaluation limited. Evaluations on benchmarks like NextQA, ActivityNet, etc is still necessary. This is because ordering task is naturally just a small subset of temporal reasoning.

### Questions
See comments above.

### Soundness
3

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
The paper attempts to address current limitations in temporal reasoning of Video Large Language Models (Video LLMs). Current models still often struggle with understanding temporal sequences, despite advances in video comprehension. Through a detailed analysis, the authors empirically demonstrate that the bottleneck primarily lies in the LLM's capability to understand temporal concepts. This is in contrast to a multitude of concurrent work that often aim to improve the temporal encoding or adaptor functions. To address this limitation, this paper also introduces the Textual Temporal Reasoning Transfer (T3) approach, that generates temporal reasoning tasks solely in textual format. The experiments reported in the paper demonstrates the effectiveness of the approach where it obtains performance gains in multiple video question answering benchmarks, without requiring additional video and language annotations for training.

### Strengths
1) In terms of significance, this paper addresses the problem of video and language reasoning in multimodal Large Language Models (MLLMs) from a new perspective. It attributes the limitation of existing (MLLMs) to the LLM component instead of the video or adaptor functions. This is a very interesting perspective since it proposes an approach that improves the LM's ability to understand temporal concepts through text. The proposed Textual Temporal Reasoning Transfer (T3) approach creatively uses text-only datasets to improve temporal reasoning without requiring any video-language annotations.

2) The quality of the paper is relatively high, especially with regards to the empirical analysis of the bottleneck in video and language reasoning. The experiments conducted in the analysis are well motivated. The finding that the performance of existing MLLMs is constrained by their LLM decoders instead of the visual encoding function is insightful.

3) In terms of clarity, the paper is well-written and motivated. The model figures are informative and especially helpful in helping the reader to understand the differences between questions that focus on different temporal reasoning abilities in videos.

### Weaknesses
1) The text-based tasks used in T3 are largely devised based on templates and may not always be similar to the language concepts that are contained in real-world videos. For example, such templated sentences may lack the subtle temporal cues that naturally occur in descriptions of complex events. This might affect the model's ability to generalize to different downstream tasks.

2) In this work, the authors only address four temporal aspects: order, attribute change, temporal referring, and grounding. However, this excludes some other common aspects of temporal reasoning such as understanding causal relationships and durations. Including more training samples that require more complex forms of reasoning could improve robustness of the trained models across a broader spectrum of temporal tasks.

### Questions
See weaknesses.

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
The paper studies the video's large language models, particularly its temporal reasoning ability. It first designs probing experiments using synthesized videos and analyzes the bottleneck in temporal understanding: primarily on LLMs but not the vision encoder.  To mitigate the issue, the authors propose a simple text data augmentation method to leverage the image-text datasets to generate diverse
temporal reasoning tasks and enhance the video LLMs training. The experiments based on LongVA-7B show its competitive performances across different datasets.

### Strengths
1. The paper is well structured and written, making it easy to understand its key points. 

2. The enhanced model, built on LongVA-7B, has shown strong performances, surpassing large-scale models such as InternVLChat-V1.5-20B and VILA1.5-40B.

### Weaknesses
1. The claims of the paper do not fully convince me of the paper made. I agree that most of the vision encoders used today do not help much with temporal reasoning, even though they are trained with millions of videos. However, this can not be claimed as "the temporal reasoning most of rely on the temporal reasoning ability from LLMs. There might be reasons that the temporal reasoning also replies on the model alignment ability between the text and the images/videos. The authors should design extensive prompting experiments on more models and datasets to support their strong claims.

2. The synthesized tasks are mainly based on GPT-4o. And for me, how to design the synthesized tasks seems very arbitrary and empirical. Are there any particular reasons you designed these tasks and how can you ensure its generalization on more domain/datastes? The authors should have more deep analysis and experiments on those two issues.

### Questions
Besides the questions I listed before, there are two additional questions for the authors:

1. How to explain the strong temporal reasoning ability of GPT-4o? Is it only because 4o has a very strong temporal reasoning ability from the language side, not related to its vision encoder or alignment? 

2. Is there any way you can conduct the probing experiments on real datasets, not the synthesized ones?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the limitations in Vision Language Models (VLMs) for temporal reasoning tasks in video understanding. Through detailed probing experiments, the authors identify the primary bottleneck as the LLM component rather than the visual encoder. To address this, they introduce an approach called T3, which fine-tunes only the LLM component on text-only data, enhancing performance on several temporal reasoning benchmarks.

### Strengths
1. The authors provide a well-defined motivation for their work, verifying through experiments that the LLM, rather than the VLM, is the limiting factor in video understanding tasks, and proposed solutions.
2. The authors introduce an innovative fine-tuning technique that only tunes the LLM within a VLM, bypassing the need for visual data. This approach yields significant performance improvements across several video understanding benchmarks.
3. The dataset is generated in a fully automated manner, adding to the scalability of their approach.
4. Extensive experiments and in-depth analysis are provided.

### Weaknesses
1. As mentioned in L-538, the approach shows minimal improvement when applied to larger LLMs, which could restrict its broader applicability.
2. Several areas of the paper would benefit from further clarification (see questions below).
3. The paper does not sufficiently demonstrate that the performance improvement is due to enhanced temporal reasoning rather than improved instruction following. The analysis of mis-formatted responses is limited, and the ablation study using image-based transfer does not fully isolate the effect of instruction following from the temporal reasoning capabilities.
4. The use of GPT-4o for caption generation, while automated, introduces a potential bias or limitation in the quality of the generated captions. The paper does not fully explore the impact of these captions on the overall performance, especially when compared to human-annotated captions.

### Questions
1. Could you report results on larger LLMs (e.g., Qwen2-72B)? Although the performance gain is noted to be limited, these results could be informative for future research.
2. Could you provide examples of captions generated by GPT-4o as mentioned in L-133? It would help clarify whether specific attribute information is inadequately encoded in the caption, potentially leading to near-random results in LLM responses. (You partial addressed this in L216-L217, but the performance achieved by larger model is still 20% percent lower than the performance achieved by LSTM, which makes it not convincing).
3. Minor issue: It appears LLaVA-ReCap-558K is derived from LCS-558K (a subset of the LAION/CC/SBU dataset) rather than BLIP558K (as stated in lines 861-862) [1].
4. I question whether the performance improvement is due to enhanced instruction-following ability (e.g., the ability to "Answer the option only") rather than true temporal reasoning. Could you report the portion of mis-formatted or invalid responses across all experiments to clarify this?

[1] Section on Open Source Release: https://llava-vl.github.io/blog/2024-05-25-llava-next-ablations/

### Soundness
3

### Presentation
4

### Contribution
3
