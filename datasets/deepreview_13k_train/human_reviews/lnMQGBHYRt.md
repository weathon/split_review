# Scalable do-Shapley Explanations with Estimand-Agnostic Causal Inference

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Among explainability techniques, SHAP stands out as one of the most popular, but often overlooks the causal structure of the problem. While do-SHAP uses interventional causal queries, its reliance on estimands hinders scalability. To address this problem, we propose employing estimand-agnostic Causal Inference, which allows for the estimation of any identifiable query with a single model, making
do-SHAP feasible on arbitrarily complex graphs. We also develop a novel algorithm to significantly accelerate its computation at a negligible cost with a marked improvement in computational speed, as well as a method to explain inaccessible Data Generating Processes. We validate our approach on two real-world datasets, highlighting its potential in obtaining reliable explanations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes two key contributions: first, it introduces an estimand-agnostic approach based on SCMs to compute causal effects with a single model, and hence improving scalability. Second, it presents a Frontier-Reducibility Algorithm to enhance do-SHAP's efficiency. The authors validate their method through empirical tests to demonstrate the effectiveness of their approach in generating explanations for ML models.

### Strengths
The paper identifies and addresses the limitations of traditional SHAP, which do not adequately consider causal relationships in data. By focusing on causal structures, it enhances the reliability of model explanations.

### Weaknesses
1/ The paper is poorly written and may not meet the required standards. It fails to highlight its real-life applications. In particular, the introduction does not convince readers of the need to incorporate causal structure into Shapley.

2/ For the do-SV (defined in Eq. 3) to be identifiable, I believe that specific assumptions are needed. However, they are not clearly stated in the paper. Do we need standard assumptions such as SUTVA, consistency, etc? Is it assumed that the confounders are all observed? Specifically, if latent confounders exist that are common causes of both S and Y, how can the do-SV be calculated?

3/ Experiments focus on estimation error of do-SHAP and the speedup of FRA, but not on why the proposed method is better than SHAP. The experiments do not demonstrate the failure modes of non-causal SHAP when the underlying data generating process has a known causal structure.

4/ It would be valuable to compare the proposed method with existing explainable method such as:

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?" Explaining the predictions of any classifier. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems.

Fisher, P. (2018). "Permutation feature importance." In Machine Learning: A Probabilistic Perspective by Kevin P. Murphy.

Ribeiro, M. T., Singh, S., & Guestrin, C. (2018). Anchors: High-Precision Model-Agnostic Explanations. AAAI Conference on Artificial Intelligence.

Selvaraju, R. R., Cogswell, M., Das, A., et al. (2017). Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. International Conference on Computer Vision.

Although these methods do not consider causal structure, it is valuable to compare with them to showcase superiority of the proposed method in generating explanation.

5/ This is a minor comment: It is unnecessary to include so much bold text and highlighting in the paper.

Overall, I believe that the presentation of the paper needs to be improved, and more experimental evaluation is necessary.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes Frontier Reducibility Algorithm to make the computation of do-shapley values more efficient. Specifically, the authors propose to use estimand-agnostic approach for calculating each combinatorial terms in do-shapley and simplified the process based on graphical information, e.g., by omitting non-ancestors. The authors also empirically validates the proposed method by synthetic data.

### Strengths
1. The topic is interesting and important to many related fields.
2. The proposed Frontier Reducibility Algorithm seems to be more computationally efficient than baselines.

### Weaknesses
1. The presentation can be improved. The notation is not aligned, e.g., $\mathbf{V}$ refers to set of variables (line 117), while later $\mathcal{V}$ is used (line 125). It is unclear why these two different notations are used, and this inconsistency makes the paper harder to read. The authors should clarify the difference between these two sets, or use a consistent notation throughout the paper. The lack of consistent notation extends to other parts of the paper, which adds to the confusion.

2. I am not sure about whether the contribution is enough. The first claimed contribution is the use of estimand-agnostic approach, which is not novel (from Parafita&Vitria 2022). The second claimed contribution is the Frontier Reducibility Algorithm for calculation of do-shapley based on Thm 4.7, and yet it is related to Lutheretal. (2023). The authors claim that their method is different because it considers causal structure, but the novelty of this approach is not clearly demonstrated. The third claimed contribution is a novel explainability strategy with do-SVs, which also looks non-significant. The authors need to better articulate the novelty of their approach and how it differs from existing methods. Due to that I am not very familiar with this particular field I will defer to other reviewers regarding this point.

### Questions
Could you provide a more detailed description on the example in Figure1? specifically, in terms of why do-shapley would be better than e.g., marginal or conditional shapley? It would also help if the authors can use the example in Figure 1 to explain the method in Section 4.3.

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
4

### Summary
In this work, the authors present a method for efficient estimand-agnostic computation of causal do-SHAP values, i.e., explanations of models with causal interventions. To this end, the authors present the Frontier-Reducibility Algorithm (FRA), a novel algorithm to decide a cacheing scheme for causal models. FRA achieves this speedup by avoiding unnecessary re-computation of parts of the graph that are independent of the causal effects. Furthermore, explainability of inaccessible data generating processes is considered.

### Strengths
1. Overall, the mathematical presentation of the contributions is consistent and clear.

2. The FRA algorithm is shown to setup an efficient cache for speeding up the runtime of the causal do-SHAP explanation method (Fig. 4 c).

3. The FRA algorithm is shown to have a minor impact on overall computation times (Fig. 4 b).

4. The presented method is shown to be applied in cases where the data generating process is not available (although the causal structure is assumed to be known).

### Weaknesses
1. Although Figure 2 compares a range of models, only Deep Causal Graphs (DCG) are considered in the second experiment in Figure 4. As CNF performs better in Figure 2 (higher log-likelihood, lower estimation loss), even if DCG is supposedly faster (which is not shown in the experiments), it would be interesting to see if, e.g., FRA may enable the use of the more accurate but on its own slower model. The choice of DCG seems primarily driven by the presence of latent confounders, but this is not a factor in the experiment of Figure 4, which limits the generalizability of the results. Furthermore, the speed of DCG is not explicitly demonstrated, making it hard to assess the trade-off between accuracy and speed. It would be beneficial to see a direct comparison of estimation times for both DCG and CNF, especially when the choice of model is not critical for the experiment itself.

2. The abstract may misrepresent the contributions of the paper. First, it states that they "propose estimand-agnostic Causal Inference", which is (as outlined on page 2) prior work. Stating that estimand-agnostic method are employed in this paper would be more clear in this regard. Second, it states that the presented method is "making do-SHAP feasible on arbitrarily complex graphs". Although a significant speedup is shown (Fig. 4 c), the exponential growth in computation time persists. The claim of feasibility on arbitrarily complex graphs is misleading, as the method still suffers from the inherent exponential complexity of SHAP, even if the constant factor is reduced. The authors should clarify that they are making do-SHAP more practical, but not eliminating the fundamental scalability issues.

3. As stated in the abstract, part of the motivating hypothesis for this paper is that the "reliance on estimands hinders scalability" (abstract). But, a comparison with such methods is missing in the evaluation. The paper does not provide any empirical evidence to support the claim that estimand-based approaches are less scalable. A direct comparison, even if limited, would strengthen the argument. The absence of such a comparison leaves the reader to assume the scalability issues, rather than demonstrating them empirically. This weakens the motivation for the proposed method, as the claimed bottleneck is not explicitly shown to exist.

Minor:

1. The abbreviation DCG is only introduced in the appendix (page 24).

2. A confusing double negation in the footnote on page 9 ("nor have not").

### Questions
1. Why is FRA's execution time in Figure 4 (b) going down with a growing number of variables and only starting to grow once about 8 variables are involved?

2. In Figure 4 (c), three variants are compared (no cache, cache, and FRA cache). It did not become apparent to me how the non-FRA cache is setup (line 504 simply states "employ a cache").

### Soundness
2

### Presentation
3

### Contribution
2
