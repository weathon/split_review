# Ensemble Kalman Diffusion Guidance: A Derivative-free Method for Inverse Problems

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
When solving inverse problems, it is increasingly popular to use pre-trained diffusion models as plug-and-play priors. This framework can accommodate different forward models without re-training while preserving the generative capability of diffusion models.  Despite their success in many imaging inverse problems, most existing methods rely on privileged information such as derivative, pseudo-inverse, or full knowledge about the forward model. This reliance poses a substantial limitation that restricts their use in a wide range of problems where such information is unavailable, such as in many scientific applications. To address this issue, we propose Ensemble Kalman Diffusion Guidance (EnKG) for diffusion models, a derivative-free approach that can solve inverse problems by only accessing forward model evaluations and a pre-trained diffusion model prior. We study the empirical effectiveness of our method across various inverse problems, including scientific settings such as inferring fluid flows and astronomical objects, which are highly non-linear inverse problems that often only permit black-box access to the forward model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new approach to solve inverse problems using a derivative-free optimization method based on the Ensemble Kalman Filter. The core idea is to approximate the data-fidelity term gradient with a statistical
linearization from the ensemble Kalman methods. The method is applied to three  types of inverse problems: computational imaging problems, the Navier-Stokes equation, and the black-hole imaging problem. The method is compared other derivative-free baselines.

### Strengths
- Interesting approach to solve inverse problems.
- Derivative-free approaches can be useful in many cases and have received much less attention than gradient-based methods.

### Weaknesses
 - Positioning relative to the state-of-the-art is not clear, in particular with respect to the proposed framework, which seems to be a variant of the existing ones (see **Q2**). The connection to existing plug-and-play methods, particularly those using diffusion models, is not adequately addressed. The paper needs to clearly articulate the novelty beyond simply being a derivative-free version of existing methods.
- The evaluation is not completely satisfactory (see **Q3, Q4**). The lack of comparison with methods that utilize gradients of the forward operator makes it difficult to assess the true potential of the proposed approach. The experiments should include a more comprehensive set of baselines, especially those that leverage differentiable forward models.



### Questions
- **Q1:** Use of a `pretrained diffusion model`  is mentionned. I can see this type of models for images, but for complex data with varying domain of definition, like in many scientific applications, the diffusion model needs to be retrained for each type of data no? IT is not completely clear how reusable these models are outside computational imaging.

- **Q2:** The prediction-correction scheme strongly relate to the usual Plug-and-Play methods classicaly used in inverse problem resolution. The proposed scheme is related to the Forward-Backward Splitting (FBS) method, which is typically used in the DiffPIR [B]. From what I understand, equation (9) in this paper corresponds to equation (13) in [A]. Could you elaborate on the main difference of between the proposed method and the DiffPIR framework? (except the derivation free aspect). Other missing references are [B], a survey on using diffusion models for inverse problems, and [C], which also consider diffusion prior for inverse problems, with gradient based method but applied to the Black-hole imaging problem. Adding comparison with their method would be very useful.

- **Q3:** To make is possible to evaluate how good the results are compared to methods that are able to access the gradient of the forward operator, it is necessary to add a few methods that have access to the forward operator's gradients. Indeed, even though ODE solvers are not always natively differentiable, there are more and more works that consider making them differentiable, for instance using `jax` for Navier stokes using pseudo-spectral solver  [here](https://github.com/google/jax-cfd). The interesting question is: should we spend some time making them differentiable or do we not gain much by doing so. Therefor, quantifying how much is lost on simple cases as the ones presented here is necessary to make the case of derivative free methods. In particular, adding the results of the DPS method and the DiffPIR method would be very useful at least for the imaging task. Note that these models are both implemeted in the [`deepinv`](https://deepinv.github.io) library (see [here](https://deepinv.github.io/deepinv/deepinv.sampling.html)). Also, adding the DPS base line and PnP-DM form [C] for black hole imaging would better illustrate how much we loose by note considering the gradient of this differentiable operator. Adding them for Navier-Stokes would also be very interesting but probably more challenging.

- **Q4**: The value of $J$ and $Q$ in the experiments are not reported. Could the author provide them? From equation (16), I understand that we need to compute the forward operator $J$ or $Q$ times at each iteration. From the NAvier stokes experiment, assuming that the procedure is run for 1k steps, I guess $J = 295$ and $Q=2048$? How were these value chosen? What are their impact on the results? Also, would having access to the gradient mean going roughly 100 times faster than EnKG? (The computational cost of computing the gradient through autodiff is approximately x2/3 times the cost of evaluating the forward operator). Note that the metrics chosen (# of evaluation of Fwd/DM, Seq) are not clear. Better definition of what they represent mean would be useful. Adding the total runtime of the method would help a lot to assess the computational cost.

- **Q5:** In the black-hole experiment, how many simulation are used to train the diffusion model?

### Minor comments, nitpicks and typos

- Missing ref: 
- l.066: "One more challenging" -> "On"
- l.069: "More computationally efficient" -> than what?
- l.078: "often Gaussian" -> They are almost never Gaussian, but they are modeled as such and this gives reasonable results.
- l.141: "and Nelder-Mead simplex methods" -> Extra `,`.
- l.198: The drop of the subscript $x$ for the gradient is confusing
- Eq (7) -> The notation $\Delta x_i$ is not defined. As it is not used anywhere else, I would recomment using $\|x_{i+1} - x_i\|$ instead.
- Eq (12) -> $x_i'$ should have a super script $(j)$. It is also not completely consistent for $x_{i+1}$.
- l.302: "instead"
- l.316: `our approach outperforms the standard strong DPS baseline` -> The DPS result are not present in the table, so I think they are missing?
- l.335: What is the `EDM` framework?


- l.847: The change from  "l" to "j" should be made explicit as it is not immediately clear and can appear as a typo. 

### References

[A] : Daras, Giannis, et al. [A survey on diffusion models for inverse problems.](https://arxiv.org/pdf/2410.00083) arXiv preprint, 2024.  
[B] : Zhu, Yuanzhi, et al. [Denoising diffusion models for plug-and-play image restoration.](https://arxiv.org/pdf/2305.08995) Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023.  
[C] : Wu, Zihui, et al. [Principled Probabilistic Imaging using Diffusion Models as Plug-and-Play Priors.](https://arxiv.org/pdf/2405.18782) arXiv preprint, 2024.

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
3

### Summary
The paper presents Ensemble Kalman Diffusion Guidance (EnKG), a novel derivative-free method for solving inverse problems using pre-trained diffusion models. Traditional approaches often require detailed knowledge of the forward model, such as derivatives, which limits their applicability. EnKG overcomes this by relying solely on black-box evaluations of the forward model and a pre-trained diffusion model.
Key contributions are twofold: 1) EnKG operates solely with black-box access to forward model evaluations and a pre-trained diffusion model, making it particularly useful in scenarios where derivative information is inaccessible. 2) The authors introduce a prediction-correction (PC) framework that utilizes the empirical covariance matrix of ensemble particles during the correction step. This innovation allows EnKG to effectively bypass reliance on gradients, enhancing its applicability in non-linear inverse problems.
The paper demonstrates the effectiveness of EnKG across various inverse problems, including applications in fluid dynamics. These examples highlight the method's capability to handle complex, non-linear scenarios that are common in scientific research.
In summary, this work expands the toolkit for addressing inverse problems in machine learning by introducing a flexible and robust approach that maintains the generative power of diffusion models.

### Strengths
1)	EnKG operates without gradients, needing only black-box access to forward models, making it highly applicable to complex inverse problems with unknown or undefined derivatives. The proposed PC framework generalizes existing methods, enabling adaptability across various inverse problems without retraining.
2)	The current work demonstrates strong performance, notably in complex tasks like the Navier-Stokes equation, outperforming gradient-based solutions
3)	Provides deeper understanding and new interpretations of diffusion-based approaches, contributing to the field of inverse problem-solving.

### Weaknesses
1) The method may face challenges when scaling to very large models or high-dimensional data, as ensemble-based approaches can become computationally expensive. A further insight along this line would be useful. Also, it relies on pre-trained diffusion models, which might limit effectiveness if high-quality models are not available for certain tasks. Specifically, the computational cost of maintaining and updating the ensemble, especially in high-dimensional spaces, needs further analysis. The paper should discuss the memory footprint and computational time required for each iteration, considering the number of ensemble members and the dimensionality of the problem. The reliance on pre-trained diffusion models also raises concerns about the method's adaptability to novel tasks or datasets where suitable pre-trained models are not readily available. The paper should discuss the sensitivity of the method to the quality of the pre-trained model, and how performance might degrade with less optimal models.
2) The empirical validation focuses on specific problem sets; broader testing across diverse applications would strengthen the generalizability claim. The current validation is limited to a few examples, and it is unclear how the method would perform in other types of inverse problems, such as those involving different types of physical systems or data modalities. A more comprehensive evaluation, including a wider range of benchmark problems, would be necessary to establish the robustness and general applicability of the proposed method. The paper should also discuss the limitations of the current validation and suggest future directions for more extensive testing.
3) A further analysis on the algorithm complexity would be beneficial as the combination of the prediction and correction steps might introduce additional computational and implementation complexity due to ensemble covariance estimation. While the paper mentions the prediction-correction framework, it lacks a detailed analysis of the computational complexity of each step. Specifically, the cost of the prediction step, which involves sampling from the diffusion model, and the correction step, which involves updating the ensemble based on the forward model evaluations, should be analyzed separately. The paper should also discuss the potential for parallelization in each step and how this might affect the overall computational cost.

### Questions
1) How does EnKG perform when applied to larger-scale problems or high-dimensional data? Are there specific limitations to its computational efficiency?
2) Is there any dependence on the performance and the pertrained model? How sensitive is the method to the quality and type of pre-trained diffusion model used? What are the implications if a suitable model is not available?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Diffusion models have been used to address inverse problems, with numerous diffusion-based solvers that avoid retraining existing diffusion models. These approaches typically rely on pseudo-inverses or derivatives tied to the forward model. This paper introduces a novel diffusion-based inverse solver designed for cases where the forward model is unknown.

The authors propose Ensemble Kalman Diffusion Guidance (EnKG), a derivative-free method that utilizes only forward model evaluations along with a pre-trained diffusion model.
In the proposed method, guidance term is computed as follows:
1. Particles are initialized to compute covariance in following steps.
2. During the diffusion trajectory, the particles are pushed by ODE solver.
3. Then, synthesized samples are applied to the forward model and compute covariance of them.
4. Diffusion trajectory is updated by the formula given the EnKG.
The proposed method replace the derivative of the forward model by computation of covariance and ODE solving.

The empirical results demonstrate the effectiveness of EnKG across diverse inverse problems, including cases where the measurement operator is treated as a black box. Specifically, the method is applied to image inversion problems with explicit forward models, Navier-Stokes inverse problems where the forward model is computed by solving PDEs, and black hole imaging, where the forward model is a black box.

### Strengths
1.	Novel Approach: The paper introduces statistical linearization within ensemble Kalman methods to diffusion-based inverse problems, a novel concept in this context.
2.	Innovative Guidance Term Formulation: The authors present a unique formulation for the guidance term, with a clever trick that replaces the derivative of the forward model with covariance from forward evaluations.
3.	Comprehensive Validation: The effectiveness of EnKG is demonstrated across three different scenarios: (1) cases where the forward model is known and differentiable, (2) cases where the forward model is known but differentiating it is impractical (e.g., PDE-based models), and (3) cases where the forward model is a black box, with observations as the only available information.

### Weaknesses
1. Limited Discussion of Related Work: The paper lacks depth in interpreting and explaining related works.
- The motivation behind the weighting matrix $w_i C_{xx}^{(i)}$ is unclear. Could you provide further explanation on the intuition and reasoning behind the choice of weighting matrix?
- Although the Kalman method is a core component, the paper does not provide a thorough explanation of its role and mechanics in this context. Specifically, which parts of the method are directly applied from existing literature and which represent novel contributions of this paper? For example, the introduction of weighting matrix, the derivation using local linearity of the operator in the proof, and the convergence claim. Related to above questions, please clarify the intuition and motivation provided by the literature versus that introduced by the authors.
2. Overstated Contribution: The claimed contributions seem somewhat overstated. The concept of Predictor Corrector interpretation in guidance-based methods is not entirely new.

Additionally, I would like to highlight some points that were missed during the previous review process:
If a matrix $A = \sum_i a_i a_i^T$, then $\text{tr}(A) = 0 \iff a_i = 0 \, \forall i \iff A = 0$.

The assumptions imply that $\psi(x^{(j)}) - \bar{\psi} = 0 \implies x^{(j)} = \bar{x}$, which is a rather strong condition, especially when $\psi$ is ill-posed.

I recommend that the authors provide empirical evidence to demonstrate that the proposed derivative-free correction adequately approximates the actual correction term.

### Questions
- Line 316: Is the DPS baseline included in the table?
- Black-Hole Imaging Problem: In the black-hole imaging problem, how is $G(\phi(x_i, t_i))$ computed if $G$ is unknown and $\phi(x_i, t_i)$ differs from the observed data? Could you provide a step-by-step explanation of how the black-box forward model is handled in the case? Additionally, please clarify if any assumptions are made about $G$ or generated samples in this scenario.
- Proof of Lemma 1: The proof shows a monotonic decrease in $\text{tr}(C_{xx}^{(i)})$. Why does this quantity converge to zero? From another perspective, a vanishing covariance implies the trajectories converge to a single point. Does this implication contradict the ill-posed nature of inverse problems, which typically have many possible solutions?

Possible Errata
- Lines 225 and 284: Remove  \Gamma .
- Line 731: Remove the extraneous ‘(‘.
- Line 847: Replace with $\approx$.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors address inverse problems using diffusion models as priors within a restrictive setup where the forward model is accessible only point-wise.
They employ a Predictor-Correct framework, where in the prediction stage, samples are drawn from the prior using the ODE describing the diffusion model.
In the correction stage, a MAP problem involving the forward model at the current diffusion step is solved through gradient-based updates.
Unlike previous approaches, the authors approximate the intractable term in this MAP formulation by evaluating it on samples generated via the ODE.
Since only point-wise access to the forward model is available, the authors estimate the gradient through statistical linearization and ensemble Kalman methods.
This approach maintains a set of particles and uses them, along with their centroids, to approximate the gradient.
The authors validate their algorithm on three different inverse problems.

### Strengths
Introduction of an algorithm that solves inverse problems with diffusion models prior that only requires point-wise access to the forward model

### Weaknesses
 
**Methodological concerns**

- The authors’ motivation for their "Derivative-free correction step" in Lines 246–263. The matrix $C_{xx}$ appears without adequate justification, and in Equation (12), the authors invert $C_{xx}$ even though it is a singular matrix, as the number of samples used to compute it is less than the dimensionality of the problem. Consequently, $C_{xx}$ cannot be treated as a preconditioning matrix in this context. The authors claim that $C_{xx}$ facilitates interaction among particles; however, this is not rigorously justified, and the use of a singular matrix in this manner is questionable. The update rule derived from this singular matrix may not be well-defined or effective.
- In the appendix, the authors base their proofs on Equation (20), which is introduced without sufficient explanation. This equation appears to correspond to the ensemble update, which assumes an estimation of the gradient, the very objective of the lemmas and propositions that follow. This circular reasoning raises concerns about the validity of the proofs. Furthermore, the derivation of $C_{xx}$ in the appendix (Lines 801-804) is flawed because the outer product between the involved quantities does not necessarily commute, invalidating the simplification. Specifically, $(a + b)(a + b)^\top = a a^\top + 2ab^\top + b b^\top$ only holds if $a b^\top = b a^\top$, which is not generally true in this context.


**Technical concerns**

- In Lines 125–127 (paragraph following Equation (4)), the authors suggest that the guidance term depends on the noise scheduler $\dot{\sigma} \sigma$. However, this dependence result from their specific formulation. As verification, the authors can review Equation (5) in [1] or write DPS's algorithm in terms of the score. The guidance term is not scaled by the noise scheduler. This indicates a potential misunderstanding of the underlying theory of diffusion models.
- The statement in Lines 194–195 is misplaced. Specifically, $\log \hat{p}(y | x_{i+1})$ is a composition of the simulated ODE and the forward model, making it highly non-convex. Therefore, the hypothesis of convexity is unrealistic. Besides, this term varies at each diffusion step, as it is composed with the ODE at different time steps, which diverges from the requirements outlined in [2], Chapter 4. Hence, the iterative updates may not converge to a true MAP estimate within this setups.


**Errors and clarifications**

- Equations (12)–(14) lack clarity. The variable $x_{i+1}'$ is undefined, and while the argmin is specified with respect to $x_{i+1}^{(j)}$, this variable does not appear in the equations. This makes the equations difficult to interpret and implement.
- In Lines 897–903, the gradients of $p$ are missing a logarithmic term. This is a critical error in the derivation, which could affect the correctness of the results.
- The first part of Assumption (3) regarding $C_{xx}$ is redundant. Since $C_{xx}$ is a positive semi-definite matrix, its trace is non-negative, being the sum of positive eigenvalues. Therefore, if the trace of $C_{xx}$ is zero, $C_{xx}$ must be the zero matrix.
- In Lines 316–317, "DPG" should replace "DPS," as DPS is not included in the experiments.
- The term "guidance" is repeated twice in Line 52.


### Questions
- Plot (b) in Figure 3 is difficult to interpret. Could you clarify what the values 0.2, 0.4, ..., 0.8 represent? Additionally, what do "Seq # DM" and "Seq # DM grad" refer to in this context?
- Plot (c) reports the runtime of the proposed algorithm, with an average of  approximately 140 minutes. This is a considerable computational cost (about 2 hours) for solving one inverse problem.
    * How does this runtime compare to other algorithms (aside from EKI) ?
    * Can you comment on the practical applicability of the method given this runtime?
    * Considering the high computational cost, how does the algorithm perform relative to methods that fine-tune or train smaller network components for the guidance term, as seen in [1, 2, 3, 4]?


---
.. [1] Black, Kevin, et al. "Training diffusion models with reinforcement learning." arXiv preprint arXiv:2305.13301 (2023).

.. [2] Uehara, M., Zhao, Y., Black, K., Hajiramezanali, E., Scalia, G., Diamant, N. L., ... & Levine, S. (2024). Fine-tuning of continuous-time diffusion models as entropy-regularized control. arXiv preprint arXiv:2402.15194.

.. [3] Fan, Ying, et al. "Reinforcement learning for fine-tuning text-to-image diffusion models." Advances in Neural Information Processing Systems 36 (2024).

.. [4] Denker, Alexander, et al. "DEFT: Efficient Finetuning of Conditional Diffusion Models by Learning the Generalised $ h $-transform." arXiv preprint arXiv:2406.01781 (2024).

### Soundness
1

### Presentation
2

### Contribution
2
