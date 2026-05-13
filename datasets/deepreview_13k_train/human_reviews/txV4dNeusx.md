# Near-Exact Privacy Amplification for Matrix Mechanisms

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
We study the problem of computing the privacy parameters for DP machine learning when using privacy amplification via random batching and noise correlated across rounds via a correlation matrix $\bfC$ (i.e., the matrix mechanism). Past work on this problem either only applied to banded $\bfC$, or gave loose privacy parameters. In this work, we give a framework for computing near-exact privacy parameters for any lower-triangular, non-negative $\bfC$. Our framework allows us to optimize the correlation matrix $\bfC$ while accounting for amplification, whereas past work could not. Empirically, we show this lets us achieve smaller RMSE on prefix sums than the previous state-of-the-art (SOTA).
We also show that we can improve on the SOTA performance on deep learning tasks. Our two main technical tools are (i) using Monte Carlo accounting to bypass composition, which was the main technical challenge for past work, and (ii) a ``balls-in-bins'' batching scheme that enables easy privacy analysis and is closer to practical random batching than Poisson sampling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the computation of privacy parameters for differentially private (DP) machine learning, specifically when using privacy amplification through random batching and noise correlated across rounds via a correlation matrix C. Previous work either restricted C to banded matrices or provided loose privacy parameters. The authors introduce a framework for computing near-exact privacy parameters for any lower-triangular, non-negative C, optimizing C while considering amplification. They show empirical improvements over the state-of-the-art in root mean squared error (RMSE) for prefix sums and performance on deep learning tasks. The key techniques include Monte Carlo accounting to avoid composition and a balls-in-bins batching scheme for practical random batching.

### Strengths
- Propose a more practical minibatch sampling method, the Balls-in-Bins, that achieves better privacy amplification.

- Use Monte Carlo accounting to bypass composition. The limitations of the current work are well-discussed, especially the limitation of the construction of P.

### Weaknesses
See questions.

- Could the authors interpret "near-exact" privacy analysis by:
  - Provide a more precise definition or explanation of what it means by "near-exact".
  - Discuss the potential impact of the looseness in $P$ on the overall privacy guarantees, given that the construction of $P$ in the dominating pair is potentially too loose.

- In lines 358-364, the authors discuss the choice of $b$ in experiments, which is chosen from the set {$ 1, 2, 4, 8, 16, 32, 64, 128, 256 $}. How does the (sub)optimal choice of $b$ vary with the other key parameters (e.g., $\varepsilon$)? Could the authors briefly discuss the intuition behind these variations, or include an ablation study showing the impact of suboptimal b choices on performance?

- The authors note that the "balls-in-bins” batching scheme enables easy privacy analysis. However, will the practical variant of balls-in-bins batching in Appendix H complicate the privacy analysis? Would it encounter the same difficulties in privacy analysis as Poisson sampling?

- In line 280, the authors mention that the bisection requires $O(\log(1/\delta))$ iterations, where $\delta$ is supposed to be the privacy parameter in $(\varepsilon, \delta)$-DP. However, should it be $O(\log(1/\text{err}))$, where $\text{err}$ is the error tolerance of $\sigma^*$?

Minor:
- Figure 1 explains the amplification methods quite well. However, I would suggest additional notes indicating that the first row corresponds to the batches in the first epoch (e.g., $E = 1$), and that the second row is the second epoch (e.g., $E = 2$).

- In the introduction, the authors mention that one of the limitations of previous work is the banded $C$ issue. Could the authors provide the key intuition as to why the banded $C$ may restrict utility and efficiency, or discuss any specific scenarios or applications where non-banded C matrices are particularly beneficial?

- In Appendix H, for the practical variant of balls-in-bins batching, the authors pad the small batch with some zero-gradient examples to avoid wasted computational resources. Could the authors further explain why wasted computational resources would be a problem?

### Questions
- Could the authors interpret "near-exact" privacy analysis by:
  - Provide a more precise definition or explanation of what it means by "near-exact".
  - Discuss the potential impact of the looseness in $P$ on the overall privacy guarantees, given that the construction of $P$ in the dominating pair is potentially too loose.

- In lines 358-364, the authors discuss the choice of $b$ in experiments, which is chosen from the set {$ 1, 2, 4, 8, 16, 32, 64, 128, 256 $}. How does the (sub)optimal choice of $b$ vary with the other key parameters (e.g., $\varepsilon$)? Could the authors briefly discuss the intuition behind these variations, or include an ablation study showing the impact of suboptimal b choices on performance? 

- The authors note that the "balls-in-bins” batching scheme enables easy privacy analysis. However, will the practical variant of balls-in-bins batching in Appendix H complicate the privacy analysis? Would it encounter the same difficulties in privacy analysis as Poisson sampling?

- In line 280, the authors mention that the bisection requires $O(\log(1/\delta))$ iterations, where $\delta$ is supposed to be the privacy parameter in $(\varepsilon, \delta)$-DP. However, should it be $O(\log(1/\text{err}))$, where $\text{err}$ is the error tolerance of $\sigma^*$?

Minor:
- Figure 1 explains the amplification methods quite well. However, I would suggest additional notes indicating that the first row corresponds to the batches in the first epoch (e.g., $E = 1$), and that the second row is the second epoch (e.g., $E = 2$).

- In the introduction, the authors mention that one of the limitations of previous work is the banded $C$ issue. Could the authors provide the key intuition as to why the banded $C$ may restrict utility and efficiency, or discuss any specific scenarios or applications where non-banded C matrices are particularly beneficial?

- In Appendix H, for the practical variant of balls-in-bins batching, the authors pad the small batch with some zero-gradient examples to avoid wasted computational resources. Could the authors further explain why wasted computational resources would be a problem?

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
3

### Summary
In this paper, the authors propose a ``balls-and-bins'' batching scheme, for which the privacy analysis is quite straightforward (by analyzing hockey-stick divergence of the `dominating pairs'). Based on their novel batching scheme, the authors use Monte Carlo accounting to estimate the privacy parameter and avoid the estimation errors introduced by DP composition theorems. The experimental results indicate that their scheme performs better than existing works.

### Strengths
The paper is well-written, and the theoretical results seem to be correct (I didn't check the full proof carefully, but I believe it makes sense at a high level).

### Weaknesses
 - In the abstract, the authors claim that the ``ball-and-bins'' scheme is closer to practical random batching than Poisson sampling. But there is no theoretical explanation in the paper. Not sure if I miss anything here.
- The Algorithm 2 applies bisection method to compute the $\sigma$. But the proof of monotonicity is missing.

### Questions
- What is the ``practical random batching'', and why is the balls-and-bins scheme approximates it better than Poisson sampling?
- Can the authors provide a proof for the monotonicity between $\sigma$ and $\delta$?

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
The paper provides a differential privacy accountant for the "ball-in-bins batching", where the disjoint mini-batches for DP-SGD are formed via multinomial sampling. A particularly nice property of the accounting method is that it can be combined with so-called matrix mechanisms, where correlated noise is added to the DP-SGD iterations. The accounting is based on the randomized differential privacy accounting framework provided by [Wang et al., 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/6ae7df1f40f5faeda474b36b61197822-Paper-Conference.pdf), where Monte Carle sampling of the hockey-stick integral (when expressed using the privacy loss distribution) is carried out. This is enabled by Lemma 3.2 which gives a dominating pair of distributions $(P,Q)$, where $P$ can be sampled efficiently and $Q$ has a tractable density function. This way, the PLD can be sampled and the hockey-stick integral estimated.

### Strengths
- The paper provides a novel and practical mini-batch sampling scheme applicable to matrix mechanisms. 

- Seems like a novel way for using the randomized accounting framework proposed by Wang et al. (2023). To the best of my knowledge, this is the most "non-trivial" use of that framework and sets an example that the Monte Carlo sampling is viable tool for differential privacy accounting and designing DP mechanisms.

- Although the convergence analysis is missing, and there are many future questions (e.g., the tightness of the dominating pair and the efficiency of the sampling), the paper gives convincing experimental results indicating this is a viable way of carrying out privacy accounting for the proposed mini-batch sampling scheme.

### Weaknesses
 - The theory is a weak side of the paper. There are really no theoretical guarantees given for the accuracy of the estimates. Theorem 2.1 is stated (Theorem 9 by Wang et al., 2023) however there are no results that would materialize this result. Also, I think it would be good to elaborate on that result, especially since it is stated so differently than Theorem 9 by Wang et al.

- The paper is not fully polished: I don't see the neighborhood relation of datasets stated anywhere. Due to the form of the dominating pair $(P,Q)$ given in Section 3, I assume you consider the add/remove relation. Perhaps the definition you use could be added somewhere in Section 2?

### Questions
- In Lemma 3.2: What exactly guarantees that $(P,Q)$ dominates the pair $(Q,P)$ (for those stated $P$ and $Q$) ? I think the proof of Lemma 3.2 could be elaborated to make it more readable. Perhaps you could add the required results from the reference paper (Choquette-Choo et al., 2024b) to the appendix instead of shortly referring to the lemmas and theorems (example: "see e.g. the first part of proof of Theorem 4.8").

- What would be required to for providing convergence guarantees for the estimates? Could you use the results by Wang et al. for that?

- As I said I assume the analysis is for the add/remove neighborhood relation of datasets. In addition to adding it somewhere (e.g., Section 2), you could briefly discuss in Section 3 how the results might change (or not) for the substitution neighborhood relation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an algorithm for calculating privacy parameters in differentially private SGD when using privacy amplification through random batching and noise correlated across rounds via a correlation matrix, known as the matrix mechanism.

### Strengths
This paper studies a very important problem, balls-in-bins batching with correlated noise, an alternative privacy amplification method in DP-SGD different from the classic subsampling amplification. Existing methods for analyzing privacy in this setting have drawbacks, especially with specific types of correlation matrices (banded matrices). The simulation method proposed shows an interesting and simple way to estimate the security parameter for arbitrary correlation matrix, which can be further used to optimize the noise form.

### Weaknesses
1. A significant limitation of the results is that, while a concrete simulation algorithm is presented, the paper lacks formal high-probability or confidence bounds for the computed DP security parameter. This absence leaves ambiguity about the paper's contribution: whether it offers merely a heuristic estimation or an approach with provable guarantees. My evaluation could improve if high-confidence bounds were provided.

2. The paper does not provide a closed-form or asymptotic bound for the amplification rate produced by the methods, or, equivalently, an indication of the amount of noise required or potentially saved. This lack of theoretical clarity makes it difficult to determine the extent of improvement the method could yield beyond empirical optimization of the noise form.

3.  Furthermore, the paper's analysis of the matrix mechanism in the context of DP-SGD raises concerns about its direct applicability. The analysis assumes a static linear aggregation model, where the input matrix x is predetermined. However, in DP-SGD, the gradient x is not fixed; each iteration's gradient depends on the noisy output of the previous iteration. This adaptive nature of SGD means that the sensitivity analysis, which considers the difference between Cx and Cx' for adjacent datasets, may not accurately capture the privacy leakage in the iterative SGD setting. The paper needs to clarify how the sensitivity analysis of the matrix mechanism applies to the adaptive nature of DP-SGD.

### Questions
1. How to derive high-confidence bound for the monte-carlo simulation results?

2. Can the authors provide the noise parameter or the noise variance in Figure 4 to help readers understand the amplification? The accuracy itself does not tell too much meaningful information as the performance of SGD may be influenced by many other factors. 

3. Can the authors comment more on why in large eps, the proposed method performs much worse compared to subsampling amplification?

### Soundness
2

### Presentation
2

### Contribution
2
