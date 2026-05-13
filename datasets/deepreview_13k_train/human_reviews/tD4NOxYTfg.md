# The Convergence of Variance Exploding Diffusion Models under the Manifold Hypothesis

- Decision: Reject
- Scores: 8, 6, 6, 6

## Abstract
Variance Exploding (VE) based diffusion models, an important class of diffusion models, have empirically shown state-of-the-art performance in many tasks. However, there are only a few theoretical works on the VE-based models, and those works suffer from a worse convergence rate $1/\text{poly}(T)$ than the $\exp{(-T)}$ results of Variance Preserving (VP) based models. The slow convergence rate is due to the Brownian Motion without the drift term and introduces hardness in balancing the different error sources. In this work, we design a new forward VESDE process with a small drift term, which converts data into pure Gaussian noise while the variance explodes. Furthermore, unlike the previous theoretical works, we allow the diffusion coefficient to be unbounded instead of a constant, which is closer to the SOTA VE-based models. With an aggressive diffusion coefficient, the new forward process allows a faster $\exp{(-T)}$ rate. By exploiting this new forward process, we prove the first polynomial sample complexity for VE-based models with reverse SDE under the realistic manifold hypothesis. Then, we focus on a more general setting considering reverse SDE and probability flow ODE simultaneously and propose the unified tangent-based analysis framework for VE-based models. In this framework, we prove the first quantitative convergence guarantee for SOTA VE-based models with probability flow ODE.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new forward Variance-Exploding stochastic differential equation (VESDE) process by including a drift term whose coefficient can be unbounded. The resulting VPSDE process that enjoys the faster $\exp(-T)$ convergence rate and the authors establish the first polynomial sample complexity result under a manifold hypothesis. The authors also propose a unified framework for VE-based models and obtain the first quantitative convergence results for VE models with probability flow ODE.

### Strengths
The paper introduces a drift term to balance out the beginning, discretization and score function errors, which allows the authors to establish faster forward convergence rate and a polynomial sample complexity for the reversed process. The newly proposed VESDE process could be of practical relevance as demonstrated on a toy 2-D example.

### Weaknesses
I'm wondering how important the manifold assumption is. Some discussion on this may be helpful.

### Questions
Is there a reason for using different metrics in Sections 5 (total variation) and 6 (Wasserstein)?

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
Score-based diffusion models have gained wide attention in recent years. Two common SDEs used are variance exploding SDE (VESDE) and variance preserving SDE. This paper proposes a new forward VESDE. Unlike the previous theoretical works that assuming constant diffusion coefficient, the paper allows unbounded coefficient that grows in time, which is closer to SOTA VE-based models. The new forward process allows a faster exponential convergence rate. The polynomial sample complexity is obtained for VE-based models with reverse SDE under the manifold hypothesis. The paper then proposes the unified tangent-based analysis framework for VE-based models, and the first quantitative guarantee for SOTA VE-based models with reverse PFODE is obtained.

### Strengths
The paper is relatively well written. The model, and the contributions are well stated. With the new VESDE forward process, the polynomial sample complexity is obtained for VE-based models with reverse SDE under the manifold hypothesis. Moreover, the first quantitative guarantee for SOTA VE-based models with reverse PFODE is obtained.

### Weaknesses
The forward process the paper proposes, to me, is just a small modification of variance preserving SDE with a parameter $\tau$. When $\tau=1$, it is exactly the well-studied variance preserving SDE in the literature. Because of that, it is not clear to me the advantage of proposing this new VESDE given that it seems to be quite similar to the VPSDE.

Moreover, since it is a small extension of the VPSDE, the paper should be more transparent about the technical contributions. What is the technical novelty and difficulty to extend the existing theoretical works in this field to allow this added parameter $\tau$. For example, Lemma 13, Lemma 14, Lemma 15 all come from De Bortolli (2022). The authors should make it more clear what is the novelty that arises from this new VESDE.

It is not clear the advantage of this new VESDE compared to VPSDE or other diffusion models. It would be helpful if the authors can compare the complexity with the existing literature to demonstrate theoretically that this new VESDE can indeed outperform or at least comparable to the existing models. What is more important is the paper lacks convincing numerical experiments. There is only a very small numerical section in the appendix about a 2-dimensional Gaussian distribution, which is not enough to suggest this new VESDE model is promising. Given that this VESDE is just VPSDE with an added parameter $\tau$, would it be possible for the authors to utilize the publicly available codes from the previous literature to see if it works well? Also, in terms of practice, it seems that it is quite often in the literature people simply take $T=1$. If that is the case, then you get $\tau=1$ which corresponds exactly to the VPSDE. The point is that without numerical experiments, it is not clear to me why this new VESDE is a good idea, and what advantage it can bring compared to VPSDE.

### Questions
In the abstract, please mention what T stands for so the readers who are not familiar with this field can understand it better.

On page 1, in the last paragraph, “the these models” is a typo.

On page 1, the description that “The VESDE corresponds to a Brownian motion” is not one hundred percent accurate in the sense that my understanding is that VESDE has a deterministic and non-trivial diffusion term in front of the Brownian motion. As a result, more rigorously speaking, VESDE is a Brownian motion with a (deterministic) time change.

On page 2, “We propose a new forward VESDE with the unbounded coefficient $\beta_{t}$ and a small drift term.” It is not clear to me whether this description is accurate. Maybe it is better to say “and a drift term that is typically small”? The reason is that in your model, you can choose $\beta_{t}=t^{2}$ and $\tau=T$. Under this choice, when $t$ is of the order $T$, the drift term can be large?

On page 6, it would be better if you can add some more detail about Assumption 3. Currently, you are saying “similar to (Chen et al. 2022; Benton et al. 2023)”, is your Assumption 3 exactly the same as in (Chen et al. 2022; Benton et al. 2023)? If yes, you can simply make it more transparent. If not, please comment on the difference.

On page 7, “We note that Theorem 2 has exponential on $R$ and $\delta$” did you mean “exponential dependence”?

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
The forward process, which has been the state-of-the-art in many tasks, is Variance Exploding based diffusion models. However, unlike VPSDE, it had the drawback of a slow convergence rate. Consequently, this paper introduces a new VESDE that exhibits a faster convergence rate. Additionally, it demonstrated the first polynomial sample complexity based on the realistic manifold hypothesis. Experimentally, it showed quantitative convergence guarantees for the state-of-the-art under such settings.

### Strengths
1. The introduction of a new forward VESDE process with an unbounded diffusion coefficient and a small drift term, allowing for faster convergence, is a valuable contribution.

2. The paper leverages the manifold hypothesis to achieve a polynomial sample complexity, providing practical insights for real-world applications.

3. The proposal of a unified tangent-based framework for analyzing VE-based models with probability flow ODE is a novel approach to address the convergence guarantee.

### Weaknesses
1. While the paper introduces new concepts and theoretical results, it would have been beneficial to have more specific experiments on datasets. The current experiments are limited in scope and do not fully demonstrate the practical advantages of the proposed method across diverse data modalities or complexities. For instance, it would be valuable to see results on more complex image datasets or other types of data, such as audio or time-series data, to assess the generalizability of the approach.

2. While it's understood that the introduced VESDE exhibits a faster convergence rate than VPSDE, there's no guarantee that it offers better fidelity. The paper does not provide a clear and comprehensive comparison of the sample quality achieved by the proposed VESDE compared to existing methods, particularly in terms of metrics like FID or IS scores when applied to image generation. It is crucial to demonstrate that the faster convergence does not come at the expense of the quality of the generated samples.

3. I find it puzzling whether the variance-exploding property has any utility beyond qualitative convergence guarantees. The paper does not clearly articulate the practical benefits of the variance-exploding property in the context of generation quality or other relevant metrics. It remains unclear how this property translates to tangible improvements in the performance of the model, beyond theoretical convergence rates.

### Questions
Please refer to Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes and studies the convergence of a variance-exploding diffusion model by introducing a small drift term and manifold hypothesis, and proves a faster exponential rate. The paper is mainly theoretical, and also includes numerical experiments to corroborate the theory.

### Strengths
The paper proposes a new variance exploding diffusion model, and proves under the manifold hypothesis that the underlying algorithm converges faster. The paper is mostly well written, and I enjoyed reading it. I have also checked part of the proofs, and they seem to be correct.

### Weaknesses
There are several weaknesses of this paper:

(1) It was claimed in the introduction that the underlying algorithm converges at rate $\exp(-T)$. However, upon looking at Theorem 2, there is a term which is linear in $T$ (under the Wasserstein distance). The authors may comment and explain this "discrepancy" -- otherwise it seems to be that the abstract is exaggerated. Specifically, the convergence rate of the reverse process, which is what is relevant for sampling, seems to be dominated by the discretization error, which scales polynomially with $T$, rather than the claimed exponential rate. The interplay between the forward and reverse processes, and how the exponential convergence rate of the forward process translates to the overall sampling performance, needs to be clarified.

(2) As the authors pointed out themselves, the analysis is similar to De Bortoli (2022). I understand that the technicality comes from analyzing the "tangent" process to avoid $\exp(T)$ term. The authors may highlight/summary the novelty earlier in the introduction. The specific technical contribution, beyond adapting existing techniques, needs to be made clearer. It's not immediately obvious what the key insight is that allows for the improved convergence rate.

(3) In most theorems/corollaries, the authors distinguish "aggressive" $\beta_t = t^2$, and "conservative" $\beta_t$'s (e.g. $\beta_t = t$). I wonder if there is some "phase transition" at exponent $2$ (i.e. $\beta_t = t^\alpha$ with $\alpha < 2$ and $\alpha = 2$). The authors may comment on this point. The theoretical implications of this distinction, and whether it represents a fundamental difference in the behavior of the diffusion process, should be discussed in more detail.

(4) Now all the experiments are deferred to appendix. I feel that the authors may lift some of experiments to the main text. (and put some proof techniques to appendix.) The paper would be significantly strengthened by the inclusion of key experimental results in the main body, demonstrating the practical impact of the theoretical findings. The current presentation makes it difficult to assess the empirical relevance of the proposed method.

### Questions
See the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
