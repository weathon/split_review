# Multiplicative Logit Adjustment Approximates Neural-Collapse-Aware Decision Boundary Adjustment

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Real-world data distributions are often highly skewed. This has spurred a growing body of research on long-tailed recognition, aimed at addressing the imbalance in training classification models. Among the methods studied, multiplicative logit adjustment (MLA) stands out as a simple and effective method. What theoretical foundation explains the effectiveness of this heuristic method?
We provide a justification for the effectiveness of MLA with the following two-step process. First, we develop a theory that adjusts optimal decision boundaries by estimating feature spread on the basis of neural collapse. Second, we demonstrate that MLA approximates this optimal method. Additionally, through experiments on long-tailed datasets, we illustrate the practical usefulness of MLA under more realistic conditions. We also offer experimental insights to guide the tuning of MLA hyperparameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a theoretical foundation for the Multiplicative Logit Adjustment (MLA) method used in long-tailed recognition tasks. First, the authors develop a theory for optimally adjusting decision boundaries by leveraging feature spread estimates derived from neural collapse (NC). They then demonstrate that MLA effectively approximates this optimal adjustment method. Experiments conducted on various long-tailed datasets validate the practical applicability of this approximation, showing that MLA performs well under realistic conditions.

### Strengths
- This paper presents a theory for optimally adjusting decision boundaries based on NC and links it to the MLA method, providing a strong theoretical explanation for MLA and adding depth to its empirical success.
- The authors conduct a series of experiments on long-tailed datasets to validate the theory and demonstrate the practical utility of MLA.
- The authors offer both theoretical and empirical comparisons between MLA and ALA, clarifying their differences and highlighting the advantages of MLA.

### Weaknesses
 - The iNaturalist dataset is a widely used large-scale long-tailed dataset. Conducting experiments on this dataset would be beneficial to examine the behavior of MLA, ALA, and the 1vs1 adjuster in a larger-scale real-world context. Specifically, the performance of these methods should be evaluated under the more realistic conditions of iNaturalist, which includes a greater number of classes and more complex image variations. Additionally, testing on CIFAR-LT with more extreme imbalance ratios, such as an imbalance factor of 200 or greater, would further evaluate the effectiveness of the proposed method under highly skewed class distributions. This would help determine the robustness of MLA in scenarios where the tail classes are extremely underrepresented.

- The theoretical framework relies on some strict assumptions that may not always hold in practice. The assumption of conditions under which neural collapse (NC) occurs is particularly concerning, as NC may not be fully realized in highly imbalanced real-world datasets, potentially affecting the validity of the derived adjustments. Furthermore, the assumption that $\psi \rightarrow \pi/2$ does not hold when $K$ is small, which could limit the applicability of the theory to datasets with a small number of classes. The impact of these deviations from the theoretical assumptions on the practical performance of MLA needs to be more thoroughly investigated.
- There are some typos, such as on line 373, where "the optimal decision boundaries during inference is effected by" should be corrected to "the optimal decision boundaries during inference are affected by".

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to provide a theoretical justification for Multiplicative Logit Adjustment (MLA) in long-tailed recognition by linking it to Neural Collapse theory. The authors develop a theoretical framework for optimal decision boundary adjustment based on feature spread estimates from Neural Collapse and demonstrate that MLA approximates this optimal method.

### Strengths
The framework that connects MLA with Neural Collapse is novel.  The assumptions and conditions are clearly stated, and the notation is consistent and well-defined.

### Weaknesses
1. **Motivation**:
   The paper fails to establish a compelling motivation for the study. The claim that "MLA has demonstrated significant empirical success" is not sufficiently substantiated. There is no systematic analysis of the current strengths and challenges of MLA in long-tailed recognition.

2. **Theory-Practice Gap**:
   The connection between optimal decision boundary adjustment and actual performance improvements in long-tailed scenarios is weak. While the paper seems to demonstrate the effectiveness of MLA as a close approximation to the 1vs1adjuster from both theoretical and experimental perspectives, and contrasts it with Additive Logit Adjustment (ALA), it does not thoroughly analyze how MLA addresses the specific challenges of long-tailed learning from a theoretical standpoint. Additionally, there is no comparison with state-of-the-art long-tailed baselines or discussion on how MLA could be integrated with them. The experimental section focuses more on hyperparameter tuning for MLA rather than examining its impact on long-tailed learning.

### Questions
The paper mentions that "MLA has demonstrated significant empirical success," but it does not provide sufficient evidence to support this claim. Could more literature or experimental results be added to demonstrate the current advantages of MLA in long-tailed recognition?

The theoretical comparison between MLA and ALA is addressed in some aspects, but why is there no comparison with other advanced baselines in long-tailed recognition (such as the latest contrastive learning methods or distribution-balanced loss)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses the problem of class imbalance in classification models and analyzes the effectiveness of the Multiplicative Logit Adjustment (MLA) method. The authors propose a theory on optimal decision boundaries based on neural collapse, demonstrating that MLA approximates these optimal boundaries. The paper is supported by experiments across various modalities, providing insights into MLA’s performance under different conditions.

### Strengths
* The problem of class imbalance is clearly motivated, and the investigation into MLA is a valuable contribution to this area of research.
* The mathematical framework is well-developed, offering a solid theoretical foundation for understanding the method.
* The analysis extends beyond image datasets to include other modalities, such as text, enhancing the paper's applicability.
* Extensive experiments are conducted, which reinforce the theoretical claims and provide a comprehensive evaluation of MLA’s performance.

### Weaknesses
 * While the theoretical concepts are accurately communicated, the writing could be improved by breaking up overly long sentences to enhance readability (e.g., lines 098-104).
* The results in Tables 6-10 are intriguing, but more explanation is needed to clarify the implications of "Many," "Medium," and "Few" categories. Additionally, the reasons for the Baseline outperforming others in the "Many" category should be discussed in more depth. Specifically, it is unclear how these categories are defined in relation to the class imbalance ratio and how this impacts the interpretation of the results. Furthermore, the performance of the baseline in the "Many" category, while expected, needs a more detailed analysis to contextualize the improvements of the proposed method.
* The descriptions for tables and figures are too brief, making it difficult for readers to grasp the full context of the results. Adding more detailed captions would help in understanding the findings. For example, the captions should include details about the experimental setup, the specific metrics being reported, and the statistical significance of the results.
* The paper contains numerous formal definitions and formulas, which can disrupt the reading flow, especially for readers who are not deeply familiar with this specific research area. The paper could benefit from more intuitive explanations of these concepts, perhaps through the use of examples or analogies, to improve accessibility.

### Questions
1. Why did you primarily focus on ResNet models for the image analysis? Were there specific reasons for this choice over other architectures?
2. Why did you create imbalanced versions of balanced datasets instead of using inherently imbalanced datasets? For example, datasets that exhibit natural class imbalances could offer more realistic evaluations.
3. Although the paper focuses on post-hoc LA methods, did you compare the results with loss-function-based approaches? How does MLA's performance compare to other logit adjustment methods?

### Soundness
3

### Presentation
3

### Contribution
3
