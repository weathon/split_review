# Optimizing Calibration by Gaining Aware of Prediction Correctness

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Model calibration aims to align confidence with prediction correctness.
The Cross-Entropy (CE) loss is widely used for calibrator training, which enforces the model to increase confidence on the ground truth class. However, we find the CE loss has intrinsic limitations. For example, for a narrow misclassification, a calibrator trained by the CE loss often produces high confidence on the wrongly predicted class (\eg, a test sample is wrongly classified and its softmax score on the ground truth class is around 0.4), which is undesirable. In this paper, we propose a new post-hoc calibration objective derived from the aim of calibration. Intuitively, the proposed objective function asks that the calibrator decrease model confidence on wrongly predicted samples and increase confidence on correctly predicted samples. 
Because a sample itself has insufficient ability to indicate correctness, we use its transformed versions (\eg, rotated, greyscaled and color-jittered) during calibrator training. 
Trained on an in-distribution validation set and tested with isolated, individual test samples, 
our method achieves competitive calibration performance on both in-distribution and out-of-distribution test sets compared with the state of the art.
Further, our analysis points out the difference between our method and commonly used objectives such as CE loss and mean square error loss, where the latters sometimes deviates from the calibration aim.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces two innovative methods to address calibration errors in deep learning predictions: a correctness-aware loss function and a sample transformation technique. The correctness-aware loss function aims to directly minimize calibration error, effectively improving the calibration of misclassified samples by narrowing discrepancies across all classes. Additionally, to boost cross-domain performance, an augmentation-based transformation is applied to calibration samples, enhancing robustness across varied domains. Both methods are implemented in a post-hoc calibration framework, and the proposed algorithm demonstrates state-of-the-art performance, particularly in cross-domain settings.

### Strengths
This paper presents a range of validation scenarios to assess the effectiveness of the proposed framework. In numerous cases, the framework achieves state-of-the-art performance, validating the impact of its two novel schemes. The experimental setup and comparisons are thoughtfully designed, with detailed descriptions that enhance clarity and reproducibility. Mathematical derivations are presented comprehensively, and the overall narrative is organized in a way that makes the framework easy to follow and understand, emphasizing key components effectively.

### Weaknesses
The paper has several strengths, yet I have some specific concerns that warrant attention:

1. Definition of "Narrow Misclassification":
The term "narrow misclassification" appears in the abstract, and the correctness-aware (CA) loss is presented as targeting this condition by adjusting predictions across different classes rather than solely reducing confidence in the incorrect class. However, a clear definition of "narrow misclassification" is missing, and it’s challenging to discern how it differs from absolutely wrong samples even after reviewing the derivations. Clear definitions and empirical analysis based on outcomes would help clarify this distinction. Specifically, it is unclear if a 'narrow misclassification' refers to a sample where the predicted probability for the incorrect class is only slightly higher than the true class, or if it encompasses a broader range of misclassifications where the probabilities are close across multiple classes. This ambiguity makes it difficult to understand the precise problem the CA loss aims to solve.

2. Limitations from Augmentation Types Used:
The transformation component uses augmentations, but it lacks an analysis of how different types of augmentation affect performance across domains. Depending on the augmentation type, the efficacy in cross-domain scenarios may vary. Experimental validation or analysis is needed to determine the diversity of augmentation types required or which specific augmentations are essential. For instance, it's not clear if augmentations like color jittering, rotations, or cropping contribute equally to the robustness, or if certain augmentations are more beneficial for specific types of domain shifts. Without this analysis, it's hard to justify the choice of augmentations used.

3. Similarity with Temperature Scaling:
If the framework were designed with temperature scaling, where the temperature parameter is shared across all classes, it could similarly distribute confidence across classes rather than reducing only the incorrect class's confidence. This raises questions about the uniqueness of the proposed algorithm’s approach in addressing "narrow misclassification." It is not clear how the proposed method's adjustment of logits differs fundamentally from a temperature scaling approach that also redistributes confidence across all classes, potentially achieving a similar effect without the added complexity of the CA loss.

4. Derivation for the CA Loss Function:
The derivation of the CA loss function appears to be unnecessarily complex. Initially, the paper emphasizes the use of continuous calibration error rather than Expected Calibration Error (ECE), suggesting a different approach. However, the final derivation seems equivalent to ECE-based loss, assuming discrete samples and small sample sizes, which undermines the rationale for a continuous assumption. Clarification is needed on why continuous assumptions were initially made if the final derivation closely resembles an ECE-based approach. The transition from a continuous formulation to a discrete one is not well-justified, and it's unclear what advantages the continuous formulation provides if the final loss is essentially a discrete approximation.

5. Bounds of the CA Loss:
Bounds for the CA loss are derived based on assumptions that the sample sizes and accuracy across classes are similar. However, the significance of these bounds remains unclear, as they appear merely descriptive of the assumed conditions. Additional insights or generalized bounds demonstrating reduced CE loss could improve understanding. The bounds, as presented, do not offer any practical insights into the behavior of the loss function or its convergence properties, and it's not clear how these bounds help in understanding the effectiveness of the CA loss.

6. Unclear Derivation in Equation 15:
The derivation in Equation 15 is ambiguous due to an unexplained arrow, which might imply a limit. Clarification on which parameter converges to produce this outcome is necessary to improve the transparency of this mathematical derivation. The lack of explanation for the arrow makes it difficult to follow the mathematical reasoning and understand the convergence behavior of the loss function.

7. Parameter \theta in Equation 19:
It is unclear if \theta in Equation 19 exclusively refers to the fully connected layers added for post-hoc calibration. This specification is important for clarity. Without a clear definition, it's difficult to understand the scope and impact of the parameter \theta in the overall calibration process.

8. Synergy between CA Loss and Transformation Component:
The CA loss reduces ECE, while the transformation improves cross-domain robustness. However, the synergy between these components is unclear, as seen in experimental results: applying CA loss significantly reduces ECE, while the transformation tends to increase ECE, showing a trade-off rather than synergy. Clarification is needed on why these mechanisms must be combined rather than sequentially applied as separate approaches. The experimental results suggest that the two components may be working at cross-purposes, and it's not clear why they should be combined if they do not consistently improve calibration together.

9. Baseline (CE Only + PTS) Already Achieving State-of-the-Art Performance:
In the result tables, the baseline (CE Only + PTS) already achieves state-of-the-art ECE and accuracy in multiple scenarios. While adding CA and transformation components improves performance further, it seems that these improvements are achieved largely because of the baseline's strong performance. To mitigate this concern, I recommend testing the proposed algorithm on alternative baselines. The incremental improvements over a strong baseline are not substantial enough to justify the complexity of the proposed method, and it's important to evaluate the method's performance against a wider range of baselines.

10. Minor Points:
    - The text in figures is too small, making them hard to read.
    - Typo: Line 136, “samples'.” should be “samples.'”

### Questions
Why does the paper initially emphasize using a continuous calibration error instead of the Expected Calibration Error (ECE)?

What is the intended synergy between the CA loss and the transformation component, given their distinct purposes of reducing ECE and enhancing cross-domain robustness?

Could the proposed algorithm’s effectiveness be validated further by testing it on alternative baselines?

### Soundness
3

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
The paper describes a method for post-hoc calibration of a classifier based on estimating  for each sample a scaling temperature on the output logits(sample-adaptive calibration strategy). Test time data augmentation is used to predict the scaling temperature and relies on a complementary network taking as input the softmax of selected transformed images and minimizes what is called a correctness-aware loss. The loss is justified by a better management of narrowly wrong predictions. The strategy is evaluated on several small to mid-size datasets and 10 networks per dataset.

### Strengths
- The idea of using test-time augmentation to predict a sample based temperature scaling factor and learning a network for predicting such temperature is novel, as far as I know.

- The justification of the loss on a toy example pointing out its behavior on so-called narrowly wrong samples is intuitive.

- Rather extensive experiments on several types of image datasets show the benefit of the approach over standard calibration methods and other optimization losses.

### Weaknesses
 - The goal of the formal development (Section 3.2) is not clear: what is it supposed to show? Is it to prove that the empirical criterion (7) is a good proxy for optimizing (3), given that $\hat{c}$ is produced by the calibration pipeline of Figure 2? If so, I am not convinced that the formal developments of Section 3.2 actually prove this. The connection between the theoretical objective (3) and the empirical loss (7) is not rigorously established. Specifically, the derivation relies on a series of approximations, such as replacing the true conditional distribution with a Dirac delta function-based empirical distribution and approximating the conditional accuracy with a single sample. These approximations, while practical, lack a clear justification in terms of their impact on the calibration objective. The paper does not provide a clear analysis of the error introduced by these approximations, nor does it discuss the conditions under which these approximations are valid. The claim that the empirical criterion is a sound proxy for the theoretical calibration error is not sufficiently supported by the mathematical formulation.

- The writing lacks precision (see my first question, same symbol $E_f^{emp}$ but different concepts for instance). The use of the same symbol $E_f^{emp}$ to represent different concepts at various stages of the derivation is confusing and obscures the logical flow. It is unclear how the different forms of $E_f^{emp}$ relate to each other and to the overall calibration objective. For example, the transition from the expectation in equation (5) to the sample-based approximation in equation (6) is not clearly explained, and the mathematical validity of this step is questionable. The lack of clear definitions and distinctions between these concepts makes it difficult to follow the argument and assess its validity.

- The data augmentation is justified by the fact "that consistency in model predictions for transformed images correlates strongly with accuracy" (l. 261): if I can agree with this law, I don't clearly see where it applies in your framework. Or is it that by introducing some local perturbation of the data through transformations and measuring the variation in confidence scores, one can infer accuracy?  Then why not directly predict the confidence instead of a temperature? The paper does not adequately explain how the consistency of model predictions for transformed images is leveraged to improve calibration. The connection between data augmentation and the predicted temperature is not clear. The paper suggests that the variation in confidence scores across transformed images can be used to infer accuracy, but it does not explain why this is the case. Furthermore, if the goal is to infer accuracy, it is not clear why the method predicts a temperature instead of directly predicting the confidence score.

- In general, I have difficulty understanding the conceptual connections between the test time data augmentation, the formal development, and the narrowly wrong sample analysis. The global logic of the writing is hard to follow. The paper lacks a clear narrative that connects the different components of the proposed method. The formal development, the data augmentation strategy, and the narrowly wrong sample analysis seem disconnected, and it is not clear how they contribute to the overall goal of improving calibration. The paper does not provide a clear explanation of how these different aspects of the method work together to achieve better calibration.

### Questions
- What is the difference between CA only and CA trans.? Is CA only the calibration strategy that estimates the calibrator $g$ from the calibration set using the loss of Eq. (7) and no data augmentation? This is not clear.

- The approach focuses on calibration of the maximum confidence: can the strategy be adapted to calibrate the whole confidence vector (multiclass calibration)?

### Soundness
2

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
The paper addresses the issue of model calibration in machine learning, specifically aiming to align a model's confidence with its prediction correctness. The authors identify limitations with the commonly used Cross-Entropy loss for calibrator training and propose a new post-hoc calibration objective, the Correctness-Aware loss. This objective function is designed to decrease model confidence on wrongly predicted samples and increase it on correctly predicted ones. The method utilizes transformed versions of samples to train the calibrator and is tested on both IND and OOD datasets. The paper claims that their method achieves competitive calibration performance compared to state-of-the-art techniques and provides a better separation of correct and incorrect test samples based on calibrated confidence.

### Strengths
**Novel Calibration Objective:** The paper introduces a new loss function, CA loss, which is a significant contribution to the field of model calibration. This loss function is intuitively designed to align with the goal of calibration, which is to ensure high confidence for correct predictions and low confidence for incorrect ones.

**Empirical Evidence:** The authors provide extensive experimental results demonstrating the effectiveness of their proposed method across various datasets, including IND and OOD test sets. The consistent performance improvement over uncalibrated models and other calibration techniques is a strong point.

**Theoretical Insights:** The paper not only proposes a new method but also provides theoretical insights into why existing methods like CE and MSE losses are limited, particularly for certain types of samples in the calibration set.

### Weaknesses
 **Dependency on Transformations:** The effectiveness of the CA loss relies on the use of transformed images to infer correctness. If these transformations do not adequately capture the characteristics of correct and incorrect predictions, the calibration might be less effective. Specifically, the transformations used, such as rotations or color jittering, might not always induce a change in the model's prediction behavior that is indicative of the true correctness. For instance, a slightly rotated image might still be correctly classified, while a more significant distortion could lead to a misclassification, but the boundary between these two is not always clear and consistent across different image types or model architectures. 

**Transfomations lack of theoretics:** While the use of transformations such as rotation, grayscale, color jittering, and others has proven to be effective in practice; however, the choice of transformations and their number in Fig. 4 are currently guided more by empirical results rather than a theoretical framework that explains why these five transformations should correlate with prediction correctness as so many transformation exists. And the paper also does not provide a theoretical basis for which transformations are the most informative for calibration or how to select the optimal set of transformations. The current approach might be seen as somewhat arbitrary, and the effectiveness could be dependent on the specific characteristics of the dataset and the model architecture. And There is a risk that the calibrator might overfit to the specific transformations used during training, which may not generalize well to real-world variations in data that were not captured by the training transformations



### Questions
1. See above weakness

2. What is the core difference between calibration and misclassification (e.g. [R1]), both of them seem to be focusing on the incorrect predictions.

3. Fig. 6  illustrates the impact of ablating the top-k selection on the CA loss. The figure suggests that increasing k beyond 4 leads to a significant decline in performance. This trend raises questions about the potential effects of even higher values of k, such as 100 or 200, particularly in datasets like ImageNet. Additionally, since the authors have chosen k=4 as the default setting, it is important to consider how the model manages scenarios where the correct prediction is not included among the top-4 predictions.

4. The method involves training a calibrator with a new loss function and using transformed images, which could be more complex to implement compared to simpler calibration techniques.

 [R1]  Zhu, Fei, et al. "Openmix: Exploring outlier samples for misclassification detection." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

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
4

### Summary
The paper undertakes the problem of calibrating deep neural networks for the task of classification. At the core of the method is a past-hoc calibrator which proposes a correctness-aware loss to search for the optimal temperature which is then used to scale the logits for a given sample. To determine the correctness of a sample, the method uses the well-known concept of consistency across different augmentations. A simple network is used to map top-K softmax predictions across augmentations to the temperature value. The correctness-aware loss optimizes this network to obtain the best temperature. The paper also shows mathematical insights on the proposed loss. The experiments have been conducted on different datasets to validate the effectiveness of the post-hoc calibrator. Results claim to achieve competitive performance against other post-hoc calibration methods, such as naive temperature scaling, ensemble temperature scaling, adaptive temperature scaling and isotonic regression.

### Strengths
**1**) Calibrating deep neural networks is an important step towards making AI models reliable and trustworthy, especially in safety-critical applications.

**2**) The proposed post-hoc calibrator is simple as it also learns to identify a per-sample temperature value that can be used to scale the logits.

**3**) The paper also mentions some theoretical insights into the proposed correctness-aware loss term by comparing and contrasting it with CE and MSE losses.

**4**) Results show that proposed idea is competitive against other post-hoc calibration methods.

### Weaknesses
 **1**) The related work section completely misses an emerging direction of train-time calibration methods such as [A], [B], [C],  [D],  [E] and [F]. 

**2**) The paper lacks reliability diagrams to better understand the potential of proposed post-hoc calibrator in overcoming overconfidence and under confidence over the full spectrum of model confidence. Furthermore, the reliability diagrams should compare against stronger post-hoc baselines such as MIR or ProCal, not just the uncalibrated model.

**3**) Why the proposed post-hoc calibrator is able to improve OOD calibration performance? There is no analyses that supports these results.

**4**) How the proposed post-hoc calibrator would perform under class-imbalanced scenarios?

**5**) The proposed correctness-aware loss appears similar to MDCA loss [C]. What are the key differences?



### Questions
**1**)  What are the key differences with MDCA loss [C] and DCA loss [G] ? I would like to see concrete differences between them.

**2**)  Can MDCA loss and/or DCA loss be used in place of correctness-aware loss to obtain optimal temperature value? Beyond, CE and MSE losses, I believe it would be an interesting comparison between the effectiveness of proposed CA loss and these losses

**3**)  Is the post-hoc calibrator capable of calibrating non-ground truth classes as well?

**4**) What is the performance of the method under the SCE metric [H] compared to other post-hoc calibration methods? 

**5**) The intuition behind learning a mapping through g network from top-K softmax scores (corresponding to transformed versions) to temperature value is not very clear. 

**6**) L499: The paper mentions that existing methods do not improve AuC compared to proposed one. Will require more explanation.

**7**) How good is the method in overcoming under confidence of the model?

**8**) Can this post-hoc calibrator be used after a train-time calibration method? It would be interesting to observe the complementary strengths of the proposed post-hoc calibration method.

### Soundness
3

### Presentation
2

### Contribution
2
