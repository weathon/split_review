# DECENTRALIZED MULTI-AGENT REINFORCEMENT LEARNING VIA ANTICIPATION SHARING

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
In the realm of cooperative and decentralized multi-agent reinforcement learning (MARL), a fundamental challenge is reconciling individual incentives with collective outcomes. Previous studies often use algorithms where agents share rewards, values or policy models to align individual and collective goals. However, these methods pose issues like policy discoordination, privacy concerns, and considerable communication overheads. In this research, we obviate the need for sharing rewards, values, or model parameters. To bridge the gap between individual and collective goals, we set up a personal target based on a collective objective. This involves comparing what each agent anticipates other agents to do with what those agents intend to do. We introduce a novel decentralized MARL method based on the idea - Anticipation Sharing - where local agents update their anticipations regarding the action distributions of neighboring agents, reflecting their preferences, and share them with the corresponding agents. Based on the anticipations, each agent rectifies the deviation of its individual policy from the collective cooperation objective. Our approach has been validated as effective and viable through both theoretical analysis and testing in simulated environments. Our study shows the proposed MARL framework can induce cooperative behaviors among agents, even when they have private information about rewards, policies, and values. This represents a paradigm shift in orchestrating effective ways of cooperation by explicitly reconciling both individual and collective interests within multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript describe a method through which the optimization step of a multi-agent learning problem is constrained with a step discrepancy bound. The authors show the bound requires global policies, which indeed violates the decentralizability constraint of the advertised problem. The paper then propose a more local approach with estimating and sharing of "anticipated policies" as a more practical replacement.

### Strengths
The paper is written with generally mathematical definitions, and the proposed clipping method makes intuitive sense, despite requiring a certain leap of faith. Given the popularity of PPO, I have reasons to believe that the method should provide some performance gains.

### Weaknesses
The proposed method is still inherently a centralized approach since information regarding policies is, strictly speaking, being shared in the communication network of the networked MMDP. The centralization issue, however, can be ignored if the proposed method can be shown to avoid local nash such as seen in well-known dilemmas. Unfortunately, the authors do not mention optimality of the solutions, and intuitively, I do not think the method will solve the optimality problem. In addition, I think related works of this paper should also include some papers on opponent modeling. Some convergence results are already available in the case of policy prediction.

minor: in proof for theorem 1, after eq.20, you have \E_s^\prime where it should have been \E_{s^\prime}

### Questions
what happens in more challenging scenarios where there are actual dilemmas? have you considered partially observable settings? would the theory still sound in partially observable environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is about a solution for multi-agent reinforcement learning. The solution refers to it as "anticipation sharing". In my opinion, the anticipation the authors refer to is essentially an estimation of the values of the other agents. The authors provide a series of "theorems", which are presented as an extension of results in the original TRPO paper. The validation is based on a series of experiments value function parameter sharing, value sharing and policy parameters sharing.

### Strengths
+ The problem of decentralized RL has been widely explored, but, in actual truth, it can be considered still a rather open problem.

### Weaknesses
 - It is unfortunately quite difficult to understand the actual mathematical underpinnings of the paper. The first part presents a series of "theorems". However, their proofs do not appear convincing. The authors do not prove the inequalities reported in the Section 4.1 (more specifically, Theorem 1, Theorem 2 and Theorem 3). Then the authors introduce a surrogate optimization objective (in Section 4.3). However, the authors do not justify the introduction of this surrogate objective. It is very difficult for the reader to understand why it is a good idea such a function, which is quite complex computationally.
- The reviewer struggles to understand the introduction of the constraints in Section 4.3. This might be due to a presentation issue, but the derivations of the constraints from the optimization problem listed in Section 4.2 is not straightforward.
- The results reported in the evaluation are difficult to explain. Why do some of the methods perform so badly?
- For the Pred. task the performance appear very similar to value sharing.

### Questions
- What is the difference between value estimation of the other agents vs anticipation?
- What is the advantage in using the surrogate optimization objective in Section 4.3?
- Can you please motivate/derive the constraints in Section 4.4?
- Can you please explain the results in Figure 1?
- Can you please explain why we observe difference in terms of performance for the various tasks? Why does your method perform better for certain environments? If the difference is low, it seems that value sharing would be a preferable solution given its lower complexity. What is the trade-off a practitioner should consider in this situation?
- Can you please explain this sentence: "Theoretically, we established that the difference between agents’ actual action distributions and the anticipations from others bounds the difference between individual and collective objectives."? I am not sure that is the actual theoretical result that you showed in the first part of the paper. Alternatively, this might be considered as an expected fact, which does not need a proof?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In decentralized multi-agent reinforcement learning (MARL), aligning individual and collective goals is challenging. Traditional methods share rewards or models, risking discoordination and privacy breaches. This study introduces a new approach that bridges this gap without sharing parameters, emphasizing anticipation of other agents' actions. A novel MARL method with anticipation sharing is presented.

### Strengths
1. The article presents "Anticipation Sharing", a pioneering decentralized MARL method. This method enables agents to update anticipations about neighboring agents' action distributions, offering a fresh perspective in MARL.
2. Both theoretical analysis and simulated environment tests have been employed to validate the proposed approach, ensuring its robustness and applicability in diverse settings.
3. By addressing prevailing challenges like policy discoordination and privacy concerns, the research aptly underscores its relevance and timeliness to the current state of MARL.
4. Real-world implications, including the complexities of decentralized learning and agents' privacy preferences, are thoroughly discussed, highlighting the practical significance of the study.

### Weaknesses
1. The simulated environment tests presented seem overly simplistic. Without testing in more complex scenarios, the method's scalability and robustness remain unproven. Specifically, the paper lacks experiments in environments with a larger number of agents, more intricate state spaces, and more complex reward structures. The current tests do not adequately demonstrate the method's ability to handle the increased computational demands and coordination challenges that arise in more realistic multi-agent settings.
2. The paper's narrative occasionally lapses into redundancy, indicating a need for more concise and focused writing. Certain sections repeat similar ideas or arguments, which could be streamlined for better clarity and impact. This redundancy distracts from the core contributions of the paper and makes it harder to follow the key technical details.


### Questions
1. How does the proposed "Anticipation Sharing" method handle non-stationarity introduced by agents continuously updating their anticipations? Continuous updates can lead to a moving target problem in MARL.
2. While the paper addresses the challenges of policy discoordination and privacy concerns, how does the proposed method handle issues related to credit assignment, especially when agents have conflicting goals or when their contributions to the global reward are imbalanced?
3. The simulated environment tests mentioned in the paper appear to be somewhat simplistic. Were any tests conducted in environments with high agent heterogeneity or with more complex interaction dynamics? If not, how can the effectiveness of the method be ascertained in such scenarios?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the mixed motive problem setting, where each individual agent only has access their own individual rewards, but the system objective is to maximize social welfare (defined as the sum of individual agents' returns). The authors propose a decentralized learning method called Anticipation Sharing (AS) based on teammate modelling. The key idea is that each agent j will predict their teammates' actions (teammate modelling), and maximize a surrogate objective based on the teammate models, subject to a KL constraint. At each update step, each agent shares both their own actions and the predicted teammate actions with neighboring teammates. In the proposed method, rewards, values and model parameters are not shared. The empirical evaluation is performed on three mixed-motive tasks: exchange, cooperative navigation, and cooperative predation, and shows that (1) AS achieves higher returns than baseline methods, (2) AS is robust to number of neighbors / neighbor distance hyperparameters

### Strengths
- The paper is addressing an understudied and important problem, that of the mixed motive setting where agents must cooperate and compete with others to achieve their own objectives. Based on the strength of the empirical results, the contribution is good. 
- The mathematical notation is mostly well-defined, and the proofs are written rigorously. I did not discover any major mistakes or inconsistencies in the paper, and the authors have described their theory, algorithm, and experiments in enough detail for others to replicate. 
- The empirical results seem strong. The proposed method seems to converge more stably and to a higher return than related methods. The experiments figure is also nicely done (figure text size is appropriate, colors are well differentiated, and legend is fixed across figures for easy comparison).

### Weaknesses
The biggest weakness of this paper is that it fails to establish why AS has better assumptions/performs better than related methods. It also fails to provide intuition for the method.
- While the authors have provided many details on AS and have good results, fundamentally, the authors failed to communicate to me answers to the following important questions. What is the motivation for AS? Put another way, what are the existing methods and why would we expect AS to do better than them? Put a third way, what is the problem with the existing methods that AS solves?
- The abstract states, "In this research, we obviate the need for sharing rewards, values, or model parameters." Sharing action distributions is not a weaker assumption, since it involves sharing a similar amount of information. So why is it a better assumption?
- The intuition behind the proposed method and the motivation isn't totally clear to me. In Definition 2, the authors define the expectation over individual anticipated advantages.  If I understood correctly, this is the ith agent's advantage of the modelled joint action over the joint actions sampled from π^′, which I believe is the value of the true joint policy (but am not totally sure). As each agent has a different reward function, the advantages may not even be on the same scale. Thus,  it seems dubious to average over all agents' advantages.  Can the authors provide further intuition for what this quantity means, and why we might wish to bound the difference 
				
 The second biggest weakness of the paper is the experimental analysis.
- The current analysis is too speculative and makes vague statements. For example, the authors have the following statement in the experimental section: 
				
	"In comparison, the performance of VS and VPS is not stable across all the tasks. This may imply that the mere act of sharing value or value functions and achieving a consensus on values may not be sufficient to establish cooperative policies. This is because, even though value updates can approximate a system-wide value, **the policy updates of agents lack a coordination mechanism, thereby leading to inferior cooperation performance.** Our algorithm provides a policy coordination mechanism, which directly rectifies the deviation of individual policy update from the collective cooperation goal." 
				
 The bolded claim is a causal statement that is unsubstantiated by evidence. It is simply a speculation by the authors. The authors should either provide an experiment to support this claim, OR clearly mark it as a hypothesis. Overall, this section of the experimental analysis provides only weak insight into why AS is better than the baselines. 
				
- Missing experiment: It seems a bit impractical for each agent to have an accurate anticipated policy for all other agents. It would limit the scalability of the method. Can the authors add an experiment on, and discussion of how inaccuracies in teammate modelling affect the performance of the method? 
				
 The following issues are relatively minor, but I would still like to see them corrected. 
1.  Miscellaneous clarity issues:
- There should be a nice figure summarizing the method, somewhere in the paper. 
- The language of 'anticipated policies' isn't clear. It would be much clearer (and more reflective of what the paper is doing) if the paper replaced the terminology "anticipation" by "teammate modelling".
2. Algorithm 1, lines 13 and 14: this notation seems that the policies are shared, not the action distribution. Perhaps the authors can add a clarifying note to the caption. 
3. The paper makes overbearing claims. For example, in the abstract, the authors state their method represents a "paradigm shift". I feel that the results don't support such a strong claim. 
4. Missing related work: there is a large body of related work on teammate modelling, both in the CTDE setting and the ad-hoc teamwork setting. Please see Albrecht et al.'s survey (https://arxiv.org/abs/1709.08071), and add an appropriate subsection of related work.

### Questions
See the weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
