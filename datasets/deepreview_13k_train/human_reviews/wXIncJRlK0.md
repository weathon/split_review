# Mirror Descent Actor Critic via Bounded Advantage Learning

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Regularization is a core component of recent Reinforcement Learning (RL) algorithms. Mirror Descent Value Iteration (MDVI) uses both Kullback-Leibler divergence and entropy as regularizers in its value and policy updates. Despite its empirical success in discrete action domains and strong theoretical garantees, the performance improvement of a MDVI-based method over the entropy-only-regularized RL is limited in continuous action domains. In this study, we propose Mirror Descent Actor Critic (MDAC) as an actor-critic style instantiation of MDVI for continuous action domains, and show that its empirical performance is significantly boosted by bounding the values of actor's log-density terms in the critic's loss function. Further, we relate MDAC to Advantage Learning by recalling that the actor's log-probability is equal to the regularized advantage function in tabular cases, and theoretically show that the error of optimal policy misspecification is decreased by bounding the advantage terms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to clip the logarithmic term in Mirror Descent Actor Critic (MDAC) when improving the Q value. Experiments on classical benchmarks show that the new approach can attain faster convergence compared to baseline methods. To justify the clip operation, The work argues that it can reduce the upper bound of a certain error term appeared in their convergence analysis.

### Strengths
* After applyinig the bound operation, the algorithm is empirically observed to converge faster and achieve higher scores.
* The clip operation is easy to implement.

### Weaknesses
 * The justification on larger error tolerance for critic value estimation is not valid. Specifically, the paper argues that the proposed algorithm's error term's **upper bound** (the last term in equation (10)) is lower compared to the baseline algorithm (line 345-350). However, lower upper bound does not indicate that the term is lower. Given that the main motivation for the algorithm is its better error tolerance, a rigorous justification is critical. The core issue is that the paper claims a reduction in the error term by bounding the log term, but only shows a reduction in the upper bound of the error term. This is not sufficient to prove that the actual error is reduced, as the error could still be larger even with a smaller upper bound. The analysis needs to show that the bounding operation consistently reduces the actual error, not just its potential maximum value.

* The writing needs to be polished; the paper is full of tedious definitions and theorems that are not helpful for readers to understand the main argument. There are many typos as well.

### Questions
* My conjecture is that the faster convergence from the clip operation comes from lower variance of the stochastic gradient, which helps stablizing the training?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes mirror descent actor-critic (MDAC), extending the Munchausen RL proposed in the discrete action case to continuous actions. To address the issue of ill-behaved log density when using off-policy data, the paper suggests bounding the added log density term and hopes that the modified term would provide benefits during learning. Empirically, the suggested ad-hoc fix to the ill-behaved log density term is demonstrated to fix the issue and performs better than the baseline without the added term. Theoretically, the paper studies the bounding strategy in the tabular case and shows that the corresponding value iteration algorithm converges while also providing arguments for bounding over not bounding.

### Strengths
The strengths of the paper include its originality, clarity, and significance:
1. The originality of the paper is one of its strengths. Although the technique of bounding the log density term in the off-policy case is ad-hoc and not entirely novel (as the original Munchausen RL also has a similar variant), the theoretical results are new to my knowledge.
2. The paper is mostly clear. It has clear writing and is easy to follow. It also covers most of the important related works.
3. The studied problem, continuous control, is of significance in the RL literature. Mirror-descent-based algorithms are also an important and interesting approach that enjoys theoretical motivations. Thus, the paper might be of interest to many RL researchers.

### Weaknesses
Despite having many strengths, this paper is weak in the following areas:
1. The empirical evaluation is limited. The main empirical results only include experiments on six MuJoCo environments and show only marginal improvements over the baseline. There are many other commonly used continuous control benchmarks (e.g., DeepMind Control Suite and Omniverse Isaac Gym environments), including some experiments for these environments that would strengthen the paper, especially if there is a larger improvement to be seen. Furthermore, the reported performance gains appear to be primarily in terms of sample efficiency, with the final performance levels being quite similar to the baseline. This raises questions about the practical significance of the proposed method, as the overall performance ceiling is not improved. It would be more compelling to see results where the proposed method can achieve significantly higher final performance, or solve tasks that the baseline cannot.
2. This is a minor point, but the paper is also weak in its literature discussion. While there are many approaches based on the idea of mirror-descent, this paper only discusses relevant work that follows Munchausen RL. If it can include some discussion of alternative mirror-descent-based approaches, especially how they differ from the studied approach, it could improve the contextualization of the paper. The paper should also discuss how the proposed method relates to other off-policy algorithms that use similar techniques to stabilize learning, such as clipping or trust region methods. A more comprehensive discussion of the broader landscape of mirror descent and off-policy RL would be beneficial.

### Questions
Here are some questions that might affect the evaluation:
1. Why would there be a significant difference between *clip(x, -1, 1); current* and *clip(x, -1, 1); successor* in Figure 8? Shouldn’t it be quite small, given that consecutive transitions should be included in the replay buffer?
2. Why is the clipping frequency of *clip(x/10, -1, 1)* so low, given that the log density term is shown to be so large in Figure 3?

Other minor comments:
* There isn’t a definition of $A_k$ in Line 235. Is it $A_k=\alpha\log\pi_{k+1}$?
* Typo in Line 262: genral -> general
* It would be better to clarify the tradeoff mentioned in Line 357. The sentences read incomplete to me.

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
This paper introduces Mirror Descent Actor Critic (MDAC), a novel approach to enhance reinforcement learning in continuous action spaces. By bounding the log-density values in the critic's loss function, MDAC significantly boosts performance over traditional entropy-only methods. The authors show that this approach reduces policy error, connecting MDAC to Advantage Learning and providing theoretical support for improved stability in continuous domains.

### Strengths
**Good motivation**
- Improvement of the performance of Mirror Descent RL on continuous action tasks.

**Theoretical and Empirical Rigour**
- The progression from MDVI to MDAC is well-motivated, and the authors thoughtfully discuss the relation to SAC’s temperature tuning. I found the performance gap between non-bounded (identity) and bounded (tanh) log-policy to be surprisingly substantial.

### Weaknesses
 **Section 4**
- It seems that bounding the log-policy was meant to yield a tighter bound in Theorem 3, connecting it to Advantage Learning (AL). Could you clarify if BAL was introduced specifically for this purpose? It's unclear if the theoretical analysis is driving the design or if BAL was an ad-hoc choice that was later justified theoretically.
- L224: I didn’t see definitions for regularized MDP and soft state value function—could you include these? Specifically, the connection between the KL-regularization and the soft-state value function is not clear from the current description. It would be helpful to define the soft state value function in terms of the KL-regularized policy and Q-function.
- L227: Why does V(s)=max_{⁡a∈A} Q(s,a) hold when α=0? The current explanation lacks the necessary detail to understand this limit. It is not clear how the log-sum-exp function converges to the max operator in this specific context.
- L239 (Eq. 9): Could you provide the derivation for this Bellman operator? The jump from equation 6 to 9 is not obvious and requires a more detailed explanation, especially how the error term is handled.
- L245: Could you explain how the gap-increasing Bellman operator reduces suboptimal action values? The explanation is too high-level and lacks the necessary mathematical details to understand the mechanism of reduction.
- L247: I’m unfamiliar with the literature on successor state functions—could you clarify the meaning of successor state-action pairs here? It's not clear how the state transition operator is applied to the advantage function and how this relates to the successor state-action pairs.

**Section 5.1**  
What was the objective of comparing M-VI and BAL here? I’d appreciate more insight into why M-VI performs so much worse in this setup. The current explanation does not provide sufficient detail on the specific conditions that lead to M-VI's poor performance, nor does it explain the role of the hyperparameter β in this context.

**Section 5.2**  
In Figure 9, several agents haven’t converged. Could you provide fully converged results? Additionally, the abstract claims “significant empirical improvement”—could you specify the basis for this assertion? The claim of significant improvement needs to be substantiated with more robust experimental evidence, including convergence plots for all agents and a clear definition of what constitutes a significant improvement.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes Mirror Descent Actor-Critic (MDAC), which extends Mirror Descent Value Iteration (MDVI) into continuous action domains. The authors showed that naively implementing MDAC in practice can lead to instability, and found that this is caused by the magnitude of the log policy terms being much larger than the magnitude of the rewards. As a fix, the authors proposed to bound the effect of the log policy terms by transforming them through a bounded function, and showed that this can recover the agent’s performance. The authors then demonstrated that this ad-hoc fix can be seen as an instantiation of advantage learning, Lastly, the authors demonstrated that the proposed approach is competitive with previous methods like SAC and TD3.

### Strengths
1. The paper extends MDVI style regularization, which was found to be useful in the discrete action domains, to continuous action domains. This can potentially enable more robust design of algorithms, and is certainly a valuable contribution to the community.
2. The proposed solution (i.e., bounding the effect of the log policy terms) is backed by both theory and empirical evidence (mujoco experiments). In addition, the theory can also explain certain design decisions made in previous works (e.g., the log policy clipping used by munchausen DQN).

### Weaknesses
My main concern is that it is not clear to me whether the proposed fix (bounding the log policy terms through transformations) is more effective than simply constraining the policy (e.g., lower bounding the standard deviation of the Gaussian policy) to avoid this problem in the first place.

Since SAC is a special case of MDAC, I don’t understand why SAC is not suffering from the same problem of exploding log policies. After digging through the code provided by the authors, I think this is partially due to the authors using a much lower bound on the log_std parametrization. For example, in the CleanRL SAC implementation, log_std_min is set at -5, while the authors set this parameter at -20. As another example, the official implementation explicitly lower bounds the standard deviation at 1e-5, which is much larger than the value used by the authors. This might explain why, in Figure 3, the log policies are showing extreme values. To test this, I would suggest the authors to reproduce Figure 3 for different values of log_std_min to see its impact. It also appears that the instability is not solely due to the log policy terms, but also the alpha parameter and how it's optimized, since the log policy terms for log_std=-2 are on a similar scale compared to the bounded approach before 1e5 steps (for Walker2d), and things started to destabilize only after alpha started increasing.

### Questions
1. On line 349, it appears that using functions with smaller $c_f$ can improve convergence speed, then why not simply use $f\equiv 0$? What would be the trade-off here?
2. In contrast to previous methods, the sub-optimality of BAL (Equation 10) does not seem to explicitly depend on the value estimation error $\epsilon_k$. Can the authors elaborate a bit on this?

### Soundness
3

### Presentation
2

### Contribution
3
