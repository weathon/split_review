# Model-Free Offline Reinforcement Learning with Enhanced Robustness

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Offline reinforcement learning (RL) has gained considerable attention for its ability to learn policies from pre-collected data without real-time interaction, which makes it particularly useful for high-risk applications. However, due to its reliance on offline datasets, existing works inevitably introduce assumptions to ensure effective learning, which, however, often lead to a trade-off between robustness to model mismatch and scalability to large environments. In this paper, we enhance both aspects with a novel double-pessimism principle, which conservatively estimates performance and accounts for both limited data and potential model mismatches, two major reasons for the previous trade-off. We then propose a universal, model-free algorithm to learn an optimal policy that is robust to potential environment mismatches, which enhances robustness in a scalable manner. Furthermore, we provide a sample complexity analysis of our algorithm when the mismatch is modeled by the $l_\alpha$-norm, which also theoretically demonstrates the efficiency of our method. Extensive experiments further demonstrate that our approach significantly improves robustness in a more scalable manner than existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work enhances offline RL by developing a scalable, robust model-free algorithm that optimizes worst-case performance within an uncertainty set. Using a double-pessimism principle to handle data uncertainty and model mismatch, the method adapts across settings without model estimation. Through theoretical analysis the author demonstrates the algorithm’s near-optimal data efficiency, advancing robustness and scalability in offline RL.

### Strengths
1. The paper introduces a "double-pessimism principle" that uniquely addresses both model mismatch and limited dataset coverage within a model-free framework
2. The authors provide a rigorous theoretical foundation, including sample complexity analysis and convergence guarantees, which enhances the paper's quality

### Weaknesses
1. The paper lacks sufficient experiments to demonstrate the effectiveness of the proposed method. For instance, there is no comparison with model-based baselines, and the evaluation environment is relatively simple.

2. There are no ablation experiments analyzing the functionality of the proposed "double-pessimism principle."

### Questions
1. As mentioned above, have the authors evaluated how the proposed appraoch performs in any of the D4RL environments, which are widely used in offline RL research?
2. Are there any strategies for fine-tuning parameters for specific tasks?

### Soundness
2

### Presentation
2

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
In this paper, the authors proposed a novel double-pessimism principle framework for offline reinforcement learning, which conservatively estimates the performance of offline policy learning and accounts for both the pessimism caused by limited data and potential model mismatch. Compared with previous methods that usually leverage model-based approaches, the authors proposed a model free algorithm to learn the optimal policy that is robust to potential environment mismatches, which enhances robustness in a scalable manner. The authors also provide sample complexity analysis of the algorithm and extensive experiments to further demonstrate that the approach is robust and scalable.

### Strengths
- The authors present a scalable and robust model-free algorithm to quantify both the uncertainty of model mismatch and limited dataset; the way of constructing the model mismatch pessimistic allows the authors to derive a model-free algorithms;
- The authors present the sample complexity result for both finite horizon case and infinite discounted case. 
- The authors demonstrate that with the double pessimism principle, empirically we can learn better policies compared with single pessimistic based algorithms.

### Weaknesses
 -My central question about the paper is that in practise how we can justify the uncertainty set in real case, and how we can estimate the parameters of the uncertainty set instead of directly assigning some upper hyperparameter.


### Questions
- In some environments such as mujoco, how can we identify what kind of uncertainty set we should use here, and how can we estimate the uncertainty set hyperparameters to ensure the policy we learn is under the real settings?

### Soundness
4

### Presentation
4

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
This paper presents a model-free offline RL algorithm using a "double-pessimism principle" to enhance robustness against model mismatches and scalability, effectively handling uncertainties from limited data and environment shifts.

### Strengths
1. The paper is well-structured.  
2. The double-pessimism principle effectively tackles uncertainties from both data limitations and environment mismatch, adding a valuable perspective to offline RL.  
3. By avoiding transition model estimation, the algorithm shows strong scalability potential for complex environments.  
4. The paper provides a detailed sample complexity analysis and shows performance improvements on benchmark tasks, supporting the method's effectiveness.

### Weaknesses
1. While the paper shows strong results, additional tests on more diverse, high-dimensional environments could provide a clearer picture of scalability, such as d4rl. Specifically, the current experiments are limited to relatively simple environments, and it's unclear how the double-pessimism principle would perform in more complex scenarios with continuous state and action spaces, or with high-dimensional observations. The lack of experiments on standard benchmark datasets like those in d4rl makes it difficult to assess the practical applicability of the proposed method.
2. Comparing other offline RL algorithms, such as CQL, IQL, etc., will further enhance the contribution of this work. The paper would benefit from a more thorough comparison with existing state-of-the-art offline RL algorithms. Without a direct comparison, it's hard to gauge the relative performance and advantages of the proposed double-pessimism approach. The absence of such comparisons makes it difficult to determine if the proposed method offers a significant improvement over existing techniques or if it simply achieves comparable performance.

### Questions
n/a

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new approach for offline reinforcement learning that emphasizes both robustness to model mismatch and limited dataset. The paper provides theoretical results regarding robust value estimation, sub-optimality gap, and sample efficiency. The empirical results also support the superiority of the proposed double-pessimism approach, compared to the single-pessimism approach.

### Strengths
- The paper proposed the first offline model-free algorithm with a robustness guarantee.
- The empirical results on toy environments show the proposed double-pessimism approach outperforms the single-pessimism baseline.

### Weaknesses
 - The proposed method has a higher sample complexity than the baseline (Shi & Chi, 2022) regarding gamma.
- Adding another pessimistic term might lead to overly conservative policies, especially when the model mismatch problem is not significant.
- The source code is not provided, making it difficult to assess the reproducibility of the results.
- It would be more practical if the authors could provide a real-world example where model mismatch is likely to occur and construct the uncertainty set based on that scenario. While the mismatch modeled by the \ell_\alpha norm is suitable for theoretical guarantees, it is unclear if real-world perturbations would follow this type.

### Questions
- In Figure 2, can the authors provide the standard deviations or confidence intervals for the y-axis of each method? The envelopes in Figure 1 were informative, but Figure 2 does not provide such.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to offline reinforcement learning (RL) by introducing a double-pessimism principle. This principle aims to enhance robustness and scalability by conservatively estimating performance, accounting for both limited data and potential model mismatches. The authors propose a model-free algorithm that is robust to environment mismatches and provide a rigorous sample complexity analysis for a specific case of mismatch modeling using the $l_\alpha$-norm. The paper also includes some experiments demonstrating the approach's effectiveness.

### Strengths
- The introduction of the double-pessimism principle is a significant contribution to offline RL. By addressing both data limitations and model mismatches, the approach provides a more comprehensive framework for robust policy learning.
- The paper offers a detailed sample complexity analysis for the $l_\alpha$-norm model, which theoretically demonstrates the efficiency of the proposed method. This analysis is crucial for understanding the algorithm's performance and provides a solid foundation for its claims.
- Some experiments conducted in both simulated and real environments showcase the practical applicability and robustness of the proposed algorithm. The results indicate that the double-pessimism approach outperforms existing methods in handling model uncertainty.

### Weaknesses
 - The paper's focus on perturbations over transition probabilities is a limitation. In real-world applications, perturbations can occur in various forms, not just in transition probabilities. This narrow focus may hinder the practical applicability of the approach in more complex environments where other types of perturbations are present. Specifically, the method does not address potential uncertainties in the reward function or the observation space, which are common in real-world scenarios. For example, in a robotic manipulation task, the reward might be noisy or the observations from sensors might be unreliable, and the current framework does not account for these possibilities.
- While the sample complexity analysis is rigorous, it is limited to the $l_\alpha$-norm model. This restricts the generalizability of the theoretical findings to other types of perturbations or uncertainty models. A broader analysis covering more general cases would strengthen the paper's contributions. The analysis should consider other common divergence measures or uncertainty sets, such as those based on KL divergence or Wasserstein distance, to demonstrate the robustness of the approach under different types of model mismatch. The current analysis provides limited insight into how the algorithm would perform under different types of uncertainty.
- For general perturbations, the approach may require solving large optimization problems for each update. This could significantly affect learning efficiency, especially in large-scale or real-time applications. The paper would benefit from a discussion on how to mitigate these computational challenges. The paper does not provide sufficient detail on the computational cost of the $\kappa$ calculation, which is critical for the practical implementation of the algorithm. The lack of discussion on computational complexity makes it difficult to assess the scalability of the proposed method.

### Questions
- Can you provide more details on the algorithm's implementation efficiency, particularly regarding the $\kappa$ calculation? What is its computational complexity?
- Does the current definition of perturbations ensure that their impacts are not cascading—meaning they don't affect future steps?

### Soundness
3

### Presentation
3

### Contribution
3
