# Energy-based Model Training Objective Robust to Inaccurate SGLD Samples

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
We propose a novel technique for training Energy-based Models (EBMs), which are neural network-based models capable of modeling complex probability distributions. The standard approach to EBM training relies on samples generated from the modeled distribution using Stochastic Gradient Langevin Dynamics (SGLD). However, this training method is known to be unstable, as SGLD may fail to provide reliable samples. Compared to other popular generative models, EBMs can directly evaluate unnormalized log-likelihoods for input observations. Unfortunately, trained EBMs typically fail to robustly estimate the likelihoods for distant input observations, as the training procedure only considers the gradients of the log-likelihood with respect to the observations and not the actual log-likelihood values. This paper proposes a generalization of the standard training objective that addresses both issues. The proposed objective explicitly incorporates estimated unscaled log-likelihoods, allowing the EBM to estimate the likelihoods more reliably. Notably, EBMs do not need to (and as we point out, cannot) correctly estimate log-likelihoods to be effective for sampling using the non-convergent SGLD procedure. The proposed objective is controlled by a single hyper-parameter, which balances the trade-off between the quality of the estimated log-likelihoods and the generated samples. A specific setting of this parameter recovers the standard EBM training objective. Moreover, the proposed objective enhances robustness to unreliable SGLD samples by de-weighting contributions from samples that appear inconsistent with the modeled distribution, i.e., samples with very low estimated likelihoods compared to other generated samples or real training data. We demonstrate the improvement in log-likelihood modeling on toy datasets and enhanced stability in a real data scenario, where this stability leads to better performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work presents a variation of EBM learning based on importance sampling. Negative samples are drawn from the current EBM at slightly higher temperature / flatter potential determined by a parameter $\beta \in [0, 1]$ where $\beta=0$ is standard EBM training, then reweighted to obtain an approximation of the expectation of the potential gradient with respect to the model distribution at each step. This is meant to reduce the influence of biased negative samples with especially low likelihood values that result from MCMC sampling, which can lead to unstable training. Experiments on toy datasets, and unconditional modeling/JEM modeling on CIFAR-10 investigate the proposed method.

### Strengths
* Sampling with a slightly higher temperature energy surface and reweighting during learning to reduce the instability of negative samples is an interesting idea which seems to provide some stability benefits. The math behind the reweighting method is sound.

### Weaknesses
 * The experimental evaluation is very limited. There is essentially no quantitative comparison to prior works except for Table 1, which compares to the original JEM paper. There have since been several works revisiting JEM to improve stability and performance which should be used for comparison. Specifically, the lack of comparison to more recent JEM variants that incorporate techniques like spectral normalization or improved sampling methods makes it difficult to assess the true contribution of the proposed method. There is no comparison to a wide variety of recent EBM works that explore unconditional CIFAR-10 modeling with significantly stronger FID scores than the ones presented in this work. The absence of comparisons with methods using advanced sampling techniques, such as annealed Langevin dynamics or Hamiltonian Monte Carlo, further limits the evaluation. Overall, the proposed method is not validated against relevant SOTA results.
* The proposed reweighting is fairly straightforward. Without strong experimental results, the limited technical innovation might not be a strong enough contribution. The reweighting, while mathematically sound, lacks a deep theoretical justification for why the specific temperature parameterization is optimal or even necessary. A more thorough analysis of the impact of different temperature schedules and their effect on the learned energy landscape would be valuable. The method's simplicity, while a potential strength, becomes a weakness without a clear demonstration of superior performance or a novel theoretical insight.
* Sections 3.1 through 3.3 seem somewhat tangential and it is not clear whether the inclusion of positive samples among negative samples is ablated or used in the experimental section. The connection between these sections and the core contribution of the paper is not well-established. The motivation for including positive samples within the negative sampling process is unclear, and the paper does not provide a strong theoretical or empirical justification for this design choice. It is difficult to understand the necessity of these sections without a clear ablation study or explanation of their impact on the final results.

### Questions
* How does the proposed method compare relative to SOTA EBM methods for CIFAR-10 generation and for SOTA models in the JEM family?
* Can the importance of Section 3.1 be validated in an ablation study?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presented a novel technique for training Energy-based models (EBMs) to stabilize the EBM training provide an accurate estimate of the likelihood and generate good-quality samples. The proposed approach involves generalizing the standard EBM loss function by adding an inverse temperature parameter taking values between 0 and 1 for regularizing the learned distribution of the negative samples. The paper presented experiments to show that this modification has resulted in stabilized training of EBMs in real and simulated datasets.

### Strengths
The paper is presented clearly, with the authors offering essential background to understand their method. They provide an intuitive explanation that is easy to grasp. The idea that the negative samples can be OOD and correct the loss in this scenario using importance score seems novel. The authors included experiments demonstrating the method's effectiveness, along with ablation studies to highlight its key components.

### Weaknesses
1.	The main weakness of the paper is the lack of a competitive method. The experiment section presents an ablation study regarding the effect of the inverse temperature parameter. A key competitor of this approach can be Diffusion models which have shown to be highly accurate for likelihood estimation (look at “Variation Diffusion Models” by Kingma et al. 2023).
2.	The presentation of the experiment section needs improvement. What is the necessity of section 4.2? It seems to highlight issues in training the proposed approach on CIFAR-10 data. Then the authors change their framework to a Joint Energy-based Model (JEM) on CIFAR-10 and show that their method still only works when the temperature parameter is very small. Even with stabilized JEM, the approach seems to be inferior to diffusion models on CIFAR-10 (see FID scores in Kingma et al. 2023).
3.	The key argument for opting for EBMs instead of diffusion models is the former’s ability to estimate likelihood. However, there is no result regarding the accuracy of likelihood estimation (except for the visual representation in Fig 2). The authors are encouraged to include quantitative NLL estimates for their EBM and compare them to diffusion models (Table 1 in “Improved Denoising Diffusion Probabilistic Models” Nichol and Dhariwal 2021).

### Questions
1. Denoting observations as "x" in the abstract is not required.
2. The contribution section in the introduction needs improvement. The authors are encouraged to use bullet points to communicate the key contributions.
3. What does the solid line in Fig 1 represent? Is it $p_d$?
4. Sec 3.3 can go into the appendix.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper revisits the issue of non-converged Stochastic Gradient Langevin Descent introducing biases in classical contrastive divergence and persistent contrastive divergence training of energy-based models. The paper makes two contributions: Firstly, debiasing of the parameter gradient through a decomposition of the model $p_\theta(\mathbf x)$ into two tempered distributions $q_\theta(\mathbf x) = p_\theta^{1-\beta}(\mathbf x)$ and  $r_\theta(\mathbf x) = p_\theta^{\beta}(\mathbf x)$ and subsequent self normalised importance sampling. Secondly, the paper includes a positive sample in the set of contrastive negative samples to stabilise training. The paper demonstrates stabilising effects but also comments on deprecating sample quality for large $\beta$.

### Strengths
- The derivations are correct
- The factorisation of the model into an importance distribution and an importance ratio is an interesting idea to improve algorithms that involve self-sampling from the model.
- I appreciate the honesty in reporting a deprecation of sample quality when $\beta>0$ is used. This reflects that the authors are sampling from a tempered, i.e. smoothed out model distribution, and shows that the approach taken by the authors demands a trade-off between training stability and sample quality, at least for high-dimensional distributions.
- The stabilisation can be used in any self-sampling based training method for energy-based models, and can thus be impactful if executed well.

### Weaknesses
 - The experiments on toy data sets are missing a good baseline that helps putting the results in context. For example, I would expect an experimental result of contrastive divergence with the standard regularisation $f_\theta(x_+)^2 + f_\theta(x_-^2)$ for comparison which I know to produce okay results on toy data. (see, e.g. [1] for details on the stabilisation term)
- On image data, only very small values of the stabilisation parameter $\beta$ actually yield stable training of the EBM, thus changing the standard EBM training method minimally. Consequently, the stabilisation of JEM is only demonstrates marginal improvements of the generative (in terms of FID) and discriminative model (in terms of accuracy) over the base training method used. 
- The work is missing a related work section to put this work into a broader context of stabilisation tricks for EBM training. For example, the biases of contrastive divergence have also been targeted by [2]. The trick of including a positive sample to the set of negative samples has been explored before. The trick has been used to stabilise EBM training in [3]. For example, equation 21 in the appendix in your paper closely resembles [3], section 4. The trick is also known in prior contrastive estimation [4] for Bayesian experimental design.

### Questions
- Have you experimented with negative $\beta$ values? This is justified since the importance ratio does not need to be a distribution. I would be particularly curious about this for image data, where values of $\beta>0$ lead to noisy samples in the replay buffer. (you could also switch the factorisation to $q_\theta \propto \exp(\beta f_\theta))$ and choose $\beta\in \mathbb R_{\geq 0}$, which fits more closely to notations in statistical physics).
- Another reason to consider negative $\beta$ is the fact that [5] achieves good results by performing Langevin dynamics with small noise, effectively sampling from a negatively tempered distribution. This approach could potentially be debiased with your proposed methodology.

[5] Grathwohl et al. Your classifier is secretly an energy-based model, and you should treat it like one, ICLR 2020

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The present paper proposes a new training strategy for the maximum likelihood training (MLE) of Energy based Models. Namely,  the gradient of the MLE objective are estimated by combining a Langevin sampling of a “higher temperature” version of the model, and a self normalized importance sampling reweighting to recover an expectation according to beta=1. An additional empirical modification is done to bypass the importance sampling estimate when the proposed negative samples it relies on have very low likelihood according to the model. 

Numerical results are presented on toy 2d systems, as well as for a variant called joint EBM on CIFAR10.

### Strengths
- The papers’ motivation, how to train an EBM with accurate likelihood, is a challenge relevant to the ICLR community.
- The paper honestly discussed experiments with negative results.

### Weaknesses
 - The approach proposed in the paper lacks some theoretical grounding. First, for the self-normalized importance sampling estimator to be correctly implemented, the sampling procedure from the proposal $p_\theta^{1-\beta}$ distribution should be exact. Here the authors rely on a Langevin dynamics, which has discretization error (which can be moderate), but also still suffers from slow mixing if $p_\theta^{1-\beta}$ is multimodal. The use of a finite step size in Langevin dynamics introduces a bias, and while this bias might be acceptable for small step sizes, the paper does not provide a rigorous analysis of how this bias interacts with the proposed training method. Furthermore, the slow mixing issue is particularly concerning for multimodal distributions, as the sampler might not explore all modes effectively, leading to a biased estimation of the gradient. Second, there is a no thorough assessment in the main text of the impact of adding a positive sample to the negative samples, beyond the fact of effectively discarding all the negative samples in this case, which arguably does not yield a highly quality estimator of the MLE gradients. The paper mentions that this is a way to handle 'failed' samples, but it does not provide a clear justification for why discarding all negative samples in such cases would lead to a better gradient estimate, or how this affects the overall training dynamics. A more detailed analysis of the conditions under which this approach is beneficial is needed.

- The approach proposed does not solve the issue of sampling the EBM once trained.

- The numerical results are limited and moderately convincing. If the phenomenology expected by the authors is present for the 8 Gaussian example, the algorithm does not appear to reproduce robustly the relative weights of the modes in Rings. This shortcoming is not discussed in the paper. The results in Table 1 do not have error bars, making it hard to asses their robustness/significance. The lack of error bars makes it difficult to determine if the observed differences are statistically significant or simply due to random fluctuations. Furthermore, the paper does not provide a clear explanation of why the algorithm fails to capture the relative weights of the modes in the Rings example, which is a crucial aspect of the model's ability to learn the underlying data distribution. The absence of a discussion on this limitation raises concerns about the general applicability of the proposed method.

- The discussion of the Related works is incomplete, there is no section properly dedicated to it. In particular I would advise the authors to comment on other works attempting MLE training of EBM [1,2,3] and this work  [4] investigating the impact of non-mixing sampling in the EBM sampling.

- The writing of the paper needs to be improved.
	- Some statements lacks precisions or justification:
		- “Sampling from a more uncertain distribution can lead to improved mixing.” L193
		- “Notably, these two values do not necessarily need to sum up to 1; arbitrary values can be employed instead, corresponding to a different parameterization of the EBM.” L296 —> what would then be the justification?
	- A lot of arguments that the author seek to make to justify the approach are moved to appendix while some less interesting implementation details are kept in the main text.  Half a page is dedicated to explaining experiments that fail while the setting of the JEBM experiment, which is probably a positive result the author want to emphasize, is not in the main text.

### Questions
Minor: 
- There are quite a few misprints at the end of the introduction.
- Why the authors use the term SGLD? I do not believe that the gradients are stochastically estimated, they can be exactly computed with autodiff. A maybe more appropriate denomination would be ULA (Unadjusted Langevin dynamics).

### Soundness
2

### Presentation
2

### Contribution
2
