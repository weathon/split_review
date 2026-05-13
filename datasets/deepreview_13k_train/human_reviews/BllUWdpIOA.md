# Continual Momentum Filtering on Parameter Space for Online Test-time Adaptation

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Deep neural networks (DNNs) have revolutionized tasks such as image classification and speech recognition but often falter when training and test data diverge in distribution. External factors, from weather effects on images to varied speech environments, can cause this discrepancy, compromising DNN performance. Online test-time adaptation (OTTA) methods present a promising solution, recalibrating models in real-time during the test stage without requiring historical data. However, the OTTA paradigm is imperfect, often falling prey to issues such as catastrophic forgetting due to its reliance on noisy, self-trained predictions. Although some contemporary strategies mitigate this by tying adaptations to the static source model, this restricts model flexibility. This paper introduces a continual momentum filtering (CMF) framework, leveraging the Kalman filter (KF) to strike a balance between model adaptability and information retention. The CMF intertwines optimization via stochastic gradient descent with a KF-based inference process. This methodology not only aids in averting catastrophic forgetting but also provides high adaptability to shifting data distributions. We validate our framework on various OTTA scenarios and real-world situations regarding covariate and label shifts, and the CMF consistently shows superior performance compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes parameter averaging/filtering for online test-time adaptation. The idea is to first find the task minimum, and then use the previous task to form a “prior” and average the parameters. The actual algorithm can be thought of as a simplified version of the Kalman filtering algorithm but they do not consider the full covariance because of high dimensionality. The paper shows the algorithm’s effectiveness on online test-time adaptation, where a full network has been pretrained and only normalization parameters are “adapted” to each task, where different tasks exhibit distribution shift on image styles and textures or speech environments.

### Strengths
- The proposed methodology is properly derived from a Kalman filter algorithm and has probabilistic interpretations.
- The proposed methodology can be adapted and simplified to a deep network where only normalization parameters are changing.
- Empirically, the proposed method can be applied on various backbone networks and achieve strong results on online test-time adaptation.

### Weaknesses
 - The proposed method seems to work for online test-time adaptation which requires a well trained network. It would be good to investigate whether this could be a limitation. It would be good to understand whether it relies on a pretrained network or the continual style of training can also extend to a network from scratch. It would also be good to understand the limitation on the number of adaptation parameters and the number of tasks it can continually learn without forgetting. When does the method break down? Since the methodology is a general one, it would be good to understand its general characteristics. To this end, I would appreciate to see some toy experiments on parameter averaging that answers these questions.

- It would be good to study on the sensitivity of each hyperparameter.

### Questions
See above comments.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the  Online Test-time Adaptation (OTTA) by applying the Kalman filter to infer the test-time "model parameters". The proposed method is evaluated over various datasets.

### Strengths
- Casting the OTTA challenge as a Bayesian filtering issue presents an interesting approach. The incorporation of the Kalman filter (KF) to facilitate this is noteworthy, as it offers a closed-form solution for posterior inference. However, the inherent linear assumption of the KF may not align well with many real-world scenarios.

- The research commendably evaluates the proposed method across a spectrum of image classification and speech recognition tasks, and the results indicate reasonable enhancements.

### Weaknesses
 - Utilizing the Kalman filter for sequential model parameter inference might not be optimal given its inherent assumptions. The Kalman filter operates under the presumption of linear system dynamics and posits a Gaussian distribution for the posterior. This is often misaligned with real-world scenarios where state posteriors frequently exhibit multimodal distributions.

 - While the exploration of the Kalman filter and other Bayesian filtering techniques for model adaptation/TTA is not entirely novel, it is crucial to delineate this work from previous contributions. It's recommended to rigorously compare, both theoretically and empirically, with established works like EKF[1] and PFDE[2]. Such a comparative analysis can better spotlight this paper's unique technical contributions.

 - In Section 3.4, the paper discusses simplifying Bayesian filtering computations. An analysis evaluating the accuracy of these approximations is warranted.

### Questions
See weakness.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel framework called Continual Momentum Filtering (CMF) that leverages the Kalman Filter to strike a balance between model adaptability and information retention. The CMF framework alleviates the catastrophic forgetting issue and provides high adaptability to shifting data distributions. The paper provides examples of real-world situations where the CMF framework has been validated, including scenarios involving covariate and label shifts in speech recognition tasks and ImageNet-C. The results show that the CMF consistently outperforms state-of-the-art methods.

### Strengths
The investigated problem, namely adaptability and anti-forgetting tradeoff, is practical for the real-world deployment of TTA methods. The resulting CMF framework is simple yet effective. 

Experimental evaluations on various models, datasets and scenarios are thorough and demonstrate the effectiveness of the proposed framework.

### Weaknesses
The performance gains compared with ROID are a bit marginal.

### Questions
Are there any sensitivity analyses regarding the parameter $I$ in algorithm 1?

I am curious about the performance of replacing the “weight ensemble” in ROID with CMF？ (namely ROID with CMF).

How about the performance of “DW-SLR + SCE” without CMF?

How about the in-distribution performance of compared methods after the adaptation of out-of-distribution data? Please refer to the comparison manner proposed in EATA.

Could the authors provide a computational complexity (wall-clock GPU time) comparison regarding the proposed CMF? 

Could CMF help MEMO work stably in the online setting? 

More motivation/explanations from the high level about why CMF could achieve a better tradeoff between adaptability and information retention are preferred.

Could the authors provide implementation details (hyperparameters) of baselines on different models and datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on online test time adaptation and introduces a Kalman Filter (KF) based approach on momentum filtering of DNNs.  The proposed method, referred to as CMF,  integrates a SGD-based optimization process with a KF-based inference (filtering) process. Some simplification techniques, such as momentum smoothing, have been employed to reduce time complexity. The experimental results demonstrate the competitiveness of the proposed method across multiple datasets.

### Strengths
The paper studies a practical and important problem: online test-time adaptation, focusing on mitigating catastrophic forgetting during adaptation.

The proposed method, which employs a KF-based approach to filter the momentum parameter of DNNs, provides a sound solution to mitigate catastrophic forgetting in online test-time adaptation.

Overall, the paper is well-structured and effectively communicates the details of the proposed method.

Furthermore, in the experimental evaluation, the proposed method demonstrates superior performance compared to previous approaches, as reported in the paper.

### Weaknesses
1) This paper could benefit from a comparison with related works that utilize the Kalman filter for online adaptation tasks, as seen in [1,2].  Such a comparison or discussion regarding the difference between the proposed method and [1,2] would be beneficial.

2) It is very common to use replay-based approaches to overcome catastrophic forgetting, such as ER [3] and A-GEM [4].  An analysis of the advantages and disadvantages of the proposed approach in contrast to replay-based methods would provide a more comprehensive understanding of how it addresses the issue of catastrophic forgetting.

3) In the alation study on “Effectiveness of the source-conjugated transition model”, do the hyperparameters alpha and gamma remain the same? It is better to explore the effects of hyperparameters alpha and gamma individually. Since the roles of alpha and gamma are distinct and independent, isolating their impact would provide a more detailed understanding.

4) The paper simplifies the inference process by using scalar parameters to replace matrix parameters in the KF process. It would be helpful to conduct an experiment on a smaller model to compare the performance of the simplified version with the original matrix version of the method.

### Questions
1) How does the proposed method compare to related Kalman filter-based techniques for adaptation, as discussed in [1,2]?

2) What are the advantages and disadvantages of the proposed approach in contrast to replay-based methods [3,4] for mitigating catastrophic forgetting?

3) In the alation study on “Effectiveness of the source-conjugated transition model”, do the hyperparameters alpha and gamma remain the same? It is better to explore the effects of hyperparameters alpha and gamma individually. 

4) What is the performance and computational cost comparison between the simplified scalar version of the KF process and the original matrix version of the KF process?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
