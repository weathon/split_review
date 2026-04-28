# Self-Paced Augmentations (SPAug) for Improving Model Robustness

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Augmentations are crucial components in modern computer vision. While various augmentation techniques have been devised to enhance model generalization and robustness, they are conventionally applied uniformly to all dataset samples during training. In this paper, we introduce ``Self-Paced Augmentations (SPAug),'' a novel approach that dynamically adjusts the augmentation intensity for each sample based on its training statistics. Our approach incurs little to no computational overhead and can be effortlessly integrated with existing augmentation policies with just a few lines of code. We integrate our self-paced augmentations into established uniform augmentation policies such as AugMix, RandomAugment, and AutoAugment. Our experiments reveal sizeable improvements, with about 1\% enhancement on CIFAR10-C and CIFAR100-C datasets and a 1.81\% improvement on ImageNet-C over AugMix, all while maintaining the same natural accuracy. Furthermore, within the context of augmentations designed to enhance model generalization, we demonstrate a 0.4\% improvement over AutoAugment on CIFAR100, coupled with a 0.7\% enhancement in model robustness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an adaptive augmentation technique which dynamically adjust the augmentation intensity based on training statistics. The approach can be applied to existing augmentation framework, such as AugMix, RandomAugment and AutoAugment. The experimental results show that it can improve model robustness to image corruptions.

### Strengths
+ Interesting idea to combine curriculum learning into data augmentation, controlling how models learn from augmented samples.
+ The writing is well-structured and easy to read.

### Weaknesses
 __Missing comparisons with existing work__
The authors did not explain the difference of their approach from AugMax [1] framework, which combines augmented images with adversarially calculated weights.  Similarly, Hou et al. [2] adopted the idea of curriculum learning and applied it to decide when to augment data during training. But this is also not discussed by the authors. Other augmentation techniques being sota, PRIME [4] and TrivialAugment [5], are not compared with.

__clarity__
Explanation of equation (4) is not clear and in Fig. 3, the formula for hard sample should be: L_i - \sigma(m_i)
It is unclear in the formula whether the cross-entropy loss should be calculated on the original images or the augmented images. If the cross-entropy loss is computed based on the augmented images, then the parameter m_i could be also updated through backpropagation, just like AugMax [1].

__Non-comprehensive experimental results__
The authors only show results of SPAug combined with AugMix on ImageNet, while the results of it combined with AutoAugment and RandomAugment are not provided. The standard performance of models are not given in Table 2. The evaluation metrics in [3] used for benchmarking the robustness of models to image corruptions are not used. 
Experiments are mostly focused to small datasets, while ImageNet is only used for a single comparison. The claims and observations made on CIFAR10/100 are thus limited and cannot be generalized and compared with those in other papers that extensively experiments on ImageNet. Furthermore, only a single architecture is tested: how would this method perform with transformer training strategies?

__Figures do not have enough explanations__
The meaning of x and y axes in Fig, 4 are not explained and  the figure itself is not easily readable. From the figure, I cannot interpret how the binary mapping function governs the extent of augmentations. In Fig. 5, the authors provide four augmented versions for one class, alongside the changes of m_i during training. However, the relationship between the augmented images and the m_i tendency is not explained. 

__Missing appendices__
The authors mention appendix and supplementary materials, but it is not given. 

Minor: Implementation python code directly pasted as pseudo code.

### Questions
- How is the work different from [1,2] and what improvements have been made regarding them? This work is quite similar to AugMax[1] in the sense of combining augmented images with their original version using weights calculated by backpropagation.
- In the experiments, how is the threshold τ that distinguishes easy samples from hard ones in the minibatch determined? Is it affected by the minibatch size? Is there any trade-off between them, considering needed computational resources?
- In Tables 4 and 5, the results of models trained in the 100 and 200 epochs are given. However, the gained performance through more training epochs is not significant. For instance, in Table 4, the gained C-Err for SPAug-Learnable is on average 0.5, while this value for AA is 0.9. What is the reason for training more epochs to obtain trivial improvement using SPAug-Learnable? Besides, why is the baseline model WRN-28-10 having different C-Err in Table 2 and 4?
- How does the method perform on ImageNet with other existing augmentation techniques, and with other architectures (e.g. Transformers)?

### Soundness
3 good

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
This paper introduces the used of a self-paced algorithm for training with data augmentation. Each sample is now a linear combination of a sample without transformations plus a sample with augmentations, where the blending factor is learned during training with a self-paced strategy based on the loss. In practice, during training, easy samples with low loss are augmented more than hard samples with high loss, that are more difficult to learn. This approach is supposed to improve results, especially on corrupted datasets. Results are presented for CIFAR 10/100 original and corrupted.

### Strengths
- The idea of using self-paced learning for augmentations is new up to my knowledge and makes sense.
- The method can be adapted to many kind of data augmentation by adding a few lines of code as shown in Algorithm 1.

### Weaknesses
 - The method is not compared directly with other reported results and the provided baselines seems to be weak, making results not accurate. For instance, in RA the error reported on CIFAR10/100 for Wide-ResNet 28-10 are respectively 2.7 and 16.7, while in the proposed paper are 3.3 and 19.1.
- Authors state that all previous data augmentation models use augmentations that are not instance specific. However, there are papers, (eg. [1] or [2]) that learn instance specific augmentation through a neural network. Authors should cite the family of data augmentation methods based on transformations learned by a network and if possible compare with them.
- Results are limited to CIFAR10/100. Results on a larger dataset as ImageNet should be provided.
- In related work, there should be a part considering self-paced methods. There is a vast literature on such kind of approaches and even if it is not applied to data augmentation it is still relevant. Some approaches are cited during the presentation of the method, but I think that a more exhaustive presentation in related work is needed.
- With large datasets, you need to store a large number of parameters, one per sample.

### Questions
- Due to the stochastic nature of the augmentations, the corresponding loss for a given sample can fluctuate and introduce a certain noise on the selection of the easy/hard samples. Did you find any instabilities in the training due to this noise?
- Why you train with a limited budget instead of training until convergence? This makes results not compareble with the state of the art. 
- What is the reason to propose the toy experiment in section 4.2. The following evaluations are also performed on the same dataset.
- What is the value of the thresholds $\tau$ for the experiments in Table 2?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposed self-paced augmentations for training neural networks. In particular, it chooses the data augmentation strength dynamically according to the training statistics of training samples. The author conducts experiments on CIFAR10/CIFAR100 and demonstrates its effectiveness and robustness.

### Strengths
i) The idea and the implementation are easy to follow, and the writing is clear to read.

ii) The author provides visualization and quantitative analysis to validate the effectiveness of the proposed method.

### Weaknesses
i) The experiments are only conducted on some small datasets (e.g. CIFAR), it is not convincing without the experiment results on a large-scale dataset(e.g. ImageNet)

ii) The proposed augmentation, as illustrated in Eq.1, shares a similar formulation as two widely used augmentation methods: CutMix and Mixup. However, there is no comparison between the proposed method and CutMix/Mixup

iii) There are also some related works[a,b], which also adjust the augmentation strength according to other training statistics. They are not discussed and compared in experiments.

### Questions
Refer to the weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an adaptive data augmentation strategy for deep neural networks, focusing on enhancing model robustness and performance. By employing a self-paced augmentation method, the research dynamically adjusts the intensity of data augmentation based on individual sample characteristics. The paper demonstrates the effectiveness of this approach using various datasets.

### Strengths
(1) The point of the paper is very good.
(2) Combining with multiple strategies to demonstrate performance improvement is also a great approach.

### Weaknesses
(1) In Section 4.3, you mentioned that the learnable SPAug has a significant improvement effect on the performance of AugMix in processing corrupted data. However, in the above Table 2, compared to the optimal model, your performance improvement is very limited or there is no improvement at all. The superiority of the model is not sufficiently reflected.
(2) You did not discuss the threshold τ in the subsequent experiments. It is not clear how you optimized the threshold. It feels like you are showing the best experimental results that you got separately with τ=0.1 or τ=0.2.
(3) The last two models, after adding SPAug-Learnable, indeed improved on the corrupted dataset, but there was a loss on the clean dataset. I hope you can consider the adaptability issue between the specific data augmentation strategy and the data.
(4) Introducing an adaptive learning data augmentation strategy increases the complexity of the model and may lead to extended training times and computational costs. While you mentioned that this method introduces minimal overhead, there is no specific experimental data in the article to support this claim.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
