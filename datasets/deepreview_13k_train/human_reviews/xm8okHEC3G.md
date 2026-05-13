# Boosting Dataset Distillation with the Assistance of Crucial Samples

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
In recent years, massive datasets have significantly driven the advancement of machine learning at the expense of high computational costs and extensive storage requirements. Dataset distillation (DD) aims to address this challenge by learning a small synthetic dataset such that a model trained on it can achieve a comparable test performance as one trained on the original dataset. This task can be formulated as a bi-level learning problem where the outer loop optimizes the learned dataset and the inner loop updates the model parameters based on the distilled data. Different from previous studies that focus primarily on optimizing the inner loop in this bi-level problem, we delve into the task of dataset distillation from the perspective of sample cruciality. We find that discarding easy samples and keeping the hard ones that are difficult to be represented by the learned synthetic samples in the outer loop can be beneficial for DD. Motivated by this observation, we further develop an Infinite Semantic Augmentation~(ISA) based dataset distillation algorithm, which discards some easier samples and implicitly enriches harder ones in the semantic space through continuously interpolating between two target feature vectors. Through detailed mathematical derivation, the joint contribution to training loss of all interpolated feature points is formed into an analytical closed-form solution of an integral that can be optimized with almost no extra computational cost. Experimental results on several benchmark datasets demonstrate the effectiveness of our approach in reducing the dataset size while preserving the accuracy of the model. Furthermore, we show that high-quality distilled data can also provide benefits to downstream applications, such as continual learning and membership inference defense. The code can be found at https://github.com/to_be/released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an Infinite Semantic Augmentation (ISA) method for dataset distillation, which enhances the performance of existing methods like MTT and IDC. The authors begin by demonstrating that discarding easy samples from the original datasets is beneficial, as it focuses on extracting crucial features from the more challenging samples. Drawing inspiration from MixUp, they propose an augmentation technique to enrich these difficult samples. The effectiveness of the proposed ISA is verified through experiments conducted on CIFAR, Tiny ImageNet, and ImageNet subsets.

### Strengths
Strength:
1. This method is an augmentation-based method that can be embedded with other existing dataset distillation methods for improved performance. 

2. The authors evaluate the effectiveness of the proposed ISA in downstream tasks, including continual learning and membership inference defense. 

3. The visualizations in this paper are impressive and comprehensive, significantly enhancing its clarity.

### Weaknesses
My major concern is on discarding easy samples. 
1. On the one hand, this step requires computing the NFR loss in FRePo twice, which would require longer running time for dataset distillation and make the baseline complex. 
2. On the other hand, this technique is heuristic and seems counterfactual. Intuitively, easy samples should contain some common patterns that can reflect what a class of objects looks like in general. These samples should be more effective than hard samples to capture the major features of each class. In dataset distillation, major information is expected to be stored while other unusual patterns are discarded. It seems strange to me that discarding easy samples leads to better performance, especially when IPC is small. 
3. This strategy drops some samples, which destroys the original data distribution. However, according to Fig. 1, it makes the distilled data better follow the original distribution, which seems strange to me.
4. Moreover, there seems to be a paper using a similar technique [a].
5. I would like to see separate results of only using this strategy without ISA, such as in Tab. 2, 3, 4, and 8.
6. I suggest the authors compare qualitative samples of the baseline, with selection, and with ISA together to better reflect the functionality of each part. Currently it seems that the qualitative results are not different from the original FRePo too much.

### Questions
The questions are listed as the weaknesses in the previous section. 

[1] Liu, Yanqing, et al. "DREAM: Efficient Dataset Distillation by Representative Matching." arXiv preprint arXiv:2302.14416 (2023).

[2] Liu, Songhua, et al. "Dataset distillation via factorization." Advances in Neural Information Processing Systems 35 (2022): 1100-1113.

[3] Yin, Zeyuan, Eric Xing, and Zhiqiang Shen. "Squeeze, Recover and Relabel: Dataset Condensation at ImageNet Scale From A New Perspective." arXiv preprint arXiv:2306.13092 (2023).

[4] Rui Song, Dai Liu, Dave Zhenyu Chen, Andreas Festag, Carsten Trinitis, Martin Schulz, and Alois
Knoll. Federated learning via decentralized dataset distillation in resource-constrained edge
environments. arXiv preprint arXiv:2208.11311, 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes two techniques to boost the performance of kernel-based dataset distillation methods: discarding easy samples and infinite semantic augmentation. Experiments on several benchmarks demonstrate the effectiveness of the proposed methods.

### Strengths
1. The proposed infinite semantic augmentation technique is mathematically elegant and effective.
2. The experimental evaluations are comprehensive enough to validate the effectiveness.
3. The writing is coherent and easy to follow.

### Weaknesses
1. **Inconsistent and Marginal Gains in Test Accuracy**: The test accuracy of the proposed method doesn't consistently outperform existing techniques. When it does show an improvement, the margin is sometimes minimal. This inconsistency raises concerns about the robustness of the method and its practical applicability across diverse datasets. The lack of a clear pattern in performance gains makes it difficult to ascertain the conditions under which the proposed method is most effective. For instance, while the method may show improvements on some datasets, it is not clear if these improvements are statistically significant or if they are simply due to random fluctuations. 
2. **Incomplete Review of Related Work**: The paper falls short in its coverage of existing literature. The need for a more comprehensive review is also detailed in the "Questions" section below. The current related work section does not adequately position the proposed method within the broader landscape of dataset distillation and related fields. This lack of context makes it difficult to assess the true novelty and contribution of the work.
3. **Lack of Comparative Analysis with Data Selection Algorithms**: The experiments in the paper do not include comparisons with data selection algorithms, leaving a gap in understanding how the proposed method stacks up against these approaches. This omission is significant because data selection methods also aim to identify crucial samples, and a comparison would help to clarify the unique advantages or disadvantages of the proposed approach. Without this comparison, it is difficult to determine whether the proposed method offers a significant improvement over existing data selection techniques.

### Questions
Please refer to Weaknesses for details.

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper innovatively tackles the challenge of Dataset Distillation (DD) with a focus on sample cruciality in the outer loop of the bi-level learning problem. Building upon the neural Feature Regression (FRePo) framework, the authors introduce the Infinite Semantic Augmentation (ISA) algorithm. This algorithm enriches harder-to-represent samples in the semantic space through a process of continuous interpolation between two target feature vectors. Importantly, the algorithm is highly efficient as it formulates the joint contribution to training loss as an analytical closed-form integral solution. The method is rigorously evaluated on five benchmark datasets including MNIST, Fashion-MNIST, CIFAR10, CIFAR100, and Tiny-ImageNet. It is also compared against six baseline dataset distillation algorithms: DSA, DM, MTT, KIP, RFAD and FRePo. The experimental results demonstrate that the proposed ISA method effectively reduces dataset size while maintaining or even enhancing model accuracy. The distilled data also proves to be beneficial for downstream applications such as continual learning and privacy protection.

### Strengths
- **Originality**: The paper's focus on optimizing the outer loop in the bi-level optimization problem for Dataset Distillation is original.
- **Quality**: The paper is methodologically sound, demonstrated by a comprehensive set of experiments across five benchmark datasets. It also includes an ablation study that pinpoints the contributions of different components. The derivation of the integral into an analytical closed-form solution makes the algorithm an efficient solution.
- **Clarity**: The paper is well-organized and the algorithmic steps are outlined in detail.
- **Significance**: The proposed method is efficient, achieving state-of-the-art results in dataset size reduction while maintaining or even improving model performance.

### Weaknesses
The author only demonstrated through some simple experiments that in data distillation, the importance of difficult samples is stronger than that of simple samples. However, this conclusion cannot adequately explain that, in Figure 5 of the appendix, it can be observed that discarding difficult samples still allows the distilled data to achieve the comparable performance as the original distillation method, or even better.
             
Can the author provide more profound and solid explanations for the point mentioned above?

When comparing with baseline methods, the author did not compare with the state-of-the-art methods like FTD and TESLA. Nevertheless, this method only achieved state-of-the-art performance in 8 out of the 14 experimental setups.

Can the author complete the relevant comparative experiments and provide an objective analysis of the experimental results？


Directly using MSELoss as a criterion to discard a substantial proportion of samples.  Could this lead to a bias in distilled data?

### Questions
1. **Clarification on "Data Extension" Terminology**: The term "data extension" is unfamiliar and appears to be non-standard. Is it synonymous with commonly used terms like "data augmentation" or "data interpolation"? If not, what differentiates it, and why opt for this term?
2. **Major Revisions in Related Work Section Needed**: The section on related work requires substantial updates for completeness and context.
    1. **Coresets**: The paper cited is neither the seminal work nor the most recent in the field of coresets. It would be beneficial to include at least these two papers [1*] and [2*], and consider citing earlier foundational works they mention, perhaps in an appendix.
    2. **Dataset Distillation**: In addition to [2*], works like [3*] and [4*] are missing from both the discussion and comparison tables. Also, MTT, which is covered in the experiments, lacks mention in the related work section. Please include these papers in both the textual discussion and comparative evaluations.

[1*] Yang, Y., Kang, H. & Mirzasoleiman, B.. (2023). Towards Sustainable Learning: Coresets for Data-efficient Deep Learning. *Proceedings of the 40th International Conference on Machine Learning*, in *Proceedings of Machine Learning Research* 202:39314-39330 Available from https://proceedings.mlr.press/v202/yang23g.html.

[2*] Shin, S., Bae, H., Shin, D., Joo, W. & Moon, I.. (2023). Loss-Curvature Matching for Dataset Selection and Condensation. *Proceedings of The 26th International Conference on Artificial Intelligence and Statistics*, in *Proceedings of Machine Learning Research* 206:8606-8628 Available from https://proceedings.mlr.press/v206/shin23a.html.

[3*] Kim, J., Kim, J., Oh, S.J., Yun, S., Song, H., Jeong, J., Ha, J. & Song, H.O.. (2022). Dataset Condensation via Efficient Synthetic-Data Parameterization. *Proceedings of the 39th International Conference on Machine Learning*, in *Proceedings of Machine Learning Research* 162:11102-11118 Available from https://proceedings.mlr.press/v162/kim22c.html.

[4*] Wang, K., Zhao, B., Peng, X., Zhu, Z., Yang, S., Wang, S., ... & You, Y. (2022). Cafe: Learning to condense dataset by aligning features. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 12196-12205).

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors delve into the task of dataset distillation from the perspective of sample cruciality, they argue that hard samples in the original dataset contain more information. To this end, they discard some easier samples and enrich harder ones in the semantic space through continuously interpolating between two target feature vectors during data distillation.

### Strengths
The authors delve into the task of dataset distillation from the perspective of sample cruciality and propose the idea of adjusting the proportion of difficult and easy samples in the data distillation process; few papers considered this aspect before.
They put forward an infinite semantic augmentation method by continuously interpolating between two target feature vectors, requiring no extra computational costs while being effective.
The applicability of distilled data is considered, They demonstrated that their distilled data is capable of providing benefits to continual learning and membership inference defense.

### Weaknesses
The author only demonstrated through some simple experiments that in data distillation, the importance of difficult samples is stronger than that of simple samples. However, this conclusion cannot adequately explain that, in Figure 5 of the appendix, it can be observed that discarding difficult samples still allows the distilled data to achieve the comparable performance as the original distillation method, or even better.
             
Can the author provide more profound and solid explanations for the point mentioned above?

When comparing with baseline methods, the author did not compare with the state-of-the-art methods like FTD and TESLA. Nevertheless, this method only achieved state-of-the-art performance in 8 out of the 14 experimental setups.

Can the author complete the relevant comparative experiments and provide an objective analysis of the experimental results？


Directly using MSELoss as a criterion to discard a substantial proportion of samples.  Could this lead to a bias in distilled data?

### Questions
Please refer to the Weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
