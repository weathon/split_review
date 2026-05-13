# Annealing Flow Generative Model Towards Sampling High-Dimensional and Multi-Modal Distributions

- Decision: Reject
- Scores: 6, 3, 3, 5, 1

## Abstract
Sampling from high-dimensional, multi-modal distributions remains a fundamental challenge across domains such as statistical Bayesian inference and physics-based machine learning. In this paper, we propose \textit{Annealing Flow} (AF), a continuous normalizing flow-based approach designed to sample from high-dimensional and multi-modal distributions. The key idea is to learn a continuous normalizing flow-based transport map, guided by annealing, to transition samples from an easy-to-sample distribution to the target distribution, facilitating effective exploration of modes in high-dimensional spaces. Unlike many existing methods, AF training does not rely on samples from the target distribution. AF ensures effective and balanced mode exploration, achieves linear complexity in sample size and dimensions, and circumvents inefficient mixing times. We demonstrate the superior performance of AF compared to state-of-the-art methods through extensive experiments on various challenging distributions and real-world datasets, particularly in high-dimensional and multi-modal settings. We also highlight AF’s potential for sampling the least favorable distributions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposed a so-called Annealing flow (AF) sampling method for  high-dimensional multi-modal distributions.  The key idea is to learn a continuous normalizing flow (CNF)  based transport map, guided by annealing process, to transition samples from an easy-to-sample distribution to the target distribution. The feature of  AF training does not rely on samples from the target distribution. The results in dimensional up to 50  show that AF ensures effective and balanced mode exploration, especially for multi-model distribution by comparing  AF to other SOTA methods though various challenging distributions, particularly in high-dimensional and multi-modal settings, including  AF’s potential for sampling the least favorable distributions.

### Strengths
The paper present a continuous Normalizing flow  based method for sampling from challenging high dimensional multi-modal distributions.  There are some theoretically insights on the proposed models using the  predefined intermediate and the numerical results show the superiority of the proposed sampling method under variety of criteria.

### Weaknesses
1. The details of training process is missing. Especially, the cost of the training process of CNF flow is not mentioned,  and also how many intervals are needed in order to obtain a stable sampling process. It seems also crucial especially how the overall sampling results depend on the flow interval. 

2. It is unclear how the method can be generalized to real high dimensional problems arising from real applications and distribution free problems where only samples are available. 

3. The sample efficiency (both sampling speed and quality) is not commented and compared with different methods.

### Questions
1. The author should explain  the detail of training  including how the minimization problem is solved and how the parameters would affect the sampling performance. 
2. Comments or preliminary results  on how it can appplied to any real high dimensional applications (>>50), for example a real physical machine learning problem. 
3. Other comparisons results in terms of computational cost.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to fit continuous normalizing flows (CNFs) to multi-modal unnormalized target distributions using annealing and optimal transport techniques. The proposed method first defines a sequence of annealed distributions interpolating the target distribution and a simple base distribution. Leveraging the dynamic optimal transport objective, the authors propose to train a sequence of CNFs to model the transition between each pair of neighboring annealed distributions. This method encourages the model to explore modes without relying on any target samples or running MCMC chains. Various experiments show that the proposed method has comparable or better performance than some of the traditional MCMC, particle-based and NN-based methods.

### Strengths
1. The paper is generally well-written. The description of the proposed method is clear and easy to follow.
2. The proposed sampler is able to explore modes in multi-modal target distributions, which is a desired property in many applications.
3. Once the model is trained, the sampling cost is low since it does not require running MCMC chains and sampling scales linearly with the sample size and dimensionality.
4. The proposed method is evaluated on various experimental settings and has comparable or better results than some of the tradition MCMC, particle-based and NN-based samplers, showing its good applicability.

### Weaknesses
1. The manuscript contains a GitHub link in Line 369-370, which reveals the authors' identity.

2. The proposed method lacks technical novelty and is a bit incremental, since it directly applies an optimal transport loss with KL relaxation to train a sequence of CNFs to model the transitions between neighboring annealed distributions, which is a trivial combination of existing techniques. The core idea of using annealing to bridge between a simple base distribution and a complex target is not new, and the use of optimal transport for training flows is also established. The specific combination here, while functional, does not introduce a significant conceptual advance.

3. The scalability and reliability of the proposed training algorithm is questionable, since it requires training K seperate CNFs sequentially, each modeling the transition between one of the K neighboring pairs of annealed distributions. Furthermore, within each transition, the interval is further discretized into S grid points in order to estimate the integral. This sequential training process is computationally expensive, and the approximation error in each transition will accumulate as the sampler gets closer to the target distribution due to the bootstrap-style training method. Specifically, the method's reliance on a fixed number of intermediate distributions (K) and discretization steps (S) raises concerns about its adaptability to varying complexities of target distributions. A small K may lead to large jumps in the distribution space, making it difficult for the CNFs to learn the transitions effectively, while a large K increases the computational cost. Similarly, a small S will introduce significant discretization errors, while a large S will also increase the computational burden. The paper does not provide a clear strategy for choosing these hyperparameters, nor does it analyze the trade-offs between accuracy and computational cost.

4. It is also unclear how the proposed method should be positioned among other flows-based or NN-based samplers with similar techniques, since many important recent related works are not discussed in the paper, including 
- flow-based sampler trained with annealing: [1, 2, 3]
- score/diffusion-based sampler: [4, 5, 6, 7, 9]
- optimal control-based sampler: [8]

5. Several closely related baselines are missing in the experiment section:
- At the moment, most baselines are MCMC/particle-based samplers.
- Since the proposed method is a flow-based model trained with the annealing technique, it should be empirically compared to at least the following models which use similar flow-annealing techniques: AFT [1], CRAFT [2], FAB [3]. 
- In addition, since the proposed method is broadly an NN-based sampler, ideally it should also be compared with some of other types of SOTA NN-based samplers, such as iDEM [6], DDS [7], PIS [8], PDIS [9].

6. For the toy 1D experiment in Figure 2, it would be more convincing if 
- the two modes in the target distribution are unbalanced (i.e., one has a larger density than the other), as suggested by [5] to test whether the proposed method exhibits a similar blindeness issue as in some of the score-based samplers.
- it also includes results of other flow and annealing-based baselines in this comparison to get a sense of how these similar methods compare to each other, since they are more related to the proposed method in this paper.

7. [Optional] The proposed method is only tested on synthetic problems. Perhaps for future work, it would be nice if the authors could consider some real-world problems, such as sampling from Boltzmann distributions (i.e., Boltzmann generator, see e.g., [3, 6]) which share exactly the same problem setting as in this paper.

### Questions
1. How sensitive is the weight hyperparameter $\gamma$ that controls the balance between the two terms in the dynamic optimal transport loss? Does the value of $\gamma$ vary a lot across different experiments? How the values of $\gamma$ were chosen in the experiments?

2. How does the hyperparameters $K$ (the number of intermediate distributions) and $S$ (the number of discretization grids within each transition between two intermediate distributions) scale with the dimensionality and multi-modaility of the target distribution?

3. [Typo] What is "MEID" in table 2? Is it "MIED"?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The present paper proposes a sampler based on a continuous normalizing flow. The idea is to decompose the transport into sub-transport tasks following an annealing scheme between a simple base distribution and the target. Velocity fields are learned independently for each such transport task so as to minimize a Kullback-Leibler divergence with a transport cost penalization. Once the networks are trained, the sampling is operated by simply sampling from the continuous NF. 

The paper also points that the method can be employed to learn a flow as a proposal distribution in a rare event  importance sampling (IS) scenario. It is proposed that the IS weights are estimate by training a neural network to estimate the density ratio between the flow and the target. 

Numerical experiments report a good mode exploration and qualitative good coverage for the proposed method compared to diverse samplers not relying on deep learning.

### Strengths
- The proposed methods addresses the important point of mode coverage in the task of sampling multimodal distributions in high dimension, which is demonstrated in numerical experiments.

### Weaknesses
 - The paper lacks a related works section. Namely, the connections to  NN-assisted MCMCs, which are in my opinion the most related methods, are not discussed and the performances of these approaches are not reported. In my experience, these methods have better performance than what the paper seems to indicate. In particular, they typically do correct for the mode imbalance that a traditional MCMC based on local updates could not do.

 - In this regard, the novelty of the paper is lesser than what it appears. Annealed Flow Transport  (Arbel et al 2021 in the paper) proposes a very related strategy.

 - Limitations are not properly discussed: 
	- The proposed sampling methods lacks theoretical guarantees of the accuracy of the sampling conversely to NN-assisted (Markov Chain) Monte Carlo samplers, such as Neural IS [3], Flow MC (Gabrie et al 2021, 2022 in the paper) or Annealed Flow Transport (Arbel et al 2021 in the paper). 
	- The cost of training only one velocity field at the time is not discussed, nor how to choose the number of these intermediary steps.
	- For the importance flow method as well, the paper claims “The estimator is unbiased and can achieve zero variance theoretically” but this is only true if the density estimation ratio is predicted exactly by the neural network. 


Minor: 
- About “score based sampling that do not rely on neural networks” (line 66), the paper should also cite RDMC [1] and SLIPS [2].

### Questions
- Is the condition of optimality of the transport crucial to the success of the method? 

- I am surprised by PT’s result in Figure 2. I would expect that this exact sampler designed to sample from multimodal distribution works perfectly in this 1d example. Can the author justify underwhich circumstances the imbalance result was obtained?

- Table 3, what are the expected ground truth values?

- The notations between $\tilde f_k$ (the target annealing path of distributions)  and $f_k$ (the intermediary push forwards of the CNF) is maybe inconsistent in some places. For instance in (8) and (10), should the expectation be over $\tilde f_{k-1}$ instead of $f_{k-1}$ ?

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
4

### Summary
A continuous normalizing flow-based transport map guided by annealing is designed to sample from high-dimensional
and multi-modal distributions with unknown normalization factor. The approach supports effective exploration
of modes in high-dimensional spaces. The paper contains several comparison with state-of-the-art methods.
The method can be extended to a distribution-free model that allows 
to learn an importance flow from a dataset for sampling its least-favorable distribution with
minimal variance.

### Strengths
The basic idea is straightforward, but interesting and the numerical results are quite convincing.

### Weaknesses
The mathematical notation is in many parts cursorily or wrong as the proof of Proposition 1. The numerical experiments which are restricted to symmetric multimodal targets must be improved. 
See questions and experimental suggestions  below.

- in the introduction in connection with normalizing flows I am missing stochastic normalizing flows, see
\nH. Wu, J. Köhler, and F. Noe, Stochastic normalizing flows, in Advances in Neural Information
Processing Systems 33, 5933–5944, 2020.
\nP. Hagemann, J. Hertrich, G. Steidl,
   Stochastic normalizing flows for inverse problems: a Markov Chains viewpoint
SIAM Journal on Uncertainty Quantification 10 (3), 1162-1190,2022
	
- in (3): don't call the \textbf{value} of the integral $\mathcal T$; later this is your OT transport map.
- line 126: hint to Fig. 1 is too early here since $t_1,t_2$  is not explained so far
- line 152: ,,pushes density from $f_{k-1}(x)$ to $f_{k}(x)$, since these are function values, please skip the $x$;
this appears also at other places (but is a minor remark)
- line 159: I would not say that (3) is equivalent to (6)
- in (6) and in the following: what is the pushforward of $\tilde{f}_{k-1}$ by $\mathcal{T}$  for an unnormalized density? Definition of KL for 
unnormalized densities ?; see Prop 1 
The authors should write the definitions down, then they would see that this notation does not work.
- In general the authors switch between $f_k$ and $\rho_k$

- Prop 1 (Appendix A): Despite that the tilde notation does not work  and that $T$ is indeed $\mathcal T$ the authors have to correct
  line 770: first equality is wrong; you need here and in the following $\mathbb E_{x \sim \mathcal T _\#  \tilde f_{k-1} }$ (unfortunately the system does not translates this latex formula correctly, but the authors hopefully see what I mean);
 - from 774 to 776 is wrong and becomes correct with my correction above.
- First equality in 794 is wrong and in the final equality it should be $\log \rho_{k-1} (x(t_{k-1})) - \int ...$

- Prop. 2 is folklore; in formula (9) in the expectation value $x(t) \sim ??$ is missing

- Prop 3: Do not start ,,By Taylor expansion''. This is already the proof.
Write the correct assumptions on x and $\tilde E$ for this Taylor expansion.
Indeed 1. and 2. are folklore and there is nothing to prove. 
However, the authors  wrongly replaced $x$ by $X$ in part 2 of the appendix.
- from formula (19) to (20) there is nothing to prove; in general the heuristic App. B appears superfluous to me,
but maybe it could be of interest for people not directly working in the field.
- The results of the experiments seem to depend heavily on the symmetry of the target density, Please show a modified experiment of Fig. 6 where you shift the target density in the first dimension e.g. by 5 to the left (and keep the variance of the latent distribution).
I guess that the reconstruction misses modes.
- the comparison with HMC is a little unfair. Please redo the HMC experiment with a different chain for each sample starting in the same latent distribution as your model. I would expect that for your symmetric target distribution this woks fine.

### Questions
- in the introduction in connection with normalizing flows I am missing stochastic normalizing flows, see
\\
H. Wu, J. Köhler, and F. Noe, Stochastic normalizing flows, in Advances in Neural Information
Processing Systems 33, 5933–5944, 2020.
\\ 
P. Hagemann, J. Hertrich, G. Steidl,
   Stochastic normalizing flows for inverse problems: a Markov Chains viewpoint
SIAM Journal on Uncertainty Quantification 10 (3), 1162-1190,2022
	
- in (3): don't call the \textbf{value} of the integral $\mathcal T$; later this is your OT transport map.
- line 126: hint to Fig. 1 is too early here since $t_1,t_2$  is not explained so far
- line 152: ,,pushes density from $f_{k-1}(x)$ to $f_{k}(x)$, since these are function values, please skip the $x$;
this appears also at other places (but is a minor remark)
- line 159: I would not say that (3) is equivalent to (6)
- in (6) and in the following: what is the pushforward of $\tilde{f}_{k-1}$ by $\mathcal{T}$  for an unnormalized density? Definition of KL for 
unnormalized densities ?; see Prop 1 
The authors should write the definitions down, then they would see that this notation does not work.
- In general the authors switch between $f_k$ and $\rho_k$

- Prop 1 (Appendix A): Despite that the tilde notation does not work  and that $T$ is indeed $\mathcal T$ the authors have to correct
  line 770: first equality is wrong; you need here and in the following $\mathbb E_{x \sim \mathcal T _\#  \tilde f_{k-1} }$ (unfortunately the system does not translates this latex formula correctly, but the authors hopefully see what I mean);
 - from 774 to 776 is wrong and becomes correct with my correction above.
- First equality in 794 is wrong and in the final equality it should be $\log \rho_{k-1} (x(t_{k-1})) - \int ...$

- Prop. 2 is folklore; in formula (9) in the expectation value $x(t) \sim ??$ is missing

- Prop 3: Do not start ,,By Taylor expansion''. This is already the proof.
Write the correct assumptions on x and $\tilde E$ for this Taylor expansion.
Indeed 1. and 2. are folklore and there is nothing to prove. 
However, the authors  wrongly replaced $x$ by $X$ in part 2 of the appendix.
- from formula (19) to (20) there is nothing to prove; in general the heuristic App. B appears superfluous to me,
but maybe it could be of interest for people not directly working in the field.
- The results of the experiments seem to depend heavily on the symmetry of the target density, Please show a modified experiment of Fig. 6 where you shift the target density in the first dimension e.g. by 5 to the left (and keep the variance of the latent distribution).
I guess that the reconstruction misses modes.
- the comparison with HMC is a little unfair. Please redo the HMC experiment with a different chain for each sample starting in the same latent distribution as your model. I would expect that for your symmetric target distribution this woks fine.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper addresses the challenge of sampling from unnormalized probability distributions by introducing a novel approach called Annealed Flow (AF). The authors define a sequence of annealed distributions and propose learning continuous normalizing flows between each distribution in the sequence. Furthermore, the paper presents an additional method, termed Importance Flow (IF), which allows for computing expectations by first sampling the optimal importance distribution using AF and then learning the associated importance ratio. Experimental results validate the effectiveness of AF and IF across a diverse set of target distributions.

### Strengths
- The importance flow technique is original

### Weaknesses
 - The paper is poorly written (and follows unusual notations for instance with the normalizing constants)
- The paper suffers from theoretical issues/typos (KL between unnormalised distributions, proof of proposition 1, ...)
- The authors don't mention or compare to direct competitors [1, 2] who solve the same problem with the same tools
- Poor experimental part with very few comments
- The proposed method is very close to existing works. Given a sequence of unnormalized densities, this work suggests learning multiple CNFs to move between time k and time k+1 by minimizing a loss at time k+1 given previous samples. This iterative approach is similar to [1] which learns a velocity field inducing an ODE with the same marginals as the sequence of densities. The two losses are extremely similar and both rely on samples from previous steps. However, [1] uses importance sampling in its loss to ensure that the expectation is taken with respect to the right measure while the proposed method seems to blindly trust samples from the previous flow as samples from f_k. This is a major concern as the relative weight between the modes of f_k and f_{k+1} can be very different when using tempering paths. The lack of importance sampling in the proposed method is surprising as it seems unavoidable when minimizing divergences between densities with unknown normalizing constants.
- The paper does not compare against state-of-the-art sampling methods, particularly those based on diffusion models [3,4,5] which have shown significant improvements over normalizing flow techniques. This omission is a major weakness as it fails to contextualize the performance of the proposed method within the current landscape of sampling algorithms.

### Questions
- Could you compare your work against [1] and [2] which have solved the same problem with very similar tools ?
- Could you rewrite sections 2 and 3 but defining the normalizing constants from the beginning ? I think it will make the paper much clearer. Moreover, it would avoid writing KL divergences between unnormalised distributions as done extensively in section 3 and appendix 1.
- I suspects mistakes have been made in the proof of proposition 1. Could you explain the following points ?
1. In common litterature, the Kullback-Leiber divergence is defined between normalized distributions as $D(p || q) = \mathbb{E}_{X \sim p}[\log p(X) / q(X)]$. However, L760 shows a completely different definition (different order and unormalized densities);
2. According to the beginning of section 3.2, the quantity $\rho_k$ is the density of the flow following $v_k$ which means that $\log \rho_k(x(t_{k-1}))$ is not independent of $v_k(x(s),s)$  which would contradict L800.
- The block-wise training procedure (Sec. 4.1) uses AF samples from step $k-1$ to train for step $k$. However, those samples are approximate and have no reasons to be calibrated according to $f_{k-1}$. Can we trust those samples to compute expectations with respect the $f_{k-1}$ ? (Note that the same remark goes for the Importance Flow procedure)
- At L260, you claim that your training procedure only requires a single neural network. Doesn't your sampling procedure require to keep all the intermediates $\{v_k\}_{k = 1}^K$ ?
- Could you perform the experiment on Fig. 1 with differently weighted modes ? I feel like recovering the weights of the modes is the true challenge.
- Could you provide numerical comparisons with recent VI approaches [3,4,5] and with similar approaches [1,2] ? Those methods are important competitors.
- Could you compute the metrics given in [6] which seem computable in your case ? Those metrics really focus on multimodal distributions.
- Could you provide metrics's mean and standard deviation (as well as the number of samples used) for each experiment ?
- Could you display true samples from the Funnel distribution alongside yours ? It would clarify the pros and cons of each algorithm.


[1] Tian, Y., Panda, N., & Lin, Y. (2024). Liouville Flow Importance Sampler. In Proceedings of the 41st International Conference on Machine Learning (pp. 48186–48210). PMLR.

[2] Fan, M., Zhou, R., Tian, C., & Qian, X. (2024). Path-Guided Particle-based Sampling. In Proceedings of the 41st International Conference on Machine Learning (pp. 12916–12934). PMLR.


[3] Francisco Vargas, Will Sussman Grathwohl, & Arnaud Doucet (2023). Denoising Diffusion Samplers. In The Eleventh International Conference on Learning Representations .

[4] Qinsheng Zhang, & Yongxin Chen (2022). Path Integral Sampler: A Stochastic Control Approach For Sampling. In International Conference on Learning Representations.

[5] Richter, L., & Berner, J. (2024). Improved sampling via learned diffusions. In International Conference on Learning Representations.

[6] Blessing, D., Jia, X., Esslinger, J., Vargas, F., & Neumann, G. (2024). Beyond ELBOs: A Large-Scale Evaluation of Variational Methods for Sampling. In Proceedings of the 41st International Conference on Machine Learning (pp. 4205–4229). PMLR.

### Soundness
1

### Presentation
2

### Contribution
2
