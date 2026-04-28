# VaQuitA: Enhancing Alignment in LLM-Assisted Zero-Shot Video Understanding

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 3, 5

## Abstract
Recent advancements in language-model-based video understanding have been progressing at a remarkable pace, spurred by the introduction of Large Language Models (LLMs). However, the focus of prior research has been predominantly on devising a projection layer that maps video features to tokens, an approach that is both rudimentary and inefficient. In our study, we introduce a cutting-edge framework, \ours, designed to refine the synergy between video and textual information. At the data level, instead of sampling frames uniformly, we implement a sampling method guided by CLIP-score rankings, which enables a more aligned selection of frames with the given question. At the feature level, we integrate a trainable Video Perceiver alongside a Visual-Query Transformer (abbreviated as VQ-Former), which bolsters the interplay between the input question and the video features. We also discover that incorporating a simple prompt, ``Please be critical'', into the LLM input can substantially enhance its video comprehension capabilities. Our experimental results indicate that \ours consistently sets a new benchmark for zero-shot video question-answering tasks and is adept at producing high-quality, multi-turn video dialogues with users.%

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an adaptive sampling technique to enhance video feature extraction for LLM-based video understanding. Additionally, it introduces a Video Perceiver alongside a visual query mechanism to improve video-text interactions. A simple method involving the prefilling of a specific language prompt is also presented. The proposed approach is evaluated on three mainstream video QA benchmarks, and qualitative results for video dialogues are thoroughly organized and presented.

### Strengths
The idea of adaptively sampling video frames is well motivated and presented. It has practical values for large multimodal models when processing extrememly long videos.

The paper is well written and implementation details are sufficently presented.

The language prompt for enhancing LLM is intriguing.

### Weaknesses
**Unclear Rationality of the Technical Solution:**
While the concept of adaptive frame sampling is reasonable, I question the technical approach of inferring the distance between a query and a video using the CLIP score. This concern arises for several reasons:

- Lack of Semantic Grounding: A significant portion of queries are not semantically grounded in video frames. For example, a query like “describe the video” does not directly correspond to specific visual elements.
- Influence of Nonexistent Objects: The similarity measure may be affected by objects mentioned in queries that do not exist in the video. For instance, given a video without a cat and a query “Does a cat exist in the video?”, the selected frame might be misleading.
- Limitations of Pretrained CLIP: A pretrained CLIP model functions similarly to a visual bag-of-words model, capable of recognizing objects, attributes, and simple interactions. However, it struggles to model words related to video dynamics, potentially reducing the accuracy of the CLIP score in such contexts.

**Insufficient Evaluation:**
Building on the previous point, I am concerned about evaluating the accuracy of the CLIP-based frame selector using questions that involve the existence or nonexistence of certain elements, such as those question format in POPE[1]. A more comprehensive evaluation is necessary, incorporating queries that reflect realistic scenarios (e.g., conversations, open-ended QA) rather than solely relying on complex, specially designed evaluation queries. Additionally, including more visualization results for long videos would be beneficial. It is also puzzling that the performance on longer videos (e.g., ActivityNet-QA) shows less superiority over state-of-the-art methods compared to shorter videos (MSVD/MSRVTT).

[1] Li et al., Evaluating Object Hallucination in Large Vision-Language Models, 2023.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces VaQuitA, a framework designed to enhance the synergy between video and textual information. It employs a CLIP-guided sampling method for improved frame selection, aligning better with the input question. Additionally, a trainable Video Perceiver and a Visual-Query Transformer (VQ-Former) are utilized to strengthen the interaction between video features and the input question.  Experiments are conducted to validate the performance of the proposed VaQuitA.

### Strengths
1. The paper is well-written and easy to follow.
2.  Experiments are conducted on open-ended video question-answer datasets to validate the performance of VaQuitA compared to existing methods.
3. The paper proposes CLIP feature similarity-based frame selection for training, which is interesting and could provide insight for future work in the community.

### Weaknesses
1. The experiments are insufficient. The VideoChatGPT Benchmark also includes TGIF-QA and Video-based Text Generation Performance Benchmarking to evaluate the performance of MLLMs across five aspects, such as correctness, orientation，temporal understanding, and so on.  However, the paper lacks these experimental results.
2. The experimental results are not impressive. Furthermore, the LLM employed in this paper is based on LLaMA2, while VideoChatGPT utilizes Vicuna. The inherent performance disparities between different LLMs undermine the persuasiveness of the experimental results due to the absence of a consistent LLM. It would be beneficial for the experimental tables to specify the exact LLM used, along with the number of parameters.
3. The paper proposes utilizing a Video Perceiver and a Visual-Query Transformer to extract text-guided video embeddings. Is there any way to verify that this approach effectively aligns visual and textual features as expected? Additionally, the experiments lack comparative results with similar methods, such as the QFormer of BLIP2.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a framework, namely VaQuitA, for Video reasoning tasks. Authors modify a typical VLM architecture for Video understanding with Perceiver-inspired module paired with modified inputs to transformer layers. Paper also discusses an improved sampling strategy which relied on CLIP similarity between visual features of video frames wrt. a textual prompt. VaQuitA yields improvements on 2 video understanding benchmarks compared to other baselines.

### Strengths
1. Paper introduces interesting and effective improvements in VLMs for video understanding.
2. Authors thoroughly study different aspects of their method in provided ablation studies. 
3. Paper is generally easy to follow.

### Weaknesses
1. The Method section is confusing at times. E.g. Figure 1. - it is unclear from the diagram that in the Data Alignment stage the frames are first being encoded through CLIP to compute Clip similarity to the question. 
2. Tables in Sec. 4 are hard to read, especially the numbers in Table 4.
3. The discussion on CLIP sampling efficiency is missing, e.g. I’d be interested to see what the computational cost is. 
4. Multi-round conversation tasks is very interesting but lacks quantitative evaluation.
5. Regarding prompt engineering - the suggested prompt might just be effective for one particular model, hence leaving the contribution of the paper less significant.

### Questions
- What is it to be understood by: utilizing a step size of value 2e − 5 in Sec. 4?
- It’s unclear to me why CLIP sampling is not employed at test time.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a video-language framework, coined VaQuitA. The proposed VaQuitA first augments video-language training data by keyframe / high-quality frame selection with CLIP-similarity, and then projects video information into LLM space via a two-step design (1. video perceiver and 2. visual-query transformer). Authors also find that specific prompt engineering can effectively enhance the downstream task as a free lunch. The proposed VaQuitA was tested on 3 video question-answer datasets and shows strong performance across those tasks under the chatgpt-based evaluation.

### Strengths
1. the overall idea makes sense to me.

2. the prompt engineering part is interesting (but somehow lacks more experimental support)

3. the authors conducted extensive ablations to show the effectiveness of each model component.

### Weaknesses
1. The evaluation dataset/metrics seem to be sub-optimal and might not be sufficient. The proposed method only focuses on three old open-ended video question-answering datasets with ChatGPT-based evaluation. Some datasets like MSVD/MSRVTT have a strong single-frame bias as shown in some previous studies [1], so evaluating those benchmarks might not be sufficient, while recent video-llms more focus on video QA datasets with longer/more complex video, like video-mme/next-qa. Also, the ChatGPT-based evaluation is problematic, even it has been adopted by some previous works, it might lack solid human agreement study, thus it is not a very reliable/stable metrics, and will even give different responses with the same input according to some related research [2].  So multi-choice video QA tasks (e.g. video-mme, MVLU, Nextqa, star, TVQA) might be necessary to fully understand and validate the proposed method.

2. According to my understanding, the proposed model still pre-trains/fine-tunes the alignment modules on instructional video data, so why this can be claimed as a zero-shot video understanding? The zero-shot is only for downstream video QA tasks, so this claim is bit weird from my perspective. Could you make me clear on this?

3. What is the trade-off between efficiency (running speed/memory) and effectiveness (accuracy) for using CLIP selected frames during inference

4. Is the conclusion in the 'Prompt Engineering Design' section supported by experiments with different LLM backbones? or it is only specific to llama2/llava 1.5?

5. missing baselines, including but not limited to [3]

[1] Revealing single frame bias for video-and-language learning. ACL23.  

[2] Freeva: Offline mllm as training-free video assistant.  

[3] Slot-VLM: Object-Event Slots for Video-Language Modeling. NeurIPS24.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper highlights the rapid advancements in language-model-based video understanding, particularly through the development of Large Language Models (LLMs). It critiques previous research for relying on a basic projection layer to map video features to tokens, which is inefficient. The authors introduce VaQuitA, a novel framework that enhances the integration of video and textual information by employing CLIP-score guided frame sampling and a trainable Video Perceiver with a Visual-Query Transformer. The study also finds that adding the prompt "Please be critical." significantly improves LLM video comprehension, and VaQuitA sets new benchmarks for zero-shot video question-answering tasks while facilitating high-quality multi-turn dialogues.

### Strengths
1. The proposed method is effective for video-text alignment in video-llms

2. the experimental results are sufficient for verifying the effectiveness of the proposed method

### Weaknesses
1. Recently, some video datasets have been released to test long or short video understanding and reasoning, such as video-mme, video-vista, and MVBench. These datasets can better test the overall performance of models. 

2. Some video-llms should be compared, such as Video-CCAM-v1.0, CogVLM2-Video-Chat, LLaMA-VID, MiniGPT4-Video, and others.

### Questions
No any other questions

### Soundness
2

### Presentation
3

### Contribution
2
