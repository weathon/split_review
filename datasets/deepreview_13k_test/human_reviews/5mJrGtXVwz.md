# VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Large language models (LLMs) are increasingly applied to complex reasoning tasks that require executing several complex steps before receiving any reward. Properly assigning credit to these steps is essential for enhancing model performance. Proximal Policy Optimization (PPO), a state-of-the-art reinforcement learning (RL) algorithm used for LLM finetuning, employs value networks to tackle credit assignment. However, value networks face challenges in predicting the expected cumulative rewards accurately in complex reasoning tasks, often leading to high-variance updates and suboptimal performance. In this work, we systematically evaluate the efficacy of value networks and reveal their significant shortcomings in reasoning-heavy LLM tasks, showing that they barely outperform a random baseline when comparing alternative steps. To address this, we propose VinePPO, a straightforward approach that leverages the flexibility of language environments to compute unbiased Monte Carlo-based estimates, bypassing the need for large value networks. Our method consistently outperforms PPO and other RL-free baselines across MATH and GSM8K datasets with fewer gradient updates (up to 9x), less wall-clock time (up to 3.0x). %

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
VinePPO uses Monte Carlo-based credit assignment, reducing reliance on large value networks and enhancing accuracy and efficiency. It outperforms PPO and other baselines on complex math tasks, particularly with challenging datasets. Performance improves with more Monte Carlo samples, demonstrating strong scalability potential.

### Strengths
VinePPO uses Monte Carlo-based credit assignment, reducing reliance on large value networks and enhancing accuracy and efficiency. It outperforms PPO and other baselines on complex math tasks, particularly with challenging datasets. Performance improves with more Monte Carlo samples, demonstrating strong scalability potential.

### Weaknesses
1. Lack of baselines. I suggest the author adding value-network-free methods as baselines, particularly GRPO [1] which also uses a PPO-like objective with the average reward of multiple rollouts as the baseline for the policy gradient.
2. Misuse of terminology. According to the hyperparameter setting for PPO provided in the Appendix where $\lambda = 1$ and $\gamma = 1$, PPO should produce an unbiased estimate for the value function. So it is better not to use "bias" in Line 467 and 475 but to use "inaccuracy".

### Questions
Questions:
1. The results show that VinePPO is quite promising for LLM reasoning, but can we extend it to the more general alignment task?
2. Is there any intuitive or theoretical explanation for why value networks fail to provide accurate estimates?

[1] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. CoRR, abs/2402.03300.

### Soundness
3

### Presentation
3

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
The paper proposes vine-PPO, which uses Monte Carlo-based estimates to replace the value function. This approach is far more accurate and therefore performs better than the parameterized value function. Although the cost could be a concern, the authors argue that inference or generation is much faster due to many inference-optimized modules. Additionally, because of the rapid increase in performance, it may even be more efficient.

### Strengths
- The idea of Monte Carlo estimates, although it has been used in traditional RL tasks, is novel for PPO in the context of LLMs. I find it quite interesting that it can achieve superior results even with K=1.
- The applicability stemming from the fact that it only replaces the value function, allowing it to be used in many PPO-like methods, is highly beneficial.
- The analysis of the value function helps clarify the motivation.
- The proposed method is simple and easy to follow, and the paper is well-written.

### Weaknesses
- Fundamentally, I think the difference between your approach and GRPO [1] and RLOO [2] is that you have fine-grained value estimations by generating multiple responses from each intermediate group state. However, since this involves more computation, I wonder about the trade-offs compared to GRPO.
- This question arises because you do not compare your method with GRPO and RLOO. As these methods also employ similar ideas, why only compare with the original PPO? The authors should clearly explain the selection of baselines, and efficiency comparisons should also include this line of research.
- Furthermore, I wonder why you do not report baselines that use finer credit assignment for the DPO objective. Since you report that PPO performs better in terms of credit assignment, I am curious how it still shows superiority even when DPO is combined with finer credit assignment.
- Additionally, in practical situations, if one needs to find an optimal K for training configuration, it’s unclear whether we can say that Vine-PPO is more efficient in general, as it might require more hand-engineering. However, training the value network also requires engineering, so I wonder about the complexity comparison between these methods.

References

[1] Shao et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

[2] Ahmadian et al. Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs

### Questions
- How does the method's dependency on K differ by model? I am also curious about the K ablation.
- Additionally, I think creating a graph to show the trade-off between larger K values and efficiency would be interesting.
- Very minor, but there is a missing period on line 264 (or 265).

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Large Language Models (LLMs) are increasingly being applied to complex reasoning tasks, ranging from solving math problems to developing code. The most common method for training these models is Proximal Policy Optimization (PPO), which addresses the credit assignment problem using a value network. However, this value network can be significantly biased, which may impact performance. The authors propose VinePPO, inspired by VineTRPO, to learn a value function from Monte Carlo (MC) samples. They demonstrate that the value function from PPO performs poorly, while the MC sample estimates of the value function show strong performance and leverage compute-efficient inference techniques.

### Strengths
- The author's observation that the issue with PPO was the value function estimates is very insightful, given that there has been a lot of work to replace PPO with new techniques.
- The paper was well written.
- The paper's experimental results provide a lot of interesting insights regarding issues around PPO's value function.
- The authors performed experiments across several tasks, model sizes, and model types.
- The authors' ablations studies show interesting pitfalls of the value function from PPO. Additionally, the authors clarify the tradeoff between VinePPO and PPO.

### Weaknesses
- I understand that the paper focuses on addressing the pitfalls of PPO; however, comparing it with RLOO [1] would provide practitioners with valuable context on which algorithm they might want to use in practice.
- The paper lacks details on how the inference engines were utilized to accelerate data gathering.

[1] Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs by Ahmadian et al. 2024

### Questions
- Missing citations
   - RL + LLM: [1, 4]
   - RL: [2, 3, 5]
- How does VinePPO compare to the RLOO baseline as the value of K increases in RLOO?
-Did you do large-batch PPO updates? (Refer to [6] for the large-batch updates.) If you didn’t use the large-batch setting, essentially what you do is compute all the data statistics offline. This approach allows you to avoid loading the reward model onto the GPU, enabling you to increase your batch size much higher than if the reward model were loaded onto the GPU.
- Why is PPO more deterministic in early steps, while VinePPO is more deterministic in later steps, as mentioned in the "Error per reasoning step" section?
- Could you share a plot showing the "explained variance" of the value function you learn with normal PPO? (see [7])

[1] Learning to Generate Better Than Your LLM by Chang et. al 2023
[2] Exploring restart distributions by Tavakoli et al. 2018
[3] Data-efficient deep reinforcement learning for dexterous manipulation by Popov et al. 2017
[4] Dataset Reset Policy Optimization for RLHF by Chang et al 2024
[5] Mastering the game of Go with deep neural networks and tree search by Huang 2016
[6] SimPO: Simple Preference Optimization with a Reference-Free Reward by Meng et al. 2024
[7] http://joschu.net/docs/nuts-and-bolts.pdf

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The key motivation of this manuscript is to locate and solve the problem, while PPO is finetuning LLM，the value network is inaccurate and has high variances. It finds that in heavy and complex reasoning tasks, PPO barely outperform a random baseline due to this issue. Thus, this paper proposes a simple and straightforward approach, so called VinePPO, which computes the value using unbiased Monte Carlo estimation and improve the credit assignment. Many experiments on MATH and GSM8K datasets with RhoMath 1.1B and DeepSeekMath 7B, show that the proposed VinePPO can consistently outperforms PPO and other RL-free baselines.

### Strengths
1.	The authors found the problem via systematical evaluation that, inaccurate value estimation can limit PPO’s ability to finetune LLMs in complex reasoning tasks. It can’t reflect the real reward and importance. This problem results in the barely fair performance compared with a random baseline.
2.	This paper proposes the VinePPO via utilizing MC samples to compute value in the PPO pipeline, and the value of a state can be estimated by the average return of K sampled trajectories from the state. 
3.	The experiments and analytics are convincing. The results of VinePPO is better than PPO, via improved credit assignment.

### Weaknesses
1.	The proposed VinePPO is a straightforward method to use MC estimation. However, MC has been studied for a long time. It has zero bias, but also has high variance and computational efficiency problem.
2.	This paper adopts the math reasoning problem. The state is the concatenation of input prompt and generated tokens, so the following trajectories can be sampled from any state s, and then MC computation can work. But, if the problem is more complex, not simple math problem, MC might not work, because long trajectory or low efficiency.
3.	In VinePPO, K is very important, because accurate MC estimation needs K be large enough, which also would cause low efficient issue.
4.	Based on the discussion above, the generalizability of VinePPO is not analysed and  solved in the paper.

### Questions
1.	The influence of K needs to be discussed, from both performance and efficiency.
2.	As MC is a method with high variance, does VinePPO outperform PPO when MC estimation is not inaccurate?
3.	In Fig 9, the ground truth is chosen as results via 256 MC samples. Is this reasonable?
4.	It might be more convincing to provide the resulting of credit assignment. For example, are critical steps detected by VinePPO?
5.	Some equations are not clear, for example:$S_{t+1} =  s_t;[a_t]$

### Soundness
2

### Presentation
3

### Contribution
2
