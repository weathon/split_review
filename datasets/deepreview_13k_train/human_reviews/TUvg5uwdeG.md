# Neural Sampling from Boltzmann Densities: Fisher-Rao Curves in the Wasserstein Geometry

- Decision: Accept
- Scores: 8, 5, 8, 5, 6

## Abstract
We deal with the task of sampling from an unnormalized Boltzmann density $\rho_D$
by learning a Boltzmann curve given by energies $f_t$ starting in a simple density $\rho_Z$.
First, we examine conditions under which Fisher-Rao flows are absolutely continuous in the Wasserstein geometry.
Second, we address specific interpolations $f_t$ and  the learning of the related density/velocity pairs $(\rho_t,v_t)$.
It was numerically observed that the linear interpolation, 
which requires only a parametrization of the velocity field $v_t$,
suffers from  a "teleportation-of-mass" issue.
Using tools from the Wasserstein geometry,
we give an analytical example,
where we can precisely measure the explosion of the velocity field.
Inspired by Máté and Fleuret, who 
parametrize both $f_t$ and $v_t$, we propose an
interpolation which parametrizes only $f_t$ and fixes an appropriate $v_t$. 
This corresponds to
the Wasserstein gradient flow of the Kullback-Leibler divergence related to Langevin dynamics. 
We demonstrate by numerical examples that our model provides a well-behaved flow field which successfully solves the above sampling task.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work contributions are twofold:

1. First, the work provides conditions under  which a probability flow admits a velocity field satisfying the continuity equation
2. Following from the theory this work then proposes learning the vector field via a PINN loss on the log of the continuity equation (PDE arising from taking the log of the probability flow) and explore several different interpolation schemes.

The work then presents some empirical results motivating the success of their proposed method.

### Strengths
The paper is rigorous and very well written and proposes a very sound approach for sampling from unnormalised densities based on the continuity equation, with strongly backed theoretical results and some modest numerical results; the paper also proposes a novel interpolation scheme (gradient flow interpolation) in the context of learning the vector field with promising numerical results.

In general I find the connections to Wasserstein gradient flows and the general formal machinery in the W_2 metric space to be a rather strong selling point of this work in contrast to prior works which explore learning the same vector field, during the review period I look forward to discussing/exploring this further with the authors, in order to improve the manuscript and highlight their contributions.

### Weaknesses
Unfortunately, this work misses prior work, which already explores learning the exact same vector field / continuity equation in the exact same context/task.

1.  Prior work [1]  (ICLR 2024 , ArXived July  2023)  provides a family of objectives for learning the vector field of the continuity equation in the exact same continuity equation + vector field up to a divergence. Notice [1] also provides an existence result for the vector field in the context of sampling from boltzman distributions (See Proposition 3.2 Appendix D3), the authors should make it clear how their results are different (from what I can see this submission has stronger / more general results, however they should be more precise in comparing to prior work). Note that whilst [1] has formulated their work in the SDE setting it is easy to see that their SDE in Equation 21 satisfies the same continuity equation as your work (See Equation 50 in their appendix) when using the optimal drift / velocity field considered in both works. Finally note that concurrent work [3] (Appendix 5.6 ) provides an explicit connection between [1] and your PINN based objective 
2. Prior Work [2]  (workshop version [4] Published on March 2024 around 5 months before the ICLR deadline https://openreview.net/pdf?id=KwHPBIGkET) explores the exact same objective for learning (They call it ODE anneal, see [3] equation 26 for a more clear rewriting of the PINN objective in [2,4]). As you highlight [5] also explores this loss

So, unfortunately, I would say that works [1,2,4] cannot be deemed as concurrent and have already explored NN-based learning of the vector field in the continuity equation for sampling from Boltzmann densities.  Therefore, this work needs to both conceptually and empirically discuss/compare these prior / non-concurrent works as you have done with [5]. Finally, [2,4] have explored the **exact same PINN-based objective** for learning the vector field (and much more thoroughly so from an empirical standpoint), so I'm not sure from a methods standpoint what contribution on the methods side this work brings.

 It is a shame; the paper is very well written, and it is a good idea. However, it has indeed been already explored. I am happy to focus more on the theoretical contributions in the discussion period, and given a better understanding of their novelty I will be happy to increase my score; in particular, I suspect the assumptions in proposition 2 of [1] do seem (Assumption D1) like they might be more restrictive and their results seem to have a less broader scope than yours (i.e. you show the curves are a.c. in the Wasserstein 2 space, which feels like a stronger and more insightful result).

Another point that seems novel is the gradient flow interpolation from what I can see in works [1,2,4] they also explored learned interpolations too and in particular the $t(1-t) * \mathrm{NN}(x,t)$ parameterizations can be seen in [2,4,5], that said the gradient flow interpolation seems novel, If a more comprehensive comparison of this to prior works / motivation as to why this is an improvement over [1,2,4]  is provided I would also happily increase my score.

### Questions
Am I correct in understanding that the linear and learned methods in your experiments are no different to the approach proposed in [5] ? thus from a methods standpoint the gradient flow interpolation is the novel algorithmic contribution ?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper deals with the problem of sampling from unnormalized density (with known energy function). This is done by means of learning a specific Fisher-Rao curve in the probability measures space, which transforms the data distribution to some simple distribution (Gaussian one is considered). Since the vector field of this curve is learned, it could be inverted and simulated with ODE for sampling.

### Strengths
The paper has some interesting theoretical results about absolute continuity and optimality of Fisher-Rao flows. Also, the paper demonstrates the connection between Fisher-Rao flows and Wasserstein Gradient flows (w.r.t KL functional).

### Weaknesses
I think that the paper has rather limited methodological and practical contributions.
1. In fact, the authors take the method from [Mate&Fleuret] (in particular, eq. 15 is exactly eqs. 11 and 12 from [Mate&Fleuret]), but with specific parameterization of the vector field $v_t$. In turn, the chosen vector field parameterization exactly corresponds to Wasserstein gradient flows (WGF) with KL divergence. Therefore, the proposed method - modeling WGF with KL from data to Gaussian (with subsequent inversion) using  techniques from [Mate&Fleuret]. At this point I want to note that there are other papers which also solve something similar to WGF inversion task with different techniques (e.g., [Boffi], JKO: [Xu]). So, what is the advantage of your proposed method? In particular, [Xu] manages to work with image data, while I am not sure if the presented method scales to high dims.
2. The scalability of the method is under question. The experimental illustrations do not stress test high-dimensional applications.

### Questions
1. General background section. What do you denote by $C_{c}^{\infty}$? Is it the set of (infinitely-many) differentiable functions?
2. Lines 261 - 267. I missed whether you introduce your method in these lines, or just explain the method by [Mate&Fleuret]. But in the latter case, this loss is different from [Mate&Flauret], because instead of sampling $x \in U[a, b]^d$ uniformly, as in eq. (17), they propagate $x$ along the learned vector field (treated as continuous normalizing flow).
3. Lines 359-360. I do not understand, what you mean by “[...] it is not clear if Boltzmann densities stay Boltzmann densities”

**Misprints**

1. Line 187 - no comma in $\nabla \cdot (\rho_t, v_t)$ in eq. (11).
2. Line 037-038. Velocity field $v: [0, 1]\times \mathbb{R}^d \rightarrow \mathbb{R}$ maps to scalar? Misprint?

**Minor comments**

A bit difficult to read the text (Introduction section, Related works subsection). Line 118, eq. (2). What is $s_t$ in eq. (2), what is $\alpha_t$, $\overline{\alpha}_t$ in eq. (2)? All of these quantities are introduced later, in the main text, but I think it is strange to introduce a formula in the introduction which will be understandable only after reading the main text. Some references/brief explanations should be given.

**Related works**

[Mate&Fleuret] Mate et. al., Learning Interpolations between Boltzmann Densities, TMLR’2023

[Xu] Xu et. al., Normalizing flow neural networks by JKO scheme, NeurIPS’2023

[Boffi] Boffi et. al., Probability flow solution of the fokker--planck equation

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper considers the problem of sampling from probability densities. The key idea is to use a so-called Fisher-Rao flow, which is a general equation that transports a simple density to a more complex one, going through a sequence of interpolating densities that are only assumed to be known up to an unknown normalizing constant. The main theoretical results of this paper (Theorem 1 and 2) show under very general conditions the uniqueness of a weak solution of the Poisson equation of this flow for which the Fisher-Rao curve is Wasserstein absolute continuous. The solution of this Poisson equation is found by parametrizing it using neural networks, and minimizing a certain loss function (explained on pages 5 and 6). Given this solution, the ODE of equation (6) is solved backward to yield samples from the target distribution by transporting a simple initial distribution to the target. Multiple different paths (interpolating densities) are considered, namely linear interpolation, and learned interpolation, where the interpolation curve itself is also parameterized by a neural network, and certain loss function enforcing more smooth transitions along the Fisher-Rao curve is optimized.

### Strengths
The theoretical results are quite fundamental, and show existence of unique solution to the Poisson equation that ensures Wasserstein absolute continuity. The idea of using a neural network to parameterize the interpolating distributions is also novel for Fisher-Rao flow, as far as I know. The numerical results sufficiently illustrate the methodology, and the choice of metrics makes sense.

### Weaknesses
There could be a more precise description of the ODE solver used to solve equation (6) backward, since this is the essence of the method for sampling from targets. It is not clear what specific numerical method is used, what is the step size, and how the error is controlled. The lack of detail makes it difficult to assess the practical performance and reliability of the sampling procedure. 
There is no theoretical guarantees for the neural network approximation that is used to solve (17) actually is able to solve it. While the authors propose to use a neural network to approximate the solution of the Poisson equation, there is no discussion of the approximation error, nor any theoretical justification for the convergence of the neural network training process to the true solution. This is a critical point, since the quality of the samples depends directly on the accuracy of this approximation. 
The scalability of this approach to high dimensional problems has not been demonstrated. The numerical experiments are limited to 2 dimensions, and it is unclear how the computational cost and the approximation error of the neural network would scale with the dimensionality of the problem. This is a major limitation, since many real-world applications involve high-dimensional probability distributions.

### Questions
Could you please explain in more detail the precise methodology used for solving the ODE (6)? Do you need a stiff ODE solver?

Both examples you've considered are 2 dimensional. Could you discuss the scalability of this methodology to higher dimensional problems?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The present paper considers the problem of sampling from a Boltzmann distribution known up to a normalization constant.

The author investigate theoretically the connection between the evolution of Boltzmann distributions with energy indexed by time, which give rise to Fisher Rao flow, and absolutely continuous curve in the Wasserstein space that obey a continuity equation. In particular, the author set the conditions under which a regular velocity field expressed as a gradient is solution to continuity equation associated with a the Boltzmann distribution curve.

Using this connection, the authors propose to learn a curve of Boltzmann densities bridging a base distribution to the target: assuming it follows a continuity equation for a velocity field expressed as a gradient a training objective is derived as in Mate & Fleuret (2023).  Going further, the authors take inspiration from the Fokker Plank equation of the Ornstein-Uhlenbeck process, recalling it’s interpretation as a Wassertein gradient flow on the reverse KL, to propose corresponding forms for the velocity field and learned energy. As such the learned curve is related to a variance preserving noising scheme of the target distribution.

Ultimately, the ODE associated with the velocity field can be integrated backward for sampling. The proposed method is compared against closely related methods that learn different interpolation schemes between a simple Gaussian base distribution and the target. The simple experiments in 2 and 8 dimensions suggest that the present method is less sensitive to the choice of the base distribution.

### Strengths
- The paper introduces well the concepts and challenges it aims to address, for example using the analytical example of Figure 1 and 2.
- The paper highlights and fruitfully exploits connections between SDE/ODE sampling and gradient flows on probability spaces. 
- The paper draws its inspiration from prior literature, but draws new connections to propose amendments to the approach.
- The proposed sampling method appears to be superior to related ones as its initial distribution can be chosen as a standard Gaussian regardless of the variance/mode location in the target. 

I am not familiar enough with the formal literature on Wasserstein curves to judge the novelty of the theoretical results of the paper.

### Weaknesses
 - The writing of the paper could be improved, in particular, some notations are regularly used before being introduced. 
- The discussion of related works should be extended to include:
	- Stochastic interpolants: https://arxiv.org/abs/2303.08797 
	- Non-parametric denoising based samplers: RDMC https://openreview.net/forum?id=kIPEyMSdFV & SLIPS https://proceedings.mlr.press/v235/grenioux24a.html
- The experimental validation is currently very limited, notably in terms of how the method scales with increasing dimension. The experiments do not sufficiently explore the sensitivity of the method to the complexity of the target distribution, such as multi-modal distributions with varying degrees of separation between modes. Furthermore, the comparison against other methods should include a more detailed analysis of computational cost, such as training time and sampling time.

Minor:
- maybe misses the assumption that $\rho_1 = \rho_D$?
- Notations in Equation (2) are not defined, also lacking Equation (5)
- In (17), the space variable is sampled uniformly on an hypercube? How are the boundaries chosen?


- typos:
	- line 96: Kullback Leibner
	- extra comma between $\rho_t$ and $v_t$ in the divergence (11)

### Questions
-

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper deals with the problem of sampling configuration from an un-normalized Boltzmann density. The author consider an approach where the energy function is interpolated by a function $f_t$ that is learned, following an approach developed by Máté and Fleuret. The main scope of the paper is to prove that the curve of the Boltzmann densities are absolutely continuous Wasserstein curve. They also demonstrate on an analytical example that the approach of Máté and Fleuret lead to a discontinuity in the particle transport due to the explosion of the velocity field. They propose a new reparametrization for the interpolant where a single function has to be learned while the velocity field is fixed.

### Strengths
The paper make very interesting connections between Wasserstein Flows and the developed method. 
It also underlines its relation with Diffusion models.

### Weaknesses
The article is particularly technical for those not-familiar with Wasserstein flows etc. While I find the results very interesting, I'm confused about the overuse of mathematical technicality, which tends to make the paper hard to grasp for a non-specialist. I'm wondering if the authors could ease part of it (eventually keeping a lot of details in the appendix) but putting an emphasis on the general direction and method. 

Among all these technicalities, I end up not understanding the details on how the function $\psi_t$ is learned, or the velocity in the "learned interpolation" case.

The results on the experiments are ok, but not super-convincing either.

### Questions
- The experiments that are done in Máte-Fleuret, show that problems of mode-collapse occur more severely when the Gaussian distributions are unevenly distributed. While the dataset proposed by the authors is not homogeneous since the mean of the Gaussians are random, it might be better to include a test on a mixture with unequal weights and variances.
- Does there exist a case where the gradient flow method is clearly better than the learned one ?
- There very few experimental validations, I would like to see another dataset, maybe inspired from the one investigated in Máté and Fleuret.

It seems to me that the phenomena described by the use of the linear interpolation, as in fig 1, is very similar to what is called "first order transition" in physics. As a parameter is slightly change, the overlap between the distribution $\rho_t$ and $\rho_{t+\delta t}$ is very small. That being said, the condition for annealed importance sampling to work is that the overlap between two nearest neighbors of the interpolation remain high enough. Is there a way to interpret the diverging of the velocity as characterize by the authors with such a phenomenon ?

Minor remark:
- there is a tipo at "Leibner" line 96

### Soundness
3

### Presentation
2

### Contribution
3
