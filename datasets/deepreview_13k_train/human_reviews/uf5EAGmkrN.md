# Dynamical versus Bayesian Phase Transitions in a Toy Model of Superposition

- Decision: Reject
- Scores: 8, 6, 5, 3

## Abstract
We investigate phase transitions in a Toy Model of Superposition (TMS) \citep{elhage2022superposition} using Singular Learning Theory (SLT). We derive a closed formula for the theoretical loss and, in the case of two hidden dimensions, discover that regular $k$-gons are critical points. We present supporting theory indicating that the local learning coefficient (a geometric invariant) of these $k$-gons determines phase transitions in the Bayesian posterior as a function of training sample size. We then show empirically that the same $k$-gon critical points also determine the behavior of SGD training. The picture that emerges adds evidence to the conjecture that the SGD learning trajectory is subject to a sequential learning mechanism. Specifically, we find that the learning process in TMS, be it through SGD or Bayesian learning, can be characterized by a journey through parameter space from regions of high loss and low complexity to regions of low loss and high complexity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work analyses the empirically observed phenomenon that, during stochastic-gradient-decent (SGD) based training of neural networks, there appear to be "phase transitions" in which the loss suddenly drops rapidly in between longer "plateaus" of relatively constant loss; and that these phase transitions typically go from parameter-space regions of lower complexity and lower loss to regions of higher complexity and higher loss. To characterise this phenomenon, the authors focus on a simple but analytically tractable model.

Specifically, for certain numbers of hidden and feature dimensions in this model, they classify the critical points in the parameter space. They then characterise Bayesian phase transitions in this model as training sample sizes at which the much of the posterior probability mass shifts from one region to another. Finally, they verify that critical points with lower loss are typically associated with higher weight-configuration complexity. Taken together, these findings lead the authors to conjecture that "phase transitions" observed in SGD training have underlying them a Bayesian phase transition.

### Strengths
**Originality**
To my knowledge the main results in this work are novel. As a side note: I am not familiar with the literature in this area. In particular, especially in the characterisation of Bayesian phase transitions in Section, it is hard for me to tell which results are novel and which are due to the various works of Sumio Watanabe. However, even if this characterisation is largely based on existing work, I would still argue that the work is sufficiently novel for publication in ICLR.

**Quality**
I also believe that this work is rigorous enough for publication in ICLR;  

**Clarity**
I think the writing and presentation is overall reasonably clear. But please see some suggestions for improvement in the "weaknesses" below.

**Significance**
This work sheds some much needed light on the phase transitions observed in SGD training (at least in a simple, tractable scenario).

### Weaknesses
To make this work more self contained, it would be good to explain/define concepts from Singular Learning Theory at the beginning. In particular, I really missed a clear definition of the "local learning coefficient" which is central to this work, and therefore found this work quite difficult to read without going through [1] first which gives a definition of this concept. 

Additionally, the fact that the guide for understanding some aspects of, e.g., Figure 1 is only found in Appendix B (rather than the main paper) is not optimal.

### Questions
Do you have any intuition about whether/how the dynamic phase transitions would be affected if we used an optimiser with momentum instead of SGD?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
If I understand well, they characterize some critical points of the likelihood function for the TMS in the high sparsity limit. They then use SLT to get approximate theoretical predictions on the phase transitions (for the sample size $n$ large enough) that the Bayesian posterior undergoes when $n$ increases. They confirm these predictions experimentally (Figure 2).

Then it is stated that the phase transition of the Bayesian posterior is a good indicator of the dynamical transitions (the Bayesian Antecedent Hypothesis)

### Strengths
The ideas are interesting and lead to intriguing experimental results. The paper seems to introduce novel findings on TMS in the high sparsity limit through the characterization of critical points.

### Weaknesses
The paper contains a lot of information and there seems to be a lot of prerequisites for understanding it. It is also difficult to get an idea of the context. It would have been nice to have more context on why this problem (TMS) matters and what is already known about its critical points.

The theoretical results could be made more formal; for example, the authors emphasize that applying SLT in Section 4.1 is a strong point of the paper compared to the usual use of the Laplace approximation for example in (Wei et al., 2022b; Lau et al., 2023). However, the paper does not discuss whether the assumptions of SLT hold in their setting. Specifically, the conditions for the validity of the SLT, such as the existence of a limiting distribution and the convergence of moments, are not explicitly verified for the likelihood function in the high sparsity regime. This is a significant gap, as the asymptotic behavior of the likelihood is crucial for the theoretical claims.

I would also find very interesting to have a theoretical discussion of the Bayesian Antecedent Hypothesis. The paper presents it as a hypothesis with empirical support, but a deeper theoretical justification is lacking. The connection between the phase transitions in the Bayesian posterior and the dynamical transitions observed in training requires more rigorous explanation.

### Questions
Is it true that the conditions of (Watanabe, 2009) hold for the local free energy formula (9) for the Gaussian prior considered in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates phase transitions in a Toy Model of Superposition using both dynamical and Bayesian methods. It uncovers critical points in the form of regular k-gons and demonstrates their impact on learning processes. The findings support the idea of a sequential learning mechanism in Stochastic Gradient Descent. The study enhances our understanding of phase transitions in deep learning.

### Strengths
The paper demonstrates originality by focusing on the analysis of phase transitions in a small-scale learning task. This approach offers a fresh perspective on learning processes, especially in a Toy Model of Superposition (TMS). The study takes an innovative angle by investigating the role of critical points and sequential learning mechanisms in understanding phase transitions.

### Weaknesses
One significant weakness is the limited exploration of how the results obtained from this small-scale learning task can be applied to larger-scale and more practical problems. The paper does not clearly articulate how the insights gained from this Toy Model of Superposition (TMS) could be extended to real-world, complex learning scenarios. Providing a bridge between the toy model and practical applications is essential for enhancing the paper's impact.

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper examines a simple auto-encoder model with just two hidden units, applied to extremely sparse data where only one element of the input vector is non-zero. The primary contribution lies in providing a complete analytical characterisation of the critical points of the population loss in this specific setup. This characterization is then leveraged to make arguments about the existence of distinct phases within the model's behavior as a function of the number of samples available. Furthermore, it serves as a guide for exploring the transitions between these different phases during the model's dynamics.

### Strengths
While the model under consideration has already been proposed in Elhage et al., 2022, the authors present a complete, explicit and exact characterisation of the critical points of the population loss, which is in quite rare. This is then used to compute a rough approximation of the free energy of the network near the critical points in order to give some qualitative indication on the phase of the model under study.

### Weaknesses
The presentation in this paper is extremely ineffective. The classification of critical points is crucial to understanding the paper, yet a complete and accurate description is relegated to the appendix. Similarly, there are many k-gon diagrams in the main text with no direct explanation on how to read them. I believe the paper would be much easier to read with a compact set of definitions clearly stated in the main text.

While I personally believe that studying simple models can be interesting, I struggle to see any practical interest in studying the model the authors propose, and I am not sure how feasible it can be to relax the many underlying assumptions: having more than 2 hidden units makes the structure of the critical points significantly more complicated, and changing the data model would make the whole theory collapse.

Even accepting all the limitations above, I don't think the authors provide an adequate quantitative study of the phase transitions of this model beyond some general remarks. I would argue that the analytical results on the loss play no role in the discussion of the dynamical transition picture, as the energy levels could have been identified from the experiments, and knowing the exact values has no importance in what is presented.

### Questions
1) Would it be possible to also study analytically whether the critical points are (local) minima? This is particularly interesting for energy levels $4^{+,3-}$, $4^{2+,3-}$, $4^{+,2-}$, $4^{2+,2-}$, $4^{+,-}$, $4^{2+,-}$, $4^{2+}$ in Figure 3, as it seems there are no plateaus associated to those levels.

2) In section 4.1 you define a transition as the number of samples for which the phase changes. The simulation in Figure 2 seems to suggest that there is also a number of samples for which a certain phase has proportion zero. Is it the case? If so can you characterise it?

3) In Figure 3 it would seem you are doing up to 1/4 million SGD steps. Is it a typo?

3) Also in Figure 3, I would expect that for large enough times SGD escapes the plateaus and jumps to a lower energy level. I think there is already an example of this in line 5 of the right panel. Is it possible to characterise this phenomenon?

4) What would Figure 3 look like if SGD was randomly initialised?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
