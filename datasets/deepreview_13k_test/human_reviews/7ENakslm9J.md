# Bandit Learning in Matching Markets with Indifference

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
A rich line of recent works studies how participants in matching markets learn their unknown preferences through iterative interactions with each other. Two sides of participants in the market can be respectively formulated as players and arms in the bandit problem. To ensure market stability, the objective is to minimize the stable regret of each player. Though existing works provide significant theoretical upper bounds for players' stable regret, the results heavily rely on the assumption that each participant has a strict preference ranking. However, in real applications, multiple candidates (e.g., workers in the labor market and students in school admission) usually demonstrate comparable performance levels, making it challenging for participants (e.g. employers and schools) to differentiate and rank their preferences. To deal with the potential indifferent preferences, we propose an adaptive exploration algorithm based on arm-guided Gale-Shapley (AE-AGS). We show that its stable regret is of order $O(NK \log T / \Delta^2)$, where $N$ is the number of players, $K$ the number of arms, $T$ the total time horizon, and $\Delta$ the minimum non-zero preference gap. To the best of our knowledge, this is the first polynomial regret bound applicable to the more general indifference setting, and it is only $O(N)$ worse than the state-of-the-art result in the strict preference setting. Extensive experiments demonstrate the algorithm's effectiveness in handling such complex situations and its consistent superiority over baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper is a contribution that falls under the line of works where the goal is to match participants in a market when the preferences of these participants is not known apriori. While previous works, which the paper lists, have proposed algorithms to solve this problem for the setting where each participant in the market has a strict preference order, this work proposes an approach called AE-AGS that also accounts for the case of indifferent preferences. Indifferent preference is the case when a market participant (player or bandit arm) has an equal preference among one or more options from its complementing partner. 

The indifferent preference scenario is critical for real-world applications since often it is not practical or even reasonable for a market player to create a strict preference ranking order over its complementary market participant. For example, a company might be indifferent towards hiring one among a collection of equally qualified employees. 

The work proposes the AE-AGS algorithm for the centralized and de-centralized with communication settings. They analyze the algorithm and provide an upper bound on stable regret for both these settings. Finally experiments are conducted to compare the approach to baselines from the literature, and establish superior performance especially in the case of preference indifference.

### Strengths
The work addresses an important gap in the matching markets with unknown preferences literature where previously the approaches were not able to handle the preference indifference setting but this work can. The work proposes a UCB-style algorithm (AE-AGS) for both settings when centralized decision making is feasible and provides an separate algorithm and analysis for the decentralized setting as well.

The theoretical analysis of their algorithm backed by empirical validation of their approach makes for a strong contribution overall.

### Weaknesses
With my level of understanding of this area, I am unable to identify any big picture weaknesses. Instead, I have presented my concerns in the form of questions.

### Questions
1. There appears to be some inconsistency between the message of Table 1 classifying prior work, and section 2 on related work. While the table suggests that there have been prior works (Liu et al. 2020 and Basu et al. 2021) that address the preference indifference setting however there is a line towards the end of para 2 in Section 2 that reads: "In all the above works, both players and arms are assumed to have a strict preference ranking ... ".

Please clarify whether Liu et al. 2020 and Basu et al. 2021 can indeed handle preference indifference, and if so, how your approach differs from or improves upon these prior works. This would help resolve the apparent contradiction between Table 1 and the statement in Section 2.

2. Seems to me that the definition of Stable Regret in Eqn 1 needs to be motivated better. In particular, why is stable regret bench marked against the least reward that could be obtained from a stable matching and not the maximum stable matching reward? Please provide a justification for why you chose the least reward from a stable matching as the benchmark, rather than the maximum. Additionally, please discuss the implications of this choice on your results and how the results would compare with those under alternative definitions of stable regret.

3. Please increase the font size of the legend text in Figure 1 to improve readability for printed versions.

4. Please provide a clear definition of "Cumulative Market Instability" and explain how it relates to stable regret.

5. Please clarify why enumerating all stable matchings is problematic, even for small toy problems. Also consider including results using stable regret for these smaller examples if feasible.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors study the problem of bandit learning in matching markets when there are ties in the users' preference over arms.  They study the stable regret, i.e. regret with respect to the least reward achieved in any stable matching. They adopt arm side proposal which leverages the fact that the arm side knows about their respective preferences. This way the user don't suffer from the dilemma of whether to declare two arms tied or continuing the exploration. Instead, the user requires only segregate non-tied arm through pairwise computations. This ensures even if ties are present a stable match is discovered with logarithmic regret.

### Strengths
- The authors try to study the effect of ties in the well studied field of bandit learning in matching markets.  
- They design algorithms in both centralized and decentralized setting that achieves logarithmic stable regret. 
- They identify that the existing algorithms with User side proposals cease to work when there is ties on the User side (the side where information is absent). The issue is identifying ties against lack of appropriate exploration.

### Weaknesses
- The paper lacks discussions on the user optimal regret. The arm side proposal makes it hard to obtain user optimal regret even if ties are not present. 
- The motivation to move to arm side (the side that knows the preference) proposal is not clear. Is it a fundamental shift necessary for handling ties while maintaining logarithmic regret?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
The authors study market stability in a two-sided market with agents whose preferences are unknown. This work allows for indifferent preferences, which have not been considered previously. They propose AE-AGS algorithm, which achieves $NK\log(T)/\Delta^2$ for each agent. Additionally, they provide numerical experiments to demonstrate their superiority over baseline methods

### Strengths
1. Their algorithm can achieve tight regret bound under preference indifference. 
2. They also provide decentralized algorithm maintaining the tight regret bounds.

### Weaknesses
1. For the regret definition, they use the minimum reward value for the oracle, which may lack sufficient justification, under the absence of an optimal or pessimal stable matching.

2. In the experiments, another benchmark (C-ETC), which is much simpler, also appears to perform well in this setting.

3. The algorithm's presentation is difficult to follow. Especially, the main idea of dealing with preference indifference does not seem to be well described.

### Questions
1. Could you offer further justification for defining regret using the oracle's minimum value? Why minimum value is more proper than maximum reward?
2. Could you explain the key idea in your algorithm that enables it to handle preference indifference?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper studies the problem of bandit learning in matching markets with ties, while previous literature usually assumed that preferences were strict. The authors propose an Adaptive Exploration Arm-guided Gale-Shapley algorithm, both in a centralized setting and a decentralized setting. The authors provide the corresponding stable regrets and conduct simulated experiments to validate the results.

### Strengths
The paper studies an important unexplored question of learning matching markets with indifference and indifference is common in real life applications. The authors provided both a centralized and decentralized variant of the AE-AGS algorithm, and showed the stable regrets. The authors also provide a discussion on whether other algorithms can deal with ties (Appendix A).

### Weaknesses
The formulation of the problem setting is not convincing enough. For matching markets with ties, there are notions of weak stability, strong stability, and super stability [1], while the authors focus on weak stability without sufficient discussions. In the example 3.1, both (weakly) stable matchings (line 221, 222) are pareto efficient matchings in the sense that no other (weakly) stable matching can pareto dominate the matching for players. Therefore, it is not accurate to state that no player-optimal stable matching exists in this sense. Finally, the definition of regret compares the difference with $m_i$, which is defined as the worst partner among all weakly stable matchings. By the definition,  {i, m_i} is not a stable matching since the worst partner might be in different matchings. I feel it might be better to define the collective stable regrets instead of individual stable regrets.

I am also concerned with the algorithmic novelty in the paper. The AE-AGS algorithm looks like a simple (not necessarily trivial) generalization of ODA algorithm [2] and the AE arm-DA algorithm [3]. These algorithms utilize arm-guided Gale-Shapley to find stable matchings and utilize UCB structure to eliminate sub-optimal arms. From my understanding, the algorithmic difference in AE-AGS is that players do not need to eliminate an arm if there are ties while still proceeding with the arm-guided Gale-Shapley. Also, the analysis and proof also look similar to [2].

[1] Robert W Irving. Stable marriage and indifference. Discrete Applied Mathematics.
[2] Fang Kong and Shuai Li. Improved bandits in many-to-one matching markets with incentive compatibility. AAAI 
[3] Hadi Hosseini et. al. Putting Gale & Shapley to Work: Guaranteeing Stability Through Learning. arXiv:2410.04376

### Questions
I suggest the authors to formalize the problem in a more convincing way, e.g. the notion of stability, player-optimal stable matching, stable regrets (see the last part). 

Questions:
(1) Can the AE-AGS algorithm be generalized to many-to-one matching markets? I'm asking this question since the ODA algorithm is designed for many-to-one matching markets.

### Soundness
2

### Presentation
3

### Contribution
2
