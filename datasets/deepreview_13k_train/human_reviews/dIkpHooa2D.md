# MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Machine learning models are often required to perform well across several pre-defined settings, such as a set of user groups. Worst-case performance is a common metric to capture this requirement, and is the objective of group distributionally robust optimization (group DRO). Unfortunately, these methods struggle when the loss is non-convex in the parameters, or the model class is non-parametric. Here, we make a classical move to address this: we reparameterize group DRO from parameter space to function space, which results in a number of advantages. First, we show that group DRO over the space of bounded functions admits a minimax theorem. Second, for cross-entropy and mean squared error, we show that the minimax optimal mixture distribution is the solution of a simple convex optimization problem. Thus, provided one is working with a model class of universal function approximators, group DRO can be solved by a convex optimization problem followed by a classical risk minimization problem. We call our method MixMax. In our experiments, we found that MixMax matched or outperformed the standard group DRO baselines, and in particular, MixMax improved the performance of XGBoost over the only baseline, data balancing, for variations of the ACSIncome and CelebA annotations datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper provides a reparameterization of the group DRO objective from the parameter space to function space under the assumption that the hypothesis class for the predictor contains the set of the bayes optimal classifiers. Under this reparameterization, they introduce an algorithm to optimize this objective. Empirical results show the proposed algorithm outperforms groupDRO.

### Strengths
1)The problem is important and relevant to OOD generalization.

2)The proposed method is novel in its approach and theoretically justified.

3)Experimental results show that the proposed method outperforms groupDRO.

4)The paper is well written.

### Weaknesses
See questions.

### Questions
1)Under the assumption that the bayes optimal predictor is a subset of the set of hypothesis, wouldn't the same f minimize the objective for any dp in the set P? If this is the case, this weakens the theoretical contribution.

### Soundness
3

### Presentation
4

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
The paper formalizes the DRO problem in the case of bounded functions and shows that a solution is an optimal data mixture. In case of cross-entropy and L2 losses the problem can be further simplified to a single maximization of a concave function. An empirical version of the problem is further presented even in the case where the Bayes optimal functions are unknown. Several experiments on both synthetic and real data demonstrate that the empirical version of the MixMax improves over previous group DRO baselines in parametric cases as well as over non parametric data balancing algorithms.

### Strengths
- The major theoretical result that under certain conditions the DRO problem is equivalent to a single maximization over a concave objective function and that a solution can be achieved by fitting an optimal data mixture.

- The authors also provide a practical algorithm that computed the empirical MixMax solution.

### Weaknesses
 - $Emperical^2$ $MixMax$ relies on an accurate estimation of $\hat{f}_p(x)$, which in practice requires to optimally fit a model on every distribution, including performing a HP search by cross validation. This might be computationally prohibitive in some practical cases. Could you discuss computational trade-offs or potential approximations that could be used in resource-constrained settings? How those approximations would impact the  $Emperical^2$ $MixMax$ estimate?

- In some of the experiments where a Mixmax method was compared to an alternative method, the MixMax requires more compute which makes the comparison less fair. (e.g. experiment 6,3). It would be helpful to have experiments that control for computational budget across methods.

### Questions
- For the experiment described in 6.3, which strategy was used to upsample the minority class ? Was the training loss reweighed in order to de-bias the loss estimation ?

- Two different ways of using the MixMax weights were described, either retraining a model on the weighted dataset or reweighing models at inference time. Do you have a sense of how those 2 approaches compare in practice under different settings ?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper aims to provide a solution to the problem of group distributionally robust optimization (DRO). It considers the class of all bounded functions to address this issue. The group DRO problem is a specific case of the broader DRO problem, where the set of distributions is finite and consists of predefined distributions. 

The paper first demonstrates that group DRO over the space of bounded functions satisfies a minimax theorem. Additionally, it claims that when the loss function is either cross-entropy or mean squared error, the problem can be transformed into a convex optimization problem, which subsequently leads to a classical risk minimization problem.

### Strengths
The issue is both intriguing and significant in the literature.

### Weaknesses
The theoretical proofs are quite brief and unclear. It would be beneficial to discuss and clarify the proofs step by step.

The VC dimension of the class of bounded functions is indeed unbounded, which raises concerns about the practical applicability of the proposed method. Specifically, an unbounded VC dimension suggests that the empirical minimax solution may not converge uniformly to its expected value. This could lead to poor generalization performance in real-world scenarios. The paper's reliance on the assumption of a rich function class capable of approximating the Bayes optimal classifier is also a point of concern, as this may not be achievable in practice with a parameterized function class.

It is claimed that in Equation 1 the objective is concave with respect to $\lambda$. However, the convexity of $f_\lambda$ with respect to $\lambda$ is not clear. Although it is true that, if the class is rich enough, it can approximate the error of $p_\lambda(y|x)$, it is not exactly equal to this function. Furthermore, the concavity of the objective with respect to $\lambda$ is not directly demonstrated. The proof in Equation 3 shows concavity with respect to $p$, but not with respect to $\lambda$, which is a crucial distinction.

### Questions
1- I believe the VC dimension of the class of bounded functions is unbounded. Could this present a challenge for solving real-world problems?

2- It is claimed that in Equation 1 the objective is concave with respect to $\lambda$. However, the convexity of $f_\lambda$ with respect to $\lambda$ is not clear. Although it is true that, if the class is rich enough, it can approximate the error of $p_\lambda(y|x)$, it is not exactly equal to this function. 

3-To prove that the function $f_\lambda$ is concave with respect to $\lambda$, it must be shown that $f_{\alpha \lambda_1 + (1 - \alpha) \lambda_2} \geq \alpha f_{\lambda_1} + (1 - \alpha) f_{\lambda_2}$. However, in Equation 3, this is not demonstrated. Instead, concavity with respect to $p$ is proven in that equation.

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
The paper proposes a reparameterization technique for the group DRO problem to address the non-convexity of the parameters, under the most popular machine learning backgrounds. This reparameterization from parameter space to bounded function space admits a generalized minimax theorem. Moreover, the paper proves that group DRO can be decomposed into a convex optimization problem followed by a risk minimization problem for the frequently-used cross-entropy and mean squared error. Comprehensive experimental results align closely with the theoretical guarantee.

### Strengths
1. The idea of reparameterization seems novel in the context of group DRO.
2. The experiments are comprehensive in terms of the choice of datasets and the diverse ways of presentation.
3. The paper is written clearly, especially for the theoretical results.

### Weaknesses
There are multiple disadvantages, mainly regarding the methodology itself, together with its relevance to the existing literature on (empirical) group DRO.

1. The main contribution of this paper (Theorem 3.1) seems a direct generalization of Sion's minimax theorem by transforming the topology in the function space. While the authors introduce the weak*-topology, the core idea of applying a minimax theorem by carefully choosing the topology is not entirely novel. The novelty of the specific application to the group DRO problem should be more clearly emphasized.
2. The key discovery is that group DRO can be solved by fitting a specific mixture distribution. However, this seems like a straightforward idea in the optimization community (Nemirovski et al., 2009, Section 3.2) and recent works on group DRO [2,3] also use this property to reformulate the optimization problem. I understand that the second step in this paper, i.e., transforming the minimax object into a concave optimization problem of the distributional weights, is different from the ways in the papers I cited, but the first step (supported by the main theorem), has already been exploited in a similar way.
3. The reparameterization enables line 2 of Algorithm 1, which allows the possibility of iterative training and the whole MixMax schema. However, I am a little skeptical about parameterizing $f_\lambda(\cdot)$ in this form. It seems that MixMax exerts a constraint on the function class in the group DRO objective, which is not satisfactory. What happens if $f_\lambda(\cdot)$ can not be expressed via the closed form shown in the paper? This limitation on the function class needs to be more clearly discussed, particularly regarding its impact on the generality of the approach.
4. As an optimization paper in ICLR, the authors should consider adding complexity analysis of the proposed algorithm, either the computation complexity of Empirical MixMax, or the sample complexity of Population MixMax. From my understanding, Algorithm 1 needs to compute the empirical risk among each data group per iteration. This seems too expensive for modern machine learning or large-scale optimization tasks. Although the experiments verify the effectiveness of MixMax over other group DRO approaches, theoretical justifications still need to be presented in an optimization paper. The lack of a clear complexity analysis is a significant weakness.
5. The original form of group DRO involves risk function in the form of expectation, which is intractable in reality. That's why stochastic approximation algorithms prevail. However, as it requires computing the risk function for each group in Algorithm 1, I was wondering if MixMax can be directly applied to group DRO (at population level). If not, then the main contribution of this paper should be the reparameterization of empirical group DRO, rather than group DRO. The distinction between population and empirical group DRO needs to be clarified, and the limitations of the proposed method for population-level problems should be addressed.
6. The baselines used in the experiments could be improved. The algorithm proposed by Sagawa et al. (2020) suffers from a suboptimal complexity, which may cause unfair comparisons in Figure 4. The authors could try adopting the near-optimal algorithms of Zhang et al. [2, Algorithm 1 and 2], whose complexity is $|P|$ times lower than that of Sagawa et al. (2020). The choice of baselines needs to be more carefully considered to ensure a fair comparison.
7. Both the algorithm and the experiments target empirical group DRO problems. However, only group DRO algorithms are compared. It would be more persuasive to compare with empirical group DRO algorithms [3] since the latter could use the problem structure to further improve the complexity.

### Questions
I would appreciate it if the authors were willing to answer some of the questions I raised in the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2
