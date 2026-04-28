# ACTIVE: Offline Reinforcement Learning via Adaptive Imitation and In-sample $V$-Ensemble

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Offline reinforcement learning (RL) aims to learn from static datasets and thus faces the challenge of value estimation errors for out-of-distribution actions. The in-sample learning scheme addresses this issue by performing implicit TD backups that does not query the values of unseen actions. However, pre-existing in-sample value learning and policy extraction methods suffer from over-regularization, limiting their performance on suboptimal or compositional datasets. In this paper, we analyze key factors in in-sample learning that might potentially hinder the use of a milder constraint. We propose Actor-Critic with Temperature adjustment and In-sample Value Ensemble (ACTIVE), a novel in-sample offline RL algorithm that leverages an ensemble of $V$-functions for critic training and adaptively adjusts the constraint level using dual gradient descent. We theoretically show that the $V$-ensemble suppresses the accumulation of initial value errors, thereby mitigating overestimation. Our experiments on the D4RL benchmarks demonstrate that ACTIVE alleviates overfitting of value functions and outperforms existing in-sample methods in terms of learning stability and policy optimality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address the overestimation problem of offline RL methods that learn in-sample value functions to avoid querying out-of-distribution samples. The main idea is (i) to learn ensemble of V functions and use clipped V function for learning V functions and (ii) use automatic tuning of hyperparameter used for in-sample value learning such as quantile regression. Arguments for introducing the idea are strong. Several ablation/analysis are provided to support the claims in the paper. Experiments are conducted on D4RL benchmark.

### Strengths
The main strength of this paper is that the paper does not have any big flaw and does not make any big mistake. Writing is clear, motivation is clear, intuition is clear, and the results look okay. The idea of learning ensemble of value functions has been very popular in offline RL context and also clipped Q learning is also widely-used, so the idea of using it for regularizing IQL-like method is solid.

### Weaknesses
- The main problem of this paper is that it's not clear how important the problem this paper aims to address, or the importance of such problem is not clearly evidenced & presented in the writing, mainly because D4RL is quite saturated benchmark at this point and it's not clear how the observation / results in this benchmark would transfer to other scenarios.
- It's not clear the motivating overfitting problem can be generally observed in diverse domains or it is only happening on D4RL tasks. Motivating figures could be provided on more tasks / domains to support that overfitting is a common problem across various scenarios. More results on different tasks from different benchmarks such as NeoRL or visual offline RL benchmarks can be a plus.
- Weak performance compared to MSG is not clearly justified to me; if that is from not using CQL-like regularizer, can ACTIVE be better if it incorporates similar regularizer?
- It could be nice to make tables be more self-contained as far as possible. For instance, make it clear that what -I and -S means in each caption, or make it clear what $m$ means in Table 1.

### Questions
See Weaknesses.

### Soundness
3

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
3

### Summary
The paper focuses on resolving the problem of overregularization induced by in-sample learning methods in an offline RL setting. It provides a motivating experiment to demonstrate that existing approaches like IQL could still suffer from overestimation in the late learning stages. The proposed method differs from existing IQL algorithms mainly in two ways: 1) it introduces an ensemble to learn the value function; and 2) it introduces an entropy constraint on the policy learning, which is further reformulated by Lagrangian and solved by dual gradient descent. Empirical results on commonly used offline RL datasets are presented to verify the effectiveness of the proposed algorithm.

### Strengths
1. The paper studies an important topic.
2. The paper presents promising empirical results. 
3. The paper explains its main algorithm clearly.

### Weaknesses
The main weaknesses are as follows. 

Definition of Over-Regularization: The paper repeatedly emphasizes that existing approaches suffer from over-regularization induced by in-sample constraints, while the proposed method can mitigate this. However, the term "over-regularization" is never clearly defined. Intuitively, it might imply that the learned action values are somewhat underestimated due to in-sample constraints. Yet, it is confusing that Section 4.1 claims that existing algorithms like SQL still overestimate. If overestimation is an issue, doesn’t this suggest that there is insufficient regularization? And, isn't it simpler to bring in methods to mitigate overestimation (there were already many methods proposed for this)? 

Theoretical Clarity: The theoretical result appears confusing. Theorem 4.5 states that the initial error can be penalized, but it is unclear how this penalization of initial error relates to preventing overestimation.

Choice of Competitors for Empirical Testing: Figure 1 omits tests on the original IQL and CQL. Additionally, a fair comparison seems to be missing; the proposed approach should ideally be compared with in-sample softmax by Chenjun Xiao et al., as cited by the authors. This paper directly bootstraps from in-sample actions and also incorporates entropy regularization, and it was proved to converge to an optimal entropy-regularized policy on the empirical MDP defined by offline dataset.

Effectiveness of the Proposed Method: Line 286 states, "...but cannot completely solve the overregularization problem." However, it remains questionable whether even with the proposed dual gradient descent method, this problem can be fully resolved.

Need for Ablation Study: The paper should include an ablation study on the use of the ensemble value function and dual gradient descent to carefully verify their effect and necessity.

### Questions
see above.

### Soundness
2

### Presentation
2

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
This paper addresses the observed overfitting issue of V-functions in offline reinforcement learning. Specifically, the authors claim that a V-function may overfit to unstable overestimates in the target Q-values, which can, in turn, adversely impact the learning of both the actor and critic. The authors propose two primary techniques to mitigate this issue:

**First Technique: IVE (V-function Ensemble and Pessimistic Estimation).** To mitigate overfitting and prevent exploding Q-values, the authors propose maintaining an ensemble of V-functions and using their minimal estimate as the target during policy improvement:

$$L\_V^f(\psi\_i) = \mathbb{E}\_{(s,a)\sim D} [f(Q\_{\hat{\theta}} - V\_{\psi\_i}(s))]$$ 

$$L\_Q(\theta) = \mathbb{E}\_{(s,a,s')\sim D} [ \Big(r(s,a) + \gamma \min\_i V\_{\psi_i}(s') - Q\_\theta(s,a)\Big)^2]$$

, where $f$ is a general distance function. Seems the author use $\alpha$-divergence, as implied in Algorithm 1 (ACTIVE) on page 6. 

The intuition behind this V-function ensemble is that for unstable or highly overestimated target Q-values, there is likely to be at least one V-function instance in the ensemble that does not fit this overestimated target well. This imperfect approximation helps prevent catastrophic overestimation.

**Secondly, ACT (Adaptive Cloning Temperature)**

The authors propose an adjustment to the advantage function used in policy extraction, building on modifications to the vanilla Advantage-Weighted Regression used in SQL and IQL:

$$\hat{A}(s,a) := Q\_{\hat{\theta}}(s,a) - \mathbb{E}^c \[V\_{\psi_i}\](s)$$

with $\mathbb{E}^c$ denotes the c-th quantile of the V-predictions. Besides, the author conduct policy extraction on both Q-function and A-function, which is different to IQL and SQL.

### Strengths
1. This paper is well-organized. Presenting work with two distinct techniques can be challenging, yet this paper does so effectively. The descriptions of each technique are clear, with a justification provided for the first technique, IVE.

2. It is a noteworthy finding that sota offline RL algorithms, such as SQL and IQL, still encounter overestimation issues in certain scenario. The introduction of a V-function ensemble to mitigate this problem yields incremental improvements, as demonstrated in Table 2 of the experiments. I also observed that the reproduced IQL results are slightly better than those in the original paper, while the SQL results are slightly lower—both of which align with expectations based on my own experience reproducing these algorithms in my research.

### Weaknesses
**(Minor)** **Inconsistent naming of techniques**. The names of the proposed techniques are inconsistent, which may confuse readers. The second technique, ACT, is mentioned under various names, including *automating likelihood adjustment*, *adaptive cloning temperature*, and *adaptive imitation*. Maintaining a single, consistent name for each technique would improve clarity.

**(Minor) Insufficient theoretical analysis for V-function ensemble.** The theoretical analysis supporting the V-function ensemble feels somewhat lacking. My understanding is that the theorem attempts to show that recursively expanding the pessimistic target could provide certain benefits:
$$Q = [1 + \gamma + ... + \gamma^t]r + (\Omega - B) \gamma [1 + \gamma + ... + \gamma^t] + \mathcal{O}$$
where B is some form of $V_\text{var}$, and $\Omega$ is a form of initial error. I believe this is not entirely new to the RL community. Additionally, the analysis lacks a convergence guarantee to ensure that such a recursive expansion can be reliably conducted.  Besides, the assumption 4.3 that $\pi_\text{imp} \propto \dfrac{|f'(Q(s,a) - V^*(s))|}{|Q(s,a) - V^*(s)|}$ is fixed throughout the learning process, seems infeasible. Since we are continuously updating the Q-function during Q-learning, it would be challenging to hold this assumption constant.

### Questions
I tend to rate this paper as “marginally below the acceptance threshold” for the following reasons:

1. **V-function ensemble in offline RL**: Introducing a V-function ensemble for offline RL is somewhat interesting. Although V-function ensembles are new to me, they appear conceptually similar to existing Q-function ensembles, such as REM and other methods with pessimistic estimates (e.g., SAC-N, PBRL, EDAC, VPQ).
2. **Insight on overestimation in sota Offline RL**: This paper makes an interesting observation that sota offline RL algorithms still encounter overestimation issues in some scenarios. While the authors refer to this as “overfitting,” it is, in effect, overfitting to unstable overestimated Q-values.
3. **Clarity of contributions.** The contributions of this paper feel somewhat overshadowed by an abundance of technical details. The modifications proposed by this paper include:
    1. *Equations (6) and (7)*: A V-function ensemble designed to approximate stable Q-targets while avoiding unstable overestimated values,
    2. *Equation (6)*: Using a suitable  f-divergence for mapping the V-function to the Q-value of the best action in the dataset, and
    3. *Equations (14) and (15)*: Extracting the policy based on the learned Q-function, V-function, and a quantile.
    
    Each of these components would benefit from comprehensive analysis, but in this paper, they are presented in a tightly condensed manner aimed at deriving a sota offline RL algorithm. While I respect the author’s effort, this approach makes it challenging to appreciate each individual contribution.

In summary, I find the core idea of this paper less compelling, with limited new insights or utility in the analysis. The primary contribution appears to be the development of a potentially strong offline RL algorithm, rather than a well-motivated solution for offline RL. Nevertheless, I rate this paper “marginally below the acceptance threshold” to avoid letting my personal preferences bias the review of this well-executed experimental study.

Question for the author: I believe Equation (8) may be unnecessary, as it could potentially confuse readers, especially when read alongside Equations (14) and (15). Right?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes an offline reinforcement learning algorithm ACTIVE that can mitigate the over-regularization problem of existing in-sample learning schemes. This paper first demonstrates through experiments that using a higher $\tau$ in IQL (or using a lower $\alpha$ in SQL) will lead to unstable estimates during the training process. And they demonstrate theoretically that V-ensemble can mitigate value overestimation by suppressing the accumulation of initial value errors, and experimentally demonstrates that ACTIVE can mitigate the overfitting of the value function and thus outperforms existing in-sample methods.

I have reviewed this manuscript submitted to NeurIPS 2024, and the authors have modified the manuscript in response to my comments and added comparison experiments with some ensemble algorithms, and these modifications address most of my questions.

### Strengths
1. This method has reasonable motivation and theoretical basis.
2. This method could help address the issue of in-sample value learning and policy extraction methods performing poorly on suboptimal or compositional datasets.
3. The experiments demonstrate that the method achieves some empirical improvements.

### Weaknesses
1. The innovation of this paper is moderate. As far as I know, the use of ensemble tricks to stabilize value estimation has been widely used in the RL field. 
2. The algorithm introduces two new superparameters $c$ and $\mathcal{H}$, which are somewhat sensitive according to Figure 4 and Figure 5. Especially $\mathcal{H}$, it needs to be adjusted for specific datasets.

### Questions
1. Besides the run time, can you provide a comparison of the algorithm's parameters?

### Soundness
2

### Presentation
3

### Contribution
2
