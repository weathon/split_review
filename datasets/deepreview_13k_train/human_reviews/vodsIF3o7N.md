# On the Modeling Capabilities of Large Language Models for Sequential Decision Making

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
Large pretrained models are showing increasingly better performance in reasoning and planning tasks across different modalities, opening the possibility to leverage them for complex sequential decision making problems. In this paper, we investigate the capabilities of Large Language Models (LLMs) for reinforcement learning (RL) across a diversity of interactive domains. We evaluate their ability to produce decision-making policies, either directly, by generating actions, or indirectly, by first generating reward models to train an agent with RL. Our results show that, even without task-specific fine-tuning, LLMs excel at reward modeling. In particular, crafting rewards through artificial intelligence (AI) feedback yields the most generally applicable approach and can enhance performance by improving credit assignment and exploration. Finally, in environments with unfamiliar dynamics, we explore how fine-tuning LLMs with synthetic data can significantly improve their reward modeling capabilities while mitigating catastrophic forgetting, further broadening their utility in sequential decision-making tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors study how Large Language Models (LLMs) can produce decision-making policies, either by generating actions or by creating reward models for reinforcement learning (RL). The authors use experimental results to reveal that LLMs excel at reward modeling, particularly when using AI feedback, and fine-tuning with synthetic data enhances performance in unfamiliar environments, helping prevent catastrophic forgetting.

### Strengths
1. The authors perform extensive experiments to evaluate the capabilities of large language models (LLMs) in sequential decision-making tasks. Specifically, they demonstrate that using LLMs to generate preference data and then train a reward model for RL training has the highest performance gain compared with other methods such as directly modeling policy by LLMs. This conclusion seems interesting and helpful for future works in designing RL agents incorporating LLMs.

2. The experiments in Fig. 3 and Fig. 4 clearly illustrate the effect of the rewards learned through the LLM Feedback.

3. It is interesting that the authors show that prompting engineering can steer LLMs for active exploration on the 
NetHack task, which approximates the count-based exploration bonus.

### Weaknesses
1. The related works section is very incomplete. The authors should discuss more recent works that study LLM decision-making problems and self-rewarding of LLMs such as [1]-[7]. The introduction of LLM for better reward design on RL is also studied in [8] and should be discussed carefully.

2. The authors compare direct and indirect policy modeling and use experiments to show that indirect policy modeling attains higher performance in multiple tasks. However, I am a little unconvinced about the experimental configuration, where the authors only query the GPT for the direct policy modeling but train an RL agent with multiple steps for the indirect policy modeling. It seems that the computation cost and the number of interactions with the environment are not controlled. Moreover, it has been shown in ([1]-[3]) that LLM can also serve as a critic model to give a numerical estimated value in the direct policy modeling. Maybe the authors should also add an experiment to analyze what would happen if the estimated reward from the indirect policy modeling were incorporated into the direct policy modeling. In this case, no RL training is involved and computation cost is easier to control.

3. Minor typos: Line 762: "except fro".

### Questions
1. When reporting the final results in Fig 1, Fig 2, and Fig 6, do the authors control the number of interactions with the environment? I'm also interested in understanding how performance changes with an increasing number of interactions, as shown in the learning curves typically found in reinforcement learning (RL) papers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studied the capabilities of Large Language Models (LLMs) for reinforcement learning (RL) in interactive decision-making tasks, by directly producing policies or indirectly generating rewards for policy optimization.

### Strengths
1. The paper is well-written and easy to follow.
2. The experiments are conducted on various environments.

### Weaknesses
1. The motivation of this paper is limited. One conclusion of the paper is that leveraging the feedback from the LLM to optimize the policy is better than using the LLM directly as a policy. However, since the latter is fine-tuning free, it is not surprising that the former is better. Even if the AI feedback is noisy, as long as the overall feedback is accurate, fine-tuning the policy against it can obtain some improvements.
2. The policy modeling and reward modeling abilities of LLMs in decision-making tasks have been widely studied in previous works [1,2]. No new methods are proposed in this paper, and the novelty is thus limited compared to these works.
3. The analysis is also not convincing. The authors claim that AI feedback helps better credit assignments. However, given only the training curves, it is not clear when and why credit is better assigned.

### Questions
See weakness.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the potential of large language models (LLMs) for tackling complex sequential decision-making problems in reinforcement learning (RL). The authors investigate two approaches: using LLMs to directly generate actions or indirectly generate reward models that guide RL agent training. Their findings demonstrate that even without specialized fine-tuning, LLMs excel at reward modeling. Notably, leveraging AI feedback to craft rewards emerges as a highly effective and generalizable strategy. This approach enhances performance by improving both credit assignment and exploration within the RL framework. Furthermore, the authors address the challenge of unfamiliar environments by demonstrating that fine-tuning LLMs with synthetic data significantly boosts their reward modeling capabilities. Importantly, this fine-tuning process effectively mitigates catastrophic forgetting, preserving the LLM's broad knowledge base.

### Strengths
## Pros

- The studied topic is very interesting. The authors explore the sequence modeling capability of large language models in the context of reinforcement learning, which can be of interest to a large number of researchers in the community
- The authors study either directly using LLM as the policy or leveraging LLM for decision-making and conduct numerous experiments
- The authors show that without task-specific fine-tuning, current LLMs only show limited decision-making capabilities when directly generating actions. Furthermore, the authors find that AI-feedback-based rewards produce dense functions that correlate positively with high-quality value functions. Such reward functions can significantly reduce the difficulty of assigning credit by redistributing rewards across different steps within a trajectory. Some of these observations and conclusions are interesting and can be useful for researchers, e.g., using LLM to directly output scalar reward signals can be surprisingly good on some tasks
- The results reported are averaged over 10 seeds, which is great considering the unstable nature of RL

### Weaknesses
## Cons

- This paper does not propose any new method and looks more like an empirical paper that investigates the application of LLMs in either direct policy modeling or its capability of facilitating policy learning. Although I agree that such kind of paper is also of importance to the community, its technical novelty is still somewhat weak.
- Some conclusions derived by the authors are not surprising. For example, in environments with unfamiliar dynamics, fine-tuning LLMs with synthetic data can significantly improve their reward modeling capabilities while mitigating catastrophic forgetting. Many of the observations are actually known or acknowledged by many scholars and this paper seems to verify them through some designed experiments
- Another concern is that the conducted experiments may not be necessarily sufficient to back up the observations and conclusions in this paper. I list some of them below
  - the studied topics are limited and some selected topics are too broad to be covered in depth within a 10-page ICLR paper. The considered experimental settings are limited as described in Section 3 (lines 207-215), i.e., the authors only study approaches that can directly interface with the action space supported in the environment and assume that LLMs are used without any gradient update. When dealing with indirect policy learning, the authors only consider reward as code. Yet, there are many other options, e.g., LLMs to execute high-level plans for the agent, etc. Furthermore, the authors only consider a simplified version of reward as code without introducing some extra components or tricks as recent works do [1, 2, 3]. When using LLMs for exploration, the authors do not consider the possibility of letting LLMs write intrinsic reward functions, constructing intrinsic rewards [4, 5], etc.
  - the number of the base LLMs is limited. The authors used the closed-source GPT-4o model for direct policy modeling and the open-source Llama 3 for indirect policy modeling when environment observations consist of text, and PaliGemma when environment observations consist of pixel images. The number of LLMs is quite limited, making it hard to tell the significance and applicability of the observations and conclusions
  - the authors do not compare many baselines in this paper, e.g., the authors only consider the count-based exploration method in Section 4.2 (Figure 5). It would be better to compare against stronger baselines.

### Questions
- It seems that this work has some preliminary requirements for the LLMs to make it function well, e.g., chain-ot-thought (CoT), in-context learning, and self-refinement, as described in Section 2.1. How important are these components to the sequential decision-making capabilities of the LLMs? How do they affect the direct or indirect policy modeling of LLMs? 
- Under many real-world scenarios, we often expect a timely or frequent decision-making ability of the agent. When using LLMs directly or indirectly during the decision-making process, how can we guarantee that the decision is made timely yet effective?
- How much expert data do you use to fine-tune the PaliGemma model in Section 5? How about a different dataset quality, will there be a significant difference? I would expect a more in-depth discussion on fine-tuning LLMs here

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
4

### Summary
The paper investigates how LLMs can be leveraged for RL, comparing direct policy generation versus indirect reward modeling approaches across diverse domains. The authors find that using LLMs to generate reward models, particularly through AI feedback preferences, yields better and more consistent performance compared to direct policy generation. They also explore fine-tuning approaches and analyze how LLM-based rewards can help address core RL challenges.

### Strengths
- Comprehensive empirical evaluation across diverse domains.
- Interesting exploration of fine-tuning trade-offs between direct and indirect approaches.
- The paper is well written and easy to follow.

### Weaknesses
The proposed method relies on consistent preference feedback from LLMs to construct reward signals, but doesn't adequately address cases of preference uncertainty. Consider a scenario where the LLM assigns similar preference probabilities to different states, or worse, provides inconsistent rankings when the same state pair is presented multiple times with slightly different prompts.
	- So, what happens when the LLM expresses low confidence or contradictory preferences?
	- Could inconsistent preferences lead to unstable reward signals that harm policy learning?

The paper demonstrates the method primarily on environments where progress is relatively obvious (e.g., clear Wordle feedback, discrete game states in NetHack). However, many real-world tasks involve subtle, continuous progress where improvements may be hard to detect from observations. I have several concerns regard this problem:
	- How sensitive is the LLM's preference detection to small state changes?
	- Could the method miss important incremental progress by only detecting large, obvious changes?

Sec 4.1 shows some evidence that AI feedback can help with credit assignment, the underlying mechanism isn't clear. In complex tasks, progress often results from a sequence of coordinated actions rather than single decisions. Can the method distinguish between critical and auxiliary actions when both contribute to the final outcome?

### Questions
- The proposed method relies on consistent preference feedback from LLMs to construct reward signals, but doesn't adequately address cases of preference uncertainty. Consider a scenario where the LLM assigns similar preference probabilities to different states, or worse, provides inconsistent rankings when the same state pair is presented multiple times with slightly different prompts. 
	- So, what happens when the LLM expresses low confidence or contradictory preferences? 
	- Could inconsistent preferences lead to unstable reward signals that harm policy learning?
- The paper demonstrates the method primarily on environments where progress is relatively obvious (e.g., clear Wordle feedback, discrete game states in NetHack). However, many real-world tasks involve subtle, continuous progress where improvements may be hard to detect from observations. I have several concerns regard this problem:
	- How sensitive is the LLM's preference detection to small state changes?
	- Could the method miss important incremental progress by only detecting large, obvious changes?
- Sec 4.1 shows some evidence that AI feedback can help with credit assignment, the underlying mechanism isn't clear. In complex tasks, progress often results from a sequence of coordinated actions rather than single decisions. Can the method distinguish between critical and auxiliary actions when both contribute to the final outcome?

### Soundness
3

### Presentation
3

### Contribution
2
