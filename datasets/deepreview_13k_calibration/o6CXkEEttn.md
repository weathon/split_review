# Strategic Classification With Externalities

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
We propose a new variant of the strategic classification problem: a principal reveals a classifier, and $n$ agents report their (possibly manipulated) features to be classified. Motivated by real-world applications, our model crucially allows the manipulation of one agent to affect another; that is, it explicitly captures inter-agent externalities. The principal-agent interactions are formally modeled as a Stackelberg game, with the resulting agent manipulation dynamics captured as a simultaneous game. We show that under certain assumptions, the pure Nash Equilibrium of this agent manipulation game is unique and can be efficiently computed. Leveraging this result, PAC learning guarantees are established for the learner: informally, we show that it is possible to learn classifiers that minimize loss on the distribution, even when a random number of agents are manipulating their way to a pure Nash Equilibrium. We also comment on the optimization of such classifiers through gradient-based approaches. This work sets the theoretical foundations for a more realistic analysis of classifiers that are robust against multiple strategic actors interacting in a common environment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study a generalization of strategic classification where the game between the principal and agents is Stackelberg, but the game between the agents itself is simultaneous. The principal's goal is to compute the Stackelberg-Nash equilibrium to maximize its utility.

They show:

Under some assumption the PNE of this game is unique and can be computed efficiently.

PAC learning results for the principal.

And they show ERM results through gradient-based methods.

### Strengths
I think the writing of the paper is fantastic!
Also, the problem formulation is interesting.

### Weaknesses
Besides their novel formulation, their main result is their sample complexity result, but that seems to me to just be using a standard covering argument to bound the discretization error. Do you think you can get tighter bounds using other techniques like Rademacher complexity etc.?

They assume that the number of agents that participate in the game is not fixed, but comes from the distribution. However, this assumption does not impact the PAC learning result. This assumption is mostly interesting from the modeling point, but are there scenarios where this assumption leads to different outcomes compared to a fixed number of agents?

Line 196, shouldn't it be f_{\omega}(x') instead of x inside the parentheses? If this is correct, then you may want to double-check it throughout the paper, in case it appears in other equations or explanations.

### Questions
They assume that the number of agents that participate in the game is not fixed, but comes from the distribution. However, this assumption does not impact the PAC learning result. This assumption is mostly interesting from the modeling point, but are there scenarios where this assumption leads to different outcomes compared to a fixed number of agents?

Line 196, shouldn't it be f_{\omega}(x') instead of x inside the parentheses? If this is correct, then you may want to double-check it throughout the paper, in case it appears in other equations or explanations.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a new variant of strategic classification that explicitly models how one agent's feature manipulation can affect other agents' utilities, a form of externalities. The authors model this multi-agent interaction as a Stackelberg game between the classifier (leader) and agents (followers). The paper contains several results under this model:
- Under certain conditions, the agent manipulation game has a unique Pure Nash Equilibrium (PNE)
- The PNE can be efficiently computed under certain technical conditions
- A PAC learning guarantees for learning the optimal classifier
- Some characterization of the optimization problem for learning the classifier
- Two concrete externality models (that can be special cases of their general model): proportional externality and congestion externality.

### Strengths
In my opinion, the primary strength of the paper is modeling externality in strategic classification. I believe this aspect of externality has been missing in the long literature of strategic classification. 

The authors also did a good job at identifying a clean set of technical conditions (ell_2 norm costs, pairwise symmetric externalities, and convex total externality) for a unique Pure Nash Equilibrium. In particular, the conditions lead to a potential game formulation, enabling the use of well-established game theoretic tools.

These technical conditions also lead to a clean analysis of their PAC learning guarantees. The Lipschitzness condition of NE in Lemma 1 seems quite nice and certainly facilitates the analysis for generalization error.

### Weaknesses
The paper's main weakness lies in its treatment of optimization. While the authors elegantly establish the existence and uniqueness of equilibria, they essentially punt on the crucial question of how to actually find the optimal classifier. Their argument - that gradient-based methods often work well for non-convex problems - feels particularly thin in this context. After all, we're not dealing with standard non-convexity here, but rather with a nested optimization where agents are reaching equilibrium inside the classifier's optimization loop.

While the authors derived gradients through the equilibrium, they stopped short of showing these gradients are actually useful. A simple set of experiments on synthetic data or semi-synthetic data would have been useful here. For instance, does gradient descent reliably find good classifiers? How does the convergence behavior change with the number of agents or the strength of externalities? The field of strategic classification has evolved. Recent papers have routinely complemented their theoretical results with experimental validation.

### Questions
- Since the authors set up the downstream game as a potential game, perhaps they can make the point that the agents can reach NE through simple best-response dynamics? 

- The authors did a good job surveying recent related work on strategic classification, but perhaps missed the following:
** On the Long-term Impact of Algorithmic Decision Policies: Effort Unfairness and Feature Segregation through Social Learning, ICML 2019. This paper models the "information externality" of some agents over others in settings like strategic classification.
** Strategic Instrumental Variable Regression: Recovering Causal Relationships From Strategic Responses, ICML 2022. This paper also accounts for causal effects in strategic classification.

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
This paper considers agents being classified by a classifier $f_{\omega}$ in a setup where these agents can manipulate their features in order to increase their utility in the classification task. Their utility also depends on the cost they incur to modify their features: the more they modify, the more they pay. Such phenomena naturally arise in tasks such as classifying students for admission at university (you - an agent - would like to manipulate your features to be better classified and get a better university). 

The paper brings externalities to the model, which means that one agent's manipulations can affect the outcomes or incentives of others.

The paper frames the interactions as a Stackelberg game, where the principal (the classifier) commits to a strategy first, and is followed by agents responding simultaneously. Beyond theoretical contributions that study the arising equilibria, the paper establishes PAC learning guarantees for classifiers trained in these strategic multi-agent environments. It ends with several considerations on various models of externalities.

### Strengths
I think that the problem tackled is very important and relevant. It is nice to see a problem arising from real-world concerns that is studied through a Econ-ML lens.

By combining Stackelberg/Nash game theory concepts with externalities, the authors create a framework that captures both the principal-agent and multi-agent dynamics in a unified model. This approach positions the principal as a leader setting a classifier policy, followed by agents interacting with both the classifier and one another, which is a complex yet analytically tractable setup. Then, based on the first results, they interestingly show that PAC learning is achievable.

The paper is well-written, with a lot of content and interesting theoretical results.

### Weaknesses
I think that the assumption of pairwise symmetric externalities is very limiting. Of course, it helps to obtain a model which exhibits nice results and gives Theorem 1 but it seems a bit far from a lot of real-world issues to me. “Equilibrium of Data Markets with Externality” is mentioned as a reference to justify this assumption but does not provide any material to motivate it. “How (Not) to Raise Money”, Goeree et al. is the other reference to justify this assumption, although they only mention symmetry for a very specific case of lottery. I think that more motivation is needed. Removing the assumption would be even better.

More discussion could be provided on the social optimality of the equilibria studied in the paper, for the players as a whole.

### Questions
The externality of an agent $j$ suffered by agent $i$ is modeled as $t(x_i, x_i’, x_j, x_j’)$. However, I would intuitively say that externalities are global: the externality suffered by an agent due to a group $J$ might not be factorized as a sum over elements from $J$. Is it possible to have more explanations about your choice?

At the PNE, the agents cannot increase their utility by changing their responses. However, I would be very interested in a discussion about what a coalition of agents could achieve. I feel like a lot of setups involve agents that could behave together and this question is not studied at all in the paper. How would the equilibrium be affected?

“To give an example of a non-linear but convex externality, consider the loan application setting where a bank (the learner) is screening candidates for approval. The more adversely affecting all candidates.” The general setup and this example from your paper in particular remind me the setup of “Strategic Apple Testing”, Harris et al., 2023 (with agents arriving sequentially and manipulating their type). A discussion could be interesting.
The inter-agent externalities explain the whole inter-agent dynamics but I would be interested in a discussion about how the agents could find other ways to interact together, such as through contracting for instance (which is essential in Coase’s theory).

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper serves as the first framework to consider externalities in a multi-agent strategic classification (SC) game. The SC game is still a Stackelberg game with the externality modeled as an extra cost term $T(x_i, x_i', \mathbf{X}, \mathbf{X}')$. Assuming the externalities are pairwise symmetric and *the total cost and the sum of all combinations of externality* is smooth and strictly convex, the authors proved that a unique Nash Equilibrium ($NE$) exists for the post-manipulate features of $k$ agents. Based on this, the authors then characterized the conditions for $NE$ to be Lipschitz in the model parameter and further proved the sample complexity to guarantee the generalization error of the decision policy ($f_\omega$)  in PAC learning. Finally, the authors explored the differentiability of $NE$ w.r.t. model parameter $\omega$, proving the plausibility of using gradient-based algorithms to perform empirical risk minimization.

### Strengths
1. Considering externalities in SC settings is well-motivated and the university admission example is quite natural. 
2. The paper is well-written and easy to follow. As a purely theoretical work, the authors provided both the PAC learning bound and discussed empirical risk minimization using gradient methods.
3. The technical parts seem to be solid and mostly make sense to me.
4. The paper is situated well in the previous literature. The discussion of [Eilat et al., 2023] is necessary.

### Weaknesses
Overall, I do believe the work has some merit and will enrich SC literature. But the paper can still benefit from some more comprehensive discussions.

> Assumptions:

1. the paper assumes a "full-information" SC setting where the decision policy is linear and all strategic agents know the decision policies, cost functions, and externality functions. The authors claimed to adhere to previous literature. However, recent works on SC questioned the plausibility of the assumptions, and a number of them are trying to relax the full information setting (e.g., [1,2,3]). I believe it is at least beneficial to discuss the assumption a bit more. Specifically, the assumption that all agents have perfect knowledge of the classifier parameters, cost functions, and externality functions is quite strong. This is particularly problematic in settings with many agents, where it is unlikely that each agent would have access to all this information. The paper should discuss the limitations of this assumption and perhaps consider how the results might change under more realistic information structures.

2. It seems that assuming each agent knows the exact externality $T$ can be more problematic. Each agent has to know the features of all other agents to calculate its utility, and NE is a function of $\mathbf{X}$. Is this realistic in practice and how can each agent know the full $\mathbf{X}$ matrix? At least the authors should make this assumption clear. This is a significant limitation as it requires each agent to have complete knowledge of the features of all other agents, which is unrealistic in most practical scenarios. The paper should discuss the implications of this assumption and perhaps consider alternative models where agents have only partial or noisy information about the features of others.

3. In Section 5 the authors present some examples of symmetric externality functions, but I still have some confusion. Consider the proportional externality in the admission example. Assume there are 2 agents $i,j$ with $1$-d feature $x_i, x_j$ and they rank $1,2$. Then $j$ seems to be able to manipulate $x_j$ at no externality if $i$ does not manipulate $x_i$. This example highlights a potential issue with the proposed externality model. The fact that a manipulating agent can avoid externalities if others do not manipulate seems counterintuitive. The paper should provide a more detailed explanation of the rationale behind this behavior and perhaps consider alternative externality models that better capture the intended effects.

### Questions
1. Is it reasonable to assume each agent knows the full $\mathbf{X}$?
2. Could you elaborate more on the symmetric externality function in the admission example? Specifically, why the agents who do not manipulate will not impose externality on other agents who manipulate? Am I missing something?
3. Given that you still have one page of space, could you provide at least one set of case studies?

### Soundness
4

### Presentation
3

### Contribution
3
