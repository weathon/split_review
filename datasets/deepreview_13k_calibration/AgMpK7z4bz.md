# Efficient Action-Constrained Reinforcement Learning via Acceptance-Rejection Method and Augmented MDPs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Action-constrained reinforcement learning (ACRL) is a generic framework for learning control policies with zero action constraint violation, which is required by various safety-critical and resource-constrained applications. The existing ACRL methods can typically achieve favorable constraint satisfaction but at the cost of either high computational burden incurred by the quadratic programs (QP) or increased architectural complexity due to the use of sophisticated generative models. In this paper, we propose a generic and computationally efficient framework that can adapt a standard unconstrained RL method to ACRL through two modifications: (i) To enforce the action constraints, we leverage the classic acceptance-rejection method, where we treat the unconstrained policy as the proposal distribution and derive a modified policy with feasible actions. (ii) To improve the acceptance rate of the proposal distribution, we construct an augmented two-objective Markov decision process (MDP), which include additional self-loop state transitions and a penalty signal for the rejected actions. This augmented MDP incentives the learned policy to stay close to the feasible action sets. Through extensive experiments in both robot control and resource allocation domains, we demonstrate that the proposed framework enjoys faster training progress, better constraint satisfaction, and a lower action inference time simultaneously than the state-of-the-art ACRL methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents acceptance-rejection augmented MDPs, a novel framework proposed to improve action-constrained reinforcement learning. The method aims to address the computational inefficiencies and architectural complexities in existing Action-Constrained Reinforcement Learning (ACRL), by incorporating two key innovations: an acceptance-rejection mechanism to filter out infeasible actions, and an augmented MDP to optimize policy training towards feasible regions by penalizing constraint violations. The framework is empirically tested against state-of-the-art ACRL benchmarks in robotic control and resource allocation domains. Overall, the idea of combining the acceptance-rejection method with the augmented MDP is interesting, but the work could be improved in both the methodology and the experimental demonstration (see Weakness and Questions below for further details).

### Strengths
1. The computational overhead caused by solving QPs is challenging in existing ACRL methods, particularly scaling to high-dimensional action spaces.

2. The paper integrates a multitude of concepts such as action-constrained reinforcement learning, Acceptance-rejection
method, and Augmented MDPs. These topics have been at the forefront of recent research trends.

3. The paper is well-organized, with clear explanations of the background, the proposed methods, theoretical foundations (including Proposition 1), and detailed experimental setups.

### Weaknesses
1. The two main components, i.e., the acceptance-rejection method and augmented unconstrained MDPs, seem somewhat contradictory. They represent opposing optimization strategies: the acceptance-rejection method directly filters out actions outside the feasible set, potentially leading to overly conservative decisions by restricting the search space; then, the augmented MDP penalizes constraint violations in a gradual way, providing a “soft” learning approach for the agent. However, this softer approach does not fully guarantee that actions remain within the feasible set, and the interplay between these two mechanisms is not clearly defined, raising questions about their combined effectiveness.

2. While some theoretical insights are provided, including optimality equivalence in Proposition 1, key theoretical gaps remain unaddressed. Specifically, for augmented MDPs, there is no guarantee that actions won’t violate constraints, i.e., a critical issue in action-constrained reinforcement learning. The paper lacks a rigorous analysis of constraint violation bounds or convergence properties, which are essential for establishing the reliability of the proposed method in safety-critical applications.

3. The introduction highlights the computational challenges of scaling quadratic programs to high-dimensional action spaces. However, the experimental analysis in Section 5 primarily explores action constraints in relatively lower-dimensional spaces. The performance of ARAM in high-dimensional action spaces (such as complex robotic manipulators) would benefit from more in-depth analysis, including a comparative study against existing ACRL methods that are designed for high-dimensional action spaces. The current experiments do not sufficiently demonstrate the practical advantages of ARAM in these challenging scenarios.

### Questions
1. How can the augmented MDP approach guarantee that actions remain within constraints? Even if complete avoidance of constraint violations is not feasible, it would be useful to establish an understanding, such as defining a convergence rate and probability that constraint violations will diminish to a certain margin of error over time.

2. Can the scalability of the proposed ARAM framework be demonstrated in high-dimensional action spaces, through a comparative analysis with existing ACRL methods?

3. Although the authors state "... we directly leverage the multi-objective extension of SAC that can learn policies under all the penalty weights." (page 2), it seems that multi-objective reinforcement learning approaches might be sensitive to hyperparameters, such as the penalty weight. Is ARAM similarly sensitive to this hyperparameter, particularly in its convergence behavior? Additionally, how is the penalty weight selected in practice?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel framework for action-constrained reinforcement learning, named ARAM, which integrates an acceptance-rejection method and an augmented Markov decision process to alleviate the low action acceptance rate problem under ARM. ARAM aims to avoid the computational burden associated with quadratic programs in existing ACRL methods while achieving less constraint violations. The authors demonstrate through experiments on robot control and resource allocation tasks that ARAM achieves faster training, better constraint satisfaction, and reduced action inference time compared to various recent ACRL algorithms.

### Strengths
- Well-written paper with clear objectives.
- Although the two key improvements (ARM and AUTO-MDP) are straightforward, the experimental results demonstrate the elegance and efficiency of this method in addressing the ACRL problem.
- The paper is well-supported with experiments that compare ARAM against various benchmarks, showcasing improvements in training speed, constraint satisfaction, and inference time.
- The authors have the intention to share the code.

### Weaknesses
 - The experiments are only conducted in simple simulation environments. Applying the method to real-world scenarios would make the results more impressive and convincing.
- Lacks experimental comparisons of the ARM acceptance rate.
- The paper lacks a discussion on the limitations of the method.

### Questions
- Does the choice of different target distributions in ARM have a significant impact on the final results?
- Is the ARM’s acceptance rate analyzed in detail across the different stages of training? It would be useful to understand if and how the acceptance rate varies in the proposed setup.
- What role do quadratic programs (QP) play in ARAM? QPs are not included in Algorithm 1 or Figure 2.
- How is MORL implemented in ARAM? Does it significantly increase computational requirements?
- The layout of Algorithm 1 in the paper needs adjustment.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to adapt the standard unconstrained RL method to ACRL via two proposed techniques: an acceptance-rejection method and an augmented two-objective MDP. It compares ARAM with various recent benchmark ACRL algorithms on MuJoCo tasks and Resource allocation for networked systems, showing the superiority of ARAM in terms of training efficiency, valid action rate, and per-action inference time.

### Strengths
1. This paper is well-written and easy to follow.
2. I appreciate the experiments in terms of the considerable evaluation metrics.
3. I am not very familiar with the ACRL field. From my perspective and limited knowledge of this field, I appreciate the proposed direction to solve the ACRL problem, I think it is a new try.

### Weaknesses
1. The proposed preference distribution tuning procedure seems a bit redundant. It is better to compare ARAM with fixed $\lambda$  to the baselines for a fair comparison. Otherwise, it is hard to distinguish whether the main components (acceptance-rejection method and AUTO-MDP) are more important or the preference distribution tuning procedure. As we can observe in Figure 11, ARAM is not quite robust to the  $\lambda$, and a single set of  $\lambda$  could not achieve satisfactory performance across all tasks.  To make the comparison more fair and isolate the effects of the main components, it would be helpful to suggest that the authors include results for ARAM with a fixed λ alongside the current results in the main paper and hope to see the superiority of ARAM without $\lambda$-tuning. This would allow readers to better understand the relative contributions of the acceptance-rejection method, AUTO-MDP, and preference tuning. Of course, you may not need to fully resolve this weakness, yet I suggest explicitly mentioning it as a limitation. 
2. Several experimental details have not been provided. For example, what is the value of M and $\kappa$ for all the tasks, and other parameters used? They are quite important details.

### Questions
1. Could you provide the value of $M$ and $\kappa$ for all the tasks?  Do you need extra tuning on these two hyperparameters? 
2. Could you provide the computation infrastructure?
3. Is it possible that ARAM with a single setting of fixed $\lambda$  outperforms other baselines across MuJoCo locomotion tasks? It is suggested that the authors conduct an experiment with a single fixed λ across all MuJoCo tasks and report those results, or explain why such an experiment might not be feasible or meaningful.
4. I find in Table 2 that NFWPO enjoys the highest valid action rate. That indicates that it requires a smaller number of QP operations, as opposed to DPre+ and SPre+. Yet in Figure 4, NFWPO shows the highest number of QP operations, which seems conflict to with the analysis in Lines 456-462. Please clarify this apparent contradiction and, if necessary, correct either the data or the analysis.
5. In the last row of Table 2, 0.77 is much lower than 0.84, thus I suggest not making it bold.
6. As claimed in the abstract, "We propose a generic and computationally efficient framework that can adapt a standard unconstrained RL method to ACRL through two modifications". Could the authors provide ARAM techniques with another backbone standard RL algorithm to support this claim?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work presents a groundbreaking approach to learning control policies that adhere to strict action constraints, making it perfect for safety-critical and resource-constrained applications. The authors introduce a novel framework that enhances traditional reinforcement learning methods by utilizing the acceptance-rejection method and an augmented two-objective Markov decision process.

### Strengths
The framework significantly reduces the computational burden associated with traditional ACRL methods, which often rely on solving complex quadratic programs (QPs). By utilizing the acceptance-rejection method, the need for QP operations is largely obviated, leading to faster training times.

### Weaknesses
The effectiveness of the acceptance-rejection method heavily relies on the quality of the initial policy. If the initial policy is far from optimal, it may result in a high number of rejected actions, which can hinder learning progress and increase computational overhead. While the augmented MDP approach aims to improve acceptance rates, it introduces additional complexity to the learning process. The design and tuning of the penalty function and self-loop transitions may require careful consideration, and improper tuning could lead to suboptimal performance. Specifically, the choice of penalty weight, which dictates the trade-off between constraint satisfaction and reward maximization, is not clearly addressed. Moreover, the self-loop transitions, while intuitively designed to encourage exploration within the feasible action space, could potentially lead to a bias in the learned policy if not carefully calibrated. The paper lacks a detailed analysis of how these parameters affect the overall performance and convergence of the algorithm.

### Questions
1. What metrics were used to evaluate the acceptance rate during the experiments, and how were these metrics calculated?
2. Is there a systematic approach to determine the optimal penalty weight, or is it left to empirical tuning?
3. Conducting more experiments on hyperparameter sensitivity is better.
4. Whether introducing AUTO-MDP in the theoretical aspect will affect the guarantee of convergence, while the current article only discusses the optimality.

### Soundness
3

### Presentation
2

### Contribution
2
