# Multi-Agent Path Finding via Decision Transformer and LLM Collaboration

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Multi-Agent Path Finding (MAPF) is a significant problem with pivotal applications in robotics and logistics. The problem involves determining collision-free paths for multiple agents with specific goals in a 2D grid-world environment. Unfortunately, finding optimal solutions for MAPF is an NP-hard problem. Traditional centralized planning approaches are intractable for large numbers of agents and inflexible when adapting to
dynamic changes in the environment. On the other hand, existing decentralized methods utilizing learning-based strategies suffer from two main drawbacks: (1) training takes times ranging from days to weeks, and (2) they often tend to exhibit self-centered agent behaviors leading to increased collisions. We introduce a novel approach leveraging the Decision Transformer (DT) architecture that enables agents to learn individual policies efficiently. We  capitalize on the transformer's capability for long-horizon planning and the advantages of offline reinforcement learning to drastically reduce training times to a few hours. We further show that integrating an LLM (GPT-4o), enhances the performance of DT policies in  mitigating undesirable behaviors such as prolonged idling at specific positions and undesired deviations from goal positions. We focus our empirical evaluation on both scenarios with static environments and in dynamically changing environments where agents' goals are altered during inference. Results demonstrate that incorporating an LLM for dynamic scenario adaptation in MAPF significantly enhances the agents' performance and paves the way for more adaptable multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the Multi-Agent Path Finding (MAPF) problem, where multiple agents need to reach designated goals in a shared 2D grid environment while avoiding collisions. To improve efficiency and adaptability, the authors propose a hybrid approach using a Decision Transformer (DT) for offline learning and a large language model (GPT-4o) for real-time guidance. The DT trains individual agents on expert trajectories, achieving reduced training time and long-horizon planning. The addition of GPT-4o helps mitigate undesirable behaviors, like redundant moves or prolonged idling, by guiding agents in static and dynamically changing environments. Experimental results demonstrate that this DT + LLM approach performs well across various MAPF scenarios, achieving lower collision rates and shorter paths compared to benchmarks.

### Strengths
1. This paper builds on the recent trend of research exploring the planning abilities of transformer architectures, in this case DT+GPT-4o. 
- DT trained offline using expert trajectory data is used separately for each agent in a decentralized manner for evaluation. 
- By combining DT and LLMs, the authors create a flexible system that can handle both static and dynamic environments, adapting quickly to changes like shifted goals. 
- Although the experiments are limited to simulation results, the proposed framework could be developed to address common MAPF challenges in realistic scenarios, such as partial observability and dynamic goal adjustments, which are beneficial for applications in logistics or swarm robotics.

2. The paper is overall clearly written. The authors have also discussed some limitations of this line of research using LLMs in planning.

### Weaknesses
1. The use of prompt engineering for LLM guidance may limit generalization, especially if prompt templates don’t fully capture variations across different environments. Moreover, relying on GPT-4o for real-time guidance could present latency issues as the number of agents increases in complex environments.

2. Results reported in this paper do not include standard error values across trials.
- Tables 3 and 4 do not clearly show DT+GPT-4o outperforming other baselines.
- Fig 4 shows that the competitive baseline DCC outperforms the proposed framework especially with larger team sizes. It is hard to argue in favor of the usefulness of the DT+GPT-4o framework if it only outperforms prior work when evaluated in smaller settings with fewer agents.

### Questions
1. Since the results show that GPT-4o provides valuable guidance to DT especially in dynamic environments, what would be the effect of only using GPT-4o for such tasks without any DT policy for each agent?


2. Line 376: "number of collisions ... in a successful episode ..." : is an episode still successful if there are inter-agent collisions?

3. Have the authors run any experiments where the DT offline training data also includes a large number of sub-optimal trajectories along with fewer expert trajectories? How would the performance differ compared to the current results when deploying DT+GPT-4o in such settings?

4. Have the authors thought about any automated prompt generation techniques to make the proposed framework more efficient?

### Soundness
2

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
5

### Summary
The paper is devoted to the use of offline-RL methods and language models to solve the multi-agent pathfinding problem. The authors use the well-known Decision Transformer architecture, which is trained on a pre-collected dataset from the ODrM* heuristic planner. At some point in time, the agents' policy switches from a DT-based policy, to actions within 5 steps, which is generated by GPT-4 in a centralized manner. The authors proposed a special chain-of-thoughts style prompt to resolve conflicts that arise most often when agents switch goals. The authors conducted experiments with a stationary setting and compared them with PRIMAL and DCC methods, showing some advantages mainly in reducing collisions. For changing goals, a quality improvement is shown by using GPT-4.

### Strengths
The authors consider an important formulation of the MAPF problem with changing goals and are among the first to use a combination of DT and LLM to generate agent actions. The paper as a whole is written in easy-to-understand language, and the idea of the method and the experiments are very clear.

### Weaknesses
The main disadvantage of the paper is the author's lack of familiarity with the latest benchmarks in the field of learning MAPF and weak positioning of the paper from the point of view of the MAPF community. At the same time, it should be noted that from the point of view of using neural network models and representation models, the novelty of the work is not traceable, so it can only be evaluated in terms of its contribution to the general pool of modern works on learning MAPF. Several specific remarks:
1. Since the prompt for LLM describes entirely the map and information about other agents (as can be understood from the text), the proposed approach is no longer fully decentralized and partially observable. This is analogous to calling a centralized scheduler like ODrM* at some point in time and taking action from it five steps ahead. This aspect, which violates the original Dec-POMDP problem statement, should at least be discussed in detail, and comparing DT+LLM with DT+ODrM* or DT+DCC would improve the work.
2 The authors, by introducing agent communication via LLM, should ideally consider and compare with other work using explicit agent communication with language models, including for the MAPF task.
3. The authors point out that centralized planners are not scalable to a large number of agents. However, first, the authors themselves consider only 64 agents, which is also small, and second, there are modern centralized planners such as LaCaM [1] that scale up to 1K agents.
4. The authors use a 5-year-old PRIMAL method as their main baseline. At a minimum, the authors need to include in the comparison the SCRIMP and CACTUS they mentioned, which are seriously better than PRIMAL in classical MAPF tasks.
5. The authors use a rather simple formulation of the problem with nonstationary conditions, although there are several papers [2], in which the problem of nonstationarity in MAPF has already been considered. Also, the formulation used by the authors is similar to the life-long MAPF problem, which has its own set of methods, such as PRIMAL2 [5].
6. The authors use custom maps and low obstacle density. Although there is a large set of maps and benchmarks (MovingAI [3], POGEMA[4]) that make sense to use as the main dataset for experiments. So that comparisons can be more correct and complete.
7. Emphasizing a significant reduction in training time cannot be considered correct. First, the number of parameters in each of the models (PRIMAL, DCC, DT) should be taken into account. It is possible that somewhere the work with large maps (like 128 by 128) was assumed and neural network models are more redundant than those used by the authors. Secondly, training on demonstrations is a significant simplification of the optimization problem and it is quite natural that the convergence of the process here will be orders of magnitude faster. The use of expert data, which also needs to be collected, is a significant competitive advantage.

### Questions
1. How did the authors account for the variable number of agents to tokenize actions and observations when training DT?
2. Would the results be significantly worse if only the observations seen by each agent were passed to the LLM and decentralization was not violated?

### Soundness
2

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
5

### Summary
The paper addresses the Multi-Agent Path Finding problem using a Decision Transformer architecture combined with a Large Language Model to improve decentralized learning efficiency and agent coordination. The proposed approach aims to reduce training times significantly and improve adaptability in both static and dynamic environments.

### Strengths
The paper includes well-designed visual aids, which effectively illustrate the experimental setups and outcomes.

### Weaknesses
The primary contribution is the combination of DT with LLMs, both well-established methods, but the motivation behind integrating these two specific algorithms is not clearly justified. The combination feels somewhat arbitrary, as each component could theoretically be combined with other methods without unique synergy. 

Incorporating LLMs potentially introduces global information into the system, which conflicts with the decentralized nature of the approach. This inclusion may undermine the paper's objective of maintaining a decentralized framework. Specifically, the use of an LLM, even for a limited number of steps, introduces a centralized planning element that could allow agents to implicitly coordinate their actions through the LLM's global view, thus deviating from a purely decentralized approach. The paper does not adequately address how this centralized element impacts the overall decentralized learning paradigm.

While the study asserts that offline reinforcement learning can reduce training times, the experimental setup is too simplistic, relying only on simulated environments. Evaluations in real-world settings would provide a stronger validation of the method's claims and its practical applicability in realistic, complex scenarios. The simulated environments used appear to be relatively small and do not fully capture the complexities of real-world MAPF problems, such as sensor noise, communication delays, and unpredictable agent behaviors. This limits the generalizability of the findings.

The paper lacks clarity on the mechanism for assigning credit to each agent. The approach claims to be decentralized, however the training relies on a joint reward (e.g., collision penalty). It remains unclear how this joint reward is allocated to each agent individually. While a collision penalty is a common approach, the paper does not detail how the individual agents learn from this shared signal in a decentralized manner. This is a critical point that needs further clarification.

### Questions
I have no further questions.

### Soundness
2

### Presentation
3

### Contribution
2
