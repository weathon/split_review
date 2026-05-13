# Parallel simulation for sampling under isoperimetry and score-based diffusion models

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
In recent years, there has been a surge of interest in proving discretization bounds for sampling under isoperimetry and for diffusion models. As data size grows, reducing the iteration cost becomes an important goal. Inspired by the great success of the parallel simulation of the initial value problem in scientific computation, we propose parallel Picard methods for sampling tasks.  Rigorous theoretical analysis reveals that our algorithm achieves better dependence on dimension $d$ than prior works in iteration complexity  (i.e., reduced from $\widetilde{\gO}(\log^2 d)$ to $\widetilde{\gO}(\log d)$), which is even optimal for sampling under isoperimetry with specific iteration complexity. Our work highlights the potential advantages of simulation methods in scientific computation for dynamics-based sampling and diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a parallel Picard method aimed at enhancing the efficiency of sampling under conditions of isoperimetry and score-based diffusion models (SGMs). It addresses two primary sampling problems: sampling from log-concave distributions and sampling for SGMs used in generative modeling. The method presents improvements in iteration complexity from $O(poly(\\log d))$ to $O(\\log d)$ which aligns with known theoretical lower bounds. By leveraging parallelization techniques across both time slices and within Picard iterations, the authors propose a discretization scheme that could potentially reduce the computational burden associated with sampling, especially for large-scale datasets.

### Strengths
1. The paper is well-written with good motivations and explicit technical contributions.

2. The diagonal-style parallelization across time slices sounds fresh to me, which addresses limitations in convergence faced by existing methods that do not fully parallelize time slices.

3. The paper provides rigorous theoretical bounds, such as convergence rates with respect to KL divergence. The approach's complexity analysis indicates a substantial improvement over previous methods, achieving nearly optimal bounds in iteration complexity.

4. By adapting the approach for diffusion models and incorporating techniques like shrinking step sizes, the paper shows versatility and application potential across a range of generative modeling tasks.

### Weaknesses
While the paper includes theoretical comparisons, empirical validation on real-world datasets or benchmarks would strengthen the paper's claims regarding practical performance. Comparing accuracy, iteration complexity, and space complexity with existing SGMs on these benchmarks, as demonstrated in the experiments by Shih et al. (2024), would provide valuable insights into the practical advantages of the approach. Furthermore, the paper's analysis of space complexity, particularly concerning overdamped Langevin diffusion, lacks sufficient detail. The discussion of space complexity trade-offs should include a more rigorous analysis of memory requirements, especially in high-dimensional settings. The current analysis does not sufficiently address the practical limitations that might arise from increased memory usage, which could be a significant bottleneck in resource-constrained environments. A more detailed examination of memory scaling with respect to problem size and parallelization degree is needed to fully assess the method's feasibility. Finally, the paper does not provide a clear discussion of how the proposed parallelization strategy interacts with different hardware architectures, which is crucial for understanding its real-world performance.

### Questions
1. Regarding the sub-optimal space complexity resulting from the application to overdamped Langevin diffusion, could the authors clarify what hinders the analysis of their methods in the context of underdamped Langevin diffusion?

2. Considering that the authors demonstrate improved iteration complexity at the expense of slightly increased space complexity, a detailed cost-related analysis would be beneficial to more thoroughly discuss the trade-offs. Specifically, evaluating computational time and memory usage under the utility maximization problem could demonstrate how these factors affect performance in practical scenarios, which might inform the method's applicability in resource-limited environments.

Miscellany: In L.3 of Algorithm 1, the subscript should be written as $B\_{nh + mh/M}$ to avoid confusion.

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
The manuscript proposes a novel parallel simulation technique for sampling under isoperimetry and score-based diffusion models. It leverages a parallel Picard iteration approach that reduces iteration complexity compared to existing methods. By drawing parallels from scientific computation, particularly parallel initial-value problem solvers, the authors introduce a time-parallelized approach to improve sampling efficiency in high-dimensional settings. The manuscript provides theoretical proof for iteration and space complexity improvements and positions the technique as beneficial for tasks involving large data distributions.

### Strengths
**Novel Application of Parallel Picard Methods.** Adapting Picard methods for parallel sampling in high-dimensional contexts is innovative, particularly the integration of time-slice parallelization that challenges existing sequential frameworks.

**Strong Theoretical Contributions.** The manuscript rigorously addresses the theoretical guarantees of the proposed method. Its complexity bounds represent an improvement over established sampling methods, particularly with respect to the iteration complexity in the sampling task.

**Applicability to Diffusion Models.** The method has implications for score-based generative models (SGMs), which are widely used in machine learning applications. The proposed algorithm, therefore, has potential relevance in real-world applications like image generation and inverse problems.

### Weaknesses
 **Practical Feasibility of Assumptions.** The paper relies on several strong assumptions, including accurate score function estimates and Lipschitz conditions. While these are theoretically convenient, they may limit the method's applicability in practical scenarios where these conditions are challenging to achieve. Specifically, the assumption of a perfectly accurate score function is rarely met in practice, as score estimation is typically noisy and biased. Furthermore, the global Lipschitz condition on the score function is a strong requirement that may not hold for complex, high-dimensional data distributions, potentially leading to instability or divergence in the sampling process.

**Complexity of the Approach.** While the theoretical aspects are well-elaborated, the algorithm’s practical implementation seems complex. There is minimal discussion of the challenges in implementing this parallel algorithm, particularly regarding memory bandwidth and processing demands. The parallel Picard iteration, while theoretically appealing, may introduce significant overhead in terms of communication between parallel processes, and the need to synchronize these processes could negate some of the potential speedup. The manuscript lacks a detailed analysis of the practical trade-offs between the reduced iteration complexity and the increased communication and synchronization costs.

**Lack of Empirical Validation.** The manuscript lacks experimental results. Empirical tests comparing the proposed method with existing sampling techniques would provide crucial insight into its real-world performance and validate the theoretical improvements. Without empirical validation, it is difficult to assess whether the theoretical gains translate into practical improvements in sampling efficiency and quality, especially in comparison to established methods.

### Questions
**Space Complexity and Scalability.** Although the paper mentions an increased space complexity, it lacks a detailed discussion of how this would scale with large data distributions in practical applications. How feasible is this method for scenarios requiring substantial memory resources?

**Empirical Benchmarks.** Could the authors provide insights on the types of empirical tests they would recommend or any preliminary results? Testing on standard datasets or benchmarks in score-based generative models would be particularly valuable for evaluating this method’s efficiency.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies Picard method based discretization of Overdamped Langevin Dynamics and Diffusion Models. Picard method iterates over the entire trajectory in contrast to the Euler method which iterates point-by-point causally. Thus, Picard method is highly parallelizable and has received a lot of interest in the recent years for efficiently sampling from posterior distribution and from Diffusion models. 

This work introduces the parallel picard method which increases the parallelism compared to previous method and decreases the number of Picard iterations from $\mathsf{polylog}(d)$ to $\log (d)$.

### Strengths
[1] The paper has a clean exposition of prior work and background material.

[2] The main technique and the idea is clearly presented and the work proposes an interesting trade-off between number of iterations and number of parallel threads. The number of Picard iterations is nearly optimal. 

[3] The proof crisply analyzes the changing initial point of the Picard iteration inorder to fully parallelize it.

### Weaknesses
[1] There are no empirical evaluations of the proposed method. Diffusion models work with dimension $d \sim 10^4$. Providing an algorithm which requires $d/\epsilon^2 \log (d/\epsilon^2)$ parallel threads with $\log(d/\epsilon^2)$ iterations instead of $d/\epsilon^2$ parallel threads with $\log^2(d/\epsilon^2)$ iterations seems ineffective/ vacuous since such a degree of parallelism cannot be achieved in the first place. Therefore, the relative merit of the currently proposed algorithm has to be established empirically in practical settings. It would help the case made by the paper if suitable empirical evaluations are included.

[2] Since the algorithmic modification proposed in the work is straightforward, and there are no empirical evaluations, the main technical contribution of the paper is the proof. The paper has very little exposition of proof techniques. It would be helpful to add a deeper discussion of this.

[3] The tables 1 and 2 can be improved by stating the exact polylog factors of $d$ in prior works. This is important since the main improvement claimed in the manuscript is the improvement in these factors. I found the comparison to underdamped Langevin dynamics presented together with the results for Overdamped Langevin dynamics in Table 1 very confusing. Consider splitting these comparisons or making it more clear. Similarly, comparison of SDE based methods to ODE based methods in Table 2 is also confusing.

### Questions
[1] Address the questions/ concerns raised in the Weaknesses section.

[2] In line 228, the equation description picard iteration, the index i appears both in the RHS as well as inside the summation. This cannot be correct. Please fix this update.

[3] In equation (1), is there a $\sqrt{2}$ missing in the diffusion term ? Without this, the stationary distribution cannot be $\mathcal{N}(0,I)$. 

[4] In lines 210-212, it is stated that the reverse process contracts exponentially as per the work of Huang et al 2024. From my reading of the work, I could not find any results in the referenced work which makes this claim. Can you please elaborate?

[5] In Page 4, the score function for SGMs is assumed to be bounded. This seems like a stringent assumption. Can you elaborate and compare this with the assumptions made in prior works ?

### Soundness
3

### Presentation
4

### Contribution
2
