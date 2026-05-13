# Learning Imperfect Information Extensive-form Games with Last-iterate Convergence under Bandit Feedback

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
We study learning the approximate Nash equilibrium (NE) policy profile in two-player zero-sum imperfect information extensive-form games (IIEFGs) with last-iterate convergence. The algorithms in previous works studying this problem either require full-information feedback or only have asymptotic convergence rates. In contrast, we study  IIEFGs in the formulation of partially observable Markov games (POMGs) with the perfect-recall assumption and bandit feedback, where the knowledge of the game is not known a priori and only the rewards of the experienced information set and action pairs are revealed to the learners in each episode. Our algorithm utilizes a negentropy regularizer weighted by a virtual transition over information set-action space. By carefully designing the virtual transition together with the leverage of the entropy regularization technique, we prove that our algorithm converges to the NE of IIEFGs with a provable finite-time convergence rate of $\widetilde{O}(k^{-\frac{1}{8}})$ with high probability under bandit feedback, thus answering the second question of \citet{Fiegel2023adapting} affirmatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an algorithm for two-player zero-sum imperfect information extensive-form game with bandit feedback. The algorithm ensures that if both players use it simultaneously, the last iterate of their strategies converge to the Nash equilibrium in a rate of t^{-1/8} (or t^{-1/6} in expectation). The technique is based on negative entropy regularization that has been utilized in normal-form game / Markov game, with the additional technique called virtual transition.

### Strengths
- This works gives the first algorithm for 2p0s imperfect information extensive-form game with polynomial-time last-iterate convergence guarantee under bandit feedback. 
- This work introduces a virtual transition technique designed to regularize policy updates in extensive-form games, driving last-iterate convergence. This approach adapts the commonly used entropy regularization technique from normal-form games to the extensive-form game setting.

### Weaknesses
 - The work seems to be a straightforward extension from Cai et al. (2023), which studies last-iterate convergence in normal-form game with bandit feedback. This is not a major concern though, as it speaks more to the simplicity of the setting than to the insufficiency of the solution. 
On the other hand, though the virtual transition seems to be the main innovation of this paper, I am not sure whether it is indeed needed (see related questions in the Questions section).

 - The necessity of the virtual transition remains uncompelling. The justification for its inclusion appears to stem from low-level proof difficulties rather than a high-level algorithmic need. The algorithm's reliance on the virtual transition introduces a dependence on the learner's prior knowledge of the game's infoset structure, which is a limitation. In contrast, methods like Kozuno et al. only update based on visited infosets, avoiding this requirement.



### Questions
- Can you explain why 1/X * 1/p^x_{1:h}(x_h) <= 1 (claimed in the last line of Page 23)?  
- Does the algorithm still work if replacing the p^x(x_h) in Line 278 simply by 1/X (essentially making p^x a uniform distribution over infoset)?  If this is possible, then Line 278 is essentially not using virtual transition because you can absorb the factor 1/X into \epsilon_k.  If not, can you point out where the analysis might break? 
- I do not quite understand the explanation in Line 340-344. Why is bounding the stability of dilated negentropy critically relies on its closed form? This is not the case for general OMD.  Stability term is related to how much the iterate moves between rounds, and the stability term in a "more constrained case" is smaller than that in a "less constrained case". So why not the stability term in \Pi_max smaller than that in the entire space, and existing analysis suffices?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of learning approximate NEs in IIEFGs, with the perfect-recall assumption and bandit feedback. They propose an algorithm based on a negentropy regularizer weighted by a virtual transition. The proposed algorithm achieves finite-time last-iterate convergence and is fully uncoupled between the two players involved.

### Strengths
This paper is in general well-written and smooth to follow. The authors did a great job in introducing the background literature, and in motivating the design of the proposed algorithm. The theoretical results, namely the finite-time last-iterate convergence for learning approximate NEs in IIEFGs, are of vital importance in the literature, and the theoretical proofs seem to be rigorous. The results of this paper serve as an important step towards improving the last-iterate convergence guarantee.

### Weaknesses
Although the theoretical side of this paper is strong, simulation parts are completely missing. I would appreciate the authors could simulate the proposed algorithm on several example settings to validate the last-iterate convergence and potentially the rate of convergence.

Although the authors provide a justification for the constraint on the policy space, the specific choice of $\mu(a_h | x_h) \geq \frac{1}{A(k+1)}$ remains somewhat arbitrary. A more detailed explanation of how this particular bound affects the convergence rate, beyond a simple multiplicative constant, would be beneficial. The current justification relies on a trade-off between the regularization term and the distance to the true NE, but a more precise analysis of this trade-off is needed.

The role of the virtual transition, while explained, still lacks a clear, intuitive necessity. While the authors state it allows operating OMD in the space of visitation measures, the connection to the sequence-form representation in Eq (5) seems contradictory. The explanation that this allows for tighter bounds via Pinsker's inequality is not entirely convincing without a more detailed analysis of why the sequence-form representation is insufficient in this context. The justification for using the KL divergence with the virtual transition is also not fully clear, and a more in-depth discussion of why this particular divergence is crucial would be helpful.

### Questions
- Intuitively, why do you choose subset $\Pi_{\max }^{k+1}$ such that  $\mu\left(a_h \mid x_h\right) \geqslant \frac{1}{A(k+1)}$, and why constraining this feasible set won't affect the convergence?
- It is stated that employing the virtual transition helps to operate OMD in the space of visitation measure instead of sequence-form representations of policies. However, as is shown in Eq (5), the virtual transition is directly related to a sequence-form representation. Can the authors discuss more on this? And why operating OMD in the space of visitation measure is important?
- It seems that the virtual transition is fixed at the beginning (once the game tree is fixed), could one potentially define an adaptive virtual transition, utilizing the historical bandit feedback up till now to further improve the convergence rate?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies learning in partially observable Markov games with bandit feedback. An algorithm is proposed that leverages the negentropy regularizer weighted by a virtual transition over infosetaction space. The proposed algorithm is proved to obtain last-iterate convergence. A lower bound for learning in imperfect-information extensive-form games under bandit feedback setting is also provided.

### Strengths
The considered partially observable setting is significant in practical.The results are well-structured, and the analysis is explained in a way that flows smoothly, making it easy to follow despite the technical complexity. The introduction of the virtual transition seems to be novel in the proof. Overall this paper is well-written.

### Weaknesses
My main concern is the lack of experiments to support the theoretical results. I would be particularly interested in seeing how the proposed algorithm performs in practical game scenarios. The theoretical analysis, while well-structured, would benefit from empirical validation to assess its practical relevance and limitations. Specifically, the paper does not provide any concrete examples of games where the algorithm is applied, making it difficult to evaluate the practical impact of the proposed approach. Without experimental results, it's challenging to determine the algorithm's sensitivity to various game parameters, such as the size of the state space or the complexity of the game dynamics. Furthermore, the paper does not discuss the computational resources required for the proposed algorithm in practice, which is a crucial aspect for assessing its feasibility in real-world scenarios. The absence of empirical results makes it difficult to compare the proposed method with existing algorithms in terms of both performance and computational cost. 



### Questions
- What is the computational cost required in Algorithms 1 and 2?

- Is there any other method that can solve the game described in this paper? If so, how does the empirical performance compare?

Typo:
- In line 101, there are two 'to'.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper establishes the first finite-time last-iterate convergence for learning an appeoximate NE of IIEFGs in the bandit feedback settting. They prove that their algorithm achieves the last-iterate convergence of order $O(k^{-1/8})$ with high probability and of order $O(k^{-1/6})$ in expectation. Also, they provide the lower bound of order $\Omega(k^{-1/2})$ for learning IIEFGs  with last-iterate convergence guarantee in the bandit feedback setting.

### Strengths
This paper presents the first finite-time last-iterate convergence results for learning an approximate NE of IIEFGs in the bandit feedback setting. The proposed algorithm achieves a last-iterate convergence rate of $O(k^{-1/8})$ with high probability, $O(k^{-1/6})$ in expectation, and establishes a lower bound of $\Omega(k^{-1/2})$.

### Weaknesses
In my view, the theoretical contributions of this paper are sound and without weakness. My concerns are primarily focused on the following aspects:

- The paper's analysis of the limitations of previous regularizers is overly obscure and difficult to comprehend. Firstly, I do not fully understand why the vanilla negentropy regularizer is generally difficult to control the NE gap, given that it directly regularizes the sequence-form representation policies. Secondly, the authors claim that bounding the stability term of OMD with dilated negentropy critically depends on its closed-form update solution. However, when solving Eq. (2), I find that no closed-form solution is provided.

- The benefits of the proposed regularizer are not clearly articulated. Based on the current version, I do not fully understand the advantages of the proposed regularizer, such as its impact on proving the convergence results of the proposed algorithm.

- The convergence results presented in the paper seem to rely on the exact solvability of Eq. (2). However, Eq. (2) only yields an approximate solution.

### Questions
- Could you explain the limitations of previous regularizers? It would be best if you could provide some simple examples.

- Could you elaborate on the contribution of your proposed regularizer to the convergence results of the algorithm?

- Could you provide the computational complexity for solving Eq. (2)?

- Could you offer a brief experimental analysis? For instance, discussing the convergence rate and runtime of the proposed algorithm in Kuhn Poker and Leduc Poker.

### Soundness
3

### Presentation
3

### Contribution
3
