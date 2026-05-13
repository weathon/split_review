# Test Time Augmentations are Worth One Million Images for Out-of-Distribution Detection

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Out-of-distribution (OOD) detection is a major threat for deploying machine learning models in safety-critical scenarios. Data augmentations have been proven to be beneficial to OOD detection by providing diverse features. However, previous methods have only focused on the role of data augmentation in the training phase, overlooking its impact on the testing phase. In this paper, we present the first comprehensive study of the impact of test-time augmentation (TTA) on OOD detection. We find aggressive TTAs can cause distribution shifts on OOD scores of In-distribution (InD) data, whereas mild TTAs do not, resulting in the effectiveness of mild TTAs on OOD Detection. Based on the above observations, we propose a detection method that performs a K-nearest-neighbor (KNN) search on mild TTAs instead of InD data. With only 25 TTAs, our method outperforms state-of-the-art methods using the entire training set (1.2 million images) on IMAGENET for OOD detection. Moreover, our approach is compatible with various model architectures and robust to adversarial examples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this study, the authors present a study of the impact of test-time augmentation on out-of-distribution (OOD) detection. The authors first analyze that strong test time augmentations can cause distribution shifts on both OOD and ID data but mild augmentation could only affect OOD samples. Based on this analysis, the authors propose a new OOD detection method with a KNN search on mild augmentation. With 25 test time augmentation samples, the authors show that the proposed method could detect OOD samples with a performance which is comparable to other methods.

### Strengths
- The authors analyze data augmentations and categorize strong(aggressive) data augmentation and mild data augmentation in the view of OOD detection (whether these augmentations shift in distribution samples or not). It is very interesting to present the effect of different augmentation schemes on OOD detection.
- The method can be used without retraining or accessing additional OOD samples.
- The proposed method is simple and shows comparable performance on CIFAR10 and ImageNet.

### Weaknesses
 - The novelty is very limited. The data augmentation has recently also been investigated in OOD detection or anomaly detection [R1-R2]. [R1] uses data augmentation for anomaly detection. [R2] uses simple test-time blurring (a kind of data augmentation) for OOD detection. It would be better to discuss related studies and clarify the novel contribution of this paper. It is important but is currently missing from the current version of the paper. 
- The paper might lead to a misunderstanding of the related studies. The authors claim that InD-Independent approaches (MSP, DICE, GradNorm, and ReAct) have a limitation, which requires accessing the in-distribution samples. Some of them also can be just used at the test time like the proposed method. Even using some portion of training data is not a critical limitation of these studies in many cases. The authors also did not compare the proposed method with DICE and GradNorm. ASH which does not require additional test data also outperforms the proposed method. [R3] is also important study but it is missing.
-  It would be better to analyze the distribution shift of ID and OOD samples under data augmentation in a more theoretical way. Why some data augmentations are good at OOD detection and others are not.
- The proposed method requires 25 inferences which limits the real-time use of the method
- Comparison with other methods is performed on only CNN-based architectures. ViT result is only reported on the proposed method. The OOD detection score is different with respect to the model and it would be great to compare with other methods on ViT architecture.

### Questions
- It would be great to clarify the novel contribution of the method compared with other augmentation-based approaches.
- It would be great to further discuss the limitations of InD-independent approaches because it is unclear to me. It would be better to correctly clarify the method which does not require to access InD samples.
- Discussion with DICE and ASH, [R3] will strength the paper.
- How the method can be generalizable to different architectures? It would be great to compare with other methods on the ViT backbone.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focus on performing test time augmentation to improve semantic-shift OOD detection. It first categorizes the OOD detection in to In-Distribution Augmentation (IDA) and Out-of-Distribution Augmentation (OODA) and proposes to utilize the learned Perceptual Image Patch Similarity (LPIPS) distances to differentiate between IDA and OODA. Further, a  TTA method based on the sequential mask is proposed to boost the OOD performance when employing the K-th nearest neighbor (KNN) as the OOD score.  Moreover, a thorough ablation studies are presented.

### Strengths
- The paper is well-written and clearly presented.
- The findings related to IDA and OODA are novel, and the proposed OOD score, which does not rely on in-distribution data, is a logical and reasonable approach.
- Section 2 is well-organized and clearly explained.

### Weaknesses
 - Novelty and Baselines: While the proposed method shows novelty, a few relevant baseline methods are missing. It would be beneficial to categorize the proposed approach as a post-hoc OOD scoring method and compare it to existing techniques, such as Maximum Softmax Probability (MSP), Energy score, GradNorm [1], and GEN [2]. Including a comparison with GEN [2], a recent post-hoc OOD scoring method that only requires access to probability information, would strengthen the evaluation. Specifically, the paper should include a comparison with methods that operate directly on the output probabilities or logits, as these are the most relevant baselines for a post-hoc approach. The current evaluation lacks a clear comparison to these methods, making it difficult to assess the true advantage of the proposed approach.

- Additional Architectures: It is commendable that Table 8 includes TTA performance across different architectures. However, for a more comprehensive evaluation, the performance of other baseline methods (e.g., Energy score) should also be reported. Without these comparisons, it is difficult to discern whether the observed performance changes are due to architectural differences rather than a specific advantage of TTA. A table similar to Table 13 in Appendix F, but for other architectures (ViT-b-16 and ResNet-50), would address this concern. The evaluation should not only show that TTA works across architectures, but also how it compares to other OOD detection methods on those same architectures. This is crucial for understanding the method's generalizability and relative performance.

- Optional Suggestion for Table 1: For readability, it may be helpful to split Table 1 into two sections: one for methods that do not require access to training data and another for methods that do.

- (Optional suggestion) Generalizability of TTA: It would be interesting to explore whether TTA could be combined with other post-hoc scoring methods, such as Energy and GEN. The paper should discuss the potential for combining TTA with other post-hoc methods and whether the proposed approach is orthogonal to existing techniques. This would provide a more comprehensive understanding of the method's applicability and potential for integration with other OOD detection strategies.

### Questions
See weakness

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
4

### Summary
Out-of-distribution (OOD) detection poses significant challenges for deploying machine learning models in safety-critical applications, and while data augmentations have been shown to enhance OOD detection by providing diverse features, previous research has primarily focused on their role during training, neglecting their effects during testing. This paper presents the first comprehensive study on test-time augmentation (TTA) and its impact on OOD detection, revealing that aggressive TTAs can lead to distribution shifts in OOD scores for in-distribution (InD) data, while mild TTAs do not, making them more effective for OOD detection. The authors propose a detection method that utilizes K-nearest-neighbor (KNN) searches on mild TTAs instead of InD data, achieving superior performance with just 25 TTAs compared to existing methods that use the entire training set of 1.2 million images on IMAGENET. Additionally, their approach is compatible with various model architectures and demonstrates robustness against adversarial examples.

### Strengths
1. Improved Efficiency: Achieves superior OOD detection with only 25 mild TTAs, reducing computational costs compared to methods using large datasets.

2. Versatile and Robust: Compatible with various model architectures and resilient to adversarial attacks, enhancing reliability.

3. Focus on Testing: Addresses the critical impact of test-time augmentation, leading to more effective OOD detection strategies.

### Weaknesses
1. The article lacks preliminary section.

2. The method designed in the article lacks an overall algorithm description; the current narrative is not clear enough.

3. What OOD score is used in Tables 1 and 2 is not clarified.

4. Can the proposed TTA method adapt to more OOD scores, such as MSP and ASH?

5. Adaptation to other architectures needs corresponding baselines, rather than just reporting the performance of the proposed method.

6. How will it perform on more challenging benchmarks, such as hard OOD detection and pseudo-correlation benchmarks?

### Questions
see Cons

### Soundness
3

### Presentation
3

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
- The author finds that some TTAs, which are the so-called IDA, don't change the feature representation of ID data while they have greater influence on OOD data. Therefore, using these TTAs, each input image is assigned an ID score, i.e., the k-th similarity between the feature of input image and its TTAs counterparts.

### Strengths
- The main idea is easy to follow. 
- The results shown in Table 4 are better than previous methods.
- I would like to raise my rating if the weakness is well tackled.

### Weaknesses
 - The layout needs further improvement. For example, line40, line48, line65-68, and line93-107 are either too crowded or leaving many blank spaces.
- Reference error in Figure 1. The reference style should be corrected as KNN (Sun et.al 2020) and VIM (Wang et.al 2022). Check the remaining parts of your manuscript carefully.
- What's the score represent in Table 1? It looks like the F1-Score.
- Are IDAs stable across different datasets? I noticed the results shown in Table 2 are dataset-dependent. On CIFAR-10, the LPIPS in ascending order is Mask (0.0052)-->Crop (0.0171)-->Hflip (0.048)-->Rotate90 (0.082)-->Gray (0.1184)-->ColorJitter (0.1618)-->Invert (0.2368). On ImageNet, the LPIPS in ascending order is Mask (0.01)-->Crop (0.1425)-->Gray (0.2466)-->Hflip (0.2961)-->ColorJitter (0.4484)-->Invert (0.5656)-->Rotate90 (0.6312).
- The definition of IDA and OODA from line 183 to line 142 is not rigorous. IDA and OODA are identified by the degree of feature changes on a pretrained model. It is important to state that the feature change is measured by a pretrained model instead of our eyes. Otherwise, all TTAs in Table 1 are IDA if the feature change is measured by eyes.

### Questions
- see weakness

### Soundness
3

### Presentation
2

### Contribution
2
