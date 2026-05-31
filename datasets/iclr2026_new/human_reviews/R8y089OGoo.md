## Human Reviewer 1

### Summary
This paper proposes DIPOLE (Dichotomous diffusion Policy improvement), a novel reinforcement learning algorithm for training diffusion-based policies. The authors identify a key challenge in prior work: directly optimizing the standard KL-regularized RL objective,
$$\max_{\pi} \mathbb{E}[G(s,a)] - \frac{1}{\beta} D_{KL}(\pi||\mu)$$
is difficult because its closed-form solution, $\pi^*(a|s) \propto \mu(a|s) \cdot \exp(\beta G(s,a))$, leads to an unstable weighted regression loss where the $\exp(\cdot)$ term can explode.
To overcome this, DIPOLE proposes a new "greedified" KL-regularized objective (Eq. 5). The key insight is that the optimal solution to this new objective can be decomposed into a ratio of two "dichotomous" policies:
1. A "positive" policy $\pi^+ \propto \mu(a|s) \cdot \sigma(\beta G(s,a))$
2. A "negative" policy $\pi^- \propto \mu(a|s) \cdot (1 - \sigma(\beta G(s,a)))$

Critically, the authors claim these policies can be trained stably using diffusion models with bounded sigmoid weights ($\sigma$ and $1-\sigma$), solving the stability-optimality trade-off.
Furthermore, the paper shows that sampling from the optimal policy $\pi^*$ can be achieved by linearly combining the scores of the two dichotomous policies, resulting in an inference rule analogous to Classifier-Free Guidance (CFG):
$$\tilde{\epsilon}(a_t, s, t) = (1 + \omega) \epsilon_{\theta_1}^{+}(a_t, s, t) - \omega \epsilon_{\theta_2}^{-}(a_t, s, t)$$
The authors demonstrate DIPOLE's effectiveness on ExORL and OGBench benchmarks and scale it successfully to a 1-billion parameter vision-language-action (VLA) model for autonomous driving.

### Strengths
1. **Originality**: The primary strength is the novel formulation. The idea of decomposing the optimization into a reward-maximizing ($\pi^+$) and a reward-minimizing ($\pi^-$) policy is creative and provides a new lens for policy optimization.
2. **Strong Empirical Results & Scalability**: The method clearly works well in practice. The successful application of DIPOLE (using LoRA) to a 1-billion parameter VLA model is a significant achievement and demonstrates the method's practical utility for fine-tuning large models with RL.

### Weaknesses
1. **Questionable Necessity (Unsound Premise)**: The paper's motivation is that the standard KL-regularized objective (Eq. 2) is unusable because its solution (Eq. 3) implies an unstable weighted regression (Eq. 4). This implicitly assumes that weighted regression is the only way to optimize this objective. This premise is challenged by recent work like BDPO (Gao et al., 2025, ICML), which tackles the exact same standard objective. BDPO shows that by decomposing the $D_{KL}$ term along the diffusion path ($D_{KL}[p_{0:N}^\pi || p_{0:N}^\nu]$), the objective becomes a sum of per-step, analytic KL divergences $\sum_n D_{KL}[p_{n-1|n}^\pi || p_{n-1|n}^\nu]$. Since these per-step transitions are Gaussian, this penalty becomes a simple, stable, analytic MSE between the predicted noise vectors (Eq. 17 in BDPO). This suggests that DIPOLE's "greedified" objective (Eq. 5) is an overly complex solution to a problem that has a simpler, more direct solution within the original, standard RL framework.
2. **Flawed Training Mechanism (Sigmoid Saturation)**: The core of DIPOLE's solution is the replacement of $\exp(\beta G)$ with the bounded $\sigma(\beta G)$ (Eq. 9). This introduces a new, critical problem: signal saturation. The sigmoid function saturates, meaning its output approaches 1 for all values above a certain threshold (e.g., $\sigma(10) \approx \sigma(20) \approx 1.0$). This means the training loss for the positive policy $\epsilon^+$ loses all gradient information that distinguishes "good" actions from "excellent" actions. The network is not learning a fine-grained reward landscape, but rather a near-binary classification of "good" (weight $\approx 1$) vs. "bad" (weight $\approx 0$).
This saturation flaw directly contradicts the goal of the inference step (Eq. 10). The inference mechanism $\tilde{\epsilon} = (1+\omega)\epsilon^+ - \omega\epsilon^-$ relies on the "greediness factor" $\omega$ to amplify the difference between the two policies. However, if $\epsilon^+$ has already lost the high-reward gradient information due to saturation, $\omega$ is merely amplifying a "blurry" or "clipped" signal. It's unclear how this can steer the policy towards truly optimal actions if the network was never trained to distinguish them in the first place.
3. **Gap Between Theory and Practice (The $k$ parameter)**: This saturation flaw is strongly corroborated by the implementation details. The paper's theoretical derivation (Eq. 9) relies purely on $\sigma(\beta G)$. However, Appendix D.2 reveals the practical use of a modified weight, $\sigma(\beta G + k)$. This 'shift factor' $k$, which is absent from the main theory, serves as strong evidence that the sigmoid-based weighting is not robust. It implicitly confirms the saturation problem, as the model's performance is highly sensitive to the distribution of $G(s,a)$. The mechanism is therefore not as 'principled' as claimed, requiring an ad-hoc hyperparameter to manually shift the sigmoid's non-saturating region to align with the data.

**References**

Chen-Xiao Gao, Chenyang Wu, Mingjun Cao, Chenjun Xiao, Yang Yu, Zongzhang Zhang Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:18630-18657, 2025.

### Questions
1. On the Premise (re: BDPO): The paper's motivation rests on the instability of the $\exp(\beta G)$ weight (Eq. 4). However, recent work (e.g., BDPO) shows that the standard KL-reg objective (Eq. 2) can be optimized stably via a pathwise KL decomposition, resulting in an analytic MSE penalty. Given this, what is the theoretical advantage of proposing a new "greedified" objective (Eq. 5)?
2. On the Training Mechanism (re: Saturation): The core training relies on $\sigma(\beta G)$ (Eq. 9). This weight saturates for high $G(s,a)$ values. How can the network $\epsilon^+$ learn to distinguish between a "good" action ($G=10$) and an "excellent" action ($G=20$) if the training signal (the weight) is nearly identical for both?
3. On the Inference Mechanism (re: $\omega$): Following Q2, if $\epsilon^+$ has lost the high-reward gradient information due to saturation, how can the inference factor $\omega$ (Eq. 10) recover this information? Is it not simply amplifying a "clipped" or "binary" signal, rather than steering the policy towards the truly optimal (e.g., highest $G(s,a)$) actions? Could the authors comment on what $\epsilon^+$ is actually learning?
4. On the shift factor $k$: Regarding the 'shift factor' $k$ introduced in Appendix D.2 (using $\sigma(\beta G + k)$): This parameter is absent from the theoretical derivation. Could the authors confirm that this is necessary to counteract the sigmoid saturation and center the function's active region over the data's value distribution? How sensitive is the algorithm's performance to the choice of $k$, and doesn't its necessity undermine the robustness and principled nature of the proposed theoretical framework?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces DIPOLE (Dichotomous Diffusion Policy Improvement), a stable, scalable, and controllable reinforcement learning framework for training large diffusion policies. Existing RL approaches for diffusion policies either (i) directly optimize value or reward objectives, leading to high gradient variance and training instability, or (ii) approximate Gaussian likelihoods across multiple denoising steps, which are computationally expensive and often inaccurate. By revisiting the KL-regularized RL formulation, DIPOLE proposes a greedified KL-regularized objective that naturally decomposes into two dichotomous sub-policies: the positive policy that favors high-reward actions and the negative policy that models low-reward actions.

### Strengths
This work derives a new closed-form optimal policy under a modified KL objective with a bounded sigmoid weighting, effectively avoiding unstable exponential terms and preventing gradient explosions. The dual-policy decomposition enables learning from both high- and low-reward samples, mitigating data imbalance and overfitting to rare high-reward trajectories. Empirical results demonstrate that DIPOLE consistently outperforms strong baselines across offline, offline-to-online, and large-scale VLA tasks. Moreover, the training procedure remains simple and modular, as it only modifies the loss weights of standard diffusion objectives, maintaining full compatibility with existing architectures.

### Weaknesses
1.	In DIPOLE, the weight term $\sigma(\beta G(s,a))$ (or $1 - \sigma(\beta G(s,a))$) is treated as constant with respect to the diffusion model parameters. This means that the diffusion model learns to denoise under static weighting but does not explicitly learn how to adjust the action distribution to improve $G(s,a)$ directly. Consequently, there is no gradient signal guiding the modification of intermediate noisy actions to increase the expected reward, which may lead to slower convergence or plateaued performance when the current policy’s support does not already include near-optimal actions. As a result, the performance of DIPOLE heavily depends on the quality of the value estimator. If $G(s,a)$ overestimates certain actions, the weighting will amplify these errors, making policy improvement rely entirely on value accuracy rather than direct reward gradients. This issue is particularly pronounced in offline RL, where value estimates can be severely biased in out-of-distribution (OOD) regions. Thus, the diffusion process learns primarily through denoising consistency instead of reward shaping across time. Furthermore, since updates are based on weighted regression rather than policy gradient optimization, there is no stochastic gradient noise or entropy regularization to encourage exploration. In online fine-tuning scenarios (e.g., DIPOLE’s autonomous driving setup), this lack of exploratory signal could slow adaptation to unseen environments.
2.	The paper derives the optimal policy formulation but does not provide rigorous convergence guarantees or theoretical error bounds for the dichotomous approximation.

3.	Although the parameter $\omega$ controls the degree of greediness, the paper lacks quantitative analysis on how $\omega$ and $\beta$ jointly influence training stability and performance.

4.	Training two separate diffusion models likely doubles computational and memory costs, yet the paper does not report comparisons on training time or efficiency.

5.	The method assumes a reliable reward function or Q-estimator $G(s,a)$, but it remains unclear how performance degrades when the value estimates are noisy or biased.

### Questions
1.	For DP-VLA, the reward shaping, return computation, and LoRA-based adaptation are briefly described but not rigorously analyzed.
2.	The paper uses both temperature $\beta$ and greediness $\omega$, how do they jointly affect stability and optimality?
3.	The linear combination resembles CFG, but is $\omega$ chosen adaptively per state or fixed globally? How does this choice affect exploration–exploitation balance?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces DIPOLE, a new framework for training diffusion-based policies in goal-conditioned offline reinforcement learning. Instead of using a single diffusion policy with unstable exponential advantage weighting, the authors propose a dichotomous formulation: two separate diffusion policies are trained — one favoring high-return behaviors ($\pi^+$) and one suppressing low-return behaviors ($\pi^-$). The final policy is synthesized at inference by combining their score functions. This approach avoids instability caused by unbounded weighting and enables a controllable trade-off between greediness and safety. Empirically, DIPOLE achieves strong performance across several offline RL tasks (ExORL, OGBench), improves stability in training, and scales to large vision-language-action models in autonomous driving (NAVSIM benchmark), outperforming prior imitation-based diffusion policies.

### Strengths
* The paper proposes a simple but effective method (DIPOLE) that trains two diffusion policies instead of one, helping stabilize learning in offline RL.
* The method is well-motivated and theoretically justified, avoiding unstable exponential weighting by using bounded scores.
* Strong experimental results across many tasks, including large-scale vision-language-action models for autonomous driving.
* The paper is clearly written, well-organized, and easy to follow.

### Weaknesses
* The method is only evaluated in offline or offline-to-online settings. I am not sure why the same idea can't be applied to online RL?
* The baselines for comparison seem random to me. Not sure what are the reasons to choose those baselines as opposed to some other diffusion-based / non-diffusion-based offline RL baselines. For example, there are plenty of model-based offline RL baselines and I think the authors primarily only choose model-free baselines. Is this intentional? What are the rationals behind choosing these baselines? I have read Sec 4.1 but I am not fully convinced by the explanation.

### Questions
Can this algorithm generalize to the online setting? There is some recent work on using KL-regularized RL and mirror descent to define the diffusion policy loss function in the online setting (see below reference), which has the same form as Equation 4. I think the same dichotomous idea may also work there. Could you please explain if this will work or not?

"Efficient Online Reinforcement Learning for Diffusion Policy", Haitong Ma, Tianyi Chen, Kai Wang, Na Li, Bo Dai, ICML 2025

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes DIPOLE, a novel reinforcement learning (RL) framework for optimizing diffusion-based policies. The key idea is to reformulate the KL-regularized RL objective into a “greedified” version that can be decomposed into two dichotomous diffusion policies — one maximizing reward (positive policy) and one minimizing reward (negative policy). During inference, their score functions are linearly combined, enabling controllable trade-offs between greediness and stability.
Extensive experiments on ExORL, OGBench, and a large-scale autonomous driving benchmark (NAVSIM) demonstrate performance gains over prior RL and diffusion-based baselines.

### Strengths
1. The proposed dichotomous decomposition of the KL-regularized objective is both elegant and conceptually novel. The analogy to classifier-free guidance (CFG) provides a strong intuitive and theoretical bridge between diffusion modeling and RL optimization.

2. The paper presents comprehensive experiments across multiple RL benchmarks and an ambitious large-scale 1B-parameter VLA model for end-to-end driving, showing clear improvements over strong baselines (IQL, FQL, CFGRL, etc.).

3. The paper presents comprehensive experiments across multiple RL benchmarks and an ambitious large-scale 1B-parameter VLA model for end-to-end driving, showing clear improvements over strong baselines (IQL, FQL, CFGRL, etc.).

### Weaknesses
1. The reviewer is a little bit confused about why we need to train a policy that minimizes the rewards. In my opinion, to avoid the large difference between the optimized policy and the behavior policy of offline data, we can directly perform imitation learning on the second diffusion policy rather than minimizing the reward. 
2. How can we get $G(s, a)$ in the proposed method? Should we apply some special technique to learn it, such as CQL [R2]?
3. The method can be classified as a weighted-based diffusion RL method and lacks the citation of the recent weighted-based diffusion RL method [R1].

[R1] Ding S, Hu K, Zhang Z, et al. Diffusion-based reinforcement learning via q-weighted variational policy optimization[J]. Advances in Neural Information Processing Systems, 2024, 37: 53945-53968.

[R2] Kumar A, Zhou A, Tucker G, et al. Conservative q-learning for offline reinforcement learning[J]. Advances in neural information processing systems, 2020, 33: 1179-1191.

### Questions
The proposed method requires training two separate policy networks $\epsilon^+, \epsilon^-$, which effectively doubles the computational and storage costs. However, the paper does not discuss or evaluate this overhead: How long is the training time compared to single-policy baselines? During inference, although the final score is obtained by a linear combination, two models must be executed—what is the resulting latency? In the autonomous driving experiments, the authors mention using LoRA to mitigate this issue, but they do not quantify the number of additional parameters introduced by LoRA or its impact on training efficiency

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4