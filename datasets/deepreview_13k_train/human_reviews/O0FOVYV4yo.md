# A LOCAL POLYAK-ŁOJASIEWICZ AND DESCENT LEMMA OF GRADIENT DESCENT FOR OVERPARAMETERIZED LINEAR MODELS

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Most prior work on the convergence of gradient descent (GD) for overparameterized neural networks relies on strong assumptions on the step size (infinitesimal), the hidden-layer width (infinite), or the initialization (large, spectral, balanced). Recent work relaxes these assumptions for two-layer linear networks trained with the squared loss. In this work, we derive a linear convergence rate for training two-layer linear neural networks with GD for general losses and under relaxed assumptions on the step size, width, and initialization. A key challenge in deriving this result is that classical ingredients for deriving convergence rates for nonconvex problems, such as the Polyak-Łojasiewicz (PL) condition and Descent Lemma, do not hold globally for overparameterized neural networks. Here, we prove that these two conditions hold locally with constants that depend on the weights. Then, we provide bounds on these local constants, which depend on the initialization of the weights, the current loss, and the PL and smoothness constants of the non-overparameterized model. Based on these bounds, we derive a linear convergence rate for GD. Our convergence analysis not only improves upon prior results, but also suggests a better choice for the step size, as verified through our numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies convergence of gradient descent for matrix factorization (also called over-parametrized linear models). Prior work[1] established linear convergence for the quadratic loss by introducing two constants ($c_1, c_2$) to bound changes in singular values along trajectory of GD. This work writes their result for stronlgy convex and smooth losses and tracks those changes better which allows for an easier computation of adaptive stepsizes.

---
[1]Xu, Ziqing, et al. "Linear Convergence of Gradient Descent for Finite Width Over-parametrized Linear Networks with General Initialization." International Conference on Artificial Intelligence and Statistics. PMLR, 2023.

### Strengths
- This work cleans up and offers an improved analysis of a prior result.
- It is clearly written.

### Weaknesses
- The prior work this works improves on already has entire sections on adaptive step sizes: It is in a small sentence on page 8 we discover that [1] already proposes adaptive stepsizes when throughout it is presented as only having fixed stepsize schemes. The presentation of the prior work needs to include this fact. Specifically, the authors should clarify how their adaptive stepsize scheme differs from that proposed in [1]. While the current work emphasizes a novel approach to computing adaptive stepsizes, a more thorough comparison to the existing adaptive scheme in [1] is needed to fully appreciate the advancements presented in this paper. The authors should elaborate on the limitations of the adaptive stepsize scheme in [1] and how their method overcomes these limitations, particularly regarding the reliance on auxiliary constants c1 and c2.

- Significance: This result is carefully analyzes matrix factorization, after papers before have proved linear convergence of GD. Once the linear convergence question has been answered, can the authors justify why it is still significant to study matrix factorization ? The original reason for studying this simplified setting was to prove that non-convexity can be benign. This question was already answered. So the authors should provide more arguments as to why it would still be interesting to derive adaptive stepsizes to improve an already linear rate. A more compelling argument for the continued significance of studying matrix factorization in the context of linear convergence is needed. While the authors mention that prior work established linear convergence, they do not adequately address why further refinements, such as adaptive stepsizes, are crucial in this setting. The authors should discuss potential practical implications or theoretical insights gained from their improved analysis, beyond simply achieving a faster linear rate.

- Would the authors agree to say that the central contribution of this work that differentiates it from [1] is lemma 3.1 ? The paper would benefit from a clearer articulation of its core contributions. While Lemma 3.1 appears significant, the authors should explicitly state whether this lemma, potentially in conjunction with other results like Theorem 3.1 and 3.2, represents the primary advancement over prior work. A more precise definition of the novel aspects of Lemma 3.1, particularly how it enables a wider choice of step sizes compared to [1], would strengthen the paper's impact.

### Questions
- Would the authors agree to say that the central contribution of this work that differentiates it from [1] is lemma 3.1 ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors tackle the challenge of analyzing the convergence of gradient descent (GD) for two-layer linear neural networks with general loss functions, relaxing previous assumptions about step size, width, and initialization. They introduce a new approach based on the Polyak-Łojasiewicz (PL) condition and Descent Lemma, demonstrating that these conditions hold locally with constants depending on the network's weights. By bounding these local constants related to initialization, current loss, and non-overparameterized model properties, the paper establishes a linear convergence rate for GD. Importantly, the study not only enhances previous results but also suggests an optimized step size choice, validated through numerical experiments. The authors further prove that local PL and smoothness constants can be uniformly bounded by specific properties of the non-overparameterized models. The paper concludes by proposing an adaptive step size scheme, accelerating convergence compared to a constant step size, and empirically validating the derived convergence rate's accuracy.

### Strengths
$\textbf{(1) Rigorous analysis of convergence conditions}$: A key strength of this paper is its rigorous analysis of convergence conditions for two-layer linear neural networks. The authors thoroughly explore the convergence behavior of gradient descent under various circumstances, relaxing previous assumptions and providing a detailed understanding of the impact of factors such as step size, width, and initialization. By establishing convergence conditions and deriving a linear convergence rate, the paper significantly advances the theoretical understanding of optimization processes in neural networks.

$\textbf{(2) Adaptive step size scheme}$: The paper proposes an adaptive step size scheme based on the derived convergence analysis. Introducing this adaptive approach showcases the practical implications of the research findings. By suggesting a dynamic step size strategy that accelerates convergence compared to a constant step size, the paper offers a concrete and actionable method for improving optimization efficiency in neural networks. This innovation enhances the applicability of the research, providing a valuable contribution to the field of optimization techniques for machine learning models.

### Weaknesses
$\textbf{(1) Incremental contribution}$: Arora et al. in Ref [1] studied linear convergence of gradient descent for multi-layer neural networks. While Arora et al. assumed balanced weights and a deficiency margin, these conditions were proven by them in the context of gradient descent. In this work, although the authors only focus on general loss, they just study two-layer linear networks. Moreover, their convergence rate also depends on margin and imbalance. The contribution of this work is very incremental in terms of Ref [1]. Specifically, the convergence rate derived in Theorem 3.2 appears to be qualitatively similar to the results in [1], as both depend on margin and imbalance parameters. While the current work relaxes the assumption of balanced weights at initialization, it is not clear if this relaxation alone provides a significant advancement over the existing theory. A more detailed comparison of the derived convergence rate with that of [1] under comparable settings would be helpful to highlight the improvements. 

$\textbf{(2) Limited generalizability to deep linear networks}$: It seems that the authors don't mention how to generalize their results to deep linear networks. It is believed that deep networks are more commonly used in applications. The paper leaves a significant gap in its discussion by omitting details on the generalization of their findings to deep linear networks. The extension to deep linear networks is not straightforward. For instance, how would the local PL and smoothness constants be bounded in the deep network case? Would the analysis still rely on the singular values of $\mathcal{T}$, and if so, how would the structure of $\mathcal{T}$ change with multiple layers?  Addressing these questions would significantly strengthen the paper's impact.

### Questions
$\textbf{Q1.}$ Is it possible to generalize the current analysis to deep linear networks or deep nonlinear networks? T

$\textbf{Q2.}$  In Theorem 3.2, it is assumed that $\alpha_1 > 0$. Can the authors verify this condition?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the convergence rate of gradient descent for overparametrized two layer linear neural networks with generic loss.
It does so without assumptions previously used in the literature, be it on infinitesimal stepsize, infinite width, etc.
Instead, the analysis is based on local versions of the Polyak-Lojasiewicz inequality and of the descent lemma, where the global constants in both inequalities are replaced by iterate dependent versions (eq 10).
The analysis up to Eq 14 is straightforward, and most of the work consists in showing that there exists a choice of stepsize $\eta_t$ that can ensure $0 < (1 - 2 \mu_t \eta_t + \mu_t K_t \eta_t^2) \leq \rho < 1$ and $\eta_t K_t < 2$ simultaneously.

### Strengths
Apart from the work of the previous of Xu et al (2023), the paper is the first to study the setting of finite stepsize, finite width and "general" init (still requiring imbalance)

### Weaknesses
 - There is **very limited novelty** with respect to Xu et al 2023, "Linear Convergence of Gradient Descent For Finite Width Over-parametrized Linear Networks With General Initialization". If the authors could point at the novelty in the proofs, it'd be more convincing, because they seemed extremely similar and this felt thin-sliced.
- There is still a dependency on initialization through the assumption on $\alpha_1$, which excludes some initializations.



### Questions
Can the authors detail the novelty in the proof compared to previous Xu work?




Minor comments:
## References
A work which "revived" the interest in PL form the Optimization community is "Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Łojasiewicz Condition", Karimi 2016, which the authors could cite.


## Cosmetics:
- the way the authors cite the Descent Lemma is broken: " where Descent lemma is" should be "where the Descent Lemma is", same for "to derive Descent lemma," etc
- "for arbitrary non-convex functions that is": for *an* arbitrary non-convex *function* that is (singular)
- "satisfies μ-PL condition.": missing "the"
- "via chain rule:": missing "the"
- P6 "In §2.1, we show that as": we showed
- "if the $\lim_{t \to \infty}": extra "the", this time.
- "too larger" is incorrect; this whole paragraph has other typos ("but not too much $\eta_t \leq 1/K_t$)

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Well-structured and well-presented. However, I suspect that the result can be incremental: there have been a lot of results applying the PL inequality to get convergence of neural networks, e.g. [Nguyen & Mondelli, 2020] (which is not cited). Also, they do not really discuss the requirement \alpha_1 > 0 much. It does not seem like a purely technical requirement. I suspect it might fail in reality, at least, sometimes.

The paper considers a general optimization problem for a two-layered linear network and aims to prove that GD converges to a minimum with a linear rate under some constraints on learning rate. Curiously, the learning rate can even increase throughout training.

The paper starts with a review of the classical linear convergence analysis for linear models by Polyak. This analysis stems on two ingredients: 1) Descent lemma, and 2) PL-inequality. However, neither PL-inequality, nor smoothness inequality which the Descent lemma is based on, cannot hold globally for a multi-layered linear model. The paper presents generalizations of both results with "local" smoothness constants. The local smoothness constants allow for bounds which are sufficient to derive linear convergence of GD under some (time-dependent) learning rate constraints.

The paper is very well-written. The first diagram is weird (and not really the way to do things... e.g. putting NTK in the 'finite step size' category is weird). 

The paper contains no experimental validation for the main linear convergence result.

Questions: (1) Th.3.2 requires \alpha_1 > 0; what is the probability for this requirement to fail for the standard [Glorot & Bengio, 2010] initialization? (2) How could we estimate \eta_\max? How small could it be? What does it depend on?

### Strengths
Interesting theoretical result, useful, sound. Good discussion.

### Weaknesses
Well-structured and well-presented. However, I suspect that the result can be incremental: there have been a lot of results applying the PL inequality to get convergence of neural networks, e.g. [Nguyen & Mondelli, 2020] (which is not cited). Also, they do not really discuss the requirement \alpha_1 > 0 much. It does not seem like a purely technical requirement. I suspect it might fail in reality, at least, sometimes.

The paper considers a general optimization problem for a two-layered linear network and aims to prove that GD converges to a minimum with a linear rate under some constraints on learning rate. Curiously, the learning rate can even increase throughout training.

The paper starts with a review of the classical linear convergence analysis for linear models by Polyak. This analysis stems on two ingredients: 1) Descent lemma, and 2) PL-inequality. However, neither PL-inequality, nor smoothness inequality which the Descent lemma is based on, cannot hold globally for a multi-layered linear model. The paper presents generalizations of both results with "local" smoothness constants. The local smoothness constants allow for bounds which are sufficient to derive linear convergence of GD under some (time-dependent) learning rate constraints.

The paper is very well-written. The first diagram is weird (and not really the way to do things... e.g. putting NTK in the 'finite step size' category is weird).

The paper contains no experimental validation for the main linear convergence result.

Questions: (1) Th.3.2 requires \alpha_1 > 0; what is the probability for this requirement to fail for the standard [Glorot & Bengio, 2010] initialization? (2) How could we estimate \eta_\max? How small could it be? What does it depend on?

### Questions
(1) Th.3.2 requires \alpha_1 > 0; what is the probability for this requirement to fail for the standard [Glorot & Bengio, 2010] initialization? 

(2) How could we estimate \eta_\max? How small could it be? What does it depend on?

(3) Novelty wrt existing literature.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
