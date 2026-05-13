# Tight Time Complexities in Parallel Stochastic Optimization with Arbitrary Computation Dynamics

- Decision: Accept
- Scores: 8, 8, 5, 5

## Abstract
In distributed stochastic optimization, where parallel and asynchronous methods are employed, we establish optimal time complexities under virtually any computation behavior of workers/devices/CPUs/GPUs, capturing potential disconnections due to hardware and network delays, time-varying computation powers, and any possible fluctuations and trends of computation speeds. These real-world scenarios are formalized by our new \emph{universal computation model}. Leveraging this model and new proof techniques, we discover tight lower bounds that apply to virtually all synchronous and asynchronous methods, including \algname{Minibatch SGD}, \algname{Asynchronous SGD} \citep{recht2011hogwild}, and \algname{Picky SGD} \citep{cohen2021asynchronous}. We show that these lower bounds, up to constant factors, are matched by the optimal \algname{Rennala SGD} and \algname{Malenia SGD} methods \citep{tyurin2023optimal}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper provides new lower bounds for parallel optimization where the workers can have arbitrary delays. While this setting has been studied in many previous works, and there are known optimal analyses of algorithms such as asynchronous SGD, the paper studies a more general computation model where the delays are not only arbitrary but can also evolve in a structured or unstructured manner over time. Under this model, the paper provides tight lower bounds for many problems of interest, such as periodic delay patterns (common in cross-device federated learning), random device outages, etc. The paper studies homogeneous and heterogeneous distributed setups, matching the best-known upper bounds (up to log factors) in both settings. Overall, the paper closes important gaps in parallel optimization and I support accepting the paper.

### Strengths
1. **Closes significant gaps**: The paper closes critical gaps in parallel optimization by providing lower bounds that match the convergence rates for existing algorithms, meaning they are tight. I like that the paper makes these connections explicit, providing relevant corollaries for upper bounds where needed. 
2. **Good writing**: The paper's writing is clear and rigorously describes all results. In notationally heavy parts, such as while introducing the computation model, the paper provides the rough intuition for each term/unit/state, which is very helpful. 
3. **Exhaustive coverage**: Another good thing is that the paper considers both homogeneous and heterogeneous settings relevant to applications like federated learning, which is uncommon in much of the literature on asynchronous optimization, which focuses on data center settings. Overall, the paper's coverage is exhaustive, with both non-convex and convex results.

### Weaknesses
There are no significant weaknesses in this paper, but I think the following may help improve the writing and exposition:
1. See my question about [[3]](https://arxiv.org/abs/2305.12387) below.
2. See my question about the graph-oracle framework [[4]](https://arxiv.org/abs/1805.10222). Adding a comparison in the appendix would make the paper even more exhaustive.
3. Since the paper does not consider data heterogeneity, it can not recover the homogeneous lower bound. For instance, in the fixed computational power model, (19) can not recover (12). From reading the proof, I raise this issue because the heterogeneity across the workers (in the lower bound) looks pretty adversarial, and it is unclear to me what practical settings will have such heterogeneity. Theoretically, I understand there is no reason the lower bound would not use the full power of the adversary. This is why, theoretically, I think the fully heterogeneous setting is a bit too pessimistic. For instance, if we restrict the heterogeneity to disallow arbitrary division of data blocks ($h_j$'s), the lower bound should be worse (i.e., go down).

### Questions
1. I am unsure if I understand the difference between Theorems 6.1 and 6.2. Why does it matter if the functions are randomized v/s not? The inner/max player can always put all their weight on the worst functions for a given algorithm.
2. Can the authors comment on what Theorem 6.2 (or 6.1) implies for the partial participation setting in Federated learning (as studied in papers such as [[1]](https://arxiv.org/abs/2008.03606), [[2]](https://openreview.net/forum?id=SNElc7QmMDe)), where sampling from a meta distribution of users is standard?
3. Could the authors provide a detailed comparison against [[3]](https://arxiv.org/abs/2305.12387) regarding the main difference in the lower bound proof techniques while highlighting which delayed feedback settings can not be captured by their lower bound? It also seems that much notational/computational heavy loading was already done in this published paper.
4. One benefit of the graph oracle framework [[4]](https://arxiv.org/abs/1805.10222) is that it is easier to describe the information flow between different oracle queries between different time steps and agents, compared to using the states like the authors do in their computational model. Could the authors describe what can be captured in their model that can not be captured in the graph oracle model? What do their lower bounds say about existing gaps in the graph oracle framework?
5. Can the authors highlight in their proof sketches or at least in the appendix why the techniques used in the heterogeneous setting can not recover the homogeneous results under some notion of data heterogeneity? For instance, second or first-order heterogeneity notions combined [[2]](https://openreview.net/forum?id=SNElc7QmMDe) could help interpolate between these two settings (given the hard instances are similar to the usual zero-distributed lower bounds). Or is there any other restriction on the adversary that would make the lower-bound construction less pessimistic?

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
This work studies distributed stochastic optimization in a parallel and asynchronous setting. In the literature, there is an assumption that all workers operate at a stable and uniform speed, which is unrealistic in practice. This work extends the framework to account for arbitrary computational capacities of workers, capturing their instability and time-varying nature. It then analyzes this generalized framework by deriving both lower and upper bounds.

### Strengths
-The paper considers a realistic scenario for analyzing distributed stochastic gradient descent by introducing a universal computation model. This model is general and can capture unstable, time-varying random workers.

- It defines a class of algorithms within this new framework and derives tight lower bounds achievable by optimal algorithms.

- The paper also connects previously developed algorithms for distributed stochastic gradient descent, showing that they remain optimal in this new setting.

### Weaknesses
The paper lacks numerical results and experiments, which would strengthen its contributions.

The paper does not address the communication aspects of the distributed stochastic gradient descent. Specifically, it assumes that when a worker computes a stochastic gradient, it is instantaneously broadcast to all other workers. This assumption is unrealistic in practical distributed settings, where communication bandwidth limitations and straggler effects can significantly impact performance. The model should consider scenarios where communication bottlenecks exist, or where, due to stragglers, communication may fail, preventing the message from being broadcast.

### Questions
Do you also consider a model for communication bandwidth? From what I understand, when a worker computes a stochastic gradient, it is broadcast to all other workers. Do you account for situations where there is a communication bandwidth bottleneck or where, due to stragglers, communication may completely fail, preventing the message from being broadcast?

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
3

### Summary
This paper analyzes the time and oracle complexities of distrusted stochastic gradient descent. To approach this problem, the authors proposed a general computation model where the stochastic gradient is accessed through a set of workers that have different computational speed. In contrast to the classical oracle complexity results for SGD, this work considers an additional level of complexity that the time spent for each oracle access may be different. Then, the authors proved lower bound for the time complexity under the proposed setting and then provided two algorithms that match the lower bound.

### Strengths
This paper offers a very detailed analysis for distributed SGD 
- I agree with the author's claim that their proposed computation model is in some sense "universal" because it greatly extends the model considered by the previous works such as [1].
- For the proposed setting, this paper offers matching lower and upper bound, thus provides a complete narrative for this problem.

I appreciate that the author does a good job explaining all of the mathematically technically and despite the verbosity required for the very general setting, the definitions in this paper do not take major effort to follow.

The introduction is direct and concise and I immediately know what kind of results I should expect to see in the technical sections.

[1] Tyurin A, Richtárik P. Optimal time complexities of parallel stochastic optimization methods under a fixed computation model. Advances in Neural Information Processing Systems. 2024.

### Weaknesses
In terms of organization, I suggest that the examples should be moved forward. Currently, the statements of Theorem 5.1 and 6.1 are very long and hard to digest. Having the examples immediately following these theorems would be appreciated. Also, since Them 5.1 and 6.1 are implicit due to the generality of the setting, it could be useful to make some plots for a specific problem instance (say for the fixed computation model) so it is easier to parse the implications of these results.

For equations (12) (13) and (15), I think the minimum is always at $m=1$ and therefore redundant?

The proof sketch in Section 7 is not helpful at all. In particular, I want to see the "worst case function" being spelled out. From reading the full proof, this step is highly nontrivial and I would like to see some intuition. Also, on line 486, I think you meant "first coordinate." The random variables $\eta_k$ should be defined earlier in that paragraph. Lastly, I don't understand Section 7.2 at all even after multiple re-reads, in particular, I am left with a feeling with that something important was left out between lines 517 and 522.

Lastly and most importantly, **I do not think this paper has sufficient delta from earlier work [1].**
- From what I can tell, Theorems 6.4 and A.2 from [1] correspond exactly to Examples 5.4 and 6.5. Since the problem setup is quite complicated, it is important for the authors to justify that the added generality actually leads to some meaningful implications. Not having any further examples beyond 6.5 for the heterogeneous setting does not help the cause.
- And there seem to be a major reuse of proof techniques between the two papers. The proof of Theorem 5.1 up to equation (25) is almost a line-by-line reproduction of the existing analysis in [1]. While I am in no way suggesting any ill intent from the authors, I want to hear from the authors what are the main technical difficulties going from [1] to their proofs.

In light of these observations, I am hesitant to recommend  an accept because this paper seems to a straight extension of an earlier work [1] that added a lot of mathematical complexity but without too much of new insights. I think the amount of new contribution is insufficient for a new conference paper but could be worthwhile as a journal submission. So I will give score of **5** for the time-being.

### Questions
I am happy to hear from the author's response to my main concern that how this work adds significant value over [1]. If the authors convince me to change my mind during the rebuttal process, then I expect the authors to incorporate those discussion into the final version of the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the challenges and establishes optimal time complexities for distributed stochastic optimization methods that utilize parallel and asynchronous computation. The authors introduce a universal computation model that captures the real-world scenarios of fluctuating computation speeds, hardware and network delays, and other irregularities often encountered in parallel computing environments. They apply this model to demonstrate tight lower bounds for both synchronous and asynchronous optimization methods, and highlight that these bounds are closely matched by the Rennala SGD and Malenia SGD methods.

### Strengths
1. The paper proposes a new computation model that more realistically simulates the computational irregularities of distributed systems, which advances over previous models that assumed stable and uniform computation speeds.
2. The analysis encompasses a broad range of stochastic optimization methods and considers both homogeneous and heterogeneous computing environments.

### Weaknesses
1. The theoretical results, while comprehensive, may be too complex to be applied to practical algorithms. This complexity could limit their usability for practitioners who require simpler and more accessible tools for system design and analysis. Consequently, the tight lower bounds for time complexities are primarily of theoretical interest and provide limited insight into the potential performance improvements achievable with parallel stochastic optimization methods. Specifically, the paper does not clearly articulate how the derived time complexities translate into actionable guidelines for practitioners choosing between different optimization methods or parameter settings in real-world distributed systems. The lack of concrete examples or case studies further exacerbates this issue.
2. The paper does not provide sufficient discussion on the limitations of the universal computation model. Are there any properties in parallel or distributed systems that fall outside the scope of this universal model? For example, the model assumes that computation speeds are independent of the data being processed, which might not hold in practice where data-dependent computations can introduce significant variability. Furthermore, the model does not explicitly account for the impact of network congestion or packet loss on the overall performance, which can be a major factor in distributed environments. It is also unclear if the model can capture the effects of stragglers, i.e., slow workers that can significantly delay the overall computation.

### Questions
1. Does the computation power characterize server’s computation speed? 
2. In Methods 3 and 4, is the communication time between the workers and the server taken into account? In practical systems, it may take a significantly longer amount of time for a worker to transmit a gradient than to compute it. How does the universal computation model account for this?
3. Line 209: What does $\mathcal{D}$ mean?

### Soundness
3

### Presentation
3

### Contribution
3
