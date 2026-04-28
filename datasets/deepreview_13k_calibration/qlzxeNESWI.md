# Bandits with Anytime Knapsacks

- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
We consider bandits with anytime knapsacks (BwAK), a novel version of the BwK problem where there is an anytime cost constraint instead of a total cost budget. This problem setting introduces additional complexities as it mandates adherence to the constraint throughout the decision-making process. We propose SUAK, an algorithm that utilizes upper confidence bounds to identify the optimal mixture of arms while maintaining a balance between exploration and exploitation. SUAK is an adaptive algorithm that strategically utilizes the available budget in each round in the decision-making process and skips a round when it is possible to violate the anytime cost constraint. In particular, SUAK slightly under-utilizes the available cost budget to reduce the need for skipping rounds. We show that SUAK attains the same problem-dependent regret upper bound of $ O(K \log T)$ established in prior work under the simpler BwK framework. Finally, we provide simulations to verify the utility of SUAK in practical settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies a version of stochastic Bandit with knapsack when the budget constraint has to be respected at each time step. In particular, the average budget spent in $t$ iterations has to be at most $B \cdot T/t$. 

The authors construct a learning algorithm, based on UCB methods, that provides instance-dependent regret bound with respect to the best fixed feasible distribution in hindsight. This learning algorithm performs empirically better than the trivial algorithm that simply runs any BwK algorithm and skips rounds every time the anytime constraint may be violated.

### Strengths
Bandits with knapsack is a relevant topic for ICLR. The paper is fairly well written, and the authors made an effort to address the obvious questions concerning their model.

### Weaknesses
Although somewhat natural, the idea of studying anytime constraints is pretty incremental with respect to previous work. I am not saying that the problem is immediately solvable by algorithms in the literature, but the algorithmic approach, i.e., “skipping rounds where the constraints may be violated + underspend a bit to minimize skips” is somewhat natural. 

The authors did address the natural question regarding standard algorithms complemented with a skipping strategy (see Section 3.1.), but they only analyze empirically a single algorithm. It would have been more convincing to prove that any non-anytime knapsack algorithm would fail if equipped with the extra skips. Moreover, it is not clear whether such algorithms would still enjoy the instance-independent $\sqrt T$ regret bound. 

Another downside of the paper is that the results are difficult to parse, given the abundance of instance-dependent parameters. Moreover, assumption 2 is not entirely motivated. Once we know $\omega$, then setting the underspending parameter is easy.

Finally, the comparison with the “replenishment” literature is not very satisfactory. The main claim is that the algorithms in that line of work do not contemplate the possibility of starting with $0$ budget. A natural fix there would be to wait for some initial rounds to build up some budget. Second, it is incorrect that \emph{only positive drift (replenishment of the resource) is considered} by Bernasconi et al. From my understanding they only require the existence of a void action that replenish the budget, which may be equivalent to the skipping action in this paper. Overall, a more comprehensive comparison is due.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the problem the problem of bandit with anytime knapsack, meaning that the knapsack constraint needs to be satisfied at all times and not only overall.

### Strengths
The paper is clearly written and easy to digest. The bandit with knapsack framework is interesting and this paper proposes a new model.

### Weaknesses
My main issue is understanding the connection with prior literature. I strongly believe that there are easy reductions from existing works (admittedly very recent) that can obtain the same results as your algorithm.

For example, take any algorithm that satisfies the constraints in high probability apart from O(sqrt(T)) violation (at any time!). Why can't you instantiate an instance of your problem with B-sqrt(T) initial budget and use any of these algorithms? Also, I'm not convinced that the skipping mechanism is not implicitly embedded in some of the existing works. In BwK you always have a default option with zero cost and zero reward, however, in more recent generalizations of the problem (usually called bandits with constraints [1,2,3]), the assumption is written slightly differently as the existence of a strictly feasible action. 

I do not think this is a fundamental problem as these works are very recent. However, a real detailed discussion of the technical differences is necessary, in my opinion.

### Questions
What are the technical reasons why the problem presented in this paper cannot be reduced to the more recent works on bandits with constraints, which, in the stochastic setting, provide small constraint violations?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work considers bandits with anytime knapsacks (BwAK), where there is an anytime cost constraint instead of a total cost budget. The authors propose a new algorithm SUAK that attains the instance-dependent regret upper bound of $O(K\ln T)$ established in prior work under the BwK framework. Numerical simulations are provided to verify the performance of SUAK.

### Strengths
- The paper is relatively easy to follow. Writing is mostly clear.
- The model considered is simple yet interesting and important. It has not been well studied in previous work.
- The analysis is largely sound and rigorous.

### Weaknesses
 - Algorithm design components and novelty need further investigation.
- Assumptions might be too strong and more results might be needed to gain deeper understanding.
- Experiment details need clarification.
- Proof requires great polishing.

See Questions for details.

### Questions
1. SUAK Line 32: "+" should be "-"? Line 240 "The main objective of this skipping mechanism is to decouple the skips ... in practice this skipping mechanism can be ignored". Can you provide more elaboration? Since in practice it can be skipped, can you provide more formal evidence supporting the argument?
2. I am a bit confused about the algorithm design as well as the technical novelty in SUAK compared to Algorithm 3 in Kumar & Kleinberg (2022). I know the setting is a bit different, but it seems the design principle is similar especially on the "under-utilization" principle. I also want to mention another related work [1], where the authors consider an online knapsack problem with random budget replenishment (there is also an anytime budget constraint). In their setting the decision maker can only accept/reject a random cost (can be negative), and so there is no control over which "arm" to be pulled. However, the $\ln T$ buffer idea also appears (although in their setting the fluid benchmark can be too loose and different types of costs require different levels of buffer). Please provide more discussions if possible.
3. Assumption 1 and 2 implies that the decision maker has prior access on a very small $\omega \leq \delta$. It is claimed that it is necessary for meeting the anytime constraint. I think the assumption is somewhat restrictive. Can you provide more explanation why this is necessary and whether it can be relaxed?
4. The current work obtains an instance-dependent $O(\ln T)$ regret under some strong non-degeneracy assumptions as well as knowing $\omega$. What about the worst-case scenario? Is it possible to show that a policy such as OPS has a $O(\sqrt T)$ regret? Clearly OPS does not require the knowledge of $\omega$. I know generalizing to the multi-dimensional setting as in Kumar & Kleinberg (2022) can be challenging, but I think more results are needed to gain deeper understanding on the problem.
5. The paper gives $2$ simulation experiments. In the first one OPS performs much worse, while in the second one OPS performs fairly well. Why is this happening? Is it because there is some intrinsic structural difference between the two instances? Is it the case that the instance-dependent metrics $\delta$ and $\Delta$ are taking effects? Also, how do you decide $\omega$ in SUAK?
7. Technical questions. I strongly suggest the authors polish the proof. I believe the general framework is correct, but it seems there exists some confusing parts. Some examples are shown below:
 - Line 1086 - 1094: I do not think the statement is rigorous.
 - Line 1100: "≥" should be "≤"？
 - Line 1183 - 1190: I do not quite understand the proof.
 - Line 1197 - 1205: Somewhat unclear.
 - Line 1269: How do you get this from Line 1265 - 1267? Why $N_i^s(T)$ is an expected number while $N_i(T)$ is a random number?

[1] Bayesian Online Multiple Testing: A Resource Allocation Approach. arXiv preprint arXiv:2402.11425.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies an interesting variant of the bandits with knapsack problem, namely the bandits with anytime knapsacks. The difference is that now the constraint is imposed for any period $t$. That is, up to each period $t$, the average cost should be upper bounded by a threshold. Though the formulation is different from the bandits with knapsack problems, luckily, they admit the same linear relaxation. Thus, previous methods for bandits with knapsack problems could be modified and applied here. However, forcing the online algorithm to satisfy the anytime constraint would require additional new elements. The paper develops a novel algorithm with a carefully designed UCB principles. Further combining with a resolving LP techniques, the paper is able to show that their algorithm achieves a problem-dependent $O(\log T)$ regret. This is a new result for bandits with anytime knapsack problem and the algorithm in the paper is also new. The paper finally conducts numerical experiments to show that their algorithm performs well in practice.

### Strengths
1. The theoretical result is strong in that a problem-dependent $O(\log T)$ regret has been derived, in contrast to the worst-case $O(\sqrt{T})$ regret usually seen in the literature.

2. The paper conducts numerical experiments of their algorithms and delivers convincing results.

### Weaknesses
1. The paper only considers a setting where there is a one-dimensional cost. That is, for each period $t$, there is only one cost constraint to be satisfied. However, in the classical bandits with knapsack problems, there are usually multiple cost constraints to be satisfied.


### Questions
1. The paper mentions the non-degeneracy issue. However, the cost constraint considered in the paper is one-dimensional. Is non-degeneracy still an issue when the constraint is one-dimensional? Could the methods developed in the paper be further generalized to handle multi-dimensional cost constraints?

### Soundness
3

### Presentation
2

### Contribution
3
