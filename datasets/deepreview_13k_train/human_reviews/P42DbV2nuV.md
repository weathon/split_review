# Instance-dependent Early Stopping

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
In machine learning practice, early stopping has been widely used to regularize models and can save computational costs by halting the training process when the model's performance on a validation set stops improving. However, conventional early stopping applies the same stopping criterion to all instances without considering their individual learning statuses, which leads to redundant computations on instances that are already well-learned. To further improve the efficiency, we propose an Instance-dependent Early Stopping (IES) method that adapts the early stopping mechanism from the entire training set to the instance level, based on the core principle that once the model has mastered an instance, the training on it should stop. IES considers an instance as mastered if the second-order differences of its loss value remain within a small range around zero. This offers a more consistent measure of an instance's learning status compared with directly using the loss value, and thus allows for a unified threshold to determine when an instance can be excluded from further backpropagation. We show that excluding mastered instances from backpropagation can increase the gradient norms, thereby accelerating the decrease of the training loss and speeding up the training process. Extensive experiments on benchmarks demonstrate that IES method can reduce backpropagation instances by 10%-50% while maintaining or even slightly improving the test accuracy and transfer learning performance of a model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a method, Instance-dependent Early stopping (IES), a variant of standard dataset-level early-stopping mechanism that in contrast uses an instance-level mastery threshold on second-order differences of the loss function to decide which examples to drop from the training (backward path). Calculation of this metric requires the forward path for the example to be dropped in the next epoch. This results in lossless acceleration in both nominal computational cost and real-world training time.

The empirical analysis presented in the paper quantifies these improvements in CIFAR-10/100 and ImageNet-1K. Multiple optimization algorithms and multiple learning rate schedules are analyzed separately. Results show nominal sample reduction of 10-55% and speedups of 20-40% and neutral accuracy. Further analysis shows that larger speedups are achievable if small suboptimality is allowed. Another empirical analysis is performed on the choice of hyperparameter (delta), establishing its effect on the error rate and training speedup.

### Strengths
- The paper is well motivated and easy to follow.

- Comparisons against the baseline and also early-stopping / data-efficiency  methods show strong SOTA in training acceleration for a few datasets.

- The speedups are not just in nominal sample complexity, but also in world-clock training time.


- The method only relies on the forward path and has an efficient implementation path in most ML frameworks.

### Weaknesses
 - There is no theoretical analysis of the proposed method presented. There is also no rigorous suggestion on how one might attempt such analysis.

- There is no mention of catastrophic forgetting, which is a well-known and well-studied topic in non-uniform training (e.g. in RL and active learning). This setup is not as episodic as a full-blown RL domain, but there are clear similarities that would suggest catastrophic forgetting could occur if examples are completely dropped (too early) and never revisited. I suggest adding at least one experiment in which early dropped examples are evaluated at the end of training to measure an report any forgetting effects.

- The empirical test cases are very limited. SOTA results only on CIFAR-10/100 are not enough to establish the efficacy of the method on other settings. The study on the higher level (yet still vision) tasks is also somewhat limited and not against other data-efficiency methods. A comparison vs. other method can be added to the higher-level vision task study to improve the analysis. 

- A very important point is raised in the limitations and not addressed in the paper: the fact that instance-based early stopping can introduce biases in the learning process that affect fairness or policy considerations. One could argue that without special care such side effects are bound to happen. To study this effect, one can build an adversarial dataset with easy examples from one protected group and harder ones from another group. Non-uniform training can result in shifted per-group precision/recall metrics compared to the baseline, which can be measured and reported.

### Questions
- How does the world-clock training time of the 1-order diff. method compare to the 2-order diff.? Calculating first-order differences might require less compute/memory even if the nominal complexity reduction is less than higher order differences.

- Figure 5, last row: training time reduction can also be added here + legend.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an early stopping mechanism called Instance-dependent Early Stopping (IES) that takes into account individual instances in the training set. It is based on a concept that once the model learns an instance, it should stop iterating more on that particular instance. They define an approach to measure when an individual instance has been “mastered” based on the second-order derivative of its difference in loss. They empirically evaluate different aspects of the proposed method and also show that their proposed algorithm speeds up the training process while maintaining the generalization performance of the model.

### Strengths
- The paper is well-written, presents an interesting and intuitive idea, and is well-positioned within the existing literature.
- The proposed early stopping criterion offers computational efficiency by avoiding back-propagation, leading to faster training and reduced computation without sacrificing generalization.
-  The empirical results are extensive and address critical questions related to the method's effectiveness.

### Weaknesses
 - A crucial missing element in this study is an analysis of the impact of noisy samples within the training set.  It is likely that in the presence of noisy labels, correctly labeled samples would be quickly learned and excluded, leaving the model to train primarily on incorrect information. This could lead to detrimental effects, potentially causing the model to "forget" previously learned correct trends and suffer from significantly worse generalization performance compared to standard training. Since, in practice, the presence of noise in a dataset is often unknown, this limitation raises concerns about the practicality of the proposed method in real-world scenarios.  Specifically, the claim that "well-learned" instances become redundant may not hold true when noisy samples are present, as the model may need to revisit correctly labeled data to counteract the influence of noisy labels. While Figure 2 addresses the persistence of learning in a clean setting,  a corresponding analysis for noisy datasets is crucial to fully evaluate the robustness and practicality of the proposed method.
- The "mastered" criterion introduces two new hyperparameters: a threshold, delta, and a step count, N. Introducing additional hyperparameters necessitates further tuning and selection, which reduces the practicality of the method. While the authors demonstrate some stability with respect to these parameters, it remains unclear how to optimally select them for datasets significantly different in nature from CIFAR-10 and CIFAR-100. This raises concerns about the method's generalizability and ease of use across diverse datasets.

### Questions
1. In Figure 1, The rate of excluded samples differs significantly between CIFAR-10 and ImageNet (non-linear vs. linear). What factors might explain this observation?
Why is training stopped prematurely without "mastering" all the training samples? What is the rationale for not continuing training beyond ~150 epochs?

2. Does the reported training loss in Figure 4 represent the loss calculated over the entire dataset (including mastered/dropped samples) or only on the remaining samples in each training epoch?

3. Figure 4 indicates that IES typically exhibits higher gradient norms. Could this lead to instability in certain settings due to larger steps and jumps during iterations? If so, under what conditions might this occur, and how can such instability be mitigated?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces instance-dependent early stopping (IES), which refines the idea of early stopping from the entire training dataset to the instance level. The method uses second-order loss information to determine whether the data sample was mastered or not. The authors showed empirically that using second order information gives better results compared to zeroth, first and third order information (Figure 5). Finally, the authors provide a range of experiments showing great results of their methodology. Importantly, and as mentioned in Sec. 5, the analysis is focused on dataset-level performance and class-level performance (performance on underrepresented groups) is not taken under consideration in this work.

### Strengths
This paper was a very good read. The idea is simple, intuitive and provides a very elegant in-between to curriculum learning, dynamic data pruning and early stopping. The flow of the paper is very good, and the literature review feels very strong to me (only with some minor issues in relation to dynamic data pruning that I mention later). The experiments are well thought through and feel reasonably extensive to me. Finally, the results are great, which is a very good sign for a methodology paper. I think that it’s a strong paper that should be accepted and will be of interest to the research community, especially due to connection to various research fields mentioned in Section 2, and clear improvements to very popular algorithm (early stopping). I also really appreciate that the authors have explicitly pointed out their lack of studies on underrepresented groups in Limitations, clearly opening path for future research.

### Weaknesses
# Reasoning behind second-order information
On one hand I do think that information in Figure 5 is enough to validate using second-order loss information instead of higher- or lower-order information. On the other hand, I cannot agree with a statement that “the choice of using the second-order difference as the removal criterion for IES has been **extensively** validated through experiments” (L537-538). This statement feels too strong in my opinion. For that to be the case I would expect to see third-order information in Figures 3 and 6, and a more thorough analysis of the trade-offs between computational cost and performance gains when using different orders of loss information. The current analysis does not fully justify the claim of extensive validation, especially given that higher-order information could potentially capture more nuanced changes in the loss landscape, even if at a higher computational cost.

# Distinction from dynamic data pruning
(L147-L151) I am not completely sold on this argument. IES feels to me like a variant of dynamic data pruning. Because of that I also do not understand why the authors did not include training times in Figure 5, especially as it’s the only experiment where they compare their method with dynamic data pruning methodologies. The comparison with only one dynamic data pruning method is also insufficient. There are various dynamic data pruning techniques, and a more comprehensive comparison would strengthen the paper. The current analysis does not fully explore the nuances of how IES compares to different dynamic data pruning strategies, particularly in terms of computational overhead and convergence behavior. It is also not clear how the method handles the trade-off between the number of training instances and the convergence speed, which is a crucial aspect of dynamic data pruning.

# Potential improvements in clarity (minor)
1. (Eq. 2) I assume that the formula comes from Taylor approximation, but this is something that the authors should explicitly state rather than leave for the reader to deduce. A brief explanation of how the second-order difference relates to the curvature of the loss function would also be beneficial.
2. It is not clear why different optimizers were used for different architectures. This should be either explained or a reference should be provided (unless it is somewhere in the appendix and I missed it). The choice of optimizer can significantly impact the performance of the model, and a clear justification for the selection of different optimizers for different architectures is needed.
3. Typos in L137, L328, L368, L423, and L1004
4. (L295-L296)  “As shown in Figure 1, our method can reduce the number of training instances in backpropagation by over 40%” - please specify that it’s only in the later stages of the training. Otherwise it’s too ambiguous and could be considered as overselling results.

# Lack of fully extensive experiments
It would be interesting to see the comparison for different speedups (e.g., Table 4). Maybe IES becomes more effective, in relation to other methods, as we increase the speedup. The current experiments do not fully explore the performance of IES under different computational constraints. A more thorough investigation of how the performance of IES scales with different speedups would be valuable.

### Questions
# Clarification
1. Why did the authors not use FLOPs in their time analysis? Aren’t FLOPs more reliable for this setting? Also, why are there no precise times stated? It feels to me that it’s a very simple thing to do that would give a better perspective on speedups.
2. (L425-L426) Did the authors use IES in fine-tuning as well? Why or why not?
3. When authors compare the results of their IES with the baseline (No removal), is early stopping incorporate into that baseline? I don't think that's something that has been explicitly stated, and it feels to me that if the baseline uses early stopping then it would be significantly clearer to simply call it traditional early stopping (TES) or something similar.
# Future direction
1. (In relation to Figure 2) It would be interesting to show what samples are forgotten (lost their mastered status after removing). I would expect that these are samples that are objectively hard (according to probe models), but subjectively easy for this particular model (at this particular initialization). If we could identify a subset of mastered samples that can be forgotten (unmastered), then we might be able to improve IES by not removing them (a follow-up question is whether this would actually improve the performance). I am curious if the authors thought about it or did any experiments in this direction.

### Soundness
4

### Presentation
4

### Contribution
3
