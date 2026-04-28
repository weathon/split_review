# Posterior Sampling via Langevin Monte Carlo for Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
In this paper, we consider offline reinforcement learning (RL) problems. Within this setting, posterior sampling has been rarely used, perhaps partly due to its explorative nature. The only work using posterior sampling for offline RL that we are aware of is the model-based posterior sampling of \cite{uehara2021pessimistic}. However, this framework does not permit any tractable algorithm (not even in the linear models) where simulations of posterior samples become challenging, especially in high dimensions. In addition, the algorithm only admits a weak form of guarantees -- Bayesian sub-optimality bounds which depend on the prior distribution. To address these problems, we propose and analyze the use of Markov Chain Monte Carlo methods for offline RL. We show that for low-rank Markov decision processes (MDPs), using the Langevin Monte Carlo (LMC) algorithm, our algorithm obtains the (frequentist) sub-optimality bound that competes against any comparator policy $\pi$ and interpolates between $\tilde{\mathcal{O}}(H^2 d \sqrt{C_{\pi}/ K})$ and $\tilde{\mathcal{O}}(H^2  \sqrt{d C_{\pi}/ K})$, where $C_{\pi}$ is the concentrability coefficient of $\pi$, $d$ is the dimension of the linear feature, $H$ is the episode length, and $K$ is the number of episodes in the offline data. For general MDPs with overparameterized neural network function approximation, we show that our LMC-based algorithm obtains the sub-optimality bounds of $\tilde{\mathcal{O}}(H^{2.5}  \tilde{d}  \sqrt{C_{\pi} /K})$,  where $\tilde{d}$ is the effective dimension of the neural network. Finally, we collaborate our findings with numerical evaluations to demonstrate that LMC-based algorithms could be both efficient and competitive for offline RL in high dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission studies a Bayesian method for offline RL. The proposed method is quite simple (which I see as a pro), simply do the noisy gradient descent on the regression objective. Analysis with improved bounds is the main contribution of the paper.

### Strengths
- The proposed method is simple and seems implementable in practice. 

- The bounds are improved from previous work. 

- Analysis of the NTK regime is performed, which might be of independent interest.

### Weaknesses
 - I do not see particularly new ideas from the submission, either in the algorithm or in the analysis. Thus, the novelty of the paper is limited. 

- The work in Uehara and Sun [US21] considers the setting where the representation of state-action $\phi(s,a)$ is unknown, whereas the submission assumes the feature representation function is known. I think it is not fair to claim the improvement from [US21].

In general, even though this is a technical paper, the submission is a bit hard to parse. 

- How is the regression objective related to posterior sampling? How is this a "Langevin" Monte Carlo method? It would be good to be introductory to Langevin Monte Carlo methods, and how the concepts are attached to the actual algorithm presented. 

- I had to understand the linear (or low-rank) MDP part very clearly before paying attention to the NTK function approximation part. I do not see any particular contribution from the NTK part to reinforcement learning theory. It is a good add-on result though.

### Questions
- I wonder how this method performs on some offline deep-RL benchmarks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores convergence of posterior sampling via Langevin Monte Carlo for offline RL.

### Strengths
The study sounds solid, although I did not go through each step of the proof.

### Weaknesses
The paper did not clearly explain the fundamental difference between the convergence of Langevin Monte Carlo and the convergence of the RL posterior sampling under the offline setting. Specifically, it's unclear how the theoretical convergence guarantees of LMC, which are typically established under assumptions like log-concavity of the target distribution and sufficient smoothness, translate to the convergence of the RL posterior, which is a more complex object dependent on the offline data and the specific RL objective function. The paper does not sufficiently address the potential for discrepancies between the stationary distribution of LMC and the true posterior, especially given the approximations inherent in the offline RL setting.

Furthermore, the choice of LMC over SGLD in Algorithms 2 and 3 is not well-motivated. While the authors mention that SGLD introduces additional complexities, they do not elaborate on the specific challenges or why these complexities cannot be addressed using standard techniques. The use of LMC, a deterministic method, seems counterintuitive given the stochastic nature of RL and the potential benefits of using stochastic gradients for exploration. The paper lacks a clear justification for this seemingly restrictive choice, especially when considering the computational efficiency of SGLD.

### Questions
1. What is the difference between the convergence of Langevin Monte Carlo and the convergence of the RL posterior sampling under the offline setting? Will the former lead to the latter? 

2. Why is LMC, instead of SGLD, used in Algorithms 2 and 3?  Can mini-batch data be used in simulations of the proposed algorithm?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a model-free posterior sampling approach for offline RL using Langevin Monte Carlo (LMC) for posterior approximation. They introduce practical algorithms in an episodic setting for both linear low-rank MDPs, and general MDPs (with over-parameterized neural networks for value function approximation, alongside an auxiliary linear model for LMC). Notably, the paper establishes frequentist sub-optimal bounds both cases. Empirical evaluations on linear MDP and non-linear contextual bandits support the proposed algorithms' effectiveness.

### Strengths
I believe the most important strength is that the paper offers an insightful advancement in offline RL through a Bayesian lens. While the value-based variation to classical PSRL and the employment of LMC for posterior approximation are not novelties in isolation, their integration within offline RL is both meaningful and aptly executed. 

The implicit pessimism by posterior sampling with the proof of a frequentist bound is also a non-trivial contribution, and provides a fresh perspective to ongoing discussions in this domain.

### Weaknesses
While the paper makes significant theoretical advancements, it would further solidify its applicability if the proposed algorithms were tested on well-regarded benchmarks, such as the MuJoCo tasks from the D4RL suite. Additional experiments with model-based approaches would offer a comprehensive perspective on the approach's effectiveness.

The presented approach captures pessimism through posterior sampling. While innovative, one could question whether this form of pessimism adequately represents the complex nature of uncertainties found in the offline dataset, particularly given the non-stationary distributions that can arise from varied data collection policies.

### Questions
Please refer to the concerns in the weaknesses part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
