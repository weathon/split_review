# Reflected Schr\"odinger Bridge for Constrained Generative Modeling

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Diffusion models have become the go-to method for large-scale generative models in real-world applications. These applications often involve data distributions confined within bounded domains, typically requiring ad-hoc thresholding techniques for boundary enforcement. Reflected diffusion models aim to enhance generalizability by generating the data distribution through a backward process governed by reflected Brownian motion. However, reflected diffusion models lack the flexibility to adapt to diverse domains and do not guarantee optimal transport properties. To overcome these limitations, we introduce the Reflected Schrödinger Bridge algorithm—an entropy-regularized optimal transport approach tailored for generating data within diverse bounded domains. We derive elegant reflected forward-backward stochastic differential equations with Neumann and Robin boundary conditions, extend divergence-based likelihood training to bounded domains, and explore natural connections to entropic optimal transport for the study of approximate linear convergence—a valuable insight for practical training. Our algorithm yields robust generative modeling in diverse domains, and its scalability is demonstrated in real-world constrained generative modeling through standard image benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper generalizes shrodinger bridge models to constrained domains. The construction uses reflected brownian motion to construct the diffusion processes and an IPF procedure to fit the machine learning component. Compared with the previous work on score based reflected diffusion models, this method has the added benefit of being more generalizable across geometries and base distributions.

### Strengths
* The proposed framework is technically sound and helps overcome fundamental issues with working with the more complex geometry of the base space.
*  The technical constructions are constructed very cleanly with a full explication of the strengths and limitations of the underlying model.
* The technical analysis showcase theoretical speedups for convergence, which can be important on more complicated geometric base spaces.

### Weaknesses
 * I wouldn't say that [1] doesn't necessarily propose approaches to deal with general geometries. In particular, they propose a diffeomorphic mapping scheme that should help generalization to other spaces although there are of course analytic blowups at edges/corners.
* There could be more experimental results. In particular, the current results mostly show that the method works and can scale to high dimensions. Importantly, a more involved example (e.g. high dimensional simplex) would be needed to show that the method retains its niceties, as compared with [1].

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose to extend the Schrodinger Bridge methodology to state space which are defined by constraints. They follow closely the methodology based on Forward Backward Stochastic Differential Equations (FBSDEs) introduced in [1]. The main contribution of the paper is to extend this set up to the case where the FBSDEs are replaced with a reflected FBSDE. This is in accordance with the recent works of [2,3] who study reflected versions of diffusion models. Another contribution of the paper is to study the convergence of Iterative Proportional Fitting (IPF) approaches. In that setting, the authors follow [4]. The authors also illustrate the efficiency of their method with 

[1] Chen et al. (2021) -- Likelihood Training of Schrödinger Bridge using Forward-Backward SDEs Theory

[2] Lou and Ermon (2023) -- Reflected Diffusion Models

[3] Fishman et al. (2023) -- Diffusion Models for Constrained Domains

[4] Chen et al. (2023) -- Provably Convergent Schrödinger Bridge with Applications to Probabilistic Time Series Imputation

### Strengths
* The extension of the Schrodinger Bridge framework to the reflected setting is new to my knowledge. 

* The convergence guarantees presented in the paper are also interesting (although see my comments in the "Weaknesses" section for some concerns I have regarding their novelty and soundness).

* I appreciate the fact that the authors produce extensive experiments and compare themselves to [1]. 

[1] Lou and Ermon (2023) -- Reflected Diffusion Models

### Weaknesses
 * My main concern is with the motivation of the paper. While it is certainly possible (as shown by the authors) to extend the Schrodinger Bridge framework to the reflected setting it is not clear why one would like to do this. I think that a contribution to a top tier venue such as ICLR requires more motivation (either theoretical, methodological or experimental), note that I am not talking about the novelty here (there is no doubt that the presented work is novel). It seems that the authors want to put forward that Schrodinger Bridge has the ability to reduce the length of the integration time in generative modeling (a reason first put forward in the work of [1]) "Notably, the forward process (1a) requires a long time T to approach the prior distribution, which inevitably leads to a slow inference". However there already exist many works focused on improving the speed of diffusion models (distillation, better samplers, etc.) which have proven to be more efficient than Schrodinger bridges.

* The authors claim that Proposition 1 is a valid ELBO, however this result is only true at equilibrium. It is no longer true when the vector fields are parametric functions. 

* I am not very convinced by the significance of the empirical results. As I emphasized earlier, I appreciate the fact that the authors provide an extensive image investigation, however the results are not very convincing. The quality seems to be worse than [2]. If the authors claim that the reflected SB method improves the speed of the generation then it would have been useful to compare NFE.

* It is not clear at all for me what are the differences between the theoretical section and the work of [3]. The work of [3] is cited but not comparison or discussion is provided. 

* The assumption A4 is very strong. It is claimed that it is similar to the one of [4] but this is not true. In fact, the assumption of [4] only holds for one iteration of the IPF. The stability of the approximation across IPF iterations is not clear at all and should be discussed. 

Minor comments:

* In the introduction [5] should be cited when citing [6] as the works are concurrent.

* In (3) missing index $t$ in $x_t$ 

* When deriving the reflected FBSDE framework I would have appreciated more emphasis on the introduced quantities.

* Could the authors be more precise on the algorithmic differences between the introduced algorithm and the one of [7]?

* It would be very interesting to understand if the current setting can accomodate for an understanding of the dynamic thresholding procedure used in [8]

### Questions
Please answer to the main comments in the "Weaknesses" section. The authors should focus on the motivation of their method. As of now, it is not clear what are the key contributions of the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors combine reflected SDEs [1] with the diffusion schrodinger bridge methodology [2] and IPF training scheme. This enables regularized OT on constrained domains. The authors show good empirical performance.

[1] Lou and Ermon Reflected Diffusion Models, 2023 \
[2] Bortoli et al Diffusion Schrodinger Bridge 2023

### Strengths
- In general equations and methods appear correct
- This provides a neural entropic OT approach to constrained domains, which is novel as far as I am aware (other diffusion and or simple mapping approaches are not capable of this)
- Generation performance is good for image datasets

### Weaknesses
 - This is a straight forward connection between reflected SDEs [1] and schrodinger bridge IPF [2,3], without a clear reason or motivation. The paper does not adequately explore the specific benefits of this combination, such as a reduced number of diffusion steps or the advantages of entropic OT on constrained spaces. It is not clear how this method is beneficial compared to existing approaches.

- Likelihood based training of IPF appears incorrect. The first terms in algorithm 1 involve expected $\log y_T$ and $\log y_0$ starting from points from the alternate marginal distribution $x_0$ and $x_T$ respectively. My understanding form [3] is that these are the result of simulating the diffusion backwards and hence depend on the parameters of the networks. These log terms do not coincide with the log densities of the target measures unless the IPF procedure has converged, hence these one cannot simply ignore them and use this as a loss without taking gradients through the diffusion simulation. I would argue this is not likelihood training and [3]'s argument is incorrect unless there's the assumption that the method has already converged, in which case there is no need for further iterations? This point is critical as it undermines the theoretical justification of the training procedure. It has been shown by the same authors of [3] that this coincides with regular IPF of [2] and does not require this (incorrect) likelihood derivation.

Minor:

- Section 1: Shi et al 2023 does not use IPF but IMF.
- Vargas et al 2021 does non perform SB on high dimensional examples as claimed, maximum dimension is 4..
- There are many other constrained domain diffusion methods e.g Fishman et al Diffusion Models for Constrained Domains 2023
- The authors mention other related work such as Riemannian SGM Bortoli et al 2022, it should be noted that even more relevant to this work is SB and hence OT has been performed on manifolds in Thornton et al Riemannian Diffusion Schrodinger Bridge, 2022

### Questions
What are the applications and significance of OT on constrained domains?

Does the proposed method use fewer diffusion steps to obtain similar results to non SB constrained methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
