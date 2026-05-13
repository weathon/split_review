# Harmonized Learning with Concurrent Arbitration: A Brain-inspired Motion Planning Approach

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Motion planning, regarded as a sequential decision-making problem, poses a challenge for robots in high-dimensional continuous environments due to inefficient sampling. In contrast, humans inherently possess a distinctive advantage in decision-making by leveraging limited information, primarily relying on the concurrent reasoning mechanism in the prefrontal cortex. Motivated by this, we propose a brain-inspired Deep Reinforcement Learning scheme for planning, called Harmonized Learning with Concurrent Arbitration (HLCA). The approach effectively mimics human capacity for concurrent inference tracks and the ability to harmonize strategies. Specifically, in the planning process, a general Concurrent Arbitration Module (CAM) is meticulously crafted to balance the exploration-exploitation dilemma simply and efficiently. Besides, the harmonized style facilitates robots self-improving learning during the learning process, enabling the selection of appropriate strategies to guide planning. Experimental results show that HLCA outperforms the state-of-the-art benchmarks in terms of three representative metrics, which confirms the potential of emulating human-like capabilities to enhance the intelligence and efficiency of robotic planning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes Harmonized Learning with Concurrent Arbitration (HLCA), a brain-inspired Deep Reinforcement Learning (DRL) algorithm for motion planning. This is inspired by the human capability for inferring concurrently and harmonizing strategies.

### Strengths
The algorithm sees quite novel.

### Weaknesses
The authors do not provide sufficient details about the parameters of the algorithm to compare with, which impairs the credibility of the experimental results. In addition, the runtime for success rates must be reported as well.

In addition, the benchmarked tasks seem fairly easy; it would be more convincing if the authors carried out experiments on larger 2D maze maps or more obstacle-rich arm motion planning problems.

There are other learning-based algorithms to compare with. The reviewer would like to see the comparison results against those learning methods: Zhang, Ruipeng, et al. "Learning-based Motion Planning in Dynamic Environments Using GNNs and Temporal Encoding." Advances in Neural Information Processing Systems 35 (2022): 30003-30015.

Minor: Section 3.1 miss left parenthesis.

### Questions
1. In Figure 4(a), I am curious about why success rates all drop down to 0.4 for Ur5, which are supposed to be quite easy for sampling algorithms such as RRT*.

2. The benchmarked tasks are all short-horizon problems. These tasks can be quite easy for the algorithms to compare with. The reviewer would like to see to larger 2D maze map or more obstacle-rich arm motion planning problems.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author propose a motion planning algorithm, for high-dimensional continuous environments, based on two ideas inspired from models of decision making in the human brain, and the prefrontal cortex (PFC) in particular. The first idea is concurrent arbitration module (CAM), inspired by the concurrent inference track of the human PFC, allowing the algorithm to consider multiple candidates during the exploration phase using an observation function $\phi$, before deciding to switch to the exploitation phase. The second idea is to define a self-improving learning algorithm that takes into account the feedback received from the environment to improve the decision-making process by incorporating estimates of both the ex-ante and ex-post reliabilities. The learning algorithm combines a learning based planner $\omega_u$ with a number of non-learning planners $w_i$. The total number of planners in the inference buffer is limited, again, inspired by the observed number of concurrent plans in human studies. The authors evaluate the algorithm in comparison to 7 baselines over 7 different environments of varying complexity and number of DoFs.

### Strengths
- Extensive comparison against multiple baselines across different environments of varying complexity.
- Significantly improves over state-of-the-art across a number of key performance measures, i.e., success rate, number of collision-checks, and average path cost.

### Weaknesses
- To me the derivation of the main algorithm was cluttered by discussion of (models of) brain function that I wasn't able to appreciate, more so as it was difficult for me to connect it to the description of the algorithm (which itself seemed to be presented rather loosely, relying on the figures and a sequence of paragraphs tending to different aspects, issues, and proposed solutions.) It would have helped to present the main logical steps in a pseudocode listing, with pointers to equations or section numbers that deal with finer issues.
- I have a concern about basing the evaluation on the quality of the output, without examining the performance of the algorithm itself; see below.
- I also have concerns about the chosen benchmark leading the proposed algorithm to achieve 100% success rate. It is necessary to include a more challenging benchmark that specifically exposes failure cases, and compare to other baselines in that case too.

### Questions
**Technical comments:**
- Experiments:
    - It is necessary to include the computation/running-time of the motion planning algorithm itself, rather than just the number of collision-checks (also storage requirements for the memory buffers). Namely, as the proposed algorithm runs multiple candidate strategies in parallel, it is likely that its performance scales linearly with the number of active candidates. If pre-computation/caching, e.g., reusing past results is incorporated to overcome some of this overhead, then this deserves more discussion.
    - Related to the above point, the maximum number of samples $N_T$ ends up playing an important role in addressing the exploration-exploitation trade-off. I find that surprising as the proposed algorithm specifically aimed to offer new insights into this trade-off. Isn't it possible for the algorithm to produce running statistics indicating how much improvement can be expected if more samples are to be collected? Indeed, the ablation study with varying number of samples showed that performance reaches a plateau. Can the algorithm detect this? (e.g., in the course of arbitration as in S4.2.)
- The choice of the thresholds $\beta$ and $\rho$ seems to be absent.
- General:
    - The authors seem to use the word "optimal" in context where either it is not accurate (perhaps local optimal?, e.g., S4.3.2 optimal strategy $\omega^\ast$), properly-qualified (e.g., S2 second line), or lacking evidence (S5.2 last line). It is necessary to revise each instance and make sure it's used correctly.

**Concerns related to Neuroscience:**
- The main concern is whether the brain models mentioned are the kind of science that can undergo significant revisions in the future, and whether the inclusion of such statements is essential to an article on RL algorithms in an AI/ML venue.
- Section 2:
    - While it is beyond me to vet the contents of this section, I'm unable to take the assertions made about brain function at face value. First, I'd strongly recommend to preface this entire section by a clear statement of which articles this is drawn from. Then, it would help to qualify each assertion by specific references and statements of the form "current experimental evidence from neuroscience using brain scans/activation patterns suggests that", or "in experiments conducted on humans/animals on tasks involving", etc.
- Section 3:
    - "... designed by imitating the inference buffer of the human brain" - It would help to refer to this instead as "the XYZ model for inference in the human brain", rather than the "human brain" itself, still with a reference for XYZ. (Section 4.1 seems more inline with what I'm asking for here. Please follow this style consistently throughout.)
- Section 4:
    - "Motivated by the concurrent inference track in human PFC," same as the previous point.

**Presentation:**
- Section 3:
    - S3.2: This short section doesn't seem to offer much at this point. In particular, there's nothing about it that explains the proposed harmonized self-improving learning. (I wonder if this remainder of this section was deleted by mistake?)
- Section 4:
    - S4.3.2: I recommend replacing the number 200 with a hyperparameter, and explaining why this particular value was suitable for the experiments presented.
- Section 5:
    - Fig. 11 & 12: it would help to include the metrics mentioned in the caption within the figure itself.
    - S5.4
        - Fig.6(c): it seems NEXT+CAM actually increases the average path cost. The associated paragraph states that "CAM optimizes the path cost in high-dimensional environments."
- Appendix-A & B:
    - The paragraph at the top appears redundant as it does not include meaningful conclusions from the results. It would be better to include a sentence or two about each table, beyond what's in the table captions. Perhaps that was all deferred to Appendix-B. If that's the case, it would help to communicate this structure, though I'd recommend to keep each paragraph next to the relevant table. (Prefer to have the conclusions closer to the supporting evidence.)
    - Table 1: only few cells have non-zero stdev. A comment about that would be helpful, and I wonder if this indicates that experiment configurations need to be revised to include more challenging cases over all environments. Specifically, it would help to supplement this table with a new set of experiments (and table) designed to show HLCA failure cases, e.g., average success rate near 80%, and show how far other baselines regress for the same test cases.
    - Table 3: the gap in HLCA is highest for UR5. I wonder if this indicates different priors/hyperparameters are needed for this environment. It would help to include a comment about how this gap may be reduced by specialization of the proposed approach.
- Appendix-C:
    - Please indicate that this entire section is focused on the HCIL method, and revise figure captions to mention this as was done for Fig.9. Looking into this again, it's not immediately clear how the first paragraph+Fig.8 differs from the second paragraph+Fig.9.

**Nitpicking:**
- Abstract:
    - "meticulously crafted" appears too strong at this point, that only detracts from the main content. Recommend to replace it with simply "designed"
- Section 3:
    - S3.1: unmatched parenthesis in the definition of $U_i$.
    - S3.2: all possible histories *before* t-episodes
    - S4.2: Candidate states are sample(d) guided by
- Section 4:
    - S4.3.1: $Z_t^\mu$ and $Z_t^\lambda$ are "regularization factors" -> normalization?
    - S4.3.1: be direct as a constant -> be directly used as?
    - S4.3.2: many occurrences of "cycle" are better replaced with "iteration" or "epoch"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work the authors draw inspiration from the human biological brain to design an algorithm capable of adaptively switching from exploitation to exploration, amongst multiple strategies for path planning. Drawing inspiration from the function of the human Prefrontal Cortex (PFC), the authors have developed a model that can select amongst multiple stored planning strategies, augmenting their performance by utilizing space exploration when the observed reliability of the known strategies is compromised.  At the core of the authors work lies the Concurrent Arbitration Module(CAM), which is responsible for assessing the performance of the currently followed strategy and deciding whether to keep following it, switch to another one or explore new possibilities by sampling from the environment. 
At each planning iteration, the agent rolls out new trajectories starting from a starting state, attempting to reach a goal state. The agent selects, at each step, the action that leads to the state with the maximal predicted reward and also features a reliability exceedinga hyperparameter beta. If the current strategy omega_k cannot produce new states that have an estimated reliability above beta, then the strategies in the Inference buffer I are considered. If these strategies cannot also produce reliable states, then the agent switches to a new strategy stored in the long term memory buffer U and uses it to explore new state possibilities. If the new probing strategy omega_p can be considered reliable, then it is chosen otherwise the agent simply adopts the strategy with the highest reliability and continues roll outs. The agent adds rolled out paths to a training buffer D, and every 200 paths it updates its value and policy estimators, which are given by a network with shared parameters. The agent utilizes several metrics to produce the reliability measures of each strategy, such as probability of collision from each state, cost  and estimated reward. It uses a bootstrapping method where confirmed values ( after trajectory executions) are used to update the reliability estimator.

### Strengths
The main contribution of this work, the ability to switch between strategies and alternate between exploration and exploitation when the agent is uncertain about next steps, is predicated on a traditional learning objective, that updates the value and policy network parameters after observing past path choices. 

The method is founded upon a solid idea of attempting to gauge the reliability of multiple strategies each time the agent finds itself in uncertain situations. The agent can utilize the diverse set of outcomes from the multiple of strategies to escape local optima that can lead to unimprovable performance.

The authors use traditional metrics such as path cost, estimated reward and collision probability to attempt to gauge a path's feasibility in a convincingly feasible manner. 
They use post state expansion feedback to improve reliability for each strategy.

The method seems to be able to have offline training capacity by updating past example's reliability score through equation 3.

### Weaknesses
The author’s method requires a few critical hyperparameters which might be difficult to predefine in complex problems. The reliability threshold, being the most critical, appears to be extremely sensitive to not only the environment but also subtasks with an environment. Additionally, the perceived volatility parameter ti, is rather arcane in how it is selected. 

The following assumption is given without adequate proof or reasoning. 
 “Since π(s ′ |s; θ) is trained based on prior local optimal successes on various challenges, it can lead the policy to gradually approach the optimal policy.”
Why does the superimposition of locally optimal solutions approach an overall optimal policy? 
While it might make intuitive sense, and can have practical soundness in several cases.

Paper has several typos and requires additional proofreading to correct them i.e
Section 4 line 2 “which can optimize the collection of training buffer and V (s; θ) and π(s ′ |s; θ) can be self-improving learned” or Section 4.3.1 last line of last paragraph “Thus, F(ω | Ut, I) does not require calculation and can be direct as a constant”, to name a few.

No mention of the resources and time complexity the method requires versus the competition.

An algorithmic presentation of the algorithm is mandatory. The writing style made it rather hard to understand what is learned, when the strategies are rotated etc. 

The authors mention that 2 ⁄ 3 strategies are handcrafted. How are they thus and how do they operate? Since the authors do have a learnable strategy trainable by backpropagation on their loss signal, why wouldn't they accommodate more classes or learnable policy / value networks and switch between them? This raises the question of the amount of engineering done in the hand-crafted strategies and how much they can generate states that can dislodge the learned strategy from local optima. While the multistrategy idea is quite interesting, its efficacy would be much more strongly showcased if there were multiple learned strategies or if hand crafted were indeed required, if they were simple heuristics.

It is confusing when the reliability checks happen for all strategies in I. Does a complete reliability assessment of all strategies happen when the current strategy k becomes unreliable or at each state expansion?

When a current strategy  omega_k (learned) becomes inactive, and a new probing strategy is selected, how does this work? Is the new strategy omega_p initialized from omega_k and then further trained? Or are there several trainable strategies during initialization and at each time a learnable strategy omega_k becomes unreliable, a new omega_p supplants it and is trained differently? The latter would be mean that during the initial cycles more than one untrained strategy are selected and trained. Is that correct?

### Questions
It is confusing when the reliability checks happen for all strategies in I. Does a complete reliability assessment of all strategies happen when the current strategy k becomes unreliable or at each state expansion?

When a current strategy  omega_k (learned) becomes inactive, and a new probing strategy is selected, how does this work? Is the new strategy omega_p initialized from omega_k and then further trained? Or are there several trainable strategies during initialization and at each time a learnable strategy omega_k becomes unreliable, a new omega_p supplants it and is trained differently? The latter would be mean that during the initial cycles more than one untrained strategy are selected and trained. Is that correct?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
