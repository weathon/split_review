# TULiP: Test-time Uncertainty Estimation via Linearization and Weight Perturbation

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
A reliable uncertainty estimation method is the foundation of many modern out-of-distribution (OOD) detectors, which are critical for safe deployments of deep learning models in the open world. In this work, we propose TULiP, a novel, theoretically-driven, post-hoc uncertainty estimator for OOD detection. Our method considers a hypothetical perturbation applied to the network prior to convergence. Based on linearized training dynamics, we bound the effect of such perturbation, resulting in an uncertainty score computable by perturbing model parameters. Ultimately, our approach computes uncertainty from a set of sampled predictions, thus not limited to classification problems. We visualize our bound on synthetic regression and classification datasets. Furthermore, we demonstrate the effectiveness of TULiP using large-scale OOD detection benchmarks for image classification. Our method exhibits state-of-the-art performance, particularly for near-distribution samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a test-time post-hoc OOD detection method, which is theoretically driven by considering hypothetical perturbations applied to model parameters before convergence, allowing for the computation of an uncertainty score. The overall idea is interesting. However, there are a few points to be clarified.

### Strengths
This paper is overall well-written. The idea is theoretically driven and offers good interpretability. The method is thoroughly evaluated and demonstrates excellent performance compared to many OOD detection methods.

### Weaknesses
1.What's the motivation for calculating the upperbound of variations for uncertainty quantification? As shown in Eq 1. The objective is to estimate the variance given an different parameters initializations. To solve this, the DNN is first linearized locally with the NTK theory and the upperbound for introducing the changes are calculated with the NTK theory.  The paradox is if the parameters can be already be perturbed, why NTK is needed for calculating the upperbound. Besides, calculating the upperbound will bring biased estimations of uncertainty. Another simple way to achieve this might be directly apply random perturbations to the network parameters (like random noises injection, dropout parameters), can easily get ensemble of neural network parameters. What is the advantage over these methods?

2. Given that $\lambda \in{\{\sqrt{o}, 3 \sqrt{o}\}\}$, where $o$ represents the number of output dimensions, why does Figure 4 only explore the range of $\lambda$ values between 0 and 3 on ImageNet-200? The authors should consider exploring a broader range of this hyperparameter.

3. The authors mention that TULiP is over three times faster than ViM, noting that ViM takes more than 30 minutes just to extract ID information on a recent GPU machine. However, it appears that the proposed method requires $M=10$ forward passes per sample for OOD detection. Compared to classic OOD detectors like EBO, does this imply that the detection speed of the proposed method is relatively slower?

4. In the experiments, the authors calculated Equation 8 using 256 samples from the ID dataset (ImageNet-1K) and 128 samples per OOD dataset. However, the authors do not clarify how these 256 ID samples and 128 OOD samples were selected or whether OOD samples align with test samples. Additionally, did the authors know beforehand which samples were ID and OOD when using these samples?

6. Have the authors considered the impact of different types of OOD data? For example, have the authors considered situations where OOD data is very far from ID data to improve detection of far-OOD.

7.Why can Equation 11 be approximated by this way proposed by the authors? This approximation ($\nabla_{\boldsymbol{\theta}} f_T^{emp}(\boldsymbol{z}) \boldsymbol{\Gamma} \approx \nabla_{\boldsymbol{\theta}} f(\boldsymbol{z})$) only considers the impact of params in each layer and does not account for the effect of the order of layers with the same params in network. Figure 1: a) Although it presents training trajectories under different params, it does not indicate which specific layer each color represents. The authors should conduct more experiments and theoretical analyses to explore this aspect.

### Questions
See weakness.

### Soundness
2

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
This paper proposes a novel uncertainty estimation method TULiP for OOD detection. The core idea of the paper is to generate uncertainty scores by perturbing model parameters based on linearized training dynamics.

### Strengths
* The paper is clearly written and experiments have been extensively conducted across a set of diverse datasets.

* Theoretical analysis is thorough.

### Weaknesses
 * There are so many hyperparameters that implementing the method in realistic scenario may have some difficulties.

* Performance on far OOD is not good enough.

### Questions
How does the performance compared to deep ensembles[1]？ 

[1] Simple and scalable predictive uncertainty estimation using deep ensembles

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
4

### Summary
This work introduces TULIP (Test-time Uncertainty by Linearized fluctuations via weight Perturbation), a post-hoc out-of-distribution (OoD) score that leverages the epistemic uncertainty of a trained network. Grounded in the theoretical framework of linearized training dynamics, TULIP demonstrates effectiveness in detecting both semantic-shift and covariate-shift OoD scenarios.

### Strengths
- This work proposes an uncertainty-based score to detect both semantic-shift OOD and covariate-shift OOD without accessing the training data.  
- The derivation of the proposed bound for ||f_T(x)-\hat{f}_T(x)|| and its upper bound are written down thoroughly.

### Weaknesses
 - Line 018: Could the authors clarify what is meant by “other problem settings”?

- Connection Between Concepts (Line72-73): The relationship between semantic shift and covariate shift in Out-of-Distribution (OOD) detection and epistemic uncertainty is not clearly motivated [1].  Could the authors provide further elaboration on this connection?
- Post-hoc OOD Detectors: The related work section appears somewhat outdated and incomplete. A notable aspect of TULiP is its ability to perform OOD detection without access to the training data, which aligns it with post-hoc detection methods. Additionally, TuLiP addresses both semantic-shift and covariate-shift OOD detection. Therefore, the related work should be expanded to include recent studies on post-hoc detectors for semantic-shift OOD [2] and covariate-shift OOD [3], respectively.

- Clarity of the Paper: The overall clarity of the paper could be improved. For instance, the section on the theoretical framework (particularly sections 3.1 and 3.2) could be condensed, as it does not represent a primary contribution of this work.

- The discussion on the bound for the ||f_T(x)-\hat{f}_T(x)|| and its upper bound is appreciated. However, the implementation section (Section 4) is somewhat unclear. For example, the “early checkpoint” in Algorithm 1 is set to zero by default (Line 376), though it is marked as optional. Additionally, the OOD score is based on Shannon entropy, which has been explored previously in [2]. The primary difference appears to be that [2] directly utilizes the predictive distribution from a trained network, whereas TULiP relies on perturbed predictions.

- Performance on ImageNet-1k: When evaluating OOD detection on large-scale benchmarks using ImageNet-1k as the in-distribution data, the method’s performance in terms of AUROC and FPR95 is worse than ASH (see Table 1). This discrepancy raises questions about the claim in the abstract regarding TULiP achieving state-of-the-art (SOTA) performance. Additionally, a discussion on why performance degrades with ImageNet-1k as the in-distribution data would be helpful.

- Optional Suggestion for Table 1: For improved readability, Table 1 could be divided into two sections: one for methods that do not require training data access, and another for those that do.

- Additional Architectures: Testing on alternative architectures, such as BiT [4] and ViT [5], would further demonstrate the robustness and effectiveness of the proposed approach. The current evaluation is limited to convolutional neural networks, and it is unclear if the method would generalize to other architectures, particularly transformer-based models which have become increasingly popular in computer vision.

- Results on Table 2: It seems inappropriate to compare methods designed specifically for semantic-shift OOD detection, as the current task focuses on covariate-shift OOD detection.  Additionally, could the authors clarify the metric reported in Table 2?  The purpose of TULiP is somewhat ambiguous—whether it aims to detect covariate-shift OOD samples or to demonstrate robustness against them. If the latter is the case, a fairer comparison would be with methods developed explicitly for covariate-shift OOD samples, such as [3].

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2
