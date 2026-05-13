# Optimal Algorithm for Max-Min Fair Bandit

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
We consider a multi-player multi-armed bandit problem (MP-MAB) where $N$ players compete for $K$ arms in $T$ rounds. The reward distribution is heterogeneous where each player has a different expected reward for the same arm. When multiple players select the same arm, they collide and obtain zero reward. In this paper, we aim to find the max-min fairness matching that maximizes the reward of the player who receives the lowest reward. This paper improves the existing regret upper bound result of $O(\log T\log \log T)$ to achieve max-min fairness. More specifically, our decentralized fair elimination algorithm (DFE) deals with heterogeneity and collision carefully and attains a regret upper bounded of $O((N^2+K)\log T / \Delta)$, where $\Delta$ is the minimum reward gap between max-min value and sub-optimal arms. We assume $N\leq K$ to guarantee all players can select their arms without collisions. In addition, we also provide an $\Omega(\max\{N^2, K\} \log T / \Delta)$ regret lower bound for this problem. This lower bound indicates that our algorithm is optimal with respect to key parameters, which significantly improves the performance of algorithms in previous work. Numerical experiments again verify the efficiency and improvement of our algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies a multi-player multi-armed bandit problem with heterogeneous reward and collision. 
This paper aims to find a fair bandit algorithm that matches each player to a distinct arm while maximizing the reward of the player who receives the smallest reward. 
This paper provides a max-min regret lower bound of $\Omega(\max(N^2, K) \log T/\Delta)$. 
The authors propose the decentralized fair elimination (DFE) algorithm that guarantees the exploration of all valid player-arm pairs by constructing matchings, controls the communication times by the doubling trick, and eliminates player-arm pairs whose upper confidence bounds are smaller than the lower confidence bound of the current max-min value.
The authors show that DFE achieves $O((N^2+K)\log T/\Delta)$ max-min regret.
There is also an empirical study of the performance of the proposed algorithm compared to prior decentralized competitive MP-MAB algorithms.

### Strengths
- The problem studied (fairness in MP-MAB) is important and interesting.
- The algorithmic designs of exploration and elimination procedures are interesting.
- This paper conducts both theoretical and empirical studies.
- I appreciate the diagrams for algorithmic design illustration.

### Weaknesses
 - The claim that the proposed algorithm is optimal concerns me because the upper bound $O((N^2+K)\log T/\Delta)$ does not match exactly with the lower bound $\Omega(\max(N^2, K) \log T/\Delta)$ in terms of $N$ and $K$. While the proposed DFE algorithm is near-optimal, a more precise characterization of its optimality would be beneficial.

- The readability of this paper can be further improved. Notations can be introduced more clearly. For example:
    - A matching $m$ is first introduced as "matching set" $m(t)$, but later more used as matching $m$ or $m_i$. It would be beneficial to consistently use a single notation throughout the paper and clearly define it at its first occurrence. For instance, the authors could state "Let $m(t)$ denote the matching at time $t$, where $m_i(t)$ represents the arm assigned to player $i$ at time $t$."
    - The definition of regret in this paper is very different from that in multi-armed bandit literature. I would suggest the authors make this point clearer in the paper, perhaps by explicitly contrasting their definition with the standard definition and justifying the choice of a max-min regret in the context of fairness.
    - The last sentence on the first page is too long and could be broken down into multiple sentences for clarity.
    - $\mathcal{P}$ has always denote player-arm set in the rest of the paper. However, it is used differently in Section 4. The authors should ensure that $\mathcal{P}$ is used consistently throughout the paper to represent the player-arm set.
    - Claim 1 only holds for the instance described in Section 4. This point should be made clear, as in Lemma 1, by explicitly stating the conditions under which Claim 1 holds.
    - Figure 5 is not very color-blind friendly or black-white printable. Using different patterns or markers in addition to colors would improve accessibility.

### Questions
- Is the $O(\log T \log \log T)$ regret bound of Bistritz et al. (2020) analyzed against the max-min regret same as defined in Section 2? If not, it seems unfair to compare with it in the introduction. 
- Is there any hyperparameter for the proposed algorithm or the benchmarks the authors set in the experiments? If so, please add them to the paper to increase replicability.

### Soundness
3

### Presentation
2

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
This paper considers max-min fair bandit, an important variant of multi-player multi-armed bandit problem where fairness means to maximize the reward of the player who receives the lowest reward. Existing work in max-min fair bandit suffer from large regret and heavy assumptions. The authors give tight regret bound for the bandit problem that is optimal with respect to all parameters. Special case for the lower bound is provided. The work closes the gap of the man-min fair bandit problem.

### Strengths
This paper fills an important gap in existing max-min bandit literature. Tight regret bound is proved and special case is provided to demonstrate the lower bound. The improvement is significant compared to existing work. The regret bound is tight in all parameters. The algorithm is splitted into three phases with detailed algorithmic and graphical illustrations.

### Weaknesses
The main section of the decentralized fair elimination algorithm is a bit hard to read. It would be good if the authors can highlight the novelty part of the algorithm and clearly demonstrate how the three steps of the main algorithm contributes to the regret and which dominates the regret. The elimination phase is a commonly used strategy. The exploration phase is new, but it does not seem to directly contribute to the improvement of overall regret. The communication phase is also seen in the matching bandit literature. Specifically, the connection between the exploration phase and the final regret bound is not clear. While the algorithm description provides a high-level overview, the precise mechanism by which the exploration phase achieves the claimed $N^2 + K$ exploration bound, and how this bound translates to the overall regret, is not sufficiently explained. Furthermore, the role of the communication phase in ensuring the correctness of the exploration and elimination steps needs more clarification. The current description leaves the reader wondering how the information exchange between players is used to coordinate the exploration and elimination processes.

### Questions
• Line 90 What is the doubling trick?   
• Line 242 about the second type of elimination – unclear. How to determine the assertion of “with high probability”?  
• If there is no elimination phase, how the regret is affected? Line 310 is confusing.  
• Can you give intuitive idea / sketch proof to Thm 1, which is the key result for the whole paper, to explain how the three steps contribute to the regret bound?

-------------------------After Rebuttal-----------------------------
Thank you for the response. This helps me better understand the technical contribution of the paper. I see it's a theoretically interesting paper. I increased my confidence in my assessment.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the multi-player multi-armed bandit (MP-MAB) problem, with the goal of finding a max-min fairness matching that maximizes the reward of the player receiving the lowest reward. The authors propose a decentralized fair elimination (DFE) algorithm to handle heterogeneous reward distributions and collisions between players. The algorithm improves the regret upper bound from $O(\log T \log \log T)$ to $O\left(\left(N^2+K\right) \log T / \Delta\right)$, where $\Delta$ is the minimum reward gap. Additionally, they provide a regret lower bound, demonstrating that the algorithm is optimal concerning key parameters.

### Strengths
1. The authors design a new phased elimination algorithm that improves max-min fairness by adaptively eliminating suboptimal arms and exploring the remaining ones. The algorithm achieves a regret upper bound of $\mathrm{O}\left(\left(\mathrm{N}^2+\mathrm{K}\right) \log \mathrm{T} / \Delta\right)$, which outperforms existing results.
2. The paper derives a tighter regret lower bound of $\Omega(\max (\{N^2, K\}) \log T / \Delta)$, which considers the parameters $N$, $K$, and $\Delta$, improving upon prior work.
3. Numerical experiments confirm the effectiveness of the DFE algorithm across different settings.

### Weaknesses
1. I appreciate the contribution of this work, which presents the first optimal result for the MP-MAB problem, aligning with the lower bound established here. However, compared to earlier studies, particularly those by Bistritz et al. (2020) and Leshem (2023), this study, which employs a classic elimination-based strategy, only improves the regret results by a factor of $\log\log T$. This improvement may not be particularly significant for smaller values of $T$. Does this work demonstrate advantages over others in terms of factors such as $N$ or $K$?

2. Recently, several studies have reported intriguing results on reducing communication costs in the MP-MAB problem for both competitive and cooperative settings. I believe the authors could strengthen this study by incorporating a communication-efficient algorithm. Can the authors provide a rigrous upper bound for the communication cost in this work and discuss the possibility to make it optimal? Did the work improve the communication cost compared to previous work?

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a theoretical study for the Multi-Player Multi-Armed Bandit (MP-MAB) problem with a max-min fairness objective. In this scenario, multiple players choose from a set of arms, and collisions between players result in zero rewards. The goal is to maximize the reward for the player with the lowest reward. The authors propose a decentralized algorithm called Decentralized Fair Elimination (DFE), which improves the existing regret upper bound from $O(\log T \log \log T)$ to $O({\log T}/ {\Delta})$. Additionally, a matching lower bound is provided, demonstrating the optimality of the proposed algorithm. The effectiveness of the algorithm is also verified through numerical experiments.

### Strengths
1. The DFE algorithm addresses fairness without requiring a central coordinator, making it scalable to larger systems and addressing practical concerns in decentralized settings like wireless networks.

2. The algorithm proposes a novel exploration assignment strategy that ensures even exploration across player-arm pairs, which leads to efficient elimination of sub-optimal arms and reduces overall regret.

3. The authors provide both a theoretical analysis (including regret upper and lower bounds) and empirical validation through simulations.

### Weaknesses
1. In remark 1, the authors claim that "we could still use collisions to transmit information bit by bit, resulting in an additional constant length of information bits without the communication assumption." However, using collisions to transmit information, players should quantize UCB/LCB estimates to avoid potentially infinite communication length upon communication, as these numbers are often decimal numbers. To ensure that the elimination phase remains work despite the quantization errors, the required communication length would need to be on the order of $O(\log 1/\Delta)$. Given that the number of epochs is $O(\log T)$, this results in an additional term of $O((\log T \log 1/\Delta))$ in the regret bound. Furthermore, the paper does not specify how the players would agree on a common quantization scheme in a decentralized manner, which is a critical detail for practical implementation.

2. Could the authors elaborate on why the inequality in line 698 holds? The paper does not provide any explanation for this, and additional details would be greatly appreciated. Additionally, I am unsure if the definition of $\Delta_{i,k} = \gamma^* - \mu_{i,k}$ is meaningful, as this value can be non-positive. Specifically, if $\mu_{i,k}$ is greater than $\gamma^*$, then $\Delta_{i,k}$ would be negative, which contradicts its use in the regret analysis where it is implicitly assumed to be a positive quantity. This needs to be clarified for the theoretical analysis to be sound.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
3
