# Networked Communication for Decentralised Agents in Mean-Field Games

- Decision: Reject
- Avg Score: 3.80
- Scores: 1, 3, 6, 6, 3

## Abstract
We introduce networked communication to the mean-field game framework, in particular to oracle-free settings where $N$ decentralised agents learn along a single, non-episodic run of the empirical system. We prove that our architecture has sample guarantees bounded between those of the centralised- and independent-learning cases. We provide the order of the difference in these bounds in terms of network structure and number of communication rounds, and also contribute a policy-update stability guarantee. We discuss how the sample guarantees of the three theoretical algorithms do not actually result in practical convergence. We therefore show that in practical settings where the theoretical parameters are not observed (leading to poor estimation of the Q-function), our communication scheme significantly accelerates convergence over the independent case (and sometimes even the centralised case), without relying on the assumption of a centralised learner. We contribute further practical enhancements to all three theoretical algorithms, allowing us to present their first empirical demonstrations. Our experiments confirm that we can remove several of the theoretical assumptions of the algorithms, and display the empirical convergence benefits brought by our new networked communication. We additionally show that the networked approach has significant advantages, over both the centralised and independent alternatives, in terms of robustness to unexpected learning failures and to changes in population size.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper aims to introduce networked communication to the mean field game framework and show how communication accelerates convergence of the learning. Two games are provided, namely, cluster and agree on a single target, to validate the proposed framework.

### Strengths
It introduces a practical communication network to accelerate the convergence of independent learning, without relying on a central learner.

### Weaknesses
1. The experiments have shown extensive results but only on two games. The insights are more on the practical side that introducing communication could benefit convergence.
2. The theoretical contribution of this paper is unclear. It showed that practically introducing communication could benefit convergence, but where the theoretical contribution lies is not well motivated.

### Questions
The statements are not clear. MARL is a learning framework assuming a finite number of N agents, while MFG is a game-theoretical framework with N-player limit. My understanding is that this paper aims to address the challenge in MARL when the population size grows, but still finite. Thus, it remains unclear how the proposed algorithm is related to MFG, and how MFG can help with the learning of N agents even under the communication scheme. Could the authors clarify the relationship?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates learning in mean-field games with a communication network. Specifically, previous work investigated centralized (communicate arbitrarily) and independent learning (no communication at all) in mean-field games. This paper extends the result to the cases when players can only communicate with some neighbors, which is an interpolation between the centralized and the independent cases.

The contribution of the paper is two-fold. Firstly, it shows that when players can communicate partially, the sample complexity is bounded between that of the centralized and the independent cases. Secondly, it shows that the algorithm will converge faster empirically with a replay buffer, including centralized, independent, and partially communicated settings.

[1] Batuhan Yardim, Semih Cayci, Matthieu Geist, and Niao He. Policy Mirror Ascent for Efficient and Independent Learning in Mean Field Games. In International Conference on Machine Learning, pp. 39722–39754. PMLR, 2023.

### Strengths
- The authors provide experiments to justify the results.
- Using a communication network to interpolate between centralized and independent learning is interesting.

### Weaknesses
## Main Concerns
- The theoretical results in this paper do not show the superiority over independent learning. The assumptions in Theorem 3 are too restrictive ($\tau_k\to 0$) and the gap $(\frac{1}{d_{\mathcal G}})^C$ is small.

## Minor Weaknesses
- Writings: The writing of this paper can be further improved.
  - For example, in Section 3.2, where the authors first introduce $\sigma_{k+1}^i$, the authors may add a brief explanation about what it is and why it is needed for the algorithm.
  - On line 376, when $C\geq d_{\mathcal G}$, it is not $(\frac{1}{d_{\mathcal G}})^{C}=0$ but instead that term in the bound above disappears. Moreover, the current bound is not rigorous since the number of policies does not decrease uniformly in most graph structures. For instance, in a random graph with each player $w$ degrees, $E[\Delta_{k, C}]=O(N-w^C)$. Therefore, an accurate estimation of $\Delta_{k,C}$ might be better.


### Questions
- In Theorem 3, when $C$ grows larger, why does the gap between learning with partial communication and independent learning seem to be smaller instead of larger? Since more communication may further stabilize the learning process.
- Why when $d_{\mathcal G}$ is 1, the gap between learning with partial communication and centralized learning is 1? Since they are now identical to each other. Also, I'm wondering why the gap between learning with partial communication and independent learning is 0 when $d_{\mathcal G}$ is 1.
- Why is there no ablation study of replay buffer?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a networked communication multi-agent reinforcement learning framework to solve mean-field games. The paper first provides theoretical insights into this networked communication paradigm, including the conceptual, sample efficiency, and convergence speed relationships between networked communication learning and centralized versus decentralized learning approaches. Based on this, the paper presents the practical implementation of the paradigm, including a specific method for generating communication content and the introduction of an experience replay buffer to accelerate learning. Through experiments on two grid-world scenarios, the authors demonstrate that the networked communication-based algorithm achieves performance comparable to centralized algorithms, along with higher robustness.

### Strengths
1. The theoretical analysis in the paper is comprehensive and aligns with intuition. The authors point out that the networked communication paradigm conceptually lies between centralized and decentralized approaches and demonstrate that this is also true in terms of sample efficiency and convergence speed, which is very interesting.
2. The experimental results demonstrate that the networked communication method is robust and high-performing, combining the advantages of centralized and decentralized framework. This is consistent with the authors' claims.
3. The paper is well-written and easy to follow. The authors provide all the necessary theories and experimental settings in the main text, with more detailed proofs and specifics included in the appendix.

### Weaknesses
1. In the theoretical section, the authors present a highly general framework (Algorithm 1), which can evolve into various specific algorithms by adjusting parameters. However, I note that the authors do not compare their practical algorithm with existing MFG algorithms in their experiments. Specifically, the paper lacks a direct comparison to other algorithms that solve mean-field games, making it difficult to assess the relative performance of the proposed method. The absence of such comparisons raises questions about the practical advantages of the proposed approach over existing methods. Can any existing algorithms be compared in the experiments?
2. The communication concept in the paper differs from the typical concept of communication in multi-agent reinforcement learning, which may cause confusion for readers. In those works, communication content between agents is often a learnable vector, such as parameters of a policy or value function. In contrast, the networked communication paradigm proposed here is more akin to an evolutionary paradigm, where the policies with higher estimated can propagate within the population. This approach, while potentially effective, deviates significantly from standard communication protocols in MARL, and the paper does not adequately address this difference or its implications.

### Questions
1. How much improvement in learning speed does the introduction of the experience replay buffer bring? 
2. How are the RL states specifically configured in the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers a networked learning setting for mean field games that is in-between centralized learning and independent learning. Agents independently learn as in prior work, but share policies through a graph to reduce sample complexity by spreading better policies. The main contribution is theoretical, implying that communication should result in better sample complexity than independent learning. The resulting algorithms were also empirically verified on two problems.

### Strengths
- The paper is very well written and very clear on the main ideas. 
- The work novelly fuses analysis of networked learning with the more realistic recent independent learning concept in MFGs.
- The theoretical results from analyzing the number of independent learned policies are elegant, interesting and significant, as they imply the usefulness of communication in the field of learning in MFGs.
- The discussion of related work and placement of contribution is very extensive and good.

### Weaknesses
 - Although the primary contribution is theoretical, the empirical results are limited in terms of considered problems and their complexity. The exact definition of the problems remains unclear to me, but as far as I understand there is no example with mean field interaction in the state dynamics. 
- The performed empirical changes discussed on page 10 were not empirically shown to be important / no ablation was performed.
- The robustness results are limited to failure in the communication networks and naturally the numbers of agents, so I am not sure what is the benefit over independent learning for robustness.
- See also questions below.

### Questions
- What is the benefit over independent learning and centralized learning in terms of robustness? In Fig. 3 it seems to me that all the curves observe the same relative shock. 
- I am not sure why it would make sense to "cooperate" in a competitive game (sharing policies with other agents).
- Could one consider other types of robustness, e.g., against self-interested agents manipulating the policies of others, or model errors / heterogeneity?
- How is the approximation of decrease in divergence obtained in Appx. B.7?
- Figures 1, 2, 3 are hard to read due to their small size. What is depicted in the shaded region?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies mean field games in which there is assumed to be a stationary distribution of agents’ state at equilibrium. The authors propose an algorithm for networked policy learning in these games, prove that its performance interpolates that of purely independent and centralized learning schemes, and evaluate the performance of all three approaches in two toy problems. This evaluation shows that the proposed approach works well in parameter regimes and with algorithmic modifications which are not explained by the theory.

### Strengths
The main theoretical result is particularly interesting: it is quite intuitive that learning in a networked setting would interpolate the performance of independent and centralized schemes, but proving that this is so is a very nice contribution.

### Weaknesses
* It would be better if the limitations and future work were included in the main text, not the appendix.
* Operator \Gamma_q is not defined properly in the main text. First use is on line 233.
* It would be useful to provide some explanation of what is going on in Definition 7 for readers unfamiliar with Yardim 2023.
* The construction of Definition 8 is not self-contained. All variables ought to be clearly defined in the main text; otherwise the paper is very difficult to understand.
* Nitpick: I suggest moving Alg. 1 up 1 page, so that one does not need to scroll so much between its introduction on line 256 and the algorithm itself.
* The prose description of the algorithm in Sec. 3.2 is difficult to understand as it refers to terms and relations which are not on the same page. I suggest defining all terms formally and precisely inline with proper equation numbers, and structuring the description at a high level with paragraph headers whose titles describe what is going on.
* I also suggest adding comments in the algorithm in order to make it more clear what is going on in different parts. Currently, it is hard to parse because there are so many symbols that were not clearly defined in the main text, and are also not explained in the algorithm block clearly enough to make sense of them without referring back to the main text and trying to connect the dots. For example, I have no idea what \sigma^i_k is precisely, and can only deduce that it is a scalar by examining its use in line 15 of Alg. 1. Line 351 says it can be chosen at random (on line 11 of Alg. 1), but that only adds to my confusion.
* \epsilon is undefined in Thm. 2.
* Graph diameter is never defined as far as I can see.
* The transition buffer usage appears to be a major contribution of the paper, yet it is not described precisely in the final subsection of Sec. 3.
* Fig. 1 is way too small to be readable. All text should be readable by the naked eye. (Same for Fig. 2 and Fig. 3.)
    * It is unclear how many independent trials these results are based upon. Confidence intervals are overlapping for many of the methods, which makes it difficult to visually distinguish between them, and also makes any statistical claims unclear. For example, stating that “our networked architecture significantly outperforms…” (line 508) does not really make sense because all the confidence intervals are so often overlapping, and without a direct pointer to a graph where this is not happening it is hard to justify that conclusion.
    * “Exploitability” is not defined as far as I see in the main text. Neither is “policy divergence.”
* More precise descriptions of the tasks and experiment setup should be provided in the main text of Sec. 4. Without additional information here, the results are difficult to interpret.
* It would be nice if there were figures (in the main text) illustrating the relative performance of the theoretically-sound version of the algorithm with the “hacked” version which breaks the theoretical guarantees but is claimed to perform better. This seems to be a major oversight in the results, since it is such an important part of the authors’ claimed contributions in the introduction and in the discussion on page 10.
* The point on line 538 does not make sense because it relies on something defined only in the appendices.

### Questions
* The restriction to stationary MFGs seems to be quite substantial, in the sense that — I can imagine — a player could have an incentive to act in a way which differs from how others act in some games, and that could plausibly lead to a change in the empirical distribution of agents’ state. By restricting ourselves to cases where this does not happen, are we removing potentially-important NE from consideration?
    * My sense is that the only reason for considering this restriction is that it allows us to write down policies as maps from agents’ individual state to action distributions. Without this restriction of stationarity, I believe we would need players’ policies to depend also upon the current (overall) state distribution. If this is the case, it would be helpful to explain things in this way to justify the restriction as necessary for tractability reasons.
* Thm. 1 asserts that there is a unique MFG-NE point. Under what conditions is this assured?
* In Thm. 3, why are there three different upper bounds being discussed? There only appears to be one ultimate upper bound for all three methods in Thm.  2, because the intermediate bounds are not quantified explicitly. Reading the equation on line 373, it seems like we are just talking about somehow roughly quantifying the differences between the three terms on the left of the equation on line 359. 
    * I don’t understand how (1/d_G)^C = 0 on line 376. That does not seem arithmetically possible.
    * I am not clear on how to interpret the \approx symbols in line 373. Is there a precise interpretation?
* It is unclear to me why the changes discussed on line 404 break the theoretical properties derived in the previous section. Especially because this is so central to the structure of the paper, I urge the authors to emphasize the relevant assumptions in the main text rather than punting so much to the appendices.
* The intuition in the paragraph starting on line 418 is very clear! Can the authors provide any theoretical analysis which supports this intuition? Or failing this, can the authors provide a clear remark explaining why such analysis is difficult so as to provide a template for future investigation on this topic?
* Why does the green networked curve appear to be doing better in Fig. 2 than it was in Fig. 1? Isn’t the scenario harder? What is going on here?
    * The statement “independent learners cannot do this and hardly appear to learn at all” is confusing because the reader must deduce on their own that this is referring only to the center subfigure and not to the others. Labelling subfigures would help.
* It is not quite clear to me how the proposed method is handling the change in population size. I suggest the authors clarify exactly how this is done.
* I would appreciate further discussion of the non-uniqueness issue raised in line 535, and how it relates to convergence to a single equilibrium as \lambda \to 0. It is not clear to me how coordination mathematically arises here, or why things do not break (e.g., due to ill-conditioning) as \lambda \to 0.

### Soundness
2

### Presentation
1

### Contribution
3
