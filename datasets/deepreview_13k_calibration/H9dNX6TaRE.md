# Mitigating Reward Over-optimization in Direct Alignment Algorithms with Adaptive Importance Sampling

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 8, 3

## Abstract
Recently, Direct Alignment Algorithms (DAAs) such as Direct Preference Optimization (DPO) have emerged as alternatives to the standard Reinforcement learning from human feedback (RLHF) for aligning large language models (LLMs) with human values. Surprisingly, while DAAs do not use a separate proxy reward model as in RLHF, their performance can still deteriorate due to over-optimization – a phenomenon found in RLHF where the policy can exploit failures of the reward model to achieve high rewards but the actual quality of the model begins to degrade. Recent studies find that DAAs tend to increase probability mass on out-of-distribution responses and the training objective in DAAs is heavily under-constrained on these out-of-distribution (OOD) responses due to a mismatch between offline distribution and the LM policy. In this paper, we propose a method to mitigate the distribution shift between the offline distribution and the LM policy by multiplying with an importance weight to reflect the policy distribution. The resulting method, called Adaptive Importance Sampling (AIS), relies on importance sampling techniques and resolves the high variance issue in importance sampling without extra hyper-parameters. Our experiment results showed Adaptive IS can improve win rates by 15% while maintaining a lower KL budget compared to DAAs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the reward optimization problem in direct alignment algorithms (DAAs) from the angle of distribution shift. In existing DAAs, the KL estimation is only unbiased when the samples are on-policy. However, as the policy being updated during learning, the responses from the offline dataset become off-policy, and thus distribution shift happens.

To address this issue, the authors propose adaptive importance sampling (AIS) as a solution. Assuming the preference data are generated from the SFT policy, AIS applies an importance sampling weight on each data point to correct the off-policyness. This weight term is further adapted by an exponential coefficient which is the inverse of the response length to tradeoff the bias and the variance. AIS is first evaluated in a toy example and demonstrates better estimation of the KL divergence than its unweighted counterpart. When combined with DPO, AIS demonstrates better KL-win rate tradeoff and higher peak performance than the baseline in a simulated setup, following Gao _et al_, 2022. The authors also conducted some empirical analysis in the simulation setup to understand the detriment of distribution shift.

### Strengths
This work addresses a widely observed phenomenon where DAAs like DPO suffers from reward overoptimization even before completing the first epoch of the dataset. Insights into this phenomenon can help us understand the underlying mechanism of DAAs  and resolving this issue can mitigate the gap between online and offline algorithms and can provide us with computationally cheap yet performant alignment algorithms.

The proposed solution, AIS, is a principled algorithm with well-understood theoretical grounding. Empirically, AIS demonstrates more effective KL regularization and strong performance over the baseline. AIS is simple, easy to implement, and preserves the low computational cost of offline DAAs.

In terms of presentation, overall the paper is easy to follow. The work is well motivated and the method is clearly explained. The authors did a good job connecting to existing works in the literature.

### Weaknesses
Important analysis on the proposed AIS method is missing. Importance sampling is one of the simplest techniques to address off-policy learning. The authors claim that vanilla IS suffer from high variance and thus an adaptive heuristic is applied to make a tradeoff between the bias and the variance. However, there is no analysis into this adaptive heuristic to justify its necessity and to provide insights into how this tradeoff impacts the overall performance. Specifically, the paper lacks a theoretical analysis of how the exponential smoothing factor, which is the inverse of the response length, affects the bias and variance of the importance sampling estimator. A more rigorous analysis, perhaps including bounds on the variance or bias, would be beneficial. Furthermore, the paper does not explore the sensitivity of the method to different values of this smoothing factor. It is unclear if the inverse of the response length is an optimal choice or if other values could lead to better performance. 

Similarly, the empirical analysis in Section 4.3 demonstrates the detriment of distribution shift to DAAs. One natural question to ask is, as a method proposed for addressing distribution shift, how does AIS perform in these experiments? The current study does not provide any results to answer this question. It is crucial to demonstrate that AIS effectively mitigates the negative impacts of distribution shift in the same settings where the problem is highlighted. Without this, it is difficult to assess the practical value of the proposed method. The paper should include a direct comparison of AIS with standard DPO under varying degrees of distribution shift, showing how AIS improves performance and stability as the shift increases.

One limitation the authors did not call out in the limitation section is that AIS assumes that the preference dataset is generated from the SFT policy. However, this is not always the case in practice. Usually the responses in the preference dataset are sampled from different generations of the same data class, or even from different model classes. Thus this assumption is often violated and it hinders the effectiveness of AIS. The paper should acknowledge this limitation and discuss its implications for real-world applications. It would also be beneficial to explore how the performance of AIS degrades as the preference data deviates from the SFT policy, and perhaps suggest potential solutions to address this issue. 

Presentation-wise, the authors use inconsistent / incorrect citation formats through the paper. Calandriello _et al_ '24 should be cited in Section 3.1 for online DDAs. There are a few typos in writing. I think it should be "budget" in the last sentence of the abstraction. The Azar '23 and Gheshlaghi Azar '24 citations are citing the same paper.

### Questions
1. In Figure 2, Figure 4, and Figure 5, how was the KL computed? Was it estimated by taking on-policy samples from the current LM?

2. Could the authors provide online alignment algorithm results such as PPO in the main evaluation in Section 4.2? In my opinion, AIS does not need to outperform PPO. The main purpose is to provide better context to the readers. These results can help the readers understand how much of the online-offline gap can be explained by distribution shift and can be addressed by AIS. These results can also provide guidance for follow-up work and future research.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper primarily deals with the issue of reward over-optimization in specifically Direct alignment algorithms and proposes an adaptive low variance importance sampling strategy to mitigate the issue, with an exponential smoothing technique that balances bias and variance in IS estimates. The proposed method effectively reduces over-optimization by achieving higher model win rates and maintaining a lower KL divergence budget than baselines.

### Strengths
The paper primarily deals with the issue of reward over-optimization in specifically Direct alignment algorithms. The over-optimization issue is an extremely critical concern in the current alignment paradigms, and arises due to a distributional shift between offline training data and the LM's current policy, leading to increased probability on out-of-distribution (OOD) responses. The paper introduces an adaptive importance sampling strategy to mitigate the distributional shift issue using an exponential smoothing technique that balances bias and variance in IS estimates.

### Weaknesses
1. The importance sampling term defined in the equation in line 212, suggest that the original equation is E_{\pi_{\theta}}[\rho_theta]? Can you mathematically show why thats the case? In the context of online RLHF, it makes sense as shown in [1], but in offline whats the exact ideal optimization objective, leading to this importance weight? Can you specify, will be helpful. Also, highlight the difference from [1].
2. Whats the mathematical motivation behind choosing the value of the alpha? How does it affect the convergence?
3. There are several works on pessimism based methods to achieve reward over-optimization which are similar in principles, hence its not clear the novelty of the proposed work. A detailed comparison and contrast is critical to understand the novelty of the proposed approach.

4. The method is presented as an offline approach, but it's not clear if the importance sampling is solely for variance reduction or if it plays a role in adjusting the distribution shift. A clearer explanation of the role of importance sampling is needed.
5. The reward function appears to be dependent on the policy parameters, which is not explicitly addressed in the derivation of the optimization objective. The gradient calculation in line 977 needs further clarification, considering the policy-dependent reward. A detailed derivation of the optimization problem is still missing.
6. The Taylor expansion around \rho_{\theta} = 0$ is not fully justified. While it's true that $\pi_{\theta}$ and $\pi_{\text{ref}}$ are initialized close, the expansion point is also dependent on the difference between $\pi_{\theta}(y_w|x)$ and $\pi_{\theta}(y_l|x)$. If these are far apart, the expansion may not hold, and this needs to be addressed.

### Questions
The Taylor expansion is shown around rho_theta = 0, whats the point of expanding around  rho_theta = 0? It occurs when y_w = y_l or the preferred and chosen responses are very similar? Whats the intution behind expanding at that point is not clear.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed to use adaptive importance sampling during offline post-training alignment of LLMs as a way to reduce over-optimization. They use a smoothed exponential IS estimator (where the exponent is the reciprocal of the length of the generation) in order to reduce the variance of the IS in exchange for some bias. Their experiments show that with this smoothed IS correction, they are able to reduce over-optimization in DPO and IPO and reach better performance in a lower KL budget in the TL;DR summarization task. They also show that distribution shift is indeed problematic and makes over-optimization worse.

### Strengths
-  The idea is simple and easy to integrate into existing algorithms like DPO and IPO as done in the paper.
-  The paper shows clear gains in terms of less overfitting and better performance per KL budget.

### Weaknesses
Overall, some more ablations or more in-depth investigation is lacking. There isn’t a good understanding of how important picking alpha is for the experiments. There is also not an investigation into how distribution shift (section 4.3) interacts with IS. See questions for more details.

### Questions
- Figure 1 and section 3.2 could be improved a lot by using the smoothed IS estimate and ablating over alpha, showing how the tradeoff between bias and variance works in such a toy domain as well.
- Some ablation over alpha in TL;DR would also be very insightful. Right now it seems that alpha is set arbitrarily to 1/|y|, when other values like 1/sqrt(|y|) might also be under consideration. Even if they perform worse, it is valuable insight into how alpha affects the performance or over-optimization.
- The distribution shift experiments in section 4.3, while does show that distribution shift is directly harmful, seems to be missing the natural followup of applying IS or smoothed IS in order to improve. How much does adding IS help? Or would it actually hurt performance because the data is no longer form pi_ref, so importance sampling towards pi_ref is actually increasing the distribution shift? Knowing something about how IS interacts with distribution shift would be a very good contribution to the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the reward-optimization issue in aligning large language models. It focuses on direct alignment methods, such as Direct Preference Optimization (DPO) and Identity Preference Optimization (IPO). The paper argues that these issues arise from off-policy distribution shifts between the learning policy and the reference policy. Accordingly, an importance-sampling weighting term with adaptive schemes is proposed. Experiments with Pythia models on the TL;DR dataset are conducted.

### Strengths
- The idea of using importance sampling to address distribution shift is not new, but it sounds interesting in the context of direct alignment methods.
- This paper is well-written and easy to follow.
- Numerous empirical results are presented, along with their limitations (see below).

### Weaknesses
 - This paper lacks technical depth. It studies the distribution shift issue in DPO, which is a valuable perspective. Unfortunately, it fails to explicitly point out or mention that DPO's gradient estimator is not unbiased because the data distribution is defined by the data-collection distribution policy $\pi$ (see previous works [1, 2]). Furthermore, it fails to justify that the proposed gradient estimator is unbiased. The reviewer believes that it is not theoretically unbiased. In fact, the importance sampling weight requires the optimal policy $\pi^*$, which is not available a priori.

[1] Liu, Tianqi, et al. "Statistical rejection sampling improves preference optimization." *arXiv preprint arXiv:2309.06657* (2023).

[2] Xiong, Wei, et al. "Iterative preference learning from human feedback: Bridging theory and practice for RLHF under KL-constraint." *Forty-first International Conference on Machine Learning*. 2024.

From the reviewer's perspective, there are two factors in DPO's formulation that prevent it from finding the true optimal policy:

First, DPO uses a fixed and offline dataset, where the data distribution does not originate from the optimal policy. 

Second, DPO employs KL regularization with a fixed policy. To address these issues, two simple strategies can be applied: periodically updating the reference policy [3] or using entropy regularization [4].

[3] Guo, Shangmin, et al. "Direct language model alignment from online AI feedback." *arXiv preprint arXiv:2402.04792* (2024).

[4] Xiao, Jiancong, et al. "On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization." *arXiv preprint arXiv:2405.16455* (2024).

- The superiority over other simple baselines is unclear. A straightforward way to address the distribution shift issue is to use a moving average of the reference policy that can ensure the policy moving beyond the KL contraint. 

- Experimental results are weak. The experiments are conducted on the TL;DR dataset, which unfortunately has very short response lengths, and the Pythia model used as a base is quite weak. Consequently, empirical conclusions and insights may have limited value for modern language models. Moreover, some experiment details are missing, which hinders reproducibility and understanding of key results.

### Questions
1. Can the authors theoretically justify that the estimator is unbiased?

2. Can the authors discuss the issue of length bias in the importance sampling weight? The length bias affects reward estimation [5], so the reviewer wonders about its effect on the importance sampling estimator used in this paper.

[5] Park, Ryan, et al. "Disentangling length from quality in direct preference optimization." arXiv preprint arXiv:2403.19159 (2024).

3. Can this paper provide comparisons with online algorithms such as PPO, REINFORCE, and online DPO? Except for PPO, which requires extensive computational resources, other methods require nearly the same resources as DPO.

4. Can the authors clarify the methods used for KL calculation and "gold win-rate" calculation in the experiments?

### Soundness
1

### Presentation
2

### Contribution
2
