# DRoP: Distributionally Robust Pruning

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
In the era of exceptionally data-hungry models, careful selection of the training data is essential to mitigate the extensive costs of deep learning. Data pruning offers a solution by removing redundant or uninformative samples from the dataset, which yields faster convergence and improved neural scaling laws. However, little is known about its impact on classification bias of the trained models. We conduct the first systematic study of this effect and reveal that existing data pruning algorithms can produce highly biased classifiers. We present theoretical analysis of the classification risk in a mixture of Gaussians to argue that choosing appropriate class pruning ratios, coupled with random pruning within classes  has potential to improve worst-class performance. We thus propose {\em DRoP}, a distributionally robust approach to pruning and empirically demonstrate its performance on standard computer vision benchmarks. In sharp contrast to existing algorithms, our proposed method continues improving distributional robustness at a tolerable drop of average performance as we prune more from the datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a dataset pruning method that helps the models trained on the pruned datasets be more fair in their class accuracies. The proposed method is called "DRoP", and it selects class-specific pruning ratios based on the error rates, improving performance on underrepresented classes.
The emprical evaluations are performed using VGGs, ResNets on CIFAR-10, CIFAR-100, TinyImageNet, and WaterBirds datasets.
Most of the evaluations are very favourable for the proposed method.

### Strengths
The idea of DRoP is quite interesting and to the best of my understanding very novel. 

The method seems to be simple and straightforward.

The paper provides detailed theoritical insights and this helped understand the method.

### Weaknesses
The framing of the paper is currently unclear to me.
(W1) Firstly, It would significantly help in include "Dataset Pruning" rather than just "Pruning" in the title of the paper, because given the dominence of "model pruning" methods, it is very understandable that one might get confused by the title. One suggestion would be DRoPD (.... Pruning Datasets).

(W2) Secondly, the problem of "classification bias" is never really defined in the paper, that is, it is never explained what is meant by "classification bias" and why is it a problem and how datasets affect this so-called "classification bias".

(W3) Next, the use of the word "Robustness" seems incorrect in this context. It is not really "robustness" being evaluated but class-wise fairness. Might be prudent to frame the paper differently around this.

(W4) Lastly, the evaluations are limited to non-robust small models like VGG-16, VGG-19, ResNets up to ResNet50. However, it has been seen that large models like ResNet101, ConvNeXt-B onwards, and ViT based large models are more robust to distribution changes. They might be more robust to underrepresentation of classes as well, or might not show gains when using the proposed "DRoP" method. Thus having experimental evaluations with these models would help better understand the applicability of the proposed method.

### Questions
Q1- In Figure 9 (leftmost plot), when dataset sparisty is more than 50% (density less than 0.5) why is the proposed DRoP significantly less stable than all the other methods? Some explaination for this would be very helpful.

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the effect of dataset pruning on classification bias for several existing methods using the metrics of worst-class accuracy, difference between best and worst class accuracy, and standard deviation. Due to the purported worsening of worst-class accuracy at the cost of better average performance, the paper proposes random pruning based on error rates on a holdout set which is motivated by a theoretical analysis of a simple 1-D mixture of two Gaussians. Experimental analysis is conducted on CIFAR10, CIFAR100, TinyImageNet and ImageNet datasets for the various settings.

### Strengths
1. The presented theoretical analysis on the GMM for minimizing worst-case statistical risk and average risk is good and aligns with the proposed pruning method.
2. The experimental analysis is comprehensive and convincing.

### Weaknesses
1. While the Random+DRoP method does reduce classification bias compared to existing dataset pruning strategies, it generally seems to do slightly worse on average accuracy (Figure 5). The combined Strategy+DRoP seems to mitigate this a bit but the trend is not clear.
2. The experiments do not always indicate such a clear and striking trend towards robustness as the authors suggest. Some aggregate scalar numbers might be beneficial to understand which strategy does better across all data densities.
3. in Figure 6, right, why does a higher negative correlation of class accuracy to class density indicate more robustness? Ideally class accuracy should have zero correlation with class density for a model invariant to class size.

### Questions
1. in Figure 6, right, why does a higher negative correlation of class accuracy to class density indicate more robustness? Ideally class accuracy should have zero correlation with class density for a model invariant to class size.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies classification bias in data pruning. It first provides a systematic study of the existing methods and shows that they are all biased to some extent. To this end, the authors propose DRoP, a distributionally robust approach for pruning that preserves good robustness against classification bias. Their method achieves state-of-the-art robustness performance when combined with random subsampling across different settings.

### Strengths
- The proposed method DRoP is quite concise, which is highly appreciated since it can potentially increase the accessibility and applicability of the method beyond the current scope.
- Despite its simplicity, DRoP + random sampling achieves superior performance across various settings.
- The paper conducts a systematic evaluation of the existing data pruning methods and reveals a valuable conclusion that none of the existing methods actually has good robustness in terms of classification bias.
- The evaluation covers a wide range of scenarios beyond the classic data pruning, which enhances the importance of the method as it could lead to potential influence that extends beyond traditional use cases.
- The discussion of the limitations and future work is sound and makes sense.

### Weaknesses
 - The flow of the paper can be improved. At the moment it feels that the related work is scattered throughout the paper, which disrupts readability and makes it challenging to grasp. It would be clearer to bring all of the related work into one section and then refer back to it when needed in the experiment section. For example, the authors may group related work into categories like "Data Pruning Methods", "Robustness and Fairness", "Long-Tailed Recognition Techniques", and "Robust Data Pruning Methods", and place this consolidated section after the introduction.

- Since there is no standalone related work section, it is difficult to assess the novelty of the proposed method and the relation with existing data pruning techniques. It would be great to also include a brief discussion of the most recent advancements in data pruning and how DRoP is similar to/different from them.

- The robustness evaluation on imbalanced datasets and group distributional robustness is not compared with the methods from the corresponding fields. It would be great if the performance of some task-specific methods is also compared in Figures 8 and 9, which helps to better assess the method's relative performance in context. For example, [1,2] for "imbalanced datasets" and [3,4] for "group distributional robustness"

### Questions
- It is quite impressive that Random + DRoP outperforms other methods when the overall dataset density is low (e.g. in Figure 5). But do the authors have an idea why in many cases, it gives inferior worst-class performance when the overall dataset density is high? For example, for ResNet18 + TinyImageNet at 90% density, Random + DRoP is the second worst performance (only better than Forgetting) in terms of the worst-class performance in Figure 5.

### Soundness
3

### Presentation
3

### Contribution
3
