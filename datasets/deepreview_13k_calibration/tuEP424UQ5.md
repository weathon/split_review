# On Generalization Within Multi-Objective Reinforcement Learning Algorithms

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Real-world sequential decision-making tasks often require balancing trade-offs between multiple conflicting objectives, making Multi-Objective Reinforcement Learning (MORL) an increasingly prominent field of research. Despite recent advances, existing MORL literature has narrowly focused on performance within static environments, neglecting the importance of generalizing across diverse settings. Conversely, existing research on generalization in RL has always assumed scalar rewards, overlooking the inherent multi-objectivity of real-world problems. Generalization in the multi-objective context is fundamentally more challenging, as it requires learning a Pareto set of policies addressing varying preferences across multiple objectives. In this paper, we formalize the concept of generalization in MORL and how it can be evaluated. We then contribute a novel benchmark featuring diverse multi-objective domains with parameterized environment configurations to facilitate future studies in this area. Our baseline evaluations of state-of-the-art MORL algorithms on this benchmark reveals limited generalization capabilities, suggesting significant room for improvement. Our empirical findings also expose limitations in the expressivity of scalar rewards, emphasizing the need for multi-objective specifications to achieve effective generalization. We further analyzed the algorithmic complexities within current MORL approaches that could impede the transfer in performance from the single- to multiple-environment settings. This work fills a critical gap and lays the groundwork for future research that brings together two key areas in reinforcement learning: solving multi-objective decision-making problems and generalizing across diverse environments. Code is available at: [https://anonymous.4open.science/r/morl-generalization](https://anonymous.4open.science/r/morl-generalization)

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies generalization in the context of multi-objective reinforcement learning (MORL), which extends standard RL to the case in which the reward function is a vector containing multiple conflicting objectives. In particular, the paper defines the problem as a contextual multi-objective MDP, in which a context variable defines changes in the MDP’s state-transition and reward functions. The goal of an agent is to learn a set of Pareto optimal policies that generalize over different contexts. Next, the paper introduces a set of environments that extends existing benchmark environments in MO-Gymnasium to the case in which the dynamics and the state space can be modified. The paper evaluates several state-of-the-art MORL algorithms in the introduced benchmark and shows that existing algorithms often do not generalize well to different contexts.

### Strengths
- This is the first work, to the best of my knowledge, that studies MORL under environments with changes in its dynamics/state-transition function. 
- The introduced benchmarks are potentially useful to the community for designing novel MORL algorithms that can tackle problems in which the MOMDP's dynamics can change.

### Weaknesses
 - Since the main contribution of the paper is the testbed containing new extensions of MORL benchmarks and an extensive evaluation of existing algorithms, it is possible that this paper would be more suitable to the Dataset & Benchmarks track than the main track of the conference.
- The theoretical contributions are limited to the definition of a contextual MOMDP, which follows directly from previously studied formalisms of MOMDP and contextual MDPs, and the definition of a normalized evaluation metric for evaluating agents in this formalism.
- The paper requires clarifications regarding the mathematical formulation of the problem, and its implications on the evaluation metrics used and the experimental results (see below).
- In particular, it is not clear if the existing MORL algorithms are performing poorly due to their limitations or if the proposed benchmark is actually impossible to solve with optimality (i.e., obtaining NHGR=1). For instance, in the Mujoco environments, it is impossible for an agent to act optimally w.r.t. all possible friction coefficients without having any form of access to the current coefficients.
- In the setting of linear utility, the hypervolume metric can be increased by adding solutions in concave regions of the PF, which do not result in an increase of utility. Hence, hypervolume would be misleading in the context of linear utility.
- The hypervolume metric is difficult to interpret and does not give information about the shape of the PF or which preferences/trade-offs the agent is able to solve.
- Computing hypervolume is NP-Hard, and is infeasible to compute in problems with many objectives (e.g. 10 objectives).
- While the authors addressed the problem of different reward magnitudes by normalizing the PF, I believe introducing a normalized metric of expected utility (and other metrics) are necessary for better evaluation of MORL algorithms due to the limitations of hypervolume.
- It is unclear whether (in both the problem formulation and in the proposed benchmark) the context is part of the observation, i.e., whether agents know which context they are in. If the agents do not have access to the context, it is expected that generalist agents do not perform well. In general, a different policy is required to act optimally with respect to each context, and learning a policy that optimizes for the average context will be probably suboptimal to every context (unless contexts are too similar). Hence, the NHGR metric in Definition 5 would never be equal to 1, even assuming access to a perfect algorithm that learns the optimal policy in Definition 3. I suggest the authors clarify whether perfect generalization (NHGR=1) is theoretically possible in these environments.
- Regarding the MO-SuperMarioBros, the paper mentions that “There are a total of 32 possible stages”. Is that correct? Based on the Appendix, there are 8 stages.
- In Section 6.1, what was the training budget in terms of environment interactions for the specialist and generalist agents? Since generalist agents have to learn to solve multiple contexts instead of only one, it would be fair that they are given sufficient time to learn them. Otherwise, would it be possible to explain the results solely on the fact that the generalist agents did not have enough training time?
- I also suggest discussing the hyperparameters used for the algorithms in the experiments. For instance, would it be necessary to use larger neural networks or larger replay buffers when we train an agent to optimize for many contexts simultaneously? It is not clear whether the algorithms do not perform well due to a lack of hyperparameter turning.

### Questions
Below, I have questions and constructive feedback to the authors:

1) Regarding Definition 3, what does it mean for a policy to be “generalized across contexts”? There are two options here: (i) learn a single policy that maximizes its expected value over contexts, possibly being suboptimal because a policy that is optimal to every context simultaneously likely does not exist; or (ii) learn a policy that is conditioned on the context, and then can adapt its behavior depending on the context. I suggest discussing and clarifying this aspect of the problem defined in Section 3. In case (ii), the environments introduced should contain the context as part of the state space.

2) In Definition 4, I suggest defining how the Pareto front is normalized and mentioning the range of the normalization, e.g., [0,1].

3) Given that, in Definition 3, the authors are restricting to linear utility problems (which induce convex Pareto Fronts), it is worth noting that hypervolume is a metric that considers Pareto-optimal points in concave regions of the Pareto front, which are not useful for increasing the expected utility. For example, if we have an optimal convex Pareto front and we add a point in a concave region, this point would increase the hypervolume but would not increase the expected utility. For this reason, I suggest focusing on expected utility metrics (following the utility-based approach) instead of using hypervolume, which is an axiomatic metric. Currently, it is contradictory that the paper advocates for utility-based approaches, but mainly uses an axiomatic metric for evaluation. I suggest the authors either justify their use of hypervolume in this context or adopt metrics more consistent with their utility-based approach (e.g., normalized expected utility).

4) It is unclear whether (in both the problem formulation and in the proposed benchmark) the context is part of the observation, i.e., whether agents know which context they are in. If the agents do not have access to the context, it is expected that generalist agents do not perform well. In general, a different policy is required to act optimally with respect to each context, and learning a policy that optimizes for the average context will be probably suboptimal to every context (unless contexts are too similar). Hence, the NHGR metric in Definition 5 would never be equal to 1, even assuming access to a perfect algorithm that learns the optimal policy in Definition 3. I suggest the authors clarify whether perfect generalization (NHGR=1) is theoretically possible in these environments.

5) Regarding the MO-SuperMarioBros, the paper mentions that “There are a total of 32 possible stages”. Is that correct? Based on the Appendix, there are 8 stages.

6) In Section 6.1, what was the training budget in terms of environment interactions for the specialist and generalist agents? Since generalist agents have to learn to solve multiple contexts instead of only one, it would be fair that they are given sufficient time to learn them. Otherwise, would it be possible to explain the results solely on the fact that the generalist agents did not have enough training time?

7) I also suggest discussing the hyperparameters used for the algorithms in the experiments. For instance, would it be necessary to use larger neural networks or larger replay buffers when we train an agent to optimize for many contexts simultaneously? It is not clear whether the algorithms do not perform well due to a lack of hyperparameter turning.

Minor: “long-term discounted reward” - > long-term discounted sum of rewards.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates a very important problem of generalization in multi-objective reinforcement learning (MORL), an area that has received limited attention compared to single-objective RL. The main contribution of the paper includes a novel testbed featuring diverse MORL domains with different contexts, which provides a systematic evaluation framework for generalization in MORL. The paper also presents a comprehensive analysis of state-of-the-art MORL methods (Envelope, GPI, CAPQL, PGMORL, MORL/D) using normalized hypervolume generalization ratio. Overall, the paper provides a foundation for understanding how MORL algorithms generalize across different environmental contexts and parameters, addressing a crucial gap in the current literature.

### Strengths
* The paper contributes a novel testbed featuring various multi-objective RL environments with parameterized environment configurations, facilitating valuable research in MORL generalization. 
* The proposed framework for evaluating generalization in MORL using normalized hypervolume generalization ratio is sound and promising. 
* The paper provides reasonable coverage of relevant literature and effectively justifies its claims with thorough experimental evaluations.
* The paper is generally well-written and easy to follow.

### Weaknesses
 * The proposed testbed appears to be a straightforward extension of MORL environments to generalization with limited variations, lacking clear evidence of full interpolation/extrapolation properties across context changes. Specifically, the variations seem to be primarily parameter adjustments within existing environments rather than fundamentally new environmental dynamics or state spaces. The paper does not demonstrate how these variations lead to a diverse set of challenges that would truly test the generalization capabilities of MORL algorithms, such as changes in the transition function or the introduction of novel environmental features.
* The evaluation lacks analysis of important MORL metrics such as sparsity, expected utility, and cardinality, which limits the comprehensive understanding of algorithm performance. For instance, while hypervolume measures Pareto coverage, it does not address how spread the solutions are within the Pareto front, which is an important concept in utility-based approaches. Similarly, the expected utility metric is essential as it directly reflects an agent’s ability to maximize total utility, which is the ultimate goal in utility-based approaches. Furthermore, the lack of sparsity metrics makes it difficult to assess the diversity of the solutions found by different algorithms, which is crucial for understanding their exploration capabilities.
* The paper's focus on utility-based approaches with limited discussion of different utility or scalarization functions restricts the broader applicability. For instance, for linear scalarization functions, the resulting Pareto front is usually convex while for non-linear scalarization functions, the resulting Pareto front may have concave regions. It is unclear which class of scalarization method is used and how different classes affect generalization in MORL. The paper should investigate how different scalarization methods impact the generalization performance of MORL algorithms. The current evaluation seems to assume a specific form of utility function, which limits the generalizability of the findings.
* The empirical evaluation is limited to environments with a small number of objectives (maximum 4) which raise questions about scalability and generalizability. Testing in environments with higher objective counts, such as the Fruit Tree Navigation environment (5-7 objectives) by Yang et al. (2019) or the MO-highway environment from the mo-gymnasium API, which can be configured for more objectives, would strengthen the paper. The current set of environments might not capture the complexities that arise when dealing with a larger number of competing objectives, which is a common challenge in real-world MORL problems.

### Questions
1. How does the proposed framework handle cases where utility functions are unknown, non-linear, or non-monotonic? 
2. What specific scalarization functions were used in the MORL algorithms, and how were weight vectors initialized in methods like the Envelope algorithm? 
3. Why were other MORL metrics such as sparsity, cardinality, and expected utility not considered during evaluation? 
4. How do MORL methods generalization affected by varying numbers of objectives in underlying environments? 
5. Can the authors explain the discrepancy in CleanRL SAC performance in default hopper environment which achieved 3000 episodic return vs the one reported in Figure 5 (left most plot)? Could this because of the hyperparameter? If yes, then a well-tuned SAC may outperform the MORL methods.


Minor comments:

In Definition 1, should the reward be represented as a vector in bold notation for consistency with Section 2? 

The related work should be placed in the main paper. This can be done by moving the detailed environment descriptions to the appendix for better space utilization.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper, based on the MuJoCo platform, presents a comprehensive set of parameter variations for different MORL (Multi-Objective Reinforcement Learning) testing scenarios. Additionally, it introduces a novel metric designed to standardize the evaluation of the Pareto front and hypervolume measurements. By establishing a wide range of parameterized benchmarks, this work evaluates recent state-of-the-art MORL algorithms across the proposed environment variations, highlighting the performance differences under diverse parameter settings. This serves as a valuable resource for researchers aiming to study the generalization capabilities of MORL algorithms, providing a flexible and well-defined platform for experimentation.

### Strengths
1. The paper introduces a substantial number of parameterized scenarios, significantly modifying standard MuJoCo test environments to induce pronounced changes in specific features. This extensive and detailed effort reflects a thorough approach in expanding the range of testing conditions.

2. It challenges the widely-used hypervolume metric by proposing a new metric based on hyperarea coverage, aimed at standardizing the quality assessment of the Pareto front.

3. Although there are some flaws in the writing, the overall readability is smooth, and the paper maintains a clear focus on its key contributions throughout the narrative.

### Weaknesses
1. **On the Use of Lebesgue Measure and Hypervolume:**
   The Lebesgue measure in two-dimensional space corresponds to calculating area. If we assume the solution set's Pareto front is a closed, well-defined curve, the area enclosed by the origin and the Pareto front can indeed be computed using the Lebesgue measure. In this specific two-dimensional case, where all solution sets are located in the first quadrant (i.e., all objective values are positive) and the origin is used as the reference point, the calculated hypervolume effectively becomes equivalent to the Lebesgue measure. While the authors propose normalizing the hypervolume, this normalization does not fundamentally change the underlying measure. The core issue remains that the hypervolume, whether normalized or not, is still a measure of the area enclosed by the Pareto front and the reference point. The magnitude of the Lebesgue value is smaller and does not alter the comparative outcomes of optimization results. A smaller hypervolume (HV) will still lead to smaller two-point Lebesgue values. Although $HV_{norm} $ and $NHGR$ exhibit slightly higher penalty effects compared to the default in challenging scenarios, they do not provide additional benefits in terms of interpretability. Therefore, the proposed normalization does not seem to address the issue of result surges caused by outliers, as mentioned by the authors. Consequently, the introduction of $NHGR$ based on the hyper-area ratio appears to lack sufficient motivation.

2. **Regarding Metrics in Figure 3:**
   The two metrics presented in Figure 3 are actually different measurement dimensions of the same indicator. The mirrored images illustrate the overlap between these two metrics, which suggests they cannot be considered as introducing two new metrics. Specifically, the optimality gap and IQM, while presented as separate metrics, are both derived from the same underlying data, namely the performance of the algorithms across different environments. The optimality gap measures the difference between the achieved performance and the optimal performance, while IQM aggregates these differences. The mirrored images in the figure highlight that these metrics are essentially capturing the same information from different perspectives, rather than providing distinct insights into the performance of the algorithms.

3. **Multi-Objective Reward and Weight Vector Scalarization:**
   Multi-objective reward and weight vector scalarization is a well-established method. A substantial body of work has demonstrated the inefficiency of single scalar rewards in MORL optimization, such as in PGMORL and dynamic-weight MORL. Incorporating this concept as part of the experimental results does not significantly contribute to your experimental results, as it reflects existing knowledge in the field. The paper does not provide a novel perspective on the limitations of scalarization in MORL, and the inclusion of these results does not offer new insights beyond what is already known.

4. **Modifications to the Traditional Mujoco Environment:**
  In the original Mujoco environment, altering these values only requires adding instructions in the `step()` function, which is facilitated by the Mujoco simulation environment's API. The paper does not clearly indicate or demonstrate any additional code development or engineering improvements in this aspect. The modifications made appear to be straightforward adjustments of existing parameters within the Mujoco framework, rather than a significant engineering contribution.

5. **Efficiency of Benchmarking:**
   The benchmarking approach appears inefficient, as no new algorithm is proposed to compare against the state-of-the-art (SOTA). The paper focuses on evaluating existing algorithms on a new benchmark, but does not introduce any novel algorithmic contributions. This limits the impact of the work, as it primarily serves as an empirical study rather than a methodological advancement.

### Questions
1. **Selection of Mujoco Environments:**
   Why were only certain environments from the Mujoco,i.e., only some of the two-ojective problems,  are selected as baselines for demonstration, while other important environments were omitted (problems of 3 or more objectives)? Including a broader range of environments would strengthen the validity and generalizability of the motivation.

2. **Modifications to the Traditional Mujoco Environment:**
   Is there any basis or reference for the numerical changes made to the standard Mujoco environment?

3.**Normalization range (NR):**
   Under what circumstances are NRs conducted, and why are they remain reliable despite changes in training or neural network parameters?

4.**Mujoco modifications:**
 Can you provide more details on any specific challenges encountered or innovations that has been made in implementing these modifications.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a framework and testbed for evaluating generalization in multi-objective reinforcement learning (MORL). **The authors claim that generalization in MORL is a crucial research direction, but existing MORL algorithms are not sufficient for MORL generalization.** To support the claim, the authors propose the concept of a multi-objective contextual MDP and introduce the normalized hypervolume generalization ratio (NHGR) as a metric for assessing generalization in MORL. To empirically test this, they modify existing MORL environments by adjusting key environment parameters and applying domain randomization techniques during training. The paper reports NHGR performance across different MORL algorithms during the evaluation phase and concludes by highlighting the need for further research on MORL generalization.

### Strengths
* Considering generalization in MORL is a sound direction in the RL community.
* The necessity of MORL generalization is empirically demonstrated in Section 6.2, partly supporting the authors' claim.

### Weaknesses
1. **The overall contribution and novelty of this paper remain incomplete.** While the paper highlights a promising research direction, it lacks a concrete solution for addressing the problem of MORL generalization. To enhance the paper’s completeness, the authors should propose and integrate their own method to tackle MORL generalization effectively.

2. **The authors' claim is not fully supported due to the unclear soundness of the proposed NHGR metric.**
* 2-1. For clarity, does the combined specialist Pareto front consist of the *filtered* nondominated value vectors from the *union* of nondominated value vectors across the 8 MORL algorithms, each trained individually on a specific context?

* 2-2. The computation of NHGR is highly demanding, especially as the number of MORL algorithms and contexts increases during evaluation. If performance can be directly computed for any given context, there would be little need for a generalized algorithm, as the "combined specialist" would suffice. This raises concerns about NHGR's practical applicability in scenarios with large computational requirements.

* 2-3. A key weakness of NHGR is that its denominator relies on the performance of existing MORL algorithms, which may not perform well in certain contexts or in environments with many objectives. In such cases, where the "combined specialist" performs poorly, NHGR becomes an unreliable metric.

* 2-4. The necessity for normalization in NHGR is questionable, especially since true upper and lower bounds for each objective are not typically known a priori. If these bounds are not tightly set, the reliability of NHGR results is compromised. Moreover, determining accurate bounds (e.g., $v^c_{min}$ and $v^c_{max}$) requires running multiple MORL algorithms, increasing computational complexity. Establishing these bounds is itself a challenging task, particularly during online training.


* 2-5. A potentially better approach would be to use the expected standard hypervolume across evaluation contexts, supplemented by the expected standard sparsity to address the limitations of relying solely on hypervolume.


* 2-6. Figure 1 does not align with the definition of normalization bounds $v^c_{min}$ and $v^c_{max}$. The reference point is determined by the x-coordinate of the upper-leftmost point and the y-coordinate of the lower-rightmost point.


* 2-7. For clarity, is the number of the episodes evaluated for each context is set at 100/(number of evaluation contexts) (excluding Mario)?


3. **The paper’s organization needs improvement.**
- 3-1.  It would improve the flow of the paper if Section 6.2 were moved closer to the background section to better emphasize the motivation behind the work.
- 3-2. Including the related work section in the main body of the paper would enhance readability, as it is critical for contextual understanding.
- 3-3. A more detailed explanation of how each MORL algorithm operates, such as the weight adaptation variant of MORL/D SB, would be beneficial (this could be placed in the Appendix for conciseness).

4. **Several technical clarifications are needed.**
- 4-1. Is SAC trained with a standard scalar reward function (described in Appendix D) for each context vector independently, or does it follow domain randomization (i.e., sampling random environment parameters for each episode)? I assume the authors intended the latter.
- 4-2. In Line 479, the phrase "...scalarized them using $f_{SORL}$​..." is unclear. Additionally, how many solution vectors are sampled for each algorithm?
- 4-3. How is the optimality gap calculated?
- 4-4. For the SAC implementation in Mario and LavaGrid, is it "SAC-discrete"? If so, how was SAC-discrete implemented, and how does its performance compare to DQN?
- 4-5. In Section 6.2, what is meant by the "upward speed" in the scalar reward formulation (Line 461 and Figure 6)?

5. Minor Suggestions:
- I recommend dividing paragraphs to improve readability.
- Line 302: "We introduce an 8-dimensional parameter..." should be corrected to "7-dimensional."

### Questions
Please see the weaknesses part above.

**Post Rebuttal Comment**


After careful consideration, I have revised my final rating. 

As the authors acknowledged, the proposed metric has inherent limitations and these can be mitigated by also providing standard metrics. Each standard metric in MORL - hypervolume, expected utility metric, sparsity, and so on - has its strengths and weaknesses; therefore, the best approach can be to report multiple metrics to complement one another. This principle can be applied to the paper's setting as well. Introducing a new evaluation metric for MORL is a promising research direction, and it may be harsh to penalize the effort solely because the metric is not perfect.

I hope the authors include a thorough discussion on the metric's limitations and potential mitigations in a future version, if possible.

### Soundness
2

### Presentation
2

### Contribution
2
