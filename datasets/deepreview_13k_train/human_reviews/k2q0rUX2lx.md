# Enhancing Multi-Step Reasoning Abilities of Language Models through Direct Q-Function Optimization

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Reinforcement Learning (RL) plays a crucial role in aligning large language models (LLMs) with human preferences and improving their ability to perform complex tasks. However, current approaches either require significant computational resources due to the use of multiple models and extensive online sampling for training (e.g., PPO) or are framed as bandit problems (e.g., DPO, DRO), which often struggle with multi-step reasoning tasks, such as math problem-solving and complex reasoning that involve long chains of thought. 
To overcome these limitations, we introduce Direct Q-function Optimization (DQO), which formulates the response generation process as a Markov Decision Process (MDP) and utilizes the soft actor-critic (SAC) framework to optimize a Q-function directly parameterized by the language model. The MDP formulation of DQO offers structural advantages over bandit-based methods, enabling more effective process supervision. 
Experimental results on two math problem-solving datasets, GSM8K and MATH, demonstrate that DQO outperforms previous methods, establishing it as a promising offline reinforcement learning approach for aligning language models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel offline reinforcement learning (RL) algorithm, Direct Q-function Optimization (DQO), aimed at improving the multi-step reasoning capabilities of large language models (LLMs). The authors propose formulating the response generation process as a Markov Decision Process (MDP) and utilize the soft actor-critic (SAC) framework to optimize a Q-function parameterized by the language model. The paper claims that DQO outperforms previous methods on math problem-solving datasets, GSM8K and MATH, establishing it as a promising approach for aligning language models.

### Strengths
1. The paper addresses a significant issue in the field of language model alignment and multi-step reasoning, which is a valuable contribution to the advancement of LLMs.
2. The presentation of the material is coherent and the paper is generally easy to follow, which aids in the understanding of the proposed DQO algorithm.

### Weaknesses
A primary concern is the rationality behind the derivation of the proposed method. Please see the question section below.

1.  The paper assumes the existence of a ground-truth reward function, which undermines the necessity of the log \pi^*(a|s) representation used later in the paper. In particular, In Lines 149-151, the authors presuppose the existence of a ground-truth reward function. Given this, why do we still need log \pi^*(a|s) as the representation of r (See Eq 8 and Eq 9)? The use of a ground-truth reward, even if unknown, implies that the optimal policy is implicitly defined by this reward, making the explicit representation using log \pi^*(a|s) seem redundant. If the goal is to learn the optimal policy, why not directly learn a policy that maximizes the expected return under the ground-truth reward, rather than using a proxy representation based on the optimal policy's log probabilities?
2.  The transition from Eq(9) to Eq(11) is questionable. Eq(7) represents the value function fitting target, not the policy optimization target. It is unclear how substituting Eq(9) into Eq(7) achieves policy optimization, despite the introduction of a reward term reparameterized by \pi_\theta. The authors must elaborate on how the substitution of Eq(9) into Eq(7) facilitates policy optimization, especially considering that Eq(7) is a value function target, not a policy optimization target. Specifically, the objective in Eq(7) seems designed to fit the Q-function, not to directly update the policy parameters. The connection between minimizing the Q-function error and optimizing the policy is not clearly established.
3.  There is a conflict between the definitions of reward in Line 223 and Eq 14, with the former being log \pi_ref + r and the latter being \log \pi_ref/pi + r. This inconsistency needs to be resolved. The discrepancy between these two definitions raises concerns about the consistency of the reward formulation throughout the paper. It is crucial to have a unified definition of the reward to ensure the validity of the proposed method.
4.  The rationale behind the use of importance sampling in Section 3.3 needs further justification, particularly in the context of value function learning where it is not typically necessary. Importance sampling is typically required when the sampling policy and the current policy are inconsistent during policy optimization, not during value function learning as implied by Eq 6 and Eq 7. The justification for using importance sampling in the context of value function learning, where the goal is to estimate the value of a given state under a specific policy, is not clear. The standard approach for value function learning does not typically involve importance sampling, and the paper needs to provide a more compelling reason for its inclusion.

### Questions
1. The paper assumes the existence of a ground-truth reward function, which undermines the necessity of the log \pi^*(a|s) representation used later in the paper. In particular, In Lines 149-151, the authors presuppose the existence of a ground-truth reward function. Given this, why do we still need log \pi^*(a|s) as the representation of r (See Eq 8 and Eq 9)? 
2. The transition from Eq(9) to Eq(11) is questionable. Eq(7) represents the value function fitting target, not the policy optimization target. It is unclear how substituting Eq(9) into Eq(7) achieves policy optimization, despite the introduction of a reward term reparameterized by \pi_\theta. The authors must elaborate on how the substitution of Eq(9) into Eq(7) facilitates policy optimization, especially considering that Eq(7) is a value function target, not a policy optimization target.
3. There is a conflict between the definitions of reward in Line 223 and Eq 14, with the former being log \pi_ref + r and the latter being \log \pi_ref/pi + r. This inconsistency needs to be resolved.
4. The rationale behind the use of importance sampling in Section 3.3 needs further justification, particularly in the context of value function learning where it is not typically necessary. Importance sampling is typically required when the sampling policy and the current policy are inconsistent during policy optimization, not during value function learning as implied by Eq 6 and Eq 7.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Direct Q-function Optimization (DQO) improves language model performance by treating text generation as a Markov Decision Process and using soft actor-critic methods to directly optimize the Q-function, demonstrating superior results on math problem-solving tasks.

### Strengths
* The theorem is presented in a straightforward manner.
* The experiments demonstrate promising results, particularly in the context of small-scale open-source LLMs.

### Weaknesses
 * I believe the method can heavily rely on the accuracy of the process value. but the difficulties should be analyzed in your experiment.
* There is a lack of analysis regarding whether the process value is fairly accessible or measurable.
* The motivation appears to be aligned with the process-supervised reward model approach. Could you clarify and demonstrate the key differences between your method and theirs?

### Questions
* Could you provide a more in-depth analysis of your strengths when it comes to handling long-horizon tasks?
* Could you expand on how experiments can contribute to evaluating the process value? And how to produce these process values to make it could scale in practice.
* What methods or strategies can be employed to effectively generate process value?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focus on token-level optimization in LLMs. They rewrite the learning objective in LLMs and utilize the soft actor-critic (SAC) framework to optimize a Q-function directly parameterized by the language model. Experimental results on GSM8K and MATH  demonstrate the performance of proposed method.

### Strengths
The problem is significant, as sparse rewards cause the instability of learning process in RL.

### Weaknesses
It seems that the author just apply SAC in the context of LLM and rewrite the objectives. 

The excessive number of formulas has made the text lengthy and difficult to follow; the paper should be written in a more concise way. Below are some suggestions.
- Eq 9 can be removed and mention to parameterize the following modules $Q_\theta$, $\pi_{\theta}$, $V_{\phi}$, as it is almost the same with Eq 8. 
- Could it be more reasonable to move Eq. (6) and Eq. (7) to the preliminaries section or move them into appendix. Since Eq 6 and Eq 7 come from the previous work and it can be regarded to replace the original reward $r$ with $\bar{r}$.
- If $\pi^*$, $Q^*$ and $V^*$ are not used after the definition in Eq 3 - 5, also consider to move them into Appendix.
- Section 3.2 and Section 3.3 also can be more concise by referring to the original paper and discuss more about the challenges or special design in order to apply them in LLMs.

Additionally, minor issues in the formulas require proofreading to correct (see questions for specifics). 

The experimental results over Qwen2-7B-Instruct model are not convincing:  the proposed method achieves an improvement of less than 1% on the two datasets, it is not sure if it comes from randomness. Could you please provide statistical significance tests or report the average performance/standard error over different seeds? Alternatively, other experiments over additional models or tasks to demonstrate stronger improvement?

### Questions
In Eq. (2), it appears $\beta$ is missing.

In Eq. (7), should it be $r$ instead of $\bar{r}$? 

In Line 220, "By plugging in (9) to (7)" -> "By plugging in Eq. (9) into Eq. (7)."

If I understand correctly, there is a missing minus sign in Eq. (11) which causing the RHS of Eq. (10) and Eq. (11) sum to zero. 

In Eq. (12), could you clarify the meaning of $ s_{h+1} \sim P(\cdot \mid s_h, a_h) $? Does this imply a deterministic process where $s_{h+1} = \text{Concat}(s_h, a_h) $?

In Eq. (14), should it be $ r(a_{h+l}, s_{h+l}) $?

If I’ve misunderstood any part of this, please feel free to correct me.

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
4

### Summary
This paper introduces the Direct Q-Function Optimization (DQO) approach, which leverages a Markov Decision Process (MDP) formulation to enhance the performance of large language models (LLMs) on reasoning tasks. By adopting the multi-step nature of MDPs, DQO addresses limitations found in bandit-based offline methods, such as DRO, and remains effective even when preference-based datasets are unavailable.

### Strengths
1. The proposed algorithm frames response generation as a MDP, making it more suitable for long-horizon, step-by-step reasoning tasks compared to DRO.
2. The approach demonstrates potential in effectively leveraging process rewards to enhance performance through feedback at each step.
3. DQO incorporates lambda-return and importance sampling to ensure efficient use of offline data.
4. Experimental results highlight the superior performance of DQO on widely used GSM8K and MATH datasets.
5. The paper is well-written and easy to follow.

### Weaknesses
1. Fairness of Comparison:  According to Table 8, the size of datasets for each model differs significantly.  For example, DQO uses datasets up to four times larger than those for DPO. Although DPO's data subset is sampled from DQO's dataset, this disparity raises concerns about fair comparisons, especially given the relatively small performance margin of DQO over DPO for the Qwen2-7B-Instruct model when dataset differences are minimal.

2. Lack of Experimental Details: The paper lacks sufficient discussion on the evaluation of generated/augmented responses, the distribution of positive and negative responses in the training and testing data, and detailed training parameters (e.g., number of epochs for DRO and DQO). This makes it difficult to directly explain performance discrepancies, such as those seen between this work and [A1] for Qwen2-7B-Instruct (see Question 3).

3. Hard to assess the benefits of  MDP formulation: Without importance sampling, DQO’s performance (as shown in Table 5) is worse than DRO’s performance in Table 4. This raises the question of whether the key factor in DQO's superior performance is the MDP formulation itself or the use of importance sampling.

4. Risk of overfitting: The dependency on offline data and importance sampling introduces the risk of overfitting to this data, especially if it does not represent the diverse scenarios encountered in real-world applications.

5. Potentially high computational costs: DQO involves complex training procedures, including learning Q and V functions and using  \lambda-return and importance sampling. This complexity may lead to higher computational costs compared to DRO, especially for long-horizon tasks. The paper does not discuss computational efficiency; for example, chain-of-thought prompting [A2] can also provide intermediate checks without additional training. A more thorough comparison with CoT and [A2] is recommended.

6. Clarification of Specific Challenges: While this work effectively incorporates SAC, lambda_return, and importance sampling for improving reasoning performance, there is insufficient discussion on the challenges encountered during this integration. Highlighting these  challenges would strengthen the work.

7. Insufficient discussion on unbalanced data and process reward: While Table 1 notes that DQO can learn from unbalanced samples, no experiments substantiate this claim. In Section 4.4, a synthetic process reward mechanism is presented, but more explanation and experimentation with different process score designs are needed.

### Questions
1. How were generated responses evaluated for each augmented dataset? What is the distribution of positive and negative responses in the training and testing data?

2. For Qwen2-7B-Instruct, why does DPO consistently outperform KTO and DRO, while DRO outperforms DPO for Gemma-1.1-7B-it? Could the authors provide insights into this discrepancy??
3. The related work [A1] reports pass rates of 82.3% and 49.6% for Qwen2-7B-Instruct on GSM8K and MATH, respectively. Why does this differ from the results in Table 3?
4. Could the authors explain why DQO with lambda=1 outperforms lambda=0.95?
5. What is the correlation between the learned value function and constructed process scores during testing?

Minor issue:
1. Undefined/Misleading Notations: In eq (6), the expectation should be taken w.r.t. a_h. In Line 247, it should be V^{\pi}. The update equation (16) should be G^{\lambda}_{\phi, \theta}(s_h) = G^{(H-h)}_{\phi, \theta}(s_h) when \lambda=1. 
1. Grammar and Typos: The Line 240-241 should reference DRO instead of DQO.



[A1] Lai, Xin, et al. "Step-dpo: Step-wise preference optimization for long-chain reasoning of llms." arXiv preprint arXiv:2406.18629 (2024).

[A2] Wei, Jason, et al. "Chain-of-thought prompting elicits reasoning in large language models." Advances in neural information processing systems 35 (2022): 24824-24837.

### Soundness
2

### Presentation
3

### Contribution
3
