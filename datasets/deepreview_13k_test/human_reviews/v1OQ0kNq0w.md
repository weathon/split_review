# MotionRL: Align Text-to-Motion Generation to Human Preferences with Multi-Reward Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 6, 5, 5

## Abstract
We introduce \textbf{MotionRL}, the first approach to utilize Multi-Reward Reinforcement Learning (RL) for optimizing text-to-motion generation tasks and aligning them with human preferences. Previous works focused on improving numerical performance metrics on the given datasets, often neglecting the variability and subjectivity of human feedback. In contrast, our novel approach uses reinforcement learning to fine-tune the motion generator based on human preferences prior knowledge of the human perception model, allowing it to generate motions that better align human preferences. In addition, MotionRL introduces a novel multi-objective optimization strategy to approximate Pareto optimality between text adherence, motion quality, and human preferences. Extensive experiments and user studies demonstrate that MotionRL not only allows control over the generated results across different objectives but also significantly enhances performance across these metrics compared to other algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes incorporating human preference priors into the text-to-motion task to enhance the quality of generated motions. Through the use of reinforcement learning and a motion perception model, the paper construct a human preference reward, enabling the generation model to learn human perception. To prevent degradation in other performance metrics resulted by human preference reward, the paper introduces a motion quality reward and a text adherence reward, forming a proposed multi-reward system. To mitigate potential training instability caused by multiple rewards, Pareto optimality is employed to balance the different rewards. The experimental results demonstrates superior performance in FID, R-Precision, human perceptual model scores, and user studies.

### Strengths
This paper introduces human preference into the text-to-motion generation task by applying a motion perception model from the motion generation field. Additionally, two other rewards (text adherence and motion quality) are used to prevent potential degradation caused by the human preference reward. Experimental results demonstrate the superiority of the proposed approach.

### Weaknesses
The most concerning limitation of this paper lies in its novelty. Introducing human perception into the field of motion generation is not novel, as also mentioned by this paper in line#86-87 (Voas et al., 2023; Wang et al., 2024). Wang et al. utilizes their proposed motion perception model as an effective supervision signal to finetune the motion generator. This paper similarly uses the motion perception model from Wang et al. as a supervision signal to train model for motion generation. Given these, the technical novelty is limited.

There are also insufficiencies in the experimental section: **1)** The main insufficiency is that the ablation study does not adequately demonstrate the effectiveness of the proposed multiple rewards. Table 2 lacks a baseline ablation result with no rewards applied, making it difficult to confirm the method’s effectiveness. **2)** In text-to-motion generation tasks, methods are typically validated on both the HumanML3D and KIT-ML datasets, but this paper only provides results for HumanML3D. **3)** Additionally, on the HumanML3D dataset, the MModality metric is usually reported; however, this paper neither provides MModality results nor explains why it was omitted. **4)** For the Diversity metric, Diversity closer to real test data is preferable, yet this paper labels higher values as better.

Minor comments:
1. The paper does not explain the metrics reported in the tables, such as Diversity.
2. The “Conclusion and Future Work” section does not include future work but instead links to the appendix.
3. Descriptions for figures should not be placed in the appendix; for example, <mm> and <mt> in Fig. 5 lack explanation in the main text.

### Questions
1. “Aligning Motion Generation with Human Perceptions” by Wang et al., 2024, utilizes their proposed motion perception model as an effective supervision signal for training a motion generator. This paper similarly uses the motion perception model from Wang et al.  as a supervision signal to aid motion generation. What are the distinction and novelty of this paper's method compared to the approach of Wang et al.?
2. The use of **skeleton** rendering in the user study section for evaluation could be more reasonable, as there is a gap between **skeleton** and **SMPL** rendering. Some unnatural details are more noticeable in SMPL, using SMPL rendering for the user study might be more convincible.

### Soundness
2

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
3

### Summary
The paper introduces a novel approach that leverages Multi-Reward Reinforcement Learning to optimize text-to-motion generation tasks. Unlike previous methods that primarily focus on numerical performance metrics, MotionRL incorporates human preferences to enhance the alignment of generated motions with human perception. The approach uses a multi-objective optimization strategy to balance text adherence, motion quality, and human preferences, aiming for Pareto optimality. Extensive experiments and user studies demonstrate that MotionRL significantly outperforms existing methods in generating high-quality, realistic motions that align well with textual descriptions and human feedback. This work represents a significant advancement in the field of text-driven human motion generation, offering a more nuanced and human-centric approach to evaluating and improving motion quality.

### Strengths
Human-Centric Optimization: MotionRL uniquely incorporates human preferences into the optimization process, ensuring that the generated motions align better with human perception. This focus on human feedback addresses the limitations of traditional metrics that may not fully capture the nuances of human motion quality.
Multi-Objective Optimization: The use of a multi-reward reinforcement learning framework allows MotionRL to balance multiple objectives simultaneously, such as text adherence, motion quality, and human preferences. This approach ensures that the generated motions are not only accurate and high-quality but also meet the subjective preferences of users.
Pareto Optimality: MotionRL introduces a novel multi-objective optimization strategy to approximate Pareto optimality. By selecting non-dominated points within each batch, the model learns to balance different rewards effectively, leading to more stable and optimal training outcomes. This method enhances the overall performance across various metrics compared to other algorithms.

### Weaknesses
Dependence on Pre-trained Perception Models: MotionRL relies on pre-trained human perception models to capture complex human perceptual information. If these models are not of high quality or do not accurately reflect human preferences, the performance of MotionRL could be significantly impacted. This dependency limits the flexibility and robustness of the approach.

Limited Dataset Size: The text-to-motion domain typically has smaller datasets compared to other fields like image or text generation. This limitation makes the model more sensitive to small changes in input text and can lead to overfitting. The smaller dataset size also poses challenges in effectively training the model to generalize well across diverse motion scenarios.

Complexity of Multi-Objective Optimization: While the multi-reward optimization strategy aims to balance text adherence, motion quality, and human preferences, it introduces significant complexity into the training process. Managing and fine-tuning multiple rewards can lead to unstable training and requires careful calibration to ensure that the model does not prioritize one objective at the expense of others. This complexity can make the approach less accessible and harder to implement effectively.

### Questions
How does MotionRL handle the trade-offs between text adherence, motion quality, and human preferences during the training process?

What are the limitations of relying on pre-trained human perception models for aligning generated motions with human preferences, and how can these limitations be addressed in future work?

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
3

### Summary
The paper "MotionRL: Align Text-to-Motion Generation to Human Preferences with Multi-Reward Reinforcement Learning" introduces MotionRL, a framework that leverages Multi-Reward Reinforcement Learning to enhance text-to-motion generation by aligning outputs with human preferences. Unlike prior models, MotionRL incorporates human perceptual data in its reward structure to address limitations in previous approaches focused on numerical metrics alone. MotionRL employs a multi-objective optimization strategy to achieve a balance between text adherence, motion quality, and human preferences, approximating Pareto optimality for optimal trade-offs. The authors demonstrate the model's effectiveness through extensive experiments and user studies, showing MotionRL's superior performance in terms of perceptual quality and alignment with human expectations.

### Strengths
The paper introduces a novel approach by combining reinforcement learning with human preference alignment for text-to-motion tasks, which is an underexplored area in motion generation. The application of multi-reward RL to text-to-motion represents a good contribution, especially as it integrates human perceptual feedback.

### Weaknesses
The model’s reliance on pre-trained perception models, as mentioned in the limitations, could restrict generalizability. Fine-tuning without additional human annotations might limit the model’s adaptability to new or unique datasets, where the pre-trained perception model may not fully capture the nuances of human preferences.

While the multi-reward RL framework is effective, there is limited discussion on dynamically adjusting the weight of each reward in real-time based on specific user feedback. A more adaptive reward weighting mechanism could further enhance user-centered customization.

Although the human preference model provides valuable perceptual data, additional insights from continuous human interaction could help refine the model further. The paper would benefit from exploring how human feedback could be iteratively incorporated to improve long-term model performance, potentially through ongoing human-in-the-loop adjustments.

### Questions
Could the authors elaborate on the potential for dynamically adjusting the weighting of rewards based on real-time feedback?

How does the model handle scenarios where text descriptions are ambiguous or open to interpretation? Is there a mechanism to weigh certain rewards more heavily in such cases?

For practical applications, are there plans to develop more user-friendly interfaces for non-technical users to fine-tune MotionRL’s generated motions?

Please also provide some details about the dataset you created

### Soundness
2

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
4

### Summary
The paper offers MotionRL, an approach for optimizing text-to-motion generation tasks using Multi-Reward RL. This method aims to align the generated motions with human preferences more effectively than traditional models by incorporating human perceptual models into the RL training process. This is done by employing a multi-objective optimization strategy to balance text adherence, motion quality, and human preferences, approximating Pareto optimality. The paper provides experiments, demonstrating that the proposed model outperforms baselines on traditional metrics and in user studies assessing human perception.

### Strengths
* Introducing RL with the set of reward functions to optimize for multiple objectivesin text-to-motion generation seems to be a novel approach to that specific domain.

* The idea is simple and easy to understand which is also further improved by a good presentation and writing. The images helps me understand what is the problem you're trying to solve.

* I find the ablation in table 2 important as it shows that human perception does not always align with the metricses typically used.

### Weaknesses
* The overall novelty of the method is modest at best, but the domain application seem to be novel.

* There is a great lack of details about the user study and "volunteers for evaluation" could mean anyone. Given that the participants was called "volunteers" (and not paid?) it seems like it's not randomly recruited people which makes it hard to evaluate the soundness of the user study. 

* The paper uses up all 10 pages but given that it's a simple idea with limited technical contribution I think it's excessive, especially since the limitation was pushed to the appendix.

### Questions
* How did you come up with the balance between the three different rewards?

* How is the pareto-based policy gradient optimization different from simple PPO?

* What is the demographic data for the user study, did you do any formal survey? 

Minor things:
- You introduce the abbreviation "RL" multiple times in the text
- Line 200: the Appdix -> the Appendix

### Soundness
3

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
This paper introduces MotionRL, a reinforcement learning (RL)-based framework for multi-objective optimization in human motion generation. Recognizing that prior methods often overlook human perceptual nuances, MotionRL integrates human perceptual priors into the generation process through a reward structure. The framework balances three objectives: human perception, motion quality, and text adherence. To address the challenges of optimizing multiple objectives, MotionRL incorporates a multi-reward optimization strategy that approximates Pareto optimality by selecting non-dominated points in each batch, ensuring better trade-offs across objectives.

### Strengths
The experimental metrics show good results, and a motion generation framework based on RL has been designed.

### Weaknesses
The reason for introducing RL is not well explained.

### Questions
1. In line 95, it seems that the purpose of introducing RL is merely to supervise human preference, and the rationale for using RL isn’t well explained.

2. The concept of Pareto optimality lacks a citation—what specific issue does this?

3. There are factual inaccuracies in the stated contributions, as ReinDiffuse appears to have introduced RL into motion before this paper.

4. The supplementary materials don’t clearly explain their purpose, which only provides some generated samples. 

5. The paper contains several grammatical errors. The title should change "Align" to "Aligning". A layout issue in line 292.

### Soundness
2

### Presentation
1

### Contribution
2
