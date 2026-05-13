# Task-agnostic Pre-training and Task-guided Fine-tuning for Versatile Diffusion Planner

- Decision: Reject
- Scores: 5, 5, 6, 5, 3

## Abstract
Diffusion models have demonstrated their capabilities in modeling trajectories of multi-tasks. 
However, existing multi-task planners or policies typically rely on task-specific demonstrations via multi-task imitation, or require task-specific reward labels to facilitate policy optimization via Reinforcement Learning (RL). To address these challenges, we aim to develop a versatile diffusion planner that can leverage large-scale inferior data that contains task-agnostic sub-optimal trajectories, with the ability to fast adapt to specific tasks. In this paper, we propose \textbf{SODP}, a two-stage framework that leverages \textbf{S}ub-\textbf{O}ptimal data to learn a \textbf{D}iffusion \textbf{P}lanner, which is generalizable for various downstream tasks.
Specifically, in the pre-training stage, we train a foundation diffusion planner that extracts general planning capabilities by modeling the versatile distribution of multi-task trajectories, which can be sub-optimal and has wide data coverage. Then for downstream tasks, we adopt RL-based fine-tuning with task-specific rewards to fast refine the diffusion planner, which aims to generate action sequences with higher task-specific returns. Experimental results from multi-task domains including Meta-World and Adroit demonstrate that SODP outperforms state-of-the-art methods with only a small amount of data for reward-guided fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel framework called SODP, designed to train a multi-task diffusion planner using sub-optimal data. SODP aims to reduce dependency on task-specific labeled data through a two-stage training process. Initially, a diffusion model is pre-trained without the need for task-specific rewards or demonstrations. Subsequently, the model undergoes a second stage of online interactive reinforcement learning-based fine-tuning to rapidly refine its capabilities. The effectiveness of this methodology is validated on two multi-task domains: Meta-World and Adroit. Experimental results show that SODP outperforms the considered baseline methods, highlighting its potential in multi-task learning environments.

### Strengths
1. The paper is well-written and includes illustrative figures that aid comprehension.

2. It reports that SODP not only surpasses baseline methods in performance but also shows rapid convergence and robustness across diverse tasks and input modalities. Additionally, the included ablation study offers valuable insights into the design and effectiveness of the proposed methods.

### Weaknesses
My primary concerns arise from the evaluation protocols, specifically:

1.	Was the fine-tuning stage also applied to the baseline methods? If not, this might represent an unfair comparison, as all baselines are trained on sub-optimal data while SODP gains an advantage from an additional online fine-tuning stage.
2.	Regarding the Adroit task, was the 3D visual feature process (from DP3) also employed for the Diffusion Policy in Table 2? Moreover, what is the performance of SODP when this process is not utilized?

### Questions
1. Is the 3D visual feature process not compatible with MTDIFF? Have the authors tried combining the 3D visual feature process with MTDIFF on the Adroit task?
2. What does the vertical orange dashed line indicating in Figure 4?

### Soundness
3

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
SODP is a two-stage diffusion-based framework designed to enhance multi-task planning in reinforcement learning. This framework comprises a pre-training phase that leverages large-scale, sub-optimal, task-agnostic data to learn a broad range of behaviors and a fine-tuning phase that uses task-specific rewards for adaptation. The pre-trained model captures general action patterns, allowing it to rapidly adapt to diverse tasks through fine-tuning, guided by reinforcement learning techniques. SODP demonstrates improved generalization in handling diverse tasks with minimal task-specific data and outperforms existing methods on benchmarks like Meta-World and Adroit.

### Strengths
* It leverages sub-optimal, task-agnostic data for pre-training, which contrasts with traditional reliance on task-specific demonstrations or expert data.
* The proposed behavior-cloning (BC) regularization in the fine-tuning stage offers a creative solution to the problem of model drift, allowing the model to maintain useful pre-trained capabilities while adapting to new tasks.

### Weaknesses
 * Action and State Space Limitations: SODP requires tasks to share the same action space, limiting adaptability to tasks with different action spaces. It’s unclear how the method handles varying state space dimensions. Specifically, the paper does not discuss how the diffusion model's input and output layers are adapted when the action space dimensionality changes, which is a critical consideration for real-world applications involving diverse robotic systems. Furthermore, the method's reliance on a fixed state space representation raises concerns about its applicability to tasks with varying sensor modalities or observation spaces. For instance, a robot might use different sensors (e.g., cameras, lidar, tactile sensors) across different tasks, resulting in heterogeneous state representations that are not directly compatible with the proposed framework.

* Typographical Errors: There are minor errors, such as $a_0^t$ in Line 215, which should be $a^0_t$.

* Dependence on Online Fine-tuning: SODP relies on an online environment for fine-tuning, which may limit practical applications. The paper also lacks details on the number of fine-tuning steps and associated costs. The reliance on online fine-tuning is a significant limitation, as it necessitates real-time interaction with the environment, which can be expensive and time-consuming, especially for complex robotic tasks. The paper does not provide a clear analysis of the computational resources required for fine-tuning, making it difficult to assess the practical feasibility of the proposed approach. Furthermore, the lack of details on the number of fine-tuning steps makes it challenging to reproduce the results and compare them with other methods.

### Questions
* For different tasks with different state spaces, how to train these different tasks?
* After fine-tuning the pre-trained model on the specific task, can you evaluate the performance of the fine-tuned model on the other tasks? I'm very concerned that the catastrophic forgetting of the model has been addressed.
* Can you explain how to select the target policy in details?

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
3

### Summary
This paper introduces SODP, a two-stage framework for training versatile diffusion planners for robotic manipulation tasks. The framework first pre-trains a diffusion model using large-scale sub-optimal data from multiple tasks without reward labels, then fine-tunes it for specific downstream tasks using policy gradient optimization with a novel BC regularization.

### Strengths
Pros:

- The paper is well-written with clear organization and easy to follow.

- The fine-tuning stage presents a systematic design, particularly in its BC regularization mechanism that effectively balances between preserving pre-trained knowledge and exploring new high-reward behaviors, supported by comprehensive ablation studies comparing different regularization strategies.

### Weaknesses
Cons:
1. While the paper claims using sub-optimal data for pre-training as an innovation, there appears to be no specialized design or methodological advancement in handling such data. The pre-training stage follows standard diffusion model training procedures, identical to those used with expert demonstrations.  Specifically, the method does not address the potential issues of noisy or inconsistent transitions present in sub-optimal data, such as how to weight or filter these transitions during training to prevent the diffusion model from learning poor action priors. The paper should clarify how the diffusion model handles the variance and potential biases introduced by sub-optimal data compared to expert demonstrations.
2. A significant concern arises regarding the fairness of experimental comparisons. First, the learning curves in Figure 4 only display fine-tuning steps while omitting SODP's substantial pre-training phase (5e5 steps), potentially understating the total computational requirements. This makes it difficult to assess the true efficiency of the proposed method. Second, the paper fails to clarify whether baseline methods undergo pre-training or have access to online data collection during training. This is particularly important as SODP benefits from continuous online data collection to build its target policy, which may give it an unfair advantage if baselines are limited to offline data. The lack of detail regarding the baseline training procedures makes it difficult to ascertain whether the performance gains are due to the proposed method or simply due to more favorable training conditions.
3. A fundamental limitation is that the paper fails to isolate whether the performance gains stem from sub-optimal data pre-training or from the online data collection during fine-tuning. Critical control experiments are missing, particularly (1) fine-tuning with high-quality offline data and (2) direct training with high-quality data without pre-training. Without these comparisons, it remains unclear if the proposed two-stage framework and the use of sub-optimal data are truly necessary, as the improvements might simply result from the continuous collection of high-quality samples during online fine-tuning. The paper needs to demonstrate that the pre-training phase with sub-optimal data provides a tangible benefit over simply training from scratch or using high-quality data directly.
4. A direct empirical comparison between optimal and sub-optimal pre-training data is missing. Specifically, the paper should compare the current approach (using the first 50% of SAC training data) with a variant using high-reward trajectories (e.g., the last 30% of converged SAC data) for pre-training. This would help validate whether sub-optimal data is truly sufficient or if optimal data would lead to substantially better performance. The paper should also explore the impact of varying the quality of the sub-optimal data, for example, by using different percentages of the SAC training data or by introducing artificial noise into the sub-optimal dataset.
5. Why not directly BC in finetune phase. Since the method already collects high-reward trajectories during online interaction for BC regularization, why not directly fine-tune the pre-trained model using imitation learning on these trajectories? This simpler approach might achieve similar performance without the complexity of MDP formulation and policy gradient optimization. Without this comparison, it's unclear whether the proposed fine-tuning framework provides substantial benefits over straightforward behavior cloning of high-reward samples. The paper should also investigate the sensitivity of the method to the choice of BC regularization coefficient and provide a justification for the chosen value.

### Questions
See weakness. 
I believe that more experiments are needed to illustrate the soundness and Contribution of the paper's SETTINGS and Designs.

### Soundness
2

### Presentation
3

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
This paper proposes a pre-training and fine-tuning method, SODP, for diffusion planner. The model is pre-trained on sub-optimal and multi-task data offline. Unlike reinforcement learning approaches, the pre-training stage does not require rewards. Additionally, the model is designed to operate without task descriptions or trajectory returns as conditions. The authors aim to show that generalizable capabilities can be acquired from multi-task sub-optimal data in pre-training, providing helpful knowledge for task-specific fine-tuning in an online reinforcement learning setting.

### Strengths
1. The approach of using sub-optimal, multi-task trajectories for pre-training to enhance downstream task performance after fine-tuning is interesting.
2. The paper offers a comprehensive discussion on various regularization techniques during fine-tuning, and the experiments show that the proposed BC-regularization method effectively balances reward maximization with preventing performance collapse.

### Weaknesses
 1. Clarification is needed on whether both multi-task and sub-optimal data in pre-training equally contribute to improved fine-tuning performance for specific tasks.
    1. There is no experiment using only single-task sub-optimal data for pre-training. Although previous work [1] suggests that multi-task diffusion planners outperform single-task setups, the setting in this paper is different, involving both pre-training and fine-tuning. It remains unclear whether multi-task data specifically benefits downstream RL fine-tuning or if the model could already gain useful patterns from sub-optimal data by training on the same task as the target downstream task. If this is the case, unrelated tasks in pre-training may be redundant. Thus, experiments or analyses are needed to separate the contributions of multi-task data versus sub-optimal data, at least for a few representative tasks.
    2. The choice of using 50% and 30% of experiences collected from RL agents' replay buffers in Meta-World and Adroit needs to be explained. Additionally, results from varying the ratios of experience while keeping the total number of pre-training transitions fixed would be valuable. This analysis could clarify if there is a trade-off between fine-tuning performance and the quality of pre-training data (i.e. if using lower-quality data for pre-training negatively impacts fine-tuning). A comparison between fine-tuning results using expert data (100% experience) versus sub-optimal data with the exact transition count would be especially insightful.
2. Key baselines are missing, and the baselines used in state-based and image-based environments are inconsistent.
    1. Since online interactions with the environment are allowed in the fine-tuning stage, online RL methods should be included for a fair comparison. Currently, only BC and offline RL are used as baselines.
    2. Both BC and offline RL methods are compared in Meta-World, whereas offline RL methods are excluded in Adroit.
    3. Given that diffusion-based policies in BC, offline RL, and online RL [2-7] have shown strong performance compared to non-diffusion methods in prior work, including offline and online diffusion-based RL baselines would offer a more complete comparison for evaluating the fine-tuning approach with online RL for the diffusion model.
    4. Overall, the most critical baselines to prioritize, in both image and state-based environments, would be online RL (non-diffusion, such as PPO) and diffusion-based offline and online RL methods [2-7]. Including these baselines would allow for a fairer comparison by incorporating methods that offer strong modeling capabilities with diffusion and interaction with the environment.
3. The problem setting for sub-optimal data collection may lack precision, as in line 52, “sub-optimal data can be easily obtained in the real world.” Concrete examples or scenarios of how sub-optimal data might be collected in real-world settings would be helpful. Discussing potential challenges or limitations of these collection methods would provide readers with a clearer understanding of the motivation’s validity.
    *  Currently, the experimental setup collects sub-optimal data by training RL agents and treating part of the replay buffer as "inferior data." However, without rewards, identifying data that qualifies as sub-optimal could be challenging or even infeasible, especially since, as noted in line 153, “reward labels may be scarce or costly to obtain.” If rewards were readily accessible in the offline data or during interaction with the environment, then a diffusion planner could be directly trained using offline or online RL methods [2-7], and pre-training on reward-free sub-optimal data might no longer be necessary. This raises questions about the practicality of the motivation and problem setting proposed in the paper. It would be more meaningful if data with mixed or random levels of inferiority—without requiring a curated collection mechanism—could still enhance downstream fine-tuning during pre-training.
4. Several descriptions are either inconsistent or need further clarification:
    1. The claim in line 362, “The baselines used in Meta-World struggled to handle this high-dimensional data structure,” lacks supporting analysis or experimental evidence. Where in the paper is this conclusion demonstrated?
    2. Are all baselines for Meta-World evaluated in a multi-task setting, while those used in Adroit are in a single-task setting? Additionally, what does "Simple DP3" in Table 2 refer to? This term is not explained anywhere in the paper.
    3. There are inconsistencies in the experimental setup descriptions. In Sec. 5.1 (EXPERIMENTAL SETUP), line 344 states, “All baselines and our pre-training stage are trained on the same dataset” for Meta-World, while line 346 states, “All baselines are trained on expert demonstrations and our pre-training stage is trained on sub-optimal transitions” for Adroit. However, in Sec. 5.2 (RESULTS), line 376 says, “All baselines are trained on sub-optimal data.” Could you clarify which statement is correct? Do lines 344 and 346 mean that all baselines in Meta-World are trained on the same sub-optimal data used for SODP pre-training, while expert data are used in Adroit baselines? If so, what is the reason behind using different data sources for each environment?
    4. This could introduce unfairness if it is accurate that baselines are trained with sub-optimal data. For SODP fine-tuning, the model can interact with the environment to optimize actions guided by rewards, whereas the BC and offline-RL methods do not have this privilege. Additionally, while offline RL methods can leverage low-reward transitions, BC methods typically require expert-level data to imitate expert policies effectively. Sub-optimal data, especially when only 50% or 30% of the RL agents' replay buffer is used, likely does not approximate expert-level quality. It would be more convincing if offline-RL and BC baselines were trained with expert data or even allowed to interact with the environment, as in methods like GAIL [8].
5. Concerns regarding experimental results and setup:
    1. There is an imbalance in the number of tasks between the state-based and image-based environments: 50 tasks are used in Meta-World, while only 3 are used in Adroit. Why wasn’t image observation utilized in Meta-World to create an image-based environment there as well? Including more image-based tasks would provide a more comprehensive evaluation of SODP’s image-based performance and could clarify whether the performance drop observed in tasks like “Hammer” is an isolated case, as shown in Table 2. If SODP generally struggles with challenging image-based tasks, such as “Hammer,” this would indicate limited generalization ability.
    2. The claim in line 432—“training on inferior data is more difficult, and the baselines trained on expert data perform better in this case”—is not entirely convincing, as SODP has access to interact with the environment and obtain rewards in the fine-tuning stage, which should be advantageous even if the baselines are trained with expert data.
    3. Does the same trend appear in state-based environments, where SODP performs worse in challenging tasks, as observed in the image-based setting? Could you provide task-specific performance results from Table 1 instead of just the average success rate? This would allow for a more precise identification of any special cases.
    4. In Fig. 7, it appears unreasonable that SODP_scratch could not succeed despite being able to interact with the environment and optimize with rewards. Additional experiments with a diffusion planner trained from scratch using online RL methods [2] should be included to see if online RL methods also fail entirely. Training with online RL from scratch would be a fairer comparison for SODP_scratch.
    5. Line 511 states, “We use the same rollouts generated by the pre-trained model to approximate the target policy and initialize the replay buffer.” Could you clarify the methodology used here and discuss its validity for testing the performance of SODP_scratch?

### Questions
1. Is the weight coefficient λ in Eq. 15 sensitive to changes? I could not find any implementation details or discussion regarding this hyperparameter. A sensitivity analysis for this hyperparameter should be provided to show how different values of λ affect the performance of their method.
2. In line 332, the statement “state space differs across tasks” could be clarified further. Does this mean that the dimensions of the state space differ across tasks or that the physical meanings of each index in the state space vary between tasks? If it refers to dimensional differences, how is this managed during the pre-training stage with multi-task data?
3. Could you clarify the meaning of line 968: “We show that directly fine-tuning the pre-trained planner without any regularization, as done in DPPO, fails in the multi-task setting”? As I understand it, fine-tuning task-specific rewards would shift to a single-task setting in the fine-tuning stage. Do you mean that the diffusion planner is actually fine-tuned on multiple tasks simultaneously?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel framework, SODP (Sub-Optimal Diffusion Planner), designed for optimizing reinforcement learning (RL) models by integrating Proximal Policy Optimization (PPO) with a Behavior Cloning (BC) loss function. This approach leverages PPO to maximize task-specific returns during fine-tuning, while incorporating BC regularization to preserve competencies gained during the pre-training stage. The framework addresses the challenge of utilizing sub-optimal data, enabling effective policy adaptation across various downstream tasks.

The authors validate their methodology through extensive empirical evaluations in multi-task environments, demonstrating that SODP can efficiently adapt and learn from low-quality datasets. The experimental results show that the proposed framework consistently outperforms state-of-the-art methods, highlighting its ability to produce competitive outcomes despite the limitations of pre-training on sub-optimal data.

### Strengths
- Introduction of BC Surrogate Loss: The paper introduces a novel Behavior Cloning (BC) surrogate loss that effectively regularizes the fine-tuning process, ensuring stability and preserving pre-trained competencies.
- Effective Use of Sub-Optimal Data: SODP demonstrates an innovative approach for leveraging sub-optimal data, overcoming the need for high-quality labels while still achieving strong performance across tasks.
- Strong Empirical Results: The experimental results on Meta-World and Adroit benchmarks show clear advantages over state-of-the-art methods, highlighting the practical effectiveness of the proposed framework.

### Weaknesses
 - Insufficient Explanation of Key Equations: The derivation of Equations (11) and (12) is not fully explained. Specifically, the summation of the log probabilities in the reverse diffusion process in Equation (11) lacks clarity, as it differs from the standard $p(a|s)$ formulation commonly used in reinforcement learning. The paper states that $\pi_{\theta}(a|s) = p_{\theta}(a_t^{k-1}|a_t^k, s_t)$, but it is not clear how this relates to the standard policy gradient formulation where the gradient is taken with respect to the probability of an action given a state, $p(a|s)$. The connection between the reverse diffusion process and the policy gradient is not sufficiently justified. This discrepancy requires further explanation to justify its relevance and correctness.
- Misapplication of Trust Region Loss: In Equation (12), the trust region loss is applied to the diffusion process rather than directly addressing the reinforcement learning process. The paper argues that the action distribution is represented as $p(a_t|s_t) = p_{\theta}(a_t^{0:K}|s_t)$, and therefore the trust region loss for the RL MDP is equivalent to the loss for the diffusion MDP. However, this equivalence is not clearly established. Applying the trust region constraint to the diffusion process does not guarantee that the policy in the RL environment will also adhere to a similar trust region. This choice appears to overlook the key challenge of improving sample efficiency in reinforcement learning, which could undermine the effectiveness of the method in dealing with limited data. The paper needs to clarify how optimizing the diffusion process directly translates to improved policy learning in the RL environment.
- Over-reliance on BC Regularization: I suspect behavior cloning the better samples from the replay buffer starting from a diffusion model pre-trained on sub-optimal data is the key to the performance gain over baselines in the proposed method. The paper does not adequately explore the individual contributions of the PPO fine-tuning and the BC regularization. The fact that SODP without regularization decreases in performance with online samples further suggests that the BC term is the primary driver of performance. The paper should include an ablation study that isolates the effect of the BC regularization term, particularly by comparing the performance of a model trained solely with the BC loss against the full SODP framework. This is crucial to understand the true contribution of the proposed method.

### Questions
- In equation (11), I assume $\sum_{k=1}^K \triangledown \log p_\theta (a_t^{k-1} | a^{k-1}_t, s_t)$ is modeling $ \triangledown p(a_t | s_t) $ in policy gradient for the RL MDP. The probability of a specific sample is known to be intractable in the diffusion process. Can you provide proof for calculating the gradient of probability of a specific sample in the diffusion process? Note, DDPO is applying the policy gradient to each step of the diffusion reverse process, where the probability of each reverse step is defined as an isomorphic gaussian distribution, whose probabilities are well-defined.
- In equation (12), is "generating new samples" (page 5, line 238) referring to samples in the RL MDP or the diffusion MDP? If it is in the RL MDP, how does applying the surrogate loss to the diffusion MDP help solving the RL MDP?

### Soundness
2

### Presentation
3

### Contribution
2
