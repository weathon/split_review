# Generative Adversarial Equilibrium Solvers

- Decision: Accept
- Avg Score: 4.50
- Scores: 1, 5, 6, 6

## Abstract
We introduce the use of generative adversarial learning to compute equilibria in general game-theoretic settings, specifically the \emph{generalized Nash equilibrium} (GNE) in \emph{pseudo-games}, and its specific instantiation as the \emph{competitive equilibrium} (CE) in Arrow-Debreu competitive economies. Pseudo-games are a generalization of games in which players' actions affect not only the payoffs of other players but also their feasible action spaces.
  Although the computation of GNE and CE is intractable in the worst-case, i.e., PPAD-hard, in practice, many applications only require solutions with high accuracy in expectation
  over a distribution of problem instances. We introduce {\em Generative Adversarial Equilibrium Solvers} (\nees{}): a family of generative adversarial neural networks that can  learn GNE and CE from only a sample of problem instances. We provide computational and sample complexity bounds, and apply the framework to finding Nash equilibria in normal-form games, CE in Arrow-Debreu competitive economies, and GNE in an environmental economic model of the Kyoto mechanism.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a novel algorithm, General Adversarial Equilibrium Solvers, for training general GNE solvers.

The goal of equilibrium solvers is, given a strategic game between multiple players, to find a (generalized) Nash equilibrium of the game. 

While there has been a few previous work that proposes algorithms to train equilibrium solvers, they all suffers from three technical challenges:
- the gradient of the exploitability requires solving a concave maximization problem
- the exploitability of pseudo-games is in general not Lipschitz-continuous
- the gradients cannot be bounded in general

The authors formulates equilibrium solver training as training a generative adversarial networks, where the generator takes a pseudo-game representation, and outputs a tuple of actions (one per player), and the discriminator takes both the pseudo-game, and the output of the generator, and outputs a best-response for each player.

The goal of discriminator is to output a best-response actions that produces the exploitability, and the goal of generator is to output actions that minimizes the exploitability, i.e., GNE.

### Strengths
# Presentation
- The paper is well-organized and easy-to-follow: Sec.1 motivates the readers by illustrating the possible applications of GNE solvers, including network communication, cloud computing, and economic models (e.g., Arrow-Debreu exchange economy, Kyoto joint implementation mechanism)

# Novelty, Technical Contribution
- The formulation of GAES establishes a novel, efficient, simple, and scalable algorithm to train generic GNE solvers.
    - To the best of my knowledge, most of the previous work relied on supervised learning, and suffered from a few technical challenges in terms of computational tractability and stability. 
    - GAES beautifully solves these problems, and provides a simple yet powerful framework for training GNE solvers.
- The formulation is strongly backed up by theoretical guarantees; convergence of the networks towards a stationary point of exploitability, and sample complexity. 
- The experiments are conducted on non-trivial games, namely Arrow-Debreu exchange economies and Kyoto joint implementation mechanism — which are non-monotone or non-jointly convex. Strong empirical results on these games verifies the efficiency of GAES.

### Weaknesses
 # Weaknesses
- I don’t see any special weakness in this paper. The authors establish a simple yet powerful framework for training GNE solvers, and backs up their algorithm both with strong theoretical guarantees and empirical results.

### Questions
- Would it be possible to scale GAES to modern games that consists of multiple neural networks (e.g., GANs, multi-agent RL problems, etc.)? If not, what would be the main technical challenges to do so?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper study the generalized Nash equilibrium of pseudo games where a player’s action not only affects his utility, but also other players’ action sets. The authors use GAN and employ exploitability as the loss function. The solver is applied to compute the GNE of Arrow-Debreu competitive economies and the Kyoto mechanism.

### Strengths
1. Introduce a novel method to compute GNE by GAN.
2. Provide theoretical guarantee on convergence and generalization bounds.
3. The performance is better according to the experiments.
4. The literature review in the appendix summarizes the current methods to solve GNE and the application of pseudo games.

### Weaknesses
 1. Assume strong concavity in assumption 1, however, the utility function is not strong convex in Arrow-Debreu competitive economy.
2. Do not provide guarantee for the performance on the training set.
3. Use different network architecture in two experiments which means GAES is not a general solver for GNE.

### Questions
1. In which paper was the name "pseudo game" and "GNE" made? It seems that the cited paper by Arrow Debreu mentioned the game first, but did not name it.
2. Do you measure the difference between the results and the optimal action in the feasible set? Notice that the results “is on average better than at least 99% of the action profiles” in the experiments.
3. Is there any guarantee when the utility function only satisfy convexity?
4. What is the title of this paper?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces generative adversarial equilibrium solvers (GAES), a GAN that learns to map pseudo-games to their generalized Nash equilibria from a sample of problem instances. In particular, they provide a formulation that makes the problem amenable to standard stochastic first-order methods. They use GAES to compute in a scalable way competitive equilibria in exchange economies and an environmental economic model of the Kyoto mechanism, outperforming earlier methods.

### Strengths
Pseudo-games are very general game-theoretic models with a number of applications, most notably Arrow-Debreu competitive economies. Yet, there is a lack of scalable techniques for computing generalized Nash equilibria in such settings. This paper makes a concrete contribution in that direction by providing a method with promising performance across a number of benchmarks. The proposed method is natural and the experimental results are overall convincing and quite thorough. Indeed, the paper appears to attain state of the art performance in a number of important applications, and could have significant impact in this area.

### Weaknesses
There are some soundness issues that the authors have to address. First, there appears to be a significant gap between the theoretical analysis and the experimental settings. Specifically, it is not clear how a stationary point in the sense of Theorem 4.1 translates to a GNE. If stationary points are not necessarily GNE, the narrative of the paper has to be restructured. In particular, it is often claimed that the method maps pseudo-games to GNE, and it is not clear whether that claim is theoretically sound. Of course, computing GNE is intractable, but it is alluded (for example in the abstract) that under a distribution over problem instances the problem could be easier. Theorem 4.1 also makes a strong concavity assumption which appears to be violated in all settings of interest. It should be the case that a "small" regularizer can always be incorporated without affecting the equilibria by much, but I think this should be discussed in more detail.

I am also confused about Footnote 4. It is claimed that the method obtains the state of the art $O(1/\epsilon^3)$ complexity, a major improvement over $O(1/\epsilon^6)$, which the authors claim was the previous state of the art. The authors have to explain more precisely the class of problems this applies to; there are many variants of the PL condition studied in the literature. In particular, the following papers seem to obtain a much better dependency: "Faster single-loop algorithms for minimax optimization without strong concavity," "faster stochastic algoritms for minimax optimization under Polyak-Lojasiewicz Conditions" and "Doubly smoothed GDA for constrained nonconvex-nonconcave minimax optimization."

Besides the issues above, the algorithmic approach is very close to the paper "Exploitability minimization in games and beyond," which limits to some extent the algorithmic contribution of the present paper. The authors have to highlight the comparisons in more detail.

### Questions
Some minor comments for the authors:

1. The title of the submission document is the default one.
2. The references have to be polished. There are many papers that are published many years ago and only the arXiv version is cited. There is also an issue with consistency: sometimes URLs are included, sometimes they are not. Please fix those issues.
3. There are underfull equations in Observation 1 and immediately below.
4. I don't understand how the paper of Daskalakis et al. (2009) is relevant in the context of Footnote 4 about min-max optimization.
5. The appendix has many overfull equations that need to be formatted properly.

### Soundness
2 fair

### Presentation
3 good

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
In this paper, the authors present a novel neural network-based method for approximating the generalized Nash equilibrium (GNE) within pseudo-games derived from a specific distribution. These pseudo-games consist of players operating within compact and convex action spaces, where the choices made by each player can influence the feasible action space of others.

To facilitate the training of the GNE neural network solver, the authors introduce exploitability as the loss function.  Exploitability quantifies the total utility gains that all players would achieve by deviating to their own best responses. However, calculating exploitability poses a challenge due to the potentially infinite action space. To tackle this issue, an adversarial network is employed to approximate each player's best response.

The authors also establish a theoretical framework by providing a generalization bound for this neural solver. Furthermore, in practical experiments, they apply this approach to identify Nash equilibria in normal-form games, compute competitive equilibria in Arrow-Debreu economic models, and determine GNE in an environmental economic model involving the Kyoto mechanism.

### Strengths
- The versatility of this method is evident because it can be applied to a wide range of games, thanks to the inherent generality of pseudo-games.
- The methodology looks strong. The use of two neural networks (a generator and a discriminator) and adversarial training is intriguing to me.
- The concept of employing a neural network as a function approximator to compute GNE is innovative. I believe it has the potential to expedite equilibrium computation in practice.

### Weaknesses
 - The title in the PDF is still the template title.
- The paper concentrates on finding a single equilibrium, yet many games have multiple equilibria. Incorporating a discussion on equilibrium selection would enhance the work.
- The overall presentation of this paper would benefit from further refinement. The figures within the paper are small and appear blurry due to the absence of vector graphics formats such as .pdf or .svg. Upgrading the figures to vector graphics would improve their clarity and overall visual impact.

### Questions
- How does the performance of GAES degrade with approximate discriminators in practice? Is there a way to quantify the required discriminator accuracy?
- Could you apply GAES to find other solution concepts like correlated equilibria? How would the formulation need to change?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
