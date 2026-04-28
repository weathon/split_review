# ReweightOOD: Loss Reweighting for Distance-based OOD Detection

- Decision: Reject
- Scores: 6, 5, 3, 3, 3

## Abstract
Out-of-Distribution (OOD) detection is crucial for ensuring the safety and reliability of neural networks in critical applications. Distance-based OOD detection is based on the assumption that OOD samples are mapped far from In-Distribution (ID) clusters in embedding space. A recent approach for obtaining OOD-detection-friendly embedding space has been contrastive optimization of pulling similar pairs and pushing apart dissimilar pairs. It assigns equal significance to all similarity instances with the implicit objective of maximizing the mean proximity between samples with their corresponding hypothetical class centroids. However, the emphasis should be directed towards reducing the Minimum Enclosing Sphere (MES) for each class and achieving higher inter-class dispersion to effectively mitigate the potential for ID-OOD overlap. Optimizing low-signal dissimilar pairs might potentially act against achieving maximal inter-class dispersion while less-optimized similar pairs prevent achieving smaller MES. Based on this, we propose a reweighting scheme \textbf{ReweightOOD}, that adopts the similarity optimization which prioritizes the optimization of less-optimized contrasting pairs while assigning lower importance to already well-optimized contrasting pairs. Such a reweighting scheme serves to minimize the MES for each class while achieving maximal inter-class dispersion. Experimental results on a challenging CIFAR100 benchmark using ResNet-18 network demonstrate that the proposed reweighting scheme improves the FPR metric by a whopping ~38\% in comparison to the baseline. In various classification datasets, our method outperforms existing methods, making it a promising solution for enhancing OOD detection capabilities in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of OOD detection. It is motivated from supervised contrastive learning and propose to further disperse the inter-class distance while reduce intra-class variance via reweighting. Specifically, it encourages the model to focus more on hard positives and negatives samples. The experimenets on several benchmarks show the performance advantages of the method.

### Strengths
- The motivation is clear and presentation is easy to follow.
- The proposed method is straightforward and weights for positives and negatives are dynatmically adjusted based on the similarity score. 
- Table 1 and 2 shows the dispersion cross class and compactness within the class for the proposed method compared to SupCon
- Performance gains on CIFAR10/100 and ImageNet100

### Weaknesses
Novelty:
- Although the reweighting on constrative learning has been under-explored in OOD detection community, focusing more on hard postivie/negatives are widely applied in deep metric learning (especially in face recognition). E,g [1][2]. I think the novelty is sort of limited as the paper adopt hard sample mining/weighting into OOD detection task. In rebuttal, can you explain the difference bewteen your work and [1,2] in terms of hard samples re-weighting?

Experiment:
- In ImageNet100, can we have numbers from other methods (e.g, CIDER) instead of SupCon only.
- For Table 1,2, I am interested to see how the MES score and Average centroid dispersion for CIDER. 
- Hyperparameters test on linear transformation are encouraged. It is said that ResNet18 network are set to (5, −2, 2, 1) and (5, −4, 2, 1). Do you have to set differently for other backbones or datasets?
- For Figure 5 (b), why there is only one cluster? also, can you provide feature vislization for SupCon or CIDER as well?

[1] CurricularFace: Adaptive Curriculum Learning Loss for Deep Face Recognition
[2] AdaFace: Quality Adaptive Margin for Face Recognition

### Questions
Please refer to the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The traditional distance-based OOD detection assumes that OOD samples are far from In-Distribution (ID) clusters in the embedding space. A recent method involves contrastive optimization to create an OOD-detection-friendly embedding space. However, this approach doesn't effectively reduce the Minimum Enclosing Sphere (MES) for each class and achieve higher inter-class dispersion, leading to potential overlap between ID and OOD samples. To address this, the paper proposes a reweighting scheme called ReweightOOD. This scheme prioritizes optimizing less-optimized contrasting pairs while assigning lower importance to already well-optimized pairs.

### Strengths
This paper addresses the important issue of Out-of-Distribution (OOD) detection in neural networks, crucial for ensuring safety and reliability in critical applications.

### Weaknesses
1. The figures 3 and 4 are not mentioned in the article.
2. I find Figure 5 visually unappealing, and I wonder why there is only one category in the right figure.
3. Table 2 only has two columns, it's not worth occupying such a large space in the paper.
4. More importantly, why not conduct experiments on the ImageNet dataset, like existing works [1] have done?

[1] Sun Y, Guo C, Li Y. React: Out-of-distribution detection with rectified activations[J]. Advances in Neural Information Processing Systems, 2021, 34: 144-157.

### Questions
See above.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes some modifications to contrastive optimization-based OOD detection. Previous approaches assign equal importance to all similar instances. This paper proposes to give different weights to these instances and tries to enforce the minimum enclosing sphere and higher inter-class dispersions. Experiments on CIFAR100 and ImageNet 100 demonstrate the effectiveness of the proposed approach.

### Strengths
1. The proposed method is very simple and intuitively makes sense. The idea of obtaining a minimum closure sphere makes sense to separate OOD and ID data, and it is also easy to implement this idea by adding weights to the loss functions.

### Weaknesses
1. **There are many recent OOD baselines but they are not taken into consideration for comparison.** There are many recent OOD baselines but the authors either do not cite them [1,2,3] or do not add them in the comparison (e.g., ASH, GradNorm). In particular, these are very strong baselines and I see the performance of this method at the same level as ReAct. It is a bit strange that the evaluation does not involve any activation-clipping baselines such as ReAct and ASH (they are clear state-of-the-art methods and do not require any training). 


>[1] React: Out-of-distribution detection with rectified activations. NeurIPS 2021.
>
>[2] RankFeat: Rank-1 Feature Removal for Out-of-distribution Detection. NeurIPS 2022. 
>
>[3] Boosting Out-of-distribution Detection with Typical Features. NeurIPS 2022. 


2. **The experiments are not sufficient only on CIFAR/ImageNet100.** The authors only validate the proposed approach on CIFAR100 and ImageNet100, which is far from sufficient and comprehensive. Usually, people evaluate OOD methods on CIFAR10, CIFAR100, and ImageNet-1k benchmarks. I would be convinced if the method also works for ImageNet-1k. 

3. **The instance weight can be replaced with learnable temperatures.**  Adding weight significance to the samples is one way to obtain a higher inter-class separation, but I am wondering if would it also make sense to make the temperature learnable. Compared with weight significance, it would bring another benefit: learnable distribution shaping for each category.  

4. **How does the method perform when scaling to more/fewer categories?** I would suspect the performance is highly related to the number of categories. If the value is too large (e.g., 1000) or too small (e.g., 5), the performance might deteriorate. Can authors provide some ablation studies on subsets of the used datasets?

5. **Does the method also work for Transformer-based architectures?** Currently the authors evaluate their approach with ResNet-18, DenseNet and WideResNet? Can authors do more experimental evaluation on Transformers?

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses contrastive learning to address out-of-distribution (OOD) problems. The article introduces what contrastive learning is and discusses the challenges encountered by classical contrastive learning in tackling OOD problems. The authors believe that the main issue with contrastive learning in addressing OOD problems is that the discrimination between many difficult samples is not high enough, resulting in a close proximity among these challenging samples. As a result, it becomes difficult to recognize OOD samples. Therefore, the authors propose a reweighting approach to enhance the discrimination between different categories in contrastive learning, thereby improving the effectiveness of OOD detection.

### Strengths
1. The method proposed in this paper is simple and intuitive, and may be a good way to solve OOD problems.
2. According to the author's experimental results, the proposed method can indeed improve the performance of OOD detection.
3. The author's writing is very clear, and the description of the method section is easy to understand, combining formulas and diagrams.

### Weaknesses
1. In the abstract, the author emphasizes that their method outperforms the baseline by 38%, which seems impressive. However, this improvement is mainly due to the low performance of the baseline method itself. The proposed method does not actually achieve such a significant improvement compared to the state-of-the-art (SOTA). In my opinion, this exaggerates the contribution of this paper. It would be better to clarify the improvement relative to SOTA in the beginning to avoid misleading the readers.

2. The simplicity of the method itself can be considered an advantage. However, based on the experimental results, the improvement of this paper compared to the state-of-the-art is limited. Therefore, I hope the authors can further explore this direction and achieve more substantial advancements.

3. The experiments conducted in this paper are not comprehensive enough. Firstly, experiments on complete ImageNet-1K were not conducted. Additionally, the comparison with the latest methods, such as those presented in recent conferences like CVPR 2023, was not included.

### Questions
Please address the problem in weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Out-of-distribution (OOD) detection has been widely studied. This paper focuses on the distance-based OOD detection with contrastive optimization methods. It points out that assigning equal significance to all similar pairs is not efficient in reducing the MES for each class and achieving higher inter-class dispersion. Therefore, this paper proposes ReweightOOD, a weight mapping function based on similarity, to prioritize hard positives and hard negatives. Experiments and visualization results show the proposed ReweightOOD surpasses the baseline and SOTAs by a large margin on FPR and AUROC.

### Strengths
Based on the distance-based methods in OOD detection, this paper may first combine reweighting the hard samples with contrastive optimization.

The paper conducts explicit experiments on the influence the ReweightOOD brings to MES and inter-class dispersion. The results on CIFAR and ImageNet also verify its effectiveness.

### Weaknesses
The novelty of this idea is quite limited. Designing different weights for hard samples has been widely applied in many fields including classification, detection, etc., and yields success. It can be directly accustomed to nearly all methods and will not result in depreciation at least.

The baseline chosen in this paper training a not-well-adjusted model to perform OOD Detection is quite unfair. As the proposed method is a loss function, it can be combined with other contrastive optimization methods easily. A method designed for OOD detection is more suitable to be a baseline. Therefore, it makes the results less convincing.

The important hyperparameters including the scaling and shifting scalars of the final linear transformation are not studied in the ablation experiments.

### Questions
Why are the parameters of two linear transformation layers directly set to (5, -4, 2, 1) or (5, -2, 2, 1)?

What is the reason for using a smaller shifting scalar from -2 to -4 when training with a smaller dataset CIFAR10?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
