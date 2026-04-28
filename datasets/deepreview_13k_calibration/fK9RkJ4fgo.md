# Stochastic interpolants with data-dependent couplings

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Generative models inspired by dynamical transport of measure -- such as flows and diffusions -- construct a continuous-time map between two probability densities. 
Conventionally, one of these is the target density, only accessible through samples, while the other is taken as a simple base density that is data-agnostic.
In this work, using the framework of stochastic interpolants, we formalize how to \textit{couple} the base and the target densities, whereby samples from the base are computed conditionally given samples from the target in a way that is different from (but does preclude) incorporating information about class labels or continuous embeddings.
This enables us to construct dynamical transport maps  that serve as conditional generative models.
We show that these transport maps can be learned by solving a simple square loss regression problem analogous to the standard independent setting.
We demonstrate the usefulness of constructing dependent couplings in practice through experiments in super-resolution and in-painting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper formalizes conditional and data-dependent generative modeling within the stochastic interpolates framework. The authors derive the relevant transport equation for the deterministic scenario (ODE) and the forward and backward SDE for the stochastic scenario. They demonstrate that these equations can be acquired by minimizing straightforward regression losses. Lastly, data-dependent coupling is introduced, providing a recipe for constructing base densities that depend on the target distribution.

### Strengths
- The paper formalizes two important notions in generative modeling, conditional and data dependent coupling, in the stochastic interpolates framework. 
- The authors show how to construct both conditional and data-dependent coupling.

### Weaknesses
1. **Limited contribution** - the work does not introduce a new concept and is a formulation of existing concepts into an existing framework.

   1. The derivation of the transport equations in section 2.1, which takes a great portion of the paper, was already done in section 4 of [3] for the unconditional case, where the addition of the conditioning repeats the same derivation with marginalization over the condition. Furthermore, conditioning for super-resolution has been shown in [5] as well as beening widely used in diffusion models (e.g., [4]), and since they can be thought of as particular cases of stochastic interpolants, the addition of conditioning is straightforward.
   2. Data dependent coupling was already introduced in the context of Flow-Matching [1,2], which is an essentially equivalent framework to stochastic interpolants. While the work provides a coherent, complete formulation of conditional and data-dependent generative modeling in the stochastic interplant framework, I believe the paper needs to be reframed and further emphasize the analogies to existing works and highlight the benefits of formulating these concepts in the stochastic interpolants framework as opposed to for example Flow-matching which already provides the same degrees of flexibility in the design of generative models, or another example, the inpainting application considered in section 3.1 which is equivalent to the setting used in [4] only with a different noise scheduling. 

   The core issue is that while the paper presents a formulation within the stochastic interpolants framework, it does not sufficiently distinguish itself from existing methods, particularly in terms of practical advantages. The data-dependent coupling, while presented as a general approach, lacks a clear demonstration of superiority over existing methods like those in [1,2], which also achieve similar coupling effects through optimal transport. The paper needs to clarify what specific benefits this formulation offers beyond simply re-expressing existing ideas in a new framework.

2. **Empirical evaluation** - the empirical evaluation is solely qualitative, which makes it impossible to assess whether there is a benefit in using conditional and data dependent couplings in the stochastic interpolant framework. The lack of quantitative metrics makes it impossible to assess the practical value of the proposed approach, especially when compared to existing methods that have demonstrated performance through established benchmarks. The qualitative results are insufficient to justify the introduction of this formulation, as it does not provide a clear indication of its effectiveness or advantages over existing methods.

### Questions
1. Can the authors emphasize the analogies to existing works and highlight the benefits of formulating conditioning and data-dependent coupling concepts in the stochastic interpolants framework?
2. Does this formulation add flexibility compared to [1,2] or [6] which uses both conditioning and data dependent coupling (sec 5.3). (I'm aware [6] is not to be considered as previous work, but I want to understand the superiority of this work over applications already present in other frameworks).

[6] Song et. al., [Equivariant Flow Matching with Hybrid Probability Transport for 3D Molecule Generation](https://openreview.net/pdf?id=hHUZ5V9XFu)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the framework of stochastic interpolants to conditional generation. In particular, one conditions the interpolating density between $x_0$ and $x_1$ with a conditional $\xi$. The $\xi$ can be incorporated in a data dependent and independent way, which allows for applications in conditional generation as well as upsampling/infilling.

### Strengths
* The paper is theoretically sound, as the derivations follow directly from the continuity equation.
* Additionally, some experiments show the method's viability for common image generation tasks.

### Weaknesses
 * I'm not sure the method is that original in practice. In particular, the paper notes that much of the construction can be connected with existing SDE and ODE formulations, all of which depend on the score function ([1] for the straight path ODE that is described in the paper, otherwise the standard OU process). In that case, the conditional methodology would follow from the score function argument as well, implying there would be little difference on the empirical side with existing methodologies. However, the proposed framework does generalize beyond this to other base distributions (for example), so I would expect (or rather, like to see) more empirical emphasis to be placed on this setting.
* In a similar vein, for the inpainting experiments, there is a big issue in that existing score based methods (e.g. ScoreSDE) can inpaint (up to some approximation error + some necessary hacks) without having to retrain, while the current results come about through retraining.
* The experiments don't give me that much confidence. In particular, the results are entirely qualitative (meaning they can be easily cherrypicked). For the upsampling experiments, I want to see some numerical comparisons against the standard cascaded diffusion models setup (eg generate 64x64 and upscale to 256x256 to compare FIDs).

### Questions
Nothing beyond addressing the weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces couplings between the prior and the target distribution in order to do (conditional) generative modelling. Here, plenty of former generative modelling frameworks are generalized. First the authors introduce a stochastic interpolant with coupling, then it is shown that the density satisfies the transport equation and a loss is derived. Furthermore, in the style of diffusion forward and reverse SDEs are introduced. Then this approach is applied to (class) conditional sampling for instance image superresolution and inpainting.

### Strengths
The idea is very neat and the theory seems well-executed. Qualitatively the experiments look really nice. Furthermore, the approach presents a nice unifying framework for many papers attempting to handcraft the couplings.

### Weaknesses
1) The biggest glaring weakness is the lack of quantitative experiments. While I am a huge fan of the idea and the developed theory, I think quantitative experimental evaluation is necessary for acceptance. An appropriate baseline could be the OT coupling flow from Tong et al.  

2) In the proof of Theorem 1, I do not fully understand one step. In equation (23) for the second equality apparently the definition of conditional expectation is used. Please clarify this via some additional justification and the definition of conditional expectation. You kinda have to use that the expected value only depends on (the time derivative) of the stochastic coupling. 

3) Is there any intuitive interpretation for the losses like in the diffusion case? 

4) It would be nice to see failure cases of  joint learning of time coefficients and score. Since one simultaneously learns the time coefficients $\alpha$, $\beta$ .. and the $g$ I am expecting some not so nice local minima when one is not careful with initializing. Did you encounter any of those? Why didnt you use it in the inpainting/superres experiments and decided to fix $\alpha$ and $\beta$?

5) In the paper it is discussed, that one needs $\sigma>0$ in the superresolution experiment. If not one would try to establish a normalizing flow between a lower and a higher dimensional manifold. However when one thinks about the inpainting example filling all the boxes with random (Gaussian) noise could lead to an overestimation of the dimension of the target data, therefore prohibiting "a true transport equation" to hold as this defines a normalizing flow. 

6) Is it possible to derive the losses from the forward/reverse SDEs so one does not necessarily enforce invertibility?

7) A small nitpick: I think the formulation "reverse" SDE is more appropriate since backward has a different meaning in the probability theory context.

### Questions
See weaknesses. Overall I appreciate the idea, but imo the following three things would greatly strengthen the paper: some quantitative evaluation, some discussion on the "invertibility" constraints and showing that learning of the schedules $\alpha,...$ also works in these image examples.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
