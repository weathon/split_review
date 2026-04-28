# Multi-Label Test-Time Adaptation with Bound Entropy Minimization

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Mainstream test-time adaptation (TTA) techniques endeavor to mitigate distribution shifts via entropy minimization for multi-class classification, inherently increasing the probability of the most confident class. However, when encountering multi-label instances, the primary challenge stems from the varying number of labels per image, and prioritizing only the highest probability class inevitably undermines the adaptation of other positive labels. To address this issue, we investigate TTA within multi-label scenario (ML--TTA), developing Bound Entropy Minimization (BEM) objective to simultaneously increase the confidence of multiple top predicted labels. Specifically, to determine the number of labels for each augmented view, we retrieve a paired caption with yielded textual labels for that view. These labels are allocated to both the view and caption, called weak label set and strong label set with the same size k. Following this, the proposed BEM considers the highest top-k predicted labels from view and caption as a single entity, respectively, learning both view and caption prompts concurrently. By binding top-k predicted labels, BEM overcomes the limitation of vanilla entropy minimization, which exclusively optimizes the most confident class. Across the MSCOCO, VOC, and NUSWIDE multi-label datasets, our ML--TTA framework equipped with BEM exhibits superior performance compared to the latest SOTA methods, across various model architectures, prompt initialization, and varying label scenarios. The code is available at https://anonymous.4open.science/r/ML-TTA-10BE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on test time adaptation under a multi-label setting, this is an early work in this field.  This paper first analyzes why widely used entropy loss is not helpful in multi-label settings, and proposes a new method to adapt with multi-label. Then, the author proposes the view prompt and caption prompt to adapt the model for each instance. The experiments on three datasets show the effectiveness of the proposed method.

### Strengths
1. This paper focuses on an important question.
2. This paper has a good theoretical analysis.
3. The proposed method achieves better result than baselines.

### Weaknesses
1. The equ(6) is quite difficult to understand, more explanation is needed to show the meaning. The author should explain more about how weak labels and strong label is recognized in the proposed method, and the meaning of $\hat{s}_{ij}^{x^{test}}$.
2. It is unclear which parameter is learnable in this method. The authors need to clearly point out all the learnable parameters.
3. The authors could explain more about the motivation of the view prompt and caption prompt, and why they are useful for this setting.

### Questions
1. The equ(6) is quite difficult to understand, more explanation is needed to show the meaning. The author should explain more about how weak labels and strong label is recognized in the proposed method, and the meaning of $\hat{s}_{ij}^{x^{test}$.
2. It is unclear which parameter is learnable in this method. The authors need to clearly point out all the learnable parameters.
3. The authors could explain more about the motivation of the view prompt and caption prompt, and why they are useful for this setting.

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
5

### Summary
This paper proposes a novel method for Multi-Label Test-Time Adaptation (ML–TTA) using a technique called Bound Entropy Minimization (BEM). Unlike traditional test-time adaptation (TTA) that optimizes for the most confident single-label prediction, BEM increases the confidence of the top-k predicted labels simultaneously. This approach addresses the challenges associated with multi-label data where prioritizing one label can reduce the adaptation effectiveness for others. The framework also incorporates paired captions as pseudo-positive labels to guide adaptation. Experiments conducted on MSCOCO, VOC, and NUSWIDE datasets demonstrate that ML–TTA outperforms existing methods and the original CLIP model, showcasing superior adaptability across diverse architectures and prompt setups.

### Strengths
1. The paper demonstrates robust experimentation across diverse datasets (MSCOCO, VOC, NUSWIDE) and architectures (e.g., RN50, ViT-B/16), showcasing the generalizability and efficacy of the proposed method.
2. The introduction of the Bound Entropy Minimization (BEM) for Multi-Label Test-Time Adaptation (ML–TTA) is a significant theoretical and practical advancement. It effectively addresses the challenges inherent in multi-label test-time adaptation, a space where traditional single-label approaches like entropy minimization fall short.

### Weaknesses
1. The method section, particularly the mathematical formulations and algorithmic details, could be more clearly presented. The explanations surrounding the implementation of label binding and how the paired captions are retrieved need additional clarity for readers less familiar with the intricate mechanisms of vision-language model adaptations.
2. While the paper effectively shows ML–TTA's superiority over traditional methods, it would benefit from a more detailed discussion about the choice of baseline methods and potential reasons for their relative underperformance.

### Questions
See weakness.

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
4

### Summary
This paper introduces a Bound Entropy Minimization method for improving test-time adaptation in multi-label scenarios. BEM addresses the challenge of adapting multiple labels simultaneously. By integrating textual captions to determine the number of positive labels, the method enhances the confidence of several top predicted labels. The proposed Multi-Label Test-Time Adaptation (ML–TTA) framework leverages both visual and textual data, leading to superior performance across various datasets compared to state-of-the-art techniques.

### Strengths
1. The proposed Bound Entropy Minimization (BEM) method presents an innovative solution to improve test-time adaptation in multi-label scenarios.
2. The use of paired captions as pseudo-labels is a clever strategy to determine the number of positive labels for each test instance.
3.  It considers both visual and textual modalities, optimizing for a more robust adaptation to distribution shifts.
4. The figures are well presented.

### Weaknesses
1. More detailed motivation behind the model design is preferred. It is important to explain why the authors propose the method in this work.
2. The proposed method involves multiple steps, including view augmentation, caption retrieval, and label binding, which might introduce complexity in practical implementation. Simplifying the process could enhance usability.
3. The effectiveness of the method heavily relies on the quality and relevance of the paired captions. In real-world scenarios, captions might not always accurately represent the image content, which could affect performance.

### Questions
Please refer to the weakness.

### Soundness
4

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
3

### Summary
The paper presents a novel approach to Test-Time Adaptation (TTA) for multi-label scenarios using a method termed Bound Entropy Minimization (BEM). The paper is well-structured, the problem statement is clear, and the proposed solution is innovative. The integration of view and caption prompts and the application of BEM to meet the test time adaptation are innovative to some extent. However, there are  some details should be clarified.

### Strengths
1) This paper is well-structured, the problem statement is clear, and the proposed solution is innovative. 
2) The integration of view and caption prompts and the application of BEM to meet the test time adaptation are innovative to some extent.
3) Compared with the latest and most advanced methods, the method in this paper achieves the best performance.

### Weaknesses
1) In your paper, the choice of top-k seems to be very important, so how do you determine the setting of k? You said "we retrieve a paired caption with derived textual labels for each view, which then serves as weak label set of size k for the corresponding view." How do you make sure the selected weak label set is reliable?
2) I can not see any explanation about the "augmented view" in this paper, what is the definition of it and what effort does it have in the framework?
3) The comparison methods you selected in the paper may be not designed for multi-label datasets, so is this comparison fair? Could you add more ML-TTA specific framework to the results?
4) Some details: Table 1 lacks a description of evaluation metric; Marking the second-best result in the experimental results is more beneficial to the reader.

### Questions
See the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
