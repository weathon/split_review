## Human Reviewer 1

### Summary
This paper proposes CORectifier, a reinforcement-learning-based framework for Neural Combinatorial Optimization (NCO) that introduces hierarchical trajectory rectifications.

The key idea is to probabilistically replace partial segments of policy-generated trajectories with locally optimal fragments from expert solutions during training.

This “Rectified Reinforcement Learning” (RRL) paradigm aims to alleviate reward sparsity and poor sample efficiency in standard RL-based solvers while retaining the flexibility of sequential decision making.
Empirical results on TSP, ATSP, and PCTSP show significant improvements over prior RL-based baselines and competitive performance compared to supervised and unsupervised methods.

### Strengths
**Originality** 

-	The paper introduces an interesting and nontrivial attempt to integrate expert information into RL via partial trajectory replacement, bridging imitation and RL in a structured way. Extensive results with ablations, comparison with recent neural solvers
-	The three-level (batch, instance, sub-instance) rectification mechanism is well-motivated and could be a general recipe for hybrid learning in NCO.

**Quality**

-  common and consistent notation, good writing

**Significance**

-	Extensive results with ablations, comparison with recent neural solvers (not only RL-based ones) which show substantial gains in solution quality
-	The idea of reusing expert solutions as decomposable local fragments is promising, especially under limited supervision.

### Weaknesses
**Limited applicability beyond simple TSP-like problems**

The proposed rectification mechanism fundamentally relies on being able to replace local segments of a trajectory while maintaining feasibility.  
This assumption breaks down for problems with richer constraints (e.g., scheduling with precedence relations, capacitated VRPs, PDPs), where feasibility depends on multi-dimensional states (capacity, time, precedence).  
In such settings, ```Feas(a*, s)``` would likely fail for most rectifications, making the method ineffective.
Experiments are restricted to TSP variants, which all share the same single-tour structure.

**Lacking clarity**

The paper would benefit from a more detailed figure describing the rectification process or a small toy example. All in all, The definition of the rectifier $\mathcal{R}(\tau, \tau^\ast, \mathcal{M})$ seems underspecified (see questions). 

**Dependence on expert-labeled data**

The approach requires high-quality reference solutions for supervision. For larger or more complex problems, such data are difficult and expensive to obtain.

**Scaling behavior**

The method underperforms on larger instances compared to recent heatmap-based approaches. The authors should explicitly discuss why this happens (e.g., policy entropy collapse, reduced rectification success) and suggest possible remedies.

**Lack of detailed analysis of the rectifier’s behavior**

The paper would benefit from more in-depth analysis on the rectifier operation. E.g., showing the impact of rectification on the reward; analysing how often a rectification fails (possibly grouped by step t, as I reckon rectification in later stages is more difficult as most nodes are already visited)

### Questions
- How could CORectifier be applied to problems with more complex constraints, such as job-shop scheduling, capacitated VRPs, or pickup-and-delivery problems?  
Given that feasibility in these domains depends on non-local state variables, how would rectification be defined or enforced?

- In Algorithm 1 and Eq. (10), the rectification operator replaces certain actions in a sampled trajectory $\tau$ with successors of corresponding nodes in the expert trajectory $\tau^\ast$. However, after such a replacement, the subsequent actions in $\tau$ were originally generated under a different state (i.e., before rectification)- Could the authors clarify, how exactly the remainder of the trajectory, i.e., $\tau_{t+k+1:M}$ is constructed / restored to ensure feasibility?

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

## Human Reviewer 2

### Summary
This paper proposes CORectifier as a method to address the challenge in Neural Combinatorial Optimization (NCO), where it becomes increasingly difficult to explore better solutions as training progresses. The authors present an approach that refines the exploration results of reinforcement learning (RL) using optimal solutions, and then utilizes the refined trajectories for further model training.

Specifically, the proposed training process operates as follows:
First, a batch is constructed by mixing problems with and without known optimal solutions. Then, among the multiple trajectories explored in parallel, a subset is selected. The selected trajectories are subsequently improved using the optimal solutions and masked rectifiers, and the improved trajectories are used to train the model.

Experiments are conducted on TSP, ATSP, and PCTSP, and the proposed method is compared with various heatmap-based and sequential decision methods.

### Strengths
- The paper introduces a novel training approach that refines parallelly generated trajectories using optimal solutions.

- The idea of leveraging optimal solution information to improve the quality of RL-based exploration is innovative and holds potential to enhance both training stability and convergence speed.

### Weaknesses
- The proposed method can only be applied when an oracle solver is available, since it relies on optimal solutions during training. However, if such a solver exists, the need for Neural Combinatorial Optimization (NCO) diminishes; conversely, when no oracle solver is available, the proposed approach cannot be applied.

- The method appears to be limited to TSP-type problems (i.e., problems involving Hamiltonian path finding) and may not generalize well to other types of combinatorial optimization tasks.

- In the experimental results, the method shows inferior performance compared to heatmap-guided methods, particularly as the problem size increases. Moreover, in the comparison with sequential decision methods, there are considerable discrepancies between the reported results in this paper (Table 1 and Table 2) and those presented in the original papers (e.g., TSP-POMO, ATSP-GOAL).

### Questions
- Is the RRL Loss presented in Equations (11) and (12) different from the Loss function used in POMO [28]? If so, what are the key differences?

- In Section 3.2.2 (2), is there a specific strategy for selecting the subset $\mathcal{\widehat{T_i}}$? Is it chosen randomly, or by some defined criterion?

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

## Human Reviewer 3

### Summary
This paper presents CORectifier, an extension of reinforcement learning (RL) methods for solving combinatorial optimization problems (COPs). The key idea is to incorporate expert solutions (reference trajectories from oracle solvers) into the RL training process in a systematic way. Specifically, the proposed Rectified Reinforcement Learning (RRL) framework probabilistically replaces parts of the model’s predicted trajectories with expert segments, enabling the training procedure to benefit from both reinforcement learning (exploration-based optimization) and supervised/imitation learning (expert guidance). The method introduces a hierarchical rectification mechanism operating at batch, instance, and sub-instance levels, effectively balancing exploration and guidance. Empirical results on several COP benchmarks (TSP, ATSP, and PCTSP) show that CORectifier consistently outperforms prior RL- and SL-based baselines, achieving improved sample efficiency, stability, and scalability.

### Strengths
The paper is mathematically well-structured and takes care to clearly define all variables and formulations, which improves readability and rigor.

The proposed idea of combining supervised (imitation) and reinforcement learning is conceptually sound and aligns with recent efforts to improve sample efficiency and stability in neural combinatorial optimization.

The method has practical appeal, as many real-world optimization settings can provide partial or full expert solutions that could be leveraged in a similar rectification manner.

### Weaknesses
1)
The applicability of the proposed approach appears fundamentally limited to relatively simple combinatorial optimization problems such as TSP and ATSP, which involve minimal or well-structured constraints. The method’s core mechanism—replacing segments of a policy-generated trajectory with expert subsequences—implicitly assumes that any inserted segment remains feasible within the overall solution. However, in more realistic or constraint-heavy problems (e.g., CVRP, VRPTW, scheduling or assignment tasks with capacity or time-window constraints), such partial replacements can easily violate global feasibility, leading to invalid solutions or an extremely low feasible-sampling rate during training. This structural fragility makes the method difficult to extend beyond toy-like routing benchmarks. The paper does not discuss strategies for preserving feasibility under complex constraints, nor does it include experiments on problems with non-trivial feasibility conditions. As a result, the proposed approach seems best suited for simplified academic benchmarks rather than real-world CO applications.

2)
The paper would benefit from a stronger empirical validation of its claimed ability to leverage expert data. For instance, an ablation experiment varying the number of expert trajectories (e.g., 1K, 10K, 100K) could help demonstrate whether the model genuinely improves as more expert supervision becomes available. Such an analysis would clarify whether the reported gains stem from the proposed rectified learning principle or from engineering-heavy interventions such as dynamic scheduling, hyperparameter tuning, and imitation-based warm-up. In its current form, it remains unclear how much of the observed performance improvement can be attributed to the central idea of combining RL and SL, rather than to these auxiliary mechanisms.

### Questions
Line 080: in analogy to the language models when the next token grow increasingly distant from the initial state, leading to unstable and inaccurate predictions.
The sentence could be rephrased for clarity. I cannot understand what it means.

### Soundness
2

### Presentation
4

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes CORectifier, a rectified reinforcement learning (RRL) framework that integrates hierarchical supervision into reinforcement learning to improve sample efficiency and reward sparsity in neural combinatorial optimization (NCO). The proposed method regularizes the exploration process by probabilistically replacing partial policy-generated trajectories with high-quality segments from expert solutions.

### Strengths
1. The proposed method has good generality and can be adapted to multiple NCO approaches.
2. The core idea is simple and easy to understand, integrating expert-guided rectification into RL in a straightforward way.
3. The experimental section is rich, covering multiple tasks and baselines.

### Weaknesses
1. The motivation is not entirely clear. Although the paper points out three limitations of existing RL-based NCO methods, it does not clearly explain how the proposed method effectively addresses each of them.
2. The advantage of the proposed way to combine RL and imitation learning (IL) is not deeply analyzed. It is intuitive that integrating IL can improve RL, but it is unclear whether the proposed RRL provides substantial benefits over simple integration schemes such as first-IL-then-RL two-stage training or approaches like [1] that use local search to refine sampled rollouts as expert demonstrations during training.
3. During trajectory rectification, feasibility checks are applied, so the actual number of replaced segments is unknown. An analysis of this aspect would help understand the mechanism behind the improvement.
4. The backbone models used for each problem type are not clearly stated in the main text.
5. The proposed framework introduces many hyperparameters, raising concerns about potential tuning difficulty and task-specific parameter dependency.
6. The hyperparameter study lacks convincing justification. For instance, the choice of 0.1 for $p_{batch}$, $p_{inst}$, $\alpha$ and $\beta$ seems arbitrary, and it is unclear how performance changes with smaller values.
7. The technical presentation of the trajectory rectification process (involving masks and mathematical notation) is somewhat difficult to follow, which may hinder understanding of the implementation details.
8. The reference formatting does not fully conform to the ICLR citation style.

[1] Preference optimization for combinatorial optimization problems, ICML 2025.

### Questions
1. Are the three hierarchical levels (batch, instance, intra-instance) truly complementary? Could the authors provide ablation results for enabling/disabling each level independently?
2. Is the proposed approach applicable to non-routing combinatorial optimization problems?
3. The definition of $M$ as problem size seems inconsistent. In the Intra-instance Level section, $M$ sometimes appears to represent the length of the decision sequence. Could the authors clarify this definition?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5