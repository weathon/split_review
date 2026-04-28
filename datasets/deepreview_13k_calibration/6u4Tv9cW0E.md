# Balancing Domain-Invariant and Domain-Specific Knowledge for Domain Generalization with Online Knowledge Distillation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
Deep learning models often experience performance degradation when the distribution of testing data differs from that of training data.
Domain generalization addresses this problem by leveraging knowledge from multiple source domains to enhance model generalizability.
Recent studies have shown that distilling knowledge from large pretrained models effectively improves a model's ability to generalize to unseen domains. However, current knowledge distillation-based domain generalization approaches overlook the importance of domain-specific knowledge and rely on a two-stage training process, which limits the effectiveness of knowledge transfer. To overcome these limitations, we propose the Balanced Online knowLedge Distillation (BOLD) framework for domain generalization. BOLD employs a multi-domain expert teacher model, with each expert specializing in specific source domains to preserve domain-specific knowledge. This approach enables the student to distil both domain-invariant and domain-specific knowledge from the teacher. Additionally, BOLD adopts an online knowledge distillation strategy where the teacher and students learn simultaneously, allowing the teacher to adapt based on the student's feedback, thereby enhancing knowledge transfer and improving the student's generalizability. Extensive experiments conducted with state-of-the-art baselines on seven domain generalization benchmarks demonstrate the effectiveness of the BOLD framework. We also provide a theoretical analysis that underscores the effectiveness of domain-specific knowledge and the online knowledge distillation strategy in domain generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present an approach called Balanced Online Knowledge Distillation (BOLD) for domain generalization. BOLD uses a multi-domain expert teacher model to retain domain-specific knowledge and employs an online distillation strategy, allowing the teacher and student models to learn simultaneously. This setup enhances knowledge transfer and improves the model’s ability to generalize across unseen domains. Extensive experiments on seven benchmarks demonstrate the effectiveness of BOLD over state-of-the-art methods.

### Strengths
1. The clarity of the paper is commendable, and the Balanced Online Knowledge Distillation (BOLD) framework demonstrates effectiveness across seven benchmarks.
 
2. The authors provide both theoretical and empirical evidence to support the effectiveness of this method.

### Weaknesses
1. The theoretical analysis in this paper lacks rigor in establishing a strict upper bound for convergence and relies heavily on assumptions without concrete mathematical proofs. Specifically:
- Absence of Formal Proof for Upper Bound: The derivations, such as in Equations (11) and (13), introduce error terms  ϵ and ϵo ​but lack rigorous proof that these terms converge in the desired manner, resulting in an incomplete justification for the generalization bound. The analysis does not provide a clear mathematical argument showing that these error terms diminish to zero or a sufficiently small value as the training progresses. Furthermore, the relationship between these error terms and the overall generalization error is not explicitly defined with a convergence rate.
- Reliance on Assumptions: The analysis assumes that incorporating domain-specific knowledge and applying online distillation will reduce domain discrepancy and empirical risk, yet these effects are only qualitatively described without mathematical substantiation or a precise convergence rate. The paper does not offer a formal definition of 'domain discrepancy' or how the proposed method explicitly minimizes it. The assumption that online distillation inherently leads to better generalization is not rigorously proven, and the analysis lacks a clear connection between the distillation process and the reduction of empirical risk. There is no mathematical demonstration that the distillation process will lead to a tighter bound on the generalization error.
2.  The Balanced Online Knowledge Distillation (BOLD) framework is underexplored, as it does not account for the imbalanced dataset distribution across different domains. This limitation raises concerns about the assumption that all experts are well-pretrained. The paper assumes that each domain expert is equally capable and well-trained, which might not be true in real-world scenarios where domain datasets can vary significantly in size and quality. The framework does not address how to handle situations where some domain experts are poorly trained due to limited data or noisy labels, potentially leading to biased knowledge transfer.

### Questions
1. Can you provide a more rigorous theoretical analysis or formal proof for the convergence of the error terms introduced in Equations (11) and (13)?

2. How does the BOLD framework handle imbalanced dataset distributions across different domains?

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
4

### Summary
This paper proposes a novel framework, termed Balanced Online Knowledge Distillation, for addressing the challenge of domain generalization. The paper initially underscores the critical role of domain-specific knowledge within the domain generalization task. Subsequently, it advocates for the integration of both domain-invariant and domain-specific knowledge through an online distillation strategy. Additionally, the paper endeavors to undertake a theoretical analysis to substantiate the efficacy of domain-specific knowledge in scenarios where the target domain exhibits resemblances to the source domain, while also elucidating the advantages of the online distillation strategy in enhancing generalization performance.

### Strengths
1.The paper proposes the Balanced Online Knowledge Distillation framework, which combines domain-invariant and domain-specific knowledge and employs the strategy of online knowledge distillation, which is a novel attempt. 
2.The paper attempts to provide a theoretical analysis of the effectiveness of domain-specific knowledge in cases where the target domain has similar properties to the source domain, and how online knowledge distillation strategies can reduce the domain generalization error boundaries.
3.The English writing and essay organizations are good.

### Weaknesses
1.I would like to get more explanatory notes about the domain loss . From my perspective, the idea involves leveraging the text embedding of domain i as the positive sample of the Specific Embedding of domain i, while employing the text embedding of the domain other than i as the negative sample of the Specific Embedding of domain i. Given this interpretation, it may be more coherent to redefine the loss function.
2.When computing the Kullback-Leibler (KL) divergence loss, it is imperative to establish a clear delineation regarding which distribution is employed to guide the other. In this context, Equation (4) suggests that  signifies the utilization of the domain expert adapter to guide the student model. However, in Equation (6), the intended implication is for the student model to guide the domain expert adapter, a distinction not currently reflected in the discourse. Furthermore, the corresponding definition of  in Equation (5) remains unspecified.
3.Within the part labeled "Effectiveness of Domain-Specific Knowledge for Domain Generalization" in the Theoretical Discussion section, the current exposition primarily underscores the significance of shared attributes between the source and target domains. This emphasis appears somewhat detached from the core concept of "domain-specific knowledge."
4.Equation (7) does not seem to lead to the derivation of equation (11) within the specified conditions delineated in equation (10).
5.Does the student model learning from both Invariant Embedding and Specific Embedding create a conflict of knowledge?
6.While the results are advanced on multiple datasets, the performance on the Terra Incognita and Digits datasets is too poor.
7.Domain expert adapters should be a key module, but the corresponding details are missing from both the figure and the text.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper propose the Balanced Online knowLedge Distillation (BOLD) framework for domain generalization, which employs a multi-domain expert teacher model, with each expert specializing in specific source domains to preserve domain-specific knowledge. This is the first investigation into the effectiveness of online knowledge distillation for domain generalization. The study also demonstrates that distilling both domain-invariant and domain-specific knowledge, rather than only domain-invariant knowledge, enhances model generalizability. Extensive experiments across seven domain generalization benchmarks validate the effectiveness of the proposed BOLD framework compared to state-of-the-art methods.

### Strengths
1. The writing of this work is good, and the explanation of the method is clear and easy to understand.
2. The authors provided theoretical analysis to support the proposed method.

### Weaknesses
1. The novelty is limited. In fact, learning both domain-invariant and domain-specific features is a common approach in domain generalization, with a lot of theoretical and experimental research already existing on it (e.g. Bui, Manh-Ha, et al. "Exploiting domain-specific features to enhance domain generalization." Advances in Neural Information Processing Systems 34 (2021)). The main difference between the author's work and previous research lies in the integration of this idea with knowledge distillation and different loss function design.

2. The authors claim that their method distills both domain-invariant and domain-specific knowledge. However, the mechanism by which the proposed method explicitly disentangles and distills these two types of knowledge is not entirely clear. The loss functions used seem to encourage the student model to mimic the teacher's output, but it's not obvious how this process leads to separate representations of domain-invariant and domain-specific information. A more detailed explanation of this disentanglement process is needed.

3. The experimental results, while showing improvements over baselines, do not provide a thorough ablation study to justify the design choices. For example, the contribution of each loss term in the overall objective function is not analyzed. It is unclear whether all components of the proposed loss function are necessary or if a simpler approach could achieve comparable performance. Furthermore, the choice of using a multi-domain expert teacher model is not sufficiently justified. It would be beneficial to compare the performance of the proposed method with a single teacher model trained on all source domains.

### Questions
1. As described by the authors, the results in Table 1 are based on leave-one-out evaluation strategy, with distillation from ViT-B/32 to ResNet-50. However, the evaluation results on some datasets are lower than those reported in the paper "In Search of Lost Domain Generalization"(e.g. ERM on PACS, 80.8 vs 83.3; ERM on VLCS, 75.5 vs 76.8), which also uses leave-one-out evaluation strategy and ResNet-50. The authors should explain these discrepancies and differences in experimental setup or implementation that might account for them.

### Soundness
3

### Presentation
4

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
Current knowledge distillation-based domain generalization approaches overlook the importance of domain-specific knowledge and rely on a two-stage training process, which limits the effectiveness of knowledge transfer. To overcome these limitations, this paper proposes the Balanced Online knowLedge Distillation (BOLD) framework for domain generalization, exploring the domain invariant for effective knowledge transfer while domain-specific knowledge is reserved. Experiments demonstrates its effectiveness.

### Strengths
1. The codes are provided, which makes it easy to reproduce performance.

2. The question raised is meaningful. How to retain domain-specific information is a point worth exploring in the field of knowledge transfer.

3. Theoretical proof is provided, and the effectiveness of the method is analyzed theoretically.

### Weaknesses
1. There is some deficiency in related works. The exploration of domain-specific has been reflected in some domain adaptation/domain generalization literatures in the past, and it needs to be reflected in related works. e.g., [1][2][3].

2. The variant of ablation study was a little too simple, and we expected to see the effect of domain-invariant and domain-specific knowledge separately and the corresponding analysis.

3. The student embedding is constrained by both the invariant distillation loss and the specific distillation loss. These two constraints aim to find cross-domain common information and domain-specific knowledge, respectively, which are potentially contradictory (orthogonal). Therefore, why can these two contradictory losses directly affect the same embedding and still ensure effectiveness? Intuitively, it seems impossible for one embedding to both share information across domains and be unique to each domain. I hope the author can address this concern. This concern is not about the existence of two losses, but rather the fact that the same embedding is expected to satisfy two opposing constraints without a clear mechanism to ensure this.

### Questions
The student embedding is constrained by both the invariant distillation loss and the specific distillation loss. These two constraints aim to find cross-domain common information and domain-specific knowledge, respectively, which are potentially contradictory (orthogonal). Therefore, why can these two contradictory losses directly affect the same embedding and still ensure effectiveness? Intuitively, it seems impossible for one embedding to both share information across domains and be unique to each domain. I hope the author can address this concern.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present an approach to improve the generalizability of deep learning models across multiple domains. It introduces the Balanced Online Knowledge Distillation (BOLD) framework, which leverages CLIP-based model as the teacher model and extract its domain-specific and domain-invariant knowledge through an online distillation strategy. Extensive experiments on multiple benchmarks indicate the effectiveness of the proposed method.

### Strengths
1. The writting and the structure of the paper is clear. The idea of online knowledge distillation is interesting and seems to be effective.
2. The authors provides theoretical analysis.
3. The experiments are thorough.

### Weaknesses
1. The proposed method is based on CLIP output adapters, which is an already well investigated topic in the previous works [1]. Even though the proposed online knowledge distillation ($L_{spc}$) seems to be novel, but it is only a tiny component of the proposed method. From this point of view, the contribution of this work to the community might be limited. The authors should further discuss this.
2. What is the intuition of using cross-entropy loss in the expert training? Why not just using the similarity-based metrics for text-image matching?
3. The implementation of the existing methods is unclear. For instance, for the baseline RISE, they claim to achieve around 90.2 with ResNet-50 backbone on PACS dataset. But in Table 1 their performance is only 86.6. The author should further clarify this. Besides, the authors mentioned that they used the setting "ViT-B/32 to ResNet50" for Table 1, while RISE used ResNet-50 as the backbone. The authors should describe more experimental details regarding this for a fair comparison.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
