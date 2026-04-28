# Byzantine Robustness and Partial Participation Can Be Achieved Simultaneously: Just Clip Gradient Differences

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
Distributed learning has emerged as a leading paradigm for training large machine learning models. However, in real-world scenarios, participants may be unreliable or malicious, posing a significant challenge to the integrity and accuracy of the trained models. Byzantine fault tolerance mechanisms have been proposed to address these issues, but they often assume full participation from all clients, which is not always practical due to the unavailability of some clients or communication constraints. In our work, we propose the first distributed method with client sampling and provable tolerance to Byzantine workers. The key idea behind the developed method is the use of gradient clipping to control stochastic gradient differences in recursive variance reduction. This allows us to bound the potential harm caused by Byzantine workers, even during iterations when all sampled clients are Byzantine. Furthermore, we incorporate communication compression into the method to enhance communication efficiency. Under quite general assumptions, we prove convergence rates for the proposed method that match the existing state-of-the-art (SOTA) theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a robust distributed algorithm against Byzantine attacks that allows partial client participation. While previously proposed methods require the participation of all clients to compute the aggregation rule and have a convergence guarantee, the proposed algorithm allows partial participation using gradient clipping and therefore limits the impact of the Byzantine clients, even if they form a majority in the set of subsampled clients at a given round. The authors provide a convergence guarantee for the proposed algorithm.

### Strengths
- The paper is clear and easy to follow.
- To the best of my knowledge, this is the first paper to allow partial participation for a robust distributed algorithm against Byzantine attacks.

### Weaknesses
 - Given that the main motivation for this paper is to allow partial participation because it is more natural in practice, as the authors point out, I would have expected to see some practical experiments to see how gradient clipping actually allow partial participation (and thus the sampling of a majority of Byzantine clients in some rounds) while maintaining good performance. It seems to me that even if clipping can control the impact of Byzantine clients, rounds where they are in the majority will still penalize learning. Do the authors have any insights or perhaps experiment results on the performance of the proposed algorithm?

 - In the algorithm, it is said that the clipping levels $\lambda_k$ are given as inputs, how is it possible since they depend on the value of $x^{k+1}$ and $x^k$ ?

 - How are the gradients clipped at the first iteration since $\lambda_0$ is not defined?

 - Can the authors explain why full participation Is needed in some rounds? Would it be possible to avoid full participation and use only partial participation in each round?

### Questions
In the algorithm, it is said that the clipping levels $\lambda_k$ are given as inputs, how is it possible since they depend on the value of $x^{k+1}$ and $x^k$ ?

How are the gradients clipped at the first iteration since $\lambda_0$ is not defined?

Can the authors explain why full participation Is needed in some rounds? Would it be possible to avoid full participation and use only partial participation in each round?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of partial participation in Byzantine robust algorithms for distributed learning. The authors introduce gradient clipping to limit the influence of Byzantine workers in rounds where they form a majority in the set of selected participants. They prove convergence rates, for a general algorithm featuring variance reduction and communication compression, and claim to match state-of-the-art theoretical results.

### Strengths
1. The problem of partial participation is not well understood in Byzantine robust machine learning, and this paper makes a promising step towards solving it by introducing gradient clipping. Also, the use of the latter method is novel in this context.

2. The technical content and proofs are sound.

### Weaknesses
My main concerns revolve around practicality, clarity, related work review, and assumptions.

### A. Practicality: 
* A.1. A major weakness of the paper is the absence of experimental results. I would expect at least experiments on simple tasks, given that the only addition in the proposed algorithm (compared to previous works) is gradient clipping, which is simple to implement. The lack of experiments makes it difficult to assess the practical performance and robustness of the proposed method, especially under different types of attacks and varying degrees of data heterogeneity.

* A.2. An important weakness in the theoretical analysis is the choice of the clipping parameter. For example, in Theorem 3.1, the clipping parameter $\lambda_{k}$ depends on the maximum local smoothness constant, the computation of which can be highly impractical. This dependence on a global smoothness constant makes the algorithm difficult to deploy in real-world scenarios where such constants are unknown or difficult to estimate. Moreover, the adaptive strategy for tuning the clipping parameter is not sufficiently justified or tested.

* A.3. For the variance reduction method employed to have a gradient oracle cost comparable to SGD, $p$ needs to be in the order of $\frac{1}{m}$ where $m$ is the number of samples per worker. However, my concern is that the excess (non-vanishing) term in (6) of the main theorem would increase proportionally to $m$, which is untight following the existing lower bounds, e.g. Karimireddy et al. (2022). This raises concerns about the practical scalability of the method, especially when dealing with large datasets and a high number of samples per worker.

### B. Clarity:
There are many clarity-affecting issues in the paper, which make the submission seem rushed:
 * Several quantities are undefined before they appear: $S_k$ and $g^k$ in the second paragraph of Section 2, $G^k_C$ in the first equation of Section 3
* How is $g^k$ initialized in Algorithm 2? Does arbitrary initialization work in theory?
* $n \choose k$ is incorrectly denoted in the second paragraph of Section 3, and correctly denoted elsewhere.
* The last sentence in Section 2 seems to be in conflict with Algorithm 1. In the latter, clipping is also performed at the worker level with probability $1-p$.

### C. Related work:

C.1. An important piece of related work is missing from the paper. Data & Diggavi (2021) have tackled the problem of partial participation (and local steps) in Byzantine robust distributed learning. It is essential to include a comparison with their work.

Reference: Deepesh Data and Suhas Diggavi. Byzantine-resilient high-dimensional SGD with local iterations on heterogeneous data. ICML 2021.

C.2. Some claims regarding related work, in the paragraph following Definition 1, are inaccurate: a standard aggregator (coordinate-wise trimmed mean) satisfies Definition 1.1 because it satisfies an even stronger robustness criterion as shown by Allouah et al. (2023). Please include this in the paragraph. Moreover, using Bucketing (Karimireddy et al., 2021) is known to amplify the Byzantine fraction, and this may be problematic when considering partial participation.

### D. Assumptions:

Some assumptions are poorly justified: there is no justification for why "popular [...] robust aggregation rules presented in the literature" verify Assumption 1. A formal, even simple, justification is important because the assumption seems necessary for the convergence theory.

### Questions
I am willing to raise my score if the authors address the weaknesses above. In particular:

1. How do you set the clipping parameters in practice, when you cannot compute smoothness constants? (see A.2)

2. How do your results compare to the work of Data & Diggavi (2021)? (see C.1)

3. If we constrain the oracle cost to be of the same order as SGD, is the excess term in the convergence upper bound tight? (see A.3)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors develop a novel method called Byz-VR-MARINA-PP, which can allow partial participation and have Byzantine robustness simultaneously. The convergence results of Byz-VR-MARINA-PP for non-convex objectives and objectives that satisfy PL conditions are provided.

### Strengths
(1) The paper is generally well-written and not hard to understand. 

(2) A rigorous theoretical analysis is provided in this paper. Although I did not check the details, the proof seems to be correct.

### Weaknesses
However, there are also some weaknesses, as listed below.

(1) The main differences between Byz-VR-MARINA-PP and Byz-VR-MARINA are that Byz-VR-MARINA-PP adopts gradient clipping and thus allows partial participation (PP). There are typically two benefits of PP, i.e., tolerating inactive clients and accelerating training processes. However, Byz-VR-MARINA-PP seems to perform poorly in either of the two aspects.

(1a) As presented in Algorithm 1, in Byz-VR-MARINA-PP, the clients are sampled by the server before each round. Therefore, if a selected client becomes inactive, the whole training process will be blocked. In other words, Byz-VR-MARINA-PP cannot tolerate inactive clients. This is a significant limitation, as real-world federated learning scenarios often involve clients with intermittent connectivity or availability, and the algorithm should ideally be robust to such situations. The method's reliance on a synchronous update mechanism makes it particularly vulnerable to stragglers or unresponsive clients.

(1b) All clients will participate in the $k$-th training round if $c_k=1$. That is to say, all clients will participate in the training per $1/p$ rounds in expectation. I understand that $p$ is typically small. However, it will also greatly limit the acceleration effect of PP since in federated learning (especially in cross-device federated learning), the fraction of selected clients in each round is usually small. The forced full participation rounds could negate the benefits of partial participation, especially in scenarios with a large number of clients and limited resources. The method seems to oscillate between full and partial participation without a clear strategy for optimizing the trade-off between communication cost and convergence speed.

Given the reasons above, could the authors specify what benefits the partial participation mechanism can bring?

(2) The computation of full gradients is time-consuming. Moreover, it is unknown whether the gradient clipping is empirically compatible with the PAGE estimator. The interaction between gradient clipping and the variance reduction mechanism of PAGE needs to be thoroughly investigated. It is not clear if the clipping introduces any bias or affects the convergence rate. I strongly suggest the authors empirically test the performance of the proposed method on some federated learning benchmarks such as LEAF [1].

### Questions
Please see my comments above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
