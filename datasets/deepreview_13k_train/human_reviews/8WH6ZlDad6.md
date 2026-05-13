# EWoK: Tackling Robust Markov Decision Processes via Estimating Worst Kernel

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Robust Markov Decision Processes (RMDPs) provide a framework for sequential decision-making that is robust to perturbations on the transition kernel. However, current RMDP methods are often limited to small-scale problems, hindering their use in realistic high-dimensional domains. To bridge this gap, we present **EWoK**, a novel approach for the online RMDP setting that **E**stimates the **Wo**rst transition **K**ernel to learn robust policies. Unlike previous works that regularize the policy or value updates, EWoK achieves robustness by simulating the worst scenarios for the agent while retaining complete flexibility in the learning process. Notably, EWoK can be applied on top of any off-the-shelf *non-robust* RL algorithm, enabling easy scaling to high-dimensional domains. Our experiments, spanning from simple Cartpole to high-dimensional MinAtar and DeepMind Control Suite environments, demonstrate the effectiveness and applicability of the EWoK paradigm as a practical method for learning robust policies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to solve the Robust Markov Decision Process (RMDP) problem in a realistic high-dimensional scenario, and introduces a method named EWoK. EWoK assigns a higher probability to the transition where the next state has a lower estimated value such that the agent gets a higher chance to learn from the worse transition. EWoK acts as a layer between the true transition metrics and the agent and directly changes the sampled next state, rather than requiring any specific change on the learning agent. Thus, it is able to work with any non-robust reinforcement learning algorithm.

### Strengths
- The paper focuses on a nice topic, dealing with the issue that many RMDP algorithms cannot scale to high-dimensional domains. The idea of EWoK is creative. The method bridges robust and non-robust reinforcement learning algorithms, by changing the transition metrics to let it focus more on the robust case and learning the policy with any non-robust algorithm. Therefore, EWoK reserves the ability to scale to high-dimensional inputs by learning a policy using existing reinforcement learning algorithms. 

- The experiment section has enough runs (40 and 10 seeds in different environments) to provide relatively reliable average and confidence intervals.

- The experiment section provides ablation studies for two introduced parameters ($\kappa$ and $N$).

### Weaknesses
However, the method may need further improvement. 

- I am not convinced yet that EWoK can be applied in a realistic domain as claimed. As the paper indicates in the conclusion section, EWoK assumes the environment is able to sample from the same state and action pair multiple times. This requirement is easy to achieve when using simulators or when there exists a perfect model, but is unrealistic in real environments. In the real world, it is almost impossible to reset the environment to the previous state and apply the same action multiple times. Given that the paper defines EWoK as an online method for realistic domains, I think this assumption contradicts the scenario which EWoK is supposed to work with. It might be more accurate if the paper reduces the scope to high-dimensional domains.

- At the end of the experiments section, the paper mentions a larger number of next-state samples does not affect the wall clock time a lot. It is nice to notice and discuss the running time of a method, but  I would like to point out that this happens in simulators because simulators react fast. In real-world scenarios, the environment could be much slower for sampling one next state. It would be nice to also check a case in robotics, or some other environments taking relatively long time to respond.

- It might be worth checking a more difficult experiment setting, such as the one single trajectory case.

### Questions
- Could the authors provide a learning curve to show how long the method takes to converge? It would be better if the learning curve plot could also include your baselines.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach, called EWOK, to address robust MDPs based on the KL-divergence $(s,a)$-rectangular ambiguity set. Specifically, this paper simulates the transited state to approximate the worst-case transition kernel based on the analytical form of the robust Bellman update. Also, the comprehensive experiment illustrates the robustness and good performance of the EWoK in various RL environments.

### Strengths
This paper is easy to follow. While EWoK is provided based on specific KL-divergence $(s,a)$-rectangular ambiguity set, it provides a new perspective to estimate the worst-case transitions.

In the experiments, the authors compare their algorithm to both the benchmark non-robust algorithm and the commonly used domain randomization method. The results demonstrate the outperformance of the proposed algorithm in multiple RL practical problems.

### Weaknesses
One reason for not giving a higher score at this point is that it seems to me that all the results in this particular paper are rather intuitive or expected. It is worth noting that the convergence analysis of $(s,a)$-rectangular RMDPs has already been extensively studied. While Theorem 3.2 provides the explicit form of the worst-case transition kernel for the KL-divergence ambiguity set, other results do not seem particularly surprising. In particular, Theorem 3.5, which claims an iterative method to find the worst-case transition kernel, lacks sufficient novelty and its convergence analysis seems to follow standard results in the analysis of RMDPs. The iterative nature of finding the worst-case transition kernel, while practically useful, does not present a significant theoretical leap. 

Another aspect that seems to be lacking is a discussion on how the radius $\beta_{sa}$ of the ambiguity set affects the algorithm's performance, although it would be transferred to new parameters $\omega_{sa}$ and $\kappa_{sa}$. I do expect that the parameter selection procedure could be discussed more. Specifically, the paper does not provide guidance on how to choose the hyperparameter $\kappa_{sa}$, which directly influences the size of the ambiguity set and thus the conservativeness of the resulting policy. The lack of a principled method for setting this parameter is a significant practical concern.

### Questions
The numerical results and theoretical discussion make sense to me. I have the following questions and suggestions:
1. The literature review is not comprehensive. A recent paper [1] also studied RMDPs with global optimality, and it would be helpful if the author discussed it. 
2. The official definition of the robust Bellman operator should be added in Section 2.3 for completeness.
3. While we consider a practical problem lying in the KL-based $(s,a)$-
rectangular ambiguity set, the only parameter that the agent can choose is $\beta_{sa}$; however, the other two parameters $\omega_{sa}$ and $\kappa_{sa}$ would be settled directly. Could you explain more about the relationship between $\beta_{sa}$ and the other two parameters $\omega_{sa}$ and $\kappa_{sa}$, or how can the agent reach the latter when setting the former? 

[1] Wang, Qiuhao and Ho, Chin Pang and Petrik, Marek. "Policy Gradient in Robust MDPs with Global Convergence Guarantee." ICML (2023)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies online RL in robust Markov decision processes from the perspective of worst transition kernel estimation, which can help scale RMDP-based methods to high-dimensional domains and is thus of great significance to the advance of robust RL. The authors start from the theoretical side by giving a closed form solution to the worst case transition kernel (Theorem 3.2). Motivated by the explicit expression, an approximation of the worst case transition is proposed. The proposed algorithm is extensively studied on various robust RL experimental setups.

### Strengths
1. The paper first characterizes the worst case transition dynamic within KL-constrained uncertainty set by a closed form solution (Theorem 3.2), which is of independent interests for future researches on robust MDPs. 
2. The idea to simulate the worst case transition based on an approximation of the closed form solution is novel.
3. The method break the curse of scalability of traditional RMDP-based methods with several experimental demonstrations in complex RL domains. The experiments are well organized and convincing.

### Weaknesses
1. I think the idea of using a resampling trick to simulate the true worst case transition dynamic (Line 4 of Algorithm 1) is interesting and makes sense given the product form of the solution (Theorem 3.2). However, the intuition behind the empirical choice of the unknown parameter $\omega_{s,a}$ (Eq. 12) is somehow elusive, even the authors provided Proposition 3.4 to argue. Specifically, while Proposition 3.4 shows that the empirical average provides an *overestimation*, it does not clarify *why* this specific overestimation is a good choice for approximating the worst-case transition. The connection between this specific overestimation and the desired robust behavior is not clearly established. It's unclear if other forms of overestimation could perform better or worse, and the justification for this particular choice is weak.
2. Minor typos and notation clarity problem in the theory part (Section 3).

### Questions
1. About the Weakness 1 I mentioned, I would appreciate it if the authors could explain more about the empirical choice of the unknown parameter  $\omega_{s,a}$ (since the empirical average over the samples $s_i^{\prime}$ from $\bar{P}(\cdot|s,a)$ forms an overestimation of $\omega_{s,a}$ as suggested by Proposition 3.4).
2. Some typos and notation clarity: (i) in Eq (12) it should be $\sum_{i=1}^Nv(s_i')$; (ii) the notion of $\omega_n$ and $\kappa_n$ is not pre-defined (even with subscript $s,a$). I suggest explicitly giving them a definition (as the parameter associated with the worst case transition kernel when the target function is $v_{P_n}^{\pi}$).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new method to learn robust policies by approximately simulating the worst-case transition probabilities. The method works for KL-divergence based sa-rectangular uncertainty set. A large set of numerical experiments is conducted.

### Strengths
* The authors conduct large-scale experiments.
* It is nice that we can combine the methods proposed in the paper with other (non-robust) RL algorithms.

### Weaknesses
 * The authors conduct large-scale experiments.
* It is nice that we can combine the methods proposed in the paper with other (non-robust) RL algorithms.

### weaknesses:
 * “The optimal policy”, “The worst-case transition probabilities”: some there are multiple optimal policies/worst-case kernels, I think that the authors should be more careful with the phrasing. I also don’t know what it means to “train” a transition kernel (last sentence of the paragraph after Eq. (7)), and I don’t know what is a “perfect value function” (paragraph before Eq. (14)). I list other inaccurate statements below. 

* The Theoretical results are very weak. Nothing new in Appendix A.1 (proof of Theorem 3.2), it is already in [A].

* The Theoretical results are only for KL divergence.

### Questions
1. Can the EWOK be modified to cope with other uncertainty sets than KL-based uncertainty?

2. For completeness, can you recall how to tune $\beta_{sa}$ the uncertainty radius, or give a precise reference for this?

3. Paragraph after Eq. (7): it is now well-recognized that the minimization problem from Eq. (7) is also an MDP, see for instance Section 3 in [1] or Section 4 in [2]. Can we use gradient-based method in this adversarial MDP to learn the worst-case transition probabilities?

4. Please properly introduce the parameter $\omega_{sa}$ and $\kappa_{sa}$ in Th 3.2.

5. Th 3.5 only states that the value converges to the robust value. It does not state that “the estimated kernel converges to the worst kernel”. Also why is \pi not indexed by the iteration, since you update it at every iteration?

[1] Vineet Goyal and Julien Grand-Clement. Robust Markov decision processes: Beyond rectangularity. Mathematics of Operations Research, 2022.

[2] Chin Pang Ho, Marek Petrik, and Wolfram Wiesemann. Partial policy iteration for l1-robust
Markov decision processes. The Journal of Machine Learning Research, 22(1):12612–12657, 2021

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
