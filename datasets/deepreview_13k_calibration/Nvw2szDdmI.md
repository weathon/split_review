# Direct Distributional Optimization for Provable Alignment of Diffusion Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5, 8, 6

## Abstract
We introduce a novel alignment method for diffusion models from distribution optimization perspectives while providing rigorous convergence guarantees.
We first formulate the problem as a generic regularized loss minimization over probability distributions and directly optimize the distribution using the Dual Averaging method.
Next, we enable sampling from the learned distribution by approximating its score function via Doob's $h$-transform technique.
The proposed framework is supported by rigorous convergence guarantees and an end-to-end bound on the sampling error, which imply that when the original distribution's score is known accurately, the complexity of sampling from shifted distributions is independent of isoperimetric conditions.
This framework is broadly applicable to general distribution optimization problems, including alignment tasks in Reinforcement Learning with Human Feedback (RLHF), Direct Preference Optimization (DPO), and Kahneman-Tversky Optimization (KTO). We empirically validate its performance on synthetic and image datasets using the DPO objective.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Authors study the problem of sampling from distribution $\hat q$ given as the minimizer of a general optimization problem in the space of distributions given by $F(q) + KL(q||p_{ref})$, where $p_{ref}$ is the base distribution (e.g. obtained by pretraining) and $F$ is a functional in the space of distributions. $F$ can be defined as the DPO objective given user preferences of the samples from the distribution. A simple toy example of the DPO based F, which authors use for sampling from a single gaussian when the reference measure $p_{ref}$ is mixture of gaussians,  is when the DPO preference function between two samples picks the one that is closer to the correct gaussian mean.
 
Authors introduce an algorithm for this task based on applying the Dual averaging method in the space of distributions, and learning the gradient of $F$ at each iteration by neural networks. At the end of DA, they get access to a neural net that approximates the log density and the score of $\hat q$ with respect to $p_{ref}$. Then, they use a trick based on Doob’s $h$-transform relation to translate this information to the score function of  $\hat q$, which they use to obtain fresh samples from $\hat q$ using the backward process of Ornstein-Uhlenbeck.

### Strengths
The overal approach linking optimization in the space of distributions to diffusion models is new to me and looking interesting. Authors seem to derive bound for smoothness coefficients of score function of $\hat q$ based on smoothness of the diffusion for the reference measure. Their approach in using Doob's h-transform for estimating the score functions of the corrected distribution is also very interesting. The presentation of the beginning part of the paper looks clean and authors clearly state their high level goal.

### Weaknesses
Overall choice of the Dual averaging for this task seems unmotivated, I don’t see why we can’t use simpler algorithms like GD in the space of distributions, and learning the gradients with neural nets?

Other concerns:
One concern that I have is where authors use Doob’s h-transform to estimate the score of $\hat q$ as $\nabla \log\mathbb{E}[e^{-f(X_t)} | X_T]$, by estimating the derivative of probability density instead of log density, in line 1252, with samples. Given that estimating the density is ill-conditioned in general, can authors elaborate on the exact guarantee they get for this approach?

The presentation of the proofs can be more clear, right now the logical order between Lemmas, etc is not clear. I would suggest authors add more intuition before stating the mathematical formulations in each Lemma, in how that relates to the bigger picture. 

The derivative notation in line 143 is not clear.
224: one and zero should be written in English rather than numbers

### Questions
What is $\nabla_x \nabla_x^\top$ in line 1471
What is the meaning of subindices $|_{x=\bar X_t}$ ? The notation is very confusing
What is the benefit of using the Dual averaging method compared to gradient descent in the Wasserstein space? I assume you can also implement that by learning the gradient of the functional by neural nets?

Can authors clarify why they use the proof of Liu et al for their proof of convergence of the Dual averaging method in the non-convex case, instead of the more classical older papers on Dual averaging?

In the case of gaussian mixture where the authors define the objective of DPO  with the goal of sampling from one of the single gaussians, is it the case that it can mathematically be shown that the minimizer of the DPO objective is exactly a single gaussian?

In the case of gaussian mixture, Is it possible to prove guarantees for learning the sequence $\bar q_k$ rigorously with neural nets or some polynomial regression?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a distributional optimization algorithm that builds on the dual averaging (DA) algorithm combined with Doob's 
ℎ-transform. This framework encompasses several methods, including Reinforcement Learning(RL), Direct Preference Optimization (DPO), and Kahneman-Tversky Optimization (KTO). The paper includes an error analysis and provides numerical implementations of Gaussian mixtures and image generation tasks.

### Strengths
1. The paper provides a general framework for distributional optimization, integrating a sophisticated optimization algorithm (dual averaging) with Doob's ℎ-transform to capture the score function effectively.

2. The authors present a convergence rate analysis based on suitable assumptions, enhancing the theoretical robustness of the approach.

3. Experiments are conducted on both synthetic data (Gaussian mixtures) and real-life CT images, demonstrating the practical applicability of the proposed method.

### Weaknesses
The method introduces an additional entropic regularization term involving a hyperparameter, $\beta'$. In the theoretical analysis, beta prime is assumed to be larger than $\beta$, yet in the experiments, $\beta'$ is set equal to $\beta$ in all cases. There is a lack of discussion on the role of these parameters and their impact on the results. Specifically, the paper does not explore the sensitivity of the algorithm to different values of $\beta'$ relative to $\beta$, which could significantly affect the convergence rate and the final solution. Furthermore, the choice of setting $\beta'=\beta$ in the experiments, despite the theoretical requirement of $\beta' > \beta$, is not justified and raises concerns about the practical applicability of the theoretical findings. This discrepancy between theory and practice needs to be addressed with more detailed analysis and empirical validation.

Typically, the score estimation error is assumed in the $L^2$ sense, but Assumption 3.3 assumes it in the $L^\infty$ sense. This assumption is quite strong and might not hold in many practical scenarios. The $L^\infty$ norm requires the error to be uniformly bounded, which is a much stricter condition than the $L^2$ norm, which only requires the error to have a finite average magnitude. The use of the $L^\infty$ norm could limit the applicability of the theoretical results to a narrower class of problems where the score function is very well-behaved. It would be beneficial to explore if the theoretical analysis could be extended to the $L^2$ error case, which is more commonly used and more realistic for many applications.

### Questions
Typically, the score estimation error is assumed in the $L^2$ sense, but Assumption 3.3 assumes it in the $L^\infty$ sense. Could this assumption be improved?

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
The paper formulates the diffusion model alignment problem as a general distribution optimization problem. The proposed general objective, which involves regularized loss minimization over probability distributions, encompasses important tasks in language model alignment, including RLHF, DPO, and KTO. The authors propose an algorithm that first employs Dual Averaging to approximate the optimization objective function over a distribution into a potential function (thereby transforming the variable from a distribution to a point), and then uses this learned potential function to fine-tune diffusion models. The approach is supported by theoretical guarantees.

### Strengths
1. The paper's formulation of a general distribution optimization problem is significant as it unifies several widely-studied alignment tasks under a single framework, making it relevant to current research priorities in the field.
2. The paper is well-written and easy to follow.

### Weaknesses
1. The paper lacks crucial implementation details for applying Dual Averaging to diffusion models. Specifically, while the objective involves  $KL(q|p_{ref})$ and $exp(-f)p_{ref}$, it doesn't address how to compute these terms when only time-dependent score functions are available by diffusion models. The potential Monte Carlo alternatives would be computationally intensive.

2. In phase 2,  the proposed correction term u(x,t) in equation 17 is computationally impractical, requiring multiple reverse process simulations at each inference timestep.

3. Based on 2, the paper's key Assumption 3.4 regarding the small approximation error of u* is questionable, particularly given the gradient terms and complexity of the approximation.

### Questions
1. According to Alg. 4.1, we've already got $q_K \propto exp(-f_K)p_{ref}$, which is exactly the optimal solution of (1) (also the target of phase 2), why do we need to conduct phase 2?

2. The paper claims to provide convergence guarantees for diffusion alignment problems without relying on isoperimetric conditions. However, Assumption 3 requires that $\nabla \log p_t$ is $L_p$-smooth at every time $t$. Could this requirement serve as an alternative to isoperimetric conditions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
From my understanding, the paper presents a novel distribution alignment technique for score-based diffusion models based on optimization techniques over probability measures. Standard measure optimization techniques face challenges in the diffusion model setting because both the density governed by the model and the density of the true reference distribution cannot be evaluated. The model parametrizes its distribution using the score function/networks, whereas the true reference distribution is accessible only through samples. The work reformulates the measure optimization as an optimization problem over potentials. Then, sampling using the learned potential proceeds by the Doob's $h$-transform technique.

### Strengths
- The proposed method is usable on relevant examples such as reward-based alignment, DPO, and KTO. There are contributions even in the small details of this derivation, including rewriting the DPO objective in a way that is more amenable to statistical analysis.
- The sampling error is bounded while taking into account all sources of approximation: the discretization of the SDE, approximation of the score, and approximation of the Gibbs distribution resulting from the potential.
- While the theoretical derivations in the paper are already a strong contribution, the experiments are helpful in confirming that the method works on simple tasks.

### Weaknesses
Broadly speaking, the significant portions of the paper are unreadable. While I applaud the authors effort in producing this work, I request an equal effort in presenting it well. Some specific points are outlined below.
- The "two main challenges" addressed by paper are stated at least three times (045-048, 162-168, 185-194). While I believe this was done for clarity sake, the "challenge" is never described in an accessible way. While I interpret them as what I wrote in the summary, it is not explicitly clear to me. To say "particle-based optimization methods are not designed for resampling from the distribution where obtained particles follow" is meaningless without having described what particle-based methods are. The pre-trained distribution "failing to satisfy isoperimetric conditions" is meaningless without clearly explaining the implication of this (for example, are there no distributional optimization guarantees for distributions that do not satisfy isoperimetric conditions)? 
- The appendix is a literally a list of theorems and proofs. Whether for optimization or sampling-style analysis, it is important to give context to all results. Concretely, this means: 1) providing a proof outline, 2) describing which technical steps are identical to/adapted from previous work (with references), and what proof techniques are specific to this paper. In its current state, it is hard to even verify the technical correctness of the paper.
- The notation is excessive, and not always introduced. Unless I am misunderstanding, $\hat{q}$ is presented as the minimizer of the objective, but seems to be changed to $q^*$ towards the end. I am also not sure that $\tilde{X}_{kh}^{\leftarrow}$ is introduced in 416. In the final version, please provide a global notation table in the first appendix containing all symbols and a verbal description.

### Questions
- In Assumption 2, are both (i) and (iii) necessary? Can we not assume (iii), the derive (i) with TV^2 instead of KL, and then apply Pinkser's inequality to achieve the smoothness relative to KL?
- The nonconvex convergence analysis results only in convergence of the successive gaps of iterates. What would it take to achieve convergence to an appropriately-defined stationary point?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new optimization procedure to minimize entropy-regularized versions of finetuning losses for diffusion models such as DPO or KTO losses. This optimization method is an approximation of Dual Averaging (DA), where, instead of tracking a set of particles to approximate the distribution as done in prior work, an estimate of the unnormalized density ratio between the iterate and the original reference model is tracked. These changes make it possible to sample from finetuned model (e.g. the final iterate) by simulating the backward SDE of a OU forward process (à la diffusion model), where the score of the forward process is estimated by a Monte Carlo approximation its expression obtained using Doob's h-transform formula, whose ``correction'' terms can be estimated from the density ratio-estimate.

On the theoretical side, global convergence (in TV) of the final DA iterate to the true minimizer is provided when the loss is Convex, its first variation is bounded and smooth, and the density ratio estimates are accurate enough, while non global convergence (convergence of the gradient) to some limit is established if the loss in nonconvex. Finally, the TV between the distribution of the final finetuned model samples and true finetuning loss minimizer is controlled, assuming a bound on the error of score of the reference OU process, and a bound in the error of the Doob correction term.

The method is implemented on a synthetic 2d mixture of Gaussians reference model with mode alignment, an image dataset with color alignment, and Head CT scans from Medial MNIST with orientation alignment, where it is show that the loss trends downwards, and that the finetuned samples are more aligned than the ones from the reference models.=

### Strengths
The present submission tackles an important problem (diffusion model alignment). The method is an interesting twist on existing dual averaging approaches, whose setting does not involve estimating density ratios.

A significant effort is spent providing end-to-end guarantees for both the optimization procedure and the sampling procedure. These guarantees do not directly require a Log-Sobolev inequality on the target. 

Finally, on the experimental side, the method is tested on high-dimensional dataset, and display reasonable performance (although there is no relative point of comparison due to the lack of results reporting the performance of existing methods on the datasets and tasks explored by the paper).

### Weaknesses
My main concern is the lack of comparison against existing methods to finetune diffusion models, both in terms of performance and in terms of space and memory complexity. I personally like the paper, however I believe it needs comparison against the applicable baselines before acceptance. Specifically, a comparison against methods that directly optimize a DPO loss for diffusion models is needed to understand the relative benefits of the proposed approach. An investigation of the impact of $\beta$ would also be interesting, as it controls the strength of the entropy regularization and could significantly affect the final performance and convergence properties.

The method involves some computationally expensive operations such as Monte Carlo estimation at every iteration of the DA loop. It would be nice to have the total time and space complexity of the algorithm described somewhere, complementing a Computational time comparison with other methods. The fact that only one previous density ratio estimate (and not k) are needed to approximate the next one (see l 1953, algorithm D1) seems important to cap the total time and space complexity of the method and not directly obvious from equation 2 and 3, should be mentioned in the main. Furthermore, the computational cost of the sampling phase, which requires estimating the Doob's h-transform correction term, should be discussed in detail, as this could be a significant bottleneck.

The presentation needs to be clarified. Currently,
  - How is the reader supposed to know that the equality on equation (2) holds? It seems hidden as specific instances of Lemma 1, but this should be highlighted more. The connection between the theoretical results and the practical implementation of the algorithm is not always clear.
  - The recipe for estimating the density ratios during DA is not clearly described in the main body. The exact procedure for obtaining these estimates, including the choice of neural network architecture and training details, should be explicitly stated.
  - The presentation of the image generation results could be improved: what is the color (0.9/0.9/0.9)? this deserves to be on one of the figures IMO. Figure 7 definitely helps to understand how much the model has learned, and should be at least referenced in the main text. The quantitative metrics used to evaluate the alignment should also be clearly defined and justified.
  - I did not understand the meaning of the ("Linear/nonlinear", "k=1/2/3 DA Loops") terms. Do you mean number of DA iterations? Why linear and nonlinear? The distinction between these cases should be made more explicit and related to the theoretical analysis.
  - The reason "our method works without isoperimetry conditions such as Log-Sobolev inequality" could be explained more clearly: my understanding is that the original DA update for MLFD required running an inner Langevin sampler, which is sensitive to LSI. On the other hand, the current method estimates the density ratio by using the backward SDE to sample from the reference model, which does not rely on an LSI to converge. This should be clearly articulated in the main text, highlighting the key differences and advantages of the proposed approach.

### Questions
.

### Soundness
3

### Presentation
2

### Contribution
3
