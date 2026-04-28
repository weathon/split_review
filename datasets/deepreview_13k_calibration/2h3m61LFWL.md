# Value-Biased Maximum Likelihood Estimation for Model-based Reinforcement Learning in Discounted Linear MDPs

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
We consider the infinite-horizon linear Markov Decision Processes (MDPs), where the transition probabilities of the dynamic model can be linearly parameterized with the help of a predefined low-dimensional feature mapping. While the existing regression-based approaches have been theoretically shown to achieve nearly-optimal regret, they are computationally rather inefficient due to the need for a large number of optimization runs in each time step, especially when the state and action spaces are large.
To address this issue, we propose to solve linear MDPs through the lens of Value-Biased Maximum Likelihood Estimation (VBMLE), which is a classic model-based exploration principle in the adaptive control literature for resolving the well-known closed-loop identification problem of Maximum Likelihood Estimation. We formally show that (i) VBMLE enjoys $\widetilde{O}(d\sqrt{T})$ regret, where $T$ is the time horizon and $d$ is the dimension of the model parameter, and (ii) VBMLE is computationally more efficient as it only requires solving one optimization problem in each time step. In our regret analysis, we offer a generic convergence result of MLE in linear MDPs through a novel supermartingale construct and uncover an interesting connection between linear MDPs and online learning, which could be of independent interest. Finally, the simulation results show that VBMLE significantly outperforms the benchmark method in terms of both empirical regret and computation time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies reinforcement learning (RL) on MDP with linear decomposition. The authors proposed a MLE-based algorithm to directly estimate the MDP, unlike previous approaches which need to solve a regression problem on the estimated value functions and need to construct a confidence set of the parameters of the MDP. They also provided experiments to show the superiority of the proposed algorithm compared with existing baselines, especially on the computational time aspect.

### Strengths
The intuition of the proposed approach is very clear. The authors successfully showed the strengths of the proposed algorithm from both the theory side and experiment side. The proof is also technically sound.

### Weaknesses
My main concern is the significance of this work given the works about RL with general function approximation. The main novelty of this work is an MLE-based approach with an additional optimal value function bias term. However, similar approaches have already been considered and analyzed in previous works about RL with posterior sampling [1,2]. In detail, [2] analyzed RL with general function approximation, and the proposed algorithm (Algorithm 3 in [2]) is nearly the same as the algorithm proposed by the authors. The only difference is due to the problem setting (e.g., discounted v.s. episodic, frequentist vs bayesian). Given the fact that the MDP instance considered in this work is just a special case of the MDP instances considered in [2], I can not find enough contribution or novelty of this work.

[1] Zhang, Tong. "Feel-good thompson sampling for contextual bandits and reinforcement learning." SIAM Journal on Mathematics of Data Science 4.2 (2022): 834-857.

[2] Zhong, Han, et al. "Gec: A unified framework for interactive decision making in mdp, pomdp, and beyond." arXiv preprint arXiv:2211.01962 (2022).

Meanwhile, the presentation of this paper is no clear enough, especially for some key points of the theoretical claims and experiment implementations. For example, 

1. The big-O notation in this work is not well-defined. In Theorem 2, the authors used a big-O notation to propose the regret of their proposed algorithm, which only depends on terms $T, \gamma$ and $d$. However, from their proof (e.g., (97)) which is used to bound the regret) the regret should also depends on $1/p_{min}$, which is the smallest transition probability $p(s'|s,a)$. The first issue is that, $1/p_{min}$ could be very large, which could make the regret bound derived in Theorem 2 very loose. The second issue is that, the regret bound of UCLK does not depend on $1/p_{min}$, and the authors did not mention or compare them. Therefore, I suggest the authors to revise their big-O notation definition and give a detailed comparison of regret between their algorithm and UCLK.

2. The term 'linear MDP' used in this paper, which refers to MDP instance whose transition probability can be decomposed by a feature $\phi(s'|s,a)$, is not correct enough, as previous works [3,4] claimed such an instance as 'linear kernel MDP' or 'linear mixture MDP'. 

[3] Dongruo Zhou, Jiafan He, and Quanquan Gu. Provably efficient reinforcement learning for discounted mdps with feature mapping. In International Conference on Machine Learning, pp.
12793–12802. PMLR, 2021b.

[4] Dongruo Zhou, Quanquan Gu, and Csaba Szepesvari. Nearly minimax optimal reinforcement learning for linear mixture markov decision processes. In Conference on Learning Theory, pp. 4532–
4576. PMLR, 2021a.

3. There also lack some experiment implementation details. From the description of the proposed algorithm (at (14)), the parameter $\theta$ should be selected from a set $\mathbb{P}$, which requires the parameter $p_{min}$. The authors did not mention how to find or estimate such a quantity in their experiment.

### Questions
See Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The primary focus of this paper revolves around the learning of discounted linear Mixture Markov Decision Processes (MDPs). Diverging from previous frameworks, the author introduces the VBMLE algorithm, which directly learns the parameterized transition without the need for a value-target regression process. This innovative algorithm attains a regret bound of $O(d\sqrt{T}/(1-\gamma)^2)$ with reduced computational complexity. Additionally, the empirical results provide strong evidence confirming the effectiveness of the proposed algorithm.

### Strengths
1. The VBMLE algorithm eliminates the value-target regression process and achieves a regret bound of $O(d\sqrt{T}/(1-\gamma)^2)$, resulting in reduced computational complexity.

2. The empirical results offer compelling evidence that affirms the effectiveness of the proposed algorithm.

3. Exploring the connection between online learning and the analysis of regret can be an independent and valuable area of interest.

### Weaknesses
1. There exist some error in the related works. The linear MDP setting is first introduced in the Jin et al., 2020 [1], which assume the transition probability satisfies $P(s'|s,a)=\langle  \theta(s,a),\mu(s')\rangle$. In comparision, this work focuse on the linear mixture MDPs setting that $P(s'|s,a)=\langle  \phi(s'|s,a),\theta\rangle$, which is first introduced in Ayoub et al.,2020 [2] and Zhou et al., 2021[3]. Providing accurate references and explanations for these concepts is essential to avoid any confusion or misinterpretation.

2.In contrast to previous work, this study relies on prior knowledge of the zero transition set $P_0$ and assumes a lower bound for non-zero transition probabilities. While these assumptions are made to support the VBMLE algorithm, it's important to recognize that they may restrict the broader applicability of the algorithm. Specifically, the dependence of the regret bound on this minimum probability $p_{min}$ is not explicitly stated, which could be a significant factor in practical applications. The assumption about knowing the zero transition set $P_0$ is also quite strong and not realistic in many scenarios.

3. Regarding computational complexity, solving the optimization problem outlined in equation (10) may still pose challenges in terms of efficiency. The non-concavity of the objective function means that standard convex optimization techniques cannot be directly applied, and finding a global optimum could be computationally expensive. The paper does not provide a detailed analysis of the practical computational cost of this step, nor does it discuss approximation methods that could be used.

### Questions
1. The standard Azuma-Hoeffding Inequality requires $|X_t-X_{t-1}|\leq c_t$ and set $M_t=\sum_{i=1}^t c_t^2$. In Lemma 3, it appears that the Azuma-Hoeffding Inequality is being extended to handle adaptive $c_t = X_t - X_{t-1}$, which is indeed a notable extension. Further clarification or explanation from the author on this extension would be beneficial.

2. In the experimental section, it is necessary to explicitly state the chosen dimensions $d$. Additionally, the experiments are conducted on a relatively small state-action space. Under this situation, tabular method may also have good performance. Conducting experiments with larger state-action spaces or comparing the results with tabular methods would indeed provide valuable insights into the algorithm's scalability and efficiency.

3. The author misses some related work about the linear mixture MDP. For instance, He et al., 2021 [1] utilized Bernstein-type concentration properties to improve results in Cai et al., 2020 [2] and attained a near-optimal regret guarantee. Including these references would enhance the completeness of the related works section.

[1] Near-optimal Policy Optimization Algorithms for Learning Adversarial Linear Mixture MDPs

[2]  Provably efficient exploration in policy optimization.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the infinite-horizon linear mixture MDPs with a low-dimensional feature mapping. This paper first proposes a different Value-Biased Maximum Likelihood Estimation based algorithm, which is more computational efficient than previous work. Then this paper provides a theoretical regret bound. In addition, simulation results are provided to validate that VBMLE outperforms previous methods in terms of both empirical regret and computation time.

### Strengths
1. This paper considers another algorithm to estimate models and find the optimal policy under linear mixture MDPs with a low-dimensional feature mapping and provides theoretical regret bound.

2. Simulation results are provided to validate theoretical results.

### Weaknesses
1. Assumption 1 assumes the lower bound of non-zero transition probabilities to be $p_{min}$. I understand there always exists such a $p_{min}$, but the authors should have discussions on it. I check the proofs that there should be a term like $\frac{1}{p_{min}}$ in regret bound which is hidden by $\mathcal{O}$ notation. However, $1/p_{min}$ can be quite large, even larger than $d$ and $\frac{1}{1-\gamma}$. So in small $p_{min}$ regime, the algorithm is not efficient, and the regret bound result is worse than UCLK [1], which makes the result not good enough. In addition, I suggest to keep $p_{min}$ in the regret bound.

2. This paper claim their better computation efficiency over UCLK [1] because UCLK requires computing an estimate of the model parameter for each state-action pair in each iteration, but it is also hard to solve VBMLE, which is non-convex. Could the authors provide the computation complexity to solve VBMLE, and compare the complexity with the one of UCLK? In addition, for theoretical analysis, the author assume an oracle returning optimal estimators for VBMLE. What if an empircal optimization algorithm is adopt to estimate the parameter? For example, the estimator $\hat{\theta}$ is no longer the optimal one but may have some errors, say $\|\hat{\theta}-\theta^{MLE}\| \leq \epsilon$ for some $\epsilon$.


3. In related work, the linear MDPs in Jin et al., (2020) is different from the model in this paper (which is also called linear mixture MDPs in some literature). I think it will be better if the authors can discuss some other RL works using MLE to estimate transition kernels (For example, FLAMBE [3] and it follow-ups under MDPs and POMDPs) and how the analysis of these work is different from this paper.

Minor

4. I believe the presentation of the this paper can be improved a lot. Many notations and concepts come without definitions and explanations, which makes it hard to follow. Also, there are many typos.

Just to name a few,

Page 3: "All of their algorithm achieve a regret bound of $\mathcal{O}(d\sqrt{H})$", miss $T$; no definition of $\gamma$.

Page 4: no definition of $\pi_{\infty}^{MLE}$.

Page 6:  Eq. (16) "$.... +\sum_{i=1}^{t-1}z_i$". Eq. (21): "$\hat{p}_{min}$".

### Questions
1. In section 6, I am a little confused about " Notably, due to UCLK learning distinct parameter for each state-action pair, ...." . Why is the vector $\theta$ dependent on $(s,a)$? 

2. The authors indicate that VBMLE employs this biasing method to handle the exploration-exploitation trade-off. Could the authors explain more in details how to handle the exploration-exploitation trade-off?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to apply the value-biased maximum likelihood estimation (VBLMLE) principle to solve linear MDP problems. The authors show that the VBMLE method can achieve a $\widetilde{O}(d\sqrt{T})$ regret.  They also demonstrate the proposed method is computationally more efficient than existing methods like UCLK through numerical experiments.

### Strengths
* The paper is overall well-written and easy to follow.

* The proposed method is intuitive and well-motivated. The objective for VBMLE clearly exhibits an exploration-exploitation tradeoff.

* The section of theoretical analysis is technically solid, unveiling interesting connections between the proposed methods and the domain of online learning.

### Weaknesses
 * My main concern is the computational efficiency of the VBMLE method. The authors claim VBMLE method is computationally efficient. But in each time step, VBMLE needs to solve a hard optimization problem (Equation (10) in the paper). And as $t$ gets larger, the problem seems increasingly difficult to handle. The authors say they handle the optimization problem by "incorporating the value iteration into the optimization subroutine". This argument is vague and further explanations are needed. In fact, from the results of numerical experiments, we may find that the VBMLE method needs around 40s to perform one single iteration when solving a small-scale MDP problem ($|\mathcal{S}|=15,|\mathcal{A}|=4$). Although this result is far better than the UCLK algorithm, I feel that the proposed algorithm cannot be called computationally efficient (especially because of its online nature).

* The empirical evaluation is weak. First, the authors only test VBMLE on MDPs with small state/action space. In fact, such tabular problems can be solved without the use of linear function approximation. Second, the authors only compare the proposed method with the UCLK baseline, while there already exists an improved version called $\text{UCLK}^+$ that can achieve near-minimax regret. Also, I think the authors should explain how they solve the inner optimization problem in actual numerical experiments. If there is a problem with page limits, the authors should include the explanations in the Appendix (for example, Appendix C).

* Some notations appear without proper definition. For example, the $\pi_\infty^{\text{MLE}}(s)$ in Section 4.

### Questions
* The ideas behind the VBMLE remind me of model-based RL via the optimistic approach ([2]). Can the authors give a brief discussion about any potential connections between the two approaches?

[2] Jaksch, Thomas, Ronald Ortner, and Peter Auer. "Near-optimal Regret Bounds for Reinforcement Learning." Journal of Machine Learning Research 11 (2010): 1563-1600.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
