# Provable Convergence Bounds for Hybrid Dynamical Sampling and Optimization

- Decision: Accept
- Scores: 8, 6, 8, 8, 3

## Abstract
Analog dynamical accelerators (DXs) are a growing sub-field in computer architecture research, offering order-of-magnitude gains in power efficiency and latency over traditional digital methods in several machine learning, optimization, and sampling tasks. However, limited-capacity accelerators require hybrid analog/digital algorithms to solve real-world problems, commonly using large-neighborhood local search (LNLS) frameworks. Unlike fully digital algorithms, hybrid LNLS has no non-asymptotic convergence guarantees and no principled hyperparameter selection schemes, particularly limiting cross-device training and inference.


In this work, we provide non-asymptotic convergence guarantees for hybrid LNLS by reducing to block Langevin Diffusion (BLD) algorithms.
Adapting tools from classical sampling theory, we prove exponential KL-divergence convergence for randomized and cyclic block selection strategies using ideal DXs. With finite device variation, we provide explicit bounds on the 2-Wasserstein bias in terms of step duration, noise strength, and function parameters. Our BLD model provides a key link between established theory and novel computing platforms, and our theoretical results provide a closed-form expression linking device variation, algorithm hyperparameters, and performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper concerns analysis of hybrid large neighborhood local search (LNLS) frameworks, in which the authors provide non-asymptotic convergence guarantees for this framework. In particular, an exponential non-asymptotic bound is obtained for the KL divergence of DXs employing two different strategies (randomized and cyclic block) and a bias bound on the 2-Wasserstein distance is established for finite device variation. Numerical experiments supporting the theoretical results developed.

### Strengths
This is an interesting paper and I believe the contributions are novel. The authors provide a good literature review and contextualization of their results with respect to the past literature. Moreover, the authors did a good job in identifying the limitations of their work. 

The paper is objective and its contributions are clearly identified.

I did not have time to review all proofs in detail.

### Weaknesses
-I believe that a discussion on the performance differences between Random and Cyclic block approaches would be good for clarification (see questions).


### Questions
- Can the authors provide further examples of distributions that would satisfy the LSI? How realistic is that assumption in applications?

- Random and Cyclic block approaches seem to produce similar outcomes. What is the motivation to choosing one over another? Is there any intuition on which one should I choose based upon my application?

- In Figure 2 (e), why doesn't the curve associated with \delta=0 match the ideal curve?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
I am not engaged in research related to this problem, so I am unable to provide an
objective evaluation on this topic. Please disregard my review comments.

### Strengths
N/A

### Weaknesses
N/A





### Questions
1. In this paper, the authors assume that a vector can be decomposed using tensor products or Kronecker products. However, this decomposition does not span the entire Hilbert space, which implies that the conclusions presented in the paper lack generality.

2. All equations lack punctuation and should be corrected.

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
2

### Summary
Analogue accelerators are attracting renewed interest, promising far superior power efficiency and latency compared to digital methods for problems in machine learning, optimization, and sampling.
While the theoretical understanding of analogue accelerators has evolved quickly, significant gaps remain when taking into account a fundamental practical aspect of those devices:
their limited capacity makes it necessary to solve larger problems "piece-by-piece".
That is, the device operates on a subset of the problem at a time while keeping the rest constant, progressively iterating over the entire problem.

The authors find a rich connection between this constraint and the theory of block Langevin diffusion algorithms.
With the connection to well-established theory, the authors adapt existing methods to obtain novel bounds on the performance of a class of hybrid analogue-digital algorithms and non-asymptotic guarantees for their convergence when accounting for non-ideal devices (which are inevitable in practice).

### Strengths
1. The paper is well-written.
    The exposition is clear with remarkably few typos, the motivation is put clearly, the authors bring and discuss relevant limitations, and they provide some discussion after presenting design choices, results, and new ideas, in general.
    They also highlight key ideas underlying their proofs.

2. The work is decently contextualized.
    The contribution relies significantly on many existing works, which the authors appear to recognize and discuss fairly.

3. The authors are upfront and honest about the limitations of their work.

4. The general topic is interesting and timely.

5. The reduction to block Langevin diffusion seems like a natural (and, thus, promising) approach to the problem.
    I believe it should motivate several follow-up works.
    The approach also yields significantly softer assumptions compared to similar previous results.

6. The results feature valuable properties for practical applications, such as explicit constants, hyperparameter simplification, and the handling of some device variation.

### Weaknesses
1. The care mentioned in strength (1) does not extend to the appendices. E.g., Appendix A would greatly benefit from some discussion about the impact and intuitions behind the choices made for the experiments. For instance, the specific parameter choices for the Gaussian distributions (means, variances), the rationale behind the number of iterations, and the selection of the block sizes are not justified. A discussion of how these choices might affect the observed convergence rates would be valuable. Furthermore, the presentation of the experimental results in the appendices lacks sufficient analysis, making it difficult to fully grasp the implications of the findings.

2. The last sentences of the paragraph 051-059 ask for some substantiation, but the authors offer no references to back them up. The claim that device variation requires retraining or hyperparameter adjustment needs to be supported by evidence or at least a reference to relevant literature. Without this, the assertion appears speculative. Some further discussion could also solve this issue, detailing the specific types of device variations that are most problematic and how they typically manifest in analogue accelerators.

3. Despite strength (2) and my comprehension of the space constraints, I believe the paper relies too heavily on references to explain the concept. I do not see the reliance on previous works as a problem in general, as much of it is a side effect of the strong fruitful connection the authors made with consolidated theory. Still, at points such as Section 4, I felt like essential details were left to be found in the references. For example, the specific details of the Dynamical System (DX) baseline, including its architecture and parameters, are not fully explained, making it difficult to assess the validity of the comparison. The reader is left to infer these details from cited works, which hinders the paper's self-contained nature. I am sure there is some curse of knowledge at play here, which is understandable, but it would be a good use of the authors' sharp eloquence to make the paper a bit more self-contained.

4. The role of analogue-to-digital conversion is not discussed. While I am not sure how pertinent this is for this particular work (see question 1), ADC bottlenecks are so common in analogue computing that it should deserve at least a mention. The impact of ADC resolution on the accuracy of the computations, the latency introduced by the conversion process, and the power consumption associated with ADCs are all critical factors that should be acknowledged, even if they are not the primary focus of the paper. The absence of any discussion on these aspects leaves a gap in the overall picture of hybrid analogue-digital accelerators.

### Questions
1. In the applications familiar to me, analogue-to-digital conversion tends to be an crucial bottleneck for hybrid analogue/digital accelerators.
    This affects their accuracy, latency, power efficiency, and, most crucially, die footprint which largely determines their cost.
    ADCs are so expensive in so many ways that many applications sacrifice as much precision as possible to minimize their use.

    In this light, how are those aspects relevant to your work?
    Do the experiments take them into account?
    Do previous works on the topic address them?


2. As the authors say, performing experiments with Gaussian distributions allows for closed-form solutions for the 2-Wasserstein distance. Yet, even though the plots from Figure 2 display a $y$-axis with units, it is hard to reason quantitatively reason in terms of $W_2$. Could you provide some general guidance for that? I mean, is a $W_2$ of 1 large? I understand this can be problem-dependent, but some general guidance would be helpful.

### Soundness
4

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
1

### Summary
This paper presents the first explicit probabilistic convergence guarantees for hybrid Langevin Noise Likelihood Sampling (LNLS) algorithms in activation sampling and optimization. The authors reduce hybrid LNLS to block sampling using continuous-time Langevin diffusion sub-samplers, analyzing randomized and cyclic block selection rules. They demonstrate that ideal accelerators converge exponentially under a log-Sobolev inequality, while finite device variation introduces bias in the Wasserstein distance. Numerical experiments on a toy Gaussian sampling problem illustrate the effects of device variation and hyperparameters.

### Strengths
- The paper is clearly structured, with each theorem building on the previous results to form a coherent narrative.

-  The findings of the paper are supported by clear numerical experiments.

### Weaknesses
N/A

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors analyze analog accelerators and large-neighborhood local search (LNLS) frameworks. Reducing LNLS to block Langevin Diffusion algorithms, the paper provides convergence guarantees using the tools from the classical sampling theory.

### Strengths
Before I start my review, I should acknowledge that the topics of this paper, including Langevin Diffusion (BLD) algorithms, Analog dynamical accelerators, SDEs, LNLS frameworks, are very different from what I do in my research. My main field of interest is mathematical optimization.

I have no doubt that analog computations are an important direction to accelerate the current expensive digital algorithms: the topic is important and relevant. The author's attempt at approaching the issue is unusual (in a good way) and nontrivial.

### Weaknesses
The main weakness is that it is challenging to read the paper. From the beginning, the authors introduce many uncommon words and terms that are very unlikely to be easily understood by most researchers from the ICLR community. I think the introduction and the background should be significantly simplified for a broad audience. For instance, the main object of interest is LNLS, but the authors do not try to explain the mathematical foundation and the background of LNLS. Figure 1 is too abstract to understand LNLS.  

Other weaknesses and questions:
1. Why do you consider Block Langevin Diffusion? Why can't we optimize w.r.t. all variables?
2. Lines 345-347: I guess there should be $||x - y||^2$ instead of $||x^2 - y^2||$
3. Assumption 5: How does the function inside the integral depends on $t$?
4. Assumption 6: In my experience, this is a very *uncommon* assumption. Also, Assumption 3 is also very uncommon.
5. Theorem 3: This theorem yields the convergence rate $\log \frac{1}{\varepsilon} + \varepsilon,$ which is $\geq 1.$ What If one wants to make the Wasserstein distance less or equal $0.001$?

Unfortunately, reading this paper, I'm not convinced that the reduction to Langevin Diffusion algorithms can not help to improve and explain analog accelerators. At the same time, I do not have expertise in these fields, so I choose low confidence.

### Questions
(see weaknesses)

### Soundness
2

### Presentation
1

### Contribution
2
