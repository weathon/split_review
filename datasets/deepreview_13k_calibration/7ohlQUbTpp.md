# Collab: Controlled Decoding using Mixture of Agents for LLM Alignment

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Alignment of Large Language models (LLMs) is crucial for safe and trustworthy deployment in applications. Reinforcement learning from human feedback (RLHF) has emerged as an effective technique to align LLMs to human preferences, and broader utilities, but it requires updating billions of model parameters which is computationally expensive. Controlled Decoding, by contrast, provides a mechanism for aligning a model at inference time without retraining. However, single-agent decoding approaches often struggle to adapt to diverse tasks due to the complexity and variability inherent in these tasks. To strengthen the test-time performance w.r.t the target task, we propose a mixture of agents-based decoding strategies leveraging the existing off-the-shelf aligned LLM policies. Treating each prior policy as an agent in the spirit of mixture of agent collaboration, we develop a decoding method that allows for inference-time alignment through a token-level selection strategy among multiple agents. For each token, the most suitable LLM is dynamically chosen from a pool of models based on a long-term utility metric. This policy-switching mechanism ensures optimal model selection at each step, enabling efficient collaboration and alignment among LLMs during decoding. Theoretical analysis of our proposed algorithm establishes optimal performance with respect to the target task represented via a target reward, for the given off-the-shelf models. We conduct comprehensive empirical evaluations with open-source aligned models on diverse tasks and preferences, which demonstrates the merits of this approach over single-agent decoding baselines. Notably, COLLAB surpasses the current SoTA decoding strategy, achieving an improvement of {up to 1.56x} in average reward and $71.89\%$ in GPT-4 based win-tie rate.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes to extend decoding / inference time alignment using a mixture-of-experts based decoding strategy. For this, the authors make use of existing LLMs as policy experts. The decoding method proposed by the authors uses a token level selection strategy where an LLM is selected from the experts / agents for each token. This selection is performed using a utility metric which is based on the implicit Q function. The authors also provide a theoretical justification of their approach and support it using empirical results.

### Strengths
* Dont need to update the billions of parameters that RLHF needs.
* Their approach can make use of specialized models which are experts in a subset of capabilities that are desired.
* Current solutions to mixing multiple experts relies on either tuning a model, or explicit formulas, and rely on expert demonstrations. This work dynamically merges models 
* This approach is especially beneficial in settings where reward models / policy parameters of models are not available readily thus impacting a lot of industry applications.
* The theoretical justification and details are sound.
* The paper is generally well written and easy to follow.
* The evaluations are diverse and across 7 different setups, however, only 2 datasets: Berkeley Nectar and HH-RLHF.

### Weaknesses
 * It is unclear what is the reference policy used in the KL terms that is used to obtain the objective of each policy (J). 
* "The sub-optimality gap will be lower when 1) the best agent’s reward function is close to the target reward function, and 2) when the regularization terms are properly controlled so that both the reference policy and the optimal policy are close" -> The choice of the reference policy seems to be important.
* I would have liked to see analysis on compute requirements.
* Minor point: There is no human evaluation done in this work. Evaluating using GPT4 should not be used to claim alignment with humans.
* The main usage of this work seems to be in using domain expert policies that are good in different aspects / tasks. It is unclear how the chosen policies are experts in different areas that are evaluated. For this, I would suggest using evaluation on harder tasks maybe like reasoning / coding datasets (alpaca eval, arena hard, mt bench).


### Questions
* What is the distribution of the selection of agents.
* How much is the compute difference between doing RLHF + single decoding vs mixture of decoding?
* Line 97-99 seems repeated.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Controlled Decoding using Mixture of Agents for LLM Alignment, a method that achieves alignment at inference time without retraining the policy model. However, the comparison with classical alignment methods is insufficient and some critical experimental details are unclear.

### Strengths
1. The approach of achieving alignment without retraining the policy model is innovative and could significantly reduce computational costs.

2. The concept of using a mixture of agents for decoding provides a fresh perspective on controlling language model outputs.

### Weaknesses
1. Is the implicit Q-function an additional trained language model? How does its cost compare to methods based on DPO, PPO, and RLHF?

2. Can the implicit Q-function directly guide a policy model in decoding? Is it necessary to use multiple agents collaboratively for decoding?

3. How were the agents initialized in the experiments? Were these agents explicitly trained for alignment?

4. The experimental section lacks a comparison with alignment algorithms based on DPO and PPO.

5. The authors should consider more complex, objective tasks such as those involving reasoning and math to avoid potential biases from the reward model and GPT-4 evaluations.

### Questions
please see weaknesses

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
The paper proposes a method to elaborate multiple LLMs at the time of inference to combine the strengths of the models. For each token generation, the most promising policy to generate the rest of the sequence is selected. The method is evaluated on two generic alignment tasks using multiple generic LLMs, outperforming single-LLM decoding algorithms.

### Strengths
- How to elaborate multiple LLMs is an important research question. Given that we have little knowledge on how to investigate the strengths and weaknesses of the LLMs (as of now), ensemble methods should be useful.
- The method is simple and intuitive.
- The theoretical result is nice to have, yet its practical implication seems not immediate to me.

### Weaknesses
 > (p.10 l.536) Empirical evaluations demonstrate its superiority over traditional single-agent decoding baselines, providing a robust and computationally efficient method for model alignment in complex, real-world scenarios

- I failed to understand the computational cost of the method. My understanding is that it requires the inference of the whole sequence for each policy, per each token. So the computational cost of generation a sequence of length N would be O(N^2) times of query to LLMs. It would be nice to have a walltime of the algorithm compared with BoN sampling and Agent-1 and 2.

- Although the strength of the method is claimed to be able to adapt to a diverse set of tasks, the experiments are not designed to evaluate in such a scenario. It would be beneficial to evaluate the method for each subtask rather than showing the aggregated result. For example, how does the model perform in the Harmlessness and Helpfulness subsets in HH-RLHF datasets? What kinds of tasks benefit from the ensemble? It would be helpful if we have a post-hoc analysis of what makes the proposed method better than a single-LLM method in the empirical scenario.

### Questions
- What is the computational complexity and the walltime of the algorithm in the experiment? I understand that the walltime depends on the hardware and the system but would be a good reference to understand the effectiveness.

- Which algorithm does the SoTA decoding strategy refer to? Is it Transfer Q* (Souradip Chakraborty et a l. 2024)? Or is it controlled decoding (Sidharth Mudgal et al. 2024), which is called SoTA in Chakraborty et al.? A paper should use a term that uniquely identifies the subject rather than a term that changes over time.

- (p.7 Example) Why can COLLAB correctly answer the question when both Agent-1 and 2 fail to answer the question? Is there a reason COLLAB decoding can acquire an ability neither of the Agents have?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents the idea of switching between different LLMs during the decoding process in order to maximize the reward of the generated response. To find which policy should be used at each generation step, they define the problem as KL-constrained RL and sample a token greedily with respect to a Q function (regularized by the KL constraint).

### Strengths
- The idea of using a Q function to perform routing between different models is novel. Moreover, doing collaborative decoding to maximize reward is an interesting problem that does not have a lot of literature about it.
- The empirical results seem strong, with the proposed algorithm outperforming the baselines.

### Weaknesses
The paper is hard to read and understand; in addition, some important details are not discussed at all. Some examples:
- There is no discussion about how the Q functions are trained, although this is a crucial part of the algorithm.
- The only description of the experiments (models, rewards, etc.) is in the appendix. It is also unclear why the author chose these specific experiments.
- The authors explain their method as an extension of CD, which proposes sampling according to equation 3. However, in practice they sample according to equation 5. This is not the same, as the probability under pi_ref is not taken into consideration in equation 5. 
- Line 428 hint that you are doing top-K but Algorithm 1 (line 330) talks about top-p, which one is true?

### Questions
Control Decoding and other similar works [1] use $Q^{\pi_{ref}}$ to augment the decoding. This is not an approximation of $Q^*$ as mentioned in lines 260-261 of the paper, but an alternative solution to the KL-constrained RL problem, known as RWR [2]. The advantage of using $Q^{\pi_{ref}}$ is that it can be easily learned using trajectories from $\pi_{ref}$. 
Collab, on the other hand, uses $Q^{\pi_i}$ as an approximation to $Q^*$. Does the author have an explanation (either empirical or theoretical) as to why this is better than just using $Q^{\pi_{ref}}$? This is an important design choice in the algorithm that I feel hasn’t been discussed enough.

In the related work section, I’m missing a discussion about the connections to hierarchical RL. Collab is very close to it, as it learns a policy (parametrized as Q function) to choose which one of several policies to sample from in each state.

I find some of the metrics used in the experiment section are not related to the motivation behind the algorithm. The idea, as presented in the paper, is to use models trained on different reward functions to perform decoding that will maximize a new one. In the experiment section, however, you evaluate non-reward metrics like win rate, diversity, and coherence. Let’s take win rate, for example. Is your claim that the new reward function correlates with the win rate better than the ones that the original models were trained for? And therefore, a higher win rate is equivalent to a higher reward? If so, where is the evidence?

[1] Han, Seungwook, et al. "Value Augmented Sampling for Language Model Alignment and Personalization." arXiv preprint arXiv:2405.06639 (2024).
[2] Peters, Jan, and Stefan Schaal. "Reinforcement learning by reward-weighted regression for operational space control." Proceedings of the 24th international conference on Machine learning. 2007.

### Soundness
3

### Presentation
1

### Contribution
4
