# Comparisons Are All You Need for Optimizing Smooth Functions

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
When optimizing machine learning models, there are various scenarios where gradient computations are challenging or even infeasible. Furthermore, in reinforcement learning (RL), preference-based RL that only compares between options has wide applications, including reinforcement learning with human feedback in large language models. In this paper, we systematically study optimization of a smooth function $f\colon\R^n\to\R$ only assuming an oracle that compares function values at two points and tells which is larger. When $f$ is convex, we give two algorithms using $\tilde{O}(n/\epsilon)$ and $\tilde{O}(n^{2})$ comparison queries to find an $\epsilon$-optimal solution, respectively. When $f$ is nonconvex, our algorithm uses $\tilde{O}(n/\epsilon^2)$ comparison queries to find an $\epsilon$-approximate stationary point. All these results match the best-known zeroth-order algorithms with function evaluation queries in $n$ dependence, thus suggest that \emph{comparisons are all you need for optimizing smooth functions using derivative-free methods}. In addition, we also give an algorithm for escaping saddle points and reaching an $\epsilon$-second order stationary point of a nonconvex $f$, using $\tilde{O}(n^{1.5}/\epsilon^{2.5})$ comparison queries.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors consider the gradient-free method to optimize functions without requiring function value evaluations, relying only on comparisons between function values. In particular, for convex optimization problems, an $\epsilon$-optimal solution can be found, using Theorem 2, in $\mathcal{O}(d/\epsilon)$ oracle queries, which matches the result of [Nesterov & Spokoiny, 2017] in terms of its dependence upon dimension $d$, at the same time, being worse in terms of its dependene upon $\epsilon$. The authors also suggest an algorithm with poly-logarithmic complexity based on cutting plane method. The key technical contribution is Theorem 1, that allows to construct an estimator of the direction of gradient.

### Strengths
The main text of the paper is well-written, and the main results of the submission are well-explained. The authors have put efforts to explain their technical contributions, in particular, the way how the estimates of normalized gradients of theorem 1 are propagated through the further results.

### Weaknesses
I find the novelty of the paper somehow limited, since the main results of the paper (Th. 2 and Th. 4) directly corresponds to the known results for Stochastic Three Points method (STP, [Bergou et al., 2020]), with the same oracle complexities. In this sense the main novelty of the submission comes from the fact that the method in the paper is purely comparison-based. Moreover, the sample complexity results achieved by, for example, Theorem 2, is worse in terms of its dependence upon tolerance level $\epsilon$, compared to the best known results, for example, [Nesterov & Spokoiny, 2017]. In this case I would be curious to find a setting, where the comparison-based method is more valuable, than STP.

### Questions
Is it possible to generalize the results presented in the paper for variational inequalities? In particular, is it possible to apply the results for the Nash equilibrium seeking problems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies comparison-based optimization algorithms and prove the convergence.

### Strengths
The paper propose several comparison-based optimization algorithms and show the convergence to first-order and second-order optimal solutions. Both convex and non-convex scenarios are analyzed.

### Weaknesses
1. I would suggest the authors provide a table of sample complexity of the algorithms for comparison with the results in the literature. Although the authors carefully discuss the existing results, the query complexity is still not very clear. Specifically, it is difficult to assess the practical applicability of the proposed algorithms without a clear understanding of how the number of comparisons scales with problem dimensionality and desired solution accuracy. A table summarizing the dependence of sample complexity on key parameters would be highly beneficial.
2. The writing should be improved. First, interpretation of each theoretical result is necessary. I would suggest highlighting the technical contributions for each theorem and lemma. For example, for each convergence result, it would be helpful to explicitly state the conditions under which convergence is guaranteed, the rate of convergence, and the implications of these results for practical use. Meanwhile, be careful about the equation numbering. (2) and (3) are missing in the main text; see proof of Theorem 1.

### Questions
As comparison-based optimization algorithms can be used in RLHF and LLMs, I am curious about the practical performance of these algorithms over real-world dataset and models.

### Soundness
3

### Presentation
2

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
The paper addresses optimization for scenarios where gradient computation is difficult or impossible. The authors focus on comparison-based methods, which leverage only the relative magnitudes of function values at different points, rather than their exact values or gradients. This approach is particularly relevant for cases like reinforcement learning from human feedback (RLHF) in training large language models, where only preferences, not precise rewards, are available.
The key technical contribution is a gradient direction estimation algorithm using only comparisons, which underlies the proposed optimization methods. Their work advances comparison-based optimization, demonstrating that comparisons can achieve similar performance to zeroth-order methods that require function evaluations. Future directions include adapting accelerated gradient methods to comparison-based frameworks and extending the applicability of these methods to machine learning, particularly in preference-based RL contexts.

### Strengths
Originality: 
    The paper tackles an emerging topic by focusing on optimization using only comparisons, which has relevance in preference-based reinforcement learning (RL) and derivative-free optimization scenarios. This direction is increasingly important, especially with applications in reinforcement learning from human feedback (RLHF) for large language models.

Theoretical Quality: 
    The paper provides rigorous theoretical complexity bounds for both convex and non-convex optimization, closely matching traditional zeroth-order methods. These analyses are well-supported mathematically, showing an in-depth understanding of comparison-based optimization.

Clarity: 
    The methods and algorithms are clearly explained with concise mathematical descriptions, which makes the theoretical contributions accessible and reasonably easy to follow. Definitions, assumptions, and theorems are presented in an organized manner, contributing to overall readability.

### Weaknesses
Originality: 
    While the topic is relevant, the contributions primarily extend existing methods in comparison-based and zeroth-order optimization rather than introduce fundamentally new concepts. The work’s novelty is incremental, repurposing established techniques like normalized gradient descent within a comparison-based framework. The core idea of using comparisons to estimate gradient directions, while useful, is not entirely novel, and the paper could benefit from a more detailed discussion of how its approach differs fundamentally from existing comparison-based optimization methods.

Lack of Empirical Validation: 
    The paper is exclusively theoretical, lacking experiments or simulations to verify that the proposed methods work effectively in practice. This absence limits the reliability of the results, as real-world performance, especially under noisy conditions, may deviate from the theoretical predictions. The theoretical analysis, while rigorous, does not address practical concerns such as sensitivity to hyperparameter choices or the computational overhead of the comparison-based gradient estimation.

Contextualization: 
    The paper’s literature review and discussion sections do not fully differentiate the contributions from prior work, particularly in terms of practical advantages over other comparison-based methods. This leaves the impression that the paper does not convincingly address why its approach is preferable in applications. The paper needs to more clearly articulate the specific scenarios where its method would outperform existing alternatives, and provide a more thorough analysis of the limitations of existing methods that it aims to address.

Significance: 
    The impact of the contributions is limited due to the lack of application-driven validation. While the theoretical results are valuable, without empirical demonstrations or clear real-world applicability, the significance for the broader ML community remains uncertain. The paper would be more impactful if it could demonstrate the effectiveness of its methods on benchmark problems or in practical applications, especially in the context of preference-based RL.

### Questions
1. Including experiments would significantly strengthen the paper. Can the authors provide empirical results or simulations to validate the theoretical claims, especially in noisy or real-world conditions?

2. Given the motivation in reinforcement learning from human feedback (RLHF), how might the proposed algorithms be adapted or tested in RL scenarios? A discussion on how these methods could integrate with or improve current preference-based RL approaches would add value.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes algorithms for optimization where the learner only has access to comparisons between the function values at two points. Under this setting, the authors propose algorithms for both convex and non-convex settings that achieve order-optimal performance in terms of sample complexity.

### Strengths
The proposed algorithms achieve optimal performance across a variety of cases, which cover the most commonly encountered scenarios. This provides a holistic view of comparison oracle based optimization.

I think the design of the routine for estimating if the point has negative curvature is also interesting and novel.

### Weaknesses
I think the main weakness of the paper is limited novelty. As pointed by the authors, the key technical contribution is designing the routine comparison-GDE, which builds an estimate of the gradient at a given point by querying points in the vicinity. After that all the algorithms, their design and analysis largely from existing literature.

As far as I understand, this comparison-GDE is also very similar to the gradient estimation technique in dueling convex optimization (Saha et al, 2021, 2022). The only difference is that the authors in Saha et al. use a direction drawn uniformly at random to estimate the gradient direction while the approach in this work relies on choosing the directions deterministically. In terms of both analysis and algorithm design, I see little different between the two approaches. Even in terms of computational costs, the difference is negligible. 

As mentioned in the previous response, I think the curvature estimation routine is new and interesting, but is not sufficient on its own to warrant a publication.

On a separate note, I think the motivation for the problem is also somewhat misplaced. Learning via preference based feedback for RLHF stems from a practical concern of challenges in reward estimation. For optimization, this is not the case because function is well-defined in a lot of cases and from a ML optimization point of view, comparing two function values is not necessarily simpler than computing the gradient on a batch of samples.

### Questions
1. As discussed above, what is the difference between the proposed approach and the one in Saha et al, 2021. I am more curious about the difference at a fundamental level, not the superficial difference in terms of random vectors vs deterministic choice. 

2. Also, it seems like you separate comparison oracle based optimization from dueling convex optimization. To the best of my understanding, these are technically the same thing. If anything, dueling optimization is slightly more general, allowing for noisy observations.

3. For the case where your $x$ is very close to the boundary, you will have to slightly modify the algorithm to ensure that the query points are within the domain. It is relatively simple to fix, but something that needs to be kept in mind.

4. Clearly, there is an inherent assumption that the observations are noiseless. Can the algorithm be modified to adapt to the scenario when the preference feedback is noisy?

### Soundness
3

### Presentation
3

### Contribution
1
