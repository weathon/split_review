# Tractable Multi-Agent Reinforcement Learning through Behavioral Economics

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
A significant roadblock to the development of principled multi-agent reinforcement learning is the fact that desired solution concepts like Nash equilibria may be intractable to compute. To overcome this obstacle, we take inspiration from behavioral economics and show that---by imbuing agents with important features of human decision-making like risk aversion and bounded rationality---a class of risk-averse quantal response equilibria (RQE) become tractable to compute in all $n$-player matrix and finite-horizon Markov games.  In particular, we show that they emerge as the endpoint of no-regret learning in suitably adjusted versions of the games. Crucially, the class of computationally tractable RQE is independent of the underlying game structure and only depends on agents' degree of risk-aversion and bounded rationality. To validate the richness of this class of solution concepts we show that it captures peoples' patterns of play in a number of 2-player matrix games previously studied in experimental economics. Furthermore, we give a first analysis of the sample complexity of computing these equilibria in finite-horizon Markov games when one has access to a generative model and validate our findings on a simple multi-agent reinforcement learning benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Motivated by behavioral economics, this work proposes to investigate the combination of bounded rationality and risk aversion to define a regularized game leading to a new risk averse nash equilibrium concept. The main motivation of the paper is to introduce tractable equilibria in all n-player matrix and finite horizon Markov games. Notably, the introduced class of games is ‘tractable’ independently of the game structure while only depending on both levels of bounded rationality and risk aversion. The paper further proposes illustrations to motivate the games from the behavioral economics viewpoint and performs a few simulations to test the algorithms on simple examples. A sample complexity for finite Markov games under the generative model further completes the theoretical results.

### Strengths
- Writing is clear overall (I have some concerns for some aspects though, see next section) and the paper is well-organized. The proofs are well exposed in the appendix. 
- Investigating the tractability of games combining bounded rationality and risk aversion is interesting. In particular I find the idea of achieving tractability independently from the payoffs interesting. 
- The paper covers matrix games and their extension to finite horizon Markov games. More importantly the results hold for general sum games.  
- Modelling the behavior of decision making agents and their strategic interaction beyond expected utility theory is interesting on its own.

### Weaknesses
 - My main concern about this paper is the following question: What exactly makes the introduced games tractable? The paper argues that it is the combination of bounded rationality and risk aversion. I find the focus on tractability rather confusing. 
Risk aversion has its own motivation but it is unclear if it is required here for tractability. To be precise, I think the contribution in this paper is that you can achieve tractability (for computing another solution concept  than NE/CCE relating to a modified game) independently of the knowledge of payoff functions (their bounds I guess). More precisely, I think bounded rationality is already enough to allow for tractability but it should require some assumptions on the payoffs which this paper avoids. Please correct me if I have missed something here. The paper does not exactly present the contribution this way. In particular, I think the following statements would gain in clarity: 

-- l. 111-112: ‘RQE not only incorporates features of human decision-making but are also more amenable to computation than QRE …’ Why? There is no extended discussion about this whereas I believe it is essential to clarify the contributions. 

-- l. 235-238: While risk aversion might not be enough, I think bounded rationality should be enough (e.g. QRE as demonstrated in a number of works) under relevant assumptions on the structure of the game (mainly conditions on the bounded rationality level compared to the magnitude of the utilities/rewards). I find the presentation order confusing here. You start by introducing risk aversion and show its shortcomings as for the tractability of computing equilibria in such risk averse games to motivate the need of something else but equilibria should become tractable only with bounded rationality. 

-- From the title and the abstract (and throughout the paper), the emphasis is on tractability, as if both are actually needed to ‘achieve’ tractability. If this is not the case as bounded rationality is the main enabler, I would maybe highlight less this computational aspect and clarify that the combination brings you the possibility to achieve tractability under a condition on both levels of bounded rationality and risk aversion which is independent of the rewards. How does this condition compare to the one for say QREs? What’s the price to pay and advantages (if any) for RQNEs compared to QREs (beyond the advantage of incorporating risk aversion)? 

- Equilibrium collapse is briefly mentioned in l. 294. I would like to see a more in-depth description of how the results of this paper connect to the prior work regarding this phenomenon. It seems that the extended game you introduce seems to have some zero sum structure under a perhaps more stringent assumption than what you set (\epsilon_1 = \xi_{2,1} and \epsilon_2 = \xi_{1,2}, a condition satisfying your condition), under which J_1 + J_2 + \bar{J}_1 + \bar{J}_2 = 0. This can be seen from setting \lambda = 1/2 in your proof of Theorem 7 p. 21, l. 1133-1146. Is this an observation that connects to prior work about zero sum games and equilibrium collapse? It is also worth mentioning that setting \lambda = 1/2 leads to a condition that is consistent with your extension to the n-player setting (l. 1226-1232). 

- I think the introduction and motivation of (6) and (7) needs some improvement. Could you give more motivation and intuition? 

- The notations $\xi_1^*, \xi_2^*$ are quite confusing, especially that you also use the notations $\tau_1, \tau_2$ in Fig. 1 without defining them in the main part. What do you mean precisely by $\tau_1, \tau_2$ satisfy the conditions of Theorem 2 (l. 328)? How do the \tau s and \xi s relate?I believe one issue in the presentation is that you chose to hide \tau in the definition of the regularizer D without putting it in front of D (as it appears from the appendix). Maybe a solution is just to add the examples to the main part to clarify this and further comment on the relationship between the \xi s and \tau s. 

- Comments about experiments: While the paper focuses on RQREs, experiments do not seem to illustrate the concept. What are the RQREs in this game and why? Are they different from NEs? Why would they be more reasonable? 

- The introduction (and some other parts of the work e.g. l. 772-780), highlights the limitations of CCEs. Then Theorem 2 assumes access to a CCE of the 4-player game (which can be computed with a no-regret algorithm). While this CCE is for the modified (regularized) game and not the original one, why would this alleviate all the limitations that are inherent to CCEs in general and that you highlight in the paper? More specifically, the facts that the set of CCEs can be large, may have support on strictly dominated strategies and that stationary CCEs are PPAD-hard to compute in dynamic general sum games (l. 47-51). For the last point, does it mean that your output is also a nonstationary CCE since you also rely on no-regret algorithms (l. 8 of algorithm 1). 

- Dependence on the action space size: a host of theoretical results in the MARL literature have devoted efforts to ‘break’ the ‘curse of multi-agency’ and go from the product of action spaces to the sum. Your sample complexity is exponential in the number of players. While I understand that space might have been constraining, at least a comment is needed here on the theorem. The very last point of the conclusion mentions scalability but this is not clearly delineating the limitations of the result and why. 

- I have several other questions that I would like the authors to address for clarifying their contributions and the technical novelty.

Minor:
- l. 47-48: ‘the set of CCE can be large (introducing an additional problem of equilibrium selection)’: This equilibrium solution problem is already largely relevant for Nash equilibria, I find the argument confusing here. This is even more confusing since you also rely on CCE computation (for a modified game though) in the paper. 
- l. 305-307: H notations do not seem to be used in the main part. 
- l. 377, eq. (9): \tilde P V: the notation is a bit confusing here, I guess it is the usual dynamic programming notation but \tilde{P} \in \Delta_S and V \in R^S is a bit unclear, \tilde{P} is usually a matrix. 
- (24) l. 1045: for the argmax to be unique I guess you need D_i to be strictly convex w.r.t. p_i here. 
- Proposition 1 p. 20: bounded rationality does not seem to play any role in obtaining this result, this is probably worth mentioning.

### Questions
1. Could you please elaborate on how do you obtain figure 1? l. 69-71: ‘The markers … represent the necessary parameter values required to recreate the average strategy played by people in various 2-player games  in observational data…’
Could you please clarify this?  How do you find the values of the bounded rationality and risk aversion levels (or their ratio) only looking at behavioral data? Are you saying that you test several such ratios, computing the equilibria that you define in the risk averse and bounded rationality game (which ones? There are not a priori unique?) and then the deployment of the obtained equilibrium policy cpincides with the ‘average strategy played by people’ (whatever that exactly means). As Fig. 1 plays an important role in motivating your approach (at least as a motivating illustration for the games you consider), I would expect a more rigorous and precise description here in order to strengthen the message and clarify to. 

2. Are both risk aversion formulations (2) and (3) related by Jensen’s inequality? Any implications? 

3. Where is continuity w.r.t. both arguments of D needed? Does this exclude the examples of D considered in this work? It seems to exclude the ones considered in the appendix (because of continuity w.r.t. second argument that is likely not needed). While I understand that the space limitation is constraining, I think examples should appear in the main part. 

4. Could you rather state your condition as $\epsilon_1 \epsilon_2 \geq \xi_1^* \xi_2^*$ to include zero values of the parameters? This comes from your specific choice of $\lambda$ that cancels one of the terms in your proof. Note that a symmetric choice for lambda is also possible (cancelling the other term). Otherwise the condition looks non-symmetric (I can set $\epsilon_1 = 0$ but not $\epsilon_2 = 0$, similarly for \xi_1^*, \xi_2^*) whereas the game is symmetric. Is positivity of all these parameters needed? Comments about the corner cases would be welcome here. 

5. More generally, it seems that one of the key argument in the proof of the main result (theorem 7) (if not the only key argument) is the joint convexity invoked. Under which condition do CCEs and NEs coincide more generally? How does your result fit with such known existing results. 

6. l. 373: You put a continuity assumption for matrix games (l. 207) and consider lower-semicontinuity in l. 373. Any specific reason for this discrepancy? Which ones of the examples you provide in table 1 satisfies continuity w.r.t. both arguments? 

7. Definition 7: Why is there a deviation w.r.t. the horizon step and not just $\pi’_i, \pi_{-i}$? Is this standard? If I set $\epsilon_i = 0$ and remove the regularizers, do I recover the standard definition of NEs in finite horizon Markov games? 

8. Theorem 3: The condition you obtain for RAMG is not a generalization of the matrix games (two-player) one. Does this show some fundamental difference between the two player and multiplayer (\geq 3) settings? 

9. Eq. 19 p. 17: If you exclude the action a_i of player i from being subject to \rho_i, \pi_{-i}, I guess you would get a less stringent assumption than what you currently have. Is this right? Essentially, excluding k=i in (31). 

10. Can you provide a proof of Corollary 7.1? 

11. Proof of Theorem 4: Do the examples you provide satisfy the L lipschitzness of D wrt the l_1 norm for the 2nd argument, the first one being fixed? 

Minor: 
- You cite Tversky and Kahneman (1992) in l. 154-155: ‘a preponderance of empirical evidence suggests that people do not play their Nash strategies …’ To the best of my knowledge, there is no single occurrence of the word ‘Nash equilibrium’ in this paper. The reference is relevant  though for the risk aversion discussion at least for single agents and beyond as a reference in behavioral economics. 
- \sigma is introduced as a probability distribution over the product space P \times \bar{P}, then you also use it only for $\pi$ s (l. 317), perhaps a slight abuse of notation here. 
- I think Theorem 6 p. 18 should appear in the main part to make existence very clear. You report an existence result in theorem 1 for RNEs but you do not state it for the equilibrium which are the focus of the work. I understand that space imitation might have been the issue, but I think this is important. Suggestion: In that case maybe defer Theorem 1 to the appendix and move Theorem 6 to the main part? 
- l. 392: ‘non-linear sum over’ is this a sum? The terminology is confusing here, is it rather a composition or a recursion? 
- Please be precise in the statement of Theorem 4, this is a high probability result, the result holds with probability at least 1-\delta. 
- l. 452-453: the sentence needs to be revised, something missing.
- l. 515 ‘and goal states for agents as well as goal states of agents’, meaning? 
- l. 518: ‘To introduce multi-agent effects’, what do you mean exactly by these effects? Collisions? Are they possible in your implementation? 
- l. 529: why would agent 1 wait? Does agent 2 make it riskier for agent 1 to move if they move together? Can you explain? 
- l. 988: what do you mean by a strictly competitive game? 
- p. 21, l. 1132- …: The 1/2 does not seem to be useful in the proof. 
- p. 29: ‘to arrive at the CCE \sigma of the four player game’, is there a unique one?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates incorporating risk aversion and bounded rationality in order to tractably compute risk-averse quantal response equilibria (RQE) for n-player matrix and finite-horizon Markov games. The paper proposes computing the RQE is advantageous because it is tractable under certain conditions independent of the game structure and it models human behavior better. The conditions for tractability of RQE is stated with respect to degree of risk aversion and degree of bounded rationality. The connection between using no-regret learning algorithms and computing the coarse correlated equilibrium (CCE) of the 2n-player game and computing the RQE of the n-player game is provided. The method and the definitions are extended to Markov games and the experiment results on a toy Cliff Walk grid-world game is given which support the claims of the paper.

### Strengths
* Novel contribution while bringing a theoretically grounded view on risk aversion and bounded rationality to Markov games which can eventually be applied to more complex MARL scenarios. Adjusting the games so that RQE is achieved tractably by no-regret learning and having the tractability not depend on the underlying game structure is useful.
* Claims are supported extensively by proofs.
* The experiment on Cliff Walk demonstrates the risk averseness well.
* Paper is well written in general.

### Weaknesses
 * There is only one example game for Markov game results and it is very toy.
* Bounded rationality is less obvious than risk averseness on Cliff Walk experiments. Interpreting bounded rationality from the experiments is difficult.
* Paper has some minor typos (example line 160).

### Questions
* What is the significance of the choice of aggregate risk aversion and action-dependent risk aversion? When should we pick either one?
* Is there any advantage of converging to the RQE rather than optimizing to the optimal solutions, since the policies are to be used by artificial agents and the purpose is not to model human behavior? Is it only to be used because it is more tractable or do you foresee another significant use for it due to risk aversion and bounded rationality modeling?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper discusses multi-agent learning in a setting where the agents are risk-averse. By introducing risk aversion and quantal response into the agents' behaviour, the authors simplify computations to achieve a risk-averse quantal response equilibrium (RQE). This is accomplished via some clever tooling, applying a dual representation from [1] to convert the problem into a convex optimization problem under certain values of risk aversion. The trade-off is that it introduces n additional players into the game. The theory from the repeated game setting is then extended to the Markov game setting, where it establishes equivalence to the repeated game setting, quantifies the learning error, and implies convergence to RQE under specific parameter settings. A toy example is presented to convince the reader that the technology is functional.

[1] Föllmer, Hans, and Alexander Schied. "Convex measures of risk and trading constraints." Finance and stochastics 6 (2002): 429-447.

### Strengths
- The authors perform a rigorous analysis and provide convincing arguments for a well-defined system.
- The work could have real economic applications.
- There is good novelty in applying the dual formulation of [1] to this multi-agent setting and constructing the loss functions in Eq. (6) and (7).

### Weaknesses
 - The notation could be a bit confusing at times; the difference between $\pi$ and $p_i$ is not clearly defined and can be hard for the reader to follow. Specifically, it's unclear whether $\pi$ refers to a specific joint action profile or a distribution over joint action profiles, and how this relates to $p_i$, which seems to represent an individual agent's policy. The lack of clarity makes it difficult to understand the precise mathematical formulation of the risk-averse quantal response equilibrium (RQE).
- Typo in line 160: "we make u a general class..."
- The experiments lack breadth in demonstrating the algorithm’s efficacy across diverse problem settings. Only one cliff walk example is demonstrated, and very standard simple benchmarks are used for the repeated game. The cliff walk example, while illustrative, is a relatively simple environment. The lack of more complex and varied environments makes it difficult to assess the generalizability of the proposed approach. Furthermore, the standard matrix games used for the repeated game setting do not sufficiently showcase the benefits of the risk-averse approach, as these games often have well-known solutions that do not require risk-aversion to be solved effectively.

### Questions
- Could we not also have a baseline comparison with standard algorithms, such as Nash Q-learning in the MG, or other MARL algorithms (e.g., multi-agent PPO), to assess its performance against established algorithms?
- Similarly, could we extend the MG setting to more than two players in the toy examples? This could significantly increase computation time, even with the proposed, more efficient, algorithm.
- How would this accommodate non-convex compositions of risk-averse functions? Is there a simple extension, or would it be more complex?
- What economic scenarios could the RAMG apply to, given that the concept of risk aversion originally stems from economics?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose an algorithm for multi-agent game and reinforcement learning inspired by behavioral economics, with risk aversion and bounded rationality. They study a new class of equilibria called risk-averse quantal response equilibria (RQE), which is computationally tractable and with more human characteristics. Moreover, it provides an analysis of sample complexity for computing RQE in finite-horizon Markov games using generative models

Especially, these equilibria are independent of specific game structures and instead hinge on the degree of agents' risk aversion and bounded rationality. The authors also validate the effectiveness of RQE by showing its alignment with human behavior in experimental game studies.

### Strengths
- The authors introduces games with risk-averse agents and bounded rationality, allowing for the computation of risk-averse quantal response equilibrium (RQE), which is realistic and computationally feasible.
- RQE can be computed in polynomial time in all $n$-player matrix games under specific risk aversion and bounded rationality conditions, irrespective of the underlying payoffs.
- The authors present a sampling-based algorithm with finite-sample guarantees for learning approximate RQE in unknown environments.

### Weaknesses
 - While the paper applies duality and risk aversion concepts, these techniques have been previously explored in the context of game theory and multi-agent reinforcement learning, raising questions about the technical novelty of the contributions.
- Extending the findings to finite-horizon Markov Decision Processes (MDPs) may be somewhat straightforward, as the process involves relatively conventional methods. While this extension adds scope, it may not significantly deepen the theoretical insights or complexity of the approach.
- The proposed algorithm requires access to a simulator, which is a strong assumption and may limit the practical applicability of the method, especially in real-world scenarios where such simulators are unavailable or costly to obtain.

### Questions
- Typo on L161: To allow agents to have risk preferences we make u a general class of convex
- What challenges arise in adopting conditions weaker than requiring a simulator?

### Soundness
3

### Presentation
3

### Contribution
2
