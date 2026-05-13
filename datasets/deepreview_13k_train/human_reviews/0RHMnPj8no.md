# Improved Sample Complexity for Private Nonsmooth Nonconvex Optimization

- Decision: Reject
- Scores: 6, 8, 5, 5

## Abstract
We study differentially private (DP) optimization algorithms for stochastic and empirical
objectives which are neither smooth nor convex, and propose methods that return a Goldstein-stationary point with sample complexity bounds that improve on existing works.
We start by providing a single-pass $(\epsilon,\delta)$-DP algorithm that
returns an $(\alpha,\beta)$-stationary point as long as the dataset is of size $\widetilde{\Omega}\left(1/\alpha\beta^{3}+d/\epsilon\alpha\beta^{2}+d^{3/4}/\epsilon^{1/2}\alpha\beta^{5/2}\right)$,
which is $\Omega(\sqrt{d})$ times smaller than the algorithm of \citet{zhang2023private} for this task,
where $d$ is the dimension.
We then provide a multi-pass polynomial time algorithm which further improves the sample complexity to $\widetilde{\Omega}\left(d/\beta^2+d^{3/4}/\epsilon\alpha^{1/2}\beta^{3/2}\right)$,
by designing a sample efficient ERM algorithm,
and proving that Goldstein-stationary points generalize from the empirical loss to the population loss.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents algorithms to improve sample complexity in differentially private (DP) nonsmooth, nonconvex (NSNC) optimization. The authors propose two zero-order algorithms that improve the results over Zhang et al. 2024
1. Single-pass, sqrt(d) improvement over Zhang et al. 2024. The authors also establish a dimension-independent “non-private” term, which is not known before for NSNC DP optimization.
2. A multi-pass algorithm further improves the sample complexity, yielding the first algorithm to preform private ERM with sublinear dimension-dependent sample complexity for NSNC objectives.
Additionally, the authors show that Goldstein-stationarity generalizes from the ERM to the population.

### Strengths
- The paper is well-structured and easy to follow.
- The results improve over prior state of the art, establishing the first DP NSNC ERM algorithm with sublinear dim-dependent sample complexity. The non-private term is dimension-independent, which improves over the previous dimensional dependent result in Zhang et al. 2024.

### Weaknesses
My main concern is about contextualizing the contribution:
Like Zhang et al. 2024, this paper also heavily relies on “Online-to-Non-Convex conversion” (O2NC) of Cutkosky et al. (2023). The authors also mention that a lower bound is unknown, making it hard to assess the contribution beyond incremental improvement.

A discussion of the Tree Mechanism is missing. It would be very hard for readers not familiar with the Tree Mechanism to understand.
Typo: page 2 and in particular is the first algorithm to [preform] private ERM

### Questions
1. I am confused by the explanation of the improvement on the non-private term Remark 3.2. The authors explain that
> while the optimal zero-order oracle complexity is d/αβ^3 (Kornowski & Shamir, 2024), and in particular must scale
with the dimension (Duchi et al., 2015), the sample complexity might not.
Since the algorithm is one-pass, then the sample complexity would be worse than the oracle complexity?
2. Is Online-to-Non-Convex conversion optimal? (Related to the weakness above) If not, any algorithms based on it will be suboptimal.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of designing Differentially Private Algorithms for Nonsmooth Nonconvex Optimization. It specifically studies the zeroth order settings. Thanks to more careful analysis, the paper is able to improve on the dimension dependence of the previous results. It also extends the past result to the ERM settings.

### Strengths
- The paper is a fairly simple extension of previous results. The authors are able to improve the past sample complexity by an order of $O(\sqrt{d})$ by using a high probability subgaussian bound on the sensitivity of the queries. 

- The paper also extends the results to other settings.

- The generalization statement (Proposition 5.1) is a cool result to show the validity of the ERM approach for solving the Goldstein-stationary point.

- The paper is well written overall.

### Weaknesses
 - The paper is basically using the same algorithm proposed by [1]. This is not a huge issue since they are able to make some nice modifications to improve the sample complexity. However, this does limit the potential impact of the paper.

- I also think $m$ is quite large, which would make it really inefficient to run in practice. Currently, m can be something like $O(d^2T^{4/5})$, which is very hard to do in practice.

- It would be interesting if there were some matching upper bounds.

### Questions
- Why did the authors decide to use Gaussian Mechanism instead of the tree mechanism for ERM?

### Soundness
3

### Presentation
4

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
This paper explores differentially private (DP) optimization algorithms for stochastic and empirical objectives that are non-smooth and non-convex, presenting methods that achieve Goldstein-stationary points with improved sample complexity bounds compared to prior work. The authors introduce a single-pass ($\epsilon$,$\delta$)-DP algorithm capable of producing ($\alpha$,$\beta$)-stationary points. Subsequently, they propose a multi-pass, polynomial-time algorithm that further refines sample efficiency by designing an effective ERM algorithm and demonstrating that Goldstein-stationary points can generalize from the empirical to the population loss.

### Strengths
The paper studies an important problem in DP non-convex optimization, and achieves improved sample complexity bounds over existing works.

### Weaknesses
The presentation is at times unclear, leading to a disjointed reading experience.

Additionally, the paper offers limited technical innovation. Most of the algorithmic framework and techniques appear to be adapted from previous works.

The tree mechanism in Algorithm 1 is hard to understand and seems logically inconsistent. Specifically, regarding the function NODE, what is its intended purpose? There appears to be no defined output for NODE. Moreover, in line 13, $k'$ is assigned a value greater than $k$, however, line 14 subsequently tests the condition $k'\le k$, which can never be true. As a result, $S$ remains an empty set and is never updated.

In the fourth line of Proposition 2.5, for calculating each $X_i$, should it instead use $\sum_{j=1}^i M_j$  rather than the expression given in the paper  $\sum_{j=1}^i M_i$?

In (Cutkoskyetal.,2023), $\Delta_{t+1}$ is updated by $\Delta_{t}+\eta g$ (as stated in their Remark 10), while in Algorithm 2 line 8, $\Delta_{t+1}$ is updated by $\Delta_{t}-\eta g$. Could you clarify the rationale behind this difference?

In Theorem 3.1, while the sample complexity has been reduced by a factor of $\Omega(\sqrt{d})$ compared to (Zhang et al., 2024), this comes at the expense of increasing the number of random directions $m$ from $d$ to $d^2$, potentially resulting in a longer runtime.

### Questions
1. The tree mechanism in Algorithm 1 is hard to understand and seems logically inconsistent. Specifically, regarding the function NODE, what is its intended purpose? There appears to be no defined output for NODE. Moreover, in line 13, $k'$ is assigned a value greater than $k$, however, line 14 subsequently tests the condition $k'\le k$, which can never be true. As a result, $S$ remains an empty set and is never updated.

2. In the fourth line of Proposition 2.5, for calculating each $X_i$, should it instead use $\sum_{j=1}^i M_j$  rather than the expression given in the paper  $\sum_{j=1}^i M_i$?

3. In (Cutkoskyetal.,2023), $\Delta_{t+1}$ is updated by $\Delta_{t}+\eta g$ (as stated in their Remark 10), while in Algorithm 2 line 8, $\Delta_{t+1}$ is updated by $\Delta_{t}-\eta g$. Could you clarify the rationale behind this difference?

4. In Theorem 3.1, while the sample complexity has been reduced by a factor of $\Omega(\sqrt{d})$ compared to (Zhang et al., 2024), this comes at the expense of increasing the number of random directions $m$ from $d$ to $d^2$, potentially resulting in a longer runtime.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses differential privacy (DP) in nonsmooth, nonconvex optimization, aiming to improve sample complexity for finding Goldstein-stationary points in such challenging settings. Traditional DP optimization methods often assume convexity or smoothness, but this work proposes new algorithms that can handle nonsmooth nonconvex (NSNC) objectives.
### Key Contributions

1. **Single-Pass Algorithm**  
   The authors present a single-pass (ε, δ)-DP algorithm that finds an (α, β)-stationary point with improved sample complexity. This algorithm reduces dimensional dependence by a factor of \(\Omega(\sqrt{d})\) over previous approaches, making DP optimization feasible in high-dimensional settings while maintaining privacy guarantees.

2. **Multi-Pass Algorithm**  
   A multi-pass ERM-based algorithm further enhances sample efficiency, allowing the algorithm to iterate over the data multiple times and achieve sublinear dimension-dependent sample complexity. This approach improves convergence while satisfying DP constraints.

3. **Generalization from ERM to Population Loss**  
   The authors establish that Goldstein-stationarity achieved on empirical loss also applies to the population loss with high probability. This result expands the utility of their approach by ensuring that empirical results generalize to the population.


The proposed algorithms make notable progress in DP optimization for NSNC problems, improving sample efficiency while maintaining privacy. This advancement is valuable for practical applications where data privacy is essential, especially in high-dimensional machine learning settings. Additionally, the generalization result strengthens the applicability of Goldstein-stationary points beyond empirical settings.

### Strengths
1. **Significant Improvement in Sample Complexity**  
   The paper offers a substantial reduction in sample complexity for differentially private (DP) nonsmooth nonconvex (NSNC) optimization. The single-pass algorithm achieves a lower dependence on dimension \(d\) compared to prior work, which is highly impactful for high-dimensional problems in machine learning.

2. **Innovative Use of Goldstein-Stationarity**  
   By focusing on Goldstein-stationary points, the authors leverage a nuanced stationarity condition suitable for nonsmooth nonconvex optimization, allowing for more practical solutions where traditional gradient-based methods fall short. This approach builds on and expands the utility of Goldstein-stationarity in DP settings.

3. **Generalization from Empirical to Population Loss**  
   The paper addresses a theoretical gap by proving that empirical guarantees of Goldstein-stationarity translate to the population loss. This generalization strengthens the theoretical foundation and practical relevance of the proposed algorithms, as it ensures that results on empirical data apply to broader distributions.

4. **Applicability to Real-World DP Machine Learning Tasks**  
   The proposed algorithms are zero-order (using only function evaluations) and thus avoid the need for gradient information, making them suitable for a wider range of machine learning models that may have nonsmooth, nonconvex loss landscapes. This approach is particularly beneficial in privacy-sensitive applications like federated learning.

5. **Novel Dimension-Independent Term**  
   The single-pass algorithm introduces a dimension-independent term in the "non-private" component of the sample complexity, challenging previous assumptions in DP optimization for NSNC objectives. This innovation indicates potential for further sample complexity improvements and opens new directions for DP research in nonconvex settings.

### Weaknesses
1. There is some typo, for instance, line 077 the last word should be perform.

2. Randomized Smoothing is an ordinary technique used in this setting, and I wonder the novelty except for this to deal with the non-smooth setting.

### Questions
1. Is the result in the paper tight? In other words, is there a lower bound provided?

2. What is the key challenge in improving the result by at least $\(\sqrt{d}\)$? Specifically, how does this improvement compare to the results in the referenced work?

3. What role does the (α, β)-Goldstein stationary point play in this paper?

4. What is the novelty of this paper compared to previous works?

5. Can you explain more about the result regarding the non-private term and private and how they contribute to the final result?

### Soundness
3

### Presentation
3

### Contribution
2
