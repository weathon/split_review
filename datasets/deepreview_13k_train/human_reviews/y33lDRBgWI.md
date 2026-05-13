# AdjointDPM: Adjoint Sensitivity Method for Gradient Backpropagation of Diffusion Probabilistic Models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
This paper considers a ubiquitous problem underlying several applications of DPMs, \ie, 
optimizing the parameters of DPMs when the objective is a differentiable metric defined on the generated contents. 
Since the sampling procedure of DPMs involves recursive calls to the denoising UNet, na\"ive gradient backpropagation requires storing the intermediate states of all iterations, resulting in extremely high memory consumption. 
To overcome this issue, we propose a novel method AdjointDPM, which first generates new samples from diffusion models by solving the corresponding probability-flow ODEs. It then uses the adjoint sensitivity method to backpropagate the gradients of the loss to the models' parameters (including conditioning signals, network weights, and initial noises) by solving another augmented ODE. 
To reduce numerical errors in both the forward generation and gradient backpropagation processes, we further reparameterize the probability-flow ODE and augmented ODE as simple non-stiff ODEs using exponential integration. 
AdjointDPM can effectively compute the gradients of all types of parameters in DPMs, including the network weights, conditioning text prompts, and noisy states.
Finally, we demonstrate the effectiveness of AdjointDPM on several interesting tasks: guided generation via modifying sampling trajectories, finetuning DPM weights for stylization, and converting visual effects into text embeddings.git}
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an interesting idea, named AdjointDPM, merging Diffusion Models and techniques from Neural ODE literature. The core offering of the paper is a way of backpropagating gradients of any loss computed using the output of a (trained) Diffusion model. Specifically the authors used the well-known Adjoint Backpropagation method from Neural ODE, which is a backprop algorithm with $\mathcal{O}(1)$ memory w.r.t the *discretization* of the ODE solver.

The authors applied their AdjointDPM method on three tasks that either require gradients w.r.t initial state $X_T$ of the reverse process, all intermediate states $\\{ X_t \\}\_{t=1}^T$ of the reverse process or the parameters $\theta$ of denoising model $\epsilon_{\theta}(\cdot)$. They showed good performance in terms of quantitative metrics and also showed qualitative results.

### Strengths
The proposal of the paper is overall good, theoretically sound and shown to have worked well.

- Theoretically, it makes sense to use the Adjoint method on the reverse ODE.
- The authors exploited the semi-linear nature of the ODE even in the Adjoint backprop, following DPM-Solver/DEIS.

### Weaknesses
 - While the proposal is quite novel, one might still argue that it is not really necessary to use Adjoint Backprop. One can very well accomplish the same task by backprop-ing through the solver machinery (maybe by deceasing sampling steps and using better sampler), which of course, won’t be very efficient. So, at the end, it all boils down to compute/memory efficiency. While I understand the memory advantage, sadly, the paper barely talks anything about computational requirements of the method. BTW, Neural ODEs (and Adjoint Backprop) are known to be not very scalable.
- Experiments are okay-ish, but not really extensive. Qualitative samples are lacking in some experiments (e.g. vocabulary expansion). Also Vocabulary Expansion is shown for only two classes.
- No comparison or mention of methods that DO backprop through the ODE solver.

### Questions
I have the following questions for the authors.

- I am confused about section 3.4. That is not AdjointDPM — that is just unconditional generation with an already known sampler (DEIS, which used Adam-Bashforth) that exploits the semi-linear nature. What part of this is your contribution ? Am I missing something here ?
- In the “security auditing” application, what exactly is the guidance $L$ ? What is the meaning of “distance between a harmful prompt and a prediction score” ? Also, what exactly is the NSFW filter $f(\cdot)$ ? Can you provide more details please ?

Minor questions or suggestions:

- The unnumbered eq b/w Eq. 5 & 6 — what is the meaning of that line (”Similarly, for $\theta$, we can regard ..”) ?
- “adjoint state $\mathbf{a}(t) = ..$, which represents how the loss depends on the state ..” → “adjoint state $\mathbf{a}(t)$ = .., which represents how the loss **changes w.r.t the** state ..”.
- The AdjointDPM eq. 8 shows gradient w.r.t $t$ — is it acutally used anywhere ?
- Why is it called “vocabulary expansion” ? I still don’t get it.
- “Security Auditing” is just fancy name for Adversarial Samples ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work leverages the adjoint methods for optimizing the parameters and/or samples of diffusion ODEs under a given differentiable scalar-valued function. To efficiently solve the adjoint ODE, this work also leverages the expoenential integrators and introduce a change-of-variable formula to obtain a simpler ODE. Experiments show that the proposed method can be used for classifier-based sampling, adversarial sampling and stylization with a single reference.

### Strengths
- The proposed method is easy to understand and the writing is clean and easy to follow.
- The proposed adjoint method is novel to the diffusion model community and the combination with exponential integrator is useful.
- The studied topic is important to the field.

### Weaknesses
 - Major:

  - The proposed method seems to be quite **inefficient** because it needs to optimize the model / sample at each specific task, while other guided sampling methods (e.g., classifier guidance or classifier-free guidance) do not. Note that the optimization procedure needs to solve the whole ODE at each training step, the training cost (i.e., total training time) seems to be quite expensive. This inefficiency is a significant concern, especially when compared to methods that amortize the guidance process across multiple samples or tasks. The need to solve the full ODE for each optimization step implies a high computational overhead, potentially limiting the practical applicability of the approach.

  - The proposed method cannot guarantee the property of diffusion models, i.e., the noise-pred network corresponds to the score functions, because it directly train the neural ODE. Thus, it may be hard to leverage the other properties of diffusion models, such as classifier / classifier-free guidance, and it may be hard to further use diffusion SDEs for better sample quality. Instead, other guided sampling methods introduce another guidance model at each time step, which is based on the score functions and thus can maintain the diffusion property. This deviation from the score-matching objective could lead to instability or reduced sample quality, and it limits the ability to directly leverage existing techniques developed for diffusion models.

- Minor:

  - Equation(9) is exactly the EDM sampler so it is not a new method. It should be compared and discussed in detail.

[1] Tero Karras, Miika Aittala, Timo Aila, and Samuli Laine. Elucidating the design space of diffusion-based generative models. 

### Questions
1. What is the training time for each experiment?

2. After training, can the model be used for classifier / classifier-free guidance and diffusion SDEs?

==========

Thanks for the detailed reply! After reading the authors' rebuttal, I raised my score to 6.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper...
- proposes AdjointDPM for differentiating through the diffusion sampling process,
- reparametrizes PF ODE and augmented ODE to reduce numerical errors,
- applies AdjointDPM to a wide variety of tasks, such as vocabulary expansion, security auditing, stylization, etc.

### Strengths
- The paper is well-written and easy to follow.
- This paper is a nice application of adjoint sensitivity methods to diffusion models. To the best of my knowledge, such application of adjoint sensitivity methods has not been explored before.
- The proposed method can potentially be applied to a wide variety of downstream tasks for diffusion models.

### Weaknesses
I must clarify that I am not very familiar with application of diffusion models to tasks such as vocabulary expansion, security auditing, etc. Hence, I am not sure whether the authors have chosen an appropriate and comprehensive set of baselines, or have followed proper evaluation protocol. So, my current score for this paper is "marginally above the acceptance threshold", and I will adjust my score based on other reviews and authors' reply to my concerns.

- NFE and wall-clock time for AdjointDPM and the baselines is missing, so it is difficult to gauge the efficiency of AdjointDPM.
- A background section explaining and comparing other related backpropagation methods, such as DOODLE, FlowGrad, DEQ_DDIM in detail would help readers understand the position of AdjointDPM w.r.t. previous work. Specifically, this paper lacks a discussion of theoretical and practical advantages/disadvantages of AdjointDPM w.r.t previous work on backpropagation through diffusion sampling. For instance, the authors state DEQ-DDIM require the diffusion sampling process to have equilibrium points -- is this a significant drawback? Are there certain tasks where this equilibrium assumption do not hold, so AdjointDPM is applicable while DEQ-DDIM is not?

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
