# Q-Adapt: Adapting LMM for  Visual Quality Perceiver with Progressive Instruction Tuning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
The rapid advancement of Large Multi-modal Foundation Models (LMM) has paved the way for the possible Explainable Image Quality Assessment (EIQA) with instruction tuning from two perspectives: overall quality explanation, and attribute-wise perception answering. However, existing works usually overlooked the conflicts between these two types of perception explanations during joint instruction tuning, leading to insufficient perception understanding. To mitigate this, we propose a new paradigm for perception-oriented instruction tuning, i.e., Q-Adapt, which aims to eliminate the conflicts and achieve the synergy between these two EIQA tasks when adapting LMM, resulting in enhanced multi-faceted explanations of IQA. Particularly, we propose a progressive instruction tuning strategy by dividing the adaption process of LMM for EIQA into two stages, where the first stage empowers the LMM with universal perception knowledge tailored for two tasks using an efficient transfer learning strategy, i.e., LoRA, and the second stage introduces the instruction-adaptive visual prompt tuning to dynamically adapt visual features for the different instructions from two tasks. In this way, our proposed Q-Adapt can achieve a lightweight visual quality perceiver, demonstrating comparable performance and, in some instances, superior results across perceptual-related benchmarks and commonly-used IQA databases.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposed a paradigm for perception-oriented instruction tuning named Q-Adapt, aiming to alleviate the conflict between overall quality explanation task and attribute-wise perception answering task. The authors designed a two-stage training strategy. In stage one, a LMM is finetuned to obtain a powerful base for two tasks; in stage two, some parameters in the LMM are frozen while the other parameters are finetuned to drive LMM more focus on the task instruction. In the second stage, a V-T generator and a T-V prompter are designed to achieve the bi-directional multimodal interactions.

### Strengths
In terms of originality, this paper proposes a new method; In terms of quality, based on the experimental results provided by authors, the proposed method can only improve the performance in a small number of experiments, thus its superiority is worth reconsidering. In terms of clarity, the authors describe the implementation details of the proposed method in detail, but the description of the experimental settings is not clear enough, which is easy to mislead the reader. In terms of importance, if the proposed method could actually improve the performance of LMM on two tasks, it would be a promising method which worthes further researching.

### Weaknesses
[1]The motivation section needs improvement. In Line 51, the conflict between the two EIQA tasks is mentioned without explaining why this conflict arises or giving examples. This should be clarified in the introduction rather than in Line 220. Specifically, the paper should elaborate on the inherent differences in the information required for each task. For instance, overall quality assessment might rely on holistic scene understanding, while attribute-wise perception requires fine-grained analysis of specific image regions and features. The lack of this explanation makes the motivation less compelling.

[2]It’s unclear what the proposed method gains from the perception answering task in the second phase. The paper stresses the importance of the explanation task and highlights the negative impact of the perception answering task during joint training. If this is the case, why include the perception answering task at all? The authors should provide a detailed analysis of the knowledge required for both tasks, as well as how they benefit from and conflict with each other. It is not sufficient to simply state that the tasks are conflicting; the paper needs to explain the specific mechanisms through which they interfere with each other during training and how the proposed approach mitigates these issues. For example, does the perception answering task introduce noise or bias that hinders the learning of the explanation task?

[3]The proposed V-T Generator and T-V Prompter are central to the paper, but their approach seems similar to [1]. While this might be new for the IQA field, the contribution to the broader CV and MLLM communities appears limited. The V-T Generator, which extracts visual features conditioned on text, closely resembles the Q-Former in [1], and the T-V Prompter, which generates visual prompts based on text, is functionally similar to the VTC module in [1]. The paper needs to clearly articulate the novel aspects of these modules beyond their application in the IQA domain.

[4]The results in Figure 3 are confusing. The caption refers to the quality explanation task, but Line 216 and the y-axis suggest these are results for the attribute-wise perception answering task. This needs clarification. The discrepancy between the caption and the text creates ambiguity about what the figure is actually demonstrating. The authors should ensure consistency in the description and labeling of results.

[5]In the experiments presented in Figure 3, was the data volume kept consistent across the two tuning settings? Assuming that Figure 3 indeed represents results for the attribute-wise perception answering task, why does the model tuned specifically for this task perform the worst? Could this be attributed to differences in data volume? The paper needs to provide more details about the experimental setup, including the exact dataset sizes used for each tuning setting. If the data volume was not consistent, this could be a confounding factor that affects the interpretation of the results.

[6]The reviewer suggests merging the paragraph starting at Line 244 in Section 3.3 with Section 3.4. The current organization may mislead readers into thinking that the connector is responsible for adaptively selecting the required perceptual knowledge based on task instructions. The separation of these sections creates a misleading impression of the connector's role, and merging them would provide a more coherent explanation of the overall architecture.

[7]How significant is the impact of using MLP versus Q-Former as the connector on the final results? The paper should present an ablation study that directly compares the performance of these two connector options. This would help to understand the contribution of the Q-Former to the overall performance of the model.

[8]Table 7 lacks an ablation study that focuses solely on fine-tuning with the quality explanation task in the second stage. This would help evaluate whether including the attribute-wise perception answering task is beneficial to model training. Without this ablation, it is difficult to assess the true impact of the attribute-wise perception answering task on the final performance.

[9]Based on the results reported in Table 2, the sum score for Qwen-VL-Max should be 5.18, not the current value. The reviewer recommends carefully verifying the reported data throughout the paper. This discrepancy raises concerns about the accuracy of the reported results, and the authors should double-check all numerical values.

[10]Including more comparisons with other MLLM performance benchmarks would further strengthen the paper. For instance, comparisons with models such as LLaVA-OneVision [2], LLaVA-NeXT-Interleave-7B [3], and Qwen2-vl [4] would be highly beneficial. These comparisons would provide a better understanding of the proposed model's performance relative to the state-of-the-art.

[11]Minor Weaknesses:
- The use of "(i)" and "(ii)" in the second paragraph of the Introduction appears multiple times, which disrupts the flow and readability. The reviewer suggests varying the symbols when listing multiple points.
- There is a typo in Table 6, second row: "$Q$-$Former^{Co}$" should be "$Q$-$Former^Q$."

### Questions
1.	Why does the author only analyze the experimental results of Q-bench-A1 in Table 1 and not those of Q-bench2-A1?
2.	What does a score of 0, 1, and 2 mean in Table 2, and how is the GPT score calculated?
3.	In Table 1 and Table 3, the proposed method is even worse than vanilla LMM in many experiments. Can the author explain the reasons for this phenomenon?

### Soundness
1

### Presentation
2

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
This work proposes to adapt MLLM for visual quality assessment (as textural output) with a two-stage instruction tuning.

### Strengths
1. The use of MLLM for visual quality assessment is a rising research direction that is worth deep investigation.
2. The related work section, for example, the categorization of MLLM-based visual quality assessment, is very well written.
3. The experimental results look good.

### Weaknesses
1. The term "progressive" is a little misleading; it is simply a two-stage training method.

2. The motivation for this work is unclear. The authors claim that the two examined tasks are conflicting, which is not well justified. From the reviewer's perspective, the two tasks could complement each other: a holistic understanding of visual quality aspects of the image can enhance more detailed quality assessment tasks involving local image analysis, and vice versa. This indeed motivates the authors to propose the two-stage training method.

3. The use of LoRA in the first stage of training is not clearly explained. Why is parameter-efficient fine-tuning (such as LoRA) necessary? Which subset of parameters is subject to LoRA fine-tuning, and how are these parameters identified?

4. The information flow in stage two (Figure 2) appears somewhat redundant. For example, both raw visual features and processed visual features (by the V-T generator) are sent to the T-V prompter, and then combined with the raw features to feed into the language model. Is such a complex design necessary? Further justification would be appreciated.

5. The generated quality-relevant textual descriptions should be evaluated for both correctness and diversity. Template-like textual outputs are unlikely to be perceived as explainable.

6. The experimental setups need clearer descriptions. For instance, how are the competing methods implemented?

7. How were the visualizations in Figure 4 generated, and how should these results be interpreted and compared?

### Questions
The authors should work on Points 2, 3, 4, and 5 to raise the reviewer's rating.

### Soundness
2

### Presentation
2

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
The paper introduces Q-Adapt, a framework designed to adapt Large Multi-modal Models (LMMs) for Explainable Image Quality Assessment (EIQA). It tackles the challenge of handling two conflicting EIQA tasks: overall quality explanation and attribute-wise perception answering. To resolve these conflicts, the authors propose a progressive instruction tuning approach that consists of two stages. In the first stage, universal perception knowledge is acquired using a parameter-efficient method like LoRA to fine-tune the model for both tasks. In the second stage, instruction-adaptive visual prompting is introduced to allow the model to dynamically adapt to task-specific instructions, improving the synergy between vision and language features. The experimental results show that Q-Adapt significantly improves performance across benchmarks, efficiently balancing both EIQA tasks and leading to better visual perception and reasoning.

### Strengths
[1] The paper provides extensive experiments, which convincingly demonstrate the effectiveness of the proposed method.

[2] The approach achieves performance on par with 8B models while only using a 3B model, which is highly encouraging.

[3] The method is simple and straightforward, making it easy to implement and understand.

[4] The method offers valuable insight into the task conflicts within EIQA, shedding light on how to address these challenges effectively.

### Weaknesses
[1]The motivation section needs improvement. In Line 51, the conflict between the two EIQA tasks is mentioned without explaining why this conflict arises or giving examples. This should be clarified in the introduction rather than in Line 220.

[2]It’s unclear what the proposed method gains from the perception answering task in the second phase. The paper stresses the importance of the explanation task and highlights the negative impact of the perception answering task during joint training. If this is the case, why include the perception answering task at all? The authors should provide a detailed analysis of the knowledge required for both tasks, as well as how they benefit from and conflict with each other.

[3]The proposed V-T Generator and T-V Prompter are central to the paper, but their approach seems similar to [1]. While this might be new for the IQA field, the contribution to the broader CV and MLLM communities appears limited.

[4]The results in Figure 3 are confusing. The caption refers to the quality explanation task, but Line 216 and the y-axis suggest these are results for the attribute-wise perception answering task. This needs clarification.

[5]In the experiments presented in Figure 3, was the data volume kept consistent across the two tuning settings? Assuming that Figure 3 indeed represents results for the attribute-wise perception answering task, why does the model tuned specifically for this task perform the worst? Could this be attributed to differences in data volume?

[6]The reviewer suggests merging the paragraph starting at Line 244 in Section 3.3 with Section 3.4. The current organization may mislead readers into thinking that the connector is responsible for adaptively selecting the required perceptual knowledge based on task instructions

[7]How significant is the impact of using MLP versus Q-Former as the connector on the final results? 

[8]Table 7 lacks an ablation study that focuses solely on fine-tuning with the quality explanation task in the second stage. This would help evaluate whether including the attribute-wise perception answering task is beneficial to model training.

[9]Based on the results reported in Table 2, the sum score for Qwen-VL-Max should be 5.18, not the current value. The reviewer recommends carefully verifying the reported data throughout the paper.

[10]Including more comparisons with other MLLM performance benchmarks would further strengthen the paper. For instance, comparisons with models such as LLaVA-OneVision [2], LLaVA-NeXT-Interleave-7B [3], and Qwen2-vl [4] would be highly beneficial.

[11]Minor Weaknesses:
- The use of "(i)" and "(ii)" in the second paragraph of the Introduction appears multiple times, which disrupts the flow and readability. The reviewer suggests varying the symbols when listing multiple points.
- There is a typo in Table 6, second row: "$Q$-$Former^{Co}$" should be "$Q$-$Former^Q$."

[1] Instruction Tuning-free Visual Token Complement for Multimodal LLMs.

[2] Llava-OneVision: Easy Visual Task Transfer.

[3] Llava-Next-Interleave: Tackling Multi-Image, Video, and 3D in Large Multimodal Models.

[4] Qwen2-VL: Enhancing Vision-Language Model’s Perception of the World at Any Resolution.

### Questions
[1] What are the computational costs of using the V-T generator and T-V prompter modules, respectively?

[2] Are there some examples of failed feature visualizations?

[3] The overall quality of IQA images is related to both global and local information. The Visual Prompt (Task 2) in Figure 4 seems to rely too much on global information, which seems unusual. Could you explain why this might be the case?

### Soundness
3

### Presentation
2

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
This article proposes progressive instruction tuning to address the Explainable Image Quality Assessment problem. This method can solve the conflict problem when two types of datasets are jointly trained and achieve better multi-task training. The article also proposes bidirectional interaction between instruction and visual feature to further improve model performance. The proposed method has achieved excellent performance on multiple EIQA tasks.

### Strengths
1. This article is well written.
2. The proposed method performs well on some datasets.

### Weaknesses
1. In Table 1, Q-Adapt-3B is worse than Co-Instruct-8B with Co-Instruct dataset for training. Can you explain this phenomenon? Considering that Co-Instruct have more data than Q-Instruct. Does this mean that your method will fail (i.e., worse than Co-Instruct-8B) when the amount of data is large enough? If it is due to the amount of model parameters, is it possible to conduct a comparative experiment using the same LLM as Co-Instruct-8B?
2. Lack of ablations. From Table 7, i notice that joint training (69.73) is better that Perception training (68.89) but worse than Quality training (73.41) in Stage 1. However, there is a lack of only quality training experiments in Stage 2. So, i wonder if joint training is the best method in stage 2? What about joint training v.s. quality training in stage 2?

### Questions
Please comment the two points in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
