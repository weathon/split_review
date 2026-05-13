# A Differential Equation Approach for Wasserstein GANs and Beyond

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
We propose a new theoretical lens to view Wasserstein generative adversarial networks (WGANs). In our framework, we define a discretization inspired by a distribution-dependent ordinary differential equation (ODE). We show that such a discretization is convergent and propose a viable class of adversarial training methods to implement this discretization, which we call W1 Forward Euler (W1-FE). In particular, the ODE framework allows us to implement persistent training, a novel training technique that cannot be applied to typical WGAN algorithms without the ODE interpretation. Remarkably, when we do not implement persistent training, we prove that our algorithms simplify to existing WGAN algorithms; when we increase the level of persistent training appropriately, our algorithms outperform existing WGAN algorithms in both low- and high-dimensional examples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new variant of Wasserstein generative adversarial networks (WGANs) based on a distribution-dependent ordinary differential equation (ODE). It introduces a method called W1 Forward Euler (W1-FE), which includes persistent training to improve efficiency. When persistent training is not utilized, the approach reverts to standard WGAN algorithms. By appropriately increasing the level of persistent training, the model's performance is enhanced.

### Strengths
This paper presents a novel framework for Wasserstein generative adversarial networks (WGANs) based on distribution-dependent ordinary differential equations (ODEs). It utilizes persistent training to enhance the training process of WGANs and provides a solid mathematical foundation for this approach. Additionally, the paper includes numerical results that demonstrate the effectiveness of persistent training at various levels.

### Weaknesses
The experiments are insufficient; the paper should include additional datasets or real-world applications. It is better to present empirical results using well-known standard datasets.

The mathematical framework needs further clarification. For instance, the inequality at the top of page 4 should be explained more thoroughly. Specifically, the connection between the definition of J in (3.3), the duality formula of the W1 distance in (2.2), and the 1-Lipschitz property of the Kantorovich potential needs to be explicitly stated. The current explanation lacks sufficient detail to be easily followed.

The section on "MATHEMATICAL PRELIMINARIES" could benefit from more references. Please include citations for definitions and related concepts. The current presentation assumes a level of familiarity that may not be universal, and explicit citations would improve the accessibility and rigor of the work.

The contributions seem to lack originality, as mentioned in paragraph 2 of the Introduction. This section suggests that the differential equation approach outlined in the paper is already well-established in the existing GANs literature. Therefore, the question to the author is: Is the approach a variant of Generative Modeling using Wasserstein-1 loss, achieved by minimizing Wasserstein-2 loss (Huang and Malik, 2024)? If the novelty is something else, please clarify this in the Introduction. See references from the papers itself

Y.-J. Huang and Z. Malik. Generative modeling by minimizing the wasserstein-2 loss, 2024. URL
https://arxiv.org/abs/2406.13619.

Y.-J. Huang and Y. Zhang. GANs as gradient flows that converge. Journal of Machine Learning
Research, 24(217):1–40, 2023. URL http://jmlr.org/papers/v24/22-0583.html.

### Questions
I have a few questions and suggestions as follows.

1.	For completeness, please include a proof for the statement, “$\mu \rightarrow W_1(\mu,\mu_d)$ is strictly convex on $P_1(X)$.”

2.	In Proposition 3.1, it would be helpful to explain the first inequality (at the top of page 4).

3.	The manuscript mentions the use of persistent training, which is known to have certain limitations. Could you elaborate on how these limitations are addressed or mitigated in your training approach?

4.	The manuscript's writing could benefit from some improvements, particularly in conveying the contributions of the proposed work more clearly and concisely.

5.	Please consider including some recent, relevant citations to enhance the manuscript's context within the field.

6.	The numerical experiments are limited in scope; please include more real-world datasets (such as CIFAR-10 or CIFAR-100) in the empirical results.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work analyzes Wasserstein GAN training through the lens of gradient flow dynamics derived from the optimal transport map between initial and data distributions. Authors demonstrate in Theorem 4.1 that by applying a sequence of updates to the generator distribution according to the gradient of the W1 witness function (Kantorovich potential), the resulting distribution in the limit matches the optimal one. 
This framework motivates the use of *persistent training* of the generator, where at each substep of training the discriminator and generator noise $z$ is frozen while the generator $G_\theta$ is updated for K steps. Lastly, the authors use a few simplified experimental settings  (e.g. 2D mixture of Gaussians) to demonstrate how persistent training can improve the rate of training convergence.

### Strengths
* Utilizes tools from optimal transport for analyzing WGANs, providing a generalized WGAN training framework.
* Theory provides good insight into generator training hyperparameters, which is corroborated by experiments.

### Weaknesses
 * It seems to me that most of the uncertainty about how well WGAN training follows idealized gradient flow dynamics lies with the discriminator. Can you still arrive at a similar conclusion to thoerem 4.1 when the distance between approximated + true potential function is bounded?
* I'd like to see more discussion in the introduction about key differences between contributions of this work and the W2-FE paper.

Minor Notes:

* Eq 2.2 \mu_t, \mu^d not defined initially
* both \varphi and \phi used on line 087
* Eq. 2.3 variable i is not defined

### Questions
* What was the number of steps used when training the discriminator in figure 1? Does your theory suggest when it is more or less important to have accurate $\varphi$ approximations during training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a new perspective on WGAN from the view of ODE associated with the gradient of Wasserstein derivative, demonstrating that persistent training on a generator can improve WGAN training.

### Strengths
1. This paper provides a clear and novel explanation of WGAN's training from the perspective of the gradient flow of Wasserstein distance.

2. Both theoretical explanations and experiments on toy and MNIST datasets demonstrate the effectiveness of persistent training, a common trick for training WGAN.

### Weaknesses
1. The main contributions in this paper, i.e. discretization and persistent training, are common tricks for training WGANs[1,2], which are not novel enough in practical implementation. For example, as is shown in the proof of Proposition 4.1, persistent training seems equal to just increasing the generator's iterations in the original WGAN's training. Thus please clarify how discretization and persistent training differ from the above existing methods.

2. Obtaining Kantorovich potential is a challenging and important step in ODE-based WGAN's training, but in this paper, it's still the same as the original WGAN, leaving some problems for persistent training as discussed in Remark 4.2, harming the consistency between theory and practice.

3. Experimental validation is not comprehensive enough, the used datasets are too small scale, like in WGAN and WGAN-GP,  more common and large-scale baseline datasets should also be verified. For example, how does the proposed method perform on CIFAR-10 or CelebA compared to baseline WGAN methods in terms of FID, IS, and convergence speed?

4. Some mathematical explanations and notations should be modified. For example, there is no definition of $m$ in Eq.(2.4). Besides, more introduction of $\nabla \frac{\delta J}{\delta m}$ are suggested to be added, since $\nabla \frac{\delta J}{\delta m}$ is very important in the whole method, how to understand this gradient and how to get Eq(3.2) from Eq(3.1) should be added in the main paper.

### Questions
1. please clarify how persistent training differs from simply increasing generator iterations.

2. As discussed in the third point of the above weaknesses, more common large-scale datasets should also be verified.

### Soundness
2

### Presentation
3

### Contribution
2
