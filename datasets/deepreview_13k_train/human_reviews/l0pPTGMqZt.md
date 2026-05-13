# Domain Generalization for Domain-Linked Classes

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Domain generalization (DG) focuses on transferring domain-invariant knowledge from multiple source domains (available at train time) to an \emph{a priori} unseen target domain(s). This requires a class to be expressed in multiple domains for the learning algorithm to break the spurious correlations between domain and class. However, in the real-world, classes may often be \emph{domain-linked}, i.e. expressed only in a specific domain, which leads to extremely poor generalization performance for these classes. In this work, we aim to learn generalizable representations for these domain-linked classes by transferring domain-invariant knowledge from classes expressed in multiple source domains (\emph{domain-shared} classes). To this end, we introduce this task to the community and propose a \textbf{F}air and c\textbf{ON}trastive feature-space regularization algorithm for \textbf{D}omain-linked DG {\mymethod}. Rigorous and reproducible experiments with baselines across popular DG tasks demonstrate our method and its variants' ability to accomplish state-of-the-art DG results for domain-linked classes. We also provide practical insights on data conditions that increase domain-linked class generalizability to tackle real-world data scarcity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses a key challenge in Domain Generalization (DG): the difficulty in generalizing to unseen target domains when classes are unique to specific domains (domain-linked). The authors introduce the concept of domain-linked classes in DG and propose the FOND algorithm, which enhances generalization by leveraging knowledge from domain-shared classes. Through comprehensive experiments, they demonstrate that FOND achieves state-of-the-art results in DG tasks, particularly for domain-linked classes. The paper also offers theoretical and practical insights into managing domain-linked class generalizability in real-world scenarios.

### Strengths
Indeed, modeling that explicitly considers the relationship between domains and classes is not extensively developed in existing methodologies. In this regard, addressing this specific aspect presents a novel approach to problem-solving in the field. This innovative focus could provide significant advancements in understanding and tackling domain-specific challenges.

It's reasonable to assume that domain-linked classes might have limited data compared to domain-shared classes. If the information from the more abundant domain-shared class data can be effectively utilized for the learning of domain-linked classes, it could indeed be beneficial. This approach seems quite plausible and potentially impactful in addressing data scarcity challenges in specific domains.

### Weaknesses
The simplicity of the proposed methodology, which essentially relies on contrastive learning based on domain-shared classes and aligns the losses between domain-linked and domain-shared classes, does seem straightforward. While leveraging information from domain-shared classes to inform domain-linked classes could be beneficial, it's understandable to question whether such loss matching alone suffices to supply rich information. The contrastive loss, while effective for representation learning, may not fully capture the nuanced relationships between domain-linked and domain-shared classes, potentially leading to suboptimal generalization. The method's reliance on aligning loss magnitudes, without considering the underlying feature distributions, might result in a superficial alignment that doesn't truly transfer the complexities of domain-shared classes to domain-linked ones.

Furthermore, the connection between merely aligning loss magnitudes and achieving fairness metrics seems tenuous. A deeper, more nuanced approach might be necessary to ensure that the model not only aligns superficial loss values but also genuinely captures and transfers the underlying complexities and variances of the classes across different domains. The current approach lacks a mechanism to explicitly address potential biases that may exist within the domain-shared classes, which could inadvertently transfer to the domain-linked classes. Simply matching loss magnitudes does not guarantee that the model learns to disentangle domain-specific and class-specific features, which is crucial for robust generalization.

The term "domain-linked class," used to describe classes that correspond one-to-one with a specific domain, does not seem particularly intuitive. Just recommend utilizing an other word.

The assumption of awareness on domain-shared classes and domain-linked classes are also not realistic.

The likelihood of encountering domain-linked classes in real-world problems may not be immediately apparent or intuitive. Can you provide a clear, real-world example where such classes prominently emerge?

The result of Theorem 1 appears overly direct. Its derivation through the PAC-Bayes bound seems far too straightforward, making it questionable to regard this as a true theorem.

### Questions
Q1. Is it common in this field to define a dataset comprising both inputs and labels as a domain, as done in this paper?

Q2. (Same as weaknesses) The likelihood of encountering domain-linked classes in real-world problems may not be immediately apparent or intuitive. Can you provide a clear, real-world example where such classes prominently emerge?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel task of domain generalization and devises an algorithm aimed at acquiring generalizable representations for domain-linked classes by transferring valuable insights from domain-shared classes.

### Strengths
- This paper introduces a new setting of domain generalization where classes can be domain-shared or domain-linked.
- The proposed method applies fairness for the domain-linked classes.

### Weaknesses
(1) In section 5.2, the description of fairness is somewhat unclear. The paper states that the fairness loss is intended to reduce the classification loss gap between domain-linked and domain-shared classes, suggesting that minimizing the fairness loss aims to make the classification loss for both types of classes have similar values during training. However, the connection between this specific loss and the broader concept of fairness remains vague. It is not clear how equalizing loss values across these class types ensures fairness in a domain generalization context, especially since the classes themselves have different characteristics and may not be directly comparable in terms of fairness metrics. Furthermore, the paper does not discuss potential negative consequences of enforcing such a fairness constraint, such as a possible reduction in overall accuracy or a bias towards domain-shared classes.

(2) Does $\beta$ in equation (4) have different values for each domain? If $\beta$ is a unique value for all domains, then equation (4) can be rewritten as $...log\frac{\alpha}{\beta} \frac{exp(...)}{\sum exp(...)}$. In this case, should we use $\frac{\alpha}{\beta}$ as one hyperparameter instead of two separate hyperparameters ($\alpha$ and $\beta$)? If so, $\frac{\alpha}{\beta}$ would be similar to $\lambda_{xdom}$. The current explanation lacks sufficient detail on the practical implications of choosing separate values for $\alpha$ and $\beta$, and how this choice impacts the model's learning process.

(3) In section A.3 of the appendix, the hyper-parameter selection and model selection process is not quite clear. It references evaluation settings for domains without distinguishing the source and target domains. It is unclear whether the selection process uses the target domain to evaluate the performance, which would be a significant methodological flaw. The paper needs to explicitly state that the target domain is not used during the hyperparameter selection process to ensure the validity of the results.

### Questions
Please refer to the Weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper delves into the realm of Domain Generalization (DG), emphasizing the challenges posed by domain-linked classes, which are specific to certain domains and thus present significant hurdles in generalization. The authors introduce an algorithm, Fair and cONtrastive feature-space regularization algorithm for Domain-linked DG (FOND), designed to enhance the generalizability of domain-linked classes by leveraging representations from domain-shared classes. Through extensive experiments, FOND purportedly demonstrates state-of-the-art performance in DG tasks for domain-linked classes, provided a sufficient number of domain-shared classes are available. The paper also offers theoretical insights into the factors influencing the performance of domain-linked classes.

### Strengths
Novelty: The paper addresses a less-explored area in DG — the challenge posed by domain-linked classes, which significantly hinders the performance of generalization models.

Quality: The introduction of the FOND algorithm, which aims to improve the generalizability of domain-linked classes by utilizing domain-shared class representations, is a noteworthy methodological contribution.

### Weaknesses
1. Significance: The practical applicability of the research is questionable, given that the empirical validation is conducted on standard domain generalization datasets, which, while containing real-world images, are still constructed to simulate specific domain shifts rather than reflecting the full complexity of real-world scenarios. The paper does not present a compelling real-world application where the domain-linked class problem is a significant bottleneck.

2. Quality: The theoretical analysis lacks depth, presenting generalized bounds without significant divergence from existing domain generalization theories, thereby offering limited novel insights. The theoretical contribution seems to be a re-application of existing theory to a new setting, rather than developing fundamentally new theoretical results.

3. Novelty: The paper's innovation is constrained, primarily adapting existing fairness methods to a new context. The complexity introduced in the loss function, specifically the inter-domain positive and intra-domain negative comparisons, is not sufficiently justified by the performance gains observed. The paper does not adequately demonstrate that this specific form of complexity is necessary compared to simpler alternatives.

4. Clarity: The paper could benefit from a more coherent presentation of ideas, especially concerning the algorithm's design and the theoretical underpinnings. The connection between the theoretical analysis and the specific design choices of the FOND algorithm is not clearly articulated, making it difficult to understand why the chosen loss function is the most appropriate.

### Questions
1. Could you elaborate on the choice of synthetic datasets for validation? How do these datasets simulate the challenges of real-world applications?

2. The theoretical analysis seems to align closely with established domain generalization theories. Could you elucidate the novel contributions of your theoretical insights?

3. The FOND algorithm introduces considerable complexity, especially in the loss function. Can you justify this complexity in relation to the performance gains observed?

4. How does the FOND algorithm ensure the transfer of useful representations between domain-shared and domain-linked classes? Is there a mechanism to prevent the transfer of domain-specific biases?

5. Given the focus on domain-linked classes, could the proposed method be adapted to scenarios with fewer or no domain-shared classes?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
