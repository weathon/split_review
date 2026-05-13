# A Versatile Influence Function for Data Attribution with Non-Decomposable Loss

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
\emph{Influence function}, a technique rooted in robust statistics, has been adapted in modern machine learning for a novel application: data attribution---quantifying how individual training data points affect a model's predictions. However, the common derivation of influence functions in the data attribution literature is limited to loss functions that can be decomposed into a sum of individual data point losses, with the most prominent examples known as M-estimators. This restricts the application of influence functions to more complex learning objectives, which we refer to as \emph{non-decomposable losses}, such as contrastive or ranking losses, where a unit loss term depends on multiple data points and cannot be decomposed further. In this work, we bridge this gap by revisiting the general formulation of influence function from robust statistics, which extends beyond M-estimators. Based on this formulation, we propose a novel method, the \emph{Versatile Influence Function} (VIF), that can be straightforwardly applied to machine learning models trained with any non-decomposable loss. In comparison to the classical approach in statistics, the proposed VIF is designed to fully leverage the power of auto-differentiation, hereby eliminating the need for case-specific derivations of each loss function. We demonstrate the effectiveness of VIF across three examples: Cox regression for survival analysis, node embedding for network analysis, and listwise learning-to-rank for information retrieval. In all cases, the influence estimated by VIF closely resembles the results obtained by brute-force leave-one-out retraining, while being up to \(10^3\) times faster to compute. We believe VIF represents a significant advancement in data attribution, enabling efficient influence-function-based attribution across a wide range of machine learning paradigms, with broad potential for practical use cases.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an influence function (IF) for loss functions beyond M-estimators. The proposed IF is derived from an approximation of a general IF formulation. Its simplified form enables better computational efficiency, as verified through experiments.

### Strengths
The proposed idea is well-motivated and the presentation is good overall.

### Weaknesses
1. Some of the notations are incorrect. $P$ and $Q$ are probability measures defined on the sample space. $\boldsymbol{1}$ is a vector of ones, but not a probability measure. In (8), (9), and some other places, they look like letting $P$ be  $\boldsymbol{1}$.

2. The finite difference approximate is confusing. Why the limit of $\varepsilon \to 0$ can be approximated by $\varepsilon=1$? What does finite difference mean here as $\varepsilon \in [0,1]$? What are the theoretical guarantees about this approximation? This approximation is crucial for Definition 2 and the advantage of VIF. It should be properly justified.

### Questions
See weakness 2

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a novel method for approximating the Leave One Out (LOO) data attribution scores. This is achieved by extending the influence-function-based attribution method into a more general class of loss functions. They highlight the fact that this formulation allows the computations to be approximated using finite differences, in turn allowing the influence function to be calculated using autodiff methods. Experiments are included to support the closeness of the approximations and to show the improvement in computational efficiency, when compared to the ordinary LOO computation.

### Strengths
1. The paper presents a novel formulation of a general class of losses (including non-decomposable losses, i.e., the losses which cannot be written as a sum of a function of each training example alone) which facilitates the application of an influence function for data attribution.
2. Provides analytical results justifying the accuracy of the finite difference approximation (VIF) of the influence function.
3. Experiments back-up the usefulness of VIF as a data attribution method, in terms of both accuracy and computational efficiency.
4. The presentation of the contents and the notation is generally well understandable.

### Weaknesses
1. I believe the selection of $\epsilon=1$ in the finite difference approximation of the IF is not sufficiently justified. Why not use any other $\epsilon$? Specifically, the paper lacks a clear explanation of how this choice impacts the accuracy of the approximation, especially when considering that the influence function is defined as a limit. The justification should include a discussion of the trade-offs between computational efficiency and approximation accuracy when selecting different values for $\epsilon$. Furthermore, the paper should explore how the choice of $\epsilon$ relates to the underlying data distribution and the specific loss function being used.
2. The VIF approximation is shown to be very close to the exact IF in two special cases. However the discussion on IF as an approximation for LOO (i.e., Eq. (7) being a good approximation of (3)) under the assumption of P and Q being uniform distributions over the corresponding samples with and without the object of interest is limited to M-estimators. Can anything be said on the Cox regression or any other model? The paper should provide a more comprehensive analysis of the approximation error for a broader class of models, including those with non-convex loss functions. The current analysis is insufficient to demonstrate the general applicability of the proposed method.
3. The paper will benefit from a limitations section which summarizes all the assumptions made along the way (e.g.: the convexity of the loss). This section should also discuss the potential impact of these assumptions on the performance and reliability of the proposed method. For example, it would be beneficial to discuss how violations of the convexity assumption might affect the accuracy of the VIF approximation and what steps could be taken to mitigate these effects.

### Questions
Please see weaknesses.
A suggestion: Complementing Fig. 1, a heat-map of “influence estimated by VIF” and another heat-map of “actual difference in the contrastive loss” for a given pair of nodes, plotted on the graph would be more visually expressive.

### Soundness
3

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
This paper provides one efficient influence function estimation procedure for non-decomposable loss beyond the M-estimator. The procedure is directly estimated from the definition of influence function under the first-order optimal condition and illustrates superior computational benefits against the brute-force while enjoying similar results.

### Strengths
-	The formulas of VIF proposed in such paper is general for handling non-decomposable loss. To the best of my knowledge, I do not see much discussion for computing data influence under such non-decomposable loss.

### Weaknesses
 - 	**Lack of empirical baselines**: Numerous data attribution methods exist beyond the brute-force LOO. Many of these are likely faster than the naïve brute-force and can provide insights into empirical performance are in attributing data importance, e.g., some retrained-based methods such as datamodels [Illyas et al. 2022] and Shapley-value based approaches are relevant alternatives. A more thorough empirical comparison would clarify how the proposed VIF method stands in relation to these approaches.
- 	**Insufficient theoretical discussions**: The paper would benefit from additional theoretical analysis regarding VIF convergence to true influence values, such as error bounds. Additionally, a comparison of VIF’s time complexity benefits—specifically, its matrix approximation efficiency relative to other methods and brute-force approaches—would strengthen the contribution. Given that VIF relies on approximations from influence functions, the authors should use terminology carefully in Sections 3.4 and 3.5, especially concerning terms like “empirically negligible” when attributing the target function and deriving formulas for Cox regression.
- 	**Missing (explicit) conditions**: The paper would be improved by an explicit discussion of VIF’s limitations with respect to deep models or a clearer indication of when VIFs are applicable. The derivations depend on the first-order optimality condition (Line 263), inheriting limitations from prior work [Koh and Liang 2017]. Given that deep models often do not satisfy this condition [Basu et al. 2021], it is unclear how the influence-based calculations are expected to perform in such settings.

### Questions
-	The authors need to be more rigorous for the difference in literature. I do not understand why the difference of denominator between IF (derived for Cox regression) and VIF in Line 380 – 386 can be ignored. A detailed comparison between these would be necessary Furthermore, a clear definitions of $\epsilon_{ij}$ means in this context would be helpful.
-	The authors can benefit from providing additional examples of non-decomposable losses to illustrate the advantages of expressing the influence function in the form of (10) – where the loss difference is first computed and then the gradient is taken, as opposed to directly using the inverse. Note that M-estimators should not be included here as one example, as they inherently have straightforward forms, as mentioned in Section 3.5.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper tries to generalize the influence function for cases where the used loss functions are non-decomposable, i.e., loss functions that can not be expressed as a sum of individual losses. To avoid deriving analytical formulas for calculating the limit in Eq. (7), the paper uses finite difference approximation method, which leads to their proposed versatile influence function (VIF).

### Strengths
The writing is clear, though there are some ambiguities in notation. I think tackling non-decomposable loss functions is a non-trivial generalization of the influence function.

### Weaknesses
Minor:
- In Lemma 1, strictly speaking,  Eq. (7) equivalently reduces to Eq. (3) as $\text{Eq. (7)} = n \times \text{Eq. (3)}$.

- The use of $\mathcal{L}(\theta, P) = \mathcal{L}(\theta, \mathbf{1})$, i.e., Eq. (8), is somewhat confusing. For example, according to Eq. (2), $\mathcal{L}(\theta, \mathbf{1}) = \sum_{i=1}^{n}\ell_i(\theta)$, but $\mathcal{L}(\theta, P) = \frac{1}{n} \sum_{i=1}^{n}\ell_i(\theta)$ in lines 664-666. Besides, while $\mathcal{L}(\theta, P)$ is understandable, the used instances, e.g., Eqs. (4) and (6), do not contain a data distribution $P$, and $\mathcal{L}(\theta, \mathbf{1})$ is more suitable. Therefore, I would suggest treating $P$ as an (unnormalized) weight vector instead of a data distribution for consistency in notation, and there might be better solutions.

Major:
- Lemma 2 lacks a proof, and I did not see why it holds. Substituting the defined $Q$ in what is in line 683 yields $\frac{1}{n-1}\sum_{1\leq j\leq n, j\not= i} \nabla_{\theta}\mathcal{L}(\hat{\theta}, z_j)$, whereas the result is $\nabla_{\theta}\mathcal{L}(\hat{\theta}, z_i)$ if we use $\delta_{z_i}$ instead.  This makes me feel $IF(\hat{\theta}(P); Q) \not= -IF(\hat{\theta}(P); \delta_{z_i})$, meaning that Lemma 2 is invalid.

- I feel the assumptions of strictly convexity and obtainable optimal solutions are too strong. Note that Bae et al. (2022) has addressed these two issues with the influence function, but their focus is on decomposable loss functions. With respect to non-decomposable loss functions, it would be beneficial for this work if these strong assumptions could be mitigated in some way.

- For the practical aspect, a potential drawback of the influence function (IF) is its need to calculate the inverse of Hessian matrices, which could be computationally expensive. It is clear that the proposed VIF also suffers from this issue which may limit its application to large scale settings. For decomposable loss functions, the corresponding Hassian matrices can be approximated by a sum of outer products, and then the calculation of inverse can be approximately simplified; see (Kwon et al., 2024). However, from my perspective, it is very likely that this technique is not applicable to non-decomposable losses. 

Overall, I assess this work in two aspects. First, for the derivation of the proposed VIF, it is a straightforward adaptation of IF that makes me feel the contribution in methodology is minimal — nothing surprising. In particular, the imposed strong assumptions obscure why VIF is good. Second, I did not find any noticeable contributions to its practical deployment; the paper does not dicuss what if $\theta$ is large, and the conducted experiments only invlove small-scale settings as mentioned in lines 398-406.

### Questions
Please refer to my comments on the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
