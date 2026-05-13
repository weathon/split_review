# The Utility and Complexity of In- and Out-of-Distribution Machine Unlearning

- Decision: Accept
- Scores: 8, 6, 6, 8, 5

## Abstract
Machine unlearning, the process of selectively removing data from trained models, is increasingly crucial for addressing privacy concerns and knowledge gaps post-deployment. Despite this importance, existing approaches are often heuristic and lack formal guarantees. In this paper, we analyze the fundamental utility, time, and space complexity trade-offs of approximate unlearning, providing rigorous certification analogous to differential privacy. For in-distribution data, we show that a surprisingly simple and general procedure—empirical risk minimization with output perturbation—achieves tight unlearning-utility-complexity trade-offs, addressing a previous theoretical gap on the separation from unlearning ``for free" via differential privacy. However, such techniques fail out-of-distribution, where unlearning time complexity can exceed that of retraining, even for a single sample. To address this, we propose a new robust and noisy gradient descent variant that provably amortizes unlearning time complexity without compromising utility.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work analyses the utility and complexity trade-offs in approximate machine unlearning, focusing on both in-distribution and out-of-distribution scenarios. The authors address the challenge of efficiently removing specific data from trained models. For in-distribution data, they demonstrate that ERM with output perturbation can achieve tight trade-offs between unlearning accuracy and computational complexity, connecting a theoretical gap regarding differential privacy limitations in unlearning. However, they identify that these techniques do not work with out-of-distribution data, where the unlearning process can become less efficient than retraining from scratch. To overcome this, the paper introduces a robust and noisy gradient descent algorithm that maintains utility while improving unlearning efficiency in out-of-distribution contexts.

### Strengths
* The paper provides an in-depth theoretical exploration of the utility and complexity trade-offs in approximate machine unlearning, which I liked and found beneficial.
* The authors tackle unlearning in both in-distribution and out-of-distribution (OOD) contexts and make an interesting separation between the scenarios
* A notable contribution is the introduction of a robust and noisy gradient descent algorithm (Algorithm 2) for OOD unlearning. 
* The paper addresses and resolves a theoretical question Sekhari et al. (2021) posed regarding dimension-independent utility deletion capacity. 
* Overall, it is well-written and straightforward to follow.

### Weaknesses
 * Strong Assumptions Limit Applicability: The theoretical results rely on assumptions such as strong convexity, smoothness of the loss function, and the existence of a unique global minimum. While these are standard assumptions for theoretical work, their applicability in practice needs to be clarified. Specifically, the strong convexity assumption, while simplifying the analysis, is rarely met in practical deep learning scenarios, where loss landscapes are often highly non-convex and contain saddle points and multiple local minima. The reliance on a unique global minimum further limits the scope, as many models, especially neural networks, have multiple global minima that can lead to different model behaviors.
* Limited Experimental Evaluation: The experimental validation is conducted on relatively simple tasks, such as linear regression with synthetic data. This raises concerns about the generalizability of the findings to more complex, real-world scenarios. The use of synthetic data, while allowing for controlled experiments, does not fully capture the complexities of real datasets, which often exhibit high dimensionality, noise, and non-linear relationships. The absence of experiments on benchmark datasets or with more complex models makes it difficult to assess the practical impact of the proposed algorithms.
* Assumption of Known Forget Set Size: The algorithms and theoretical guarantees often assume that the size of the forget set is known and relatively small compared to the total dataset size. This assumption is not always realistic, as in many practical unlearning scenarios, the size of the forget set may not be known in advance or may be a significant portion of the total dataset. This limitation could severely impact the applicability of the proposed methods in real-world settings where the forget set size is uncertain or large.

### Questions
* Am I correct in stating that unlearning is not generally possible for non-convex models without a unique minimiser? Can the authors comment on relaxing their assumption to general non-convex models? 
* Could access to a global minimiser be relaxed with a weaker assumption, like the optima within a bounded set of known diameters?

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
4

### Summary
The paper presents a theoretical analysis of the utility and complexity trade-offs in approximate machine unlearning with the deletion capacity under fixed error bound and computational budgets. The authors consider both in-distribution and out-of-distribution unlearning scenarios and propose a new robust and efficient variant of the gradient descent method for the latter situation.

### Strengths
1. The study of the out-of-distribution scenario is very meaningful. 
2. The insight of deletion capacity under fixed computational budgets while maintaining utility is novel.
3. The theoretical analysis is rigorous.
4. The paper is well-organized.

### Weaknesses
1. Adding a detailed explanation of out-of-distribution in Abstract would be better.
2. The reviewer is quite confused about Definition 2. 
   - $\mathcal Z^*$ is a space (stated on line 127) rather than "the set of training sets". Please clarify the definition and usage of $\mathcal Z^*$. It's unclear how a space can be a set of training sets. The definition needs to specify the nature of the elements within $\mathcal{Z}^*$ more precisely. Are they individual data points, sets of data points, or something else? This ambiguity makes it difficult to understand the subsequent theoretical analysis.
   - Does $\mathcal L*$ represent the minimum population risk on the training set or retain set? Simply defining $L*:=\min\mathcal L(\theta)$ (without the dataset) is not clear. Please specify over which dataset $\mathcal L^*$ is defined. It is crucial to specify the domain over which the minimization is performed. Is it over the entire data distribution, or a specific subset? The lack of clarity here undermines the rigor of the theoretical framework.
   - Should $\mathcal L_{\mathrm {ID}}$ and $\mathcal L_{\mathrm{OOD}}$ be bounded by a certain value? The absence of explicit bounds on these loss functions raises concerns about the applicability of the theoretical results. Without bounds, it's unclear if the analysis holds for all possible loss functions, or if there are specific conditions that need to be met. This needs to be clarified to ensure the robustness of the theoretical claims.
3. The authors should add descriptions of gradient descent in Algorithms 1 and 2. It is not clear how the algorithms are implemented without specifying the optimization method used. The description should include details such as the learning rate, batch size, and stopping criteria.
4. Lack of explanation for the initialization error $\Delta$. The paper should clearly define how this error is calculated and its implications for the analysis. Is it a fixed value, or does it depend on the dataset or model parameters? The lack of clarity makes it difficult to assess the practical relevance of the theoretical results.
5. Although this work focuses more on the theoretical part, it is still better to provide some preliminary results on some datasets under practical scenarios. The theoretical analysis would be more convincing with some empirical validation, even if it's preliminary. This would help to demonstrate the practical relevance of the proposed methods.
6. Some typos, e.g., missing bold for $\theta$ in Table 1.

### Questions
What is "procedure 2" in Algorithm 2? Please either define "procedure 2" explicitly in Algorithm 2, or remove this reference if it's not needed.

### Soundness
3

### Presentation
2

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
This paper studies the problem of machine unlearning, the removal of certain data points from a model after unlearning, for both in and out of distribution data, with a focus on the deletion capacity of unlearning algorithms. First, they present a general theorem for analyzing the utility deletion capacity of an unlearning algorithm, the number of deletions an unlearning algorithm can tolerate while maintaining some error rate. Next, they present an algorithm (Algorithm 1) for unlearning in-distribution data using a noisy ERM approximation and analyze the time and space complexity of their algorithm. They demonstrate that the time complexity of Algorithm 1 can become unbounded for even a single out-of-distribution data removal, and propose a new algorithm for unlearning out-of-distribution data using gradient descent with coordinate-wise trimmed mean gradients.

### Strengths
The theoretical study of out-of-distribution deletions in unlearning is valuable and lacking in the unlearning literature.

Proposition 1 gives a generic framework for assessing the very important tradeoff between utility and deletion capacity which I think could be very informative to the community.

### Weaknesses
I think this paper would be improved by a comparison of the utility and computational deletion capacity between the Noisy-GD algorithm from Chourasia and Shah [2023]. The algorithms are very similar and Chourasia and Shah [2023] also have a detailed discussion of the tradeoffs between utility, deletion capacity, and computation time of their algorithm.

For the unlearning algorithms in this paper, the learning and unlearning time are both $\tilde{O}(nd)$. Although some time is saved during unlearning, the goal of unlearning is to unlearn using significantly less time than retraining from scratch. The fact that the unlearning time has the same asymptotic complexity as the learning time is a significant drawback, especially since the practical motivation for unlearning is to quickly remove data points without needing to retrain from scratch. This is particularly concerning given that the unlearning process would likely be invoked much more frequently than the initial training phase.

For Table 1, wouldn’t it be more fair to just compare unlearning times, rather than the sum of both learning and unlearning times? Especially since the goal of unlearning is primarily to process deletion requests quickly at the time of unlearning, and one would have to unlearn many more times than one would have to learn. For example, the unlearning time of Sekhari et al [2021] is independent of n, even though the learning time depends on n, but this distinction isn’t clear in Table 1. Perhaps separate columns for learning and unlearning times would make the comparison more clear

### Questions
For Table 1, wouldn’t it be more fair to just compare unlearning times, rather than the sum of both learning and unlearning times? Especially since the goal of unlearning is primarily to process deletion requests quickly at the time of unlearning, and one would have to unlearn many more times than one would have to learn. For example, the unlearning time of Sekhari et al [2021] is independent of n, even though the learning time depends on n, but this distinction isn’t clear in Table 1. Perhaps separate columns for learning and unlearning times would make the comparison more clear

Suggestions

In line 203, I would suggest using a different variable (other than alpha), such as epsilon, because alpha has been used to represent the bound on the generalization error, but in line 203, it is being used to represent a bound on the empirical error.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a theoretical analysis of the utility and complexity trade-offs in approximate machine unlearning, with in-distribution and out-of-distribution cases. For the former one, the authors uncover the dimension independency with the help of an optimisation procedure with output perturbation. For the latter one, which is more challenging and under explored, the authors propose a robust gradient descent variant with satisfying time and space complexity, and corresponding statistical guarantee.

### Strengths
The paper is very well-written. The problem addressed in the paper is important and interesting, with solid theoretical insights on both in-distribution and out-of-distribution cases. The discussion is comprehensive and the comparisons with the differential privacy and the illustrations are insightful to me.

### Weaknesses
None.

### Questions
None.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a comprehensive framework for approximating the trade-off between deletion utility and complexity, addressing two complementary deletion scenarios: when the forget set is in distribution and when the forget set is out of distribution. The author's algorithm defines that the optimal values of unlearning algorithms and retraining algorithms can be bounded, allowing for the derivation of the utility and time complexity of gradient descent algorithms based on this bound to achieve a balance between utility and complexity. However, the author does not provide a proof for this bound.

### Strengths
1. Exploring unlearning algorithm with theoretical guarantees is very meaningful, as the paper states that existing heuristic algorithms lack formal guarantees, rendering it unclear when they comply with regulatory standards.

2. Analyzing unlearning when the forgotten data can deviate arbitrarily from the test distribution have certain significance in some potential cases.

### Weaknesses
 1. **Theoretically**
   - **Lack of Necessary Proof:** The author directly defines that the outputs (models) of the unlearning and retraining algorithms satisfy (Equation 12), $\left\|\theta^{\mathcal{U}}-\boldsymbol{\theta} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star}\right\|^2 \leq \frac{\alpha \varepsilon}{4 L d},$ but lacks a crucial proof for Equation 12. 

Specifically, The author defines (Equation 12), and proves that the utility objectives $\mathcal{L}\left(\mathcal{U}\left(\mathcal{S} _ f, \mathcal{A}(\mathcal{S})\right) ; \mathcal{S} \backslash \mathcal{S} _ f\right)-\mathcal{L} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star} \leq \alpha$ (Equation 16) based on Equation 12. They then state that within $T=\mathcal{O}\left(n d \log \left(1+\frac{d}{\alpha \varepsilon}\left(\frac{R f}{n}\right)^2\right)\right)$time, it's possible to guarantee that the optimization achieves a difference in Equation 16 that is less than $\alpha$. However, just because the optimization leads to a result less than $\alpha$ in Equation 16, it doesn’t mean the unlearning model $\theta^{\mathcal{U}}$ and the minimum values of  retraining algorithms satisfy $\left\|\theta^{\mathcal{U}}-\boldsymbol{\theta} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star}\right\|^2 \leq \frac{\alpha \varepsilon}{4 L d}$.  In other words, at time $T$, the model we found satisfies Equation 16, but it does not necessarily satisfy Equation 12.

For instance, consider the $L$-smoothness function $\mathcal{L}(\theta _ 1,\theta _ 2,\theta _ 3) = \theta _ 1^2 + \theta _ 2^2 + \frac{1}{{10}^6} \theta _ 3^2$ which has $L=2$ and dimension $d=3$, with the optimal value occurring at $(\theta _ 1,\theta _ 2,\theta _ 3)=(0,0,0)$. Let $\epsilon=2400, \alpha=0.01$. According to the author’s definition in Equation (12), it follows that $\left\|\theta^{\mathcal{U}}-\boldsymbol{\theta} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star}\right\|^2 \leq \frac{\alpha \varepsilon}{4 L d} \leq 1$  and we can derive that $\mathcal{L}\left(\mathcal{U}\left(\mathcal{S} _ f, \mathcal{A}(\mathcal{S})\right) ; \mathcal{S} \backslash \mathcal{S} _ f\right)-\mathcal{L} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star} \leq 0.01$. When unlearning algorithm optimizes to a loss difference of less than 0.01 in $T$ time, we still cannot guarantee $\left\|\theta^{\mathcal{U}}-\boldsymbol{\theta} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star}\right\|^2 \leq 1$ .A counterexample illustrates this: taking $(\theta _ 1,\theta _ 2,\theta _ 3)=(0,0,100)$,  we find $\mathcal{L}(\theta _ 1,\theta _ 2,\theta _ 3)-\mathcal{L}(0,0,0) = 0.01$, but $||(\theta _ 1,\theta _ 2,\theta _ 3)-(0,0,0)||^2=(100)^2 \gg1$.  Hence, the author should firstly prove bound  $\left\|\theta^{\mathcal{U}}-\boldsymbol{\theta} _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\star}\right\|^2$ similarly to [Ref 1] in order to proceed with the subsequent analysis.
   - For $\mathcal{U}\left(\mathcal{S} _ f, \mathcal{A}(\mathcal{S})\right):=\boldsymbol{\theta}^{\mathcal{U}}+\mathcal{N}\left(0, \frac{\alpha}{2 L d} \mathbf{I} _ d\right)$ and $\mathcal{U}\left(\varnothing, \mathcal{A}\left(\mathcal{S} \backslash \mathcal{S} _ f\right)\right):=\theta _ {\mathcal{S} \backslash \mathcal{S} _ f}^{\mathcal{A}}+\mathcal{N}\left(0, \frac{\alpha}{L d} \mathbf{I} _ d\right)$，please check Equation 15, $\mathrm{D} _ q\left(\mathcal{U}\left(\mathcal{S} _ f, \mathcal{A}(\mathcal{S})\right) \| \mathcal{U}\left(\varnothing, \mathcal{A}\left(\mathcal{S} \backslash \mathcal{S} _ f\right)\right)\right)=\frac{q}{2 \cdot \frac{\alpha}{2 L d}}\left\|\theta^{\mathcal{u}}-\boldsymbol{\theta} _ {\mathcal{S}}^{\mathcal{A}} \backslash \mathcal{S} _ f\right\|^2$, is consistent with the Rényi divergence expression between multivariate Gaussians given by: $D _ q\left(f _ i \| f _ j\right)= \frac{q}{2}\left(\boldsymbol{\mu} _ i-\boldsymbol{\mu} _ j\right)^{\prime}\left[\left(\Sigma _ q\right)^*\right]^{-1}\left(\boldsymbol{\mu} _ i-\boldsymbol{\mu} _ j\right)  -\frac{1}{2(q-1)} \ln \frac{\left|\left(\Sigma _ q\right)^*\right|}{\left|\Sigma _ i\right|^{1-q}\left|\Sigma _ j\right|^q},\ \  \left(\Sigma _ q\right)^*=q \Sigma _ j+(1-q) \Sigma _ i$. The paper did not provide the derivation process, and the result I obtained based on the expression above is inconsistent with the authors.
   - For a gradient method, assumptions such as a unique empirical loss minimizer and strong convexity limit its applicability.
2. **Experiments:** The paper lacks experimental evaluation, only providing a comparison of differential privacy in Figure 1. The author should compare their work with relevant unlearning research. While it's understandable that cutting-edge certified unlearning approaches, as a gradient method, it should at least be conduct experiment for existing gradient methods, such as [Ref 1]. Additionally, the author should report runtime and other metrics, such as privacy budget.
3. **Clarity：** The author should further explain in what privacy contexts data forgetting may encounter out-of-distribution issues to highlight the significance of this research. Considering that all users may submit deletion requests, this means we cannot guarantee that every piece of data to be removed from the model is out-of-distribution and may be far smaller than the in-distribution data. This uncertainty could complicate the design of forgetting mechanisms.
4. **Notation:** The author's notation and symbolic system are very confusing and unclear. The definition of $\alpha$ is confusing: in #203 it refers to worst-case deletion error, in #217 it denotes approximation error, in #234 it is used for the training procedure to approximate the empirical risk minimizer up to squared distance (which seems to conflict with the notation in #220), and in #256 it represents precision.  Please ensure a consistent definition.  Additionally, is $S _ f$ an unlearning request or the forget set as stated in #119? If $S _ f$ represents the forget set, then Equation 3 implies that your unlearning algorithm only needs to utilize the forget set, which conflicts with your algorithm. Furthermore, the paper contains many undefined symbols, such as $\theta _ S^A,\theta _ S^{A _ f}$.

### Questions
1. In Algorithm 1, it is required that the unlearning algorithm approximates the retraining risk minimizer on $\mathcal{S} \backslash \mathcal{S}_f$  to a squared distance of $\frac{\pi \in}{4 L \mathcal{d}}$. This requirement is unreasonable because we do not know when the unlearning algorithm approaches $\frac{\pi \in}{4 L \mathcal{d}}$. We have no way of knowing whether the output of the algorithm can even be bounded by this value in relation to the retraining risk minimizer. 

2. Considering that there is already a definition of efficiency, it is not wise to extend deletion capacity to computational efficiency. Specifically, deletion capacity was initially intended to understand the relationship between the maximum number of samples that can be deleted and generalization error. The author additionally defines computational (efficiency) deletion capacity, which refers to the maximum number of samples that can be removed within a fixed time overhead. I do not recommend such a generalization, as there are already related metrics, making it a redundant definition. Otherwise, we could generalize deletion capacity to all unlearning metrics, such as efficacy deletion capacity (the maximum number of samples that can be deleted while maintaining good remaining accuracy) and fidelity deletion capacity (the maximum number of samples that can be deleted while maintaining good forget accuracy).

[Ref 1] Descent-to-Delete: Gradient-Based Methods for Machine Unlearning. Seth Neel, Aaron Roth, Saeed Sharifi-Malvajerdi. Proceedings of the 32nd International Conference on Algorithmic Learning Theory, PMLR, 2021.

### Soundness
3

### Presentation
2

### Contribution
3
