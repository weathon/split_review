# Ask more, know better: Reinforce-Learned Prompt Questions for Decision Making with  Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Large language models (LLMs) demonstrate their promise in tackling complicated practical challenges by combining action-based policies with chain of thought (CoT) reasoning. Having high-quality prompts on hand, however, is vital to the framework's effectiveness. Currently, these prompts are handcrafted utilising extensive human labor, resulting in CoT policies that frequently fail to generalise. Human intervention is also required to develop grounding functions that ensure low-level controllers appropriately process CoT reasoning. %\yanxue{In this paper, we \replaced{propose}{ take the first step towards} a fully integrated end-to-end framework for task-solving {in real settings employing complicated reasoning.}} 
{In this paper, we propose a comprehensive training framework for complex task-solving, incorporating human prior knowledge into the learning of action policies. %\DM{perhaps we could make the claims a bit softer?}.
}%To that purpose, we offer a new leader-follower bilevel framework capable of learning to ask relevant questions (prompts) and subsequently undertaking reasoning to guide the learning of actions to be performed in an environment. 
To that purpose, we offer a new leader-follower bilevel framework that is capable of learning to ask relevant questions (prompts) and subsequently undertaking reasoning to guide the learning of actions. 
{The prompt policy is employed to make introspective revisions based on historical findings, leading the CoT process to consider the anticipated goals and generate outputs that lead to decisive, high-performing actions. }%To incentive these high quality actions, the prompt policy has its own objective in our system, allowing it to adapt to the action policy.} 
The action policy subsequently learns to comprehend and integrate the CoT outputs to take actions. Our empirical data reveal that our framework outperforms leading methods in $5$ decision-making tasks such as Overcooked and FourRoom. %\DM{the abstract is quite long}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a bi-level framework which learns to select a set of prompts to enable effective operation on downstream tasks. A set of prompts is generated using chatGPT 3.5, which are then selected from using a learned policy. Generated chain of thought skeleton are then input into a action policy which acts in the environment. Experiments show the efficacy of the approach.

### Strengths
- The proposed bi-level mechanism to select from a set of prompts and then act in the environment is novel to my understanding
- The method in the paper I generally clear and understandable

### Weaknesses
 - The formatting of the paper is odd, for example the distance from the subsection heading from text is way too small in page 5
- The results in the paper would be more readable if there were more illustrations of the process (for example in the introduction)
- The LLM takes as input only text. In this case, for embodied domains with image observations, it seems like there is no way for the LLM to really know the current state, which means that the method essentially just trains a low-level image based policy given some set of thoughts (since the high-level policy is invariant to task completion).
- As a result, this framework doesn't really make sense for decision-making in my opinion -- it makes much more sense in the setting of reasoning and I would like to see evaluation in that setting.

### Questions
- Given the setting described above, why is that the approach actually improve performance over baselines?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a bilevel framework that consists of the prompt-generation policy, thought reasoning policy, and action policy. In particular, at each timestep, the prompt-generation policy generates a prompt, which is then used by the thought reasoning policy to produce the CoT. The produced thought is used by the action policy to select an action in the environment. The proposed bilevel-LLM method is evaluated in ChainWorld, FourRoom, and Overcooked domains and shows better performance than baselines.

### Strengths
1. The bilevel optimization with the prompt-generation policy to minimize the actor policy's uncertainty is new & interesting. 
2. The paper is well-written and addresses the important challenge of automated prompt engineering for solving decision-making tasks.

### Weaknesses
1. While the proposed bilevel-LLM generally achieves better performance than baselines, the performance gap is marginal compared to the GFlan baseline (the difference may not be statistically significant). 
2. The novelty could be limited with respect to prior work: learning to select a prompt based on policy gradient is similar to PromptPG, and the use of Chain-of-thought prompting to act in the environment is similar to ReAct. As such, this paper could be viewed as combining these two directions.
3. While one of the paper's objectives is to avoid the expensive prompt crafting by humans, the framework would still need human-constructed questions. In Figure 3(c), the paper presents the Bilevel-LLM-Auto that does not rely on human-constructed prompts, but it is unclear whether this method applies to other domains, including Overcooked (only the ChainWorld(Full) performance is shown).
4. The prompt-generation policy aims to minimize the actor policy's entropy. However, I am unsure whether this is the correct objective to optimize for because 1) the actor policy may be certain but certain about incorrect actions (i.e., low uncertainty but convergence to sub-optimal actions), 2) for some domains, an optimal policy could be stochastic not deterministic, and 3) a positive entropy could help exploration. 
5. The proposed bilevel optimization could be difficult because the actor policy is learning and thus keeps changing its behavior over time. Theoretically, this non-stationary actor's behavior makes the reward function (i.e., the entropy reward) non-stationary from the prompt-generation policy's perspective, which could render the Markov property invalid and induce unstable training of the prompt-generation policy. Would it be possible to ask for more discussion about this possible non-stationarity issue, which is one of the main challenges in multi-agent learning?
6. Because the domain is POMDP (Section 2), would the Vanilla PPO use RNN/LSTM/transformer architecture instead of MLP architecture (i.e., no memory)?

### Questions
1. I hope to ask the authors' responses to my concerns (please refer to the weaknesses section for details).
2. The prompt-generation policy aims to minimize the actor policy's entropy. However, I am unsure whether this is the correct objective to optimize for because 1) the actor policy may be certain but certain about incorrect actions (i.e., low uncertainty but convergence to sub-optimal actions), 2) for some domains, an optimal policy could be stochastic not deterministic, and 3) a positive entropy could help exploration. 
3. The proposed bilevel optimization could be difficult because the actor policy is learning and thus keeps changing its behavior over time. Theoretically, this non-stationary actor's behavior makes the reward function (i.e., the entropy reward) non-stationary from the prompt-generation policy's perspective, which could render the Markov property invalid and induce unstable training of the prompt-generation policy. Would it be possible to ask for more discussion about this possible non-stationarity issue, which is one of the main challenges in multi-agent learning?
4. Because the domain is POMDP (Section 2), would the Vanilla PPO use RNN/LSTM/transformer architecture instead of MLP architecture (i.e., no memory)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the Bilevel-LLM approach for solving complex RL tasks. Bilevel-LLM (1) trains a promp-generating policy, (2) applies chain-of-thought reasoning to the prompt, and (3) trains an action policy conditioned on the final chain-of-thought output. The authors evaluate on several simple tasks (ChainWorld, FourRooms) and a more complex Overcooked task, where the authors demonstrate that their approach works better than several baselines.

### Strengths
- The paper is generally clearly written, with the algorithms and objective functions clearly written out. 
- I believe the approach of using a policy to generate prompts for a CoT process that conditions an action policy is novel.
- The experiments and ablation studies convincingly show the value of the method. In particular, the ablation study over a random prompt generation baseline demonstrates the value of training the prompt generating policy, and the small performance increase over GFLan demonstrates the benefit of the more complicated bi-level approach.

### Weaknesses
 - Some of the notation is complicated and I believe it could be simplified. In particular, there are many subscripts (t+, I, etc.) that I think could be removed that could make the presentaiton of the technical method a bit easier to read.

- The performance of the method is not that much higher than GFLan, which is surprising given that GFlan has no chain-of-thought reasoning. This implies that perhaps that chain-of-thought reasoning is not very effective for the tasks (given that it is a much more complex process), or that the tasks are too simple for the method to demonstrate it's benefits.

Minor:
The "t+" notation seems a bit unnecessary. I believe it can be removed and the equations would still make sense.

### Questions
- For reproducibility purposes, it would be great if the authors could report all learning rates & hyperparameters used in the experiments (also for baselines), as well as the hyperparameter sweeping strategy.
- What does the subscript "I" mean in the "\gamma_I" discount factor in Eq 1 & 4? I did not find this notation explained previously.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the leader-follower bilevel framework, for learning relevant prompts for task-relevant actions. To verify the effectiveness of the proposed method, experiments are conducted on the Overcooked and FourRoom environments.

### Strengths
1. The paper is well organized.
2. Figure 1 provides an intuitive illustration of the proposed method.

### Weaknesses
1. [Major] The presentation of this paper is vague and confusing. For example, this paper introduces many notations in the POMDP setting, but as far as the reviewer understands, the main usages of these notations only help the definition of policies $\pi_\phi,\pi^{re},\pi_\theta$. However, $\pi_\phi,\pi^{re},\pi_\theta$ themselves still remain unclear to the reviewer, even with the fancy math notations.  See other detailed examples in the “Question” section.
2. [Major] The experimental results are not convincing. After reading Section 4 (Experiments) and Appendix 8 (Detailed descriptions of experiments), the reviewer still could not understand how the experiments are conducted (e.g., what are the inputs and outputs of each environment, and what are the reward functions). The reviewer would like to see the inputs, outputs, and reward functions of each environment clearly introduced, not being vaguely described in the text. See detailed questions in the “Questions”.
3. [Minor] The paper seems to be overclaiming the contribution. In the first sentence of page 2, the author claims that “we take the first step towards a fully unified LLM framework that learns to perform complex tasks”. The reviewer does not believe the current paper is the “first” (see e.g., [1]), nor the Overvooked or FourRoom are complex enough (compared to [MineDojo](https://minedojo.org/) studied in [1]).

### Questions
> The presentation of this paper is vague and confusing.

1. What are the exact inputs and outputs (e.g., are they symbolic vectors of the tasks texts) of $\pi_\phi,\pi^{re},\pi_\theta$? The reviewer has carefully read through section 2, and the reviewer guesses that (1) $\pi_\phi$ is a text-to-text mapping; (2) $\pi^{te}$ is a state-to-text mapping, but what exactly is the state space, is it text or images, or vectors? (3) $\pi_\phi$ is a mapping from (observation, text) to action, but what are the observation and action spaces (text, symbolic vectors, or others)?
2. In the last paragraph **CoT reasoning with Prompts**, the authors mentioned “$\pi^{re}$ is severed by an LLM such as GPT3.5”, what exactly is $\pi^{re}$? If it is GPT3.5, which version of GPT3.5 (`turbo`, `turbo-16k`, or others)? If not GPT3.5, what exactly is it?
3. In paragraph **Action policy training via PPO with LLM** of page 6, the authors mentioned “we use the pre-trained LLM, FLAN-T5 small… as the action policy”. Does this suggest that $\pi_\theta$ itself is also an LM? If yes, could the author clarify how the state space serves as text inputs to $\pi_\theta$ and how the text outputs of $\pi_\theta$ are post-processed into actions? 

> The experimental results are not convincing.

1. What is the reward function in the `overcooked` environment? In Section 8.1 (Environment), the authors have introduced the reward functions for ChainWorld and FourRoom. But for Overcooked, the author mentioned in the last sentence of paragraph “Overcooked” that: “we use an incremental reward shaping scheme where we give a small reward to agent for…” What is the incremental reward shaping scheme, and how is the reward function actually defined in this case?
2. The experimental results presented in Figures 2 and 3 only slightly surpass the previous SOTA GFlan by a small margin, given the fact that only 5 random seeds are selected, it is hard for the reviewer to believe that the proposed method is actually better than GFlan. Note that in the original paper (Figure 3 of GFlan [1]), GFlan actually improves the prior baselines by a huge margin.


[1] Carta, Thomas, et al. "Grounding large language models in interactive environments with online reinforcement learning." arXiv preprint arXiv:2302.02662 (2023).

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
