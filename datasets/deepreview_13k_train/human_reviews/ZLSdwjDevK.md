# Generative Modeling on Manifolds Through Mixture of Riemannian Diffusion Processes

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Learning the distribution of data on Riemannian manifolds is crucial for modeling data from non-Euclidean space, which is required by many applications in diverse scientific fields. Yet, existing generative models on manifolds suffer from expensive divergence computation or rely on approximations of heat kernel. These limitations restrict their applicability to simple geometries and hinder scalability to high dimensions. In this work, we introduce the Riemannian Diffusion Mixture, a principled framework for building a generative diffusion process on manifolds. Instead of following the denoising approach of previous diffusion models, we construct a diffusion process using a mixture of bridge processes derived on general manifolds without requiring heat kernel estimations.
We develop a geometric understanding of the mixture process, deriving the drift as a weighted mean of tangent directions to the data points that guides the process toward the data distribution.
We further propose a scalable training objective for learning the mixture process that readily applies to general manifolds. Our method achieves superior performance on diverse manifolds with dramatically reduced number of in-training simulation steps for general manifolds.\protect\footnotemark

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper introduces the Riemannian Diffusion Mixture, a framework for generative modeling on manifolds.
- The proposed framework uses a mixture of endpoint-conditioned diffusion processes to model the generative process on manifolds.
- The paper introduces a simple and efficient training objective that can be applied to general manifolds.
- The method outperforms previous generative models on various manifolds, scales to high dimensions, and requires fewer in-training simulation steps.

### Strengths
- The paper addresses the limitations of existing generative models on manifolds, such as expensive divergence computation and reliance on approximations.
- The paper shows the applicability of the framework to general manifolds with non-trivial curvature, including synthetic distributions on triangular meshes and a 2-dimensional hyperboloid.
- Experiment shows better/ comparable results with other methods such as CNFM etc.
- The paper provides a simple and efficient training objective that can be applied to general manifolds.

### Weaknesses
 - The computation of the Riemannian divergence, which is required for implicit score matching, scales poorly to high-dimensional manifolds. This can limit the applicability of the method to complex datasets.
- The experimental validation of the method may not be comprehensive and may not cover all possible scenarios. The details of the experimental setup and results may not be easy to follow.
- The training time of the proposed framework is not extensively discussed or compared with other methods. While it is mentioned that the proposed method allows for faster training compared to previous diffusion models, a more detailed analysis of the computational efficiency and scalability of the framework would be beneficial.

### Questions
- Does the author try such method on higher dimensional manifolds?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces Riemannian Diffusion Mixture models which aim to build generative models on Riemannian manifolds. Toward this goal, the paper builds SDEs on manifolds that simulate Brownian bridges between two points on the manifold. For simple manifolds, the paper proposes a Logarithmic bridge process conditioned on the target endpoint and uses a noisy geodesic random walk approach to build an SDE. For more general Riemannian manifolds the authors propose Spectral bridge processes that use the eigenvalues associated with the Laplace-Beltrami operator on the manifold to move in a direction that minimizes this spectral distance. Empirically, the Riemannian Diffusion Mixture approach is tested on standard benchmarks for Sphere, Torii, and mesh datasets.

### Strengths
There are a few aspects to this paper that are worth highlighting. First learning generic brownian bridge processes on Riemannian manifolds is of special interest to the community and this paper's contribution to this line of work is appreciated. Second, the approach taken in this paper is also quite natural as it leverages two concepts in building a noisy path. 1.) It uses the tangent vector that minimizes the geodesic on the manifold (Logarithmic Bridge process) 2.) It uses the tangent vector that minimizes the spectral distance of the manifold. These distance-minimizing maps are conditioned on an endpoint and provide a simple target. The second idea is an extension of Riemannian Flow Matching (Chen and Lipman 2023) to Brownian bridges (SDEs) and as such quite elegant. 

The paper also introduces the idea of two-way bridge matching to reduce the computation of the calculation. Finally, the training objective is divergence-free and can be time-rescaled to minimize variance which aids more numerically stable and accurate training.

### Weaknesses
There are several weaknesses in the current draft that I hope the authors can address.

**Presentation**

In a few places, I believe there to be imprecise statements:
- The authors write "the time reversal of the noising process that accompanies score function in the drift which does not
explicitly take into account the underlying geometry.`" --- I don't think this is true as the score function on $\mathcal{M}$ uses the $\textit{Riemannian}$ gradient which needs information on the metric $g$. 
- Background: "compact manifolds". Actually, I think you consider, compact, connected, orientable Riemannian manifolds. Otherwise, you cannot define a volume form needed for the integration of probability distributions. Furthermore, the inverse of the expmap may not be well defined. Also, hyperbolic spaces do not fit this definition.
- You haven't introduced the Bolded notation and capitalized notation in eqn 1.
- What is $U$ in equation 1?
- The authors write: "the inverse of the exponential map on the manifold," Not True! For example when the exp map fails to be a diffeomorphism ---i.e. at the cut locus. As a concrete example, in the Lie group, the image of the exponential map of the connected but non-compact group $SL2(R)$ is not the whole group.

**Technical limitations**
I also have several technical concerns that I hope the authors can address.
- The authors write the Bridge process is conditioned on the endpoint $z$. But to build a Brownian bridge you need to pin both endpoints at $t=0$ and $t=T$, otherwise, it's not a bridge. Certainly, that's what is being done when you do two-way bridge matching so this focus and imprecision in the earlier parts of the text are confusing.
- One of the main claims of this paper is that the proposed approach is a lot cheaper computationally because 1.) you do not have to simulate both directions of the SDE and 2.) there is no divergence computation. However, I believe the first part of the claim is a bit misleading because you are effectively trading of variance of the objective for simulation by reusing the same sample in forward and backward matching losses. Moreover, I believe this is exactly why the proposed approach has high variance because to get a low variance estimate you would need to simulate the SDE multiple times as it is noisy so reusing samples here is counter-productive.
- It seems that when you simulate the SDE for training you are effectively caching the training samples. This approach could also readily be applied to Riemannian Flow Matching for general geometries. That is simulates the ODE and caches the samples instead of resampling time uniformly and then simulating the ODE up to that time point for every Loss computation step. So I would love to have a fair comparison to see the numerical benefits to substantiate the faster training claim.
- The authors comment that the time-rescaled proposal distribution $q(t)$ is different than Huang et. al 2022. I disagree, this is the exact same idea that you can resample time instead of uniformly sampling it. Huang et. al 2022 do this using a 1-d flow which is quite cheap and can be done as a pre-processing step while here it is a constant. These are essentially the same but the proposed approach is a cruder approximation.
- The Table 1 results are problematic for two reasons. First, these earth science datasets have known issues and lead to wildly different results based on the subset used for training and test sets. This largely means that we cannot take table numbers from other papers. A quick check shows that the baseline numbers are copied from the papers and looking at the provided code it seems the baselines were not implemented. This leads me to believe that the authors did not try the baselines themselves on the **same training and test splits** as their own reported models. As a result, this table is not useful and cannot be compared. I actually the proposed method will likely be even better if all baselines are compared properly. So I encourage the authors to include this in the updated paper.
- A major claim in the paper is the ability of the method to start from any prior distribution on the manifold to hit any target. This is a strength that vanilla diffusion models do not have. However, I could not find an experiment in the main paper where this is exploited.
- Another claim in the paper is that the method can scale to high dimensional problems, but the largest dimensionality problem is a Torii of $10^3$ dimension. This is hardly a high dimensional manifold as Torii can be written as a product group $S^1 \times S^1 \times \dots \times S^1$ and each manifold in the product is simple and does not need to actually utilize the difficulty that comes with high dimensions. I would consider toning down this claim.


If all of my concerns are addressed I am willing to upgrade my score.

### Questions
1.) The noisy paths learned by this approach do not appear to be optimal in the sense of matching the empirical marginal densities. Can we make this better and perhaps more numerically stable by using Optimal transport paths like done in OT-Flow matching (Tong et. al 2023) for Euclidean geometries?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to approach generative modelling on Riemannian manifolds by constructing a mixture of diffusion processes. This is achieved by defining a family of stochastic processes with explicit drift terms that mimic the Euclidean Brownian bridge drift, and mixing the drift according to the data distribution. The authors show how training can be achieved in this scheme.

### Strengths
- the authors approach diffusion generative modelling on manifolds with new ideas
- guiding a diffusion process by mixing tangent directions to the data distribution is a nice idea

### Weaknesses
 - the presentation is a places not clear. For example, I have a hard time extracting meaning from a sentences such as "In addition, previous diffusion models on the manifold are geometrically not intuitive as their generative processes are derived from the time reversal of the noising process that accompanies score function in the drift which does not explicitly take into account the underlying geometry." I believe the score of a Brownian motion is indeed quite related to the underlying geometry?
- as far as I can read, the class of processes in equation (3) are not new (they are claimed to be new in the paper). In the stochastic analysis literature, they are denoted 'Fermi bridges' see https://arxiv.org/abs/1604.05182 They have been used for bridge simulation in e.g. https://arxiv.org/abs/2105.13190 and https://arxiv.org/abs/2104.03193 . I haven't seen them used in context of generative modelling though.
- I am unsure what is the main benefit of the approach: The score matching in denoising diffusion models is replaced by a loss depending on the distance which is also in general expensive to compute (the logarithm map (inverse exponential) on general manifolds is expensive to compute). I am not sure of the general validity of claims such as 'Our method shows superior performance on diverse manifolds that can scale to higher dimensions' because logarithm map computations can be quite non-trivial in high dimensions
- I don't think the authors convincingly argue why (11) is fast to evaluate. As I read it, it will require a large amount of logarithm evaluations during training. The spectral bridge processes can speed this up, but finding eigenfunctions of the Laplace-Beltrami operator on high-dimensional manifolds is likely not feasible

### Questions
I would be great to hear convincing counterarguments to the weaknesses listed above. I think the approach has merit, but the weakness listed above makes me unsure about the actual benefit of the method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
