# How Discrete and Continuous Diffusion Meet: Comprehensive Analysis of Discrete Diffusion Models  via a Stochastic Integral Framework

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Discrete diffusion models have gained increasing attention for their ability to model complex distributions with tractable sampling and inference. However, the error analysis for discrete diffusion models remains less well-understood. 
    In this work, we propose a comprehensive framework for the error analysis of discrete diffusion models based on L\'evy-type stochastic integrals. 
    By generalizing the Poisson random measure to that with a time-independent and state-dependent intensity, we rigorously establish a stochastic integral formulation of discrete diffusion models and provide the corresponding change of measure theorems that are intriguingly analogous to It\^o integrals and Girsanov's theorem for their continuous counterparts.
    Our framework unifies and strengthens the current theoretical results on discrete diffusion models and obtains the first error bound for the $\tau$-leaping scheme in KL divergence.
    With error sources clearly identified, our analysis gives new insight into the mathematical properties of discrete diffusion models and offers guidance for the design of efficient and accurate algorithms for real-world discrete diffusion model applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the challenge of error analysis in discrete diffusion
models. To bridge the gap between discrete and continuous diffusion models
(for which the error analysis is better understood), the authors propose a
framework based on Levy-type stochastic integrals, by generalizing Poisson
random measures to support state-dependent and time-varying intensities
under assumptions of regularity of rate matrix, and bounded and continuous
score function. This framework allows for error decomposition into
components such as truncation, approximation, and discretization errors,
providing clearer insight into error sources.  The analysis is performed
for tau-leaping and uniformization methods, two methods to simulate the
backward process. They establish stronger error bounds compared to previous
work using KL divergence.

### Strengths
Pros:
- Very non-trivial theoretical work.

### Weaknesses
Cons:
- Positioning of the work is not clear. It is not compared clearly with
  previous work.
- Motivation and implications for practical usage not provided.
- Very dense writing. Hard to understand.

Details:
The main results are two theorems, one for tau-leaping and the other for
uniformization. No attempt is made to provide outlines of the proofs. What
is the basic motivation for this research? How does it contribute to the
field (reduce algorithmic complexity, improve guarantees, etc.)?
The reader could greatly benefit from proof outlines.

The paper is very hard to understand. For a reader who is not deeply
immersed in this topic, it is almost impossible to understand the
implications, general approaches, and the proofs themselves.

The third bullet in contributions says that the work unifies and fortifies
existing research on discrete diffusion models. The reviewer did not come
across any statement in support of this or elaborating this point.

Related works does not cover any theoretical work on discrete diffusion
models. The introduction does mention several papers in this regard.
Organization can be made better.

The paper starting at Preliminaries is very dense. That said, the authors
have put effort to state the assumptions clearly and provided discussions
on differences between continuous and discrete diffusion models w.r.t. the
various errors considered.

### Questions
Questions inserted in weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper develops a rigorous theoretical foundation for discrete diffusion models, drawing parallels with continuous diffusion models. The authors introduce a novel stochastic integral framework using Lévy-type integrals, which enables a structured representation of discrete diffusion processes. They establish change-of-measure techniques analogous to Girsanov’s theorem, facilitating error analysis in terms of KL divergence.
By decomposing errors into truncation, approximation, and discretization components, the paper provides the first KL divergence bounds for the τ-leaping scheme in discrete settings. This unified framework also compares $\tau$-leaping and uniformization methods, highlighting computational efficiency and accuracy. Overall, the work advances the theoretical understanding of discrete diffusion models, making it possible to design more accurate and efficient algorithms for real-world applications that require discrete data modeling.

### Strengths
1.Theorem 3.3 establishes a change of measure theorem for Poisson random measures with evolving intensity, the authors introduce a discrete analog to Girsanov's theorem. This is a breakthrough, as it enables KL divergence analysis for discrete models, a theoretical advancement that makes error analysis feasible for the discrete setting.
2.Section 4, the paper follows a classical error analysis for diffusion models, breaking down error into truncation, approximation, and discretization components. This analysis, grounded in Theorems 4.7 and 4.9, is particularly valuable as it allows for practical application through the $\tau$-leaping and uniformization algorithms, with explicit convergence guarantees.
3.The paper presents the first KL divergence bounds for the t-leaping scheme in discrete diffusion models. This error bound is stronger and more informative than prior work using total variation distance.

### Weaknesses
I don't see major weaknesses of this work, but I have some comments:
1. The paper provides rigorous theoretical error bounds for τ-leaping and uniformization (Theorems 4.7 and 4.9). Do the authors plan to empirically validate these bounds on synthetic or real-world datasets? It would be beneficial to see experiments that not only validate the theoretical bounds but also explore the tightness of these bounds in practice. Specifically, how do the empirical errors scale with the parameters of the algorithms, such as the time step τ in τ-leaping or the uniformization rate? This would provide a more complete picture of the practical implications of the theoretical results.
2. Could the authors provide runtime or memory complexity comparisons for τ-leaping versus uniformization under varying parameters? A more detailed analysis of the computational cost is needed. For instance, how does the runtime of each algorithm scale with the dimensionality of the discrete state space, and how does the choice of parameters affect the practical runtime? Furthermore, a comparison of memory usage should consider not only the storage of the neural network but also the memory required to store intermediate states and random variables during the simulation.
3. The paper centers on Lévy-type integrals for discrete diffusion models. Could the authors comment on other potential stochastic frameworks for discrete models and when the proposed Lévy-type integral framework would be preferable over alternatives? While the Lévy-type integral framework is a novel approach, it would be valuable to understand its limitations and when alternative frameworks might be more appropriate. For example, how does this framework compare to other approaches that might not rely on Markov assumptions or those that use different types of stochastic processes?

### Questions
see above Weaknesses section.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper provides a framework to analyze the KL-error of discrete diffusion models using a stochastic integral approach. The authors introduce a formulation for discrete diffusion processes using Poisson random measures with time- and state-dependent intensities. This framework allows them to decompose the error into truncation, approximation, and discretization errors. The key contributions include considering the $\tau$-leaping scheme and establishing an error bound for it in terms of KL divergence.

### Strengths
The integral formulation for discrete diffusion models is insightful and provides strong motivation for the proposed algorithms. The error bounds in theorems 4.7 and 4.9 are neat.

### Weaknesses
While this is a theory-focused paper, some experimental evaluation would enhance the work, particularly to demonstrate the practical accuracy of the error bounds or the performance of Algorithm 1 and Algorithm 2 in generative applications.

The presentation is highly technical from the outset, assuming a strong theoretical background in diffusion models. The extensive use of dense notation and specialized terminology makes the paper challenging to read and less accessible.

### Questions
How important is the request "Q symmetric" for assumptions 4.3--4.6?

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
2

### Summary
This paper investigates the error analysis of discrete diffusion models. To this end, the authors develop a framework based on Levy-type stochastic integrals and establish a stochastic integral formulation of discrete diffusion models. The framework is utilized to derive the first error bound and sheds insight into the design of efficient and accurate discrete diffusion models.

### Strengths
1. This paper proposes the first error bound for the diffusion process, which provides insights and guidance for future research on discrete diffusion models.

2. Well-designed examples are presented for better illustration.

3. Rigorous theoretical analyses establish the foundation of the framework and the error bound for discrete diffusion models.

### Weaknesses
1. This paper is of theoretical interest. Some simulation experimental results are suggested to confirm the error analysis if possible.

2. This paper is mathematic-heavy. Some insights, intuitions, or illustrations are suggested to provide for better comprehension.

3. The error analysis in Theorem 4.7 is built on four assumptions, which seems to weaken the practicality of the error bound. I suggest the authors justify or explain this point.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
