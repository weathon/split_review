# Seeking Global Flat Minima in Federated Domain Generalization via Constrained Adversarial Augmentation

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
Federated domain generalization (FedDG) aims at equipping the federally trained model with the domain generalization ability when the model meets new clients with domain shifts. Among factors that possibly indicate generalization, the loss landscape flatness of the trained model is an intuitive, viable, and widely studied one. However, pursuing the flatness of the global model in the FedDG setting is not trivial due to the restriction to preserve data privacy. To address this issue, we propose GFM, a novel algorithm designed to seek Global Flat Minima of the global model. Specifically, GFM leverages a global model-constrained adversarial data augmentation strategy, creating a surrogate for global data within each local client, which allows for split sharpness-aware minimization to approach global flat minima. GFM is compatible with federated learning without compromising data privacy restrictions, and theoretical analysis further supports its rationality by demonstrating that the objective of GFM serves as an upper bound on the robust risk of the global model on global data distribution. Extensive experiments on multiple FedDG benchmarks demonstrate that GFM consistently outperforms previous FedDG and federated learning approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors adapt the work that ties flat minima to domain generalization in the context of Federated Learning. They show that the prior work in the centralized case does not naturally extend to federated learning. They then move on to build an intuitive case for its extension and propose a new method that utilizes sharpness-aware minimization and data augmentation to simulate global data distribution during client optimization.

### Strengths
The paper is easy to read, and the authors explain the concepts in a linear fashion, making it intuitive to understand the decisions they make while formulating their proposed solution. The authors also clearly identify the shortcomings of existing works and the reasons why they would fail to extend to FL, thus proving the necessity of this work.

### Weaknesses
While the paper writing is good, the problem is relevant, and the proposed solution is headed in a promising direction, several weaknesses and gaps in the study need to be addressed. The main concerns are listed below:
1. The ablation study in Table 2 shows that the main benefits are achieved by using SAM and/or GCA. This conflicts the key contribution of this work, i.e., GFM. Particularly, the authors mention "combining them can complement each other’s strengths" in line 516, but looking at the table the same cannot be inferred. Specifically, the performance gains of GFM over FedAvg appear marginal in some cases, and it is not clear if these gains are statistically significant. The ablation study does not sufficiently isolate the impact of the proposed Global Flat Minima (GFM) approach from the effects of Sharpness-Aware Minimization (SAM) and Global Consistency Augmentation (GCA).
2. Also from table 2, it can be seen that FedAvg+GCA wins in two of the 4 cases bringing up the next question: What is the impact of data augmentation in general when compared to the adversarial data-augmentation that the author's propose. It is unclear whether the gains from GCA are due to the specific adversarial nature of the augmentation or simply due to the introduction of more diverse training samples. A comparison with standard data augmentation techniques would be beneficial to understand the unique contribution of the proposed augmentation strategy.
3. The study in section 5.4 is very thorough and quite informative. The main question that the paper does not address is two-fold 
	- the statement "aggregation helps generalization." in line 191 needs either proof or a citation from prior work that proves it. While there is a citation in the paper that advocates that generalization can be achieved via flatness, one cannot infer that flatness is the necessary condition for generalization"
	- secondly the authors need to prove that this statement is further not affected by the relaxation in assumption 1.
	- Overall, while it irrefutable that authors are able to generate improved performances, it is not convincing that the reason for improvements can be attributed totally to flatness of the minima of the global model. The paper lacks a clear theoretical justification for why seeking flat minima in the global model necessarily leads to better generalization in the federated learning setting, especially given the heterogeneity of client data.
4. Apart from comparing the methods based on performance that authors should also present the comparison in terms of computational and space complexity, e.g., plot comparing FLOPs vs performance or number of parameters shared vs performance, etc. The paper should include a detailed analysis of the computational overhead introduced by the proposed method, including the FLOPs required for the adversarial augmentation and the additional memory needed to store the augmentation model.

### Questions
1. Authors mention that GFM = FedAvg + SAM + GCA. However, FedSAM is FedAvg + SAM. Could the authors clarify their contribution with respect to FedSAM?
2. Currently the authors are working in the restrictive setting that each client has one domain each. How do they see their method adapting if each client has access to more than one but not all the domains?
3. Is it right to infer that Theorem 1 is a restatement and not an original contribution?
4. Could the authors mention some citations that use a similar assumption as "assuming aggregation helps generalization" on lines 191-192?
5. In Algorithm 1:
	- Can $c>e$? How do the authors choose the values of these hyperparameters? It is quite important to understand this especially since this is an adversarial optimization that is often unstable under the slightest change of hyperparameters.
	- How many models need to be maintained by a client to run this optimization?
	- Could the authors expand line 11 to include loop oversampling, gradient estimation, and update rule? Are the $\phi_i$s also aggregated?
6. Authors mention that the SAM optimizer uses $\gamma=0.02$. How do they arrive at this value? Could they talk about how to interpret this value or how it might impact the training?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a federated domain generalization method, GFM, which incorporates techniques from sharpness-aware learning. The authors aim to find a flat minimum by coordinating clients during federated training. In addition to sharpness-aware learning, a global model-constrained adversarial data augmentation strategy is employed to better regulate the sharpness of the converged models. The authors claim that existing methods overlook data privacy concerns, motivating the design of the GFM training algorithm. A series of experiments is conducted to verify its effectiveness.

### Strengths
1. The paper provides rigorous preliminaries and thorough theoretical support, with detailed proofs included in the appendix. 

2. A series of experiments are conducted here to verify the effectiveness of the proposed method.

3. The proposed method is tailored for domain generalization tasks in both its theoretical derivation and algorithm design.

### Weaknesses
1. The proposed method is very similar to the baseline, FedSAM; however, it has not been discussed in either the related works section or the introduction. In comparing the proposed method to FedSAM, I do not see a clear improvement or significant difference between them. The only notable difference appears to be the augmentation network discussed around Equation 9, which is directly adopted from Suzuki (2022). Additionally, the ablation study does not evaluate the performance impact of removing this augmentation network.

2. What is the primary motivation of this paper? In the introduction, the authors discuss issues related to finding flat minima and the neglect of data privacy. However, there does not appear to be any specific design or consideration aimed at enhancing privacy protection in this paper.

3. The organization of this paper could be improved. The related works and preliminaries sections span two pages, while the experimental section only covers three pages. The experimental section should be expanded with more detail in the main text.

4. It would be better to add hyperlinks to the citations for the methods listed in all the tables. Currently, all methods are cited only in Section 5.2, which makes it difficult to link each method to its corresponding paper.

5. The definition of flatness in Equation 3 is based on the assumption that $\theta$ is close to a local minimum, meaning the first-order gradient is near zero. There is no such assumption around equation 3.

### Questions
1. How is the loss landscape illustrated in Figure 2? What method is used to generate the loss landscape in this figure?

2. What would the performance be if FedSAM were combined with the augmentation network? Additionally, is there an ablation study on the augmentation network's impact within GFM?

3. Did the authors conduct experiments on CIFAR-10 or CIFAR-100, as some baselines reported results on these datasets?

4. The authors mentioned 'However, in federated learning, this becomes challenging due to the privacy concerns of the data.', which seems to be one of the motivations to derive the proposed GFM. What is the difference of the privacy protection between the GFM and FedSAM?

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
The paper proposes a method GFM that flattens the global model to a minimum in the case of federated learning. the paper proposes that the method of finding perspectives on global data is based on a solid theoretical foundation that improves the generalization of the distributional bias of a new client.

### Strengths
1. the paper's provides a sound and complete theoretical foundation for their method.
2. the paper provides sufficient experiments to show that their method is better and more suitable than FedSAM to be applied to the federated learning method of divisional offsets.
3. the paper provides sufficient literature, citations to illustrate the relevant issues.

### Weaknesses
Assumption 1 of the paper mentions that local models may outperform global models is COUNTER-INTUITIVE, and I think this hypothesis can be illustrative to a certain extent, but it does not cover so the federated learning situation. Because the local model is stronger than the global model in the federated learning chaotic situation is not a completely impossible situation.

### Questions
1. It is not particularly clear to me what is the difference between the paper's approach and the client-side optimization of local models using SAM-like methods?

2. As mentioned in the article, such methods require more power on the client side. The computational paper on how to reduce client-side computation doesn't go much further than that

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
5

### Summary
The paper addresses the challenge of federated domain generalization (FedDG), where a federated model must generalize effectively to new clients facing domain shifts. Authors introduce GFM, an algorithm designed to achieve global flat minima during the federated training of global model. GFM uses a globally-constrained adversarial data augmentation technique, which generates surrogate global data within each local client, improving the model’s flatness while preserving data privacy. Supported by theoretical analysis, this approach ensures that GFM effectively finds global flat minima. Extensive experiments further highlight GFM’s superior performance over previous FL and FedDG methods across multiple benchmarks.

### Strengths
1.	The exploration of the global loss landscape within FedDG research is novel, and the proposed approach of enhancing global flatness through data augmentation represents an innovative and promising direction.
2.	Theoretical analysis in this paper is rigorous, skillfully incorporating global flatness into local updates. This theoretical foundation effectively guides the algorithm design, resulting in a well-grounded and interpretable solution.
3.	Claims made in the methodology, including Assumption 1 and those related to model flatness, are well-validated and substantiated by experimental results.

### Weaknesses
1.	The min-max optimization process in the local updates remains somewhat unclear. Specifically, the paper does not provide sufficient detail on how the adversarial augmentation model $\phi_i$ is optimized and how this optimization interacts with the model parameter $\theta_i$. A more thorough explanation of the iterative process and the convergence properties of this min-max game would be beneficial.
2.	This paper lacks direct validation to demonstrate whether the augmented data provides a more effective surrogate for global data compared to local data. While the authors claim that the augmented data helps in finding global flat minima, there is no empirical evidence showing that the augmented data distribution is closer to the true global data distribution than the local data distribution. A quantitative comparison of these distributions would strengthen the findings.
3.	This paper does not include an analysis of hyperparameter selection, which is important for SAM-based approaches. The radius $\gamma$ in SAM is a critical parameter that can significantly impact the performance of the algorithm, and the paper does not provide any guidance on how to choose this parameter, nor does it explore its sensitivity.

### Questions
1.	Could the authors provide a more detailed analysis of the min-max process? For instance, analyzing the solutions of $\phi_i$ and $\theta_i$ would improve understanding of this component.
2.	Regarding point 2 in Weaknesses: Does the augmented data act as a better surrogate for global data than local data? A more direct evaluation would be helpful.
3.	A sensitivity analysis of key hyperparameters, such as the radius $\gamma$, would add valuable insight.
4.	The work by Sun et al. [1] also explores global flatness in heterogeneous FL using an ADMM algorithm to address constrained optimization. Including a citation of this work and a comparison would enhance the paper.

[1] Sun, Yan, et al. “Dynamic Regularized Sharpness Aware Minimization in Federated Learning: Approaching Global Consistency and Smooth Landscape.” International Conference on Machine Learning. PMLR, 2023.

### Soundness
3

### Presentation
4

### Contribution
3
