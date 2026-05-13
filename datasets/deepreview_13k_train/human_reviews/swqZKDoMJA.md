# Decoupled SGDA for Games with Intermittent Strategy Communication

- Decision: Reject
- Scores: 6, 6, 8, 6

## Abstract
We focus on reducing communication overhead in multiplayer games, where frequently exchanging strategies between players is not feasible and players have noisy or outdated strategies of the other players.
We propose \textit{Decoupled SGDA}, an extension of Stochastic Gradient Descent Ascent (SGDA), where players perform independent updates using outdated strategies of opponents, with periodic strategy synchronization.
For Strongly-Convex-Strongly-Concave (SCSC) games, we demonstrate that Decoupled SGDA achieves near-optimal communication complexity comparable to the best-known GDA rates.
For \emph{weakly coupled} games where the interaction between players is lower relative to non-interactive part of the game, Decoupled SGDA significantly reduces communication costs compared to standard SGDA. 
Our findings extend to multi-player games. To provide insights into the effect of communication frequency and convergence, we extensively study the convergence of Decoupled SGDA for quadratic minimax problems. 
Lastly, in settings where the noise over the players is imbalanced, Decoupled SGDA significantly outperforms federated minimax methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies minmax optimization, and in particular, consider the case that players only have access to their own (noisy) gradient information, so they need to communicate frequently with other player to get update information. The goal is to design algorithms that take few iterations to converge, and at the same time, minimize the communication cost. 

The paper studies the strongly-convex and strong concave setting (and with some extra smoothness assumptions), and it introduces Decoupled SGDA, an extension of the Stochastic Gradient Descent Ascent (SGDA).
The idea is to let players perform independent updates using outdated strategies of opponents (i.e., the lastest communicated strategy), and only perform periodic synchronization. 
The paper proves that Decoupled SGDA achieves near-optimal communication complexity comparable to standard GDA rates.
They introduce the concept of "weakly coupled games" - where the interaction between players is relatively minor compared to their individual objectives - and show that in this regime, their method can significantly reduce communication costs. 

The paper also perform experiments on quadratic minmax optimization problem and toy GAN tasks to demonstrate the practical performance of the algorithm.

### Strengths
Overall, the paper makes solid contribution to minimax optimization. The idea of Decoupled SGDA seems to be fairly natural, but at the same time, it means the simplicity of the algorithm could make it practical.

### Weaknesses
The idea of the algorithm (Decoupled SGDA) is natural, and the analysis seems to be standard.



Minor issue:

I think the focus on the paper is on minmax optimization, instead of games (in particular, two-player zero-sum games are really really special case of games), so I suggest the author to properly changes the title to reflect this fact.

### Questions
.

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
3

### Summary
This paper studies the problem of reducing the communication complexity of decentralized optimization algorithms in strongly monotone games. The main contribution is a strategy called Decoupled SGDA, where each player conducts $K$ local updates using outdated strategies of the other players, followed by strategy synchronization. They provide convergence and communication complexity analysis for Decoupled SGDA and conditions under which Decoupled SGDA outperforms existing methods. Numerical experiments supports the theoretical results.

### Strengths
Reducing the communication complexity of decentralized learning dynamics in games is an important and timely problem. This paper uses games with intermittent strategy communication as a model for limited communication and gives a simple algorithm for better communication complexity. The algorithm is simple and versatile for adaptation of other methods. They provide both theoretical results and experiment results showing the advantage of the algorithm over existing methods.

### Weaknesses
1. Many notations (i.e., the Lipschitzness constant and the strong convexity constants) make the theorems less intuitive and hard to interpret. It would be helpful if the algorithm's complexity and comparison with other methods were discussed in more detail. Specifically, the use of distinct variables like $L_{uv}$, $L_{vu}$, $\mu_u$, and $\mu_v$ throughout the paper adds complexity without clear justification. A more streamlined notation, perhaps consolidating these into fewer parameters where possible, would significantly enhance readability. Furthermore, a more thorough discussion of how the communication complexity scales with these parameters, particularly in comparison to existing methods like Gradient Descent Ascent (GDA), would be beneficial.
2. Table 1 presents certain conditions under which the proposed algorithm is faster than existing methods, but the condition is less intuitive. It would be helpful to give concrete examples that satisfy these conditions. For instance, providing a specific class of functions or a particular game setup where these conditions hold would make the theoretical results more tangible and easier to relate to practical applications. A more detailed explanation of the relationship between the parameters $L_c$, $\mu$, and the condition number $\kappa$ in the context of specific examples would be valuable.

### Questions
See weakness.
1. Could you give concrete examples that satisfy the conditions in Table 1?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an algorithm called Decoupled SGDA which extends stochastic GDA for the setting where information about players' strategies is noisy or outdated. In this algorithm, players update their strategies 'locally' using outdated strategies from the other players, and then perform a synchronization step to exchange all updated strategies. In strongly-convex-strongly-concave minmax games and in N-player strongly concave games that exhibits the weakly-coupled property, the paper shows that Decoupled SGDA demonstrates communication acceleration (i.e. reduced communication complexity) over baseline methods. Moreover, with a slightly stronger assumption on the coupling degree, Decoupled SGDA can be shown to exhibit communication acceleration over the optimal first order method FOAM in SCSC minmax games. Finally, the paper presents deeper analysis in several other regimes, including in quadratic minmax games with bilinear coupling between players, in a federated learning setup, and with a heuristic modification to the proposed algorithm called the Ghost Sequence. Moreover, the paper presents experiments that corroborate the theoretical results and also show interesting behavior in settings which are not theoretically studied.

### Strengths
- The paper studies an interesting problem setup with many real-world applications and possible extensions. The core research questions are well-formulated and motivated. Moreover, the proposed algorithm is intuitive and simple to implement.
- The paper presents convergence results for Decoupled SGDA, the proposed algorithm, in a number of game settings and shows a meaningful improvement in terms of communication complexity in these settings.
- The experiments presented are quite compelling and provide some interesting extensions to the theory, speaking to the efficacy of Decoupled SGDA.

### Weaknesses
 - There seems to be a discussion which is missing comparing the convergence rates of the proposed algorithm with standard methods in the literature. Table 1 compares the communication complexity of decoupled SGDA in comparison with existing methods, but it would also be interesting to have a table with the convergence rates to the minmax equilibrium, which would depend on $R,K$. Specifically, while communication complexity is a crucial metric, the actual convergence rate in terms of iterations to reach a certain accuracy is also important. The paper should include a comparison of the iteration complexity of Decoupled SGDA with other methods, showing how the local updates affect the overall convergence speed, not just the communication cost.
- The related work section on Federated Learning feels slightly misplaced given that only the experiments in Sec 5.3 are related to Federated Learning. Would it make sense to move the related work for FL to the appendix and expand more on the gradient descent/minmax optimization specific related work in the main text? This would help to focus the main body of the paper on the core contributions related to min-max optimization and make the connection to federated learning more of an extension rather than a core component of the paper.
- The notation for condition numbers $\kappa_u$, $\kappa_v$ are used before their definition (e.g. in the related work section, in the paragraph before Corollary 3). Meanwhile they are only defined at the bottom of page 6. This makes it difficult to follow the arguments in the related work section and understand the significance of the results being discussed. The paper should introduce the notation before it is used, or at least provide a forward reference to the definition.

- There are also several typos I've found, listed below:
    - Line 157: do denote should be 'to' denote
    - Line 209-210: intiualized should be initialized, and in the definition of (local-SGDA) the $x^u_{t+1}$ in the first summation should be $x^u_{t+i}$.
    - Line 390: Should this be Decoupled SGDA instead of Decoupled GDA?
    - Line 402: Decouped-SGDA should be Decoupled SGDA.
    - Figure 4: The right figure is denoted 'Left', and the reference to 5 links to the experiment section. Should this instead link to Appendix F?

### Questions
- How does Decoupled SGDA behave if the stepsizes are decreasing? Many of the existing results in the literature crucially depend on carefully chosen decreasing stepsize, so having a method which uses constant stepsize might be preferable. But regardless, I am curious how the convergence results change if (for instance) the local updates are performed with a decreasing stepsize.
- The fact that only the noise on the self-gradients needs to be bounded for the Decoupled SGDA update seems unintuitive to me, can you comment on what the trade-off is? For instance, does this come at a cost of slower convergence rate if the gradients are too noisy, even if it does not affect the communication complexity?

### Soundness
3

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
The paper presents the Decoupled SGDA approach for multiplayer games with intermittent communication, where players only occasionally update their strategies based on the actions of their competitors. This model addresses scenarios where continuous communication is impractical due to noise, outdated strategy information, or communication constraints. The authors investigate its convergence properties under SCSC conditions and extend the analysis to weakly coupled games, demonstrating significant reductions in communication costs. They also conduct extensive experiments, comparing Decoupled SGDA to traditional federated minimax and standard SGDA methods, highlighting the proposed approach’s superior performance in both quadratic minimax and non-convex settings.

### Strengths
* The method achieves notable communication efficiency when the game is weakly decoupled.
* The analysis covers the SCSC setting and N-player games.
* Strong experimental results verify the theory.

### Weaknesses
 * The analysis is restricted to strongly convex and strongly monotone games, is it possible to extend to a more general setting?
* It seems the theoretical proof is standard and the technical contribution is weak.
* The practical advantage of the 'ghost sequence' in Algorithm 4 needs further clarification. It is not clear how this heuristic consistently improves performance over the basic method, and a more rigorous analysis or justification is needed beyond empirical validation.


### Questions
* In line 287, the function r(u,v) is not clear. Is this the same as r(u,v) in Eq. (5)?
* Regarding the 'Ghost sequence' proposed in Appendix G, could you explain the update of the ghost sequence in Algorithm 4?

### Soundness
3

### Presentation
3

### Contribution
2
