# Adversarial Attacks on Cooperative Multi-agent Bandits

- Decision: Reject
- Scores: 6, 3, 5, 5, 3

## Abstract
Cooperative multi-agent multi-armed bandits (\matob) consider the collaborative efforts of multiple agents in a shared multi-armed bandit game. We study latent vulnerabilities exposed by this collaboration and consider adversarial attacks on a few agents with the goal of influencing the decisions of the rest. More specifically, we study adversarial attacks on \matob in both homogeneous settings, where agents operate with the same arm set, and heterogeneous settings, where agents have distinct arm sets. In the homogeneous setting, we propose attack strategies that, by targeting just one agent, convince all agents to select a particular target arm $T-o(T)$ times while incurring $o(T)$ attack costs in $T$ rounds. In the heterogeneous setting, we prove that a target arm attack requires linear attack costs and propose attack strategies that can force a maximum number of agents to suffer linear regrets while incurring sublinear costs and only manipulating the observations of a few target agents. Numerical experiments validate the effectiveness of our proposed attack strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies adversarial attack strategies in the Cooperative Multi-Arm Bandit setting CMA2B. In the Cooperative Multi-Arm bandit setting ($M$) agents pull one arm each in round $T$ and observes reward sampled from a distribution associated with the arm. The agents some can communicate with each other to accelerate learning. In this paper, the authors study how an attacker can take advantage of agents trusting other agent's data, and can attack a subset of agents and influence other agents as well.
They study the problem in two settings:

i) Homogeneous setting: Here all agents have access to all arms. They show only one agents can be injected with $o(T)$ corruptions and cause a target suboptimal arm to be selected for $T - o(T)$ rounds under the CO-UCB algorithm. They also show results for UCB-TCOM (a communication efficient UCB style algorithm), DPE2 (a leader-follower algorithm), and general no-regret algorithms.

ii) Heterogeneous setting: In this setting, each agent has access to a subset of arms. They show that there can be instances where arms are distributed in a way that to incur linear regret to each agent in CO-UCB, an attacker would need a linear attack budget.

They propose a selection algorithm called AAS to select the arms that are optimal for as many non-conflicting agents and TAS to select agents to attack. They provide regret guarantees for the CO-UCB algorithm under this setting. 

They also provide experiments with simulated data for comparing their attacks on the CO-UCB algorithm.

### Strengths
1. The setting of adversarial attacks on cooperating bandits studied in the paper is well-motivated
2. The authors provide the analysis for the homogeneous and heterogeneous settings, and under different CMA2B algorithms, at least in the homogeneous setting. The results that UCB style CMA2B algorithms can be  $o(T)$ corruptions and cause a target suboptimal arm to be selected for $T - o(T) times by targeting just one arm in homogeneous settings has novelty. The detailed analysis of the heuristics AAS and TAS also shows that agents showing that a large number of agents can be attacked using sublinear corruptions is also valuable. The authors also provide an analysis of the case when rankings are not known to the attacker making the attack more practical. 
2. The authors provide experimental evidence for the novelty of AAS and TAS.
3. The paper is overall well written, with clear notations

### Weaknesses
1. The homogeneous setting studied under the Co-UCB is very similar to the results for UCB obtained in Jun et al. [2018]  as every agent can see every other agents rewards and updates the mean rewards and counts, it's similar to the one agent setting, but the agent obtains $M$ samples in every round from the arm they pull instead of 1, thus I believe the results of \citet{jun2018adversarial} can can be modified to obtain this result, so there is limited novelty in this result.

2. Most of the results are on UCB style algorithms, or on the communication model where all agents immediately share the information will all other agents. I feel this is fairly limited setting as the samples are effectively shared easily and it makes the attack easy as any agent can be attacked with a big enough value that gets propagated to all other agents. What happens when the communication model is constrained through addition structures for e.g., the graph structured discussed in Landgren et al. [2016].
They do provide analysis for UCB-TCOM and DPE2 with delayed communication, but in both case, the information is still easily transmitted to all agents.

3. I believe the results against general algorithms need some more refinement in terms of assumptions. Line 1308 on Page 25 assumes that since the other arms' samples always come from a distribution with a mean less than the mean of the target arm, we can consider arm $K$ to be the best arm. The results for general bandit algorithms are based on the fact that reward samples are being sampled from a fixed distribution, if the sample distribution for the other arms is changing with $t$ (as the attack), I don't think we can directly claim Assumption 2 to hold. The main point is that in Assumption 1, it's not clear what it means that the 'agents maintain identical empirical means for making decisions'. Maybe the authors can refine Assumption 1 to a class of more restricted MAP/CMA2B algorithms like the mean based algorithms defined in Xu et al. [2021].

4. It's difficult to understand the $T_0$ term in the heterogeneous results, and how it's always a constant.

5. The experiments provided are fairly limited, with no error bars.

Minor comments:
In line 707, it should be $- \hat{\mu} (K)$ instead of  $+ \hat{\mu} (K)$

### Questions
1. What are the additional challenges in adapting the results of Jun et al. [2018] for the homogeneous setting with CO-UCB?

2. Can we experimentally verify if these results would work for cooperative versions of simple MAB algorithms like $\epsilon$-greedy or Thompson sampling?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work considers the cooperative multi-agent multi-armed bandits (CMA2B) problem to design attack algorithms, which aim to attack on a few agents to influence the decisions of the rest. The authors consider two different settings, i.e., (1) homogeneous settings, where agents operate with the same arm set, and (2) heterogeneous settings, where agents may have distinct arm sets, to design different attack algorithms. Then they provide theoretical analysis on the caused bad regret of CMA2B system under their attack algorithms. Finally, they conduct numerical experiments to verify the efficiency of their proposed algorithms.

### Strengths
1.	This paper is well-written and easy to follow, with clear assumptions and a thorough review of existing literature.
2.	The authors address both homogeneous and heterogeneous settings in designing efficient attack algorithms, offering a solid theoretical analysis of the regret lower bounds induced by these attacks.

### Weaknesses
While the paper is presented well, the assumptions are highly restrictive, and the proposed attack algorithms apply only to specific CMA2B algorithms (i.e., CO-UCB or UCB-TCOM), which limits the general applicability of this work.

Specific concerns include:
(1)  No Collision: The authors overlook collisions in the multi-agent MAB (MMAB) problem, lacking literature support for this choice. Most studies on MMAB, including works like Boursier & Perchet (2019), incorporate collisions when multiple players select the same arm simultaneously. This assumption is particularly relevant in applications such as cognitive networks.
(2)  Pre-Attack Reward Observability: The paper assumes that the attacker can observe pre-attack rewards for all agents, which seems unrealistic in practical applications. It remains unclear how an attacker would access this information.
(3)  Prior Knowledge of Local Arm Sets: In the heterogeneous setting, the assumption that the attacker knows each agent’s local arm set also seems impractical.
(4)  Algorithm Awareness: The assumption that the attacker knows each agent’s exact algorithm is the strongest and most limiting. This could be plausible if the attacker were an agent within the CMA2B setup, yet targeting a specific algorithm still limits the broader impact of the proposed methods.
(5)  Other strong assumptions include (a) the attacker knows the exact leader in the leader-follower structure, and (b) The attacker has prior knowledge of the reward ranking of all arms. While the authors relax this latter assumption in Section 4.3, introducing this relaxation earlier could strengthen the contribution.
I recognize that this is a theoretical study; however, given that the motivation for these attack algorithms is practical application, the heavy reliance on these assumptions restricts their practical relevance.

### Questions
Pls see my questions in weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work examines vulnerabilities in cooperative multi-agent multi-armed bandit systems, where agents work together to maximize rewards but can be disrupted by adversarial attacks targeting a few agents’ feedback. In homogeneous settings, where agents share the same choices, the authors show that minimal manipulation of one agent’s observations can influence the entire group to select suboptimal arms. In heterogeneous settings, with agents having different options, the authors propose strategies to induce linear regret among the maximum number of agents by attacking a few key agents. In addition to theoretical results, the authors support their claims with experimental evaluations.

### Strengths
- **Originality:** While previous works have dealt with robustness in multi-agent bandit systems against weak corruptions [1,2], this paper addresses weaknesses against adversarial attacks tailored for this setting. The attack target for the heterogeneous setting is novel compared to single-agent bandits [3]. 
- **Quality:** The theoretical analysis is rigorous, with clear proofs supporting the various claims and an experimental evaluation section. 
- **Clarity:** Using simple example cases, the paper explains the motivation and intuition behind using a different attack target than in previous works. 
- **Significance:** By highlighting the potential for low-cost adversarial disruptions in cooperative learning systems, the paper reveals critical vulnerabilities that could have implications for designing more robust systems. 

[1] Vial, Daniel, Sanjay Shakkottai, and R. Srikant. "Robust multi-agent multi-armed bandits." Proceedings of the Twenty-second International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing. 2021.

[2] Dubey, Abhi, and Alex Pentland. "Private and Byzantine-Proof Cooperative Decision-Making, 20th Conf. Autonomous Agents and Multiagent Systems, 2020.", 2020.

[3] Jun, Kwang-Sung, et al. "Adversarial attacks on stochastic bandits." Advances in neural information processing systems 31 (2018).

### Weaknesses
 **Minor issues:**
- line 47: hope->hopes
- line 68: since this point is addressed in this work, the phrase 'remain uncertain' is confusing. 
- line 75: 'remains an unresolved issue' - similar to my last remark. 
- line 101: 'with its cost analysis'-> 'and analyze its cost'. 
- line 131: the use of 'observes' is confusing here, as this is the pre-attack value and is not necessarily observed as is. 
- line 139: 'collision'-> collision model. 
- lines 143-152: The authors should explain this choice for the heterogeneous model, or cite previous works that use it. 
- lines 191,423: 'no-regret'-> sublinear regret
- section 4.1: the intuitive examples could be explained better - how many arms does each agent have?
- lines 352-361: the term 'attack value' was never formally defined, nor did the mean $\hat{\mu}$.
- line 362: 'constant fulfills'-> constant that fulfills. 
- line 424: 'affected'-> target.
- line 449: 'unknown'->known.
- line 484: 'when'-> at
- line 519: 'Leaning'-> Learning

**Other issues:**
- This work is not written clearly and assumes the reader possesses extensive technical knowledge about adversarial attacks in bandits. For example, the term attack value is not explained in the main text, and the idea behind equation (2) is also unclear. The parameters in Thm 1 are undefined as well: What are $\alpha,\Delta_0$?
- Table 1 is misleading. For the first and second lines, it is unclear whether knowledge about the time horizon $T$ is needed. The authors can cite [1] rather than [2] if it is not. More importantly, the third line assumes oracle knowledge of the attacker about arm rankings (Thm 3), which is a strong assumption. When using the version that does not use this assumption, the attack cost becomes much larger at $O(K\log T/\Delta_{\min}^2)$ (Thm 4).
- The problem addressed in this paper could be motivated better. In the Introduction, the authors mention advertisers that share information about users as an example of a multi-agent bandit system that can be attacked. However, I am not sure how practical this problem is given the requirements for user privacy preservation. It would be nice if the authors could expand on that, provide references, or suggest additional motivation. 
- While the attack design for heterogeneous systems is novel, it should be mentioned that the attack itself used in this paper 
technically resembles techniques from previous works [1,2] (for instance, equation (2)). 
- The difficulty of adversarial attacks on a heterogeneous multi-agent system is not fully characterized. The authors mention it is not possible to cause all agents to suffer linear regrets, and find a nearly maximal set of affected agents. Regarding the target agents group, it is unclear to me if the one used in this paper is the minimal one, or if we can use fewer target agents with the same effect. In addition, as mentioned above, the attack cost under realistic assumptions is $O(K\log T/\Delta_{\min}^2)$ for the heterogeneous case, but there is no lower bound to show how good this result is. 
- In the heterogeneous case, an attack is only designed for one algorithm. For single-agent bandits, it is acceptable to design attacks for very basic algorithms like UCB and $\epsilon$-greedy as done in [2], but in the multi-agent setting, it is unclear whether an attack on CO-UCB provides insight into attacks on other algorithms. Perhaps the authors can further expand on this point - is CO-UCB as fundamental for heterogeneous multi-agent bandits as UCB is for single-agent bandits?
- Figure 3a is not clear. What is the 'average regret' that is plotted here? Since it remains constant, I suppose it should be some kind of instantaneous regret, but this is not explained at all and the only regret defined in this paper is the cumulative one. In addition, it is unclear how the OA and LTA algorithms are performed without AAS. 

### Questions
- In Table 1, do we assume that all arms have different means? Otherwise, it is possible that the same agent has several optimal arms and is counted in $M_{*}(k)$ for several arms. The same holds for the results in Thms 3,4. 
- In line 359 for $\hat{\mu}_{t}(k)$, why are all pre-attack values $X_t^{(m',0)}(k)$ for arm $k$ counted? If I understand correctly, it does not hold that all agents draw the same arm at each round. 
- For the heterogeneous setting, do the authors think it is possible to choose a smaller group of target agents than the one in this paper? Can the attack cost be lower than $O(K\log T)$ for some other attack strategy? 
- In line 203, can the authors expand more on why the multi-agent setting is more challenging, and what makes the analysis more involved?
- For Figure 3a, what is the average regret, and how were experiments for OA and LTA performed without AAS?
- In the discussion on page 8 before 4.2.4, can you explain in more detail what it means that target agents are 'the first' to pull an arm? This point is repeated a few times but is not entirely clear.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies adversarial attacks in a multi-armed bandit setting, where multiple learners are collaboratively learning. The agents may communicate their shared information between themselves. An adversary may, however, sit between the environment generating rewards and the agent and specify erroneous rewards to them. The adversary wishes to derail the agents while minimizing the number of times they need to intervene. The paper studies two models - *homogeneous*, where any agent can pull any arm and *heterogeneous* where an agent may pull only a subset of arms (determined exogenously). The first setting is easy for the adversary and using similar ideas from literature, the paper gives a nearly optimal bound. The second setting is harder, and the paper gives a set of results under different adversary goals.

In general, I found the work well-written and clearly explained and exposited. Taking the model as a given, the paper studies the reasonable set of questions that arise. That said, I am not convinced of the underlying model of collaboration or adversary that is presented; while I am quite familiar with bandit literature, this sub-category of bandit literature is not as known to me and I am unsure about how to correctly contextualize the results and reason about the major takeaways. As such, I am borderline on the work.

### Strengths
The work is well-written and quite easy to follow and quickly gain the main insights. The authors do a good job of highlighting their assumptions and the model, and then investigating a lot of the natural questions that emerge. If we take the model as a given, the contributions are sound.

I found the impossibility results in the heterogenous setting particularly insightful. It almost suggests that for a goal-oriented adversary (and not a purely malicious one) it is quite difficult to achieve their target without incurring high cost.

### Weaknesses
My main concern is the applicability or relevance of the model. What exactly is the setting where one would encounter the scenario proposed and thus this work would be insightful? Could you provide some motivating examples? Specifically, the heterogenous setting (the main meat of the paper) where an oracle attacker is assumed. The setting here afaik is as follows:
* A number of agents are collaboratively learning the same online learning with unlimited communication, but a powerful adversary, who knows the true ranking of all arms, can inject arbitrary errors into the observations of any agent?

In the heterogenous section, you essentially argue for an attacker's goal as misleading agents, and not necessarily get their (attacker's) sub-opt arm picked. In this sort of purely adversarial, almost zero-sum type of attacker reasonable? Under what context could we expect such as attacker? Or do we gather any technical/conceptual insights under this model?

In the paper, it is assumed that the attacker knows the algo used by the learner. While it can be relaxed in the homogenous case, it is necessary in the heterogenous case. I am happy that the authors explicitly mention this, but given that the heterogenous case is the main contribution of the paper, I still find this quite a big assumption and somewhat unreasonable. Are there settings you can motivate where this might be the case?

### Questions
See the above weaknesses.

It is likely that the agents know the distribution type for the rewards (even if they don't know the expected value or anything else). In that setting, the attacker injecting strategically chosen errors (without any real constraint) might tip the agent to think something is amiss since the samples may not reflect the distribution family they know the problem to have. Do you think it's possible - specifically in the attacks you have discussed? In general, there might be reasonable constraints to add on what can be injected.

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
This paper presents attack strategies for collaborative multi-armed bandits using CO-UCB algorithms under two distinct settings: a homogeneous setting, where all agents have access to all arms, and a heterogeneous setting, where different agents have access to different subsets of arms. For the heterogeneous setting, the author considers two types of attackers: an oracle attacker, who has explicit knowledge of the average reward ranking of each arm, and a non-oracle attacker, who lacks this information. Additionally, the author conducts experiments to validate the theoretical results.

### Strengths
This paper is the first to explore adversarial attacks in the context of cooperative learning within multi-agent, multi-armed bandits. This problem is novel. Furthermore, the design of the algorithms for Affected Agents Selection (AAS), Target Agents Selection (TAS), and the proof of Theorem 3 are both innovative and nontrivial.

### Weaknesses
First, the paper lacks discussion about the novelty and major technical challenges for various results (e.g., Theorem 1, Proposition 1 and 2), which makes it really difficult to judge the significance of the contribution. For instance, they state: "In Section 3, for homogeneous CMA2B, we devise attack strategies for three representative algorithms by targeting a single agent to misguide all agents. We prove that the attack costs are independent of the number of agents, M." However, since observations are shared and all agents are homogeneous, it is unsurprising that attacking one agent could misguide the rest, making the cost independent of M. This result appears intuitively straightforward. Additionally, the attack strategy seems quite similar to that in Zuo, S. (2024, April), with the proof being a straightforward extension from the single-agent to the multi-agent setting. The authors do not highlight any significant additional challenges, making it unclear how significant the technical contributions are.

Second, many results and proofs are inaccurate, and require the reader’s careful verification in order to convince themselves that the proof or statement is really correct. Even I was able to verify that some missing proofs can be fixed, I was not able to check all the proofs and it makes me feel the paper really needs significant amount of re-writing and polishing before being ready for publication.
1.	In the statement of Theorem 1, the term "our attack strategy" is ambiguous because there is only some vague descriptions about the attack idea and no clear mathematical definition about the attack. The reader had to go to the appendix to check the definition.
2.	In the proof of Theorem 2 (page 16), it states “\(f\) is submodular and the greedy algorithm in Algorithm 1 gives a \((1 - 1/e)\)-approximation solution”. This is inaccurate – the paper needs to additional prove the function is monotone and non-negative (PS: the paper also need to cite papers for this statement as not everyone knows this result). I think I convinced myself that these two properties are also true, but I think a maturely written paper should not ask reviewers to complete these reasonings and verify correctness.  
3.	In Theorem 3 (also Theorem 4), the term \(\Delta(k, k+1)\) is not defined rigorously, as the author has not established that \(K \notin K_0\). If \(K \in K_0\), \(\Delta(K, K+1)\) is undefined. Also, Equation (3) does not include \(T_0\); actually none of the equations in this page has T_0. In the statement of Theorem 3, the definition of \(g(k)\) is missing, which also affects the subsequent discussion. I had to go to the appendix to double check the correct expression and definition


In addition to above concerns on the significance of contributions, the paper contains a few other major issues, including too many syntax issues, gaps in proofs, too much assumptions of prior knowledge from the reader, and a lack of discussion on the contributions (including over-claiming contributions). These factors make it difficult for readers to fully understand the key ideas and may lead them to question the rigor of the proofs. A few examples are listed as follows.

1.	Line 111 to 112, the paper claims that “Our work is the first to study how an attacker may manipulate multi-agent cooperative learning”. However, this ICML’20 https://proceedings.mlr.press/v125/boursier20a.html, Mobihoc’21 paper ahttps://dl.acm.org/doi/abs/10.1145/3466772.3467045 and AAMAS’22 https://dl.acm.org/doi/10.5555/3635637.3662992 seem to have already been studying similar problem of attacking cooperative bandit problem.  

2.	In line 6 of Algorithm 1, what is \(\omega(k)\)

3.	On Page 5, line 268, the stated goal is to “leverage sublinear attack costs to misguide the maximum number of agents, aiming to increase the overall count of agents enduring linear regrets.” However, why using Algorithm 3 will lead to “attacking the maximum number of agents” is neither justified nor adequately explained in the subsequent paragraphs, leaving readers to infer the reasoning on their own. 

4.	The second claimed contribution appears to be inaccurate. The paper states, "linear costs are necessary to fool all agents into suffering linear regrets." However, this seems straightforward, as the target arm attack might not be a suitable objective in a heterogeneous environment (as mentioned in line 252). Therefore, a more accurate contribution might be to propose an appropriate and meaningful "attacking goal" specifically tailored to the heterogeneous setting, based on my understanding.

5.	On page 7, line 327, the phrase “is it feasible to attack this group using only a limited number of agents” is unclear. It would be beneficial to clarify what is meant by “using a limited number of agents.” If the intended meaning is “attacking a limited number of agents to misguide the maximum number of agents without conflicts, resulting in linear regret,” then it should be explicitly stated to avoid confusion.

6.	On page 9, line 463, the term \( \text{UCB}_t(k) \) is introduced without being defined (though the reviewer knows, but this is not a proper way to write a general-purpose ML paper), and there is no reference to this quantity elsewhere in the text.

7.	Figure 3 lacks standard deviations or confidence intervals, which undermines the claim that “Both LTA and OA result in the most significant average regrets.” Without measures of variability, it is difficult to assess the statistical reliability and significance of this claim. To strengthen the argument, it would be beneficial to include standard deviations or confidence intervals in the figure, providing a clearer depiction of the uncertainty and supporting the robustness of the results.

### Questions
Regarding the problem setting, what is the difference between this paper’s attack setting and previous works such as ICML’20 https://proceedings.mlr.press/v125/boursier20a.html, Mobihoc’21 paper ahttps://dl.acm.org/doi/abs/10.1145/3466772.3467045 and AAMAS’22 https://dl.acm.org/doi/10.5555/3635637.3662992.(and possibly others since I only did a light search about “attacking multi-agent bandits” on Google Scholar)? 

It seems to the reviewer that the homogeneous agent setting is a simple corollary of Zuo’24 result. Would it be possible to just describe Theorem 1 as a simple corollary of Zuo’24? What’s the research value of theorem 1? 

Can we eliminate TAS? What is the benefit of including TAS? Currently Theorem 3 shows that the attack cost is independent of the number of affected agents by attacking limited number of agents generated by TAS, what if we just attack agents in K0? What will change? Will it significantly inflate the attacking cost?

Are there any real-world applications, aside from “botnets,” that can be modeled as adversarial attacks on cooperative multi-agent bandits? The introduction currently provides only one example and lacks supporting references.

### Soundness
1

### Presentation
1

### Contribution
2
