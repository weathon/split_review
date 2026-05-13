# Can Reinforcement Learning Solve Asymmetric Combinatorial-Continuous Zero-Sum Games?

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
There have been extensive studies on learning in zero-sum games, focusing on the analysis of the existence and algorithmic convergence of Nash equilibrium (NE). Existing studies mainly focus on symmetric games where the strategy spaces of the players are of the same type and size. For the few studies that do consider asymmetric games, they are mostly restricted to matrix games. In this paper, we define and study a new practical class of asymmetric games called two-player Asymmetric Combinatorial-Continuous zEro-Sum (ACCES) games, featuring a combinatorial action space for one player and an infinite compact space for the other. Such ACCES games have broad implications in the real world, particularly in combinatorial optimization problems (COPs) where one player optimizes a solution in a combinatorial space, and the opponent plays against it in an infinite (continuous) compact space (e.g., a nature player deciding epistemic parameters of the environmental model). Our first key contribution is to prove the existence of NE for two-player ACCES games, using the idea of essentially finite game approximation. Building on the theoretical insights and double oracle (DO)-based solutions to complex zero-sum games, our second contribution is to design the novel algorithm, Combinatorial Continuous DO (CCDO), to solve ACCES games, and prove the convergence of the proposed algorithm. Considering the NP-hardness of most COPs and recent advancements in reinforcement learning (RL)-based solutions to COPs, our third contribution is to propose a practical algorithm to solve NE in the real world, CCDORL (based on CCDO) and provide the novel convergence analysis in the ACCES game. Experimental results across diverse instances of COPs demonstrate the empirical effectiveness of our algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new class of asymmetric zero-sum games that features combinatorial action space for one player and an infinite compact space for the other, termed Asymmetric Combinatorial-Continuous zEro-Sum (ACCES) games. After providing its definitions and motivations, the authors prove the existence of mixed NE in ACCES games and design two algorithms to solve for NE, with proofs and analysis on their convergence. The second algorithm, which adopts RL concepts, is further validated on three instances of ACCES games and achieves positive experimental results.

### Strengths
+ Good presentations, particularly motivations for ACCES games.
+ The paper designs an algorithm with proven convergence guarantee called CCDOA to solve ACCES games, which extends the idea of double oracle-based solutions from zero-sum finite games.
+ The paper further develops a more practical version of CCDOA that uses RL and graph embedding techniques to find the approximate best response for each player.

### Weaknesses
 - Experiments for evaluating CCDOA-RL are small-scale, with at most 50 nodes, which limits the practicality of the proposed algorithm. Furthermore, there were no discussions on runtimes or potential performance optimization for reducing computations.
- Wrong bibliography style (should be [author(s), year], not numbers).

### Questions
1. Could the authors provide some remarks on ACCES games with more than 2 or more generally N players i.e., n players with combinatorial action space, and N-n players with infinite compact space? In particular, the existence of NE and generalizability of the proposed algorithms to such settings?
2. What are the runtimes for CCDOA-RL on 50-node instances?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper defines and studies a novel class of two-player zero-sum games termed ACCES (Asymmetric Combinatorial-Continuous zEro-Sum) based on the premise that most zero-sum games that have been studied are either symmetric or confined to matrix games (whenever asymmetric). A natural motivation for this class is a player with a combinatorial action space (e.g., path minimization, scheduling) who plays against an environment that adversarially sets its parameters drawing from continuous parameter-value spaces (e.g., customer demand, edge weights, targets etc). The paper seeks to answer three motivating in this setting: whether a Nash equilibrium (NE) exists, whether it can be found and whether it can be found efficiently and provides affirmative answer to all three. The existence of NE is established through the properties of weakly sequential compactness and continuity of expected utility function that are established for these games. Regarding the other two questions, the paper develops an algorithm that is based on the double-oracle (DO) methods that have been used to solve finite zero-sum games and proposes an approximate, RL-based variant to tackle the exponential blow-up in computing exact best responses in the combinatorial action space of the first player. The paper complements the theoretical proofs of convergence with experiments in three ACCES environments, also demonstrating improved convergence performance against baseline algorithms.

### Strengths
- The paper is well-written, clearly explains its motivation and its research questions. It also provides a fair discussion of its limitations, mainly the scalability of its proposed algorithms. 
- The paper is rigorous with proofs of convergence that seem correct to the extent that I could verify.

### Weaknesses
 - While the ACCES games are interesting and cover various settings as demonstrated by the studied environments, I would have expected some more machine-learning/neural network motivation when I read about the "adversarial parameter setting of the environment" that was ultimately missing from the paper. Some examples that may be helpful: (https://arxiv.org/abs/2003.01820, https://arxiv.org/abs/2002.06673).

- The paper does an effort to acknowledge related work, however literature on zero-sum games is vast and recent papers on learning in zero-sum (matrix) games are not entirely acknowledged (e.g., Online Learning in Periodic Zero-Sum Games and references therein, Zero-sum polymatrix games, Efficiently Computing Nash Equilibria in Adversarial Team Markov Games, The complexity of constrained min-max optimization, https://arxiv.org/abs/2011.00364 etc). 

- I found the existence result not surprising (maybe I am missing some technically difficult step?) and immediately following from the existence in both continuous (and bounded) and finite zero-sum games. I have a similar consideration for the convergence of the DO-based algorithm.

- Essentially combining my two previous points, it is not entirely clear to me how novel this environment is and how much more interesting that the min-max optimisation in non-convex, non-concave settings. I think that the paper does not make a very convincing argument that the current setting is not a derivative, not-niche and sufficiently different and more complex setting than what is currently studied in the literature.

### Questions
Can the authors discuss/address the weaknesses mentioned above?

**Post-rebuttal**: I thank the authors for their responses. I still believe that the properties of weak sequential compactness and continuity of the expected utility function are fairly straightforward and hence that both the existence of Nash equilibria in ACCES games and the class itself don't really depart much from existing classes of zero-sum games. Also, while the updated version cites some zero-sum papers, I don't see a meaningful discussion/comparison with the min-max optimisation in non-convex, non-concave games or these existing classes of zero-sum games. I think this discussion requires more thorough study of the related works which cannot be done on the fly during the limited time of this discussion - and is also beyond my capacity to engage in such a discussion. This limits the contribution of the current paper in my opinion.

Nevertheless, I appreciate the practicality of the algorithms for real-world cases that the paper offers and which I had underestimated in my original review. I have revised my scores accordingly.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors define and study a new useful class of two-player games called ACCES games, which feature asymmetry between the players' strategy spaces. One player has a combinatorial strategy space, while the other has a continuous one. The paper has 3 main contributions. First, the authors prove the existence of a Nash equilibrium for two-player ACCES games. Second, they describe an extension to the Double Oracle method that solves two-player ACCES games by provably converging to Nash. This method (CCDO) relies on exact best response computation at every iteration.  Finally, they present a modified version of CCDO that uses RL to approximate best responses and thus approximate Nash in more practical ACCES settings.

### Strengths
* I like this formalization. It is intuitive and seems to be a natural extension of the two-player zero-sum symmetric case that fits many interesting scenarios (like the nature vs. player and patrolling games examples mentioned in the paper).
* The paper is impressively well-written and easy to follow. The main contributions are clearly stated and motivated early on, and the theoretical results are presented in a digestible manner that guides the reader through them. 
* The authors present theoretically sound algorithms for solving and approximately solving these games. These results are impressive on their own, but I believe they are valuable to the community because they could act as a foundation for developing more scalable algorithms in this domain in the future.

### Weaknesses
 * In the conclusion, the authors mention that scalability may be a limitation of their work. Though it's not the main point of the paper, I'm somewhat concerned that the scalability of the approximate best response may limit the applicability of CCDO-RL. I don't believe the authors have to necessarily evaluate their methods on larger domains, but some insight on how the RL component of every iteration scales could help alleviate these concerns. 
* The convergence guarantees of CCDO-RL seem dependent on finding $\epsilon$ best-responses at every iteration. To the previous point, this may be unrealistic in some larger domains. This somewhat weakens the guarantees of the algorithm, but I understand that this seems true for many algorithms whose dynamics depends on best response approximation.

* What specific scalability concerns do the authors have with CCDO-RL?
* Is CCDO-RL guaranteed to terminate? It seems if both conditions on lines 6 and 8 in Algorithm 1 fail, then the strategy set is unchanged.

**Additional Comments**
* There seems to be a mistake on line 71 regarding the attacker and defender's utilities in the example patrolling game.
* From the formalization, it is clear that every two-player ACCES game is zero-sum, but I suggest mentioning that earlier.

### Questions
* What specific scalability concerns do the authors have with CCDO-RL?
* Is CCDO-RL guaranteed to terminate? It seems if both conditions on lines 6 and 8 in Algorithm 1 fail, then the strategy set is unchanged.

**Additional Comments**
* There seems to be a mistake on line 71 regarding the attacker and defender's utilities in the example patrolling game.
* From the formalization, it is clear that every two-player ACCES game is zero-sum, but I suggest mentioning that earlier.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces and studies a new class of zero-sum games – two-player Asymmetric Combinatorial-Continuous zEro-Sum (ACCES) games, where one player has a combinatorial action space whereas the other has an infinite compact space. The asymmetry lies in the differing nature of the players’ strategy spaces. The authors claim that ACCES games closely resemble real-world problems, particularly in combinatorial optimization problems (COPs), min-max games, and security games. To evaluate their algorithms, the authors provide three different ACCES game scenarios: adversarial covering salesman problem (ACSP), adversarial capacitated vehicle routing problem (ACVRP), and patrolling game (PG).

 As with any new problem in game theory, the authors first prove the existence of the Nash Equilibrium (NE) for this game. The authors then propose a double oracle-based algorithm called Combinatorial Continuous DO (CCDO) to solve ACCES games, alongside proving the convergence of the algorithm. Finally they propose a Reinforcement Learning algorithm, CCDO-RL with convergence guarantees and empirically demonstrate the effectiveness of the proposed algorithm. CCDO-RL adopts RL to compute the approximate best responses.

### Strengths
- The paper tackles a novel problem in 2p0s games by considering asymmetry in strategy space rather than the common forms of asymmetry (e.g., information asymmetry). 
- The authors provide theoretical proofs for the existence of NE and convergence of their algorithms, as well as empirical demonstrations of their effectiveness and superiority compared to baselines based on heuristics and a single-agent RL algorithm.

### Weaknesses
 - The patrolling game in the introduction might benefit from a better explanation, especially labels for P1 and P2 (attacker/defender). It would be helpful if the authors could label which player is the attacker and which is the defender. 
- Algorithm 1 in the paper seems very similar to the XDO/NXDO algorithms (McAleer et al., 2021). Perhaps the novelty is in computing the BRs (McAleer et al. consider BRs but the authors here consider approx. BRs), but the underlying algorithm, as presented, seems the same.  Highlighting the difference of the proposed algorithm with existing algorithm such as XDO/NXDO might underscore the challenge of solving the proposed problem. 
- How the mixed equilibria (step 3 in all algorithms) are solved in the subgame is unclear. This is likely the crucial part of the problem, given the different strategy spaces associated with the players. Briefly explaining the computational technique would be helpful.

### Questions
* The dynamics of the ACCES game is unclear. Is it a turn based or a simultaneous move game? Also, is it a fixed-horizon game or an infinite one with some termination criterion? 
* In line 166, shouldn't $X$ be **all** *routes* instead of **any** ? 
* Line 140: 
> As far as we know, they are limited to matrix games, ...

  * Don't McAleer et al. (2021) consider both extensive-form games and a continuous game? I am not sure what is being referred to as being "limited to matrix games" as McAleer et al. (2021) also prove convergence to $\varepsilon$-NE. Could authors please elaborate on this? Perhaps I misunderstood. 

* Line 328:
> However, the approximation of BR may cause circumstances where the utility of the approximate best response is lower than that of NE in the subgame"

  * I am curious as to how this would impact the final policy. Yes, it is possible that the approximate BR may not be accurate leading to a negative NashConv, which is theoretically not possible. Could authors comment on the impact of removing the steps 6-9 in Algorithm 1 from purely experimental standpoint? Also, explaining this part in a bit detail might help readers understand the issue. 

* I couldn't find the results and/or discussion on "how different ABRs influence convergence". Perhaps my interpretation of different ABRs as different BR approximating algorithms is not correct. Could authors please comment on this?

*McAleer, S., Lanier, J. B., Wang, K. A., Baldi, P., & Fox, R. (2021). XDO: A double oracle algorithm for extensive-form games. Advances in Neural Information Processing Systems, 34, 23128-23139.*

### Soundness
2

### Presentation
3

### Contribution
3
