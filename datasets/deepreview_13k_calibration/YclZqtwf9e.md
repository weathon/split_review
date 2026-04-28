# Slingshot Perturbation to Learning in Monotone Games

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
This paper addresses the problem of learning Nash equilibria in *monotone games* where the gradient of the payoff functions is monotone in the strategy profile space, potentially containing additive noise. The optimistic family of learning algorithms, exemplified by optimistic Follow-the-Regularized-Leader and optimistic Mirror Descent, successfully achieves last-iterate convergence in scenarios devoid of noise, leading the dynamics to a Nash equilibrium. A recent emerging trend underscores the promise of the perturbation approach, where payoff functions are perturbed based on the distance from an anchoring, or *slingshot*, strategy. In response, we first establish a unified framework for learning equilibria in monotone games, accommodating both full and noisy feedback. Second, we construct the convergence rates toward an approximated equilibrium, irrespective of noise presence. Thirdly, we introduce a twist by updating the slingshot strategy, anchoring the current strategy at finite intervals. This innovation empowers us to identify the exact Nash equilibrium of the underlying game with guaranteed rates. The proposed framework is all-encompassing, integrating existing payoff-perturbed algorithms. Finally, empirical demonstrations affirm that our algorithms, grounded in this framework, exhibit significantly accelerated convergence.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies last-iterate convergence to NE in monotone games, under full but noisy feedback. The techniques used focus on regularising the payoffs by a reference strategy named "slingshot strategy". The slingshot is then updated as the current maintained strategy at exponential intervals and thus converges last-iterate to the true NE of the game rater then to the perturbed one.

### Strengths
The per studies the problem of finding a NE under perturbed feedbacks in an important subclass of games, which are monotone games. This class includes many important examples and thus is an important achievement. The paper is fairly well written and the results seems correct (although not surprising). The topic of the per is in line with the interests of the ICLR community

### Weaknesses
My first concern is with the motivation for the work. The authors rarely mention way one should consider full but noisy feedback. You only have full feedback when you posses a great understanding of the environment, but then noise wouldn't make much sense. I would get is you considered noisy bandit feedback, but the authors do not seem to discuss the problem.
Also, it is not clear if noise ruins the guarantees of the algorithms already present in the literature. Usually no-regret algorithm still converge in full feedback, to some sort of equilibria even in the presence of noisy feedback as long as the loss used are unbiased. The authors should discuss better why existing techniques fail, why now they only fail in terms of experimental evaluation.

My second, and far more pressing, concern is on the technical innovation of the work. The "slingshot" perturbation was studied extensively in recent papers, as also noted by the authors (Sokota et al. 2023, Bernasconi et al. 2022, Perlolat at al. 2021, Liu et al. 2023).
The main technical contribution of the paper is the introduction of the noise into the feedback, but it not clearly well explained why this is challenging or important and what technical novelty does the problem require.

Moreover, I'm puzzled about some results about section 5.  In particular how is it possible to have some meaningful guarantees as the gradient of $G(\pi,\sigma)$ can be arbitrary large in general. For example if $\sigma$ is close to the boundary and $G$ is the KL divergence, probably the results of section 5 only require very nice properties of $G$ and thus it limits its applicability. 

Is also not clear to me why you do the slingshot update. You give guarantees on the exploitability of the last iterate strategy, but not on the convergence rate to the strategy itself, as you do in theorem 4.2 and 4.10 for approximate nash.

### Questions
1) Way should one care about full but noisy feedback?
2) What are the new techniques introduced here that are designed to help with noisy feedback?
3) Way don't you consider dynamic $\mu=\mu_k$ in section 5? Diminishing it every $T_\sigma$ turns would help as long as you can bound the distance (with either $G$ of $D$) between $\pi^{\mu_k}$ and $\pi^{\mu_{k+1}}$. This is a natural question that should give asymptotic rates to exact nash.
4) Do you require $G$ to have bounded gradient in section 5? Otherwise I think you cannot use some statements such as theorem 4.2 and 4.9 in section 5.
5) Have you considered using smaller and smaller values of $\mu=\mu_k$? This would create a sequence of NE equilibria that converge to the exact one. Similar techniques have been used in Bernasconi et al. 2022 and Liu et al. 2023, and I think should be discussed.
6) Way MWU does not converge in figure 1, without noise?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of computing Nash equilibria in monotone games. Monotone games are of utter importance in the (algorithmic) game theory and algorithms that can be executed in a rather decentralized manner and have provable efficient convergence rates are always sought after.

In particular, this work unifies pre-existing literature that relies on perturbing agents' payoffs and develops a general meta-algorithm, "FTRL with Slingshot Perturbation". This framework can retrieve multiple algorithms proposed in recent works, e.g., [1], [2], [3].

The algorithm (in the full-information setting) works as follows:
* A regularization function, $\psi$, and a regularization parameter, $\mu$, are selected. Every player initializes a "slingshot" strategy.
* For a fixed number of steps, players run an instance of the FTRL algorithm, with the spin-off of perturbing their utility gradient by adding the gradient of the Bregman distance generated by $\psi$ times the parameter $\mu$.
* Every player updates their "slingshot strategy" and returns to the second step.

The guarantees of this algorithm are:
* an exponential convergence rate of the sequence of strategies to the unique Nash equilibrium of the perturbed problem for a fixed slingshot strategy 
* the convergence of the slingshot strategies (i.e., the strategies as well) to an approximate equilibrium.

Further, if the algorithm is run for an infinite number of steps, it is guaranteed to reach an exact Nash equilibrium of the unperturbed game.

The results are also extended for a meta-algorithm where Mirror Descent is used in place of FTRL.

[1] Tuyls, K., Hoen, P.J.T. and Vanschoenwinkel, B., 2006. An evolutionary dynamical analysis of multi-agent learning in iterated games. 
[2] Perolat, J., Munos, R., Lespiau, J.B., Omidshafiei, S., Rowland, M., Ortega, P., Burch, N., Anthony, T., Balduzzi, D., De Vylder, B. and Piliouras, G., 2021, July. From Poincaré recurrence to convergence in imperfect information games: Finding equilibrium via regularization.
[3] Abe, Kenshi, Sakamoto, Mitsuki, Iwasaki Atsushi, 2022. Mutation-driven follow the regularized leader
for last-iterate convergence in zero-sum games.

### Strengths
* The paper unifies existing work and its main claims are quite general in their statement.
* The idea of the FTRL-slingshot-perturbation algorithm is natural and elegant.
* The paper is more or less self-contained.
* The authors establish convergence rates for both the full information and the noisy information feedback setting.
* The algorithm assets a simplified analysis of convergence.

### Weaknesses
 * At first glance, the claims about "exact Nash equilibrium" computation can seem misleading.
* The algorithm is not fully decentralized. It could be possible to discuss whether the process would converge when the frequency of update of the slingshot strategy and $\mu$ varied across players.
* There already exist algorithms with last-iterate convergence and no-regret guarantees for monotone games. This work does not have any no-regret guarantees nor does it try to consider more decentralized settings (i.e., players have to change their slingshot strategy at the same time, and $\mu$ is the same for everyone as well as $\psi$ --- at least according to my understanding)

### Questions
* Do you think that the slingshot perturbation framework achieves no adversarial regret?
* What would happen if a fixed number of agents did not update their slingshot strategy every time or every player had their own frequency of updating the slingshot strategy?
* Would it be possible to tune $\mu$ as well to achieve better convergence rates?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors studied equilibrium computation in monotone games by addressing the cases where the feedback can be contaminated by some noise through the perturbation of payoffs. To this end, they focused on perturbing the payoffs based on the distance from a slingshot strategy. They characterized the convergence rate toward a near equilibrium. They proposed updating the slingshot strategy to converge exact equilibrium with last-iterate convergence guarantees.

### Strengths
- The entire paper (including the Appendix) is well-written.
- The balance between the preliminary information and new content is very good, which makes the paper accessible.
- Addressing noisy feedback is of interest.
- Updating the slingshot strategy for exact equilibrium convergence is interesting.

### Weaknesses
 - In-line mathematical expressions makes the paper difficult to read.

### Questions
No clarification is needed.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper gives a unified framework to construct uncoupled learning algorithms that can provably converge to Nash equilibria in monotone games, for the full information feedback model and the noisy feedback model. The central idea of this framework is to introduce a slingshot strategy, so when doing (regularized) gradient descent, one does not only consider the gradient of the payoff function but also considers the gradient of the distance $G(\pi_i, \sigma_i)$ from the current strategy $\pi_i$ to the slingshot strategy $\sigma_i$. When the slingshot strategy is fixed, the algorithm can find an approximate equilibria, depending on how close $\sigma_i$ is to a Nash equilibrium. By updating the slingshot strategy periodically, the algorithm can then converge to an exact Nash equilibrium. In particular, if $G$ is the sqaured $\ell^2$-distance, then the convergence rate is $O(1/\sqrt T)$ with full information feedback and $O(T^{-1/10})$ with noisy feedback.

### Strengths
(1) The problem studied -- last iterate convergence to Nash equilibria via uncoupled learning in games -- is doubtless important.

(2) The framework, techniques, and result of this paper are very general: One can use any function $G$ to measure the distance from a strategy $\pi_i$ to the slingshot strategy $\sigma_i$, as long as $G$ is smooth and strongly convex. One can use any standard regularizer $\psi$. And the result holds for any monotone games. This is a nice combination and abstraction of the techniques in a wide range of previous works.

(3) Experimental results support the theoretical claims.

(4) The writing is really clear.

### Weaknesses
 (1) The authors didn't give any impossibility results (lower bounds) on the convergence rate. I would suggest the authors to present some lower bound results to contrast with the upper bound results they give, even if the lower bounds can be from previous work.

(2) The $O(T^{-1/10})$ bound for finding exact Nash equilibrium in the noisy feedback case (Theorem 5.2) does not seem to be tight. It would be great if the authors can provide some discussion on the tightness of this result.

(3) While the convergence rates to approximate equilibria (Section 4) are presented for any general $G$ functions, the convergence rates for exact Nash equilibria (Section 5) are only for $G$ being the squared $\ell^2$-distance. The authors say that Theorem G.1 and G.2 are for other $G$ functions, but they are only asymptotic results, with no quantitative convergence rates. Given that the main contribution of this paper is a unified framework, I feel that a quantitative convergence rate for general $G$ function is needed.

### Questions
**Questions:**

(Q1) The cited related work [Cai-Luo-Wei-Zheng, 2023, Uncoupled and Convergent Learning in Two-Player Zero-Sum Markov Games] shows that the Nash equilibria of 2-player zero-sum games can be found by an uncoupled learning algorithm with bandit feedback with $O(T^{-1/8})$ convegence rate. This is better than the $O(T^{-1/10})$ bound in this paper. Of course I'm not saying [Cai-Luo-Wei-Zheng, 2023] outperforms this paper, because this paper's result holds for more general monotone games. But I wonder whether [Cai-Luo-Wei-Zheng, 2023]'s ideas can be used to improve this paper's result? In particular, improving the convergence rate or proving results for the bandit feedback case?

(Q2) Do the authors have any responses to the 3 weaknesses I mentioned above?

**Suggestion:**

(S1) Page 3, "Other notations" paragraph: "$\langle \nabla \psi(\pi_i'), \pi - \pi_i'\rangle$" should be "$\langle \nabla \psi(\pi_i'), \pi_i - \pi_i'\rangle$"

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
