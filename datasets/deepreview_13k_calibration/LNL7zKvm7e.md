# Frame-Voyager: Learning to Query Frames for Video Large Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Video Large Language Models (Video-LLMs) have made remarkable progress in video understanding tasks.
However, they are constrained by the maximum length of input tokens, making it impractical to input entire videos.
Existing frame selection approaches, such as uniform frame sampling and text-frame retrieval, fail to account for the information density variations in the videos
or the complex instructions in the tasks, 
leading to sub-optimal performance.
In this paper, we propose \name that learns to query informative frame combinations, based on the given textual queries in the task. 
To train \name, we introduce a new data collection and labeling pipeline, by ranking frame combinations using a pre-trained Video-LLM.
Given a video of $M$ frames, we traverse its $T$-frame combinations, feed them into a Video-LLM, and rank them based on Video-LLM's prediction losses.
Using this ranking as supervision, we train \name to query the frame combinations with lower losses.
In experiments, we evaluate \name on four Video Question Answering benchmarks by plugging it into two different Video-LLMs.
The experimental results demonstrate that \name achieves impressive results in all settings,
highlighting its potential as a plug-and-play solution for Video-LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed Frame-Voyager that learns to query informative frame combinations, based on the given textual queries in the task.
Authors introduced a new data collection and labeling pipeline, by ranking frame combinations using a pre-trained Video-LLM.
Extensive experiments are conducted to support the effectiveness of the proposed Frame-Voyager.

### Strengths
This is a reasonable extension from previous keyframe selection work [1] where it relies more on single keyframe selection, and does not consider temporal relations/modeling among frames. The proposed pseudo-label scheme from a VLM + list of combinations of frames makes sense to me. 
Authors also conduct extensive experiments across diverse popular benchmarks to show their effectiveness. 
Overall, I think the proposed Frame-Voyager makes a good contribution to the keyframe selection in video-language studies. 

[1] Self-chained image-language model for video localization and question answering. NeurIPS23

### Weaknesses
1. As the paper mentioned, this pseudo-label strategy is not scalable, and I think the frame combination part is a bit tricky. This is like creating artificial rewards according to video (like a sandbox in RL) to train the reward model. However,  the reward is not always reliable from a VLM even though we compute it according to GT answers. For example, as shown in some previous studies [2],  the model will generate correct answers when provided with wrong localized clips. It is true that we might give performance improvement when using such reward data created by a human-free pipeline, but it is more like an adapter / DPO style adaptation to the model rather than letting the model truly be grounded on query-related / informative frames.

2. I think the weakness in 1 somehow affects the proposed method to require a relatively complex pre-training data construction/filtering/design, since the positive/negative signal is too sensitive according to video conditions in this framework from my view (e.g. frame blurring / redundancy).

3. Also, the keyframe selection for video-language understanding is not a brand new topic, many related works in track try to propose different ways, from continuous space learning to discrete pipeline, to address question-aware moment detection. I would suggest to include those works [1,2,3,4] for a more comprehensive study.

### Questions
Please see the weaknesses. And extra questions:

(1) What is the trade-off between efficiency and effectiveness? Can you provide some metrics like running time/memory usage/flops to the proposed methods? As the model contains an extra keyframe localization stage, it is worthy showing those results to see the trade-off.

(2) I notice that the proposed method uses VILA as a reference model to label rewards, and uses the same VILA series models for downstream tasks. Is this also a kind of self-rewarding strategy shown in the sevilla work? Or the proposed method/modules can zero transfer to other VLM like llava-ov/qwen-vl-2?

(3) to answer my 1st weakness, I would suggest authors conduct extra experiments on Next-GQA to see the grounded QA results with grounded metrics.

(4) Can you show some off-shelf llm-based localization tools like sevila localizer in Table 2? It would be interesting to see the comparison between a llm-based reasoning method with the proposed reward imitation learning method.

(5)  Regarding the claim in Figure 3 and RQ3 (Lines 431-433), is this true? Related work (e.g., [1]) suggests that some observed issues may stem from limitations in the model side (VILA). Could the authors clarify this?

[1] LONGVIDEOBENCH: A Benchmark for Long-context Interleaved Video-Language Understanding

### Soundness
3

### Presentation
2

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
In this paper, the authors present Frame-Voyager which learns to query informative frame combinations, based on the given textual queries for video qa tasks. The authors create a data collection pipeline for the proposed model/training objection and evaluate it on four video QA benchmarks.

### Strengths
1. The motivation is clear and easy-to-follow. 

2. The presentation of the paper is of high quality. 

3. The analysis is comprehensive.

### Weaknesses
1. The inflexibility of the proposed frame selection method. Different videos usually have different “information density”, which means that some video could be represented by even a single frame and some need densely sampled frames. This also would be affected by the query type. The number of keyframes in the proposed framework seems to be a fixed hyper-parameter, which would be hard to generalize to all different videos in the wild (for different length / query types, need different hyper-parameter selection). Is it possible for the model to do adaptive/dynamic frame selection?

2. The authors mention in line 170-172 that “the smaller combinations exhibit generalization capabilities when larger values of M and T are used during inference for longer video”. However, the process of this generalization is unclear (the introduction of the inference process, top-K selection is also unclear, in line 258-261). Does the inference directly apply the model to higher frame number or is the concatenation of several combinations with the highest score, what is the K setting for inference? Also, based on this, could the authors elaborate more on how Frame-Voyager makes good use of global video context?

3. In Table 1 and Figure 3, the authors only compare Frame-Voyager with the uniform sampling baseline using the same frame number of frames for Question-Answering. However, Frame-Voyager actually sees more frames for keyframe selection (128 frames and select 8 frames), which creates unfair comparisons. Also there seems to be very little improvement in performance while using 8 keyframes from 128 frames compared to just uniform sample 16 frames. Could the authors show the comparison of Frame-Voyager against the best uniform sampling configurations for a more fair comparison?

### Questions
All question in weakness and: 

1. Since the authors claim that the proposed method is a plug-and-play module, does the reference Video-LLM for data collection have to be the same model family with the MLLM for Frame-Voyager? Since different models have different features, whether the generated data only works for the ViLA-1.5 model family? It would be interesting to see the performance of these annotated data’s effectiveness on different model families like LLaVA-onevision and so on. 

2. The authors are encouraged to discuss the comparison with a related line of research which leverages LLM agents to select meaningful keyframes from the video input, including VideoAgent [1], VideoTree[2] … 

3. Also, could the authors validate the effectiveness of the frame selection method on temporal grounding as well? Which seems to be very similar in high-level (localizing key information given the text query). 

[1] VideoAgent: Long-form Video Understanding with Large Language Model as Agent

[2] VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos

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
This paper introduces Frame-Voyager, a novel frame selection method designed to improve the performance of Video-LLMs on video question-answering (QA) tasks. The key contributions are (1) an automated data collection strategy that ranks frame combinations according to the QA loss from a reference Video-LLM, and (2) a frame selection module integrated with a Video-LLM, trained using this ranked data. When applied to VILA, Frame-Voyager outperforms the uniform sampling baseline across four video QA benchmarks.

### Strengths
**1. Originality:** The novel formulation of frame selection as a ranking problem is compelling. This approach minimizes the need for extensive manual labeling to obtain ground truth, offering a fresh and efficient perspective on the task.

**2. Significance:** Frame selection is a critical challenge in video understanding due to the high dimensionality of video data and the computational demands involved. Traditional uniform sampling often misses relevant content, making this problem a key focus for advancing the field.

**3. Clarity:** The paper is well-written, with a clear explanation of the motivation and methodology. The authors effectively communicate the concepts, making the approach easy to understand.

### Weaknesses
 **1. Data Collection Cost:**
The number of frame combinations increases exponentially with M and T (L166), leading the authors to limit M to 16 or 32 and T to 2 or 4. Despite these restrictions, evaluating $C(32, 4) \approx 36K$ combinations for a single QA sample is still costly, raising concerns about data collection efficiency. Thus, this paper needs to provide more details on the computational resources and time required for data collection.

**2. Generalization to More Frames:**
The method is trained to select up to T=4 frames from M=32 candidates. Although the authors claim the model generalizes well to larger M and T values (L170), Fig. 3 shows diminishing gains over uniform sampling while increasing the number of frames. Despite the authors attributing this to benchmark constraints (L431), prior research (e.g., LongVILA [1], LongVA [2]) has shown that additional input frames can enhance QA performance, suggesting potential limits in generalization. Given the impracticality of increasing M and T for data collection, robust generalization is crucial. Thus, the authors should extend their experiments to more input frames, possibly integrating Frame-Voyager with LongVILA, to help clarify the generalization capabilities and limitations of Frame-Voyager.

**3. Fairness of Comparisons:**
The comparison between Frame-Voyager and CLIP is not fully equitable due to three factors: (i) Frame-Voyager uses superior backbones (SigLIP or InternViT-6B); (ii) it is trained on specialized ranking data, unlike CLIP; and (iii) it has additional parameters like self-attention modules. Since (ii) and (iii) are core contributions of Frame-Voyager, a fairer comparison would involve using SigLIP or InternViT-6B models with and without training on the collected data. Additionally, the authors should specify the versions of CLIP and SigLIP used.

**4. Latency Analysis:**
The authors claim that Frame-Voyager outperforms LongVILA while processing fewer frames, but this only holds for the "Long" subset of the Video-MME benchmark. In other scenarios, LongVILA performs better. Given the extra parameters introduced by Frame-Voyager, a detailed efficiency comparison between VILA+Frame-Voyager and LongVILA is necessary, including latency, memory usage, and computational complexity.

### Questions
My questions focus primarily on the weaknesses outlined above:

1. What are the data collection costs, particularly for the VideoChatGPT data?

2. How well does the method generalize when increasing the number of frame candidates and selected frames?

3. Can the proposed model outperform SigLIP and InternViT-6B, especially when they are fine-tuned on the same collected data?

4. What is the latency of the method?

5. A suggestion: Could CLIP-like models enhance data collection efficiency? Specifically, using them to estimate query-frame similarities might identify frames with extremely high or low similarities, indicating positive or negative frame combinations. This could reduce the search space and improve data collection efficiency.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents FRAME-VOYAGER, a novel approach for improving Video Large Language Models by selecting informative frame combinations based on textual queries. Traditional methods like uniform frame sampling and text-frame retrieval do not account for variations in information density or complex instructions, leading to sub-optimal performance. FRAME-VOYAGER addresses this by learning to query frame combinations with lower prediction losses, using a pre-trained Video-LLM for supervision. The method is demonstrated to enhance performance in video question answering tasks across various benchmarks. The approach also includes a new data collection and labeling pipeline, which ranks frame combinations to train the model efficiently. FRAME-VOYAGER is proposed as a plug-and-play solution, improving Video-LLMs without significant computational overhead. Experiment results show that FRAME-VOYAGER achieves significant performance in several VQA datasets.

### Strengths
1.The authors designed an efficient keyframe data construction method, exploring keyframe selection using combinations of all frames. This approach achieved significant improvements across multiple datasets with 12K high-quality clips.

2.The authors state that they will open-source the data and related code, which is valuable for the open-source community.

3.The proposed method demonstrate strong performance across multiple datasets, proving the robustness of the approach, especially in Anet dataset. As a plug-and-play method, Frame-Voyager can serve as a valuable tool for video understanding.

### Weaknesses
1.Data scaling limitations. As the authors mentioned, selecting 4 frames from 32 results in 35960 candidates, leading to prohibitively high costs for data scaling. Furthermore, keyframe selection is even more critical for longer videos, and the costs become unmanageable when dealing with selections from 128 or 256 frames. The combinatorial explosion in frame selection makes it unclear how this method can scale to videos with hundreds or thousands of frames, which is common in real-world scenarios. The paper does not sufficiently address the computational and memory requirements for such scaling, particularly during training, where many combinations must be evaluated.

2.When testing on short video benchmarks, did VILA and VILA+FRAME-VOYAGER evaluate performance by selecting 2 frames out of 16? If so, please provide the results of VILA using 16 frames on the Next-QA and ANQA datasets. Additionally, I believe that comparing results based on only 2 frames is not meaningful, as most models typically evaluate performance using 8 or 16 frames. The paper should clarify the frame selection strategy for short videos and provide a comparison with standard frame sampling techniques using a consistent number of frames.

3.Please provide additional results of the model on more benchmarks, such as MVbench and egoSchema. The current evaluation is limited to a few datasets, and it is necessary to assess the method's generalizability across a wider range of video understanding tasks and datasets. The lack of results on benchmarks like EgoSchema, which focuses on long-form video understanding, is a notable gap in the evaluation.

### Questions
See the above weakness. I am interested in how the authors consider data scaling. Constructing data with only 16 or 32 frames is not very helpful for understanding long videos.

### Soundness
3

### Presentation
3

### Contribution
3
