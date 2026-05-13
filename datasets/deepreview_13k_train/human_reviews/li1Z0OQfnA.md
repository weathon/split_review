# On Local Equilibrium in Non-Concave Games

- Decision: Reject
- Scores: 6, 1, 8, 3

## Abstract
While Online Gradient Descent and other no-regret learning procedures are known to efficiently converge to coarse correlated equilibrium in  games where each agent's utility is concave in their own strategies, this is not the case when the utilities are non-concave, a situation that is  common in machine learning applications where the agents' strategies are parametrized by deep neural networks, or the agents' utilities are computed by a  neural network, or both. Indeed,  non-concave games present a host of game-theoretic and optimization challenges:  (i) Nash equilibria may fail to exist; (ii) local Nash equilibria exist but are intractable; and (iii) mixed Nash, correlated, and coarse correlated equilibria have infinite support, in general, and are intractable. To sidestep these challenges we propose a new solution concept, termed  *local correlated equilibrium*, which generalizes local Nash equilibrium. Importantly, we show that this solution concept captures the convergence guarantees of Online Gradient Descent and no-regret learning, which we show efficiently converge to this type of equilibrium in non-concave games with smooth utilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of learning equilibria in non-concave (smooth) games. It introduces a new notion of local equilibrium, coined local correlated equilibrium, which is a variation of the correlated equilibrium in which only bounded (local) deviations are allowed. The paper shows that such an equilibrium always exists and it shows that classical no-regret algorithms such as online gradient descent and optimistic gradient efficiently converge to some special cases of such an equilibrium in non-concave (smooth) games.

### Strengths
I found the problem studied in the paper really interesting. Understanding which equilibria can be learned efficiently in non-concave games is an important step towards applying game-theoretical solution concepts in modern machine learning problems. 

The results presented in the paper are not incredibly complicated from a technical viewpoint, but they nevertheless provide a neat novel analysis of some existing algorithms, shedding the light on what these algorithms actually learn in settings beyond basic games with concave utilities.

### Weaknesses
I found that the paper writing is not sufficiently neat in some parts. While all the concepts and results are introduced and adequately explained, there are some issues with terminology and notation, which is not coherent across different sections. For example, in Section 3 the paper talks about differential games, but these have never been introduced in the previous sections (only the definition of smooth game is provided).

My score reflects the weakness above. I strongly encourage the authors to carefully proof read the paper in order to improve it, and I am willing to increase my score if they do so.

### Questions
No questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new solution concept called $\phi$-local correlated equilibrium for non-concave games with smooth utilities. The authors show that this concept captures the convergence guarantees of Online Gradient Descent and no-regret learning in such games for two specific initializations of $\phi$. They also provide a new algorithm for computing local correlated equilibria that is based on a variant of Online Gradient Descent. The paper concludes with experimental results that demonstrate the effectiveness of this algorithm in practice.

### Strengths
The paper provides important mathematical characterizations for the limit point of multiagent learning algorithms in non-convex game settings and answers important open question posed by Daslakakis et al. [1]

### Weaknesses
This is relatively minor but the organization of the paper in my opinion makes the paper hard to read. A few suggestions:
Adding a mathematical description of the problem (i.e., games) to the introduction
Moving some parts of the local correlated equilibrium section on page 2 above the contributions section and tie it in with this mathematical description
Adding more intuition and background on intractability of approximate local Nash to intro together with a mathematical description

Minor comments and questions:
Aren’t part 1) of assumption 1 redundant given part 3? And part 2) redundant given part 1 and compactness of strategy sets?

The local Nash definition that is studied in the paper considers only *pure* strategies, however, local correlated equilibrium is studied in correlated **mixed** strategies (logically). This begs the questions, can mixed local Nash equilibria be efficiently computed or is that out of reach as well? It seems like that would be out of reach since the randomization would reduce the problem to a multilinear game (albeit infinite dimensional) for which computation of Nash is PPAD. I think a description of this point is important to understand the jump from pure strategies to mixed strategies

Does Lemma 1 assume Lipschitz smoothness/continuity on the convex regrets or no?

How does part 2 of Lemma 1 relate to Hazan et al’s [2] results and in general how do the authors’ result relate to your results on projected \phi regret ?


Naive regret bound in section 3.1 seems meaninglessly loose. That is, having an additive Lipschitz continuity constant G suggests that the algorithm might make no progress at all?


Reg_proj does not have a learning rate in the step it takes this seems to affect the notion that projected and external regret can in general be unrelated?


Writing: For large enough δ, Definition 1 captures global Nash equilibrium as well >> For large enough δ, Definition 1 captures global \varepsilon-Nash equilibrium as well

### Questions
Minor comments and questions:
Aren’t part 1) of assumption 1 redundant given part 3? And part 2) redundant given part 1 and compactness of strategy sets?

The local Nash definition that is studied in the paper considers only *pure* strategies, however, local correlated equilibrium is studied in correlated **mixed** strategies (logically). This begs the questions, can mixed local Nash equilibria be efficiently computed or is that out of reach as well? It seems like that would be out of reach since the randomization would reduce the problem to a multilinear game (albeit infinite dimensional) for which computation of Nash is PPAD. I think a description of this point is important to understand the jump from pure strategies to mixed strategies

Does Lemma 1 assume Lipschitz smoothness/continuity on the convex regrets or no?

How does part 2 of Lemma 1 relate to Hazan et al’s [2] results and in general how do the authors’ result relate to your results on projected \phi regret ?


Naive regret bound in section 3.1 seems meaninglessly loose. That is, having an additive Lipschitz continuity constant G suggests that the algorithm might make no progress at all?


Reg_proj does not have a learning rate in the step it takes this seems to affect the notion that projected and external regret can in general be unrelated? 


Writing: For large enough δ, Definition 1 captures global Nash equilibrium as well >> For large enough δ, Definition 1 captures global $\varepsilon$-Nash equilibrium as well


I would love to hear answer to my questions above, but otherwise I think the authors have written an interesting and illuminating paper which deserves acceptance.





[1] Daskalakis, Constantinos, Stratis Skoulakis, and Manolis Zampetakis. "The complexity of constrained min-max optimization." Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing. 2021.

[2] Hazan, Elad, Karan Singh, and Cyril Zhang. "Efficient regret minimization in non-convex games." International Conference on Machine Learning. PMLR, 2017.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors try to shed light on a new chapter of algorithmic game theory -- i.e., nonconcave games. Nonconcave games are simply games where the utility function of each player is nonconcave with respect to their individual strategy.

Such games have come to the attention of theoreticians due to the advent of an array of machine learning applications. Traditional notions of individual rationality such as the Nash equilibrium need not exist in these games while relaxed notions of equilibria designed for nonconvex games can be intractable. Namely, local $\epsilon$-approximate Nash equilibria is a strategy profile in which no agent can improve their utility more than $\epsilon$ by only considering strategy deviations of distance $\delta$ from the initial strategy. Yet, $(\epsilon, \delta)$-local NE are either trivial to compute, PPAD-hard, or NP-hard (corresponding to the magnitude of $\delta$ compared to the natural parameters of the game). The latter two cases are known as the *local* and the *global regime*.

To this end, the authors propose the notion of a *local correlated equilibrium* as to alleviate the intractability of local-NE in the local regime. After they define this new notion of equilibrium they review the notion of $\Phi$-regret. Briefly, $\Phi$-regret unifies various notions of regret (e.g., external regret, swap regret) under an umbrella definition; it is defined as the difference between in utility at the end of the online optimization process where the best strategy in hindsight is selected using a family of function $\Phi$.

The latter notion is crucial not only for the purpose of an algorithmic solution as well as the notion of the equilibrium itself. An $(\epsilon, \Phi(\delta))$-correlated equilibrium is roughly a correlated strategy profile that achieves small $\Phi(\delta)$-regret for each agent. $\Phi(\delta)$-regret is the $\Phi$-regret where the family of modification functions only allow deviations in a radius of length $\delta$.

The authors note that, to date, there does not exist an efficient algorithm for $\Phi$-regret minimization for general sets $\Phi$. As such, two families of $\Phi$ are considered:
* Interpolations between current strategies from fixed strategies
* Deviations towards a given direction $v$ in a distance of length $\delta$.

Then, the authors utilize the existing online convex optimization framework (the gradient descent and optimistic gradient descent algorithms) to straightforwardly design algorithms that lead to $(\epsilon, \Phi(\delta))$-correlated equilibria.

As a takeaway, the authors propose that solution concepts in nonconcave games should be *meaningful, universal, and tractable*.  I suspect these notions would take the place of rationality. Nevertheless, there is not an explicit discussion as to why their proposal attains these favorable properties.

### Strengths
* The motivation is clear and is guided by both existing applications and contemporary theoretical advances.
* The paper introduces algorithmic solutions and equilibrium concepts for a nascent family of games that arguably can be proven of great importance in the future.
* The algorithmic framework is quite versatile and able to fit different instances of no-regret algorithms and $\Phi$ function families.
* The computational complexity issues are discussed and explained with clarity.

### Weaknesses
 * One has to be fair and recognize the novelty of the paper and the absence of pre-existing criteria for its assessment; nevertheless, it would be rational to ask for some justification of the proposed equilibrium notion other than computational complexity arguments. In a sense, what are real-world examples where the proposed notions of equilibria are already established as desirable states of a game?

* A more precise meaning of what a meaningful and universal equilibrium is remains unclear from the text. It would be nice if the authors could elaborate on those concepts and what makes the particular $\epsilon, \Phi(\delta)$-correlated equilibria attain these properties.

### Questions
* What kinds of $\Phi(\delta)$ families would the authors consider as important for future study and of game-theoretic importance?
* What is the connection of $\Phi(\delta)$-regret minimization and bounded rationality? Putting the computational theoretic aspects aside, we in a sense assume agents to be as rational as their first-order derivative dictates. Would assuming bounded rationality for the agents lead to tractable notions of equilibria as well?
* What would qualitatively change if we assumed access to second-order information?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a notion of “local correlated equilibrium” for non-concave games, and show that variants of GD converge to this solution concept.

### Strengths
Some of the algorithms require careful analysis? I'm not sure...

### Weaknesses
At a high level, I’m concerned about the motivation. The authors introduce a new solution concept and design algorithms, but don’t really stop to motivate their solution concept. The way I understand, in practice GAN training with OGD has limited success because it gets stuck in cycles. Now you’re basically telling me that the path of this training satisfies some new solution concept. What should I learn from that? By analogy, in Game Theory correlated equilibrium has a natural interpretation with a correlating device, and is known to satisfy some good properties (“Price of Anarchy”). What can I do with the fact that the trajectory of my GAN training algorithm is an approximate “local correlated equilibrium”?

The paper is motivated by a hardness result from [DSZ21] for the stronger notion of local Nash equilibrium. But the hardness result in [DSZ21] holds *only* in a non-standard setting where the feasible domain is not a product. In contrast, your work seems to rely on having a product domain. 

I think your solution concept should be called “local *coarse* correlated equilibrium”: You consider a single deviation rule and want to apply it to all x’s in the distribution. This also explains why you can find it by minimizing external regret.

The title should absolutely be updated to say something about (coarse) correlated.

There are two definitions (2 and 4) called “local correlated equilibrium”

### Questions
[These are more writing comments - but feel free to answer my questions from "weaknesses" section]



The paper is motivated by a hardness result from [DSZ21] for the stronger notion of local Nash equilibrium. But the hardness result in [DSZ21] holds *only* in a non-standard setting where the feasible domain is not a product. In contrast, your work seems to rely on having a product domain. 


I think your solution concept should be called “local *coarse* correlated equilibrium”: You consider a single deviation rule and want to apply it to all x’s in the distribution. This also explains why you can find it by minimizing external regret.

The title should absolutely be updated to say something about (coarse) correlated.


There are two definitions (2 and 4) called “local correlated equilibrium”

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
