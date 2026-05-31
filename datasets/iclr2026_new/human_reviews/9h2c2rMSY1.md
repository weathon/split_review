## Human Reviewer 1

### Summary
Spatiotemporal PDEs are being increasingly solved with neural operators. Uncertainty quantification on such predictions, therefore, is not immediately possible as a result of distribution shifts that occur as temporal windows slide. In this vein, previous works have studied conformal prediction under covariate shift. This paper then studied the application of such ideas to this setting, first in the full functional form and then in the discretized setting.

### Strengths
The paper presents an interesting problem of study: the study of spatiotemporal PDE coverage seems like a worthwhile direction. The exposition of the paper is also very clear, making the paper easy to follow and engage with. The paper also nicely discusses both the functional and the discretized forms of the problem statement.

### Weaknesses
In the first part of the paper, the authors establish that the TV distance between consecutive steps is maximal in the functional space. I believe the implication of this statement is supposed to be that, therefore, we cannot consider the functional space coverage using ideas from covariate shift. However, the approach of Barbet et. al only establishes that $\mathcal{P}(Y\in\mathcal{C}(X))\ge 1-\alpha-\sum_i w_i d_{TV}(z, z^i)$, which is a lower bound. How can we say anything more strongly than just making claims of this lower bound here?

Moreover, this then motivates studying this problem in a finite-dimensional discretized form. This, however, then just becomes a standard, finite-dimensional time series problem, so I do not see how this becomes any different from a typical finite-dimensional conformal time series problem. Also, Theorem 4.2 appears to be a standard proof from SDEs, so I do not see why it and its proof are provided in the main body of the paper.

Finally, the experimental results appear to be not very compelling: many times, WCP appears to produce extremely conservative prediction regions, having a coverage of 1.0 or close to it at desired coverage levels well below this. The other methods, in contrast, appropriately hit 0.90 initially.

### Questions
1. How does this particular setting differ from a general time series conformal prediction problem after the PDE has been discretized? Are there particular structures that you can uniquely leverage to develop a method in this setting that cannot be more generally applied? This reduced scope would likely yield more useful methods.

2. Why are the coverages so conservative in this setting? The empirical results seem to indicate over-coverage even before the time steps progress very far.

3. Even though the TV in the functional case is 1.0, does that necessarily mean there is no other form of covariate-shift type adjustments that could fix the miscoverage?

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper develops weighted conformal prediction (WCP)  for applying conformal prediction to time-dependent PDE surrogate models.  The authors prove that in function spaces with time-dependency, distributions at different times can be mutually singular (TV distance = 1), breaking the exchangeability assumption and hence CP coverage guarantees. As a solution, they propose reweighing the nonconformity scores with density ratios to enable exact coverage guarantees. Experiments on three PDEs (univariate, linear, with Gaussian initial conditions) demonstrate that WCP maintains coverage where two baselines, naive CP and LSCI, fail.

### Strengths
- The problem is significant and well motivated. The authors make a good point in laying out the challenge of covariance shifts in time-dependent PDEs that are common in physics and engineering. Theorem 4.1 was also a clear illustration of this challenge and how existing methods can fail.

- The paper was over-all well organized and easy to follow.

### Weaknesses
- No real algorithmic or theoretical contribution. Theorem 4.1 proves that for the heat equation with Gaussian initial conditions, the TV distance between solution distributions at any two distinct time points is maximal (equals 1). Theorem 4.2 shows that for discretized linear PDEs with Gaussian initial conditions, the solution distribution at any time t remains Gaussian, with explicitly computable mean and covariance. These two results are not particular novel for PDEs. The authors' method, then, directly applies Barber et al. 2023's weighted conformal prediction algorithm using the likelihoods. The coverage guarantees are from Barber 2023. I fail to see how this algorithm is a novel contribution. 

- The scope is limited. The algorithm only applies to _linear_ PDEs with _Gaussian_ (and location-scale) initial conditions, but most physical systems of interest of UQ have nonlinear dynamics (Navier-Stokes, reaction-diffusion with nonlinear terms, etc.). The proposed algorithm require explicit probabilities which makes it not extendable to the more general case. 

- Significant weakness and ambiguity in the experiment section. This includes:
    - What is the target coverage? Why is the target in Fig 3 set at 90% but the target for WCP said to be 99%? Why does WCP's line disappear half way through the horizon? What is $n_\infty$ in Table 1 and how should we interpret it?
    - Limited experiment setups: only linear, univariate, synthetic experiments. This is a result of the nature and assumption made by the method, but with this set of experiments it's not very convincing that this algorithm is useful in practice.  
    - Lack of comparison to baselines, and discussion of literature. From the PDE literature, there are works that provide probabilistic forecasts (for example [1,2], and the baselines in LSCI). From the CP literature, there are a swath of works that handles time series distribution shift that does not require explicit covariates or local exchangeability [3-6]. They should be compared to show what are the advantages of your algorithm, or at least discussed w.r.t. why they are not applicable to your setup. 
    - It is also questionable that WCP over-covers by so much, often achieving 1.0 coverage with infinite bands. While I respect the authors' honest reporting, this is a significant limitation on the usability of the UQ bands. UQ's goal is calibration and the tendency to over-cover is not desirable. Can you show results of both 90\% and 99\% target coverage?
    - Some qualitative plots of UQ bands (similar to figure 1) will also help the presentation of results.  

[1] Yang, Liu, Xuhui Meng, and George Em Karniadakis. "B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data." Journal of Computational Physics 425 (2021): 109913.

[2] Bülte, Christopher, Philipp Scholl, and Gitta Kutyniok. "Probabilistic neural operators for functional uncertainty quantification." arXiv preprint arXiv:2502.12902 (2025).

[3] Gibbs, Isaac, and Emmanuel Candes. "Adaptive conformal inference under distribution shift." Advances in Neural Information Processing Systems 34 (2021): 1660-1672

[4] Angelopoulos, Anastasios, Emmanuel Candes, and Ryan J. Tibshirani. "Conformal pid control for time series prediction." Advances in neural information processing systems 36 (2023): 23047-23074.

[5] Xu, Chen, and Yao Xie. "Sequential predictive conformal inference for time series." International Conference on Machine Learning. PMLR, 2023.

[6] Auer, Andreas, et al. "Conformal prediction for time series with modern hopfield networks." Advances in neural information processing systems 36 (2023): 56027-56074.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper studies how conformal prediction (CP) fails under temporal non-stationarity common in time-dependent PDEs, where calibration and test data are not exchangeable. The authors first prove that, in function-space settings, even simple PDEs (e.g., the 1-D heat equation) produce mutually singular solution distributions across time, making exact coverage guarantees impossible. They then propose Weighted Conformal Prediction (WCP) for discretised PDE surrogates, deriving closed-form Gaussian densities for the evolving solutions and using likelihood-ratio weights to re-establish exact coverage. Experiments on fractional diffusion, backward heat, and reaction–diffusion equations show that WCP maintains nominal 90 % coverage over long horizons, whereas naïve CP and local-exchangeability (LSCI) methods quickly under-cover.

### Strengths
- Mathematical clarity. The analysis of mutual singularity in function spaces (Theorem 4.1) exposes a genuine limitation of applying CP directly to PDEs.

- Principled solution. The likelihood-weighted approach is a suitable approach to time-dependent distribution shift, avoiding unverifiable “local exchangeability” assumptions.

- Clear writing and sound experiments. The presentation is precise, proofs are rigorous, and empirical results clearly support the claims.

### Weaknesses
- Limited scope. Theoretical guarantees hold only for linear PDEs with Gaussian initial conditions, where analytic densities exist.

- Incremental novelty. Weighted CP under covariate shift is known (e.g., Barber et al., 2023); the contribution is mainly its application to PDE surrogates, not a new CP framework.

- Narrow experiments. Tests on 1-D synthetic PDEs demonstrate correctness but not scalability or real-world complexity.

### Questions
- How sensitive is WCP to deviations from Gaussianity or linearity?
- Can the framework be extended to nonlinear or stochastic PDEs without closed-form densities?

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
3