# Unlocking Guidance for Discrete State-Space Diffusion and Flow Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Generative models on discrete state-spaces have a wide range of potential applications, particularly in the domain of natural sciences. In continuous state-spaces, controllable and flexible generation of samples with desired properties has been realized using \emph{guidance} on diffusion and flow models. However, these guidance approaches are not readily amenable to discrete state-space models. Consequently, we introduce a general and principled method for applying guidance on such models. Our method depends on leveraging continuous-time Markov processes on discrete state-spaces, which unlocks computational tractability for sampling from a desired guided distribution. We demonstrate the utility of our approach, \emph{\ourmethod}, on a range of applications including guided generation of small-molecules, DNA sequences and protein sequences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author introduces a guidance framework for discrete generation models. This approach relies on utilizing continuous-time Markov processes over discrete state Spaces, which frees up the computationally processability of sampling from the desired lead distribution. More importantly, the authors demonstrate the effects of the proposed discrete guidance framework on a range of applications, including guided generation of small molecules, DNA sequences, and protein sequences.

### Strengths
The authors of this paper propose a guidance framework for generating models (diffusion models, flow matching models) on discrete state Spaces. This guidance strategy is applicable to a wide range of generation models of discrete state Spaces achieved through CTMC, and has been applied to the generation of guidance conditions in many fields such as small molecules, DNA sequences, and protein sequences. In addition, this paper has a reasonable logical structure and clear expression.

### Weaknesses
While the authors have demonstrated that this guiding framework is empirically effective, more precise theoretical guarantees, such as error analysis, are lacking, and further research into potential tradeoffs between efficiency and accuracy will be of interest to the community. Specifically, the paper lacks a detailed analysis of the error introduced by the numerical integration of the continuous-time Markov chain (CTMC) and the approximation error from the trained time-dependent predictors. It is unclear how these errors propagate and affect the quality of the generated samples. In addition, the article is more inclined to show the effect of guidance and ignore the quality of generation, so it is difficult for readers to judge the practicality of this guidance framework. For instance, while the authors demonstrate the ability to generate molecules with specific properties, there is no clear benchmark comparison to existing methods, making it difficult to assess the practical utility of the approach. Finally, judging from the process of theoretical derivation, the technical route of this work seems to be weak in innovation. The core idea of applying guidance in the continuous-time limit, while effective, appears to be a straightforward extension of existing techniques in continuous state spaces to discrete state spaces, without introducing significant novel theoretical insights.

### Questions
The authors mention that the proposed framework is suitable for a wide range of generation models implemented through  the CTMC, but this guidance framework is only applied to diffusion models and flow matching models. Can you elaborate on how to apply the framework to other generation models?

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
This paper presents a technique for guiding the generation of samples from discrete state-space diffusion models. The motivation behind this approach is the guidance mechanism employed in continuous state-space diffusion models. The authors derive the explicit form of both the predictor-guided and predictor-free-guided rate matrices for the discrete diffusion model. Subsequently, they propose a Taylor-approximated guidance as a computationally efficient solution. The effectiveness of the proposed method is demonstrated through its application to various applications, including the guided generation of small molecules, DNA sequences, and protein sequences.

### Strengths
- The paper proposes a general method for applying guidance on discrete state-space diffusion models, which constitutes a novel contribution to the field.
The authors provide a comprehensive derivation of the predictor-guided and predictor-free-guided rate matrices for the discrete diffusion model, accompanied by intuitive explanations of how they compare with the continuous guidance mechanism.
- The proposed method is demonstrated through its successful application to a diverse range of applications, including the guided generation of small molecules, DNA sequences, and protein sequences.

### Weaknesses
 - The paper omits a clear introduction to the forward and backward processes of discrete state-space diffusion models, which is crucial for understanding the subsequent guidance mechanism. Specifically, the paper should detail how the forward process gradually transforms data into noise and how the backward process reverses this transformation to generate samples. Furthermore, the rationale behind the training of the rate matrix $R_t(x,\tilde x)$ is not explicitly provided. It is essential to explain the objective function used for training this rate matrix and how it relates to the desired diffusion process. I recommend that the authors begin with a more general introduction to discrete state-space diffusion models, followed by a detailed explanation of the guidance mechanism in the continuous case, with a clear comparison between the two, highlighting the similarities and differences in their mathematical formulations and practical implementations.
- Furthermore, it would be beneficial to include more algorithmic details of the training procedures for both the predictor-guided and predictor-free-guided rate matrices. This should include a step-by-step description of the optimization process, the specific loss functions used, and how these are applied to update the model parameters. This information should be provided in addition to the code available in the supplementary material, as the code alone may be less accessible and understandable for readers unfamiliar with the codebase or the specific deep learning framework used. The paper should also clarify how the predictor network is trained in the predictor-guided approach, including the specific training objective and the architecture of the predictor network.
- It is unclear how the predictor-free-guided rate matrix differs from the predictor-guided rate matrix in Equation (4), especially given that it appears to be a direct substitution of the expression from Equation (2). The paper should clarify how the predictor-free guidance achieves its objective of eliminating the need for a separate classifier-like likelihood $p_t(y|x_t)$, as is done in the continuous case. The explanation should clearly articulate how the conditional rate matrix $R_t(x, \tilde{x} | y)$ is trained and how it differs from the rate matrix used in the predictor-guided approach, and how this relates to the removal of the explicit classifier.

### Questions
- It is unclear how the predictor-free-guided rate matrix differs from the predictor-guided rate matrix in Equation (4), which is simply substituting the original expression of the predictor-guided rate matrix in Equation (2) into Equation (4). To the best of my understanding, the classifier-free guidance in the continuous case eliminates the classifier-like likelihood $p_t(y|x_t)$ from the score function, but it needs to be evident how the predictor-free-guidance in the discrete case accomplishes the same objective Could the authors provide further clarification on this matter?
- Could you elaborate on how the Taylor-approximated guidance operates in practice? Is it that instead of $p^\phi(y|x,t)$, we only store $\nabla_x \log p^\phi(y|x,t)$? What if there is no discernible order of the discrete states? How can we embed the discrete states into a continuous space for the Taylor approximation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a methodology to apply conditional guidance to generative models that are discrete and based on Continuous-time Markov Chains.
When assuming single state transitions in the Markov chain, Discrete Guidance is shown to be tractable since it does not necessitate to sum over all the chain states but only on the sparse set of reachable states.
Besides, a heuristic acceleration called Taylor-approximated guidance is propose to further limit the number of neural evaluations.
Three different examples are presented demonstrating the feasibility and efficiency of the approach and present comparison with competitive methods.

### Strengths
The paper introduces a principle mechanism for guidance in a discrete state flow-based generative model.

Experiments demonstrate the feasibility of the approach in three different settings (and small images Appendix F.1).

Reproducibility is ensured by providing source code.

Overall I find that the paper is too dense for the ICLR format and would benefit from a more in depth review. Yet the approach is certainly of interest for the community.

### Weaknesses
The term coined "discrete guidance" seems too general since there is already another competing approach called DiGress (Vignac et al. ICLR 2023) and also Dirichlet FM, sometimes with similar performance
(eg 423 "As predictor-free guidance for DirFM-CFG and DG-PFG behaved comparably (Appendix F.3.5)")
In that respect, the empirical results being relatively close to DiGress, the title of the paper is also a bit problematic  in my opinion.

The mathematical presentation in the main paper is a too quick summary in my opinion.
Equation (3) is only valid for tilde x different than x, and flow conservation is used for setting R gamma(x,x) (Equation 25). This should be included in the main text.
I read Appendix C and was a bit confused by the presentation.
At first I was surprised with key differences: In Equation (14) the numerator depends on both x tilde and x while in Equations (2) and (3) it only depends on the state x tilde. The simplification is discussed later in Section C.6, but I would have like to read this just below Equation (14).

216: The text suggests gamma is between 0 and 1, but it is used with very high values (2, 10, 100) later on. I would suggests to discuss the range of gamma right away.

In the experiments, the value of gamma used for each experiment is not reported clearly.

The presentation of the experiments is also very dense.
Somehow the conditioning mechanisms are not very clear.
One practical issue with classifier and/or classifier-free guidance is the need to eihter train a classifier on noisy data or to train a conditional generative model.
Here the effort needed for retraining is not clear, eg
419 For Discrete Guidance, we trained an unconditional flow-matching model, then used predictor guidance with either exact (DG-Exact) or Taylor-approximated guidance (DG-TAG).
How was the predictor trained ? Is there any example that is training-free ? (see question below)


Minor corrections / suggestions:
109 The text suggests that the gradient of the predictor is easily accessible of continuous DM but this is not the case and based on heuristics (eg using a classifier or assuming a Gaussian form for the distribution).
140 Why "However" ?
145 Say right away that the rate function is positive but can take negative value when x tilde equals x. Also precise the meaning of the Kroenecker delta symbol.
214: This footnote is already useful for p. 3
412: *an* conditional flow-matching model
897 Cl’ement Vignac (accent issue)

### Questions
"Originally, for DirFM-CG we used the same guidance strengths γ ∈ {1, 3, 6, 10, 20} reported by Stark et al. (2024)." Why use the same guidance ? Is the formalism similar ?

There exists training-free guidance strategies for solving imaging inverse problems using diffusion models, eg:

Diffusion Posterior Sampling for General Noisy Inverse Problems
Hyungjin Chung, Jeongsol Kim, Michael Thompson Mccann, Marc Louis Klasky, Jong Chul Ye
ICLR 2023

Pseudoinverse-Guided Diffusion Models for Inverse Problems
Jiaming Song, Arash Vahdat, Morteza Mardani, Jan Kautz
ICLR 2023

Are training-free guidance achievable for discrete diffusion/flow models?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a method for guiding diffusion models and flow models on discrete spaces. The method is constructed using continuous time Markov chain models to represent the discrete changes with jumps. A guidance scheme can be constructed by guiding the rate of the time-continuous process. The model is evaluated with experiments on small molecules, DNA and protein sequences.

### Strengths
- the paper targets an important and difficult problem
- the use of time continuous processes to enable guidance seems well-founded
- the paper is nicely presented
- the method is evaluated on relevant datasets

### Weaknesses
 - while the method is presented as working for both diffusion and flow models, I believe the experiments are only carried out using flow matching (as stated on line 297)

 - you write that the probability of jumps in two or more dimensions simultaneously is zero. But how does it work in the numerical setting where the continuous time is discretized into finite time intervals, e.g. in the Euler integration? I guess here two dimensions can jump simultaneously. Does this cause problems?
- can you comment more on the issue with diffusion models? (that you only use flow matching in the experiments) Is this a weakness of the model

### Questions
- you write that the probability of jumps in two or more dimensions simultaneously is zero. But how does it work in the numerical setting where the continuous time is discretized into finite time intervals, e.g. in the Euler integration? I guess here two dimensions can jump simultaneously. Does this cause problems?
- can you comment more on the issue with diffusion models? (that you only use flow matching in the experiments) Is this a weakness of the model

### Soundness
3

### Presentation
3

### Contribution
3
