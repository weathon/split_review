# Memory-Pruning Algorithm for Bayesian Optimization with Strict Computational Cost Guarantees

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Bayesian Optimization (BO) is a powerful tool for optimizing noisy and expensive-to-evaluate black-box functions, widely used in fields such as machine learning and various branches of engineering. However, BO faces significant challenges when applied to large datasets or when it requires numerous optimization iterations. The computational and memory demands of updating Gaussian Process (GP) models can result in unmanageable computation times. To address these limitations, we propose a new Bayesian Optimization algorithm with memory pruning (MP-BO), which restricts the maximum training data size by acquiring new queries while concurrently removing data points from the training set. This approach guarantees a maximum algorithmic complexity of $\bigO(m^3)$, where $m \ll n$ is a fixed value and $n$ represent the size of the full training set. The pruning strategy ensures reduced and constant memory usage and computation time, without significantly degrading performance. We evaluate MP-BO on synthetic benchmarks and a real neurostimulation dataset, demonstrating its robustness and efficiency in scenarios where traditional BO would fail under strict computational constraints. Our results suggest that MP-BO is a promising solution for applications that require efficient optimization with limited computing resources.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes a memory and computational cost efficient version of Bayesian Optimization algorithm by pruning the sampled data points (training data points). They work suggests various methods for pruning the data points - i) randomized pruning, ii) First in first out pruning. The work also suggests the theoretically inspired pruning method which focuses on minimal reduction of KL divergence between the updated posterior containing the point and not containing the point but does not pursue this dues to the computational costs linked with the method. Further, the computation of GP uncertainty is updated to follow the minimum of the posterior with and with out the updated point. The algorithm is tested against the benchmark algorithms and on the real world neurostimulation dataset.

### Strengths
The paper presents a memory and computational cost efficient BO algorithm which is tested on benchmark and real world data set.

### Weaknesses
Though the work presents a method for memory pruning, there is no theoretical backing for the algorithm. Also, absence of the analysis makes the algorithm less appealing.
Further, when computing the minimum of standard deviation $\min(\tilde{\sigma}(x), \sigma(x))$ the old standard deviation needs to be stored for every query which would be an additional memory cost if the old kernel matrix is stored else would be additional computational cost at each iteration if only the data points are stored.
Additionally, why is the suggested methods not computing the max of means i.e, $\max(\tilde{\mu}(x), \mu(x))$, wouldn't this result in better optimization strategy?
They flow of paper can be organized better to give more details about the algorithm. There is just one line about the randomized pruning strategy used in the algorithm, instead since this is the most novel part of the algorithm this needs to be a different subsection with the details of all the strategies tried and with insight on why the randomized strategy performed well.

### Questions
please look at In the weakness section.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a memory-pruning Bayesian optimization method that improves the running speed of BO.
The idea is discard a subset of the training data so that the training data size stays constant during Bayesian optimization.
Concretely, the author propose randomly deleting a training data after adding each new data point to the training set after certain iterations.
The authors verify this strategy improves the running speed and does not degrade the BO performance too much compared to vanilla BO.

### Strengths
- The proposed method is simple, intuitive, and easy to implement.

### Weaknesses
 - Motivation is unclear / weak experiments.
While I agree BO is costly when the number of training data is large, all experiments in the paper have at most 200 data points (including the real-world experiments).
Training data of these sizes can be handled trivially by modern computers.
Thus, I am not sure if there is a need dropping training data on these problems.

- Lack of baselines.
The authors propose reducing the data size by dropping training data randomly.
However, there is no other baselines to access how good or how bad this idea is.
Clearly, randomly dropping training data is one of the easiest heuristics that one can come up with.
At this stage, I am not sure if this paper reveal any interesting insights of the problem that the authors are trying to solve.

### Questions
In Line 15 of Algorithm 1, how enumerate all \\(x \in \mathcal{X}\\)? Is the domain discretized?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
To address the computational and memory challenges of Bayesian optimization (BO) on large datasets, this article introduces a Bayesian optimization algorithm with memory pruning (MP-BO). MP-BO limits the maximum size of the training data by selectively updating the data used for the proxy model. When the dataset exceeds a predefined limit, new queries are incorporated while older data points are removed from the training set. The algorithm’s performance was validated across various aspects on both synthetic and real-world datasets, demonstrating its effectiveness.

### Strengths
Completed work: The article is clearly written, and the charts used for the presentation are visually appealing.
Clear motivation: The memory pruning strategy could be valuable in memory-constrained scenarios.

### Weaknesses
Weakness:
Unclear notation: In the whole paper, sometimes mathematic notation happens without explanation which hinder the understanding of readers seriously. For example: “m” in the abstract, author just treat it as a “fixed value” but did not make it clear what value it is. Also in the algorithm, the author write u without any further explanation.

Insufficient illustrations: According to my understanding of MP-BO, the most important point is how to find the point to be deleted, but in the paper, the author just mentioned use KL-divergence to decided but doesn’t provide any mathematical equations to explain how to use the KL-divergence. Furthermore, the paper lacks a clear explanation of how the KL-divergence is calculated between data points in the context of Gaussian Processes, specifically how the predictive distributions are used to compute the divergence.

Also, as mentioned in the first section, the author says “m” is a fixed value, but how to decide the value of m? And same for q^* 

Baseline implementation: There are too few empirical comparison methods, only with Vanilla BO. There is plenty of literature on BO, I wonder whether the author consider comparing MP-BO with other BO methods?

### Questions
What is the specific methodology for applying KL-divergence in this context?

How is the value of  $q^*$  determined?

Is the experimental time for the Michalewicz 4D and Hartmann problems presented in Figure 6 insufficient? The results suggest that neither method has fully converged.

What considerations are there for high-dimensional outputs and alternative acquisition functions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores an extension of the GP-UCB algorithm for optimizing cheap-to-query black-box functions in discrete domains. By pruning the memory of observed points in the exact GP model, the proposed approach achieves faster computation at the cost of some performance. However, the empirical results show that the performance degradation is minimal in the tasks the authors tested. This algorithm proves useful when the objective function is inexpensive to query, there is an upper bound on the computational overhead for selecting the next query—particularly in scenarios where time is plentiful but monetary cost is high, and longer iteration cycles are needed (otherwise this algorithm reduces to standard UCB).

### Strengths
- Explicitly upper-bounding the computation time is an important problem for optimizers in general, though Bayesian optimization may not be the first choice in such scenarios.
- The neurostimulation example is interesting and effectively highlights the context of limited computation time. However, the need for longer iteration cycles is not entirely clear, which raises questions about the importance of sample efficiency in this case.
- The core idea is simple and easy to follow. However, the assumptions are dispersed throughout the text, and it is only later in the paper that we learn this method is limited to discrete domains.

### Weaknesses
 - **This algorithm is not a global optimizer**. 
It lacks the no-regret property that guarantees GP-UCB as a global optimizer. As shown in [1], the no-regret property is defined as $\lim_{T \rightarrow \infty} \frac{R_T}{T}= 0$, where $R_T := \sum_{t =1}^T r_t$ is the cumulative regret, $r_t$ is an instantaneous regret, and $t$ is the iteration step. This no-regret property assures that original GP-UCB algorithm is a global optimizer. However, this algorithm restricts the number of queries, i.e., $\lim_{T\rightarrow \infty} T = m$, meaning the regret never converges to zero. Intuitively, the GP uncertainty $\sigma$ is submodular with respect to the number of data points, allowing it to converge asymptotically for infinitely many queries. Unfortunately, this algorithm will not achieve no-regret. Therefore, the authors should clarify that this is a heuristic, similar to TurBO, which explicitly indicated this in the title (“local optimization”). The descriptions in line 323 are misleading in this regard.
- **Inaccurate complexity analysis**.
While the complexity analysis is correct for a single point $x_t \in \mathcal{X}$, in practice, the algorithm adopts a memorization step for $\sigma_t(\mathcal{X}), \sigma_{t-1}(\mathcal{X}) $, which requires 
$N = |\mathcal{X}|$ in a discrete domain. As a result, the total complexity is $\mathcal{O}(N m^3)$ for time and $\mathcal{O}(m^2 + 2 Nm)$ for memory. This makes the complexity quite comparable to that of sparse GPs. Since sparse GPs do not need to scan the entire domain, their complexity is $\mathcal{O}(M n m^2)$ for time, where $M$ is the number of iterations in the acquisition function maximizer (e.g., L-BFGS-B), and $m$ is number of inducing points. When $M \ll N$, sparse GPs are faster. Therefore, this new algorithm is not necessarily always superior to sparse GPs, and a more reasonable comparison between the two should be provided. (Sparse GP can also limit the computation time by setting appropriate $m$ and iteration $T$).
- **Why Bayesian optimization?**
Bayesian optimization may not be the first choice for optimizing cheap-to-query functions. As discussed earlier, this algorithm is not a global optimizer, but rather a heuristic approach. There are numerous other efficient heuristics for sample-efficient black-box optimization, such as CMA-ES, NES, and others, which should be considered for comparison. Additionally, if computational time is a significant factor, parallel computation (i.e., batch BO) could be a viable alternative. In environments where costs are low, cloud computing—similar to how ChatGPT operates—is also an option. As a result, the motivation for using this algorithm in such scenarios remains unclear.
- **The better baseline that is not included in the paper**. 
As the authors state, the goal is to balance computation time and convergence rate. However, this method seems to sacrifice the convergence rate too heavily, particularly since it loses the no-regret property. For example, [2] introduced a more principled approach to memory-pruning in GP-UCB, which includes regret analysis. This method achieves a similar computational time complexity of $\mathcal{O}(m^3)$ while still maintaining the no-regret property. Similarly, sparse GPs may also perform reasonably well. When the upper bound of computational overhead is known, we can use reverse calculation to determine the number of inducing points $m$, ensuring a better balance between computational efficiency and convergence.
- **Minor points.** Kappa is not fixed in GP-UCB. This should increase with iterations. Read [1] carefully.

### Questions
The questions in the above weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
