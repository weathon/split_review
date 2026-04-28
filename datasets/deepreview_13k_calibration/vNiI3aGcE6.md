# Provable Memory Efficient Self-Play Algorithm for Model-free Reinforcement Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
The thriving field of multi-agent reinforcement learning (MARL) studies how a group of interacting agents make decisions autonomously in a shared dynamic environment. Existing theoretical studies in this area suffer from at least two of the following obstacles: memory inefficiency, the heavy dependence of sample complexity on the long horizon and the large state space, the high computational complexity, non-Markov policy, non-Nash policy, and high burn-in cost. In this work, we take a step towards settling this problem by designing a model-free self-play algorithm \emph{Memory-Efficient Nash Q-Learning (ME-Nash-QL)} for two-player zero-sum Markov games, which is a specific setting of MARL. We prove that ME-Nash-QL can output an $\varepsilon$-approximate Nash policy with remarkable space complexity $O(SABH)$, sample complexity $\widetilde{O}(H^4SAB/\varepsilon^2)$, and computational complexity $O(T\mathrm{poly}(AB))$, where $S$ is the number of states, $\{A, B\}$ is the number of actions for the two players, $H$ is the horizon length, and $T$ is the number of samples. Notably, our approach outperforms in terms of space complexity compared to existing algorithms for tabular cases. It achieves the lowest computational complexity while preserving Markov policies, setting a new standard. Furthermore, our algorithm outputs a Nash policy and achieves the best sample complexity compared with the existing guarantee for long horizons, i.e. when $\min \\{ A, B \\} \ll H^2$. Our algorithm also achieves the best burn-in cost $O(SAB\,\mathrm{poly}(H))$, whereas previous algorithms need at least $O(S^3 AB\,\mathrm{poly}(H))$ to attain the same level of sample complexity with ours.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a model-free algorithm for learning Nash policy in Two-player Zero-sum Markov Game. The authors prove that this algorithm enjoy many benign properties, including outputting Markov policy, low computational/sample/space complexity in certain regime and low burn-in cost.

### Strengths
The proposed algorithm enjoys several benign properties, as mentioned in the summary. In particular, the algorithm perform well when the horizon is very long while retaining other nice properties such as Markov output policy and low burn-in cost.

### Weaknesses
1. The proposed algorithm does not break the curse of multi-agent. Although the authors argue that there are many scenarios where horizon length is very long, I still feel that this is not general enough. I personally would still be more interested in algorithms that have $O(A+B)$ dependence in complexity. Specifically, the algorithm's dependence on the product of action space sizes ($A$ and $B$) remains a significant limitation, especially in environments with large action spaces for either or both agents. This dependence can lead to impractical computational costs and memory requirements as the number of actions increases, making the algorithm unsuitable for many real-world scenarios where agents have a wide range of possible actions. The authors should more thoroughly address the limitations imposed by the $O(AB)$ dependence, even if long-horizon scenarios are the focus.
2. The algorithmic novelty is a bit unclear to me. While the paper introduces a new algorithm, the core ideas do not seem to be fundamentally different from existing approaches. It would be beneficial to explicitly highlight the novel components and how they differ from prior work. Without a clear understanding of the unique contributions, it is difficult to assess the significance of the proposed method. The paper would benefit from a more detailed explanation of the specific techniques that are original to this work, and how they provide a substantial improvement over existing methodologies.

### Questions
1. There are many elements mentioned in the paper, such as complexity, burn-in cost, Nash policy, Markov policy etc. While I understand that no prior algorithm surpassing this algorithm in every aspect, I wonder what do the authors think is the most important aspect/what is the main focus?
2. Can the authors explain what is the most salient algorithmic novelty to the newly proposed algorithm?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a model-free algorithm for two-player zero-sum Markov game, which enjoys low sample complexity and computational/space complexity. The resulting algorithm has optimal dependency on S and H but sub-optimal dependence on the number of actions. The algorithm design features the early-settlement method and the reference-advantage decomposition technique.

### Strengths
+ The paper is well written and easy to follow. 
+ The proposed algorithm outperforms existing algorithms in terms of space complexity and computational complexity.

### Weaknesses
 - My main concern is the technical novelty. The reference-advantage decomposition technique has already been incorporated in two-player zero-sum Markov game by Feng el al (2023) (not cited by this work), which achieves a regret in \tilde{O}(\sqrt{H^2SABT}) and matches with the regret bound in this work. The main novelty of the algorithm design thus lies in the early-settlement design in order to reduce the burn-in cost, which is not new in the literature.

Feng, S., Yin, M., Wang, Y. X., Yang, J., & Liang, Y. (2023). Model-Free Algorithm with Improved Sample Efficiency for Zero-Sum Markov Games. arXiv preprint arXiv:2308.08858.

### Questions
+ Regarding my point in weakness section, is there any other technical contributions besides reference-advantage decomposition and early-settlement design?

+ Is it possible to obtain similar result for learning CCE in multi-agent general-sum Markov games?

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
This paper studies two-player zero-sum Markov games (TZMG). It proposes the model-free algorithm Memory-Efficient Nash Q-Learning (ME-Nash-QL), which achieves state-of-the-art space and computational complexity, nearly optimal sample complexity, and the best burn-in cost compared to previous results with the same sample complexity. Moreover, the proposed algorithm generates a single Markov and Nash policy rather than a nested mixture of Markov policies, by computing a relaxation of the Nash equilibrium instead, i.e. Coarse Correlated Equilibrium (CCE).

### Strengths
# Originality
- The related works are covered in detail.
# Quality
- The theoretical proofs seem to be rigorous. 
# Clarity
- This paper is in general well-written and easy to follow. The design idea of the algorithm is clearly explained.
# Significance
- The theoretical results of this work are strong. It achieves state-of-the-art space and computational complexity, nearly optimal sample complexity, and the best burn-in cost compared to previous results with the same sample complexity.
- TZMG is foundational and critically significant for MARL. This research has the potential to establish a new benchmark, providing a foundation for further studies in the related literature.

### Weaknesses
 - Although the proposed algorithm is compared to Nash-VI (Liu et al., July 2021) and V-learning (Jin et al., 2022) in detail, the design idea of the proposed algorithm seems to share certain similarities with those from the two works. For example, they all compute a CCE policy and take the marginal policies; the choice of learning rate $\frac{H+1}{H+N}$, the form of bonus terms, and the update of lower and upper bounds for Q-functions are similar. The originality of this paper could be significantly enhanced if the authors could discuss thoroughly the fundamental distinctions between the ideas of the proposed algorithm and the aforementioned Nash-VI and V-learning. Specifically, while the paper mentions differences in space and computational complexity, a more detailed comparison of the core algorithmic mechanisms is needed. For instance, how does the specific structure of the bonus term in ME-Nash-QL differ from those in Nash-VI and V-learning, and what are the implications of these differences on the convergence properties? A deeper dive into the algorithmic nuances is necessary to establish the unique contributions of this work.
- The theoretical findings are limited to the TZMG and CCE setting, which somewhat diminishes the overall contribution of this paper. The practical relevance of CCE in general-sum games is not always clear, and the paper should discuss the limitations of this choice. Furthermore, while the authors claim to achieve a Nash equilibrium in the TZMG setting, the connection between CCE and Nash equilibrium in this specific context needs more explicit justification. The theoretical analysis could be strengthened by exploring the potential for extending the results to broader classes of games or by providing a more detailed discussion of the practical implications of the CCE solution.
- The auxiliary functions in Algorithm 2 are too nested, making it hard to read. The lack of clarity in the presentation of these functions hinders the understanding of the algorithm's implementation. A more modular and well-documented presentation of these functions would greatly improve the readability and accessibility of the paper. For example, breaking down the nested functions into smaller, more manageable components with clear descriptions of their inputs and outputs would be beneficial.
### Minor:
- There seems to be a blank section A.3.1 on page 14.

### Questions
- How is $\operatorname{CCE}(\bar{Q}, Q)$ compuated? I was anticipating a detailed introduction to its calculation to ensure the paper's comprehensiveness. An explicit explanation would greatly contribute to the paper's self-containment.
- Is the achievement of the space complexity independent of $T$ attributed to the fact that the output policy is a single Markov policy? In this context, do the authors consider the CCE as an essential relaxation for realizing such space complexity?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies provably efficient reinforcement learning in two-player zero-sum Markov games, an important special case of multi-agent RL. This paper improves existing results in the following directions: sample complexity, memory efficiency, Markov output policy, and burn-in cost.

### Strengths
This paper studies an important topic in MARL theory. The proposed algorithm simultaneously achieved state-of-the-art results in all the aspects it considers: It matches the best sample complexity bounds, reduces the burn-in cost, and improves the space complexity while still outputting a Markov policy. The theoretical analysis looks solid.

### Weaknesses
I reviewed this paper at NeurIPS 2023. My concern was about the technical novelty of the paper because the proposed algorithm follows the mature framework of Nash Q-learning. The improved sample complexity is achieved by also following an existing reference-advantage decomposition technique. 

In terms of the bounds, the biggest improvements that this paper makes over existing works are regarding the space complexity and burn-in cost. In my opinion, these are less important metrics compared to sample complexity or time complexity, yet this work has to optimize these metrics at the cost of a much more complicated algorithm and proof procedure. 
While I still hold most of my previous opinions, I appreciate the authors’ effort in improving their work and would like to increase my score compared to my NeurIPS evaluation. 

Compared to the NeurIPS submission, the new major results are Theorems 2 and 3. I found that the extension to multi-player general-sum games (Theorem 3) particularly interesting, but I was not able to find any algorithm or proof for this theorem. What is the learning target for general-sum games, Nash or correlated equilibria?

### Questions
1.	Could you please point me to the proofs of Theorem 3? Also what is the algorithm for this theorem (as I assume that Algorithm 1 only applies to two-player zero-sum games)? I do not think the extension from zero-sum to multi-player general-sum is straightforward and would hope to see a more detailed discussion.

2.	Since you now also consider multi-player general-sum games, it is probably helpful to include related works for learning in general-sum games, especially those using Nash V-learning (to name a few):

a. Song, Ziang, Song Mei, and Yu Bai. "When can we learn general-sum Markov games with a large number of players sample-efficiently?." arXiv preprint arXiv:2110.04184 (2021).

b. Mao, Weichao, and Tamer Başar. "Provably Efficient Reinforcement Learning in Decentralized General-Sum Markov Games." arXiv preprint arXiv:2110.05682 (2021).

c. Daskalakis, Constantinos, Noah Golowich, and Kaiqing Zhang. "The complexity of markov equilibrium in stochastic games." The Thirty Sixth Annual Conference on Learning Theory. PMLR, 2023.

3.	From what I understsand, the new major results compared to the NeurIPS submission are Theorems 2 and 3. Could you please let me know if there are any other new results that I am missing?

4.	In your future work, you mentioned the possibility of achieving A+B sample complexity instead of AB. Does the Nash V-Learning algorithm help with this?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
