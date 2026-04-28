# Learning Orthogonal Multi-Index Models: A Fine-Grained Information Exponent Analysis

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
The information exponent (\cite{ben_arous_online_2021}) --- which is equivalent to the lowest degree in the Hermite
  expansion of the link function for Gaussian single-index models --- has played an important role in predicting the 
  sample complexity of online stochastic gradient descent (SGD) in various learning tasks. In this work, we 
  demonstrate that, for multi-index models, focusing solely on the lowest degree can miss key structural details 
  of the model and result in suboptimal rates. 

  Specifically, we consider the task of learning target functions of form $f_*(\x) = \sum_{k=1}^{P} \phi(\v_k^* \cdot \x)$, 
  where $P \ll d$, the ground-truth directions $\{ \v_k^* \}_{k=1}^P$ are orthonormal, and only the second and 
  $2L$-th Hermite coefficients of the link function $\phi$ can be nonzero.  
  Based on the theory of information exponent, when the lowest degree is $2L$, recovering the directions requires 
  $d^{2L-1}\poly(P)$ samples, and when the lowest degree is $2$, only the relevant subspace (not the exact 
  directions) can be recovered due to the rotational invariance of the second-order terms. In contrast, we show that 
  by considering both second- and higher-order terms, we can first learn the relevant space via the second-order
  terms, and then the exact directions using the higher-order terms, and the overall sample and complexity of online 
  SGD is $d \poly(P)$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of learning an additive Gaussian multi-index model with know link function, where the directions in the multi-index model are orthonormal and the non-linearity only includes the Hermite polynomials of degree 2 and $2L$ for some $L \geq 2$. It is shown that when using online SGD on the squared loss, while looking at the 2nd degree Hermite polynomial is not sufficient for strong recovery of all directions, one can leverage the 2nd degree Hermite polynomial to weakly recover the subspace with $\tilde{O}(d)$ samples. From this weak recovery, once can use the higher-order Hermite term to strongly recover the individual directions in the multi-index model, while maintaining the $\tilde{O}(d)$ sample complexity.

### Strengths
The majority of theoretical work on learning high-dimensional Gaussian single/multi-index models focus on the importance of the first non-zero term in the Hermite expansion of the link function. It is nice to show that sometimes the higher order terms can be useful in the analysis.

### Weaknesses
My main concern with the current submission is its scope. Specifically, the picture presented here will never be relevant to functions with information exponent larger than 2, as Oko et al., 2024 show that only looking at the first non-zero term in the Hermite expansion is sufficient. Even if the information exponent is exactly 2, as Oko et al., 2024 argue, after the subspace is recovered with online SGD, it is possible to subtract it with quadratic activation from the multi-index model, thus obtaining a new model that has information exponent larger than 2.

I think while the current analysis is interesting, this submission could be more strengthened if we also had a story for other types of link functions with information exponent 2, e.g. $h_2 + h_3$. Also, moving from exactly orthogonal to approximately orthogonal weights and characterizing the effect of this approximate orthogonality can be another valuable contribution.

Some possible typos:

* What is $\epsilon_*$ and how does it relate to $\epsilon$ in Theorem 2.1?

* Is there a normalization step missing from Stage 1 of the algorithm in Section 2.3? Assuming there is a normalization step, then it seems the ODE in Line 278 is only considering the gradient step and not the projection. It is mentioned that the second term on the RHS comes from the projection, but it seems that the second term on the RHS is only coming from the higher degree Hermite term.

* I think $v_k = {v^*}_k^\top v$ has not been formally introduced before the equation in Line 278.

* $\Vert v_{\leq P}\Vert^2$ is missing from the numerator of the last in term in Line 304.

* It seems like the RHS of the equation in Line 352 must be $4L(1 - \Vert v_{\leq P}\Vert^2 + c_L(\Vert v_{\leq P}\Vert^2 - v_1^2))v_1^{2L} \geq 4Lc_L(\Vert v_{\leq P}\Vert^2 - v_1^2)v_1^{2L}$.

### Questions
Some possible typos:

* What is $\epsilon_*$ and how does it relate to $\epsilon$ in Theorem 2.1?

* Is there a normalization step missing from Stage 1 of the algorithm in Section 2.3? Assuming there is a normalization step, then it seems the ODE in Line 278 is only considering the gradient step and not the projection. It is mentioned that the second term on the RHS comes from the projection, but it seems that the second term on the RHS is only coming from the higher degree Hermite term.

* I think $v_k = {v^*}_k^\top v$ has not been formally introduced before the equation in Line 278.

* $\Vert v_{\leq P}\Vert^2$ is missing from the numerator of the last in term in Line 304.

* It seems like the RHS of the equation in Line 352 must be $4L(1 - \Vert v_{\leq P}\Vert^2 + c_L(\Vert v_{\leq P}\Vert^2 - v_1^2))v_1^{2L} \geq 4Lc_L(\Vert v_{\leq P}\Vert^2 - v_1^2)v_1^{2L}$.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors study the problem of learning multi-index models of the form $\sum_{k=1}^P {\rm He}_2 (z_k) + {\rm He}_L(z_k)$ where $L$ is even and greater than $2$ with a two layer neural network of width $m$. The training in the first layer is performed using online SGD and keeping the second layer fixed and small, while the second layer is learned at the end of training using linear regression.

Interestingly, the authors discover that in the training of the first layer there are two phases: first the subspaces are recovered, and then the individual directions are recovered.

### Strengths
The paper is exceptionally well written and easy to follow. The outline of the proof in sections 3 and 4 is incredibly clear, and it gives an insightful and intuitive picture of the different stages of learning.

The problem of studying this class of multi-index models is in my opinion incredibly important as they are instrumental in developing a theory of two layer networks, and studying the interaction between different terms in the Hermite expansion is an important piece that needs to be figured out.

### Weaknesses
I think the paper could greatly benefit from a set of numerical experiments implementing the algorithm in 2.3. The learning algorithm described in the paper is different from a standard gradient descent iteration in which one updates the weights in both the first and second layer together, and it's not clear to me if such a case will have qualitatively the same behaviour as what is presented. Additionally, I believe the assumption that the weights in the first layer evolve independently is not true in practice, and I would expect such interactions to be considered in future works. All of these points could have been addressed by a set of numerical experiments, which could have at least offered a justification for the assumptions taken in this work.

### Questions
1. Is it necessary to keep the weights in the first layer as a collection of orthonormal vectors? Would it be sufficient for them to be extracted from a Normal distribution?
2. Do you have some intuition of what happens if $a_0$ is not so small? As you state the dynamics of different weight vectors in the first layer are no more independent, but do you expect this to impact the qualitative behaviour you describe in your theorems? This could be explored numerically.
3. What would change if we were studying the model $\sum_{k=1}^P {\rm He}_2 (z_k) + {\rm He}_3(z_k)$?
4. What is the role of the regularisation $\lambda$ in learning the second layer? It's common not to regularise when training a two layer network. Could you comment on its role here?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work investigates the sample complexity of learning Gaussian multi-index functions of the type $f_{\star}(x) = \sum\limits_{k=1}^{P}\left(h_{2}(\langle v_{k}^{\star},x\rangle)+h_{2L}(\langle v_{k}^{\star},x\rangle)\right)$ with two-layer neural networks trained under a particular two-step spherical one-pass SGD scheme.

The main result is to show that this target can be strongly learned with this procedure with $\tilde{O}({\rm poly}(P))$ hidden-units and $\tilde{O}(d{\rm poly}(P))$ samples / steps, in contrast with the purely quadratic case where the target can only be weakly learned. This result stems from an asymptotic description of the training dynamics in two phases, the first where only a subspace is recovered, followed by a second phase where the exact directions $\{v_{k}^{\star}\}_{k=1}^{P}$ are retrieved.

### Strengths
The description of the time scales for the dynamics is interesting. The informal discussion of how the SGD argument can be derived from the GF analysis and "user-friendly" discussion of the martingale argument from (Ben Arous 2021) is a nice addition to the literature.

### Weaknesses
 - The setting studied is quite specific, and the focus on the information exponent without a broader discussion of the Gaussian multi-index literature can be misleading to the reader (see *Questions*).
- Overall, the manuscript is quite technical, which hinders clarity.

- The information exponent (IE) was introduced by Ben Arous et al., 2021 specifically in the context of characterizing the sample complexity of one-pass SGD for well-specified single-index models. While this concept was shown to be also relevant to the sample complexity in non-parametric settings (e.g. learning a single-index target with an infinite width 2-layer neural network, e.g. [Bietti et al. 2022] or [1,2]), there are a couple of works that already highlight that the information exponent is not a relevant concept beyond the rather specific scope for which it was introduced. For instance, Abbe et al., 2022 already points that is not sufficient to characterize strong learnability of multi-index functions, and other works show that the IE is not a robust concept to the change of algorithm even for weak learnability of single- and multi-index models [3, 4, 5, 6, Dandi et al., 2024, Damien et al., 2024, Lee et al., 2024]. In other words, it is already a consensus in the community that the IE is not a fundamental notion of computational complexity. For this reason, I find it is quite a stretch to motivate the result in this manuscript around this concept (e.g. as in the first bullet point in "*1.2 Our Contributions*").

- In line 280, is $k\in[d]$ a typo?
- I would suggest the authors to avoid using the same index for quantities which are in different ranges, e.g. $k\in [P]$ or $k\in[m]$ for target and model neurons. This could help readability of the technical parts.
- In this work, you consider a noiseless multi-index target. Would the strong recovery result holds true in the presence of label noise?
- The second sentence in the discussion in L99-103 on the differences with respect to Ben Arous et al., (2024) is confusing, specially in light of Appendix A. If the analysis rely on a reduction to tensor decomposition, the settings do not look so different after all. Maybe be more precise on what you mean by "not comparable".

### Questions
As the authors discuss in the introduction, the information exponent (IE) was introduced by Ben Arous et al., 2021 specifically in the context of characterizing the sample complexity of one-pass SGD for well-specified single-index models (a.k.a. generalized linear models). While this concept was shown to be also relevant to the sample complexity in non-parametric settings (e.g. learning a single-index target with an infinite width 2-layer neural network, e.g. [Bietti et al. 2022] or [1,2]), there are a couple of works that already highlight that the information exponent is not a relevant concept beyond the rather specific scope for which it was introduced. For instance, Abbe et al., 2022 already points that is not sufficient to characterize strong learnability of multi-index functions, and other works show that the IE is not a robust concept to the change of algorithm even for weak learnability of single- and multi-index models [3, 4, 5, 6, Dandi et al., 2024, Damien et al., 2024, Lee et al., 2024]. In other words, it is already a consensus in the community that the IE is not a fundamental notion of computational complexity. For this reason, I find it is quite a stretch to motivate the result in this manuscript around this concept (e.g. as in the first bullet point in "*1.2 Our Contributions*").

In my reading, one contribution of this work is to provide an explicit example of a non-staircase multi-index target where strong learnability is achieved with one-pass SGD in $\tilde{O}(d)$ steps, showing that the staircase structure of Abbe et al. (2022, 2023) is not a necessary property. This hierarchical "weak-to-strong" learning structure is interesting per se.

Below are some specific questions / suggestions:

- In line 280, is $k\in[d]$ a typo?
- I would suggest the authors to avoid using the same index for quantities which are in different ranges, e.g. $k\in [P]$ or $k\in[m]$ for target and model neurons. This could help readability of the technical parts.
- In this work, you consider a noiseless multi-index target. Would the strong recovery result holds true in the presence of label noise?
- The second sentence in the discussion in L99-103 on the differences with respect to Ben Arous et al., (2024) is confusing, specially in light of Appendix A. If the analysis rely on a reduction to tensor decomposition, the settings do not look so different after all. Maybe be more precise on what you mean by "not comparable".    

Some comments on the related literature:

- Reference [Lee et al., 2024] is concurrent to [4], please acknowledge both when referring to this result.   
- The statistical and computational sample complexity results for single-index models in Damien et al. (2024) generalize the ones from [3]. Please acknowledge this in the discussion in L44-47.
- In L47-48: beyond SGD, computational weak-learnability results for multi-index functions were derived in [5] for polynomials and in [6] general link functions but linear sample complexity.
- Convergence rates for gradient flow on multi-index targets were derived in [7]. The setting studied in this manuscript (which assumes a small learning rate with respect to the initial conditions) should be close to that. Can you comment the relationship to this?

**References**

- [1] Raphaël Berthier, Andrea Montanari, Kangjie Zhou. [Learning time-scales in two-layers neural networks](https://link.springer.com/article/10.1007/s10208-024-09664-9). Foundations of Computational Mathematics. 2024 Aug 22:1-84.
- [2] Yatin Dandi, Florent Krzakala, Bruno Loureiro, Luca Pesce, Ludovic Stephan. [How Two-Layer Neural Networks Learn, One (Giant) Step at a Time](https://arxiv.org/abs/2305.18270). arXiv:2305.18270 [stat.ML]
- [3] Jean Barbier, Florent Krzakala, Nicolas Macris, Léo Miolane, Lenka Zdeborová. [Optimal Errors and Phase Transitions in High-Dimensional Generalized Linear Models](https://www.pnas.org/doi/10.1073/pnas.1802705116). PNAS 2019
- [4] Luca Arnaboldi, Yatin Dandi, Florent Krzakala, Luca Pesce, Ludovic Stephan. [Repetita Iuvant: Data Repetition Allows SGD to Learn High-Dimensional Multi-Index Functions](https://arxiv.org/abs/2405.15459). arXiv:2405.15459 [stat.ML]
- [5] Sitan Chen, Raghu Meka. [Learning Polynomials of Few Relevant Dimensions](http://proceedings.mlr.press/v125/chen20a/chen20a.pdf). ICML 2020
- [6] Emanuele Troiani, Yatin Dandi, Leonardo Defilippis, Lenka Zdeborová, Bruno Loureiro, Florent Krzakala. [Fundamental computational limits of weak learnability in high-dimensional multi-index models](https://arxiv.org/abs/2405.15480). arXiv:2405.15480 [cs.LG]
- [7] Alberto Bietti, Joan Bruna, Loucas Pillaud-Vivien. [On Learning Gaussian Multi-index Models with Gradient Flow](https://arxiv.org/pdf/2310.19793). arXiv:2310.19793 [stat.ML]

### Soundness
4

### Presentation
3

### Contribution
3
