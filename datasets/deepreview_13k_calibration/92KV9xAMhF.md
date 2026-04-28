# On gauge freedom, conservativity and intrinsic dimensionality estimation in diffusion models

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
<- trailing '%' for backward compatibility of .sty file
	Diffusion models are generative models that have recently demonstrated impressive performances in terms of sampling quality and density estimation in high dimensions. They rely on a forward continuous diffusion process and a backward continuous denoising process, which can be described by a time-dependent vector field and is used as a generative model. In the original formulation of the diffusion model, this vector field is assumed to be the score function (i.e. it is the gradient of the log-probability at a given time in the diffusion process). Curiously, on the practical side, most studies on diffusion models implement this vector field as a neural network function and do not constrain it be the gradient of some energy function (that is, most studies do not constrain the vector field to be conservative). Even though some studies investigated empirically whether such a constraint will lead to a performance gain, they lead to  contradicting results and failed to provide analytical results. Here, we provide three analytical results regarding the extent of the modeling freedom of this vector field. {Firstly, we propose a novel decomposition of vector fields into a conservative component and an orthogonal component which satisfies a given (gauge) freedom. Secondly, from this orthogonal decomposition, we show that exact density estimation and exact sampling is achieved when the conservative component is exactly equals to the true score and therefore conservativity is neither necessary nor sufficient to obtain exact density estimation and exact sampling. Finally, we show that when it comes to inferring local information of the data manifold, constraining the vector field to be conservative is desirable.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the conservativeness of the score vector field in the context of diffusion models. The author show that density estimation and sampling can be exact even if the learned score vector field is non-conservative, as long as the gauge freedom condition holds. This condition enforces that the remainder vector field (i.e. the gap between the true and learned vector fields) must be both divergence-free and orthogonal to the true score everywhere. Two dimensional empirical examples are presented to support the derivations. Moreover, the authors show that for exact estimation of of intrinsic dimensionality of the underlying manifold, a conservative vector field is sufficient.

### Strengths
The paper is written fairly clearly with a nice flow. The topic of conservativeness of the learned vector field in the context of diffusion models or denoising is still an open-ended question, with important empirical and theoretical implications. Proposing the gauge freedom condition as a valid relaxation of conservativeness requirement is an interesting and fairly significant theoretical contribution.

### Weaknesses
In my opinion, the main weakness of the paper is that it cannot yield to real world practical results. More specifically, in order to test or enforce the gauge freedom condition (eq 11 or conditions 12a and 12b), one needs to have access to the true score, which is not generally possible. In fact, diffusion models are mostly used for cases where the true score is not known. So it is not clear how knowing this condition would solve the question of conservativeness. The empirical results given in the paper are all toy examples for this very reason.

The result of section 4 states that for exact density estimation only condition 12a needs to be satisfied. In other words, if the discrepancy between the true score and the learned score can be written as a rotation then the density can be estimated precisely from eq 3. However, this result also assume that the model generates exact samples, which is not clear how can be tested in real cases such as image densities.

In section 4.1 a two dimensional example is discussed to show that conservativeness of score is neither necessary nor sufficient. The true score in this example has a divergence of zero which make it quite trivial. Is this an inevitable consequence of conditions 12a and 12b in 2 dimensions? In other words, doesn't satisfaction of gauge freedom conditions imply that the true score must have zero divergence in 2D? Since the authors use this example to make a more general conclusion in higher dimensions, it might be more convincing if 1) it is shown whether an example exists where the true score divergence is not zero yet the conditions are satisfied 2) if such example exists, that could replace the current example so that the generalization to higher dimensions would be more realistic.

### Questions
In section 4.1 a two dimensional example is discussed to show that conservativeness of score is neither necessary nor sufficient. The true score in this example has a divergence of zero which make it quite trivial. Is this an inevitable consequence of conditions 12a and 12b in 2 dimensions? In other words, doesn't satisfaction of gauge freedom conditions imply that the true score must have zero divergence in 2D? Since the authors use this example to make a more general conclusion in higher dimensions, it might be more convincing if 1) it is shown whether an example exists where the true score divergence is not zero yet the conditions are satisfied 2) if such example exists, that could replace the current example so that the generalization to higher dimensions would be more realistic.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates whether learning a conservative vector field is a necessary and/or sufficient condition to perform various generative modeling tasks, namely, sampling, density estimation, and dimensionality estimation. For the first task (and maybe the second one, see below), the authors show that it is slightly different condition which is necessary and sufficient. For the third task, the authors show that being conservative is sufficient.

### Strengths
The paper tackles an important issue on which there is both interest and confusion in the community, as there have been several conflicting studies on the topic of conservativeness of learned score vector fields. Section 3 is particularly well-written and makes an important point that had been overlooked in the literature. The numerical experiments in Section 5 are also very convincing.

### Weaknesses
I have several comments:

- Though the $r$ part of the learned score does not influence the marginals along the ODE trajectory in _continuous time_, it might do so when the ODE is _discretized_. In that case, it seems reasonable that "straighter" trajectories would be easier to discretize, and that these would correspond to $r = 0$, thus giving another practical motivation for regularizing the network to be conservative. This point could be strengthened by discussing specific discretization schemes (e.g., Euler, Runge-Kutta) and how the error introduced by a non-zero $r$ component might vary with the choice of scheme and step size. Furthermore, the argument that straighter trajectories are easier to discretize needs more justification. While intuitively plausible, it would be beneficial to provide a more rigorous argument or cite existing work that supports this claim.

- I am slightly confused by section 4. It seems to me that a subtle point when evaluating densities is that the score $s$ appears both explicitly in the integral in (3), but also implicitly through the trajectory (3). Therefore, it seems hard to evaluate exactly the effects on the modeled density. Besides, it seems that the paper make conflicting statements about the result: is the condition that $r$ satisfies (10), or that it satisfies both (12a) and (12b) (which are stronger than (10))? Different parts of the paper state different results (e.g., abstract and Figure 1 vs section 4). It seems to me that $r$ satisfying (10) is sufficient, since the samples have the correct distribution, and the change of variable formula still holds for $s$, so (3) must compute the correct density. The confusion arises from the fact that the change of variable formula is applied to the flow of the ODE, and the score appears both in the flow and the integral. A more careful analysis of how the $r$ component affects the change of variable formula and the density calculation is needed. The paper should clearly state whether (10) is sufficient or if (12a) and (12b) are necessary, and provide a rigorous justification.

- Theorem 1 should state that the assumptions imply that $r$ vanishes when $t \to 0$ (as shown in the proof), which makes it easier to understand the theorem. Also, the assumption that the divergence is finite may be questionable (why would $r$ remain stable when $t \to 0$ when the score explodes?), and should be discussed. In the proof, I don't see why the finite divergence of $r$ should imply that $r_\theta^T\nabla \log p_t \to 0$. Fortunately, these problems can be solved, the assumption removed, and the proof simplified. In fact, as it stands, the theorem is misleading, as assuming that $s_\theta$ is conservative implies that $s_\theta = s$ and $r =0$, and it is thus a statement about the true score rather than an approximation of it. The theorem's statement should be made more precise, explicitly stating the implications of the conservativeness assumption on the relationship between the learned score and the true score. The assumption of finite divergence of $r$ needs to be justified or removed, and the proof should be revised to clarify why $r_\theta^T\nabla \log p_t \to 0$ under the given assumptions.

- Let me suggest two additional references. [1] studies the approximation power of unconstrained conservative neural networks (not parameterized as the gradient of a scalar function). Essentially, exact conservativeness implies that the network only depends on a one-dimensional projection its input [1, Theorem 6]. It explains why $r$ will never be exactly zero in practice, unless one explicitly parameterizes the score as the gradient of a scalar function. This should be mentioned in the introduction together with the literature review on the topic. [2] studies the intrinsic dimensionality of image manifolds using the singular values of the network Jacobian and is thus very much related to Section 5. An observation that might be of interest to the authors is that for natural images the dimensionality _increases_ when the noise level vanishes, as opposed to what one expects for a low-dimensional manifold.

### Questions
I also have been thinking about score conservativeness for a while. I thus make several suggestions which I hope can help the authors improve the paper (which is already interesting and quite clear!).

### On Helmholtz decompositions

I did not find equations (12a) and (12b) to be helpful, but rather confusing. Rather than the Helmholtz decomposition, the right decomposition is that any vector field $s \in L^2(p_t)$ can be decomposed uniquely as $s = \nabla \phi + r$ where $\phi$ is a scalar field and $r$ satisfies the gauge freedom equation (10) (this decomposition then depends on $p_t$). Furthermore, this decomposition is orthogonal, in the sense that $\mathbb E[||s(x_t)||^2] = \mathbb E[||\nabla \phi(x_t)||^2 + ||r(x_t)||^2]$. This is readily checked with the integration by parts identity $\mathbb E[\nabla \phi(x_t) \cdot r(x_t)] = -\mathbb E[\phi(x_t) \left( \nabla \cdot r(x_t) + \nabla \log p_t(x_t) \cdot r(x_t) \right)]$ for any vector field $r$ and scalar field $\phi$, which shows that conservative fields $\nabla\phi$ are orthogonal in $L^2(p_t)$ to vector fields $r$ which satisfy (10). More abstractly, the adjoint of the gradient operator $\nabla$ is the "gauge freedom" operator $-(\nabla + \nabla \log p_t) \cdot$, showing that the image of the former is the orthogonal complement of the kernel of the latter.

I believe that stating this decomposition helps making the paper clearer. In particular, it has several direct implications for the paper:
- Because of the orthogonality property, the score-matching loss can be decomposed $\mathbb E[|| \nabla \log p_t(x_t) - s_\theta(x_t) ||^2] = \mathbb E[|| \nabla \log p_t(x_t) - \nabla \phi(x_t) ||^2 + ||r(x_t)||^2]$. This shows that (denoising) score matching training naturally regularizes the $r$ part of the score to have a small norm (but it cannot be zero, see above). We also see that $s_\theta$ is conservative if and only if $r=0$.
- It simplifies the proof of Theorem 1 and removes an unnecessary assumption. Indeed, the assumption that $s_\theta$ is conservative is equivalent to $r = 0$ (at all times!). There is thus no need to assume that the divergence of $r$ is finite.

### Typos

- "scaler" bottom of page 2
- "satisfie" middle of page 6
- "boundery", top of page 8
- "symmyrizing", bottom of page 8
- "conservity", middle of page 9
- "freemdom", bottom of page 9

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper investigates an additional degree of freedom that appears in the approximate learnt score function in a diffusion model when one relaxes the constraint that the score function must be a conservative vector field.

They do this by analysing the modified score function $s(x, t) = \nabla \log p_t(x) + r(x, t)$.

They show that under the constraints of 1) $\nabla \cdot r(t, \cdot) = 0$, $r$, is conservative and 2) $\nabla \log p_t(x) \cdot r(x, t)=0$, $r$, is orthogonal spatially to the score, that when initialised with the same initial distribution, the evolution of the distribution of the SDE evolved through time with and without the additional $r$ term remains the same.

They then apply reasoning from this conclusion ideas around density estimation, data generation, and local information estimation.

### Strengths
The topic discussed is an interesting one, and would have impact on how people train score based models in practise for the specific task of dimension estimation.

The presentation of diffusion models in section 2 is clean.

The main result of section 3 is interesting.

### Weaknesses
 - While the analysis in section 3 is interesting, there is no sense of how one could exploit these conditions in practise.
- The first half of section 4 to me does not make sense from a practical perspective (see questions)
- The experimentation to back up section 5 is limited.

- The conditions in equation 12, specifically the orthogonality constraint, seem extremely difficult to enforce in practice. It's not clear how one would go about constructing a vector field that is simultaneously divergence-free and orthogonal to the score, without already knowing the score itself. This severely limits the practical applicability of the theoretical results.
- The motivation for the first part of section 4 is unclear. The argument that adding a divergence-free term to the score preserves density estimation along a given path is not particularly useful if one does not have access to such a path. The paper does not explain how one would obtain this path without knowing the exact score or a score that satisfies the orthogonality constraint. This makes the entire section seem disconnected from practical concerns.
- The experiments in section 5 do not directly validate the core theoretical result of the paper. Theorem 1 states that intrinsic dimensionality can be estimated if the score is conservative and the additional vector field satisfies the gauge freedom constraints. However, the experiments only compare a fully unconstrained score with a conservative score. There is no experiment showing that one can estimate the dimension correctly when the vector field is non-conservative but satisfies the gauge constraints. This is a significant gap in the experimental validation.

### Questions
- Do the authors have an intuitive interpretation of the conditions in 12? 
- How can one practically realise the constraints of equation 12? Imposing the orthogonality constraint in combination with the divergence free part seems as difficult as just estimating the exact score.
- If one takes no drift (i.e. the ode does not move the distribution), then it becomes clear that the constraints force the dynamics to be such that 1) particles are constrained move along the same level-set of the distribution (i.e. through time a particle remains at $p_t(x)=c$ for all $t$), the orthogonal constraint, as long as 2) the dynamics do not alter the density of those level sets, the divergence free constraint. Is this perspective interesting when combined with a non-zero drift?
- I do not understand the point of the first part of section 4. I understand the argument that given a path $x_t$, if one adds a divergence free term to the score preserved density estimation. However, why would one assume they have a path? Without the exact score, or one satisfying the additional orthogonality constraint, how would one be able to generate a correct path from the model?
- Section 4.1, it would be highly instructive of the authors to plot examples of the trajectories with and without the additional $r$ term I think. From my own plots, one ends up with a series of trajectories that at each instance are "spinning" around the mean, following the shape of the covariance ellipses. One can multiply the $r$ term by a constant to speed up said spin. This related to my previous point also. Even if one initialises the ODE with the reference measure, the particles can still move as they can follow the covariance ellipses at constant speed on each ellipse.
- The experiments of section 5 do not seem to be related to theorem 1. Theorem 1 says that you can correctly estimate the data dimensionality if the extra $r$ field satisfies the gauge freedom constraints. However the experiments only use a fully unconstrained score, and a score constrained to be conservative. There is not experiment showing that one can estimate the dimension correctly if the vector field is non-conservative, but does satisfy the gauge constraints.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Score-based generative models achieve state-of-the-art performance in image generation tasks, and are based on fitting a model to the gradient of the log likelihood of blurred data. As such, it would be natural to fit models which are themselves conservative (the gradient of a function), but in practice this constraint is not enforced at all, and instead general vector fields, parametrized by a deep model, are used. This discrepancy leads to a natural question that is addressed in this work - how does learning a possibly non-conservative vector field affect the performance of score-based generative models? The authors derive an equation that precisely addresses this question (they refer to this as a gauge invariance), and show that it can be obeyed by both conservative and non-conservative vector fields. They then consider the problem of intrinsic dimension estimation and show that a conservative vector field -- under some technical assumptions -- is sufficient to estimate the intrinsic dimension of the data. Finally, they provide some empirical results on synthetic data demonstrating their ability to recover the intrinsic dimension with a conservative vector field, and an inability to recover intrinsic dimension with a non-conservative vector field.

### Strengths
This paper studies an important and relevant problem and derives a simple, clear, condition to precisely characterize when a vector field leads to the same marginal distributions as the true score. Using this equation, they cleanly show that conservativity is neither sufficient nor necessary, theoretically answering a question which has been studied empirically in the literature.

### Weaknesses
The derivation that leads to their main finding, the gauge invariance in equation (11), is not especially novel, since it follows immediately from the definition of the reverse time process. Also, their main finding - if I understand correctly, that gauge invariance as in (11) is necessary and sufficient for the time marginals of the learned process to be identical to those of the true process - is not formally stated as a mathematical result. I think the paper would be helped by a clear and precise mathematical statement of this main finding. 

Also, Theorem 1 on the intrinsic dimension estimation problem states that conservativity implies their intrinsic dimension estimation procedure is consistent (under their assumptions). But their gauge invariance finding (equation (11)) states the law of the reverse time process is unaffected under this gauge invariance, so it would be more natural to expect that the intrinsic dimension estimation procedure is consistent under the gauge invariance (so that conservativity is not necessary). And then in the discussion about Figure 3, the authors claim that their empirics demonstrate that conservativity leads to accuracy of the intrinsic dimension estimation procedure, while models which aren't constrained to be conservative have inaccurate intrinsic dimension estimation. But this is an odd finding give that their main observation is this gauge invariance, so that in particular, we would expect that enforcing conservativity is not important. There is no formal contradiction here, since the trained models which aren't enforced to be conservative may not satisfy the gauge invariance, but it does seems to somewhat contradict the essence of the paper. Finally, the empirics in Figure 3 (they are difficult to read so it's possible I am mis-interpreting them) seem to be inconsistent with their discussion of them and their Theorem 1 (see below).



### Questions
- I suggest you formalize the gauge invariance principle
- As mentioned above, the relationship of the empirics, Theorem 1, and the gauge invariance principle are confusing. It would be good to study and discuss more how these results complement (or don't) one another.
- For Figure 3: I don't see why the true singular values must be 1. They should depend on the local geometric properties of the manifold, the true data density, and the map.
- For Figure 3: the colors are very difficult to make out. Please use fewer lines (e.g. throw out 2 of the 3 non-material singular values) and more visual differentiation (e.g. different line types).
- For Figure 3: as it is constructed (and from what I can tell due to the difficult of making out the details, see above), it seems there are more than 2 singular values (green, black, yellow) converging to 1, which seems to contradict Theorem 1 and the discussion in the first paragraph after "Intrinsic dimensionality estimation using diffusion models" where it is said "2 of them converge to 1, whereas the remaining 3 diverge"
- There are many typos.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
