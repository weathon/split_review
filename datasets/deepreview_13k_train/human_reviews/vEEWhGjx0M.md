# Adversarial Attacks on Combinatorial Multi-Armed Bandits

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
We study reward poisoning attacks on Combinatorial Multi-armed Bandits (CMAB). We first provide a sufficient and necessary condition for the attackability of CMAB, a notion to capture the vulnerability
and robustness of CMAB. The attackability condition depends on the intrinsic properties of the corresponding CMAB instance such as the reward distributions of super arms and outcome distributions of base arms. Additionally, we devise an attack algorithm for attackable CMAB instances. Contrary to prior understanding of multi-armed bandits, our work reveals a surprising fact that the attackability of a specific CMAB instance also depends on whether the bandit instance is known or unknown to the adversary. This finding indicates that adversarial attacks on CMAB are difficult in practice and a general attack strategy for any CMAB instance does not exist since the environment is mostly unknown to the adversary. We validate our theoretical findings via extensive experiments on real-world CMAB applications including probabilistic maximum covering problem, online minimum spanning tree,  cascading bandits for online ranking, and online shortest path.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into adversarial attacks targeting combinatorial multi-armed bandits (CMAB). The authors introduce the concept of polynomial attackability in CMAB, wherein an attack is deemed successful if its cost remains sublinear with respect to the time horizon and polynomial, rather than exponential, in relation to the number of base arms. They provide both sufficient and necessary conditions for such polynomial attackability within CMAB and introduce an efficient attack algorithm. The discourse further extends to the challenges of polynomial attackability for CMAB instances in unknown environments, emphasizing the absence of a universal attack approach that guarantees success with polynomial costs under such unknown CMAB instances. Empirical results across diverse CMAB scenarios validate their theoretical findings.

### Strengths
1) This paper is the first to study adversarial attacks against CMAB algorithms, which is an interesting and timely topic.
2) The novel characterization of the sufficient and necessary conditions for polynomial attackability in CMAB provides insight into the distinct challenges posed by CMAB instances with polynomial costs.
3) The author presents a hard example highlighting that an instance can be polynomially attackable when the adversary is aware of the environment but becomes polynomially unattackable when the environment is unknown. This underscores the difficulty of launching general adversarial attacks on unknown CMAB instances.

### Weaknesses
1) Algorithm 1 seems to be straightforward but may lead to large attack costs when $\Delta$ is small. The attack cost's dependency on $\Delta$ from previous works [Jun et al., 2018, Liu and Shroff, 2019] is usually linear in $\sum_{i}  \Delta_i$, while the dependency in this paper is $1 / \Delta_{S^*}$, which is worse than $\sum_{i}  \Delta_i$ as $\Delta_i \le 1$. This is due to the lack of fine-grained attack value design. Specifically, the algorithm appears to apply a uniform attack strategy across all arms, rather than tailoring the attack intensity based on the specific reward gaps. This could lead to unnecessary attack costs on arms that are already close to the target arm's reward, and a more adaptive approach could potentially reduce the overall attack cost. For instance, if one arm has a reward very close to the target, the algorithm might still apply a full attack, which is wasteful.

2) While Theorem 4.1 establishes the difficulty of successfully targeting general unknown CMAB instances, there remains a potential to execute attacks in particular CMAB settings, such as PMC with **unknown** base arms. This is important since learning from the attacker side is one of the main challenges of attack design in previous works: simple oracle attacks [Jun et al., 2018, Liu and Shroff, 2019] can easily attack known K-armed bandit instances. I would expect more algorithm design and analysis for the unknown environment. The paper does not delve into specific strategies for learning the environment from the attacker's perspective, which is a crucial aspect of adversarial attacks in real-world scenarios. The current analysis focuses primarily on the theoretical limitations, but lacks concrete algorithmic approaches for the attacker to learn and exploit the environment when it is unknown.

### Questions
1) In Corollary 4.3, there is no guarantee that the randomly picked super arm $\mathcal{S}$ satisfied $\Delta_{\mathcal{S}} > 0$ (even for cascading bandits, online MST, and online PMC problem with greedy oracle, there exists $\mathcal{S}$ such that $\Delta_{\mathcal{S}} = 0$).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores adversarial attacks on Combinatorial Multi-Armed Bandits (CMAB). It discusses a sufficient and necessary condition for the polynomial attackability of CMAB and presents an attack algorithm for attackable instances. The authors also investigate how the attackability of a CMAB instance is influenced by whether the bandit instance is known or unknown to the adversary, which indicates that adversarial attacks on CMAB are difficult in practice and a general attack strategy for any CMAB instance does not exist. The findings are validated through experiments on real-world CMAB applications.

### Strengths
Originality: The paper introduces a novel concept of polynomial attackability in the context of combinatorial multi-armed bandits (CMAB). This notion captures the vulnerability and robustness of CMAB systems, which is a unique contribution to the field.

Quality: The paper provides a rigorous analysis of the attackability of CMAB systems and presents a sufficient and necessary condition for polynomial attackability. The paper also presents an attack algorithm for attackable instances. The paper validate the theoretical findings and demonstrate the effectiveness of the proposed attack via extensive experiments conducted on various CMAB applications.

Clarity: The paper is well-written and presents the concepts, definitions, and analysis in a clear and concise manner. The experimental setup and results are explained in detail, and the source code is provided, making it easy for readers to understand and replicate the experiments.

Significance: The paper addresses an important research question regarding the vulnerability of CMAB systems to adversarial attacks. By introducing the concept of polynomial attackability and providing a comprehensive analysis, the paper contributes to the understanding of the security and robustness of CMAB algorithms. The finding that the attackability of a specific CMAB instance also depends on whether the bandit instance is known or unknown to the adversary is impressive and may have practical implications for designing more secure CMAB systems in real-world applications.

### Weaknesses
1. The limitations of the findings are less discussed.

The findings regard the polynomial attackability highly depends on the threat model, in which the outcome of the base arms can be modified by the adversary. However, recent researchers discussed different types of adversarial attacks on bandit and RL [1-5], including also environment poisoning attack and action poisoning attack. In the CMAB system, the environment-manipulation adversary could manipulate the reward function $r$ and the action-manipulation adversary could manipulate the super arm $S$.

The proposed sufficient and necessary condition of the polynomial attackability is limited to the specific reward-manipulation adversary. If one environment-manipulation adversary can manipulate the reward function, $\Delta_M$ could be changed and the condition of the polynomial attackability does not work. Example 4.2 (Hard example) is also limited to the specific reward-manipulation adversary. Some statement in the abstract and introduction is inaccurate. The limitations of the findings are less discussed.

A more thorough discussion about the scope and limitation of the findings would be helpful.

2. Some problems in experimental results.

I found that the numerical experiments do not reflect the effect of the proposed attack algorithm. For example, in (2(g), 2(h)), the number of the target arm pulls is at most 4e3 after 1e5 iterations. The target arm is pulled in only 4% rounds.

In addition, the experiment that reflects the polynomial unattackablity would be helpful. I recommend that the author can run some experiments on the hard example. The adversary can attack the hard example instance using heuristics with sublinear attack budget.

### Questions
Overall, I like this paper but some statement in the abstract and introduction is inaccurate and the limitations of the findings are less discussed. Could the author provide more discussion about the scope and limitation of the findings?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies adversarial attacks on combinatorial bandits (CMAB).

### Strengths
Adversarial attack has been studied in stochastic bandits, linear bandits, adversarial bandits. The study of adversarial attack on CMAB is new. 
This work proposes new notions of attackability based on the structure of CMAB.

### Weaknesses
While the framework follows from previous work Wang & Chen, I feel the paper could benefit from a discussion on simpler CMAB models first (i.e. without the trigger function etc. )

I did not quite follow the problem setup. The formulation follows from the previous work Wang & Chen, which used infinite action space with the trigger function. However, in this submission, in the definition of super arms, it is first mentioned the action space could be infinite. But it also mentions each super arm is a set of base arm, which implies the cardinality of super arms is 2^m. Also, it seems that if we define a super arm as a set of base arms, then there is no need to define the trigger function?

Given my unfamiliarity with this line of work, it is currently unclear to me exactly how the action set is defined in this current work.

### Questions
I did not quite follow the problem setup. The formulation follows from the previous work Wang & Chen, which used infinite action space with the trigger function. However, in this submission, in the definition of super arms, it is first mentioned the action space could be infinite. But it also mentions each super arm is a set of base arm, which implies the cardinality of super arms is 2^m. Also, it seems that if we define a super arm as a set of base arms, then there is no need to define the trigger function? 

Given my unfamiliarity with this line of work, it is currently unclear to me exactly how the action set is defined in this current work.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers reward poisoning attacks on Combinatorial Multi-armed Bandits (CMAB), and provides a sufficient and necessary condition for the attackability of CMAB. This condition depends on the intrinsic properties of the corresponding CMAB instance such as the reward distributions of super arms and outcome distributions of base arms. The paper further illustrates that the attackability of a specific CMAB instance also depends on whether the bandit instance is known or unknown to the adversary.

### Strengths
The paper considers the adversarial attacks on combinatorial multi-Armed bandit. The paper introduces a new notion of attackability, which has a stronger requirement than existing conditions. The paper also characterizes a necessary and sufficient condition for this attackability when the underlying CMAB instance in a known environment.

### Weaknesses
1. The paper focuses on the new notion of attackability that requires the cost to scale polynomial in $m$. This is not well motivated. The paper only mentioned that "in practice, the exponential cost in $m$ can exceed $T$, resulting in vacuous results." Note that $T$ is growing, and we care about how the regret and the attack costs grow in terms of $T$. On the other hand, $m$ is fixed. So why it is more important to focus on the scaling in terms of $m$ than the scaling in terms of $T$? The argument that exponential cost in $m$ can exceed $T$ is not convincing, as $T$ can be arbitrarily large. A more rigorous justification is needed to explain why polynomial scaling in $m$ is a critical requirement for attackability, especially given that $m$ is a fixed parameter of the problem instance, while the time horizon $T$ is the primary factor influencing regret and attack cost in the bandit setting. The paper should clarify why focusing on the scaling with respect to a fixed parameter is more crucial than the scaling with respect to the time horizon, which directly impacts the performance of bandit algorithms.

2. The paper focuses mostly on the polynomial attackability of a CMAB instance in a known environment, i.e., all parameters of the instance such as the reward distributions of super arms and outcome distributions of base arms are given. This white box setting is of limited interest for practice. The analysis in the white-box setting, while providing some theoretical insights, does not address the more realistic and challenging scenarios where the adversary has limited or no knowledge of the environment. The paper should acknowledge the limited practical relevance of this setting and emphasize the need for future work to explore attack strategies under more realistic black-box conditions. The current focus on the white-box setting significantly reduces the applicability of the results to real-world scenarios.

### Questions
1. Better justify why one should focus on the scaling of $m$ term.
2. Can the authors provide the corresponding conditions for the black-box setting?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
