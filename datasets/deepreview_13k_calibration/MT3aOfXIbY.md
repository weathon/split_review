# Faster Diffusion Sampling with Randomized Midpoints: Sequential and Parallel

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Sampling algorithms play an important role in controlling the quality and runtime of diffusion model inference. In recent years, a number of works (Chen et al., 2023c;b; Benton et al., 2023; Lee et al., 2022) have analyzed algorithms for diffusion sampling with provable guarantees; these works show that for essentially any data distribution, one can approximately sample in polynomial time given a sufficiently accurate estimate of its score functions at different noise levels. 

In this work, we propose a new scheme inspired by Shen and Lee's randomized midpoint method for log-concave sampling  (Shen & Lee, 2019). We prove that this approach achieves the best known dimension dependence for sampling from arbitrary smooth distributions in total variation distance ($\widetilde O(d^{5/12})$ compared to $\widetilde O(\sqrt{d})$ from prior work). We also show that our algorithm can be parallelized to run in only $\widetilde O(\log^2 d)$ parallel rounds, constituting the first provable guarantees for parallel sampling with diffusion models.
    
As a byproduct of our methods, for the well-studied problem of log-concave sampling in total variation distance, we give an algorithm and simple analysis achieving dimension dependence $\widetilde O(d^{5/12})$ compared to $\widetilde O(\sqrt{d})$ from prior work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors explore sampling for diffusion with mild assumptions and introduce both sequential and parallel algorithms, which extend the ODE-based predictor-corrector framework initially presented in [CCL+23a]. In their sequential approach, they adeptly utilize the randomized midpoint method in[SL19] to discretize the probability flow ODE during the predictor phase, and use the corrector method outlined in [CCL+23a] with a short time $T$. Impressively, this method achieves a complexity of $O(L^{5/3}d^{4/9}/\varepsilon)$, which marks a substantial improvement over the previous best complexity of $O(L^2d^{1/2}/\varepsilon)$. For the parallel algorithm, the authors also apply a similar parallel randomized midpoint method from [SL19] for the predictor phase and use the parallel underdamped Langevin method from [ACV24] as the corrector. This innovative combination gives the first provable guarantees for parallel sampling within diffusion models. Furthemore, this paper gives an improved bound for log-concave sampling.

### Strengths
- Their method achieves significantly better sequential complexity and parallel complexity.

- Overall I found the paper well-written and clear.

### Weaknesses
 - Their sequential result requires a slightly stronger assumption on the score estimation error, but I think it is fine.

- The technical contributions are limited to combining existing ODE-based predictor-corrector framework and discrete schemes.

### Questions
- is it possible to improve the total query complexity of paralell version to $d^{4/9}$?

- What are the primary challenges associated with removing the smoothness assumption?

- In the parallel version of sampling for diffusion models and the log-concave sampling algorithm, the predictor-corrector framework runs only once, whereas in the sequential version, the predictor-corrector loop is repeated $N_0$ times. Why does this difference occur?

### Soundness
3

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
2

### Summary
The manuscript introduces a novel approach for enhancing sampling efficiency in diffusion models by incorporating a randomized midpoint method. This method, inspired by Shen and Lee's work on log-concave sampling, is adapted to diffusion processes to reduce sample complexity and improve iteration bounds. The authors present theoretical guarantees for both sequential and parallel sampling, addressing the limitations of previous diffusion model sampling techniques.

### Strengths
**Theoretical Innovation.** The manuscript extends a randomized midpoint technique, traditionally used in other domains, to diffusion sampling, presenting significant advancements in sample complexity for smooth distributions.

**Parallel Sampling Framework.** Including a parallel sampling approach with provable efficiency bounds is particularly notable, potentially paving the way for scalable implementations in large-scale generative modeling tasks.

**Solid Analysis.** The authors offer a rigorous mathematical foundation for their method, with thorough proofs and well-defined assumptions on score functions and dimensionality dependence.

### Weaknesses
 **Assumptions and Practical Applicability.** While the theoretical advancements are clear, the reliance on strong Lipschitz assumptions and high accuracy in score estimates might limit practical applicability. The authors could consider discussing the feasibility of these assumptions in real-world diffusion models. Specifically, the Lipschitz constant of the score function can be very large, especially at the beginning of the diffusion process, which would require very small step sizes to ensure convergence. Furthermore, the assumption of high accuracy in score estimates is also problematic, as in practice, score networks are trained to minimize an empirical loss, and thus, the score estimates are not exact. The paper could benefit from a discussion of how these assumptions impact the performance of the proposed method in practical scenarios.

**Lack of Experimental Validation.** Despite the paper's focus on theoretical results, experimental validation would have been beneficial. Empirical benchmarks could highlight practical gains and offer insights into scenarios where the proposed method outperforms existing approaches. For example, comparing the proposed method with other sampling techniques such as DDPM or DDIM on standard datasets, such as CIFAR-10 or ImageNet, would provide valuable insights into the practical performance of the method. The absence of such experiments makes it difficult to assess the practical relevance of the proposed approach.

**Parallelization Overhead.** While the approach achieves polylogarithmic round complexity, it requires significant parallel resources to fully realize these benefits. The paper could improve by addressing potential bottlenecks and clarifying hardware implications. The paper does not discuss the communication costs associated with the parallel implementation, which could be a significant bottleneck in practice. Furthermore, the paper does not discuss the memory requirements of the parallel algorithm, which could be a limiting factor in large-scale applications.

### Questions
**Space Complexity and Scalability.** Can the authors elaborate on how the proposed method would scale with large data distributions in practical applications? How feasible is this method for scenarios requiring substantial memory or computation resources?

**Empirical Benchmarks.** Could the authors provide insights on the types of empirical tests they recommend or any preliminary results? Testing on standard datasets or benchmarks in score-based generative models would be particularly valuable for evaluating this method’s efficiency.

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
3

### Summary
This paper uses the randomized midpoint method to solve the reverse-diffusion SDE in generative diffusion models, to generate samples.  The randomized midpoint method is a more efficient method of solving SDEs than methods which incur a first-order error, such as the Euler-Maruyama integrator, as long as the coefficients are smooth functions.   The randomized midpoint method was originally developed for implementing the Hamiltonian Monte Carlo Markov Chain algorithm, but the here the authors apply the same technique in the setting of generative diffusion models.  This allows the authors to obtain faster runtime bounds for sampling (in the total variation norm) from the reverse-diffusion SDE in diffusion models, provided the certain smoothness assumptions are satisfied.  As a by-product of their analysis the authors also obtain improved bounds for sampling from log-concave distributions using the Langevin MCMC algorithm.

### Strengths
The paper obtains guarantees, in the TV norm, for solving the reverse SDE in diffusion models, with improved dimension dependence on the runtime.

The paper obtains improved guarantees, which are logarithmic in dimension, for parallelized solving of reverse SDE in diffusion models.

As a by-product of their analysis the authors also obtain improved bounds for sampling from log-concave distributions using the Langevin MCMC algorithm.

The paper introduces a new technique (the randomized midpoint method, originally developed for log-concave sampling via MCMC algorithms) to the area of generative diffusion models.

### Weaknesses
The paper does not include any numerical simulations.  Numerical simulations would help evaluate whether their algorithm works well in practice (both in terms of runtime and in terms of sample generation quality).

Also, while the authors adapt a new technique to the generative diffusion models, this is still an existing technique, but was used in a different area (MCMC for log-concave sampling).  That being said, I still feel the technical contribution is good since the authors introduce an existing technique to a new area.

### Questions
Can the authors provide simulations of their methods? It would be interesting to see if their method works in practice.  This concerns both the runtime and the quality of the generated samples.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies diffusion models and introduces a faster sampling algorithm utilizing the randomized midpoint method within a predictor-corrector framework. In the predictor step, the paper introduces the randomized midpoint method, which allows for bounding the squared displacement into “bias” and“variance”terms. The corrector step follows the analysis in Chen et al.,2023b. This approach reduces discretization error, leading to an algorithm with improved theoretical dependency on the dimension $d$. Similar analysis can also be used in the setting of log-concave sampling in total variation distance, achieving a better dependency in $d$.

### Strengths
1. The organization is clear, highlighting the main contribution.

2. The analysis method is very novel, and it’s an interesting result to see that the dimensional dependency for sampling can be improved to be better than $\tilde O(\sqrt{d})$.

3. The paper shows that the analysis can also be extended to parallel algorithms.

### Weaknesses
1.The assumptions are a little strong.  It has been shown in [1][2] that the assumption of Lipschitz score can be relaxed. Moreover, it is often enough to assume that the true score is Lipschitz (Assumption 2.2). However, in this paper, the estimated score is also required to be Lipschitz. Although I don’t think it’s a big problem, can the authors remark about where this additional assumption is used? Specifically, the requirement that the *estimated* score is Lipschitz is a stronger condition than what is typically assumed, and it's not immediately clear why this is necessary for their analysis. It would be beneficial to explicitly point out where this assumption is crucial in their proofs and what would break down without it. For example, is it used to bound the error propagation in the iterative sampling process? Or is it essential for the convergence analysis of the predictor-corrector scheme? A more detailed explanation would be helpful.

2.There are issues with the proof of Lemma A.2. The argument in (Line 736 equation 17) holds only under pointwise estimation (the estimated score is accurate for any $x$). However, in Assumption 2.4, it is defined as the expectation. Similar conditions occur in Line 755. As all the lemmas after this depend on Lemma A.2, the main result is correct only with a stronger assumption, which is not reflected in the paper. The issue here is that the proof seems to assume a pointwise bound on the score estimation error, while the assumption only provides an expected bound. This discrepancy needs to be addressed carefully, as it could invalidate the subsequent analysis. The authors should clarify how they bridge this gap between the expected error and the pointwise error required in their proof. The current argument is not rigorous enough and needs to be revised to ensure the validity of the results.

3.It misses some background knowledge and discussion:

(1) The paper discusses log-concave sampling in section 3.6. However, there is no background knowledge in this paper. It is unclear what is the exact setting. Thus, the analysis in Appendix C is confusing. The authors should provide a clear definition of the log-concave sampling problem they are addressing, including the specific assumptions on the target distribution and the sampling algorithm. Without this context, the analysis in Appendix C is difficult to follow and its significance is unclear.

(2) In the main content, all the theorems are informal. Therefore, in the proof technique sections, like Sections 3.3, and 3.4, the target of the argument is ambiguous. I think at least a formal version of the theorem should be provided, and more details of the proof should be provided to help readers understand. The lack of formal theorem statements makes it difficult to understand the precise claims being made and the scope of the results. The authors should provide formal versions of their main theorems, including all the necessary assumptions and the exact error bounds. This would greatly improve the clarity and rigor of the paper. Furthermore, the proof technique sections should provide more detailed explanations of the key steps and the underlying intuition.

4.Some typos: I think Algorithms 1, 2, and 3 are exactly the same as Algorithms 4,5,6 in the appendix. Thus, the reference in Algorithm 3 Line 3 should be Algorithm 1 instead of Algorithm 4, right?

### Questions
1. As claimed in [1], the linear dependency on $d$ is optimal for KL divergence, thus $\sqrt{d}$ for TV. Can you remark on this compared with the better than $\sqrt{d}$ result in this paper?

2. In the proof of Theorem A.10, given the value of the hyperparameters in Line 1109, can you explain more about how you can get the iteration complexity? Is it max $\\{1/h_{pred}, 1/h_{corr}\\}$? Then why the dependency on $d$ is not $d^{17/36}$, which is larger than $d^{5/12}$?

### Soundness
3

### Presentation
2

### Contribution
3
