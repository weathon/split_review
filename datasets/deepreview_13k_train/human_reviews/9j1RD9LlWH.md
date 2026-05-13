# Bayesian Optimization through Gaussian Cox Process Models for Spatio-temporal Data

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Bayesian optimization (BO) has established itself as a leading strategy for efficiently optimizing expensive-to-evaluate functions. Existing BO methods mostly rely on Gaussian process (GP) surrogate models and are not applicable to (doubly-stochastic) Gaussian Cox processes, where the observation process is modulated by a latent intensity function modeled as a GP. In this paper, we propose a novel maximum {\em a posteriori} inference of Gaussian Cox processes. It leverages the Laplace approximation and change of kernel technique to transform the problem into a new reproducing kernel Hilbert space, where it becomes more tractable computationally. It enables us to obtain both a functional posterior of the latent intensity function and the covariance of the posterior, thus extending existing works that often focus on specific link functions or estimating the posterior mean. Using the result, we propose a BO framework based on the Gaussian Cox process model and further develop a \nystrom approximation for efficient computation. Extensive evaluations on various synthetic and real-world datasets demonstrate significant improvement over state-of-the-art inference solutions for Gaussian Cox processes, as well as effective BO with a wide range of acquisition functions designed through the underlying Gaussian Cox process model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose a novel method to estimate the posterior mean and covariance of the gaussian cox process model.

They do this by first approximating the posterior $p(g|{t_i})$ via Laplace approximation, and then using BIC to further simplify the computation. This is in terms of $\hat g$, which must be solved for by minimizing Eq. 6. To do this, they use RKHS along with a transformation of kernel to make the problem computationally cheap to solve. Once this is done, the posterior mean and covariance can be estimated by $\hat g$ and the expression in Eq. (9). For kernels that cannot be expanded explicitly, they also discretize and use a Nystrom approximation.

With a way of estimating posterior mean and covariance, one now is free to choose an acquisition function for the specific problem being solved. The authors discuss various settings in which different acquisition can be applied within this framework.

Experiments are carried out showing both the modelling of the latent intensity, as well as the full framework applied in various spatiotemporal settings.

### Strengths
This paper claims to be the first work on BO using Gaussian Cox Process models. I could not disprove this claim through a short search, and if true, I think shows a clear strength in its originality. Every claim seemed technically sound and I could not find any glaring problems, and there were a myriad of experiments demonstrating the method in various synthetic and real world settings. The results present are qualitatively and quantitatively compelling, and the whole paper is relatively clear to understand and well written.

### Weaknesses
Because many other people have not used Gaussian Cox Process models for BO before, I wonder how much modelling the latent intensity actually helps. I did not see any results or discussion on this, but it feels like a useful comparison to make to show that using GCP is actually more performant than standard BO. It's unclear if the added complexity of modeling the latent intensity with a Gaussian Cox Process (GCP) truly provides a significant advantage over simpler methods for Bayesian Optimization (BO). Without a direct comparison to standard BO techniques, it's difficult to assess the practical benefits of this approach. The paper lacks a clear justification for why GCP is necessary, rather than simply being a more complex alternative. Furthermore, the paper does not explore the potential limitations of using a Laplace approximation for the posterior, and how this might affect the accuracy of the estimated posterior mean and covariance. The reliance on the Nystrom approximation, while computationally efficient, also introduces a potential source of error, and the paper does not provide a thorough analysis of how this approximation impacts the overall performance of the method. Specifically, the paper does not quantify the trade-off between computational efficiency and accuracy when using the Nystrom approximation. Finally, while the paper demonstrates the method on spatial-temporal data, it does not discuss the potential challenges or limitations of applying it to high-dimensional or very large datasets.

### Questions
-I'm slightly confused about Section 3.4 in that it seems like one can choose any acquisition function that would solve their problem. What about using Gaussian Cox enables us to do this in contrast to standard BO?

-Were there any experiments done which could find the posterior mean and covariance in closed form (without Nystrom approximation)? I don't have good intuition for how much expressivity is lost in doing this approximation.

-The paper analyzes this method on spatial-temporal data, but couldn't I use this method with any temporal data?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel framework for conducting BO by leveraging Cox processes. This approach hinges on a Laplace approximation of the likelihood and uses kernel techniques to transform the optimization problem into a RKHS. The framework is empirically evaluated across a range of scenarios, encompassing well-known synthetic functions and real-world databases. The results of numerical experiments indicate that this approach exhibits competitive performance in comparison to other state-of-the-art methods. Unlike the other frameworks, it stands out by enabling BO within the context of Cox process-based models.

### Strengths
Theoretical contributions bring together techniques from the machine learning and functional analysis communities. Lemmas and other theoretical developments can be easily verified thanks to the clarity of the discussions. The diversity of examples, which take into account well-studied synthetic functions and real databases, makes it possible to assess the competitiveness of the framework in relation to the literature. The paper is generally well-written and well-organized.

### Weaknesses
Although the strengths lie in both the theoretical and numerical aspects, the motivation for performing BO in point processes lacks practical utility. For example, in the spatio-temporal application describing tornadoes in the USA, I fail to see how new events (tornadoes involving damage) can be sampled sequentially to promote active learning of the intensity function $\lambda$. I assume that for illustrative purposes, the authors considered adding the "closest event" available in the database that matches the BO's suggestion. Is this correct? If this is the case, and if the size of the database allows tractable implementations, we can consider all events for inference of $\lambda$. If the model cannot handle the whole database, the BO schema is an interesting idea that promotes a threshold between inference quality and the number of observed point events. However, what can be done if no similar events are recorded in the database?  Can the authors give further details on the practical utility of their framework?

The authors have suggested publishing the Python codes in a Github repository, but there is no evidence of their existence. I suggest sharing an anonymous repository (e.g. via https://anonymous.4open.science/) for further examination.

**Questions**
- Are the results in Table 2 consistent, i.e. similar results are obtained for a different seed? If no, the authors must consider several random replicates and provide the mean +- std of the results
- In Figure 2, at the initial step, the UCB acquisition function suggests adding new events at $t > 90$ (since we seek to maximize such criterion) but they are added somewhere else. Similarly, in step 14, the UCB targets the instants around $t = 40$ but events are again added somewhere else. Besides the authors argue that "the algorithm keeps sampling by maximizing UCB acquisition function and then improving the estimation based on new samples observed", the plots do not validate their point. Can the authors further explain the results while clarifying my concern? Is it possible to add extra plots at consecutive steps (e.g. steps 1 and 2) for a better understanding of the BO's choice?
- In the experiments, the choice of the hyperparameters $w_1, w_2, w_3$ is not discussed. Can the authors precise their values in each experiment and explain how they were tuned? 
- The authors approximate the integral $\int_{\mathcal{S}} \kappa(g(t)) dt$ using an $m$-partition Riemann sum to obtain a closed-form of the posterior covariance. Since such approximation depends on $m$, can the authors discuss the quality of the approximation in terms of $m$ and precise how they tune that value in the experimental setup? Can they also discuss the scalability of the approximation when $d$ increases?
- The limitations of the proposed framework are not discussed in the paper. Can the authors add a remark on this subject?

**Other minor remarks**
- Page 3, Table 1: the derivatives of the link functions need to be checked. For instance, $\dot{\kappa}(x) = 2x$ (quadratic case), $\dot{\kappa}(x) = \frac{e^{-x}}{(1+e^{-x})^2}$ (sigmoidal), $\ddot{\kappa}(x) = \frac{e^{-x}}{(1+e^{-x})^2}$ (softplus), ...
- Page 3, Section 3.1: $\Sigma$ is a **CO**variance
- Page 3, Section 3.1, after Eq. (2): $\lambda(t) = \kappa(g(t)) \to \lambda(t)$ (it has been already defined before Eq.(1) )
- Page 4, after Eq. (7): However, Equation equation (7)
- Page 4, after Eq. (8): $\eta_i$ and $\phi_i(\cdot)$ need to be defined in the main part of the paper (they were defined in the supplementary material)
- Page 5, Eq. (10): $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_m)$ needs to be defined
- Page 7, Section 4: To precise that further details on the "evaluation setup" are given in Appendix G
- Page 7, Section 4.1.1: to indicate the number of events considered in each toy example
- Page 9, Figure 5: to indicate the iteration step in each panel
- In Appendix C, Eq. (26): $h(t_j) = \langle h, \tilde{k}(t_j, \cdot) \rangle_{\mathcal{H}_{\tilde{k}}}$ ($j$ rather than $i$)
- In Appendix C, Eq. (32): the first line must be $\sum_{i=1}^{n} \log(\kappa(g(t_i))) - \sum_{j=1}^m \kappa(g(t)) \Delta t$. Then, the sign of $\ddot{\kappa}^2(\hat{g}_i) \Delta$ must be inverted.
- In Appendix C, Eq. (32): given the proposed notation, it is not clear that the dimension of $\nabla_{\hat{g}}^{2} \Psi(\hat{g})$ matches the dimension of the $d \times d$ matrix $\Sigma$. Can the authors clarify this and/or propose a more readable notation?
- In the References: laplace $\to$ Laplace (Illian et al., 2012), bayesian $\to$ Bayesian (Kim, 2021), to add all the authors in (Lai et al., 1985), to complete the reference (Stanton et al., 2022), to be consistent with the names of the journals and conferences and the style of displaying them.

### Questions
**Questions**
- Are the results in Table 2 consistent, i.e. similar results are obtained for a different seed? If no, the authors must consider several random replicates and provide the mean +- std of the results
- In Figure 2, at the initial step, the UCB acquisition function suggests adding new events at $t > 90$ (since we seek to maximize such criterion) but they are added somewhere else. Similarly, in step 14, the UCB targets the instants around $t = 40$ but events are again added somewhere else. Besides the authors argue that "the algorithm keeps sampling by maximizing UCB acquisition function and then improving the estimation based on new samples observed", the plots do not validate their point. Can the authors further explain the results while clarifying my concern? Is it possible to add extra plots at consecutive steps (e.g. steps 1 and 2) for a better understanding of the BO's choice?
- In the experiments, the choice of the hyperparameters $w_1, w_2, w_3$ is not discussed. Can the authors precise their values in each experiment and explain how they were tuned? 
- The authors approximate the integral $\int_{\mathcal{S}} \kappa(g(t)) dt$ using an $m$-partition Riemann sum to obtain a closed-form of the posterior covariance. Since such approximation depends on $m$, can the authors discuss the quality of the approximation in terms of $m$ and precise how they tune that value in the experimental setup? Can they also discuss the scalability of the approximation when $d$ increases?
- The limitations of the proposed framework are not discussed in the paper. Can the authors add a remark on this subject?

**Other minor remarks**
- Page 3, Table 1: the derivatives of the link functions need to be checked. For instance, $\dot{\kappa}(x) = 2x$ (quadratic case), $\dot{\kappa}(x) = \frac{e^{-x}}{(1+e^{-x})^2}$ (sigmoidal), $\ddot{\kappa}(x) = \frac{e^{-x}}{(1+e^{-x})^2}$ (softplus), ...
- Page 3, Section 3.1: $\Sigma$ is a **CO**variance
- Page 3, Section 3.1, after Eq. (2): $\lambda(t) = \kappa(g(t)) \to \lambda(t)$ (it has been already defined before Eq.(1) ) 
- Page 4, after Eq. (7): However, Equation equation (7)
- Page 4, after Eq. (8): $\eta_i$ and $\phi_i(\cdot)$ need to be defined in the main part of the paper (they were defined in the supplementary material)
- Page 5, Eq. (10): $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_m)$ needs to be defined
- Page 7, Section 4: To precise that further details on the "evaluation setup" are given in Appendix G
- Page 7, Section 4.1.1: to indicate the number of events considered in each toy example
- Page 9, Figure 5: to indicate the iteration step in each panel 
- In Appendix C, Eq. (26): $h(t_j) = \langle h, \tilde{k}(t_j, \cdot) \rangle_{\mathcal{H}_{\tilde{k}}}$ ($j$ rather than $i$)
- In Appendix C, Eq. (32): the first line must be $\sum_{i=1}^{n} \log(\kappa(g(t_i))) - \sum_{j=1}^m \kappa(g(t)) \Delta t$. Then, the sign of $\ddot{\kappa}^2(\hat{g}_i) \Delta$ must be inverted.
- In Appendix C, Eq. (32): given the proposed notation, it is not clear that the dimension of $\nabla_{\hat{g}}^{2} \Psi(\hat{g})$ matches the dimension of the $d \times d$ matrix $\Sigma$. Can the authors clarify this and/or propose a more readable notation?
- In the References: laplace $\to$ Laplace (Illian et al., 2012), bayesian $\to$ Bayesian (Kim, 2021), to add all the authors in (Lai et al., 1985), to complete the reference (Stanton et al., 2022), to be consistent with the names of the journals and conferences and the style of displaying them.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper seeks to build a novel Bayesian Optimization approach that is based on Gaussian Cox Processes for spatio-temporal data. The authors emphasize that Gaussian Cox Processes have never been used within BO settings. The posterior distribution is computed using Laplace approximation and a change of kernel that enables to transform the inference problem into a kernel regression problem. The latter kernel is computed using Nyström approximation. Then the authors present several acquisition functions that are built using posterior mean and posterior variance of the Gaussian Cox Process. Finally the authors illustrate the efficiency of their approach on two types of experiments. First, they show the quality of the mean estimation on synthetic data (4.1.1) and real word data (4.2.1). Second, they show how the BO with UCB function performs for some synthetic dataset (4.1.2) and real world dataset (4.2.2).

### Strengths
The paper is well written and the overall approach is scientifically sound and compelling. 
The motivation is clear, which is to provide a BO framework with Gaussian Cox processes.
Although Laplace approximation is a standard tool, the authors provide an elegant way to derive the maximum of the log likelihood through a trick that transform the problem into a standard kernel regression problem so that they can use the representer theorem. The main results are clearly detailed. The use of Nystrom approximation is standard, but Lemma 3 helps the reader to figure out what has been implemented. 
The numerical experiments section show that the authors made great effort to compare all the components of their methodology with some of the state-of-the-art approaches. In addition, this has been done for simulated data and real-world data.

### Weaknesses
Although the paper is well written and has many interesting components, there are a couple of points that need to be detailed.

Major comments:

- My first question is general. In a standard BO setting, we aim at minimizing a function which is costly to evaluate. It seems that this is not the objective of the presented BO problem, as the focus appears to be on modeling the spatio-temporal intensity of events using a Gaussian Cox Process. It would have been good to make a clear distinction between the two problems, clarifying how the proposed approach addresses the typical BO objective of minimizing a costly function, and how the Gaussian Cox Process model contributes to this objective in the context of spatio-temporal data.

- In the literature review, the authors write that "existing works mostly concentrate on the mean estimation". I am not an expert in Cox models, but it seems that the problem of Bayesian Optimization for Gaussian Cox Processes has been investigated in [1]. This means that this approach could have also been tested in the numerical experiments with Bayesian Optimization. It also seems that this cited paper uses some tools (Laplace approximation, eigenfunctions decomposition) similar to the ones in the paper. Would it be possible to highlight the main modeling differences with this paper? What is the theoretical/computational benefit of the paper's approach compared to the cited paper? Specifically, how does the proposed change of kernel technique and the use of the representer theorem provide advantages over the path integral formulation used in [1]?

- In Equation (5), the authors claim that the rest of the terms of the likelihood are dominated by the first term when $n$ is large. However, this assumption is not always true in a BO setting (it is not in the numerical experiments), especially in scenarios where data acquisition is expensive and the number of samples remains relatively small. Could the authors comment that point and provide more details? A more rigorous justification for neglecting these terms, particularly in the context of limited data, would strengthen the paper.

- The authors claim that they can use the Nystrom approximation to compute the next approximation from new samples in an incremental fashion. Is this step used in the experiment? How does it work in practice? A more detailed explanation of the incremental update procedure and its practical implementation would be beneficial.

Minor comments:

- After reading the proof of Lemma 2, there is a point I did not understand. Why does the function $h$ belong to $\mathcal{H}$? This fact does not look straightforward to me. Perhaps I missed something in the development. A clarification on how $h$ is constructed and its membership in the RKHS $\mathcal{H}$ would be helpful.

- In the numerical experiments, the authors do not report the results of PIF in Table 2. Is there a reason for that? I've not found it in the paper.

- In figure 2c, it looks like the maximum of the acquisition function is around t=40. This means that we have to sample around $t=40$. However I don't see any sample around $t=40$ in figure 2d. Could the authors elaborate on the sampling process and explain this apparent discrepancy?

### Questions
See questions above.
Is the code publicly available?
Depending on author responses, I would change my score.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
