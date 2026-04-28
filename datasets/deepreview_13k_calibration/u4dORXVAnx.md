# Numerical Pitfalls in Policy Gradient Updates

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 5, 6

## Abstract
Numerical instability, such as gradient explosion, is a fundamental problem in practical deep reinforcement learning (DRL) algorithms. Beyond anecdotal debugging heuristics, there is a lack of systematic understanding of the causes for numerical sensitivity that leads to exploding gradient failures in practice. In this work, we demonstrate that the issue arises from the ill-conditioned density ratio in the surrogate objective that comes from importance sampling, which can take excessively large values during training. Perhaps surprisingly, while various policy optimization methods such as TRPO and PPO prevent excessively large policy updates, their optimization constraints on KL divergence and probability ratio cannot guarantee numerical stability. This also explains why gradient explosion often occurs during DRL training, even with code-level optimizations. To address this issue, we propose the Vanilla Policy Gradient with Clipping algorithm, which replaces the importance sampling ratio with its logarithm. This approach effectively prevents gradient explosion while achieving performance comparable to PPO.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates numerical instabilities in policy gradient methods used in deep reinforcement learning. It focuses on the gradient explosion issues when training deep policy gradient algorithms like TRPO and PPO.  The authors argue that these instabilities are often due to the ill-conditioned density ratio in importance sampling used in algorithms like TRPO and PPO which will lead to large gradient magnitudes that can exceed the limits of floating-point representation. The authors demonstrate that existing constraints like KL divergence and probability ratio clipping are insufficient to address these numerical issues. Several techniques and approaches are proposed to mitigate these instabilities.

### Strengths
- The paper provides a theoretical analysis of the cause of numerical instabilities in deep policy gradient algorithms. The paper identifies the role of importance sampling and density ratios in gradient explosion araising from numerical instabilities.
- This paper critiques the limitations of existing optimization constraints such as the KL divergence and ratio clipping in maintaining numerical stability.
- This paper provides some potential solutions to mitigate the numerical instabilities in deep policy gradient algorithms.

### Weaknesses
 - The paper provides a theoretical analysis of the cause of numerical instabilities in deep policy gradient algorithms. The paper identifies the role of importance sampling and density ratios in gradient explosion araising from numerical instabilities.
- This paper critiques the limitations of existing optimization constraints such as the KL divergence and ratio clipping in maintaining numerical stability.
- This paper provides some potential solutions to mitigate the numerical instabilities in deep policy gradient algorithms.

- The paper does not provide a detailed empirical analysis of the numerical instabilities to support the theoretical claims. Specifically, the paper lacks a systematic study showing how the magnitude of the density ratio correlates with observed gradient explosions. It would be beneficial to see experiments that vary the policy parameters to induce different levels of density ratio ill-conditioning and then measure the resulting gradient magnitudes and training stability. The absence of such experiments makes it difficult to fully validate the theoretical analysis.
- The propoesed solutions are either difficult to implement or hurt the performance of the algorithms. There is no clear and effective solution presented in this paper. The paper should provide a more thorough discussion of the practical challenges in implementing the proposed solutions, such as computational overhead or hyperparameter sensitivity. Furthermore, the performance degradation observed with the proposed solutions needs to be better understood and addressed. A more comprehensive analysis of why these solutions are not as effective as desired is needed.
- Although the paper provides some experimental results for the proposed results, they are not comprehensive and do not provide a clear comparison with existing methods. The experimental section lacks a rigorous comparison with standard baselines. The results should include a comparison with vanilla PPO and TRPO implementations, as well as other existing methods designed to improve numerical stability. The current experimental results are too limited to draw strong conclusions about the effectiveness of the proposed solutions.

### Questions
- Can you provide more insights into the numerical instabilities in policy gradient methods and how they manifest during training? How do these instabilities affect the convergence and performance of deep reinforcement learning algorithms?
- Can you provide a comprehensive empirical study on the proposed solutions to mitigate numerical instabilities in policy gradient methods? Can you explain more about the limitations of these solutions?

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
4

### Summary
This paper investigates the role of the importance sampling term w.r.t. numerical instabilities in policy optimization algorithms. It takes a close look at TRPO and PPO, and shows that instabilities naturally arise when Gaussian policies’ actions are clipped to fit a bounded continuous action space. The authors argue that this type of instabilities is different (and more important) from existing sources of instabilities, and that typical algorithmic tricks like KL-penalties don’t prevent these instabilities.

Overall I found this paper mostly well written and easy to follow. My main concerns are about the soundness of the author’s argument and the significance of the work. I think the instabilities described by the authors happen in contrived scenarios, namely when the policy’s support lies mostly outside of the action space.

### Strengths
- The paper is well-written and easy to follow, even for an audience that has little background in policy gradient for continuous control. I especially appreciated that the notation is kept simple, that only relevant equations are introduced when needed, and that the flow of the paper was natural. The authors do a good job of holding the reader’s hand throughout the paper.
- I think the paper is sound. All derivations looked right (caveat: I didn’t check the Appendix) and the authors analyze many of the aspects of policy gradient algorithms.
- The topic investigated — namely, how to stabilize and scale up policy gradient algorithms — is very relevant to the ICLR community. Especially since tuning PPO remains painful and the analysis isn’t tied to a particular application domain (modulo the action space assumptions).

### Weaknesses
 - My main concern stems from the contrived analysis. The authors point three cases in which the importance sampling ratio can become numerically unstable for Gaussian policies (l. 212):
    1. If the covariance of the reference policy has large eigenvalues.
    2. If the support of the policy mostly lies outside of the action space.
    3. If the policy changes rapidly with mini-batch updates.
    
    The authors state that 1) can be controlled (eg, entropy bonus). They argue the main issue stems from 2), but I think it is unlikely unless the policy’s initialization is pathological. A sensible initialization would be to set the mean of the policy at the center of the action space, and then it’s unclear how it would drift outside of the action space. Regarding 3), I think this is directly targetted by the KL constrained. This argument is not refuted by the analysis in Section 4, which mostly targets the sources of instabilities due to 2).
    
- A second concern is that the authors study potential fixes but none works. While this is not required (pointing out an unknown issue is valuable in itself), it would have strengthened the analysis if it led to a solution. In fact, I believe there is a well-known solution: for bounded action spaces, use the so called “Tanh-Gaussian” distribution as done in the Soft Actor-Critic and derivative works (Haarnoja et al, 2018). The authors mention and try the Tanh-Gaussian distribution; yet, they do not cite Haarnoja.
- In fact, I’m doubtful of some of the experimental results. SAC with the Tanh-Gaussian gets among the best results on the Mujoco tasks studied in this paper but the authors report negative results when trying this distribution with TRPO / PPO. Having tried this the Tanh-Gaussian distribution on continuous control Mujoco tasks and with PPO, my intuition tells me it should perform no worse than a Gaussian distribution if tuned properly.
- Finally, there are some more minor issues. I think the introduction, abstract, and title are slightly over-claiming: they don’t qualify the claims that the importance sampling instabilities only arise for continuous and **bounded** action spaces. This should be mentioned early, not on p. 3 (l. 137). Some of the figures could also use some work; eg, I don’t know what’s the difference between the plots in Fig. 2: is it with clipped / tanh policies? is it different tasks? why does Max Ratio monotonically increase in (b) and (c) but not in (a)? is max_t computed over all optimization steps or just the current one (if former, then monotonic increase is not surprising)? Another example, for Table 1 it would be good to include the reference results without any clipping or tanh.

### Questions
Please see the “Weaknesses” section above. In addition:

- Why would the policy distribution drift significantly outside the box defined by the action space?
- l. 357: Why would $\mu$ be outside the action space at initialization?
- Do the same issues appear on discrete action spaces?

### Soundness
4

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
Gradient explosion, during policy optimization is a significant problem in deep reinforcement learning (DRL). The authors present an analysis of why this issue occurs and propose directions for improving stability in policy gradient methods. The authors hypothesize that the root cause lies in the importance sampling step, specifically the density ratio in the surrogate objective function. They show that the TRPO/PPO loss is inherently ill-conditioned due to importance sampling and action clipping, which directly contribute to the numerical instability.

### Strengths
The paper is organized, progressing logically from problem definition to analysis, experiments, and suggested approaches.  By comparing PPO with TRPO and vanilla policy gradient, the authors effectively demonstrate that vanilla policy gradient methods, despite their simplicity, do not suffer from the same instability. This comparative approach highlights the specific issues with importance sampling and policy constraints.

### Weaknesses
FINAL RETURN is not a fully informative comparison measure. The hyperparameter tuning process in your experiments is not clearly explained, and five runs seem insufficient for reliable results. Increasing this to ten runs would provide more robust data. Additionally, were these runs conducted with different random seeds?

Another concern I have is regarding the content. I would have given a strong recommendation if the paper had introduced a rigorous algorithm to bypass the need for importance sampling in TRPO/PPO. Bypassing IS has been addressed in works such as 'Efficiently Escaping Saddle Points for Non-Convex Policy Optimization' (https://arxiv.org/pdf/2311.08914), which should have been referenced to provide context and highlight potential alternative approaches.

### Questions
Why did you use FINAL RETURN to report? why the final is important? not previous ones?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors conduct an empirical study of a specific issue related to the importance weights in policy optimization, which is that the probability ratio of the current policy to the data collection policy is not necessarily upper bounded and can be arbitrarily large with a non zero probability. The paper hypothesizes that this could lead to numerical instability and goes on to propose ways to prevent this from occurring especially for feasible bounded continuous action sets. However, they observe that while this is successful at bounding the maximum probability ratio, this actually leads to worse final performance on the returns and then go on to speculate that this implies that the success of deep policy gradient methods may be attributable in part to the numerical instability. This doesn't seem like a valid inference to me, since the maximum probability density ratio might not explain what is happening in the non-extreme cases that constitute the bulk of the samples being learned from.

### Strengths
- Authors conduct a focused experimental study of a specific numerical issue that might not otherwise be highlighted in literature.
- The paper puts forth bold hypotheses and presents a good didactic discussion of issues related to clipping the action and how the mean being outside a feasible set can unintentionally lead to a large density ratio.

### Weaknesses
 - The authors claim that the success of policy gradient algorithms is due to numerical instability -- this seems like an odd thing to infer from their ablations. 
- While the point made in L137-140 about sampling from $\pi$ notwithstanding, clipping them to a bounded range leading to an unintentionally small value for $pi$, this doesn't seem like a strong enough case to justify the broad claim in the title in the section, "importance sampling considered harmful".
- Most of the insights contained in the paper are either not entirely novel or they are hard to be convinced of (e.g. claims about importance sampling being harmful, or numerical instability benefitting deep pg algorithms), from the empirical observations. There isn't much theory to speak of, and the main theorem is just a simple statement about the standard gaussian normal density.

### Questions
- Figure 2 unclear what is the experiment ablation being studied across the three variants (a), (b) and (c). 
- In Table 2, can you describe "explosion rate" a bit more and how this impacts the learning? Is this the fraction of samples for which the gradients are NaN and in which case the sample is effectively discarded from the mini batch that computes the model update? Or is it the fraction of minibatches where the update is not computed, i.e. effectively a full training step wasted.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the issue of numerical instability in deep reinforcement learning. It begins by positing that importance sampling weights are the primary cause of exploding gradients in PPO and TRPO. A series of example calculations is then used to demonstrate why the importance sampling factor can lead to exploding gradients. Finally, the paper presents potential solutions to ensure numerical stability, along with a discussion of their respective advantages and disadvantages.

### Strengths
Numerical instability is an important topic, and understanding its root cause will help improve the practical application of RL.

### Weaknesses
I found it challenging to identify a distinctly new contribution in this paper. The issue of numerical instability due to importance sampling is well recognized, and several of the potential solutions explored here have also been discussed in prior work. While the deeper mathematical analysis of these causes is undoubtedly helpful, I am not entirely convinced that the contribution provides enough novelty in its current form.

W1: The analysis seems to be limited to gaussian policies. 

W2: From a statistical point of view, using just three environments to support your claims is insignificant. In my view, a case study with a statistically significant sample size would be necessary to substantiate your hypotheses effectively.

W3: I found it difficult to understand the figures from the captions, and at times, the text didn’t clarify either. For example, in Fig. 1(a), what exactly is being plotted? The condition number $\kappa(\theta)$ requires a function $f$ (which I assume is $p_\theta$ here), but what do $\mu_0$ and $\mu$ refer to, respectively? Please also see additional questions below.

### Questions
Q1: What changes when other policy parameterisations are used e.g. beta distribution reshaped to fit the desired action range. Then clipping becomes unnecessary. Is the importance sampling weight still the root course of exploding gradients?

Q2: I understand why large importance sampling rates cause numerical issues, but I didn’t immediately see the connection to exploding gradients, as a large objective value does not directly imply a large gradient. This question remained until Section 3, in the paragraph titled "Ill-conditioned probability ratio," where you explain the link between large importance sampling weights and large gradients (or a large condition number) for Gaussian policies. Could you elaborate on this in more detail for general parameterizations? This explanation is fundamental to the understanding of the paper and might be discussed in the beginning of Sec. 3.

Q3: What happens when a small epsilon is added in the denominator of the importance sampling weight? Specifically, if we have $p_\theta(a|s) = \frac{\pi_\theta(a|s)}{\pi(a|s) +\epsilon}$, this would ensure numerical stability for the objective function and would be the first approach I would consider to address the issue. However, what is the effect on the gradients?

Q4: In line 379, you state that a large mean always leads to the same clipped action. I don’t see how this is true in general; this only holds if the mean is far outside the action space, which is probably what you meant? 

Q5: Fig. 3(b): What neural network is used to approximate the value function? If I am informed correctly, neural networks are only smooth when analytic activation and output functions are used. Especially using ReLU leads to non smooth functions, right?

Q6: Fig. 4.: What is plotted in (a); What is the y-axis? What causes the constant lines in (b)? Is the algorithm converged?


**Remarks on Notation:**

R1: line 431: The vanilla objective was not yet introduced.

R2: line 432: what is $\alpha$? Is it the step size as later in (12)?


-----------------------------------------------------------------------
Update: I would like to thank the authors for their thoughtful revision.

Upon reviewing the updated version of the paper, I noticed that the manuscript now conveys a completely new message. In my understanding, the primary contribution of the paper lies in the newly proposed policy optimization method presented in Equation (15). This method replaces the importance sampling ratio in PPO with the logarithm of the importance sampling weight.

The authors argue that this approach addresses numerical instability, which is a notable improvement. While I am not deeply familiar with every variation of policy gradient methods, I cannot confidently confirm whether this specific approach has been proposed before. However, if the method is indeed novel, I find it to be a highly interesting contribution that would be valuable to share with the community. I raised my score to 6.

### Soundness
2

### Presentation
2

### Contribution
2
