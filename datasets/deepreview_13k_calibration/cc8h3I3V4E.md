# Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
We propose the first loss function for approximate Nash equilibria of normal-form games that is amenable to unbiased Monte Carlo estimation. This construction allows us to deploy standard non-convex stochastic optimization techniques for approximating Nash equilibria, resulting in novel algorithms  with provable guarantees. We complement our theoretical analysis with experiments demonstrating that stochastic gradient descent can outperform previous state-of-the-art approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a loss function for computation of approximate Nash equilibria in general-sum multiplayer matrix games for which unbiased estimators can be constructed. This allows the exploitation of stochastic optimization algorithms for computation of Nash equilibria in general matrix games. They provide numerical evidence that this approach is competitive with existing approaches.

### Strengths
1. The paper is generally well-written.
2. The formulation of the loss function which allows for unbiased sampling is a solid novel technical contribution. As the authors note, this is a step towards enabling computation of Nash equilibria in large-scale settings (in spite of theoretical hardness results), which is quite important for operationalizing game theory in the real world. 
3. The paper provides numerical evidence supporting that the loss function is "easy" to optimize in many benchmark games of interest, and that it is competitive with other SOTA approaches.

### Weaknesses
1. The empirical section (6.2) could use some additional explanation/discussion. The baselines that are compared against should be explicitly stated in the body text (and cited appropriately) instead of just stating that they are the baselines used in Gemp et al. 2022's simulations. It is unclear what specific algorithms or implementations are being used as baselines, making it difficult to assess the significance of the results. Furthermore, the specific hyperparameter settings used for the baselines and the proposed method should be detailed for reproducibility.
2. The flow of Section 6 generally could be improved (one suggestion is provided below). The current structure, which introduces SGD, then a bandit algorithm, and then immediately discusses the bandit algorithm's performance, is disjointed. This makes it hard to follow the experimental logic and understand the motivation behind each algorithm's evaluation. The lack of a clear narrative makes it difficult to assess the relative strengths and weaknesses of each approach.


### Questions
1. There is a typo in the definition of the projected-gradient (it should be $\Pi_{T\delta^{d-1}}(z) = z - \frac{1}{d} \mathbf{1}^\top z \mathbf{1}$)
2. In Section 6, it is confusing to introduce SGD first and then the bandit algorithm and then immediately have a subsection discussing the bandit algorithm, especially since it is stated that "in the next section, we find it performs well empirically in games previously examined by the literature." Perhaps it makes sense to include the SGD experiments before any discussion of the bandit approach.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new loss function for approximating Nash equilibria in normal-form games. The key idea is that the loss function can be unbiasedly estimated through Monte Carlo sampling of the joint strategies. This allows the use of stochastic optimization, eliminating the need to read all the payoffs, which would be exponential with respect to the number of players.

The loss function upper-bounds the exploitability of an approximate equilibrium. The authors prove this both theoretically and empirically. This approach enables the scaling of equilibrium computation to larger games than previously thought feasible. Experiments are conducted on games with up to 286 actions.

Two algorithms are explored: vanilla SGD and a bandit-based method. The bandit algorithm comes with theoretical guarantees regarding exploitability.

### Strengths
1. The paper proposes a new loss function for approximating Nash equilibria in normal-form games that is amenable to unbiased Monte Carlo estimation. This allows for the use of powerful sample-based stochastic optimization techniques, eliminating the need to read all the payoffs.
2. The loss function upper-bounds the exploitability of an approximate equilibrium. The authors provide theoretical proofs and present empirical results.
3. The proposed approach enables the scaling of equilibrium-finding techniques to larger games than was previously possible. The paper presents experiments on games with up to 286 actions.
4. Two algorithms are analyzed: vanilla SGD and a bandit-based method. The bandit approach offers theoretical guarantees, such as a high probability bound on exploitability.

### Weaknesses
1. The loss function only captures fully mixed equilibria. The authors address this by considering quantal-response equilibrium. As a result, a zero loss can only serve as an approximation to a Nash equilibrium. This limitation stems from the fact that the proposed loss function is inherently designed to measure deviations from a fully mixed strategy profile, and thus cannot directly identify pure strategy Nash equilibria or mixed equilibria with support on a subset of actions. The reliance on quantal response equilibrium, while addressing this issue, introduces an approximation that may not always be suitable, especially in games where the quantal response parameter is difficult to tune or interpret.
2. There is limited empirical evaluation on real-world games. Most experiments involve small synthetic games from previous research. It's possible that more complex games may expose certain limitations. The current empirical evaluation primarily focuses on relatively small, often symmetric, games, which may not fully capture the challenges of real-world scenarios. For instance, games with asymmetric payoff structures, a large number of players, or complex action spaces could reveal limitations in the proposed approach that are not apparent in the current experiments. The lack of experiments on established benchmark problems from game theory or economics further limits the generalizability of the findings.
3. SGD encounters issues with saddle points in certain games, which is a common challenge in non-convex optimization. The use of vanilla SGD, while computationally efficient, is known to be susceptible to getting trapped in saddle points, especially in high-dimensional non-convex landscapes. This issue is particularly relevant in the context of game-theoretic optimization, where the loss function often exhibits complex saddle point structures. The paper does not explore more advanced optimization techniques that are specifically designed to mitigate the saddle point problem, such as momentum-based methods or adaptive learning rate algorithms.

### Questions
1. How well does the approach scale to larger real-world games with structures like symmetry? Are techniques such as grouping actions necessary?
2. Have the authors attempted more advanced optimization methods like Momentum SGD or Adam to address saddle points?
3. What heuristics could be employed to guide equilibrium selection when multiple equilibria exist?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of solving a Nash equilibrium (NE) inside a normal-form general-sum game (NFG). Unlike previous works, the authors propose a new kind of loss that serves as an upper bound for $\epsilon$ (coefficient of $\epsilon$-Nash). More importantly, the authors show that an unbiased gradient of the loss can be obtained using the symmetrization technique. As a result, the problem of NE can be treated as a stochastic optimization problem, such that some famous algorithms like SGD and BLiN can exploited. Moreover, the authors also consider the case when the NE is not inside the simplex but on its boundary. And they show that this issue can be also handled by optimizing on a refined game with additional bonuses. Finally, empirical studies validate the effectiveness of the proposed method.

### Strengths
I have not read the papers about how to solve an NE efficiently before. However, this paper is quite clear in this presentation, such that I have now obtained a whole picture of this problem. The problem setup is clearly introduced. The solution is illuminated step by step, which is clear and intuitive. It is worth mentioning that the authors give several illustration figures (e.g., Figures 1 and 2) to help the readers understand the paper better, which is very good. The experiments are also sufficient and complete. Moreover, this work offers the community a new and principled way of solving NEs efficiently, and many more stochastic optimization algorithms can be leveraged in this field.

### Weaknesses
I do not see major weaknesses in this work, though I am not an expert in this field.

### Questions
I do not have any questions, as the presentation of this work is quite clear and intuitive, along with some illustrations to help readers understand it well.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
