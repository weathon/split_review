# Distribution Corrected Estimation via Adversarial Density Weighted Regression

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
We propose a novel one-step supervised imitation learning (IL) framework called Adversarial Density Regression (ADR). This IL framework aims to correct the policy learned on unknown-quality to match the expert distribution by utilizing demonstrations, without relying on the Bellman operator. Specifically, ADR addresses several limitations in previous IL algorithms: First, most IL algorithms are based on the Bellman operator, which inevitably suffer from cumulative offsets from sub-optimal rewards during multi-step update processes. Additionally, off-policy training frameworks suffer from Out-of-Distribution (OOD) state-actions. Second, while conservative terms help solve the OOD issue, balancing the conservative term is difficult. To address these limitations, we fully integrate a one-step density-weighted Behavioral Cloning (BC) objective for IL with auxiliary imperfect demonstration. Theoretically, we demonstrate that this adaptation can effectively correct the distribution of policies trained on unknown-quality datasets to align with the expert policy's distribution. Moreover, the difference between the empirical and the optimal value function is proportional to the upper bound of ADR's objective, indicating that minimizing ADR's objective is akin to approaching the optimal value. Experimentally, we validated the performance of ADR by conducting extensive evaluations. Specifically, ADR outperforms all of the selected IL algorithms on tasks from the Gym-Mujoco domain. Meanwhile, it achieves an \textbf{89.5\%} improvement over IQL when utilizing ground truth rewards on tasks from the Adroit and Kitchen domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a one-step supervised imitation learning (IL) framework that addresses the challenge of training policies on suboptimal datasets while aligning them with expert demonstrations. The proposed method leverages two variational auto-encoders (VAEs), trained separately on the suboptimal data and expert demonstrations, to estimate the respective behavior distributions. These VAEs are then employed to calculate density weights for offline policy training. This training is performed using an adversarial density regression (ADR) approach. ADR minimizes the Kullback-Leibler (KL) divergence between the policy’s behavior distribution and the expert demonstration distribution while simultaneously maximizing the KL divergence between the policy and the suboptimal dataset distribution. This formulation translates into a density-weighted regression between the policy’s output and the actions observed in the suboptimal dataset. Notably, this approach circumvents the reliance on the Bellman operator and demonstrates competitive performance compared to other offline reinforcement learning (RL) methods. The proposed framework exhibits robustness to noisy demonstrations and mitigates the risk of out-of-distribution (OOD) generalization issues.

### Strengths
1. **Empirical Validation**: The paper demonstrates the efficacy of the proposed Adversarial Density Regression (ADR) method through comprehensive experimental results. ADR consistently outperforms baseline algorithms across diverse task domains, achieving higher accuracy while exhibiting robustness to noisy demonstrations and a reduced risk of out-of-distribution generalization.
2. **Training Efficiency**: The one-step supervised learning paradigm employed by ADR effectively minimizes cumulative errors, resulting in stable training without tuning conservative terms. This streamlined approach contributes to the method’s practical appeal.
3. **Theoretical Analysis**: The authors provide theoretical for ADR’s effectiveness. They prove that minimizing the ADR objective function is aligned with attaining an optimal policy, which forms a valid theoretical justification for the proposed method.

### Weaknesses
1. **Novelty**: The main innovation in Density Weighted Regression (DWR) is the importance sampling term combined with a behavior cloning objective. However, the novelty is unclear. The justification relies on comparisons to traditional Behavior Cloning (BC) and DICE, but the connection to DICE seems weak. DICE addresses a reinforcement learning problem using its dual form, involving a Bellman flow constraint, while ADR focuses on an imitation learning problem. These approaches are based on different formulations. The core idea of re-weighting samples based on density ratios is not novel, and the paper does not sufficiently articulate how the specific combination of VAE-estimated densities and adversarial training leads to a significant advancement over existing methods.
2.  **Computational Overhead**: The reliance on auxiliary Variational Autoencoder (VAE) training for each task raises concerns regarding computational efficiency. Although the paper does not explicitly address the associated computational cost, this aspect warrants further investigation. The paper should include a detailed analysis of the computational resources required, including training time and memory usage, particularly when scaling to more complex tasks and datasets. The overhead of training two VAEs, one for expert data and one for suboptimal data, needs to be quantified and compared to the computational cost of other offline RL methods.
3. **Technical Significance and Soundness.**
- Theorem 4.2 seems to be an obvious reformulation of equation (8). The necessity of naming it as a theorem is unclear. For example, what's the main observation and conclusion from this theorem is unknown. The paper should clarify the specific contribution of Theorem 4.2 beyond a simple algebraic manipulation. The theorem should highlight a non-trivial insight or provide a formal justification for a key step in the algorithm.
- The application of KL-divergence has several limitations. For instance, it requires that the compared distributions have exactly the same support, and it isn't a true distance metric because it's not symmetric. Nowadays, more promising alternatives like Wasserstein distances are gaining attention, with wide exploration in reinforcement learning applications. The paper should discuss the limitations of using KL divergence and justify its choice over other distance metrics, especially considering the potential for distributions with non-overlapping support in the context of imitation learning.

### Questions
1. Dataset Size: The paper could benefit from an analysis of the impact of the demonstration dataset size on ADR’s performance. Could you please demonstrate the relationship between dataset size and model accuracy?
2. Noisy Data Handling: It would be beneficial to investigate the robustness of ADR in the presence of noisy or low-quality suboptimal datasets. Could you please demonstrate the capability of your method to address noisy or low-quality suboptimal data issue?
3. VAE Choice: A clear justification for selecting VAEs as the behavior distribution estimator would enhance the paper’s clarity. Could you please discuss the advantages of VAEs compared to other potential estimators?

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
The author propose a simple yet effective one-step supervised IL framework termed Adversarial Density Regression (ADR), which leverages demonstrations to correct the policy distribution learned from datasets of unknown-quality toward expert distribution without relying on the Bellman operator.

### Strengths
The author introduces a substantial and well-validated advancement in IL with Adversarial Density Regression (ADR). ADR addresses key limitations in current IL methodologies by diverging from the typical reliance on multi-step Bellman updates and conservative RL policies, which can introduce cumulative errors and struggle with out-of-distribution (OOD) data. Experimentally, ADR surpass selected IL algorithms and achieves better performance than the offline RL algorithm IQL in the Android domain.

### Weaknesses
This paper introduces ADR and demonstrates strong results in the Gym-Mujoco, Kitchen, and Adroit domains. However, these environments primarily focus on continuous control tasks with static distributions. This choice does not fully capture the complexity of real-world applications, which often involve changing dynamics or high-dimensional, sparse observation spaces (e.g., partially observable or dynamic obstacle environments). Testing ADR on environments with dynamically shifting conditions, like robotic control with dynamic obstacles or changing goals, could provide more insights into its robustness and generalizability. ADR's density-weighted objective, VAE-based density estimation, and adversarial learning framework are likely to introduce significant computational overhead, this paper limited analysis of computational efficiency.

### Questions
Could the authors comment on how ADR would handle more substantial or structured noise?
Could the authors provide insights into ADR’s computational demands and compare them to other IL methods?
Could the authors clarify the benefits of using adversarial learning here? For instance, how much does Adversarial Density
Estimation (ADE) contribute to ADR’s overall performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an offline imitation learning (IL) algorithm, where the agent lacks access to environment rewards and cannot collect new samples. Instead, it relies on two datasets: (1) expert demonstrations and (2) sub-optimal demonstrations. The scarcity of expert data, a realistic scenario in IL, makes learning expert-level policies particularly challenging in this offline setting.

The authors design their approach with two objectives in mind:
 It avoids the caveats of offline learning with the Bellman operator like TD learning or Value Distribution Corrected Estimation (ValueDICE) learning which are known to suffer from bootstrapping errors, especially in the offline case and with small datasets where OOD evaluations are inevitable.
It utilizes both the expert and the sub-optimal demonstrations with the goal of learning a policy that is as close as possible to the expert policy.

To achieve these goals, they design a policy loss function (termed ADR) that starts with expert behavioral cloning KL-div loss but adds negative KL-div loss (maximizing the KL-div) against the sub-optimal policies.

In order to learn this objective the authors suggest to learn an intermediate model of the expert policy P* and the sub-optimal empirical policy P^ with Variational Autoencoders (VAE) and use the log-ratio P*/P^ as a (log) Importance sampling weight for the policy loss. This results in a simple two-steps optimization problem (1) learn VAEs, (2) learn policy and avoids the Bellman operator.

In order to compensate for the scarcity of expert demonstrations, they add to the VAE loss a discriminator loss (GAIL [1] like, termed ADE) that lets adding samples from the sub-optimal dataset at the expense of altering the expert policy estimation.

The paper then analyses some theoretical bounds on the expected learned policy and its overall performance (i.e. value function). 

In terms of experiments, first, the authors demonstrate some similarity of the frequency of states in the learned policy with respect to the expert policy. Then they conduct experiments in 3 test benches (Mujoco, Androit, Kitchen) and show superiority of their method over algorithms like Behavioral Cloning (BC), CQL, IQL+Oracle, IQL+OTR, IQL+CLUE which are designed for similar (yet not always identical) settings (offline RL, potentially with reward and without sub-optimal datasets) .

References:
1. Ho, Jonathan, and Stefano Ermon. "Generative adversarial imitation learning." Advances in neural information processing systems 29 (2016).

### Strengths
The paper clearly motivates the problem, reviews relevant methods, and identifies their limitations.

The proposed approach is straightforward and avoids the complexities of Bellman-based TD learning.

### Weaknesses
1. Is ADR an appropriate optimization objective?

It is questionable whether the ADR loss is an adequate objective function for this RL setting. First, intuitively when the sub-optimal policy gets closer (or converges) to the expert policy, ADR converges to a degenerated objective function. Next, even if the sub-optimal policies are sufficiently different from the expert policy, the ADR policy does not converge to the P* solution or even sufficiently close to the P* solution. For example in the discrete case, the ADR objective is:

pi = argmin sum_i pi_i \log(\frac{P^_i}{P*_i})

Lets take for example the case where P* = (0.6, 0.2, 0.2) and P^=(0.2, 0.2, 0.6) (no states in this case, only 3 actions). The ADR policy converges to pi = (1, 0, 0), since actions with similar probability  between P* and P^ do not add weight to the policy. This means that ADR tends to increase the actions with positive ratio (where P*>P^), reduce (up to zero) the actions with negative ratio (P^ > P*) and ignore the actions where P*~=P^ which fails to capture the expert policy.

Moreover, ADR tends to yield policies with smaller action-support than the expert policy (more deterministic, where some expert actions are never taken) this can lead to potentially sub-optimal results as some actions may be crucial for functional policy. This trend of smaller support of ADR can be both observed in my toy example and in Fig 2 where we find that in both ANT and HALFCHEETAH ADR has smaller state support than the expert policy.

Proposition 5.2 tries to upper-bound the KL distance between the learned policy and the expert policy. As indicated in this analysis, when the distance between P* and P^ is small (delta) then the bound gets looser.

2. Are P* and P^ really needed and does ADR really avoid bootstrapping and OOD errors?

Given that one wish to design the ADR policy, it is not clear why the learned P* and P^ models are required. In a sense, if data is sufficient we can sample the backward KL-div D-KL(P*,pi) and D-KL(P^,pi) from the data. Therefore, assuming that the reason for incorporating P* and P^ models is to compensate the data scarcity (i.e. using both the sub-optimal and the expert dataset to regress for the ADR policy), one must ask himself whether ADR really avoids the caveats of bootstrapping (in the sense of using an estimated quantity as part of the ground truth for another model) as the ground truth for ADR includes the estimated log-ratio log(P^/P*) which also means that we evaluate P* out-of-distribution over the sub-optimal dataset, which essentially requires another bandage (the ADE auxiliary loss).

3. Value bounds: Do they provide insight?

Proposition 5.3 tries to lower-bound the value differences between the ADR policy and the expert policy. In general for any two policies p and q we have |V_p(s0) - V_q(s0)| <= 2R_max / (1 - \gamma). For ADR, the upper bound contains several more multiplicative factors, however, since elements like \Delata C and D_TV(d*|d^D) are constant terms (i.e. not diminishing to zero) at any case, this bound is too loose to provide concrete reasoning about the similarity between pi and P*.

4. Is ADE a proper way to handle the demonstrations scarcity?

ADE is presented as a practical auxiliary loss to ADR that should mitigate the problem of small expert dataset at the expense of altering the P* network which does not represent anymore the estimation of the expert policy. I’m not sure this is a sound solution for the need to compensate for small dataset as it basically lead to a deadly tradeoff where as we increase the weight of the auxiliary loss we better avoid OOD samples but on the same time we move away from our desired function (i.e. the expert policy). There are other alternatives that should be considered here, for example to estimate the KL-div between the expert and the sub-optimal empirical policy (as it is done in [1]), this lets you train both networks from samples from both D* and D^ without altering the structure/behavior of both networks.

### Questions
1. Regarding VAE for density estimation: 
There appear to be issues in the formulation of the ELBO loss (Eq. 5), which should align with Eq. 4 in [1] (CLUE). Additionally, what motivates the choice of this conditional VAE structure (with actions as input/output and state as context) over simpler density estimators like normalizing flows? You do not leverage latent space information in the algorithm (as CLUE does), and evaluating \log⁡ P∗(a∣s) and \log P^*(a|s) requires Monte Carlo sampling. 
Could you clarify this choice and how you approximate \log ⁡P∗(a∣s) and \log P^*(a|s)?

2. Regarding theorem 4.2 (theorem D.1 in the appendix). Can you clarify the last move in Eq 18 in the appendix, which probabilistic model do you assume the policy follows?

references:
1. Liu, Jinxin, et al. "Clue: Calibrated latent guidance for offline reinforcement learning." Conference on Robot Learning. PMLR, 2023.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Adversarial Density Regression (ADR), a novel supervised Imitation Learning (IL) framework learning from expert and suboptimal data. Different from prior works, it minimizes the KL divergence between the learner and the expert behavior while diverging from the sub-optimal behavior. The paper proves that such objective is equivalent to weighted behavior cloning with weights being the log probability ratio on the given state-action pairs of expert and sub-optimal policy's behavior density, and estimates the weight with a VAE density estimator. The author proves the convergence of ADR theoretically and demonstrate its effectiveness on several testbeds.

### Strengths
1. The work is well-written and easy to follow. Though there are many mathematical notations and derivations in this paper, they are clearly introduced in a proper order. In particular, every formula in Sec. 3 and 4 is properly and briefly explained (without too much text between each formula) and highlighted with bold fonts.

2. The idea of this work is simple, intuitive but effective: it proposes a weighted behavior cloning method where the weights are probability ratio learned by VAE. The final formula of weights is straightforward, and using VAE to model distribution is a natural approach.

3. The results are not only tested on many environments (including mujoco, kitchen and adroit) with proper ablations (including loss components, upper bound of ADR, training stability and OOD risky analysis), but also guaranteed by theoretical derivations.

### Weaknesses
1. The literature investigation could be improved.

a) While imitation learning can indeed be categorized as mentioned in the "imitation learning" part of the related work, the paragraph did not show sufficient connection between related work and this work. It would be beneficial to explicitly state how this work fits into the broader context of offline Learning from Demonstration (LfD).

b) The work claims that it is a DICE-type framework in its abstract, but there is no literature investigation for DICE at all. The summary for DICE is inaccurate. This work is very different from DICE because the fundamental idea of DICE is to match occupancies, while in this work "occupancy" is not involved; the VAE is essentially learning *policies*, not *occupancies*. They are each other's Lagrange dual variables. TAILO [5] introduces a much simpler way (originated from DICE works such as SMODICE [1]) for estimating *occupancy* ratio, and is also a streamlined one-step supervised framework with log probability ratio for weighted Behavior Cloning (BC) without any RL. I suggest the authors revise the categorization and thoroughly discuss the relationship to DICE methods.

c) The introduction for DICE is inaccurate. Not all DICE works consider KL-divergence - SMODICE [1] uses $\chi^2$-divergence for many of its tested environments. There are also many DICE works that rely on Wasserstein distance, such as PW-DICE [2] and SoftDICE [3]. Also, the objective (Eq. 5 of their paper) of DemoDICE [4], which is one of your baseline, does not seem to fit in your Eq. 4; they have two KL terms instead of one with a linear reward term in the objective.

2. The last step of Eq. 18, which turns $\pi_\theta(a|s)$ into $\|\|\pi_\theta(\cdot|s)-a\|\|^2$, is based on the assumption of Gaussian policy which is not mentioned. This constraint of the policy being Gaussian could be a potential limitation for the proposed method, especially when considering discrete action spaces where actions cannot be directly subtracted.

**Minor Issues**

1. There is no y-axis in Fig. 7 and Fig. 8, which makes the message from this figure unclear.

2. line 98, "Latent" in ".../Latent representations" should be lower case.

3. It would be better to add "λ=0" on "ablation of ADE and DWR" part to help the readers understanding the ablation.

### Questions
I have several questions:

1. Why does this work choose VAE instead of normalizing flow or diffusion model for estimation of density weight? One does not need approximation in Eq. 17 for normalizing flow, and diffusion models are stronger generative models than VAE (for ratio estimation, see diffusion DPO [1, 2]). An ablation on this would be great.

2. How does the ablation "ADR without DWR" work? From my understanding, DWR is the crucial step that retrieves the policy to learn.

3. Around line 187, the authors claim "Some off-policy offline frameworks... overly conservatism constrains the exploratory capacity of policies, limiting their ability to adapt and improve beyond the demonstrations provided." This is true. But the problem is, since your algorithm is an offline, it is necessary to overcome such issue since you will not explore beyond your dataset at all? Or are the authors arguing that they have a better inductive bias for OOD area than the common pessimisitic principle (in this case there are some more recent improvements such as MCQ [3])?

**References**

[1] B. Wallace et al. Diffusion Model Alignment Using Direct Preference Optimization. In CVPR, 2024.

[2] K. Black et al. Training Diffusion Models with Reinforcement Learning. ArXiv, 2023. 

[3] J. Lyu et al. Mildly Conservative Q-Learning for Offline Reinforcement Learning. In NeurIPS, 2022.

### Soundness
2

### Presentation
3

### Contribution
3
