# Motif: Intrinsic Motivation from Artificial Intelligence Feedback

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Exploring rich environments and evaluating one's actions without prior knowledge is immensely challenging.
In this paper, we propose Motif, a general method to interface such prior knowledge from a Large Language Model~(LLM) with an agent. 
Motif is based on the idea of grounding LLMs for decision-making without requiring them to interact with the environment:
it elicits preferences from an LLM over pairs of captions to construct an intrinsic reward, which is then used to train agents with reinforcement learning.
We evaluate Motif's performance and behavior on the challenging, open-ended and procedurally-generated NetHack game.
Surprisingly, by only learning to maximize its intrinsic reward, Motif achieves a higher game score than an algorithm directly trained to maximize the score itself.
When combining Motif's intrinsic reward with the environment reward, our method significantly outperforms existing 
approaches and  
makes progress on tasks where no advancements have ever been made without demonstrations.
Finally, we show that Motif mostly generates intuitive human-aligned behaviors which can be steered easily through prompt modifications, while scaling well with the LLM size and the amount of information given in the prompt.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method called Motif for tackling the exploration problem in RL by making use of an LLM to learn an intrinsic reward function, which is used to learn a policy using a standard RL algorithm. The testbed for this approach is the NetHack Learning Environment, a popular procedurally generated environment with sparse reward. This approach leads to strong improvements in performance over prior approaches without demonstrations and also results in human understandable behaviours.

### Strengths
- Figure 1 provides a nice clean bird's eye view of the overall approach and helps with readability.
- The evaluation of the agent for not just the game score but also other dimensions provides a helpful qualitative assessment of the proposed approach and baselines through the spider graph in Figure 4.
- The ablation experiments for the approach are quite exhaustive, covering scaling laws, prior v/s zero knowledge, rewordings of the prompts, etc.

### Weaknesses
 - Using a 70-billion LLM to generate a preference dataset from given captions is quite expensive; while I understand this is out of the scope of the paper, perhaps using a large VLM to annotate frames without captions might have been more economical?
- Given that one of the key contributions of the paper is the intrinsic reward function that is learnt from preferences extracted from the LLM, it might be worthwhile having a baseline that gives preferences using a simpler model (say sentiment analysis) and learn the RL policy using this intrinsic reward model.



### Questions
- In the part on "Alignment with human intuition", the paper mentions that the agent exhibits a natural tendency to explore the environment by preferring messages that would also be intuitively preferred by humans. Is this a consequence of having a strong LLM, or is it due to the wording of the prompt?
- An ablation over $\alpha_2$ has been provided in the appendix, but the value of the coefficient for the intrinsic reward $\alpha_1$ is kept fixed at 0.1; could you explain the reason behind that?
- In Figure 6c, the score for the reworded prompt is quite low but its dungeon level keeps steadily rising compared to the default prompt. Is this a case of the agent hallucinating its dungeon level due to a very high intrinsic reward, or is it something else?

### Soundness
3 good

### Presentation
3 good

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
The paper introduces Motif, a method for integrating the common sense and high-level knowledge of LLMs into reinforcement learning agents. Motif works by eliciting preferences from the LLM based on pairs of event captions. These preferences are then translated into intrinsic rewards for training agents. The authors test Motif on the NetHack Learning Environment, a complex, open-ended, procedurally-generated game. The results show that agents trained with Motif's intrinsic rewards outperform those trained solely to maximize the game score. The paper also delves into the qualitative aspects of agent behavior, including alignment properties and the impact of prompt variations.

### Strengths
1. The paper is clear and well presented.
2. The idea of using intrinsic rewards generated from an LLM's preferences is both innovative and practically useful, potentially paving the way for more human-aligned agents.
3. The method scales well with the size of the LLM and is sensitive to prompt modifications, offering flexibility and adaptability.
4. The paper provides a comprehensive analysis, covering not just the quantitative but also the qualitative behaviors of the agents.

### Weaknesses
1. The paper could benefit from a more extensive comparison to other methods, especially those that also attempt to integrate LLMs into decision-making agents. Specifically, the paper lacks a detailed comparison to methods that use LLMs to generate reward functions or provide guidance for exploration, making it difficult to assess the novelty and advantages of Motif compared to existing approaches.
2. There is a lack of discussion on the computational cost and efficiency aspects of implementing Motif. The paper does not provide details on the time and resources required for generating the event captions, eliciting preferences from the LLM, and training the agents with the resulting intrinsic rewards. This is a critical consideration for the practical applicability of the method, especially when dealing with complex environments like NetHack.
3. While the paper makes a strong case for Motif, it doesn't delve deeply into the limitations or potential drawbacks of relying on LLMs for intrinsic reward generation. The paper should discuss potential biases in the LLM's preferences, the impact of prompt engineering on the generated rewards, and the possibility of the agent exploiting the intrinsic reward in unintended ways.

### Questions
1. Could the authors offer insights into why agents trained  on extrinsic only perform worse than those trained on intrinsic only rewards?
2. What's the best strategy to optimally balance intrinsic and extrinsic rewards during training?
3. Can the authors elaborate on the limitations of using LLMs for generating intrinsic rewards? Are there concerns about misalignment or ethical considerations?
4. How robust are agents trained with Motif against different types of adversarial attacks or when deployed in varied environments?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides Motif, a method for training a reinforcement learning (RL) agent with AI preferences. The main idea of Motif is to use AI preferences (or Large Language Model (LLM) preferences), instead of human preferences, for the preference-based RL. More specifically, Motif trains an intrinsic reward model on a LLM preference dataset, and then trains a RL agent by harnessing the intrinsic reward model. In summary, Motif consists of three phases: (1) dataset annotation by a LLM, (2) reward training on a LLM preference dataset, and (3) RL training with the reward model. This paper applies Motif to the NetHack Learning Environment (NLE). The paper uses Llama-2-70B as a preference annotator, and CDGPT5 as a baseline NetHack agent. This paper shows that RL agents trained with Motif's intrinsic reward surprisingly outperform agents trained using the score itself.

### Strengths
- S1. First of all, this paper is well-written and well-organized.
- S2. The idea of using a LLM as a preference annotator for preference-based RL is interesting and promising.
- S3. This paper provides a loss function (equation 1) to train an intrinsic reward model.
- S4. This paper shows that training agents with intrinsic rewards is very effective.

### Weaknesses
 - W1. One of my main questions is whether Motif can be generally applied to other environments. Even though the NetHack Learning Environment (NLE) is a very challenging environment, it seems that the NLE may be one of environments that a LLM can easily annotate preferences. Specifically, the structured nature of the NLE, with its discrete actions and relatively constrained visual space, might make it easier for a LLM to understand and generate meaningful preferences compared to more complex, continuous environments. For example, environments with high-dimensional continuous action spaces, such as those found in robotics, or environments with more complex visual scenes, such as those found in real-world driving scenarios, might pose significant challenges for the LLM preference annotation process. It is unclear how well the LLM would be able to discern subtle differences in agent behavior in these more complex settings, and whether the resulting reward model would be effective for training RL agents.

### Questions
- Q1. Can Motif be applied to other environments beyond the NetHack Learning Environment (NLE)?
- Q2. What a RL algorithm is used for RL fine-tuning?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Motif: 1) replacing human labeling in preference-based RL with LLM labeling, and 2) joint optimization of preference-based and extrinsic rewards to solve the NetHack environment. After collecting sufficiently covered offline data from the existing RL methods, preference labels are annotated using LLaMA 2. Motif trains the preference reward model from those data and leverages it for online training from scratch, jointly maximizing preference-based and extrinsic rewards. Motif exhibits strong performance in staircase tasks from NetHack.

### Strengths
### quality and clarity
- This paper is well-written and easy to follow.

### significance
- The empirical results are strong. It would be notable to solve the difficult, sparse-reward NetHack environments that previous intrinsic-motivation methods cannot solve by leveraging preference-based reward.

### Weaknesses
 - I think the point of this paper is that "joint optimization of preference-based and extrinsic reward helps resolve the sparse reward problems". As the source of feedback, either humans or LLMs are OK. I think describing this as LLM's contribution might be an overstatement.
- As a preference-based RL method, I guess there are no differences from the original paper [1]. In the LLM literature, [2] leverages GPT-4 to solve game environments, and [3] incorporates LLM-based rewards for RL pretraining.
- Terminology: I'm not sure if a preference-based reward should be treated as an "intrinsic" reward. I think it is extrinsic knowledge (from humans or LLM).

[1] https://arxiv.org/abs/1706.03741

[2] https://arxiv.org/abs/2305.16291

[3] https://arxiv.org/abs/2302.06692

### Questions
- Which RL algorithm is used for Motif? I may miss the description in the main text.
- Are there any reason why employ LLaMA 2 rather than GPT-3.5 / 4?

(Minor Issue)
- In Section 2, `... O the observation space ...` might be `... O is the observation space ...`.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
