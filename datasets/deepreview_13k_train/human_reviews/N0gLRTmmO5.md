# Open-Ended Learning in General-Sum Games: The Role of Diversity in Correlated Equilibrium

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
The primary in this work focuses on the challenging and crucial task of identifying and selecting equilibria for $n$-player general-sum games. PSRO serves as a comprehensive framework for tackling complex games by leveraging the concept of the meta-game. However, prior research on PSRO mainly concentrates on solving two-player zero-sum games. Extended approaches such as JPRSO and $\alpha$-Rank can address multi-player general-sum games, and these methods theoretically ensure uniqueness and convergence. Nonetheless, a noticeable gap often exists between the joint policy distribution derived by the solver and the target equilibrium, which can undermine the robustness of the joint policy. Within the PSRO framework, diversity characterizes the distinctions among policies within the population, representing the exploration of the policy space by players. Consequently, allocating greater sampling probabilities (meta-strategy) to more diverse policies encourages players to employ more exploratory policies, thereby mitigating the risk of exploitation. We begin by incorporating diversity measures into solving equilibria for $n$-player meta-games and introduce a novel equilibrium concept, called Diverse (C)CE, the objective of which is to maximize sum of expectations of each player's diversity. In alignment with this, we present a policy training algorithm, Diverse Correlated Oracle (DCO), which effectively associates policy dynamics with the joint policy distribution. The experimental results conducted on a range of multi-player, general-sum games demonstrate that our algorithm outperforms JPSRO and $\alpha$-Rank and enhances the approximation of the joint policy distribution towards the target equilibrium by notably reducing the gap.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a variant of the JPSRO methodology for solving meta-games but instead of a standard (C)CE equilibrium solver they use an adapted equilibrium solver that aims to find maximally diverse equilibria. The paper shows that under some tuning of internal parameters the uniqueness of the resulting solution concept follows and presents some closed formed descriptions of the solutions. Experimental results showcase that in some games the resulting solver can outperform previous solvers when the internal parameters are  "selected appropriate through extensive hyper-parameter tuning".

### Strengths
I think the paper examines an interesting domain of meta-game solvers and has some interesting ideas about incorporating diversity which has not been previously precisely formulated in the case of n-player games. The experimental results show some promise in terms of the value of the explored direction.

### Weaknesses
Although the paper studies an interesting setting the implementation feels somewhat lacking. First, I would expect the experimental results to actually showcase and discuss the actual diversity of the found solutions but this is surprisingly not really explored. Instead the paper only focuses on the extent in which these new techniques find states of low exploitability. I find this to be a critical weakness of the paper and I would be very interested in a deeper dive that tries to explore what are the properties of the solutions found and not whether they are epsilon equilibria for small enough epsilon. 

Even the current experimental implementation leaves something to be desired. For example, it is stated that the stated performance of the technique is for a choice of internal parameters which is "selected appropriate through extensive hyper-parameter tuning". Is this an apple to apple comparison with other techniques?

The theoretical analysis of the paper is not particularly deep. Finally, the paper showcases some obvious typos or undefined notations that indicate a bit of rushed implementations.
Examples include:
Page 3. \Pi^{O:T}_{-i} from Marris et al paper not defined.
Page 4. In Equation 4 \rho is not defined.
Page 8 In all figures Itertions-> Iterations.

### Questions
Can you be a bit more precise about the hyper-parameter tuning process of $k$? For example when $k$ is very small (which you need to be small enough to guarantee uniqueness) then the solution you find is not optimizing for diversity but for maximizing the convex objective $\sigma^T \sigma$. So it is not clear to me whether the success of low exploitability is really due to optimizing for diversity.

Also in terms of an apple to apple comparisons to other techniques did you try to examine what would happen if a similar fine-tuning was explored for the other competing techniques?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper defines a new metric for policy diversity in multi-player games, then defines a new equilibrium concept (Diverse [Coarse] Correlated Equilibrium), then proposes an extension of population-based methods PSRO / JPSRO that presumably finds this equilibrium (Diverse Correlated Oracles). 

Theory is given for the uniqueness of such an equilibrium, and a closed-form solution to find it.

Experiments are performed on a few general-sum or multi-player games, showing the CCE gap of the novel algorithm versus JPSRO with various diversity metrics.

### Strengths
The research direction is interesting: investigating definitions of diversity in multi-player games, and using them to define equilibrium concepts and using them with a PSRO-like algorithm. The theory given seems sound (although I did not check carefully).

### Weaknesses
In its current state, this paper is not ready for publication. Most of the issues are in the writing of the paper. In my reading, I was unable to find explanations for key parts of the algorithm. There are also some minor issues: it's not intuitive to me why the definition of diversity expectation would be good, which would be fine if the experiments convincingly showed that the algorithm is good, but they don't. (Maybe the definition of diversity expectation is a good one, but the paper didn't show me that it is.)

- The algorithm is not clearly explained: I feel like this paper is missing a paragraph or a section, because Section 4 and Algorithm 1 should explicate the algorithm. However, to my reading, they do not. The paper does not explain what MS is, which is the most important part of the paper. (Without stating the specific choice of MS, Algorithm 1 seems to be equivalent to PSRO.) I infer that MS does the computation described in Section 3.3, but this does not seem to be explicitly stated anywhere! And even if I make this inference, I don't know whether it is Equation 14 (General support) or Equation 15 (Full support) which is being calculated. The paper also does not explain what DM is, although I infer that it is the diversity measure from Equation 6.

- However, this also seems undefined! Section 3.1 explains how sum of diversity expectations is calculated based on each player's diversity measure $f_{i|l,m,...q}$, which is defiend in terms of $f$. However, as far as I can see, the choice of $f$ used in the experiments was never described! (I cannot even infer the choice of $f$, since Section 2.4 describes two different diversity measures, and states that this work uses a combination of them, with the method of combination left undefined.)

- Presumably the output of DCO is supposed to be a D(C)CE, but this is never stated. It should be stated. It should also be stated and proved that the termination condition given in Algorithm 1 leads to the output being a D(C)CE.

- I don't entirely understand the sentence in Section 3.1: "Inspired by JPSRO, we use a quadratic function as the optimization objective". If my interpretation is correct, JPSRO uses the Gini impurity as an objective, which is quadratic. Here, I don't see why you would be inspired to maximize $(f^\top \sigma)^2$ -- aren't both of those vectors non-negative, so maximizing their square is equivalent to maximizing the original thing?

- It's stated in Section 3.1 (and throughout the paper) that "our objective it to increase the sampling probability assigned to diverse policies. This is achieved by maximizing the sum of each player's policy diversity expectations, thereby ensuring that the more exploratory policies play a more significant role in approximating the full game (C)CE." I don't immediately see why this objective is achieved by maximizing the sum of each player's policy diversity expectations. Maybe I am misunderstanding, but as defined, it seems that each $f_{i|l,m,...q}$ is dependent on the set of player $i$ policies, but is not dependent on their distribution over those policies. It would be helpful for the paper to explain or give intuition for why the policy diversity expectations achieve this goal.

- On that note, it would be good for the paper to include qualitative examples of things like the policy diversity expectation value for different strategy profiles, and especially for the difference in distributions over a given set of strategy profiles for D(C)CE vs. MG(C)CE.

- Results are not convincingly strong. Only in 3-Player Kuhn Poker is the novel method clearly better. 2 of the 3 experiment games are 2-player, not multi-player.

Minor:
- the first paragraph of Section 3 mentions "MGCE" but this is not defined anywhere.
- Game notation (Section 2.1) could use work. Probably should clarify in the first sentence that this describes sequential games. Policies are not defined. State transitions are not defined. In the description of meta-game, should it say that "a meta-strategy is used to denote the probability distribution over policy *profiles*" instead of "over policies"? And perhaps a more suitable name for "meta-strategy" would be "joint meta-strategy"?
- Notation in Section 2.2 could also be more clear. It could be specified what the summation in Inequality (1) is over. Sigma is defined in 2.1 using brackets but is used in 2.2 with parentheses. Underneath it says it can be written as $A_i \sigma$ but neither of those symbols are defined (it is not explicated anywhere that they are vectors). I would appreciate a citation for the statement that the maximum sum of social welfare under CEs is greater than or equal to that under NEs. Should it say that "The NE *are* located on the boundary" instead of "The NE *is* located on the boundary"? In the definition for NE, the symbol $\sigma(\pi_i)$ is used, and although it's clear to someone familiar with the topic what this means, it's not defined anywhere and could be confusing for some readers. In the definition for CCE, should it say "only consider deviating *before*" instead of "only consider deviating *until*"? Also, this "recommended policy" is referenced to define CCEs, but is not previously mentioned in the definition of CEs, so the reader doesn't know what a "recommended policy" is. For the definition of CCEs (inequality 2), the foralls should be clearly restated instead of implied, otherwise the definition of $i$ is not clear.
- Section 2.3 uses the term "Meta-Solver (MS)" but doesn't describe what it is or give any examples (e.g. Nash Equilibrium solver). The symbol $u^*_i$ is used but not defined anywhere.
- Section 3.2 is titled "Existence of the Equilibrium" but it seems to me to concern the uniqueness of the equilibrium and not the existence of the equilibrium. 
- Section 4: "it differs from other algorithms by assigning greater sampling probabilities to more diverse policies": could this be made more precise or expanded upon? What is a "more diverse policy"? When does it assign greater sampling probability? (in the meta-solver?) 
- Section 6: The sentence "In [multi-player general-sum games], players aim not only to coordinate their policies or actions within a unified join policy but also seek to maximize overall social welfare" seems wrong to me. That may be the players' goal, or it may be the algorithm designer's goal, but generally players just care about their own utility, right? Unless the setting is intended to be fully cooperative.


Nitpicks / typos:

- Abstract: "The primary in this work"
- Introduction: "frameowrk"
- Quotation marks in Section 2.1 are both in the same direction for "game of games"
- Section 2.1: "used to denoted" should be "used to denote"
- Section 2.2: it's weird that the original Aumann paper is not cited here for the definition of CE (I know it was cited earlier, in the Introduction, but should it be cited here?)
- Section 2.4: Perhaps rearrange the first sentence so it says "... the diversity of player $i$'s population $\Pi_i ...$, given the opponent's policy $\pi^l_{-i}$  is denoted by ..." to emphasize that the diversity is of a population and conditional on an opponent's policy?
- Section 3: grammar - "The sampling probability of the policy is closer to the uniform distribution, the entropy or Gini impurity is larger." Also, the "sampling probability of a policy" is referred to a few times but as far as I can tell it's not precisely defined what it means.
- Section 3: should "regular term" be "regularization term"? This would also benefit from a quick explanation of "policy exploitability (PE)"
- should "the corresponding expected return (ER)" be "the corresponding expected returns (ER)"?
- Section 5 (page 8): "the weight K of the diversity term should be smaller than ..." the fraction has a typo?
- Figure 1 x-axis should be "Iterations" not "Itertions"

### Questions
- The explanation of the metrics and equilibrium concept and algorithm implies that they can be used for both correlated as well as coarse correlated equilibria. However, the experiments seem to all use CCE versions and measure the CCE gap. Can the experiments be performed for CE as well?

- Throughout the text, it's stated that we want to assign higher sampling probabilities to "more diverse policies". But what does it mean for a policy to be "more diverse" than another? Isn't diversity defined for a set of policies, not for an individual policy?

- I don't understand the (C)CE in Equation 8. When this is for CCE, what is $A_i$?

- Section 3.2 says that "calculating entropy can be challenging" -- why is that? Isn't it just $O(|N| \times |\Pi|)$ where $|\Pi|$ is the size of each player's population?

- Section 5 says "the CCE Gap, which is evaluated under Maximum Welfare CCE". What does it mean that it is evaluated under Maximum Welfare CCE? (What part of the definition is Maximum Welfare CCE specific?)

- First-price Sealed-bid Auction (FPSBA) is described as a multi-player game. This paper is about multi-player games. Then why is the experiment only in a 2-player FPSBA?

- Blotto is a 2-player zero-sum game. Can we compare to normal PSRO with a Nash Equilibrium meta-solver?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of solving for correlated equilibrium in n-player general-sum games. They accomplish this through the Policy-Space Response Oracles (PSRO) framework that solves a game by proxy through an empirical game. From this, they study the role of different diversity-based exploration methods in improving the quality of the solution computed. To do this they propose increasing the sampling probability assigned to "diverse" policies in the solution. They evaluate their method on a few OpenSpiel 2/3-player games.

### Strengths
- Studies an important problem which is the role of diversity in strategy exploration methods (a subroutine of empirical game solving).
- Includes an ablation study that covers the space of both reward and behavioral diversity measures. 
- Theoretically, and empirically, show that their solution can be computed analytically.

### Weaknesses
 - It's not clear to me why we should want to "increase the sampling probability assigned to diverse policies" nor that this is well defined.
  - The diverse policies are not necessarily profitable in equilibrium.
  - If our population is diverse then this suggests we want a uniform distribution. Otherwise, the population isn't diverse, and then increasing the sampling probabilities of diverse policies would reduce return.
  - How would this claim apply to deterministic versus stochastic policies? Including purification of policy subsets?
- The contributions of this paper appear marginal, as it suggests using existing diversity measures to solve for maximum welfare coarse correlated equilibrium (MWCCE).
  - The paper frames itself as solving for CE and CCE generally but only has an evaluation for MWCCE.
  - The interesting ablation study of different diversity metrics is shown only on a single game (3-player Kuhn poker).
  - The empirical performance of "Diverse CCE" only shows a benefit over a baseline in one of the three games studied.


### Questions
- "the isolation diversity term is meaningless" What do the authors mean by this? Could they define this precisely?
- Why is NE not included as a baseline meta-strategy solver? 
- How does the ablation study perform on the other games?
- "Given that diversity has the ... and being computationally tractable." Diversity is not generally guaranteed to be tractable.
- How do the methods compare if you're interested in finding an equilibrium as opposed to the maximum welfare equilibrium?
- Some of the citations are confusing, for example Correlated Equilibrium is credited by two papers that came out after 2020.

Nits:
- frameowrk --> framework
- Issues with spacing before citations and after parenthesis throughout.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new meta-solver for Joint PSRO (JPSRO) for use in computing CCE and CE. Their meta-solver includes a term for the "diversity" of the resulting strategy. Empirical experiments seem to suggest that their meta-solver yields faster convergence at least in some games.

### Strengths
The concept of using policy diversity as a metric in selecting a meta-strategy for PSRO is interesting. It seems to have a positive effect on the convergence rate in some games.

### Weaknesses
My main concern is the quality of the writing. I had trouble understanding the main ideas of the paper, mainly because there were many confusing definitions and notational jumps. Here are some concerns, in no particular order.

1. In 2.1, the definition of a "game" seems to be a complete-information, alternating-move sequential game. But the paper is general to incomplete-information or simultaneous-move settings as well, so I think that the definition of game should be changed to accomodate that. In fact, since the paper doesn't care about the sequentiality at all, why not just use normal-form games throughout?

2. The citation of [Farina et al 2020, Marris et al 2022] for correlated equilibrium is strange---especially the former, as the concept it discusses isn't CE. For CE I believe the correct citation is [Aumann 1974].

3. The definition of $\epsilon$-CE used here is a bit strange. Indeed, it seems to imply that the uniform-random policy is a $1/N$-CE, where $N = \min_i |\Pi_i|$ (which could be very large), and that not every $\epsilon$-CE is an $\epsilon$-CCE. Perhaps it would be better to define $\epsilon$-CE with the set of swap deviations instead of the set of internal deviations (see e.g. [Blum & Mansour 2007]). But also this doesn't seem to matter much to the rest of the paper, so I mostly disregard it.

4. In the diversity metric definitions (3) and (4):

    a. the metric seems to depend on the ordering in which the profiles are added (i.e., on which strategy is the new one). Perhaps then the diversity metric should be expressed as a two-argument function, $\text{Div}(\Pi_i, \pi_i')$, so that this dependence is clear.

    b. The definition of occupancy measure should be stated in the text. 
    
    c. Since Nash equilibria are not generally unique, (4) is not well-defined until a specific NE is selected. This should be explicitly stated and discussed.
    
    d. It is unclear how the definition $\text{Div}(\cdot)$ relates to the function $f(\cdot)$ used later in the paper. In particular, it appears as if the diversity metric $\text{Div}(\cdot)$ is built to affect how *new policies* are introduced (i.e. to affect the best-response oracle, which is the thing picking the $pi_i'$), whereas the rest of the paper concerns the meta-solver. How are these related? This to me is a crucial point, because $f$ is used liberally in the remainder of the paper.
    
The experimental evaluation is also not very convincing. On the single example in which the authors do a comprehensive test against other metrics, the proposed method, which is a combination of two prior methods, performs second-worst, being outperformed by both of the prior methods individually.

A Blum & Y Mansour. "From External to Internal Regret", JMLR 2007

### Questions
1. (from 4(d) above) How does the definition $\text{Div}(\cdot)$ relate to the function $f(\cdot)$ used later in the paper?

1. For Prop 3.1, what's an "elementary matrix"? $I - \kappa \mathbf{ff}^\top$ does not seem to satisfy the [definition I am familiar with](https://en.wikipedia.org/wiki/Elementary_matrix)

1. Why is it "unrealistic" to solve (7-9)? If the game has a manageable size, it's is just a convex program.

1. Doesn't Theorem 3.4 actually hold for all $\epsilon > 0$?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
