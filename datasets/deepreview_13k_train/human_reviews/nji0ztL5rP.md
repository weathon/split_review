# Best Arm Identification for Stochastic Rising Bandits

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
\settingname (SRBs) model sequential decision-making problems in which the expected reward of the available options increases every time they are selected. This setting captures a wide range of scenarios in which the available options are \emph{learning entities} whose performance improves (in expectation) over time (\eg online best model selection). While previous works addressed the regret minimization problem, this paper focuses on the \textit{fixed-budget Best Arm Identification} (BAI) problem for SRBs. In this scenario, given a fixed budget of rounds, we are asked to provide a recommendation about the best option at the end of the identification process. We propose two algorithms to tackle the above-mentioned setting, namely \ucbeshort, which resorts to a UCB-like approach, and \succrejectshort, which employs a successive reject procedure. Then, we prove that, with a sufficiently large budget, they provide guarantees on the probability of properly identifying the optimal option at the end of the learning process and on the simple regret. Furthermore, we derive a lower bound on the error probability, matched by our \succrejectshort (up to constants), and illustrate how the need for a sufficiently large budget is unavoidable in the SRB setting. Finally, we numerically validate the proposed algorithms in both synthetic and realistic environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of best arm identification in the context of stochastic rising bandits with a fixed budget, aiming to identify the arm with the maximum expected reward in the final round. Two algorithms are proposed to tackle this issue: one is a UCB-typed algorithm, and the other is a successive-reject-typed algorithm. The paper also establishes a sample number lower bound for BAI problem of SRB setting, as well as an error lower bound when the sample number is fixed. The theoretical guarantees obtained show that R-UCBE is optimal but requires additional prior knowledge, while R-SR reduces the dependence on prior knowledge. Empirical results further demonstrate that R-UCBE and R-SR outperform other algorithms in comparison.

### Strengths
This work is clearly written and provides two solid approaches supported by theory and experiments. It also offers lower bounds for the problem, making it a fairly complete piece of work.

### Weaknesses
Assuming there is a unique best arm seems somewhat unrealistic, especially after T rounds, when there is a high probability that multiple arms could have the same reward. This can be observed in Figure 2 of the experiment, where several lines easily overlap, clearly demonstrating this point. Moreover, this situation is influenced by the randomness of the algorithm, similar to the paper's mention that "$i^*(T)$ may change," which is also a result of the algorithm's randomness. While similar assumptions are made in classical MAB settings, in those cases, the algorithm does not have an impact on the best arm.

### Questions
see the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focus on the stochastic rising bandits, the objective is maximize the success rate of identifying the best arm within fixed budget. The authors propose two algorithms, and one of them is optimal in success rate as the authors further give the lower bound that matches the upper bound. Authors further conduct synthetic experiments to validate the theoretical findings.

### Strengths
- The theoretical proofs are strict and easy to follow, the results seem sound to me.
- The experiments are explicitly introduced with specific details.
- The guarantee of R-SR is strong, and the analysis on the minimum budget the problem is solvable is crucial to the problem, making it clear on which parts of the problem is unsolvable.

### Weaknesses
 - My major concern is the insufficient problem motivation. In the introduction, the example introduces the SRB is ``the arm improve performances over time'', but the problem setup of SRB is arms whose performances increase with pulls. I personally feel it is the example of adversarial MAB or non-stationary MAB rather than SRB. The experiments still do not give the real-world applications. In fact it's hard for me to figure out real-world scenario (with the neccessary to model as a SRB) that solves practical problems.

- The problem statement is a little bit unclear. Specifically, it is mentioned that SRB is a special case of SRB, but it is never explained what the word ``rested'' means.

- There should be some discussions about the difficulties of applying existing algorithms (or some trivial variants) to solve SRB. For example, it is only mentioned in the experiments that non-stationary MAB algorithms and adversarial MAB algorithms is outperformed, but it is essential to verify that the increasing structure of SRB is crucial both theoretically and empirically. It would be helpful to see a more detailed explanation of why algorithms designed for stationary bandits, such as UCB-E and Successive Rejects, fail in this setting. Specifically, what are the theoretical barriers that prevent these algorithms from achieving optimal performance in the SRB problem? Furthermore, while the experimental results show that non-stationary and adversarial MAB algorithms are outperformed, the discussion should include a deeper dive into the specific reasons for this underperformance, linking it back to the unique structure of the SRB problem. For instance, are these algorithms too sensitive to the increasing rewards, or do they fail to exploit the specific structure of the reward functions?

### Questions
See above

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of fixed-budget best arm identification (BAI) within stochastic rising bandits. Specifically, it introduces both pessimistic and optimistic estimators for algorithm design. Building upon these estimators, two distinct algorithms emerge: R-UCBE and R-SR, drawing inspiration from UCB-E and SR as presented in Audibert et al. (2010). Regarding theoretical findings, the authors provide guarantees on the error probability of the two algorithms and investigate the minimal time budget $T$ required for the BAI task. Finally, numerical experiments conducted on synthetically generated data as well as a practical online best model selection problem serve to affirm the superiority of the proposed algorithms.

### Strengths
1. This paper is clear and well-organized.
2. The theoretical guarantee is exhaustive. Both the error probability and the minimum required time budget to accurately identify the optimal arm are taken into account.
3. The numerical experiments are impressive and comprehensive. The proposed algorithms clearly outperform the baselines.

### Weaknesses
1. While Assumption 2.1 appears intuitive, Assumption 2.2 falls short of being satisfactory. Even though the authors present some theoretical findings solely under Assumption 2.1, their interpretability is somewhat lacking. Specifically, the assumption that the increments satisfy $\gamma_i(n) \leq c n^{-\beta}$ for some $c, \beta > 0$ seems overly restrictive and lacks clear motivation. It is unclear what types of real-world reward functions would satisfy this condition, and the theoretical implications of this assumption are not thoroughly explored. The lack of justification makes it difficult to assess the practical relevance of the theoretical results derived under this assumption.

2. The proposed algorithm closely resembles UCB-E and SR for standard multi-armed bandits, with the primary distinction lying in the estimators. I'm not suggesting this is unacceptable, but it does somewhat diminish the novelty of this work. A promising future direction would involve integrating both estimators into a unified algorithm.

3. Since the expected rewards are bounded in $[0,1]$ and non-decreasing, they must converge to some value. Thus, it is not surprising that the error probability lower bound will be matched by R-SR for large $T$. For non-stationary BAI, the algorithm SR is minimal optimal up to constant factors.

### Questions
1. Theorem 6.1: In any case, the algorithm can make a random guess. Therefore, it is not appropriate to state that $e_T(\boldsymbol{\nu}, \mathfrak{A})=1$.

2. Minor issue in Section 2: \citet should be used in "As in (Metelli et al., 2022)".

3. Figure 3: Could you elucidate some intuitions/explanations behind the remarkable performance of R-UCBE in cases where $T$ is small? The error probability approaches zero very quickly.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
