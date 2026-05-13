# Flow Matching for One-Step Sampling

- Decision: Reject
- Scores: 6, 3, 1, 3

## Abstract
Flow-based generative models have rapidly advanced as a method for mapping simple distributions to complex ones for which the distribution function is unknown. By leveraging continuous-time stochastic processes, these models offer a powerful framework for density estimation, i.e. an algorithm that samples new points based only on existing samples. However, their requirement of solving ordinary differential equations (ODEs) during sampling process incurs substantial computational costs, particularly for large amount of data and numerous time points. This paper proposes a novel solution, which is based on a theoretical analysis of Flow Matching (FM), to overcome this bottleneck, namely, we developed an algorithm to find the point prototype for a given point from the target distribution. By eliminating the need for ODE solvers, our method significantly accelerates sampling while preserving model performance. Numerical experiments validate the proposed approach, demonstrating its efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers continuous normalizing flows and proposes an algorithm for finding the corresponding point in the base distribution (called its prototype) for a given point from the target distribution, without having to solve the defining ODE. For each sampled target point, the explicit velocity function is followed backwards to find a suitable base distribution point. Using the set of point pairs as a training set, a model is trained on them; that is, the generation can take place in a single step, and the network does not need to be invertible.

### Strengths
The single step sampling results in a greatly improved speed without significantly affecting the model performance.

### Weaknesses
Language: there are many spelling and grammatical errors, and the sentences are sometimes incomprehensible.
Especially in the introduction, the main ideas are hard to comprehend, especially if one does not know the previous work in detail.
The experiment in Section 4.2 should be explained in more detail or a reference needs to be added if it is a common method for image colorization.
Line 114: there is no "Introduction and Related Work" section, these are two separate sections in the paper.

The problem description for the color transfer task is missing. The section starts with "For *the* color transfer problem", which implies it has been already introduced, but it has not.

The paper does not explicitly state that the `tol` parameter is a hyperparameter that needs to be tuned. It should also mention that `tol` affects the ODE solver accuracy.

### Questions
1. Sec 3.3: what does the >>tol<< parameter have to do with the generation? Why and how does it affect the shape of the base distribution?
2. Page 3, footnote 2: "up to a constant": Is it a constant factor or a constant term?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a flow-based generative modelling approach that does not require solving an ODE for inference. The method seems to rely heavily on the "exact velocity" from (Ryzhakov et al., 2024); however, both the motivation and details of this need more development. Moreover, more comparison (especially numerical results) to previous works is needed. E.g. other approaches that bypass inference integration, like consistancy models, are not mentioned in the related work.

### Strengths
1. Adresses the problem of long inference time by bypassing the inference ODE integration.

### Weaknesses
1. More elaboration on the method of Ryzhakov would be helpful.
2. Unclear about motivation and comparison to related works.
3. Lack of numerical results.

### Questions
1. Where exactly is the convexity in the problem?
2. How does this method compare to related work?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a one-step sampling method based on flow matching. Given a set of training samples from an unknown distribution $\rho_1$, a mapping is learned from a simpler known distribution $\rho_0$, typically a normal distribution, to $\rho_1$.  Using a discretized estimate of the flow, derived in (Ryzhakov et al. 2024), so-called prototypes in $\rho_0$ are found by solving an ODE for each training sample in $\rho_1$, under the assumption of linear flow. A network is then trained to directly map from $\rho_0$ to $\rho_1$, using the set of training samples paired with their respective prototypes.

### Strengths
The most important benefit of the proposed sampling approach is its speed, since instead of solving an ODE, sampling is done in one step using a neural network.

### Weaknesses
The experiments described in the paper are extremely limited. It is shown that 8 Gaussians can be generated using the proposed sampling method. It is also shown, with four example images, how colors can be transferred from one distribution to another, with target colors given by a separate image. Furthermore, in the paper, the sampling method was not compared to any other alternative method or ablated versions of the same method. For a publication to be recommended, the experiments should be expanded to include comparisons against relevant baselines. The text describing the color transfer experiments should preferably also be rewritten since the current version is too unclear.

It is rather unclear what a prototype is, whether it is the point in $\rho_0$ one would converge to if there are no errors in ODE solver, or whether a prototype can be any point in $\rho_1$ that you happen to converge to. Something that would have been interesting to know is how precise the prototypes truly are, and what effect the errors have on the end result. It is claimed that the quality of the prototypes is sufficient for images to be predicted, but this is a question that ought to be studied in greater depth. 

When prototypes are found in $\rho_0$, noise is first added to the position in $\rho_1$, but the motivation for this is hardly satisfactory. In almost a full page the paper tries to argue why the added noise is necessary. It seems that the implementation of the Runga-Kutta method relies on a particular set tolerance parameter. If the tolerance is set too high, the method will stop early, and points will never reach $\rho_0$. However, if normal distributed noise is added in $\rho_1$, at least the points end up being spread like a normal distribution, but there is no convincing argument that the errors would then be smaller.

The language of the paper is unfortunately rather problematic with numerous missing articles (the, a), improper prepositions, and awkward sentences that are hard to interpret. However, the problems are not too severe for the material to be understood and should be relatively easy to correct in a final version of the paper.

The two algorithms are very similar to each other. The only difference seems to be that if you have a discrete label, a separate mapping is learned for each value of the label. It would have been sufficient to just keep Algorithm 2.

The notation for buffer B varies in different parts of the text.

### Questions
* What is a prototype? How would a prototype be defined? For each point in $\rho_1$ are there many potential prototypes?
* Does the $\sigma$ in (1) have anything to do with the $\sigma$ in (3)? Isn’t the $\sigma$ in (1) necessary to make the mapping invertible, while the $\sigma$ in (3) is related to the tolerance? 
* Why is no noise added in (4), just like in (3)?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new flow matching approach for efficient sampling. The method finds an approximate prototype mapping by using importance sampling and the soft-max distribution. The prototype is finally found by solving a Cauchy problem. The prototypes and the connected target samples are used to define the  velocity field of the flow. The algorithm is evaluated on a 2D GMM task and a color transfer task.

### Strengths
- the new algorithm could potentially provide more computationally efficient generative models
- the presented algorithm seems to be reasonable, even though a few theoretical justifications are unclear

### Weaknesses
(1) there are no comparisons to other flow matching approaches or generative models (diffusion, consistency models) provided
(2) The evaluations are only done on a simplistic 2D dataset and the color transfer task, where I have difficulty assessing how good the result really is
(3) No evaluation and comparison of the computational efficiency of the generative model is offered (which was the main motivation of the approach). Its unclear to me how the single-step sampling here actually works? We still have the solve the ODE, don't we?
(4) Theory is also quite hand-wavy. For example, it is unclear to me how importance sampling is used to estimate the integral of Eq (1). Which distributions are replaced here ? I.e., what is the sampling distribution?
(5) It is unclear to me how tolerance and sigma interact and why we need sigma. From the presented theory, sigma would not be needed, would it? But without sigma, only very poor prototypes are learned, so this seems to be unsatisfactory to me

### Questions
- comparisons to other flow matching and consistency models (As they have the same goal) is needed
- Add more experiments for more complex target distributions
- Add more detail for the color tansfer task and compare to other methods (also qualitatitively)

See also weaknesses for more questions.

### Soundness
2

### Presentation
2

### Contribution
2
