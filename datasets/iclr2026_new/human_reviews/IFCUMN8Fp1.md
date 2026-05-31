## Human Reviewer 1

### Summary
This work presents a method for learning the transition and observation functions of POMDPs from action-observation sequences obtained through random exploration. The method works by estimating a similarity transform $P$, converting a standard learned PSR into an equivalent basis where transition and observation probabilities can be directly recovered, enabling downstream inference and planning.

### Strengths
**Originality of the approach.** The paper presents a novel method for estimating the transition and observation functions of POMDPs.

**Presentation flow.** The paper is technically deep, and even quite dense at times. However, the ideas are presented in a way that benefits the reader by allowing them to build on each other.

**Theoretical Soundness.** The paper establishes the correctness of the approach under clear assumptions.

**Significance of the contribution** Though it may be somewhat limited to very small POMDPs and comes with significant scalability concerns, the ability of the method to recover the transition and observation likelihoods is a clear advantage over prior work.

### Weaknesses
**Scalability.** The method is constrained to very small-scale domains. The data and computation requirements are impractical for even modest state spaces and observation sequence lengths. The approach is only validated on tiny POMDPs with 3 or 4 states in the state space.

**Planning evaluation.** While the paper motivates its approach through planning, as stated above, the experimental domains are so small that it is unclear whether the claimed potential planning benefits would generalize to more realistic problems.

**Practical motivation.** The broader motivation and real-world relevance of learning full POMDP models through this method are questionable. Even if the method could be scaled considerably compared to how it works presently, I don't immediately see when such a computationally intensive approach would be preferable to modern function-approximation or model-free alternatives.

### Questions
* In the problem setting, the authors mention "For the purposes of evaluation, we may also require the agent to learn a tabular reward R function by including rewards as observations", but it's unclear whether this is done in the experiments section. Could the authors please clarify this point?
* Could the authors please elaborate on potential methods for scaling the approach?

Typos / etc.
* Line 245: "We call this alternate grouping is called a..."

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
2

---

## Human Reviewer 2

### Summary
The paper studies learning discrete POMDP parameters from a single long action–observation sequence. Building on PSR/Hankel factorizations, the authors show how to compute a similarity transform that maps a linear PSR model to the original POMDP parameters (initial belief, observation, and transition matrices) under a set of assumptions. Because recovering each state separately is often infeasible, the authors prove recovery up to an observability partition, in which states that produce identical observation distributions across all full-rank actions are merged into the same group. Algorithmically, they (i) estimate a Hankel matrix from trajectories, (ii) obtain a low-rank factorization, (iii) recover a similarity transform via joint diagonalization over full-rank actions, and (iv) infer partition-level transitions and per-action observation matrices. Experiments on Tiger, T-Maze, and Sense-Float-Reset variants evaluate parameter recovery errors and planning returns with a PO-UCT planner run on the learned model.

### Strengths
- The paper introduces recovery up to a full-rank observability partition and a similarity-transform approach that reconstructs POMDP parameters via joint diagonalization over full-rank actions. This combination appears novel and relaxes identifiability assumptions of prior tensor-based POMDP methods
- The work moves PSR theory toward interpretable model-based planning, yielding explicit $b_\pi, O$, and $T$ parameters instead of opaque predictors. The partition perspective offers a practical middle ground between exact recovery and real-world observability, with potential impact on safe or explainable model-based RL.
- The empirical tests, though small, validate the feasibility of the end-to-end pipeline from estimation to planning.
- The Sense–Float–Reset example and the step-by-step reconstruction pipeline make the ideas concrete. Figures illustrating partitions and transitions are clear and help the reader follow the matrices involved.

### Weaknesses
- Several assumptions look strong for realistic POMDPs and probably require more discussion:
    1. the chain over $(s,a,o)$ under a uniform random policy is ergodic and mixes to a stationary distribution from which the Hankel is effectively estimated; 
    2. existence and practical identification of “full-rank actions” for each state partition;
    3. independence properties of Back’s rows when restricted to histories; and 
    4. starting the Hankel with the stationary distribution $b_{\pi}$ rather than an arbitrary $b_0$ (the paper later argues it emerges in the limit, but this places the burden on data).

    I would recommend a dedicated subsection up front explaining why such assumptions are acceptable, when these hold in common environments/benchmarks, and where they might fail.
- Only tiny POMDPs (3–6 states) are considered. Several plotted trends are not discussed in the text (e.g., when the proposed method underperforms baselines in planning return), and there is little analysis of why.
- A comparison to baselines sharing the same assumptions and goal (no access to the transition/observation dynamics+model learning) is missing (e.g., model-based RL).
- Although the appendix derives an exploration count (Figure 5), the text never reports total time (wall clock); the Hankel grows exponentially in the observability length, and PO-UCT is time-demanding, so practical limits matter.
- Planning is done with a shallow PO-UCT at the partition level (depth 3/1000 sim). It is unclear whether differences in returns stem from model quality or planner mismatch.
- Even if the actions are played uniformly at the model training time, there's no guarantee of _where_ the model is accurate after a finite number of steps; according to the underlying MDP dynamics, some parts of the MDP might be unexplored and so turn the model inaccurate in those regions, and there is no way to detect that phenomenon. As a result, the approach doesn't guarantee the usefulness of the learned model in a finite number of steps.

### Questions
- In Section 2, the observation model is written as $P(o_t = o \mid s_t = s, a_t = a)$  “on leaving the state,” This is non-standard against the usual $P(o_{t + 1} \mid s_{t + 1}, a_t)$ convention. How does this impact the belief computation? Are the two notions of observation functions strictly equivalent?
- In practice, you do not know which actions are full-rank. How do you detect $A_{\text{full}}$ from data robustly? What happens when no action is full-rank for some states?
- Could you expand on the practical plausibility of the Assumptions presented in Section 3.3? (cf. weaknesses)
- Does it make sense to start the computation from the stationary distribution $b_\pi$ (that you do not have access to since you can't observe the states)? Moreover, there is a stark difference between beliefs that you infer from sequences of actions and observations and the underlying occupancy measure of the (hidden) MDP. Could you elaborate on that?
- Is the theory expandable to non-uniform exploration strategies, e.g., with stochastic behavioral policies having full support (as standard in regularized MDPs)?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper looks at how you infer a model of a POMDP through only sequences of actions and observations.  In essence, the goal is to recover a notion of state with corresponding transition and observation dynamics.  The work builds off of PSR representations and seeks to learn a transformation of the representation to recover the POMDP.  The works make assumptions about the POMDP and is only able to recover models up to a (fairly restrictive) observability partition.

### Strengths
The paper is exploring an interesting problem, which is certainly at the heart of representation learning.  This problem was particularly of interest 10-15 years ago, and to my knowledge, was not solved.  While PSRs have been shown to be able to be efficiently and directly estimated from an action-observation sequences, POMDPs have not.  The PSR model class is strictly largely than POMDPs, but they do no admit the same finite latent state interpretation.  Even if you knew the underlying environment could be modeled as a POMDP, we don't have direct methods to extract that POMDP.  State of the art (disappointingly)  is still likely EM.  Returning to an open problem that the community has "forgotten" about is valuable.

The paper takes a novel approach of extracting a "similarity transformation" of the latent state vector representation of a linear PSR to recover the POMDP states, observation, and transitions.

### Weaknesses
The paper has a number of weaknesses cutting across soundness, presentation, and contribution.

As for contributions, while it seeks to address an unsolved problem that was never solved, it doesn't really succeed at doing so.  The authors' notion of an observability partition, and Theorem 1's limitation to only matching the POMDP in aggregate over the partition seems to be dodging the open question of identifying a POMDP representation.  POMDPs whose states can identified from their next observation distribution is an extremely limiting class.  While the toyest of toy POMDPs might satisfy this restriction (e.g., any POMDP with <= 2 states must satisfy it, which includes Tiger), that doesn't make it an interesting class.  T-Maze, for example, does not have this property as the long hallway would exactly be collapsed by the observability partition.  And indeed, the experiments include only a truncated T-Maze (for which no description is given in the paper that I could find).  If we're unconcerned with the recovered POMDP allowing negative probabilities for states within a partition, then why not be happy with linear PSRs?  Furthermore, the abstract claims it produces "proper probabilistic models leveragable by downstream inference operations."  But they are not "proper probabilistic models".  And what downstream operations are being referred to, when none are given (besides planning, for which PSRs suffice and are performative by the paper's own experiments).

As for soundness, there are a number of statements that lack precision.
* The abstract claims "[PSRs] cannot, however, yield direct estimates of transition and observation likelihoods", which seems wrong as PSRs have simple closed form transition updates, observation distributions.  Indeed on line 178 the authors say, "A PSR can be used to compute the likelihood of observations ..."
* The Singh et al. (2004) paper defines a "system dynamics matrix", but the SDM is not a Hankel matrix at all (which 3.1 seems to suggest it is).  The first column of the SDM (assuming tests start with the empty test) would be all ones.  The first row of the SDM (assuming histories start with the empty history) would not be all ones, as some pairs of tests are mutually exclusive.
* Similarly, Equation (6) doesn't come from Wolfe nor is it the ${\hat P_{\cal T, H}}$ matrix from Boots.  Those both use the SDM.
* The paper makes an early remark that data is gathered with a uniform random exploration, but doesn't elaborate further or include it formally as an assumption.  Yet, equations (1-6) all depend on that requirement for them to make sense, otherwise conditioning on future actions might leak information about past observations.  See Bowling et al. (2006, ICML).
* Line 163: Doesn't this need proof or a citation?  
* In 3.3, it sure seems like assumption 3 is redundant.  Assumption 2 states ${\bf Back}$ is full rank.  So, the rows of ${\bf Back}$ must be linearly independent, as the rows are the $|S|$ dimension in the $|S|\times\infty$.

In addition, the experiments are not particularly compelling.
* There is no description of what the shading in Figure 3 means.

### Questions
1. In what way does this method provide a "proper probabilistic model" that PSRs do not?
2. What would happen if the underlying system was a PSR that could not be represented with a finite-state POMDP?  What would your learning algorithm extract for the similarity transformation?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper addresses the problem of learning discrete POMDP parameters from action-observation sequences without prior knowledge of the state space or transition dynamics. The authors make a solid theoretical contribution by establishing a novel connection between Predictive State Representations (PSRs) and tensor decomposition methods for POMDP learning. Their key result (Theorem 1) characterizes what can be learned from observations: the method recovers transition and observation matrices up to a full-rank observability partition, where states sharing identical observation distributions across all full-rank actions are grouped together. This relaxes restrictive assumptions from prior tensor-based approaches that required unique observations per state for each action. The authors develop a theory-driven algorithm that: (1) constructs a Hankel matrix from data, (2) performs spectral decomposition to obtain a PSR model, (3) recovers the similarity transform using joint diagonalization of observation matrices from full-rank actions, and (4) extracts probabilistic POMDP parameters. Experiments on small-scale benchmarks (Tiger, T-Maze, Sense-Float-Reset with 2-4 states) demonstrate convergence of learned parameters to ground truth and show that planning performance matches that of the true POMDP model, validating the theoretical framework's practical viability.

### Strengths
**Solid theoretical contribution**: Establishes the first formal connection between PSRs and tensor decomposition methods for POMDP learning. Theorem 1 characterizes learnability—recovering transitions/observations up to full-rank observability partitions—and relaxes prior assumptions by requiring observation uniqueness only across all full-rank actions (not per-action), enabling learning of a broader class of POMDPs.

**Principled theory-driven algorithm**: Clear pipeline from Hankel matrix construction to PSR learning to similarity transform recovery via joint diagonalization. The approach of using full-rank actions as anchors to extract probabilistic parameters is elegant and directly motivated by theory.

**Convincing experimental validation**: Learned parameters converge to ground truth with <10⁵ samples for small problems, and planning performance matches true POMDP models. Figure 4 visualization provides clear evidence of meaningful recovery.

**Well-motivated problem**: Addresses fundamental gap where PSRs lack explicit probabilities for inference while tensor methods are too restrictive. Real-world examples (hidden locking mechanisms) effectively motivate the work.

### Weaknesses
**Major:**

- **Limited experimental scale and analysis**: Experiments only test 2-4 state problems with no evaluation of how performance scales with state space size. Runtime complexity O(|S|(|A||O|)^(2n_obs+2)) is exponential in observability length, but no empirical analysis demonstrates where this becomes prohibitive. Missing comparisons with other POMDP learning methods (e.g., EM-based approaches, other spectral methods). While the experiments serve to validate the theory, these limitations significantly reduce the practical contribution of the algorithm. A clearer failure analysis showing where the method breaks down and computational time comparisons would strengthen the work.
- **Restrictive algorithmic requirements reduce practical applicability**: The algorithm fundamentally requires at least one action with a full-rank transition matrix to recover observations—many real-world POMDPs may lack this property (e.g., deterministic systems, heavy aliasing). The ergodicity assumption may not hold in systems with absorbing states or disconnected components. While the paper is honest about partition-level recovery, it underemphasizes how these structural requirements limit the class of learnable POMDPs in practice.
- **Together, these limitations constrain practical impact**: The combination of scalability concerns and structural assumptions means the algorithm's applicability remains narrow, despite the solid theoretical contribution.

**Minor:**

- **Presentation could be clearer**: Dense mathematical exposition without pseudocode makes the algorithm difficult to follow. An intuitive explanation before diving into formalism and explicit algorithm pseudocode would improve accessibility.
- **Missing ablation studies**: No experiments examining key design choices (e.g., impact of normalization step in Section 4.3, joint vs. per-action diagonalization, sensitivity to Hankel matrix size).
- **Limited engagement with recent work**: Would benefit from discussion of or comparison with recent neural approaches to POMDP learning and connections to related system identification literature, though this is not critical for the theoretical contribution.

**Note**: These weaknesses do not diminish the solid theoretical contribution, but they do limit the overall impact of the work.

### Questions
**Scalability**: Can the authors provide experiments or analysis on larger state spaces (e.g., 10-20 states) to demonstrate where the method becomes computationally infeasible? 

**Full-rank action requirement**: How restrictive is requiring at least one full-rank action in practice? Can the authors provide guidance for practitioners to verify this assumption holds for their domain, and characterize what happens empirically when violated?

**Hyperparameter sensitivity**: Table 1 shows widely varying parameters across domains (e.g., 1/κ from 0.015 to 0.34). How sensitive is the algorithm to these choices? Can the authors provide principled selection guidance or demonstrate robustness through sensitivity analysis?

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