# Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Reinforcement learning from human feedback (RLHF) is an effective method for aligning large language models (LLMs) with human values. However, reward over-optimization remains an open challenge leading to discrepancies between the performance of LLMs under the reward model and the true human objectives. A primary contributor to reward over-optimization is the extrapolation error that arises when the reward model evaluates out-of-distribution (OOD) responses. However, current methods still fail to prevent the increasing frequency of OOD response generation during the reinforcement learning (RL) process and are not effective at handling extrapolation errors from OOD responses. In this work, we propose the *Behavior-Supported Policy Optimization* (BSPO) method to mitigate the reward over-optimization issue. Specifically, we define *behavior policy* as the next token distribution of the reward training dataset to model the in-distribution (ID) region of the reward model. Building on this, we introduce the behavior-supported Bellman operator to regularize the value function, penalizing all OOD values without impacting the ID ones. Consequently, BSPO reduces the generation of OOD responses during the RL process, thereby avoiding overestimation caused by the reward model’s extrapolation errors. Theoretically, we prove that BSPO guarantees a monotonic improvement of the supported policy until convergence to the optimal behavior-supported policy. Empirical results from extensive experiments show that BSPO outperforms baselines in preventing reward over-optimization due to OOD evaluation and finding the optimal ID policy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach named Behavior-Supported Policy Optimization (BSPO) to address the challenge of reward over-optimization in Reinforcement Learning from Human Feedback. The core issue addressed is the extrapolation error that arises when the reward model evaluates out-of-distribution responses, leading to discrepancies between the performance of LLMs under the reward model and true human objectives. The authors propose using a behavior policy to model the in-distribution region of the reward model and introduce a behavior-supported Bellman operator to regularize the value function, penalizing out-of-distribution values without impacting in-distribution ones. Theoretical proofs are provided to show that BSPO guarantees monotonic improvement of the supported policy until convergence to the optimal behavior-supported policy. Empirical results demonstrate BSPO's effectiveness in preventing reward over-optimization and finding the optimal ID policy.

### Strengths
1. The paper is well-organised and articulated with clarity, the complex concepts are explained in a clear and concise manner. 
2. The paper provides theoretical justifications, and the results are convincing.

### Weaknesses
1. The paper primarily focuses on the synthetic set for evaluating reward over-optimisation, the alignment of the reward with real human annotators’ evaluation remains insufficiently validated.
2. Although the paper did experiments on the robustness of BSPO with noisy data, a more in-depth analysis of how BSPO performs under various types of noise or distributional shifts could strengthen the paper.
3. The justification for using V-values instead of Q-values, while presented as a stability improvement, is not entirely convincing. Given the large action space in LLMs, the immediate reward term r(s,a) in the Q-value calculation still introduces significant variance, making it unclear how using V-values provides additional stability.

### Questions
The paper mentions that using V values instead of Q values provides greater stability, mainly because state transitions are deterministic in the context of LLMs. Specifically, for a given input prompt and a sequence of generated tokens, the generation of the next token is deterministic—given the current state and action, the next state is uniquely determined. In this case, there is a direct relationship between V values and Q values. But what if the next token generation is sampled, introducing uncertainty into the transition function? How does BSPO work in such a situation?

There is a lack of analysis of the experimental results. What causes the drop observed during the training of CPPO?

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
5

### Summary
This work addresses reward over-optimization in RLHF by penalizing out-of-distribution (OOD) responses, which are a significant source of extrapolation errors during evaluation. The proposed approach, Behavior-Supported Policy Optimization (BSPO), identifies OOD tokens by checking if the predicted probability from the reward model falls below a defined threshold. It integrates an auxiliary loss based on the supervised fine-tuning (SFT) objective into the reward model’s training. The proposed mechanism helps mitigate OOD overestimation without impacting the model’s performance on in-distribution (ID) data.

### Strengths
1. The paper effectively addresses a critical and well-motivated issue in RLHF, reward over-optimization due to OOD responses.

2. The proposed Behavior-Supported Policy Optimization (BSPO) method introduces a unique approach by leveraging a behavior policy for OOD detection and integrating it with value regularization.

3. The empirical validation through synthetic experiments demonstrates that BSPO outperforms baseline methods.

4. The paper’s methodology is rigorously supported by theory, with proofs ensuring the convergence and stability of the behavior-supported value functions.

### Weaknesses
1. A significant concern is that the experiments are conducted solely on synthetic data. This limitation raises questions about the applicability and effectiveness of the proposed method in real-world scenarios.

2. The experimental results lack an ablation study on the sensitivity of the parameter $\epsilon_\beta$.

3. The paper does not adequately discuss related works that incorporate SFT loss into the training objective, albeit for different purposes, such as in policy loss. Notable examples include:
- Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer
- Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF

### Questions
1. How do you select the value of $V_{min}$ and $\epsilon_\beta$?

2. If the SFT loss is not added to the training of reward model, can the reward model still recognize OOD prompts?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses reward over-optimization in Reinforcement Learning from Human Feedback (RLHF), where large language models (LLMs) sometimes align poorly with human objectives due to extrapolation errors when evaluating out-of-distribution (OOD) responses. The authors propose Behavior-Supported Policy Optimization (BSPO), which models the in-distribution (ID) region by defining a behavior policy based on the reward training dataset’s next token distribution. To regularize the value function, BSPO introduces a behavior-supported Bellman operator, penalizing OOD values while leaving ID values unaffected, thus reducing OOD response generation. BSPO is shown theoretically to guarantee monotonic improvement of the policy within the ID region, leading to convergence at the optimal policy. Empirical results confirm BSPO’s superiority over baselines in preventing reward over-optimization, making it effective in aligning LLMs with human intent.

### Strengths
- The research focus is clearly presented, providing readers with the essential background needed to understand the main contributions of the paper.

- The core idea of Behavior-Supported Policy Optimization (BSPO) is intuitive and easy to implement, with a strong theoretical ground covering key properties like contractivity, monotonicity, and convergence.

- The synthetic experiments are well-designed to demonstrate the rigor of the proposed method. The results are presented and interpreted clearly, making the comparisons with baseline methods easy to follow and effectively highlighting the strength of BSPO.

- The literature review is thorough, giving readers, even those unfamiliar with reward over-optimization, a clear view of the related research landscape.

### Weaknesses
 - The experimental results presented in this paper are demonstrated exclusively on the UltraFeedback dataset, making it essential to evaluate the generalizability of the proposed method by conducting experiments on additional benchmark datasets.

- The paper emphasizes the concept of the "In-Distribution (ID) region of the reward training dataset" as a key to avoiding reward over-optimization, with BSPO’s foundational idea built on this concept. Given this emphasis, it would have been helpful to see a performance comparison with DPO-based methods, which directly utilize the ID region of reward training datasets (e.g., win response $y_w$ and lose response $y_l$), to further contextualize BSPO’s effectiveness. Specifically, a comparison against methods like DPO, KTO, or CTO would help clarify BSPO's advantages in terms of utilizing the ID region for policy optimization.

- As noted in the limitations, significant differences may exist between human preferences and model-predicted preferences, underscoring the importance of human evaluation for generated responses. In cases where human judgment is not feasible, using an LLM-as-a-judge (please refer to Reference) could serve as a practical alternative for conducting pseudo-human evaluation. However, the paper does not explore the use of multiple LLMs as judges to validate the robustness of the results, which is important given the potential biases of individual LLMs.

- Some visual content is challenging to interpret at first glance. For instance, it seems unclear in Figure 1(c) what "correct/incorrect" specifically indicates, as this is not explicitly mentioned in the main text. Additionally, Figure 2(a) is somewhat confusing, as it places the "query+answer (given past tokens)" at the top and the "behavior distribution (next tokens)" at the bottom, unlike the conventional layout where the past context is on the bottom and the future sequence is on the top. A reversed figure layout might have improved clarity. Furthermore, the lack of detailed axis labels and legends in some figures makes it difficult to fully grasp the presented data.

- Some explanations were not detailed enough. For example, it would be helpful if there were some sentences describing where the (pretrained) proxy reward model $R_{\phi}(\cdot)$, which is optimized by $\mathcal{L}_{\text{ScoreLM}}(\phi; \mathcal{D})$, is placed at the calculation of $\mathcal{L}_{V}(\phi; \pi)$. The paper would benefit from a more detailed explanation of how the proxy reward model is integrated into the overall training process, particularly in the context of the Bellman operator.

### Questions
- In Eq (6), is the supervised loss calculated with respect to both $y_w$ and $y_l$?

- Regarding the main results in Figure 3, how were the remaining 27k samples, which were not used for training the proxy reward model, utilized? What was the rationale behind splitting the dataset into 30k and 27k?

- As noted in the Weakness section, is there a specific reason for not comparing BSPO with direct preference optimization methods like DPO, KTO, and CTO?
  - In what ways do you consider BSPO to be superior to DPO-related methods?

- In the first line of Eq (15) in the Appendix, should it be $a' \sim \pi(\cdot|s')$ instead of $a' \sim \pi(\cdot|\pi)$?

### Soundness
4

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
3

### Summary
This paper investigates the issue of reward over-optimization in RLHF and introduces Behavior-Supported Policy Optimization (BSPO) to prevent the generation of out-of-distribution responses during RL training. By learning the value function using in-dataset actions, the author refines the policy through PPO updates. Empirical results demonstrate the effectiveness of the proposed method.

### Strengths
* The studied problem is important for RLHF and the proposed method is well-motivated.  

* The idea of using reward model training distribution to regularize the value function learning for LLMs is novel, to the best of my knowledge.

* The empirical evidence shows promising results to alleviate the overoptimization issue.

### Weaknesses
Despite the strengths of this paper, I identified several limitations that require further attention:

1. The paper claims that prior constraint optimization methods "only suppress overestimation in the ID region.", which I disagree. The worst-case optimization method with ensemble has been shown to mitigate over-optimization for OOD actions [1]. During PPO training, a worst-case reward can also penalize OOD responses generated by the trained LLM. The authors should provide a more accurate comparison of BSPO with previous methods.

2. There seems to be a problem in the proof of Corollary 1. The authors suggest that optimizing the objective in Eq 23 forces the learned policy to choose behavior-support actions. However, there are cases where all actions are OOD for a given prompt $s$, which could inevitably introduce OOD actions. This situation can arise when the SFT model and reward training use different datasets. Thus, the argument may not hold.

3. The current BSPO can only be applied to token-level RLHF, while many studies focus on response-level RLHF. Can the proposed method also be adapted for response-level RLHF?

4. The evaluation is restricted to reward models smaller than 3B. Validating on 7/8B reward models would strengthen the experiments.

5. The authors should explore how the two threshold hyperparameters, $V_{min}, \epsilon_{\beta}$, affect the method's performance.

6. Prior work [2][3] considers a noisy label setting, where the over-optimization problem is more severe. Can BSPO be effective in this challenging setting?

7. Typos: In Eq 36, the use of Q function is not correct.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
