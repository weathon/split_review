# Simple Policy Optimization

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 3, 8, 8

## Abstract
Model-free reinforcement learning algorithms have seen remarkable progress, but key challenges remain. Trust Region Policy Optimization (TRPO) is known for ensuring monotonic policy improvement through conservative updates within a trust region, backed by strong theoretical guarantees. However, its reliance on complex second-order optimization limits its practical efficiency. Proximal Policy Optimization (PPO) addresses this by simplifying TRPO's approach using ratio clipping, improving efficiency but sacrificing some theoretical robustness. This raises a natural question: Can we combine the strengths of both methods? In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm. SPO integrates the surrogate objective with Total Variation (TV) divergence instead of Kullback-Leibler (KL) divergence, achieving a balance between the theoretical rigor of TRPO and the efficiency of PPO. Our new objective improves upon ratio clipping, offering stronger theoretical properties and better constraining the probability ratio within the trust region. Empirical results demonstrate that SPO outperforms PPO with a simple implementation, particularly for training large, complex network architectures end-to-end.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
--Why: 
It has been shown that consistent policy improvement can be achieved through constrained policy optimization or trust region policy optimization. 

--What: 
However, in practice, current methods use approximations to enforce the trust region. In particular, PPO uses clipping of the probability ratio to enforce the trust region constraint. It's simple and works well in practice. However, the author argues and shows that theoretically, this cannot always satisfy the bound. When the probability ratio is out of bounds, this method zeros the gradient, and therefore there isn't any corrective gradient to push the policy back towards the trust region. Thus, this paper investigates better trust region enforcement for PPO.

--How:
Authors propose an objective (eq 15), which directly constrains the total variation divergence instead of KL divergence. They show theoretically that this is a better divergence (see Proposition 3.2 and 3proposition 3.2 .3). They also argue that, in practice, their objective can apply a corrective gradient when the probability ratio goes over the bound (see Figure 2 and Figure 4).

### Strengths
Paper is well written, problem statement is clear and is easy to follow. Motivations are supported with references and theoretical justifications as well as toy examples.

### Weaknesses
 --Originality and Significance
 
the idea of using  total variation divergence is not new and it's been proposed in original TRPO paper already as authors has also mentioned. Also some follow up work on constraint optimization and safe RL has explored similar ideas that worth being mentioned, for example see:

https://arxiv.org/pdf/1705.10528
,https://arxiv.org/pdf/1805.07708

Given that the idea of using total variation divergence is not entirely new, this paper requires strong experimental evidence to support its claims. The authors' decision to use hyperparameters from the original PPO paper seems unfair, considering that changes in the setup necessitate retuning. However, even with this caveat, Figures 9 and the continuous control results show no significant improvement over the original PPO. I believe tuning PPO could achieve better results. Furthermore, the results in Figure 6 are puzzling. A larger ResNet benefits SPO but not PPO. Observing the constant bias in Figure 7, it appears that choosing a different epsilon for PPO might lead to better results. This suggests that the performance difference could be attributed to suboptimal hyperparameter selection for PPO.

### Questions
--What is the significance of proposition 3.2 and theorem 3.3?
Could not we use the theorem (3) to conclude that Total Variation divergence is the better choice compare to KL divergence? 


--As the authors rightly mentioned, larger ResNets or deeper MLPs could help better representation learning and, therefore, better performance, as shown in Figures 5 and 6. I have personally observed this to be true in my own experiments with PPO. Could the authors provide a more compelling reason for why PPO in their experiments does not benefit from better representation learning, beyond the claim that PPO's performance deteriorates with an increasing number of parameters? Could tuning hyperparameters help PPO in this case?

--In figure 7, is it possible to match the curve for SPO(epsilon=0.2) if we choose different epsilon for PPO?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces an on-policy RL algorithm called Simple Policy Optimization (SPO). SPO is proposed as an improvement to PPO that can more effectively constrain the probability ratio between the next and current policy. The objective of SPO is designed to update the probability ratio to the boundary of $[1-\epsilon, 1+\epsilon]$ in the direction that improves the surrogate objective. Experiments on Atari and MuJoCo benchmarks in Gymnasium demonstrate that SPO controls the probability ratio and achieves performance that generalizes across different network architectures, compared to PPO which is more sensitive to implementation choices.

### Strengths
- **[S1] Simple implementation:** The implementation of SPO requires minimal changes to PPO and considers a simple unconstrained optimization problem.
- **[S2] Robust performance across architectures:** Experiments show that SPO generalizes well across different implementation choices such as network size, compared to PPO which is much more sensitive to these choices. Given the widespread use of PPO, improvements that provide robustness to hyperparameters / architectures are helpful for applying RL training across different applications.

### Weaknesses
 **[W1] Limited novelty compared to prior works, with several missing citations to relevant prior works**
- The results presented in the paper have limited theoretical novelty. Section 3 uses results that have already been shown in [1] to rewrite the TV distance, and applies Pinsker’s inequality in ways that have been used previously in [2]. The optimization problem in (15) is also not novel, and can be motivated from the policy improvement bounds proposed in [2] that include an expected TV distance penalty term (instead of a max over states). Section 4 formulates an objective that satisfies the set of assumptions put forth by the authors in Definition 4.1.
- Several methods have been proposed to better constrain the probability ratio in PPO, and SPO represents another implementation of this same idea. [1, 3] apply adaptive learning rates based on TV or KL divergence, [4, 5] propose modifications to the clipping function / rollback mechanisms, and [6, 7] consider non-parametric updates that determine target probability ratios. The SPO objective in (14) is designed to move each data point towards the target probability ratio in Definition 4.1, which is similar to what is accomplished by many of these methods. Specifically, the formulation of (9)-(10) uses results previously shown in [1], and motivates the optimization problem in (15) that is almost identical to the $L^\infty$ constraint formulation in [6], which adds an extra constraint. Proposition 3.2 / Theorem 3.3 directly follow from Pinsker’s inequality which has been used throughout the policy improvement literature. The optimization problem in (15) is also not novel, and can be motivated from the policy improvement bounds proposed in [2] that include an expected TV distance penalty term.  The paper could go directly from (10) to (15), and then use (15) to motivate (14).
- Most of the relevant works mentioned in the 2 previous bullet points are never referenced in the paper ([4] is the only work that is cited in the paper / compared against in the experiments). In general, the paper does not adequately frame its contribution with respect to prior work (there is no Related Work section in the paper).

**[W2] Experiments: contributions are overstated and suboptimal PPO implementation is used for comparison**
- At several points throughout the paper, the authors claim that SPO achieves state-of-the-art performance. However, the results shown in the paper are not state-of-the-art. Several off-policy algorithms have been shown to perform much better than SPO (and on-policy algorithms in general) on these benchmarks, and in some cases it is possible to find other implementations of PPO that achieve better performance than what has been reported in this paper (see the results contained in the references below).
- Experiments compare against PPO for a single set of hyperparameters / implementation choices that may be suboptimal based on other results reported in the literature. While I understand that this shows PPO can be more sensitive to implementation details than SPO, it would be much more convincing to show that SPO can perform similar to a well-tuned version of PPO across different tasks / architectures.

**Minor technical issues:**
- I believe that (8) is not correct due to the min that appears in the PPO objective in (6). The cases must also consider the sign of the advantage function (e.g., see (7) in [4]).
- The connection between TV distance and the probability ratio in (9) / Appendix B requires the assumption that the support of $\tilde{\pi}$ is contained in the support of $\pi$. This technical assumption is not mentioned anywhere in the paper.

### Questions
**[Q1] Can you please explain why each assumption in Definition 4.1 is important?** When comparing the objective in (14) to PPO, it seems like the existence of a unique optimal probability ratio in SPO is actually the important feature compared to multiple optimal solutions in PPO.

**[Q2] Could you please explain the purpose of Section 3 and the optimization problem in (15)?** It does not look like (15) is actually being used by SPO. Instead, the main algorithmic contribution is the objective in (14), which is motivated by considering the optimization problem in (17) at every state-action pair. Applying constraints at every state-action pair is more restrictive than the constraint in (15), and also does not account for the dependence across state-action pairs that occurs because $\pi$ must be a probability distribution.

**[Q3] Experimental suggestions:** I understand that these suggestions may not be possible in a limited rebuttal window.
- How does SPO compare to well-tuned versions of PPO across each setting?
- How does SPO compare to PPO using the adaptive learning rate in [3], which is a simple implementation detail used in the literature to prevent probability ratios from becoming very large?
- How does SPO compare to non-parametric policy update methods such as [6, 7]? Similar to SPO, these methods apply updates based on target probability ratios.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an actor-critic algorithm, Simple Policy Optimization (SPO), which achieves a more tight bound on the policy _probability ratio_ by modifying the loss function of Proximal Policy Optimization (PPO) algorithm. The authors demonstrate both theoretically and empirically that SPO imposes a stricter upper bound on the _ratio deviation._ Notably, SPO outperforms PPO across various tasks, especially when applied to policies with deeper network architectures. Although several papers have already pointed out issues with the heuristic clipping technique in PPO and proposed alternatives, I find the authors' approach offers a novel perspective, leading me to lean towards acceptance.

### Strengths
* This paper is well-written and clearly structured.
* The theoretical foundation is straightforward (in a positive way), and the implementation is simple, which could enhance reproducibility.
* SPO demonstrates superior performance over PPO, especially when using deeper networks (e.g., 7-layer MLP and ResNet).

### Weaknesses
 * SPO tends to make the _ratio deviation_ overly small in cases with fewer layers (see Table 2). Could the authors address whether the tighter ratio deviation in SPO may be limiting performance in some simpler tasks, and if so, how this trade-off might be managed?

* More importantly, without a comparison to existing methods like TR-PPO (as mentioned by the authors / Line 90), it is hard to assess how effective SPO is relative to other approaches that aim to address the same clipping issue in PPO. Could the authors include a comparison of SPO with TR-PPO and other recent methods addressing PPO's clipping issues, particularly focusing on performance and ratio deviation metrics across different network depths?

### Questions
**[Q1]**
In Table 2, SPO does not outperform PPO with a 3-layer network. Could you clarify this? In tasks where SPO underperforms (e.g., Ant, HalfCheetah, Walker2d), the ratio deviation appears to be constrained overly tightly.

**[Q2]**
To me, the transition from Equation (10) to Equation (14) feels somewhat abrupt. Could you elaborate further on this derivation? I understand the motivation behind Equation (14), presumably to demonstrate the bounded nature of the probability ratio as indicated by Theorem 4.3. However, if you could clarify how the $C$ and the max operator in Equation (10) relate to Equation (14), it would provide stronger theoretical support.

**[Q3]**
Is SPO also more applicable to large-scale scenarios and does it still show superiority in terms of ratio deviation? I’m curious about its performance difference from PPO in cases with extensive parallelism, such as environments with many actors like Isaac Gym.

**[Q4]**
When using a 3-layer network, what is the performance difference between SPO-0.3 and SPO-0.2? If SPO-0.2 constrains the ratio deviation overly tightly, causing it to underperform compared to PPO, SPO-0.3 might perform better due to the slightly looser upper bound on ratio deviation. If this is the case, it would provide stronger theoretical support for the approach.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a new RL algorithm, Simple Policy Optimisation (SPO), designed to address the challenges present in existing policy gradient methods, particularly PPO and TRPO. The primary goal is to develop a surrogate objective that constrains the policy ratio more effectively than PPO without the computational burden of TRPO's second-order optimisations. SPO achieves this by using TV divergence, combining TRPO's theoretical robustness with PPO's simplicity, and is demonstrated to improve performance across Atari and MuJoCo benchmarks.

### Strengths
1. **Clarity and Theory**: The paper is clearly written and provides strong theoretical grounding. New theorems and proofs substantiate the methodology, ensuring that the approach is technically sound.
2. **Experimental Rigor**: Extensive experiments on various benchmarks, including a range of baselines, demonstrate SPO's performance relative to other algorithms. The inclusion of pseudo-code and naming the used open-source repositories contributes to the reproducibility of the work. Additionally, hyperparameters are provided.
3. **Algorithm Simplicity and Impact**: SPO is a straightforward modification of PPO by changing the surrogate objective slightly, achieving meaningful performance improvements, particularly in terms of ratio constraint handling. The simplicity of SPO, combined with its impact, makes it valuable for the community.
4. **Comparative Baselines**: The paper employs a wide array of baselines (for the Mujoco tasks at least), giving context to the results and situating SPO’s benefits accurately. Understandably, Atari is very computationally expensive so it is hard to baseline everything as done in Mujoco so I am not too fazed although I would have liked 1 additional algorithm.

### Weaknesses
1. **Lack of Confidence Intervals**: The experimental results lack confidence intervals, which limits the ability to assess the performance variance across runs. It is difficult to ascertain the reliability of the reported mean performance without knowing the spread of the data. For instance, a high mean could be misleading if the variance is also high, indicating inconsistent performance across different trials.
2. **Absence of Statistical Tests**: No statistical testing (such as that from the [rliable](https://github.com/google-research/rliable) package) was performed, making it difficult to confirm the statistical significance of the improvements over PPO and other methods. This draws concern as to whether the improvements are statistically significant. Without statistical tests, it's impossible to determine if the observed differences are due to the algorithm itself or random chance. The lack of p-values or other measures of statistical significance makes it hard to draw firm conclusions.
3. **Potential Baseline Tuning Issues**: PPO and similar RL algorithms are known to be highly sensitive to hyperparameters like batch size, mini-batch size, and the number of rollout steps. The paper does not discuss any dedicated hyperparameter tuning for the baselines, raising concerns about potential underperformance. It was noted that hyperparameters were used from the original papers but this is not always a fair approach especially considering certain types of parameters are not always listed such as number of rollout workers. This lack of tuning could lead to an unfair comparison if the baselines are not operating at their optimal performance levels.
4. **Code-level Optimisations**: As noted in the paper, code level optimisations can significantly impact the performance of certain algorithms, but the paper does not specify what implementation tricks were used in the baselines and SPO itself. This lack of transparency makes it difficult to reproduce the results and understand the true source of performance gains. For example, using vectorized environments or specific GPU memory management techniques can significantly alter performance, and these details are missing.

### Questions
**Questions for the Authors**  
1. Could you provide confidence intervals and other statistical measures for the experimental results to help clarify performance variance and statistical significance?
2. Were any efforts made to tune the baseline hyperparameters specifically? If so, could you detail the tuning process? Additionally, how much effort was made tuning SPO? 

Ultimately, I liked the paper, think it is a simple yet efficient algorithm and I believe it would be useful and warrants acceptance **if just slightly more validated results are presented.** This should be as simple as presenting the mean, median and interquartile mean of the results as well as using stratified bootstrapping to produce confidence intervals i.e. no further training runs should be done. Due to this, I am giving it a 5 as I do not believe the results can be presented as it currently stands. I look forward to raising the score.

### Soundness
4

### Presentation
4

### Contribution
3
