# Two-Player Zero-Sum Differential Games with One-Sided Information and Continuous Actions

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Unlike Poker where the action space $\mathcal{A}$ is discrete, differential games in the physical world often have continuous action spaces not amenable to discrete abstraction, rendering no-regret algorithms with $\mathcal{O}(|\mathcal{A}|)$ complexity not scalable. To address this challenge within the scope of two-player zero-sum (2p0s) games with one-sided information, we show that (1) a computational complexity independent of $|\mathcal{A}|$ can be achieved by exploiting the "Cav u" property of behavioral strategies in incomplete-information games and the Isaacs' condition that commonly holds for control systems, and that (2) the computation of the two equilibrium strategies can be decoupled under the Isaacs' condition. We provide computational complexity of the resultant algorithm for approximating continuous-action mixed strategies (CAMS). Empirically, we demonstrate correctness of CAMS using a homing game where the Nash equilibrium exists analytically, and scalability through the same game with higher-dimensional actions. Codes available in [anonymous repo](https://anonymous.4open.science/r/iclr-3245).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an algorithm for solving two player zero sum differential games with one-sided information under the assumption that Isaac's condition holds. In particular, the paper exploits the fact that in a one-sided imperfect information game with a finite set $I$ of payoff types and  the imperfect information is on the payoff types, the game (which originally could have an infinitely large action set) can be reformulated as a a nonconvex-nonconcave problem of size $O(I^2)$, which can potentially be much smaller than the original game size. Then, the paper introduces an algorithm called Continuous Action Mixed Strategy solver that is able to achieve approximate Nash equilibria of the game with a complexity of $O(TNI^2 \epsilon^{-4})$. The key contribution of this paper is the characterization of a class of differential games for which tractable solutions can be found even with continuous action spaces, and the accompanying analysis of an algorithm which exploits the structure of the game to compute equilibria faster than SOTA methods.

### Strengths
- To my knowledge, this is the first paper that gives a framework to solve 2p0s differential games where the imperfect information is specifically about the payoff types and is one-sided in the sense that P1 obtains information about the payoff type before P2. While this seems like a fair niche class, the paper gives game examples from the literature that satisfy this condition, showing that the proposed algorithm performs well in practice and indeed shows time-invariance to increasing action sets since the underlying payoff types are invariant.
- The paper gives a thorough description and analysis of the specific class of games studied and the accompanying primal-dual reformulation. Overall a good description of why and when the proposed approach works is given, and the structure of the paper as a whole is good.

### Weaknesses
 - The paper gives a comprehensive analysis which crucially hinges on the assumptions of information asymmetry and a finite set of payoff types. However, there is a lack of explanation for when these assumptions are natural as well as when or how one can verify that a game lives in this class. It seems that Hexner's game is certainly an important game in this setting, but are there more game examples that can be shown to satisfy these assumptions? Specifically, while the paper claims that discretization of continuous payoff sets is common, it would be helpful to see a more detailed discussion of how the discretization process affects the solution quality and convergence properties of the proposed algorithm. Furthermore, the paper does not discuss the limitations of the finite payoff type assumption, such as the potential for information loss when the true payoff space is continuous. 
- There are a few typos in the paper (some are listed below), and the notation especially in the preliminaries are quite dense. The paper could be improved by taking more time/space to explain the notation (particularly for readers unfamiliar with differential games), perhaps in the appendix. The current presentation makes it difficult to follow the technical arguments, especially the transition from the original differential game to the primal-dual reformulation. A more detailed explanation of the mathematical steps and the underlying intuition would greatly improve the paper's accessibility.

Typos:
- References for Diplomacy seem to be broken, displaying as (, FAIR). 
- 'tractable solve' in the last line of the conclusion is a grammatical error.
- Some typos in the references, e.g. P Cardaliaguet vs Pierre Cardaliaguet; some proper nouns are not properly capitalized.

### Questions
- A question about the experiments on Hexner's game: Unless I am misunderstanding the results, the normal-form variants of Hexner's game you experimented with are all with finite $\vert A \vert$. Would there be an easy way to verify your results in a game where $\vert A \vert = \infty$ but $I$ is finite?
- Given that the games you study are of the pursuit-evasion type, would it also be interesting to study Stackelberg equilibria and algorithms to compute Stackelberg equilibria in this setup?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper studies zero-sum two player differentiable games with one-side information and infinite action space.
The paper shows that under some conditions (Cav u and Isaacs conditions) there exists an algorithm with complexity that does not depend on the cardinality of the action space. Experimental evaluation is provided

### Strengths
Finding algorithms with better dependency on the cardinality of the action space is an important topic.

### Weaknesses
The paper has important presentation issues. Someone non familiar with differentiable games has difficulty even understanding the setup. 
Moreover the authors do not make a great job at differentiating between their contributions and known results. In the reviewer's opinion the paper needs substantial rewriting.
For example, from section 3, it seems that the game is in continuous time, while the related works section speaks about cfr+ and deep CFR, which are designed for EFG. What is the exact setting considered by the paper? The theoretical grounding of the works seems to be based on Cardaliaguet (2007), which is based on different assumptions/language/theory than the works the authors cite as related works. This might be a strong point in favor of the paper (bringing concepts from another field into the computational game theory framework); however, the authors should invest more effort in relating the two. 
I even struggle to understand what the Cav u property is.

### Questions
Have you considered the online convex optimization point of view of learning in EFG? There, you consider a continuous actions space (although a polytope). More in general, games with continuous actions are not unfeasible to optimize per se. How does this relate?
What exactly are your technical contributions? Theorem 1 and related lemmas seem straightforward from existing results.
Is the game continuous or discrete time? How can you adapt something like CFR to work in continuous time?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors consider the problem of solving a differential two-player zero-sum game with one-sided information, meaning a game where only one player is informed about the "type" of the terminal function, i.e., the reward/loss function.

### Strengths
Unfortunately, I cannot identify any significant strengths in this work. The writing is so unclear that it is nearly impossible to follow.

### Weaknesses
Immediately upon beginning to read the paper, it becomes evident that it requires extensive rewriting. The phrasing is often either ambiguous or nonsensical. This issue is apparent even from the abstract, where the authors attempt to present their results with phrases like "a computational complexity independent of $|A|$ can be achieved," when they actually mean "a method/algorithm with computational complexity independent of $|A|$ can be achieved." They define CAMS as approximating continuous-action mixed strategies, but then ambiguously state “we demonstrate correctness of CAMS.”

Throughout the paper, there are missing articles and numerous errors. Additionally, the definition of zero-sum differential games is presented hastily; understanding the concept requires consulting other sources. Even the statement of the problem—that in zero-sum differential games, P1 seeks to minimize the terminal payoff function $g_i(x(T))$ (plus a running cost) while P2 aims to maximize it—is not clearly stated. The equilibrium, which is presumably the key concept, is not defined. Even in the introduction, the authors mention a no-regret algorithm without explaining what no-regret is. They reference no-regret algorithms, but the work instead presents a direct game-solving method, rather than focusing on minimizing regret. 

Furthermore, in the introduction, the authors claim to reformulate a convex-concave problem (which is not clearly articulated) into a nonconvex-nonconcave one (also not clearly articulated) that they assert can be solved easily, though without clear reasoning. Overall, there are missing explanations throughout, making it nearly impossible for the reader to follow. Here are a few additional specific examples:

- **Line 128**: The motivation for including the additional running cost $l(u,v)$ is unclear.
- **Line 130**: The phrase “has a value” is misattributed, and the concept of "the value" is only explained later on the page.
- **Line 143**: "to have pure Nash" lacks clarity and does not seem adequately explained.
- **Line 175**: In equation 5, the expected payoff includes $V_	au$ and $l(u,v)$, though the former represents the expected value of the terminal payoff plus the integral of the running cost $l(u,v)$.
- **Line 179**: The phrase “has a pure equilibrium” is not defined.
- **Line 179**: The sentence “If $U_	au$ is not convex in $p$, P1…” is nonsensical.

### Questions
Please read the comments above.

### Soundness
1

### Presentation
1

### Contribution
1
