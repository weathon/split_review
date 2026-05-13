# Single-agent Poisoning Attacks Suffice to Ruin Multi-Agent Learning

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
We investigate the robustness of multi-agent learning in strongly monotone games with bandit feedback. While previous research has developed learning algorithms that achieve last-iterate convergence to the unique Nash equilibrium (NE) at a polynomial rate, we demonstrate that all such algorithms are vulnerable to adversaries capable of poisoning even a single agent's utility observations. Specifically, we propose an attacking strategy such that for any given time horizon $T$, the adversary can mislead any multi-agent learning algorithm to converge to a point other than the unique NE with a corruption budget that grows sublinearly in $T$. To further understand the inherent robustness of these algorithms, we characterize the fundamental trade-off between convergence speed and the maximum tolerable total utility corruptions for two example algorithms, including the state-of-the-art one. Our theoretical and empirical results reveal an intrinsic efficiency-robustness trade-off: the faster an algorithm converges, the more vulnerable it becomes to utility poisoning attacks. To the best of our knowledge, this is the first work to identify and characterize such a trade-off in the context of multi-agent learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the robustness of multi-agent learning (MAL) algorithms in strongly monotone games with bandit feedback. The authors propose the Single-agent Utility Shifting Attack (SUSA) method to shift the Nash Equilibrium of monotone games by corrupting a single agent's utility feedback, using a sublinear corruption budget relative to the time horizon. Their analysis uncovers a trade-off between efficiency and robustness, showing that faster-converging MAL algorithms are more vulnerable to such attacks. They also validate their theoretical findings via numerical experiments.

### Strengths
1) The paper highlights a significant and underexplored vulnerability in multi-agent learning (MAL), specifically through single-agent utility poisoning attacks. It may stimulate further research into designing MAL algorithms that are robust to adversarial attacks.

2) The authors provide a rigorous theoretical analysis of the Single-agent Utility Shifting Attack (SUSA), clearly outlining the conditions under which SUSA can effectively alter the Nash Equilibrium (NE). The exploration of the efficiency-robustness trade-off is valuable, highlighting the increased vulnerability of faster-converging algorithms.

3) The authors conduct extensive empirical simulations, showcasing the practical impact and effectiveness of their proposed method

### Weaknesses
1) The current attack objective is focused on shifting the Nash Equilibrium (NE) with specific distance guarantees. While the paper briefly discusses steering the NE deviation in a desired direction (lines 295-300), it remains unclear if it is feasible to mislead agents toward specific, predefined strategies. The analysis does not explore the practical implications of guiding agents to particular strategy profiles, especially if those profiles are suboptimal or exploitable. This limitation reduces the practical relevance of the attack, as real-world adversaries might aim for more specific and damaging outcomes than simply shifting the NE.
2) The study is primarily focused on monotone games, illustrated through Cournot competition and Tullock contests. It would be valuable to examine whether these insights hold in other game-theoretic contexts. For instance, in non-monotone games with multiple NEs, it would be interesting to explore alternative attack objectives, such as guiding agents toward an NE with low utility outcomes. The current analysis does not consider the complexities of non-monotone games, which might exhibit different vulnerabilities and require different attack strategies. The restriction to monotone games limits the generalizability of the findings.
3) The paper evaluates the effectiveness of attacks based on NE shift and cumulative budget. Expanding the evaluation to include additional robustness metrics, such as stability and utility outcomes, would provide a more comprehensive understanding of the impact of attacks on MAL. The current metrics do not fully capture the potential damage an attacker could inflict, such as destabilizing the learning process or significantly reducing the overall utility of the agents. A more holistic evaluation is needed to assess the true vulnerability of MAL algorithms.

### Questions
1) Given that the attack model assumes full knowledge of the victim agent’s utility function, do the authors believe that SUSA could still be effective in a limited-information setting? Are there alternative attack strategies that might be feasible with only partial information?

2) The attack model relies on "strong" corruption, where the attacker observes the current round action. It would be valuable to investigate whether the results extend to scenarios where the attacker lacks this observational ability, as well as whether it becomes easier to design robust algorithms against such "weaker" attackers.

3) To what extent might the findings on NE shifting and efficiency-robustness trade-offs apply to non-monotone games or games with multiple NEs? Could the authors envision scenarios where the attack objective is to guide agents toward a low-utility NE?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper designs the attack policy for multi-agent learning in monotone games. It shows that attacking a single agent is enough to diverge the convergence away from NE. The paper also studies the robustness of the MAL algorithm, presenting several interesting open problems and numerical simulations.

### Strengths
1. This paper's writing is clear and easy to follow. The figures (especially Figure 1) and remarks help readers understand the paper. 
2. The contributions of the attack policy to a single agent and proving a sublinear attack is theoretically enough (Theorem 1) are novel in the literature. 
3. The discussion of the robustness and efficiency trade-off is very insightful and opens the door for more interesting future works.

### Weaknesses
1. As the authors mentioned that the trade-off had been studied in a single agent, it would be helpful to discuss whether or not the three raised open problems are also present in the single-agent setting. If so, can we extend the single-agent results? If not, why?



### Questions
Minor comments:

1. Line 147, “will useful” → “will be useful”.
2. Line 242 is a “strong” attack, [Lykouris et al., 2018] is a “medium” attack before observing the action. For strong attack, the related literature has: 
    1. Jun, Kwang-Sung, et al. "Adversarial attacks on stochastic bandits." *Advances in neural information processing systems* 31 (2018).
    2. Liu, Fang, and Ness Shroff. "Data poisoning attacks on stochastic bandits." *International Conference on Machine Learning*. PMLR, 2019

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the vulnerability of multi-agent learning (MAL) systems in strongly monotone games with bandit feedback. Specifically, the authors propose an attack strategy called Single-agent Utility Shifting Attack (SUSA), which can steer the learning dynamics away from the Nash equilibrium with a sublinear (w.r.t. T) budget. The authors also provide theoretical and empirical results to validate their points.

### Strengths
1. The paper introduces a novel type of poisoning attack that focuses on a single agent in multi-agent systems, a context underexplored in prior work. The proposed poisoning strategy can mislead any MAL dynamics in strongly monotone games away from the original NE, with a sublinear corruption budget.  

2. The authors show a trade-off between convergence speed and the robustness to attacks.

3. The authors provide a thorough theoretical analysis to validate theoretical results.

### Weaknesses
In the attack model, the authors assume full knowledge of the victim agent’s utility function, which may not always be practical in real-world applications. Moreover, since the agent is unaware of their utilities and the adversary has such knowledge which further allows to compute more information such as gradient, misleading the system not to converge the original NE looks not surprising due to the information asymmetry. It could be more interesting to restrict the adversary. For example, the adversary only observes the noisy rewards.

### Questions
Can the authors discuss the attack strategy if the adversary only observes noisy rewards, e.g.,  sub-gaussian rewards?

Is there any lower bound on the budget that misleads the convergence?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers the poisoning attacks in multi-agent learning, targeting a single agent. The authors first propose the attack strategy which steers the game from the NE with sublinear attack cost. They then explore the robustness of learning algorithms, analyzing how the convergence rate can affect the algorithms' robustness. Finally, the experiments verify the theories by showing the derivative and the cost under different parameters.

### Strengths
This paper considers an interesting topic: Attacking a single agent in multi-agent learning. The two main contributions are both noteworthy:

* The first main result indicates that to shift the global equilibrium, an attacker only needs to target one agent with sublinear cost. This practical finding provides valuable insights into the potential risks of multi-agent learning. 

* Second, the trade-off between efficiency and robustness is very interesting. I believe this will provide some heuristic for the design of robust algorithms.

Moreover, this paper is well-written.

### Weaknesses
I have several concerns about this paper:

1. The assumptions underlying the proposed attack are quite strong. (1) As the author admits,the adversary is assumed to have complete knowledge of the victim agent's utility function. This assumption, while useful for theoretical analysis, may not hold in practical scenarios, potentially limiting the contribution. Specifically, the assumption of perfect knowledge of the utility function is a significant limitation, as in real-world scenarios, this information is rarely available to an attacker. Furthermore, the paper does not discuss the implications of imperfect knowledge or potential strategies for the attacker to estimate the utility function. (2) The agent is assumed to be unaware of the attacker's presence. If the agents do know, will the attack still work?

2. There’s no knowledge regarding the difficulty of the problem. In other words, can the authors show any lower bound on the cost, which will further indicate the efficiency of the attack? It is worth noting that in a similar topic which is also mentioned by this paper, $[1]$ has already closed such a gap. Furthermore, Figure 2 illustrates the significance of this concern, as in the last sub-figure, the cost increases at an almost linear rate. What’s more, this $\alpha$ is determined by the dynamic itself, therefore it cannot be well controlled. Thus, the cumulative cost is quite large to some degree. After all, both $\log(\log(T))$ and $T^{1-\alpha}$ are sublinear, but their outcomes are totally different. The paper needs to provide a more rigorous analysis of the lower bounds on the attack cost, and how the specific learning dynamics influence the attack cost. The current analysis lacks a more granular understanding of the relationship between the learning rate, the attack cost, and the convergence properties of the multi-agent system.

3. The authors may have partially overstated their work. The problem they considered is a specific attack problem in monotone games, however, the title and introduction demonstrate greater ambition (in general games). Whether the results can be generalized remains unknown.

### Questions
Please try to solve the problems in weaknesses. Besides, there are some extra questions:

* The trade-off between robustness and efficiency is very intriguing. I suggest authors further highlight this part in the next version.
* In Line 169-170, is the parameter $L$ known to the adversary? How can the adversary select the target agent “smartly”?
* In Line 295-301, the authors want to show that more information will lead to the ability to control the attack direction. However, without more knowledge (which means more assumptions), this is not addressed. Similarly, in Line 319-322, the same issue arises for the derivative distance.
* In Proposition 1, what will happen if the target agents are a subset of all agents? I.e., for example, if the attacker can manipulate the utilities of two agents, is there any related result?
* Minor typo: There is a missing "." in Line 390.

### Soundness
4

### Presentation
4

### Contribution
3
