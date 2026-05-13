# Adaptive Batch Size for Privately Finding Second-Order Stationary Points

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
There is a gap between finding a first-order stationary point (FOSP) and a second-order stationary point (SOSP) under differential privacy constraints, and it remains unclear whether privately finding an SOSP is more challenging than finding an FOSP. Specifically, Ganesh et al. (2023) demonstrated that an $\alpha$-SOSP can be found with $\alpha=\Tilde{O}(\frac{1}{n^{1/3}}+(\frac{\sqrt{d}}{n\epsilon})^{3/7})$, where $n$ is the dataset size, $d$ is the dimension, and $\epsilon$ is the differential privacy parameter. Building on the SpiderBoost algorithm framework, we propose a new approach that uses adaptive batch sizes and incorporates the binary tree mechanism. Our method improves the results for privately finding an SOSP, achieving $\alpha=\Tilde{O}(\frac{1}{n^{1/3}}+(\frac{\sqrt{d}}{n\epsilon})^{1/2})$. This improved bound matches the state-of-the-art for finding an FOSP, suggesting that privately finding an SOSP may be achievable at no additional cost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors find that finding second-order stationary points privately can be as fast as finding first-order stationary points privately at a rate of $\tilde{O} (\frac{1}{n^{\frac{1}{3}}} + (\frac{\sqrt{d}}{n\epsilon})^{\frac{1}{2}} )$.

### Strengths
1. The authors present in a nice and neat way.

2. This paper studies a timely and interesting problem - finding SOSP privately. 

3. The authors introduced simple yet effective tools to solve this problem effectively. Tree mechanism has been applied in many DP papers but this paper illustrates its power when combined with the adaptive batch size. And the analysis part is non-trivial. This technique might be applicable to other private optimization problems.

### Weaknesses
I see no apparent weaknesses in this paper.

### Questions
Can the authors expand the related work section by briefly comparing this work to the momentum-based variance-reduction methods like [1] and
DP-SRM ([2])? I think these papers are somewhat relevant.

[1]: Tran, Hoang, and Ashok Cutkosky. "Momentum aggregation for private non-convex ERM." Advances in Neural Information Processing Systems 35 (2022): 10996-11008.

[2]: Wang, Lingxiao, et al. "Efficient privacy-preserving stochastic nonconvex optimization." Uncertainty in Artificial Intelligence. PMLR, 2023.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies privately finding second-order stationary points of stochastic optimization problems. This problem is a relevant to private machine learning. A related problem is privately finding first-order stationary points. First-order stationary points include saddle points and local optima, making them less valuable for machine learning compared to second-order stationary points, which exclude saddle points.

The paper gives a differentially private algorithm for finding second-order stationary points. Prior state-of-the-art had a rate higher than for first-order stationary points. This work achieves rate-parity between second-order and first-order stationary points under differential privacy.

The prior state-of-the-art algorithm involves infrequent gradient queries interspersed with many gradient-difference queries. The queries are answered by randomly subsampling the dataset by a fixed-size batch. Gaussian noise is introduced to ensure privacy. A drift variable tracks the total amount of l2-movement of the variable and a fresh gradient query is made when the drift crosses a threshold, which ensures that the gradient estimates do not deteriorate significantly.

This work improves upon the prior work in two ways. First, the Gaussian noise mechanism is replaced with a correlated noise mechanism that reduces the cumulative noise introduced by successive gradient-difference queries. Second, the batch-size for gradient-difference queries between two points is chosen adaptively in proportion to the l2-distance between the two points. Due to the underlying smoothness assumption, the sensitivity of the gradient-difference queries grows in proportion to this distance. Thus adaptive batch-sizes allows for more targeted noise levels and also tightens the utility-analysis.

### Strengths
The paper proposes a novel algorithm for an important problem in private machine learning. The algorithm improves meaningfully on the previous state-of-the-art in multiple clear ways.

The writing is generally clear and ideas are easy to follow.

### Weaknesses
My only concern is a lack of experimental results. It would be nice to see a small experiment comparing the algorithm to the prior state-of-the-art in order to give a sense of whether the new algorithm is practical to run or not as well as whether the theoretical improvements actually translate into substantive improvement in the quality of the SOSP. In particular, I would be interested to see how the runtime as well as the $\alpha$ value of your approach compares to prior approaches on benchmark problem instances of increasing size.

I was a bit surpised that the private rate only improved from $\tilde{O}((\sqrt{d}/\epsilon n)^{3/7})$ to $\tilde{O}((\sqrt{d}/\epsilon n)^{1/2})$ after what seem at a high level like fairly substantial improvements to the algorithm. Is this bound known to be tight for FOSP?

> In our setting, $\mathcal{O}_1$ is more accurate but incurs higher computational or privacy costs.

This point is not entirely clear to me and it seems very foundational to the structure of the algorithm. Why shouldn't we just query $\mathcal{O}_1$ every time? I assume it is related to the sensitivity of the queries. It would be helpful for the authors to clarify the motivation for using both oracles by explicitly state the tradeoff between using $\mathcal{O}_1$ and $\mathcal{O}_2$ in terms of accuracy, privacy cost, and/or computational complexity.

> When the privacy parameter $\epsilon$ is sufficiently small, we observe that $\alpha_F \ll \alpha_S$.

I am not completely following this either. If $n$ and $d$ are fixed and we take $\epsilon \to 0$, then eventually we should have $(\sqrt{d}/\epsilon n)^{1/2} > (\sqrt{d}/\epsilon n)^{3/7}$. Could the authors explain the regime (in terms of relationships between $n$, $d$, and $\epsilon$) where the improvement is most significant and clarify whether there are any limitations of their approach as $\epsilon$ becomes very small?

### Questions
I was a bit surpised that the private rate only improved from $\tilde{O}((\sqrt{d}/\epsilon n)^{3/7})$ to $\tilde{O}((\sqrt{d}/\epsilon n)^{1/2})$ after what seem at a high level like fairly substantial improvements to the algorithm. Is this bound known to be tight for FOSP?

> In our setting, $\mathcal{O}_1$ is more accurate but incurs higher computational or privacy costs.

This point is not entirely clear to me and it seems very foundational to the structure of the algorithm. Why shouldn't we just query $\mathcal{O}_1$ every time? I assume it is related to the sensitivity of the queries. It would be helpful for the authors to clarify the motivation for using both oracles by explicitly state the tradeoff between using $\mathcal{O}_1$ and $\mathcal{O}_2$ in terms of accuracy, privacy cost, and/or computational complexity.

> When the privacy parameter $\epsilon$ is sufficiently small, we observe that $\alpha_F \ll \alpha_S$.

I am not completely following this either. If $n$ and $d$ are fixed and we take $\epsilon \to 0$, then eventually we should have $(\sqrt{d}/\epsilon n)^{1/2} > (\sqrt{d}/\epsilon n)^{3/7}$. Could the authors explain the regime (in terms of relationships between $n$, $d$, and $\epsilon$) where the improvement is most significant and clarify whether there are any limitations of their approach as $\epsilon$ becomes very small?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper improves the theoretical bounds for reaching a Second-Order Stationary Point (SOSP) under differential privacy constraints. By employing an adaptive batch size and replacing the independent Gaussian mechanism with a private tree mechanism, the paper effectively reduces the error in achieving SOSP. Detailed theoretical proofs are provided.

### Strengths
This paper addresses an important problem by improving the theoretical bound for achieving a second-order stationary point (SOSP) under differential privacy constraints, aligning it with the bound for a first-order stationary point (FOSP). Leveraging the tree mechanism in differentially private continuous observation, which has been shown to achieve asymptotically minimal error, the paper successfully reduces the error for SOSP.  I believe the idea is noval and the contribution is sufficient.

### Weaknesses
1. There is a line of work that further improves the theoretical bound of the tree mechanism, called matrix mechanism [1]. It improves the bound of the tree mechanism by a constant factor. When training a model, it generally works better than the tree mechanism [2]. I would like to hear some discussions about whether using the matrix mechanism can help improve the theoretical analysis.

2. I am confused by how you describe the adaptive batch size, the expression of $b_t$ in Lemma 3.8 depends on $\tilde{\Delta}_t$. Is  $\tilde{\Delta}_t$ private? If you need to change the batch size based on the dataset, there's a risk of leaking private information when the batch size is not protected. Could you explain how you make the batch size private?

3. As stated in point 2, the notations sometimes confuse me. If would be great if there is a table of notion provided, which would help the paper more readable.

### Questions
A minor question, does the norm in the paper mean $l_2$ norm?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new algorithm for private stochastic optimization that builds on the SPIDER algorithm, incorporating a well-known differential privacy technique called the "tree mechanism" and an adaptive batch-size approach. The adaptive strategy adjusts the batch size based on a bias-variance criterion. The authors provide proofs showing that their algorithm achieves faster convergence rates to second-order stationary points than previous methods.

### Strengths
- The paper provides a theoretical improvement over the existing methods, particularly by achieving faster convergence to second-order stationary points under privacy constraints.
- The proofs are thorough and well-written, giving strong support to the theoretical claims.
- The paper gives sound reasons for developing the algorithm, which addresses both theoretical and practical needs in private stochastic optimization.

### Weaknesses
 - The structure and flow could be improved, and feels a bit rushed. At times, the paper feels like a sequence of technical lemmas without enough overview or context, which can make it hard to follow. Specifically, the transitions between sections are abrupt, and the motivation for certain technical steps is not always clear. For example, the introduction of the adaptive batch size could benefit from a more detailed explanation of why this particular approach was chosen over other potential methods.
- The paper does not include an empirical evaluation of the proposed method. Although the main focus is on theoretical improvement, a comparison with other methods in private stochastic optimization would be helpful to understand the practical performance of the algorithm. The absence of experiments makes it difficult to assess the real-world applicability and limitations of the proposed algorithm. It is unclear how the theoretical gains translate into practical improvements, and whether the algorithm is robust to various hyperparameter settings.
- The notation $\mathcal{O}_1$ and $\mathcal{O}_2$ for the gradient oracles could be confusing, as it resembles the common asymptotic notation $O$. An alternative notation might reduce ambiguity. This could lead to misinterpretations, especially for readers who are not deeply familiar with the specific notation conventions used in this paper. The lack of a clear distinction between the oracle notation and asymptotic notation can cause confusion and hinder the readability of the paper.
- How do the assumptions in this work compare to those in related papers? A comparison could add useful context. The paper does not provide a thorough discussion of how the assumptions compare to those in other works on private stochastic optimization. This makes it difficult to understand the scope and limitations of the proposed method. A detailed comparison would help to clarify the novelty and contribution of the work.
- The current approach allows each data point to be seen only in one of the inner loop of the SPIDER algorithm. Could sample complexity be improved by sharing data across outer loops while tracking privacy using composition and subsampling amplification? The paper does not explore the possibility of reusing data points across outer loops, which could potentially improve sample complexity. The current approach may be suboptimal in terms of data efficiency, and a discussion of alternative approaches would be beneficial.

### Questions
- The notation $\mathcal{O}_1$ and $\mathcal{O}_2$ for the gradient oracles could be confusing, as it resembles the common asymptotic notation $O$. An alternative notation might reduce ambiguity.
- How do the assumptions in this work compare to those in related papers? A comparison could add useful context.
- The current approach allows each data point to be seen only in one of the inner loop of the SPIDER algorithm. Could sample complexity be improved by sharing data across outer loops while tracking privacy using composition and subsampling amplification?

### Soundness
4

### Presentation
2

### Contribution
3
