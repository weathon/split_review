## Human Reviewer 1

### Summary
The author proposed the information-theoretical notion of complexity and a model-free algorithm for the general decision-making problem with structured observations (DMSO). The proposed Dig-DEC mechanism works seamlessly in both stochastic and adversarial environments (with stochastic transitions and adversarial rewards). It achieves the first model-free regret guarantees with bandit feedback in many general settings, resolving the existing open problem.  Additionally, the proposed approach improves the regret bound for Bellman-Complete MDPs to match classical optimism-based approaches.

### Strengths
- General framework that covers many existing RL settings and improves upon the existing optimistic DEC bounds.
- Guarantees for model-free algorithms in adversarial settings.
- Interesting online learning technique for the posterior update that seems to be of independent interest.

### Weaknesses
- Restrictive linear reward with known feature assumption for an adversarial hybrid setting;

### Questions
- What are typical values of $\log|\Phi|$ in the examples described in Section 5 (for example, in the case of worst-case finite MDPs)?
- How is DigDEC connected to a classical DEC in terms of regret lower bounds?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper positions itself as a bridge between two major approaches : model-based methods (which learn a full world model) and optimistic, model-free methods (which guess the best outcome). Its main contribution is a new, improved framework called Dig-DEC that removes the "optimism" mechanism. Instead of blindly chasing high rewards, Dig-DEC drives exploration  by seeking out information that helps it distinguish between different high-level "theories" about how the environment works. This shift leads to better performance guarantees in standard settings—improving regret bounds—under certain assumptions.
It aims at replacing a simple heuristic (optimism) with a  possibly more fundamental principle (targeted information gain) to solve harder problems more efficiently.

### Strengths
- the paper presents impressive theoretical developments (though I was far from being able to check all the details of the 30 pages of the appendix),
- the paper introduces Dig-DEC, a new complexity measure for decision-making. By removing the "optimism" principle and replacing it with pure "information gain," it provides an interesting exploration driver. 
- The theoretical proof that Dig-DEC is always smaller than or equal to the prior optimistic DEC is a strong, clean result. This gives improved regret bounds but more fundamentally could give new perspectives of what can be done structured MDPs.

### Weaknesses
Implementation challenge
The first major challenge lies in the computational feasibility of solving the core minimax optimization (point 2 in the algorithm) at each round. This problem seems exceptionally difficult: the learner must optimize over distributions of policies against an adversary optimizing over distributions of models, with an objective function that involves nested expectations and KL divergences over trajectories. For any non-trivial state space, the policy and model classes are likely to be enormous, making an exact solution intractable. The objective is also non-convex and non-concave in general (?). While the paper provides a theoretical blueprint, it offers no practical implementation or approximation scheme. Bridging this gap would require major algorithmic innovations,


Assumptions
 The  core assumptions of the paper present a significant gap between the theory and the reality of most RL problems. The most restrictive assumption is possibly the requirement for a pre-defined, finite partition of the model space into infosets where all models within an infoset share a unique optimal policy and value function (Assumptions 1 & 3). In practice, such a discrete and perfectly aligned partition seems unavailable; the "optimal policy" may not be uniquely defined or may change during learning. Furthermore, Assumption 4 (linear rewards with known features) for the hybrid setting is a strong structural limitation, as it assumes the learner has perfect knowledge of the reward representation, which is often the very thing that needs to be learned in adversarial settings.

Presentation
A major weakness is the presentation. The paper is very difficult to read. Many notions are supposed known to the reader and there is no attempt to aim at a bit of self contained presentation.  For instance, the assumptions 5,6 are difficult to grasp. This makes the contribution of the paper less valuable because more difficult to gauge.
The presentation of the assumptions could be done differently by first describing informally the context and main restrictions and then making them mathematically precise.

### Questions
- What would be the complexity of the minimal AIR optimisation problem? Can you give approximate solutions at a reasonable complexity? (This is one of the most crucial point that the paper does not discuss...)

- Related to that last point, Im a bit lost with the "model free learning" terminology.  I guess for a large part of the community, model free means that you do not have access to the model ( and hence to means) but only to observations.
When solving the optimisation problem, you are not model free? 
So,  given that you claim that optimism principles should be dropped, a lot more details should be given on how a practical estimation scheme can be leveraged  for your proposal?  The regret bounds are MDPs bound? not RL bounds?
In conclusion,  some precisions should be given on what you call (along with other papers) model free learning and more importantly what are the contours of your results...

- In Lemma 12, what does: "In the stochastic setting, Assumption 1 together with -completeness" mean?

- It would have been helpful to have a very simple toy example to underline that the assumptions are useful...

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper introduces a new, model-free complexity measure Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), which removes the optimism-based exploration mechanism (allows adversal setting ) and is upper bounded by optimistic DEC. Then, this work adopts this framework to the stochastic and hybrid adversarial MDP setting and achieves a series of SOTA results with different MDP structures (bilinear classes, Bellman-complete, etc.).

### Strengths
* This work achieves a series of improved results under the Dig-DEC framework.

### Weaknesses
* Since this work has provided a series of new SOTA results, it would be very helpful to add some discussion and intution after each results or assumption (for example, Assumption 1).

### Questions
Q1: Can this work provide experiments (even simulation experiments) to show the relationship between Dig-DEC and optimistic DEC.

### Soundness
3

### Presentation
2

### Contribution
4

### Rating
8

### Confidence
2

---

## Human Reviewer 4

### Summary
This work proposes a new decision-estimation coefficient (DEC) notion, which enables conducting exploration via information gain instead of the optimism principle in a model-free manner. The first benefit of the new DEC notion is the improvement of previous results in cases of bilinear classes or Bellman-complete MDPs with bounded Bellman eluder dimension. The second benefit is that this new DEC notion leads to the first model-free algorithm for MDPs with stochastic transitions and adversarial loss functions in the bandit feedback setting.

### Strengths
1. **Novelty**: The proposed new notion seems interesting and fundamental, enabling the exploration solely based on information gain.
2. **Results**: The model-free algorithm leads to a series of new results in stochastic MDPs, with matched or even improved results. This work also resolves the open problem of previous work for solving MDPs with stochastic transitions and adversarial loss functions in the bandit feedback setting.
3. **Presentation**: This paper is well-written.

### Weaknesses
If any, I would feel that some parts could be clearer and more thoroughly explained. For instance, from Table 1, I notice that the regret bound of off-policy exploration might be inferior to that of on-policy exploration. Could the authors explain why this happens? 

Also, most previous works for tabular and linear MDPs with adversarial loss functions use occupancy measure (OM)-based or policy optimization (PO)-based methods, both of which are model-based and require to learn the transitions explicitly to construct the loss estimator. Could the authors intuitively explain how to construct the “loss estimator” without explicit learning of transitions?

### Questions
Please see my questions in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4