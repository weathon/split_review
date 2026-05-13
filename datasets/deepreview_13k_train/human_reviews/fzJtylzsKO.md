# Batched Bayesian optimization with correlated candidate uncertainties

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Batched Bayesian optimization (BO) can accelerate molecular design by efficiently identifying top-performing compounds from a large chemical library. Existing acquisition strategies for batch design in BO aim to balance exploration and exploitation. This often involves optimizing non-additive batch acquisition functions, necessitating approximation via myopic construction and/or diversity heuristics. In this work, we propose an acquisition strategy for discrete optimization that is motivated by pure exploitation, qPO (multipoint Probability of Optimality). qPO maximizes the probability that the batch includes the true optimum, which is expressible as the sum over individual acquisition scores and thereby circumvents the combinatorial challenge of optimizing a batch acquisition function. We differentiate the proposed strategy from parallel Thompson sampling and discuss how it implicitly captures diversity. Finally, we apply our method to the model-guided exploration of large chemical libraries and provide empirical evidence that it performs better than or on par with state-of-the-art methods in batched Bayesian optimization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an exploitive batched acquisition function that can be efficiently approximated as the sum of individual acquisitions. The method assumes a low-noise environment and explicitly encourages diversity in the queries. Due to the absence of an analytic form of the optimum, the acquisition function is implemented using Monte Carlo approximation. The paper demonstrates empirical evidence on real-world applications.

### Strengths
1. The core idea of the algorithm—devising a batch acquisition function that is the sum of individual acquisitions to enhance computational tractability—is convincing.

2. The illustrative case studies, along with figures, effectively demonstrate the advantages of promoting diversity.

### Weaknesses
1. The core idea of the algorithm—devising a batch acquisition function that is the sum of individual acquisitions to enhance computational tractability—is convincing.

2. The illustrative case studies, along with figures, effectively demonstrate the advantages of promoting diversity.


1. The proposed algorithm resembles Predictive Thompson Sampling (pTS). Although the paper briefly discusses the differences between the proposed qPO and pTS and argues its advantages over existing methods, I find the argument not sufficiently convincing. There are two main reasons: First, pTS comes with convergence guarantees, whereas qPO only provides experimental results on unconventional metrics. Second, the randomness inherent in pTS and qEI is arguably the merit, offering robustness to model misspecification—which is common in real-world applications, as the paper also mentions. I hope the authors can elaborate more on the source of robustness in qPO, whether it arises from the sampling-based approximation or the deterministic acquisition that encourages diversity.

2. The paper omits a critical baseline: GIBBON (Moss et al., 2021), which shares the advantage of efficient batched acquisition calculation and is easy to implement with BoTorch.

3. Despite claiming that qPO is designed to be a computationally more efficient batched acquisition function, the paper includes no comparison of computational complexity, either analytically or empirically. This omission is problematic, especially since a Monte Carlo approximation is employed.

4. The metrics used in Section 4 are not the conventional cumulative regret or simple regret. Instead, the paper reports the retrieval of the top-k and the average reward of the top-k. It's unclear if these are valid choices without further justification.

### Questions
1. I'm a bit confused by the discussion regarding the ensemble method as a surrogate model. It seems that the experimental section employed a Gaussian Process with a Tanimoto kernel. What is the role of the ensemble method in the paper, especially as shown in Figure 1?

2. Why is the equality between Equation (6) and Equation (7) valid? What are the assumptions about $f$ and $y$? It is confusing that the paper assumes $f$ is noise-free in line 87 while also assuming low but non-zero observation noise for the GP in line 168. Is there the assumption that $f$ follows a certain distribution, e.g., GP? If not, what is the distribution of $f$?

### Soundness
2

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
4

### Summary
This paper proposes a batch acquisition function for Bayesian optimization on finite (and necessarily discrete) domains.
The acquisition function is the probability that the selected candidates contain the global optimum:
\\[
    \Pr(x^* \in \mathcal{X} _ {\text{selected candidates}}).
\\]
While it's quite challenging to compute this probability on continuous domains, it's easier to estimate this probability on discrete domains.
Indeed, the authors propose approximating this probability using Monte Carlo samples.
On antibiotic discovery and organic electronics design problems, the authors show that the proposed method outperform parallel Thomson sampling, multiple point EI, and UCB.

### Strengths
- The method is intuitive and simple.
- The writing is overall good.
- The improvement over parallel Thompson sampling, qEI, and UCB seems to be consistent across several datasets.

### Weaknesses
 - This paper focuses on finite domains, which certainly simplifies the problem a lot.
This is reasonable.
However, if the primary application is molecule designs, I'd like to see comparisons with recent alternative Bayesian optimization methods that do not frame this problem as a finite discrete BO problem.

There are several immediate ideas worth considering. Without trying these ideas, the paper seems underdeveloped at this moment.
1. As noted by the authors, the probability \(\Pr(x^* = x_i)\) is an orthant normal probability, which can be handled by many existing Monte Carlo methods.
These methods are probably much more efficient and accurate than the proposed estimation method in this paper.
In particular, the method of Genz (1992), which is based on importance sampling, is not too hard to implement.
So employing better numerical methods estimating this normal probability is a nice plus.
2. The biggest improvement actually comes from filtering \(10000\) candidates using a greedy metric (which seems to be the posterior mean).
The authors argue that they do so due to the large computational cost of GP posterior sampling.
However, the experiments in Section 4.2 (\(n = 39,312\)) should be easily handle by modern GP packages, and the experiments in Section 4.3 (\(n = 133,000\)) should be easily handled by variational GPs.

- Also, in my opinion, the paper title is not reflective of the paper content.

### Questions
- The authors mentioned multiple times that the proposed acquisition function is purely exploitative.
I am not sure if this statement is accurate.
On a high level, the method seeks candidates that are more likely to be the optimum.
Its spirit is similar to predictive entropy search in the continuous setting, which is not purely exploitative.

- While the writing is good overall, it's not clear what the candidates \\(\\mathbf{x}\\) are at line 180. (Also at Line 220 ALgorithm 1).
Based on the experiments, it seems that \\(\mathbf{x}\\) is a subset of the domain selected by the greedy strategy (based on posterior mean)?

- I am not sure how Equation (4) makes sense.

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
This paper investigates a novel acquisition function (qPO) for enhancing batch diversity in Thompson sampling. The approach shares conceptual similarities with entropy-search-based methods, as it leverages numerous Thompson sampling trials to estimate the posterior belief of the global optima, due to the non-closed-form nature of this distribution. The estimated function is then maximized to guide selection. While the proposed method relies on several approximation techniques to accelerate computation—whose statistical consistency and bias have yet to be thoroughly validated—it demonstrates superior performance over three baseline methods, which were not specifically designed for diversified batch sampling.

### Strengths
- Highly parallel Bayesian Optimization is an important challenge in real-world tasks, though numerous existing works have pursued similar approaches with clearer conceptual frameworks and stronger theoretical foundations.
- While real-world examples add interest, they rely solely on existing datasets, such as QM9, and thus do not introduce new applications. This work remains primarily an algorithm-focused paper.
- While I appreciate the authors’ effort in presenting Figure 1 to convey the intuition behind the method, I would have liked to see a more precise mathematical explanation.

### Weaknesses
My primary reasons for recommending rejection are as follows: (1) issues with clarity, particularly in the mathematical exposition, (2) limited insights and contributions to the community, and (3) an unfair selection of baselines, which undermines the validity of the claimed empirical improvements.

- **Clarity**
One of the major issues in this paper is clarity, particularly regarding the mathematical exposition. I had a hard time to understand Eqs. (6)–(11). My detailed concerns are as follows:

**Eqs. (6)–(10):** What do the bold vectors $\textbf{x}$ and $\textbf{y}$ represent? Are they the observed points so far, or do they represent all candidates, where $|\textbf{x}| = N$? The former interpretation doesn’t make much sense, so I assume it’s the latter. In that case, this expression becomes a utility function for probability of improvement (PI) (see page 2 in [1]). Then $p(\textbf{y} \mid \textbf{x})$ in Eq. (9) would describe an ideal scenario where we have access to the entire domain $\textbf{x}$, $\textbf{y}$. However, this understanding conflicts with the textual explanations. Specifically, in lines 192–193, the reference to “myopic construction” isn’t clear. If this is indeed the PI utility function $u$, then it would follow that the resulting PI is myopic. Although $Pr(x^\star)$ is indeed the optimal acquisition function, it’s also not achievable in practice, since we could identify $x^\star$ in a single iteration if we had access to the “oracle acquisition function.” Thus, we use a surrogate model to estimate $x^\star$, resulting in an estimate $\hat{x}^\star$, not $x^\star$. Consequently, the myopicness originates from the belief model $f$, not the utility function $u$. Thus, the entire discussion is confusing.

**Eq. (11):** This equation is especially difficult to interpret. What do $y^{(m)}_i$ and $\textbf{y}^{(m)}$ represent? I assume $\textbf{y}^{(m)}$ is a sample function drawn from the GP posterior, with $\max \textbf{y}^{(m)}$ as its maximum, similar to Thompson sampling (TS). However, what is $y_i$? Is it the predictive mean $m(x_i)$? If my understanding is correct, then only one point should be true, with all others zeroed out in the indicator count $\textbf{1}$. Isn’t this an embarassingly inefficient Monte Carlo estimation? Even if we were to take a very large number of samples $M$, the belief model is not the true function. This would imply that the resulting estimate is the posterior belief of the optimum $Pr(\hat{x}^* = x_i)$. Why, then, would this recover the probability of the true optimum $x^*$? This is not strictly an approximation of Eq. (10); while it may be asymptotically convergent, further justification is required to establish this.

- **Unclear Benefits and Inaccurate Descriptions**
Due to clarity issues, I was unable to fully understand how this method differs from existing approaches, such as entropy-search-based methods [2] or other principled approaches in diversified parallel TS. First, the term "correlated candidate uncertainty" in the title is unclear, as it isn’t fully explained within the paper. If this refers to the diversification of the batch selection, there are many existing works. On line 320, the phrase “Deterministically maximize” is somewhat misleading. This statement would hold if Eq. (11) had a closed-form solution. However, since this algorithm relies on multiple approximations, it will not be deterministic due to numerical randomness, similar to TS. Additionally, the “diversity heuristics” mentioned on line 280 are inaccurately described. For instance, Nava et al. (2022) demonstrated a theoretical improvement in convergence rates over parallel TS, showing that these are not merely heuristics but instead clearly proven benefits. In contrast, this paper does not present any convergence analysis results, making it a heuristic approach. Could you clarify which aspects of the parallel TS convergence rate [3] qPO improves upon? Is such improvement better than recent work by Nava et al. (2022) and Ren & Li (2024), which proves tighter regret bounds via batch diversity? If this method (qPO) cannot achieve theoretical or empirical improvements over these methods, I see limited justification for adopting it over these established approaches.

- **Robustness Issues**
Recent work [4,5] raises issues that contrast with the claims in this paper. While this paper argues that parallel TS is overly explorative and suggests an exploitative approach as a remedy, [4,5] contend that parallel TS lacks sufficient diversity and instead requires an explorative adjustment. Intuitively, one would expect an exploitative approach to reduce batch diversity rather than enhance it. Why, then, does this method claim that exploitation leads to diversification? Additionally, [4] and [5] underscore robustness issues in parallel TS-based methods, specifically regarding accurate sample drawing and model misspecification. For example, [4] shows that heuristic approximations, such as the greedy sampling used in this paper, introduce bias in approximating the probability distribution, proposing Matheron’s rule as a corrective approach. Furthermore, [5] demonstrates that if GP hyperparameters are misspecified (e.g., lengthscale), the Monte Carlo estimate in TS becomes biased, and they address this with a robust kernel quadrature approach. Both of these concerns are relevant to the tasks considered in this paper: the sampling approach does not utilize an exact Cholesky decomposition, and the Tanimoto kernel lacks a consistency guarantee for MLE-based hyperparameter estimation. More generally, hyperparameter estimation with MLE in GPs is theoretically ill-posed [8]. Since this paper does not address these robustness concerns, it is unclear what progress or insights it contributes, especially since both [4] and [5] achieve improved diversity akin to the results here.

- **Unfair Baselines**. It’s also worth noting that the baselines selected in this paper are outdated and do not reflect recent advancements. For instance, the qEI baseline should employ sample average approximation with quasi-Monte Carlo as in the original BoTorch paper [6], while UCB should ideally use DB-GP-UCB [7], which is a more theoretically grounded batch approach in UCB. Furthermore, for pTS, which is the main target of this work, a fair comparison would require recent theoretical contributions, such as those by Nava et al. (2022) and/or Ren & Li (2024), as well as empirical work from [4, 5]. Without these comparisons, it is difficult to gauge the practical utility of this method. Given the variety of heuristic and theoretical methods already available, if this approach is intended to be an improvement, a comprehensive empirical comparison with the aforementioned methods is essential. Alternatively, if the goal is to provide new insights, the paper should offer theoretical analysis and/or a clearer empirical study to identify scenarios where this method excels yet other state-of-the-art methods fail, making it more relevant to the community. While this method may have presented an improvement over parallel TS in 2017, it now appears outdated.

- **Minor points**. I also believe that [3] should be cited as a foundational reference for parallel TS, as it provides a clearer theoretical understanding of the method. While Hernández-Lobato et al. (2017) originally proposed it, [3] now serves as a key reference for the theoretical insights underpinning parallel TS.

- **Citations**
- [1] https://www.cse.wustl.edu/~garnett/cse515t/spring_2015/files/lecture_notes/12.pdf
- [2] Takeno, Shion et al., "Sequential and Parallel Constrained Max-value Entropy Search via Information Lower Bound", ICML 2023
- [3] Kandasamy, Kirthevasan, et al. "Parallelised Bayesian optimisation via Thompson sampling." AISTATS 2018
- [4] Wilson, James, et al. "Efficiently sampling functions from Gaussian process posteriors." *ICML 2020*
- [5] Adachi, Masaki, et al. "A Quadrature Approach for General-Purpose Batch Bayesian Optimization via Probabilistic Lifting." arXiv:2404.12219 (2024).
- [6] Balandat, Maximilian, et al. "BoTorch: A framework for efficient Monte-Carlo Bayesian optimization." NeurIPS (2020).
- [7] Daxberger, E. A. et al. "Distributed batch Gaussian process optimization". ICML (2017)
- [8] Karvonen, T. et al. "Maximum Likelihood Estimation in Gaussian Process Regression is Ill-Posed". JMLR (2023)

### Questions
See the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new batch acquisition function (qPO) for bayesian optimization in discrete search space. qPO is a purely exploitative approach, and its objective is to maximize the probability that the true optimum exists within the selected batch. qPO has nice property that it can be decomposed into a sum of scores over candidates, which allows naive parallelization in batch setting and simplifies the implementation.

The authors evaluate qPO on two molecular optimization tasks and show empirically that qPO performs comparably to or better than state-of-the-art batch acquisition method like q-TS, q-EI and UCB.

### Strengths
Originality
1. The formulation of batch acquisition function is novel, and its unique decomposition property where the batch acquisition function equals sum of individual probabilities is useful
2. Achieving batch diversity through formulation towards exploitation is creative

Quality
1. Mathematical formulation and derivation of qPO is clear and sound.

Clarity
1. Visualization of batch diversity in Figure 3 showing both network structure and similarity distributions is great.
2. The 3-point example in Section 3.2 helps illustrate key properties of the acquisition function

Significance
1. Introduces a simpler alternative to complex batch construction strategies
2. The decomposition property makes the method computationally tractable for moderated sized search space

### Weaknesses
1. There is no theoretical justification for why maximizing probability of optimality leads to better sample efficiency (compared with other existing batch acquisition functions like q-EI, q-PI, etc.), and convergence analysis is also absent
2. The diversity property is not unique to qPO as similar property exists in q-PI and other joint probability based methods, but the paper does not provide discussion for this
3. The empirical study is not sufficient:
    1. Missing standard BO benchmarks like synthetic functions
    2. No ablation studies to analyze impact of batch size, effect of pre-filtering threshold, sensitivity to number of MC samples, etc.
    3. There is no comparison to existing joint probability based methods like q-PI, as they are most similar to qPO
4. The pre-filtering strategy may miss promising candidates, therefore, there should be robustness analysis of this method

### Questions
1. Estimation of qPO through MC sampling seems computational expensive, can you provide runtime comparisons with other batch acquisition methods?
2. How robust is the method to model poor initial training data?
3. Does the pre-filtering step risk overlooking promising candidates in the regions with high uncertainty?

### Soundness
2

### Presentation
2

### Contribution
1
