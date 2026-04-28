# Faster Approximation of Probabilistic and Distributional Values via Least Squares

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
The family of probabilistic values, axiomatically-grounded in cooperative game theory, has recently received much attention in data valuation. However, it is often computationally expensive to compute exactly (exponential w.r.t. the number of data to valuate denoted by $n$). The existing generic estimator costs $O(n^2\log n)$ utility evaluations to achieve an $(\epsilon,\delta)$-approximation under the 2-norm, while faster estimators have been developed recently for special cases (e.g., empirically for the Shapley value and theoretically for the Banzhaf value). In this work, starting from the discovered connection between probabilistic values and least square regressions, we propose a Generic Estimator based on Least Squares (GELS) along with its variants that cost $O(n\log n)$ utility evaluations for many probabilistic values, largely extending the scope of this currently best complexity bound. Moreover, we show that each distributional value, proposed by Ghorbani et al. (2020) to alleviate the inconsistency of probabilistic values induced by using distinct databases, can also be cast as optimizing a similar least square regression. This observation leads to a theoretically-grounded framework TrELS (Training Estimators based on Least Squares) that can train estimators towards the specified distributional values without requiring any supervised signals. Particularly, the trained estimators are capable of predicting the corresponding distributional values for unseen data, largely saving the budgets required for running Monte-Carlo methods otherwise. Our experiments verify the faster convergence of GELS, and demonstrate the effectiveness of TrELS in learning distributional values. Our code is available at https://github.com/watml/fastpvalue.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed two generic probabilistic values estimators (one for ranking and the other for exact probabilistic values) that achieves $O(\frac{N}{\epsilon^2} \log \frac{N}{\delta})$ utility evaluations, improving upon previously known generic estimators that require $O(\frac{N^2}{\epsilon^2} \log \frac{N}{\delta})$. The authors prove theoretically convergence rates of their estimators, and present their performance with numerical experiments.

### Strengths
The result is interesting and novel to me, though I am not an expert in this area. The estimators proposed is general enough, and comparisons with previous literature is thorough. The paper provides both good theoretical and numerical evidence.

### Weaknesses
1. Lack of direct comparisons to previous estimators specific to special cases achieving the same rate. I would like to see more discussions on SHAP, MSR and AME estimators. Why they cannot be generalized? What are their main ideas comparing to this paper, what is the fundamental differences?
2. It may be that I'm not familiar with the field, but the presentation does not properly introduce the background. It would be nice if the authors can provide a few more demonstrations in the introduction, i.e. examples for Shapley and Banzhaf. I did not see proper explanations on those probabilistic values while reading the paper.
3. The numerical plots could look better in log-scale, for now it's hard for me to distinguish between lines when they converge.
4. Lack of expanding on the theoretical results. Some explanations on the intuition on why an $\Theta(N/\epsilon^2)$ convergence rate is expected and what makes it different from previous estimators would be nicer.

### Questions
In conjunction with 1-4 in the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Probabilistic values, rooted in cooperative game theory, play a pivotal role in data valuation. 
However, their computation poses significant challenges, especially as dataset size (N) increases. 
Many current estimators either come with high computational overheads or cater only to specific instances.

Here are the main contributions of this paper:

* The authors introduce two versatile estimators, anchored in least squares regression, 
  capable of efficiently approximating a broad range of probabilistic values, 
  transcending the confines of earlier methods typically designed for specific values like the Shapley value. 
  (Refer to Sections 3.1 and 3.2)
* Through Propositions 3 and 5, the authors establish that both novel estimators necessitate only O(N log N) utility evaluations 
  to achieve a (ε,δ)-approximation, thereby aligning with the best-known computational complexities for certain cases.
* Section 3.3 unveils a pioneering approach to cast the distributional value—a more consistent alternative 
  to probabilistic values—as a least squares problem. 
  This breakthrough facilitates the training of machine learning models that can swiftly gauge distributional values of unseen data in a single pass.
* Validating the efficacy of their proposals, Section 4 presents experiments that 
  substantiate the accelerated convergence of their estimators compared to preceding methods. 
  Moreover, they successfully illustrate the potential of training models to adeptly predict distributional values for novel data points.

### Strengths
* The paper introduces efficient methods for both ranking and value estimation of data points. 
  Through Propositions 1 and 2, they've laid out a mechanism to estimate the relative ranking underlying any probabilistic value.
  Notably, this method is computationally advantageous.
* They've established a framework, as seen in Theorem 1 and the related discussions, for training models to serve as value estimators. 
  This is highly valuable, as trained models can swiftly evaluate any unseen data point 
  from similar distributions in just a single forward pass, making the evaluation process much more scalable.

### Weaknesses
 * There are computational challenges associated with training value estimators. When evaluating the distributional values, even with approximations, the computational costs are significant. 
* The paper mentions that the faster convergence of certain estimators like SHAP, SHAP-paired, and the complement comes at the cost of using Θ(N^2) memory storage instead of Θ(N). However, the implications of this memory increase, especially for large-scale applications, are not discussed in depth. Specifically, the paper does not detail how this increased memory requirement affects the scalability of these methods when dealing with massive datasets, nor does it explore potential strategies to mitigate these memory constraints.

### Questions
* While the paper presents a novel approach to data valuation using distributional Shapley values, could you shed light on the practical applications where this approach might be most beneficial?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an algorithm that estimates the probabilistic value $v_i$ of each data point $i\in[n]$, i.e., $v_i:=\sum_{S\subseteq [n]\setminus \{i\}} p_{|S|}\cdot (U(S\cup \{i\})- U(S))$, where $U$ is a given utility function that maps any subset of data points to a value, and the weights $p_{k}$'s can be chosen arbitrarily by the user, as long as they satisfy $\sum_{k=0}^{n-1} p_k\cdot \binom{n-1}{k} = 1$. The well-known Shapley value is a special case of the probabilistic value. Their estimator uses $O(n\log n)$ evaluations of the utility function $U$, an improvement over the previous work [Kwon and Zou 2022] which uses $O(n^2\log n)$ evaluations.

Their estimator is based on a simple observation: because $\sum_{S\subseteq [n]} p_{|S|}\cdot U(S)=\sum_{S\subseteq [n]\setminus\{i\}} p_{|S|}\cdot U(S) + \sum_{S\subseteq [n]\setminus\{i\}} p_{|S|+1}\cdot U(S\cup\{i\})$, we have $\sum_{S\subseteq [n]\setminus\{i\}} p_{|S|}\cdot (U(S\cup \{i\})- U(S)) + \sum_{S\subseteq [n]} p_{|S|}\cdot U(S) = \sum_{S\subseteq [n]\setminus\{i\}} (p_{|S|}+p_{|S|+1})\cdot U(S\cup i)$.

Hence, their method uses random sampling to simultaneously estimate $v_i':=\sum_{S\subseteq [n]\setminus\{i\}} (p_{|S|}+p_{|S|+1})\cdot U(S\cup i)$ for all $i\in[n]$ and $\sum_{S\subseteq [n]} p_{|S|}\cdot U(S)$, and then substracts the later from the former to get the estimates of $v_i$ for all data points $i\in[n]$.

The advantage of their method is that a random sample $S\subseteq [n]$ can be used to estimate $v_i'$ for all $i\in S$ simultaneously, using just a single evaluation of the utility function -- $U(S)$. In comparison, if we use the sample $S$ to estimate the $v_i$ for all $i\in S$ directly, we would need to evaluate $v(S\setminus \{i\})$ for all $i\in S$. Thus, they get an improvement from $O(n^2\log n)$ evaluations to $O(n\log n)$ evaluations.

### Strengths
- The idea is simple and cute.
- The writing is fine overall.

### Weaknesses
 - The result is technically a bit thin.
- The least squares interpretation seems a bit artificial and redundant.
- From the experiments in appendix, it is not obvious to me that the proposed estimator is any better than previous works (e.g., the well-known SHAP for estimating Shapley value).

### Questions
Could you elaborate the advantage of your estimator over previous works in terms of practical performance?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes two generic estimators of the importance value of the $i$-th data point for the whole family of probabilistic values. Both estimators require $O(\frac{N}{\epsilon^2}\log\frac{N}{\delta})$ evaluations to obtain $(\epsilon,\delta)$-approximation, which is the optimal among known bounds. Further, the paper designs a framework for computing the distributional value estimator by connecting it to the obtaining least square regression. Vast experimental results show the faster convergence of the estimator over other benchmarks.

### Strengths
The paper extends the current results to general probabilistic values by resolving the main limitation in computing the estimator of importance value. Further, the connection between estimating distributional value and the least square estimator in (13) saves computational costs drastically. These results have a potentially significant impact on data valuation.

### Weaknesses
(1) One major concern I have is whether $\gamma$ (which is defined in the proof of Proposition 3 and 5) is a constant independent of $N$ for any probability values $\mathbf{p}$. It seems that setting $p_1 =1/2$ and $p_i \approx 0$ for $i>1$ yields $\gamma=O(1/N)$. As the $\gamma$ appears in the bound [(34) and (39)] for the number of evaluations, this seems critical in the first main contribution. Specifically, the dependence of $\gamma$ on the probability distribution $\mathbf{p}$ is not sufficiently explored, and it is unclear if the proposed estimators maintain their efficiency for all possible $\mathbf{p}$. A more rigorous analysis of the behavior of $\gamma$ under various choices of $\mathbf{p}$ is needed to solidify the theoretical claims.

(2) The intuitive explanation of how the generalization to general $\mathbf{p}$ is possible should be included in the main text. The current explanation is not sufficient to understand the core mechanism behind the generalization. It would be beneficial to provide a more detailed explanation of the mathematical techniques or insights that allow the method to handle a wide range of probability values.

(3) Discussion on the cases when $\phi_i^{\mathcal{B},\mathbf{w}}(U)$ in Theorem 1 is close to $\phi_i^{\mathcal{D},\mathbf{w}}(U)$ would be helpful. The paper should elaborate on the conditions under which the empirical estimator closely approximates the true distributional value. This would include a discussion on the properties of the data distribution and the size of the dataset required for convergence. Furthermore, it would be beneficial to discuss the implications of using a finite sample approximation and the potential biases that may arise.

### Questions
Q1. Is $\gamma$ defined in the proof of Proposition 3 and 5 is a constant independent of $N$?
Q2. How the generalization to a general family of probability values $\mathbf{p}$ is possible?
Q3. When can $\phi_i^{\mathcal{B},\mathbf{w}}(U)$ converge to $\phi_i^{\mathcal{D},\mathbf{w}}(U)$? Could any convergences results be derived?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
