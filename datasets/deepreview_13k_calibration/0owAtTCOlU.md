# GRIC: General Representation and Informative Content for Enhanced Out-of-Distribution Detection

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Out-of-distribution (OOD) detection is crucial for ensuring the robustness of machine learning models in open-world scenarios by identifying inputs from unknown classes. Vision-language models like CLIP have enabled zero-shot OOD detection without requiring labels or training on in-distribution (ID) data. However, current approaches are limited by their dependence on \textit{closed-set text-based labels} and \textit{full image feature representations}, constraining CLIP’s capacity to generalize across diverse labels. In this work, we propose GRIC, a novel method that improves zero-shot multi-modal OOD detection by leveraging two key insights: (1) OOD detection is driven by general ID representations rather than class-specific features, and (2) large language models (LLMs) can enrich the model’s understanding of ID data and simulate potential OOD scenarios without actual OOD samples. GRIC is simple yet highly effective, reducing the false positive rate at $95\%$ recall (FPR95) by up to $19\%$, significantly surpassing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method called GRIC (General Representation for Inference and Classification), designed to improve zero-shot and few-shot learning by leveraging representations from large-scale pre-trained models. GRIC integrates domain-specific knowledge into a unified embedding space that allows the model to transfer knowledge effectively across tasks and domains. The major contributions are the introduction of general ID features for OOD detection with hierarchical prompting.

### Strengths
**1. Presentation**

The paper is generally well-presented and easy to follow. It begins with a clear hypothesis that using a generalized feature segment from the full feature space can improve ID/OOD sample distinction, followed by a systematic explanation of the proposed method for extracting this general feature space.

**2. Algorithm**

The algorithm is straightforward and effective, yielding significant performance gains on both small- and large-scale datasets. Ablation studies demonstrate that both the proposed general subspace extraction and hierarchical prompting contribute substantially to the performance improvements.

### Weaknesses
 **1. Formatting Issues**  
- **Text Accessibility**: The text is not selectable or OCR-scanned, which complicates review and readability.
- **Font and Equation Sizing**: Equations appear in a very small font, raising concerns about compliance with the `.sty` file specifications; table and figure fonts are also difficult to read.
- **Inconsistent Spacing**: Vertical spacing is uneven throughout, affecting readability. Additionally, Section 3.2 would be more appropriately placed in the related work section to improve structure.

**2. Missing Experiments and Analysis**  
While the paper presents a solid set of experiments across multiple datasets, further analysis would strengthen the justification of the approach:
   - **Single-Modality Vision Models**: The paper should demonstrate the effectiveness of general feature extraction in **vision-only models**, without hierarchical prompting, to show that the method generalizes beyond multi-modal settings. Specifically, the method should be evaluated on a standard image classification task using a vision transformer or a convolutional neural network, without relying on text prompts, to isolate the impact of the feature masking strategy.
   - **Integration with Other OOD Scoring Methods**: It would be valuable to evaluate GRIC with alternative OOD scoring metrics, such as **energy-based scores** and **feature-based scores**, to understand its compatibility with established scoring methods beyond MSP. The paper should explore how the proposed feature masking strategy interacts with methods like Mahalanobis distance-based OOD detection or energy-based OOD scores, providing a more comprehensive view of the method's applicability.
   - **ID Accuracy**: Given that real-world deployment typically involves handling both ID and OOD data, the paper should report ID accuracy to confirm that GRIC performs reliably on ID data without regression. The paper should include a detailed analysis of the impact of the feature masking on ID classification performance, ensuring that the gains in OOD detection do not come at the expense of ID classification accuracy.

**3. Additional Ablation Studies**  
- **PCA Transformed Feature Space**: Examine the effectiveness of using PCA-transformed features (from \( R^{s \times r} \) to \( R^{s \times k} \), where \( k \) is the number of principal components) for OOD detection. The paper should analyze the performance of OOD detection using PCA-transformed features, varying the number of principal components to understand the trade-off between dimensionality reduction and OOD detection performance.
- **Principal Component Masking**: Evaluate whether masking high-variance principal components in the PCA-transformed space, while using the remaining components, can improve OOD detection by focusing on features less affected by dominant ID patterns. Specifically, the paper should explore the impact of masking the top-k principal components, where k is a hyperparameter, and analyze how this affects OOD detection performance.
- **Full Feature Matrix for PCA**: Justify why the paper does not use the full feature matrix across all samples per class to compute PCA, as this could potentially improve the robustness of general feature extraction. The paper should discuss the computational cost of using the full feature matrix and provide a rationale for using a subset of features, potentially comparing the performance and computational efficiency of both approaches.
- **Hyperparameter Sensitivity**: Include a sensitivity analysis on the threshold in Equation 3, as this parameter may significantly influence detection performance. The paper should include a detailed analysis of how the threshold parameter affects OOD detection performance, possibly by plotting the performance metrics as a function of the threshold value.

### Questions
Please refer to the weakness

### Soundness
3

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
This paper proposes a new enhancement method called GRIC for CLIP-based OOD detection. GRIC extracts general ID representations rather than class-specific features and introduces LLM-based informative prompts for OOD detection. Experimental results show the proposed GRIC outperforms existing methods.

### Strengths
- GRIC surpasses the two baseline methods, MCM and GL-MCM.

### Weaknesses
 - There is a limited novelty. DICE [1] has a similar concept to drop unnecessary dimensions and shows the effectiveness for OOD detection.

- The motivation in this paper’s method—that class-specific information is unnecessary—raises some questions. In DICE, the motivation is to exclude signals that introduce noise.  Rather than removing information specific to the ID class, I consider this method actually exclude noise signals. Including the ID accuracy of GRIC without informative prompts in Table 6 would help clarify whether the information being removed is indeed ID class-specific.

- A recent challenge in OOD detection is accurately identifying "OOD images that are semantically similar to ID." In this problem setting, known as Hard OOD detection, certain classes within a dataset (e.g., ImageNet) are treated as ID, while other classes in the same dataset are treated as OOD. Therefore, I believe class-specific information is necessary rather than relying on the general representation of the dataset. I would like to see results on the effectiveness of this method when experimenting on Hard OOD detection benchmarks [2, 3].

- The approach is defined as a zero-shot method in L518. However, since it utilizes ID images for PCA processing, I consider this method to be a few-shot learning method, not a zero-shot. The definition of Zero-shot is not using ID images in preprocessing, regardless of whether training is involved [4].

- The code has not been shared, raising concerns about the reproducibility of the method.

### Questions
I wonder about the motivation of this method that class-specific information is unnecessary.  To validate this statement, I would like to know the result of GRIC without informative prompts in Table 6 to clarify whether the information being removed is indeed ID class-specific, not a noisy signal.

Also, I would like to know the result of hard OOD detection.

For more details, please refer to the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Out-of-distribution (OOD) detection is essential for enhancing the robustness of machine learning models in open-world environments by identifying inputs from unknown classes. While vision-language models like CLIP facilitate zero-shot OOD detection without the need for labels or training on in-distribution (ID) data, existing methods are constrained by their reliance on closed-set text-based labels and complete image feature representations, limiting CLIP's generalization capabilities. This work introduces GRIC, a novel approach that enhances zero-shot multi-modal OOD detection by focusing on general ID representations instead of class-specific features and utilizing large language models (LLMs) to enrich the understanding of ID data and simulate potential OOD scenarios without requiring actual OOD samples. GRIC demonstrates significant effectiveness, achieving a notable reduction in the false positive rate at recall (FPR95) and outperforming state-of-the-art methods.

### Strengths
1. The  concept of general representation of ID data is novel to CLIP-based OOD detection.
2. The method is well designed with  various modules.
3. The extensive experiments show the effectiveness of the proposed method.

### Weaknesses
1. One major issue with this paper is that it claims to be in a zero-shot OOD detection setting, but it should actually be classified as a few-shot setting. This is because the calculation of PCA requires the use of ID data, whereas in a zero-shot setting, ID images should be mixed with OOD images to form the test set, making them unavailable. The entire setting of the paper is flawed and needs to be revised

2. There are more state-of-the-art (SOTA) methods for zero-shot OOD detection that have not been compared, such as NegLabel [1], which demonstrates superior performance, and EOE [2], which also utilizes large language models (LLMs) for CLIP-based OOD detection.

3. The results in Table 1 are not representative, as the baseline MCM has already achieved a score of 99%, indicating that the OOD issue in this benchmark has been effectively addressed.

4. There are many more adjustable benchmarks that have not been explored, such as: hard OOD detection, robustness to domain shift and transfer the method to other CLIP-like models (ALIGN, AltCLIP, GroupViT)

### Questions
1. The figures and algorithm seems screenshot and too ambiguous.
2. Many typos are in the paper and need to be revised. For  example,  'fPR95' in 412 is wrong spelling. When using "citation" as the subject, parentheses should not be added. Additionally, lines 493 and 494 overlap due to insufficient line spacing.

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
5

### Summary
This paper introduces GRIC, a novel approach for zero-shot multi-modal OOD detection aimed at enhancing the robustness of machine learning models in open-world environments. Unlike existing methods that rely on closed-set text-based labels and complete image features, GRIC leverages general ID representations and LLMs to improve OOD detection. GRIC's approach rests on two main insights: (1) using general ID representations instead of class-specific features, and (2) enriching the model’s understanding with LLMs to simulate potential OOD scenarios. This method is straightforward yet effective.

### Strengths
1. The paper is well-crafted and clearly presented, with an engaging motivation and good performance results.
2. Extensive experiments demonstrate the effectiveness of the proposed method.
3. The supplementary material provides useful experiments and details.

### Weaknesses
1. The authors claim that "GRIC reduces the FPR95 by up to 19%, significantly surpassing SOTA methods." However, this statement is inaccurate. For instance, NegLabel [1], published a year ago, achieved an FPR95 of 25.40% on the ImageNet-1k benchmark, while the proposed method achieves 20.32%. Thus, the actual improvement is, at most, 5%.

2. I understand that it may be overkill to ask the authors to compare their methods with [2]. However, since [2] also utilizes superclasses for constructing prompts and achieves even higher performance (17.51% evaluated by FPR95), I consider it valuable for authors to add a discussion about the similarities and differences between their proposed method and [2]. If possible, [1] and [2] should be mentioned in the related work part and added to Table 2 to provide a more comprehensive comparison, which will not harm the unique contribution of this work.

3. If possible, the authors are recommended to provide more visualization results for deeper analysis.

4. There are multiple typos. It is recommended that the authors conduct a thorough review of the writing. For example, Line 110: G(x;Yin). L278: FOr this sake.

5. The paper has severe formatting weaknesses.

### Questions
See Weakness

### Soundness
2

### Presentation
3

### Contribution
3
