# Mechanism design with multi-armed bandit

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
A popular approach of automated mechanism design is to formulate a linear program (LP) whose solution gives a mechanism with desired properties.  We analytically derive a class of optimal solutions for such an LP that gives mechanisms achieving standard properties of efficiency, incentive compatibility, strong budget balance (SBB), and individual rationality (IR), where SBB and IR are satisfied in expectation.  Notably, our solutions are represented by an exponentially smaller number of essential variables than the original variables of LP.  Our solutions, however, involve a term whose exact evaluation requires solving a certain optimization problem exponentially many times as the number of players, $N$, grows.  We thus evaluate this term by modeling it as the problem of estimating the mean reward of the best arm in multi-armed bandit (MAB), propose a Probably and Approximately Correct estimator, and prove its asymptotic optimality by establishing a lower bound on its sample complexity.  This MAB approach reduces the number of times the optimization problem is solved from exponential to $O(N\,\log N)$.  Numerical experiments show that the proposed approach finds mechanisms that are guaranteed to achieve desired properties with high probability for environments with up to 128 players, which substantially improves upon the prior work.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies mechanism design problem under multi-armed bandit framework. The authors analytically derive a class of optimal solutions for such an LP that gives mechanisms achieving standard properties of efficiency, incentive compatibility, strong budget balance (SBB), and individual rationality (IR), where SBB and IR are satisfied in expectation.

### Strengths
1. The paper is well written and the theoretical results appear to be correct.
2. The paper improves the previous results in Osogami [2023].
3. The paper proposes numerical experiments to show the advantages of their designs.


Osogami [2023]: Takayuki Osogami, Segev Wasserkrug, and Elisheva S. Shamash. Learning efficient truthful mechanisms for trading networks.

### Weaknesses
1. I hold reservations about the contributions in the paper. In Section 3, the authors introduce four properties that the mechanism needs to satisfy: Dominant Strategy Incentive Compatibility (DSIC),  Decision Efficiency (DE), $\theta$-IR, and $\beta$-WBB/SBB. Such properties should be the key challenges in the mechanism design. However, as the authors stated, directly using the VCG mechanism can satisfy the first two properties. Furthermore, regarding the other two properties, they can be represented as two linear constraints of the optimization problem. In this regard, in Section 5, the authors are essentially stating the fact "LP has a solution only when the feasible region of the constraints is non-empty", which is really trivial. The authors claim to analytically solve the LP, but the core challenge of mechanism design lies in formulating the correct constraints and objective, not in solving a standard LP. The paper does not address the fundamental difficulty of choosing the right constraints to achieve the desired mechanism properties. The analytical solution, while technically correct, does not offer significant insight into the underlying mechanism design problem.

2. Similar to the first point, the method described by the authors in the Section 6 is essentially just the basic mean estimation of each arm's reward in stochastic MAB. While the authors claim a specific sample complexity, the novelty of this result is not clear. The core challenge in MAB is often the exploration-exploitation trade-off, which is not addressed in this paper. The paper seems to focus on a simplified setting where the mean reward is estimated independently for each arm, which is not a novel contribution in the MAB literature. The paper does not address the core challenges of MAB, such as dealing with non-stationary environments or delayed feedback.

3. The title of the paper is "Mechanism design with multi-armed bandit". However, in Section 3, the authors do not introduce any information regarding MAB. The connection between the mechanism design problem and the MAB framework is not established until Section 6, making the title misleading. The paper should either integrate the MAB concepts earlier or change the title to better reflect the content.

4. In Section 3, the authors assume that the types are generated from a fixed distribution. However, in Section 6, the authors state that the algorithm can access to an arbitrary size of the sample that is independent and identically distributed (i.i.d.) according to $P(\cdots|t_n)$ for any $t_n$. These two statements seem to conflict. The assumption of a fixed distribution for types in Section 3 seems to contradict the i.i.d. sampling from conditional distributions in Section 6. This inconsistency needs to be clarified.

### Questions
1. See weakness.

2. Prior to line 346, the paper does not mention MAB at all. Are the authors assuming that $ t_n \in [K] $ for all $n\in [N]$ here?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies automated mechanism design. First, a class of optimal solutions is derived that requires an exponentially smaller number of essential variables than the previous version of linear programming. To resolve the computational issue, a connection is drawn towards best mean reward identification in MAB. Then, provably efficient design to perform best mean reward identification is provided, which is further plugged back in the original mechanism design problem.

### Strengths
- The automated mechanism design is an interesting problem. While I do not have exact background in this direction, I believe the efforts provided in this work are of relevance and importance to the community.

- The connection from mechanism design to multi-armed bandits is inspiring. With my background in MAB, I largely appreciate such intersection that leverages MAB techniques to faciliate other domains.

- The overall presentation and writing is clear. It has been a smooth reviewing experience for me.

### Weaknesses
 - As I do not have a strong background in mechanism design, I would leave the further judgement of the significance and novelty of this part to other reviewers.

- For the MAB part, while the connection is interesting, I found the adopted technique is a bit straightforward. In particular, while best mean identification (BMI) and best arm identification (BAI) have their differences (e.g., the example in line 380), the upper bound is obtained in Theorem 1 is from an algorithm that perform BAI first while following up with additional samples to do BMI. I, in general, have doubts that this can be done in a more efficient way.

### Questions
- I would love to hear the author's opinion on the novelty of the BME design in this work. I understand that it serves as a tool for the overall mechanism design; thus it is acceptable if the novelty of this part is limited (in that case, I might need to rely on other reviewers to get an assessment for the novelty in mechanism design).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies how to solve an LP for mechanism design. It first formulates this LP, which can satisfy four conditions, and then illustrates that the solution of this LP enjoys an exponentially smaller variable size. Then, to approximate the solution, the paper proposes to use the MAB algorithm and shows that this approximation is asymptotic optimal. Numerical simulations are also reported.

### Strengths
1. The numerical simulation section is designed to verify several theoretical results, which are good paper complements.

### Weaknesses
1. Unclear contribution. Although the paper provides an approach with computational efficiency, the LP studied in this paper differs from and looks more accessible than the prior work (Osogami et al., 2023). So, it is hard to evaluate this paper's contribution from the aspects of significance and methodology. It would be helpful if the author could discuss the technical challenges they encountered in this paper. 
2. The theoretical results' organization is not easy to follow. This is a theoretical paper, providing a lot of lemmas and corollaries in Sections 5 and 6, where the essential parts are. However, the authors should put more effort into revising the presentations in these two sections. For example, in Section 5, the Lemmas 1 and 2 composes the Corollary 1. Why not directly give Corollary 1 and move Lemmas 1 and 2 to the appendix? This could help the reader quickly understand the meat of this paper.
Another example is that Corollaries 3, 4, and 5 are all on different conditions; why not just have one corollary with three bullets? For Section 6, Lemmas 4 and 5 are components to support Theorem 1. Why not use a proof sketch to posit Lemmas 4 and 5 so that readers familiar with these materials can directly skip them?

### Questions
### Minor Comments

- Line 170, notation $\mathcal N=[1,N]$ is confusing; how about $\{1,2,\dots,N\}$?

### Soundness
3

### Presentation
2

### Contribution
2
