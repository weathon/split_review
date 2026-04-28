# Embarrassingly Simple Dataset Distillation

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Dataset distillation extracts a small set of synthetic training samples from a large dataset with the goal of achieving competitive performance on test data when trained on this sample. In this work, we tackle dataset distillation at its core by treating it directly as a bilevel optimization problem. Re-examining the foundational back-propagation through time method, we study the pronounced variance in the gradients, computational burden, and long-term dependencies. We introduce an improved method: Random Truncated Backpropagation Through Time (RaT-BPTT) to address them. RaT-BPTT incorporates a truncation coupled with a random window, effectively stabilizing the gradients and speeding up the optimization while covering long dependencies. This allows us to establish new state-of-the-art for a variety of standard dataset benchmarks. A deeper dive into the nature of distilled data unveils pronounced intercorrelation. In particular, subsets of distilled datasets tend to exhibit much worse performance than directly distilled smaller datasets of the same size. Leveraging RaT-BPTT, we devise a boosting mechanism that generates distilled datasets that contain subsets with near optimal performance across different data budgets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Random Truncated BPTT (RaT-BPTT) for solving the bi-level optimization problem in dataset distillation. RaT-BPTT incorporates a truncation coupled with a random window, effectively stabilizing the gradients and speeding up the optimization while covering long dependencies. Empirical results show that such simple method outperforms existing methods for dataset distillation application.

### Strengths
- The idea is simple and easily applicable in practice
- The empirical results are positive

### Weaknesses
 - No theoretical results supporting the empirical results. Analyzing the bi-level optimization problem might be difficult in general, but it is better to find some simple setting where theory can explain when/why the proposed method outperforms existing methods.


### Questions
Is the proposed algorithm applicable for general bi-level optimization problems, not only for the dataset distillation application? If so, it would be great to add some discussions on what other applications using bi-level optimization (which currently use BPTT) one can use RaT-BPTT instead.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes three key changes to the meta-matching framework of data distillation: (1) randomly truncated backpropagation through time (BPTT); (2) boosting in data distillation; and (3) using Adam optimizer in the inner-loop (although the authors don’t state this as a primary difference). These changes lead to SoTA results on numerous image classification datasets, especially compared to the naive meta-matching algorithm [1].

[1] Zhiwei Deng and Olga Russakovsky. Remember the past: Distilling datasets into addressable memories for neural networks.

### Strengths
- Thorough empirical evaluation, and SoTA performance on multiple datasets and IPC settings.
- Improved efficiency for meta-gradient computation compared to full BPTT [1] in terms of both memory & time.
- I really like the brief hardness-stratified analysis in Figure 10.

### Weaknesses
 - Using meta-gradient norm as an indicator for stability (more in questions).
- Boosting is optimization-agnostic procedure however it’s only tested with RaT-BPTT (more in questions).
- Section 5 (boosting) is not well-discussed with key details shifted to the appendix. I would suggest keeping a subset of results from Figures 7-10 (and moving others to the appendix), but with all details for those experiments complete in the main-text.
- The paper does not provide a comprehensive study on the effect of varying the boosting strength parameter, $\beta$, on the final performance, which is crucial for understanding the robustness of the method.


### Questions
- (Figure 3) The change in gradient norm with more steps is not a good indicator of training stability. I would suggest looking at either the variance of these gradients [1], or the eigenvalues of the hessian matrix (a.k.a. sharpness) [2] as better aligned indicators.
- Do you expect the boosting idea to work with techniques other than RaT-BPTT, e.g., DSA [3], MTT [4]?
- One subtle change in RaT-BPTT is the usage of Adam optimizer in the inner-loop. Notably, all existing distillation techniques use SGD. Is this the main reason for improvement compared to other techniques? How does RaT-BPTT (SGD) compare with RaT-BPTT (Adam)? I would suggest referring to [5] for a better understanding of using Adam in data distillation.

I'd be happy to consider increasing my overall rating if some of these questions are addressed in the rebuttal.

Other comments and suggestions (not used in deciding my overall rating):
- Please include full-data performance in Table 1.
- The meta-gradient of SGD in the inner-loop can be efficiently computed [6]. Please mention it in the full-text.
- It would be great to include an analysis of the effect of varying $\beta$ in Boost-DD on downstream generalization.

[1] Faghri, Fartash, et al. "A study of gradient variance in deep learning." arXiv preprint arXiv:2007.04532 (2020).

[2] Cohen, Jeremy M., et al. "Gradient descent on neural networks typically occurs at the edge of stability." arXiv preprint arXiv:2103.00065 (2021).

[3] Bo Zhao and Hakan Bilen. Dataset condensation with differentiable siamese augmentation. In Proceedings of the International Conference on Machine Learning (ICML), pp. 12674–12685, 2021b.

[4] George Cazenavette, Tongzhou Wang, Antonio Torralba, Alexei A. Efros, and Jun-Yan Zhu. Dataset distillation by matching training trajectories. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 4750–4759, 2022.

[5] Sachdeva, Noveen, et al. "Farzi Data: Autoregressive Data Distillation." arXiv preprint arXiv:2310.09983 (2023).

[6] Maclaurin, Dougal, David Duvenaud, and Ryan Adams. "Gradient-based hyperparameter optimization through reversible learning." International conference on machine learning. PMLR, 2015.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes simple and effective method for dataset distillation. Since Back Propagating Through Time (BPTT) is computationally expensive, we truncate a trajectory of inner  optimization steps, called truncated BPTT. However, the performance of truncated BPTT is worse than BPTT due to the biased gradient. In order to get better trade-off between computational cost and performance, the paper proposes to sample random window of inner trajectory, which uses the same amount of computational cost as the truncated BPTT but with better performance. Moreover, it proposes "Boosted Dataset Distillation" to mitigate intercorrelation between distilled images, where it iteratively learns to distill a dataset into a small set while setting the learning rate of previously distilled instances to small value.

### Strengths
- The proposed method is simple and effective. It outperforms most of the baselines on CIFAR, CUB and Tiny-ImageNet datasets.

- Ablation studies show the effective of proposed method.

- The proposed method can be easily integrated with other bilevel optimization based dataset distillation methods.

### Weaknesses
 - Although the proposed method uses the same amount of computational cost as the truncated BPTT method, it still requires to store a trajectory of length $M$. If the dataset becomes large, we may need large $M$ for convergence at inner loop, which hinders scalability of the proposed algorithm.

- It is hard to analyze why the proposed method helps improving performance compared to BPTT or truncated BPTT.

- The paper requires more comprehensive empirical experiments to verify the effectiveness of the proposed method. First and foremost, the authors of the paper did not conduct experiments for architecture generalization. While Table 1 simply demonstrates the method's ability to generalize from a shallow convnet to a wide convnet, I believe this is not adequate. I am curious about how the proposed dataset distillation method can be applied to other architectures, such as VGG, EfficientNet, and ResNet. Secondly, I wonder the proposed method scales to ImageNet dataset which has 1000 classes. 

- There is no comparison of computational cost between the proposed method and the other baselines. I think the proposed method is way more expensive than other baselines (such as FrePo) which simplify the  inner loop.

- I am not still convinced that the proposed method scales to large dataset because it still requires backpropagating through truncated inner trajectory. I am not sure the technique from [1] is applicable to the proposed method since [1] requires the inner optimization procedure "invertible". In general, Reverse Mode Differentiation requires large space complexity [2]. I am not familiar with [3], hard to say whether it does really save the memory. I highly recommend authors empirically show that some of those technique reduce the memory without performance degradation so that the proposed method scales to large datasets.

- I do not think FRePO is applicable. Although we sample a feature extractor from a model pool, we need to optimize a linear classifier for inner optimization step.



### Questions
- What happens if we scale the meta-gradient of BPTT with the norm of the gradient during training? The authors argue training instability of BPTT based on the larger gradient norm. Then the most straightforward way to mitigate the issue would be gradient clipping or scaling the gradient.

- What happens if we gradually increase the total number of unrolling steps for BPTT instead of using fixed $T$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
