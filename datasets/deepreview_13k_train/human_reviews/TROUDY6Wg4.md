# Accelerated Preference Optimization for Large Language Model Alignment

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has emerged as a pivotal tool for aligning large language models (LLMs) with human preferences. Direct Preference Optimization (DPO), one of the most popular approaches, formulates RLHF as a policy optimization problem without explicitly estimating the reward function. It overcomes the stability and efficiency issues of two-step approaches, which typically involve first estimating the reward function and then optimizing the policy via proximal policy optimization (PPO). Since RLHF is essentially an optimization problem, and it is well-known that momentum techniques can accelerate optimization both theoretically and empirically, a natural question arises: Can RLHF be accelerated by momentum? This paper answers this question in the affirmative. In detail, we first show that the iterative preference optimization method can be viewed as a proximal point method. Based on this observation, we propose a general Accelerated Preference Optimization (APO) framework, which unifies many existing preference optimization algorithms and employs Nesterov's momentum technique to speed up the alignment of LLMs. Theoretically, we demonstrate that APO can achieve a faster convergence rate than the standard iterative preference optimization methods, including DPO and Self-Play Preference Optimization (SPPO). Empirically, we show the superiority of APO over DPO, iterative DPO, and other strong baselines for RLHF on the AlpacaEval 2.0 benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the optimization problem in the reinforcement learning from human preferences setup. It focuses on the direct preference optimization algorithm and proposes using the classical idea of Nesterov's acceleration. The paper theoretically proves that the algorithm reduces optimization sub-optimality but at the cost of increasing the statistical generalization error. Numerical results on the Mistral model with the UltraFeedback dataset are provided.

### Strengths
1. This paper is well-written and easy to follow.
2. It provides a new theory for validating Nesterov's extrapolation idea in the iterative DPO framework.

### Weaknesses
1. There is a trade-off between optimization error and statistical error in the developed theory. Therefore, it is unclear whether Nesterov's acceleration offers a true advantage over the naive method.
2. Empirically and theoretically, the advantages and weaknesses compared to direct reward optimization algorithms (e.g., PPO) are unclear.
3. Experiment results are somewhat weak and does not validate the theory.

### questions:
1. The implementation of Algorithm 1 is unclear.

    - To the reviewer’s understanding, new preference data is required in each iteration $t = 0, 1, \dots, T$. Is this correct? Could the authors clarify the preference collection process? Is the preference collected using the BT model with random noise?

    - Related to this, in the experiments, a reward model is used. Why not study direct reward maximization (e.g., PPO) both empirically and theoretically? To the reviewer's knowledge, direct reward maximization methods can handle such tasks effectively and demonstrate strong empirical evidence in practice.

    - How should (3.6) be implemented in practice? Could the authors provide more details? Should the parameter or the distribution be extrapolated? Additionally, how can this result be extended to cases where $ y $ is sequential? Is it straightforward to apply this closed-form solution?

2. The reviewer is concerned about the soundness of the theory.

    -  Assumption 4.3 is strong. Essentially, it requires $ \pi_t $ to be a purely stochastic policy. On the other hand, the optimal policy $ \pi^* $ in Theorem 4.4 is deterministic. Therefore, the theory with this assumption seems problematic in the asymptotic case.

    -  The implications of the theory are based on upper bounds and are weak. Could you provide simulations for a simple case to validate the tightness of the developed method? Additionally, could you use simulations to study the trade-off between optimization sub-optimality and statistical error?

      -  It is recommended to explain in the main text why momentum increases the statistical error.

3. Comments on experimental settings and results:

    -  In the experiments, it seems unusual to have 2k instructions per iteration. To the reviewer's knowledge, the entire dataset contains 64k samples. Could the authors explain the rationale behind this choice? Furthermore, why are the experiments conducted with only three iterations? Could performance continue to improve with more iterations?

    -  Why was the RMSprop optimizer used in the experiments instead of the Adam optimizer? The Adam optimizer includes momentum, which can also accelerate optimization, similar to Nesterov's acceleration technique. The reviewer would like to see empirical results using the Adam optimizer to determine whether the proposed technique shows a clear advantage in this scenario.

    -  The improvements on AlpacaEval and MT-Bench are promising but come with some concerns. Evaluation results on these two benchmarks can be manipulated (e.g., by increasing response length). The reviewer appreciates that the length-controlled win rate is used; this is a positive step. However, concerns remain, as the training data (ultrafeedback) is collected by GPT-4 and evaluation on these benchmarks also relies on GPT-4. Could you test your method on other, more reliable benchmarks, such as IFeval or math reasoning tasks?

    -  Empirically, the advantage of this approach over the model extrapolation technique introduced by Zheng et al. (2024a) is unclear. Additionally, the empirical comparison with direct reward optimization methods is also unclear, which is important for establishing the superiority of the proposed method and techniques.

### Questions
1. The implementation of Algorithm 1 is unclear.

    - To the reviewer’s understanding, new preference data is required in each iteration $t = 0, 1, \dots, T$. Is this correct? Could the authors clarify the preference collection process? Is the preference collected using the BT model with random noise?

    - Related to this, in the experiments, a reward model is used. Why not study direct reward maximization (e.g., PPO) both empirically and theoretically? To the reviewer's knowledge, direct reward maximization methods can handle such tasks effectively and demonstrate strong empirical evidence in practice.

    - How should (3.6) be implemented in practice? Could the authors provide more details? Should the parameter or the distribution be extrapolated? Additionally, how can this result be extended to cases where $ y $ is sequential? Is it straightforward to apply this closed-form solution?

2. The reviewer is concerned about the soundness of the theory.

    -  Assumption 4.3 is strong. Essentially, it requires $ \pi_t $ to be a purely stochastic policy. On the other hand, the optimal policy $ \pi^* $ in Theorem 4.4 is deterministic. Therefore, the theory with this assumption seems problematic in the asymptotic case.

    -  The implications of the theory are based on upper bounds and are weak. Could you provide simulations for a simple case to validate the tightness of the developed method? Additionally, could you use simulations to study the trade-off between optimization sub-optimality and statistical error?

      -  It is recommended to explain in the main text why momentum increases the statistical error.

3. Comments on experimental settings and results:

    -  In the experiments, it seems unusual to have 2k instructions per iteration. To the reviewer's knowledge, the entire dataset contains 64k samples. Could the authors explain the rationale behind this choice? Furthermore, why are the experiments conducted with only three iterations? Could performance continue to improve with more iterations?

    -  Why was the RMSprop optimizer used in the experiments instead of the Adam optimizer? The Adam optimizer includes momentum, which can also accelerate optimization, similar to Nesterov's acceleration technique. The reviewer would like to see empirical results using the Adam optimizer to determine whether the proposed technique shows a clear advantage in this scenario.

    -  The improvements on AlpacaEval and MT-Bench are promising but come with some concerns. Evaluation results on these two benchmarks can be manipulated (e.g., by increasing response length). The reviewer appreciates that the length-controlled win rate is used; this is a positive step. However, concerns remain, as the training data (ultrafeedback) is collected by GPT-4 and evaluation on these benchmarks also relies on GPT-4. Could you test your method on other, more reliable benchmarks, such as IFeval or math reasoning tasks?

    -  Empirically, the advantage of this approach over the model extrapolation technique introduced by Zheng et al. (2024a) is unclear. Additionally, the empirical comparison with direct reward optimization methods is also unclear, which is important for establishing the superiority of the proposed method and techniques.

### Soundness
2

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
DPO is a popular offline methodology for LLM alignment. It has led to a family of preference optimization algorithms with different formulations of loss functions and problem formulations. In this work, the authors formulate iterative preference optimization (a variant of DPO class of algorithms) as an optimization problem with proximal point method being the optimization framework. Consequently, the authors use Nesterov's momentum technique to speed up the convergence. 

The authors demonstrate theoretically that the new framework (APO) leads to faster converge in comparison to standard iterative preference optimization methods. They also conduct empirical experiments to demonstrate the improvements of APO

### Strengths
1. To the best of my knowledge, this is the first work that examines the converge of iterative DPO and proposes improvements towards the convergence specifically
2. The theoretical analysis demonstrates that APO does lead to faster convergence in comparison to standard DPO
3. The empirical results shows that APO leads to better alignment in comparison to the baselines.

### Weaknesses
1. To the best of my understanding, Equation 3.6 in the APO algorithm does not update the neural network weights. Instead it is derived by keeping reference of the policy from the previous and the current iterations. It is not clear how the final policy in step 7 is used in the next iterations in steps 5 and 6.
2. This work might benefit from additional baselines in the empirical studies - IPO, SPPO, SimPo, KTO and especially ExPO
3. To the best of my understanding, the extrapolation step adds additional memory overhead since it keeps a reference of two iterations of the policy. This might not be practical for very large language models.

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on reinforcement learning from human feedback (RLHF) for large language models (LLMs), specifically examining the iterative preference optimization framework. It first observes that existing methods within this framework resemble the proximal point method in the optimization literature. Building on this connection, the paper proposes the accelerated preference optimization (APO) framework. APO incorporates Nesterov's momentum technique, originally introduced in optimization, to accelerate the preference optimization process. Theoretically, it proves that APO achieves a faster convergence rate compared to existing methods. Experimentally, the authors demonstrate APO's superiority over DPO, iterative DPO, and other preference optimization methods on the AlpacaEval 2.0 benchmark.

### Strengths
1. The paper establishes a novel and intriguing connection between iterative preference optimization and proximal point optimization. This connection has the potential to inspire further research that leverages advanced techniques from classical optimization literature for preference optimization.
2. The paper presents a rigorous theoretical analysis of the proposed APO method, demonstrating that APO can achieve a faster convergence rate.

### Weaknesses
1. The theoretical results in this paper are not particularly strong and do not conclusively show that APO is superior to previous methods. Specifically, in Theorem 4.4, compared to DPO ($\alpha=0$), APO achieves a smaller optimization error by a factor of $1-\alpha$, but incurs a larger statistical error by a factor of $1/(1-\alpha)$. Therefore, in the finite-data case, it remains unclear whether APO is theoretically better than DPO. Similar concerns also arise in Theorem 4.8.
2. There is a mismatch between the theoretical results and the experiments in this paper. Theoretically, the paper proves that APO achieves a convergence rate of the order $\widetilde{\mathcal{O}}((1-\alpha) / t)$. This rate is meaningful only in the large-iteration regime, as it ignores certain constants. However, in the experiments, the LLM is trained with only a small $t=3$. This discrepancy creates a gap between the theoretical analysis and the empirical results. As a result, I believe that the improved convergence rate in theory does not fully explain APO's empirical performance, and the experimental results do not adequately reflect its theoretical convergence rate.

### Questions
In Equation (3.1), the loss function for reward models is denoted as $\ell\left(r, x, y^w, y^l, \pi_t\right)$. However, it appears that this function does not actually take $\pi_t$ as an input.

### Soundness
2

### Presentation
3

### Contribution
2
