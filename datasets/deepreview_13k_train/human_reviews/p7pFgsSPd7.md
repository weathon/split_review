# Sample-aware RandAugment

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Automatic data augmentation (AutoDA) improves the generalization of neural networks by filling in the missing data in the target distribution. However, mainstream AutoDA methods suffer from either a time-consuming search process that sets barriers for a wide range of applications, or limited performance due to a lack of dynamic adjustments to policy during training. We propose an asymmetric search-free augmentation strategy Sample-aware RandAugment (SRA) that dynamically adjusts the augmentation policy while maintaining a simple implementation. SRA introduces a heuristic score-based module to dynamically evaluate the difficulty of the original training data, which guides the appropriate augmentation independently for each sample. SRA consists of three steps: 1) distribution exploration, 2) sample perception, and 3) distribution refinement. In a variety of settings, SRA significantly shrinks the gap between search-based and search-free AutoDA methods. The proposed method achieves 78.31% ResNet-50 Top-1 accuracy on ImageNet, which is the state-of-the-art among search-free methods. SRA can lead to simpler, more effective, and more practical AutoDA designs for diverse applications in the future.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a search-free sample-aware automatic data augementation strategies, in which a heuristic metric is proposed to evaluate the difficulty of  training samples. Such evaluation results are used to guide the generation of augmented samples that contribute to decision boundaries during training. Further, an asymmetric data augmentation strategy is proposed.

### Strengths
The research question this work focuses on holds significant research value. It is meaningful to study how to perform data-aware augementation instead of augmenting with an entirely random strategy.

### Weaknesses
The biggest problem is the targeted issue has been well-studied in SelectAugment [1], which is also a sample-aware data augmentation strategy learned using RL. Compared to the heuristic design, RL-based learning might be more generally applicable. The authors omit this for necessary comparison and analysis. This also makes the technical contributions unclear and makes the scope of contribution scope be quite limited.

### Questions
Are the proposed method sensitive to the configurations of data augmentation operators?

What is the scope of application for the proposed method? Are there any limitations in its use?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes an asymmetric search-free augmentation strategy, named SRA, that can dynamically adjust the augmentation policy during the training procedure. Specifically, the authors split a batch into two sub-batches, one is applied with random data augmentation and the other is applied with a sample-aware data augmentation. First, the sub-batch is fed into the model concatenated by a MIS module, which will output the magnitude of the augmentation operators. Then the same sub-batch is augmented and fed into the model again to update the weights.

### Strengths
1.	The proposed method is straight-forward and easy to implement.

2.	Extensive experiments show the effectiveness of the proposed method.

### Weaknesses
1.	This method requires three times forward to update the weights twice, which can be inefficient.

2.	The augmentation operator in the sample-aware augmentation branch is fixed. I wonder how to design the augmentation operators since the selection will significantly affect the performance. The proposed MIS module simply outputs one scalar serving as magnitudes of the augmentation operators, leading to a quite small search space. Specifically, the method only adjusts the magnitude of augmentation, but not the type of augmentation, which limits the diversity of the augmented samples.

3.	I wonder if is there any theory supporting that the cosine similarity between logits and labels has a linear positive relationship with the magnitude of augmentation operators. It is not clear why this specific metric is chosen to determine the magnitude of augmentation, and the relationship between the cosine similarity and the optimal augmentation magnitude is not well established. Furthermore, the method does not consider the semantic meaning of the image when applying augmentations, which could lead to semantically inconsistent augmented images.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the task of Automatic Data Augmentation (AutoDA). To achieve simplicity and effectiveness, this paper proposes a method named Sample-aware RandAugment, which dynamically adjusts the magnitude of augmentation operators according to the Magnitude Instructor Score (MIS). MIS shows the consistency between the prediction and the label, which is a heuristic metric to measure the difficulty of samples. Three steps will be adopted during training, including Distribution Exploration (adopting Rand Augmentation with uniformly sampled magnitudes), Sample Perception (measuring MIS), and Distribution Refinement (adopting Rand Augmentation with MIS). The authors conduct experiments on both CIFAR and ImageNet with different network architectures and show performance improvements compared to SOTA AutoDA methods.

### Strengths
1. The writing and presentation of this paper is good. The idea is very strightforward and easy to follow.
2. The authors conduct experiments on both CIFAR and ImageNet and adopted the proposed methods with several orthogonal methods to show the effitiveness.

### Weaknesses
1. The improvement between the proposed method and RandAugment is marginal. For example, there is only a 0.2% improvement between the SRA and the reproduced RA with ResNet-50 and DeIT in ImageNet experiments.
2. The proposed method highly depends on RandAugment. I consider the most important contribution of this paper to be the strategy of using MIS to adjust the magnitude of each sample. What about adopting the proposed strategy with other augmentation methods? For example, randomly choosing augmentation operators from a search space, and comparing the performances with and without the proposed method.
3. What is the purpose of Step 1? Is it necessary to split the batch into two splits? (1) What about doing step 1 on the first batch and then doing steps 2 and 3 on the second batch? (2) What about removing step 1?

### Questions
Please refer to the weaknesses, expecially the second and third weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
