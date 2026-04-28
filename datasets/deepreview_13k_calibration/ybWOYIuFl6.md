# BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 3, 5

## Abstract
Developing an efficient sampler capable of generating independent and identically distributed (IID) samples from a Boltzmann distribution is a crucial challenge in scientific research, \textit{e.g.} molecular dynamics.
In this work, we intend to learn neural samplers given energy functions instead of data sampled from the Boltzmann distribution.
By learning the energies of the noised data, we propose a diffusion-based sampler, \textsc{Noised Energy Matching}, which theoretically has lower variance and more complexity compared to related works.
Furthermore, a novel bootstrapping technique is applied to NEM to balance between bias and variance.
We evaluate NEM and BNEM on a $2$-dimensional $40$ Gaussian Mixture Model (GMM) and a $4$-particle double-well potential (DW-4). The experimental results demonstrate that BNEM can achieve state-of-the-art performance while being more robust.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a neural sampling method for known energy functions. The importance of this problem is well-established, and the distinction between this and methods learned from sample data is sound. The NEM method improves on previous neural samplers by using an energy-based training objective, using a lower noise target, and introducing a bootstrapping method. The results show improvements over other listed neural samplers.

### Strengths
The paper describes the method very clearly. In particular, figure 1 is quite concise. Moreover, it shows proof that the improvements suggested are indeed improvements. Section 3 is well written, and the score vs. energy section contribution is valuable.

The results are strong and show improvement over other methods for the toy problems.

### Weaknesses
While the paper clearly shows improvement over previous neural sampling methods, it still makes little or no progress on the fundamental challenge of scaling to larger systems. The authors acknowledge this, but it ultimately make this an incremental improvement, not a transformational one.

Why is the distribution of interatomic distances for NEM and BNEM less sharply peaked than the ground truth for  LJ-55?

### Questions
Why is the distribution of interatomic distances for NEM and BNEM less sharply peaked than the ground truth for  LJ-55?

Have the method been tried on any larger, more complicated systems? Even if the results are not impressive, it would be useful for the field to know when this method breaks down.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors consider a setting in which we want to draw samples from a Boltzmann distribution, for which we have the ground truth energy function, but cannot normalize into a probability distribution (for the usual reasons).  A very recent proposal (Akhound-Sadegh et al., 2024, "iDEM") for this problem is to model the "score function" (in Hyvarinen's sense) with a neural network, as in a diffusion model; but, lacking data samples, to target not the empirical score (via Tweedie's formula) but rather a Monte Carlo estimate written in terms of the energy function.  The MC samples are drawn in an outer loop by simulating the reverse diffusion process, using the current score-estimating network.

The present MS proposes to alter iDEM slightly, by modeling the *energy* rather than the score--again by targeting a MC estimate, in this case of the energy itself rather than its gradient.  They prove that (under certain conditions--I did not read the proof in detail) the error of iDEM's score estimator is strictly larger than the error of their own energy estimator; and (empirically) than the error in the score function that is produced by differentiating their energy estimator (and which matters because it will be used for sampling).  To reduce variance in this estimator further still, the authors further propose a "bootstrapping" technique in which the target energy is not constructed from the known data energy, but instead estimated from a model energy at a smaller noise level.

Empirically, the authors show that their approach yields superior samples to iDEM as well as other recent proposals, particularly with the "bootstrap" improvement.

### Strengths
The MS attacks an important problem and improves upon the state of the art.  The solution is original (to the best of this reviewer's knowledge) and provides theoretical as well as empirical reasons to prefer their proposal over alternatives.

### Weaknesses
 (1) On the GMM-40 task, the manuscript's version of iDEM (Fig. 2) is visibly inferior to the one in the original paper (Akhound-Sadegh et al, Fig. 3), which is much closer to ground truth.  Something similar is true of the energy histogram for LJ-55 (Fig. 3 in this MS, Fig. 4 in op. cit.).  Can the authors explain these discrepancies?

(2) For DW-4, LJ-13, and LJ-55, the improvement in Wasserstein-2 distance provided by NEM and BNEM over iDEM appears marginal (Table 1).  Considering the additional computational cost of evaluating the energy gradient, this may not justify the proposed approach.

(3) The reported W2-E for iDEM is high, potentially due to outlier samples as pointed out in the manuscript. It would be nice to re-evaluate W2-E removing outliers for comparison with NEM and BNEM.  

(4) Learning energy instead of score may improve estimation, but sampling requires costly repeated gradient evaluations as steps increase.  A table comparing sampling times for score-based (iDEM) and energy-based (NEM) training would be helpful.

(5) The descriptions of the problem setting and proposed solution could be much improved; this reviewer, at least, found the exposition in Akhound-Sadegh et al. (2024) much clearer.

(6) The Fisher divergence (Eq. 8) is a well understood quantity, with connections to KL divergence---e.g., in the context of diffusion models, it arises naturally under the standard ELBO loss.  Can the authors provide any similar theoretical appeal for the squared error in energy, Eq. 10?


MINOR  
Diffusion models were introduced by Sohl-Dickstein et al. in "Deep unsupervised learning using nonequilibrium thermodynamics" (ICML, 2015) and this paper should be referenced when they are introduced in the MS.

### Questions
See "Weaknesses" above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors propose Noised Energy Matching (NEM) and Bootstrap NEM (BNEM), a diffusion-based neural sampler based on previous related work (iDEM). In particular, the authors propose to parametrise the energy with a network, instead of the score, to reduce the variance of the estimator. They also propose to bootstrap the energy estimator at high noise levels from learned estimators at lower noise levels to further reduce the variance.

### Strengths
The paper is generally well-written and easy to follow. The authors provide enough background to make the paper easy to understand. The topic of diffusion-based samplers is also an important and interesting topic with applications in many domains. Additionally,  improving the MC estimator of the score when we have access to the energy and not data is, in my opinion, very well-motivated.

### Weaknesses
 **Novelty and Motivation**: 
Although the NEM algorithm is a simple reparametrization of the estimator in iDEM, the paper analyzes the implications of an energy or score parametrization and  shows that this simple change can lead to a better estimator. The more novel algorithm is BNEM, however, the paper does not provide enough experimental results to support the benefit of this method (see my notes under Experiments).

- Theoretical Limitations: The work makes several claims regarding the variance of the estimators which aren’t precise. For example, the claim that “the variances of EK and SK explode at high noise levels as a result of the VE noising.” This isn’t correct as the variance is a function of multiple factors, including the importance sampling proposal chosen for the estimator, as well as the energy landscape itself. Additionally, the proof of proposition 2 considers low-energy regions and claims that $exp{(\mathcal{E}(x_{0|t}^{(i)})} \geq c$. However, it isn’t clear to me how these regions are defined as the energy is evaluated at the noised samples.

**Experiments**: 
- The work contains several experiments on the same datasets and benchmarks as the previously related paper (iDEM), showing better performance of the method, especially when the number of MC samples and integration steps are limited. However, I find that additional experiments, to show the benefit of lowering the variance at the cost of increasing the bias would strengthen the claims of the paper much more. For example, the performance gain from BNEM, at the cost of increasing the bias isn’t clear in my opinion. Generally, neural networks are fairly good at training in high-variance settings (e.g. diffusion models). On the other hand, for complex energy distributions and in high dimensional settings, the bias could result in significant problems. In general, I think the authors should provide more analysis of the trade-off of bias and variance when introducing the BNEM estimator.
- The paper also claims that the proposed approach is more robust compared to iDEM as it doesn’t rely on clipping the score. However, for the LJ potentials cubic spline interpolation was used, as the energy is very sharp. It isn’t clear to me how much of an advantage this provides if smoothing is still necessary and how applicable this is to other complex and realistic settings.
- The results for iDEM on LJ-13 and LJ-55 tasks are significantly different from what iDEM paper reported. The authors also indicate divergent training for DDS, PIS and FAB on those tasks, while iDEM reported competitive values for both FAB and PIS on LJ-13 and for FAB on LJ-55. Could the author elaborate on how and why they were unable to reproduce the results?
- Some metrics such as NLL and ESS which are commonly reported in relevant works are not reported.
- In Table 3, the standard deviations over the seeds isn’t reported, and the authors report the best value, making the results misleading. For example, they indicate that the mean E-W2 of LJ-55 over the 3 seeds is in fact even higher than the one they report for iDEM. This in fact confirms my concern that improving the variance of the estimator with bootstrapping at the cost of increasing the performance doesn’t necessarily lead to increased performance.

### Questions
See above.

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
Neural sampler of Boltzmann distributions. A variation of iDEM with better variance. The central idea of iDEM and this paper is to fit a diffusion model which generates samples which are approximately Boltzmann distributed mu(x) \propto e^(-E(x)) where E(x) is the energy function. In iDEM model is learned by matching a score network to the gradient of a monte-carlo estimator of the noised energy at a given time, t. This estimator is simulation-free but very high variance, and a bi-level training scheme is introduced to stabilize training.

The key innovation in this paper is to match the energy instead of the gradient of the energy (force/score), which they show in Propositions 1 and 2, has smaller error and variance than training against the score. A second contribution in this paper using a bootstrapping scheme to further reduce variance, at the cost of introducing some bias.

### Strengths
1. The paper is clearly written and addresses an important problem
2. The authors are transparent about the limitations of the work and in particular the challenges that remain for with regard to training stability etc.

### Weaknesses
 1. Apart from the memory overhead highlighted by the authors in their limitations section, the new methods also introduce significant computational overhead, by having to use autograd to compute the derivative of the energy during sampling. This overhead is particularly concerning as it requires backpropagating through the neural network during the sampling process, which is typically a forward-pass only operation in standard diffusion models. The computational cost of this backpropagation needs to be carefully considered, especially for high-dimensional systems where the neural network is large.
2. Experiments are performed on toy systems and not systems which reflect the actual use cases of methods like this, e.g. molecules. A simple case should be included, such as ALA2. The lack of experiments on realistic systems makes it difficult to assess the practical utility of the proposed method. The toy systems used do not capture the complexities of real-world energy landscapes, such as the presence of multiple local minima and high energy barriers.
3. Missing comparisons to standard sampling baselines for non-normalized densities such as parallel tempering. In particular, considering the number of evaluations of E, and overall compute cost. The absence of these comparisons makes it difficult to assess the relative performance of the proposed method against established techniques. It is important to understand if the gains in variance reduction justify the additional computational cost compared to methods like parallel tempering or Hamiltonian Monte Carlo, which are widely used for sampling from complex energy landscapes.

### Questions
1. To point in the weaknesses, can you give an estimate of the additional overhead with the change from score to energy parameterization? Specifically, to better understand the practical utility, an empirical comparison of the it the decrease of the variance per compute unit would need to be needed.
2. The authors speculate on the use of a Metropolis-Hastings type correction in future work. How do they envision doing this within the current BNEM framework?
3. Is it possible to correct for distributional bias of the neural sampler e.g. through importance sampling? it is with many of the base-lines you compare against. If so, what is the computational cost of this compared to the baselines?
4. Why did the authors not try a standard molecular benchmark such as ALA2? Is it related to the smoothing that needs to be performed to get the LJ-n systems to train stably? If this is the case, how do you envision moving this methodology beyond toy-systems?

### Soundness
3

### Presentation
3

### Contribution
2
