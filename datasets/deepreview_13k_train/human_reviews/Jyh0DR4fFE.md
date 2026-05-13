# Injective flows for star-like manifolds

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Normalizing Flows (NFs) are powerful and efficient models for density estimation. 
When modeling densities on manifolds, NFs can be generalized to injective flows but the Jacobian determinant becomes computationally prohibitive.
Current approaches either consider bounds on the log-likelihood or rely on some approximations of the Jacobian determinant.
In contrast, we propose injective flows for star-like manifolds and show that for such manifolds we can compute the Jacobian determinant exactly and efficiently, with the same cost as NFs.
This aspect is particularly relevant for variational inference settings, where no samples are available and only some unnormalized target is known.
Among many, we showcase the relevance of modeling densities on star-like manifolds in two settings.
Firstly, we introduce a novel Objective Bayesian approach for penalized likelihood models by interpreting level-sets of the penalty as star-like manifolds.
Secondly, we consider probabilistic mixing models and introduce a general method for variational inference by defining the posterior of mixture weights on the probability simplex.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a normalizing flow technique for a specific class of manifolds in which the computation of the Jacobian determinant is both exact and efficient, while related works rely on approximations or predefined manifolds. This approach is particularly relevant for variational inference problems where the manifold is known, and the goal is to approximate a density on it. The effectiveness of the method is demonstrated through variational inference on well-designed problems that meet the manifold constraints.

### Strengths
- The general idea of focusing on this class of manifolds, which has desired properties, is both simple and interesting, and the technical aspects appear solid.
- Based on the experiments conducted, the proposed model supports the claims.
- The paper is generally well-written and well-structured (see Questions for some suggestions).

### Weaknesses
 - Even if this class of manifolds is useful for density modeling in the considered scenarios, it becomes somewhat restrictive if the $r(\theta)$ is not trainable. This limitation is particularly pronounced in scenarios where the underlying manifold is not precisely known or is subject to deformation, as the fixed radial parameterization would not be able to adapt to these changes. The lack of flexibility in $r(\theta)$ could lead to suboptimal density approximations, especially when the true posterior deviates significantly from the assumed manifold structure.
- Further experiments and/or comparisons with related works, such as in a maximum likelihood setting, could have been beneficial for demonstrating both the effectiveness and efficiency of the approach. The current experiments, while supportive, are limited to variational inference and do not explore the performance of the proposed method in other relevant settings, such as maximum likelihood estimation. This lack of broader evaluation makes it difficult to assess the general applicability of the approach and its competitiveness against existing methods in different contexts.

### Questions
Q1. I believe Fig. 2 does not significantly aid in understanding the proposed approach, and a more intuitive figure could better illustrate the concept of the injective flow graphically. Additionally, moving the proof sketch to the appendix could free up space for a more intuitive figure(s), details on the mappings considered (e.g., as in Appendix A.5), and discussions on variational inference, maximum likelihood, and additional experiments.

Q2. The proposed approach appears to rely on the circular bijective layers of Rezende et al. (2020); a brief description in the appendix would be helpful. How does this approach scale in higher dimensions, and is this critical to the proposed approach?

Q3. Regarding experiment 5.1, is it possible that the density effectively modeled through the spherical flows (circular bijective layers) used for the transformation $\mathcal{T}_{\theta}$?

Q4. It would be interesting to include some (synthetic 2D or 3D) experiments where the manifold is more complicated, such as variational inference problems with a posterior concentrated on a star-shaped manifold, where $r(\theta)$ is potentially a learnable function.

Q5. Minor: What is meant by the density will be expressed in Cartesian coordinates (line 160)? Does this simply mean that the push-forward samples $x$ are just points in the ambient space?

### Soundness
3

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
A method is presented for efficiently computing normalizing flows on star-shaped d-manifolds embedded in (d+1)-dimensional Euclidean space. Using a decomposition based on spherical coordinates, the Jacobian determinant can be analytically computed in O(d^2) time. Numerical examples are given to show that the method outperforms the (d+1)-dimensional default sampler.

### Strengths
1. Paper is well written and readable.
2. The method is clearly explained and understandable, and it improves over sampling in the ambient dimension.
3. Claims are supported with proof and numerical evidence.

### Weaknesses
1. The method only applies to star-shaped manifolds embedded in one dimension higher. The authors acknowledge the limitation that their proof cannot be extended to manifolds with higher co-dimension. This is the main concern with the method - since this method only applies to a very specific class of co-dimension 1 submanifolds, I wonder about its applicability to problems of general interest. Since the method applies to a very specific class of manifolds instead of a more general class, the benefits for this specific class need to be greater to warrant acceptance into ICLR, in my opinion
2. The numerical examples seem limited (as a result of 1). To justify this approach, more examples of star-shaped manifolds and real-world applications should be presented and/or the benefit of the method over normal normalizing flows should be significant.

### Questions
1. The asymptotic efficiency of the method is shown to be O(d^2), it could be interested to look at the rate in more detail. Specifically, I am curious about the constant factors in the rate as compared to the normal normalizing flow methods. This can be done either analytically or empirically with comparisons of runtimes.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the substantial computational cost associated with normalizing flows when applied to densities on manifolds. The proposed method is specifically tailored for star-like manifolds and efficiently computes the Jacobian determinant, outperforming standard normalizing flows. Furthermore, the paper introduces Bayesian methods for penalized likelihood models, where penalty level-sets are regarded as start-like manifolds, and variational inference methods for probabilistic mixture models.

### Strengths
- The proposed injective flow method for star-like manifolds significantly reduces the standard complexity of $O(d^3)$ to $O(d^2)$.
- The injective flow approach appears to be both intriguing and novel, and the proof presented is sound.
- The paper outlines several potential applications, including the objective Bayesian approach and posterior inference in probabilistic mixing models.

### Weaknesses
 - Experiments are relatively limited, and no baselines are employed for comparison apart from the MCMC sampler in FIgure 9. I would suggest state-of-the-art normalizing flow methods and possibly other generative models for the baselines.
- The purported efficiency enhancement from $O(d^3)$ to $O(d^2)$ is not substantiated by experimental results. The authors could include runtime comparisons between their method and standard normalizing flows for increasing dimensionality $d$. This would provide empirical evidence for the claimed computational improvement.
- A minor issue: the caption of Figure 6 should include the correct probability distribution: $p(\boldsymbol\pi)|\mathcal{D}$.

### Questions
- In Theorem 1, it is stated that $\mathcal T_\theta$ can be an arbitrary diffeomorphism in $\mathbb{R}^{d-1}$. However, to the best of my understanding of normalizing flows, the evaluation of its Jacobian could be as computationally expensive as $O(d^2)$ if not specifically designed. Do you require any constraints on $\mathcal{T}_\theta$?
- How do the properties of the manifold influence the training process of the flow model?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an embedding of arbitrary d-1 dimensional star-like manifolds (i.e., deformations of the unit sphere) into the $\mathbb{R}^d$ which allows the computationally efficient evaluation of its determinant. They apply this embedding for constructing normalizing flows on such manifolds, by using an injective mapping from a d-1 dimensional latent space to the manifold. The proposed model is applied to several examples.

### Strengths
The paper is easily readable and written in a clear way. As far as I know the approach is new, implementable and computationally tractable. In contrast to prior papers it covers a whole class of manifolds.

### Weaknesses
My main critic on the paper is the missing comparison to existing injective flows. The authors emphasize at several points of the paper that it is important to have density evaluations of the model which are i) exact and ii) have improved complexity. As outlined in the literature part of the authors, there exist plenty of methods meeting one of the properties i) or ii). To validate the importance of meeting both at the same time, I would suggest two experiments:

i) Run an experiments to fit a not too simple distribution on a star-like manifold (maybe something like Fig 3b) and train an injective flow once with naive O(d^3) evaluation of the change-of-variables formula and once with the formula proposed in Thm 1. Then, create a plot of execution time vs dimension.

ii) Run an experiment in a similar setup for variational inference. Train an injective flow with exact determinant (as proposed) and some approximate determinant (e.g., one of the models which are cited in the related-work part) and compare the quality of generated samples (e.g. in Wasserstein/MMD or a similar two-sample comparison of distributions). Following the authors claims, the injective flow with exact determinant should lead to more accurate results than the approximate.

Even though the existing numerical experiments provide some proof-of-concept, I think that the paper could benefit a lot by evaluating more the proposed architecture itself in terms of speed and accuracy instead of using it for specific applications. The comparison with the completely different MCMC samplers looks a bit out of place since it is a completely different model which is known not to scale well along the dimensions (which is also observed in Fig 9).

Additionally, I would like to point the authors to the papers [1,2]. [1] considers a specific architectures which makes the evaluation of the necessary determinant cheap and easy, [2] which trains the normalizing flows with a VAE loss.

From a technical side, I am bit confused since the change from spherical to Cartesian coordinates is not a bijection and definitely not a diffeomorphism. The vectors $(0,\theta_2,...,\theta_{d-1},1)$ map all to the same point in the $\mathbb{R}^d$ regardless of the choice of $\theta_2,...,\theta_{d-1}$. Certainly, one can exclude sets of measure zero from domain and image of this transformation such that it becomes bijective, but then still the determinant of this transform becomes arbitrary close to zero when $\theta_1$ approaches zero such that the inverse is no longer a $C^1$-function (and hence the embedding not a $C^1$ diffeomorphism). I am not completely sure if this can cause limitations in actual applications. But the issue should be treated more thoroughly in the paper. In fact, it is easy to see that there exists no diffeomporphism from $\mathbb{R}^{d-1}$ to a sphere (or any other star-like manifold) since those have different topologies (e.g., $\mathbb{R}^{d-1}$ is contractible in contrast to star-like manifolds). A possible way to overcome such issue is the use of a mixture of several embeddings (for star-like manifolds two should be enough), see [3]. As the authors do not need too many geometrical properties of their embedding an "we exclude zero sets"-solution might be enough, but again, this issue should be discussed in the paper.

In summary, I think some numerical comparisons to existing works are necessary such that I think that the paper is below the acceptance threshhold, but I am willing to raise my score if the critics from above is addressed.

### Questions
I outlined my questions and suggestions in the "weaknesses" part.

### Soundness
2

### Presentation
3

### Contribution
3
