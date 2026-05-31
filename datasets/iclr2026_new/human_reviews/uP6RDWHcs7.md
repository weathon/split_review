## Human Reviewer 1

### Summary
What the paper claims. The paper introduces Marginal Flow, a density estimator defined as a Monte‑Carlo marginal over latent parameters $w$. Choose an easy‑to‑evaluate component family $q(x\mid w)$ (often diagonal‑covariance Gaussian); draw $w$ by pushing base samples $z\sim p_{\text{base}}$ through an unconstrained neural map $f_\theta$; then define the model as the finite average
$q_\theta(x) \;=\; \frac{1}{N_c}\sum_{i=1}^{N_c} q(x\mid w_{\theta,i}),\quad w_{\theta,i}=f_\theta(z_i)$.
Crucially, $w$ is resampled for every density evaluation and sampling call (Fig. 2; §2.2). The paper argues this yields (i) exact evaluation for the finite mixture in Eq. (2), (ii) single‑step sampling, (iii) architectural freedom (no bijectivity/Jacobians/ODEs), (iv) the option to choose $p_{\text{base}}$ in lower dimension to “learn manifolds,” and (v) efficient training with forward or reverse KL. Experiments cover 2‑D toy densities, reverse‑KL fitting without observations, conditional SBI, SPD matrices via Wishart, and latent‑space “manifolds” for MNIST/JAFFE; runtime plots (Fig. 3) emphasize speedups over NF/FM/FFF.

### Strengths
- Simplicity & speed: No Jacobians/ODEs; likelihood is a sum over $N_c$. Runtime plots (Fig. 3) back the speed advantage.  
- Flexible component families: Wishart experiment on SPD matrices is a nice demonstration (Fig. 9).  
- Both KL directions: Efficient sampling and evaluation allow reverse‑KL training without tricks; synthetic results look competitive with NFs in reverse‑KL (Fig. 8).  
- Clear exposition & code: Equations (5–11) and Appendix A.1 make reproduction feasible, and specific $N_c$ choices are stated for some tasks.

### Weaknesses
1. **Stochastic “exact” likelihood & evaluation protocol.**. 
Likelihoods depend on a fresh resample of w every call (pp. 3–4; Fig. 2). Report NLL mean+/-std over resamples, define a fixed‑mixture evaluation protocol (freeze one draw of w at test time), and separate “finite‑mixture exactness” from “marginal exactness.”  
2. **No guidance on $N_c$ and no scaling study.**. 
Provide NLL/accuracy vs $N_c$ curves, wall‑clock trade‑offs, and dimension sweeps. Connect observations to known nonparametric rates to discuss when growth of $N_c$ becomes prohibitive.  
3. **Manifold claims need precision or a different construction.**. 
Either adopt degenerate/anisotropic components (with care for normalization) or manifold‑native densities to achieve genuine lower‑dimensional support; otherwise rephrase as mass concentrated near low‑dimensional structure.   
4. **Novelty vs MDN not delineated.**. 
Explicitly compare (conceptually and experimentally) to Mixture Density Networks [MDN] (network‑parameterized mixtures/kernels). Discuss statistical/compute advantages beyond not needing to evaluate $q_\theta(w)$. Does this limit novelty? Also, can you show that the approach is going to learn something different than a Kernel Density Estimation method? 
5. **Comparisons emphasize low-dimensional micro‑benchmarks.**. 
Mixture of Gaussians does not scale well with ambient space dimension $D$; curse of dimensionality. Theoretical properties of $N_c$ as a function of $D$ are missing. Introduce higher dimensional experiments to convince otherwise, e.g. on typical image generative modelling datasets (MNIST; CelebA; ImageNet 64x64).  
6. **Universal approximation theory is missing.**. 
Even light‑touch results would help: e.g., approximation error of the Monte‑Carlo mixture to the ideal marginal as a function of $N_c$; and conditions under which the model inherits known universal approximation properties of mixtures (with references).

References
----
[MDN] Mixture Density Networks. Bishop 1994.

### Questions
1. Test‑time protocol & variance. Do you freeze one draw of $\{w_{\theta,i}\}_{i=1}^{N_c}$ for the entire test set, or resample per‑example? Please report NLL mean+/-std over 20 resamples on your test sets and clarify which numbers appear in figures. The paper currently implies resampling at every evaluation (pp. 3–4; Fig. 2).  
2. Guidance on N_c. Provide ablations of NLL/C2ST vs $N_c$ and discuss compute/variance trade‑offs. In Appendix A.4 you pick $N_c=$ half the training set, SBI uses $N_c=2048$, JAFFE $N_c=128$; what drives these choices? For latent-variable MNIST, is the VAE trained jointly with the Marginal Flow? What is the training procedure exactly?
3. Dimension scaling. Have you tried ambient $D \ge 32$ in data space (not latent) with quantitative benchmarks? How does runtime and NLL change with d when keeping a fixed compute budget? Report test log-likelihood and sample quality metrics (FID,KID) comparing against other generative modelling methods using networks with similar sizes.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposed marginal flow, supporting sampling and density estimation using a latent variable model, showing success in toy examples, low dimensional datasets and small images.

However, unfortunately, I think this paper has a very limited contribution: the idea of marginalisation has existed in early generative models, like VAE or implicit models. In fact, one can also view diffusion models (like DDPM) as one example with many layers of latents. Then the question is, why did these models not use the approach mentioned in this paper? The answer is because given one $x$, it is very difficult to sample enough $w$ to yield a reliable estimation of $q(x)$, even though all the terms in the MC estimator (eq 2 in this paper) are tractable. 
Therefore, one can imagine that as the dimensionality grows, the efficiency of the proposed methods will significantly reduce, especially when $q(w|x)$ is far from $q(w)$. (I use $q$ to follow the notation of this paper).  And hence I am not convinced that this approach is efficient.

Even not considering this inefficiency, the claim that marginal flow supports **exact** density evaluation is not accurate: it is only exact when $N_c\rightarrow \infty$. Given this assumption, many approaches (for example, diffusion density estimator by [1] and even VAE) are also exact. 



Therefore, given the fundamental limitation of this paper, I am sorry to say that I am not convinced that this work achieves the bar of publication. 


[1] Huang, Chin-Wei, Jae Hyun Lim, and Aaron C. Courville. "A variational perspective on diffusion-based generative models and score matching." NeurIPS 2021.

### Strengths
Please see Summary

### Weaknesses
Line 128-129: $f(w)$ should be $f(z)$?

### Questions
One may also estimate a proposal $q(w|x)$ similar to VAE for importance sampling to boost the efficiency. This will also be exact when $N_c\rightarrow \infty$. Will this strategy help the method to scale up to higher-dimensional datasets?

How do you distinguish VAE and this proposed approach, except that the training strategy is different? 

How does the performance change with respect to $N_c$?

The training is an important part of the algorithm, maybe its benefial to include it in the main text.

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents Marginal Flow, a density estimation framework the directly marginalizes the latent parameters sampled from a learnable distribution induced by a flexible mapping function from z to w where the distribution of z is typically known (e.g., standard Gaussian or uniform distribution). The authors claim that the proposed method is highly flexible and also efficient in training, evaluation, and sampling. The authors also conducted experiments in several simulation datasets and showed some results in the image dataset where a dimension reduction tool (e.g., VAE) is used. The whole model can be considered as a neural network parameterized Gaussian mixture in the default setting. I list some constrains, limitations, and questions below.

### Strengths
1.	The problem is well described and formulated.
2.	The method is easy to understand.
3.	The results show some advantage in the current settings.

### Weaknesses
1.	The novelty is limited as the approach is essentially a mixture model where the mixing density is induced by a flexible neural network (e.g., MLP with a few layers). The marginalization is also not new as it is just Monte Carlo.
2.	The scalability is very constrained. Since the method requires the evaluation of full likelihood on all samples and the all Ws from Monte Carlo. I can image that the method could not work efficiently as sample size grows to a large number.
3.	Many important baselines are missed for comparison or not even mentioned. E.g., Roundtrip, MAF, and RealNVP. Roundtrip uses exactly the same idea of marginalization in estimating p(x) by adopting a cycleGAN architecture.
4.	The authors benchmarked the method mostly on toy datasets (e.g., 2 dimensional). The ability to handle high-dimensional density estimation is not actually demonstrated. 
5.	The model should be highly sensitive to Nc since it determined the Monte Carlo error. How to determine the optimal Nc is not discussed.

### Questions
1.	Please show the benchmark results in high-dimensional settings since traditional statistical methods can already handle very well for density estimation in low-dimensional settings (e.g., d<10).
2.	Please conduct sensitivity analysis to the parameter Nc. There should be at least an empirical guidance on how to choose Nc.
3.	In terms of scalability, the current training requires the computation of full log-likelihood. Is it possible to improve the scalability by mini-batch update? If so, how performance will be affected?
4.	Can the authors provide scenarios where the proposed method is preferable in practice over normalizing flow, diffusion models?
5.	Marginal Flow seems to be a misleading name, since xxxFlow typically refers to methods with multiple transformations between the base distribution and the target distribution, such as normalization flow with multiple invertible transformations functions, and flow matching/mean flow with infinite steps (t=0 to 1). While the proposed approach does not involve multiple steps of transformation.
6.	Some errors or typos. Line 111: Sigma=diag(sigma_1^2,…, sigma_d^2). Line 129: f_theta(z) instead of f_theta(w)
7.	The author claimed the approach can evaluate the density exactly is misleading since there is a Monte Carlo error that is not discussed at all in the paper, which depends on the Nc. So the equation (2) is still an approximated density.
8.	How the variance term is learned? Any constrain on it or just set it to be a trainable parameter?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
5
