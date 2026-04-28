# Pursuing Feature Separation based on Neural Collapse for Out-of-Distribution Detection

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
In the open world, detecting out-of-distribution (OOD) data, whose labels are disjoint with those of in-distribution (ID) samples, is important for reliable deep neural networks (DNNs). To achieve better detection performance, one type of approach proposes to fine-tune the model with auxiliary OOD datasets to amplify the difference between ID and OOD data through a separation loss defined on model outputs. However, none of these studies consider enlarging the feature disparity, which should be more effective compared to outputs. The main difficulty lies in the diversity of OOD samples, which makes it hard to describe their feature distribution, let alone design losses to separate them from ID features. In this paper, we neatly fence off the problem based on an aggregation property of ID features named Neural Collapse (NC). NC means that the penultimate features of ID samples within a class are nearly identical to the last layer weight of the corresponding class. Based on this property, we propose a simple but effective loss called OrthLoss, which binds the features of OOD data in a subspace orthogonal to the principal subspace of ID features formed by NC. In this way, the features of ID and OOD samples are separated by different dimensions. By optimizing the feature separation loss rather than purely enlarging output differences, our detection achieves SOTA performance on CIFAR benchmarks without any additional data augmentation or sampling, demonstrating the importance of feature separation in OOD detection. The code will be published.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an OOD detection approach that enhances feature separation. The proposed method is based on Neural Collapse (NC), which suggests that features of ID samples collapse to similar values within a class. Motivated by NC, the authors introduce Separation Loss to encourage OOD features to occupy subspaces orthogonal to the principal subspace of ID features, effectively separating ID and OOD samples at the feature level.

### Strengths
- The paper is well-motivated in its use of Neural Collapse (NC) to improve OOD detection, effectively highlighting NC’s natural feature clustering property as a robust basis for separating ID and OOD data. 
- The incorporation of Neural Collapse as a theoretical foundation adds substantial depth to the methodology, offering a compelling explanation for the effectiveness of feature-level separation in enhancing OOD detection. 
- The proposed approach is conceptually straightforward and easy to implement.

### Weaknesses
 - In Section 3.4, the paper discusses two alternative training strategies: one that directly incorporates all loss terms and another that initially trains with cross-entropy (CE) loss before introducing the proposed losses. However, guidance on when to choose between these strategies in general cases is lacking. Additional discussion on how this choice could affect the model’s performance or usability would be beneficial. The current method requires a manual selection of techniques depending on whether it is half-trained or fully trained, which is often impractical. The reliance on a two-stage process, where the switch point is determined by monitoring training loss, introduces a heuristic element that reduces the method's practicality. The lack of a clear, automated criterion for transitioning between stages makes the method less user-friendly and potentially inconsistent across different implementations.
- The proposed method mainly includes two loss terms, i.e., the Sep loss and Clu loss, upon the OE loss. As discussed in the paper (e.g., the abstract), the Sep loss reflects the main motivation of neural collapse (NC). The ablation studies in Table 5 show that these two terms perform with different significances. The behaviours and importance of these two loss teams are unclear. All experiments indicate that Clu loss alone is not effective. It only shows utility when combined with Sep loss and performs well exclusively on the CIFAR-100 dataset. This raises questions about the claimed effectiveness of Clu loss. The limited utility of the Clu loss, especially its ineffectiveness when used in isolation, suggests that its contribution to the overall performance is marginal and highly dependent on the specific dataset and the presence of the Sep loss. The paper needs to clarify the conditions under which Clu loss provides a tangible benefit.
- Although the proposed method performs well on ImageNet-1k (Table 1), its performance is less consistent on other benchmarks, as seen in Table 2 and particularly Table 3, where broader comparisons are provided. Further explanation or analysis regarding this variability would be valuable to understand the method’s limitations. The performance inconsistencies across different datasets, particularly the weaker results on benchmarks beyond ImageNet-1k, raise concerns about the method's generalizability. The paper should provide a more thorough analysis of why the method's effectiveness varies so significantly across different datasets and explore potential reasons for this variability.
- More analysis of the learned representation space, such as visualizations of the embedding space, would provide insight into how well the method achieves feature separation and could strengthen the evaluation of its effectiveness. The current visualizations only show two classes along with OOD samples. Why not visualize samples from all classes together in a single plot? The visualization of only two classes at a time limits the understanding of the overall feature space. A visualization that includes all classes would provide a more comprehensive view of how the method separates in-distribution and out-of-distribution data.

### Questions
Please check questions alongside the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel strategy for out-of-distribution detection. The approach is based on Neural Collapse and employs this property to avoid modeling OOD feature distributions while effectively segregating ID and OOD features.

### Strengths
The motivation behind this method is reasonable and worth exploring.

### Weaknesses
 - While Figure 2 demonstrates the distribution changes of the OOD training set during training, which is expected, it would be more insightful to see the distribution patterns of OOD data during the testing phase.
- The improvement in AUROC metrics compared to existing methods is relatively modest.
- Although the authors claim to follow DAL's experimental setup on ImageNet (lines 321, 332), there are discrepancies between the metrics reported in Table 1 (lines 374, 375) and those in Table 16 of the DAL paper ("Learning to Augment Distributions for Out-of-Distribution Detection").
- The experimental comparison on ImageNet is limited to only two methods, whereas the DAL paper compared five methods in their Table 16, suggesting insufficient comparative analysis.

p.s. There appears to be an inconsistency in decimal places for the average AUROC of Energy between lines 381 and 382.

### Questions
- The proposed method shares fundamental similarities with KNN, as both approaches classify data based on distance calculations in feature space, identifying ID data through closer distances and OOD data through farther distances. Could the authors elaborate on the key distinctions between their method and the KNN approach?
- Given the use of Wide ResNet-40-2 architecture for CIFAR-10 and CIFAR-100 datasets, does the method have specific requirements regarding network feature dimensions? A detailed analysis of this aspect would be valuable.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on feature-space separation rather than output-space discrepancies. The authors propose a novel approach leveraging Neural Collapse, which describes how ID samples’ penultimate features converge near their respective class weights. The core contribution is the Separation Loss, which aligns OOD features orthogonally to ID feature subspaces. Extensive experiments across standard benchmarks demonstrate that the proposed method achieves state-of-the-art performance in OOD detection.

### Strengths
1. The paper introduces a separation loss based on the Neural Collapse phenomenon to enhance feature-space disparity between ID and OOD samples. This approach builds on strong analytical foundations from NC, addressing key challenges specific to OOD detection.

2. The experiments are comprehensive, covering multiple datasets and architectures, with ablation studies that effectively address most concerns.

3. The proposed method is straightforward and clear. The proposed method is broadly applicable to any OOD detection method based on Outlier Exposure.

### Weaknesses
I hope the authors could address my questions as follows.

 1. The improvements on the ImageNet benchmark are relatively marginal compared to the CIFAR benchmarks. Could you provide a more detailed discussion to clarify the potential reasons for this difference?

 2. As noted in line 469, `When faced with unseen OOD data, the feature variations tend to fall on the new dimension, resulting in minimal changes on the output.` Would these orthogonal dimensions become exhausted when dealing with a large-scale ID dataset? Additional justification on this point would be helpful, no further empirical results are needed.

 3. In Table 9, the calculation relies on FC weights, which aligns with the paper’s motivation since the optimization is specifically designed to achieve these results. Would using empirical class mean features instead of FC weights yield different outcomes? This approach could also further align with the NC motivation, given that the penultimate features of ID samples within a class are nearly identical to the last layer weights.

### Questions
1. The improvements on the ImageNet benchmark are relatively marginal compared to the CIFAR benchmarks. Could you provide a more detailed discussion to clarify the potential reasons for this difference?

2. As noted in line 469, `When faced with unseen OOD data, the feature variations tend to fall on the new dimension, resulting in minimal changes on the output.` Would these orthogonal dimensions become exhausted when dealing with a large-scale ID dataset? Additional justification on this point would be helpful, no further empirical results are needed.

3. In Table 9, the calculation relies on FC weights, which aligns with the paper’s motivation since the optimization is specifically designed to achieve these results. Would using empirical class mean features instead of FC weights yield different outcomes? This approach could also further align with the NC motivation, given that the penultimate features of ID samples within a class are nearly identical to the last layer weights.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a novel approach for enhancing out-of-distribution (OOD) detection in deep neural networks (DNNs) by improving outlier exposure training. This approach leverages the Neural Collapse (NC) phenomenon where features within each class collapse to a point forming an ETF simplex with other classes to improve the separability of in-distribution (ID) and OOD data. The authors propose a new loss function, "Separation Loss," designed to maximize the orthogonality between the feature representations of ID and OOD data. The orthogonality is maximized by minimizing the cosine similarity with the last layer FC layer weights for OOD data and by aligning the representation of ID data with the predicted class weight from the last layer. This method achieves state-of-the-art (SOTA) performance on CIFAR10, CIFAR100, and ImageNet benchmarks without requiring additional data augmentation or sampling techniques.

### Strengths
- The concept of applying the NC phenomenon to directly manipulate feature spaces for OOD detection is innovative. Unlike traditional methods that focus on output discrepancies, this paper focuses on feature separability, which is a fresh perspective in the field.

- The empirical validation is robust, covering several benchmarks and comparing against a comprehensive suite of methods. The novel loss function, grounded in theoretical insights from NC, is shown to effectively enhance feature separation.

- The paper is well-organized and articulately written, with clear explanations of the NC phenomenon, the motivation for the new loss function, and the experimental setup. The visualizations effectively illustrate how feature separation is achieved, aiding in understanding.

- The approach addresses a critical gap in OOD detection by improving model reliability in real-world applications, where ID and OOD data may not be clearly distinguishable through outputs alone. This has significant implications for deploying DNNs in safety-critical domains.

### Weaknesses
Dependency on NC Property: The effectiveness of the method is heavily dependent on the presence of the NC phenomenon, which may not occur in all network architectures or training configurations. (The NC property usually fail on the testing set [1])

The authors claim that their method works well across different architectures while only testing ResNet and WideResnet and DenseNet. It would be more valuable to test your method against transformer based architecture like ViT or Swin as their features differ due to the global attention mechanism and patch based representations. This experiment will validate the method’s generalizability to different architectures.

In table 2, categorizing the OOD datasets into Near and Far OOD would provide useful insight in the performance of the separation loss, as it might be working on Far-OOD better than Near-OOD which are more entangled in the representation space.

### Questions
1- I would suggest testing your method using OpenOOD framework[1], as you can test Near vs Far OOD beside testing transformer based architectures.

2- The manuscript discusses the application of your method under the assumption of the Neural Collapse (NC) property. However, it is not clear how these methods might perform in scenarios where NC does not hold, such as in imbalanced datasets[2]. Could the authors investigate and elaborate on the potential impact on the results if the NC property is weakened or absent due to dataset characteristics like imbalance? Additionally, I recommend including experiments with imbalanced datasets to provide empirical evidence of the method's robustness under these conditions. This would enhance the paper's contribution by addressing the generalizability of the NC phenomenon across different data distributions.


Bibliography:

1. Zhang J, Yang J, Wang P, Wang H, Lin Y, Zhang H, Sun Y, Du X, Zhou K, Zhang W, Li Y. Openood v1. 5: Enhanced benchmark for out-of-distribution detection. arXiv preprint arXiv:2306.09301. 2023 Jun 15.

2. Zhang E, Li C, Geng C, Chen S. All-around Neural Collapse for Imbalanced Classification. arXiv preprint arXiv:2408.07253. 2024 Aug 14.

### Soundness
4

### Presentation
4

### Contribution
3
