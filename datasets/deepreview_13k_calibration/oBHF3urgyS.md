# Extracting Heuristics from Large Language Models for Reward Shaping in Reinforcement Learning

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Reinforcement Learning (RL) suffers from sample inefficiency in sparse reward domains, and the problem is further pronounced in case of stochastic transitions. To improve the sample efficiency, reward shaping is a well-studied approach to introduce intrinsic rewards that can help the RL agent converge to an optimal policy faster. However, designing a useful reward shaping function for all desirable states in the Markov Decision Process (MDP) is challenging, even for domain experts. Given that Large Language Models (LLMs) have demonstrated impressive performance across a magnitude of natural language tasks, we aim to answer the following question: \textit{Can we obtain heuristics using LLMs for constructing a reward shaping function that can boost an RL agent's sample efficiency?} To this end, we aim to leverage off-the-shelf LLMs to generate a plan for an abstraction of the underlying MDP. We further use this LLM-generated plan as a heuristic to construct the reward shaping signal for the downstream RL agent. By characterizing the type of abstraction based on the MDP horizon length, we analyze the quality of heuristics when generated using an LLM, with and without a verifier in the loop. Our experiments across multiple domains with varying horizon length and number of sub-goals from the BabyAI environment suite, Household, Mario, and, Minecraft domain, show 1) the advantages and limitations of querying LLMs with and without a verifier to generate a reward shaping heuristic, and, 2) a significant improvement in the sample efficiency of PPO, A2C, and Q-learning when guided by the LLM-generated heuristics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of sample inefficiency in RL, especially in sparse reward settings and domains with stochastic transitions. It proposes using heuristics derived from LLMs to shape rewards and improve RL training efficiency. The authors explore the idea of leveraging LLMs to generate plans that act as heuristics for constructing reward-shaping functions, which can help RL agents converge more quickly to optimal policies. Experiments across diverse environments (BabyAI, Household, Mario, Minecraft) demonstrate improvements in sample efficiency.

### Strengths
1. The overall algorithm is straightforward and easy to understand.
2. Experiments are conducted under different settings and environments and the discussion of the experimental results is clear.

### Weaknesses
1.	The LLM prompting part is too simple. According to the illustration, all prompting parts are just necessary to input all state and task information for LLM to process. Also, the verifier part is more like a legal action checker, which is also common in a lot of LLM agent implementations and frameworks. Considering this, the writing illustration is over-complicated and the idea of the prompting part does not preserve too much novelty. Furthermore, the paper dedicates a significant portion of its content (over a page, including the entirety of Section 4) to describing this prompting process, which, if not a core contribution, seems disproportionate.
2.	The writing is not that clear and makes me confused. For example, the figure 1 seems to be confusing. It mentions that the algorithm updates the buffer with shaped rewards, but there is no arrow pointed from the replay buffer. Only an arrow points to the replay buffer. (see more in questions)
3.	The experiment results cannot fully support the argument. According to the result in Table 1, it seems that GPT-3.5 and GPT-4o themselves can already reach a high reward (e.g., 0.9+ for empty room, 0.85+ for LavaGap). Then what is the sense of training RL with these expert-level LLMs? Why not directly imitate these LLM’s policies? Also, the paper needs to take more ablation studies (how different setting influences the performance) and comparisons with other LLM+RL algorithms (for example, [1] also conducted experiments on BabyAI)

### Questions
1.	What specifically is the potential function used in the reward shaping?
2.	Which LLM are you using in Section 5.3?
3.	Why does figure 4 have such a big standard deviation in all 3 tasks?
4.	What is the major limitation of your algorithm?

### Soundness
3

### Presentation
2

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
This paper aims to answer the following question: Can we obtain heuristics using LLMs for constructing a reward shaping function that boost an RL agent's sample efficieny? To this end, authors propose to use off-the-shelf LLMs to generate a plan for an abstraction of the underlying MDP, which will then be used as a heuristic to construct the reward shaping signal for the downstram RL algrithms (e.g., PPO, A2C, etc.). Experiments on multiple tasks, including Baby AI environment suite, Household, Mario and Minecraft domain illustrates the effectiveness of the poposed method.

### Strengths
1. This paper is clearly written and easy to follow.

### Weaknesses
1. [1] focuses on the same problem, i.e., using an LLM for reward shaping to improve the sample efficiency of RL algorithms. It also proposes to use goal-based potential shaping. However, relevant comparisions and discussions are missing.
2. The verifier in the proposed framework should be manully designed, which is task-specific and rule-based, or even burdensome for humans to design.

### Questions
1. In all of the environments, the action space are discrete and has only one dimension. What about multi-dimensional continuous action space or even hybrid action space (e.g., turn right 34 degrees)?
2. For the long-horizon stochastic environments, the LLM will generate a high-level plan, in which a high-level state will serve as a sub-goal 
for reward shaping. How can we determine which sub-goal to use? How can we ensure that a sub-goal is finished?

### Soundness
3

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
4

### Summary
This paper focuses on the challenge of sample inefficiency in reinforcement learning (RL) in sparse reward domains, particularly in the presence of stochastic transitions. The authors propose using Large Language Models (LLMs) to generate heuristics for constructing a reward shaping function that can enhance the sample efficiency of RL agents. Specifically, they leverage off-the-shelf LLMs to generate a plan for an abstraction of the underlying MDP. They conduct experiments in various domains, demonstrating the improved performance of RL algorithms when guided by LLM-generated heuristics.

### Strengths
- The idea of leveraging heuristics fom LLMs for enhancing the sample efficiency of reinforcement learning is interesting and promising.

### Weaknesses
 - My main concern is the contribution novelty. This work heavily relies on the PDDL model introduced in prior research [1]. The use of LLM verifiers or feedback from environments to revise plans is not a novel idea [2, 3].
- The paper lacks a detailed description of the extraction of the PDDL models and the reward shaping functions, which induces a challenging reading experience.
- The experimental domains are limited to grid-world settings with discrete state and action spaces that have explicit semantics, raising significant concerns about scalability and applicability. Specifically, the use of grid-world environments, even with stochastic transitions, does not adequately represent the complexities of real-world RL problems with high-dimensional, continuous state and action spaces.
- The introduction of the evaluation benchmarks in Appendix B lacks details about the observation space, making it difficult to assess whether the proposed method is applicable to tasks with partial observability. It is unclear how the method would handle situations where the agent does not have complete information about the environment state.
- There are no citations regarding the evaluation benchmarks, making it hard to ascertain the representativeness of the evaluation domains, especially for Mario and Minecraft, as their descriptions in the paper do not align with common understandings. The specific versions or modifications of these environments are not specified, making it difficult to reproduce the results or compare them with other studies.
- There is a lack of comparisons with other LLM-enhanced RL methods. For example, the authors mention several related works in Section 2, but none are considered for comparison in the experiments. This makes it difficult to assess the relative performance and advantages of the proposed method compared to existing approaches.
- What is the inference frequency of the LLMs in providing the guide plan? It seems that the proposed method incurs significantly higher LLM inference costs, raising concerns about its practical efficiency. The paper does not provide a clear analysis of the computational overhead associated with LLM inference and how it impacts the overall training time and resource requirements.
- It appears that the proposed method requires substantial manual effort to design the prompts, further raising concerns about its real efficiency compared to manually designed reward functions or human-provided plans. The sensitivity of the method to prompt design and the potential for bias introduced by manual prompt engineering are not adequately addressed.
- There is limited discussion of the paper's limitations. The paper should include a more thorough discussion of the limitations of the proposed approach, including its sensitivity to prompt design, the computational cost of LLM inference, and the limited scope of the experimental evaluation.
- Why is only a tabular Q-learning method utilized in RQ2.2? What is the performance of deep RL methods, such as DQN or PPO? The choice of a tabular Q-learning method limits the applicability of the results to more complex, high-dimensional environments, and it is unclear how the proposed method would perform with more advanced deep RL algorithms.

### Questions
Please take a look at the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a method for reward shaping that leverages plans generated by Large Language Models across three sets of domains and at two levels of abstraction and with an added component of plan verification for one experimental condition. Given a textual description of the environment (which is derived using two separate methods for the deterministic and hierarchical abstraction settings), LLMs are asked to produce a guide-plan, a sequence of actions it guesses will solve the MDP. Using this guide-plan, potential-based reward shaping (PBRS) is used to generate a shaping reward function, which is used to train a variety of RL agents on three sets of environments (including A2C, PPO, and Q-Learning). In another experimental condition, a verifier is used to validate whether the planning actions generated by the LLM are valid, and the LLM is re-prompted if they are not.

### Strengths
- The paper introduces a novel synthesis of LLMs, planning, and reward shaping that, to my knowledge, has not been done before.
- A large number of environments are used to evaluate the method.
- More than one RL algorithm is used to assess the value of the shaped reward function.
- A variety of LLMs are used to assess their abilities to make plans.

### Weaknesses
While the paper presents a novel idea, the pipeline provided seems quite contrived and the presentation of the ideas is slightly confusing and not well-placed in the surrounding literature. Here are a few points of criticism:
1. LLMs are prompted for guide-plans, and verifiers are used to assess the validity of guide-plans, so why not simply use the plans to solve the MDPs outright? As mentioned in the discussion section:
> while we could use PDDL planners to get this abstract plan, these planners are useful in a narrow set of domains whereas LLMs can be useful in many more generalizable scenarios.

   However, I'm not convinced that this method was actually demonstrated to be more generalizable than PDDL planning. See point 4.
2. From what I can tell, all the environments are discrete tabular environments and there does not appear to be a mention of non-deterministic environments. Also, the environments do not appear particularly difficult or long-horizon.
3. The standard deviation appears to be huge in the RQ2 results, and the statistics are calculated over only 5 runs. This makes it difficult to compare the methods. I would suggest averaging over more runs.
4. The deterministic method relies on a huge amount of prompt engineering including a task description, an observation description, and a query description. This can include a textual representation of the entire environment, and in the hierarchical setting it includes a full PDDL specification. In addition, in the verifier condition the full transition dynamics are needed. The goal of reward shaping is to get an agent maximize reward in a difficult MDP that it doesn't have full access to. If you require nearly full access to the MDP to create the shaped reward function, what is the point of shaping? Perhaps a comparison to policy iteration or value iteration, which are given the entire MDP to calculate the optimal policy.
5. The deterministic <-> hierarchical dichotomy is ill-posed and doesn't fit nicely into the existing literature. There is a deterministic <-> non-deterministic dichotomy, and there can be determinism and non-determinism in a hierarchical setting. This choice of words is confusing. Long-horizon might be a better descriptor than hierarchical, and primitive or base-level might be a better descriptor of deterministic.

### Questions
1. Why are plan lengths and rewards averaged across 3 runs as mentioned in Table 1? What non-deterministic elements are you testing and why are 3 runs enough to get a good sample?
2. How were the hyperparameters chosen for the learning agents? Did they differ across experimental settings? There is no appendix attached.
3. Example environment prompts for the deterministic and hierarchical setting would be useful to the reader. Can we see an example?

### Soundness
3

### Presentation
2

### Contribution
2
