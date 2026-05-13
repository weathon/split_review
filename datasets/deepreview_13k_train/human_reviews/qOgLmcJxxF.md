# Sample-Efficient Training for Score-Based Diffusion

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Score-based diffusion models have become the most popular approach to deep generative modeling of images, largely due to their empirical performance and reliability. Recently, a number of theoretical works \citep{chen2022, Chen2022ImprovedAO, chen2023probability, benton2023linear} have shown that diffusion models can efficiently sample, assuming $L^2$-accurate score estimates. 
The score-matching objective naturally approximates the true score in $L^2$, but the sample complexity of existing bounds depends \emph{polynomially} on the data radius and desired Wasserstein accuracy.  By contrast, the time complexity of sampling is only logarithmic in these parameters.  We show that estimating the score in $L^2$ \emph{requires} this polynomial dependence, 
but that polylogarithmic samples actually do suffice for sampling.  We show that with a polylogarithmic number of samples, the ERM of the score-matching objective is $L^2$ accurate on all but a probability $\delta$ fraction of the true distribution, and that this weaker guarantee is sufficient for efficient sampling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the sample complexity for estimating the score functions in the diffusion model sampling process. They establish a polynomial sample complexity under a robust measure they proposed in the paper. They also apply their results to the sampling procedure by incorporating the convergence rate of Benton et al 2023. Their technique might be helpful to improve the sample complexity bound for diffusion based algorithms.

### Strengths
This paper studies the sample complexity of estimating the score functions in diffusion model. To evaluate the estimation error, they propose a robust measure of distance. For their main result, they show that if the true score function can be approximated well using the function class $H$, and $H$ is finite, then $m = poly(d, 1 / \epsilon, 1 / \delta, N, \log |H| / \delta_{train})$ samples is sufficient for getting $\epsilon$ accuract simultaneously for all score functions. This rate does not require the target distribution is bounded, hence generalizes that of Block et al 2020.

### Weaknesses
1. The presentation lacks clarity, making it difficult to fully appreciate the paper's contributions. For instance, the relationship between the robust measure of distance and the convergence rate of the sampling procedure could be better explained. The authors should elaborate on how the proposed measure facilitates the improved sample complexity bound. Specific examples demonstrating the limitations of existing measures in this context would be beneficial. 
2. The absence of formal theorems in the main text is a significant drawback. While informal statements provide intuition, formal theorems with precise conditions and assumptions are crucial for rigor. The authors should include formal statements of their main results, including all necessary definitions and assumptions, in the main text. This would enhance the paper's credibility and facilitate a more thorough evaluation of the theoretical contributions. 
3. Corollary 1.1, while seemingly intuitive given the finite nature of $H$, lacks sufficient justification. The authors assert that it is not a straightforward consequence of the uniform law of large numbers, but they do not adequately explain why. A more detailed discussion is needed to clarify the challenges involved and how the proposed approach overcomes them. For instance, what specific aspects of the score matching objective or the structure of $H$ prevent the direct application of standard concentration inequalities? Providing concrete examples of how naive applications of the uniform law of large numbers might fail in this context would strengthen the motivation for Corollary 1.1.

### Questions
1. I think $m_2$ appears a lot before the authors define it as the second moment. 
2. I think the statement "approximates $q_0$ up to $\epsilon$ TV error and $\gamma$ Wasserstein-2 error" in introduction section is not accurate. As far as I am concerned, the right expression is "there exists a distributions $q$, such that $W(q, q_0) \leq \gamma$ and $TV(q, \hat q) \leq \epsilon$, where $\hat q$ is outputted by the diffusion model" (at least this is the case in Benton et al 2023). The authors might want to clearly state that to avoid causing confusion.  
3. What does it mean by "$H$ contains sufficiently accurate approximations to each score" in Corollary 1.1? 
4. What is the relation between the last sentence on page 3 and Theorem 1.2? Theorem 1.2 seems to be independent of training, why can we see from this theorem that our outlier-robust approximation suffices for sampling? 
5. Maybe the authors can comment a little bit on the polynomial dependency? Like what is the order of the polynomial. Block et al 2020 has an explicit polynomial dependency, and it is not clear if the results presented here is indeed better if the form of polynomial is not presented. 
6.  It is a little bit restrictive to assume $H$ is finite.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the complexity of training and sampling using score-based diffusion models. The authors focus on the sample complexity, i.e., the number of samples needed to reach a given accuracy measured e.g. in TV or Wasserstein-2 distance. The key result is an improvement from ${\rm poly}(R/\gamma)$ to ${\rm poly}\log(m_2/\gamma)$ samples, where $R$ is the bound on the norm of the distribution, $\gamma$ the required accuracy in Wasserstein-2 distance, and $m_2$ the second moment. The scaling with respect to the other parameters (input dimension, 1/accuracy in TV distance) remains polynomial.

The idea is to consider a less restrictive measure for the estimation of the score: instead of the L2 norm, the authors propose a form of quantile error in which regions with low probability are not considered. In fact, they authors show that the estimation of the score in L2 requires polynomially many samples in $1/\gamma$ via an explicit example.

### Strengths
* The improvement in the sample complexity in terms of the accuracy in Wasserstein distance is significant: from polynomial to logarithmic.

* The idea of using a different notion of distance to evaluate the error in the score estimation is new and could be useful more broadly when analysing score-based diffusion models. 

* I also appreciated the explicit counterexample on the difficulty of learning the score in L2.

### Weaknesses
 * The scope of the paper is quite limited. While the improvement in terms of accuracy in Wasserstein distance is remarkable, the dependency on the accuracy in TV remains polynomial. What's the point of improving drastically the accuracy in W2, if the accuracy in TV remains bad? For this reason, while I like the idea of using the quantile measure, the benefit of doing so in the context of score-based diffusion remains unclear.

* The complexity is also polynomial in $d$. Recent papers analysing diffusion models (see e.g. Table 1 in "Linear convergence bounds for diffusion models via stochastic localization") show that this dependency is linear or quadratic in $d$. I appreciate that the setting of this paper is different (most works assume access to a good L2 score, which is shown to be impossible if one sticks with a logarithmic dependency in $1/\gamma$). Nonetheless, the authors should track how the bound scales in $d$ and compare to existing work.

* It would also add value to the paper to track the dependency on something more explicit than the cardinality of the hypothesis class $|\mathcal H|$. Along the same lines, for the result on neural networks (Theorem 3.1), one needs to assume the existence of a network that approximates the score well enough.

* The novelty in terms of proof is not high. Basically the idea is to exclude a region with low probability and then use existing analyses (mostly, Benton et al., 2023). This is admittedly a minor point (simple ideas can be very useful!). The two key weaknesses above are the main reason of my score.

### Questions
Can the authors comment on the points raised above?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper shows that estimating the score in L2 requires this polynomial dependence, but polylogarithmic samples actually do suffice for sampling.

### Strengths
The investigation of sample complexity is a core issue in statistics literature. For modern generative models, it is quite interesting to see the sample dependency of these systems.

This paper find a good angle that it is not necessary to learn the score accurately 
Which is particularly challenging. This idea can help to justify the success of current diffusion models

### Weaknesses
The writing of the paper should be improved. It contains too much previous work and technical details. The contribution of this work are scattered.

Too many informal results, which makes readers hard to determine which parts are not rigorous.

The setting looks artificial compared to true score-based model.

### Questions
Take Figure 1 for example, in a real score-based model, we would not evaluate score near 0, because we construct the whole process from p to N(0,I). Then we only evaluate the score p_T near 0 rather than p_0. Since the p_T is highly smoothed, and the importance can also be reflected by the number of samples, the score is generally well-estimated in L2 sense. Otherwise the mixing of the algorithm is incorrect. In [1], it is shown that the score-based algorithm has a good mixing property. From this view, the proposed metric looks a bug, not feature?
Can you explain this?

I understand the challenges and hardness of learning L2, but there are still more examples needed to justify the new metric.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the sample complexity associated with training score-based diffusion models. It introduces an essential concept: the $1-\delta$ error, a more robust measure compared to the conventional L2 error metric. It is demonstrated that using the $1-\delta$ error, efficient training can be achieved with a sample complexity of poly($log (m^2/\gamma)$) when employing score matching.This new measure proves sufficient for enabling efficient sampling through reverse SDE.

### Strengths
1. The paper introduces the concept of the $1-\delta$ error as a more robust measure for diffusion models, which is a novel and innovative contribution to the field. This new measure offers an alternative approach to assessing score estimation precision;

2. The paper effectively addresses the crucial issue of sample complexity in training diffusion models. It recognizes the challenge of balancing score estimation accuracy with the number of required samples, providing insights into how to achieve efficient training.

3. By introducing the $1-\delta$ error as a foundational measure for future work, the paper provides a valuable reference point for researchers looking to advance the field of diffusion models.

### Weaknesses
I believe the presentation of this paper can be improved and there are several typos:
1. After equation (1) on page 1, it writes 'for Brownian motion $dB_t$', while $dB_t$ is NOT the Brownian motion (actually $B_t$ is);
2. On page 1, it writes $x_t\sim e^{-t} x_0 + N(0, \sigma_t^2), which seems like $x_t$ is restricted in $\mathbb{R}$, but after equation (2) it looks like $x_t$ is a process in $\mathbb{R}^d$ before $d$ is even defined;
3. Also on page 1, it writes 'logarithmic in $m_2/\epsilon$', where neither $m_2$ or $\epsilon$ is defined before. Actually $m_2$ is defined in Theorem 1.2 for the first time;
4. Equation (4) seems to refer to the minimizer, then it should be 'argmin ...' instead of 'min ...';
5. Before equation (5), I can understand what you mean by 'with norm bounded by R', but I think it's not a commonly used expression. Maybe you can try something like 'supported in B(0,R)' instead?
6. Before equation (6), we see $m_2$ again, still undefined;
7. After equation (6), 'to satisfy' should be 'to be satisfied' instead;
8. In Lemma 4.1, the parameter $\eta$ depends on $m$, while $m$ is defined in the proof;
9. In Lemma 4.1, I guess $\hat{\mathbb{E}}$ means the empirical expectation, but it is not defined in the paper.
10. In Theorem A.1, the notation of $s_r$, $s^*_r$, $\hat{s}_r$ and $\tilde{s}_r$ is a bit messy.
11. A typo! The title of Appendix D should be 'Utility Results' instead of 'Utility Resuts' I think.

### Questions
1. In the part named Our results, what's the intuition of 'one would like to show ... with poly($log \frac{m_2}{\gamma}$)'? Where does this poly($log \frac{m_2}{\gamma}$) come from?
2. In the remark after Corollary 1.1, it states that 'Corollary 1.1 doesn’t depend on the domain size at all'. But H contains sufficiently accurate approximations to each score. Does it mean that $|H|$ should be related to the domain size?
3. How is the discussion in section 4 related to that in Appendix D of [1]?
4. On page 5, it states that 'If x is bounded by some value $R$, then the score would be bounded by $R/\sigma^2$. Can you prove it or provide a reference? 
5. In Theorem A.1, what does it mean by 'r-smoothed version'?
6. In Theorem A.1, are $\hat{s}_r$ and $\tilde{s}_r$ different? It seems that in the proof you assume they are equal (but actually they are not I think).

[1] Holden Lee, Jianfeng Lu, and Yixin Tan. Convergence for score-based generative modeling with polynomial complexity. arXiv preprint arXiv:2206.06227, 2022.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
