# Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Graphical User Interfaces (GUIs) are critical to human-computer interaction, yet automating GUI tasks remains challenging due to the complexity and variability of visual environments. 
Existing approaches often rely on textual representations of GUIs, which introduce limitations in generalization, efficiency, and scalability. 
In this paper, we introduce \ourmodel, a unified pure vision-based framework for autonomous GUI agents that operates across various platforms. 
Our approach leverages image-based observations, and grounding instructions in natural language to visual elements, and employs a consistent action space to ensure cross-platform generalization. 
To address the limitations of previous work, we integrate explicit planning and reasoning within the model, enhancing its ability to autonomously navigate and interact with complex digital environments. 
We construct a large-scale dataset of GUI agent trajectories, incorporating multimodal reasoning and grounding, and employ a two-stage training pipeline that first focuses on general GUI grounding, followed by planning and reasoning. 
Through comprehensive experiments, we demonstrate that \ourmodel surpasses previous state-of-the-art methods in both offline and real-world online scenarios, achieving, to our knowledge, the first fully autonomous pure vision GUI agent capable of performing tasks independently without collaboration with external closed-source models. 
We will open-source all datasets, models, and training recipes to facilitate future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
AGUVIS is a novel framework for building autonomous agents that interact with Graphical User Interfaces (GUIs) using a purely visual approach. AGUVIS utilizes image-based observations and grounding and by employing a unified action space with a plugin system, AGUVIS can operate across various platforms.

### Strengths
1. Extensive evaluations on different benchmarks;
2. Promising performances on benchmarks;
3. Interesting to see the usage of pyautogui as the bridge to unify the action space.
4. Promised to open-source (not yet)

### Weaknesses
1. overall, I did not find much difference compared to previous methods like AMEX, SeeClick, etc. They also use the pure-vision representation and use the both grounding and planning dataset to train the GUI agents.
2. The authors proposed to use the VLM to construct the CoT dataset, but how are the gains? Will the CoT training will additional performance gain? 
3. The author chose the pyautogui to unifiy the action space, but the experiments did not give the readers some examples to showcase its advantages, something like how this could help to adapt to some new actions?

### Questions
1. In table Six, how about only training with stage 2?
2. How can AGUVIS be applied to real-world scenarios beyond the evaluated benchmarks? Like closing the ads
3. I am very curious that what's the reason behind the model size choice, like in Table 4 and Table 5, Grounder is 7B, while when e2e it is 70B? 
4. When deployed for Phone and Web, should we have some specific designs respectively?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces AGUVIS, a unified, vision-based framework for autonomous GUI agents across multiple platforms. It begins by organizing existing GUI-related datasets and applying carefully designed data augmentations, especially for incorporating low-level reasoning into the existing datasets. The authors then train Qwen2-VL on these organized datasets in two stages: grounding and planning. Experiments conducted on various datasets, including, screenspot, mind2web, etc.,  demonstrate promising results.

### Strengths
- The motivation is reasonable. The model should be able to reason before performing grounding and GUI automation tasks. It is also a good idea to incorporate such data in the training stage.
- The organized datasets are valuable. The authors collect most of the existing datasets and the augmentation strategy is interesting.
- The performance is quite promising across several benchmarks, even surpassing very recent papers just released with a large margin.

### Weaknesses
1. The formalization presented by the authors is generally good. However, there is one point that needs clarification.
 **Line 123:** The update of "its belief state b_t" is mentioned, but it's unclear which specific part of the model this refers to. This needs further elaboration as it can be confusing.

**Major Concerns.** The primary contribution of this paper is the introduction of the AUGVIS collection which is then used to train Qwen2-VL. However, several crucial details are missing:

2. The authors mention using a VLM to generate the inner monologue for each step in the trajectory. However, it is unclear **which VLM** was used. Current VLMs, including GPT-4o, tend to perform poorly in understanding screenshots, as evidenced by their results in later experiments. **How was the data quality ensured to be reliable?** What is the approximate **accuracy**?

3. The paper mentions that the prompt includes various elements. However, it is unclear how the information is organized and it would be better to just show some **the specific prompt used**.

4. What does the **Planning & Reasoning Trajectories** look like? The authors highlight it in the paper, but I didn't find any examples, so it's difficult to determine how it differs from existing ones. The authors should visualize some samples.

Experiments:

5. The setting of "self-plan" in the ScreenSpot mentioned in the text is somewhat unclear. The author notes that models are required to generate plans based on the original instructions. Specifically, how is this done, and what is the prompt given to the planner? From the results, it is evident that simply adding this mechanism leads to a significant performance improvement, which is excellent. However, the author also needs to analyze the reasons behind this improvement.

6. From Table 6, it seems that the results from Stage 1 training do not significantly impact Mind2Web, as the results for (a) AGUVIS-G and (b) Qwen2-VL are quite similar. However, in Table 1, we can see a noticeable improvement in AGUVIS-G's results in ScreenSpot after Stage 1 training. Could the authors explain the reason for this? Could it be related to the benchmark settings?

7. This work is based on a stronger backbone, Qwen2-VL, compared to others. The author should more clearly highlight the performance improvements contributed by this work. For instance, low-level instructions are a significant contribution. In addition to testing Qwen2-VL (zero-shot) and the final model on ScreenSpot, could a variant be trained without low-level instructions?

8. The authors should add more training details about the proposed model over Qwen2-VL, for example, which modules are frozen, GPU hours, etc.

### Questions
1. What is the difference between "Qwen2-VL" and "AGUVIS-G-7B" in Table 1? The former is zero-shot, correct?
2. I notice that sometimes it’s written as AGUVIS and other times as AUGVIS. Is this intentional, or is it a typo?
3. What is the backbone model of "Choice" Gounder? It should be driven by an LLM, correct?
4. In Table 6, AGUVIS-7B's performance is slightly different from that in Table 2. Is this due to some test setting issues?
5. Is AGUVIS-7B compatible with other LLMs like GPT-4? I see different grounding models with LLM; can AGUVIS-7B also achieve this?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents AGUVIS, a vision-based framework for developing GUI agents. The authors compile datasets from various sources to cover multiple platforms, standardize them with a unified action space, and enhance them with intermediate planning steps and actions. They leverage a well-chosen vision-language model (VLM) within a two-stage training paradigm to create a visual-based GUI agent. The framework is evaluated on both offline and online GUI benchmarks, demonstrating promising results.

### Strengths
1. Performance: AGUVIS achieves strong performance across multiple benchmarks, including ScreenSpot, Multimodal Mind2Web, and Android Control, highlighting its versatility in visual-based agent applications.
2. Methodological Contribution: The paper offers a comprehensive roadmap for building robust visual-based agents, focusing on data curation and model training strategies.
3. Clarity: The paper is well-written and straightforward to follow, making complex concepts accessible to readers.

### Weaknesses
 **1. Limited Novelty:** The main contribution of this paper is to pre-train VLMs with massive data combinations, but lack insights and are computationally intensive. Although AGUVIS successfully integrates existing datasets for vision-based GUI model training, it neither introduces new datasets nor proposes a novel module design.
Insufficient Detail in Key Areas:

**2. Data Curation (Augvis Collection)**
- Data collection and curation are crucial to this work, yet important details are omitted. For example, what specific VLM is used for generating inner monologue components? How is the accuracy of the generated observation descriptions, thoughts, and low-level action instructions ensured?
- Training and Implementation Details: The two-stage training procedure lacks sufficient description. Key aspects, such as the training schedule for each stage, are unclear. Additionally, in Stage 2, it would be helpful to explain how inputs like observations, thoughts, action histories, and observation histories are organized. Are there truncation strategies to handle long sequences? Supplementary figures illustrating these aspects would enhance clarity.

**3. Lack of Analysis** Further analysis would improve the clarity and depth of the paper:
- Unexpected Model Behavior on ScreenSpot: The self-planning model’s outperformance over the original instructions version on ScreenSpot is surprising, given that the ScreenSpot task involves simple grounding queries. Does this imply overfitting to Stage 2 training patterns? How does the model perform after Stage 1 training alone? Providing examples of the model’s planning outputs could deepen this analysis.
- Justification for Two-Stage Training: There is no experimental evidence supporting the decision to employ a two-stage training paradigm. Why not combine both stages into a single training pipeline?
- Effectiveness of Inner Monologue: The paper lacks evidence demonstrating the contribution of the VLM-generated inner monologue component to overall performance. The observed degradation in performance without Stage 2 training could simply result from training on more data rather than specifically leveraging inner monologue components.

### Questions
- Could the authors clarify the specific VLM used for generating inner monologue components? What measures ensure the accuracy of generated observations, thoughts, and action instructions?

- For Stage 1 training, does the grounding-packing strategy employ a causal attention pattern for the packed sequence, or is there a customized attention mask to prevent attention between different grounding samples?

### Soundness
3

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
This paper proposes Aguvis, a UI agent capable of understanding and interacting with multiple types of digital devices. The authors recognize the existing challenges, such as redundancy in textual representations and heterogeneity in action spaces across platforms, in UI agent research. To tackle these challenges, the authors organize existing datasets while unifying the agent's action space across mobile phones, web browsers, and desktop software. Besides, the authors introduce a two-stage training method to enhance the understanding and planning capabilities of the Aguvis agent. Comprehensive experiments are conducted to justify the authors' designs.

### Strengths
1. The authors conduct comprehensive experiments across multiple digital platforms.
2. The writing is neat and the paper is easy to follow.
3. The authors introduce a key design, i.e., integrating planning with action grounding, which overcomes the limitation of existing planning-then-grounding methods.

### Weaknesses
1. The reviewer doubts that the authors' method, Aguvis, effectively addresses two of the three challenges (i.e., Enhancing Pure Vision Framework, and Unification Across GUI Environments) in the Intro section.
1.1 To tackle the first challenge, the authors utilize an agent framework with pure vision input and curate multi-platform datasets to train the agent. However, the authors have not conducted ablation studies on the impact of introducing these datasets listed in Tables 9 and 10, thereby providing no practical insights into whether simply combining a pile of datasets can benefit all device domains. The authors are expected to isolate the datasets from different device domains to justify that it is unifying the observation, instead of simply increasing the data amount, that contributes to the final performance gains. Specifically, the paper lacks experiments to show that training on a combination of web, mobile, and desktop data provides a synergistic effect compared to training on each domain separately. The authors should demonstrate that the unified vision input benefits from diverse data, rather than just more data.
1.2 To unify the action space, the authors design a set of pyautogui functions as a union of the allowed actions across platforms. However, the authors still have not conducted ablation studies to justify this design. The authors are expected to conduct detailed ablation experiments to confirm that unifying action spaces is better than using the specialized action space of each device type. For example, the authors should compare the performance of using a unified PyAutoGUI action space against using separate action spaces tailored to each environment (e.g., web, mobile, desktop).

2. The authors introduce several special designs to improve the agent's performances, but fail to provide solid experiments to justify them. For example, L248 states that 'This approach significantly accelerates training by maximizing the use of each image without compromising accuracy', but the experiment confirming this point is nowhere to be seen. Additionally, the expression 'we assume ...' in L250 renders the paper informal and unsolid. The authors cannot say this in an academic paper if no experiments justify that the GUI understanding capability is authentically  "robust". The claim about accelerated training needs empirical validation, and the assumption about robustness requires experimental support, not just an informal statement.

3. The authors generate reasoning steps in the training data (L203). However, no experiments are conducted to prove the usefulness of this innovation. The paper lacks a clear ablation study to demonstrate the impact of these reasoning steps on the final performance. It is unclear if the reasoning steps are truly beneficial or if the performance gains are due to other factors.

4. The experiments that compare Aguvis with existing UI grounding models are not fair enough. In Table 1, the Aguvis finetuned on Qwen2-VL (a strong VLM pretrained with massive UI data) is compared with UGround and SeeClick, which are based on VLMs without being pretrained with massive UI data. This comparison is believed to be unfair and hard to demonstrate the superiority of Aguvis. The authors are suggested to organize the experiment more carefully. The comparison should be done with models of similar pretraining data and capacity to isolate the effect of the proposed method.

5. No qualitative experiments, nor visualized examples are presented, making it hard for readers to understand the differences between Aguvis and existing methods. The paper would greatly benefit from visual examples showing how Aguvis interacts with different UI elements and how its performance differs from existing methods. This would provide a more intuitive understanding of the proposed approach.

### Questions
1. L152 states "Generally, the input length of accessibility tree observation is 6k tokens, and HTML is 4k tokens". Which data source is used to calculate these statistics?

2. Why do the authors not report the Step SR of CogAgent in Table 2?

3. What will the performance of Aguvis be on the UI planning benchmarks if Aguvis is trained with only stage 2?

4. Typos: Framwork (L51)

### Soundness
3

### Presentation
2

### Contribution
2
