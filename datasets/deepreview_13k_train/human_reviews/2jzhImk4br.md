# Strategic Exploration for Inverse Constraint Inference with Efficiency Guarantee

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
In many realistic applications, the constraint is not readily available, and we need to infer the constraints respected by the expert agents from their behaviors. The problem is known as Inverse Constraint Inference (ICI). A common solver, Inverse Constrained Reinforcement Learning (ICRL) seeks to recover the optimal constraints in complex environments in a data-driven manner. Existing ICRL algorithms collect training samples from an interactive environment. However, the efficacy and efficiency of these sampling strategies remain unknown. To bridge this gap, we introduce a strategic exploration framework with guaranteed efficiency. Specifically, we define a feasible constraint set for ICRL problems and investigate how expert policy and environmental dynamics influence the optimality of constraints. Motivated by our findings, we propose two exploratory algorithms to achieve efficient constraint inference via 1) dynamically reducing the bounded aggregate error of cost estimation and 2) strategically constraining the exploration policy. Both algorithms are theoretically grounded with tractable sample complexity. We empirically demonstrate the performance of our algorithms under various environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In applications such as robot learning, it is often the case that the learner (e.g. robot) must abide by certain safety constraints when learning to perform a task. Because such constraints can be hard to specify, methods of learning the constraints from demonstration have been proposed, an approach known as Inverse Constrained Reinforcement Learning (ICRL). Prior work has made one of the following assumptions: access to a known transition model or access to a generative transition model that can be queried at any state-action pair. The existing work that does not impose such assumptions has not examined efficiency and estimation errors. This paper proposes two algorithms for learning a set of feasible constraints that align with the expert preferences. Sample complexity bounds are presented for both algorithms. The algorithms are evaluated on Gridworld and Point Maze tasks.

### Strengths
The paper presents novel sample complexity guarantees on ICRL problems in the setting where the transition is unknown. While the paper presents substantial notation, Section 4 does a good job of describing the lemmas in understandable terms. Section 5, especially 5.1 and 5.2, would benefit from similar elaboration. The steps in the proofs are mostly explained well.

### Weaknesses
Several weaknesses are listed below, of varying importance.

I believe the paper would benefit from a broader discussion of the Related Works. More specifically, how does the paper and the setting it considers compare to the following works?
- Chou et al., “Learning constraints from demonstrations,” 2020 [1]
- Kim and Oh, “Efficient off-policy safe reinforcement learning using trust region conditional value at risk”, 2022 [2].
- Moskovitz et al., “Reload: Reinforcement learning with optimistic ascent-descent for last-iterate
convergence in constrained mdps,” 2023 [3].
- Lindner et al., “Learning safety constraints from demonstrations with unknown rewards,” 2024 [4]
- Kim et al., “Learning Shared Safety Constraints from Multi-task Demonstrations,” 2024 [5]

Nearly all of the results in the Empirical Evaluation section (Sec. 6) are visually difficult to parse. For example, the UCB results are almost entirely hidden in Figure 3’s top and middle rows (rewards and costs, respectively). While including numerous baseline comparisons is beneficial, considering including different plots in the appendix to make the comparison more interpretable. In addition to an unclear comparison to the baselines in terms of discounted cumulative rewards and discounted cumulative costs, neither BEAR nor PCSE appear to beat the Random algorithm in terms of WGloU score. It is also unclear if the shaded regions in Figure 3 represent standard deviation, standard error, or confidence intervals. Furthermore, the y-axis titles for rows 1 and 2 in Figure 3 are the same, making it unclear what each row represents. Overall, it is unclear to me what the takeaways from the empirical results are.

The paper assumes finite state and action spaces, as well as an infinite horizon. In the experiments, these assumptions do not always hold (e.g. Point Maze is a continuous environment). There is a brief mention in Appendix D.3 about the density model in the continuous space, but overall, the discussion of how the theoretical assumptions translate into the practical settings considered is lacking. Specifically, how are the state and action spaces discretized in practice? What are the implications of using a finite horizon in the experiments when the theoretical results assume an infinite horizon? These questions should be addressed to strengthen the connection between theory and practice.

In Theorem 5.6, the sample complexity of PCSE is given by the minimum of the sample complexity of BEAR and a term dependent on the minimum cost advantage function. In the proof of Theorem 5.6, the paper states that the sample complexity of BEAR (Theorem 5.5) applies to PCSE because it is optimizing a tighter bound. The justification is Corollary C.6. Examining the proof of Corollary C.6, the expressions in case 1 and case 2 do not appear to directly correspond to a tighter bound. Specifically, the left-hand side of case 1 involves a maximum over policies in a set, while the left-hand side of case 2 involves a maximum over the state-action space. It is not immediately obvious how one can be considered a tighter bound than the other. Further clarification on this point would be helpful.

The paper would benefit from further discussion of the optimality criterion. The first constraint, with the Q difference for completeness, “tracks every potential true cost function.” The second constraint, focused on accuracy, expresses that the learned cost function must be close to a true cost function. How does it “[prevent] an unnecessarily large recovered feasible set?” At a higher level, the paper would benefit from more motivation/discussion of why the estimation should be included in the optimization problem. In other words, why can we not naively solve the problem as though we had perfect estimates, and then handle the estimation errors exclusively in the analysis? As discussed above, Section 5 (especially 5.1 and 5.2) would benefit from non-technical elaboration in the style of Section 4.

In Equation 9, which defines the optimization problem of PCSE, the supremum is over distributions over the state space, rather than the state and action space. Furthermore, in the definition of $\Pi^r$, the difference between the value functions seems to be in the wrong order. Given that $\Pi^r$ is defined in terms of rewards, the value function of the expert policy should be greater than or equal to the value function of any other policy. Therefore, the inequality should be $V^{r, \hat{\pi}^*} - V^{r, \pi} \geq \mathcal{R}_k$, not the other way around. This is a critical point that needs to be clarified.

### Questions
Some questions are included in the weakness section. 

The PCSE approach, described in Algorithm 1, obtains an exploration policy pi_k by solving the optimization problem in Equation 9. In Equation 9, $\Pi^r$ (rewards, not costs) is defined as 

$$\Pi^r = \{ \pi \in \Delta: \inf_{\mu_0} \mu_0^T (V^{r, \pi} - V^{r, \hat{\pi}^*}) \geq \mathcal{R}_k \}$$

Because these are the value function of rewards, I am confused why the difference should not be flipped, such that:

$$\Pi^r = \{\pi \in \Delta: \inf_{\mu_0} \mu_0^T (V^{r, \hat{\pi}^*} - V^{r, \pi}) \geq \mathcal{R}_k\}.$$

In other words, why should the order of the two value functions not be flipped, given it is an infimum.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduce two exploratory algorithms, BEAR and PCSE,  to solve Inverse Constrained RL problem setting, where constraint signals are learnt from expert policies. The approach recovers a set of feasible constraints that align with expert preferences. A theoretical analyses of these algorithms is provided including sample complexity bounds.

### Strengths
Concrete theoretical analysis that is well detailed, along with good empirical results for the provided environments.

### Weaknesses
Although some experiments were performed on a continuous setting, it is unknown (not even addressed) how the algorithms scales in both continuous state and action spaces. The current test case is a simple environment with discrete actions.

### Questions
1) Please discuss challenges that you anticipate in scaling your approach to environments were both state and action spaces are continuous, and potential solutions to the challenges.  
2) Please include a discussion of how you might adapt your theoretical analysis and sample complexity bounds for high-dimensional continuous spaces in your future work.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses inverse constrained reinforcement learning, a problem in which we aim to infer a cost constraint by looking at expert's behaviour only. The specific setting works as follows: We can deploy a policy in the MDP to get a rollout of state transitions and expert's actions, but we cannot see the cost. We aim to infer a set of costs compatible with the expert's actions, which are assumed to be optimal, while minimizing the samples taken from the environment. The paper proposes two algorithmic solutions for this setting, a bonus-based exploration strategy called BEAR and a further refined version called PCSE, together with the analysis of their corresponding sample complexity and a brief empirical evaluation.

### Strengths
- The paper tackles an interesting problem setting that may have practical upside for relevant applications;
- The paper addresses the strategic exploration problem in ICRL, which it has been previously studied in settings with known dynamics or a generative model;
- The paper provides two algorithmic solutions and corresponding sample complexity results;
- The paper includes a numerical validation, which is not that common in purely theoretical RL papers.

### Weaknesses
I summarize below some of my main concerns about the work. More detailed comments are below.
- The paper dives into a theoretical analysis of a rather peculiar setting without providing proper motivations;
- The paper seems to have some presentation issues: I understood (most of) the interaction protocol at the start of Section 5, but some details are still obscure, whereas the notation does not look always sharp and detailed. The sample complexity results include some terms for which the dependence with $S, A, \gamma$ is not obvious;
- The paper lacks a in-depth discussion of the results, e.g., how they relate with prior works on IRL or ICRL with generative models, the considered assumptions (especially deterministic policies), computational complexity of the algorithms, the technical novelty of the presented analysis;
- The numerical validation does not seem to be conclusive. Most of the curves are not separated with statistical significance.

**COMMENTS**

MOTIVATION. The formulation of the setting could be more clearly motivated. While it is roughly clear the kind of applications that are target, it is less clear why some choices are made.
- Is the discounted setting more interesting than finite-horizon for ICRL?
- In which kind of applications we can expect to have unconstrained access to the MDP online, even though the expert acts under constraints? Do the authors have any example of an application with cost constraints that allows for unconstrained exploration?
- Also the PAC requirement is somewhat questionable: Under approximation errors of the MDP and expert's policy we are not guaranteed that the optimal policy for the costs in the feasible set is "safe" to use in the true MDP (i.e., it would respect the true constraint). This is common in other inverse RL paper, but while some sub-optimality can be acceptable in unconstrained RL, some violations of the constraints are less acceptable in a constrained setting.

PRESENTATION. The presentation is not always sharp in the paper. I am listing below some questions, suggestions on how I think it could be improved.
- Some broader context could be added to first sentence of the abstract, e.g., that we want to optimize an objective function under cost constraint(s);
- The equation at l. 143 likely includes a typo. The Definition 3.1 would also benefit from more context and a more formal introduction to the notation (e.g., what do the value functions mean exactly?). It requires quite a lot of time to be processed;
- I could not fully comprehend Eq. 2. Are $\zeta$ and $E$ defined somewhere? If that is the case, perhaps it is worth recalling their meaning here;
- The interaction setting shall be introduced earlier than Sec. 5.1 and some aspects are still not clear then. How is the reward accessed/estimated?
- Sec. 5.5: "The above exploration strategy has limitations, as it explores to minimize uncertainty across all policies, which is not aligned with our primary focus of reducing uncertainty for potentially optimal
policies." This is not fully clear and would benefit from further explanation. I thought the goal was to achieve the PAC requirement with minimal sample complexity. In general, the description of PCSE is not easy to process.

TECHNICAL NOVELTY. BEAR looks like a rather standard bonus-based exploration approach, in which the main novelty seems to come from adapting the bonuses expression to the ICRL setting. Can the authors describe if other uncommon technical challenges arise from the specificity of the setting (especially w.r.t. prior works) and how are they addressed? I am not very familiar with the related literature in solving ICRL with a generative model, but in theoretical RL is sometimes straightforward to get a "strategic exploration" result from a "generative model" result.

DETERMINISTIC POLICY. Assuming the expert's policy to be deterministic in MDPs is reasonable, a little less in CMDP. Can the authors discuss this point? It looks like they think determinism is necessary. Can they prove that formally?

COMPARISON WITH PRIOR WORK. The paper shall discuss how the presented sample complexity results compare with prior works in IRL, reward-free exploration, and, especially, ICRL with a generative model. Is the PAC requirement significantly different from prior works? Moreover, the $\sigma$ terms in the sample complexity may have hidden dependencies in $S, A, \gamma$...

OTHER COMMENTS
- ll. 175-181. Those considerations look informal if not incorrect. One can easily imagine optimal trajectories that do not fully overlap with the expert's one in the given example, whereas not all of the sub-optimal trajectories are necessarily satisfying constraints!
- How can the C_k bonus be computed in BEAR? It seems to include the advantage, but the estimation of the reward is not mentioned anywhere;
- Are the described approaches computationally tractable?
- Another alternative yet interesting setting is the one in which the cost is also collected from the environment, but the constraint (threshold) is not known;
- Some additional related works on misspecification in IRL https://ojs.aaai.org/index.php/AAAI/article/view/26766, https://arxiv.org/pdf/2403.06854 and sample efficient IRL https://arxiv.org/pdf/2402.15392, https://arxiv.org/abs/2409.17355, https://arxiv.org/pdf/2406.03812 could also be mentioned.

### Questions
I reported some of my questions in the comments above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper analyses the problem of learning the constraints underlying some expert demonstrations in a provably efficient manner. Given that multiple constraint functions are compatible with the observed behavior, the learning target is the set of cost functions compatible with them.

### Strengths
The problem setting of designing provably-efficient algorithms for ICRL is really interesting in my opinion.

### Weaknesses
The paper is based on Definition 3.1, which defines the notion of feasible cost set. However, because of the typos and of the absence of explanation provided, it is impossible to understand what is the feasible cost set in a formal manner. Specifically, the definition lacks clarity on the structure of the cost functions and how they relate to the observed expert demonstrations. Without a precise mathematical definition, it's unclear how the set of feasible costs is constructed, making it impossible to verify subsequent results. The lack of a formal definition makes it difficult to assess the validity of Lemma 4.3, which is crucial for the rest of the paper. Since all the theorems proved are based on Lemma 4.3, then it is not possible to understand whether the results are correct or not.

TYPOS:
- 103: what is a space? The term 'space' is used without specifying whether it refers to a vector space, a metric space, or another type of mathematical space. This lack of precision makes it difficult to understand the context of the definition.
- 107: there is an additional dot . not needed
- 137: $r$ should not be present in the tuple. The inclusion of the reward function $r$ within the definition of the Markov Decision Process (MDP) is redundant, as the reward is typically considered separate from the transition dynamics and state/action spaces.
- 138: no need to write "CMDP without knowing the cost", because this notation has already been defined earlier. This is redundant and does not add any value to the explanation.
- 139: the cost should be defined as bounded. The cost function $c$ is introduced without specifying whether it is bounded, which is a critical assumption for many theoretical results in reinforcement learning. The absence of this constraint makes the analysis incomplete.
- 139: simbol $\Pi^*$ never defined. The symbol $\Pi^*$ is used without a clear definition, making it difficult to understand its meaning and role in the analysis. It is not a standard notation and should be defined before being used.
- 141,143: bad definition of set. The definitions of the sets at lines 141 and 143 are unclear and seem to be missing a dependence on the cost function $c$, which is crucial for the analysis. The lack of clarity makes it difficult to understand the properties of these sets.
- ...: definitely too many typos. Have the authors read the paper after having written it? Why me and the other reviewers have to waste time in reading your paper if not even you have read it?

### Questions
None

### Soundness
2

### Presentation
1

### Contribution
2
