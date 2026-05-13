# Achieving Dimension-Free Communication in Federated Learning via Zeroth-Order Optimization

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Federated Learning (FL) offers a promising framework for collaborative and privacy-preserving machine learning across distributed data sources. 
However, the substantial communication costs associated with FL significantly challenge its efficiency. 
Specifically, in each communication round, the communication costs scale linearly with the model's dimension, which presents a formidable obstacle, especially in large model scenarios. 
Despite various communication-efficient strategies, the intrinsic dimension-dependent communication cost remains a major bottleneck for current FL implementations.
This paper proposes a novel dimension-free communication algorithm -- {\alg}, which leverages the zeroth-order optimization techniques and reduces the communication cost from $\mathcal{O}(d)$ to $\mathcal{O}(1)$ by transmitting only a constant number of scalar values between clients and the server in each round, regardless of the dimension $d$ of the model parameters.
Theoretically, in non-convex functions, we prove that our algorithm achieves state-of-the-art rates, which show a linear speedup of the number of clients and local steps under standard assumptions. With additional low effective rank assumption, we can further show the convergence rate is independent of the model dimension $d$ as well.
Empirical evaluations, encompassing both classic deep learning training and large language model fine-tuning, demonstrate significant reductions in communication overhead. 
Notably, {\alg} achieves this by transmitting only around 1MB of data in total between the server and a client to fine-tune a model with billions of parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors consider the practical problem of communication costs in federated learning with increasingly large models especially in the era of LLMs. The authors propose DeComFL, which decomposes the local gradient updates from the clients into a scalar magnitude and a pseudo-random perturbation vector. Since the pseudo-random perturbation is recoverable with known seeds, only the scalar magnitude and the random seed are required to be transmitted during each round of FL training, reducing the communication cost to $O(1)$. The author further provides convergence analyses of the proposed algorithm with and without a low effective rank assumption. Empirical experiments show competitive test accuracies and significantly reduced communication costs for DeComFL.

### Strengths
1. The paper is generally well-written and has a good flow.
2. The convergence analysis is necessary and duly provided. The discussion on the effective rank assumption to improve the pessimistic convergence bound is interesting. I did not check through the details for the correctness of the proof.
3. The algorithm design is sound.

### Weaknesses
1. I am not convinced about the critical role of zeroth-order optimization in the problem setting to reduce communication costs. The authors consider the optimization of model parameters which is essentially white-box. The authors are “downgrading” to zeroth-order information for model updates when first-order information is accessible (since the whole model architecture and parameters are known), which may be suboptimal. Specifically, the use of a finite difference approximation of the gradient, as employed in zeroth-order methods, introduces approximation errors that could be avoided with direct gradient computation. This raises concerns about the efficiency of the optimization process, especially when compared to first-order methods that directly use the gradient.
2. Related to the question above, the authors claim in Line 63 that “decomposition into a gradient scalar and a perturbation vector” is a unique property of zeroth-order gradients. Please clarify and justify this. Can I achieve a similar effect (eventual convergence, though might be different rates) by projecting the first-order gradient to a specific direction of a perturbation vector? This projection would also allow for dimension-free communication by transmitting only the scalar projection magnitude and the random seed, similar to the proposed method. It is unclear why the specific form of zeroth-order gradient estimation is essential for this decomposition.
3. In related works, please clarify the similarities and differences between DeComFL and FedZO? Is DeComFL an extension to FedFL by exploiting the $\kappa$-effective rank assumption? The current discussion lacks a detailed comparison, making it difficult to understand the novelty of DeComFL compared to existing zeroth-order federated learning approaches. A more precise delineation of the differences is needed to fully appreciate the contributions of this work.
4. In Table 2, no doubt that the communication saving is substantial. However, the last column is misleading as it has a larger P than FedZO (4th column). I would prefer it removed to avoid confusion.
5. There is no validation of the practical assumption for effective rank. I suggest a comparison of the convergence rate of several differently-sized LLMs. If similar practical convergence rates are observed (with respect to communication cost, I understand the communication costs should be the same for differently-sized models), then $d$ is shown to be pessimistic.

### Questions
1. It is unclear to me why zeroth-order gradients are essential in the problem setting: The authors consider the optimization of model parameters which is essentially white-box. The authors are “downgrading” to zeroth-order information for model updates when first-order information is accessible (since the whole model architecture and parameters are known), which may be suboptimal.
2. Related to the question above, the authors claim in Line 63 that “decomposition into a gradient scalar and a perturbation vector” is a unique property of zeroth-order gradients. Please clarify and justify this. Can I achieve a similar effect (eventual convergence, though might be different rates) by projecting the first-order gradient to a specific direction of a perturbation vector?
3. In related works, please clarify the similarities and differences between DeComFL and FedZO? Is DeComFL an extension to FedFL by exploiting the $\kappa$-effective rank assumption?
4. In Table 2, no doubt that the communication saving is substantial. However, the last column is misleading as it has a larger P than FedZO (4th column). I would prefer it removed to avoid confusion.
5. There is no validation of the practical assumption for effective rank. I suggest a comparison of the convergence rate of several differently-sized LLMs. If similar practical convergence rates are observed (with respect to communication cost, I understand the communication costs should be the same for differently-sized models), then $d$ is shown to be pessimistic.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper uses zero-order optimization in federated learning for achieving communication-efficiency. The main idea is that since the update for zero-order optimization consists of (1) random direction sampled from a gaussian distribution and (2) magnitude 1-d value computed on the data, only (2) needs to be transmitted and (1) could be recovered by the server/other clients if they know the random seed, thus significantly reducing communication cost per each round of training.

The paper provides convergence guarantees of their proposed method, particularly showing that if the loss function has small effective rank, then convergence does not depend on the dimension of the problem d, but rather depends on the rank of the loss function. 

The paper additionally provides experimental verification of the proposed algorithm.

### Strengths
The problem tackled is interesting and important and the proposed method saves a lot of communication (order of 1000s in experiments). Theoretical analysis allows to reason about potential communication savings during the overall course of training. Experiments are done on large models (up to OPT-1.3 B).

### Weaknesses
1. The paper does not state how exactly the random seeds are chosen, which might affect the distribution of the generated sequence. 
As far as I know, random generators guarantee the distribution of sampling a sequence of numbers from the same generator initialized once at some random seed, however with each number having its own random generator with its own random seed, I am not sure what guarantees exist and I imagine it depends on the distributions of the random seeds and particular implementation of random number generator, i.e. if random seed are deterministically chosen in the increasing order (i.e. the next random seed is equal to s + 1, where s is the previous random seed), then the generated numbers probably won’t follow the gaussian distribution. Also, if the random seeds are sampled from the uniform distribution, it is unclear to me, which distribution will follow the generated vectors. 
Therefore, the authors should add a formal statement about the generated sequence of vectors and specify how to generate a sequence of random seeds.

2. In experimental comparison on MNIST, the learning rate is set as the same constant across all the algorithms and settings, which might favor some of the algorithms/settings. For fair comparison it would be better to tune the learning rate separately for each experiment. 

3. Experiments on OPT do not compare to the fine tuning with federated averaging. I am wondering, how close to the finetuning with fed avg can zeroth order optimization get. 

4. On Fig 3. FedAvg + Topk converges much faster than DeComFL in terms of the number of rounds, and it is only slow on the right plot because k is quite large. I am wondering, if you reduce k, so that FedAvg + Topk converge with similar speed as DeComFL, would ZO optimization still provide substantial communication savings compared to FedAvg + Topk for that smaller k?

### Questions
1. What is the difference between the result in Theorem 1 and the prior work that analyzed federated learning with zero-order optimization, e.g. (Fang et al., 2022)? As I understood, algorithmically your method is exactly very similar with only a difference of how direction gradients are samplied & how the communication is performed. Does it pose some extra challenges for the analysis? 

2. Why do all the $z_r^k$ are equal on different nodes? I think algorithmically nothing prevents $z_r^k$ to be different on different nodes? The server would just need m times more memory to save all of $z_r^k$. Would such a modification provide a faster convergence?

3. On lines 052-053 paper comments that “because the models become large, communication becomes a bottleneck” howether, for modern models the computation cost can scale quadratically with model dimension, while communication cost scales only linearly. See e.g. [1]. While I do believe communication cost is an important issue in federated learning, I would recommend rephrasing this sentence.

    [1] SWARM Parallelism: Training Large Models Can Be Surprisingly Communication-Efficient, Ryabinin et al. 

4. communication cost analysis - might not be accurate? 

5. I think $m$ was never introduced in the paper. I understood that $m = | C_r |$, but I didn’t find where it was defined. 

6. Could you give an intuition how large the server memory is for training some standard benchmarks? Is it bigger/smaller than saving the full model? 

7. I think setting $\mu$ as in Corollary 1 does not give the desired result, as the term $2 \mu^2 L^2 (d + 3)^3$ would still have d at the nominator instead of $\sqrt{d}$. 
8. In Assumption 4, which matrix norm do you use? 

9. In theorem 2 $d_{\kappa}$ wasn’t defined before. 

10. Could you also analyze local steps in Theorem 2? What is the difficulty? 

11. I think that condition $\kappa >> P$ could be replaced with just $\kappa > P$. 

12. In Theorem 2, why is setting round R sufficiently large allows to remove the $\sigma_G^2 + \sigma^2$ term?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses a federated framework using zeroth order (ZO) optimization called DeComFL. It improves the previous ZO method by Fang et al. (2022) because, in each iteration, DeComFL only uses a constant number of bits of communication for each agent.

The authors prove the standard convergence theorem and provide a corollary under the $\kappa$-effective rank assumption. Additionally, they present experiments on training DeComFL, comparing it to the traditional first order method and other zeroth order methods.

### Strengths
It is quite novel to see the use of a zeroth order method for federated learning, and this paper makes a valuable contribution to this area.

With small and clever modifications to the previous algorithm by Fang et al. (2022), this research effectively reduces the per-iteration communication costs to a constant for each agent. Supported by both theoretical and experimental evidence, this new method significantly outperforms FedAvg in terms of communications costs.

### Weaknesses
The assumption made in Theorem 2 is not very standard. I am not sure if $\kappa$ can be truly seen as $O(1)$ constant and independent from $d$. What will be the consequence if $\kappa$ will scale up with $d$, even if it is not $\Theta(d)$?

Minor:
1. I think the algorithm was stated for $P=1$. When reading pages 4 and 5, $P$ does not appear to be any part of the algorithm. It was confusing what role the constant $P$ plays in the algorithm.
2. In assumption 4, the second maximum should be over $\xi_{i,r}$? Could it be a typo?

### Questions
Can you provide any evidence for the low-rank assumption you made?

### Soundness
4

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
The authors propose a new approach to reducing communication overhead between a server and clients. They have developed a new algorithm that reduces the overhead using zero-order optimization techniques. Noting that in zero-order optimization, it is sufficient to send scalars between a server and clients (unlike first-order optimization, which requires sending vectors), they introduce a new method, called DeComFL, that works with function values. This method is validated by theory and experiments.

### Strengths
The paper addresses the significant problem of communication overhead in the field of Federated Learning (FL). Unlike many previous approaches, which typically focus on reducing the communication overhead of gradients, this paper proposes leveraging techniques from zero-order (ZO) optimization, where only function values, which are scalars, need to be transmitted. The idea is promising (though not new; see Weaknesses). I haven't checked the proofs in detail, but they, along with the final results, appear reasonable and clean.

### Weaknesses
Let me point to the weaknesses of the paper:

1. Unfortunately, I'm not sure if the authors are aware, but exactly the same idea to utilize Assumption 4 in the FL setting was in [1]. Albeit, [1] consider the gradient estimator 
$$\langle \nabla f_i(\cdot), z\rangle z$$
instead of (3) from this paper (if $\mu \to 0,$ they are equivalent); after that, the idea and the proof techniques are almost the same between this paper and [1]. The core idea of using random projections to reduce communication by transmitting only scalar values is present in [1], and while the specific gradient estimator differs slightly, the underlying principle and the resulting communication efficiency gains are very similar. The authors should more clearly differentiate their approach from this existing work, highlighting the novel aspects of their method beyond the specific form of the gradient estimator.
2. Additionally, the theory from this paper almost replicates the theory [2] adapted to the multi-client setting. The theoretical framework, particularly the convergence analysis, appears to be heavily influenced by [2], with the primary adaptation being the extension to a multi-client federated learning scenario. The authors should more clearly articulate the novel theoretical contributions beyond this adaptation, perhaps by demonstrating a unique analysis technique or a significantly improved convergence bound.
3. As a base method, the authors take the FedAvg method. While it is the most famous FL method in the literature, there are numerous more modern methods that should be discussed and compared to this approach (e.g. [3]). The choice of FedAvg as the sole baseline is limiting, as it does not provide a comprehensive evaluation of the proposed method's performance against state-of-the-art federated learning algorithms. The authors should include comparisons with more advanced methods that incorporate techniques such as variance reduction or adaptive learning rates to provide a more robust assessment of DeComFL's effectiveness.

### Questions
-

### Soundness
3

### Presentation
4

### Contribution
2
