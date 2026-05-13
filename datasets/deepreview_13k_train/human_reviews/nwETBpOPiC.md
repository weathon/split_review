# Overcoming label shift in targeted federated learning

- Decision: Reject
- Scores: 3, 5, 3, 6, 3

## Abstract
Federated learning enables multiple actors to collaboratively train models without sharing private data. This unlocks the potential for scaling machine learning to diverse applications. Existing algorithms for this task are well-justified when clients and the intended target domain share the same distribution of features and labels, but this assumption is often violated in real-world scenarios. One common violation is label shift, where the label distributions differ across clients or between clients and the target domain, which can significantly degrade model performance. To address this problem, we propose \algname{}, a novel model aggregation scheme that adapts to label shifts by leveraging knowledge of the target label distribution at the central server. Our approach ensures unbiased updates under stochastic gradient descent, ensuring robust generalization across clients with diverse, label-shifted data. Extensive experiments on image classification demonstrate that \algname{} consistently outperforms standard baselines by aligning model aggregation with the target domain. Our findings reveal that conventional federated learning methods suffer severely in cases of extreme client sparsity, highlighting the critical need for target-aware aggregation. \algname{} offers a principled and practical solution to mitigate label distribution mismatch, ensuring models trained in federated settings can generalize effectively to label-shifted target domains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work addresses the realistic scenario of generating a global model for an arbitrary target distribution that may differ from the distribution of the aggregated client training datasets. To tackle this challenge, the authors assume that the central server has knowledge of the different label distributions of the clients and target domains, while this information remains unknown to the clients. They introduce FedPALS, a method that effectively balances the trade-off between bias (related to the target distribution relative to the aggregated training dataset) and variance stemming from the number of each client dataset.

### Strengths
This paper is the first to tackle the realistic federated learning scenario of generating a global model for an arbitrary target distribution that may differ from the aggregated client training datasets.

### Weaknesses
The presentation of this paper is notably poor, as it contains numerous inaccuracies and unclear statements throughout. For instance:

1. (L87-88 and L136)  "A common assumption in federated learning is that all client distributions are identical." 
-> This is not right. Federated learning generally allows for differences in client distributions, with data heterogeneity being one of the main challenges.

2. (L 97-98)-> the phrase "Given a set of clients S_1, ..., S_M" -> these are the set of client's marginal distribution.

3. (L98)There is a lack of clarity regarding the loss function; the specific loss being used is not mentioned.

4. (L108) "While the server has access to all marginal label distributions," reflects an assumption made in the paper. Given the emphasis on data privacy in federated learning, this assumption requires a much deeper justification. The authors only reference a single paper (Ramakrishna & Dan, 2022) in (L113-115) to support this assumption, which is insufficient. More extensive discussion is needed to validate this critical assumption.

5. (L161) The phrase "As we see in Table 1"  is unclear, as Table 1 appears several pages later. A more helpful reference would be "As we see in Table 1 in Section 5."

6. Proposition 1 discusses the importance of the aggregated training dataset's distribution being equal to that of the target dataset. However, establishing this equivalence alone does not address the challenges of federated learning. The issue of data heterogeneity among clients must be resolved when the aggregated training dataset's distribution matches the target dataset's distribution, particularly when local iterations are performed only once. In practice, due to communication issues, multiple local iterations are typically needed, and the implications of unbiasedness discussed in Proposition 1 are not sufficiently emphasized until lines 285-289.

7. (L 161) There is no definition provided for vector alpha and S  which creates confusion.

8. (L 300) The validation set's specific dataset type is not defined. If it is identical to the target dataset, this would constitute a dangerous approach that could be seen as cheating.

9. The inclusion of the hyperparameter lambda in (L 302) is a significant weakness, as it necessitates searching for optimal lambda values in arbitrary settings, which may vary across different settings.

10. The term "this benchmark" in (L 359) lacks clarity. It should specify what is being referred to. Additionally, the experimental setup appears weak, as modern federated learning research typically uses at least CIFAR-100, with ImageNet or Tiny ImageNet as benchmarks. This study seems to rely on a dataset with fewer than 10 classes, which lacks challenge. Moreover, with only 10 clients and an alpha value of 0.1 for data heterogeneity, it is unclear how performance will change as data heterogeneity increases.

11. In (L 444-445), the phrase "varying the number of clients C across 10 clients" is confusing, as C does not accurately convey the number of clients.

### Questions
I am curious about the performance comparison of the proposed method with baseline federated learning algorithms (such as SCAFFOLD) in scenarios where the label distribution of the aggregated training dataset matches that of the target domain.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studied a new FL problem under label shifts where the server knows the different label distributions of clients and target domains are known to the central server but unknown to the clients. To solve this problem, this paper optimized the aggregation weights using the label distributions. Experimental results demonstrated the effectiveness of the proposed methods over several baselines.

### Strengths
(S1) A novel FL problem with label shifts is formulated by assuming that the server knows the different label distributions of clients and target domains are known to the central server but unknown to the clients

(S2) A novel parameter aggregation strategy is proposed based on the label distributions. It also balances the effective sample size and the alignment with the target label distribution.

(S3) Experimental results on several data sets demonstrate the effectiveness of the proposed method.

### Weaknesses
 (1) The training procedures of the proposed FedPALS method based on equation (7) are confusing. The parameter $\lambda$ largely affects the model performance in the experiments. Though section 3.2 provides several options, it is unclear how $\lambda$ is selected in the experiments, e.g., Figure 3(a)(b).

(2) The assumption of this paper is strong. 
- It assumes that the target label distribution $T (Y )$ is known to the server, but no training examples are available for the target client. It would be better to provide more realistic FL scenarios to illustrate the importance of this special problem settings.
- It assumes that the server knows the different label distributions of clients. This can also result in the privacy concern.

(3) The prior information regarding $T (Y )$ is only available for the proposed FedPALS approach. It might be unfair for performance comparison between FedPALS and baselines.

(4) The proof of Proposition 2 is confusing. When $\mu = 2\sum_i \frac{\alpha_i^*}{n_i}$, how can it derive $\mu = \frac{2}{sum_i n_i}$ using the the primal feasibility condition?

(5) How is the parameter $\lambda$ selected in Figure 3(a)(b)?

(6) It seems that the approaches in Figure 3(b) do not converge yet after 80 communication rounds, as their target F1-scores keep increasing.

(7) The paper [c1] also studied the FL problem under unknown target client. It can assume no prior information regarding the target client. Thus, the developed AFL can be one of the strong baselines for FedPALS in the experiments.

### Questions
(1) The proof of Proposition 2 is confusing. When $\mu = 2\sum_i \frac{\alpha_i^*}{n_i}$, how can it derive $\mu = \frac{2}{sum_i n_i}$ using the the primal feasibility condition?

(2) How is the parameter $\lambda$ selected in Figure 3(a)(b)?

(3) It seems that the approaches in Figure 3(b) do not converge yet after 80 communication rounds, as their target F1-scores keep increasing.

(4) The paper [c1] also studied the FL problem under unknown target client. It can assume no prior information regarding the target client. Thus, the developed AFL can be one of the strong baselines for FedPALS in the experiments.

[c1] Mohri, Mehryar, Gary Sivek, and Ananda Theertha Suresh. "Agnostic federated learning." In International conference on machine learning, pp. 4615-4625. PMLR, 2019.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses label shift in federated learning, a challenge where label distributions vary across clients and differ from the target domain, potentially leading to degraded model performance. The authors propose FedPALS, a novel model aggregation approach that aligns client updates with the target label distribution, enabling better generalization under label shift. The method incorporates a weighting strategy that balances the need to match target distribution closely while minimizing variance in updates. Experimental results on datasets with label sparsity demonstrate FedPALS’s effectiveness over baseline federated learning methods, showing improved model accuracy in label-shifted target domains.

### Strengths
1. FedPALS introduces a well-justified aggregation technique that adjusts model updates for label shifts, making it highly applicable in non-i.i.d. data settings commonly found in real-world federated learning applications.

2. The paper includes extensive experiments on multiple datasets with varying degrees of label sparsity, demonstrating FedPALS’s superiority over standard methods like FedAvg, FedProx, and SCAFFOLD, thus validating its effectiveness in handling label shifts.

### Weaknesses
FedPALS lacks novelty, largely building on existing federated aggregation methods without introducing a fundamentally new approach. It uses outdated baselines; incorporating recent models (2023-2024) would provide better comparisons. The experiments with a limited number of clients (e.g., 3 for PACS, 10 for CIFAR-10) restrict evaluation of FedPALS’s scalability in larger federated settings. Additionally, its optimization for client aggregation weights could become computationally expensive with more clients or labels. The method focuses on label shift alone, though real-world federated learning often involves covariate shifts. Lastly, FedPALS relies on a critical hyperparameter, λ, without clear guidance on selection, which may limit practical deployment.

### Questions
1. The novelty of the proposed method (FedPALS) is not strongly highlighted, as it builds upon existing model aggregation schemes in federated learning without introducing a fundamentally new approach. Although it adapts the aggregation scheme to account for label shift, similar issues have been addressed with methods like FedAvg and FedProx, making it essential to clarify the unique contributions FedPALS offers beyond these.

2. The baseline used in this paper is too old. Please use some new baselines from 2023 or 2024 for comparison.

3. The experiments are conducted with a limited number of clients (e.g., 3 clients in PACS and 10 in CIFAR-10 and Fashion-MNIST), which is not representative of typical large-scale federated learning environments. This small client network size limits the evaluation of FedPALS's scalability and robustness, especially under diverse, high-client scenarios that federated learning is intended for.

4. FedPALS introduces an optimization process to determine client aggregation weights, which may become computationally expensive as the number of clients or labels increases. The paper does not address the potential scalability issues of this approach, raising concerns about its applicability in large federated learning settings with numerous heterogeneous clients or labels.

5. The method focuses on label shift, assuming that the input distributions remain consistent across clients and the target domain. However, in real-world federated learning, covariate shift often occurs alongside label shift. Expanding FedPALS to handle both types of shifts would enhance its comprehensiveness and applicability.

6. The method’s performance relies on a crucial hyperparameter, λ, which balances bias and variance in the model. The paper does not offer a clear, practical method for choosing λ, which may pose challenges for real-world deployment where fine-tuning may not be feasible. This lack of guidance could hinder the ease of implementation and generalization of FedPALS.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of label shift in federated learning, where client data distributions differ from a target domain with a known label distribution, but no target samples are available. The authors propose a novel aggregation scheme called FedPALS that optimizes a convex combination of client models to align with the target label distribution, ensuring that the aggregated model minimizes the target risk. The paper provides theoretical justification for the proposed method and demonstrates its effectiveness through extensive empirical evaluation, showing that it outperforms traditional approaches like FedAvg, FedProx, and SCAFFOLD in scenarios with significant distributional shifts.

### Strengths
- The proposed FedPALS method is novel and addresses a specific yet significant problem in federated learning, i.e., label shift. The approach of optimizing a convex combination of client models to align with the target label distribution is well-justified.
- The paper is technically sound, with theoretical analysis and extensive empirical evaluation. The experiments cover a variety of scenarios and datasets, demonstrating the robustness and effectiveness of the proposed method.
- The writing is clear and the presentation is well-organized.

### Weaknesses
 - The paper lacks a reference to the work "Agnostic Federated Learning" by Mohri et al., presented at ICML 2019. This work also addresses federated learning with unknown target distributions and shares some theoretical similarities with the proposed method in this paper. The authors should include this reference in the related work section and provide a more detailed comparison in both the theoretical and experimental sections to highlight the differences and similarities between the two approaches.
- The paper could be improved by providing a more detailed discussion on the limitations of the proposed method. For example, how does FedPALS perform in scenarios where the label shift assumption does not hold? Are there any cases where FedPALS might fail or underperform? It would be beneficial to explore the sensitivity of the method to deviations from the assumed label shift model, such as the presence of covariate shift not induced by label shift, or situations where the client label distributions are not well-represented in the target distribution.
- The paper discusses the choice of the hyperparameter $\lambda$ but could provide more guidance on how to select this parameter in practice. A more detailed analysis of the impact of $\lambda$ on the performance and robustness of the method would be valuable. The current discussion lacks concrete recommendations for choosing $\lambda$ based on the characteristics of the data or the specific federated learning scenario. For example, how should $\lambda$ be adjusted when the label shift is more or less pronounced?

### Questions
- Could the authors provide a more detailed comparison with existing methods, particularly those that address distributional shifts in federated learning? How does FedPALS differ from and improve upon these methods?
- Does the proposed method generalize to other types of distributional shifts, such as covariate shift? If so, could the authors provide some initial results or discussion on this topic?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces FedPALS, a method to deal with label shift in federated learning. Label shift happens when label distributions change across clients or between clients and target. The authors propose a novel aggregation scheme to optimize a convex combination of client models to ensure that the aggregated model is better suited for the label distribution of the target domain.

### Strengths
S1: The problem of label skews is interesting and well positioned.

S2: The paper gives good theoretical proofs on the algorithm.

### Weaknesses
W1: The compared baselines are too old. The authors only compare algorithms before 2020 (FedAvg, FedProx, SCAFFOLD). There are several recent works on label shifts in federated learning (e.g., [1, 2, 3]). Lack of these recent baselines cannot convince that the proposed algorithm is SOTA. The issue is not simply about recency, but about the relevance of the baselines. The cited works address label distribution skews, a core problem in federated learning, and should be considered as they tackle similar challenges, even if not exactly the same setting. The absence of comparison with these methods makes it difficult to assess the true advancement of the proposed approach.

W2: The authors work with C=2,3 and beta=0.1 partitions. How about C=1, the most extreme label shift? This is a critical point because C=1 represents a scenario where each client only has one class, which is a common and challenging situation in real-world federated learning. The performance of the proposed method in this extreme case is important to evaluate its robustness and applicability.

W3: Assumes target label distribution known is often not practical. No examples of how to get this info without privacy risk. The assumption that the target label distribution is known is a significant limitation. In many real-world scenarios, this information is not readily available, and obtaining it may introduce privacy concerns. The paper does not address how this information can be acquired without compromising user privacy, which is a crucial aspect of federated learning.

### Questions
See weaknesses. Given the very weak baselines, it is not convincing that the proposed solution is SOTA to reach the bar of acceptance.

### Soundness
2

### Presentation
2

### Contribution
2
