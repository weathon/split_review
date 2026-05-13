# Distributional Bellman Operators over Mean Embeddings

- Decision: Reject
- Scores: 8, 5, 6, 3

## Abstract
We propose a novel algorithmic framework for distributional reinforcement learning, based on learning finite-dimensional mean embeddings of return distributions. 
    The framework reveals a wide variety of new algorithms for dynamic programming and temporal-difference algorithms that rely on the \emph{sketch Bellman operator}, which updates mean embeddings with simple linear-algebraic computations.
    We provide asymptotic convergence theory, and examine the empirical performance of the algorithms on a suite of tabular tasks.
    Further, we show that this approach can be straightforwardly combined with deep reinforcement learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses a method to do distributional reinforcement learning using mean embedding sketches. The advantage of this method is that the sketches can be updated without ever obtaining the imputed distribution, thereby allowing computations entirely in the sketch domain.

### Strengths
This paper satisfies all the criteria of an excellent paper:
1. It is exceptionally clearly written. Reading it and learning from it was a joy. It does a great job at being thorough without being pedantic in its discussion. I really appreciated the concrete discussion in sections 3.2 and 4.1; it dovetails quite nicely with the rest of the paper.
2. It makes a useful contribution to the fun and important problem of distributional reinforcement learning. The idea is simple yet elegant.

### Weaknesses
The formulation of feature maps used in the paper (equation (8)) is not sufficiently justified. While the translation-family feature maps are presented as a viable option, the rationale for selecting this specific formulation over other potential choices remains unclear. For instance, a more rigorous comparison against alternative feature map families, such as radial basis functions or polynomial kernels, could provide a stronger foundation for this design choice. Additionally, the paper does not explore the impact of different parameterizations within the chosen translation-family on the performance of the mean embedding sketches. A sensitivity analysis concerning the parameters of the feature maps would be beneficial.

Furthermore, the connection between the general sketch using Bellman coefficient $B_r$ and the first $m$-moments could be elaborated upon. While the paper suggests an invertible linear relationship, a more explicit mathematical derivation would enhance clarity. The claim that $B_r$ can be written as $C_rC^{-1}$ requires further justification. Providing the intermediate steps, possibly in an appendix, would make the derivation more accessible to readers. Lastly, the paper primarily focuses on the case where the reward space $\mathcal R$ is finite. While a brief mention of generalization is made, a more detailed discussion on how the method can be extended to continuous or large discrete reward spaces is warranted. This could involve exploring numerical integration techniques or other approximation methods to handle the expectation over the reward distribution.

### Questions
1. The general sketch using Bellman coefficient $B_r$ will correspond to some mean embedding sketch which is an invertible linear combination of first $m$-moments, right?
2. Why can we write $B_r$ as $C_rC^{-1}$?
3. Where's the generalization to the case when $\mathcal R$ is not finite?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel algorithmic framework for distributional reinforcement learning that works purely in the sketch space based on finite-dimensional mean embeddings of return distributions. The authors derive the approximate Bellman equation in the sketch space and propose a new algorithm that can be combined with dynamic programming and temporal-difference learning. The authors provide an asymptotic convergence theory for the proposed method, and examine the representation error of the proposed sketch on a suite of tabular tasks. They also demonstrate that this approach can be straightforwardly combined with deep reinforcement learning, obtaining a new deep RL agent that improves over the QR-DQN baseline on the Arcade Learning Environment.

### Strengths
1. The paper introduces a novel framework for distributional reinforcement learning, which is based on learning mean embeddings of return distributions. This approach avoids the need for expensive imputation strategies, which can be computationally expensive and biologically implausible.
2. The authors provide a theoretical analysis of the proposed algorithms, including asymptotic convergence results. This analysis helps to establish the theoretical foundations of the approach and provides insights into its properties.

### Weaknesses
1. The proposed method requires a linear approximation for the Bellman update equation and require calculating a Bellman coefficient matrix $B_r$ that can be computationally challenging. This contradicts the motivation to improve computation efficiency and reduce the imputation error by purely operating in the sketch space. It is unclear how the proposed method is superior to previous methods both computationally and statistically. The need to compute $B_r$ involves inverting the covariance matrix of the feature functions, which can be unstable and computationally expensive, especially with a large number of features. Furthermore, the linear approximation might not accurately capture the non-linear dynamics of the return distribution, potentially leading to suboptimal performance.

2. The experimental validation is limited. The experiment on the tabular tasks only shows the approximation error of the proposed sketch method rather than the performance of the overall approach. From the result, the proposed sketch method has a similar Cramer distance compared to the CDRL baseline. While the proposed sketch has lower excess Cramer distance and mean-embedding squared error, it is unclear how these metrics translate into the performance of the proposed approach. For the Deep RL part, the proposed method underperforms IQN and does not significantly outperform QR-DQN, which is the backbone of the proposed method. Does the proposed method have a significant computation advantage?

Minor: CDRL is mentioned but not referred to in the paper.

### Questions
1. What is the advantage of the proposed method compared with previous distributional RL methods? Does the proposed method have a provable lower approximation error or computation advantage?

2. How does the proposed method perform on the tabular tasks compared with baselines? Does the proposed method have a computation advantage in the deep RL setting?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel distributional RL framework based on the sketch Bellman operator. The approach is derived from statistical functional dynamic programming and involves constructing different sketches to formulate the Bellman equation. The authors provide a theoretical guarantee to support their proposed method and empirical studies demonstrate that it outperforms some baselines in Atari environments.

### Strengths
1) The authors provide detailed experiments, particularly for ablations on different feature functions.

2) The authors provide theoretical guarantee, which adds credibility to their proposed method.

### Weaknesses
1) The authors' motivation for using the sketch Bellman operator is to reduce the need for expensive imputation strategies when converting between sketches and distributions. However, the experiment does not verify this claim. It would be helpful if the authors could provide some quantitative results (such as training time and per-update computational cost) to demonstrate this reduction, specifically comparing the computational overhead of their sketching approach against the cost of imputation methods used in standard distributional RL.

2) The proposed method performs worse than IQN, even though the authors claim that IQN uses a more complex prediction network for non-parametric predictions. It would be beneficial if the authors could provide quantitative results (such as neural network sizes, number of parameters, and training time per iteration) to explain this performance difference. A more detailed analysis of the architectural differences and their impact on performance is needed.

3) It would be useful to include vanilla Statistical Functional Dynamic Programming (Bellemare et al., 2023) as a baseline in some toy examples to compare its performance with the proposed Sketch-DQN. This comparison should not only focus on final performance but also on computational cost and convergence speed.

4) The writings in some sections are not very clear. For example,  in the subsection on 'Computing Bellman coefficients',  the authors directly show the closed form of (5) without any explanations or citations. The derivation of this closed form should be explicitly provided or referenced, including the assumptions made about the feature space and the data distribution.

5) There are some typos that need to be addressed, such as in Sec 2.2, where it should be $\left(\left(\mathcal{T}^\pi \iota (U)\right)(x)\right)$ instead of $\left(\left(\mathcal{T}^\pi \iota U\right)(x)\right)$.

### Questions
Please answer the questions mentioned above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the mean embedding sketches, one kind of statistical functional, in the context of distributional RL. They first show the sketch framework, where the Bellman operator is applied on the sketch instead of the original value function in classical RL. Further, they also provide the convergence guarantee under the sketch framework. Experiments are conducted on both tabular MDP and Atari games.

### Strengths
* The writing is clear. The paper is well-organized and easy to follow.

* Experiments are extensive by considering both MDP and all Atari games with 200M frames.

### Weaknesses
* **Limited Methodology contribution and novelty**. Firstly, the sketch is just one special statistical functionals equipped with a specified kernel function, which is typically less commonly used than quantiles or samples. Working on algorithms simply based on a new concept may not contribute to the real development of this research field. More importantly, feature mapping has already been implicitly considered in MMDDRL paper [1], where MMD naturally induces a feature map. The mean embedding of a distribution $P$ in RKHS $\mathcal{H}$ is defined as $\mu_P = \mathbb{E}_{X\sim P}[\phi(X)]$, where $\phi$ is the feature map associated with the kernel. The distance between two distributions $P$ and $Q$ is defined as $MMD(P, Q) = \|\mu_P - \mu_Q\|_{\mathcal{H}}$. This is very similar to the proposed sketch framework. Notably. [1] also shows that not all kernels will lead to a convergent distributional Bellman operator, about which this paper has not fully discussed. For example, [1] gave some counterexamples for the convergence when we use Gaussian kernels. From the perspective of new algorithms, Sketch-DP or TD is not new to me and even straightforward. Its concrete version, e.g., in Proposition 4.4 is very similar to the categorical representation. The choice of different feature maps also has a strong correlation with the MMD equipped with different kernels. Based on my knowledge of RKHS, different kernel naturally induces a RHKS with a specific feature map. Therefore, I do not think the sketch framework has sufficient methodological contribution compared with existing works.

* **Insufficient theoretical analysis**. The biggest issue in the theoretical part is the pre-specification of a metric $d$ such that it is $\gamma^c$ contractive, which is a strong assumption. With a metric that can already guarantee the contraction, the approximation error is easy to show. Further, as mentioned in the first weakness, not all feature maps can guarantee the contraction. For example, [1] gave some counterexamples for the convergence when we use Gaussian kernels. Specifically, Theorem 2 in [1] shows that the contraction is correlated with the choice of kernel. Therefore, the current paper lacks a crucial theoretical part about what kinds of feature maps can guarantee the contraction and then bound the errors. Without this crucial part, I personally think the current theoretical results are insufficient.

* **Insignificant empirical improvements**. The viewpoint of limited methodological contribution is further demonstrated by the insignificant empirical improvements in Figure 5. Although I truly agree on the conclusion that the sketch framework slightly improves C51 and QRDQN, it performs worse than IQN. Hence, I only view the sketch paper as a feature map-based algorithm, which has already been implicitly investigated before, rather than a novel one with significant performance. The insignificant improvement also let me rethink what is the real motivation of the sketch framework. Also, it is better to compare the performance with [1] as both are kernel-based methods.

### Questions
Please refer to the Weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
