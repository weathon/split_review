# Simple Minimax Optimal Byzantine Robust Algorithm for Nonconvex Objectives with Uniform Gradient Heterogeneity

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
In this study, we consider nonconvex federated learning problems with the existence of Byzantine workers. We propose a new simple Byzantine robust algorithm called Momentum Screening. The algorithm is adaptive to the Byzantine fraction, i.e., all its hyperparameters do not depend on the number of Byzantine workers. We show that our method achieves the best optimization error of $O(\delta^2\zeta_\mathrm{max}^2)$ for nonconvex smooth local objectives satisfying $\zeta_\mathrm{max}$-uniform gradient heterogeneity condition under $\delta$-Byzantine fraction, which can be better than the best known error rate of $O(\delta\zeta_\mathrm{mean}^2)$ for local objectives satisfying $\zeta_\mathrm{mean}$-mean heterogeneity condition when $\delta \leq (\zeta_\mathrm{max}/\zeta_\mathrm{mean})^2$. Furthermore, we derive an algorithm independent lower bound for local objectives satisfying $\zeta_\mathrm{max}$-uniform gradient heterogeneity condition and show the minimax optimality of our proposed method on this class. In numerical experiments, we validate the superiority of our method over the existing robust aggregation algorithms and verify our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies nonconvex federated learning (FL) in the presence of byzantine workers with a fraction of  $\delta$ out of the workers. Then the authors proposed the Momentum Screening (MS) algorithm for such setting, achieving $O(\delta^2 \zeta^2_{max})$ error rate for $\zeta_{max}$-uniform gradient heterogeneity, and showed the minimax optimality of the proposed method in such setting. Experimental results are then given to validate the MS algorithm.

### Strengths
The algorithmic structure of the MS algorithm is simple and can adapt to the Byzantine fractions $\delta$, all of which can be practically attractive. Furthermore, the minimax optimality results seem like the first of its kind for such setting of $\zeta_{max}$-uniform gradient heterogeneity.

### Weaknesses
1. The consideration of algorithmic design for uniform gradient heterogeneity as in this paper has been done in the literature. In fact, the rate achieved here seems to be the same as the CCLIP method (Karimireddy et al. (2022)) (ref [1] as below for convenience). Yet, such literature was not well discussed enough in the paper. 
2. Following up the above point, many results in the paper are quite the same as those in CCLIP without improvement, and the analysis is quite natural and motivated from previous work. The true technical novelty of the paper, besides the MS method with simplicity, is perhaps the fact that they proved lower bound in the minimax sense for uniform gradient heterogeneity. However, this is quite a natural extension from the first work that proved such results for the case of mean gradient heterogeneity.
3. Systematic typo throughout the paper: note that yours is better than CCLIP when $\delta \leq ( \zeta_{mean}/ \zeta_{max})^2$. Can you give a sense of what $\zeta_{mean}/ \zeta_{max}$ can be in real datasets, especially those considered in your experiments? Because I think such fraction can be very small in practice, which is also acknowledged in your Section 2.1. So the regime in which MS provides benefits is in fact quite limited.

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of federated learning with Byzantine workers who can send arbitrary responses to the central server. In the non-IID case where the local distributions of non-Byzantine workers are heterogeneous, the standard aggregations will fail empirically, as shown in previous works. In this paper, the authors developed a new, simple byzantine robust algorithm that have better minimax optimal optimization error compared to the best previous algorithm when the maximum gradient heterogeneity is not much larger than the average gradient heterogeneity, whose optimality in this parameter regime is demonstrated by establishing a lower bound result. Moreover, the authors conducted numerical experiments to support their theoretical analysis.

### Strengths
The algorithm is novel and simple, makes it relatively easy to be implemented in practice. Moreover, the improvement in the minimax optimal optimization error is significant in the parameter regime where the maximum gradient heterogeneity is around the same order as the average gradient heterogeneity, which seems like a common assumption in various practical situations. The performance of the algorithm is also well demonstrated in the various numerical experiments.

### Weaknesses
 The convergence rate in terms of the number of steps $T$ might not be optimal. In particular, the algorithm is a momentum-based method, however, the convergence rate exhibits the form of a non-momentum based method, and it is unclear to me why the momentum is needed here.

### Questions
Will the convergence rate of the algorithm remain unchanged if the momentum is removed? Or, is there a better momentum-based algorithm that has better convergence rate?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new Byzantine robust algorithm called Momentum Screening (MS) for nonconvex federated learning. MS uses a simple screening test to detect and remove potentially malicious gradients from Byzantine workers. The remaining gradients are aggregated using standard momentum SGD. The algorithm is adaptive to the Byzantine fraction $δ$.

This paper gives theoretical analysis on the proposed algorithm, showing that MS achieves an optimization error of O($δ^2 ζ^2_{max}$) for the class $C_{UH}(\zeta_{max})$. A matching minimax lower bound is also provided for $C_{UH}(\zeta_{max})$. This rate differs from the rate $O(\delta \zeta_{mean}^2)$ for the class $C_{MH}(\zeta_{mean})$.

Experiments on MNIST and CIFAR10 with neural nets demonstrate MS outperforms existing methods like Centered Clipping, especially for small $δ$. This aligns with the better dependence on $δ$.

### Strengths
1. The proposed algorithm (MS) is simple to implement yet performs well. It also does not need to know the Byzantine fraction $\delta$ in advance, which is practical.
1. The rate of convergence of MS is better than the previous best known rate of $O(δζ^2_{mean})$ under the (corrected) condition when $\delta \leq (\zeta_{mean}/\zeta_{max}/)^2$, so the method is preferred if Byzantine workers are very few.
1. The author also provide a computationally efficient algorithm for their proposed MS method, whose performance is only worse than the original one by a constant factor.
1. Some experiments on MNIST and CIFAR10 with neural nets shows that MS outperforms other method.

### Weaknesses
1. In the literature the rate $O(δζ^2_{mean})$ is derived from $C_{MH}(\zeta_{mean})$, while this paper gives the rate O($δ^2 ζ^2_{max}$) for $C_{UH}(\zeta_{max})$. Now, to give a better rate, one needs
$$δ^2 ζ^2_{max} \leq δζ^2_{mean}  \Leftrightarrow δ \leq (ζ_{mean} / ζ_{max})^2, $$
where the RHS is $\leq 1$ since $ ζ_{max} \geq ζ_{mean}$. 
Therefore, **the requirement of $\delta$ is wrong throughout the paper** (the authors give $\delta \leq ( ζ_{max}/ ζ_{mean})^2$).
The authors even did not notice this mistake when they write $\delta = \Omega(1)$ (in Section 7) but in fact Byzantine fraction  $\delta < 0.5$.
Such mistake makes me doubt the correctness of the proof in this paper, but I do not have enough time to check the whole proof.

2. As argued in this paper, $ ζ_{max} \gg ζ_{mean} $, meaning that the method is only favourable when $\delta$ is very small, which seems to be not practical in the Byzantine workers setting. Moreover, since $C_{UH}(\zeta_{max})$ and $C_{MH}(\zeta_{mean})$ are different hypothesis classes, directly comparing rates seems to be improper. An analysis of MS in $C_{MH}(\zeta_{mean})$ is also needed.

3. Although the hyperparameter $\tau_t$ is adaptive to the Byzantine fraction $\delta$, it has to be be chosen according to $\zeta_{max}$, which is unknown in priori, so an inproper choice of $\tau$ could harm the performance of the algorithm. 
It would be favourable to provide an empirical way to choose $\tau_t$.

4. For the presentation of the paper, it would be clearer if the author provides a sketch of the proof rather than presenting directly some propositions.

### Questions
1. Could the authors comment more on the relation between $\zeta_{max}$ and $\zeta_{mean}$, particularly with some real datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
