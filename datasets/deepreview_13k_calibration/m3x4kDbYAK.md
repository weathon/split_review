# Incremental Aggregated Asynchronous SGD for Arbitrarily Heterogeneous Data

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
We consider the distributed learning problem with data dispersed across multiple workers under the orchestration of a central server. Asynchronous Stochastic Gradient Descent (SGD) has been widely explored in such a setting to reduce the synchronization overhead associated with parallelization. However, prior works have shown that the performance of asynchronous SGD algorithms depends on a bounded dissimilarity condition among the workers' local data, a condition that can drastically affect their efficiency when the workers' data are highly heterogeneous. To overcome this limitation, we introduce the Incremental Aggregated Asynchronous SGD (IA$^2$SGD) algorithm. With a server-side buffer, IA$^2$SGD makes full use of stale stochastic gradients from all workers to neutralize the adverse effects of data heterogeneity. In an asynchronous implementation setting, the algorithm entails two distinct time lags in the model parameters and data samples utilized in the server's iterations. Furthermore, by adopting an incremental aggregation strategy, IA$^2$SGD maintains a per-iteration computational cost that is on par with traditional asynchronous SGD algorithms. Our analysis demonstrates that IA$^2$SGD achieves a consistent convergence rate for smooth nonconvex problems for arbitrarily heterogeneous data. Numerical experiments indicate that IA$^2$SGD compares favorably with existing asynchronous and synchronous SGD-based algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper borrows the idea from IGD and proposes an asynchronous algorithm for distributed optimization accompanied by the convergence guarantee under non-convex settings. This algorithm is featured by using historical gradient information.

### Strengths
This paper borrows the idea from IGD and proposes an asynchronous algorithm for distributed optimization accompanied by the convergence guarantee under non-convex settings. This algorithm is featured by using historical gradient information. 

The analysis doesn't rely on bounded data heterogeneity assumption. 

The convergence rate enjoys a speedup in the number of clients.

### Weaknesses
The analysis is conservative in terms of the step size. According to my understanding, the proof follows the strategy of FedAvg, which restricts them to small step sizes. Specifically, the step size is inversely proportional to the maximum delay, which seems overly restrictive, especially when considering the deterministic case. The paper I showed to you, Freya PAGE: First Optimal Time Complexity for Large-Scale Nonconvex Finite-Sum Optimization with Heterogeneous Asynchronous Computations, can achieve a larger step size in the deterministic setting, which is a significant advantage. This raises concerns about the practical applicability of the proposed method in scenarios where larger step sizes could lead to faster convergence. It is not clear why the step size needs to be inversely proportional to the maximum delay, and this needs further justification.

From an optimization perspective, I was curious about the convergence rate under a deterministic setting. Based on my understanding of your proof framework, I think it cannot achieve a good rate under a deterministic setup. In addition, I think the learning rate used here in a deterministic setup will be less than the conventional distributed optimization.

In addition, I don't think your analysis significantly differs from fedavg. The technique is quite similar from my perspective. The bounded delay ($\tau_{\max}$) plays a similar role as the number of local updates as in the analysis of FedAVG. You claim that you "introduce a novel decomposition technique", I agree with the author that's a difference. But from my perspective, I feel most of the proof in the appendix is similar.

### Questions
Can you show how the step size will look like when you reduce your analysis to a deterministic setup? Can you compare the step size choice used in your work to the one used in the existing works? e.g., Freya PAGE: First Optimal Time Complexity for Large-Scale Nonconvex Finite-Sum Optimization with Heterogeneous Asynchronous Computations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Incremental Aggregated Asynchronous SGD, an algorithm that improves the performance of asynchronous SGD on heterogeneous environments. With a server-side buffer, the proposed algorithm can neutralize the adverse effects of data heterogeneity. The theoretical analysis show that the proposed algorithm achieves a consistent convergence rate for smooth nonconvex problems for arbitrarily heterogeneous data. The experiments show that the proposed algorithm has good performance.

### Strengths
1. This paper proposes Incremental Aggregated Asynchronous SGD, an algorithm that improves the performance of asynchronous SGD on heterogeneous environments. With a server-side buffer, the proposed algorithm can neutralize the adverse effects of data heterogeneity. 

2.The theoretical analysis show that the proposed algorithm achieves a consistent convergence rate for smooth nonconvex problems for arbitrarily heterogeneous data. 

3. The experiments show that the proposed algorithm has good performance.

### Weaknesses
I have 2 major concerns:

1. In overall, the proposed algorithm is very similar to SAGA (the one cited in Appendix A, additional related works). I would actually say that the proposed algorithm is indeed SAGA, except that: the participating worker is not picked in a uniformly random manner but with some bounded delay ($\tau_{max}$); and the new gradient itself could have some delay. With the assumption of bounded delay ($\tau_{max}$), the new settings do not really make too much trouble to convert the theoretical analysis of convergence from SAGA to IA2SGD. Specifically, the core update mechanism, involving a correction term based on past gradients, remains fundamentally the same. The analysis seems to primarily involve accounting for the delay, which, while requiring careful handling, doesn't introduce a fundamentally new theoretical challenge beyond standard techniques for analyzing delayed updates. Thus, the overall novelty of the proposed algorithm and the corresponding contribution of the theoretical analysis is limited.

2. The experiment results do not show significant improvement compared to some of the baselines. According to Figure 3, in all cases IA2SGD performs same as FedBuff (at least I could not see an obvious gap at the end of training), and in some cases IA2SGD performs similar to vanilla ASGD. This lack of clear empirical advantage, especially given the added complexity of the proposed method, weakens the overall contribution. The fact that IA2SGD does not consistently outperform simpler baselines raises questions about its practical utility.

### Questions
1. Could the authors explain in details about the difference between the proposed algorithm and SAGA, in both the algorithm itself and the theoretical analysis of convergence?

2. Could the authors justify the experiment results compared to FedBuff and Vanilla ASGD?

### Soundness
3

### Presentation
3

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
The authors address a distributed learning problem with smooth nonconvex objective function under a central server orchestration, and introduce the Incremental Aggregated Asynchronous SGD (IA2SGD) algorithm. This approach uses a server-side buffer to utilize stale stochastic gradients from all workers, aiming to mitigate the negative impact of data heterogeneity. The algorithm maintains a per-iteration computational cost similar to traditional asynchronous SGD algorithms and has a convergence rate independent of the degree of data heterogeneity, distinguishing it from prior asynchronous SGD methods that often impose a bounded dissimilarity condition. Numerical experiments show that IA2SGD can outperform both asynchronous and synchronous SGD-based methods.

### Strengths
- The problem of distributed learning with heterogeneous data has been extensively studied, but IA2SGD appears to be a novel algorithmic approach.

- The paper is well-written, with clear visuals. However, some explanations could benefit from more technical precision (see Weaknesses).

- The problem addressed is practically relevant, especially given the challenges in distributed learning scenarios with heterogeneous client data and variable computation times. An important strength of this work is that its theoretical results are independent of data heterogeneity.

### Weaknesses
 - The convergence result in Theorem 1 appears impractical. The stepsize $\eta = \frac{1}{2} \sqrt{\frac{n (F(w^0) - F^*)}{L \tau_{\max} T}}$ relies on unknown quantities like $F(w^0) - F^*$, $L$, and $\tau_{\max}$, and hence needs substantial tuning. I acknowledge that this is the case for many gradient-based algorithms, and hence is not a critical flaw. However, Theorem 1 contains a lower bound on $T$, requiring $T \geq 1024 L (F(w^0) - F^*) n \tau_{\max}$ regardless of the desired accuracy, making the theory seem weak. This lower bound on $T$ is particularly concerning because it scales linearly with the number of workers $n$ and the maximum delay $\tau_{\max}$, suggesting that the algorithm may require an impractically large number of iterations to achieve convergence in realistic distributed settings. Furthermore, the dependence on the initial suboptimality $F(w^0) - F^*$ makes the bound difficult to interpret in practice, as this quantity is typically unknown.

- The paper asserts that previous asynchronous methods require bounded data heterogeneity. However, this is not entirely accurate, as the work in [1] addresses similar optimization problem without assuming data similarity. The method in [1] achieves optimal time complexity with smoothness, unbiasedness, and bounded gradient variance assumptions. Given these theoretical results, a comparison between IA2SGD and the Malenia SGD method from [1] is essential in both theoretical and practical contexts. The Malenia SGD method, in particular, is designed to avoid delays in parameter updates, which is a significant distinction from IA2SGD. The paper should clarify how IA2SGD's approach to handling delays compares to methods that explicitly avoid them.

- The reliance on a maximum delay assumption limits the algorithm’s applicability. In practical federated learning, some clients may become unavailable, making delay bounds infinite. Some methods do relax the bounded delay assumption (e.g., [2], [3]), and instead assume bounded dissimilarity of local objective functions. The paper does not discuss the trade-off between these assumptions; namely, that one can either assume bounded data dissimilarity with arbitrary delays or bounded delays with unbounded heterogeneity. Either approach has limitations, and I do not think that one of these assumptions is superior to the other. This trade-off should be addressed more thoroughly. The paper should also discuss the implications of the maximum delay assumption on the algorithm's robustness to stragglers or intermittent client failures.

- The algorithm requires additional memory allocation for a $d$-dimensional vector at both the server and each worker. While server memory constraints may not be an issue, this could limit the method’s applicability for memory-constrained clients. This additional memory requirement could be a significant limitation in resource-constrained environments, especially when dealing with high-dimensional models. The paper should explore alternative implementations or modifications to mitigate this memory overhead, such as server-side memory management strategies.

### Questions
- Could the authors elaborate on the points mentioned in the Weaknesses?

- What is the origin of the dependence on $\sigma$ in the last line of Table 1, as it does not appear to follow from Theorem 1?

- Could the authors clarify why reusing outdated stochastic gradients would improve convergence rates? Intuitively, one might expect performance to degrade with increasingly stale updates.

- It is not entirely clear to me why the authors highlight the "dual-delayedness" of the updates. It seems that sample delays are already present in standard ASGD, as samples are processed after each client completes a job, creating a delay similar to that in IA2SGD. Overall, the term "dual delay" seems misleading since workers are processing freshly sampled data points.

- In lines 108-109, the authors mention that "$\xi_i^t \sim \mathbb{P}_i$ is indexed by $t$ to indicate that this particular data sample has not been utilized by the server prior to iteration $t$". Doesn't this imply single-pass data usage?

- Line 114 states that without delays, $\tau_i(t)=1$ for all $i$, implying each stochastic gradient is evaluated at the most recent model parameters. However, this would require restarts of client computations, which seems to contradict asynchronous operation.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new asynchronous SGD-based algorithm. Allowing each worker and server to have a memory term (buffer), the algorithm can provably converge without data heterogeneity bounds. The authors provide convergence guarantees for smooth non-convex functions and demonstrate the practical performance in training CNN model on CIFAR10 dataset simulating gradient computation time from truncated normal distribution and data heterogeneity by allocating data according to Dirichlet distribution.

### Strengths
- The authors provide a new asynchronous algorithm that provably converges without imposing data heterogeneity which is essential for applications such as Federated Learning
- The rate improves with the number of workers $n$
- The authors demonstrate the performance in training CNN model on CIFAR10 dataset varying data heterogeneity by Dirichlet data allocation

### Weaknesses
 - Bad dependency on the maximum delay $\tau_{\max}$ (we can create some example with $\Delta=L=1$ for that to satisfy the requirement on $T$ from Theorem 1; although this lower bound on $T$ is not needed to derive the convergence rate for the proposed algorithm). If the slowest worker responds once in the training, i.e. $\tau_{\max} \sim T$ then the theory shows no convergence while some previous algorithms can still achieve the convergence in this extreme case.
- The empirical results show that the proposed algorithm might be affected by the heterogeneity (the accuracy after the same number of iterations/time increases when the heterogeneity decreases, i.e. the problem becomes more homogeneous).
- The experiments do not show the improvement of the proposed algorithm over other algorithms (those convergence guarantees are affected by the heterogeneity bounds). The proposed algorithm performs similarly to FedBuff and vanilla ASGD even when the heterogeneity is high. These observations contradict the theory
- Some important related works are missing [1,2]. The methods from these papers also do not require data heterogeneity bounds but the comparison is not provided in this work.



### Questions
- It is not clear why the analysis needs two sequences $\tau_i(t)$ and $\rho_i(t)$. Isn't there a bijection between them? I guess it would be needed if we were allowed to assign a new job to a worker different from the one who finished the computations.
- Could the authors show that the proposed method can have a better dependency on $\tau_{\max}$ under stronger assumptions (e.g., bounded gradients)? Can we get both better dependency on $\tau_{\max}$ and no requirement to bound the data heterogeneity simultaneously? 
- Could the authors provide a detailed comparison with algorithms from [1,2]?
- The first line in Figure 4 is not readable. It is hard to distinguish the variance of algorithms. Could the authors make them more readable? Could you please clarify why there is no variance in accuracy plots for some algorithms (FedBuff, Synchronous SGD, Uniform ASGD)? Why does the red shaded area (variance) around the red dashed line in Figure 4 (second line) look so weird? Sometimes red dashed line is not inside red shaded area.
- I find it weird that uniform/shuffled ASGD performs worse than vanilla ASGD. Is there any particular reason for that since from theory vanilla ASGD converges to $\zeta^2$-neighbourhood of the solution while uniform/shuffled ASGD should converge exactly?
- The rate of the proposed algorithm in the table looks weird: why is there $\sigma$ in the denominator of the second term?
- Why is the accuracy so low? All algorithms barely achieved 50 % accuracy which I found low for the CIFAR10 dataset. Could you present the results when the algorithms' accuracy stops increasing after a sufficient amount of ''time''?
- Could the authors provide the empirical comparison against Melania SGD?

### Soundness
3

### Presentation
2

### Contribution
2
