# On Stochastic Contextual Bandits with Knapsacks in Small Budget Regime

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
This paper studies stochastic contextual bandits with knapsack constraints (CBwK), where a learner observes a context, takes an action, receives a reward, and incurs a vector of costs at every round. The learner aims to maximize the cumulative rewards across $T$ rounds under the knapsack constraints with an initial budget of $B$. We study CBwK in the small budget regime where the budget $B = \Omega(\sqrt{T})$
and propose an Adaptive and Universal Primal--Dual algorithm (AUPD) that achieves strong regret performance: 
i) AUPD achieves $\tilde{O}((1 + \frac{\nu^*}{\delta b})\sqrt{T})$ regret under the strict feasibility assumption without any prior information, matching the best-known bounds;
ii) AUPD achieves $\tilde{O}(\sqrt{T}+ \frac{\nu^*}{\sqrt{b}}T^{\frac{3}{4}})$ regret without strict feasibility assumption, 
which, to the best of our knowledge, is the first result in the literature. Here, the parameter $\nu^*$ represents the optimal average reward; $b=B/T$ is the average budget and $\delta b$ is the feasibility/safety margin.
We establish these strong results through the adaptive budget-aware design, which effectively balances reward maximization and budget consumption. We provide a new perspective on analyzing budget consumption using the Lyapunov drift method, along with a refined analysis of its cumulative variance. Our theory is further supported by experiments conducted on a large-scale dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the contextual bandits with knapsack problem under the small budget scenario. Previous research needs to know the safety margin of the budget constraint for their algorithms. This work gives an algorithm achieving the best known regret without knowledge of the safety margin. Furthermore, the algorithm can achieve sub-linear regret with not-strictly-feasible constraints in some cases.

### Strengths
This paper gives a good contribution to a natural problem. The contextual bandit with small budget knapsacks is a natural problem. Existing research requires knowledge about the safety margin, which is hard to know. This paper gets rid of this demanding requirement. Furthermore, this paper gives the first result in the not-strictly-feasible case. 

This paper is very well written. It is really easy to follow the paper. Everything is clearly defined and stated.

Overall, I think this is a well written paper, makes a good contribution to a natural problem. I am happy to see it published.

### Weaknesses
This paper has few weaknesses; I would only suggest that the authors further discuss the relationship between contextual bandits with knapsack and standard bandits with knapsack, and provide the existing lower bound. Please see the specific questions below.

Question 1: What is the relationship between contextual bandits with knapsack and standard bandits with knapsack? Although we are working with contextual bandits, the final result does not rely on the context numbers. Is this due to the learning oracle? Given a learning oracle, are there any technical differences between this approach and the algorithms for standard bandits with knapsack based on UCB and primal-dual methods?

Question 2: What is the existing lower bound for this problem? How large is the gap between the lower bound and the existing upper bound? Please discuss this point.

### Questions
Question 1: What is the relationship between contextual bandits with knapsack and standard bandits with knapsack? Although we are working with contextual bandits, the final result does not rely on the context numbers. Is this due to the learning oracle? Given a learning oracle, are there any technical differences between this approach and the algorithms for standard bandits with knapsack based on UCB and primal-dual methods? 

Question 2: What is the existing lower bound for this problem? How large is the gap between the lower bound and the existing upper bound? Please discuss this point.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies contextual bandit with knapsack in the small budget regime (B=o(T), B=\Omega(T)).
The paper provides an algorithm which achieves O(sqrt(T)/(d*B/T)) without knowing "slater" action d and O(T^{3/4}/sqrt(B/T)) without strictly feasibility (d=0).

### Strengths
The setting studied is interesting and not trivial and leads to intriguing scientific questions.

### Weaknesses
The paper is a bit difficult to read, and I think I could benefit from being inserted in a larger context with respect to prior/concurrent literature. 
For example, the recent literature that considers bandits with constraints (of which bwk is a special case) has much more relevancy than what the authors seem to realize. In particular, I'm referring to

[1] Raunak Kumar and Robert Kleinberg. Non-monotonic resource utilization in the bandits with
knapsacks problem. In Advances in Neural Information Processing Systems (NeurIPS), 2022.
[2] Bernasconi, Martino, Matteo Castiglioni, and Andrea Celli. "No-Regret is not enough! Bandits with General Constraints through Adaptive Regret Minimization."
[3] Slivkins, Aleksandrs, Karthik Abinav Sankararaman, and Dylan J. Foster. "Contextual bandits with packing and covering constraints: A modular lagrangian approach via regression." The Thirty Sixth Annual Conference on Learning Theory. PMLR, 2023.
[4] Bernasconi, Martino, et al. "Bandits with Replenishable Knapsacks: the Best of both Worlds."
The Twelfth International Conference on Learning Representations.

The paper lacks a clear explanation of how the proposed algorithm handles the small budget regime differently from the large budget one. The theoretical results, while presented, lack a discussion of their practical implications. Specifically, the regret bound of  $O(\sqrt{T} + \frac{\nu^*}{\sqrt{b}} T^{3/4})$ without strict feasibility becomes linear (and thus meaningless) when $B = \sqrt{T}$. This crucial point is not adequately addressed, and the paper would benefit from a more thorough analysis of the trade-off between the budget $B$ and the regret $R_T$, particularly in the small budget regime. It is unclear how the algorithm adapts to different budget sizes, and a more detailed explanation of the algorithm's behavior across various budget scales is needed. The current presentation does not make it clear why existing techniques cannot be adapted to small budget settings and what are the specific technical hurdles.

### Questions
What are the technical challenges that prevent adapting existing techniques such as "Contextual bandits with packing and covering constraints: A modular lagrangian approach via regression" to this context? Is it true that the authors assume large budget, but it is not obvious that their framework cannot be used to solve the small budget case. At least this merits an explanation, which might also add relevancy to your technical contributions, which at the moment are not really highlighted.
When are your results meaningful? For example, if B=sqrt(T), then the results are linear and meaningless in the case of no strictly feasible. It would be helpful to plot/discuss a B=T^alpha vs R_T tradeoff as a function of alpha.
How do your algorithms really solves the small budget? I fail to understand how your algorithm behaves differently when B=sqrt(T) or B=\Theta(T).
What would happen if you used one of the existing algorithms that do not use knowledge of the later parameter and applied it to the small-budget case?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies the contextual bandits with knapsacks problem with a focus on when the budget is "small" (i.e., $B = \Omega(\sqrt{T})$). The authors present an algorithm with $\sqrt{T}$ regret under the strict feasibility assumption and $T^{\frac{3}{4}}$ regret without it. Notably, the algorithm does not need to know which of these two regimes it is in. The algorithm improves upon prior work by being a single-stage algorithm and by using the cumulative over-consumption of resources as a Lagrange multiplier.

### Strengths
* Contextual bandits with knapsacks (CBwK) is an important model of online decision-making with many applications. This paper advances our knowledge in this area by improving upon an important limitation in existing work, namely, considering the regime of $B = \Omega(\sqrt{T})$ with and without strict feasibility. Their regret bound for the setting without strict feasibility is also the first such result.
* The algorithm has some good features: it is simple and it does not need to know whether strict feasibility holds or not.
* The choice to use the cumulative over-consumption as a Lagrange multiplier is a natural and effective idea.

### Weaknesses
 * Overall, it's a well-written paper. But I would have loved to see some intuition behind the proofs of the lemmas in the main text. When I read through the proofs in the appendix, I followed the steps. But I still would have liked to see an explanation in words about the main ideas in the proof.
* In the three settings considered in the experiments, the proposed algorithm is strictly better than the alternatives in only 1 setting; it is roughly the same as PGD Adaptive in the other two settings. It would have been nice to see other settings in which the proposed algorithm is strictly better than the alternatives.


### Questions
Questions:
1. You claim that your algorithm is "budget-aware" because of the parameter $V = b \sqrt{T}$, as opposed to $V = \sqrt{T}$. I am wondering how crucial this choice is. Quantitatively, what would have been the regret bound had you chosen $V = \sqrt{T}$? Qualitatively, where does including $b$ in the parameter help you in the proof?
2. Why are the variables $Q_t^k$ called "virtual queues"? I'm trying to understand the motivation for this terminology and if there is a connection to literature on "virtual queues" that is helpful here.
3. I understand the technical details proof of Lemma 5, but can you provide some intuition for how Lemma 4 is helpful for proving Lemma 5?
4. Do you have thoughts on whether $T^{\frac{3}{4}}$ can be improved when strict feasibility does not hold?

Minor comments and typos:
1. Line 314: "is not necessary to hold" -> "does not necessarily hold".
2. Line 337: "provide detailed proof" -> "provide a detailed proof".
3. Equation 8: This is a very minor nitpick, but I personally find it easier to parse the statement when it's written in the format $\exists k$ s.t. {condition}.
4. Line 346: Should this be denoted $a^*_t$ instead of $a^*$ since a different action will be sampled in different rounds depending on the context? Also, "be the optimal action sampling from it" -> "optimal action sampled from it".
5. Line 363-364: What is $f$? Did you mean $r$?
6. Line 368: Regret($x_t, a$) has not been defined before. But I guess it means $r(x_t, a^*_t) - r(x_t, a)$?
7. Line 400-401: "against the average usage $t \times b$ for the round t" - Isn't the average usage $b$?
8. Line 418-419: This is a very minor nit, but I suggest rewording "we have established" to "we establish". When I first read this, I was wondering where this established in the paper so far. Then I read the full sentence and realized it is proved in the next lemma.
9. Line 483-484: Did you mean 1a instead of 1b?
10. Line 708-709: Should $c$ be $\check{c}$?
11. Line 981-982: It took me some time to understand what you meant by "divide both sides". It might be clearer to explicitly say that you divide both sides of the inequality inside the argmin.
12. In Section B.3.1, you use Assumption 3. Then you use the resulting inequality (16) in Section B.4 where you don't assume Assumption 3. My guess is that this is ok since Eq 16 has a $-Q \delta b$ term and you upper bound this by 0 in Section B.4? It might be good to be clear about this in Section B.3.1.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies stochastic contextual bandits with knapsack. In this model, at each round the learner observes a context before taking an action. The goal of the learner is to maximize its utility subject to a knapsack constraint. The paper presents an algorithm that guarantees an instance-dependent regret bound both with and without the strictly feasibility assumption. The paper provides meaningful guarantees even with budget $B=\Omega(\sqrt{T})$.

### Strengths
It is the first paper to work without knowing the safe margin or without a safe margin.

### Weaknesses
The improvements with respect to previous works are minimal, and it is not clear the importance and technical challenges in removing the assumptions in previous works. Indeed, the assumption of a cost 0 "do nothing" action is fairly natural.

The algorithm and the analysis look quite standard. Which are the technical difference and challenges with respect to previous works? Why is Lyapunov Drift more effective than previous approaches?

### Questions
The algorithm and the analysis look quite standard. Which are the technical difference and challenges with respect to previous works? Why is Lyapunov Drift more effective than previous approaches?

### Soundness
3

### Presentation
2

### Contribution
2
