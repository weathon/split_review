# Conservative Contextual Bandits: Beyond Linear Representations

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
\label{sec:abstract}




Conservative Contextual Bandits (CCBs) address safety in sequential decision making by requiring that an agent's policy, along with minimizing regret, also satisfies a safety constraint: the performance is not worse than a baseline policy (e.g., the policy that the company has in production) by more than $(1+\alpha)$ factor. 
Prior work developed UCB-style
algorithms in the multi-armed \citep{conservativeMAB} and contextual
linear \citep{conservative_linear_bandits} settings.
However, in practice the cost of the arms
is often a non-linear function, and therefore existing UCB algorithms are ineffective in such settings. 
In this paper, we consider CCBs beyond the linear case and develop two algorithms $\cSquareCB$ and $\cFastCB$, using Inverse Gap Weighting (IGW) based exploration and an online regression oracle. 
We show that the safety constraint is satisfied with high probability and that the regret of $\cSquareCB$ is sub-linear in horizon $T$, while the regret of $\cFastCB$ is \emph{first-order} and is sub-linear in $L^*$, the cumulative loss of the optimal policy. 
Subsequently, we use a neural network for function approximation and online gradient descent as the regression oracle to provide $\tilde{\mathcal{O}}(\sqrt{KT} + K/\alpha) $ and $\tilde{\mathcal{O}}(\sqrt{KL^*} + K (1 + 1/\alpha))$ regret bounds, respectively. 
Finally, we demonstrate the efficacy of our algorithms on real-world data and show that they significantly outperform the existing baseline while maintaining the performance guarantee.
\vspace{2ex}

\noindent \textbf{Keywords:} Safe Bandits, Neural Contextual Bandits, Non-linear Bandits, Constrained Bandits

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This authors consider Conservative Contextual Bandits with general value function class and develop two algorithms C-SquareCB and C-FastCB, using Inverse Gap Weighting and online regression oracles. They show that the safety constraint is satisfied with high probability (the performance is not worse than a baseline policy by more than $(1+\alpha)$ factor). They also show the regret for C-SquareCB is $\tilde O(\sqrt{KT}+K/\alpha)$ and the regret for C-FastCB is $\tilde O(\sqrt{KL^*}+K/\alpha)$, where $L^*$ is the cumulative loss of the optimal
policy. The efficacy of the proposed algorithms is validated on real-world data.

### Strengths
- The paper is clearly written and mostly easy to follow, with proof roadmap and intuition moderately provided.
- The provided solution nicely connects safe conservative bandits and contextual bandits with general functions class.
- Analysis is sound and rigorous. Numerical experiment is convincing.

### Weaknesses
As a paper that combines two established sub-fields in bandits, it is a bit unclear the novelty in algorithmic design and theoretical analysis. I would like to see authors provide and emphasize more detailed discussions if possible. In particular, what is your technical/methodological contribution compared to Kazerouni et al. (2017), Foster & Rakhlin (2020), Foster & Krishnamurthy (2021)? What are the challenges of adapting/extending their tools? From what I understand, the novelty appears in: a delicate safety criterion and a time-varying exploration schedule. The authors can add more if necessary.

Some clarification questions apart from the concern in Weaknesses:

- Data-dependent bound
  - When $L^*=O(1)$, it seems the regret bound becomes $\tilde O(\ln T)$. Is there any instance-dependent metric (similar to the mean gap in the stochastic MAB setting) hiding in the constant term?
  - $\gamma_t$ seems to be requiring the knowledge of not only $L^*$ but also each component that sums up to $L^*$. Would that be too strong?

- Experiments
  - Can you provide more details on how you set $\delta$ and tune hyperparameters? How do you run C-FastCB if the optimal cost is not known?

- Typos:
  - Algorithm 2 Line 8: Is there a term related with $\sqrt{\log\delta^{-1}}$ missing?
  - Line 836 missing a sqrt term consisting of $m_{\tau-1}$ and $\texttt{Reg}$.

### Questions
Some clarification questions apart from the concern in Weaknesses:

- Data-dependent bound
  - When $L^*=O(1)$, it seems the regret bound becomes $\tilde O(\ln T)$. Is there any instance-dependent metric (similar to the mean gap in the stochastic MAB setting) hiding in the constant term?
  - $\gamma_t$ seems to be requiring the knowledge of not only $L^*$ but also each component that sums up to $L^*$. Would that be too strong?

- Experiments
  - Can you provide more details on how you set $\delta$ and tune hyperparameters? How do you run C-FastCB if the optimal cost is not known?

- Typos:
  - Algorithm 2 Line 8: Is there a term related with $\sqrt{\log\delta^{-1}}$ missing?
  - Line 836 missing a sqrt term consisting of $m_{\tau-1}$ and $\texttt{Reg}$.

### Soundness
4

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
3

### Summary
The paper studies the conservative contextual bandit problem, where the goal is to minimize the regret as in classical contextual bandit problems and, with high probability, be competitive against a baseline policy. Importantly, the cost functions are not assumed to be linear in the contexts. This extends previous study of conservative bandit problems beyond the multi-armed setting and the contextual linear setting. 

The two proposed algorithms, C-SquareCB and C-FastCB, combine the inverse gap weighting based exploration and online regression oracles (e.g. function approximation using neural network+ gradient descent), and achieve regret which is sublinear in the horizon T or sublinear in the optimal loss L*, while being (1+alpha)-competitive against the baseline with high probability. Experiments using real world data show that C-SquareCB and C-FastCB have smaller regret compared to algorithms for contextual linear bandit problems, and are more competitive against the baselines.

### Strengths
The paper is overall well written, with clearly presented problem formulations, algorithms and results. The setup considered fills in the gap of current conservative bandit literature, and the proposed algorithms have provably sublinear (in T or L*) regret while being (1+alpha) competitive against the baseline. Experiments further demonstrate their superior performance as compared to algorithms designed for conservative linear contextual bandits and for classical settings without baselines.

### Weaknesses
The proofs/assumptions may lack rigor. In particular, the proofs cite results in other works without carefully checking the assumptions under which those results hold. For instance, in line 914-915, lemma 2 in Foster & Rakhlin (2020) is invoked. If my understanding is correct, that lemma requires Assumption 3 to hold for all possible sequences. Nevertheless, in line 1736-1737, Assumption 3 is only proved to hold with high probability. This discrepancy raises concerns about the validity of the theoretical guarantees, specifically whether the high probability result is sufficient to invoke the lemma which requires the assumption to hold for all sequences, not just with high probability.

One contribution of the work is to use neural network for function approximation to deal with the non-linearity in the cost functions. However, to achieve the stated performance as in Theorem 5.2, the width (and thus the number of parameters) of the neural network is Omega(poly(T)), which might be too large for long-horizon problems, making the algorithms less practical. The specific polynomial dependence on T is not explicitly stated, but the requirement of a polynomial width in T makes the algorithm computationally expensive and potentially unsuitable for real-world applications with long time horizons. The paper should provide a more detailed analysis of the computational cost associated with the network width.

The paper could benefit from more detailed discussion on the significance of the regret bounds in Theorem 3.1 and Theorem 4.1. In particular, it appears that for any algorithm which has regret upper bounded by alpha * y_l * t, under Assumption 2, equation (2) is automatically satisfied. Some discussions on the range of parameters might help the readers better understand the significance of the results. The paper does not adequately address the trivial policy that always selects the baseline action, which also satisfies the performance constraint but does not guarantee sublinear regret. The implications of this observation on the practical relevance of the proposed algorithms should be discussed further.

### Questions
In Definition 2.2, line 124, alpha is chosen to be <1. I’m wondering if this is just a simplifying assumption, or there is difficulty in extending the results of this paper to settings where alpha>=1? 

In line 160, what is H in the ``inf’’?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes algorithms for the conservative contextual bandit problem under a non-linear reward model.  The proposed algorithms apply IGW exploration based on an online regression oracle, enabling the selection of either an exploratory or a conservative policy based on a safety condition.  The proposed algorithms achieve sub-linear regret with respect to the total time step $T$, and its performance is supported by numerical experiments.

### Strengths
- The proposed algorithm introduces the first conservative contextual bandit algorithm for a general reward model by adapting the assumption of access to a regression oracle and leveraging the IGW algorithm, which previously applied only to linear reward models. The authors also present regret analysis for the algorithm. Although I was unable to rigorously verify all proofs, the results appear consistent, achieving a regret bound comparable to that of the linear case.  
- The methodology is illustrated with examples using an online gradient descent regression oracle and feed-forward neural networks. Real-world data experiments further support the algorithm’s performance.

### Weaknesses
1. This paper introduces multiple algorithms and theoretical results for the conservative contextual bandit problem with a general non-linear cost function. Consequently, much of the main content is focused on the operation of the algorithms, assumptions required for the theoretical results, and descriptions of the outcomes, with limited discussion of the technical challenges arising from handling non-linear cost functions in CCB and how these challenges were addressed. It seems that Algorithm 1 and Algorithm 2 are almost identical aside from the use of different regression oracles. Moreover, if, as the authors state, Algorithm 2 has a tighter regret guarantee than Algorithm 1, it may be beneficial to focus more on Algorithm 2, detailing the challenges and technical novelties associated with it.

2. The main theorem statements lack completeness. For example, in the statement of Theorem 3.1, there is no indication of how to set the input parameter $\gamma$ for the algorithm to achieve the stated regret bound. Similarly, Theorem 5.1 could benefit from more precise language rather than vague expressions like “appropriate choice of parameter”. Additionally, based on my understanding, the exploration parameter $\gamma_i$ in Algorithm 2 appears to depend on $\eta_i$ (line 1218). However, $\eta_i$ in turn depends on $L_i^*$, which is the true cost value of the optimal action and unknown to the agent. Further clarification is needed on how $\gamma_i$ is determined.

3. The description for experiment reproducibility is lacking. Additional information, such as how the hyperparameters for each algorithm are set, would be helpful.

### Questions
1. In Algorithm 1, if the safety condition is not met, the baseline policy ($b_t$) is used, and its noiseless cost $h(x_{t,b_t})$ is observed. However, this data is not used in the oracle. Since the baseline policy provides high-quality data with zero noise, why is it not utilized? Would using this data yield a better estimator? Additionally, in the linear cost case (Kazerouni et al., 2017), a noisy reward is observed for actions chosen by the baseline policy (e.g., $y_{t,b_t}$). What would happen if, in this paper’s setting, the algorithm observed $y_{t,b_t}$ instead of $h(x_{t,b_t})$?

2. The algorithm introduced in Section 4 is referred to as having a “first-order regret bound.” Why is it called “first-order”? How would second-order and third-order bounds be defined?

3. When defining the Neural Tangent Kernel (NTK) matrix, is $x_t$ the feature chosen by the algorithm at time $t$? If so, it seems unclear how the NTK can be defined given that the chosen features are unknown prior to starting the algorithm. It may be better to define the NTK matrix based on the context of all actions at all times, as in Zhou et al. (2020). Additionally, the regret bounds in Theorems 5.1 and 5.2 are independent on $\lambda_0$. Why is this assumption necessary, and does it not affect the regret bound?

4. Most literature on Neural Tangent Kernel-based neural bandits shows a dependency of regret on the effective dimension of the NTK. In contrast, the proposed paper presents a dependency on $K$ instead of the effective dimension. Could you explain what enables this distinction?

5. In the Neural Conservative Bandit, the activation function in the first-order bound changed from a smooth & Lipschitz function $\phi$ to a sigmoid function $\sigma$. What are the differences between $\phi$ and $\sigma$?

6. There do not appear to be terms related to the perturbation constant or the number of ensemble $S$ in the regret bound. Do these quantities not affect the regret? Additionally, how are these hyperparameters chosen in the experiments, and how do they impact performance?

---

**[Typo]**

- line 295: “Line 7” should be “Line 8.”

### Soundness
3

### Presentation
2

### Contribution
2
