# From discrete-time policies to continuous-time diffusion samplers: Asymptotic equivalences and faster training

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
We study the problem of training neural stochastic differential equations, or diffusion models, to sample from a Boltzmann distribution without access to target samples. Existing methods for training such models enforce time-reversal of the generative and noising processes, using either differentiable simulation or off-policy reinforcement learning (RL). We prove equivalences between families of objectives in the limit of infinitesimal discretization steps, linking entropic RL methods (GFlowNets) with continuous-time objects (partial differential equations and path space measures). We further show that an appropriate choice of coarse time discretization during training allows greatly improved sample efficiency and the use of time-local objectives, achieving competitive performance on standard sampling benchmarks with reduced computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the training of diffusion samplers and neural stochastic differential equations (neural SDEs) by examining the connection between continuous-time objectives and their discrete-time counterparts. The authors establish that global objectives for discrete-time policies converge to path-space measure divergence objectives in the continuous-time limit, while local constraints asymptotically align with partial differential equations governing the time evolution of marginal densities. This theoretical grounding aims to bridge reinforcement learning (RL) objectives and stochastic control frameworks for diffusion processes. Empirically, the paper demonstrates that training with coarse, non-uniform time steps, particularly with random placements, can achieve substantial computational efficiency gains while retaining strong performance across a range of benchmarks.

### Strengths
1. The paper is very well written and easy to follow, with clear exposition of the mathematical derivations and the empirical results.
2. The experimental section is thorough and well designed, exploring the effects of different discretization strategies and their impact on performance in detail. The benchmarks used are diverse and represent a wide range of sampling challenges.
3. The work provides strong empirical evidence that non-uniform time discretization (particularly random placement) improves training efficiency. This observation could be highly relevant for practitioners working with high-dimensional diffusion models. Furthermore, the identification of random time discretization as a performant strategy is novel and supported by robust experimental evidence.
4. The paper effectively summarizes existing methods and objectives for diffusion sampling, offering a clear context for the proposed contributions and situating them within the broader body of work on diffusion models and sampling techniques.

### Weaknesses
1. While the theoretical contributions are valuable and provide an interesting link between discrete-time and continuous-time objectives, they are not completely unexpected and partly already present in the literature.
2. In the experimental results, it is noted that the ELBO gap does not converge to zero as the discretization becomes finer but instead appears to stabilize at a positive value. The authors do not give an explanation for this phenomenon. In particular, the lack of a "benchmark" makes difficult to connect these simulations to the numerical results presented in the first part of the paper above.
3. The observed performance gains with randomly placed time steps are well supported by empirical results, but the paper does not provide a theoretical explanation for why this approach works so well. Offering more insight into this phenomenon would enhance the overall impact of the findings.

### Questions
1. Is it correct to expect that the ELBO gap should converge to zero as the discretization becomes finer, or are there inherent limitations in the approach that cause the gap to saturate at a positive value? Clarifying this could help contextualize the observed results better.
2. Are there any existing benchmarks or prior work that provide a comparable measure of ELBO gap performance for optimally trained diffusion samplers? How do the proposed methods stack up in this context?
3. Can the authors provide more insight into why random placement of time steps works so (unexpectedly) well? Is there an intuitive or theoretical rationale for this observed behavior?
4. In Theorem 3.4, there seems to be a potential issue as $\vec μ_t$​ appears twice in the statement. Could this be a mistake, or is there a specific reasoning behind this repetition? Clarification would be helpful.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines training neural stochastic differential equations (SDEs) to sample from Boltzmann distributions without target samples. This work derives asymptotic equivalences by linking discrete-time policies to continuous-time diffusion. The approach is validated on sampling benchmarks.

### Strengths
1. The approach of linking discrete-time policy objectives with continuous-time SDE training is a useful idea, albeit heavily reliant on established results.

2. Authors show that this method potentially reduces computational costs for neural SDE training.

### Weaknesses
1. Firstly, I think the presentation of this work remains a major bottleneck for readers. Section 2 is preliminary, and it spans from pages 3 to 7. Such a lengthy preliminary section introduces well-known equations and results (e.g., equations (4)-(6) from GFlowNet papers, (9)-(15) from stochastic control and diffusion models, and (16), (17) as standard Euler-Maruyama discretizations).
These derivations, mostly grounded in existing work, dilute the contributions and add an undue burden for readers. Figures like Figure 3, which illustrate obvious points, seem unnecessary and further contribute to this issue. It is recommended to present additional informative and easy-to-follow diagrams in these sections.

2. The primary theoretical contribution—showing asymptotic convergence from Euler-Maruyama discretization to continuous-time SDEs (Propositions 3.2, 3.3, 3.4)—seems not surprising. The convergence results are probably straightforward applications of established SDE theory, with little added insights or unique techniques. Without further exploration of new derivation techniques or distinctive theoretical angles, the contributions feel like direct applications of existing results.

3. The experiments are conducted on standard synthetic benchmarks, such as Gaussian mixtures and low-dimensional toy distributions. To support this approach, it might be necessary to conduct higher-dimensional Bayesian inference tasks where the Boltzmann distribution is more untractable. Besides, the compared baselines exclude many recent models, such as flow-based generative models.

3. While efficiency is demonstrated, additional benchmarks comparing computational costs with traditional methods in larger dimensions would be helpful for real-world applications.

### Questions
1. Could the authors clarify why so much space is devoted to standard results? Would simplifying or condensing this content help highlight the unique contributions?

2. Beyond applying existing convergence results, what novel techniques, if any, were introduced in proving Propositions 3.2, 3.3, and 3.4?

3. Would more complex or realistic benchmarks alter the experimental outcomes, particularly in high-dimensional or non-Markovian sampling settings?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper discusses the relationship between continuous and discrete-time stochastic processes and their training. In particular, the main results give a series of propositions on how a discrete-time process can approximate a continuous time process. I have to say I had a hard time understanding the "big picture" of the authors' results.

### Strengths
The paper appears to be mathematically rigorous and experiments appear to give credence to the authors' work.

### Weaknesses
I found the paper very difficult to read. The notation is dense, not all appears to be defined, some is non-standard and unclear and I found it a little tricky to understand exactly what the authors wanted to do. It may be that the authors have solved in interesting problem in a genuinely useful way but that was unclear from the paper. All but the very expert reader would, in my view, find the paper a difficult read. 

A few specific comments are:

- Abstract could be more informative and precise
- Introduction is quite meandering and I wasn't quite clear on exactly what the authors were trying to do.
- Figures 1 and 2 were placed, in my view, quite early in the paper and were hard to interpret. They needed more textual description, or, considering where they were placed, needed "dumbing down" a little. 
- Equation (1) is somewhat standard but, for completeness, it would have been useful to know what \sigma(t) is (I could guess). Equation (1) is similar to (9) apart from \mu(t). I think the differences between the various forms of \mu(t) needs to be explained in more detail.
- It wasn't clear to me exactly what the reverse arrow meant in terms of policy e.g. the backwards arrow is used on \pi(t) below equation (3) but without any definition as far as I can see. 
- I found Section 2 quite muddled with various different concepts introduced with not too much explanation. I realise there is a page limit, but it was bordering on the unpenetrable. 
- I didn't really understand how the Propositions in Section 3 ended up affecting the Results in Section 4. Perhaps I am dense, but it would be good if the authors could explain this better.

### Questions
My main question is this: for a ML practitioner, how will the authors' results help?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the connection between continuous-time SDEs and their discretization, particularly focusing on the influence of the chosen timestep. It demonstrates that using non-uniformly discretized time with fewer steps can achieve similar performance during inference. Theoretical results are provided to support this approach.

### Strengths
* The problem studied in this paper is well-motivated.

* This paper presents extensive results in both theory and experiments.

* The appendix provides a comprehensive complement to the main text.

### Weaknesses
 * The theoretical results in Section 3 primarily focus on the convergence of the Euler-Maruyama method. Specifically, they show that convergence is ensured as the maximal step size approaches zero. However, these results do not explain why non-uniform discretization would generally be superior to uniform discretization. The advantage of non-uniform discretization—one of the main contributions of this paper—is demonstrated only through experiments

* As previously mentioned, there seems to be a gap between the theoretical and empirical sections of this paper. After reading the introduction, I expected to see concrete theoretical results that justify the use of non-uniform discretization. However, simply showing that convergence is guaranteed as $\Delta t$ approaches zero is unsurprising. The authors might consider adding more discussion on why uniform discretization is not always the optimal choice

* It has been proven that the order of convergence is determined by the step size, and the Euler-Maruyama scheme with uniform discretization has been shown to achieve optimal performance in the general case (see 'Numerical Treatment of Stochastic Equations' by Rümelin, 1982). I wonder if the claim made in this paper contradicts that result.

I would be willing to increase my rating if the authors are able to address my concerns.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
