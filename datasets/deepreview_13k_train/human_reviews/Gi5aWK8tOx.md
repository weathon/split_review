# On the Sample Complexity of a Policy Gradient Algorithm with Occupancy Approximation for General Utility Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Reinforcement learning with general utilities has recently gained attention thanks to its ability to unify several problems, including imitation learning, pure exploration, and safe RL. 
However, prior work for solving this general problem in a unified way has mainly focused on the tabular setting. This is restrictive when considering larger state-action spaces because of the need to estimate occupancy measures during policy optimization.  
In this work, we address this issue and propose to approximate occupancy measures within a function approximation class using maximum likelihood estimation (MLE). 
We propose a simple policy gradient algorithm (\algo) where an actor updates the policy parameters to maximize the general utility objective whereas a critic approximates the occupancy measure using MLE. We provide a sample complexity analysis of {\algo} showing that our occupancy measure estimation error only scales with the dimension of our function approximation class rather than the size of the state action space. Under suitable assumptions, we establish first order stationarity and global optimality performance bounds for the proposed {\algo} algorithm for nonconcave and concave general utilities respectively. 
We complement our methodological and theoretical findings with promising empirical results showing the scalability potential of our approach compared to existing tabular count-based approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The proposed method estimates state-action occupancy measures by MLE and uses them for policy gradient to maximize general utility.

### Strengths
1. MLE estimation of state-action occupancy measure is more sample-efficient than count-based algorithms and can be used in continuous state-action spaces

### Weaknesses
1. The proposed work learns state-action occupancy measures (Eq. 8). But it does not learn the occupancy measure defined in Eq. 1. In Eq 1, the occupancy measure is discounted by \gamma. However, Eq. 8 does not have a discount. And we don't know if the learned occupancy measure satisfies the backward Bellman flow equation which is mentioned in Section 3.1.


2. line 221: "Second and foremost, while prior work has used Monte Carlo estimates for
this quantity, such count-based estimates are not tractable beyond small tabular settings."

There are RL algorithms that focus on using stationary state-action distributions for learning policies that maximize expected returns with some constraint on the stationary distributions and these works do not use count-based estimates and works on continuous state-action space as well [1,2]. These methods, while not directly addressing the general utility maximization problem, demonstrate that alternatives to count-based methods exist for learning with stationary distributions in continuous spaces, which weakens the claim about the necessity of count-based methods.

[1] Lee et al. "Coptidice: Offline constrained reinforcement learning via stationary distribution correction estimation." ICLR 2022.

[2] Mao et al. "Diffusion-DICE: In-Sample Diffusion Guidance for Offline Reinforcement Learning." NeurIPS 2024.

3. Question on the practicality of the proposed method: after each policy parameter update, you would need to gather data for the MLE of the occupancy measure and fit the occupancy measure which can be time-consuming. This computational overhead is a significant concern, especially for complex environments where data collection and model fitting are expensive.

### Questions
1. How does the proposed method relate to [1][2]? Additional experiments comparing the performance of these algorithms with the proposed method would also be helpful in understanding the difference between the methods. Since [1][2] are offline RL algorithms, maybe letting the target policy collect data periodically would make it possible to run them on on-policy manner and compare them to the proposed method.

[1] Lee et al. "Coptidice: Offline constrained reinforcement learning via stationary distribution correction estimation." ICLR 2022.
[2] Mao et al. "Diffusion-DICE: In-Sample Diffusion Guidance for Offline Reinforcement Learning." NeurIPS 2024.

2. Question on the practicality of the proposed method:  Additional experiments showing the time required until convergence of the target policy performance for the proposed method and the baselines would help clear this concern.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a policy gradient algorithm for general utility reinforcement learning where an estimation of occupancy measure is involved to address the challenge caused by large state-action spaces. Provided theoretical analysis covers both statistical and optimization aspects. Additionally, numerical results are presented to demonstrate the algorithm's effectiveness in tasks involving large state-action spaces.

### Strengths
This paper identifies a challenge in General Utility Reinforcement Learning/Convex Reinforcement Learning caused by large state-action spaces and proposes a method to address it. The motivation is well-founded, and the proposed method is sound and natural, i.e. utilizing a maximum likelihood estimator to estimate the occupancy measure. The theoretical analysis is comprehensive, and the paper includes a reasonably thorough comparison with closely related existing works in the Appendix. The structure is logical, with ideas presented in a clear and coherent manner.

### Weaknesses
1. The primary weakness seems to be the limited novelty of the idea. Although the authors provide a comparison with a related work [1] in the Appendix, the advantages of the proposed method over [1] are not immediately clear. For example, it would be beneficial to include a more detailed discussion of the assumptions required in this work versus those in [1], clarifying which are weaker, stronger, or more practical for specific problem settings. Additionally, highlighting the advantages of the proposed model-free algorithm over the model-based approach in [1] would also be helpful. I think these would significantly improve the paper by more clearly demonstrating its unique contributions.

2. Based on the content in the Appendix and my observations, the technical theoretical analysis appears to draw upon existing results. The statistical analysis is derived from [2], while the optimization analysis is based on [3], with minor adaptations to handle estimation error. However, this is not a critical issue if the authors address the concerns outlined in the Weakness 1, as this would help establish the paper’s distinct contributions more effectively.

### Questions
1. It would be helpful if the authors could clarify the additional assumptions or new technical tools required for proving global convergence compared to [1]. 

2. Compared to [2], I am wondering if there exists any sacrifice in the results when you prove a last-iterate global convergence, e.g. looser upper bound, more restrictive assumptions, etc.

3. In Theorem 2, does $\epsilon_{MLE}$ implicitly depend on the number of iterations, $T$? Since the estimation errors for occupancy must be uniformly controlled across all iterations, it seems intuitive that $\epsilon_{MLE}$ might depend on $T$. Explicitly stating this dependence would clarify its impact on Corollary 2.

4.  Also, I think $\epsilon_{MLE}$ should depend on the size of the policy space because $\theta_t$ is not fixed in each iteration. If I understand it correctly,  you essentially need $sup_{t=1,...,T} \sup_{\theta_t\in \Theta}$(Estimation error at $t$) $<\epsilon_{MLE}$. I suggest to discuss more on this as the dependence on the size of policy space typically appears in the model-free methods.

[1] Barakat, A., Fatkhullin, I., & He, N. (2023, July). Reinforcement learning with general utilities: Simpler variance reduction and large state-action space. In International Conference on Machine Learning (pp. 1753-1800). PMLR.

[2] Mutti, M., De Santi, R., De Bartolomeis, P., & Restelli, M. (2023). Convex reinforcement learning in finite trials. Journal of Machine Learning Research, 24(250), 1-42.

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
3

### Summary
The paper investigates the policy gradient algorithm with occupancy approximation for general utility reinforcement learning (GURL). It proposes a policy gradient algorithm that approximates the occupancy measure using maximum likelihood estimation (MLE). The introduction of MLE eliminates the dependency of the estimation error on the state space size, leading to improved performance bounds. The theoretical gain is also corroborated by empirical evidence.

### Strengths
**Novelty**: The introduction of MLE for occupancy measure approximation is a novel contribution to the theoretical investigation of GURL. It addresses the limitation of previous count-based approximation and offers advantages over mean square error estimation.

**Clarity**: The paper is well-structured and written, making it easy to read and follow. The main results are clearly highlighted, and the conclusions are succinctly declared. This clarity enhances the reader's comprehension and engagement with the material.

**Significance**: The introduction of MLE for occupancy measure approximation and the theoretical analysis constitute a moderately significant contribution to GURL. It advances the understanding of occupancy measure approximation. 

**Quality**: The paper is of high quality, demonstrating rigorous and reliable research. The arguments are well-supported, and the methodologies are robust, contributing to the overall reliability of the results.

### Weaknesses
 **Predictable Results**: Although the introduction of MLE estimation and corresponding theoretical analysis is a novel and concrete contribution, the state space size independent performance bound is somewhat predictable given the assumptions. This result is not surprising and thus may not add substantial new insights. Additionally, the widespread use of MLE in practice diminishes the practical value of the proposal.

**Unjustified Assumptions**: The paper lacks practical examples that satisfy Assumption 3, which appears quite restrictive. The requirement for utility smoothness is particularly challenging for utilities involving Kullback-Leibler (KL) divergence. Furthermore, Assumption 5 necessitates a bijection relationship between the neighborhood of the softmax policy parameter $\theta$ and the corresponding occupancy measure $\lambda(\theta)$. However, the paper does not provide an example illustrating how this requirement can be fulfilled, leaving the assumption potentially unjustified.

### Questions
Can you provide specific types of RLGU problems where these assumptions might hold or discuss how restrictive these assumptions are in practice?

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
This paper propose to approximate the occupancy measure within a function approximation class using maximum likelihood estimation (MLE). Based on this, it develops a policy gradient method for General Utility RL, demonstrates the sample complexity for non-concave and concave utility functions, and shows the experiment results in discrete and continuous state-space settings.

### Strengths
This paper offers a  method to estimate occupancy measure potentially for large-scale state-action spaces. It shows the convergence rate for both non-concave and concave utility functions. The paper is well-written and easy to read.

### Weaknesses
The only novelty of this paper is the use of MLE in estimating the occupancy measures. Other parts in the method, such as the form of policy gradient for convex RL, are known results. However, prior work such as Barakat et al (2023) have already considered a very similar approach using mean square error (MSE) estimation. The replacement of MSE by MLE seems trivial, and the consequent analysis seems straightforward (MSE and MLE are two common estimation methods, and the only difference seems to be different loss objectives used
in the neural network). Although the authors carried out a detailed analytical comparison between MSE and MLE in Appendix A, the comparison is not very convincing (for example, when comparing the TV bound on the estimation error, the TV bound of MSE is obtained by relaxation and the dependce on |X| is based on the assumption that p* is uniform). There is no numerical comparison between the methods using MLE versus MSE. Overall, I think the novelty and contribution of this paper is quite limited.

### Questions
1. Please state the novelty of this paper clearly in the introduction, especially the connection and difference with the prior work that uses MSE for estimating the occupancy measure. Is there any technical challenge in replacing MSE with MLE? How to choose the
function class so that the true occupancy measure can be estimated well, i.e. Assumption 1(ii) is satisfied?

2. The dependency of MSE on |X| is currently shown based on the assumption that p^* is uniform. Can you provide a more rigorous analysis for the general case to support the claim that MSE depends on |X| and suffers from scalability issue? 

3. As stated in the paper, MSE method may introduce a scalability issue while MLE does not. In addition to the analytical comparison (as in question 2 above), can you compare MLE and MSE numerically to support this claim?

3. Is there any challenge in the proof of Theorem 1 and Theorem 2? Please highlight the challenges in adapting the analysis in Zhang et al. (2021) to this paper.

### Soundness
3

### Presentation
3

### Contribution
1
