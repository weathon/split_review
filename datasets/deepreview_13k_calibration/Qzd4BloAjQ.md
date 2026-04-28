# SGD with memory: fundamental properties and stochastic acceleration

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 3, 8

## Abstract
An important open problem is the theoretically feasible acceleration of mini-batch SGD-type algorithms on quadratic problems with power-law spectrum. In the non-stochastic setting, the optimal exponent $\xi$ in the loss convergence $L_t\sim C_Lt^{-\xi}$ is double that in plain GD and is achievable using Heavy Ball (HB) with a suitable schedule; this no longer works in the presence of mini-batch noise. We address this challenge by considering first-order methods with an arbitrary fixed number $M$ of auxiliary velocity vectors (\emph{memory-$M$ algorithms}). We first prove an equivalence between two forms of such algorithms and describe them in terms of suitable characteristic polynomials. Then we develop a general expansion of the loss in terms of \emph{signal and noise propagators}. Using it, we show that losses of stationary stable memory-$M$ algorithms always retain the exponent $\xi$ of plain GD, but can have different constants $C_L$ depending on their \emph{effective learning rate} that generalizes that of HB. We prove that in memory-1 algorithms we can make $C_L$ arbitrarily small while maintaining stability. As a consequence, we propose a memory-1 algorithm with a time-dependent schedule that we show heuristically and experimentally to improve the exponent $\xi$ of plain SGD.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper establishes a theoretical framework for the so-called memory-M algorithms - first order algorithms that are augmented with storage for M vectors in the gradient space, and uses a linear combination of them to compute the gradients and modify weight updates. The usefulness of this framework is that it is a natural generalization of Heavy Ball and a number of other first order algorithms. The work provides an equivalence of this formulation with recursive multi-step first-order algorithms. The work also provides a generalized loss decomposition into signal and noise propagations. The paper also provides a detailed description of convergence properties of memory-M (and focusing on memory-1) algorithms - including the main parameters controlling this convergence and an algorithm providing equivalent convergence rates for the SGD case.

### Strengths
Overall, this is a very good paper. I think it is very methodical in its development of the memory-M framework - starting with existing issues of accelerated HB for SGD, moving to the description of the generalized framework for GD and SGD, loss decomposition and improved algorithm and convergence properties. The topic coverage is very comprehensive, covering the expected questions raising with the development of the generalized framework. There are clearly a lot of efforts made towards the balance between rigor and readability - with moving a lot of the technical details into the appendix (e.g. the phrasing of Theorem 2). The contributions are novel to the field of stochastic optimization

### Weaknesses
An expected consequence of the comprehensiveness of the paper is its density - making it relatively hard to read. As mentioned before, there was clearly a lot of effort put towards reorganization and moving details into the appendix - but I wonder if more could be done in that direction. For example, the Loss expansion section with the introduction of propagators seemed too dense - and was lacking intuitions that would facilitate further reading of the paper, since those concepts were heavily relied on for further developments in the paper. Those intuitions were present in the earlier sections and were thus helpful for speeding up understanding of the paper. Specifically, the transition from the memory-M framework to the loss decomposition using propagators feels abrupt. The paper introduces the propagators as a tool to decompose the loss, but the motivation for this specific decomposition and its connection to the memory-M framework is not immediately clear. The reader is left to infer the underlying reasons, which makes the section harder to follow. Furthermore, the notation in this section, while mathematically precise, adds to the cognitive load, making it difficult to grasp the core ideas quickly. The lack of illustrative examples or a step-by-step breakdown of how the propagators are derived and used in the loss decomposition contributes to the perceived density.

### Questions
As mentioned, I wonder if there are any ways of improving the readability of the technical portions with further addition of intuitions and heuristics. This wouldn’t change the technical contributions of the paper but would make the paper more accessible for the readers and thus facilitate the propagation of ideas in it.

### Soundness
4

### Presentation
3

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
This paper introduces a framework for analyzing iterative optimization methods, referred to as memory-$M$ algorithms, which allow the gradient to be evaluated at shifted points relative to $w_t$ additionally a shift term is added to the gradient when doing the update. The authors explore both stationary (with fixed update parameters) and non-stationary versions of these algorithms. They establish that memory-$M$ algorithms can achieve the optimal convergence rate for data with a power-law spectrum, even under mini-batch noise. Notably, they propose a memory-1 algorithm with a time-dependent power-law schedule, which provides a heuristic pathway to accelerated convergence, supported by empirical results.


**Justification for the score**

While I think the result is important in establishing convergence results for a large family of methods, I think the presentation of the paper could be significantly improved.

### Strengths
The paper's biggest strength is the establishment of strong convergence rates for iterative methods. Mini-batched algorithms are difficult to analyze; hence, establishing the convergence rate for regression in the noiseless regime is interesting. 

Additionally, the method allows for controlling the constant and shows that it can also be arbitrarily improved. 

I think both of these are important contributions. 

In addition, the paper introduces a general framework for analyzing such methods. i think this is an important contribution as well.

### Weaknesses
The writing of the paper is a major weakness. It is very dense notationally, not necessarily conceptually. This makes it quite challenging to build intuition as one reads the paper. One possible suggestion is that the paper develops the results initially in the $a = 0$ as the shifts are not needed for the main contributions and then provide extensions, possibly in the appendix. The other is to hide some of the intermediate steps to provide space for more intuition for the different objects. 

One thing that threw me off is using capital letters for the propagators as these are scalars.

### Questions
1. Could such a framework be extended to non-IID batching, that is, batching with replacement (recent work [1,2])?

2. Could you say anything about the generalization error using [3]?

3. Could we add label noise or regularization?

[1] Lok, Jackie, Rishi Sonthalia, and Elizaveta Rebrova. "Discrete error dynamics of mini-batch gradient descent for least squares regression." arXiv preprint arXiv:2406.03696 (2024).

[2] Beneventano, Pierfrancesco. "On the trajectories of sgd without replacement." arXiv preprint arXiv:2312.16143 (2023).

[3]  Wang, Y., Sonthalia, R. &amp; Hu, W.. (2024). Near-Interpolators: Rapid Norm Growth and the Trade-Off between Interpolation and Generalization. <i>Proceedings of The 27th International Conference on Artificial Intelligence and Statistics</i>, in <i>Proceedings of Machine Learning Research</i> 238:4483-4491 Available from https://proceedings.mlr.press/v238/wang24l.html.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper explores how to make stochastic gradient descent (SGD) faster on certain types of optimization problems, specifically those that involve a noisy mini-batch setting. The authors examine how adding "memory" (extra helper variables) to SGD can help. They introduce "memory-$M$" algorithms, where $M$ is the number of extra velocity vectors added. Through mathematical analysis, they show that these memory-$M$ algorithms can achieve better performance by improving certain constants that affect convergence speed, even though they don’t change the basic rate of convergence.

The authors also propose a new "memory-1" algorithm, which has only one extra velocity vector and uses a special time-based schedule for learning. This algorithm is shown to improve performance both theoretically and in experiments.

### Strengths
The work is a definite interest to read, and the results seem to hold a lot of promise.

### Weaknesses
 - Introduction: The reader who is not an expert in this field will find this introduction difficult to understand. I recommend that it be significantly reworked using various welcome tricks, such as tables. In general, the text is difficult to read....

- I don't fully understand about the experimental part. Is it just not there?

### Questions
Can authors convince me that their work fits the spirit of this conference? This question is not obvious to me at this point.....

### Soundness
1

### Presentation
1

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
In this work, the authors address the open problem of theoretical feasible acceleration of mini-batch SGD-type algorithms (i.e. in the stochastic setting) on infinite-dimensional quadratic problems, particularly with power-law spectrum. 
The authors introduce memory-M algorithms with M auxiliary velocity vectors and show the equivalence to the multistep recurrence formulation if the loss $L$ is quadratic and hyperparameters of the algorithm are stationary. 
By expanding the loss in terms of so-called signal and noise propagators, the authors show that the loss convergence $L_t \sim C_l t^{-\xi}$ of stationary stable memory-M algorithms retain the exponent $\xi$ of plain GD, but can have different constants $C_L$. Finally the authors prove that memory-1 algorithms can make $C_L$ arbitrarily small while maintaining stability. The theoretical results are empirically verified on synthetic Gaussian data and MNIST using a shallow ReLU network.

### Strengths
- The authors are able to (heuristically) derive an accelerated and stable rate of convergence in their algorithm AM1 and verify the rate empirically. (However I am not too familiar with the field to judge the novelty of this contribution.) 
- The derivation of the stability of stationary stable memory-M algorithms seems rigorous and it is interesting to see that stationary stable algorithms cannot achieve a faster rate than plain GD even using arbitrary numbers $M$ auxiliary vectors. 
- The analysis of the convergence constant $C_L$ and the possibility of making it arbitrarily small for stationary stable memory-1 algorithms and how it relates to the effective learning rate $\alpha_{eff}$ was also insightful.

### Weaknesses
 - The paper seemed quite convoluted with many different symbols, equations and indices due to its mathematic rigor and it could benefit from restructuring it such that it becomes more accessible. The dense notation and multiple layers of abstraction make it challenging to follow the core arguments, especially for readers not deeply familiar with the specific mathematical techniques used. For instance, the introduction of signal and noise propagators, while crucial to the analysis, could be presented with more intuitive explanations and visual aids to enhance understanding.
- The empirical validation of the results remains quite limited with only experiments on synthetic Gaussian data and MNIST. Particularly, the spectrally expressible approximation holds exactly for gaussian data and approximately for MNIST classification. It would be interesting to see also experiments where this approximation is less exact. The experiments, while validating the theoretical claims, do not explore the algorithm's behavior in more complex, real-world scenarios where the underlying assumptions might not hold as strongly. This limits the generalizability of the findings and raises questions about the robustness of the method.
- It is seems like the optimal rate depends on the right choice of hyperparameters, such as $\alpha_0$, $q_0$ and $\delta$. However it is unclear to me how to select or estimate them in practice. This limits its application to real-world problems. The theoretical results provide guidance on the relationships between these parameters, but the practical implications for tuning them in specific applications are not well-defined. The lack of a clear methodology for hyperparameter selection poses a significant hurdle for practitioners aiming to implement the proposed algorithm.

### Questions
1. I do not fully understand the image on the right of Figure 2. What are $t_1, ..., t_4$ supposed to denote or perhaps more generally what does it mean that a signal/noise propagator is "long" or "short"?
2. I have another question regarding the stability of the maps $A_\lambda$: If I understood it correctly, $\lambda$ corresponds to the eigenvalues of the matrix $\mathbf{H}$ (line 201). Thus, it seems to me that we have to assume $\lambda > 0$ in general. Does Theorem 3 then imply that one can only have strict stability of $A_{\lambda}$ if $\lambda_{\max}$ is sufficiently small? 
3. What are the values of $\xi_V$ and $\xi_U$ respectively in Eq. (21) and (22)? 
4. Have the authors also considered non-quadratic settings and how does it perform here?

### Soundness
4

### Presentation
2

### Contribution
3
