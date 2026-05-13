# Stateless Mean-Field Games: A Framework for Independent Learning with Large Populations

- Decision: Reject
- Scores: 3, 8, 5

## Abstract
Competitive games played by thousands or even millions of players are omnipresent in the real world, for instance in transportation, communications, or computer networks. However, learning in such large-scale multi-agent settings is known to be challenging due to the so-called "curse of many agents". In order to tackle large population independent learning in a general class of such problems, we formulate and analyze the Stateless Mean-Field Game (SMFG): we show that SMFG is a relevant and powerful special case of certain mean-field game formulations and a generalization of other interaction models. Furthermore, we show that SMFG can model many real-world interactions, and we prove explicit finite sample complexity guarantees with independent learning under different feedback models with repeated play. Theoretically, we contribute techniques from variational inequality (VI) literature to analyze independent learning by showing that SMFG is a VI problem at the infinite agent limit. We formulate learning and exploration algorithms which converge efficiently to approximate Nash equilibria even with finitely many agents. Finally, we validate our theoretical results in numerical examples as well as in the real-world problems of city traffic and network access.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a generalization of congestion games where cost functions need only be monotone (rather than monotone increasing), which they term a "stateless mean-field game". Since the game can be written as a VI with a monotone operator, they propose the use of (what is effectively) L2-regularized gradient descent as an uncoupled game dynamic to recover a solution. The experiments of the paper implement the proposed L2-regularized GD and claim an empirical improvement over unregularized GD.

### Strengths
The Tor network access experiment (which I read to be a live real-world experiment using real Tor latencies) is a very creative and interesting experiment design that I have not seen before. The empirical results that online mirror descent does not perform as well as L2 regularized online mirror descent is not surprising or completely new (see below) but real-world experiments comparing the efficacy of different game dynamics is always interesting and valuable. The paper is also generally well-written.

### Weaknesses
It seems that there might be some significant overlap between the theoretical claims of the paper and what is already known about congestion games, variational inequalities, and game dynamics. First, approaching congestion games with variational inequalities instead of explicitly exploiting game potentials (e.g. via best response-dynamics) is somewhat standard; the fact that such approaches still work when one relaxes cost functions from being monotone increasing to just monotone is a fairly direct implication---although this is assuming that my understanding that SMFG = Congestion Game but with both monotone increasing/decreasing costs is correct.
One of the main technical contributions claimed by the paper is that, instead of running (what is effectively) gradient descent, the paper proposes to run (what is effectively) L2-regularized gradient descent. It seems there were three claimed benefits: 1) it makes the problem strongly monotone (to avoid needing the extragradient method), 2) it helps with stochasticity (convergence despite noise seems to just follow from normal stochastic approximation though and nothing to do with the regularization in particular), and 3) it allows them to implement the algorithm in a decentralized way across the players. The 3rd point seems to be the primary emphasis. However, I don't believe this is a new observation: a standard way of learning equilibria in online learnable (such as monotone) setups is no-regret dynamics. As a side note, Theorem 1 should probably state the dependence on $K$ instead of hiding it as a constant---it seems like the correct dependence should be $\log(K)$ at least in the full information setting (e.g. using exponentiated gradient descent).

### Questions
See above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To deal with the challenges of space complexity of multiagent RL, they propose stateless mean field games. They are able to use sampling algorithms to find approximate Nash equilibrium sufficiently quick.

### Strengths
They propose a (seemingly) novel way to deal with massive state space. The paper is well written.

### Weaknesses
It seems they find an approximate nash equilibrium rather than an exact one. They also impose lipschitz and monotonous payoffs as their restrictions. However they make a good case that these assumptions are not too limiting.

### Questions
Is finding a exact nash equilibrium possible with this methodology?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the so-called stateless mean-field games. It considers the finite-agent cases, and the authors include two information feedback settings: full-feedback and bandit feedback. For each of the settings, the authors propose efficient algorithms to learn the Nash equilibrium of the game. The convergence rates of the algorithms and the numerical validations are provided.

### Strengths
This paper focuses on a new finite-agent setting for mean-field games. The work proposes independent learning algorithms with the performance guarantees to learn the Nash equilibrium. In addition, the numerical results are provided to verify the theoretical findings.

### Weaknesses
After reading the paper, some of my concerns are not addressed:

1. The results in Theorems 1 and 2 discount the effect of mean-field approximation and need more explanations. In my personal understanding, the mean-field approximation is implemented to avoid the dependency of the number of agents $N$ in sample complexity (I understand that in the finite-player setting, the complexity can scale as $\log N$ due to for example the union bound in concentrations). However, Theorems 1 and 2 suggest that $T$ should at least grow as $poly(N)$ for a meaningful result. This implies that the results in this paper cannot be extended to the setting $N=\infty$ considered in the previous papers, e.g., [1]. This may suggest that the algorithms proposed in this paper is not suitable for the large population problem. In addition, the justification for this polynomial dependency by the comparison with [2] below Corollary 2 may be unreasonable, since mean-field approximation is not considered in [2]. Specifically, the work [2] deals with a multi-armed bandit setting, where each agent's reward is only affected by whether it collides with other agents on the same arm. This is a much simpler setting than the general payoff function considered in this paper, which depends on the empirical distribution of all agents' actions. Therefore, the comparison is not well justified.

2. The bias term $O(1/\sqrt{N})$ needs more discussion. Although the authors explain that this potentially comes from the independent learning setting, such a term does not appear in other independent learning settings, e.g., the potential games and two-player zero-sum games. I do not fully understand why there is a bias term in the problem setting considered in this paper. It is unclear if this bias is inherent to the problem formulation or a result of the analysis technique. The authors should provide more insight into the source of this bias term, and whether it can be reduced or eliminated by using different algorithmic approaches.

3. Based on the above points, I am not sure whether these concerns arise from the loose analysis of the upper bounds or from the problem formulation itself. It will be helpful to derive the lower bound for these two concerns.

### Questions
The questions are the same as the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
