# Comparing noisy neural population dynamics using optimal transport distances

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
Biological and artificial neural systems form high-dimensional neural representations that underpin their computational capabilities. Consequently, methods for quantifying geometric similarity in neural representations have become a popular tool for identifying computational principles that are potentially shared across neural systems. These methods generally assume that neural responses are deterministic and static. However, responses of biological systems, and some artificial systems, are noisy and dynamically unfold over time. Furthermore, these characteristics can have substantial influence on a system's computational capabilities. Here, we demonstrate how existing metrics fail to capture key differences between neural systems with noisy dynamic responses. We then propose a metric for comparing the geometry of noisy neural trajectories, which is based on ``causal'' optimal transport distances between stochastic processes. We use the metric to compare models of neural responses in different regions of the motor system and to compare the dynamics of latent diffusion models for text-to-image synthesis

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel metric for comparing noisy neural population dynamics based on the notion of causal optimal transport, which respects temporal causality. Other methods in the field generally assume deterministic or static neural activity, missing key aspects of biological and artificial neural systems. They validate their metric in a biological task (synthetic motor control experiment) and artificial task (conditional image generation in diffusion) and find that their metric distinguishes different neural trajectories properly.

### Strengths
- The paper is well written, providing a good motivation and background on the limitations of current metrics such as SSD and Procrustes Shape Analysis in distinguishing different types of neural dynamics. The mathematics of optimal transport is well presented and motivated with good explanations of the intuition behind the new metric. 
- The paper provided three sets of experiments: scalar task comparing the different metrics mathematically, synthetic for biological motor control, and latent diffusion models. 
- The discussion on disentangling recurrent dynamics from input-driven dynamics really highlights importance of considering temporal dependencies in the data.

### Weaknesses
 - As mentioned by the authors themselves, the metric lies on an assumption of Gaussian neural processes, which does not hold for biological and artificial neural systems. It may not apply to non-Gaussian data as it won't be able to capture the higher-order statistical dependencies between the trajectories. Specifically, the method relies on matching first and second-order statistics, which are insufficient to characterize distributions with significant skewness or kurtosis. This limitation could lead to misinterpretations when comparing neural trajectories with complex, non-Gaussian dynamics. For instance, two neural populations might exhibit similar means and covariances but drastically different higher-order moments, which would be missed by this metric.
- Estimating full covariance matrices for high-dimensional neural data (large N and T) is computationally intensive and probably requires a prohibitive number of samples. The number of parameters to estimate scales quadratically with the dimensionality of the neural data, making it impractical for large-scale neural recordings. This computational burden is not only about processing time but also about the amount of data required to obtain reliable estimates of the covariance matrices. Furthermore, the estimation of high-dimensional covariance matrices is prone to noise and instability, especially when the number of samples is not significantly larger than the dimensionality.
- The paper mentions Dynamical Systems Analysis by Ostrow et al. in the end of the paper as a possible future direction. It would be nice if the authors can actually include a comparison to that method in the current paper, as they compare Causal OT to Procrustes and SSD, but DSA seems to be a better method for studying neural dynamics than both of them. The lack of comparison to DSA, a method explicitly designed for analyzing neural dynamics, makes it difficult to assess the relative advantages and disadvantages of the proposed Causal OT metric in the context of existing tools.

### Questions
- I would love to see theoretical or empirical analysis of the metric's robustness to deviations from Gaussianity. I know this was briefly mentioned in the section on Diffusion, but I would like to see a demonstration of the metric's performance as you increase the impact of higher order statistical moments such as skewness or kurtosis. 
- The metric is computational expensive. Can it be reduced using some dimensionality reduction techniques that preserves stochastic and temporal structure (maybe Dynamic Mode Decomposition or Tensor Factorization)? Can you impose structure on the covariance matrices, such as low-rank approximations or sparsity constraints, to reduce the number of parameters to estimate? 
- Can you comment on how this method is affected by the observations in Qian et al. 2024 (Partial observation can induce mechanistic mismatches in data-constrained models of neural dynamics) that points out challenges in identifying mechanisms in neural data (such as line attractors) based on partial observation of neural data.
- I would like to see experiments comparing Causal OT to DSA in some way.
- I would like to see an example applies to actual neural data such as calcium imaging or electrophysiological recordings available publicly and see if the metric can distinguish between neural trajectories coming from different experimental conditions. This might be hard to do within the review period, but it would greatly improve the paper's quality and would motivate me to increase the score substantially.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new metric for comparing noisy neural trajectories. The metric is based on computing optimal transport distances between gaussian processes. While the metric can in principle be used to compare any two stochastic processes, the authors justify the metric rigorously for linear-time varying stochastic processes. To support their theoretical claims, the authors provide several numerical examples where their new metric performs better than two previously proposed metrics (Procrustes and SSD).

### Strengths
The paper is _very_ well-written, well-motivated, and timely. The mathematical exposition is especially clear. The numerical experiments are also nice.

### Weaknesses
The major weakness of the paper is the lack of numerical comparisons to Dynamical Similarity Analysis (DSA), introduced by Ostrow et al, 2023. This omission is very puzzling, since the authors mention DSA early and often, and even use some of the same tasks as DSA (Fig 2). Specifically, a direct comparison of the proposed metric against DSA on the experimental setups presented in Figure 2 would strengthen the paper's claims. While the authors state that DSA is theoretically justified for deterministic systems, a practical comparison on the stochastic systems considered in this paper would provide valuable insights into the relative performance of the two methods. Even if DSA outperforms the proposed metric on some tasks, this does not diminish the value of the proposed method, especially considering its theoretical grounding in stochastic processes. Furthermore, the phrasing in L046-L047 could be clarified to accurately reflect which studies addressed stochasticity and dynamics. Lastly, the claim in L050 regarding DSA needs further substantiation within the paper, as it is not explicitly demonstrated. Finally, there appears to be a missing time dependence in the $A^\top$ term of Equation 3.

### Questions
Why not compare to DSA? Even if DSA does "better" on some of the tasks, that does not make your method less valuable. As you point out, DSA is only theoretically justified for deterministic systems. Therefore, _I will be happy to raise my score if these comparisons are included, regardless of comparative performance._

EDIT 11/21--The authors have included the analysis I asked for. I have accordingly raised my score. 

### Minor points:
- L046-L047: The phrasing makes it sound like both studies addressed stochasticity and dynamics.
- L050: You don't actually show this for DSA, as far as I can tell. 
- Equation 3: There is a missing time dependence in $A^\top$.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new notion of distance between Gaussian processes based on optimal transport between them. The innovation is in considering correlation across time, such that the optimal transport incorporates information across time but respects causality. In particular, this allows the distance to differentiate processes which are indistinguishable when comparing their marginal moments. This distinction is shown to be relevant in a neuroscience-inspired synthetic problem, where distances which compare only marginal moments fail to distinguish small magnitude time segments which have high correlation with other time segments. These distances are also used to compare the output trajectories generated by denoising diffusion image models.

### Strengths
* The presentation throughout is very clear and a pleasure to read.
* The motivation of the method through prior work is exceptionally good.
* The method this paper proposes is intuitive but original, fairly simple, well-motivated, and seems to be a substantial extension of previous work.
* The experimental evaluation is appropriate.

### Weaknesses
 * The experimental evaluation is a bit terse, and doesn't demonstrate a clear advantage for this paper's method over SSD across the board. The method is only evaluated on synthetic neural data even though neuroscience is the clearest application for these ideas. Why not try the it on the actual reaching data which inspired the synthetic dataset?
* I'm unsure how important the problem this method addresses is -- the extent to which it's useful to compute distances between stochastic processes for applications like comparing diffusion models or brains is not clear.

### Questions
* I would appreciate some discussion of the derivation of the causal OT distance in the main body. This seems important to justifying how it can be viewed as an OT distance.

### Soundness
3

### Presentation
4

### Contribution
3
