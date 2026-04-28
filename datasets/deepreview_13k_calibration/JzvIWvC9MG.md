# Efficient Inverse Multiagent Learning

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 1, 8

## Abstract
In this paper, we study inverse game theory (resp. inverse multiagent learning) in
which the goal is to find parameters of a game’s payoff functions for which the
expected (resp. sampled) behavior is an equilibrium. We formulate these problems
as generative-adversarial (i.e., min-max) optimization problems, which we develop
polynomial-time algorithms to solve, the former of which relies on an exact first-
order oracle, and the latter, a stochastic one. We extend our approach to solve
inverse multiagent simulacral learning in polynomial time and number of samples.
In these problems, we seek a simulacrum, meaning parameters and an associated
equilibrium that replicate the given observations in expectation. We find that our
approach outperforms the widely-used ARIMA method in predicting prices in
Spanish electricity markets based on time-series data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a generative-adversarial (or min-max) characterization of the inverse game theory problem where a generator provides payoff parameters that minimize total regret, and a discriminator looks for action-profiles that maximize it. A min-max objective mimicking this two-player game is optimized to estimate the inverse equilibrium using gradient descent ascent algorithm (and other variations of it). It is further proposed that for games that satisfy certain assumptions guaranteeing convex-concavity of the objective, the algorithm converges in a number of iterations that are polynomial in the precision of the obtained inverse equilibrium. This formulation is further extended to give algorithms for multi-agent inverse reinforcement learning and multi-agent apprenticeship learning, accompanied by polynomial time (and space) convergence guarantees under appropriate assumptions. Experiments are conducted to identify categories of games for which the method is effective, and whether its usefulness goes beyond provided theoretical limits.

### Strengths
* An inverse game theoretic perspective to multi-agent inverse reinforcement learning is certainly a novel direction to approach the problem with. Backed by results in inverse game theory, this approach leads to algorithms with desirable convergence guarantees that prior work in multi-agent imitation learning does not provide.

* The low restrictiveness of the assumptions made allow for the framework to be effective on a vast majority of markov games, leading to useful and efficient solutions on a wide variety of multi-agent problems.

* While the paper focuses on the inverse nash equilibrium, the simplicity of the objective allows for easy extensions of the framework to alternative game theory solution concepts.

* All presented algorithms are succinct and easy to understand. Sufficient mathematical background is provided as and when necessary.

### Weaknesses
 * It would be helpful to expand on the proofs of theorems 6.1, 6.2, and 6.3 in the supplementary material. I know that a reference has been provided, but a slight explanation of the cited result and how it relates to the theorem in question would be nice.

* Although a comparison of the method has been shown with the ARIMA model on the spanish electricity market data, it would be beneficial to have a comparison with prior methods in inverse multi-agent reinforcement learning. Especially in terms of efficiency since it's one of the main points of the paper. The abstract says that the method outperforms other widely-used methods (plural), and we only get to see it being compared with one other model which is specific to time-series data. A more thorough experimental evaluation against state-of-the-art multi-agent inverse reinforcement learning methods is needed to substantiate the claims of superior performance, particularly in terms of computational efficiency.

* Some comparison/contextualization with prior work in multiagent inverse reinforcement learning would also be helpful. The current related works section is lacking a discussion of how this work fits into the existing literature on multi-agent inverse reinforcement learning, especially regarding approaches that also use adversarial or game-theoretic perspectives. Specifically, it would be beneficial to see a discussion of the similarities and differences in the problem formulation and solution techniques.

### Questions
What does the term $\psi(\pi, \rho; \theta)$ in the "Multiagent Apprenticeship Learning" section expand to? Cannot seem to find a definition anywhere.

Assuming that Algorithm 3 was used on the spanish electricity market data, how was the observation distribution specified?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied inverse game theory to find parameters of the payoff functions of the game. Polynomial time and sample efficient algorithms are provided and claimed.

### Strengths
1. This paper formulate the inverse game as an generative-adversarial optimization problem and provide polynomial time algorithms.

### Weaknesses
1. The proofs are not completed, e.g., I cannot find the proofs for Theorem 4.1 and Theorem 5.2.

2. The presentation can be further improved, e.g., more intuitions about the assumptions and theorems.

### Questions
1. See weaknesses.

2. Can you further polish the paper? Some typos: for example, in the fifth line of the abstract, should it be "to solve them"?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper formalizes the problem of inverse game-theory (determining
equilibrium strategies and associated game structure from historical play) as a
novel min-max optimization problem and solves it using a primal-dual gradient
method. This technique is deployed on a practical and interesting application
domain of market pricing dynamics.

### Strengths
The simple formulation of the set of inverse Nash equilibria (NE) as a min-max
game is elegant and appears to be original. If it is indeed original, for this
alone, the paper merits publication and should be highlighted.

The paper overall is well written and showcases immediate applications of the
proposed solution to an important and practical domain as a proof-of-concept. I
believe these results are significant and will be impactful.

### Weaknesses
As an easily rectified issue, Figure 1 could have been better represented by
plotting residuals over time or, by subsampling the data, plotting mean
residuals with error bars.

As a minor complaint, I do not prefer the language of "generative-adversarial"
(especially not in terms of a "discriminator"), even if this is the closest
analogy familiar to machine learning practitioners: This is a standard min-max
optimization problem that need not be wed to the ML setting.

### Questions
Remark 1 is indeed interesting, but it is not obvious. Did I miss an associated
proof or example?

Why was the proof of Theorem 3.2 omitted? Was it rephrased to appear as Theorem
6.1 in the supplementary material?  Establishing the convergence rates of
various algorithms is not my expertise, but the results seem reasonable,
especially given assumptions of convexity and Lipshitz smoothness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Game theory provides a structured approach to predicting outcomes of interactions between rational agents. Inverse game theory deals with situations where the players' behavioral models are unknown and aims to deduce the payoff functions that explain observed actions as equilibria. This paper presents a new approach for solving inverse equilibrium problems in a range of games, using generative adversarial optimization to match game-theoretic models to observed data and make predictions, as exemplified by modeling the Spanish electricity market.

### Strengths
The authors study an interesting and challenging problem of inverse MARL. The theoretical results are nice; they are simple yet relevant and impactful. 
The experiments on an electricity market are well thought and designed.

### Weaknesses
The readability can be improved. I think Section 3 never mentions that it is for the one-shot game setting. 
There is no methodological contributions. All presented algorithms are simple extension of known algorithms. (On the other hand we should not invent/propose algorithms just for the sake of proposing them).

### Questions
Minor remark/question: what is the meaning of that weird symbol in Theorems 3.2, 4.1, 5.2? I assume it means of the same order as (but I don't think this is standard notation.)
In Theorem 3.2, it is a little bit surprising that the optimal is obtained by averaging prior solutions instead of the last one. What is the intuition behind averaging (which includes initial solutions that can be of very low quality)? I assume the proof is correct.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
