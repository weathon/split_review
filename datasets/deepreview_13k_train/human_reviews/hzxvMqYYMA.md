# Understanding the Generalization of Blind Image Quality Assessment: A Theoretical Perspective on Multi-level Quality Features

- Decision: Reject
- Scores: 6, 8, 3, 6

## Abstract
Due to the high annotation costs and relatively small scale of existing Image Quality Assessment (IQA) datasets, attaining consistent generalization remains a significant challenge for prevalent deep learning (DL)-based IQA methods. Although it is widely believed that quality perception information primarily resides in low-level image features, and that effective representation learning for the multi-level image features and distortion information is deemed crucial for the generalization of the Blind IQA (BIQA) methods, the theoretical underpinnings for this belief still remain elusive.  Therefore, in this work, we investigate the role of multi-level image features in the generalization and quality perception ability of the CNN-based BIQA models from a theoretical perspective. For the role of low-level features, in Theorem 1, we innovatively derive an upper bound of Rademacher Average and the corresponding generalization bound for the CNN-based BIQA framework under distribution invariance in training and test sets, which indicates that the generalization ability tends to be reduced as the level of quality features increases, demonstrating the value of low-level features. In addition, under distribution shifts, a much tighter generalization bound is proposed in Theorem 2, which elucidates the theoretical impact of distributional differences between training and test sets on generalization performance. For the role of high-level features, in Theorem 3, we prove that BIQA networks tend to possess higher Betti number complexity by learning higher-level quality features. This indicates a larger representation power with smaller empirical errors, highlighting the value of high-level features. The three proposed Theorems can provide theoretical support for the enhanced generalization in existing BIQA methods. Furthermore, these theoretical findings reveal an inherent tension between robust generalization and strong representation power in BIQA networks, which inspires us to explore effective strategies to reduce empirical error without compromising the generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the generalization of CNN NR-IQA models and also investigates the roles of low- and high-level image features. It does establish theoretical generalization bounds, showing the effect of low-level  and high level features on generalization and representation capabilities.  The paper ends with 3 suggestions incorporated into a loss function that they claim to train CNN based IQA models better.

### Strengths
1. Theoretical analysis provides valuable insights into BIQA model performance in terms of generalizability, representation power, empirical results
2. This paper offers actionable insights drawn from theoretical results in the form of a new loss function to improve the training of CNN-based IQA models.
3. The results show that the method improves the training of BIQA methods. However, as highlighted in the weakness section, the experiment setup and results have some limitations.

### Weaknesses
1. Regarding cross-database experiment results in Table 1-4. In Tables 1-2, the results with $\mu, v =0$ should be provided. This will help gauge the usefulness of using the loss function proposed in Equation 15. In Table 4, it would be nice to have results in more than one cross dataset, or should authors justify using the KADID(train)/CID(test) database in the paper as to why the pair is a representative dataset?
2. Regarding results in Table 3, 7 the authors. The performance increase for the Resnet-50+ KonIQ scenario is much when incorporating the suggestions in the paper, while for MUSIQ+KonIQ, the performance boost is pretty low.  Do the authors have an intuition or explanation for this? Also, the results in Table 8 show negligible gains (probably statistically insignificant). Can this be interpreted as the method does not work well for transformer-based models?
3. Overall, the authors should also report RMSE in addition to SRCC and PLCC (as in many IQA/VQA papers). This should give an idea of improvement in predicted absolute values apart from the correlation. 
4. Regarding the paper draft: Improving the paper's readability and organization of the text is needed.

### Questions
1. Please reply to Weaknesses #2
2. The paper ignores the use of the largest IQA (FLIVE, https://arxiv.org/pdf/1912.10088) database in the analysis and results. Could the authors explain the reasoning? The paper claims that generalization is limited by the small scale of the training IQA datasets, so leaving out the largest dataset needs some explanation.
3. How does the generalizability of the NR-IQA methods differ in two scenarios: real-life (UGC) distortions v/s synthetic distortions? Does training and testing in the same and different scenarios have any effect? Example: UGC(Train)- Synthetic(Test), UGC(Train)- UGC(Test) among others.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper investigates the role of multi-level image features in the generalization and quality perception ability of the CNN-based BIQA models from a theoretical perspective. Specifically, three theorems are proposed, which can provide theoretical support for the enhanced generalization in existing BIQA methods.

### Strengths
This paper investigates the role of multi-level image features in the generalization and quality perception ability of BIQA models from a theoretical perspective.
Different generalization bounds for CNN-based BIQA networks are formulated.
The fundamental conflict between the generalization and representation abilities of CNN-based BIQA models is undercovered.

### Weaknesses
1.	This paper is pretty theoretical, which may give better understanding of the current BIQA models. However, the contributions of this paper to the practical BIQA model design and the relevant research should be highlighted.
2.	The theoretical derivations of the whole paper rely heavily on the existing theoretical research of general deep neural networks. The core differences/adaptions/contributions achieved in this paper (which are different from the existing research) should be well-explained.
3.	It seems that theoretical derivations only work for some specific architectures of BIQA models. The generalization to broader scope of BIQA networks should be discussed.
4.	Only limited BIQA models are selected to validate the theorems of the paper, and quantitative results in the paper are also limited.

### Questions
Following the above weaknesses, some questions are suggested to be answered.
1.	What are the contributions of this paper to the practical BIQA model design and the relevant research.
2.	What are the core differences/adaptions/contributions achieved in this paper, which are different from the existing research?
3.	What about other kinds of architectures beyond CNN, as more and more complicated model designs are involved. Nowadays, even LMMs are introduced for BIQA.
4.	More extensive experimental verifications are suggested to be given, for example, hand-crafted models like BMPRI, as well as DNN-based methods like RichIQA and StairIQA.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a theoretical analysis of multi-level image features in CNN-based BIQA models through three theorems. The findings reveal that low-level features enhance model generalization, high-level features boost representation power, and distribution differences between training and test sets affect generalization performance. Extensive experiments confirm these theoretical insights.

### Strengths
1. This paper investigates the role of multi-level image features in the generalization and quality perception ability of the CNN-based BIQA models from a theoretical perspective. Such theoretical research is rare in the field of IQA.
2. The theoretical findings are validated through both extensive experimental results and consistency with previous research observations in the field.

### Weaknesses
1. Limited contribution: The theoretical derivations in this paper primarily focus on analyzing existing consensus in the field using established theoretical frameworks, without presenting new insights, methods, or theoretical analysis approaches, thus lacking meaningful guidance for future work.
2. The paper's theoretical analysis focuses on model depth. Can the conclusions drawn from this effectively explain the role of multi-level feature fusion within the same network?
3. Theorem 1's significance is questionable as its core conclusions appear redundant with Theorem 2.
4. The derivation in Theorem 2 requires further explanation: 1) How is Equation 45 obtained? 2) The substitution of Equations 44 and 45 into Lemma 2 doesn't appear to yield Equation 46; please provide more detailed derivation steps. 3) There is an error in the definition of Z (missing ϵi).
5. Theorems 1 and 3 have different requirements for activation functions, potentially creating contradictions. For instance, ReLU is not a Pfaffian function and thus doesn't apply to Theorem 3, while tanh is not a non-negative function and doesn't apply to Theorem 1.
6. The meaning of Corollary 1 is unclear. It does not appear to have been explained in the paper.
7. The experimental section includes validation for Theorems 1 and 2, but lacks validation for Theorem 3.
8. In line 474, it is mentioned "According to the theoretical results of this work, we propose the Consistency Regularizer and Parameter Regularizer in the loss function Eq. (15)." However, both regularizers lack detailed explanations, and Eq. (15) is not thoroughly introduced.
9. There are some writing errors, such as in the y-axis of Fig. 1(b).

### Questions
N/A

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
2

### Summary
In this paper, the authors theoretically analyze the influence of multi-level image features on the generalization and quality perception abilities of CNN-based BIQA models. By establishing generalization bounds and employing Betti number-based analysis, they highlight the importance of low- and high-level features for model performance under distribution shifts. Their findings expose an inherent tension between generalization capacity and representational power, offering valuable insights for optimizing BIQA training.

### Strengths
1. This work provides the first theoretical establishment of a generalization boundary in the IQA domain, offering foundational guidance to improve BIQA model generalization.
2. Both key scenarios in IQA—distribution invariance and distribution shift—are thoroughly investigated.
3. Extensive experiments are conducted to empirically validate the theoretical findings.

### Weaknesses
1. Some symbols lack clear definitions in certain equations. For instance, $b$, $M$, $\delta$, and $L_{\phi}$ in Eqn. (7) and (8) are not well explained. Please explicitly define these symbols in the text preceding the equations to enhance clarity.
2. In Sec. 4.2, Theorem 1, the conclusion in (1) regarding the impact of increasing depth $L$ on the RA term's upper bound lacks rigor; increasing depth $L$ could also reduce empirical errors, potentially benefiting the generalization bound.  The authors are encouraged to clarify their conclusion under specific conditions. An additional discussion on the trade-off between the increase in the RA term and the potential decrease in empirical error would further enhance the analysis.
3. Theorem 2 suggests that the choice of loss function significantly affects the generalization capacity of BIQA models. It would be beneficial to analyze the advantages of loss functions like NIMA and Norm-in-Norm to further support Theorem 2. A brief comparative analysis of how different loss functions might influence the generalization bound derived in Theorem 2 is recommended.
4. While this paper focuses on CNN-based BIQA models, it would be useful to explore whether the conclusions apply to CNN-based general regression tasks, given that network settings or loss functions may not be IQA-specific. An additional discussion on the potential generalizability of the findings to other CNN-based regression tasks is recommended.

### Questions
Suggestions on the choice of loss function are advised, based on the insights from Theorem 2. It would be beneficial to test examples demonstrating how advanced loss functions might be more suitable for BIQA.

### Soundness
3

### Presentation
3

### Contribution
3
