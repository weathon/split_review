# On Designing Effective RL Reward at Training Time for LLM Reasoning

- Decision: Reject
- Avg Score: 5.17
- Scores: 6, 6, 8, 5, 3, 3

## Abstract
Reward models have been increasingly critical for improving the reasoning capability of LLMs. Existing research has shown that a well-trained reward model can substantially improve model performances \emph{at inference time} via search or best-of-N votes. 
However, the potential of reward models during \emph{RL training time} still remains largely under-explored. 
It is currently unclear whether these reward models can provide additional training signals to RL training that uses sparse success rewards, which verify the correctness of solutions.
In this work, we evaluate popular reward models for RL training, including the Outcome-supervised Reward Model (ORM) and the Process-supervised Reward Model (PRM), and train a collection of LLMs for math problems using RL by combining these learned rewards with success rewards. Surprisingly, even though these learned reward models have strong inference-time performances, they may \emph{NOT} help or even hurt RL \emph{training}, producing worse performances than LLMs trained with the success reward only. 
Our analysis reveals that an LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue for RL training. 
Therefore, we introduce two novel reward refinement techniques, including \textbf{\emph{Clipping}} and \textbf{\emph{Delta}}. The key idea is to ensure the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited. 
We evaluate our techniques with multiple reward models over a set of 1.5B and 7B LLMs on MATH and GSM8K benchmarks, where both \textbf{\emph{Clipping}} and \textbf{\emph{Delta}} consistently stabilize RL training. 
Finally, we also demonstrate that with a carefully designed reward function, pure RL training without any additional supervised tuning can further improve all the evaluated LLMs, including the state-of-the-art 7B LLM Qwen2.5-Math-7B-Instruct on MATH and GSM8K benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work has two important messages for the field of LLM Reasoning: 1) the rewards models, especially the PRM can be hackable. Therefore, integrating them into LLM RL training may lead to hacking this reward performing worse than just removing it. 2) The paper argues that by clipping and then delta-ing the PRM rewards one can actually use these rewards models to gain a boost in their performance.

### Strengths
I think the paper has important messages for LLM reasoning community:

1) The message that PRMs are hackable is important and valuable. Also, the paper digs into showing what goes wrong which provides insight into what actually goes wrong when using them. That the LLM trained with these PRMs leans towards some steps that are correct but does not move us closer to a solution. I think this contribution is also important. 

 2) Also, the paper shows limiting these rewards is not obvious. It is only by mixing the clipping and the delta method that they can boost the performance. This is interesting that it shows the problem is serious, although I don't agree that the clip-delta completely solved it.

### Weaknesses
I think the paper focuses a lot on the boost it gets from mixing the clip and delta. However, I have some concerns if the clip and delta is a generalizable approach. First, the delta mechanism seems unmotivated. There is not nothing wrong with being unmotivated if it works super well. But, I think the gains are modest. The delta mechanism rewards action `a_t` if the reward of action `a_{t+1}` is less which is a very strong change to the RL environment. I understand that some interesting properties like the summation and small change to the returns arise from this, but I believe this is still an unmotivated change to the environment. However, maybe I don’t have the correct intuition on this. It is quite surprising that none of them work well on their own which makes me wonder if there is any intuition behind why this mixture of both works better? I am just afraid that this is not that well motivated.

### Questions
1- What is the motivation behind the delta mechansim? Why should we assign credit to a_t if the reward of a_{t+1} is lower?

2- Can we consider the gains by mixing the clip and delta mechanism are strong and not modest? 

3- Your PRM is trained on automatic data. Is this possible that this hackability issue is because of the noise caused by the automatic procedure and would be avoided when trained on human-data or better PRM data generation (I understand better PRM data generation is itself a research question)?

4- Is there any intuition on why both clip-and-delta should be applied to get a boost and none of them work well in isolation?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper examines the use of learned reward models, such as Outcome-supervised (ORM) and Process-supervised Reward Model (PRM), to enhance reasoning in LLMs during RL training. They show that ORM does not improve and PRM can even hinder RL training due to reward hacking. The authors propose “Clip” and “Delta” to address this.

### Strengths
- The proposed idea is new, interesting, and well-motivated. 
- The paper is easy to read and follow. 
- The addressed problem is of significance.

### Weaknesses
 - More details on the experimental setup could be provided for reproducibility, including the reward thresholds for the Clip and Delta mechanisms and hyperparameters for PPO. 
- Smaller LLMs may offer a larger scope of improvement, and so the proposed methods may seem to have been successful. However, to confirm the advantage, experiments on larger LLMs may be necessary; e.g., the paper reports GPT-4o-2024-08-06’s performance to be 92.9 on GSM8K, which is higher than almost all other models and variations, and offers less scope of improvement.

### Questions
- Any discussion on the computational overhead or ease of integration of Clip and Delta into existing workflows would be beneficial. 
- Although mathematical reasoning is a good testbed, any comments on the potential applicability of these techniques in non-mathematical or multi-modal reasoning tasks?

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
2

### Summary
This work discusses the role of reward models in enhancing the reasoning capability of LLM models during RL training, which is under-explored compared to inference. It shows the impact of popular reward models, the Outcome-supervised Reward Model (ORM) and the Processsupervised Reward Model (PRM), on the performance of LLMs after being combined with the success sparse reward signals on math problems. It was observed that such reward models may not help or even hurt the performance of the LLM due to the reward hacking issue. This work proposes two reward refinement methods to tackle this issue, named Clipping and Delta. Those techniques have shown potential in stabilizing the RL training of a collection of LLMs when evaluated on the MATH and GSM8K benchmarks. In addition, performance improvement across all evaluated LLMs can be obtained by carefully designing a reward function for pure RL training.

### Strengths
- The paper is well-written, and the problem is nicely motivated.
- The empirical results are enough to assess the potential of the reward model, with some techniques for mitigating reward hacking during RL training to enhance the LLM reasoning.
- I appreciate the case study shown in Fig. 2 and the others added in the appendix.

### Weaknesses
## Major Comments:
- We saw in the empirical results that the improvement in the small models was higher than in the larger ones. I disagree with the authors about the importance of evaluating the study or the proposed techniques on larger models.

## Minor Comments:
- Typo in Line 057: "on the reward models, it remains **un**clear whether the reward models can provide additional training".

### Questions
- As far as I understand, the outcome reward (OR) gives a likelihood that the solution is correct. That means a solution can have a success reward of zero but still be close to the correct solution; hence, the likelihood could be relatively high. It can also be high because of the uncertainty of the reward model. **Why do you still think that did not help when combined with the success reward?** I believe a probability of success in the form of reward, instead of ones and zeros, should contribute to the learning. If I understood the outcome reward wrong, then the explanation of the reward models was unclear.

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
3

### Summary
This paper investigates how to effectively use reward models during reinforcement learning (RL) training to improve LLMs' mathematical reasoning abilities. The authors discover that traditional reward models can either be ineffective (in the case of Outcome-supervised Reward Models) or lead to reward hacking through unnecessary repetition of steps (in the case of Process-supervised Reward Models). To address these issues, they introduce two novel techniques - "Clipping" and "Delta" mechanisms - that help prevent reward exploitation while maintaining the benefits of process rewards. Using these refined reward techniques, they demonstrate consistent improvements across various LLMs, including enhancing the performance of state-of-the-art models like Qwen2.5-Math-7B-Instruct on the MATH and GSM8K benchmarks.

The key innovation is showing that while reward models are useful for inference-time improvements, they need careful refinement to be effective during RL training. Their solutions help stabilize training and prevent the model from gaming the reward system through repetitive or unnecessary steps.

### Strengths
Strengths:
1. Identifying the issues with using rewards: The authors systematically analyze both Outcome-supervised Reward Models (ORM) and Process-supervised Reward Models (PRM), revealing important limitations of each approach. They demonstrate that ORMs, despite working well at inference time, don't provide additional benefits beyond success rewards during training. More significantly, they uncover a serious reward hacking issue with PRMs, where models learn to game the system by repeating simple or unnecessary steps to achieve high rewards. This analysis is particularly valuable because previous work primarily focused on using rewards at inference time, making this identification a novel contribution to the field.
2. Experiments: The authors conduct comprehensive evaluations across multiple model sizes (1.5B and 7B parameters) and variants (including Qwen2, Qwen2.5, and both general and math-specific models) on standard benchmarks like MATH and GSM8K. Their experimental design includes thorough ablation studies showing the impact of different components, careful comparisons of various reward mechanisms, and detailed analysis using synthetic examples to demonstrate reward hacking.

### Weaknesses
Limited Novelty:
- Clipping is indeed a well-established technique in the RL community, commonly used to stabilize training
- The concept of bounded rewards is a fundamental principle in RL, not a new innovation
- The Delta mechanism, while presented as novel, essentially implements reward shaping - another well-known concept in RL

The paper's contribution seems more incremental than innovative: It primarily applies known RL techniques to the specific context of LLM reasoning. The main finding that reward models can be exploited during training is somewhat expected given the general challenges of reward design in RL. The solutions proposed (Clipping and Delta mechanisms) are straightforward applications of existing RL principles.

Missing Reward Shaping related work:
1. Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping, Ng et.al 
2. Hindsight credit assignment,  Harutyunyan et.al
3. Rudder: return decomposition for delayed rewards, Arjona et.al
4. Align-RUDDER: Learning from few demonstrations, Patil et.al
5. Modern Hopfield networks for return decomposition for delayed rewards, Widirich et.al

### Questions
My current criticism is regarding the novelty of the paper. I am willing to increase my score if the authors convince me that the clipping and delta are novel enough.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces two methods to prevent reward hacking while training LLM with reinforcement learning algorithms, Clipping and Delta. The paper shows superior results when adding these techniques on top of process rewards, compared to baselines without these techniques.

### Strengths
The paper is written clearly, and well-motivated. Extensive experiments are done, ablating different parts of the algorithm to show that clipping and delta mechanisms are actually helping.

### Weaknesses
Reward clipping is not a novel idea and has been studied before. Reward hacking, even more so. IMO, a valid baseline for this paper needs to be a well-written PRM. However, looking at the baselines used in this paper, whenever PR is used the result is worse than SR alone. Other papers have already shown PRM is better than ORM alone. Clearly, the baseline is too weak and isn't setup correctly.

Basically, the authors are showing evidence that SR + PR + reward-hacking-prevention is better than SR alone, or SR + plain PR. I don't find this to be a new contribution.

The work also lacks direct examination of how these two methods work under the hood. For example, how often is the reward non-zero after clipping? i.e. Is this truly a dense reward? When delta is applied on top of clipping, the argument that the reward is bound no longer holds, because r_process(q, p_k+1) can be 0. So what's really the mechanism in this case?

In Table 2, the experimental results show pretty marginal (or, non-existent) improvements on greedy decoding, on the only valid RL baseline, Qwen2.5-Math-7B-Instruct. The other comparisons are pretty meaningless since we all know RL works & it's not the contribution of this paper.

### Questions
How often is the reward non-zero after clipping? i.e. Is this truly a dense reward?

Why does none of the PRM method in baselines work?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores how to design effective RL rewards models to improve LLMs in mathematical tasks.
It evaluates two popular reward models - ORM and PRM - during RL training.
The authors argue that using these reward models do not improve and even degrade performance during RL training; due to "reward hacking".
The authors propose two ad-hoc reward refinement techniques, Clipping and Delta, and demonstrated their performance improvement.

### Strengths
- The paper has positioned itself well as an NLP paper by referring a number of recent papers on LLM and reward models.
- The solution suggested by the paper effectively improves from previous baseline.

### Weaknesses
 - After indroducing ORM, the paper does nothing about it; since it is introduced and evaluated, we need at least an analysis on why it does not help. 

 - While the paper is suspecting the observed phenomenon as "reward hacking", I would say this is closer to the wrong usage of reward functions. As we have binary correctness label, and ORM and PRM try to get estimation of it with partial generation, all rewards will be nonnegative. In episodic settings without any discount, this naturally lead to the agents that favor long trajectory, i.e., long solution generation, regardless of whether its correct or not. The paper does not tell us about the hyperparameter choice of $\alpha$, but with some large enough $\alpha$, this may lead to agent preferring long wrong generations over short correct generations.

 - The proposed method is, in my perspective, not novel. To solve sparse reward problems, the first go-to should be reward-shaping methods. the proposed delta mechanism can be understood as a potential-based reward shaping method where PRM is the potential function. The proposed clip-delta mechanism can be understood as a potential-based reward shaping method where PRM-clip is the potemtial function. The overall paper can actually be understood as using a reward shaping methods to handle sparse rewards of RLHF, and I believe the paper should position itself well against reward-shaping methods that have been extensively studied in the past.

 - The paper argues that PR-Normed approach overfits and the performance degradation is severe. To see SR+proposed method algorithms do not suffer from the same problem, we need more information, e.g., learning curves of all algorithms.

 - While in this paper the Delta (giving agent no preference on length of generation) or the Clip (giving agent preference on shorter generation) worked, it depends on the task; on the tasks where longer generations are advantageous, both modifications might not be beneficial. In that sense, the paper only evaluates on single task, and it would not be a robust assessment on the algorithm's performance.

### Questions
- Why does ORM not suffer from the same problem?
- What's the difference between PRM and ORM: why PRM does help when ORM does not help?
- If we use PR-Clip itself, then it becomes an algorithm that prefers shorter generation as we increase $\eta$. Do you have results on the performance on varying $\eta$?

### Soundness
2

### Presentation
2

### Contribution
2
