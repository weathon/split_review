# Detecting Influence Structures in Multi-Agent Reinforcement Learning

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
We consider the problem of quantifying the amount of influence one agent can exert on another in the setting of multi-agent reinforcement learning (MARL). 
As a step towards a unified approach to express agents' interdependencies, we introduce the total and state influence measurement functions.
Both of these are valid for all common MARL systems, such as the discounted reward setting.
Additionally, we propose novel quantities, called the total impact measurement (TIM) and state impact measurement (SIM), that characterize one agent's influence on another by the maximum impact it can have on the other agents' expected returns and represent instances of impact measurement functions in the average reward setting. 
Furthermore, we provide approximation algorithms for TIM and SIM with simultaneously learning approximations of agents' expected returns, error bounds, stability analyses under changes of the policies, and convergence guarantees. 
The approximation algorithm relies only on observing other agents' actions and is, other than that, fully decentralized.
Through empirical studies, we validate our approach's effectiveness in identifying intricate influence structures in complex interactions.
Our work appears to be the first study of determining influence structures in the multi-agent average reward setting with convergence guarantees.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper mainly discusses the problem of measuring the influence levels between agents interacting in an environment in the average reward setting. Authors introduce two performance metrics: the total impact measurement and state impact measurement. The paper proposes measuring the effect of other agents by dividing the set of agents into subsystems, and measuring the effect of agents in this subsystem.

### Strengths
The paper is written clearly and the two measures are well-defined. The empirical results also support the theoretical results presented in section 5.

### Weaknesses
It seems like definition 4.1 is related to the potential function in a Markov potential game, and I would ask the authors if they can discuss any connections between the matrix entries for one state-action and a particular potential function. The formulation of the problem itself as a multi-agent MDP is indeed a Markov game. Specifically, the paper should clarify the relationship between their proposed impact measures and the concept of a potential function, particularly in the context of Markov potential games. The current discussion lacks a detailed analysis of how the proposed influence measures relate to the existence (or non-existence) of a potential function, and how this impacts the interpretation of the results. For example, if a potential function exists, how do the proposed measures reflect the potential's properties, such as its gradients and local optima? If a potential function does not exist, what does this imply for the interpretation of the influence measures? Furthermore, the paper does not discuss how the proposed measures might be used to identify or analyze the existence of a potential function, which could be a potential avenue for future work.

### Questions
How does the impact scale differ from a potential function defined as the deviation in policies between agent i and the other agents -i in the subset of agents?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of quantifying the amount of influence an agent can have over other agents in multiagent reinforcement learning settings. Its main goal is to reliably detect the inherent influence structure of an environment given a specific policy. It’s main contributions include 1) a unified way to represent a multiagent system’s inherent influence structure, irrespective of the reward setting and overall objective; 2) introducing the total impact measurement and state impact measurement to quantify the overall and state-dependent influence structure respectively in multiagent average reward settings; 3) a decentralized algorithm with stability analysis and convergence guarantees together with empirical evaluation.

### Strengths
1.	Investigated an important problem --- quantifying agents’ influence among each other --- for MARL.
2.	Both empirical evaluation and theoretical analysis are provided to justify the effectiveness of the proposed metrics

### Weaknesses
1. The novelty of this work was not fully justified.
There are many work study the structure influence of the individual agents for multiagent system. E.g,

Frans A. Oliehoek, Stefan Witwicki, Leslie P. Kaelbling, A Sufficient Statistic for Influence in Structured Multiagent Environments, JAIR2021

Thomas Spooner, Nelson Vadori, Sumitra Ganesh, Factored Policy Gradients: Leveraging Structure for Efficient Learning in MOMDPs, NeurIPS2021

If would be more convincing if more literature can be reviewed and related methods can be compared. 

2. Some technical details (e.g, stochastic iteration approximation) are introduced, but not clearly explained.

3. The usefulness of the methods if not fully justified.
The paper is mainly investigating the proposed influence quantification metric. It is understandable that this is the first step towards deploying them for more applications related to MARL. It might be better if some comparison to some MARL methods (especially those have considered the influence structure like the one mentioned above) can be provided in some simple domains.

### Questions
1.	Section 3.2 provides some basic assumptions and theories related to stochastic approximations. It would be better if some intuitive explanations can be provided to help reader better understand background of the proposed metrics
2.	In section 6.1, “using the format of Zhang et al,…” what exactly it the format? It might be better to provide more details of the environment.
3.	Some notations are a little confusing, e.g, a^{-i}  and {a^{bar}}^{i}, they seem to refer to different things, but looks quite similar at first glance.
4.	Why emphasize averaged reward settings given that the proposed influence measurement can be applied to discounted reward settings as well?
5.	In section 6.2, “deviating from the original game, we employ one-sided penalty system…” Why need to deviate from the original game?
6.	What is L_add?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper aims to quantify the inter-agent influences in MARL principally by proposing quantitative measurements on stop state values.

### Strengths
The paper is written with good clarity, with clear assumptions and definitions.

### Weaknesses
 - As a reader, I'm still not convinced how useful is the proposed measurement. More theoretical or empirical evidence is needed in order to demonstrate their utilities.
- Some of the preliminaries needs to be added, such as the definition of Q values with differing actions.

### Questions
I view the proposed measurement as an alternative way of representing the reward, which changes the problem structure of MMDP. In order to argue for correctness, one would have to prove that the solution to the new problem is exactly the solution to the original problem. How would you relate the two problems?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the exploration of influence structures within Multi-Agent Reinforcement Learning (MARL) systems. The authors introduce influence measurement functions, serving as a comprehensive descriptive framework for understanding influence structures across various common settings. Within this framework, they introduce both total and state influence measures, specifically tailored to the context of average reward settings. The paper goes on to offer a rigorous theoretical analysis, focusing on the stability of these measures, as well as providing insights into the convergence properties and error bounds of the corresponding approximation algorithms. In addition to theoretical contributions, the authors conduct experiments in randomly generated environments to showcase the convergence of approximation errors, even in scenarios involving evolving policies. Moreover, the "coin game" experiment is presented as an example, demonstrating the practical applicability of these concepts in complex and dynamic settings. This experiment sheds light on the understanding of influence within black-box environments. Overall, this work sheds valuable light on the intricate world of influence structures in MARL systems, offering both theoretical insights and practical applicability in diverse and dynamic scenarios.

### Strengths
1. The problem this paper considers is rather important.
2. The literature review is sufficient.
3. The proposed framework seems to be novel.
4. The theoretical results are sound.

### Weaknesses
1. The evaluation of the proposed method is not enough. Figure 1 and Figure 2 only show the TIM error and mean TIM approximations in two environments respectively. What about the overall performance improvement of the proposed method?
2. This paper did not show any empirical comparison between the proposed method and baselines.
3. This paper did not provide any limitation discussions of the proposed method.

### Questions
1. How do TIM and SIM combine with MARL methods?
2. What is the main difference between TIM and SIM?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
