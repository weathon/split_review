# Enhancing Decision-Making of Large Language Models via Actor-Critic

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Large Language Models (LLMs) have achieved significant advancements in natural language processing tasks, yet they encounter challenges in complex decision-making scenarios that require long-term reasoning and alignment with high-level objectives. This paper introduces a novel gradient-free LLM-based Actor-Critic framework, termed LAC, which addresses these limitations by integrating both action generation and action evaluation mechanisms. Our approach employs two distinct critics: a language-based critic that provides context-sensitive feedback and a value-based critic that offers quantitative assessments of expected long-term rewards. This dual-critic architecture enhances decision-making by leveraging the complementary strengths of both critics, enabling contextually appropriate and more robust action selection. Additionally, we propose a gradient-free policy improvement method that reduces computational overhead, facilitating efficient updates to the actor’s policy without the complexities of gradient backpropagation. We validate the effectiveness of LAC across diverse environments that cover both high-level action space (ALFWorld) and low-level action space (BabyAI-Text), demonstrating its superior performance compared to existing state-of-the-art methods. Our method outperforms other state-of-the-art baselines using the same 7B/8B open-source LLMs and even exceeds a strong baseline ReAct using GPT-4 in most settings. Our findings highlight the efficacy and generality of the dual-critic Actor-Critic framework in enhancing LLM-based decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose a self-reflecting flow architecture for multi-step problem solving which is informed by classical RL concepts.
On AlfWorld and BabyAI-text environments it exhibits good performance.

Although components of the architecture have been previously proposed, the combination is sensible.
* "Lang-critic": this components reflects upon the goal and the history and augments the prompt for the actor component.
* "actor": proposes new actions given the goal, the history, and the lang-critic augmentation.
* "rollout simulator": given a goal, history, and action: simulates the next few steps (under what policy?)
* "value-critic": given a goal, history, proposed action, and simulated future under this action: estimate the likelihood of task completion

Multiple actions are sampled from the actor at each round, scored by the value critic, the distribution is reweighted via exponential-log-odds, and then the greedy action is selected.

There are some ablations studies to provide insight into the importance of the components, and comparisons to classical RL techniques.

### Strengths
In a zero-shot context, the architecture and results are facially reasonable, given there are numerous prior results indicating large foundation models can exhibit improved performance when composed via a self-reflecting architecture, and given prior art that reasonable synthetic rollouts can improve value estimation analogous to chain-of-thought for possible futures.

On balance, despite the poor exposition around fine-tuning, I believe readers would net benefit from exposure to this paper because of intriguing concepts such as: 1) exponential log-odds reweighting of a prior action distribution is superior to policy gradient for sculpting the action distribution in the small-sample regime [line 375 vs. line 833]; 2) foundational [rather than component or architecture specific] fine-tuning induces end-to-end improvement when composed [lines 1058-1066].

### Weaknesses
This paper has two kinds of weaknesses.  

The first kind is due to the nature of academic work, which is resource constrained (small teams; limited compute).   This induces a set of "easy" criticisms such as "insufficient experimental validation" or "excessive focus on the small sample regime".  I believe both authors and readers are well-aware of practical constraints, so this reviewer will not weigh such concerns heavily.

The second kind is insufficient description to allow the reader to understand what was done.  Specifically, the weakest parts of the paper are all related to the impact of fine-tuning, which is not sufficiently described (see questions).  Authors could improve both the intelligibility and the impact of this paper via more detail.

### Questions
1. Authors mention fine-tuning under a limited budget (e.g., 18 trajectories), following the specification on lines 1048-1057.  However what is the source these trajectories?  Are they human annotated trajectories?  Trajectories sampled from the zero-shot architecture, perhaps conditioned on task success?  How are the special tokens which indicate positive/negative judgement produced for the fine-tuning data?  It is not clear, and in the small-sample regime, these details are critical.
   1. Related: Under what policy (action distribution) is the future simulator generating?  If the reweighted action distribution becomes divergent from the prior, will the future simulator be invalidated?
1. Authors argue equation (6) on line 375 is a more sample efficient way to incorporate labeled trajectory information than conventional policy gradient via the equation on line 833.  However the value-critic on line 833 does not take simulated rollouts as a parameter.  Perhaps this is a typo?  Otherwise the comparison is invalid.
1. In figure 8, it is unclear why LAC+fine-tuned-actor underperforms LAC.  The lack of commentary raises reader suspicion.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Although large language models (LLMs) have shown impressive capabilities in natural language processing tasks, they struggle with complex reasoning tasks. One common approach to tackle this issue is to train LLMs using reinforcement learning (RL); however, RL methods have several drawbacks. The authors propose a novel gradient-free Actor-Critic framework based on LLMs to overcome these limitations. This new framework includes an actor and a critic component, distinguishing it from previous approaches. Notably, the Critic is designed to provide feedback in either language or numerical form to help update the actor.

### Strengths
- The ability to help LLMs reason in complex decision-making scenarios is a very important task.
- The structure of the paper was well organized and easy to follow, aside from some terminology framing issues.
- The paper effectively demonstrates how different types of actor feedback—reasoning, evaluation, and future trajectory prediction—affect downstream performance.

### Weaknesses
 - The terminology used in the paper could be more precise, particularly in relation to terms commonly found in the reinforcement learning literature.
- The paper is missing important baselines needed to understand the performance gain claims.

### Questions
- Is it reasonable to summarize the algorithm differences in the following manner: ReAct includes reasoning + actor, Critic only includes future trajectory + actor, and Lang-critic includes evaluation + actor?
- Why does the value critic require a future trajectory, and how does it perform without future trajectories? 
- How does ReAct, combined with a value critic, perform?   
- How does ReAct, combined with a language critic, perform?
- Is the prior \pi_{LLM} the same LLMs used for Q_{LLM} for computing the critic values?
- How does language critic + value critic perform? (Essentially LAC without update action distribution, instead using the critic values to choose an action)

### Soundness
3

### Presentation
2

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
The paper proposes a new way to tune LLMs to behave as agents, by combining the initial action probabilities with predictions by a language and value critic. The language critic adds natural language feedback to various candidate actions, and the value critic uses search to assign a value (or probability of success) to those actions. The method achieves impressive empirical performance on popular benchmarks such as ALFWorld against actor-only and critic-only baselines.

### Strengths
The paper is clearly written and tackles an important problem, as many applications of LLMs rely on them to behave as long-term agents rather than simply generate responses. 

The method is sensible, using the language critic to refine the action space, then combining predictions by the value critic with the base LLM policy via a simple perturbation of initial action probabilities. 

Finally, The empirical results are impressive, outperforming previous state-of-the-art techniques such as ReAct by a large margin.

### Weaknesses
Though the method is impressive, I have some concerns about its generalizability.

Namely, the authors only consider tasks with small action spaces, where evaluating each action individually is tractable. In many more realistic tasks such as dialogue, I imagine that the action space would be more open-ended and am unsure how to adapt the proposed method. 

In addition, the tasks considered rely on being able to simulate future trajectories with high fidelity, which may be harder to do in more complex environments. Specifically, it is likely much harder to faithfully predict trajectories when the agent is engaging with another human rather than simply moving around in a static environment.

Finally, the value critic currently only works for tasks with binary outcomes (success or failure).

### Questions
Overall, I think the paper makes a valuable contribution. However, I do think there are several areas that the authors could address to further strengthen it:

(1) How would the method change when the task has a potentially infinite action space (such as in dialogue)?

(2) Have the authors experimented with tasks with more expressive outcomes/rewards? I am curious if both critic can still behave well when there are more nuanced outcomes than just success or failure. 

(3) While the benchmarks are well-known, I think they are perhaps not realistic of tasks that people might actually want LLMs to accomplish. For example, it would be interesting to see the authors evaluate on tasks considered in the GDP-Zero paper such as donation solicitation [1].

[1] https://arxiv.org/abs/2305.13660

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces LLM-based Actor Critic framework (LAC) to improve decision-making capabilities of LLM agents through an integration of the actor and the critic. LAC makes use of two different critics including a language critic that provides contextual information and a value critic that provides more quantitative information. The paper also proposed a gradient-free policy improvement approach using two critics without incurring costly backpropagation processes. The effectiveness of LAC is demonstrated in Alfworld and BabyAI-test, and even surpasses GPT4 with ReAct.

### Strengths
This paper addresses an important and relevant problem of improving decision-making capabilities of LLM agents. 

It is nice that policy improvement can be achieved without incurring costly gradient updates and loss backpropagation.

The paper shows improvements on two popular benchmarks including Alfworld and BabyAI.

### Weaknesses
 The motivation that "these methods typically adopt either an actor only or critic only approach" (line 42-43) misses many related works. The paper relies on [1] to be the only paper that discusses actor critic methods for LLM agents but many important related works are missing. Even PPO is commonly considered as an actor-critic method where it has an actor that estimates the V function to reduce variance for policy gradient estimation. Thus, many prior works that use PPO for LLM agents should be considered as actor-critic methods (e.g. [2]). Retroformer [3] can also be considered to be an actor-critic method where the critic is a natural language based critic. Other works also applied value-based actor critic methods to LLM agent tasks (e.gl [4]).

The novelty of the method is limited. The language critic and value critic are two main proposals in this paper. However, the language critic is relatively simple and can be considered as a direct use of CoT [5] where the agent is asked to generate thoughts reflecting on the previous round actions before taking actions. The objective of the value critic is also similar to constrained decoding [6] that has been widely used in the alignment domain without the need of performing gradient updates on models.

The writing of the paper, and in particular the motivation (see above) and the experiment section can be improved. Section 5.2 and 5.3 only state the the proposed methods are better than baselines and other ablations without investigating into the reason of the gap. E.g. Why is LAC so much better than ReAct/ RAP, and is there any finding of comparing the performance of LAC with different base models. The experiment section does not provide such necessary analysis information.

It is unclear how generalizable and computationally efficient the proposed method is. In particular, it seems that the method can only be applied to tasks with a finite action space and it is unclear if the method can generalize to realistic tasks with unbounded action space such as web browsing.

The tasks used in this work are more on the simple side. It would be interesting to see if the proposed method can work in more challenging tasks such as web browsing, coding, minecraft etc.

### Questions
37: long-time horizon -> long horizons

151-152: "Due to the auto-regressive nature of LLM, it does not do reasoning and planning explicitly." This seems controversial. Chain-of-thought/o-1 are also auto-regressive decoding, but arguably they have some reasoning in them. Same with 152-154, "Accordingly, LLM
with actor-only methods often struggles with complex tasks that require multiple steps of planning and reasoning".

Please see weakness.

### Soundness
2

### Presentation
1

### Contribution
2
