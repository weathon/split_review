# Exploring Non-Convex Discrete Energy Landscapes: A Langevin-Like Sampler with Replica Exchange

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
Gradient-based Discrete Samplers (GDSs) are effective for sampling discrete energy landscapes. However, they often stagnate in complex, non-convex settings. To improve exploration, we introduce the Discrete Replica EXchangE Langevin (DREXEL) sampler and its variant with Adjusted Metropolis (DREAM). These samplers use two GDSs at different temperatures and step sizes: one focuses on local exploitation, while the other explores broader energy landscapes. When energy differences are significant, sample swaps occur, which are determined by a mechanism tailored for discrete sampling to ensure detailed balance. Theoretically, we prove both DREXEL and DREAM converge asymptotically to the target energy and exhibit faster mixing than a single GDS. Experiments further confirm their efficiency in exploring non-convex discrete energy landscapes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper focuses on MCMC samplers for discrete spaces that incorporate both replica exchange and (optionally) a Metropolis correction. Some convergence results (asymptotic and non-asymptotic) are presented, as well as experimental evidence.

### Strengths
The empirical results seem promising and suggest that this may indeed be an effective algorithm in practice. In particular, the algorithm clearly outperforms its competitors both when the Metropolis adjustment is and is not present.

The motivation for the approach is clear, and the resulting algorithm is simple and well-principled.

### Weaknesses
The theoretical results are not very strong. In particular, Theorem 1 does not provide an non-asymptotic approximation error. Theorem 2 is difficult for me to interpret; see below. In general, these type of replica algorithms are known to be difficult to analyze.

Assumption 3 in the main text is too vague and its presentation in the appendix needs to moved to the main text in order for Theorem 2 to be well-understood.

I have some additional questions regarding Theorem 2 in the main text. See the following section.

Am I correct in noting that Theorem 2 only gives convergence to the biased stationary measure for DREXEL? In this case, can the authors comment on the approximation error of this stationary measure in a non-asymptotic sense?

In Theorem 1, should $\tilde \pi$ and $\pi’$ be referring to the same distribution between the two lines?

### Questions
The results seem to be in favour more generally of these type of multiscale chains. Do these methods perform better (empirically) when more levels to this scale are added?

In the figures, do the authors account for the number of rejections? How many times are the proposals typically rejected in practice? Does this affect the optimal step-size scaling compared to the other algorithms?

Can the authors offer more detail on Assumption 4 in the appendix? When does this hold for some reasonable distributions of interest?

Am I correct in noting that Theorem 2 only gives convergence to the biased stationary measure for DREXEL? In this case, can the authors comment on the approximation error of this stationary measure in a non-asymptotic sense?

In Theorem 1, should $\tilde \pi$ and $\pi’$ be referring to the same distribution between the two lines?

147: retains current -> retains the current
In the algorithm, follows -> following

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Two gradient-based discrete samplers (with and without MH corrections) are introduced by combining concepts from discrete Langevin samplers (DLS), which generalize Langevin MCMC to discrete space, and replica exchange Markov Chain Monte Carlo (reMCMC), which considers exchange between multiple replicas operating at different temperatures.

### Strengths
The numerical results are backed by tests on various model types, demonstrating statistically significant improvements over prior related methods.

### Weaknesses
While the approach is sound and results are well-presented, the work represents an incremental improvement, building heavily on previous methods, analyses, and benchmarks. It would be helpful to clarify a few points for better readability.

In terms of algorithmic progress, the new approach simply combines existing ideas (DLS and reMCMC). Moreover, the improvement in benchmark results is statistically significant but relatively modest. It is not entirely clear how much the setup (hyperparameter settings, etc.) of the benchmark affects the relative performance of the compared algorithms.

1) What is the dependence of log RMSE on temperature τ in Ising model results (Fig. 3) ?
Are the conclusions of Fig. 3 the same for a lower target distribution temperature (e.g., τ=0.1) ?
What are the results for other spin connectivity exhibiting more frustration (e.g. fully connected Sherrington-Kirkpatrick problems) ?

2)  Although the new method seems effective, the rationale behind the selection of hyperparameters for each approach is not sufficiently justified. To ensure a fair comparison, additional details about the hyperparameter settings would be beneficial.

- How are temperature and step sizes chosen in each approach? 
In particular, how is the gap between τ1 and τ2 chosen and how does it affect performance?

- Are DMALA and DULA comparison done at their respective optimal parameters (step size)?
How does log RMSE of Ising model results of DMALA and DULA change for step size from 0.1 to 0.5 ?

- Could the authors clarify the reasoning behind choosing, for E.g., a step size of 0.2 for DULA and 0.4 for DMALA on the Ising model?
Discussion the influence of hyperparameter selection would make the results more convincing.

3) The explanation of bias correction is not totally clear, specifically for methods like dDREXEL and bDREAM versus DREXEL and DREAM. While dDREXEL and bDREAM include a bias, do DREXEL and DREAM incorporate a bias correction as well (see Fig. 6)?

Others:

1) How is the bias 𝜎 σ in equation (9) chosen in practice?
2) What are the rejection rates for DREAM, and how do step size and temperature choices (𝜏1, 𝜏2) affect it?

Minor comments:

1) Missing standard errors in Tables 1 and 2
2) Typo: Asymptotic Convergence on Log-Quadratic “Distriubions"

### Questions
1) What is the dependence of log RMSE on temperature τ in Ising model results (Fig. 3) ?
Are the conclusions of Fig. 3 the same for a lower target distribution temperature (e.g., τ=0.1) ?
What are the results for other spin connectivity exhibiting more frustration (e.g. fully connected Sherrington-Kirkpatrick problems) ? 

2)  Although the new method seems effective, the rationale behind the selection of hyperparameters for each approach is not sufficiently justified. To ensure a fair comparison, additional details about the hyperparameter settings would be beneficial.

- How are temperature and step sizes chosen in each approach? 
In particular, how is the gap between τ1 and τ2 chosen and how does it affect performance?

- Are DMALA and DULA comparison done at their respective optimal parameters (step size)?
How does log RMSE of Ising model results of DMALA and DULA change for step size from 0.1 to 0.5 ?

- Could the authors clarify the reasoning behind choosing, for E.g., a step size of 0.2 for DULA and 0.4 for DMALA on the Ising model?
Discussion the influence of hyperparameter selection would make the results more convincing.

3) The explanation of bias correction is not totally clear, specifically for methods like dDREXEL and bDREAM versus DREXEL and DREAM. While dDREXEL and bDREAM include a bias, do DREXEL and DREAM incorporate a bias correction as well (see Fig. 6)?

Others:

1) How is the bias 𝜎 σ in equation (9) chosen in practice?
2) What are the rejection rates for DREAM, and how do step size and temperature choices (𝜏1, 𝜏2) affect it?

Minor comments:

1) Missing standard errors in Tables 1 and 2
2) Typo: Asymptotic Convergence on Log-Quadratic “Distriubions"

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper adapts the replica exchange technique from continuous gradient-based samplers to discrete versions, which expects to have a better gradient complexity to achieve convergence for dissipative target distributions. From an intuition perspective, this paper hopes to utilize different temperatures (or step sizes of each iteration) and exchange them for escaping the trap's local modes of non-convex discrete energy landscapes.

### Strengths
1. The problem about drawing samples from a discrete energy landscape is very interesting and worth studying
2. The core technical contribution of this paper may be the design of the swap function shown in Eq.(10), which is original and seems to have a good performance in various experiments.
3. This paper is well written; the intuition, implementation, and experiments are clear, which makes this paper easy to follow.

### Weaknesses
I have some serious concerns with respect to the theoretical part of this paper.
1. Theorem 2 considers the target distribution, which is affected by both $\theta_1$ and $\theta_2$ corresponding to the low or high-temperature particles. Actually, in such a discrete sampling setting, the return of Alg.1 is only $\theta_1$ corresponding to the low-temperature particles, which does not match the theory shown in Theorem 2. It seems that the theorem should focus on the marginal distribution of $\theta_1$ instead of the joint distribution.
2. Essentially, authors should provide the TV distance convergence between the marginal distribution of $\theta^{(1)}_i$ (denoted as $\tilde{\pi}\_n^{(1)}$) and $\theta\_{*}\sim \pi\propto(U(\theta))$. However, except for $\tau_1=1$, the target distribution provided in Theorem 2 cannot be considered as an approximation of $\pi$ even only considering its marginal distribution, i.e., $\exp(U(\theta^{(1)})/\tau_1)$ of $\theta^{(1)}$. Since additional factor $\tau_1$ exists . A more rigorous analysis should demonstrate that when $\tau_1$ is set to 1, the marginal distribution accurately reflects the target distribution.
3. According to the chain rule of TV distance, the TV distance provided in Theorem. 2 is only an upper bound of the TV distance between the output distribution of $\theta^{(1)}$ and $\pi$. This means the authors should claim the advantages of convergence improvement come from the sampling algorithm rather than the TV gap between joint distribution and marginal distribution, i.e., $TV(\pi^\prime, \tilde{\pi}^\prime_n) - TV(\pi, \tilde{\pi}^{(1)}_n)$. In other words, the current analysis does not isolate the algorithmic contribution to convergence improvement.
4. Moreover, the proof of this paper has a severe problem in Line 1013—Line 1016. We can easily find that $0<\rho<1$, and the last line of Eq.(18) can hardly be upper bounded by arbitrary small $\epsilon$. Because the last term is $(\mathcal{B}+B)\cdot 1/(1-\rho)$ where both $\mathcal{B}$ and $B$ can be founded in Assumption. It means they can be considered as a constant. Besides, the inequality $1/(1-\rho)>1$ is established. More explicitly, it can be easily found that the last inequality in Eq.(19) requires $\epsilon>(\mathcal{B}+B)$, which is unacceptable in convergence analysis. This implies a fundamental flaw in the convergence proof, as the bound cannot be made arbitrarily small.
5. The convergence improvement in the analysis is extremely limited since there is a log dependence with respect to such an improvement, which may hardly be distinguished in practice. The practical implications of this logarithmic improvement should be further investigated and discussed.

### Questions
1. In the synthetic data, it is relatively easy to determine the different temperatures. However, determining the scaling of different temperatures is difficult. Could authors give some suggestions for tuning the hyperparameters?
2. From an intuitive perspective, a Langevin dynamic with a decreasing step size seems to achieve a similar performance (get rid of the local traps) under a large initial step size. Could authors have a discussion or additional experiments to compare with those methods?

I am willing to raise my score if the authors solve my concerns.

### Soundness
2

### Presentation
3

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
In this paper, the authors tackle the task of sampling from high-dimensional discrete distributions with multimodality characteristics (i.e. non log-concave distributions) whose energy is assumed to be differentiable. This is a computational challenge since it requires to be able to locally explore the target distribution and alternating between the modes without introducing any asymptotic bias. Inspired by the rich literature in continuous state spaces, the authors propose a novel MCMC sampler, DREXEL, which can be seen as a discrete version of the well known Replica Exchange Langevin algorithm. In essence, DREXEL builds 2 Markov chains, each one targeting a tempered version of the target distribution: one with temperature 1 (i.e., the target distribution) and the other with high temperature (i.e., smoother version of the target). Each of these Markov chains consists in discrete Langevin steps, independently made on all coordinates (in order to explore the local landscape), which may be combined to Metropolis-Hastings (MH) corrections (in this case DREXEL is referred to as DREAM). To enable global exploration, swaps between the current states of these MCs may occur, based on a tractable MH acceptance rate. To validate their approach, the authors provide convergence results in the case where the target distribution is log-quadratic, which demonstrate zero asymptotic bias and better convergence rate than standard local sampler. Then they apply their method to a variety of discrete sampling settings with multimodality including Ising models and EBMs on binarized images.

### Strengths
- The current paper is well written and easy to follow; the authors pay attention to recall in their introduction the main elements previously obtained in the literature before explaining how they can be adapted to their setting. Overall, they bring intuition on each methodological brick and each theoretical statement, which makes the reading pleasant. 
- This is a complete methodological work, detailing both theoretical and numerical results for a challenging sampling task (i.e. including multimodality), and therefore, it may be highly valuable for the sampling community. 
- A large variety of numerical settings is considered in the experiments with convincing results, although they suffer from main weaknesses (see next section)

### Weaknesses
In my opinion, the main weaknesses come from the numerical evaluation of the method:
- The setting of the three main hyperparameters of DREXEL/DREAM (the local Langevin step-size, the highest temperature and the swap intensity) is not discussed anywhere in the manuscript, whereas it is critical for real world use. In particular, the authors do not detail how they tuned their hyperparameters for their experiments: in principle, one should not know in advance the ground truth samples for tuning. If this is the case, this should be well highlighted.
- No ablation study of the hyperparameters is given anywhere, which makes hard to tell how much they are critical.
- The initialization of the algorithm is not given in each numerical experiment, while it is known to have a high influence on MCMC results.
- The current numerical experiments do not rely on sampling metrics that could assess how well the true relative weights of the target modes are estimated (for distributions with isolated modes such as 8 gaussians or wave) beyond recovering the location of the modes, which is the main challenge for multimodal sampling. In particular, integrated probability metrics (such as MMD, KL, used in the first experiment) may not reflect mode collapse, as explained in [1].
- The numerical results not contain error quantifications computed on several experiment runs, which hurts their statistical significance. In particular, numerical results from various methods are really close to each other in each setting and may be considered similar by repeating runs.

### Questions
- Have you considered increasing the number of Langevin steps before applying the swap ? In the current version, there is only one Langevin step for one RE step which definitely helps the mixing ; however, having a small number of Langevin steps may actually hurt the local exploration.
- Have you considered adaptive Langevin step-size based on the result of the MH step for DREAM ? This is widely used for continuous state space and may be valuable in the current setting, as proposals are made independently on each coordinate.
- Why don't you consider more than 2 temperatures in the RE setting as it is commonly made for continuous state spaces, which may speed up the mixing of the Markov chains ?
- Why don't you consider a sample-based metric for the EBM experiment as made for the Boltzmann machine ? In particular, I think that estimating the partition function with MCMC to obtain an estimate of the EBM log likelihood may bring high statistical uncertainty to the results.
- How did you initialize the sampling algorithms in each numerical setting ?
- Since you used an annealed version of DULA (ie, discrete version of annealed Langevin dynamics) to estimate the partition function of EBMs, why don't you use this sampling algorithm as a competing method ?
- How many iterations of DREAM did you use to sample from one MNIST image once the EBM is trained? 

**Suggestions**
- I think that the assumptions on the target distribution should be more highlighted in the text.

### Soundness
3

### Presentation
4

### Contribution
3
