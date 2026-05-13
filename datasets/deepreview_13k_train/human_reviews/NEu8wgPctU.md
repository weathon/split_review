# AdaWM: Adaptive World Model based Planning for Autonomous Driving

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
World model based reinforcement learning (RL) has emerged as a promising approach for autonomous driving, which learns a latent dynamics model and uses it to train a   planning policy. To speed up the learning process, the pretrain-finetune paradigm is often used, where online RL is initialized by a pretrained model and a policy learned offline. However, naively performing such initialization in RL may result in dramatic performance degradation during the online interactions in the new task. To tackle this challenge, we first analyze the  performance degradation and identify two primary root causes therein: the mismatch of the planning policy and the mismatch of the dynamics model,  due to distribution shift. We further analyze the effects of these factors  on performance degradation during finetuning, and our findings reveal that the choice of finetuning strategies plays a pivotal role in mitigating these effects. We then introduce AdaWM, an Adaptive World Model based planning method, featuring two key steps: (a) mismatch identification, which quantifies the mismatches and informs the finetuning strategy, and (b) alignment-driven finetuning, which selectively updates either the policy or the model as needed  using efficient low-rank updates. Extensive experiments  on the challenging CARLA driving tasks demonstrate that AdaWM significantly improves the finetuning process, resulting in more robust and efficient performance in autonomous driving systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed a model-based planning method, AdaWM, to overcome the performance degradation between the offline pre-trained model and the online finetuned model. The authors first investigated the root of this issue, which are the distribution shift of both planning policy and dynamic model. Based on that, their proposed method AdaWM follows two steps for finetuning, by first identifying the the cause of the mismatch and then selectively updating the mismatched part via LoRA. The experiments are conducted on challenging Carla benchmark to demonstrate the effectiveness of the proposed method.

### Strengths
1. A motivating point-of-entry for analyzing distributional shift during adaptation in model-based planning for autonomous driving. Quantified by the distributional gap of dynamic model or planning policy, an adaptive finetuning framework (AdaWM) is proposed that selectively fine-tunes world model or planning policy given switch-based dominated mismatch assessment.
2. Analytical characterization and assessment of the performance gap for world model and planning policy. 
3. Improved adaptation results by AdaWM finetuning under several CARLA scenarios.

### Weaknesses
1. Unverified model configurations and experimental settings: 
*  The detailed setup for both the world model (dynamic) and the pretrained planning policy in AdaWM is unclear. Specifically, the architecture of the Recurrent State-Space Model (RSSM) used for the world model, including the dimensions of the latent state, the number of layers, and the activation functions, is not specified. Similarly, the structure of the actor-critic network used for the planning policy, such as the number of hidden layers, the size of each layer, and the specific optimization algorithm, is missing. This lack of detail makes it difficult to reproduce the results.
*  The paper lacks comprehensive configurations and descriptions of the experimental scenarios in CARLA. The specific sensor configurations (e.g., camera resolution, field of view, LiDAR parameters), the environmental conditions (e.g., weather, time of day), and the traffic density are not clearly defined. This makes it hard to assess the generality of the proposed method.
*  The metrics selected are not entirely objective, as key benchmarks such as Driving Score and Route Completion are missing. Additionally, using a self-defined reward cannot ensure objective measurement of performance degradation. The reward function's specific components and their relative weights are not provided, making it difficult to understand how the reward is related to the driving task and how it might influence the learning process.
2. Concerns regarding objectivity and completeness in experimental validation: 
* Lack of benchmarked results for AdaWM in CARLA, such as on Bench2Drive or CARLA Leaderboard-2. The absence of these standard benchmarks makes it difficult to compare the performance of AdaWM with other state-of-the-art methods in a fair and objective manner.
* Potentially unfair comparisons with other baselines, as AdaWM utilizes perfect BEV perception as input, whereas other baselines (e.g., VAD, UniAD) employ end-to-end pipelines with raw sensor inputs. This difference in input data makes the comparison less meaningful, as it does not evaluate the robustness of AdaWM to perception errors.
* Insufficient evaluation of generality in AdaWM's ablation studies. As a general pipeline for finetuning both the world model and planning policy, the results using various state-of-the-art models (e.g., VAD v1-v2, UniAD, TCP, PlanT) remain unclear. It is not clear how the proposed method would perform with different model architectures and training procedures.

### Questions
In addition to the following concerns that need to be addressed, several questions remain regarding the methodology and experiments:
1. Is the reward curve objective enough to reflect performance degradation? What if the reward is poorly crafted, or the adapted scenarios introduce a distributional shift in the reward? Further evaluation with metrics like driving score or success rate is recommended.
2.  How are \( C_1 \) and \( C_2 \) formulated in relation to Theorem 1? Additional clarification on the derivation would be helpful.
3. What is the purpose of introducing the switching strategy? How does it affect performance (e.g., driving score or the respective performance gap for the world model and policy) when both structures are adaptively fine-tuned?
4. How well does AdaWM perform in fine-tuning current well-known policies within the community?

### Soundness
3

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
3

### Summary
AdaWM introduces an adaptive world model-based planning method that selectively fine-tunes the policy and model to mitigate performance degradation. Theoretical analyses are provided, and experiments are conducted on well-known CARLA benchmarks.

### Strengths
- This paper makes it easy for readers to grasp the main idea.
- This paper includes theoretical analysis.

### Weaknesses
 - The author needs to provide visualizations of the model's prediction quality and trajectory planning quality to further demonstrate the model's performance.
- The author should compare more model-based/world model planning methods in autonomous driving. Because UniAD and VAD are end-to-end methods, and Dreamer is not specifically designed for autonomous driving setting.
- The method requires model and policy rollouts, which may introduce significant safety issues in the real world. Although this work addresses this by using simulation, the simulation domain gap may lead to out-of-distribution problems in real-world applications.
- The vehicle's driving behavior is not smooth, exhibiting jitter even on straight roads before turns, which is not suitable for real-world autonomous driving. This issue needs to be considered in the evaluation.
- The claim that the world model's adaptive nature provides an advantage for handling domain gaps needs more evidence. If the domain gap between simulation and real-world scenarios is too large, the trained world model might require retraining from scratch. The paper needs to address how the proposed method ensures better transferability.
- The comparison with UniAD and VAD is problematic since they use image-based inputs, while the author uses BEV inputs. This makes the comparison inherently unfair and does not adequately demonstrate the algorithm's advantages. A more detailed explanation of the input differences is needed.

### Questions
- What is the reason the author chose different fine-tuning methods for the policy and model?
- Is the BEV used by the author constructed from ground truth perception labels, or is it built directly using image inputs?
- Are the baselines trained on the ROM03, RTD12, LTM03, and LTD03 tasks?

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
AdaWM is an adaptive world model-based planning approach for autonomous driving. It leverages pretrained dynamics models and policies in the finetuning setup to accelerate the learning process. This is an interesting approach to address performance degradation caused by distribution shifts in driving environments. AdaWM achieves state-of-the-art results in CARLA simulations, with its alignment-driven finetuning improving both efficiency and robustness.

### Strengths
AdaWM presents a novel world model approach to handle distribution shifts during finetuning, identifying mismatches in the dynamics model and policy as the main causes of performance drops. With its mismatch identification and alignment-driven finetuning, AdaWM mitigates performance degradation. Extensive experiments in CARLA with challenging tasks demonstrate AdaWM’s clear advantage in both success rate and time-to-collision over baseline models.

### Weaknesses
The paper could discuss how AdaWM adapts to different task complexities, like high-density urban areas versus highways, as these may impact its adaptability and performance. This leaves some concerns about AdaWM’s robustness across highly divergent scenarios. Specifically, the evaluation lacks a detailed breakdown of performance across diverse scenarios, making it difficult to assess the method's strengths and weaknesses in different driving conditions. For example, how does the model perform in scenarios with frequent lane changes, complex intersections, or varying traffic densities? A more granular analysis would be beneficial.

Mismatch identification relies on total variation distance, which may add computational load in real time. It would be helpful to explore the complexity of this approach in more detail. The paper should provide a more thorough analysis of the computational cost associated with calculating the total variation distance, including its impact on the overall planning cycle. It would be beneficial to see a breakdown of the time spent on this calculation compared to other components of the system, as well as how this scales with the complexity of the environment.

The LoRA-based low-rank adaptation for dynamics model finetuning is described as efficient, but its effect on prediction accuracy and model stability is unclear. How does this method balance efficiency with the accuracy needed for real-time decision-making? The paper should include a quantitative analysis of the trade-off between the efficiency gains from LoRA and any potential degradation in prediction accuracy. It would be helpful to see how the rank of the low-rank adaptation affects both the computational cost and the prediction performance, and how this choice impacts the overall system performance.

Another potential concern is the generalizability and handling of corner cases. How does AdaWM handle extreme distribution shifts where the pretrained policies may not generalize well? The paper needs to address the limitations of the pre-trained policies when faced with significant distribution shifts. It would be useful to see experiments that specifically test the system's performance in scenarios that are far outside the training distribution, such as unusual weather conditions, unexpected road obstacles, or highly aggressive driving behaviors.

### Questions
Please refer to the questions in the weaknesses section.

### Soundness
3

### Presentation
4

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
This paper introduces **AdaWM**, a World Model-based planning method that uses an efficient finetuning strategy to adapt to new tasks  different from the pre-training tasks. 

The contributions of this paper are threefold: 

1. The authors identify two main reasons for WM-based planning model performance degradation when adapting to new tasks: *dynamics model mismatch* and *policy mismatch*. They propose a novel method to quantify the severity of these mismatches. 

2. An efficient finetuning strategy is proposed to adaptively update the dynamics model and policy based on the mismatch quantification. 

3. The authors validate the effectiveness of the proposed AdaWM method using the CARLA simulator.

### Strengths
This paper introduce a novel method to quantify the two mismatches that leads to performance degradation. The mathematical derivation process is impressive.

### Weaknesses
The weaknesses of the paper are threefold:

1. ***The introduction and motivation of the paper lack clarity and conciseness.*** The authors allocate a significant portion of the introduction to discussing embodied AI and world models, which serve as the research background for this paper. It is advisable to provide a more concise overview, as excessive content on these topics detracts from the overall clarity and quality of the writing. For instance, the first two paragraphs could be shortened to two or three sentences. Additionally, the section titled **A Motivating Example** could also benefit from condensation. 

2. ***The paper fails to adequately highlight the significance of its contributions and the necessity of the proposed method.*** After reviewing relevant studies, the authors should focus on clearly articulating the distinctions between their work and existing literature. Specifically, the authors should address the following questions, including but not limited to: (1) What distinguishes the proposed approach from existing methods reviewed? (2) Why can't the existing methods be directly applied to the tasks studied in this paper? (3) What challenges does this paper address that have not been solved by prior research? 

3. ***The selection of baseline methods is not appropriate.*** It is not fair to compare the performance of a model finetuned for a specific task against the pretrained baseline models that have not undergone fine-tuning for that same task. Because finetuning on a specific task undoubtedly enhances the performance of the pre-trained model. Therefore, comparison against existing un-finetuned baselines (such as UniAD, VAD, DreamerV3) cannot adequately demonstrate the advantage of the proposed method. The authors should include existing fine-tuning methods (e.g. the alternate fine-tuning, model-only fine-tuning, and policy-only fine-tuning mentioned in the motivating example, as well as studies by Feng et al. (2023), Baker et al. (2022), Hansen et al. (2022), and Ouyang et al. (2022) reviewed in the related works section) as baselines for fairer comparison.

### Questions
Apart from the questions mentioned in the weaknesses, I have two more questions:

1. What is the rationale behind the authors' choice to employ the Low-Rank Adaptation (LoRA) algorithm for model fine-tuning, particularly considering that more advanced state-of-the-art (SOTA) fine-tuning methods (such as QLoRA) have already been developed? Does this mean the selection of finetuning algorithm does not affect the final performance? If so, it would be more convincing to include an ablation study to compare the performance when the proposed AdaWM is finetuned with different finetuning algorithms.

2. In the measurement of the **Mismatch of Policy**, why do the authors calculate the state distribution shift? In deep reinforcement learning (DRL), the distribution difference of a policy should be assessed based on the differences in actions, as the state serves merely as the input to the policy while the action is the output. It would be better to explain how the approach of using state distribution shift compares to the more standard approach of using action differences.

### Soundness
3

### Presentation
3

### Contribution
3
