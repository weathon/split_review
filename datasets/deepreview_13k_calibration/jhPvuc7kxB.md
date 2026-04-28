# Look, Remember and Reason: Grounded Reasoning in Videos with Language Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Multi-modal language models (LM) have recently shown promising performance 
in high-level reasoning tasks on videos.
However, existing methods still fall short in tasks like causal or  compositional spatiotemporal reasoning over actions, in which model predictions need to be 
grounded in fine-grained low-level details, such as object motions and object interactions.
In this work, we propose training an LM end-to-end on low-level surrogate tasks, including object detection, re-identification, and tracking, to endow the 
model with the required low-level visual capabilities. 
We show that a two-stream video encoder with spatiotemporal attention is 
effective at capturing the required static and motion-based cues in the video. 
By leveraging the LM's ability to perform the low-level surrogate tasks, 
we can cast reasoning in videos as the three-step process of 
\emph{Look, Remember, Reason}, wherein visual information is extracted using low-level visual skills step-by-step and then integrated to arrive at a final answer. 
We demonstrate the effectiveness of our framework on diverse visual reasoning tasks from the ACRE, CATER, Something-Else and STAR datasets. Our approach is 
trainable end-to-end and surpasses state-of-the-art task-specific methods across tasks by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a Look, Rember, and Reason (LRR) framework to solve video reasoning task. The structure utilized LM to extract visual information by using surrogate grouding tasks and then integrated the grouding information to arrive at a final answer. The authors propose a two-stream vide encoder to capture sccene structure and object motions to learn low-level skills. Experiments on two sythetic dataset and one real-world datset shows the effectiveness of proposed method on complex spatialtemporal and causal reasoning tasks in videos.

### Strengths
1. The proposed LRR structure make use of language models to solve surrage groudning task to benefit final video reasoning task. This structural design better utilize the low-level visual skills and information from videos.

2. This paper conduct experiments on two synthetic datasets and one real-world dataset. The proposed methods achieve competative performance three datasets and outperforms other exsisting baseline models, showing the effectiveness of proposed method.

3. Table 2 and 3 also show the performance of LRR without surrogate tasks and two-stream encoder. The ablation study shows the significance of the two proposed components for the overall structure.

### Weaknesses
1. Writing, section 3 and Figure 2 is a little unclear and hard to follow.
2. For different surrogate tasks, where do the ground-truth answers such as localization or box come from?

### Questions
See section weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a Look, Remember, Reason (LRR) framework to enable language models to perform visual reasoning in videos. The proposed LRR framework uses a two-stream video encoder to extract dense spatiotemporal features from video frames capturing structural and motion cues. The language model backbone has cross-attention layers inserted between its self-attention layers to enable top-down attention over the visual features. This allows the model to extract relevant visual information based on the reasoning task. LRR is trained end-to-end using surrogate tasks like object detection, re-identification and tracking. These provide supervision to teach the model the required low-level visual skills.

The authors also demonstrate that training LRR jointly on multiple datasets leads to a "generalist" model that performs competitively compared to task-specific "specialist" models. In the experimental results, the authors demonstrate that the LRR models significantly outperform prior state-of-the-art on challenging visual reasoning tasks from the ACRE, Something-Else, and CATER datasets, showing the benefit of the proposed grounded reasoning approach.

### Strengths
Demonstrates strong performance on multiple challenging visual reasoning datasets by grounding the language model in low-level visual details.
+ Good demonstration of using surrogate tasks and end to end training

### Weaknesses
 - The datasets used are rather simple with low visual complexity, such as CATER.

### Questions
1) Could you comment on the nature of surrogate tasks? Are there some tasks that are more suited for reasoning vs others. Do low level recognition tasks (choice in the paper) work better.
2) Is there evidence that LRR is not ovefitting to these simplistic datasets due to surrogate tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Thank you for submitting your manuscript. The proposed three-step process of Look, Remember, Reason for training a Language Model (LM) end-to-end on low-level surrogate tasks, which include object detection, re-identification, and tracking, is indeed novel.

### Strengths
The approach presented is intriguing and demonstrates significant performance improvements.

### Weaknesses
1-Throughout the paper, there's a recurring mention of "low-level surrogate tasks". Could the authors elucidate the definition of these low-level tasks? Moreover, how do they differ from high-level tasks?

2-The Look, Remember, Reason (LRR) model framework is innovative. However, there seems to be a gap in explicitly correlating this framework with the actual operations carried out in the method. The unique contributions of the "Remember" and "Reason" steps, in particular, are not clearly highlighted. It would be beneficial for the readers if the authors can provide a clearer mapping of these steps to their corresponding operations.

3-Will the codebase for the presented method be made publicly available?

4-Regarding the results of Video-ChatGPT on the Something-Else dataset: Were these results replicated by the authors? I couldn't find a direct reference to such results in the original Video-ChatGPT paper.

### Questions
see Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors claim that they propose training an LM end-to-end on low-level surrogate tasks, including object detection, re-identification, and tracking, to endow the model with the required low-level visual capabilities.

### Strengths
The authors claim that they propose training an LM end-to-end on low-level surrogate tasks, including object detection, re-identification, and tracking, to endow the model with the required low-level visual capabilities.

### Weaknesses
1. In the experiments, the authors primarily focus on conducting investigations using synthetic datasets, particularly the ACRE dataset. However, it raises concerns about the generalizability of the conclusions/findings obtained from synthetic datasets to real-world datasets.

2. The experimental results primarily focus on classical models. However, the generalizability of the conclusions/findings derived from these classical models to more powerful transformer-based models, such as the models mentioned in *Related Work* part, remains a concern.

### Questions
Please refer to Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
