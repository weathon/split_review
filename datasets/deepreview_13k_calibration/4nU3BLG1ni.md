# Multi-player Multi-armed Bandits with Delayed Feedback

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 3, 8, 5

## Abstract
Multi-player multi-armed bandits have been researched for a long time due to their application in cognitive radio networks. In this setting, multiple players select arms at each time and instantly receive the feedback. Most research on this problem focuses on the content of the immediate feedback, whether it includes both the reward and collision information or the reward alone. However, delay is common in cognitive networks when users perform spectrum sensing. In this paper, we design an algorithm DDSE (Decentralized Delayed Successive Elimination) in multi-player multi-armed bandits with stochastic delay feedback and establish a regret bound. Compared with existing algorithms that fail to address this problem, our algorithm enables players to adapt to delayed feedback and avoid collision. We also derive a lower bound in centralized setting to prove the algorithm achieves near-optimal. Numerical experiments on both synthetic and real-world datasets validate the effectiveness of our algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors have considered the delayed feedback setting in multi-player multi-armed bandit problem, motivated by cognitive radio applications. A decentralized delayed successive elimination (DDSE) algorithm which takes into account stochastic delay, is proposed in the paper, and a regret bound is established.  Contrary to existing algorithms, the proposed algorithm can avoid collision by adapting to delayed feedback. A corresponding lower bound on the regret is also derived. Experiment results are presented to demonstrate the efficacy of the proposed algorithm.

### Strengths
The considered problem is well-motivated and the analysis appears to be sound.

### Weaknesses
The proposed algorithm takes a leader-follower approach which makes it semi-distributed in nature as there is a necessity of communication between the leader and the followers. There are works in the literature which can work without the requirement of a leader, e.g., 
Trinh, Cindy, and Richard Combes. "A High Performance, Low Complexity Algorithm for Multi-Player Bandits Without Collision Sensing Information." arXiv preprint arXiv:2102.10200 (2021).
The rationale behind Assumption 1 is not entirely clear. The components of delay are not well-defined. For example, it is unclear whether it includes queueing delay. The practicality of considering sub-Gaussian delay, especially given the potential for arbitrarily large queueing delays, is questionable.
The authors have considered the fixed user setting where no users are allowed to enter or leave the systems. However, in a practical cognitive radio application, users may enter or leave the system. How does the proposed algorithm behave when user entering and leaving are allowed in the system?
It is not clear why there is a provision of eliminating arms for which LCB is bigger than UCB. Please specify the motivation behind the virtual communication phase in details.
Please provide a pointer to the result where an upper bound on the feedback delay is derived. This result has been used in Lemma 1. 
Can the authors quantify the gap between the lower bound and upper bound on the regret of the proposed algorithm? It will be more justified to call the proposed algorithm near-optimal then. 
Since the paper is highly motivated by cognitive radio applications, I expected some real wireless networks simulations (such as ns-3 simulations) where delays will be real delays in a wireless network.

### Questions
My concerns are as follows:
1.	The proposed algorithm takes a leader-follower approach which makes it semi-distributed in nature as there is a necessity of communication between the leader and the followers. There are works in the literature which can work without the requirement of a leader, e.g.,  
Trinh, Cindy, and Richard Combes. "A High Performance, Low Complexity Algorithm for Multi-Player Bandits Without Collision Sensing Information." arXiv preprint arXiv:2102.10200 (2021).
2.	What is the rationale behind Assumption 1? What are the components of delay? For example, does it contain queueing delay? How practical is the consideration of sub-Gaussian delay?
3.	The authors have considered the fixed user setting where no users are allowed to enter or leave the systems. However, in a practical cognitive radio application, users may enter or leave the system. How does the proposed algorithm behave when user entering and leaving are allowed in the system?
4.	It is not clear why there is a provision of eliminating arms for which LCB is bigger than UCB. Please specify the motivation behind the virtual communication phase in details.
5.	Please provide a pointer to the result where an upper bound on the feedback delay is derived. This result has been used in Lemma 1. 
6.	Can the authors quantify the gap between the lower bound and upper bound on the regret of the proposed algorithm? It will be more justified to call the proposed algorithm near-optimal then. 
7.	Since the paper is highly motivated by cognitive radio applications, I expected some real wireless networks simulations (such as ns-3 simulations) where delays will be real delays in a wireless network.

### Soundness
3

### Presentation
3

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
Multi-player multi-armed bandits have been researched for a long time due to their application in cognitive radio networks. In this setting, multiple players select arms at each time and instantly receive the feedback. Most research on this problem focuses on the content of the immediate feedback, whether it includes both the reward and collision information or the reward alone. However, delay is common in cognitive networks when users perform spectrum sensing. This paper designs a decentralized delayed successive elimination (DDSE) algorithm in multi-player multi-armed bandits with stochastic delay feedback and establish a regret bound. This algorithm enables players to adapt to delayed feedback and avoid collision.

### Strengths
In order to address the challenge of delay in cognitive radio networks, this paper proposes a novel bandit framework where multiple players engage in a multi-armed bandit and if two or more players select the same arm, none of them receive the reward. In this framework, players receive feedback after a period of stochastic delay, which complicates their ability to learn and adapt in real time, making it exceedingly difficult to avoid collisions and optimize performance. To solve this problem, this paper designs a DDSE algorithm in multi-player multi-armed bandits with stochastic delay feedback and establish a regret bound of the proposed algorithm.

### Weaknesses
The paper provides a series of technical results,  but the writing is muddled and many key symbols are not explained. It is very hard to get some intuition about the approach and its possible advantages and disadvantages. In addition, the description of the algorithm is full of confusion, with many unexplained symbols inside.

1. Why set the length of each communication phase as $K+2M$? The authors should explain the reasons for the design. If the length of communication phase becomes time-varying, will the methods in this paper still apply?

2. The paper provides an analysis of the lower bound for centralized algorithm in Theorem 3, but lacks an analysis of the lower bound for decentralized algorithm, which should be the main focus of the paper.

3. According to Theorem 1 and Theorem 2, DDSE has better convergence performance than DDSE without delay estimation. However, in larger scenarios (Fig. 4(d)), DDSE without delay estimation performs better than DDSE. What is the significance of considering delay estimation in delay estimation algorithms in large-scale scenarios?

4. This paper lacks a description of the proof process for the theorems. In addition, the result of Theorem 1 is complex and the paper lacks specific explanations for these terms.

### Questions
1. The writing is confused, many symbols are written incorrectly, and there are symbols that are not explained. For example, 
(1) On line 157 of page 3, $r^{j}(s)$ should be written as $r^{j}_{k}(s)$; $\mu_{k}$;
(2) what is the difference between $\mu_{k}$ and $\mu_{(k)}$;
(3) The definition of $N_{t}(k)$ on line 210 of page 4 is error; 
(4) The $\mathcal{M}_{0}$ in Algorithm 1 should be  $\mathcal{M}^{M}_{0}$;
(5) What is the $\mathcal{M}_{com}$ in Algorithm 1?

2. The introduction of the Algorithm 1 is very confusing. For example,
(1) What does the line 10 line of the Algorithm 1?
(2) In the model, author claim that $M\leq K$, but in the Algorithm 1, $|[K]|=M$ is used as a criterion for judgment. Please explain this issue.

### Soundness
2

### Presentation
1

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
The paper studies the multi-player, multi-armed bandit problem. The difference from the studies is that the authors allow the feedback to be received with a random delay. 
The authors develop an algorithm named DDSE and upper bound its performance. They establish that the algorithm is near optimal by deriving a lower bound.

### Strengths
The paper provides a detailed analysis of the algorithms and establishes a low bound. However, I could not verify all the claims due to presentation issues.

### Weaknesses
The authors consider the multi-player multi-armed bandit problem with a leader-follower structure. Several authors explore this problem. The new dimension of delayed feedback is a minor extension. In addition, I have concerns about the following aspects:

1. The literature review is not detailed: Several papers consider multi-player bandits with a more general heterogenous reward structure, which is well suited for cognitive radio networks. 
2. The algorithm is hard to understand: (see details below)
3. The experiments section is weak: Why only compare with SIC-MMAB and not with other algorithms like Game-of-Thrones and Explore-Signal-Exploit Repeat

### questions:
 It is hard to understand the DDSE algorithm. 

1.  What is the duration of exploration, communication, and exploitation?
2. Line 190 says, "the best empirical set arm set of player j." How is this set defined?
3. Line 204: "To avoid collision with followers and ensure sufficient exploration, the leader first sequentially hops in the set of best empirical arms with followers." How is it ensured that the best empirical arm of leader and follower do not overlap? How is the collision avoided?
4. How are collisions interpreted in the communication phase? Is it binary signaling?


In the experiment section, why are the algorithms in any of the following papers not considered?
1. http://proceedings.mlr.press/v83/besson18a/besson18a.pdf
2. http://papers.neurips.cc/paper/7952-distributed-multi-player-bandits-a-game-of-thrones-approach.pdf
3. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8737653

Minor issues:

1. Line 209: s<T or s<t?
2. Is there any difference between sequential hopping and round-robin?
3. Notation say [n]={1,2,..,n}. Then why |[K]| is M, not K?

### Questions
It is hard to understand the DDSE algorithm. 

1.  What is the duration of exploration, communication, and exploitation?
2. Line 190 says, "the best empirical set arm set of player j." How is this set defined?
3. Line 204: "To avoid collision with followers and ensure sufficient exploration, the leader first sequentially hops in the set of best empirical arms with followers." How is it ensured that the best empirical arm of leader and follower do not overlap? How is the collision avoided?
4. How are collisions interpreted in the communication phase? Is it binary signaling?


In the experiment section, why are the algorithms in any of the following papers not considered?
1. http://proceedings.mlr.press/v83/besson18a/besson18a.pdf
2. http://papers.neurips.cc/paper/7952-distributed-multi-player-bandits-a-game-of-thrones-approach.pdf
3. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8737653

Minor issues:

1. Line 209: s<T or s<t?
2. Is there any difference between sequential hopping and round-robin?
3. Notation say [n]={1,2,..,n}. Then why |[K]| is M, not K?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers a multi-arm multi-player bandit setup with delayed reward. The paper proposes novel algorithms to counter the delay in receiving the reward. The paper bounds the regret in the decentralized setting.

### Strengths
1. Bounding the regret in the multi-armed multi-agent bandit setup is challenging. The paper additionally consider the delay, hence, the contribution seems to be significant.

2. The paper achieves the regret bound. 

3. Empirical results show the efficacy of the proposed approach.

Post-rebuttal Edit: Addressing the delay parameter in the multi-armed collision model is important. Thus, I am happy to accept this paper.

### Weaknesses
1. The paper considers cognitive radio setup. However, cognitive radio is hardly used in practice, it is only of academic interest. Can the paper provide any other relevant examples?

2. The paper is very hard to read, hence, the contributions are obscure.

### Questions
1. Can the authors highlight the main technical challenges? Delay in the multi-armed setting is considered, while the reviewer agrees that the collision model does complicate things, in the technical level, how the analysis will be different is not clear.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies multi-player multi-armed bandit (MMAB) problem with delayed feedback, motivated by the application of cognitive radio networks. Unlike previous MMAB problems that assume instantaneous feedback from arms, this work tackles the challenge posed by delayed feedback. To overcome this challenge, this work proposes a decentralized delayed successive elimination (DDSE) algorithm, which operates in three stages: exploration, communication, and exploitation. The proposed DDSE algorithm enables players to adapt to delayed feedback and avoid collision. This work theoretically analyzes the upper bound of regret for the DDSE algorithm and further compares the regret with two benchmark cases: DDSE without delay estimation and centralized lower bound. By comparison, it shows that the DDSE achieves a near-optimal regret bound.

### Strengths
1.	The problem of MMAB with delayed feedback is well-motivated and highly relevant to real-world applications.
2.	Introducing delayed feedback significantly increases the complexity of the already challenging MAB problem. The authors effectively decompose the regret to handle this complexity and present solid theoretical results.
3.	The paper is well-written and easy to follow.

### Weaknesses
1.	My main concern lies on the ID allocation for the leader-follower structure in the DDSE algorithm. If the central planner can assign an ID to each player, this DDSE algorithm is no longer fully decentralized. In many cognitive radio networks, sensing nodes are dynamic, and some nodes are even hidden or unknown to the network operator. The requirement of a central authority for ID assignment severely limits the practical applicability of the proposed approach in realistic scenarios, where such coordination is often infeasible or impossible. This reliance on a central planner undermines the distributed nature of the algorithm.
2.	The communication assumption weakens the solution in this work. The specific communication scheme, involving a leader broadcasting information, might not be robust to real-world channel impairments, such as fading or interference. The assumption that all followers reliably receive the leader's signals, without any packet loss or corruption, is not realistic in practical wireless environments. The communication overhead and latency introduced by this scheme also need careful consideration.
3.	I suggest the authors to move Subsection 5.3 ahead of Subsection 5.1 for better logic, as the centralized lower bound serve as the benchmark.
4.	In the experiments, the number of players $M$ is a relatively small compared to typical application of cognitive radio networks. The limited scale of the experiments makes it difficult to assess the scalability of the algorithm in more complex and dense network deployments. The experimental results might not be representative of real-world scenarios with a large number of players.
5.	In the experiments, the authors simply compare DDSE with two methods that do not account for delay. This comparison may be somewhat unfair. If there is no other available algorithm, it would be better to compare DDSE with the benchmark centralized algorithm.

### Questions
1.	In cognitive radio networks, players are usually dynamic. Additionally, there are some hidden nodes (players) that are unknown to each other. In this case, will the DDSE algorithm still work? 
2.	If a player $j$ is waiting for the feedback from arm $k$ (i.e., $t<s+d_s^j$) and another player $l$ pulls this arm $k$, will there be a collision? If a collision occurs, will player $j$ fail to obtain a reward from arm $k$ after waiting $t-s$ time slots?

### Soundness
2

### Presentation
3

### Contribution
2
