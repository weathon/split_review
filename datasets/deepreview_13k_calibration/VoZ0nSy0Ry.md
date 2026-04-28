# Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
In the endeavor to make autonomous robots take actions, task planning is a major challenge that requires translating high-level task descriptions into long-horizon action sequences. Despite recent advances in language model agents, they remain prone to planning errors and limited in their ability to plan ahead. To address these limitations in robotic planning, we advocate a self-refining scheme that iteratively refines a draft plan until an equilibrium is reached. Remarkably, this process can be optimized end-to-end from an analytical perspective without the need to curate additional verifiers or reward models, allowing us to train self-refining planners in a simple supervised learning fashion. Meanwhile, a nested equilibrium sequence modeling procedure is devised for efficient closed-loop planning that incorporates useful feedback from the environment (or an internal world model). Our method is evaluated on the VirtualHome-Env benchmark, showing advanced performance with better scaling for inference computation. Code is available at~\web.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes formulating long-horizon task planning with LLMs as a fixed point problem, arguing that such a formulation leads to a natural realization of many desirable properties of task planning, including global context when deciding the plan, the ability to recover from errors in drafts of the plan, and the ability to scale inference time compute to yield better plans. The authors draw from the literature of deep equilibrium models [1] to instantiate their idea, proposing a training framework based off of the implicit differentiation algorithm proposed by [1]. The full framework proposed by the authors includes a nested inference algorithm, with an inner loop that solves the fixed point problem for a static context, and an outer loop that sends the plan to the environment for feedback. In the case that the environment cannot be queried online, the authors propose training a world model to simulate environment feedback. In comparisons with baselines, the proposed approach performs the best on the VirtualHome-Env benchmark. 

[1] Bai, Shaojie, J. Zico Kolter, and Vladlen Koltun. "Deep equilibrium models." Advances in neural information processing systems 32 (2019).

### Strengths
1. As the authors mention in their introduction, there is indeed a natural match between the problems faced by task planning (and more generally long-horizon reasoning) and the benefits posed by deep equilibrium models. There appears to be substantial originality in the authors' identification of this match, and their subsequent application of deep equilibrium models to long-horizon task planning.
2. The experimental evaluations are fairly thorough, with many ablation studies I wanted to see present.
3. The manuscript is clear and well written.

### Weaknesses
1. The first row in table 3 seems to correspond to the setting in which no correction is allowed and the synthetic world model is not used (so only the inner loop is run). The results obtained by the proposed algorithm in this setting are however lower than the Tree-Planner baseline results from table 1. What explains this low performance? More generally, why is the synthetic world model needed, and could baseline approaches benefit as well from such a world model?
2. Although prior work has solely evaluated on the VirtualHome-Env benchmark, the results would be more solidified if the authors had chosen an additional benchmark to evaluate on.

### Questions
1. The authors cite [1] as evidence that self-refinement via prompting tends to not lead to successful error corrections. Figure 4 shows an example of error correction by the proposed method with environment feedback (i.e., with both the inner and outer loop). Does self-refinement via fixed point iteration (i.e., only running the inner loop, making it more similar to the setting of [1]) lead to better error correction performance than the approaches studied in [1]? If so, then it would be nice to see some empirical evidence of this or a few sample inference traces.
2. For the experimental results presented in table 2, what is the ratio of the number of calls to the synthetic world model to the number of environment interactions?
3. How does the dynamic allocation of inference compute presented in figure 6b work? What decides how many inference forward passes to take?
4. Is the dataset used for training constructed once, or adaptively generated from the newest solutions to the equilibrium problem?
5. Why can the proposed approach improve better from environment feedback than baselines?

[1] Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. In International Conference on Learning Representations, 2024.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new LLM planning framework via equilibrium models. The goal is to build a long-horizon task planner that can incorporate feedback from the environment as well. The authors start with the limitations of prior LLM planners, such as the lack of bidirectional dependency, and lack of internal error correction. Built on these insights, the authors propose to make LLM planners iterative like equilibrium models. The direct training objective of the equilibrium model is intractable, so the authors proposed a simplified objective built on prior works in theory. The simplified objective involves running the LLM iteratively to a fixed point and imposing supervised training loss only on the fixed point. An associated planning framework is then proposed using the fine-tuned LLM. The authors present empirical results on VirtualHome and compared against previous LM planning frameworks.

### Strengths
The paper is well written. The proposed concept is relatively simple and straightforward. The math is easy to follow. The intuition of self-refinement is grounded.

### Weaknesses
My strongest criticism of of paper is the core math it builds on: the authors say one can simplify Eqn(4) to Eqn (5) per Theorem 3.1 in Fung et al. (2022) under appropriate assumption. Yet the "appropriate assumption" is completely unsatisfied here which makes the entire math perspective unfounded. Specifically, Theorem 3.1 in Fung et al. (2022) on their Assumptions 2.1, 3.1, 3.2, and 3.3; Let's take Assumption 2.1 for example, the mapping used in equilibrium model ($T_	heta$ in Eqn (6) of Fung et al. (2022) and $f_	heta$ in the reviewing manuscript), must be Lipschitz with respect to input. This is absolutely ungrounded for transformer-based LLMs. In fact, ML theory papers always devote a great amount of effort to circumvent this problem just because of how unacceptable it is to assume this transformer. This is not to mention assumptions 3.1, 3.2, and 3.3 in Fung et al. (2022). Therefore, you are not even making a strong assumption, but an assumption that's widely considered wrong for LLMs.

Therefore, I urge all reviewers to review the paper by ignoring the flawed math explanation and examining its merit from its empirical merit. 

The technical contribution becomes very limited if we proceed to ignore flaws in the training objective. The feedback, iterative planner seems to be an obvious solution even considering the environmental feedback perspective. 

I think one straightforward way for the authors to address the flawed training objective is to conduct ablations that uses your planning framework but with original Llama3 8B that's not fine-tuned. This is no way making the math correct but can inform us about the performance of your method without a unfounded training objective. 

I also wonder whether the training procedures in line 204 and 205 are grounded. Specifically, how practical it is to run an LM to reach a fixed point? It seems to me that in a high-dim space like language token sequences, it's really hard to achieve convergence. Is it because the authors specifically prompted it to do so?

### Questions
How practical it is to run an LM to reach a fixed point? How sensitive is convergence with respect to the initial sequence?

How would your method perform without fine-tuning Llama model?

The authors suggested, "they divided the dataset into a training set and three test subsets, including the novel scene set, the novel task set, and the novel scene and task set." Since VirtualHome is a popular benchmark, have you surveyed prior papers about their partitioning of the tasks? Have you attempted using a more conventional partitioning used by prior works?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces a novel approach to long-horizon robotic task planning by addressing limitations in current large language model (LLM) planning agents, which often struggle with foresight and error correction. The authors propose an equilibrium sequence modeling technique that iteratively refines a plan until it reaches a stable state, or equilibrium, without requiring additional reward models or verifiers. This approach allows for efficient closed-loop planning by incorporating environmental feedback, enhancing the robot's ability to plan and adapt in complex tasks. Through self-refinement, the method improves long-horizon action prediction and reduces computation by reusing equilibrium states, resulting in superior performance on the VirtualHome-Env benchmark.

The model integrates a nested feedback system, which combines both internal (world model) and external (environmental) feedback to guide plan refinement, achieving improved executability and success rates compared to existing models. Unlike reinforcement learning-based methods, this equilibrium-based framework is trained in a supervised manner, simplifying training while enabling high computational efficiency. The results demonstrate that the proposed approach outperforms baseline methods on various metrics, indicating its potential for more robust and adaptive robotic task planning in dynamic environments.

### Strengths
If I have understood correctly, the core problem tackled by the paper is really crucial. A lot of approaches are using LLMs as high-level planners. However, multiple evaluations have shown that LLMs are unable to reason over long horizon. With the proposed approach of self introspection, LLMs can be used to aide the planning while *verifying* the LLM generated plan until the equilibrium is reached.

### Weaknesses
I do not have many specific weaknesses of the paper. The major reason for that (which is the biggest weakness and reason for my overall rating) is that the paper is extremely  hard to follow. I was not able to understand the paper properly even after reading it multiple times. As I mentioned in the summary of the paper, I was able to get the overall idea but the details of the approach are still unknown to me. However, here following are some ways in which the paper can be made readable: 

- The paper is not self sufficient. It heavily relies on previous works about equilibrium models and fixed-point iteration methods. Readers who are not familiar with these previous works would fine nearly impossible to read the paper. The paper can be updated by having Background section that discusses these methods. 
-  I did not understand how the self refinement with a fixed $c$ works? If the there is no feedback from the environment, how does the approach know even if the generated plan is correct or not in the first place. 
-  There seems to be some distinction between the "training" and "equilibrium solving via fixed point iteration" but they also seem to be connected. It is not clear from the paper how are they different and how are they connected. 
- How this is exactly connected with LLMs is not clear. What part of the modules are using LLMs are not clear from the paper. Can authors comment on it and make it clear in the paper? 
- How does nested refinement work if the context is similar for the inner loop without any feedback? How does the equilibrium model know what to change between two plans? 
- What are the inputs? What are the assumptions? This needs to be made clear in the paper. 

In general, IMO the writing of the paper needs to be self-sufficient. Which the paper is currently not. Above I have tried to outline some of the points that can be used to update the readability of the paper.

### Questions
Please refer to the weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a self-refining framework for robotic task planning using language model agents. By iteratively refining draft plans until equilibrium, this method enables efficient closed-loop, long-horizon planning. Utilizing a nested equilibrium process, the approach effectively integrates environmental feedback, enhancing task performance and inference efficiency. Evaluated on the VirtualHome-Env benchmark, it demonstrates increased scalability in robotic planning scenarios, supported by an equilibrium-based training method that allows end-to-end learning in a simple supervised manner.

### Strengths
- The introspection inspired approach provides a significant benefit over prompting based methods for similar planning tasks.
- The approach is intuitive and provides a unique perspective on solving planning problems via equilibrium methods.

### Weaknesses
While an inference study of computation is presented, it is unclear whether the training budgets of the competing approaches are fairly represented in the context of the finetuning costs of the world model for the proposed method.

### Questions
1. Are there any iteration-wise results available to show the subsequent effects of feedback over time compared to the other approaches?
2. How is the world model initialized using an LLM?
3. What is the frequency of switching between real experience and synthetic world-model generated experience?
4. Minor typo: L293: “May to easier to train”

### Soundness
2

### Presentation
3

### Contribution
3
