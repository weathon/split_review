# Sampling Multimodal Distributions with the Vanilla Score: Benefits of Data-Based Initialization

- Decision: Accept
- Scores: 6, 8, 3, 8

## Abstract
There is a long history, as well as a recent explosion of interest, in statistical and generative modeling approaches based on \emph{score functions} --- derivatives of the log-likelihood of a distribution. In seminal works, Hyv\"arinen proposed vanilla score matching as a way to learn distributions from data by computing an estimate of the score function of the underlying ground truth, and established connections between this method and established techniques like Contrastive Divergence and Pseudolikelihood estimation. It is by now well-known that vanilla score matching has significant difficulties learning multimodal distributions. Although there are various ways to overcome this difficulty, the following question has remained unanswered --- is there a natural way to sample multimodal distributions using just the vanilla score? Inspired by a long line of related experimental works, we prove that the Langevin diffusion with early stopping, initialized at the empirical distribution, and run on a score function estimated from data successfully generates natural multimodal distributions (mixtures of log-concave distributions).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies vanilla score matching in the context of mixtures of log-concave distributions, providing a recipe to learn multimodal distributions via vanilla score matching, a procedure that has provably failed in most multimodal settings: (1) data-based initialization for the Langevin Monte Carlo chain; and (2) early stopping of the diffusion. The work demonstrates substantive theoretical developments for the proposed method, along with a few toy examples to illustrate the effectiveness of empirical distribution initialization and early stopping in learning mixture of Gaussians.

### Strengths
1. This work aims to tackle a widely accepted issue of vanilla score matching that motivated the usage of annealed langevin dynamics in learning multimodal distributions (diffusion models as a class of generative models) — it has the potential to inspire new algorithms for generative modeling.
2. Code for the toy examples is provided via **Supplementary Material** to facilitate reproducibility.

### Weaknesses
1. Experiment results do not appear to be convincing enough:
* The ground truth distribution is not plotted in Figure 1 (b); by comparing to Figure 1(c), it’s not hard to tell that the weight of the component on the right is not learned very well — one has a density around $0.15$, while the other around $0.125$. Meanwhile, there is no numerical computation on the learned mean and variance of each component, and how they compare to the ground truth. It is unclear how the method performs in terms of accurately capturing the parameters of the mixture components, which is crucial for assessing the quality of the learned distribution. The lack of quantitative evaluation makes it difficult to assess the method's performance beyond visual inspection.
* Similar to the issue in Figure 1, the values of the learned projected mean, variance and weight of each component, and their comparisons with the ground truth distribution, are not reported for the experiment presented in Figure 2. The absence of these quantitative metrics makes it challenging to objectively evaluate the method's performance in higher dimensions. The paper should provide a more rigorous evaluation, including metrics that directly quantify the accuracy of the learned parameters.
2. It’s not clear how or where early stopping is proposed as a solution throughout the theoretical development. The theoretical analysis does not explicitly incorporate the concept of early stopping, making it difficult to understand how the theoretical results support the empirical findings. The connection between the theoretical framework and the practical implementation of early stopping needs to be clarified.
3. Some minor issues in writing:
* Page 1, first bullet point of positive aspects: “a simple closed form solution <when> the class of models”
* Page 3, the line above **Theorem 1**: “samplling”
* Page 3, strange expression: “Note in particular that we have can draw as many samples as we like”. Perhaps remove “have”?

### Questions
1. Could the authors comment on how the contributions in this work might help in improving diffusion models as a class of generative models?
2. Can optimization techniques such as exponential decay learning rate schedule achieve similar results as early stopping, in the context of estimating vanilla score function of a multimodal distribution?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes Langevin sampling with approximate scores, given some samples of the target distribution are provided.  It is shown that the scheme initialized from a uniform distribution over the available data points generates a sample close to the target in TV distance when stopped at a finite time T. The considered targets are mixtures of strongly log-concave measures and the paper's focus is on showing that with data based initialization, it is possible to remove the dependence on the LSI constant of the whole mixture in Theorem 2.1 of [1] which studied the same scheme.

---
[1] Lee, Holden, Jianfeng Lu, and Yixin Tan. "Convergence for score-based generative modeling with polynomial complexity." Advances in Neural Information Processing Systems 35 (2022): 22870-22882.

### Strengths
*The paper formalizes an intuitive result*: Sampling from mixtures is difficult because it is hard to transition in reasonable time from one component to another. If it was known where the mixtures were as well as their relatives weights, then no transitioning would be necessary and sampling could easily be achieved by initializing inside the components' typical sets. This intuitive natural idea (dismissed as too obvious/unrealistic in [1] sec 1.2)  is what is formalized in the paper. Although the result is not very surprising, the authors go through the laborious task of linking the components needed to establish the result: data based initialization with the existing analyses on approximate scores(or inexact langevin) and discretization of langevin diffusions. 

 *A clear and easy to follow proof outline*: There is a nice simple setting that is detailed in the main text to understand the paper's strategy, which is quite useful since the paper's result requires lengthy combinations of several results.

---
[1] Lee, Holden, Andrej Risteski, and Rong Ge. "Beyond log-concavity: Provable guarantees for sampling multi-modal distributions using simulated tempering langevin monte carlo." Advances in neural information processing systems 31 (2018).

### Weaknesses
- *Structure and unconvincing arguments*: Some sections could be better restructured namely section 1.2. It jumps from motivation to related work to possible extensions. Some remarks can also feel a little unconvincing there. For example, computational hardness arguments are invoked in the motivation but the main idea of noised score learning is to have an annealing scheme where the denoising is only performed from one noise level to a slightly lower noise level. Annealing breaks down the difficulty of denoising, so the paragraph is criticizing an alternative that is never used. A further minor point: remark 5 is an excessively long paragraph to say the mean is not in the typical set in high dimensions.
- *Log sobolev constant for well connected mixtures* : A contribution of the paper is extending the Poincare inequality through decompositions result of Madras & Randall (2002) to the log sobolev inequality. It would be very surprising if such an extension has not already been done as the result is old and functional inequalities are heavily researched. I would kindly ask the authors to check and possibly include references to ensure that they are not missing prior work.
- *On significance*: For the MCMC community this result will not be worthwhile as samples aren't available. For generative modeling where there is a dataset, the better modelling of what practitioners do uses time-varying score functions and so what is done in practice does not correspond to Langevin with a time independent score. The "long line" of experimental work that uses vanilla langevin is claimed to exist but never cited. The paper answers a small interesting curiosity related to data based initialization for sampling from mixtures with limited links with practice.

### Questions
- *Number of samples needed, Proposition 23 (and 24)*: From my understanding, for the approach to work, the available samples must have the correct weights of the components. Could the authors explain why the $M$ does not seem to depend on properties of $\mu$ besides the number of components ?
- *Samples to train and samples to initialize*: Presumably the approximate score is learnt from the same available samples $M$ used to initialize. This dependence could break some concentration arguments. Could the authors briefly discuss whether it is necessary to hold out some samples for initialization when learning the score ?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper utilizes the vanilla score-matching to sample from multimodal distributions. They also show that initialization using data  can help the score matching the ground truth distribution.

### Strengths
Sampling from multimodal distributions is an extremely interesting problem.

### Weaknesses
 - This paper is poorly written and very hard to read and follow. It constantly jumps around. It feels like you are reading lecture notes rather than a paper. The main contribution is hidden in many topics that can easily be moved to the appendix.

- Lack of comprehensive experimental results and applications to real-world data and high dimensional data.

- Lack of comparison to other bounds and theoretical results.

- This paper's analysis relies on idealized assumptions, including the exact knowledge of the score function and the assumption that the ground truth distribution is supported within a specific radius. These assumptions might not hold in real-world scenarios, limiting the practical applicability of the results. 

- The method relies on various parameters such as $\delta$ (overlap parameter), $H$ (tuning parameter), $\epsilon$ (error threshold), and step size $h$. The sensitivity to these parameters could make the approach highly sensitive to the choice of initial conditions and hyperparameters, making it challenging to justify the generalization of the method across different datasets or scenarios. 

- As mentioned earlier,  the analysis focuses on an idealized scenario and might not directly translate to real-world applications. The conditions and assumptions required for the analysis might be too strict or unrealistic for practical use cases, limiting the method's applicability in real-world data analysis or machine learning tasks.

- The analysis briefly touches upon the scenario where the score function is estimated from data. In practice, obtaining a precise score function estimation can be a challenging task and might introduce significant errors in the analysis.

- The passage does not provide a comprehensive comparison with existing methods or techniques in the field. Without a clear comparison, it's challenging to assess the novelty and superiority of the proposed approach over existing state-of-the-art methods for similar tasks. The analysis primarily focuses on theoretical aspects and lacks empirical validation on real datasets.

### Questions
- How does it compare to other bounds? it seems like this bound provides this on average and not the worst-case. In addition, it is mentioned in previous work: "in high dimensions, it will not be anywhere close to the ground truth distribution unless we have an exponentially large number of samples", how is it not the same case in their paper as well?  Furthermore, What is the computational complexity?
 - The analysis starts with several idealized assumptions, including the exact knowledge of the score function and the assumption that the ground truth distribution is supported within a specific radius. These assumptions might not hold in real-world scenarios, limiting the practical applicability of the results. Could the author please elaborate on that? 
- The method relies on various parameters such as $\delta$ (overlap parameter), $H$ (tuning parameter), $\epsilon$ (error threshold), and step size $h$. How can one justify the generalization of the method across different datasets or scenarios due to the fact that sensitivity to these parameters could make the approach highly sensitive to the choice of initial conditions and hyperparameters, making it challenging? 
- As mentioned earlier,  the analysis focuses on an idealized scenario and might not directly translate to real-world applications. The conditions and assumptions required for the analysis might be too strict or unrealistic for practical use cases, limiting the method's applicability in real-world data analysis or machine learning tasks. How does this work can be applied in practice? How does it apply to high-dimensional data? Experimental results with high-dimensional data are required to show the efficacy of the procedure. 
- The analysis briefly touches upon the scenario where the score function is estimated from data. In practice, obtaining a precise score function estimation can be a challenging task and might introduce significant errors in the analysis.
- The passage does not provide a comprehensive comparison with existing methods or techniques in the field. Without a clear comparison, it's challenging to assess the novelty and superiority of the proposed approach over existing state-of-the-art methods for similar tasks. The analysis primarily focuses on theoretical aspects and lacks empirical validation on real datasets.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is a theoretical work that addresses the problem, known from the literature, affecting vanilla score matching approaches to learn multimodal distributions from data.
The key idea is to rely on vanilla score matching, and prove that a Langevin diffusion process with early stopping, appropriately initialized at the empirical distribution, successfully generates multimodal distributions.
This result builds on several empirical works that show ways of overcoming the difficulty of using vanilla score functions for the estimation of multimodal distributions, and has the merit of being theoretically sound and -- to some extent -- practical.

### Strengths
* I really liked the pedagogical structure of the paper, which is akin to a different kind of literature such as applied mathematics, or conferences on learning theory. The main result is stated, a positioning of the work with respect to both theory and practice is clearly outlined, and open questions are discussed, in a succinct manner. Then, the bulk of the article revolves around the proof strategy used to arrive at the main theorem in the paper.

* I think there are nice connections with recent work such as [1], which deal with methods to factorize the data distribution into a product of conditional probability distributions that are strongly log-concave. Ultimately, the goal is to discover ways of using the vanilla score matching to sample from simpler distributions whereby the noise injection that is typical for score-based generative models is not needed.

* To the best of my understanding, the technical strategy used to prove the main result is correct, well developed and clearly exposed (in the main paper)

[1] Florentin Guth and Etienne Lempereur and Joan Bruna and Stéphane Mallat, Conditionally Strongly Log-Concave Generative Models, ICML 2023

### Weaknesses
 * I think there is some room for improvement in the overall narrative and exposition of the paper (there are a few typos, easy to fix and not problematic for the technical understanding).
First of all, the assumption that the score is easy to compute and, in particular for some data distributions it can be analytically available, should be emphasized more. Essentially, this work side-steps the problems of learning the score function alltogether: despite citing the seminal work from Hyvarinen 2005, the authors chose not to bring to the readers' attention the fact that in practical cases, even the vanilla score can be hard to compute, as it can require costly computations of the trace of the Hessian of the parametric score, which derives from a rewrite of the Fisher divergence. So, I think it is important to mention that the parametric score function does not come for free in general settings.

* The main results in the paper requires very important ``ingredients'':
1. An early stop mechanism, to set the Langevin Monte Carlo process evolution to stop at a very well defined diffusion time. There is no discussion about the practical implications of the tight bound on $T$ derived in Theorem 1, which is exponential in the data complexity (in the case of the paper, this takes the form of the number of mixture components $K$)

2. The tight bound on step size for the simulation of discrete-time Langevin dynamics decreases exponentially with the data complexity. Although this is not surprising, the more complex the data, the finer-grained your simulation should be, I think a discussion on practical implications is in order.

3. The quality of the approximation of the parametric score function is an assumption that is, in my opinion, very strong, and hardly achievable in practice. This is not a problem in the ``simple'' setting of this work, where data is assumed to be a mixture of $K$ log-concave, smooth components, which is needed to come up with a feasible proof strategy. However, in reality, parametric score functions can only approximate the true score.

4. The number $M$ of i.i.d. samples required to define the initial condition of the discrete Langevin process is not discussed appropriately. From Theorem 1, it seems to me that we need a fairly large number of samples, but I must confess I had a hard time finding the impact of $M$ on the proof strategy outlined in Section 2 of the paper. 

* Experiments are weak. Of course we are not talking about using the typical datasets that the current literature on score-based generative modeling. As an example, the results displayed in Figure 2 could have been commented more in the optic of explaining the relation to the above 4 points. Some hints are available in Appendix I, such as details on the learning procedure for the vanilla score network, but I still find it hard to relate such technical details to the hypothesis required for Theorem 1 to be valid.

* [minor weakness] The editorial format of the paper is somehow unconventional. There is no conclusion, and a large fraction of the real-estate available on the 9 pages is dedicated to material that often is given a prime spot in the appendix. If on the one hand I like this presentation style, as it is really helpful to go through the proof strategy detail, the downside is that it substract space to provide more insights on experiments, outline conclusion and compare to prior (albeit experimental) work upon which the authors have drawn inspiration.

### Questions
Besides asking authors to provide comments, explanations and eventually additional details for the three main weaknesses discussed above, I have the following question:

* A recent paper [2] studies discrete Langevin processes with approximate scores, and (very informally speaking) also finds that the approximation quality of the distribution obtained by the Langevin process can ``drift away'' in KL terms, from the true distribution if the simulation time $T$ is too large. Do you think there are connections that your work could draw to improve the discussion on the early stop mechanism you devise?

[2] Kaylee Yingxi Yang and Andre Wibisono, Convergence of the Inexact Langevin Algorithm and Score-based Generative Models in KL Divergence, arXiv 2211.01512

** Post rebuttal feedback **
The authors engaged in discussions about my concerns and made an effort to improve their paper. For these reasons I raised my score.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
