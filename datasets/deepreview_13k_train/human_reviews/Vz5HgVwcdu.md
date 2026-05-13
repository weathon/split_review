# Complexity of Injectivity and Verification of ReLU Neural Networks

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Neural networks with ReLU activation play a key role in modern machine learning. Understanding the functions represented by ReLU networks is a major topic in current research as this enables a better interpretability of learning processes. 

Injectivity plays a crucial role whenever invertibility of a neural network is necessary, such as, e.g., for inverse problems or generative models. The exact computational complexity of deciding injectivity was recently posed as an open problem (Puthawala et al. [JMLR 2022]).
We answer this question by proving coNP-completeness. On the positive side, we show that the problem for a single ReLU layer is still tractable for small input dimension; more precisely, we present a parameterized algorithm which yields fixed-parameter tractability with
respect to theinput dimension.

In addition, we study the network verification problem which is of great importance since neural networks are increasingly used in safety-critical systems. We prove that network verification is coNP-hard for a general class of input domains. Our result thus highlights that the hardness of network verification is intrinsic to the ReLU networks themselves, rather than specific input domains. In this context, we also characterize surjectivity for ReLU networks with one-dimensional output which turns out to be the complement of a basic network verification task. We reveal interesting connections to computational convexity byformulating the surjectivity problem as a zonotope containment problem.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the computational challenges and theoretical limitations associated with key properties of ReLU neural networks: injectivity, verification, and surjectivity. These properties are important for applications that rely on the reversibility and reliability of neural networks, such as generative models, inverse problems, and safety-critical systems like autonomous vehicles. These findings deepen the understanding of ReLU network behavior, particularly for applications where robustness and accuracy are critical.

### Strengths
This paper makes a valuable contribution to the theoretical understanding of ReLU neural networks, particularly concerning injectivity, verification, and surjectivity, by rigorously analyzing these problems’ computational complexity. Below is an assessment based on originality, quality, clarity, and significance.

**1. Originality**: The paper tackles the novel and previously open question of the computational complexity of determining injectivity in ReLU networks, establishing its coNP-completeness. This result is particularly impactful because injectivity is a fundamental property for many applications where reversible or unique mapping is essential. The authors also creatively connect network surjectivity with a zonotope containment problem, revealing links between neural network analysis and computational geometry. Additionally, the paper’s formulation of the verification problem as a coNP-hard challenge within ReLU network structure itself—independent of specific input conditions—is an insightful addition. This treatment expands our understanding of why verification is so difficult across many practical applications, which sets this work apart from prior studies focused on domain-specific hardness assumptions.

**2. Quality**: The theoretical rigor of this work is apparent, with thorough proofs supporting the coNP-completeness of injectivity and the coNP-hardness of verification. By also providing parameterized complexity results for small-dimension cases, the authors have strengthened the practical relevance of their findings. The authors appropriately cite foundational work and carefully build upon it, ensuring that their proofs are grounded in established literature while providing new contributions. However, including more experimental or empirical validations of these theoretical results (e.g., demonstrating the parameterized algorithm on real or synthetic networks) could further reinforce the paper’s quality and applicability.

**3. Clarity**: The paper is generally well-structured and organized logically, progressing through definitions, results, proofs, and implications. The separation between theoretical complexity results and parameterized algorithms is well-done, allowing readers to follow the main contributions without confusion. However, the paper is dense, and certain sections, particularly around zonotope containment and parameterized complexity, may benefit from clearer explanations or examples to improve accessibility. For instance, more intuitive descriptions or visualizations of zonotope-related results could enhance understanding for readers who may not be familiar with computational geometry.

In summary, this paper is a substantial and rigorous contribution with theoretical insights that carry practical implications. Its originality, depth of analysis, and potential influence on further research in neural network properties make it a valuable addition to the field. Improvements in clarity and empirical validation would further enhance its impact, but overall, the paper is a high-quality work that addresses foundational questions in neural network theory.

### Weaknesses
This paper makes a significant theoretical contribution to the study of ReLU networks, but there are several areas where it could be further improved to enhance both its rigor and accessibility. Here are some specific areas for improvement:

**1. Limited Empirical Validation**: While the paper focuses on theoretical complexity results, an empirical component could improve its practical relevance. Implementing and testing the parameterized algorithm for injectivity on networks with small input dimensions or low neuron counts would provide insights into its effectiveness and limitations in real-world scenarios. Demonstrating the algorithm on a range of synthetic and small real datasets could validate the algorithm's runtime and parameter tractability claims, offering a concrete sense of its usability and performance. Additionally, practical experiments to showcase the difficulty of network verification and injectivity in deeper, multi-layer ReLU networks could help underscore the paper’s theoretical findings for readers in applied fields. An empirical analysis could reveal how these challenges scale and manifest in network training and verification processes.

**2. Limited Discussion on Practical Implications and Trade-offs**: While the paper addresses theoretical complexity boundaries, it lacks a nuanced discussion on the practical implications of these results for neural network practitioners. For example, the paper could delve into how the coNP-hardness of verification and injectivity should guide network architecture choices, especially in domains where reliability is paramount. It would be valuable to suggest actionable insights for practitioners, such as how to prioritize aspects like layer depth, dimensionality, or neuron count to balance network expressivity with computational feasibility. In the discussion of parameterized complexity results, additional analysis of where these results might realistically apply in common architectures could also be beneficial. For instance, clarifying the practical relevance of fixed-parameter tractability in applications where dimensionality is inherently high (e.g., vision tasks) would help readers understand where these findings might or might not be beneficial.

**3. Limited Exploration of Related Work in Neural Network Verification**: While the paper provides foundational complexity results, the treatment of related verification research could be expanded. There has been recent work on heuristics and approximation methods for ReLU network verification, which could provide important context here. Reviewing recent approaches to approximate verification or discussing alternative methods that offer partial or probabilistic verification could provide readers with additional avenues to explore beyond purely theoretical boundaries. Specifically, citing and discussing recent advancements in heuristic-based and constraint programming approaches to verification could frame the authors’ results within the current landscape of neural network verification tools and methods. This contextualization would help readers understand both the novelty and the limitations of purely theoretical approaches in applied contexts.

### Questions
1. The relationship between zonotope containment and ReLU network surjectivity is intriguing but could be more accessible. Could you provide a more intuitive explanation or visualization of this connection? Could you also provide illustrative examples of injective/surjective/bijective ReLU networks?

2. Given the coNP-hardness of injectivity and verification, how should practitioners approach network design to avoid infeasibility? Are there specific heuristics or guidelines that could help manage these complexities?

3. The paper focuses on theoretical hardness but doesn’t discuss how existing heuristic or approximate verification methods could be employed in light of your results [1-3]. Could you comment on where your results might influence the development or improvement of such methods?

4. Neural network verification is a computationally demanding process and has been shown to be NP-hard even for simple neural networks with a single hidden layer [1]. Could the authors clarify the novel contributions of your coNP-hardness result compared to existing NP-hardness results. Specifically, how your result provides new insights or implications for verification techniques that weren't apparent from previous hardness results?

5. Could you provide more insight into the chosen parameterization for injectivity (in terms of input dimension) and its realistic applicability? For example, how might this approach scale in contexts where input dimensionality is inherently high, such as in image recognition (e.g., MNIST images vs. high-resolution images)?

6. Given the exponential runtime for injectivity checking based on input dimension, is there potential for further optimization or approaches for improving the algorithm's efficiency? Additionally, could you discuss any possible conjecture about the lower bounds that might limit algorithmic improvement?

[1] Katz et al. 2017, Reluplex: An efficient SMT solver for verifying deep neural networks.
[2] Zhang et al. 2018, Efficient Neural Network Robustness Certification with General Activation Functions.
[3] Singh et al. 2018, Fast and Effective Robustness Certification.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the complexity of deciding injectivity of a ReLU neural network. It is shown that the problem is coNP-complete. It is also shown that neural network verification (e.g., robustness verification) is coNP-hard, for "reasonable" sets in the input space (essentially, any set that contains a ball). Finally, it is also shown that deciding the surjectivity of a ReLU network is NP-complete. An explicit connection is drawn between deciding the existence of an input leading to a positive output under a scalar-valued 2-layer ReLU network, and the non-containment of two zonotopes. This gives rise to another explanation for the NP-hardness of determining positivity of a ReLU network.

### Strengths
The paper provides some answers to deep theoretical questions surrounding the complexity of certain decision problems in the analysis of ReLU neural networks. The results in this paper are certainly of interest to the ICLR community. Interesting open problems are posed to the community, in the conclusion of the paper.

### Weaknesses
I question the accessibility of this paper to the general ICLR audience. There is a lot of technical terminology used that is not defined for the general reader. The results in the main paper are all substantiated by rather imprecise proof sketches, rather than rigorous proofs. See also my Questions below.

I am still concerned about the level of detail in the proof sketches. For instance, in Proposition 4, the argument that non-injectivity can be verified by checking the feasibility of a linear program is not sufficient to justify the coNP-completeness result. The sketch does not adequately explain why finding the polyhedra $P$ and $Q$ is not a polynomial-time operation, which is crucial for the coNP argument. The sketch makes it seem like the problem is in NP, not coNP. Similarly, the use of terms like "extreme ray" and "polyhedral fan" without immediate definitions makes it challenging to follow the arguments, even with the added definitions later in the text. The connection between the zonotope containment problem and the ReLU network positivity problem also needs more elaboration to be fully convincing.

Furthermore, the notation $w(E(S,V \setminus S))$ remains unclear. While the authors have clarified that it refers to the cut induced by $S$, the initial presentation and the subsequent use in line 404 still create ambiguity. The notation should be explicitly defined before its first use, and the distinction between the set of edges and the sum of their weights needs to be made clearer. The use of "digraph" instead of "directed graph" is also a minor point that could be addressed for clarity, especially since the paper is not exclusively targeted towards graph theorists.

### Questions
1. Line 79: "hardness results is" should be "hardness results are".
2. Line 137: You didn't define the acronym "wlog" (without loss of generality), which might confuse some readers that haven't seen it before.
3. Line 147: "forms a polyhedral fan" it would help the reader to recall the definition of a polyhedral fan.
4. Line 157: Do you mean to write $\phi\_{\mathbf{W}\_i,\mathbf{b}\_i}$ instead of $\phi\_{\mathbf{W}\_{n\_i},\mathbf{b}\_{n\_i}}$? Also, it seems like you should index your projection mappings as $\pi\_{i,j} \colon \mathbb{R}^{n\_i}\to \mathbb{R}$ (projection onto coordinate $j$), instead of $\pi\_{j} \colon \mathbb{R}^{n\_i}\to \mathbb{R}$, since its domain depends on $i$.
5. Line 168: The set $\mathcal{R}$ is technically not well-defined since $\mathbf{r}\_\rho$ is not unique, although I see what you're getting at. If you can easily update things to make $\mathcal{R}$ well-defined, that would be great. (For example, would it work to take $\mathbf{r}\_\rho$ as the unique unit vector generating the ray $\rho$?)
6. Observation 3: Again, you're using terminology that may not be immediately accessible/commonplace for most ICLR readers; you should define what an "extreme ray" of a polyhedral cone is.
7. Line 176: I think that this brief recap of P, NP, NP-complete, coNP-complete, XP, and FPT is great, but that it should be included earlier in the paper, before the terms XP and FPT are used (otherwise, you might lose some readers early on in the introduction as soon as XP and FPT are mentioned). For example, can shorten these descriptions even more, so that you can squeeze them into the introduction right before line 58?
8. Line 196: Again, I suggest you define your acronym LP (linear program).
9. Proposition 4: The provided proof sketch might cause confusion, since what you're saying looks like deciding non-injectivity is polynomial time as it reduces to a linear programming feasibility problem. So, why then would determining injectivity be in coNP based on this interpretation of your proof sketch?
10. Line 223: Again, you're using terminology that might be unfamiliar to some readers, without defining it (e.g., "digraph" instead of directed graph, weakly connected, acyclic, etc.---not all ICLR readers are graph theorists).
11. Line 242: Typo ("completenss" instead of "completeness").
12. Line 384: What do you mean by the notation $w(E(S,V \setminus S)) > 0$? Are you referring to the condition that $w(e) > 0$ for all edges $e \in E$ connecting a vertex $v\in V$ to a vertex $v' \in V\setminus S$? If so, it would be great to define this for the reader, since the notation seems sort of nonstandard.
13. As a follow-up to my above question, line 404 makes it look like $w(E(S,V\setminus S))$ equals the sum of weights of all edges connecting vertices in $V$ to vertices in $V\setminus S$. In my opinion, this makes it even like likely for the reader to assume what you mean by the notation $w(E(S, V\setminus S))$.
14. Line 440: Do you mean $\mathbf{v}^+,\mathbf{v}^{-}$ instead of $\mathbf{v}^+,\mathbf{v}^+$?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper states that the computational complexity of deciding infectivity for ReLU networks is coNP-complete. To prove this, they first show that $l$-layer ReLU injectivity is in coNP. They proceed then to show that it is also coNP-hard. However, they proceed to claim that for a single hidden layer, the problem is still tractable as long as the input dimensions are few. 

They then study the network verification problem and prove that the network verification is coNP-hard for a general class of input domains. To do that, the authors define the notion of *reasonable* sequence of subsets and show that the the problem of deciding if a single hidden layer ReLU network outputting scalars is strictly positive is NP complete. They then proceed to prove coNP-hardness. The authors claim that the results highlight that the hardness of network verification is intrinsic to ReLU networks rather than the input domain.

### Strengths
The complexity of network analysis is an important area of research. In general, universal approximation and robustness are important results and an important theoretical justification in the field. The writing and presentation is mostly clear. While many results, especially in the beginning where attributed to prior works, later results appear mostly novel. Further, intuition was provided throughout the paper.

### Weaknesses
Regarding the presentation, i encourage the authors to lighten the paper with some illustrations where appropriate. Further, it would be good, to have some intuition regarding the reduction to the graph problems in the paper. However, the biggest weakness of the paper is the missing related work. It is unclear how it relates to results on universal approximation for networks certified with convex relaxations like intervals [1,2,3,4] and specifically the hardness result presented in [2]. The hardness result in [2] specifically shows that approximating the range of a three-layer network with specific activation functions is NP-hard, and it is unclear how this relates to the coNP-completeness result for injectivity of ReLU networks presented in this paper. The authors should clarify the relationship between these two hardness results. Further, the claims made in the conclusion appear too strong to me (see questions).

Missing related work: 
1. Baader et. al. "[Universal Approximation with Certified Networks](https://openreview.net/forum?id=B1gX8kBtPr)", ICLR 2020
2. Zi et al. "[Interval universal approximation for neural networks](https://dl.acm.org/doi/abs/10.1145/3498675)", POPL 2022
3. Mirman et al. "[The Fundamental Limits of Neural Networks for Interval Certified Robustness](https://openreview.net/forum?id=fsacLLU35V)", TMLR 2022
4. Baader et. al. "[Expressivity of ReLU-Networks under Convex Relaxations](https://openreview.net/forum?id=awHTL3Hpto)", ICLR 2024

### Questions
- The claim in the conclusion to exclude polynomial-time algorithms seems to be too strong based on the analysis presented, as worst case complexity was analyzed. How does this claim compare to the results of [1,2,3,4]?
- Do the authors have an intuition how their bound relate to certification in practice? I.e. not assuming worst case networks or assuming that it is fine that certification sometimes failes / times out?
- Can the authors provide some intuition regarding the reduction to the graph problems in the main paper? 

**Minor questions**
- For Definition 2, is there a reason why you decided not to write $\phi_{W_l, b_l} \circ \cdots \circ \phi_{W_1, b_1}$ and instead spell $\phi_{W_l, b_l}$ out?
- In Line 440 pint a) - i suppose it should be $v^+, v^-$, yes?

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
3

### Summary
This paper studies the complexity class of determining injectivity, surjectivity and robustness verification of ReLU networks. It proves the corresponding complexity class of each problem.

### Strengths
This paper, if the proofs are correct, should be quite novel and point out the algorithmic complexity of some problems. However, due to the writing, it is impossible for me to check the proofs end to end, even as a researcher who authored many purely theoretical papers.

### Weaknesses
The first thing bothers me is the problem itself: determining the injectivity of a ReLU network. First, when the network maps 1d input to 1d output, injectivity and continuity (naturally hold for ReLU networks) implies monotonicity. Second, in high dimensions, a function mapping from $\mathbb{R}^m$ to $\mathbb{R}^d$ with $m>d$ cannot be injective. Third, if we only consider injectivity inside a compact input set, as long as at least one neuron could be dead in the network inside this input set, this ReLU layer is not injective, and the composition of the ReLU layer with any other functions cannot be injective. Based on this facts, I fail to see how the conclusion could be correct: deciding the injectivity of a mapping from $\mathbb{R}^m$ to $\mathbb{R}$ is hard. Note that deciding whether all neurons cannot be dead in a ReLU network is easy: if all neurons in previous layers are active, they are then linear, and can be collectively merged together into a single linear layer; then, applying IBP [1] on a single linear layer results in precise bounds [8], and we can easily derive whether neurons in the current considered ReLU layer are all active.

Second, the authors write about robustness verification, but other than citing Katz et al., most of the related works are nonsense. For example, Line 110 mentions that heuristic approaches for verification exist, but instead of citing many established verification algorithms, they cite some random papers that aren't important enough. For example, they should at least cite methods such as IBP [1], DeepPoly [2], DeepZ [3], general cutting planes [4], multi-neuron certification [5], etc. and libraries such as LiRPA [6] and CTBench [7]. Line 115 also cites some random papers to support that the expressivity of ReLU nets is important.

Third, the authors state that the conclusion of Katz et al. only applies to polyhedra input sets and does not generalize, which I kindly disagree with.  Just like the authors did to generalize, a well-behaved input set contains lots of polyhedra, and Katz et al. have proven that even verification in those subsets is hard. Therefore, I fail to see how their conclusions generalize the result from Katz et al.

### Questions
See weakness. Overall, I suggest the authors at least improve the writing of their proofs, e.g., making them more intuitive and highlighting the intuition and main results instead of throwing everything at the reader. This brings bad practice to the theory field.

### Soundness
2

### Presentation
1

### Contribution
2
