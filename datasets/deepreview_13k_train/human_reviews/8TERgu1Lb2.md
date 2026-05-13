# Federated Domain Generalization with Data-free On-server Gradient Matching

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Domain Generalization (DG) aims to learn from multiple known source domains a model that can generalize well to unknown target domains. One of the key approaches in DG is training an encoder which generates domain-invariant representations. However, this approach is not applicable in Federated Domain Generalization (FDG), where data from various domains are distributed across different clients. In this paper, we introduce a novel approach, dubbed Federated Learning via On-server Matching Gradient (FedOMG), which can efficiently leverage domain information from distributed domains. Specifically, we utilize the local gradients as information about the distributed models to find an invariant gradient direction across all domains through gradient inner product maximization. The advantages are two-fold: 1) we can aggregate the characteristics of distributed models on the centralized server without incurring any additional communication cost, and 2) our method is orthogonal to many existing DG methods, allowing for additional performance improvements by being seamlessly integrated with them. Extensive experimental evaluations on various settings to demonstrate the robustness of FedOMG compared to other FL/FDG baselines. Our method outperforms recent SOTA baselines on four FL benchmarks (MNIST, EMNIST, CIFAR-10, CIFAR-100), and three FDG benchmarks (PACS, VLCS, OfficeHome).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a gradient-matching strategy on the server for federated domain generalization (FDG) using a meta-learning approach.
This essentially boils down to a convex combination update rule instead of a simple average as in FedAvg.
In practice, the optimal combination of local updates is found by bounding the optimization near a simpler update rule like FedAvg update rule.
The paper provides some theoretic results and compares to some baseline methods in several datasets showing performance improvement empirically and that the method can be combined with other methods.

### Strengths
- Proposes an new aggregation method to improve federated domain generalization based on gradient matching. 

- Provides some theoretic analysis on the proposed method.

- The empirical results show a significant improvement over baselines used and demonstrate that FedOMG can be combined with other methods for a good performance boost (caveat with not comparing to a known Federated DG benchmark paper, see Weaknesses).

### Weaknesses
 - The paper does not compare to the federated domain generalization benchmark [Bai et al. 2024] that exactly fits this setting. This benchmark paper enables comparison of your method to multiple prior DG methods adapted from central methods and federated DG methods. In particular, Bai et al. [2024] noticed that simple federated averaging or convergence-specific FL methods could beat most prior Federated DG methods. Bai et al. [2024] also control for hyperparameter tuning costs. I would like to see this method applied within this framework to compare to the methods in that benchmark. This will place FedOMG on the same playing field as prior methods and would only require wrapping the method so that it is compatible with the framework. (Additionally, Bai et al. [2024] noticed that the PACS dataset is quite a bit different from other DG datasets so seeing on other datasets in the benchmark would be helpful.)

- The explanation of the method and the key insights are not written well. Several parts are simply incorrect though I can almost guess at what is meant. Others may be correct but are not explained well or justified appropriately. Please see questions below.

- Why do you formulate this as a bi-level optimization problem? Why is this necessary? It is important to lead the reader up to this point rather than just stating it. Furthermore, this is not even a bi-level problem in 3a and 3b. This is just 2 equations. Are you minimiizing 3a subject to 3b? If so, it's not even clear that 3b is minimization problem, it's just a constraint perhaps? This is incorrectly formalized.

- What is the intuition between the difference between yours and [Shi et al., 2022]? Is it something like the some of inner pairwise products is bounded by the sum of inner products between a mean vector and each vector? Does this have relationship to standard sum of squares ideas?

- How is the update rule for your method different than FedAvg? It seems like a different aggregation method but is difficult to understand how it is different than simple FedAvg. Could you provide an more explicit comparison and discussion on how it differs? When and why would the weights be different than FedAvg and when would the be equivalent?


- Other than computational, is there a reason to limit the search space to a convex combination of local gradients? This doesn't seem necessary.

- Why is a search space limitation needed? This is not well-motivated but just stated as fact. It seems that constraining to a convex combination + constraining to be near a simpler method like FedAvg strongly regularizes the method. But it is not clear why this is necessary or justified, perhaps other than an empirical argument.

- Eq 11 is not a multi-objective optimization problem as it is written. Essentially it has been reduced to a single objective via scalarization $\gamma$ parameter. Thus, it is not clear why multi-objective optimization is needed or required. 

- Eq 11 - Why is $\kappa$ needed? It seems that this term does not depend on $\Gamma$ and thus can be ignored.

- There is no lead up to Theorem 1 and this theorem is not well-explained. Why is this an easier problem? Why did you need to go through the min-max problem setup? This whole derivation seems very convoluted and does not lead logically to the next step. A major revision and explanation is needed.

- The theoretic analysis seems to use the same basic tools and techniques from prior works. Could you briefly explain the similarity of each main lemma, theorem or corollary w.r.t. its prior (probably non-FL) counterparts? Are there any new theoretic techniques used?

### Questions
- Why do you formulate this as a bi-level optimization problem? Why is this necessary? It is important to lead the reader up to this point rather than just stating it. Furthermore, this is not even a bi-level problem in 3a and 3b. This is just 2 equations. Are you minimiizing 3a subject to 3b? If so, it's not even clear that 3b is minimization problem, it's just a constraint perhaps? This is incorrectly formalized.

- What is the intuition between the difference between yours and [Shi et al., 2022]? Is it something like the some of inner pairwise products is bounded by the sum of inner products between a mean vector and each vector? Does this have relationship to standard sum of squares ideas?

- How is the update rule for your method different than FedAvg? It seems like a different aggregation method but is difficult to understand how it is different than simple FedAvg. Could you provide an more explicit comparison and discussion on how it differs? When and why would the weights be different than FedAvg and when would the be equivalent?




- Other than computational, is there a reason to limit the search space to a convex combination of local gradients? This doesn't seem necessary.

- Why is a search space limitation needed? This is not well-motivated but just stated as fact. It seems that constraining to a convex combination + constraining to be near a simpler method like FedAvg strongly regularizes the method. But it is not clear why this is necessary or justified, perhaps other than an empirical argument.

- Eq 11 is not a multi-objective optimization problem as it is written. Essentially it has been reduced to a single objective via scalarization $\gamma$ parameter. Thus, it is not clear why multi-objective optimization is needed or required. 

- Eq 11 - Why is $\kappa$ needed? It seems that this term does not depend on $\Gamma$ and thus can be ignored.

- There is no lead up to Theorem 1 and this theorem is not well-explained. Why is this an easier problem? Why did you need to go through the min-max problem setup? This whole derivation seems very convoluted and does not lead logically to the next step. A major revision and explanation is needed.

- The theoretic analysis seems to use the same basic tools and techniques from prior works. Could you briefly explain the similarity of each main lemma, theorem or corollary w.r.t. its prior (probably non-FL) counterparts? Are there any new theoretic techniques used?

*Summary of Review*
The basic idea of doing gradient matching on the server seems natural and the paper proposes one practical way to implement this. Furthermore, the empirical results are fairly strong either by itself or in combination with other methods. However, the method is not explained well and the theoretic analysis seems very similar to prior work (useful but not itself much of a contribution).  The lack of comparison to a Federated DG benchmark paper from last year's ICLR also calls the results into question.

### Soundness
2

### Presentation
2

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
This study introduces Federated Learning via On-server Matching Gradient (FedOMG) for Federated Domain Generalization (FDG). Unlike traditional methods, FedOMG leverages local gradients to identify an invariant gradient direction across domains, enabling efficient feature aggregation on a central server without extra communication costs. It is also compatible with existing FL/FDG methods for enhanced performance.

### Strengths
1.	This paper propose a method that is effective and highly compatible with existing FL algorithms and a large number of valid experiments have been conducted on the empirical side.
2.	Although I'm not an expert in this area (FL combined with DG), I think it's a very interesting work, benefiting from the theoretical explanation of how the authors derive the final method step by step, and the theoretical analysis seems solid enough.

### Weaknesses
1. What confuses me is the explanation of the motivation for this new approach (Section 3.2), and I would appreciate it if the authors could explain this part in more detail.
2. In lines 203-215, the authors seem to consider an alternative gradient for solving the $M$ -dimensional optimization, and I would like to know if this approach is a rough estimate, and if so, can you discuss the implications in detail 
3. a formulation “any FL algorithm” was used in line 267 - 269, I would have expected the authors to mention a great deal of relevant work here to demonstrate this overly certain claim

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces FedOMG to address the challenge of Federated Domain Generalization. The core idea behind FedOMG is to leverage local gradients from distributed models as domain-specific information. FedOMG maximizes the inner product of gradients to ensure that the model finds a gradient direction that is invariant across all domains. Extensive experiments conducted to evaluate the effectiness of the proposed model under federated setup.

### Strengths
Theoretical analysis propoded which seems to be true.

### Weaknesses
1. The approach to invariant gradient direction through convex optimization and Pareto optimality increases the computational complexity.

2. The method’s effectiveness relies on the assumption that domain gradients will align under the invariant gradient matching, which may not hold well in highly heterogeneous data settings.

3. The connection between the stated motivations (privacy, communication efficiency, and domain generalization) and the chosen methodology (on-server gradient matching and invariant gradient direction) is not clear.

### Questions
1. How does on-server gradient alignment directly contribute to reducing domain-specific biases without compromising the generalization capabilities of the global model?

2. Could you clarify how using gradients alone (instead of data) ensures privacy in FDG? Are there specific privacy-preserving guarantees that FedOMG provides through gradient-only use? What limitations, if any, exist in relying solely on gradient matching for privacy preservation, especially with highly heterogeneous client data?

3. What motivated the choice of complex optimization techniques like convex optimization and Pareto optimality in this context? How do these methods specifically enhance FedOMG’s performance over simpler approaches? Could simpler optimization approaches potentially achieve similar outcomes, or are the proposed techniques essential to achieving the method's goals?

4. Could you provide a more intuitive explanation of how gradient direction alignment helps achieve domain invariance across clients?

### Soundness
3

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
4

### Summary
This paper introduces FedOMG, a method that efficiently leverages domain information from distributed domains to prove the performance of the federated domain generalization (FDG) problem. The authors propose an approach that finds an invariant gradient direction across all domains through gradient inner product maximization to achieve this. The authors take the FDG problem as a multi-objective optimization problem and optimize it by finding the Pareto front. The extensive experiment results show the strengths and effectiveness of FedOMG, which is both superior in performance and computationally efficient.

### Strengths
- The idea is presented with solid theory, which is generally easy to follow.
-  Framing the FDG problem as a multi-objective optimization problem using gradient matching is interesting and intuitive. Also, it aligns with the nature of Federated learning with optimization goals.
- The results are strong across many datasets and baselines, and FedOMG is compatible with other related baselines. Many ablation studies are presented to show the effectiveness of the proposed method.

### Weaknesses
 - **The presentation of the Introduction and Related work**: The authors mention some previous work and I think it would be good to discuss their differences, limitations, and connections, compared with FedOMG. Also, in the introduction, the authors can discuss more on the novelty and design intuitions/details of FedOMG. Now it reads only mentioning gradient matching, which is too general from my perspective. Presentation-wise, this paper can be improved greatly in my opinion.

- **About theory**: In Objective 2, Theorem 2, and Corollary 3, some variables are not defined, such as µ, M, and δ. Also, it would be good if the authors could provide more explanations on how to derive Corollary 2.

- **Toy tasks**: The figure shows too many trajectories and is a little bit confusing. The authors can think of ways to present it conveying the conclusions clearer and more straightforward.

### Questions
- Could the authors provide more intuitions behind designing the search space (why search in a ball and use L2 norm)? Also, why are you using FedAvg for g_FL here? Would other federated aggregation rules for non-iid data work better here?
- Also, the authors use a convex combination of local gradients to find the invariant gradient direction. Could you also provide more explanations and intuitions for the design behind that?

### Soundness
3

### Presentation
2

### Contribution
3
