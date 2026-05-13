# Manifolds, Random Matrices and Spectral Gaps: The geometric phases of generative diffusion

- Decision: Accept
- Scores: 6, 5, 6, 6, 5

## Abstract
In this paper, we investigate the latent geometry of generative diffusion models under the manifold hypothesis. To this purpose, we analyze the spectrum of eigenvalues (and singular values) of the Jacobian of the score function, whose discontinuities (gaps) reveal the presence and dimensionality of distinct sub-manifolds. Using a statistical physics approach, we derive the spectral distributions and formulas for the spectral gaps under several distributional assumptions and we compare these theoretical predictions with the spectra estimated from trained networks. Our analysis reveals the existence of three distinct qualitative phases during the generative process: a trivial phase; a manifold coverage phase where the diffusion process fits the distribution internal to the manifold; a consolidation phase where the score becomes orthogonal to the manifold and all particles are projected on the support of the data. This `division of labor' between different timescales provides an elegant explanation on why generative diffusion models are not affected by the manifold overfitting phenomenon that plagues likelihood-based models, since the internal distribution and the manifold geometry are produced at different time points during generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the generative process of diffusion models, meaning how samples of the target distribution are generated starting from random initial values, by looking at spectral gaps in the Jacobian matrix of the score function. 

The manifold hypothesis is adopted and, in order to conduct a mathematic analysis, the authors consider the simplified case of linear manifolds and Gaussian target measures. In this setting, the temporal evolution of the spectra of the Jacobian is computed either analytically or through a Replica computation, and the resulting spectral gaps are used to estimate the dimensionality of the data-manifold.

The main result of the paper is that, during the generative process, there is a series of spectral gaps opening, each corresponding to a different local subspace (this phase is denoted Manifold Coverage). Then, the more the process gets close to t=0, the more these gaps shrink, except from the principal one, which is the only one sharpening and remaining asymptotically.

The authors verify this theoretical prediction on synthetic datasets, by learning the score with a Neural Network and looking at the empirical distribution of the respective Jacobian.

Finally, some experiments on image datasets are presented, to look at whether the phenomenology described for linear manifolds is valid, in some way, also for more realistic settings.

### Strengths
- The paper is fairly-well written.
- The authors adopt an interesting new perspective on the study of generative diffusion processes.

### Weaknesses
- Section 7: The justification of the discrepancy in Fig. 6 between the analytical (replica) and the empirical results is weak, in my opinion. If the Neural Network is expressive enough to learn the exact score, shouldn't we expect the two curves to overlap? If one does the same experiments for the isotropic case for which an analytic solution is available, does one get the same discrepancy?
- Section 8: The results for Cifar10 and CelebA do not show the appearance of any spectral gap. I didn't understand the justification at the end of Section 8. Also for MNIST, while a spectral gap seems to appear at small values of $t$, it seems to indicate a dimensionality of the manifold of around 700. How is this compatible to the fact that the dataset considers only 10 classes?
- [minor]: In the Introduction, the Jacobian is mentioned, but it should be said it is the Jacobian of the score.

The paper presents many typos, here is a list of the ones I found (there could be many more):
- Line 40: models should be modes
- Line 66: idealize should be idealized
- Line 113: is is
- Line 126: Eq. (2) should be Eq. (1)
- Line 229: the the
- Line 357: spearated 
- Line 501: temputal
- Line 510: suble

I suggest a careful reading to correct any additional typo present.

### Questions
- I find the definition of the "support score", and later of the "stable latent manifolds" in Eq. (5), very confusing. Why are the manifolds defined in this way? What is the role of this definition for the rest of the paper? It seems to me that from Eq. (6) onward, this support score is not mentioned anymore and we come back to the normal score.
- Line 131: "radius $\sqrt{t}$" should be "radius proportional to $\sqrt{t}$"?
- I don't know how to reconcile the phenomenology described in Section 5 with the results presented in the later sections. Indeed, from the plots shown in Fig. 3 and 4, it seems that at all times we are in the so-called "Manifold Coverage" phase, with the intermediate gaps open. Does this mean that the "trivial phase" is only at $t=\infty$ and the "consolidation phase" is only at $t=0$? In general, I think the point of separation between these three phases is not well defined.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides a random-matrix theory derived result computing the exact eigenspectra of the score of a diffusion modeling a distribution supported on a linear submanifold of a sample space. This distribution is a Gaussian supported on a hyperplane in Euclidean space. A three phase process on the eigenvalues is observed in the diffusion placed on the modeled density. This theoretical computation matches the observation of a number of previous works studying the eigenspectra of the score function of diffusion models.

### Strengths
- The results are of some interest and validate observational results of the change in distribution of the eigen spectra of the score function of diffusion models through time.

### Weaknesses
- The setting studied is a rather limited setting, and given the linear nature of the submanifold the density is supported on, and the Gaussian nature of the density.
- The experimental section of the paper is very light and leaves many questions unexplored.

### Questions
- The experimental detail of section 7 is very light and lacks much detail needed for recreation. For example the number of samples from the distribution from training is missing.
- Section 7 leaves a poignant question unexplored - how does the number of samples from the data distribution used to train the score function affect the empirical results in estimating the dimension of the data manifold. The distribution of eigenvalues obtained in the results appear to not mach perfectly the theoretical results. Is this due to modeling issues, the amount of data used, or some other issues? Exploring a range of dataset sizes may shed some light on why the image experiments fail to show the definitive eigenspectra cliff needed to detect the intrinsic data dimensionality. Perhaps these datasets simply don't contain enough examples to learn the score well.
- If the conclusion of section 8 is that for real datasets the proposed method of looking at the distribution of eignevalues of the score function fails to detect the intrinsic dimensionality of the data, can the authors comment on how this menthod might be of practical utility in training or understanding diffusion models?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a theoretical perspective on generative diffusion models under the manifold hypothesis, focusing on the spectrum of the score function's Jacobian. The authors propose that spectral gaps indicate the presence and dimensionality of distinct sub-manifolds. They derive analytical forms of the spectrum under the assumption that the manifold is a linear subspace, revealing three phases in the generative process: a trivial phase, a manifold coverage phase, and a consolidation phase. THey argue that this division explains why generative models avoid the manifold overfitting issues seen in likelihood-based models.

### Strengths
1. The perspective on generative diffusion models, focusing on the spectrum of the score function's Jacobian, appears novel. 

2. The three-phase framework in generative diffusion models provides insight into model behavior across different generative stages.

3. The approach is supported by mathematical derivations under a linear assumption and is further validated with illustrative examples on toy datasets like MNIST.

### Weaknesses
1. The linear assumption is overly restrictive and unlikely to hold in practical scenarios, limiting the generalizability of the theoretical results.
2. The real data results on CIFAR-10 and CelebA (Figure 7) are difficult to interpret and lack sufficient clarity to be fully convincing.
3. In Section 5, the conjecture that "their phenomenology captures the main features of subspace separation in the tangent space of curved manifolds" lacks a clear intuition or justification, making it unconvincing based on the current presentation.

A minor issue:
There are some citation formatting issues. For example. the third reference in the first paragraph of the intro, should be Song et al, instead S et al. See also the B. et all in the same paragraph, and so on.

### Questions
Following the above weakness, I have the following questions. 

1. Can the authors either show some results for nonlinear manifold? If not, at least certain discussion is expected.
2. Can the authors further discuss the results on CIFAR-10 and CelebA? These results are not sufficient to support the claim in the paper, nor the conjecture. 
3. This is not really a question. At a first glance I thought this is a theoretical paper, but after reading it carefully I feel it's more like a summary and conjecture based on empirical observation, as the theoretical part is only restricted to linear models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the spectral properties of generative diffusion models within the framework of the manifold hypothesis. By analyzing the spectrum of the Jacobian of the score function, the authors identify and interpret three distinct phases in the generative process: trivial phase, manifold coverage phase, and manifold consolidation phase. These phases explain the internal distribution alignment and resilience against manifold overfitting, which is often seen in likelihood-based models. Through a mix of theoretical analysis using linear manifolds and random matrix theory, alongside high-dimensional experiments on image datasets, the paper demonstrates how these phases manifest and validate the theory.

### Strengths
* Clear exposition, good fit in the existing literature
* The analysis of the Jacobian spectrum and its phase-wise evolution provides a meaningful interpretation of the manifold structure and how diffusion models capture it
* Using linear manifolds and random matrices enables tractable and insightful theoretical analysis supporting the findings.
* Experiments on complex datasets, such as MNIST and CIFAR-10, align with theoretical predictions, showing the three observable phases.

### Weaknesses
* Introducing the mathematics for manifolds earlier could clarify the manifold overfitting problem and improve the logical flow.

See questions

### Questions
* In section "The linear random-manifold score in large dimensions: A random matrix analysis", is the approach aimed to study the behaviour of diffusion models when encountering random datasets?
* In Equation (5), $M_t$ appears to represent the manifold where noised data reside. Is the idea that particles are found in shells of radius $\sqrt{t}$ around the latent manifold consistent with this? If $M_t$ is not merely a union of spheres centered on data points (I don't think I believe it is the case), what precisely is its mathematical function? I understand you want to consider a specific space on which the noised data lies, in order to use the intepretations deriving from (6), but I don't think introducing $M_t$ is a good mathematical strategy

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to understand the diffusion models from the geometry of the latent space. The authors did analysis in terms of the spectrum of the score functions' Jacobian, from which the spectral gaps indicates three learning phases of the models. Further, the authors reasoned that the fitting of the distribution and the manifold geometry are disentangled so to explain the indifference of diffusion models to the manifold overfitting.

### Strengths
I think this paper is the first work using random matrix to analyze the jacobian in diffusion models, though the idea of analyzing high-dim jacobians using random matrix theory is not new, assuming I read enough literature on understanding diffusion models. Understanding diffusion models, especially from the latent space geometry, is increasingly researched and this paper provides a new way of approaching this analysis.

### Weaknesses
1. The paper is delivered in a rather vague way and there are multiple important points which should be clarified in terms of either equations, or citations on other literatures. When carefully reading the paper, I couldn't really parse the ideas at several important locations, though some of these unclear points are only explained later on in a more concrete way in Section 6. I have detailed a few of them in the questions section. 
2. The paper strives to better understand the generative diffusion models. While I appreciate the effort using RMT (random matrix theory), the analysis does not really offer deep insights to diffusion models.  In the practical diffusion models, the analysis in Figure 7 merely demonstrated there is a eigenspectrum transition in the Jacobian of the trained model on MINST, which does not have an apparent link to the three phases proposed in the paper. Similar observations have already been shown by _Diffusion Models Encode the Intrinsic Dimension of Data Manifolds_. It would be great if authors could point out the difference or novel insights compared to this work. 
3. The paper _Dynamical Regimes of Diffusion Models_ showed the three phases of the generative process in diffusion models using phase transition analysis where these key transitions are also analyzed via the distributional solution of the forward dynamics. These transitions are determined by not only the eigenvalues of the covariance matrix of the data, but also the entropy of the noised data distribution. It really interests me to see the difference between the analysis in this work and the one in _Dynamical Regimes of Diffusion Models_. So it's necessary to point out the new results from this paper compared to the previous analyses.
4. I try to locate in the paper where these different phases explains why diffusion models are prone to manifold overfitting. Unfortunately, I could not find it. It's mentioned in section 2 that likelihood based models lead to increasing model density during training (091-092), thus, resulting in the manifold overfitting. Could authors explain how the three phases of diffusion models help them to be unaffected by the manifold overfitting from this perspective? For example, add a section or paragraph that explicitly connects their three-phase model to the issue of manifold overfitting, explaining step-by-step how each phase contributes to avoiding this problem

### Questions
1. (044-045) These decomposition phenomena cannot be directly explained in terms of critical phase transitions as they are fundamentally linear processes. 
   - This reasoning is not clear to me. 
   - I assume authros wanted to explain the separation of subspaces in diffusion models using the phase transition idea, much like how B. et al. 2024a explained the separation of data classes. 
   - what's the main difference of this work from B. et al. 2024a?
2. 091-095 meantioned that the divergence of data distribution implies the model density becomes larger during training. Could authros elaborate on this? Moreover, when claiming diffusion models having three phases are unaffected by manifold overfitting, could authors provide the analysis accordingly in comparison to the likelihood based models? 
3. 096-097: it's pointed out in this work, diffusion models are not affected by the manifold overfitting. Could authors provide some evidence on this, e.g., literatures? 
4.  140-146: it's not straightforward to see how perturbations aligned to the tangent space of the manifold correcpond to small eigenvalues, while the orthogonal ones correspond to high eigenvalues. Could authors provide more details on this?
5. It's hard to parse Fig 1. Is this at a fixed time t?  I checked the cited paper Stanczuk et al. 2022, but it's still unclear to me. Why the x-axis is latent dimensionality? I do not directly see the link that perturbations more aligned to the tangent space of the manifold are located at the regim of smaller latent dimentionality, not the orthogonal ones have larger dimensionality. How do you find the one-to-one correspondence between the eigenvalues and the latent dimensionality? In Stanczuk et al. 2022, the authors pointed out that the vanishing singular values correspond to the tangent space, while the large ones correspond to the normal space. But it seems there is some nontrivial steps needed from there to here. 
7. 172: The phase separation do not correspond to singularities as there are cross-over events, not genuine phase transitions. 
   1. what are singularities in this context? 
   2. what are cross-over events?
8. It seems $\sigma_k$ is not defined. I assume it is the variance of the data distribution over manifolds with different dimensions. When would $\sigma_{k+1}^2\ll \sigma_k^2$ happen? 
9.  What is asymptotic closure? Do you mean the end time of the phase II can be infinite and one considers an approximate of when this closure happens? 
10. Please also define $r$ in line 481.

Other suggestions:
- I think the template of the paper is different from the provided one.
- Please correct and unify the bibliography.

### Soundness
2

### Presentation
1

### Contribution
2
