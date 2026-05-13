# Balancing Act: Constraining Disparate Impact in Sparse Models

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Model pruning is a popular approach to enable the deployment of large deep learning models on edge devices with restricted computational or storage capacities. Although sparse models achieve performance comparable to that of their dense counterparts at the level of the entire dataset, they exhibit high accuracy drops for some data sub-groups. Existing methods to mitigate this disparate impact induced by pruning (i) rely on surrogate metrics that address the problem indirectly and have limited interpretability; or (ii) scale poorly with the number of protected sub-groups in terms of computational cost. We propose a constrained optimization approach that \textit{directly addresses the disparate impact of pruning}: our formulation bounds the accuracy change between the dense and sparse models, for each sub-group. This choice of constraints provides an interpretable success criterion to determine if a pruned model achieves acceptable disparity levels. Experimental results demonstrate that our technique scales reliably to problems involving large models and hundreds of protected sub-groups.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper deals with the problem of pruning models with desire of not decreasing performance on subsets via constraints.

### Strengths
The technique is solid and the experiments are sound.

### Weaknesses
Can the paper deals with other pruning techniques to demonstrate the effectiveness of constraint to subsets?

Can we give some formal results with Equation(6) like the analytical solution or convergenece guarantee?

### Questions
Can we give some formal results with Equation(6) like the analytical solution or convergenece guarantee?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a new training protocol to manage pruning induced bias. The main aim is to create algorithms in which the difference in accuracy between any two groups is minimised. The authors highlight that their main focus is lessen the effects of compression and thus they treat dense models as baseline.

### Strengths
This is a useful research area. With concerns of AI inclusion and climate change, sparse models are very appealing. The authors provide a method to ameliorate some of the effects of compression by limiting the disparity between group performance.
This is a well written paper and the methodology is clear. Implementation and results are well described and the examples in the appendix provide further grounding on their work.

### Weaknesses
It is not clear from the analysis provided that solutions always exist given the constraints. Perhaps the authors could more light on this. Is there a relationship between the starting point and how tight the constraints can be?

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a new approach for fine-tuning sparse models after pruning. The proposed approach involves formulating a constrained problem, where loss function is optimized subject to a group-wise accuracy constraint (that is, the accuracy drop for each group should be bounded by a tolerance $\varepsilon$). This Lagrangian of this constrained problem is then optimized with standard gradient-based methods. This approach is empirically shown to reliably generate models where the differences in the group-wise impact of sparsity on accuracy is minimized.

### Strengths
The paper has several strengths:

* The proposed approach is interesting, novel, and flexible, and reliably reduces group wise disparities in accuracy after pruning.
* The empirical evaluation is very thorough.
* Limitations of the proposed methods and ethical considerations are discussed thoroughly as well.
* In the appendix, variations of the main results are discussed as well.;/
* The writing and presentation is clear.

### Weaknesses
The paper has a few weaknesses. 

* This method is independent of the choice of pruning strategy. However, it would have been nice to see the experiments replicated for other pruning strategies, including structured pruning methods. 
* A more detailed discussion on the feasibility of the constrained problem given in equation (4) would have been useful for readers.

### Questions
* Have the authors tried applying this technique to other pruning methods? For instance, how well would this fine-tuning method work if structured pruning was used instead of unstructured pruning? How well would the method work if other unstructured pruning methods were used instead of IMP (i.e. SynFlow [1] or SNIP [2])?
* Is there a sparsity level at which the method fails to achieve models with the desired worst-case groupwise accuracy loss? Put another way, is there a sparsity level at which the constrained optimization problem described in eq. (5) become infeasible? Can the authors comment on how this might play out in the case of structured pruning?
* Are there any formal results that can be provided for solving the CEAG (eq (5))? For instance, is Algorithm 1 guaranteed to find a solution provided the feasible set is nonempty?
* Have the authors considered ways by which the test-case performance can be improved, say by dataset splits?
* Is the CEAG method affected by dataset imbalance? Suppose certain groups have comparatively fewer samples in the dataset. How, if at all, would this affect the efficacy of the method?

[1] "Pruning neural networks without any data by iteratively conserving synaptic flow", Tanaka et al, 2020.

[2] "SNIP: Single-shot Network Pruning based on Connection Sensitivity" Lee et al, 2019.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for mitigating disparate effect on model accuracy by formulating the task as a constrained optimization problem and solving it via alternative gradient descent. The introduced approach manages to decrease the gap between average model performance and worst performance on a subgroup of data while preserving the mean accuracy on the target task.

### Strengths
The problem being addressed is quite novel in sparsification community and is of significant interest to practitioners, especially in safety-critical applications. The approach looks very reasonable and directly optimizes the imposed constraints via solving a min-max problem. The method is quite non-trivial and comprises several interesting ideas - alternating between non-differentiable accuracy constrain term and excess loss term, as well as use of replay buffers for stabilization of optimization. 

CEAG outperforms existing alternatives on a couple of benchmarks - UTKFace and CIFAR100. The method doesn’t add significant computation overhead compared to the standard training procedure.

### Weaknesses
While the proposed method manages to keep train accuracy on subgroups within desired tolerance bounds, seems it has hard to achieve on the test data, especially in the setting with many classes and subgroups (for example in the provided CIFAR-100 experiment). The generalization gap between training and test performance, particularly regarding the worst-group accuracy, is a significant concern. The method appears to overfit to the training set's subgroup distribution, failing to generalize these gains to unseen data. This is especially evident in the CIFAR-100 experiment where the number of subgroups is large, indicating a potential limitation in the method's ability to handle complex, high-dimensional group structures.

The difference between $\mathrm{max}_g \psi_g $ on the hold-out-data between NFT and CEAG doesn’t seem to be very significant in many cases - 2.0 vs 2.1 on 99% sparsity UTKFace *(Table1)*, 3.3 vs 3.6 for 92.5% *(Table2)*, 13.8 vs 14.3 on CIFAR-100 *(Table3)*. Given the standard deviation of the runs, improvement of CEAG appears to be statistically insignificant. The small absolute improvements in worst-group accuracy on the test set, coupled with the reported standard deviations, raise doubts about the practical significance of the method's advantage over existing alternatives. The lack of substantial improvement on the hold-out set suggests that the gains observed on the training data may not translate to real-world scenarios.

Experimental validation is not exhaustive enough. To demonstrate the efficiency in a more large scale and practically relevant scenario one could consider more diverse and large-scale dataset, such as ImageNet (or ImageNet-LT version), or one of the iNaturalist versions, considering only large hierarchy groups to make the task computationally tangible. The current experiments, while demonstrating the method's behavior on smaller datasets, do not fully establish its applicability to complex, real-world problems. The lack of experiments on large-scale datasets with more complex group structures limits the generalizability of the findings. The method's performance on datasets with a limited number of groups might not be indicative of its behavior on more challenging datasets.

*Minor*. The pruning strategy called in the paper is customary named **Gradual Magnitude Pruning** (GMP) [2], where after each pruning step one continues training the model from the current state. **Iterative Magnitude Pruning** (IMP) [3] adopted in discovery of Lottery Tickets rewinds the weights to initialization after pruning step. I would suggest calling the method GMP to avoid confusion.

### Questions
How sensitive is the algorithm to the initialization of dual parameters $\lambda_g$ and the corresponding update rule?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
