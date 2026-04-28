# Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Diffusion models have achieved great success in generating high-dimensional samples across various applications. While the theoretical guarantees for continuous-state diffusion models have been extensively studied, the convergence analysis of the discrete-state counterparts remains under-explored. In this paper, we study the theoretical aspects of score-based discrete diffusion models under the Continuous Time Markov Chain (CTMC) framework. We introduce a discrete-time sampling algorithm in the general state space $[S]^d$ that utilizes score estimators at predefined time points. We derive convergence bounds for the Kullback-Leibler (KL) divergence and total variation (TV) distance between the generated sample distribution and the data distribution, considering both scenarios with and without early stopping under specific assumptions. Notably, our KL divergence bounds are nearly linear in dimension $d$, aligning with state-of-the-art results for diffusion models. Our convergence analysis employs a Girsanov-based method and establishes key properties of the discrete score function, which are essential for characterizing the discrete-time sampling process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a discrete-time sampling method using score estimators at fixed points in a multidimensional state space. It provides bounds on how closely the sample matches the data distribution, with KL divergence bounds nearly linear in dimension, comparable to top diffusion models. The analysis uses a Girsanov-based approach to define key properties of the discrete score function for effective sampling.

### Strengths
The paper tackles an interesting theoretical problem. Theoretical analysis of diffusion models with finite state spaces with discrete time space is of great importance. The authors have made the effort to push further the existing methods for the current setting.

### Weaknesses
 The notation is confusing and important details are often omitted.  The assumptions seem to be rather stringent. The paper lacks mathematical clarity. See the below sections for details.
 
- *Proposition 1*. The formula for $q_t$ depends on the initial data distribution $p_{data}$. When $t \rightarrow \infty$, the term on the right side  $\frac{1}{S} \left(1 - e^{-t}\right) \mathbf{1}_S \mathbf{1}_S^\top + e^{-t} I_S \rightarrow \frac{1}{S} \mathbf{1}_S \mathbf{1}_S^\top$ . The latter is a fixed matrix and thus $q_t \rightarrow \frac{1}{S} \mathbf{1}_S \mathbf{1}_S^\top \cdot p_{data}$. This is not necessarily the uniform distribution. 
- *Proposition 1* What does approaching mean here? In what sense do you have the convergence?
-  *line 280* . The sentence `With rate $Q^{\leftarrow}_t$, it holds that...` is not clear. Is there a reference or proof for this statement? 
- *Assumption 2* It does not seem to be easy to verify this assumption. Is there a general class of distributions that are known to satisfy it?
- *Theorem 2* The number $\kappa_i$ is not always well-defined, as we deal with discrete distributions, where some of the probabilities may be equal to zero. 

#### typos
- *line 187* if setting β(t) as a time-dependent scala
- *line 206* Nota -> Note
- *line 323* For completeness, We -> For completeness, we

### Questions
- *Equation on line 723*. Why is $Q$ equal to the Kronecker sum $Q^{tok}$?   
 - *line 296* Why is the reverse process time-inhomogeneous? 
 - *line 3 of the Algorithm*: How easy is it to find the maximum of the estimated score function? Is there any concavity assumption to make this problem solvable in theory/real-time? Is this assumption satisfied for practically relevant examples?
 - *line 361* Why is there a uniform upper bound on all the scores and their estimators? On line 371 the authors mention that the score function may be as large as infinity for some data points. This means, that when $\delta$ is small, this uniform upper bound $C_1$ becomes larger, thus, it is dependent on $\delta$. Can this dependence be quantified? 
 - *Equation (4)*. Why is this true? Is there a reference or a proof for this statement?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper  examines theoretical aspects of score-based discrete diffusion models within a Continuous Time Markov Chain (CTMC) framework. The authors aim to address the underexplored convergence properties of these models, especially in discrete state spaces, compared to their continuous counterparts which have been widely studied. Key contributions of the paper include: 1. The authors propose a discrete-time sampling algorithm designed for high-dimensional discrete diffusion tasks. This algorithm leverages score estimators at specific time points to approximate the reverse process of the diffusion model. 2. They provide convergence bounds for the KL divergence and TV distance between the generated sample distribution and the target data distribution. The bounds are derived for cases both with and without early stopping, depending on assumptions about the data distribution's properties. 3.The convergence analysis is performed using a Girsanov-based method, which enables the authors to assess the score estimation error, discretization error, and mixing properties of the forward process. This method is adapted from techniques in continuous diffusion models and tailored to the discrete setting. 4. The paper establishes that their convergence bounds scale nearly linearly with the data dimension, aligning with the best results for continuous models. Additionally, they discuss practical considerations, such as the need for score clipping and early stopping under certain conditions to handle potential score function divergences. 5. The authors compare their method with prior approaches, particularly highlighting differences in sampling efficiency and the elimination of certain assumptions on score estimators, thus broadening the algorithm's applicability in discrete settings.

### Strengths
Overrall I think this work is clear and studies a clean problem which is relevant to the theoretical understanding of diffusion models.. Theorems 1 and 2 derive rigorous convergence bounds for score-based discrete diffusion models using KL divergence (Theorem 1 with early stopping, Theorem 2 without early stopping). This provides a critical theoretical foundation for discrete diffusion modeling, aligning nearly linearly with the dimension $d$, a promising result compared to continuous models. And the use of a Girsanov-based approach to analyze the sampling algorithm in a discrete setting is particularly noteworthy (Sections 5 and 6). This method adapts well-established techniques from continuous diffusion models and is a creative application in the discrete domain, enabling a novel convergence analysis.
The work also proposes a time-discretized approach (Section 4 and Algorithm 1), which involves sampling at discrete time steps rather than simulating the continuous CTMC path. This approach allows for more efficient sampling, as it does not require continuous access to the reverse CTMC. Additionally, to ensure bounded score estimates, the authors introduce score clipping as a practical solution for handling extreme values (discussed in Section 5).

### Weaknesses
 I don't see major weaknesses of this work, but I do have some comments:
1. Since the authors claim improved sampling efficiency (e.g., fewer function evaluations), would compare actual runtime or convergence speed with other discrete sampling methods (such as the uniformization technique in Chen & Ying) substantiate these claims?
2. Assumption 2 requires the data distribution to have full support and uniform bounds. This may restrict the model.
3. Although the work mentions similarities with continuous diffusion models, there is limited discussion on when to use their discrete CTMC approach versus discretized continuous models for discrete data. 
4. Generalizability to Other State Spaces: The works' algorithm assumes a general state space $[S]^d$, but would it be insightful to discuss how it might extend to more complex or structured discrete spaces, such as graph-based or hierarchical state spaces, which are common in discrete data applications?

### Questions
1. Have the authors considered adaptive step sizes as a way to minimize discretization error? If so, could author's share insights on how this might affect the overall convergence bound?
2. The paper proposes a CTMC-based discrete diffusion model, but certain continuous diffusion approaches are also adaptable to discrete data. Could the authors elaborate on specific scenarios or types of tasks where their CTMC-based model would be preferred over these alternative approaches?
3. Also see weaknesses part above

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper provides the convergence rate of the discrete diffusion models introduced by Lou and Ermon. The authors consider the finite state space $S^d$, extending early analysis by Chen and Ying in the continuous time.

### Strengths
The paper provides a timely convergence analysis of the discrete diffusion models, which is important in understanding this new class of models (with applications to LMM). I checked most proofs, and they are scientifically correct.

### Weaknesses
The weaknesses are:

(1) The main idea of proofs are very similar to Chen and Yin, with the key to the proof the representation given by Proposition 1. The differences are: (1) the paper extends the previous results from $\{0,1\}^d$ to $S^d$; (2) the paper considers the issue of discretization. I agree that (2) is important, while (1) seems to me incremental. The extension to $S^d$ from $\{0,1\}^d$ while seemingly minor, requires careful handling of the transition probabilities and the associated mixing times. The analysis of these mixing times, especially in the context of high-dimensional state spaces, is not trivial and should be more thoroughly justified. The paper should explicitly address the challenges in extending the mixing time bounds from the hypercube to a general state space $S^d$.

(2) The authors made Assumption 2, which requires the ratio constant $L$ is independent of $d$. I am dubious on this assumption, since the main application of the discrete diffusion models is on the LLM. The assumption that $L$ is independent of $d$ is a strong one, and its validity needs more rigorous justification, especially when considering applications to large language models where the state space dimension $d$ can be extremely high. The authors should provide a more detailed analysis of how this assumption relates to the properties of the data distribution, and how it might be violated in realistic scenarios. A numerical analysis would be beneficial to demonstrate the behavior of $L$ as $d$ increases.

(3) Regarding early stopping: Chen and Yin considers early stopping since they are concerned with the continuous dynamics. It is known that the score matching has large errors near time $0$, and even the continuous dynamics may not be well-defined at $0$. Since the paper studies the discrete scheme, I wonder if there is a particular reason why the authors also consider early stopping. The justification for early stopping in the discrete setting is not entirely clear. While score matching errors near $t=0$ are a concern in continuous settings, the discrete scheme might have different behavior. The authors should provide a more detailed explanation of why early stopping is necessary in their discrete framework, and how it relates to the potential divergence of the score function at $t=0$.

(4) Except the error for the initialization, which uses log-Sobolev inequality (more or less expected), the other ingredients in the proof are very similar to the existing approaches to the SDE-based diffusion models. Of course, the authors dealt with CDMC, which is slightly different. While the use of log-Sobolev inequality for initialization error is standard, the paper should highlight the specific challenges and adaptations required to apply these techniques to CDMCs. The paper should also provide a more detailed comparison of the proof techniques with existing approaches for SDE-based diffusion models, explicitly pointing out the differences and similarities in the context of CDMCs.

### Questions
Please see the weakness section.

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
This work develops an algorithm for score-based diffusion models over a discrete state space. Their new algorithm relies on the uniformization of the CTMC developed by Chen and Ying and discretization in time. The main innovation of the work is theoretical. Using this new algorithm, the authors can derive bounds on the generated samples under less restrictive assumptions than in previous work. The main assumption is an approximate score function, where analogous to the results on continuous denoising diffusion models, the authors are able to develop a bound with early stopping. Under the further assumption of bounded scores for the data distribution, the authors show that early stopping is no longer needed and can derive bounds at $t=0$.

### Strengths
The paper is well-written and represents a strong contribution to the generative model literature. The assumptions are weaker than those for existing algorithms. There is a strong case for accepting this paper due to its novel theoretical analysis of an important problem. The theoretical framework given may be useful in analyzing more general settings and motivating further algorithmic improvements.

### Weaknesses
First, It is unclear how tight these bounds are. Can the authors compare these to bounds in the continuous setting? Second, I don’t understand everything in the table, and it would be better to flesh out the comparison with Chen and Ying. In particular, their assumptions are different, can you tell us what they are? Finally, there are no tests of the algorithm in practice. While the theoretical contribution is nice, it remains to be seen if it will have an impact on practice.

### Questions
Can the authors provide more explanation comparing their result to the Chen and Ying result? 

Also, can they provide a comparison between their guarantees and the guarantees for continuous models? I am curious if they are analogous or what the fundamental differences are.

### Soundness
4

### Presentation
4

### Contribution
4
