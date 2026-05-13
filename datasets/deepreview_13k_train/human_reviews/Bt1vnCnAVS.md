# Leave-One-Out Stable Conformal Prediction

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Conformal prediction (CP) is an important tool for distribution-free predictive uncertainty quantification.
Yet, a major challenge is to balance computational efficiency and prediction accuracy, particularly for multiple predictions.
We propose **L**eave-**O**ne-**O**ut **Stab**le **C**onformal **P**rediction (LOO-StabCP), a novel method to speed up full conformal using algorithmic stability without sample splitting.
By leveraging *leave-one-out* stability, our method is much faster in handling a large number of prediction requests compared to existing method RO-StabCP based on *replace-one* stability.
We derived stability bounds for several popular machine learning tools: regularized loss minimization (RLM) and stochastic gradient descent (SGD), as well as kernel method, neural networks and bagging.
Our method is theoretically justified and demonstrates superior numerical performance on synthetic and real-world data.
We applied our method to a screening problem, where its effective exploitation of training data led to improved test power compared to state-of-the-art method based on split conformal.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes Leave-One-Out Stable Conformal Prediction, a novel method to speed up full conformal using algorithmic stability without sample splitting.

### Strengths
This paper is clearly written and easy to follow.

### Weaknesses
 - Typos and minor issues
	- L103: notation [1:m] is not defined
	- L190: the objective function (is) often highly nonconvex

 - L33: Do we require $\mathcal{Y} \subseteq \mathbb{R}$? Do we require the marginal distribution $P_Y$ is continuous for the non-conformity scores to be uniformly distributed (L81)? The assumption of $\mathcal{Y} \subseteq \mathbb{R}$ is not explicitly stated, and it is unclear if the method would extend to multi-dimensional output spaces. The requirement of continuous $P_Y$ for uniform distribution of non-conformity scores is also not rigorously justified, and it is not clear how the method would behave if this assumption is violated.
- L34: Is D_test drawn from the same distribution $P_{X,Y}$ as D? Is it iid drawn? If yes, then is it equivalent to consider a single test example (e.g., Equation (1) only need to hold for one data point instead of for all $j \in [m]$)? If not, then why all non-conformity scores are exchangeable (L78)? The paper does not explicitly state whether the test data is drawn i.i.d. from the same distribution as the training data, which is a crucial assumption for the validity of conformal prediction. The implications of this assumption on the exchangeability of non-conformity scores also need further clarification.
- L81: Does this hold for any alpha in [0,1]? How do we obtained this from the fact that the rank is uniformly distributed over $\{1, \dots, n+1\}$? The paper does not provide a clear explanation of how the uniform distribution of ranks translates to coverage for any $\alpha \in [0,1]$. A more detailed explanation of this connection is needed.
- L81:` $\mathcal{Q}_{1-\alpha}$` is not defined. Is it lower quantile function `$\mathcal{Q}_{p}:= \inf \{x: F(x) \geq p\}$`?
- L86 (Equation 2)" Shouldn't $1-\alpha$ be slightly increased to $\frac{\lceil (1-\alpha)(n+1) \rceil}{n}$ for this to hold in finite sample? See Equation (19) of https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/conformal.pdf.

### Questions
- L33: Do we require $\mathcal{Y} \subseteq \mathbb{R}$? Do we require the marginal distribution $P_Y$ is continuous for the non-conformity scores to be uniformly distributed (L81)?
- L34: Is D_test drawn from the same distribution $P_{X,Y}$ as D? Is it iid drawn? If yes, then is it equivalent to consider a single test example (e.g., Equation (1) only need to hold for one data point instead of for all $j \in [m]$)? If not, then why all non-conformity scores are exchangeable (L78)?
- L81: Does this hold for any alpha in [0,1]? How do we obtained this from the fact that the rank is uniformly distributed over $\{1, \dots, n+1\}$? 
- L81:` $\mathcal{Q}_{1-\alpha}$` is not defined. Is it lower quantile function `$\mathcal{Q}_{p}:= \inf \{x: F(x) \geq p\}$`?
- L86 (Equation 2)" Shouldn't $1-\alpha$ be slightly increased to $\frac{\lceil (1-\alpha)(n+1) \rceil}{n}$ for this to hold in finite sample? See Equation (19) of https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/conformal.pdf.

### Soundness
3

### Presentation
3

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
The paper proposes Leave-One-Out Stable Conformal Prediction (LOO-StabCP) to speed up full conformal using algorithmic stability without sample splitting for better balance of computational efficiency and prediction accuracy. This method is much faster in handling a large number of prediction requests compared to existing method RO-StabCP based on replace-one stability. The authors show that their method is theoretically justified and demonstrates superior numerical performance on synthetic and real-world data.

### Strengths
* The paper proposes a novel method to address the problem in conformal prediction lies in balancing computation cost with prediction accuracy.
* Numerical results in this paper show that the proposed method achieves a competitive average coverage and a higher power compared to existing methods.

### Weaknesses
 * The authors introduce leave-one-out algorithmic stability for stability correction. However, it is difficult to calculate the stability bounds $\tau_{i,j}^{\mathrm{LOO}}$ when a complex deep learning algorithm is chosen to fit the model. Specifically, while the authors mention using the chain rule for neural networks, obtaining tight Lipschitz constants for each layer and their composition is non-trivial, especially with common non-linear activation functions. The practical approximation mentioned, based on interactions in feature space, lacks concrete details on how to implement this effectively and how to ensure the approximation is sufficiently accurate for reliable stability bounds.

* When trying to derive the LOO stability bound of RLM and SGD described in section 3.2, similar problems are encountered as mentioned above: the conditions in Theorems 2 & 3 are difficult to verify. For instance, the assumption of a bounded loss function and a bounded gradient for SGD is not always guaranteed in practice, and the theorems do not provide practical guidance on how to check these conditions for specific loss functions and datasets. The lack of clear guidance on how to verify these conditions makes the theoretical results less applicable.

* Numerical experiments are insufficient: the covariates of synthetic data are set to be independent; the prediction algorithms used are all robust linear regression. More complex settings and algorithms should be considered and compared. The use of only robust linear regression limits the generalizability of the results, and the independent covariate setting does not reflect real-world scenarios where correlations are common. The paper should include experiments with more complex models like kernel methods or tree-based methods and with correlated covariates to demonstrate the method's robustness.

### Questions
* I think it is necessary to discuss more and carefully about applying LOO-StabCP to deep learning algorithms for reasons outlined in the weaknesses box.

* As introduced in section 1, derandomization methods can address the issue of decreasing accuracy causing by randomly split but increase computational cost. I think it is better to demonstrate the performance of some derandomization method and compare it with LOO-StabCP to illustate the differences between the two in all aspects. 

* The authors compute stability-adjusted p-values for multiple selection in section 6. I think it is better to verify the validity of p-values in (7) and state it as a proposotion for completeness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Leave-One-Out Stable Conformal Prediction (LOO-StabCP), a novel conformal prediction approach that enhances computational efficiency for multiple predictions while ensuring coverage guarantees. LOO-StabCP builds on prior work by Ndiaye (2022), which utilized replace-one stability, by leveraging leave-one-out stability to require only a single model fit on the training data, regardless of the number of test points. This eliminates the need for computationally intensive refits for each individual test point. The authors validate LOO-StabCP with theoretical stability bounds for regularized loss minimization (RLM) and stochastic gradient descent (SGD)--methods widely used in modern machine learning. Extensive experiments on synthetic and real-world datasets show that LOO-StabCP matches or exceeds existing methods in predictive accuracy, efficiency, and computational speed.

### Strengths
The paper makes a contribution to conformal prediction by addressing a critical need for efficient uncertainty quantification in large-scale applications, especially when predictions are needed across multiple test points. Building on prior work that used algorithmic stability for conformal prediction, LOO-StabCP introduces a novel approach to leave-one-out stability by treating the model trained on the dataset (=training dataset $\mathcal{D}$) as one generated by “leaving out” each test point from an augmented set (as noted in Section 3.1 following Algorithm 1). This refinement results in a significant speedup, especially valuable in scenarios with numerous predictions.

The authors provide a solid theoretical foundation to support their proposed LOO-StabCP by deriving stability bounds for Regularized Loss Minimization (RLM) and Stochastic Gradient Descent (SGD), strengthening the method’s rigor. Additionally, empirical results on both synthetic and real-world datasets effectively demonstrate LOO-StabCP’s advantages in computational speed, prediction interval size and statistical power. The comparison of computational complexity across methods (e.g., FullCP, SplitCP, RO-StabCP), summarized in Table 1, clearly showcases the efficiency gains, and the illustration of practical applications in screening tasks, described in Section 6, highlights the method’s utility.

### Weaknesses
Overall, I believe this is a well-written paper.  However, some refinements in presentation could potentially enhance clarity and completeness, even though it is already quite solid.  Here are some specific suggestions.

**1. Adding Remarks & Prospects for Broader Examples/Applications:**
Adding comments on the tightness of stability bounds for the RLM and SGD examples in Section 3.2 would improve the interpretability of results, and clarify the sharpness or looseness of the current results. 
Additionally, while RLM and SGD are valuable examples, discussing potential extensions to other models or methods, along with conjectures or insights about the scope of the applications, would help readers better understand the broader applicability of the proposed approach. Furthermore, this is a minor point, but for improved parallelism between Sections 3.2.1 and 3.2.2, it may be worth noting that RLM and SGD are not strictly parallel choices: RLM represents a problem formulation, whereas SGD is an optimization algorithm used to solve such problems.

**2. Augmenting Experiments:**
As one way to o assess the tightness of the proposed LOO-StabCP prediction intervals, the authors could compare the intervals obtained by LOO-StabCP against the tightest possible prediction set with coverage $1-\alpha$ as a benchmark, which can be calculated in numerical experiments, for instance, using the $\alpha/2$- and $(1-\alpha/2)$-quantiles of instantiated predictions from multiple runs.  This comparison would provide further insights into the tightness of the proposed method (as well as other CP methods being considered in the study).
Also, broadening the simulation studies to include a wider range of model types would offer greater assurance that LOO-StabCP's performance gains are not specific to the tested settings. Expanding these results, perhaps in an Appendix, would help readers evaluate the method’s effectiveness across diverse applications.

**3. Ensuring Notation Consistency and Simplification:** 
Ensuring that all notation is defined before use (e.g., $[1:n]$) would improve accessibility. Simplifying notation where possible--for instance, by fixing  $j=1$ in Section 2  to reduce complexity without sacrificing rigor--could enhance readability. While the authors may have intended to highlight the dependence on the test point index $j$, simplifying this notation in Section 2 and then generalizing back in Section 3 could make the initial section more approachable.

### Questions
Here is a list of questions and minor suggestions.

- *Line 34:* I think $Y_{n+j}$ should not be included in $\mathcal{D}_{\textrm{test}}$.
- *Line 58:* Consider using “RO-StabCP” for clarity instead of “in Ndiaye (2022),” which is already referenced in the preceding paragraph.
- *Line 70:* The phrase “guess $Y_{n+j}$ with $y$” may not read clearly.
- *Line 75:* Specifying the range, e.g., by “…swapped for $i, i' \in [n] \cup \{n+j\}$” would be clearer.
- *Line 90:* Typo: $y$ should be replaced by $i$.
- *Line 103 (Definition 1):* (1) Define $[1:m]$ notation; (2) clarify the quantifier regarding $\mathcal{D}$.
- *Line 108:* “Recall” may be clearer than “Let.”
- *Line 140:* Consider adding remarks right after Definition 2 to discuss (1) the pursuit of adaptive parameters rather than uniform bounds to obtain sharper stability estimates, (2) the practicality of assuming known parameters, and (3) how these parameters impact the accuracy and robustness of prediction intervals. Although these points are addressed in later sections, readers would benefit from a brief mention here.
- *Line 154:* Using varied parenthesis sizes or brackets might improve readability.
- *Line 202:* Recall the meaning of the augmented data $\mathcal{D}^y_j$ from Line 70 for context.
- *Line 367:* The statement “This leads to wider prediction intervals for all methods, and particularly for SplitCP, more variability in prediction interval length” is not clear to me. It suggests the prediction interval of SplitCP becomes particularly wider due to the increase $m=1 \to m=100$.  However, SplitCP already appears to vary similarly at both $m=1$ and $m=100$, while the other methods vary more at $m=100$.
- *Line 369:* While the authors note that derandomization (Gasparin \& Ramdas, 2024) would incur extra computational costs, how does LOO-StabCP compare with derandomization in other aspects such as prediction accuracy, coverage, and stability?
- *Line 465:* The comment “Compared to cfBH, our method is more powerful” could benefit from further clarification. How is this conclusion drawn from Figure 3 and Table 3?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a leave-one-out algorithm stability definition, which the authors utilize to reduce the computational burden of the full conformal prediction method. The finite-sample validity of the prediction interval is proved. The authors have provided some experimental results to show the superiority of the proposed method in computation speed.

### Strengths
The proposed method does reduce the computational burden by circumventing model refitting when computing prediction intervals for distinct test points. The computational complexity is then reduced by $m$ times. This is also validated by the numerical experiments.

### Weaknesses
The method proposed by the authors is quite similar to the baseline established by Ndiaye (2022). Given this foundation, the extension presented by the authors appears somewhat straightforward, leading to a limited contribution. While the proposed method significantly reduces computational burden, it relies on the assumption that the learning algorithm adheres to the LOO stability assumption. Since conformal prediction is elegant for its wide applicability as a wrapper around any machine learning model, the examples RLM and SGD discussed in the paper are very limited. This limitation is particularly notable in the current landscape, where sophisticated deep learning models and LLMs are prevalent.

### Questions
1. The only issue I care about is whether commonly used lightweight machine learning algorithms like the random forest or simple neural networks can satisfy the LOO stability proposed in the paper. It will be a major issue and I will be willing to raise my score with extra theoretical results.

### Soundness
3

### Presentation
3

### Contribution
2
