# Distribution Shift-Aware Prediction Refinement for Test-Time Adaptation

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Test-time adaptation (TTA) is an effective approach to mitigate performance degradation of trained models when encountering input distribution shifts at test time.
However, existing TTA methods often suffer significant performance drops when facing additional class distribution shifts. We first analyze TTA methods under label distribution shifts and identify the presence of class-wise confusion patterns commonly observed across different covariate shifts. Based on this observation, we introduce  \textit{label Distribution shift-Aware prediction Refinement for Test-time adaptation (DART)}, a novel TTA method that refines the predictions by focusing on class-wise confusion patterns. DART trains a prediction refinement module during an intermediate time by exposing it to several batches with diverse class distributions using the training dataset. This module is then used during test time to detect and correct class distribution shifts, significantly improving pseudo-label accuracy for test data. Our method exhibits 5-18\% gains in accuracy under label distribution shifts on CIFAR-10C, without any performance degradation when there is no label distribution shift.  Extensive experiments on CIFAR, PACS, OfficeHome, and ImageNet benchmarks demonstrate DART's ability to correct inaccurate predictions caused by test-time distribution shifts. This improvement leads to enhanced performance in existing TTA methods, making DART a valuable plug-in tool.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the poor performance of TTA caused by class distribution shifts. To address this, the authors propose to refines the predictions by focusing on class-wise confusion patterns. Extensive experimental results on CIFAR, PACS, ImageNet benchmarks demonstrate the effectiveness of the proposed method.

### Strengths
1.	The authors conduct a empirical analysis that class distribution shifts would harm the performance.
2.	The authors propose distribution shift-aware module to alleviate the test-time class distribution shifts.

### Weaknesses
1.  In Notation part, why do the test data have labels? In Section 2, the authors calculate the cross-entropy using the test labels $ CE(softmax(f_{\theta}(x)T), y) $. Is it a pseudo label?
2.  The recent work SAR[Towards Stable Test-time Adaptation in Dynamic Wild World] also considers the case with class distribution shifts. What is the advantage of the proposed method over SAR? I found that the authors prepared the imbalanced ImageNet-C dataset following SAR. However, I failed to find the empirical comparisons between the proposed method and SAR.
3.  In my understanding, the authors seek to train a distribution shift-aware module to generate a matrix for prediction refining. In this sense, the data to train such a module should be class-imbalanced. However, as mentioned in the paper, the dataset $D_{int}$ seems to be class-balanced.
4.  What is the computational cost to train a distribution shift-aware module in the “intermediate time”? Does it take a long time?
5.  In the case without class distribution shifts, what is the performance of the proposed method compared with existing methods? Better or worse?

### Questions
If the authors could address my concern, I would raise my scoring.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study examines the impact of label distribution shifts on the test-time adaptation (TTA) methods. The authors first demonstrates how class distribution shifts degrade the performance of BNAdapt, a method that updates Batch Normalization statistics during test time. Particularly, the research found that as class imbalance increased, BNAdapt's performance worsened compared to a NoAdapt approach, which maintains the original training without any modification. The study also highlights consistent confusion patterns among classes during label distribution shifts. To mitigate performance degradation caused by these shifts, the research introduces a distribution shift-aware module that refines classifier predictions by adjusting for detected class distribution changes during test time.  In various benchmarks, DART consistently outperformed existing TTA methods, especially as class imbalance ratios increased

### Strengths
- DART introduces a interesting approach to address class imbalance, presenting a significant improvement over existing TTA methods.
- The comprehensive benchmarks validate DART's superior performance across a range of imbalance ratios.
- The main modules of the proposed method is demonstrated through various ablation studies.

### Weaknesses
 - Using labeled data at intermediate time for training is a recently introduced protocol. However, compared to traditional TTA methods that cannot access labeled data, this approach may not be entirely fair. Test time adaptation, where the model learns directly during the testing phase, might be a more desirable direction.

- The distribution-aware shift matrix for refinement has been frequently employed in handling label-noise datasets (Natarajan et al., 2013; Patrini et al., 2017; Zhu et al., 2021). Although the authors argue that TTA and these tasks differ, TTA essentially involves adding noise to the original data. Therefore, the nature of the problem between TTA and handling label-noise is fundamentally similar. The authors need to further elucidate the methodological distinctions between their proposed approach and existing methods (Natarajan et al., 2013; Patrini et al., 2017; Zhu et al., 2021). Additional considerations should also be clearly addressed.

### Questions
- It would be beneficial if the authors provided a more detailed explanation or key intuition behind the use of averaged pseudo labels as inputs in the distribution shift-aware module during intermediate time.
- I wonder whether T_test is updated on every batch during test time, or if it is constructed just once across the entire test dataset.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on a challenging test-time adaptation setup where both the label shift and covariate shift exist in the testing phase and proposes a novel TTA method, named Distribution shift-Aware prediction Refinement for Test-time adaptation (DART).
In particular, DART refines the predictions made by the trained classifiers by focusing on class-wise confusion patterns, introducing a learnable module to map the class distribution onto the class-to-class matrix.
When combined with many TTA methods like TENT and BNAdapt, DART helps increase the accuracy under both covariate and label distribution shifts at test time.

### Strengths
- this paper is well-written and easy to follow

- the proposed method is simple yet effective and the key idea sounds interesting

- the results on many datasets are impressive

### Weaknesses
 - the results are limited to sever label shifts, while the effectiveness of the proposed method under only covariate shift is not well studied

- could the proposed method be extended to source-free domain adaptation like SHOT (Liang et al., ICML 2020) (more epochs)? More results are welcome to verify the versatility of the proposed method

- concerning the mapping module g_\phi, is the network design (like two-layer MLP or the hidden dimensional) sensitive?

- how about the sensitivity of the batch size $B$ in the proposed method?

### Questions
see the weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
