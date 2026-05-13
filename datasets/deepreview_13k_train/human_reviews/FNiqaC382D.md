# Provable Causal State Representation under Asynchronous Diffusion Model for POMDPs

- Decision: Reject
- Scores: 8, 5, 3, 6

## Abstract
A major challenge in applying reinforcement learning (RL) to real-world scenarios is managing high-dimensional, noisy perception input signals. Identifying and utilizing representations that contain sufficient and essential information for decision-making tasks is key to computational efficiency and generalization of RL by reducing bias in decision-making processes. In this paper, we present a new RL framework, named *Causal State Representation under Asynchronous Diffusion Model (CSR-ADM)*, which accommodates and enhances any RL algorithm for partially observable Markov decision processes (POMDPs) with perturbed inputs. A new asynchronous diffusion model is proposed to denoise both reward and observation spaces, and integrated with the bisimulation technology to capture causal state representations in POMDPs. Notably, the causal state is the coarsest partition of the denoised observations. We link the causal state to a causal feature set and provide theoretical guarantees by deriving the upper bound on value function approximation between the noisy observation space and the causal state space, demonstrating equivalence to bisimulation under the Lipschitz assumption. To the best of our knowledge, CSR-ADM is the first framework to approximate causal states with diffusion models, substantiated by a comprehensive theoretical foundation. Extensive experiments on Roboschool tasks show that CSR-ADM outperforms state-of-the-art methods, significantly improving the robustness of existing RL algorithms under varying scales of random noise.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper considers causal state representations of partially observable environments for approximately solving POMDPs. Specifically, the authors propose an approach to find bisimulation-based causal state models by denoising observations and rewards via an asynchronous diffusion model. The offers also do analysis and give some theoretical guarantees under some assumptions.

### Strengths
This is a generally well-written paper based on a novel idea (as far as I can judge). It combines a proposal of an algorithm with theoretical analysis and reasonable, well-designed experiments

### Weaknesses
A few points could be clearer in the manuscript, some of which I listed in the questions below. Part of my confusion could be my lack of in-depth knowledge of Causal State Representations.

Upon initial reading I was unclear what was meant by “POMDPS with perturbed inputs” in the abstract. Isn’t the whole point of any POMDP that its inputs (observations of the environment) are subject to noise?
Line 151: “the action a_{t-1} directly affects the state s_t rather than the observation signal o_t”: Why then is the probability of o_t defined conditional on a_{t-1} in eq. 1a.
Algorithm 1: Why does \zeta denote both the reward noise model and the bisimulation model?

### Questions
Upon initial reading I was unclear what was meant by “POMDPS with perturbed inputs” in the abstract. Isn’t the whole point of any POMDP that its inputs (observations of the environment) are subject to noise? 
Line 151: “the action a_{t-1} directly affects the state s_t rather than the observation signal o_t”: Why then is the probability of o_t defined conditional on a_{t-1} in eq. 1a. 
Algorithm 1: Why does \zeta denote both the reward noise model and the bisimulation model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a method of dealing with noisy observations in RL, which they call CSR-ADM. Intuitively, the algorithm uses both a denoise model and a bisimulation metric to find 'causal state representations' for a given observation, which can be used by off-the-shelf RL algorithms to compute policies. The authors provide a sub-optimality bound for their method under some (reasonable) assumptions on the dynamics of the environment. Empirically, the authors show that incorporating their method into SAC improves performance and outperforms methods that only consider denoising or finding causal representations.

### Strengths
* The topic of the paper is interesting and significant: dealing with partial observability is a key problem when applying RL in the real world. 
* The paper combines both theory and application nicely. Moreover, the proposed method can easily be incorporated into off-the-shelf RL methods, which makes it easier to apply in practice. 
* The authors compare their method with relevant baseline algorithms and use an ablation study to show the relevance of all proposed components.

### Weaknesses
The main weakness of this paper is its presentation. The intuition behind the methods is easy to follow, but details are often unclear: see some of my questions below. Because of this, I find it hard to determine the quality of the proposed method.

I'll note some other minor weaknesses:
* The method assumes Gaussian noise. Thus, the method may struggle with other noise (such as raindrops or colour shifts), and does not help with other types of partial observability (such as missing data). The assumption of Gaussian noise, while simplifying analysis, limits the practical applicability of the method in real-world scenarios where noise distributions are often non-Gaussian and can include complex forms of corruption. For instance, sensor noise might exhibit heavy-tailed distributions, or visual noise could involve structured patterns that are not well-approximated by Gaussian distributions. Furthermore, the method does not address the issue of missing data, which is a common problem in real-world applications of RL, where sensor readings can be intermittent or unavailable.
* The paper does not quantify the additional computational cost of the method: this would be good to add. The lack of a detailed computational cost analysis makes it difficult to assess the practical feasibility of the proposed method. It is essential to understand how the computational complexity scales with the size of the state, action, and observation spaces, as well as the number of training samples. Without this information, it is challenging to determine whether the method is suitable for resource-constrained environments or large-scale applications.

### Questions
* In Eqs. 1a-1c, what exactly are the assumptions you make about the dynamics of the model? For example, must the state-, action- and observation spaces be continuous, or can they be discrete? What about the functions $f,g$ and $h$? Can two states give the same observation?
* In eq. 1, $f$ denotes the observation function. However, in Def. 1 and in Assumption 2, $f$ is also used to denote something that looks like an observation function but has a different number of inputs. How do these relate?
* $\zeta$ is overloaded in a confusing way: it is used to describe the predicted state (line 234), the noisy state (line 269), as well as the bisimulation model (Alg 1, line 2). Do these all represent the same thing?
* In Eqs. 7 and 8 and Alg 1, $\theta$ and $\zeta$ seem to be switched. Is this a typo?
* After eq. 6, the paper mentions a variables $n$, $\hat{s}_{t+1}$ and $r_{t+1}$. What do these refer to?
* In Alg. 1, what is the function of line 7? What do we use the sampled transitions for?
* In line 297, how can the diffusion model predict a future state? I thought it only removed noise?
* In Assumption 3, what does this assumption intuitively mean? Are $s_i, s_j \in S$, or in $S \cup O$ ?
* I do not understand Thm 1: it seems to me that if we pick $c_T \approx 0$ and $c_R \approx 1$, then any states that have the same immediate reward would have a value gap of $\approx 0$ as well, which clearly is not the case. Can you explain why it holds?
* In Fig 4 (App. A), how is $P(\hat{s}_t|o_t)$ computed? I thought this was what the diffusion model was used for.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a method that incorporates the diffusion model in RL algorithms, along with the theoretical guarantees. Empirical evaluation is also included.

### Strengths
N/A

Caveat: As a researcher in learning theory, I am not familiar with the current line of research on RL with diffusion models. In below, I only evaluate this paper based on its math and theory, and my review should be taken with AC's discretion.

### Weaknesses
I find this paper difficult to understand.

1. The term "bisimulation" is never defined or well-explained. Definition 1 is also not rigorous: in POMDP, the distribution P(s_{t+1}|o_t,a) clearly depends on the history (and hence the policy). It is also not clear why there is a partition of the state space into the observation space.

2. Definition 2/Assumption 3 seems to define the bisimulation metric in terms of a fixed-point equation. While such a metric is shown to exist (at least when p=1), I find it difficult to interpret.

3. In Theorem 2, $\mathcal{E}_\zeta$ is defined twice.

4. Theorem 4 is claimed to establish the convergence of the proposed algorithm, but I can't see how. In. particular, the RHS of (15) is not vanishing when n tends to infinity. Further, the algorithm is based on gradient descent, but there is no analysis of GD here (it is vaguely mentioned that previous results can be invoked).

### Questions
See my discussion on the weakness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This work considers the decision-making problem in POMDP with diffusion as an estimation tool. The authors adopt the diffusion model to utilize the causal graph under the POMDP for better value function estimation. They provide the theoretical analysis of the proposed algorithm, and the efficacy of the algorithm is also verified by the experimental results.

### Strengths
1.	The authors propose novel methods to make use of the causal structure under the POMDP environment, which achieves better performance in the simulations.
2.	This work contains the solid theoretical guarantee for the proposed methods.

### Weaknesses
1.	The implications of the assumptions adopted in this work are not clear. For Assumption 2, it is beneficial to justify when the lower boundness of $f$ holds in the real applications. Specifically, what properties of the function $f$ or the data would guarantee this lower bound? Are there specific classes of functions or data distributions for which this assumption is more likely to hold, and what are the practical implications if this assumption is violated? For Assumption 3, I find that the statement of Definition 2 is not appropriate. When defining a mathematical notion, it is uncommon to state `` following metric exists and is unique’’, which looks like the statement of a theorem. In addition, I suggest the authors to discuss the sufficient conditions of Assumption 3. For example, if the state, action, and observation spaces are finite, will this metric exist and be unique? It would be helpful to understand if the existence and uniqueness of this metric is guaranteed under common POMDP settings, or if it requires specific structural properties of the environment.

2.	It will be helpful to discuss more about the results of diffusion model. In the existing analysis of diffusion models, the distribution estimation error usually consists of initialization error, score estimation error, and the discretization error. But such error decomposition structure is not presented in the current results. It is crucial to see how each of these errors contributes to the overall estimation error, and how the proposed method addresses each of them. Furthermore, how do the choices of hyperparameters, such as the number of diffusion steps, affect these individual error components and the overall performance of the algorithm?

3.	In addition, this is beneficial to discuss and explain each theorem below the statement of the results. The current presentation leaves the reader to infer the implications of each theorem, which makes it difficult to understand the significance of the theoretical results. For example, for Theorem 1, what does the bisimulation metric in (12) practically represent in the context of value function estimation? For Theorem 2, how does the upper bound on the value gap relate to the convergence of the algorithm? And for Theorem 3, what does the convergence of the Wasserstein-1 distance imply about the quality of the estimated distribution?

### Questions
Same as the weakness

### Soundness
3

### Presentation
3

### Contribution
3
