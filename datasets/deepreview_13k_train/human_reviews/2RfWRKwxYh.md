# Boost Self-Supervised Dataset Distillation via Parameterization, Predefined Augmentation, and Approximation

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Although larger datasets are crucial for training large deep models, the rapid growth of dataset size has brought a significant challenge in terms of considerable training costs, which even results in prohibitive computational expenses. Dataset Distillation becomes a popular technique recently to reduce the dataset size via learning a highly compact set of representative exemplars, where the model trained with these exemplars ideally should have comparable performance with respect to the one trained with the full dataset. While most of existing works upon dataset distillation focus on supervised datasets, \todo{we instead aim to distill images and their self-supervisedly trained representations into a distilled set. This procedure, named as Self-Supervised Dataset Distillation, effectively extracts rich information from real datasets, yielding the distilled sets with enhanced cross-architecture generalizability.} Particularly, in order to preserve the key characteristics of original dataset more faithfully and compactly, several novel techniques are proposed: 1) we introduce an innovative parameterization upon images and representations via distinct low-dimensional bases, where the base selection for parameterization is experimentally shown to play a crucial role; 2) we tackle the instability induced by the randomness of data augmentation -- a key component in self-supervised learning but being underestimated in the prior work of self-supervised dataset distillation -- by utilizing predetermined augmentations; 3) we further leverage a lightweight network to model the connections among the representations of augmented views from the same image, leading to more compact pairs of distillation. Extensive experiments conducted on various datasets validate the superiority of our approach in terms of distillation efficiency, cross-architecture generalization, and transfer learning performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work targets the cross architecture generalizability challenge in dataset distillation. When performing distillation, the data is often biased to the model used in the distillation process -- in this work the proposed self-supervised approach parameterizes the representations of images while studying/leveraging the effects of augmentations. This approach features a 5 stage method involving pertaining a network on the source dataset, followed by image parameterization (encoding the images and augmentations via low-dimensional bases vectors), bi-level optimization on the images, approximation to handle the distribution/representation shift, and reconstruction of the images using the bases and learned features. The method reports strong performance improvement on a variety of datasets against most of the current SOTA methods.

### Strengths
The key strengths of this paper include:

1. More diverse datasets: Not many dataset distillation papers venture beyond the CIFAR/ImageNet datasets, however these authors included results on CUB2011 and StanfordDogs. Additionally, the ViT performance has been reported, and overall it appears that the authors performance improvement is maintained on Transformer architectures, albeit smaller.

2. The basis and coefficient initialization ablation provides interesting insight into the sensitivity of the proposed framework.

3. Personally, I found the use of the approximation networks to be a clever solution to reducing memory usage while preserving the essence of image augmentation. By learning a mapping between and subsequently the shift in distribution of the unaugmented distilled representation into it's augmented views, one can efficiently store simply the network rather than all the augmented views.

4. Strong baselines: This work accurately surveyed some of the most seminal and current SOTA in the field of dataset distillation (with the exception of a few missing citations that should be added). I find the included competitive methods to be comprehensive enough to support the statements however, further comments on the benchmarking are included in the Weaknesses section.

### Weaknesses
Despite the interesting approach taken in this work, I find a few crucial weaknesses:

1. I find that the experimental support is a bit lacking. As is common in Dataset Distillation works, it is generally good practice to show the scaling over different memory budges (N) on various datasets, rather than just a single dataset, in order to show generalizability. Specifically, the performance of the method should be evaluated across a range of N values (e.g., N = 10, 50, 100, 200, 500) on multiple datasets (e.g., CIFAR-10, CIFAR-100, Tiny ImageNet) to demonstrate the robustness and scalability of the approach. This would provide a more comprehensive understanding of how the method performs under different constraints and data complexities.
2. I noticed that the resolutions on ImageNet scale to 64 x 64 -- however recently, the field has shifted to higher resolutions such as 128x128 or even 512 x 512 -- I think it would be important to see if the method can scale well to larger resolutions. The current experiments do not sufficiently demonstrate the method's ability to handle high-resolution images, which are increasingly common in real-world applications. Evaluating the performance on datasets with resolutions of 128x128 and 256x256 would be crucial to assess its practical applicability. Furthermore, it would be beneficial to analyze the computational cost and memory requirements as the resolution increases.
3. I think another important criteria that should be included is Applications -- as alluded to in the paper tasks like continual learning or neural architecture search (line 43) are important in the field, however none of these results were included in the main paper -- I think it is important to test the applicability of the method in order to determine significance and impact. The paper should include experiments that demonstrate the utility of the distilled datasets in downstream tasks such as continual learning, neural architecture search, or few-shot learning. This would provide a more comprehensive evaluation of the practical value of the proposed method. For example, the distilled dataset could be used to initialize a model for a new task in a continual learning setting, or to train a surrogate model for neural architecture search.
4. Given that this approach involves multi-level optimization, I think efficiency metrics should be compared as well (time per step, GPU memory etc). -- This will demonstrate wether the gain in performance is justified over other methods when comparing the relative compute demands. A detailed analysis of the computational cost of the proposed method is necessary. This should include a comparison of the training time, memory usage, and the number of optimization steps required with respect to other state-of-the-art methods. This analysis should be conducted on a standardized hardware setup to ensure a fair comparison. Furthermore, the authors should provide a breakdown of the computational cost associated with each stage of the proposed method.

[Minor] Some missing citations including DataDAM (ICCV'23), CAFE (CVPR'22)

### Questions
I've highlighted a few of the issues/suggestions for the Authors to consider in the rebuttal phase above in the Weaknesses Section. These are crucial in determining the significance of the work and wide scale adoption.

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
3

### Summary
This paper proposes a novel approach to self-supervised dataset distillation aimed at reducing training costs by creating compact datasets that maintain model performance. This method, intended to address challenges in self-supervised learning (SSL) for dataset distillation, introduces three key contributions: 1. Parameterization 2. Predefined Augmentation  and feature approximation 3. Optimizations with approximation Networks. Generally they have shown a very contributing method.  

The paper introduces a solid contribution to self-supervised dataset distillation, with innovative approaches to parameterization, augmentation handling, and memory efficiency with upgraded existing method named as KRR-ST. While the approach is complex, it provides a promising direction for reducing training costs in SSL, particularly in resource-limited settings. With further optimization and extension to diverse tasks, this method has the potential to make dataset distillation more accessible and applicable in real-world scenarios.

### Strengths
1. This paper demonstrated a very strategic parameterization.
The use of bases for image and representation parameterization is a sophisticated approach to compress dataset information without sacrificing accuracy. This addresses both storage efficiency and computational cost.

 2.Effective Augmentation Handling:
By predefining augmentations, the method successfully mitigates the bias introduced by random augmentations, a notable challenge in SSL distillation methods.

3. Improved Memory Efficiency:
The inclusion of approximation networks to predict representation shifts from unaugmented to augmented views significantly reduces memory usage by eliminating the need to store augmented representations. This makes the approach more scalable.

4. Transfer Learning Potential:

The method shows strong transferability to downstream tasks, making it particularly appealing for real-world applications where labeled data is scarce, and transfer learning is critical.

5. Ablation Studies and Hyperparameter Analysis:

The paper includes ablation studies that isolate the contributions of parameterization, augmentation, and approximation networks, offering clear insights into each component's impact on performance.

### Weaknesses
1. Complexity and accessibility
Critique: The method involves several sophisticated techniques, including low-dimensional basis parameterization, predefined augmentations, and approximation networks. This complexity may make it difficult for practitioners to implement and tune the method without extensive expertise in self-supervised learning and dataset distillation. The reliance on PCA for parameterization, while effective, requires careful selection of the number of components, which can be non-trivial for different datasets. Furthermore, the predefined augmentations, while mitigating bias, might not be optimal for all types of data, and the process of selecting these augmentations is not clearly defined, potentially requiring significant experimentation.

2.  Computational and memory trade-Offs
Critique: While the method claims to be memory-efficient due to approximation networks, the additional computational overhead introduced by these networks might reduce the method’s overall efficiency, especially in resource-constrained environments. The approximation networks, while reducing the need to store augmented representations, introduce additional forward and backward passes during training, which can be computationally expensive. The paper does not provide a detailed analysis of the trade-off between memory savings and computational costs, making it difficult to assess the practical benefits of this approach in various settings.

3. Dependence on Synthetic Data for Evaluation:
The experiments rely heavily on benchmark datasets like CIFAR100. However, these datasets have well-structured labels and relatively consistent image quality, which may not fully represent real-world data variability. The lack of evaluation on more diverse and challenging datasets, such as those with noisy labels, varying image quality, or different modalities, limits the generalizability of the findings. The method's performance on datasets with more complex structures and real-world noise is not clear.

### Questions
1. The datasets in the experiments are CIFAR 100 and datasets with similar image attributes. I can understand it is possible to get a distilled dataset in a lab environment and the datasets are very feature-controllable. Do you have space to show that your experiment can be successful in other different scenarios? For example, some randomly taken images. 

2. Though this is a memory saving method, a very large portion of the whole method is still computing intensive. Do you have any benchmark to show that the whole method could be executed in an efficient way?

### Soundness
3

### Presentation
3

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
This paper proposes a self-supervised data distillation method based on image decomposition. By initializing with principal components and learning the impact of data augmentation, the performance of the distilled dataset is enhanced. The experiments provide a comprehensive analysis of the method’s effectiveness.

### Strengths
1. The topic is both valuable and practical, especially in the era of large datasets. While most current research on data distillation focuses primarily on classification tasks, which may be too narrow, this work seeks to improve self-supervised tasks. This approach is more general and can better support feature learning for downstream applications.

2. The paper is well-written and easy to follow, with a straightforward method that is simple to understand. For each component, the authors clearly explain the rationale behind its inclusion.

3. The experiments demonstrate the method’s effectiveness, as it consistently outperforms baseline methods in both transfer learning and linear probing tasks.

### Weaknesses
I did not find any major weaknesses in this paper. However, there are some concerns regarding its novelty. The techniques employed are largely derived from previous work on data distillation for classification tasks. It would be helpful if the authors could clarify what unique challenges exist for self-supervised data distillation and how their method specifically addresses those challenges.

### Questions
NA

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a method for dataset distillation based on KRR-ST. Two techniques are introduced: (1) PCA-based dimensionality reduction, which transforms images and their representations into lower-dimensional bases and coefficients; and (2) Data Augmentation, which employs predefined data augmentations and approximation networks to address the limitation of KRR-ST in utilizing data augmentation during dataset distillation. The authors conduct an extensive experimental evaluation and demonstrate significant improvements over previous baselines.

### Strengths
1. Reducing data size is a critical direction in self-supervised learning research.
2. Fixing the issue of incorporating data augmentation into data distillation is important, as it significantly improves performance.
3. The authors conduct a wide range of experiments, evaluating model performance with various network architectures and different numbers of training examples.

### Weaknesses
1. The proposed techniques in the paper are not new, such as PCA and augmentation approximation networks.
2. The proposed technique leverages data augmentation while minimizing bias, and similar ideas have been explored in self-supervised learning. It is important to cmopare it with other analogous methods [1][2][3].

### Questions
1. Could the authors provide more details about the approximation networks, such as the number of networks used, structure, and layers?
2. Could the authors show a comparison of the distilled data sizes?

### Soundness
3

### Presentation
2

### Contribution
2
