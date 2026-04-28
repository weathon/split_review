# Can We Ignore Labels in Out of Distribution Detection?

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Out-of-distribution (OOD) detection methods have recently become more prominent, serving as a core element in safety-critical autonomous systems. One major purpose of OOD detection is to reject invalid inputs that could lead to unpredictable errors and compromise safety. Due to the cost of labeled data, recent works have investigated the feasibility of self-supervised learning (SSL) OOD detection, unlabled OOD detection, and zero shot OOD detection. In this work, we identify a set of conditions for a theoretical guarantee of failure in unlabeled OOD detection algorithms from an information-theoretic perspective. These conditions are present in all OOD tasks dealing with real world data: I) we provide theoretical proof of unlabeled OOD detection failure when there exists zero mutual information between the learning objective and the in-distribution labels, a.k.a. ‘label blindness’, II) we define a new OOD task – Adjacent OOD detection – that tests for label blindness and accounts for a previously ignored safety gap in all OOD detection benchmarks, and III) we perform experiments demonstrating that existing unlabeled OOD methods fail under conditions suggested by our label blindness theory and analyze the implications for future research in unlabeled OOD methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses challenges in out-of-distribution (OOD) detection, focusing on "label blindness," where OOD algorithms fail due to a lack of labeled data. It proves that unlabeled OOD detection inherently fails when label information is not linked to the learning objective, proposing an Adjacent OOD benchmark to capture these failures. Experimental results reveal that existing unlabeled methods struggle with overlapping IID and OOD data.

### Strengths
- theoretical foundation proving that unlabeled OOD detection methods are inherently limited by "label blindness" -- a fundamental flaw in current self-supervised and unsupervised OOD approaches.
- novel OOD detection benchmark to test OOD methods under conditions of high overlap between in- and out-of-distribution data, filling a critical gap in safety evaluation.
- Extensive experiments that demonstrate current unlabeled OOD methods often fail in real-world scenarios with overlapping ID and OOD data, highlighting the need for label-aware approaches.
- Offers clear guidance for future OOD research by identifying key challenges and proposing benchmarks that better capture the limitations of current methods.

### Weaknesses
 - Limited applicability of theoretical claims -- while the paper introduces a "Label Blindness Theorem," rely heavily on specific assumptions about mutual information and independence (e.g., Theorem 3.1 and Corollary 3.3), which may limit the generalizability of the "label blindness" concept to real-world applications where these assumptions don't hold. Specifically, the assumption that mutual information between features and labels is zero or near-zero may be too strong, as even without explicit labels, self-supervised learning can capture some implicit correlations. The practical implications of this theoretical constraint need further exploration, especially in scenarios where some degree of correlation between features and labels is present, which is likely in many real-world datasets.
- the practical applicability of this theory is not fully explored and assume idealized conditions (Section 3.1) which might not reflect the complexity of real-world OOD scenarios. The theory, while mathematically sound, does not sufficiently address how its assumptions hold up when applied to complex, high-dimensional data. The idealized conditions, such as perfect independence or zero mutual information, are rarely met in practice. The paper needs a more thorough discussion on the robustness of the theory when these conditions are relaxed or violated. It remains unclear how the proposed framework will perform in scenarios where the data distributions are complex and the relationships between features and labels are non-trivial.
- Relies heavily on specific datasets like ICML Facial Expressions, Stanford Cars, and Food-101, which limits generalizability, as these may not capture the diversity of OOD detection in other modalities such as language or video or audio. The evaluation is limited to image datasets, which may not fully represent the challenges of OOD detection in other modalities. The conclusions drawn from these datasets might not be directly applicable to domains like natural language processing or time-series data, where feature representations and OOD characteristics can differ significantly. The paper should include a discussion on how the findings might generalize to other data types and if the label blindness issue is equally relevant in those contexts.

### Questions
- Could the benchmark be vulnerable to artificially low variance during testing due to potential biases in data selection or label overlap?
- It seems that the notion of of "label blindness" is central to the theory of this paper. How do you address practical situations where correlations between features and labels might enable OOD detection without explicit labels, and would this differ from the guarantees provided by you theoretical assumptions?

### Soundness
4

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
This paper mainly focuses on the Out-of-distribution (OOD) detection problem in self-supervised learning settings, which investigates the conditions for the theoretical guarantee of failure in unlabeled OOD detection from the information-theoretic perspective. In summary, this work first identifies one scenario in which any self-supervised learning or unsupervised learning algorithm will fail when there exists zero mutual information between the learning objective and in-distribution labels and then introduces a new detection task, namely adjacent OOD detection, which is theoretically proved to possibly exist in real-world dataset. Experiments with several existing self-supervised and unsupervised learning OOD methods are conducted to support the major claims of this work.

### Strengths
1. This paper focuses on a new setting, i.e., self-supervised learning OOD, and investigates the feasibility of OOD detection from a theoretical perspective.
2. This paper theoretically proved the existence of failure conditions for unlabeled OOD detection algorithms, namely, label blindness, providing insights from the information-theoretic perspective.
3. This paper also introduces a new task, i.e., adjacent OOD detection, which is theoretically demonstrated to be possible in the real-world dataset.

### Weaknesses
1. The writing and presentation can be further improved, since there are numerous typos and unclear notation or concept definitions. To list some, there is no clear introduction to the general paradigm of unlabeled OOD detection algorithms, and the preliminary about OOD detection is unclear in how to detect the OOD sample beyond using $P(y\notin Y_{in}|x)$. Specifically, the paper lacks a formal definition of what constitutes an 'unlabeled' OOD detection setting, making it difficult to understand the precise problem being addressed. The explanation of how $P(y\notin Y_{in}|x)$ is actually computed or approximated in practice is also missing, which is crucial for understanding the practical implications of the theoretical claims.
2. The motivation and practical significance for considering self-supervised OOD detection is not clear. Given the current presentation and introduction content, the reviewer can hardly understand why we should conduct unlabeled OOD detection. The paper does not adequately explain why self-supervised learning is necessary or beneficial for OOD detection, especially when compared to supervised approaches. The connection between self-supervised pre-training and the ability to detect OOD samples is not clearly established. It remains unclear why a model trained without labels would be better suited for OOD detection than a model trained with labels, even if the labels are pseudo-labels. If we have the pre-trained model on the ID data, even if we adopt the self-supervised learning in pertaining, can we have the pseudo label for those unlabeled data for OOD detection? It could be better to illustrate the overall research setting using some figure or framework before the existing Figure 1 for a better explanation.
3. It seems there are no explicit assumptions for the theoretical results and most theoretical results are based on the sufficiency definition in definition 2.1 and the minimal sufficient statistic in definition 2.2. It is questionable whether the theoretical insights reflect the real-world challenge or not, as there is limited empirical justification for those intermediate theoretical results based on mutual information. The paper does not clearly state the assumptions under which the theoretical results hold, making it difficult to assess their validity and applicability. The reliance on sufficiency and minimal sufficient statistics, while theoretically sound, lacks a clear connection to practical scenarios. The paper would benefit from a more detailed discussion of how these theoretical concepts relate to the actual behavior of self-supervised models in OOD detection tasks. It could be better if the presentation incorporated more quantitative results regarding the mutual information.

### Questions
1. It seems to be an unknown reference at the end of the first key contributions on Page 2.
2. Although the adjacent ood is discussed to be different from those previously defined near ood or far ood scenarios, what is the difference between adjacent ood with anonymous outlier detection if there is significant feature overlap at both settings?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a theory to explain the failure of unlabeled OOD detection. The authors also define a new OOD task to test for label blindness and conduct experiments to verify the correctness of their theorem.

### Strengths
[1] The paper is clear and easy to understand.

[2] The theory clearly explains the potential problem of unlabeled OOD detection.

[3] The theory is verified by the empirical studies, raising real concerns about unlabeled OOD detection.

### Weaknesses
[1] While the main theory is sound in this paper, it is intuitive that the unlabeled OOD methods will fail if there is zero information between the learning objective and the label: For example, if we use linear regression to fit random noise, it is supposed to learn nothing. If the learning objective of the unlabeled OOD detection learns every feature but still has zero information with the label, then my understanding is that labeled OOD methods will also fail. Could the authors provide some comments on how the theory should be adapted in such a case?

[2] While Theorem 4.1 provides some justification on the effectiveness of the proposed Adjacent OOD task, there is a gap between Theorem 4.1 and the main theory: even if P(a randomly selected x contains y not present in $R_{y_{in}}$)>0, this is not exactly connected with the mutual information between the learning objective and the label. I would suggest the authors provide some more evidence, either theory or just simple simulation, to provide a more rigorous connection between the main theory and conclusion of Theorem 4.1.

[3] It is not clear how the theory can provide practical guidance on designing better learning objectives of unlabeled OOD. The paper provides the Adjacent OOD task, but this is different from suggesting a way of improving existing design: we know they fails, but we don't know how to improve them. Could the authors provide some comments on this?

[4] Please highlight the technical contribution when deriving the theorems. Since as elaborated in Weakness [1], the main theory is intuitive, it is not clear how difficult it is to prove it.

[5] Writing: please revise the wording in this paper to be more objective. For example, the word "you" or "your" appear 6 times in total.

### Questions
Please address my comments in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
