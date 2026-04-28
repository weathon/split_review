# Underdamped Diffusion Bridges with Applications to Sampling

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 8, 6, 8

## Abstract
We provide a general framework for learning diffusion bridges that transport prior to target distributions. It includes existing diffusion models for generative modeling, but also underdamped versions with degenerate diffusion matrices, where the noise only acts in certain dimensions. Extending previous findings, our framework allows to rigorously show that score-matching in the underdamped case is indeed equivalent to maximizing a lower bound on the likelihood. Motivated by superior convergence properties and compatibility with sophisticated numerical integration schemes of underdamped stochastic processes, we propose *underdamped diffusion bridges*, where a general density evolution is learned rather than prescribed by a fixed noising process. We apply our method to the challenging task of sampling from unnormalized densities without access to samples from the target distribution. Across a diverse range of sampling problems, our approach demonstrates state-of-the-art performance, notably outperforming alternative methods, while requiring significantly fewer discretization steps and almost no hyperparameter tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors explore training diffusion bridges with the following focus:
- investigating the case where the reference diffusion process has degenerate noise
- explores the under-damped Langevin case
- numerical experiments

### Strengths
The authors explore underdamped diffusions for sampling and appear to achieve record performance in Table 1, Figure 3 etc. compared to the baselines considered for the datasets considered, including some medium dimensional data d>1000.

The authors explore a variety of known splitting based sampling schemes to improve performance.  This appears under-explored in the literature of diffusion models.

The authors claim their method enables end-to-end hyper-parameter tuning. This appears to be a novel and valuable contribution though I do not understand how this works and it does not appear well explained in the paper (as detailed in weaknesses below).

### Weaknesses
It is not clear to me what the contributions are in this submission nor the significance.

It appears most of the propositions/ theorems are from other works. The authors claim that the novelty in this work is extending these to the degenerate noise case. It is not clear to me why the degenerate noise case is useful or important (bullet 1 of contributions).

>Even though for (underdamped) diffusion models with degenerate η, a corresponding (hybrid) score matching loss has been suggested by Dockhorn et al. (2021), it has so far been unclear whether it can also be connected to an ELBO, i.e., to likelihood optimization.

Likelihood based training for underdamped diffusion models has indeed been investigated in Dockhorn et al. (2021), see e.g. sections
"B.3 CLD OBJECTIVE"; "F.1.2 MAXIMUM LIKELIHOOD TRAINING".  (bullet 2 of contributions).

> Novel underdamped samplers:
Splitting based samplers  have been used before, as cited by the authors e.g. Monmarché · 2021. It is claimed by the authros (bullet 3 of contributions) that these samplers are novel. Is the novelty in using these for sampling with diffusions? I appreciate these splitting methods have been used before with damped diffusions and for diffusion models, but the full design space has not been explored.

The promise of end-to-end training is very attractive (bullet 4 of contributions). How is this achieved in practice? It appears this is only discussed in the numerical experiments yet is one of the main selling points of this work. Can the authors elaborate more on this? It appears from Figure 5 that learning hyper parameters is key to good performance.

The simulation based loss considered appears to be the same as that proposed in "Guided proposals for simulating
multi-dimensional diffusion bridges", [1] for forward KL eqn (9) and (11). If I understand correctly, this requires simulating the whole diffusion trajectory under some discretisation to learn the drift and has been considered by [1] for simple drift terms. The approach by [2] requires simulating in the nonlinear diffusion case up to time t and not the whole trajectory (simulation free for affine SDE); and uses a score matching loss (reverse KL) to train a neural diffusion bridge and then to sample diffusion bridges for a range of nonlinear reference diffusions.

The works [1,2] have not been discussed and appear quite relevant.



### Questions
See weaknesses

> learn the control functions u and v such that the two processes defined in (5) and (6) are time reversals with respect to each other.
Quotes from page 3.

If the marginals are fixed and preserved and the forward/ backware are time reversals of each other, then this would be the Schrodinger bridge?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper generalizes the framework for learning diffusion bridges that transport prior to target distributions, as well as proposing a new method called underdamped diffusion bridges.

### Strengths
1. The paper is well-organized. The explanation is clear and intuitive. Overall, it is easy to follow the logic and flow of the paper.
2. The detailed proofs, experiment details, as well as the code, are explicitly provided.

### Weaknesses
1. The notation is a little confusing. Maybe you should provide an explanation about the notation as it shows up in the main text firstly.
2. The theoretical benefits of underdamped diffusion bridges are lacked. Could you provide some explanations on its good performance on theory side?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work deals with the problem of sampling from a target distribution for which we can evaluate the unnormalized density, which is a common and general problem in statistics and machine learning.
The considered setting is a dynamic one, with the objective of learning a SDE which, over a finite time interval, produces terminal samples approximately distributed according to the target distribution.

The authors aim to advance the field by delivering the following contributions:
1. extending and unifying previous frameworks, including diffusion processes whose diffusion coefficient can be zero across some dimensions / times
2. propose the use of underdamped dynamics, on an extended space, for sampling
3. propose the use of numerical integrators appropriate for the setting of point 2
4. complement the theoretical developments with numerical experiments illustrating the practical relevance of 2. and 3.

### Strengths
Overall, with some limitations (see weakness section below), I found the reading enjoyable and the goal of providing an unified and clear framework is commendable.

This work covers considerable ground, briefly discussing the context where samples (instead of the density) are available for the target distribution, introducing numerical integrators appropriate for the considered setting, and carrying out numerical experiments to complement the theoretical framework.

The rating system do not allow me to be so granular, but I find this contribution to be closer to 7 than to 6.
I am open to revise my rating in view of the future developments during the rebuttal.

### Weaknesses
 > In this section, we lay the theoretical foundations for diffusion bridges with degenerate noise, extending the frameworks suggested in Richter & Berner (2024) and Vargas et al. (2024).

Part of the contributions of this work consists of extending previous results to the case where the diffusion coefficient can be zero for some dimensions. I have two remarks on this point.

Firstly, it is not completely clear what specific prior results actually require to be extended, in the sense that prior derivations leveraged results and / or proof techniques that would not hold in this newly considered setting. For example, it would be helpful to pinpoint specific theorems or lemmas in the cited works [1, 2] that rely on the non-degeneracy of the diffusion matrix and thus require a new approach in this work. Without this, the reader is left to guess which parts of the existing proofs are invalidated by the introduction of degenerate noise.

Secondly, it is a bit unclear to what level of rigorousness (specific points are raised in the following, see questions 3,4) are the results established.

In general, if I understood correctly, and with the exception of Proposition 2.5, the results are in line with the non-degenerate case (same form as prior results).
So a significant contribution would, on a solid theoretical level, establish the desired results in the more general setting here considered.

At this stage, it is unclear to this reviewer how significant the contribution 1. really is (in the sense: how non-trivial, and how rigorous).

> Our proposed framework encompasses all these works as special cases (Tab. 2).

On a side, I find this claim not completely accurate, in the sense that the mentioned works often contains additional considerations / objectives not present in this reviewed paper.

### Questions
1. Is it correct to say that without loss of generality f(x, t) could be absorbed into u(x, t), and thus v(x, t), in the sense that (5) and (6) are learnt so that (6) is the time-reversal of (5) (and viceversa)? I found unclear why f(x, t) is needed at all in the framework considered in this work, given also that it complicates some derivations. Is it there only to connect with prior works?

2. Does the divergence-based RN derivative formulation of Prop. A. 4. offer any advantage over the result of Proposition 2.3?

3. Equation (24) is not the linear growth-condition, but the globally Lipschitz condition (uniformly in time), that is used to establish uniqueness of the (strong) SDE solution. The growth-condition is missing, and also some condition is required on the diffusion coefficient even when state-independent as here.

4. A large number of conditions are reported at the beginning of pag 15., what condition implies what? Specifically, it is unclear to me how they suffices for:
- Girsanov: which requires some integrability condition
- Existance and uniqueness of solution to Fokker-Planck equation (PDE for marginal density evolution), which, from what I understand, is an assumption in [1], and justified later derivations of the same result not relying on that assumption, which at the time was very difficult to establish based on verifiable conditions (it is possible that more recent developments changed the situation, if so the authors can point this out)

5. I did not understand in the proof of Lemma A.3. what yields the equation following "First, we rewrite the problem by observing that", in particular the last two terms (the two stochastic integrals, in different time directions)

6. The authors could expand on Remark 3.3.: I quickly glanced at the references but did not spot the relevant parts.
Is it the case that the drift of the process matching a terminal distribution living on a manifold remains bounded as the process approaches terminal time?

7. What role do the distribution for the augmented space in (16) play? (On a side note: the construction on the enlarged space could be given more preeminence)

[1] Anderson - Reverse-time diffusion equation models

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
4

### Summary
The paper introduces underdamped controlled SDEs for sampling from an unnormalized target density. This approach can be seen as a generalization of earlier sampling algorithms that utilize over-damped dynamics or critically damped Langevin dynamics in diffusion generative modeling. The authors demonstrate that under-damped dynamics achieve superior performance in sampling tasks.

### Strengths
* The paper is well-motivated and clearly written, with the derivations appearing to be correct. 
* Extending previous diffusion-based sampling algorithms into under-damped dynamic is novel. 
* The proposed algorithm demonstrates superior performance in sampling tasks compared to recent methods.

### Weaknesses
 * I’m not an expert in Hamiltonian systems, but many of the paper’s derivations are heavily based on the theories developed by Vargas et al 2024 (https://arxiv.org/pdf/2307.01050). While the formulation of the sampling problem using under-damped dynamics demonstrates some performance improvement, I’m uncertain about the theoretical significance of this extension beyond its practical benefits. 
* Is there a substantial challenge in formulating the task with under-damped dynamics that has not been addressed in prior works? In my view, the primary difficulty lies in sampling from the underdamped dynamics; however, the approximation techniques have already been established in earlier research.

### Questions
To simulate Hamiltonian dynamics, the authors suggest approximation techniques such as OBAB, BAOAB, and OBABO. However, it seems that these approximations may introduce additional costs during training and inference. Could this potentially negate the advantages that the authors claim in formulating the task using underdamped dynamics, such as the capability to minimize the discretization step due to the presence of degenerate noise?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper successfully integrates the theories of diffusion-based models spanning several existing studies, providing greater flexibility in sampling computational methods. As an application, the authors propose a new sampling method using underdamped Langevin dynamics and validate its effectiveness through numerical experiments.

### Strengths
### Originality
The idea of considering underdamped Langevin dynamics as a diffusion bridge with degenerate noise allows many existing methods related to diffusion-based sampling to be handled in a unified manner. This demonstrates the originality of the authors' idea.
### Quality
The existing research is well-organized. Additionally, the effectiveness of the proposed method is robustly verified through ablation studies in the numerical experiments.
### Clarity
In Figure 5, the effective hyperparameters are clearly indicated.
### Significance
The finding that accelerated dynamics with efficient sampling can produce even better sampling methods when combined with score-matching techniques" is considered a significant and fundamental result.

### Weaknesses
### Theory Part
In Sections 2 and 3, the theory and algorithms of diffusion bridges are constructed under degenerate noise. However, I believe that the non-trivial impact of the degeneracy on the theory is minimal. In particular, the core theoretical results, such as the ELBO derivation and the Radon-Nikodym derivative, seem to follow directly from standard results by simply substituting the degenerate noise structure. The authors do not sufficiently highlight the specific challenges or novel insights that arise due to this degeneracy. In this sense, the novelty of this theory may be somewhat limited.

### Numerical Experiment
The effectiveness of the proposed method in sampling is well-validated. However, the algorithm for generative modeling mentioned in Subsection 2.1 lacks experimental validation, leaving the effectiveness of the proposed method in generative modeling unclear. Specifically, the paper does not demonstrate how the proposed underdamped Langevin dynamics performs in a generative setting where the target distribution is only accessible through samples, rather than its density. This is a critical aspect of many practical applications, and the absence of such experiments limits the practical impact of the work.

### Questions
1. Under Lemma 2.4, it is stated that "the ELBO in Lemma 2.4 does not depend on the target $\tau$". However, the current form of the ELBO is $\mathbb{E}\_{Z_0 \sim \tau}\left[\log \tau\left(Z_0\right)\right]-D_{\mathrm{KL}}\left(\overrightarrow{\mathbb{P}}^{v, \tau} \mid \overleftarrow{\mathbb{P}}^{u, \pi} \right)$, which depends on $\tau$. Could you clarify this point?

### Soundness
4

### Presentation
2

### Contribution
3
