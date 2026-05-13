# Optimal Learning of Kernel Logistic Regression for Complex Classification Scenarios

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Complex classification scenarios, including long-tailed learning, domain adaptation, and transfer learning, present substantial challenges for traditional algorithms. Conditional class probability (CCP) predictions have recently become critical components of many state-of-the-art algorithms designed to address these challenging scenarios. Among kernel methods, kernel logistic regression (KLR) is distinguished by its effectiveness in predicting CCPs through the minimization of the cross-entropy (CE) loss. Despite the empirical success of CCP-based approaches, the theoretical understanding of their performance, particularly regarding the CE loss, remains limited. In this paper, we bridge this gap by demonstrating that KLR-based algorithms achieve minimax optimal convergence rates for the CE loss under mild assumptions in these complex tasks, thereby establishing their theoretical efficiency in such demanding contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a theoretical explanation for the empirical success of conditional class probability (CCP)-based method, particularly regarding the cross entropy (CE) loss. Specifically, this paper first truncates the CCP estimator to prevent large CE loss. Consequently, the authors discuss the properties of kernel logistic regression (KLR) in three complex classification scenarios. The findings indicate that KLR can achieve minimax optimal convergence rates for CE loss under mild conditions. Furthermore, the error analysis reveals that the excess CE risk for the complex classification scenarios can be reduced to that for the standard classification, establishing a new oracle inequality of KLR for CCP estimation.

### Strengths
-	This paper is well-written and organized. The theoretical analysis is detailed and coherent. 
-	This paper has proposed a significant theoretical understanding of CCP-based approaches. The results are impressive.

### Weaknesses
Please see the **Question** section

### questions:
 1. In Section 2.1, why is the label probability $q(y)$ set to be uniform while $p(y)$ is far from being uniform? Could you provide more context behind this choice?
2. The equation in the Theorem 3.5 is not labeled. Labeling this equation would improve readability and make it easier to reference later in the paper.
3. Note that the first item on the right-hand side of Equation (11), (13) and (14) is the same. The same pattern is observed in the results of lower bounds. Could you explain this phenomenon? What it might reveal about the fundamental nature of these classification tasks?
4. This paper presents important theoretical results. Could the authors explain how the results can help improve the practical solution of complex classification scenes? For example, what particular aspects of algorithm design or parameter selection that might be informed by these theoretical results? Including toy experiments might be beneficial to illustrate the practical impact.

### Questions
1. In Section 2.1, why is the label probability $q(y)$ set to be uniform while $p(y)$ is far from being uniform? Could you provide more context behind this choice?
2. The equation in the Theorem 3.5 is not labeled. Labeling this equation would improve readability and make it easier to reference later in the paper.
3. Note that the first item on the right-hand side of Equation (11), (13) and (14) is the same. The same pattern is observed in the results of lower bounds. Could you explain this phenomenon? What it might reveal about the fundamental nature of these classification tasks?
4. This paper presents important theoretical results. Could the authors explain how the results can help improve the practical solution of complex classification scenes? For example, what particular aspects of algorithm design or parameter selection that might be informed by these theoretical results? Including toy experiments might be beneficial to illustrate the practical impact.

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
This paper proposes a theoretical framework using Kernel Logistic Regression (KLR) to address the Conditional Class Probability (CCP) estimation problem in complex classification tasks. By introducing error decomposition and a new oracle inequality, the researchers demonstrate KLR’s optimal convergence rates in scenarios like long-tail learning, label shift, and transfer learning, underscoring its effectiveness in both theoretical and practical applications.

### Strengths
1. The authors decompose the unbounded CE loss into upper and lower bounded components, ensuring the boundedness of the sample error term. This decomposition enhances the model's interpretability and strengthens the robustness of using KLR for CCP estimation in complex tasks.
2. The proposed framework is versatile, offering potential applicability across various complex classification task scenarios and showing promise for real-world applications in long-tail distributions, label shift, and transfer learning.

### Weaknesses
1 The paper focuses on theoretical analysis without experimental validation on real-world datasets or applications. Although the theoretical results suggest that KLR has potential in complex classification tasks, without empirical evaluations, it’s difficult for readers to assess the method’s practical performance or compare it to other methods.
2 The paper highlights the theoretical advantages of KLR in complex classification tasks but does not extensively compare it with other commonly used kernel methods (e.g., Support Vector Machines, Gaussian Processes) or modern deep learning methods.
3 The theoretical proofs rely on several assumptions about the data distribution, such as smoothness of conditional probabilities and specific constraints on small values. These assumptions may not hold in all real-world applications, which could affect the generalizability of the method. For example, in long-tailed or multimodal data distributions, these theoretical assumptions might be difficult to satisfy, potentially resulting in degraded model performance.

### Questions
1. The experimental section is relatively limited, which limits validation of the framework's practical utility. Examples in the paper lack real-world data validation in complex classification settings, especially regarding long-tail learning and transfer learning. More comprehensive experiments with various real datasets are needed to demonstrate the theoretical findings effectively.
2. In Assumption 3.1, the authors assume smoothness of the conditional probability function and impose a lower-bound condition on probability values. However, these assumptions are challenging to satisfy in real-world data, where extreme nonlinearity or sparse data often preclude such smoothness, especially in high-dimensional settings. This limits the generalizability of the framework for practical applications.
3. Although kernel methods can theoretically enhance model expressiveness, the complexity of Kernel Logistic Regression increases significantly with sample size and feature dimensions. Particularly in high-dimensional datasets, memory consumption and computation time grow exponentially. While the authors suggest a Gaussian kernel-based approach, they do not provide further optimization strategies to alleviate computational costs. For large-scale datasets, it would be beneficial to explore additional methods for reducing computational burdens to enhance scalability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The existing literature offers limited theoretical exploration of conditional class probabilities-based algorithms for classification in complex scenarios, particularly concerning the cross-entropy loss. In this paper, authors investigated the convergence rates of algorithms based on conditional class probabilities estimation using kernel logistic regression in complex classification scenarios, such as long-tailed learning, domain adaptation, and transfer learning.

### Strengths
1. A new oracle inequality for kernel logistic regression is established that holds with high probability.

2. The approximation error of kernel logistic regression w.r.t. the cross-entropy loss is derived.

3. The optimal convergence rates w.r.t. the cross-entropy loss for complex variants of classification problems is established.

### Weaknesses
1. As stated in the 3rd paragraph, the main motivation is "The existing literature offers limited theoretical exploration of conditional class probabilities-based algorithms for classification in complex scenarios, particularly concerning the cross-entropy loss.” It can be better to show the connection of the findings in this paper (i.e., kernel logistic regression for complex classification scenarios) and existing findings for standard classification scenario.

2. It can be better to show the connection of the three contributions in introduction. In the current version, it is even hard to find if there is some connection them with the title of this paper.

3. The main novelty is to restrict applications into three kinds of scenarios, i.e., long-tailed learning, domain adaptation, and transfer learning, which are called complex classification scenarios. I know all of them, but I don't know why they are put together in this paper (especially for long-tailed learning). Is there any logic to that? Why does the author focus on these three scenarios? The current version feels pieced together.

### Questions
Please explain the 3rd weakness mentioned above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the theoretical properties of kernel logistic regression (KLR) in addressing complex classification challenges, such as long-tailed learning, domain adaptation, and transfer learning. The study highlights KLR's strengths in conditional class probability (CCP) estimation and demonstrates that KLR-based algorithms can achieve minimax optimal convergence rates for cross-entropy (CE) loss under mild conditions. 

This paper presents the relevant theory of kernel logistic regression in complex classification scenarios and provides thorough justification. While it is a solid theoretical work, it somewhat lacks practical guidance for real-world classification problems. Readers may find it difficult to extract feasible methods for addressing issues such as long-tailed distributions from the presented arguments.

### Strengths
1. This paper provides a theoretical analysis of optimal learning for kernel logistic regression in various complex scenarios, including long-tailed learning, domain adaptation, and transfer learning.
2. A detailed proof process is provided for the theories related to KLR and cross-entropy (CE).
3. Exploring and analyzing complex classification scenarios from a theoretical perspective is insightful and innovative.

### Weaknesses
1. Currently, kernel-based methods cannot compete with mainstream neural network methods in real-world classification tasks, such as ImageNet and iNaturalist 2018. As a result, the practical significance of this work may be significantly diminished.
2. To determine whether the theory is truly applicable in complex classification scenarios, experimental validation is needed. This paper lacks experimental results to verify whether the proposed theory aligns with real-world situations. By conducting experiments, further analysis could be done to identify in which cases the theory holds and in which cases it does not. This would provide readers with more valuable insights and practical references.

### Questions
See Weaknesses.

1. Based on these theories, how should we design classification models? Could you provide some examples explicitly addressing issues like long-tailed distributions? Alternatively, could you analyze existing models, such as LDAM-DRW [1] and Logit Adjustment, and suggest possible improvements?

[1] Kaidi Cao, Colin Wei, Adrien Gaidon, Nikos Arechiga,and Tengyu Ma. Learning imbalanced datasets with labeldistribution-aware margin loss. In NeurIPS, pages 1567–1578, 2019.

[2] Aditya Krishna Menon, Sadeep Jayasumana, Ankit Singh Rawat, Himanshu Jain, Andreas Veit, and Sanjiv Kumar. Long-tail learning via logit adjustment. In ICLR, 2021.

2. Data, models, and loss functions are key considerations in classification tasks. This paper has already provided analysis from the perspective of the model (kernel methods) and the loss function (CE). Typically, when dealing with complex tasks, data augmentation techniques such as rotation, flipping, crop, and noise addition are applied. How would these operations impact the proposed framework?

### Soundness
3

### Presentation
3

### Contribution
2
