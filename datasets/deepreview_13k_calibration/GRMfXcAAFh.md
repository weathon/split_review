# Oscillatory State-Space Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We propose Linear Oscillatory State-Space models (LinOSS) for efficiently learning on long sequences. Inspired by cortical dynamics of biological neural networks, we base our proposed LinOSS model on a system of forced harmonic oscillators. A stable discretization, integrated over time using fast associative parallel scans, yields the proposed state-space model. We prove that LinOSS produces stable dynamics only requiring nonnegative diagonal state matrix. This is in stark contrast to many previous state-space models relying heavily on restrictive parameterizations. Moreover, we rigorously show that LinOSS is universal, i.e., it can approximate any continuous and causal operator mapping between time-varying functions, to desired accuracy. In addition, we show that an implicit-explicit discretization of LinOSS perfectly conserves the symmetry of time reversibility of the underlying dynamics. Together, these properties enable efficient modeling of long-range interactions, while ensuring stable and accurate long-horizon forecasting. Finally, our empirical results, spanning a wide range of time-series tasks from mid-range to very long-range classification and regression, as well as long-horizon forecasting, demonstrate that our proposed LinOSS model consistently outperforms state-of-the-art sequence models. Notably, LinOSS outperforms Mamba by nearly 2x and LRU by 2.5x on a sequence modeling task with sequences of length 50k.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a new continuous time recurrent network in the family of state space models. The architecture is proposed as an ODE that is discretized in two ways using first order implicit and implicit-explicit integrators. The terms of the ODE are further constrained to induce two different computational tricks to speed up computation; fast matrix inversion to make the implicit methods tractable, and parallel scans for faster sequence processing. The LinOSS architecture is empirically compared to other Neural ODEs and state-space models, and to transformers, on three different time domain problems for time series classification and prediction.

### Strengths
The paper demonstrates a cross cutting expertise from dynamical systems analysis through implementation optimization. The design of the ODE is crafting three advantages at three different levels of abstraction simultaneously: enforce theoretically proven stabilization, allow for efficient matrix inversion, and allow for parallel scans of the sequence recurrence. The experiments on time series problems are a good set of problems, and the results of LinOSS stand out against the broad set of comparisons. The proofs are sound, however, it is not clear if they apply to what actually is going on: see below.

### Weaknesses
One issue with the paper is highlighted in the core claim of pre hoc controlling for “forgetting” versus stability by choosing between LinOSS-IM and IMEX (Line 298).  Line 205 claims to demonstrate different advantages between the two methods, but this is not actually evident in the experiments. What characteristics of the problems in Table 1 lead to IM vs. IMEX performing differently? If anything, there is no difference between IM and IMEX in all examples but Worms. Is there something special about Worms, or is it a fluke? The result of Table 2 seems to contradict the claim that IMEX is better at long ranges and IM is better at forgetting: why does IM perform better on a problem where memory over a long sequence should be important?

It is odd to rely on the integrator choice to enforce stability vs. forgetting. Using an ODE framework, it would seem more natural to change the ODE with dissipative terms, for example, instead of changing the integrator. By relying on the integrator choice, it is unclear if those properties would actually hold after training, if the discretization is thought to add new properties that the ODE did not have. Given the unclear results of the experiments, is it possible that results of the theoretical analysis do not apply after the model is trained? Did you try inspecting if the parameters of A and S still hold the assumptions / initializations assumed in Section 3, after training?

Consider the case where the system being learned is actually stable, but the backward euler IM formula is applied. Backward Euler is dissipative even when the dynamical system does not want to dissipate. What happens when you try to learn a model that should be energy conserving using  the LinOSS-IM architecture? The authors could try this by just trying to learn to forecast a simple oscillatory system with LinOSS-IM. I would expect that the model would learn “through” the IM discretization, and converge to an parameterization of an “unstable” ODE that is stable after being discretized by IM. See Krishnapriyan, “Learning continuous models for continuous physics” for a discussion on overfitting on learning through ODE discretizations. 

One idea to start to tackle this problem: Try LinOSS-FE “forward euler”. The architecture would be similar and the tricks in parallel scans would still work. This would be an ablation that would illustrate why stabilization of the implicit and imex integrators is important. If there is no performance difference with the Forward euler discretization in the experiments, or if the IM method can forecast a stable system, then perhaps the theoretical results do not represent what actually happens after training.

- What are the runtimes of the different methods in the experiments? While the accuracy metrics are strong, one of the purported examples of SSMs is the efficiency. What are run times when enabling and disabling different introduced optimizations:
  - Run time when not using the equation for matrix inversion?
  - Run time when not using the parallel scan?
- Line 74: Why is A diagonal? Is it only to induce the matrix inversion trick later?
- Some aspects of the architecture are unclear. How exactly are the LinOSS layers stacked into each other and within the network?
  - In Figure 1, which parts of  the figure are u, y, z?
  - What effect do the nonlinearities have on the stability analysis?
  - How is the nonlinear layer in the figure a part of the model?
- In the experiments in Section 4, what are the exact hyperparameters and model graphs?
- The exploitation of Formula 3 to speed up the matrix is clever. How does this differentiate during training, though? Did you pass this formula through autodiff, or define a special differentiation rule?
- Does the parallel scans apply to only using first-order IM or IMEX integrators? Or does the ODE formula in general allow for the parallel scans with other integrators, such as a simple forward Euler, or a higher order IMEX?
- Table 1: s/UAE/UEA/g.
- Table 1: What does UEA stand for? Define abbreviations and add citations. (Is Walker 2024 supposed to be the citation?)
- Color highlighting in the tables is not colorblind friendly, nor BW printer/ereader friendly. Use symbols instead.
- Equation 7: Why is it important that equation 2 is a Hamiltonian system in this section? If the underlying ODE is indeed Hamiltonian, doesn’t that suggest that the IM discretization is not appropriate?
- Line 222: What are a, b supposed to be? Describe the specific case of operator & tuple shown here.
- Line 280: Why is it possible to assume that A_kk>0? Couldn’t they diverge from that assumption during training? What initialization is required?
- Line 289: s/constraint/constrained/
- Line 292: The steps in the proof are not obvious. More steps of proof should be presented. In the appendix would be sufficient.
- Just a remark: The title of section 4.2 is overly extravagant for the claims. These days, “extreme long ranges” would be context lengths of millions of tokens :)
- Appendix A: What are the parameter counts? What is the architecture of the “nonlinear layers”? What are the hyperparameters for the forecasting problem?
- Why does the PPG model have higher memory demands, when the models actually seem small?
- Appendix A: What ML library was used?
- Could you describe the loss functions and the complete architecture for the 3 different types of problems? How is time series classification grafted onto the LinOSS network?
- The importance of section 3.2 is unclear to me. It is nice to prove universality of a model, but what is special about LinOSS that other more general proofs of universality would not apply? I would not have questioned it. Is any aspect of the proof specific to LinOSS, or could it apply more broadly to more SSMs?

### Questions
- What are the runtimes of the different methods in the experiments? While the accuracy metrics are strong, one of the purported examples of SSMs is the efficiency. What are run times when enabling and disabling different introduced optimizations:
  - Run time when not using the equation for matrix inversion?
  - Run time when not using the parallel scan?
- Line 74: Why is A diagonal? Is it only to induce the matrix inversion trick later?
- Some aspects of the architecture are unclear. How exactly are the LinOSS layers stacked into each other and within the network? 
  - In Figure 1, which parts of  the figure are u, y, z?
  - What effect do the nonlinearities have on the stability analysis?
  - How is the nonlinear layer in the figure a part of the model?
- In the experiments in Section 4, what are the exact hyperparameters and model graphs?
- The exploitation of Formula 3 to speed up the matrix is clever. How does this differentiate during training, though? Did you pass this formula through autodiff, or define a special differentiation rule?
- Does the parallel scans apply to only using first-order IM or IMEX integrators? Or does the ODE formula in general allow for the parallel scans with other integrators, such as a simple forward Euler, or a higher order IMEX?
- Table 1: s/UAE/UEA/g.
- Table 1: What does UEA stand for? Define abbreviations and add citations. (Is Walker 2024 supposed to be the citation?)
- Color highlighting in the tables is not colorblind friendly, nor BW printer/ereader friendly. Use symbols instead.
- Equation 7: Why is it important that equation 2 is a Hamiltonian system in this section? If the underlying ODE is indeed Hamiltonian, doesn’t that suggest that the IM discretization is not appropriate?
- Line 222: What are a, b supposed to be? Describe the specific case of operator & tuple shown here.
- Line 280: Why is it possible to assume that A_kk>0? Couldn’t they diverge from that assumption during training? What initialization is required?
- Line 289: s/constraint/constrained/
- Line 292: The steps in the proof are not obvious. More steps of proof should be presented. In the appendix would be sufficient.
- Just a remark: The title of section 4.2 is overly extravagant for the claims. These days, “extreme long ranges” would be context lengths of millions of tokens :)
- Appendix A: What are the parameter counts? What is the architecture of the “nonlinear layers”? What are the hyperparameters for the forecasting problem?
- Why does the PPG model have higher memory demands, when the models actually seem small?
- Appendix A: What ML library was used?
- Could you describe the loss functions and the complete architecture for the 3 different types of problems? How is time series classification grafted onto the LinOSS network?
- The importance of section 3.2 is unclear to me. It is nice to prove universality of a model, but what is special about LinOSS that other more general proofs of universality would not apply? I would not have questioned it. Is any aspect of the proof specific to LinOSS, or could it apply more broadly to more SSMs?

### Soundness
3

### Presentation
4

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
The paper provides a novel state-space model. They have two different versions of it, in which they rigorously show the power of their algorithms and also experimentally verify it. The method outperforms SOTA methods in many tasks.

### Strengths
Provides strong theoretical together with intuitive explanations.
Contrasts their two proposed methods mathematically and also experimentally.
The experimental results are excellent and definitely contributes to the field significantly.
Supplementary material is comprehensive.

### Weaknesses
I think section 3.2 can be written more accessible.

I believe Figure 1 is very important but can be made more explanatory.

To the best of my understanding, the model cannot produce chaotic dynamics. What if the task in hand requires this? How does this contrast (if there is a contrast) with section 3.2?

### Questions
To the best of my understanding, the model cannot produce chaotic dynamics. What if the task in hand requires this? How does this contrast (if there is a contrast) with section 3.2?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Linear Oscillatory State-Space models (LinOSS), a novel approach to sequence modeling based on forced harmonic oscillators. The model comes in two variants: LinOSS-IM (implicit) and LinOSS-IMEX (implicit-explicit). The key innovation is using second-order ODEs with diagonal state matrices, offering stable dynamics while only requiring non-negative diagonal elements. The paper provides theoretical guarantees for stability and universal approximation, along with empirical validation showing significant improvements over state-of-the-art models like Mamba and LRU on long sequences.

### Strengths
The paper demonstrates strong theoretical foundations by providing rigorous mathematical analysis of stability conditions, proving universal approximation capability, and establishing clear connections to Hamiltonian systems and symplectic integration. Implementation-wise, it offers a remarkably simple parameterization requiring only non-negative diagonal elements, achieves efficient computation through parallel scans, and presents two complementary variants with different preservation properties. The empirical results are great, showing strong performance on diverse tasks.

### Weaknesses
1. Limited Analysis of Model Interpretability:

While based on oscillatory dynamics, lacks discussion of learned frequencies

No analysis of how the model captures different timescales

2. Experiment:

No ablation studies on the impact of different initialization schemes

The implementation details are unclear. For instance, how does it compare to Mamba or S5 in terms of speed, training time, FLOPs, and memory usage? Discussing these aspects could enhance its practical utility.

### Questions
1. Could the model be extended to incorporate coupled oscillations while maintaining stability guarantees?

2. What is the impact of the time step parameter Δt on model performance and stability?

3. How does the choice between IM and IMEX variants affect training dynamics and convergence?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors propose a state-space model (SSM) architecture, Linear-Oscillatory SSM, derived from the discretization of second-order linear ODEs that models a network of forced harmonic oscillators. They develop two discretization schemes for the approach, study the stability properties of the parametrization and show universal approximation of LinOSS for approximating general continuous, causal input-output mapping. Through empirical evaluations, they demonstrate that their approach outperforms other Linear SSMs on time series classification, prediction and long-horizon forecasting.

### Strengths
The work is well motivated and the writing is clear and concise. The recurrence matrix afforded by the proposed approach has desirable stability properties and is less constrained compared to the typical SSM parametrizations. The expressivity is further supported by the theoretical analysis on universality of the proposed parametrization. The experimental results are thorough and demonstrate the efficacy of the proposed approach relative to baselines.

### Weaknesses
Given that the parametrization has been introduced in Rusch & Mishra (2021) and the universality results for the non-linear counterpart to this work have been shown in Lanthaler et al., 2024, the novelty of this work is somewhat limited. Still, I think that this is a useful contribution overall as it improves the ability of SSMs for learning long-range dependencies.

Given the independent nature of the oscillators, it is unclear how the proposed architecture can model more complex temporal dynamics such as transient synchronization or desynchronization. While the linear formulation allows for theoretical analysis, it might also limit the model's ability to capture non-linear interactions present in real-world time series. Furthermore, the stability analysis relies on the assumption that the matrix $M$ is diagonalizable. While the authors acknowledge that non-diagonalizable matrices with real eigenvalues might not lead to exponential instability, the practical implications of such cases are not fully explored, especially in the context of numerical stability during training.

### Questions
* L116-118. Since the oscillators are independent, can the proposed architecture model transient synchronization/desynchronization?
* L250. `Assuming M is diagonalizable [...]`. If $M$ has real eigenvalues with algebraic multiplicity $ > 1$, would that make the system unstable? Admittedly, norm growth would be sub-exponential, so perhaps in practice it's fine.
* L289 `constraint` $=>$ constrained

### Soundness
3

### Presentation
3

### Contribution
2
