# BCE vs. CE in Deep Feature Learning

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6

## Abstract
When training classification models, it expects that the leaned features are compact within classes, and can well separate different classes. As a dominant loss function to train classification models, the minimization of CE (Cross-entropy) loss can maximize the compactness and distinctiveness, i.e., reaching neural collapse. The recently published works show that BCE (Binary CE) loss performs also well in multi-class tasks. In this paper, we compare BCE and CE in the context of deep feature learning. For the first time, we prove that BCE can also maximize the intra-class compactness and inter-class distinctiveness when reaching its minimum, i.e., leading to neural collapse. We point out that CE measures the relative values of decision scores in the model training, implicitly enhancing the feature properties by classifying samples one-by-one. In contrast, BCE measures the absolute values of decision scores and adjust the positive/negative decision scores across all samples to uniform high/low levels. Meanwhile, the classifier bias in BCE presents a substantial constraint on the samples' decision scores. Thereby, BCE explicitly enhances the feature properties in the training. The experimental results are aligned with above analysis, and show that BCE consistently and significantly improve the classification performance and leads to better compactness and distinctiveness among sample features.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores whether the binary cross-entropy (BCE) loss function can induce neural collapse, a phenomenon in which deep learning models achieve tightly clustered intra-class features and well-separated inter-class features. Through both theoretical analysis and empirical validation, the authors show that, like cross-entropy (CE) loss, BCE loss can indeed facilitate neural collapse, even in multi-class tasks. Furthermore, the experiments demonstrate that models trained with BCE loss perform better than those trained with CE loss. This advantage is from the classifier bias introduced by BCE, which explicitly optimizes feature alignment towards class centers, enhancing intra-class compactness and inter-class separation. These findings highlight that BCE loss not only fosters a beneficial feature distribution but also boosts model performance.

### Strengths
1. Strong theoretical analysis of BCE’s ability to achieve neural collapse
This paper provides a detailed theoretical analysis comparing BCE and CE on neural collapse. It shows that BCE, like CE, can achieve high intra-class compactness and inter-class separation, indicating that BCE has strong theoretical potential in feature learning.

2. Practical analysis of decision score and boundary updates
Beyond the theory, the paper also explains the practical differences between BCE and CE regarding decision score and boundary updates. BCE is shown to provide consistent updates to decision scores, leading to stronger feature constraints. This insight helps us understand how BCE can improve feature representation.

3. Solid experimental validation
The experiments effectively support the theoretical points, showing BCE’s advantages over CE across different models and datasets.

### Weaknesses
1. Some practical training factors not considered: The paper doesn’t fully address certain practical training factors, such as weight decay and class weight initialization, which might impact the formation of a simplex equiangular tight frame and the contrastive properties. Specifically, the analysis does not delve into how different weight decay rates on the classifier weights versus other network parameters might affect the convergence to neural collapse. Furthermore, the impact of various class weight initialization schemes, such as uniform or class-proportional initialization, on the final feature distribution and the observed performance gains of BCE over CE is not explored.

2. Assumptions could be generalized: Some theorems are based on the assumption that feature dimension $d$ is larger than the category number $K$. In large-scale representation tasks (e.g., face recognition), the category number can be very large, and in practice, BCE is still effective even when $d<K$. It would strengthen the paper in discussing or generalizing this assumption, considering that BCE might be useful in larger-scale scenarios. (Although the generalization is difficult.) The theoretical analysis should consider the implications of this assumption, especially when the feature space is lower-dimensional than the number of classes, which could lead to different convergence properties and feature distributions.

### Questions
1. BCE’s performance in more complex tasks: These researches and experiments focus mainly on image classification, especially when feature dimension $d$ is greater than the number of categories $K$. For more complex tasks (like simple sequence classification or large-scale classification where $K$ might be larger than $d$), do you expect BCE to show similar advantages? Are there any plans to test BCE’s applicability in these settings?

2. Explicit vs. implicit constraints in feature learning: You’ve shown that BCE’s explicit constraints give it a clear edge in feature learning, and the experiments confirm this strong feature constraint effect. Would it be possible to further derive the performance limit (Upper-boundary) of CE’s implicit constraints? This might help to make a more direct comparison of their feature learning strengths.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper compares the binary cross-entropy (BCE) loss with the traditional cross-entropy (CE) loss in the context of deep feature learning. The key idea is that both losses can lead to neural collapse, maximizing intra-class compactness and inter-class distinctiveness.

### Strengths
1. The paper is well-written and organized, clearly explaining the key ideas and providing a detailed comparison between BCE and CE.
2. The experimental results are presented systematically, supporting the claims made in the paper.

### Weaknesses
1. The volume of data used for the experiments is small, and for data-dependent deep neural networks, there will be a gap between the theoretical and practical effects. Specifically, the experiments are limited to datasets like MNIST, CIFAR10, and CIFAR100. These datasets are relatively small and may not fully represent the complexities of real-world data distributions. This raises concerns about the generalizability of the findings to larger, more diverse datasets where the behavior of BCE and CE might differ significantly.
2. The paper mentions that data augmentation techniques like Mixup and CutMix can improve classification performance, but it would be helpful to further investigate how these techniques interact with BCE and CE losses and whether they have a similar impact on feature properties. The current analysis lacks a detailed exploration of how these augmentations might affect the feature space learned by each loss function, and whether the observed benefits are consistent across different augmentation strategies and parameter settings.
3. The visualization in Figure 4 is not very explicit, and only the comparison of the two categories is clearer, which is not enough to support the authors' conclusion that “the features of BCE-trained ResNet18 for these categories are distributed in more compact areas and have signiﬁcant gaps between them, implying better feature compactness and distinctiveness.” The visualization is limited to a 2D projection of high-dimensional feature embeddings, which may not fully capture the true structure of the feature space. The lack of quantitative metrics to support the visual observations further weakens the claim of improved feature compactness and distinctiveness.

### Questions
1. Sigmoid loss and BCE loss are both commonly used loss functions for binary classification tasks, what are the differences and connections between them.
2. What is the classification performance of BCE loss on medium to large scale datasets? For example, ImageNet.
3. Would BCE loss have a theoretical advantage over sigmoid loss for comparison learning tasks?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper shows that the features learned by deep neural network architectures trained with binary cross entropy (BCE) loss maximize intra-class compactness and inter-class distinctiveness when the loss reaches its minimum, thereby leading to the well-known phenomenon of neural collapse. The paper then illustrates that both classification performance and search/retrieval performance, as previously empirically evaluated by other works, are due to the capability of BCE compared to CE in learning more compact and separated features.

### Strengths
1. The paper broadens the loss functions that can lead to neural collapse including a novel ene into the list. It is well written and organized.

2. The formal proof, similar to previous studies on neural collapse, is very interesting. The use of lower bounds for the BCE loss and identifying the conditions for achieving these lower bounds is a significant result. 

3. The specific result with respect to the CE case shows that the global minimizers' biases satisfy a particular equation.

### Weaknesses
1. The paper is hard to follow despite the very good proof. Even in the insightful parts, it does not clearly demonstrate the advantage of BCE over CS. However, it provides a solid analysis of neural collapse in the context of BCE loss. As an example, the papers Wen et al. (2022) and Zhou et al. (2023) more effectively presented the geometric relationships of the involved entities.

2. In the reviewer's opinion, the bounded aspect of BCE does not seem to provide a clear advantage over the unbounded CE. Typically, features learned with cross-entropy (CE) are used in a normalized form. This operation projects the unbounded features onto a hypersphere, placing them within a bounded hyperspherical region around the prototype. 

3. The related work section seems to be generic with respect to the addressed topic. The section concludes by stating that none of the existing works clearly reveal the advantage of BCE loss, However the insights into these advantages are still difficult to perceive at this stage. The works Wen et al. (2022) and Zhou et al. (2023) should be introduced earlier and revisited later in light of the paper's main findings on bias and decision boundaries. The current presentation makes it difficult to grasp the paper's main point.

4. Typically, papers about Neural Collapse with CE, including the two mentioned in this paper (Yang et al., 2022; Kim & Kim, 2024), show that the final classifier geometry of a regular simplex can be fixed at the beginning of training by setting the classifier biases to zero. Does BCE follow a similar pattern in this case, or do the biases play a significant role? 

5. The contrastive property seems to be very important throughout the paper and should have been discussed more thoroughly.

6. In Figure 1, features within the hyperball radius are shown as fully bounded features, with two of the hyperspheres being tangent at contact points while two are not. This needs clarification on the significance of the tangency and non-tangency.

7. Line 427: Why is the bias set to 0, 1, 2, 3, 4, etc., for visual identification purposes in the figure?

### Questions
Please refer to the weaknesses box.

### Soundness
3

### Presentation
3

### Contribution
3
