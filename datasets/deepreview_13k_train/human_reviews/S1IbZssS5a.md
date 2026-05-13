# Learning Imbalanced Data with Beneficial Label Noise

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Data imbalance and label noise are common factors hindering the classifier's performance. Data-level approaches to addressing imbalanced learning usuallyinvolve resampling by adding or removing samples, which often results in information loss or generative errors. Building upon theoretical studies of the impact of imbalance ratio on decision boundaries across various evaluation metrics in binary classification, it is uncovered that introducing appropriate label noise can alter the biased decision boundaries and thus enhance the performance of classifiers in imbalanced learning. In this paper, we introduce the Label-Noise-based Re-balancing (LNR) approach to solve both binary and multi-class imbalanced classifications by employing a novel design of asymmetric label noise model. In contrast to other data-level methods, our approach is easy to implement and alleviates the issues of informative loss and generative errors. We validated the superiority of this method on synthetic and real-world datasets. More importantly, our LNR approach can integrate seamlessly with any classifiers and other algorithm-level methods for imbalanced learning. Overall, our work opens up a new avenue for addressing imbalanced learning, highlighting the potential advantages of balancing data through beneficial label noise.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposed a method for dealing with class imbalance. The main problem with imbalanced datasets is that most labels are from the minority class and few of them are from the majority class. To deal with this, the authors proposed to flip some of the labels in order to balance the dataset and improve the performance of classification models. Moreover, the authors extended their method to multi-class classification problems. Finally, the numerical experiments showed promising results for the method, in a wide range of datasets, including tabular data classification and image data classification problems.

### Strengths
The method is generic enough to be used in any classification problem in machine learning, that involves imbalanced data. The numerical experiments demonstrate the value of the method in both tabular data and image data classification problems. 

The method has been successfully applied in a very large number of datasets, including 32 tabular datasets and 2 image datasets, and has shown promising results. 

The authors extended the method to multi-class classification problems and proposed an efficient training procedure using online label noise.

### Weaknesses
The label flipping approach can have a negative impact on the classifier's ability for predicting the majority class. 

The flipping decisions of Algorithm 1 are determined based on another classification model (C_f) that is trained on the original imbalanced dataset and therefore they can carry out any error it might have.  

What if the distribution of the majority class is very different from that of the minority class ? Would the label flipping approach make sense in this case?

### Questions
Can you comment on the effect on out of sample accuracy from your method ? My intuition is that if the test data have the same imbalance ratio as the training data, then accuracy should be worsened from that of the nominal model, while if the test data are more balanced than the training data, then it should be improved.

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
The paper presents a novel approach called Label-Noise-based Rebalancing (LNR) to address the challenges posed by imbalanced data and label noise in classification tasks. The authors argue that traditional methods, such as resampling, often lead to information loss and generative errors. They propose that introducing beneficial label noise can help adjust biased decision boundaries, thereby improving classifier performance, particularly for minority classes. The LNR method employs an asymmetric label noise model that selectively flips labels of majority class samples to minority classes, aiming to enhance the performance of classifiers in both binary and multi-class settings. The authors validate their approach through extensive experiments on synthetic and real-world datasets, demonstrating its effectiveness compared to existing methods.

### Strengths
1. The paper is well structured and the introduced idea is interesting.
2. The paper offers a solid theoretical analysis of how data imbalance affects decision boundaries.
3. The LNR method is designed to be easily integrated with various classifiers and algorithm-level methods.

### Weaknesses
1. The paper could benefit from more detailed implementation guidelines for the label noise model to enhance reproducibility. Specifically, the method for selecting which majority class samples to flip, and the exact mechanism for determining the magnitude of the label change (especially in multi-class settings) are not sufficiently described. This lack of detail makes it difficult to independently verify the results.
2. The paper does not compare with some latest methods on class imbalance. While the authors mention resampling techniques, they fail to benchmark against more recent state-of-the-art methods that directly address class imbalance through cost-sensitive learning or advanced data augmentation techniques. This omission makes it difficult to assess the true novelty and effectiveness of the proposed approach.
3. Some results could be presented more clearly, with additional explanations or context to help readers understand the significance of the findings. For instance, the performance gains on certain datasets are not clearly linked to specific characteristics of those datasets, making it difficult to generalize the findings. Furthermore, the statistical significance of the improvements should be explicitly stated.

### Questions
1. How can practitioners effectively estimate the flip-rate for different datasets? Are there specific guidelines or heuristics that can be followed?
2. How does the LNR method perform with larger datasets or in high-dimensional spaces? Are there any computational limitations or considerations?
3. How does LNR compare with other emerging techniques in imbalanced learning that also aim to modify decision boundaries or utilize noise?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method called Label-Noise-based Re-balancing (LNR) to address the data imbalance problem by introducing label noise in the majority class samples in a classification task. The method aims to adjust the decision boundary and thus improve the classification accuracy of the minority class. The authors provide a detailed theoretical analysis of how label noise can mitigate the effects of class imbalance on decision boundaries. Extensive experimental results are reported in the main text and appendices, which seem to indicate that LNR demonstrates strong performance across a wide range of datasets and is applicable to various classifiers.

### Strengths
1) This paper explores a new method to handle imbalanced data in classification tasks by introducing asymmetric label noise, rather than relying solely on traditional resampling methods or algorithm-level adjustments. This noise-based method avoids information loss or generative errors.
2) The paper presents comprehensive mathematical proofs to demonstrate how class imbalance influences decision boundaries and how the proposed method helps to mitigate these effects. Overall, the paper is well-organized, with clear and accessible writing.

### Weaknesses
1) Regarding the class imbalance problem, more recent studies can be easily found in Google Scholar or DBLP and should be reviewed and compared (if possible). However, this paper completely ignores the studies after 2022, which cannot strongly support the contributions and innovations of this paper.
2) Regarding the method, the idea of training a classifier after dividing majority class samples near the decision boundary into the minority class to improve the classifier’s performance on the minority class lacks novelty. Additionally, the proposed method still depends on an parameter $t_{flip}$ to complete the division, without an automatic strategy for optimal division, limiting the proposed method’s contribution.
3) Regarding the experimental validation, the chosen experimental metrics and experimental results are not convincing enough. Mislabeling some majority class samples near the decision boundary as minority class samples naturally increases the number of samples classified as the minority class. This, in turn, unsurprisingly boosts the recall of the minority class and the precision of the majority class. These results can not effectively validate the proposed method. Conversely, the improvement of the proposed method is very limited in terms of the metrics that reflect the overall performance (such as "Acc_{overall}" in Table 1 and "Overall" in Table 2).

### Questions
In addition to the weaknesses I have already listed, I have the following questions:
1) Since the proposed method is intended to be effective across various classifiers, why is MLP specifically chosen as the flip-rate estimator $C_f$ (see "Our method, LNR, adapts the final layer of the MLP classifier to include a soft-max function as the flip-rate estimator $C_f$" in lines 433-434)? This setup could make KNN’s performance improvement rely on MLP’s performance. Table 5 in the appendix raises this concern, as MLP’s original performance is even better than the improved KNN results.
2) What is the difference between "method", "approach", and "methodology" in this paper, and in what context are these different terms used to describe the proposed method LNR (such as "this method" in line 23, "our LNR approach" in lines 23-24, and "a novel methodology" in line 147)?
3) Does the proposed LNR have any limitations, and if so, in what context do they arise? Limitations of the method should be noted and discussed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Label-Noise-based Rebalancing (LNR) method to address both binary and multi-class imbalanced classification by using an asymmetric label noise model. Unlike conventional data-level methods, which often suffer from information loss and generative errors, LNR rebalances data by flipping the labels of majority class samples. This technique improves the recognition of minority class samples and can be seamlessly integrated with any classifier or algorithm-level methods. Additionally, the authors provide a theoretical analysis of how label noise affects classifiers, proposing that controlled noise can boost imbalanced learning without the downsides of traditional resampling methods. Experimental results demonstrate the superiority of LNR.

### Strengths
1. This paper presents a simple and effective method for addressing data imbalance, and the article is highly readable, making it easy to follow the idea.

2. This paper provides a theoretical analysis of the proposed method and validates the effectiveness of the proposed label-flipping approach.

3. The authors conducted extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses
This paper may still have some shortcomings in terms of theoretical analysis and experimental results.

1. The label-flipping method is merely considered a trick, essentially no different from the Mixup strategy [1], and it may disrupt the original data distribution and the feature extraction process [2].

[1] H.  Zhang, M.  Cisse, Y. N.  Dauphin, D. Lopez-Paz,   Mixup: Beyond Empirical Risk Minimization, ICLR 2017.

[2] B.  Zhou,  Q.  Cui,   X.  Wei,   Z. Chen,  BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition, CVPR 2020.  

2. While the theoretical analysis strengthens the persuasive power of the label-flipping technique, it is focused on binary classification, and whether it can be correctly extended to multi-class problems requires further discussion and analysis.

3. Since GCL is used as the baseline, but the experimental strategy differs significantly from the original GCL paper, there are some doubts regarding the validity of these experimental results.

4. By manually manipulating labels, the model might develop an unintended bias towards specific classes, especially in cases where the balance is artificially created through extensive relabeling. This could skew predictions and reduce the fairness of the model across different classes. It would be better if the authors could provide the confusion matrix result on CIFAR10-LT datasets.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
