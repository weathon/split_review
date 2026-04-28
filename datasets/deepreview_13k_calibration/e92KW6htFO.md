# MICE: Memory-driven Intrinsic Cost Estimation for Mitigating Constraint Violations

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
Constrained Reinforcement Learning (CRL) aims to maximize cumulative rewards while satisfying constraints. However, most existing CRL algorithms encounter significant constraint violations during training, limiting their applicability in safety-critical scenarios. In this paper, we identify the underestimation of the cost value function as a key factor contributing to these violations. To address this issue, we propose the Memory-driven Intrinsic Cost Estimation (MICE) method, which introduces intrinsic costs to enhance the cost estimate of unsafe behaviors, thus mitigating the underestimation bias. Our method draws inspiration from human cognitive processes, specifically the concept of flashbulb memory, where vivid memories of dangerous events are retained to prevent potential risks. MICE constructs a memory module to store unsafe trajectories explored by the agent. The intrinsic cost is formulated as the similarity between the current trajectory and the unsafe trajectories stored in memory, assessed by an intrinsic generator. We propose an extrinsic-intrinsic cost value function and optimization objective based on intrinsic cost, along with the corresponding optimization method. Theoretically, we provide convergence guarantees for the new cost value function and establish the worst-case constraint violation for the MICE update, ensuring fewer constraint violations compared to baselines. Extensive experiments validate the effectiveness of our approach, demonstrating a substantial reduction in constraint violations while maintaining policy performance comparable to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MICE, a novel constrained reinforcement learning method aimed at alleviating constraint violations. Its main contributions include:

1. Identifying the underestimation of cost value functions as a key factor contributing to constraint violations in constrained reinforcement learning, providing a new perspective.
2. Proposing a memory-based intrinsic cost estimation scheme that enhances the cost estimation of unsafe behaviors by storing unsafe trajectories.
3. Introducing new external-internal cost value functions and optimization objectives, offering theoretical guarantees for convergence and worst-case limits on constraint violations.
4. Experimental results demonstrate that MICE significantly reduces constraint violations while maintaining comparable policy performance to baseline methods, validating its effectiveness and reliability across various environments.

### Strengths
1. MICE introduces a novel approach that integrates memory into the CRL framework by drawing an analogy to human cognitive mechanisms. The idea of utilizing a memory module to store and leverage unsafe trajectories offers a fresh perspective for mitigating the underestimation bias of cost value functions.
2. The paper provides a rigorous theoretical foundation for the proposed MICE algorithm, including proofs of convergence and definitions of constraint violation limits, enhancing the robustness of the method.
3. The experimental design is comprehensive, testing across multiple scenarios and demonstrating MICE's effectiveness in reducing constraint violations while maintaining strong performance.
4. The authors emphasize reproducibility by providing code for replicating the results.

### Weaknesses
1. Despite experiments across several environments, the evaluation lacks assessments in a broader range of task types and robot types. The current evaluation primarily focuses on relatively simple simulated environments. It would be beneficial to see results on more complex tasks, including those with higher dimensional state and action spaces, and different dynamics. For example, tasks involving manipulation or navigation in cluttered environments would provide a more rigorous test of the method's generalizability.
2. The proposed method may struggle to scale to high-dimensional inputs, such as predicting costs based on visual input trajectories, as such extensions may incur excessive computational costs. The memory-based approach, while novel, could become computationally expensive as the dimensionality of the input space increases. The cost of storing and retrieving trajectories, as well as computing distances between them, could become prohibitive for high-dimensional inputs like raw pixel data from visual sensors. This could limit the applicability of the method in real-world scenarios where high-dimensional sensory data is common.
3. Although this method shows advantages over baselines in balancing constraint satisfaction and performance, it still does not address safety issues during the learning process, merely increasing conservativeness. The method appears to prioritize constraint satisfaction by increasing the conservativeness of the policy, which may lead to overly cautious behavior. While this reduces constraint violations, it might also hinder exploration and prevent the agent from discovering more optimal policies that operate closer to the constraint boundaries. The method does not explicitly address the issue of safety during the learning phase, which is critical in real-world applications where unsafe actions during training can have severe consequences.

### Questions
1. The approach for addressing cost underestimation in MICE is heuristic, but Figure 5 indicates that this method can still ensure that actual costs align with thresholds rather than being excessively low. The reviewer is curious about how the authors resolve this issue—specifically, how they maximize costs (implying limits on hazardous behavior) while largely avoiding constraint violations.
2. Could the authors demonstrate the scalability of MICE across more tasks and in more complex settings, particularly with high-dimensional inputs (e.g., trajectories based on images)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates underestimation bias of cost value function in actor-critic based safe RL algorithms. It provides an overview on why this underestimation occurs and proposes MICE method which learns an "intrinsic cost" to compensate this underestimation bias. The contributions include (i) designed flashbulb memory module which outputs intrinsic cost which is subsequently used to mitigate underestimation in cost-value function, (ii) provided theoretical bound on the worst-case constraint violation for MICE update and convergence guarantee, (iii) performed a number of empirical experiments to ascertain the validity of the proposed approach.

### Strengths
1. The paper is written in an easy-to-understand manner and addresses an important problem in safe RL: value underestimation, which impacts most (if not all) safe RL algorithms.  

2. The motivation behind this paper is clear and it provided useful theoretical analyses demonstrating the convergence guarantee and bound on constraint violation.  

3. The paper performed a variety of experiments showing the outperformance of its method, sensitivity analysis of hyper-parameters, ablation study and robustness validation.

### Weaknesses
1. Baseline which addresses underestimation bias

I understand that the underestimation bias was caused by the $min$ operator when safe RL algorithm is trying to fit the action-value function for cost $\hat{Q}_c$. This is analogous to the overestimation bias for reward when RL algorithm uses $max$ operator while fitting action-value function $\hat{Q}_r$.  

For the overestimation bias, what RL algorithm (e.g. TD3) did was that it uses the minimum of the output from two separately-learned action-value networks $\hat{Q}_r^1, \hat{Q}_r^2$ for policy update. Similarly, can't we use the maximum of the output from two separately-learned action-value networks for cost $\hat{Q}_c^1, \hat{Q}_c^2$ to combat this underestimation bias in cost? This sounds like a possible simpler baseline to me.  

2. Elaboration on Eq3

I think it'd be good for the paper to discuss how they design the formula for intrinsic cost. I can't fully grasp why the intrinsic cost is designed this way just by reading the main paper. For example:

a. What does the discount factor here signify? This "intrinsic discount factor" is different from the reward and cost discount factor and its exponent is $k$: iteration number of value estimation. Why is there compounding discount as the iteration increases?  

b. The L2-norm distance depends on time index $t$ such that it only compares the state-action similarity (between current trajectory and historical trajectory) at time $t$. This is quite counterintuitive because RL policy function or value function are usually not time-index dependent.  

c. The weight $\omega$ seems to be another hyper-parameter. How does one decide the right weight to use? The paper does state that $\omega$ should be between 0 and 1 but finding the right value still seems to be tricky.  

3. Explanation on how MICE eliminates underestimation bias

The paper mentions that MICE injects overestimation into the cost value-function estimate. Injecting overestimation bias to an underestimated function does not mean the underestimation bias is correctly eliminated since the injected overestimation could under-compensate or over-compensate the pre-existing underestimation bias.  

I think the paper could perhaps elaborate more on how the overestimation introduced by MICE correctly mitigates the underestimation bias.  

4. Minor typo: "worst-case" in line 073

### Questions
Please refer to the weaknesses section as all my questions have been listed there. I'm more than happy to discuss and please let me know if I misunderstood or misses out anything.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the MICE algorithm, designed to address constraint violations in constrained reinforcement learning by mitigating the underestimation of cost values. MICE introduces an intrinsic cost signal inspired by flashbulb memory, which stores and references unsafe trajectories to adjust cost estimates for actions likely to result in constraint violations. Empirical results on various safety-critical environments demonstrate a reduction in constraint violations with baselines.

### Strengths
MICE introduces a flashbulb memory module that stores unsafe trajectories, which is a novel approach in CRL to handle underestimation biases and improve constraint adherence.
Clear Problem Identification: The paper identifies and targets a critical issue in CRL: the underestimation of cost values leading to unsafe policy behavior, making this contribution relevant for safety-critical applications.
Theoretical and Empirical Contributions: MICE provides a theoretical framework with guarantees on constraint violation and convergence, supported by empirical results across various environments, reinforcing the algorithm’s applicability.

### Weaknesses
 - The writing of this paper requires significant improvement and polish. Many unclear notations and statements make it hard to follow. For example, in equations (3) and (4), the symbols $\tau_i^m(t)$ and $\tau(t)$ are never defined. The term $c_t^I$ is stated to be a function of $\gamma_I^k$, where $k$ represents the iteration number; thus, $c_t^I$ should also depend on $k$. The symbol $W$ is described as a set, yet in equation (3), $W$ appears to be used as a weight. Furthermore, it is unclear what $n$ represents in this context. Additionally, $c^E$ is not defined in equation (4).

- In the definition of $J_C^{EI}$, which depends on both extrinsic and intrinsic costs, $c^E$ seems to rely on flashbulb memory. This makes it a random variable dependent on the policy applied at each step. Fundamentally, the expectations in $J_C^{EI}$ and $J_C(\pi)$ differ, and thus, one cannot prove lemmas such as Lemma 1 by simply subtracting one from the other.

- I observed no discussion on the reward function. Typically, in safe RL, actions are chosen not solely based on the $Q$ function. Therefore, the Bellman equation presented in (6) does not appear to be correct. As mentioned in the introduction, safe RL is often solved using a primal-dual approach, which implies that the value function update should be in the SARSA form.

- Based on the experimental results, it seems the paper’s claimed contribution towards addressing training violations is not clearly substantiated.

### Questions
1. Over what is the expectation in the equation (5) taken?

2. Are there any justifications for calculating the difference in equation (3) in terms of individual steps? Two safe trajectories may not even contain the same state-action pairs at each step.

3. LP-based approaches are missing in the related work.

4. Typo in Figure 6? The word "constant" appears on top of each figure.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present MICE, a method to combat the cost underestimation problem in constrained RL. CRL cost value functions often underestimate the cost of actions taken, resulting in risky actions being taken more often than they should.

In order to address this, the authors propose a few key innovations:
1. An explicit memory storage system for bad trajectories that violate some threshold of cost.
2.  A generator model that determines an 'intrinsic' cost value for trajectories based on the stored dangerous trajectories
3. The intrinsic cost is added to the extrinsic cost, training the cost critic to estimate bad state-action pairs closer to their true cost.

### Strengths
This work is well-motivated in that it addresses an as-of-now open and broad problem in CRL, which is as much a question of study as overestimation is in value-function RL. Their idea to mitigate underestimation by explicitly storing violating trajectories seems sound as it helps counter some potential problems that could arise with constrained cost estimation in RL using function approximation such as loss of network plasticity or catastrophic forgetting. 

The bound provided in Theorem 1 also lends credibility to the idea, as it shows (seemingly convincingly based on the proof provided in the appendix) that this method should guarantee an improvement in cost estimation. 

The results in Figures 3 and 4 indicate robustness to the performance criteria while maintaining constraint validity across the environments tested. While MICE does not always reach the performance of competing baselines, it does so by ensuring coherence with the constraint thresholds indicated, which is the desirable outcome.

The ablations also provide interesting insight into the effects of changing the key hyperparameters such as constraint threshold and memory capacity, where the performance/constraint behaviour of the method changes as expected, which indicates that the intuition behind these mechanisms inferred by the authors is correct.

The clarity of the main text is fairly high and consistent across the paper, and the authors avoid bloviation or confusion by drawing clear conclusions and analogies (e.g. the comparison to the bio-inspired traumatic memory mechanism in humans is intuitive and sets up the main idea nicely).

### Weaknesses
The method requires setting hyperparameters which have non-trivial effects on the performance and constraint following of the method, resulting in a potential complication in practice. How were these hyperparameters set in the paper? How can they be appropriately determined by a practitioner hoping to use this method for a problem where, for e.g. the acceptable level of constraint violation is subjective?

The use of explicit memory places an arbitrary distinction between acceptable and unacceptable trajectories, which will affect how the intrinsic costs are determined. If adhering to an arbitrary constraint level is required, this may be appropriate. However, what if many trajectories have costs just below the threshold and are therefore not stored?

Results:
- It is not clear why the standard deviation of results was provided, when the 95% confidence interval would probably be a more appropriate measure of uncertainty across runs.

Presentation:
- The plots are not always the clearest, as axes are sometimes labelled and sometimes not
- The plot legends do not indicate what value is changing (this has to be inferred from the plot titles and the main text)

### Questions
It is not entirely clear to me why a generator network is required as it would appear that an explicit memory and trajectory-distance metric are enough for the rest of the method to work. Why not simply store violating trajectories and then provide an intrinsic cost based on new trajectories' distance to the stored trajectories? What benefit does the generator provide?

### Soundness
3

### Presentation
2

### Contribution
3
