# POC: Preventing the Over-Collapse of Classes for Class-Incremental Learning

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Deep neural network-based classification models often suffer from catastrophic forgetting during class-incremental learning (CIL). Previous studies reveal that it results from the overlap between seen and future classes after being mapped by model to its feature space through extracting the features. In this paper, we analyze that this overlap mainly results from the $\textit{over-collapse}$ of seen classes, where the model tends to map originally separated one seen class and its adjacent regions in input space to be mixed in the feature space, making them indistinguishable. To this end, we propose a two-step framework to $\textbf{P}$revent the $\textbf{O}$ver-$\textbf{C}$ollapse (POC). During training, POC first learns and applies a set of transformations to the training samples of seen classes. Based on our theoretical analysis, the transformation results will locate in the adjacent regions of the seen classes in the input space so that we can let them represent the adjacent regions. Then, the model's optimization objective is modified to additionally classify between the seen classes and the adjacent regions, separating them in model's feature space so that preventing the over-collapse. To retain the model's generalization on the seen classes, a deterministic contrastive loss that makes the separate features of seen classes and adjacent regions close is further introduced. Since POC uses the adjacent regions exclusively for classification, it can be easily adopted by existing CIL methods. Experiments on CIFAR-100 and ImageNet demonstrate that POC effectively increases the last/average incremental accuracy of six SOTA CIL methods by 3.5\%/3.0\% on average respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
the authors propose a two-step framework called Prevent the Over-Collapse (POC) for class incremental learning. During training, POC applies transformations to training samples of seen classes, maintaining their distinction in the feature space. It also introduces an expanded classifier to separate seen classes from adjacent regions. In the testing phase, the expanded classifier is masked, allowing classification of seen classes without extra computational costs. POC incorporates a deterministic contrastive loss to keep adjacent regions close to their original classes, enhancing generalization. Experimental results on CIFAR-100 and ImageNet show that POC improves the last and average incremental accuracy of several state-of-the-art CIL methods by 3.5% and 3.0%, respectively.

### Strengths
-	The proposed POC framework effectively prevents the overlap between seen and future classes in the feature space as shown in fig.3. This innovative approach might enhance the model's ability to generalize across tasks.
-	The experimental results show that POC can robustly enhance the performance of various CIL approaches across several approaches.
-	The article provides sufficient evidence for some of its claims in the appendix.

### Weaknesses
 - An important assumption of the POC is that it addresses the issue of over-collapse, which can lead to catastrophic forgetting. However, there is insufficient literature to prove that over-collapse is the cause of catastrophic forgetting. The citations provided in the article, such as Masana et al., 2022 on line 184, do not offer relevant explanations, and the article also does not sufficiently analyze the over-collapse phenomenon as claimed in its contributions. This results in the article appearing to lack a reasonable motivation for its claims.
- The POC requires inference on multiple augmented images, which may lead to a significant increase in training costs. However, the article does not discuss this issue.
- I’m not certain that the primary reason POC is effective is due to its backbone having seen multiple augmented images. I believe it is necessary to conduct an experiment where all images augmented by learnable augmentations are used as positive samples corresponding to their categories for direct training. I think this approach could also yield some performance improvement, and it might not perform worse than the results shown by POC.

### Questions
All my concerns are mentioned in the weakness. And I think the experiments in the third line of weakness should be conducted.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the over-collapse phenomenon in class incremental learning (CIL) that makes it difficult to distinguish the seen and unseen classes.
To address this issue, the authors suggest distinguishing the seen classes and their transformed versions.
To generate samples close yet adequately distant from the original ones, the authors suggest rotation and a learnable affine transformation and theoretically demonstrate the effectiveness of these transformations.
The authors argue that the proposed method can prevent over-collapse phenomenon, thereby enhancing generalization ability to unseen classes.

### Strengths
The most intriguing aspect is generating samples that are close yet distinct from the original ones.
To prevent the rotated samples from being overly similar to the original ones, the authors propose learning a set of affine transformations, ensuring the generated samples are adequately adjacent but maintain a sufficient distance from the originals.
The theoretical analysis further supports the effectiveness of the proposed transformation for generating adjacent samples.

### Weaknesses
It seems that there are no significant issues on the paper.
One minor concern may be the generalization ability of the proposed method.
Can the proposed method be applied to other tasks over the image classification task?
The reviewer thinks it is somewhat difficult to directly generalize the proposed method to other tasks, which may limit its value.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to improve the generalization on seen classes in CIL by preventing the over-collapse (POC) of seen classes. To this end, the authors generate samples in adjacent regions by some learnable transformations and making the classification model predict them with a modified loss, which is much similar to IL2A where it predicts auxiliary classes generated by mixup. The authors use theories in OOD detection to prove such transformations generate samples in adjacent regions. Furthermore, the author claims the generated samples in adjacent regions are prone to be far away from the seen class, thus introduces the deterministic contrastive loss (DCL) to make them closer to the seen class. Finally, the authors perform performance comparisons with SOTAs and similar works, verify the effectiveness of DCL and POC with ablation study on them and plotting ICD and ICG metrics during the incremental training.

### Strengths
- The reported performance of the method out-performs similar works like IL2A.
- The proposed method is compatible with various methods in CIL.

### Weaknesses
 - The reason why over-collapse leads to forgetting is not clear enough. It seems to assume the samples in the future class are in the adjacent area of the previous samples. Specifically, the paper does not sufficiently explain why the feature space representation of seen classes collapsing is directly linked to the model's inability to learn new classes. While the authors mention that over-collapse causes the model to mix seen and future classes, the mechanism of how this mixing translates to forgetting is not rigorously established. The assumption that future class samples reside primarily in the adjacent regions of previous samples is also a strong claim that requires more justification. It is possible that future classes could exist in other regions of the input space, and the paper does not address how the proposed method would handle such cases.
- The DCL is somewhat not well-motivated, there is no empirical or theoretical evidence provided about the _far away_ projection. Instead, the authors state that the distance of the transformed sample is upper-bounded in Proposition 3.2. The paper claims that the transformed samples are 'far away' from the seen class in the feature space, but this is not convincingly demonstrated. The upper bound provided by Proposition 3.2 only limits the distance in the input space, not the feature space. The motivation for using a contrastive loss to bring these 'far away' samples closer is not clear, especially given that the transformations are designed to generate samples in the adjacent regions. The paper needs to provide more evidence that these transformed samples are indeed problematic and that the DCL is the appropriate solution.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2
