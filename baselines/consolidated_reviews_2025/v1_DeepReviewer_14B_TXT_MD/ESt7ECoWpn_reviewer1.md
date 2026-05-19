### Summary

This paper proposes a method to achieve $(\epsilon, \delta)$-DP through a game-theoretic approach. Specifically, it considers a game with $n$ players, where each player $i$ controls the noise variance $b_i$ added to the $i$-th data point. The utility function of this game is defined as the weighted sum of the privacy assurance term (encouraging the game to satisfy $p$-DP) and the utility preservation term (encouraging the game to maintain utility). The authors aim to find the Nash Equilibrium (NE) of this game and prove that at the NE, the game satisfies $p$-DP. They propose a best response dynamic (BRD) algorithm to find the NE of the game and test the performance of this algorithm on two datasets, comparing it with the standard Laplace mechanism.

### Soundness

1 poor

### Presentation

2 fair

### Contribution

1 poor

### Strengths

1. This paper studies an interesting problem of designing a mechanism that satisfies $p$-DP while maximizing utility.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not better than the state-of-the-art methods for solving $p$-DP mechanisms. Specifically, the authors do not compare their method with the optimal solution for $p$-DP mechanisms, which is a significant oversight. The current state-of-the-art for achieving $p$-DP involves optimizing noise levels for each data point, and the paper fails to demonstrate how their game-theoretic approach compares to this optimal solution in terms of utility.
2. The proof of Theorem 4.1 is incorrect. The authors claim that at Nash Equilibrium, all data points satisfy $p$-DP, but this is not necessarily true. The proof relies on the assumption that if a player can improve their utility by deviating from their current strategy, then the current strategy profile is not a Nash Equilibrium. However, this logic is flawed. It is possible that a player could deviate and either improve or worsen their utility, and the game would still be at a Nash Equilibrium as long as no player can improve their utility. The proof needs to rigorously show that at equilibrium, all data points simultaneously satisfy the $p$-DP condition, which is not the case in the current version.
3. The proposed BRD algorithm is not guaranteed to converge to the NE of the game. The authors acknowledge that the game is not a potential game, and therefore, the BRD algorithm may not converge. This is a significant limitation, as it means that the algorithm may not find the desired Nash Equilibrium, and the privacy guarantees may not hold in practice.

### Suggestions

The paper needs to address several key issues to be considered for publication. First, the authors must compare their proposed method against the optimal solution for $p$-DP mechanisms. The current state-of-the-art involves solving an optimization problem to determine the noise levels for each data point, ensuring $p$-DP while maximizing utility. The authors should implement this optimal solution and compare their game-theoretic approach against it, demonstrating the advantages or disadvantages of their method. This comparison is crucial to understand the practical relevance of the proposed approach. Without this comparison, it is impossible to assess whether the game-theoretic approach provides any benefit over existing methods.

Second, the proof of Theorem 4.1 needs to be significantly revised. The current proof incorrectly assumes that if a player can deviate and improve their utility, then the game is not at a Nash Equilibrium. The proof needs to rigorously demonstrate that at the Nash Equilibrium, all data points simultaneously satisfy the $p$-DP condition. This requires a more detailed analysis of the game's equilibrium conditions and how they relate to the $p$-DP guarantee. The authors should consider using techniques from game theory that specifically deal with the convergence of strategies to a Nash Equilibrium, and then show that at this equilibrium, the $p$-DP condition is met for all data points. The current proof is insufficient and needs to be strengthened with a more rigorous argument.

Finally, the authors need to address the convergence issue of the BRD algorithm. Since the game is not a potential game, there is no guarantee that the BRD algorithm will converge to a Nash Equilibrium. The authors should either prove that the game has a specific structure that guarantees convergence under BRD (e.g., it is an exact potential game, weakly acyclic, quasi-acyclic, or aggregative) or propose an alternative algorithm that is guaranteed to converge. Without a convergence guarantee, the privacy guarantees of the proposed method are not reliable. The authors should also provide empirical evidence of the convergence behavior of the BRD algorithm in practice, and discuss the implications of non-convergence.

### Questions

1. The proof of Theorem 4.1 is incorrect. The authors claim that "if the game is not in NE, there must exist a data instance $d_i \in \mathcal{D}$ that can improve its utility by altering its own strategy." However, this statement is not true. If data instance $d_i$ can alter its strategy and get a worse utility, the game is still NE. The authors should provide a rigorous proof that at the Nash Equilibrium, all data points satisfy the $p$-DP condition simultaneously.
2. The authors claim that the proposed game is a common interest game. However, the utility function is a weighted sum of the privacy assurance term and the utility preservation term, which are not the same. Therefore, the game is not a common interest game.
3. The authors claim that the proposed game is a potential game. However, this claim is incorrect. Even if the game is a potential game, the BRD algorithm is not guaranteed to converge to the NE of the game. The authors should provide a rigorous proof that the game is a potential game and that the potential function is monotone, which would imply that the BRD algorithm converges to the NE of the game.
4. The authors should compare the proposed method with the optimal solution for $p$-DP mechanisms.

### Rating

1: strong reject

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
