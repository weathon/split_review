# Diffusion Models Meet Contextual Bandits

- Decision: Reject
- Scores: 6, 6, 6, 5, 5

## Abstract
Efficient exploration in contextual bandits is crucial due to their large action space, where uninformed exploration can lead to computational and statistical inefficiencies. However, the rewards of actions are often correlated, which can be leveraged for more efficient exploration. In this work, we use pre-trained diffusion model priors to capture these correlations and develop diffusion Thompson sampling (dTS). We establish both theoretical and algorithmic foundations for dTS. Specifically, we derive efficient posterior approximations (required by dTS) under a diffusion model prior, which are of independent interest beyond bandits and reinforcement learning. We analyze dTS in linear instances and provide a Bayes regret bound. Our experiments validate our theory and demonstrate dTS's favorable performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Diffusion Thompson Sampling (dTS), a novel algorithm leveraging pre-trained diffusion model priors to optimize exploration in contextual bandits. By capturing correlations among actions, dTS enhances both computational and statistical efficiency. It offers theoretical insights into posterior approximations and Bayes regret bounds, providing a structured and computationally manageable solution for large action spaces in contextual bandit problems.

### Strengths
1. The paper thoroughly explains the posterior approximation process for both linear and non-linear diffusion models.

2. The recursive hierarchical sampling in dTS is well-defined, which simplifies the complex diffusion model and supports efficient computational sampling.

### Weaknesses
1. The method’s performance is heavily reliant on the accuracy of the pre-trained diffusion model. If the model's prior assumptions are incorrect or misspecified, the effectiveness of the posterior approximations and subsequent regret bounds could be compromised. Specifically, the paper does not address the sensitivity of the algorithm to the choice of diffusion model architecture or training data. A poorly trained diffusion model could lead to a biased posterior and suboptimal exploration, particularly if the true action space distribution differs significantly from the diffusion model's training data distribution. This reliance on a potentially inaccurate prior is a significant concern.

2. There is limited discussion on alternative approximation techniques (e.g., variational inference or Monte Carlo methods) that could potentially offer more flexible or accurate approximations, especially for non-linear reward distributions. The paper does not delve into the trade-offs between the proposed method and other approximation techniques in terms of computational cost, approximation accuracy, and convergence properties. For example, while the proposed method offers computational efficiency, it may sacrifice accuracy compared to more computationally intensive methods like Markov Chain Monte Carlo (MCMC), particularly in complex, non-linear reward scenarios. The lack of discussion on these trade-offs limits the understanding of the method's applicability and limitations.

### Questions
1. How does the choice of the link function $ f_\ell$ impact the posterior approximation and computational efficiency in non-linear scenarios?

2. How would the regret bounds change if the action parameters $\theta^*$ were updated using a non-linear transformation?

3. How does the choice of the number of layers $L$ in the diffusion model affect the convergence rate of the posterior approximations, especially as the action space $K$ increases?

4. What impact does the sparsity assumption on the mixing matrices $W_\ell$ have on the model's computational efficiency and the quality of the posterior approximations?


5. As I have mentioned in (3) of Weaknesses, can you discuss alternative approximation techniques (e.g. Monte Carlo methods [1,2]) that could potentially offer more flexible or accurate approximations, especially for non-linear reward distributions?

References:

[1] Xu, Pan, et al. "Langevin monte carlo for contextual bandits." International Conference on Machine Learning. PMLR, 2022.

[2] Karbasi, Amin, et al. "Langevin thompson sampling with logarithmic communication: bandits and reinforcement learning." International Conference on Machine Learning. PMLR, 2023.

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
4

### Summary
This paper studies the performance of Thompson Sampling for contextual bandit problems with generalized linear model reward distribution. Starting from a prior distribution over the "action-parameter", Thompson Sampling algorithm works by randomly selecting actions according to their posterior probability of being optimal. More specifically, at each time step, it samples an "action-parameter" estimate from the posterior distribution conditioned on the history and selects the action that is optimal for the sampled parameter estimate given the context.

In this work, the authors study the case where the prior is (or can be approximated by) a diffusion model. This idea is inspired by the work of Hsieh et al. (2023), where they showed they could use diffusion model to model the prior together with Thompson Sampling algorithm to solve bandit problems. This paper builds on Hsieh results and extends their idea to contextual bandit problems. They also show how to efficiently compute an approximation of posterior and how to efficiently sample from this approximation, and call the resulting algorithm diffusion Thompson sampling. Under the assumption that the true prior can be written as a linear Gaussian system, their approximate posterior matches the exact posterior and the authors could derive Bayesian regret bounds in $\tilde{O}(\sqrt{n (d K \sigma_{1}^2 + \sum_{l=1}^L d \sigma_{l+1}^2 \sigma_{\text{MAX}}^{2l}})$ where $n$ is the number of time steps, $d$ is the dimension of the problem, $K$ is the number of possible actions, $\sigma$ is the variance of the rewards, $\sigma_1$ is the isotropic variance of the action parameter given the first latent variable, $L$ is the number of latent parameters and $\sigma_{l+1}$ is the isotropic variance of the latent parameter $l$ conditioned on the latent parameter $l+1$ (by construction the $L+1$ latent parameter is zero) and $\sigma^2_{\text{MAX}} = \max_{l\in[L+1]} 1+\frac{\sigma_l^2}{\sigma^2}$. 

The authors perform two experiments to demonstrate the performance of the proposed method. The first experiment is performed on synthetic problems where the true prior is a diffusion model. They compare their method with several baselines (LinTS, LinUCB, HierTS, GLM-TS, UCB-GLM) and show that the diffusion Thompson sampling performs better. The second experiment has a prior distribution that is not a diffusion model. In this case, the author first pre-train a diffusion model to approximate the prior distribution before running the algorithm. They show that their method performs better than LinTS.

### Strengths
The main strength of the paper is its overall clarity and coherence. The authors introduce the interesting idea of extending the work of Hsieh et al. (2023) to contextual bandit problems, show how to efficiently compute an approximation of the posterior to sample from, derive regret bounds under some specific assumptions, and perform experiments to demonstrate the performance of the proposed method. The different ideas are explained clearly, the code for the experiments is provided and user-friendly, the notations used are rigorous, and the proof techniques are thorough and explicit.

### Weaknesses
Although the paper's main ideas are interesting, the experiment section presents some weaknesses. The first experiment, Figure 2, compares the proposed algorithm dTS against several baselines HierTS, LinTS, GLM-TS, UCB-GLM for problems where the true prior is a diffusion model. Unsurprisingly, this setting perfectly fits the proposed algorithm, and it outperforms the baseline algorithms. This first experiments can be understood as a sanity check test that dTS passed. A more interesting experiment, Figure 4, tests the performance of dTS on problems where the true prior is not a diffusion model. However, the performance of dTS in this setting is only compared to LinTS, which is by design not suited to this contextual bandit problem as it cannot capture the correlations among actions. It is, therefore, not surprising that dTS improves the performance of LinTS for this problem, and it is difficult to appreciate its performance. A more fair comparison would have been against algorithms suited to the setting, such as "Vits: Variational Inference Thompson Sampling". Another interesting experiment would have been to compare the performance of dTS against the DiffTS proposed by Hsieh et al. (2023) on bandit problems and verify if dTS can recover the same performance while presenting computational advantages.

### Questions
Here is a list of suggestions for the authors. 
- In section 4.1, Statistical benefits, the authors mention "The only Bayesian lower bound that we know of is $\Omega(\log^2(n))$. The authors could have mentioned the minimax results from Dani et al. (2008) in $\Omega(d\sqrt{n})$ for the $d$-dimensional linear bandit setting.
- On line 354, the authors mention "we can show that dTS’s regret is independent of K in their setting, assuming the availability of $\phi$". It would be interesting to add this proof in the Appendix. 
- As mentioned before, it would be interesting to compare the performance of dTS against fairer baselines for the experiments on MovieLens problem such as the Vits: Variational Inference Thompson Sampling" from Clavier et al. (2023). 
- It would also be interesting to compare the performance of dTS against the DiffTS proposed by Hsieh et al. (2023) on bandit problems and verify if dTS can recover the same performance while presenting computational advantages.
- In the Appendix "Extended related work", the authors are pointed to two papers that studied the performance of TS for contextual bandits and derived Bayesian regret bounds: Neu et al. "Lifting the information ratio: An information-theoretic analysis of thompson sampling for contextual bandits" (2022) and Gouverneur et al. "Thompson sampling regret bounds for contextual bandits with sub-Gaussian rewards." (2023).
- For the sake of completeness, the authors are suggested to include in the Appendix the pseudocode of the LinTS algorithm used for the experiments.
- On line 239, the authors mention that their "bound is $\tilde{O}(\sqrt{n})$. A suggestion is to include the non-logarithmic dependencies on $d$ and $K$.
- On line 127, a suggestion to the authors to change "We design Thompson sampling that samples" to "We design a Thompson sampling algorithm that samples".
- On lines 122-123, the authors wrote "The Bayes regret is known to capture the benefits of using informative priors, and hence it is suitable for our problem". The authors are suggested to provide references to support their claim.

### Soundness
3

### Presentation
3

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
The paper introduces Diffusion Thompson Sampling (dTS), an algorithm designed to handle the exploration-exploitation trade-off in contextual bandits with large action spaces. The key idea is to leverage pre-trained diffusion models to capture correlations between actions, which can guide more efficient exploration.

The authors propose using diffusion models as priors in a Thompson sampling framework, allowing the algorithm to explore the action space more strategically by exploiting the underlying structure of the action set. The paper provides a theoretical analysis of the algorithm, including an upper bound on the Bayes regret for linear diffusion and reward structures.

In addition to the theoretical results, the paper presents empirical evaluations that demonstrate the performance of the proposed method across various settings, showing that it outperforms traditional approaches in contexts with both linear and non-linear reward and diffusion models.

### Strengths
- The paper leverages *pre-trained diffusion models* to capture correlations in large action spaces, which provides a more structured and efficient approach to exploration compared to traditional methods in contextual bandits.

- The paper provides a Bayes regret bound for diffusion Thompson sampling (dTS) in the linear case, offering some theoretical backing to the proposed algorithm, though the assumptions could be more thoroughly justified (see the Weakness section).

- Comprehensive Empirical Results: The paper presents empirical evaluations that show dTS outperforming standard methods in several settings, particularly in large-scale action spaces, which lends support to the algorithm’s practical effectiveness.

### Weaknesses
 - The unclear presentation of the assumptions, along with the lack of thorough discussion or justification, makes it difficult to fully evaluate the soundness of the work (see more details below).
- In terms of numbering, the assumptions should begin from **1** instead of 0. For example, (A0), (A1), (A2) should be renamed to (A1), (A2), (A3), etc., for consistency and clarity.
- Assumption (A0) should be separated into two distinct parts:  
  (i) The assumption that **$W_\ell$ is known** for all $\ell \in [L]$, and  
  (ii) The assumption of **Gaussian reward noise**, which is stronger than the sub-Gaussian noise typically assumed in the contextual bandit literature.
- Regarding **Assumption (A2)**, I encourage the authors to justify why such an assumption is necessary (rather than simply referring to "milder assumptions"). This assumption is non-standard compared to existing literature, and further elaboration is needed to position the analysis on firm ground. Providing a more explicit explanation would allow future work to build upon these assumptions, even if they seem restrictive.
- A fundamental concern lies in how the **$O(\sqrt{d(K+L)T})$ Bayes regret** in Theorem 4.1 compares with the well-established **$O(\sqrt{KT})$ Bayes regret** for the non-contextual multi-armed bandit (as in Russo and Van Roy, 2014). The bound of $O(\sqrt{d(K+L)T})$ in Theorem 4.1 is worse than both the non-contextual result in Bayes regret and the **worst-case regret bound of $O(\sqrt{KT})$** from Agrawal and Goyal (2023b) without prior. Why should practitioners consider this method in the linear case when the theory suggests it’s more effective to treat arms independently and use the non-contextual MAB version of Thompson sampling?
- The section “**Why the bound increases with L?**” (Line 268) is confusing. The theoretical result in the paper shows that increasing $L$ worsens the upper bound, implying that in the linear case, one should use **$L=1$**. The current explanation seems contrary to the theoretical findings for the linear case, and the authors should clarify this discrepancy.
- A **table of notations** is necessary, at least at the beginning of the appendix, to improve clarity and assist readers in following the paper’s mathematical presentation.


### **Minor Comments**:

- **Line 1151-1152**: "This sparsity assumption is both a novel and a key technical contribution to our work."  
  It is debatable whether adding a structural assumption qualifies as novel unless it offers new insights or introduces milder assumptions compared to existing literature.

### Questions
Theorem 4.1 presents a **$O(\sqrt{d(K+L)T})$ Bayes regret** bound. Compared to Russo and Van Roy’s (2014) **$O(d\sqrt{T})$ Bayes regret** for linear Thompson sampling, I am curious about how your bound handles the **$O(\sqrt{d})$** factor. While I understand that the additional **K** factor stems from a different setting (with shared parameters across arms in Russo and Van Roy’s work), I would appreciate further elaboration on how your method results in a **$O(\sqrt{d})$** regret bound. Could you explain this in more detail?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies contextual bandits where the feature vectors of the actions are hidden and generated by a known diffusion model. The authors propose an algorithm based on posterior sampling and show that the posterior update can be performed efficiently, using an approximation inspired by the linear case. The authors also theoretically demonstrate that the algorithm achieves a sublinear regret bound when the link functions are linear. Lastly, they present experiments to illustrate the practical performance of the algorithm.

### Strengths
1. Combining bandit algorithms with diffusion models is an innovative approach.

2. The paper introduces an efficient approximation for posterior updates in diffusion models, which I found interesting. The provided experiments offer valuable insights into the performance of this approximation.

### Weaknesses
1. I am unsure if the setting makes sense. Specifically, since $\theta_{\*,i}$ are fixed across episodes, their concatenation can be interpreted as a hidden vector. This allows us to reduce the problem to a generalized linear contextual bandit with dimension $dK$. In this case, the feature vector for each action $i \in [K]$ is $[0, \dots, 0, X_t, 0, \dots]$, activating only the entries corresponding to $\theta_{\*,i}$. This formulation should result in an algorithm with regret $\tilde{O}(\sqrt{dKT})$, which is a standard result for linear bandits as shown in [1]. Therefore, I question the advantage of introducing the posterior sampling over the diffusion model in this context, given that a simpler approach might achieve a similar or better regret bound.

2. The theoretical analysis assumes linear link functions. However, since a combination of linear functions remains linear, the diffusion model may effectively reduce to a single linear function. This simplification potentially trivializes the problem, as the complexities introduced by the diffusion model might not be fully utilized in this scenario. It would be more convincing if the theoretical analysis could be extended to non-linear link functions to demonstrate the true benefits of the proposed approach.

3. Certain parts of the paper are unclear. For instance, it is not specified whether the covariance matrix $\Sigma_l$ or the link function $g$ are revealed to the agent. This information is crucial for understanding the information available to the agent and the complexity of the learning problem. Without this clarity, it is difficult to fully assess the proposed algorithm and its assumptions.

### Questions
Please refer to the Weaknesses section above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper considers the classical contextual bandit problem from a Bayesian perspective, particularly through the use of a diffusion model. The arms are correlated via a shared distribution for their parameters. The paper proposes a new Thompson sampling algorithm that incorporates a diffusion model prior. The estimation of the posterior distribution and efficient sampling method are applicable to other Thompson sampling problems. The effectiveness of the algorithm is demonstrated by the regret bound in a linear case, where the regret is of order $\sqrt{KT(\log{T})^2}$. Additionally, the paper presents a numerical study to validate the algorithm, showing improvement over existing benchmarks in cases where the true prior is a diffusion model as well as in cases where the true prior is not a diffusion model.

### Strengths
1. The paper proposes a new algorithm for contextual bandits with dependent arms, using diffusion models.
2. The paper is relatively clearly written and easy to follow.
3. The paper includes a variety of interpretations of the results, both theoretical and numerical.
4. The theoretical statements and numerical experiments are solid, as they are clearly presented and explained. The regret bound is nearly optimal in that it is approximately of order $\sqrt{T}$, when the $\log{T}$ term is negligible.

### Weaknesses
1. The actual role of using a diffusion model remains unclear. If the prior is not a diffusion model, will the algorithm still perform effectively in this scenario?

2. The theoretical statements provided are only valid for the linear case. It is also unclear whether there would be a significant gap in performance between linear and non-linear cases, which could impact the applicability of the algorithm in more complex settings.

3. The paper addresses both the contextual bandit and bandits with dependent arms. However, this combined focus makes it challenging to isolate the specific impact of using a diffusion model. It remains unclear whether the diffusion model could be effectively applied in the traditional contextual bandit problem without dependent arms, as dependent arms generally allow for more informative decision-making.

4. Lastly, I am curious whether a diffusion model is truly necessary in this setting, especially if it is already pre-trained, to handle the contextual bandit scenario with dependent arms.

### Questions
I would refer to the weaknesses section. Any clarification or illustration would be very helpful.

### Soundness
3

### Presentation
3

### Contribution
2
