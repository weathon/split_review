# A Proxy Matrix-based Framework for Contextual Stochastic Optimization under Confounding Effect

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Data-driven decision-making in real-world scenarios often faces the challenge of endogeneity between decisions and outcomes, introducing confounding effects. While existing literature typically assumes unconfoundedness, this is often unrealistic. In practice, decision-making relies on high-dimensional, heterogeneous-type proxy features of confounders, leading to suboptimal decisions due to limited predictive power for uncertainty. We propose a novel semi-parametric decision framework to mitigate confounding effects.
Our approach combines exponential family matrix completion to infer the confounders matrix from proxy features, with non-parametric prescriptive methods for decision-making based on the estimated confounders. We derive a non-convergent regret bound for data-driven decisions under confounding effects and demonstrate how our framework improves this bound. Experiments on both synthetic and real datasets validate our method's efficacy in reducing confounding effects across various proxy dimensions.  We also show that our approach consistently outperforms benchmarks in practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a semi-parametric decision-making framework that combines exponential family matrix completion with weighted sample average approximation (wSAA) to estimate the confounders matrix from high-dimensional proxy features and use it for decision-making. The authors provide theoretical analysis and experimental results of the framework.

### Strengths
1. The paper is generally easy to follow. The technical results seem sound to me. 
2. The authors clearly state the limitations of previous results based on the non-confounding assumption and motivate the use of proxy matrix.
3. The authors also conduct experiments on real dataset.

### Weaknesses
While this paper proposes a framework for mitigating confounding effects in contextual optimization, I am uncertain about the overall significance of its contributions. Several aspects warrant further exploration:

- **Comparison with Existing Proxy Methods:** A substantial body of literature addresses confounding issues using proxies, notably through methods such as instrumental variables (IV) (Chen et al, 2016, Carrasco et al, 2007) and negative control proxies (Tchetgen et al, 2020). I believe a thorough comparison with the above-mentioned methods are necessary. Specifically, the paper should clarify how the proposed method handles the assumptions required by IV methods, such as the relevance and exclusion restriction, and how it compares to the assumptions needed for negative control methods, which often rely on the existence of a proxy that is independent of the outcome given the confounder. The paper should also discuss the identifiability conditions required for each method and how they relate to the proposed framework.

- **Choice of kNN and High-Dimensionality Concerns:** The framework’s reliance on k-nearest neighbors (kNN) raises concerns regarding its suitability for high-dimensional settings, as kNN gives a slow statistical rate $n^{-1/(2p + 2\hat r)}$. This is particularly relevant in high-dimensional contexts, where faster rates are often achievable through minimax estimators (Dikkala et al, 2020) and also in the context of contextual policy optimization (Chen et al, 2023). The paper needs to address the curse of dimensionality associated with kNN, where the distance metric becomes less meaningful and the number of neighbors needed to achieve a good estimate grows exponentially with the dimensionality. Moreover, the paper should discuss how the choice of $k$ affects the bias-variance tradeoff in this high-dimensional setting.

- **Technical Novelty:** The proposed framework seems to primarily combine matrix completion or factorization with a wSAA framework, both well-studied methods. The paper does not clearly highlight any novel technical advancements beyond this combination, making it difficult to identify the methodological contributions. The paper should explain how the proposed combination of matrix completion and wSAA is different from simply applying these methods sequentially. It should also discuss how the theoretical analysis takes into account the interaction between the matrix completion error and the wSAA error, and whether this interaction introduces any new challenges or insights.

- **Assumptions and Practical Limitations:** Also, I found some assumptions to be quite strong. For instance, Assumption 3 on the strong convexity of the log partition function, and Assumption 4 (iv) on the estimation accuracy of $\hat x$. To my understanding, there are cases where the underlying confounder $x$ is not identifiable. These assumptions may limit the general applicability of the framework and the authors do not make enough effort to justify these assumptions. The paper should provide more discussion on the implications of these assumptions and provide examples where they may fail. Specifically, the paper should discuss the practical implications of the strong convexity assumption and whether it is satisfied by commonly used distributions. Furthermore, the paper should discuss the sensitivity of the theoretical results to violations of these assumptions.

### Questions
I didn't find the reliable source of the real-world dataset, while the authors should provide more information about the dataset used for evaluating the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper addresses the challenge of quantifying the impact of confounding effects in real-world decision-making, where high-dimensional, heterogeneous proxy features of confounders are often used. To tackle this, the authors propose a novel semi-parametric decision framework that combines exponential family matrix completion to estimate a confounders matrix from these proxy features. This estimated matrix is then used to make more accurate and reliable decisions by accounting for confounding effects in the data.

### Strengths
1. This paper addresses a realistic and relevant problem for real-world applications: quantifying the impact of confounding effects.

2. The paper is well-written and grounded in theory, with proofs for all claims included in the appendix.

### Weaknesses
1. The experiment uses proxy features to estimate confounders, but proxy features are often high-dimensional and heterogeneous, which may not fully represent the true confounders. I am interested in how the ability of the proxy variables affects proposed methods. I assume  if the quality and representativeness of the proxy features are insufficient, it could introduce bias into the estimated confounders matrix. Specifically, the paper does not address the potential for the proxy features to be noisy or contain irrelevant information, which could lead to a poorly estimated confounder matrix and subsequently affect the decision-making process. The method's sensitivity to the quality and dimensionality of the proxy features needs further investigation. For example, if the proxy features are only weakly correlated with the true confounders, the estimated confounder matrix might be inaccurate, leading to suboptimal decisions. It is crucial to understand how the performance of the proposed method degrades with decreasing quality of proxy features.


2. The paper currently lacks a discussion on related work. In the field of causal effect estimation, there is extensive research on recovering confounders from proxy variables. I highly recommend including a literature review that addresses these studies. To further validate the proposed method, I suggest designing an experiment that compares the performance of two approaches: (1) representation learning directly from proxy variables, and (2) using estimated confounders matrices obtained from proxy variables. [1]

### Questions
See Above.

### Soundness
2

### Presentation
2

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
This paper studies the confounding effects and endogeneity in decision-making. Several stochastic regret bounds are derived to quantify the impact of confounding effects. Then a semi-parametric decision-making framework based on proxy matrices is proposed, aiming at addressing stochastic optimization problems under confounding effects. Experiments on real dataset shows the proposed framework can mitigate the repercussions arising from the unmet assumption of unconfoundedness.

### Strengths
1、The problem of confounding effects and endogeneity in making  decisions is important.

2、The proofs of the theorems of regret bounds are good.

3、Experiments show some effectiveness of the proposed decision-making framework on real dataset.

### Weaknesses
1、Proposed framework relies on too many theoretical assumptions. The regret bound may be highly sensitive to certain assumptions, where even slight deviations could lead to significant changes in outcomes. I thereby questioning the robustness of the theory.

2、In the decision-making framework, why can we assume the linearity between $X$ and $Z$? Under this assumption, when $n$ is high dimensional, how to handle with the overfitting problem?

3、The proposed algorithm is not clear. From the decision-making framework, I assumed the Weighted Sample Average Approximation is the product of $\mathbf{\hat{X}}$ and $\hat{V}$, then what will happen when the given $\mathbf{\hat{X}}$ and $\hat{V}$ differs with the actual $\mathbf{X}$ and $V$? More theoretical analysis about this is needed.

4、The experimental results are weak. Only one real dataset is used in experiments, limited data may not adequately test the robustness of the model under different conditions.

### Questions
Please response the questions in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper looks at the problem of policy learning/decision making under confounding, and in particular, when the some (potentially high dimensional) proxy ($Z$) instead of the confounding variables ($X$) are observed. Since the proxy might not capture the full information from the confounders, this can be considered as partial-information regime, and will have some excess regret when compared to the full-information regime. Under exponential assumptions on the data generating process of the proxy, one may infer the underlying $X$ from the $Z$. The authors builds on a weighted sample average approximation, and propose to use the recovered $X$ to learn the optimal decision. The paper provides non-convergent regret bounds under confounding effects and shows that the proposed method improves this bound.

### Strengths
I appreciate the explanations about each assumptions on how on whether they are standard/commonly used, the potential implications, and the role it plays in the proofs of the technical results. Moreover, the idea of framing the problem as matrix completion to recover confounding variables from observed proxies. The theoretically results also suggest the advantages of the proposed approach.

### Weaknesses
- The current discussion on the background (e.g. the detailed example on uncondoundedness, and discussion on the distinction between) might be too detailed for the main paper. It might be better to move parts of them to the appendix, and leave room for more discussion on the theoretical results of the proposed method.
- Some of the definitions can be presented in a more organized way. For instance, in assumption 4, $\mathbf{B}^*$ is referenced before defining might be better to include any definitions in the assumptions.
- I find section 3 to be a bit unclear. For instance, when learning the M-estimator, is $\hat{r}$ also a learned parameter or is it choosen? How does it relate to the rank of $V$? Since $\hat{r}$ also appears in the regret bound, it would be nice to include a discussion on $\hat{r}$ to understand how much of the excess regret is due to limitations of the estimation approach and how much is due to the intrinsic nature of the data generating process (e.g. low rank $V$).

### Questions
Throughout the paper, it was explained that if $Z$ captures all the information from $X$, is there a concrete/mathematical way quantify this from the data generating process? This might be helpful for decomposing the regret into irreducible parts (due to the data generating process) and what arises from suboptimality of the algorithm (if any).

### Soundness
3

### Presentation
2

### Contribution
3
