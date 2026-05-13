# Adversarial Adaptive Sampling: Unify PINN and Optimal Transport for the Approximation of PDEs

- Decision: Accept
- Scores: 5, 6, 1, 8

## Abstract
Solving partial differential equations (PDEs) is a central task in scientific computing. Recently, neural network approximation of PDEs has received increasing attention due to its flexible meshless discretization and its potential for high-dimensional problems. One fundamental numerical difficulty is that random samples in the training set introduce statistical errors into the discretization of the loss functional which may become the dominant error in the final approximation, and therefore overshadow the modeling capability of the neural network. In this work, we propose a new minmax formulation to optimize simultaneously the approximate solution, given by a neural network model, and the random samples in the training set, provided by a deep generative model. The key idea is to use a deep generative model to adjust the random samples in the training set such that the residual induced by the neural network model can maintain a smooth profile in the training process. Such an idea is achieved by implicitly embedding the Wasserstein distance between the residual-induced distribution and the uniform distribution into the loss, which is then minimized together with the residual. A nearly uniform residual profile means that its variance is small for any normalized weight function such that the Monte Carlo approximation error of the loss functional is reduced significantly for a certain sample size. The adversarial adaptive sampling (AAS) approach proposed in this work is the first attempt to formulate two essential components, minimizing the residual and seeking the optimal training set, into one minmax objective functional for the neural network approximation of PDEs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new objective to sample collocation points for PINNs adaptively. Specifically, the collocation points for training the PINN are sampled from a normalizing flow with soft Lipschitz constraint, enforced by Sobolev regularization. The PINNs and normalizing flows are optimized in an alternating fashion, where the normalizing flow is trained to maximize the expected PINN residual (w.r.t. to the distribution given by the pushforward of the normalizing flow). This formulation is then connected to the dual form of an optimal transport problem. In this context, it is shown that there exists an optimal solution to the proposed min-max problem where the (normalized) squared residual converges to a uniform distribution in the Wasserstein distance. The approach's effectiveness is further demonstrated on two toy problems and one high-dimensional nonlinear PDE and compared to three related methods.

### Strengths
1) Tackling adaptive sampling for PINNs using optimal transport seems to be a promising direction.
2) The proposed objective seems to be novel and can bring numerical benefits on the considered examples.

### Weaknesses
The theoretical as well as numerical contributions need to be significantly improved:

1) Further challenging problems (as in Subsection 5.3), as well as baselines (as enumerated in the section on related works), are needed to judge the performance of the proposed algorithm. Specifically, the lack of comparison to more established adaptive sampling techniques, particularly for high-dimensional problems, makes it difficult to assess the true advantage of the proposed method. The current experiments do not sufficiently demonstrate the claimed benefits over existing methods, especially in higher dimensions where the authors argue their method excels.
2) "[...] which is the first time to minimize the residual and seek the optimal training set simultaneously for PINN.": Analogous to DAS-PINNs, it seems that the final algorithm is still alternating between optimizing the two networks, see also Question 2) below. In general, it should be made more explicit what the novelty of the present work is and how it theoretically compares to related work. The claim of simultaneous optimization needs to be more rigorously justified, given the iterative nature of the proposed algorithm.
3) For the numerical results, training times and standard deviations (w.r.t. different seeds) are missing. Especially given that the adversarial training slows down training. The absence of these metrics makes it difficult to assess the practical efficiency and robustness of the method. The computational cost and variability across different runs are crucial for evaluating the method's suitability for real-world applications.
4) The loss for learning the normalizing flow seems to use the REINFORCE trick, which, however, is known to suffer from high variance. The high variance associated with REINFORCE could lead to unstable training and hinder the convergence of the algorithm. This aspect needs further investigation and discussion.
5) Since the residual continuously changes over the course of optimization, it should be better motivated what the advantage of learning a generative modeling is (as compared to just using a method to sample, e.g., according to squared residual)? The rationale for using a generative model, especially given the computational overhead, needs to be more clearly articulated, particularly when simpler sampling strategies might suffice.
6) It seems that the precise connection to optimal transport remains a bit unclear:
	* "So the minimization step will reduce not only the residual but also the Wasserstein distance between $\mu_r$ and the uniform distribution". Since there is only an upper bound shown on page 6, it is unclear why the minimization step is guaranteed to decrease the Wasserstein distance. The theoretical link between the minimization step and the reduction in Wasserstein distance needs further clarification and justification.
	* "The evolution of the residual-induced distribution has a clear path": According to the theorem, there only *exists* such a path, and it is not clear whether this path is taken by GD. It would be good to have at least plots of the residual evolution for all experiments.

**Minor issues:** 
1) use `\citep`.
2) In Eq. (4), min-max should be written on both sides of the equation.
3) What is a 'proper' constraint?
4) The last paragraph in Section 3 seems a bit convoluted. The choice for minimal variance could just be motivated by the optimal choice for importance sampling. 
5) It is unclear why we would consider $I^D$ instead of $\Omega$ when the KRnet is first introduced.
6) The text for the figures of the training set is barely readable.
7) typo: resultd

### Questions
1) Why is RAR not tested for the PDEs in (12) and (13)?
2) Why can we not use a single backward pass on the loss in (11) and update both $\theta$ and $\alpha$ (using decent and ascent, respectively).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors introduce an adaptive sampling technique that for sampling the input points (also referred to as collocation points) for training a PINN architecture on a domain. The main motivation behind it is that for highly irregular PDEs, uniformly sampling collocation points will not work well and result in high residual error for PINNs. 

The idea is similar to the adaptive sampling techniques that have been introduced in previous work by Tang et al (2023) and Gao et al (2023), however instead of directly minimizing a pushforward or adaptive sampling, the authors in this paper enforce a wasserstein loss to ensure that the residual error is uniformly distributed across the grid. 

That is, the training is done such that the error induced by PINNs is uniformly distributed across the grid, and hence the points are sampled accordingly. The authors operationalize this using a WGAN setup, wherein they train a pushforward map to learn p(x), such the wasserstein-1 loss between the the density of the residual and uniform distribution. This is similar in vein of the adaptive sampling techniques introduced in Gao et al (2023) but the weights are instead learned using a GAN type architecture.

### Strengths
The idea to use a GAN type loss with to ensure that the density of the residual is uniform across the domain is very interesting. 

In their experiments, the authors are able to do well on very sparse data, i.e., PDEs that have two-peaks, something that PINNs sometimes don’t do well in, and are able to get better results than the previous baselines by Tang et al (2023), thus showing the benefits of using the wasserstein formulation for learning $p_\alpha$.

### Weaknesses
In general the work is very similar to that by Tang et al (2023), there the authors are using a network defined using a normalizing flows type of an architecture whereas here the authors are using a GAN instead.

The paper is very hard to read with sometimes the notation and the terms used by the authors for different quantities is not clear. For example

- The authors mention that this methodology achieves variance reduction, what is the proof for that? is it similar in flavor of Tang, et al (2023)
- In Assumption 1, the authors refer to $r$ as an operator. Is that an operator, or the residual between the loss. If the authors mean that $r$ is an operator, then from which function space to what other function space? (I presume it is U x F → U).
- In theorem 1, $\nu$ is used to define the density of the residuals, whereas in the derivation under equation 6, it is defined by $\mu_r$. I think that they are the same quantity, however if not, what is $\nu$ and what is $\mu_r$?
- It is unclear as to what is being approximated by a KRNet?, since the authors first use $p_\alpha$ to define the density that they are trying to train, however, there is no mention of it after section 3.2
- Also, KRNet is not cited in the last paragraph of page 3.
- In equation 9, what is p*?

Few other questions that I think would help with the understanding of the usability of the techniques are: 

- What are the implementation details (in terms of number of parameters) etc of the networks approximating the solution $u_\theta$ and approximating the density network, i.,e $p_\alpha$.
- Since the authors are doing a min-max optimization, that is usually hard to train and get right, esp for for PDEs that may have some advective terms.

While the methodology provided by the authors seems to do better than the baselines, given the presentation and the lack of clarity of the precise steps, I think the paper would benefit from a revision

### Questions
I have asked most of the questions in the previous sections.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
A uniform approximation error is crucial in representing functions in a given vector base.  The same applies to compound function representations like neural networks. It also crucial where the errors are measured. The Authors combine both aspects, a  Wasserstein distance between a uniform and error distributions,  and an adversarial adaptive sampling of points for the PINN collocation.

The loss is divided to an analytical part that reflects the difference of the neural network from the solution and a statistical part that comes from using a finite sample.  By tuning the residual to become uniform, the density of samples becomes optimally non-uniform.

The method is used for three different PDEs with encouraging results compared to other adaptive learning techniques.

### Strengths
An excellent way to bring confidence to the inference with good proofs of convergence for the adaptive learning distributions.

Presentation is clear and not hard to follow.

### Weaknesses
Looking at the point clouds one visually can guess that the Delaunay triangulation link length distribution of  the point cloud contains very short distances i.e the point cloud is not locally smooth. Usually building meshes for FEM one prefers same size of elements locally and smaller elements in those areas do not provide more accuracy. 

I suppose this is the same for collocation points in PINNs. Currently the point clouds do not look like node distributions for FEM calculus. This is increasingly so, when creating points in the higher dimensions. The amount of wasted calculations increases and may drive this to a curse of high dimensionality.

### Questions
Any methods to solve the above problem? A possible remedy could introduce quasi random point distributions where the points do follow the error distribution, but are smoothly enough distributed in oder to avoid computation of the the error on points that are close to each other already without an expectation of significant change in the error distribution.

Could the problem above be solved with couple of iteration steps of repulsive force in the point cloud?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this article, authors raise a significant problem that linked with numerical difficulty is that random samples in the training dataset introduce statistical errors into the functional loss which may become the dominant error in the approximation, and therefore overshadow the modeling capability of the neural network. A new approach was proposed to optimize both the approximate solution and random samples in the training set by using a min max formulation. This approach is called adversarial adaptive sampling (AAS). The main idea of AAS is minimizing the residuals and meanwhile push the residual-induced distribution to a uniform one.  AAS can be divided into two parts. In the maximization part, the deep generative model helps define the difference between the residual-induced distribution and a uniform one using Wasserstein distance. In the minimization one, this difference is minimized together with the residuals.   Also, they used some benchmark test problems of comparison AAS algorithm with another state-of-the-art algorithms as DAS and RAR.

### Strengths
The motivation is clear, and the method is novel and interesting. Authors clearly described the theory of proposed method and the algorithm.

### Weaknesses
A numerical result is given for only one type of PDEs. It would be interesting to see how the AAS algorithm performs for other types of PDEs, such as singularly perturbed equations or parametric equations. There is no discussion of further development or limitations of the proposed method, particularly regarding the challenges associated with controlling the constraint on the Lipschitz norm in the regularization term.

### Questions
What other types of PDEs can the proposed algorithm be applied to? 
What are restrictions of the proposed method?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
