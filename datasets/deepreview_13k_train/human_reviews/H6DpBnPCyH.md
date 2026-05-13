# Reinforcement Learning for Finite Space Mean-Field Type Games

- Decision: Reject
- Scores: 3, 3, 8, 8

## Abstract
Mean field type games (MFTGs) describe Nash equilibria between large coalitions: each coalition consists of a continuum of cooperative agents who maximize the average reward of their coalition while interacting non-cooperatively with a finite number of other coalitions. Although the theory has been extensively developed, we are still lacking efficient and scalable computational methods. Here, we develop reinforcement learning methods for such games in a finite space setting with general dynamics and reward functions. We start by proving that MFTG solution yields approximate Nash equilibria in finite-size coalition games. We then propose two algorithms. The first is based on quantization of mean-field spaces and Nash Q-learning. We provide convergence and stability analysis. We then propose a deep reinforcement learning algorithm, which can scale to larger spaces. Numerical experiments in 5 environments with mean-field distributions of dimension up to $200$ show the scalability and efficiency of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a mean field type game (MFTG) with a finite number of noncooperative coalitions in which each coalition consists of a continuum of cooperative agents. Learning algorithms are proposed to solve approximate Nash equilibria in finite-size coalition games. Convergence and stability analysis are provided. Extensive numerical experiments are conducted.

### Strengths
Strength:
The paper is easy to follow with a clear logic from model formulation, equilibrium definition, algorithm implementation, to numerical experiments.

### Weaknesses
The novelty remains unclear. The authors are suggested to motivate readers in terms of what fundamental challenges an MFTG brings forth, of which learning algorithms and properties differ significantly from existing MFG and mean field control (MFC). The proposed two learning methods are incremental to the existing learning methods used for MFG. Reformulation with mean field MDPs is not new either.

Overall, this paper is more of a combination of existing concepts and methods for a mean field type game, rather than making fundamental contributions to the field of MFG or MFC.

### Questions
Could the authors provide more clarification in terms of why a finite space algorithm needs to presented first in Sec. 3 while having a DRL for Sec. 4? Using DRL for learning MFGs with large state and action spaces is widely used and well developed in MFG.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores the application of mean field games (MFGs) to learn approximate ϵ-Nash equilibria. The authors present several theoretical findings. One key result (Theorem 2.4) shows that, with sufficient Lipschitz constraints on the Markov game properties, the approximation error for the finite MFG can be bounded by $O(|S| \sqrt{|A|} / \sqrt{N})$. Another result (Theorem 3.2) demonstrates that, under similar Lipschitz bounds, the $\epsilon$-approximation error can be bounded by a linear function of these constraints, achieved via Nash Q-learning. In addition to the theoretical contributions, the authors present empirical results using the Deep Deterministic Policy Gradient (DDPG) algorithm. They demonstrate that, across multiple settings, the DDPG algorithm converges to an approximate Nash equilibrium.

### Strengths
- The paper addresses a relevant and practical problem, and the proposed technology could be applied to real-world scenarios such as cybersecurity and economics.

- The authors conduct a comprehensive empirical study, showing that the DDPG algorithm performs well in converging to an approximate Nash equilibrium.

### Weaknesses
 - The proofs of error bounds rely heavily on ensuring all components of the MFTG (reward, transition, policy, etc.) satisfy Lipschitz conditions. While this approach is valid, proving these conditions poses no significant technical challenge and may be considered borderline trivial.

- The authors claim to be the first to apply deep reinforcement learning (RL) to MFTGs, yet there are recent works (e.g., [1], [2]) that also explore similar applications. The paper does not adequately position its contributions relative to these advancements.

- There is a disconnect between the theoretical framework (based on Nash Q-learning) and the empirical results (focused on DDPG). The theoretical guarantees are established specifically for Nash Q-learning, but no similar results are provided for DDPG, resulting in a gap between the theory and the experiments.

### Questions
- In Section 2.3, the authors show an equivalence between mean-field games and Markov Decision Processes (MDPs). It is well known that MFGs can be represented as MDPs; were any new or useful features introduced in this reformulation to a mean-field MDP?

- In line 384, the authors suggest that solving the one-stage game is already intractable. Are we primarily interested in analyzing the sequential game outcomes, or does the focus remain on the single-stage game? This distinction is crucial, as the results between single stage game and sequential game may differ drastically.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper considers an extension of mean field games to many agents in coalitions that compete against each other. In the case of many agents, the infinite-agent case reduces the otherwise difficult problem to a classical finite player game, albeit with high-dimensional state-actions. As a result, the problem is analyzed and solved using classical techniques (Nash Q-Learning) and discretization / deep RL. The proposed algorithms are verified on a variety of examples, and compared to basic independent RL.

### Strengths
- The paper is well written and clear. 
- The work fuses existing ideas from MFGs with algorithms from both game theory and deep RL.
- The transfer of NashQ-based theoretical analysis and algorithms beyond classical mean-field RL (Yang et al., 2018) to mean-field games and mean-field-type games is interesting.
- The empirical evaluations and examples extensively demonstrate the potential of proposed algorithms.

### Weaknesses
 - The empirical significance of the paper is somewhat limited, as the experiments show only limited improvement in terms of exploitability over baselines, while the setting sounds a bit niche to me. I wonder if one could discuss more the significance of the setting, as I believe the referenced works (Tembine et al.) do not consider coalitions, but rather refer to standard MFGs as mean-field-type games.
- The theoretical results are limited due to many assumptions (Assumptions 1-8): The approximate Nash property in Theorem 2.4 requires an unusually strong condition on $\gamma$, and the algorithmic convergence (understandably) requires strong conditions on the stage games. To improve the applicability of the theoretical results, perhaps some assumptions in Section 2.2 could be relaxed or discussed more.
- The model and NashQ-based analysis are not highly novel, as partially remarked by the authors. The setting is also related to graph-based works, e.g., [1] considering infinite numbers of infinitely large coalitions through a double limit.

### Questions
- Is Assumption 3 required, or could one perhaps also consider smaller classes of policies, e.g., ones that do not depend on the deterministic-in-the-limit mean field?
- What is the difficulty in relaxing the strong condition on $\gamma$ in Theorem 2.4, as it is not required in classical MFGs [2]? 
- Could Assumption 8 follow from the previous assumptions?

[2] Saldi, Naci, Tamer Basar, and Maxim Raginsky. "Markov--Nash equilibria in mean-field games with discounted cost." SIAM Journal on Control and Optimization 56.6 (2018): 4256-4287.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper considers mean field type games which combine cooperative and competitive characteristics, i.e. agents form multiple cooperative coalitions but there is competition between coalitions. The authors focus on a quite general finite space case where they derive novel theoretical results and propose different learning schemes. They conclude their work with an evaluation of the proposed learning algorithms on different examples.

### Strengths
I think that this paper is a nice contribution to the MF(T)G literature and closes a conceptual gap in the existing literature. This work is well-written and structured. The assumptions for the theoretical results are clearly stated and discussed, and the Nash Q-learning algorithm is also analyzed rigorously. The algorithms appear to perform well on the given examples, and I liked that the authors provide both a mathematically tractable learning approach (Nash Q) as well as a scalable algorithm based on deep learning. Finally, the authors did a good job at discussing limitations of their current work.

### Weaknesses
Overall, I think the paper is sound and I did not spot major weaknesses. One general criticism that I have is that the presentation and formatting of the figures can be improved, e.g. by increasing font sizes and making captions more informative (see the following comments for details). Here are my comments:

- Lines 34-35: Mean field games were not (first) introduced in these references. I think the authors mixed these references up with the earlier works of Lasry and Lions (2007) and Huang, Malhame and Caines (2006), which would be the correct references here.

- Line 111, a small question regarding notation: Why do we need all $N_1, …, N_m$ in the superscript for the MF of coalition $i$? Wouldn’t it suffice and simplify notations if the superscript would just be $i, N_i$?

- Suggestion: One could define something like $\bar{N} \coloneqq (N_1, \ldots, N_m)$ or similar to abbreviate the following mathematical expressions.

- Assumption 3, potential typo: “The policies … satisfies” should be “satisfy”.

- The font size in most of the figures, especially Figures 1 and 3, is very small. Is it possible to increase the figure font size?

- Line 478: It says “Fig. 5 (left) shows the testing rewards”. Since Figure 5 is just one plot, what does “left” refer to here? Also, Figure 5 shows exploitabilities but not testing rewards.

- Line 481: There is a reference to Figure 1 here. Is this correct?

- Some of the figure captions, e.g. Figures 3 and 5, are very short and uninformative. For example, the caption in Figure 3 could at least mention that the exploitability is averaged over testing sets and players. And it should also briefly state what the bands surrounding the curves depict. In general, it should be possible to get a basic understanding of the figures without reading all details in the main text.

### Questions
1. Theorem 2.4: Could the authors please discuss the condition on the discount factor $\gamma (1 +L_\pi + L_p) < 1$? Especially, how restrictive is this inequality?
2. Example 1: I am not sure whether Example 1 is an expressive game. To my understanding, the optimal solution is rather trivial (Coalition 1 stays where it is, Coalition 2 moves to the state of Coalition 1) and I don’t see any potential conflict of interest between the two coalitions. Thus, my question is if the authors consider this game to be competitive in a strict sense on the coalition level? If so, what exactly are the coalitions competing about?
3. How scalable are the proposed learning algorithms with respect to a growing number $m$ of coalitions?

### Soundness
3

### Presentation
3

### Contribution
3
