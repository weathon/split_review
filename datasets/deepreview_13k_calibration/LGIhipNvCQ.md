# TUI: A Conformal Uncertainty Indicator for Continual Test-Time Adaptation

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Continual Test-Time Adaptation (CTTA) addresses the challenge of adapting models to sequentially changing domains during the testing phase. Since no ground truth labels are provided, existing CTTA methods rely on pseudo-labels for self-adaptation. However, CTTA is prone to error accumulation, where incorrect pseudo-labels can negatively impact subsequent model updates. Critically, during testing, a CTTA method can not detect its mistakes, which may then propagate through further adaptations. In this paper, we propose a simple uncertainty indicator called TUI for the CTTA task based on Conformal Prediction (CP), which generates a set of possible labels for each test sample, ensuring that the true label is included within this set with a given coverage probability. Specifically, since domain shifts can undermine the coverage of predictions, making uncertainty estimation less dependable, we propose compensating for coverage by dynamically measuring the domain difference between the target and source domains in continuously changing environments. Moreover, after estimating uncertainty, we separate reliable test pseudo-labels and use them to discriminatively enhance the adaptation process. Empirical results demonstrate that our algorithm effectively estimates the uncertainty for CTTA under a specified coverage probability and improves adaptation performance across various existing CTTA methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to mitigate error accumulation during test-time adaptation (TTA) by reducing the impact of model adaptation when the model prediction is deemed too uncertain. To achieve this, the authors propose storing a portion of the labeled source dataset as a calibration set and introducing TUI, an uncertainty indicator method based on conformal prediction. TUI weights the influence on the training process for each test sample based on this uncertainty.

### Strengths
The proposed method is model-agnostic and can be applied orthogonally to existing CTTA approaches.

### Weaknesses
[W1] Concerns arise regarding the practice of storing and utilizing source data. TTA research operates under realistic assumptions, with related studies avoiding access to training data during testing. In scenarios where training data cannot be accessed due to data privacy issues, how can this limitation be addressed? The paper "Leveraging Proxy of Training Data for Test-Time Adaptation, ICML 2023" suggests utilizing condensed data to leverage training set information while maintaining data privacy in TTA contexts. Could TUI also be applied when employing a proxy for training data, similar to the aforementioned approach?

[W2] Regarding complexity, the use of both a pretrained source model and the testing model may significantly increase time complexity. Additionally, the requirement to forward both the test and calibration data for each sample adds to this complexity. How much time does complexity increase as a result? It's not clear if the calibration data is processed in batches or individually for each test sample, which would drastically affect the computational overhead.

[W3] The corruption benchmark focuses on synthetic domain shifts, which may not reflect realistic scenarios. Validation of the method’s effectiveness on natural domain shift benchmarks is necessary. Does it perform well on natural domain shift benchmarks like VisDA-C and Cityscape-to-ACDC, which have been utilized in prior CTTA research? The VisDA-C dataset, while a domain adaptation benchmark, does not fully capture the nuances of continual test-time adaptation, particularly the error accumulation aspect. Furthermore, the Cityscapes-to-ACDC benchmark, being a segmentation task, introduces a different set of challenges compared to image classification, and it is unclear how the proposed method would extend to pixel-level uncertainty estimation.

[W4] Furthermore, there appears to be insufficient comparison with recent literature. Could the authors provide a comparison with the following works?

- (SAR) Towards stable test-time adaptation in dynamic wild world, ICLR 2023

- (DePT) Visual prompt tuning for test-time domain adaptation

- (VDP) Decorate the newcomers: Visual domain prompt for continual test-time adaptation, AAAI 2023

- (EcoTTA) Ecotta: Memory-efficient continual test-time adaptation via self-distilled regularization, CVPR 2023

- (SVDP) Exploring sparse visual prompt for cross-domain semantic segmentation, AAAI 2024

- Reshaping the online data buffering and organizing mechanism for continual test-time adaptation, ECCV 2024

- A versatile framework for continual test-time domain adaptation: Balancing discriminability and generalizability, CVPR 2024

- (Continual-MAE) Continual-MAE: Adaptive distribution masked autoencoders for continual test-time adaptation, CVPR 2024

- (ViDA) Vida: Homeostatic visual domain adapter for continual test-time adaptation, ICLR 2024

- (BECoTTA) BECoTTA: Input-dependent Online Blending of Experts for Continual Test-time Adaptation, ICML 2024

[W5] Using labeled source data may be perceived as somewhat akin to cheating. Given this, is the observed performance marginal? Is the difference in performance statistically significant?

### Questions
It is unclear whether the calibration set is constructed as a subset of the training set or if it is derived from the validation set of the source dataset. Could the authors clarify which approach is used?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel uncertainty indicator called Test Uncertainty Indicator (TUI) for continuous test time adaptation setting. Based on the existing research in Conformal Prediction Task, the authors point out that the key challenge in CTTA is the continuously changing test domain, which is neglected by the traditional CP methods. In this paper, the authors propose to compute the joint domain shifts and compensate the quantile threshold to obtain the prediction set of the test samples, which is then used to measure the uncertainty. With the help of TUI, several state-of-the-art TTA methods have been demonstrated to achieve significant improvement and better calibration performance on CIFAR10/100-C and ImageNet-C benchmark datasets.

### Strengths
1. The paper is well written and easy to follow. The authors go from introducing the traditional CP methods to the Coverage Gap Issue on CTTA and then introduce a novel solution named TUI. The whole line of thought is very coherent and easy to understand.
2. The evaluation experiments are sufficient and are conducted on several of the most representative CTTA datasets.

### Weaknesses
1. The proposed TUI method relies on maintaining a calibration set consisting of tens or hundreds of source samples, which is a significant limitation in the CTTA setting. The core principle of TTA/CTTA, as highlighted in TENT and CoTTA, is to adapt models to new test distributions without access to source data due to privacy or unavailability concerns. The requirement for a calibration set, even a small one, contradicts this fundamental principle, making the method less practical in real-world scenarios where source data is strictly prohibited.
2. The introduction of hyper-parameters, specifically $\beta$ and $\alpha$, in TUI raises concerns about the method's robustness and ease of use. While $\alpha$ is a standard parameter in conformal prediction, the paper lacks a detailed sensitivity analysis for $\beta$. The authors should provide a more thorough investigation into how different values of $\beta$ affect the performance of TUI, especially in terms of coverage and efficiency. Furthermore, the paper should offer clear guidelines on how to select appropriate values for these hyper-parameters when deploying the algorithm on new, unseen datasets. Without such guidance, the practical applicability of the method is limited.

### Questions
1. Does the notation $\pi(x)$ represent the probabilities from pre-trained model? Since $\pi_{\theta^{src}}(x)$ and $\pi_{\theta^{crt}}(x)$ appearing on the Eq. 4 represent the probabilities from source model and current model, respectively, it's not clear to me which model is used by the presence of $\pi(x)$ alone in equation 7.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the Test Uncertainty Indicator (TUI), a novel method for Continual Test-Time Adaptation (CTTA) that estimates uncertainty in test samples within dynamically changing environments. By leveraging Conformal Prediction (CP), TUI generates prediction sets with a specified coverage probability, enabling models to select genuinely high-confidence samples for adaptation. The authors propose a quantile compensation strategy to address coverage gaps arising from domain shifts, effectively reducing these gaps. Extensive experiments on CIFAR10-C, CIFAR100-C, and ImageNet-C demonstrate that TUI surpasses traditional CP methods in handling uncertainty and adapting to shifting domains.

### Strengths
1. **Clear Problem Identification**: The paper addresses a critical CTTA challenge—error accumulation from pseudo-labeling under domain shifts. It underscores the importance of accurate uncertainty estimation, particularly as most TTA methods rely on self-training.

2. **Effective Uncertainty Estimation with CP**: TUI uses Conformal Prediction to ensure each prediction meets a specified coverage probability. By dynamically adjusting thresholds for domain shifts, it provides a more adaptive and suitable approach for TTA.

3. **Broad Applicability to TTA Methods**: The proposed CPAda uses high-confidence samples for sample-wise adaptation, serving as a versatile, plug-and-play enhancement to various TTA methods, boosting robustness and accuracy.

### Weaknesses
1. **Modest Performance Gain on Error Rate**: While TUI enhances coverage and robustness, its impact on error rate is modest (often less than 1%), which is a crucial metric for TTA. The added complexity and data requirements may not justify these minor gains for some applications. Specifically, the reported error rate improvements are marginal across the various datasets, and it's unclear if these gains are statistically significant given the inherent variability in TTA scenarios. A more rigorous statistical analysis, including confidence intervals, is needed to substantiate these claims. Furthermore, the practical implications of such small error rate reductions need to be more thoroughly discussed, especially considering the computational overhead.

2. **Computational Overhead**: The additional steps in TUI and CPAda, particularly dynamic quantile compensation and uncertainty estimation, increase computational and memory demands, potentially hindering real-time use. Comparative experiments on computational and memory overhead with and without CPAda would strengthen the evaluation. The paper lacks a detailed analysis of the computational cost associated with the conformal prediction framework, including the calibration phase and the online inference. This is a critical oversight, as the practical applicability of the method hinges on its computational efficiency. A breakdown of the time and memory requirements for each component of TUI and CPAda is necessary to assess its feasibility for resource-constrained environments.

3. **Lack of Ablation Study**: The paper does not include an ablation study to isolate the effects of individual TUI components, such as dynamic thresholding, making it difficult to understand the specific impact of each on performance. It is unclear how much each component contributes to the overall performance gain. For instance, it is not clear if the quantile compensation strategy is indeed necessary or if a simpler approach would suffice. An ablation study should systematically remove or modify each component to quantify its contribution to the final results. This would provide a more granular understanding of the method's effectiveness.

4. **Dependency on Additional Calibration Set**: TUI requires an extra calibration set, which may be impractical in real-world applications due to storage limits or privacy constraints. Additionally, it remains unclear if CPAda would outperform methods like EATA and RMT that leverage additional source domain data. The reliance on a separate calibration set raises questions about the method's robustness to the quality and representativeness of this set. The paper does not discuss how the size and diversity of the calibration set affect the performance of TUI. Furthermore, a comparison with methods that utilize source domain data is crucial to understand the trade-offs between the proposed approach and existing techniques.

### Questions
Please refer to **Weaknesses**.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel method, TUI, for estimating uncertainty in Continual Test-Time Adaptation (CTTA) using Conformal Prediction (CP). This approach aims to enhance model adaptation by filtering unreliable pseudo-labels through uncertainty estimation, which is crucial for applications where model predictions must be robust across domain shifts.

### Strengths
1. The application of CP to estimate uncertainty in CTTA is new. Unlike traditional methods that may not handle domain shifts effectively, TUI provides a model-agnostic framework that enhances prediction reliability by including uncertainty measures.
2.  Evaluating both the accuracy and the uncertainty of predictions provides a more comprehensive assessment of model performance in test-time adaptation scenarios. This dual approach is crucial for understanding the practical utility of TUI in real-world applications.

### Weaknesses
 1. (**major**)The experimental comparison includes only a few methods like Tent, CoTTA, SATA, RMT, and C-CoTTA. Recent advancements in CTTA such as [1-3] in recent publications are not considered. This omission may raise concerns about whether TUI can maintain its performance advantages when compared to the latest methods.
2. (**minor**) TUI's requirement for labeled source data for its calibration set may limit its applicability in real-world scenarios where such data is unavailable or impractical to use such as CLIP. (**major**) This limitation also complicates direct comparisons with other CTTA methods that do not use source domain knowledge, potentially skewing the fairness of these comparisons .
3. (**major**)The paper claims that the TUI-guided adaptation method (CPAda) improves accuracy and reduces uncertainty. However, the evidence provided across three datasets and various settings (different alpha values) does not consistently support these claims. Notably, clear improvement is observed only when CPAda is applied to Tent on CIFAR100. In contrast, other applications show minimal or no benefits—for instance, when CPAda is applied to CoTTA and C-CoTTA on CIFAR100, as well as CoTTA, SATA, and C-CoTTA on CIFAR10, not only do the accuracy improvements lack significance, but all three uncertainty metrics (NLL, BS, ECE) actually increase. 
4. (**minor**) The paper does not provide an analysis of the computational efficiency of the TUI-guided method (CPAda), which is crucial given the computational demands of TTA methods. For each incoming batch, TUI requires that the forward process be conducted on the new batch and calibration dataset with both the original source model and adapted model. This quadruples the computational load compared to simpler methods like CoTTA, which does not require multiple forward passes per batch. This lack of information makes it difficult to assess the practicality of deploying TUI in environments where resources are constrained or efficiency is a critical factor. 

### Questions
1. A grammar error in line 310.
2. What are the deinitions of $s(y|\pi(x))$ in formula (9) and $C(x)$ in formula (14)?
3. Can you clarify the design behind formula (4), where the dimensionality doubles the number of labels? How to interpret the derived probablities? Could the order of operations be altered, for instance, concatenating after applying the softmax? 
4. The sentence from lines 461-464 is confusing, as it mentions good coverage paired with high inefficiency in the first point, contradicting the claim of excellent inefficiency but low coverage in the second point.
5. Could you provide more details on how to interpret the metrics COV and INE? How to interpret these two metrics? How are these metrics related to the performance and uncertainty assessments in the CTTA model?

### Soundness
2

### Presentation
2

### Contribution
2
