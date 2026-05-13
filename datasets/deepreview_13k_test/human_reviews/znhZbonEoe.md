# Understanding the Stability-based Generalization of Personalized Federated Learning

- Decision: Accept
- Scores: 6, 3, 6, 8

## Abstract
Despite great achievements in algorithm design for Personalized Federated Learning (PFL), research on the theoretical analysis of generalization is still in its early stages. Some recent theoretical results have investigated the generalization performance of personalized models under the problem setting and hypothesis in the convex condition, which do not consider the real iteration performance during the non-convex training. To further understand the testing performance from the theoretical perspective, we propose the first algorithm-matter generalization analysis with uniform stability for the typical PFL method Partial Model Personalization on smooth and non-convex objectives. In an attempt to distinguish the shared and personalized errors, we decouple the shared aggregation and the local fine-tuning progress and illustrate the interaction mechanism between the shared and personalized variables. The algorithm-matter generalization bounds analyze the impact of the trivial hyperparameters like learning steps and stepsizes as well as the communication modes in both Centralized and Decentralized PFL (C-PFL and D-PFL), which also concludes that C-PFL generalizes better than D-PFL. Combined with the convergence errors, we then obtain the excess risk analysis and establish the better early stopping point for the optimal population risk of PFL. Promising experiments on CIFAR dataset also corroborate our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the generalization gaps of personalized federated learning (PFL) under centralized and decentralized cases. Uniform stability tools are used to derive generalization upper bounds that reflect the influences of graph topologies.

### Strengths
The paper provides generalization bounds leveraging uniform stability of the algorithm for PFL under both centralized and decentralized settings. The bounds are topology-related, which provides new insight in how graph structures affect the generalization.

### Weaknesses
1. The main weakness of the paper is that the bounds do not recover the centralized training with SGD. To be specific, PFL reduces to centralized SGD when $K=1$ and $v_i$ is constant $\forall i \in [m]$. However, the proposed bounds in Theorem 1 indicate a worse performance than SGD (Hardt et al., 2016). 

2. The analysis of the paper is standard as literature, which means there is limited technical contribution of this paper.

3. Shown by (Sun, Niu, Wei, 2024), the generalization of FL is affected by different data heterogeneity levels, while this paper does not capture such phenomenon.

I am willing to raise the score if my concerns are addressed.

Reference:

Sun, Z., Niu, X., & Wei, E. (2024, April). Understanding generalization of federated learning via stability: Heterogeneity matters. In International Conference on Artificial Intelligence and Statistics (pp. 676-684). PMLR.

### Questions
1. Why does not the bound Theorem 1 match the centralized SGD if $K=1$ without personalization? Is it due to technical analysis? Could the authors solve such technical issue?

2. What are the main technical difficulties in the analysis, comparing to existing literature?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper derives uniform-stability-based generalization bounds (as defined in [1]) for personalized federated learning (FL). Bounds are derived in both the centralized setting (where there is a central server) and the decentralized setting. By combining the derived bounds with existing bounds on the optimization error, the paper provides an expression for the number of communication rounds which they claim is the optimal number of rounds to minimize the total (= optimization + generalization) error. Some experiments are performed to validate some of the theoretical insights.

[1]: Moritz Hardt, Ben Recht, and Yoram Singer. Train faster, generalize better: Stability of stochastic gradient descent. In *International conference on machine learning*, pp. 1225–1234. PMLR, 2016.

### Strengths
This paper considers an important problem of trying to quantify the generalization properties of personalized FL. An important by-product of such an analysis is quantifying the optimal number of communication rounds that minimizes the overall error (= optimization error + generalization error); papers on convergence guarantees do not consider the generalization error.

### Weaknesses
**Technical issues:**

**1.** In Remark 4/Corollary 1 and Remark 8/Corollary 2, where the authors are deriving the "optimal" number of communication rounds $T^{*}$, how do the authors know that the derived generalization bounds are order-optimal w.r.t. $T$, $K$ and other important quantities. If the tightness of the derived generalization bounds is not shown, then it is unfair to call it "optimal" number of communication rounds. Moreover, in Corollary 1 and 2, the dependence on other problem-specific parameters (such as smoothness constants, stochastic gradient variance, etc.) shouldn't be ignored if they are being used to derive the "optimal" number of communication rounds.

**2.** Can the authors please summarize the technical challenges compared to the seminal analysis in Hardt et al., (2016) for SGD? Is there any particular challenge due to local updates in the clients? 

**3.** Overall I'm not too impressed/surprised by the derived results -- a more satisfactory result for me would have been something that shows the generalization benefits of personalization compared to *no* personalization. 

**Presentation issues:** 

**1.** The presentation of Theorem 1 and Theorem 2 is rather poor and complicated. What is the meaning of "*They decay per iteration $\tau = t K + k$,...*"? And the equations below have $\tau_0$ instead of $\tau$. I'd have directly presented eq. (8) and (10) with the optimal value of $\tau_0$ rather than presenting the intermediate results (eq. (7) and (9)). And what is $\kappa_\lambda$ in the context of D-PFL? Also, it is very hard to parse Table 1.

**2.** Definition 2 is not clear to me -- what is the index $j$ (subscript of $z$)? In eq. (4), a bracket is missing at the end in $F(\mathcal{A}(S)$ and $f(\mathcal{A}(S)$. In Assumption 2, what is $F_i$? Only $f_i$ was introduced earlier. 

**3.** Paper writing needs to be improved. For instance, I'd suggest using "algorithm-dependent" instead of "algorithm-matter". Also, it should be "influential" in Remarks 4, 5 and 8.

### Questions
Please address the questions in Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper establishes a generalization stability analysis for a widely-used personalized algorithm, partial federated learning (PFL), in both centralized and decentralized federated learning (FL) settings. The authors also discuss the relationship between the derived stability results and previously established generalization stability upper bounds, and provide insights into  how these findings can inform and guide the training process.

### Strengths
The paper presents a well-organized structure and provides a clear comparison between its results and prior findings. Additionally, it offers an in-depth discussion on the impact of hyperparameters on generalization performance.

### Weaknesses
1. Inconsistent Notation: The notation used throughout the paper lacks alignment, which hinders readability. For instance, in Algorithm 2, the aggregation step update is defined as $u^{t+1}=\frac{1}{n}\sum u_i^{t+1}$, but in line 866, the update formula appears as ${\frac{1}{n}}\sum_{i\in \mathcal{N}}u_{i, K_u}^t$. It is unclear what $\mathcal{N}$  represents in this context. Additionally, in line 812, the notation $I$ is introduced without definition. This inconsistency in notation complicates understanding and interpretation.
2. Unclear Experimental Validation of the Proposed Theorem: It is difficult to discern how the experimental results support the theoretical findings. The authors establish generalization stability, yet in the experiments, they only measure the gap between training accuracy and test accuracy. There is no clear implementation of perturbations as discussed in the theoretical framework, making it unclear how the experiments substantiate the proposed stability theorem.

### Questions
1. In line 803, could you clarify how the inequality is derived? Specifically, how is $\Vert f(w;z) - f(\tilde{w};z)\Vert^2$ bounded given that $U=sup_{w, z}f(w;z)$.
2. In line 806, it appears there should be an inequality rather than an equality, since $\Vert a + b \Vert \leq \Vert a \Vert + \Vert b\Vert$.
3. The notation $I$ requires further explanation, as it is unclear how to derive the bound for $P(\{\xi^c\})$;
4. Since the authors discuss generalization stability, I recommend comparing the results with similar studies focused on generalization stability rather than generalization bounds as shown in Table 1.

### Soundness
3

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
4

### Summary
The paper addresses an important theoretical gap in Personalized Federated Learning (PFL) by focusing on generalization performance beyond convex conditions, specifically analyzing non-convex settings. The authors introduce a generalization analysis that incorporates algorithm-dependent factors through uniform stability. The paper investigates the effect of hyperparameters, learning rates, and communication modes (Centralized vs. Decentralized PFL) on generalization performance. Additionally, they provide excess risk bounds and propose early stopping criteria for optimal risk in PFL, supported by experiments on the CIFAR dataset.

### Strengths
The major contribution of this paper is from the theoretical aspect in generalization.

1. Generalization in (personalized) federated learning is critically important yet understudied, largely due to its complexity compared to the extensive body of work on convergence analysis in FL.

2. This paper offers a rigorous analysis, with well-rounded discussions and comparisons that cover various specific cases.

2. By focusing on the “algorithm-matter” generalization through uniform stability, the authors provide a practical framework that incorporates the effects of stepsize, learning steps, and communication structure (C-PFL vs. D-PFL). This analysis fills a significant gap in the field by moving beyond static theoretical assumptions.

3. The detailed examination of hyperparameters like learning steps and stepsizes, along with communication modes, is valuable for both theoretical insights and practical implications. The finding that C-PFL generalizes better than D-PFL is intriguing and has practical relevance.

### Weaknesses
I don’t see any major weaknesses in the paper. However, I suggest: 1) incorporating additional datasets and models in the experiments to strengthen the findings; and 2) clarifying the notation throughout, e.g., 'U' in the theorem.

### Questions
see the weakness part.

### Soundness
4

### Presentation
3

### Contribution
3
