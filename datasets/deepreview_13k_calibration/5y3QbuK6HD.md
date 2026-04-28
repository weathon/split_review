# Burning RED: Unlocking Subtask-Driven Reinforcement Learning and Risk-Awareness in Average-Reward Markov Decision Processes

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
Average-reward Markov decision processes (MDPs) provide a foundational framework for sequential decision-making under uncertainty. However, average-reward MDPs have remained largely unexplored in reinforcement learning (RL) settings, with the majority of RL-based efforts having been allocated to episodic and discounted MDPs. In this work, we study a unique structural property of average-reward MDPs and utilize it to introduce \emph{Reward-Extended Differential} (or \emph{RED}) reinforcement learning: a novel RL framework that can be used to effectively and efficiently solve various subtasks simultaneously in the average-reward setting. We introduce a family of RED learning algorithms for prediction and control, including proven-convergent algorithms for the tabular case. We then showcase the power of these algorithms by demonstrating how they can be used to learn a policy that optimizes, for the first time, the well-known conditional value-at-risk (CVaR) risk measure in a fully-online manner, \emph{without} the use of an explicit bi-level optimization scheme or an augmented state-space.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies a class of average-reward reinforcement learning problems, which includes risk-sensitive RL as special case.  The main contribution is a new framework called Reward-Extended Differential (RED) RL, which leverages structural properties of average-reward RL. RED RL can be used to devise RL algorithms for a rather broad range of objectives admitting some notion called “subtask”. In particular, the paper showcases the efficacy of this framework in the design of risk-averse RL algorithms under the CVaR risk measure, and this appears to be main motivation behind RED RL. The key benefit of the new framework here would be to avoid bi-level optimization or state-space augmentation that appear in the existing RL algorithms under CVaR criterion.

### Strengths
The paper studies an interesting problem in average-reward RL, which leverages a structural property that is specific to average-reward MDPs. The introduced framework appears interesting in its generic form, although its presentation in the paper is done in a rather high and abstract level. I found its application to CVaR RL quite interesting. In addition, that it removes the need to solve bi-level optimization problems explicitly is definitely a plus.  

The paper is mostly well-organized and well-written. I have a couple of minor comments about writing and organization that I defer until the next section. Whenever applicable, the paper uses some figures to illustrate some concept, which proved quite helpful. 

The paper includes numerical experiments, which is a positive aspect. The two domains used for the experiments sound interesting and relevant to showcase the framework.

### Weaknesses
Main Comments:
-
- One main comment is regarding the assumption. In view of statements in line 123-124, it appears to me that effectively a unichain assumption is made both for prediction and control. This is a significant limitation, as many real-world systems do not satisfy this condition. The paper should explicitly discuss the implications of this assumption and how it might affect the applicability of the proposed framework. Specifically, the analysis relies on the existence of a unique stationary distribution, which is not guaranteed without the unichain assumption. This needs to be clarified and potentially addressed with alternative assumptions or methods.

- As a weak aspect, the presented framework only is shown to enjoy asymptotic convergence (in the tabular case). While asymptotic convergence is a starting point, it is not sufficient for practical applications. The lack of non-asymptotic bounds makes it difficult to assess the performance of the algorithm in finite time. This is a critical gap, as it is not clear how quickly the algorithm converges to the optimal solution, or how the convergence rate depends on the problem parameters. The paper should discuss the possibility of deriving non-asymptotic bounds as a future direction.

- Regarding CVaR RL, use of an augmented state-space is mentioned as a standard technique. Of course, it is clear that we lack interest in extending state-space – especially if there is some workaround – for the classical performance bounds that deteriorate as the size of state-space grows. However, it is worth remarking that an “augmented but highly structured” state-space is not necessarily a weak aspect if one could leverage the underlying structure. Could you explain whether this is the case for CVaR RL? Specifically, are there known methods that exploit the structure of the augmented state space in CVaR RL to improve computational efficiency or sample complexity? If so, the paper should discuss how the proposed approach compares to these methods in terms of both theoretical guarantees and practical performance.

- In Section 5, Equation 19: could you clarify what the choice of function $f$ is. The paper should provide a more detailed explanation of the subtask function, including its motivation and properties. It is not clear how this function is chosen, and what impact its choice has on the performance of the algorithm. A more rigorous justification of this choice is needed.

- As a general comment, I wonder whether RED performs simultaneous learning of multiple subtasks without any sacrifice? If not, it is not highlighted enough in the paper (or maybe I miss something). The paper should explicitly state any trade-offs or limitations associated with learning multiple subtasks simultaneously. It is important to understand whether there are any performance penalties or additional computational costs associated with this approach.

- Subtask may bring some confusion because of its use as a standard terminology in hierarchical RL terminology. Also, I do not think that this choice of naming effectively reflects what it actually serves. Other candidates?

- I found the literature review part rather week. Admittedly, there is a rarity of prior work dealing with learning multiple goals/objectives in average-reward MDPs. However, in other MDPs settings and bandits – that are obviously more straightforward to analyze – there might exist a relatively richer literature. Further, one key contribution of the paper falls into the realm of risk-sensitive RL. It is therefore expected to see a better coverage of the related literature (and for discounted and episodic settings). The paper should discuss relevant work in risk-sensitive RL, including both theoretical and empirical results, and how the proposed approach compares to existing methods.

- The preliminary on average-reward MDPs and RL is rather long. Despite less work on them comparatively, they are standard settings and notions for a venue such as ICLR. I suggest Section 3.1 to be compressed to that the space in the main text could be used for more novel aspects.

Minor Comments:
-
- Figures are not readable.

Typos:
-
- Line 84: builds off of Wan et al. ==> Did you mean “builds on Wan et al.”?
- Line 61: in the Appendix ==> I think it is more correct to use “in Appendix” or “in the appendix”.
- Line 105: $S$ is a finite set of states, $A$ is … ==> $\mathcal S$ is …, $\mathcal A$ is …

### Questions
See above.

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
3

### Summary
This paper extends the risk-averse average-reward MDP framework from [1] and introduces a new approach called "Reward Extended Differential (RED)" for solving various subtasks (e.g., scalar prediction or control objectives) concurrently. Instead of using the observed reward $R$ directly, the TD error is defined using a modified reward $\tilde{R} = f(R,Z_1,Z_2 ...,Z_n)$ where $f$ is an invertible function mapping the observed reward and all subtasks to a modified reward $\tilde{R}$. The authors demonstrate their algorithm’s application to risk-averse (CVaR) decision-making in a fully online setting.

References: 

[1] Wan, Yi, Abhishek Naik, and Richard S. Sutton. "Learning and planning in average-reward markov decision processes." International Conference on Machine Learning. PMLR, 2021.

### Strengths
(a) The abstract, introduction, and preliminaries on average reward reinforcement learning are well-written and clearly presented.

(b) The TD and Q-learning with stochastic approximation algorithms, along with Theorems 4.1–4.3, appear to be rigorously verified with proofs in Appendix B. These proofs effectively extend the results from [1, 2, 3] to the multi-subtasks setting proposed in this work.

References: 

[1] Wan, Yi, Abhishek Naik, and Richard S. Sutton. "Learning and planning in average-reward markov decision processes." International Conference on Machine Learning. PMLR, 2021.

[2] Vivek S Borkar. Asynchronous stochastic approximations. SIAM Journal on Control snd Optimization, 36(3):840–851, 1998.

[3] Vivek S Borkar. Stochastic Approximation: A Dynamical Systems Viewpoint. Springer, 2009.

### Weaknesses
Despite the authors' in-depth understanding of stochastic approximation and model-free Q-learning proofs, the paper lacks sufficient validation regarding the extension to risk awareness in average reward MDPs.

(a) The paper demonstrates a limited engagement with prior work and foundational concepts in risk-averse CVaR MDPs. The authors inaccurately claim that “our work is the first to propose an MDP-based CVaR optimization algorithm that does not require an explicit bi-level optimization scheme or an augmented state-space.” However, several existing approaches such as dynamic risk-averse MDPs [1], risk-averse distributional RL [2, 3,11] and average-criteria CVaR [9] also avoid state-space augmentation and employ stationary Markov policies, similar to this work. Furthermore, the proposed algorithm still seems to be bilevel as it aim to optimize for CVaR but update the VaR estimate at every level. Moreover the author mentioned that "the CVaR that we aim to optimize most closely matches the static category", restricting to stationary Markov policies can impair both the optimality and interpretability of static CVaR MDPs (see [4, 5, 6, 7]), since the sum over $t \in 1:n$ for average criteria is outside of the CVaR operator, this is closer to the dynamic category where optimal deterministic stationary policy exist (see Theorem 1 of [9]). Additionally, the authors overlook related works [8] applies a similar TD update and [10] consider time-consistent policies set. It should be noted that "notable works such as [6]" describe in related work section, are known to be sub-optimal for policy optimization (see [7]). For this reason, augmented state-space primal methods with bi-level optimization, as in static CVaR MDP algorithms [4, 5, 9], are generally preferred.

(b) The CVaR analysis in Appendix C.1 is focused solely on evaluation, leaving out an analysis for policy optimization claim "We can now optimize the expectation in Equation C.5f using the RED RL framework". Additionally, the average criterion CVaR objective function itself is not explicitly presented in the paper. Sections 4 and 5 feel somewhat disconnected; providing a clearer explanation to link these sections, along with an explicit proof that the proposed algorithm can optimize the CVaR objective, would significantly strengthen the paper’s claims regarding risk-aware reinforcement learning in average reward MDPs.

(c) Limited empirical results: The results in Section 5 do not demonstrate that the proposed algorithm effectively optimizes the desired CVaR risk level. The evaluation would be more convincing if the authors trained the algorithm across multiple distinct CVaR risk levels (e.g. $\tau \in [0.01,0.05,0.1,0.5,1]$), and subsequently assessed performance by calculating the CVaR of the average reward over the final $n$ steps for each risk level $\tau' \in [0.01,0.05,0.1,0.5,1]$. Ideally, the maximum performance at each evaluated risk level should correspond to the training run specifically conducted at that CVaR risk level, reinforcing that the algorithm correctly optimizes for the specified risk. Furthermore, comparing the proposed algorithm’s performance with other approaches [4,9,11] under an average reward criterion could also provide a clearer benchmark for its effectiveness.

(d) The claim to “learn a policy that optimized the CVaR value without using an explicit bi-level optimization scheme or an augmented state-space, thereby alleviating some of the computational challenges” is not substantiated. This claim would be more convincing if the authors compared the computational complexity or running time of the proposed method with that of the algorithm proposed in [9].

### Questions
Do we know the proposed algorithm updating VaR and CVaR simultaneously would converge to the optimal fixed point, not any other fixed point?

(a) The quantile regression stochastic approximation from equation (C.2) provides a quantile estimate which may not be unique for discrete random variable, VaR is only an element of quantile which is not an elicitable risk measure (see [1]). Therefore, quantile regression may not converge to VaR, perhaps VaR is not necessary and any quantile estimate is sufficient? However, CVaR is also not elicitable which makes it unclear how stochastic approximation can approximate these values accurately. There may be an assumption missing for the subtask function $f$ to handle the nuances of the problem discussing here. 

(b) It is unclear why the VaR approximation in algorithm 7 is update with $\delta$ instead of the gradient of quantile (L1) loss update (C.2) (see [2]). Note that the gradient of L1 loss is a piecewise constant. 

(c) In Appendix C, the claim that "We can see that when the VaR estimate is equal to the actual VaR value, the quantile regression-inspired terms in Equation C.5f become zero" holds only for continuous distributions during policy evaluation. Furthermore, this is insufficient, the authors may need to demonstrate that, starting from any initial estimate, the VaR estimate converges to the actual VaR, and similarly, that the CVaR estimate converges to the actual CVaR. Even if convergence is achieved in policy evaluation, there is no proof validating this statement for the discrete case or for policy optimization.

References:

[1] Bellini, Fabio, and Valeria Bignozzi. "On elicitable risk measures." Quantitative Finance 15.5 (2015): 725-733.

[2] Shen, Yun, et al. "Risk-sensitive reinforcement learning." Neural computation 26.7 (2014): 1298-1328.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the infinite horizon average criterion, to learn CVaR return without bi-level optimization. Indeed, CVaR-MDPs i.e., MDPs under CVaR objective, require solving an optimization problem at each policy evaluation step. By switching to the CVaR of the average reward (instead of discounted), the authors introduce RED-CVaR, a TD-type algorithm that avoids the inner optimization problem. Convergence results are provided under standard assumption. The approach is validated on a two-state MDP and inverted pendulum.

### Strengths
- The paper is easy to read, and the writing skills are good.
- I am unaware of previous work that proposed CVaR optimization for the average reward criterion, so this is original (as far as I can tell).

### Weaknesses
Even in the risk-neutral case, the average reward criterion has some analytical advantages. Notably, [2] focuses on that same criterion rather than the discounted one. As a side comment, I am unaware of any provably convergent AC algorithms for the risk-neutral discounted return. In that respect, it does not surprise me that the same holds for risk-sensitive MDPs, which questions the significance of this work.
- Another missing related work is [5], which considers infinite horizon average reward but with entropic risk instead of CVaR
A discussion on the nature of the risk considered in this work is missing: is it nested or static? It looks static, i.e., the objective is $\text{CVaR}(\bar{r}_{\pi})$, not nested, see [3, 4]. Therefore, time-consistency issues may arise and if not, they should be discussed. On the other hand, the nested formulation enables doing DP but lacks interpretability.
- The initial claims in Sec 2.1 are incorrect: average criteria have been extensively studied already in the 60-s with Howard and Blackwell. In particular, the Blackwell optimality criterion bridges the gap between discounted and average returns. See Chaps 8-9 of [1].
Eqs (4)-(5) are called Poisson equations, see [2].
- In the risk-neutral case, [2] do function approximation on the average reward setting. I think the same could be done for CVaR + function approximation.
- Def 4.1 is unclear. How does this definition translate to the max in Eq. (10) ?
- The statements of Thms. 4.1 and 4.2 are vague and should be formalized: what do they show? Why not focus on just one subtask as this is the case of CVaR optimization?
- Formal algorithm pseudo-codes should appear instead of a list of equations (17)
- The learning rates $\eta$, $\alpha$ are sometimes constant, sometimes time or even state-dependent.
- The convergence plots seem to show one run per experiment. How is the seed chosen? Is it random? Have the algorithms been run on more seeds? The authors are encouraged to plot error curves with mean±std.

Broadly speaking, the following concerns led to my grading:

- Some claims are inaccurate, including related works.
- The experiments are somewhat unclear and not very convincing.
- Although optimizing a CVaR-average return criterion is new, the theoretical contribution seems to be a simple adaptation of risk-neutral TD to CVaR-TD. In particular, explaining the analytical challenges encountered under risk-sensitive criteria would be helpful. In particular, why is the unichain assumption still necessary? I think this comes from the static nature of the CVaR -- I don't think the same assumption would be required/enough if CVaR here were nested.

### Questions
I encourage the authors to account for previous reviews' comments and suggestions and update their paper accordingly.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a way to optimizes the conditional value-at-risk (CVaR) risk measure of the average-reward rate in finite MDPs. The CVaR of a random variable $X$ with a parameter $\tau in (0, 1)$ is the expectation of the lower $\tau$ quantile of X. The key idea is to utilize a property of CVaR by Rockafellar and Uryasev (2000) --- the CVaR of X with a parameter $\tau$ is the expectation of a piece-wise linear function of X and the value-at-risk (VaR; the lower $\tau$ quantile of X). By estimating VaR separately and treating the output of this piece-wise function as a new reward, the paper proposes that CVaR can be estimated using an existing average-reward algorithm. The key advantage of this approach to estimate the CVaR of the reward rate is that it does not perform the bi-level optimization and does not augment the state space, whereas existing algorithms need to do one of them.

### Strengths
The claimed contribution has sufficient novelty. However, I am not an expert in this area so I can not confirm if the claim is true.

### Weaknesses
I have three concerns about this paper.

First, the writing of this paper is vague, making it hard to understand. For example, it is not clear why subtasks are introduced when the main goal is the CVaR problem, until Section 5. Even in Section 5, the authors didn't explain explicitly how these two ideas are related and how equation (19) was derived. Another example is the discussion about the literature. The paper only mentioned one work for estimating CVaR (Xia et al. 2023) in the average-reward setting. Is that the only work? In addition, was the paper's idea applied to other settings (discounted, episodic) before? If so, what are the differences?

Yet, the major problem is that the derivation of the results in the paper seems to be problematic. Specifically, the step from 13a to 13b does not hold in general for piece-wise linear function f (the proof says that f is linear but Definition 4.1 says that f can be piece-wise linear and in order to be applicable to CVaR, f needs to be piece-wise linear). Similarly, 14a to 14b does not seem to hold.

Third, there are quite a few typos/incorrectness/weird statements of this paper. I list some of them here:
"Average-reward (or average-cost) MDPs were first studied in works such as Puterman (1994)." Puterman's book summarizes previous works. I don't think it's fair to say that these MDPs were "first studied in works such as Puterman (1994)". 
At the beginning of Section 3.1, discreet -> discrete, S -> \mathcal{S}, A -> \mathcal{A}.
Equation 1 depends on the start state S_0 while the l.h.s. shows that it is not.
"Such assumptions ensure that, for the induced Markov chain, ...". \mu_\pi here is the limiting distribution, instead of a stationary distribution. In addition, the limiting distribution does not exist for periodic Markov chains.
Max in equation (10) should be Sup. So does several other places in the paper. 
Definition 4.1 (ii) should be a property on the function f, instead of a property on the z_i, because z_i is just a scalar input of f, not a random variable.
Lower case letters r, s, s' are sometimes used as random variables and sometimes used as scalars.

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

### Contribution
3
