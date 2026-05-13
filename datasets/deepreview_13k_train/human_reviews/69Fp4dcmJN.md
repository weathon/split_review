# Scaling up the Banded Matrix Factorization Mechanism for Large Scale Differentially Private ML

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Correlated noise mechanisms such as DP Matrix Factorization (\dpmffamily) have proven to be effective alternatives to \dpsgd in large-epsilon few-epoch training regimes.  Significant work has been done to find the best correlated noise strategies, and the current state-of-the-art approach is \bandmf , which optimally balances the benefits of privacy amplification and noise correlation.  Despite it's utility advantages, severe scalability limitations prevent this mechanism from handling large-scale training scenarios where the number of training iterations may exceed $10^4$ and the number of model parameters may exceed $10^7$.  In this work, we present techniques to scale up \bandmf along these two dimensions, significantly extending it's reach and enabling it to effectively handle settings with over $10^6$ training iterations and $10^9$ model parameters, with negligible utility degradation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies a mechanism (DP-BandMF) for private machine learning that has advantages over the standard private mechanism (DP-SGD) in some regimes due to its use of optimized correlated noise. The algorithm is characterized by a strategy matrix that determines the correlational structure of the noise.

This work identifies the optimization of the stategy matrix is a computational bottleneck limiting the applicability of DP-BandMF. Prior work gives an $O(n^3)$ time and $O(n^2)$ space algorithm, which is impractical for large values of $n$. This work improves the running time to $O(bn^2)$ and the space to $O(bn)$ where the band size $b$ characterizes the level of correlation allowed between noise vectors. The authors go on to give a further improved $O(bn)$ time $O(n)$ space algorithm for a restricted class of strategies.

The authors conclude with a series of experiments that assess the scalability and solution quality of their algorithm, the optimal band-size, as well as the suitability of the RMSE measure optimized by their algorithm as a proxy for utility loss.

### Strengths
The paper investigates practical scalability issues of a useful DP-ML algorithm and makes substantial performance improvements that increase the range of high-dimensional learning tasks that may be solved by DP-BandML.

The purpose and conclusions of the experiments are well-explained.

Overall, the paper is very clearly written and pleasant to read.

### Weaknesses
A small point not addressed in this work is efficient computation of the gradient of the RMSE objective. The authors defer to the Jax implementation. It is unclear whether there is an inherent limitation of this approach or if there is room for meaningful improvement in gradient computation efficiency.

A more significant weakness of this work is somewhat limited technical novelty in the results. The primary technical contribution appears to be Algorithm 3, which leverages sparsity and computes the objective in a streaming fashion. While this is a practically useful contribution, the core idea is relatively straightforward, and the theoretical analysis does not appear to offer substantial new insights beyond what is already known about streaming algorithms.

The authors do extend their results in Proposition 3.1 to a new setting involving Toeplitz strategies. This result is nice but I found the following motivation not fully convincing: "This design decision was inspired by manual inspection of the optimal dense strategies, observing that they exhibit a near-Toeplitz structure." While this choice seems bolstered by by the result in Figure 1(a), a more careful theoretical justification would be welcome, if possible. The observation of a near-Toeplitz structure is interesting, but it is not clear that this is a sufficient justification for restricting the search space to Toeplitz matrices, especially given that the optimal dense strategies are not exactly Toeplitz. A more rigorous argument, perhaps involving approximation bounds or a deeper analysis of the structure of optimal strategies, would strengthen this aspect of the work.

### Questions
- Could context be provided for how a "strategy" should be interpreted? Around l85 in the background.
- The "workload" $A$ is introduced around l150 but the context is also unclear to me here. What is the role of this object and why is it natural to view as a lower triangular matrix of ones?
- Could the authors provide a definition of Toeplitz strategies? One was not provided.
- Lastly, is there a typo on l85? $i \leq j + b$ looks the wrong-way-around to me.

### Soundness
3

### Presentation
4

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
The paper presents a improvement to the DP-BANDMF, a differentially private mechanism that adds correlated noise to DP-SGD, aiming to address its scalability limitations. Existing approach DP-BANDMF has struggled with computational and memory demands, especially in large-scale models. The authors introduce two methods  to optimize this mechanism for scenarios involving over 10^6 training iterations and up to 10^9 model parameters, making it feasible for use with modern, large-scale models. The empirical results demonstrate significant performance gains over existing mechanisms.

### Strengths
1. This paper is well written and clearly addresses the contributions.
2. The empirical study is thorough with limitations sufficiently addressed.

### Weaknesses
The only concern here is that this paper does not discuss too much privacy utility trade-off, which is not the focus of this paper.

### Questions
1. Is there any insight on why adaptive estimator works worse than adaptive optimizer?

2. In practice, how do we manage the privacy budget for selecting number of bands?

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
2

### Summary
This paper proposes a differential privacy method that utilizes both random sampling and correlated noise via the use of b-banded strategy matrix. The number of bands b controls the proportion of privacy amplification from subsampling and correlated noise, which can be optimally selected with efficient computation cost using the banded Toeplitz strategy. Further distributed noise generation is used to save potential memory cost.

### Strengths
1. The problem is well explained and motivated.
2. Extensive theoretical and empirical analysis to support the proposed mechanism.
3. The paper is well-written and easy to follow.

### Weaknesses
1. A discussion on the communication cost w.r.t the number of bands as a tradeoff in the distributed setting would be nice to have.

### Questions
I have no questions.

### Soundness
3

### Presentation
3

### Contribution
3
