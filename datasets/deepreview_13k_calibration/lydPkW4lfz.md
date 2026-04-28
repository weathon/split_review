# Local Steps Speed Up Local GD for Heterogeneous Distributed Logistic Regression

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 8, 6, 3

## Abstract
We analyze two variants of Local Gradient Descent applied to distributed logistic regression with heterogeneous, separable data and show convergence at the rate $O(1/KR)$ for $K$ local steps and sufficiently large $R$ communication rounds. In contrast, all existing convergence guarantees for Local GD applied to any problem are at least $\Omega(1/R)$, meaning they fail to show the benefit of local updates. The key to our improved guarantee is showing progress on the logistic regression objective when using a large stepsize $\eta \gg 1/K$, whereas prior analysis depends on $\eta \leq 1/K$.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies distributed logistic regression in the context of local gradient descent (GD) with heterogeneous, separable data. 

It introduces two variants of Local GD: **Two-Stage Local GD** and **Local Gradient Flow (GF)**. 

The authors demonstrate a faster convergence rate than prior work for Local GD with $O(1/(KR))$ when using large local steps $K$ and large communication rounds $R$, contrasting previous results that show convergence at $O(1/R)$. 

The key insight is leveraging the logistic regression objective, which allows using a large step size $\eta \gg 1/K$ after a warmup period, instead of the conventional $\eta \leq 1/K$. 

They support the theoretical findings with experimental results on synthetic and MNIST datasets.

### Strengths
1. **Novel Insight into Local Steps for Distributed Logistic Regression:**

   The paper identifies a specific problem where local updates accelerate convergence, contrasting with past worst-case complexity results for Local GD. Though It focuses on the logistic loss, the result is quite new and interesting.

2. **Clear Theoretical Contributions:**

   The convergence rates for Two-Stage Local GD and Local GF are supported with rigorous theoretical analysis and are novel improvements over existing results in the distributed logistic regression setting. The proof sketch also helps readers understand the key idea better.

3. **Experimental Validation:**
   The paper includes experiments on both synthetic and real datasets, demonstrating the behavior of the proposed algorithms under different stepsizes and local steps, which supports their claims empirically

### Weaknesses
1. **Lack of Generality:**

   While the theoretical results are interesting, the scope is limited to distributed logistic regression. The analysis heavily relies on the specific properties of the logistic loss function, such as its smoothness and the separability of the data. This raises questions about the applicability of the proposed algorithms and their convergence guarantees to other common loss functions used in distributed learning, such as those arising in neural networks or other generalized linear models. The paper does not explore or discuss potential extensions or modifications needed to handle non-logistic loss functions.

2. **Weak Experimental Setup:**
   The experiments focus primarily on very small synthetic and MNIST datasets, which do not fully reflect the complexity of real-world distributed learning scenarios. The synthetic datasets are too simplistic, and MNIST, while a standard benchmark, is not representative of the scale and heterogeneity encountered in many practical distributed learning applications. The paper lacks experiments on larger, more complex datasets with higher dimensionality and more realistic data distributions, which would be necessary to validate the practical effectiveness of the proposed methods.

3. **Unclear Justification of Baseline Comparisons:**

   The comparison to previous methods could be more thorough, particularly regarding the baselines. The paper briefly mentions the worst-case results for Local GD but does not provide detailed analysis or experiments to compare directly to existing algorithms like Minibatch SGD. The paper should include a direct comparison with Minibatch SGD, showing how the proposed algorithms perform under similar conditions. The current evaluation does not clearly demonstrate the advantage of the proposed methods over standard distributed optimization techniques.

### Questions
1. **Extending to Self-Concordant Functions:**

   Could the analysis be extended to **self-concordant functions**? As introduced in [Francis Bach’s blog](https://francisbach.com/self-concordant-analysis-for-logistic-regression/), the self-concordant framework might offer additional insights. Some references are missing from the related work section, particularly the paper by **Francis Bach (2014)** on **adaptivity of stochastic gradient descent**. Including such references would strengthen the connection between your work and existing literature on logistic regression.

2. **Multiple Stages and Adaptive Stepsizes:**

   The paper discusses a **two-stage approach**, but have you considered the potential of using **multiple stages** with **adaptive stepsizes**? Would this lead to better communication round complexity, or do you believe two stages are already sufficient?

3. **Clarification of Equation (13):**

   Can the authors clarify why the bound in **line 297** (Equation 13) holds? Specifically, the reasoning behind using Lemma 3 to bound the right-hand side of (13) is unclear and would benefit from further explanation.

4. **Interpretation of $r_0$:**

   Could the authors explain the meaning of **$r_0$** in **Theorem 1**? This parameter plays a crucial role in the analysis, but its practical interpretation or impact on the algorithm’s behavior is not clearly discussed.

5. **Strange subfigures in Figure 1:**

The left column of Figure 1 is quite strange as only one curve is there. No explanation is provided.

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
4

### Summary
This paper considers distributed logistic regression and analyzes two variants of Local Gradient Descent, one with two-phases and a restart in the middle, and another (unimplementable) algorithm where the gradient flow is used as the "local optimizer" on each node before averaging. The main motivation for the paper is the longstanding open problem in distributed optimization: why do local methods (like Local GD) work well when the theoretical guarantees are outperformed by (accelerated) minibatch SGD in the worst case? By restricting specifically to distributed logistic regression, we can study this question in a specific setting.

### Strengths
1. I really like the idea of studying the performance of Local GD in the setting of distributed logistic regression. The paper's suggestion that the benefit of local methods might be dependent on the loss landscape rather than decreasing client dissimilarity is an interesting one, that I think might inspire much further work.

2. The paper is written clearly, and is well-organized. 

My main issue with this paper is that I believe there might be an issue with the proof (see weaknesses section). For this reason, I can't really recommend acceptance.

### Weaknesses
My main issue with the paper is the proof issue mentioned below, which affects the paper's main theorem.

1. (Proof issue) When going from equation (296) to equation (297), you use the condition $\eta \leq 1/(4H)$ to bound $-(2\eta-4\eta^2 H) (F(\bar{w}_t) - F(u))$ by $-\eta (F(\bar{w}_t) - F(u))$. But you can only do this in case $F(\bar{w}_t) - F(u) \geq 0$. Here, $u$ is not necessarily the minimizer. Lemma 17 should hold for any $u$ but clearly this is not true. This issue is repeated when going from (352) to (353). Since the results of Theorem 1 relies on these corollaries, it is affected as well. I'm not really sure how to fix this issue. I guess you could restrict $u$ to only comes from the points that have a lower loss, but then the proofs of Corollaries 1 and 2 would have to be modified to accommodate this. 

2. (Toy setting) The Local Gradient Flow guarantee is in a very toy setting, $M=2$ and $n=1$ plus an unimplementable gradient flow subroutine is in general very questionable as a model for anything realistic.



### Questions
1. Please address the proof issue mentioned in the weaknesses section.
2. Can we recover the same results you have by including some small regularization on the logistic regression problem, then use the fact that this problem has a minimizer?
3. (GD baseline) Shouldn't we compare not against the Local GD bounds, but also include the "trivial" GD/Minibatch SGD bound as a baseline? After all, the paper's hypothesis (that we can use larger stepsizes, hence the improved rate) would motivate us to compare against GD where we also use a warmup period.

### Soundness
2

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
3

### Summary
The paper "Local Steps Speed up Local GD for Heterogeneous Distributed Logistic Regression" proposes a two phase variant of Local SGD for which the authors can establish that despite the presence of heterogeneity will asymptotically benefit from increasing the size of the local mini-batch. This is an improvement when compared to existing lower bounds for general convex functions as it exploits additional structure of the logistic regression problem.

### Strengths
1) The paper is very well written
2) The contribution is interesting as it provides a stepping stone to understand when local SGD can be used with clear benefits, despite the fact that for the classical set of families of functions studied we know it does not.
3) The authors do a good job at providing a sketch of the proof of the main result that manages to capture the idea behind the proof.

### Weaknesses
1) Limitation in scope: from this reviewer's perspective, the conditions under under which the bias introduced by heterogeneity could potentially apply to other problems (that is total loss controls the gradient and Hessian size). The condition of separability may potentially be replaced by an interpolation condition. What is the limitation that allows the work to focus exclusively on logistic regression? 
2) Dependence on gamma: as gamma decreases the amount of time required within the first stage increases. This implies that a lower bound on gamma is required. A lower bound to it would have to be computed and shared across agents.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
For logistic regression, the paper proves convergence of local GD improves with number of local updates, based on a two-stage estimator (two stages with two different choice of step size)

### Strengths
The paper shows for a special case that the convergence rate is inversely proportional to number of local udpates

### Weaknesses
The analysis only applied to logistic regression, and only applies to linearly separately case (which is of course a simple case that usually is not satisfied, or unknown whether it is satisfied). The paper's presentation keeps switching between local GD and local SGD, this is very confusing why you use SGD. It is unclear why the analysis focuses on a two-stage estimator with two different step sizes, as this seems like an arbitrary choice that is not well-motivated. The paper claims a convergence rate inversely proportional to the number of local updates, but it is not clear if this is a practically significant improvement, or if it is just a theoretical curiosity. The paper does not discuss the practical implications of the two-stage estimator, such as how to choose the two different step sizes, and whether the two-stage approach is more computationally expensive than a single-stage approach.

### Questions
1. The paper's presentation keeps switching between local GD and local SGD, this is very confusing why you use SGD
2. Is there any other loss whose derivative is bounded by loss?
3. is the rate optimal in some sense?

### Soundness
2

### Presentation
2

### Contribution
2
