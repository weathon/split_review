# Boosting Semi-Supervised Learning via Variational Confidence Calibration and Unlabeled Sample Elimination

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Despite the recent progress of Semi-supervised Learning (SSL), we argue that the existing methods may not employ unlabeled examples effectively and efficiently. Many pseudo-label-based methods select unlabeled examples into the training stage based on the inaccurate confidence scores provided by the output layer of the classifier network. Additionally, most prior work typically adpots all the available unlabeled examples without data pruning, which is incapable of learning from massive unlabeled data. To address these issues, this paper proposes two methods called VCC (Variational Confidence Calibration) and INFUSE (INfluence-Function-based Unlabeled Sample Elimination). VCC is a general-purpose plugin of confidence calibration for SSL. By approximating the calibrated confidence through three types of consistency scores, a variational autoencoder is leveraged to reconstruct the confidence score for selecting more accurate pseudo-labels. Based on the influence function, INFUSE is a data pruning method for constructing a core dataset of unlabeled examples. The effectiveness of our methods is demonstrated through experiments on multiple datasets and in various settings. For example, on the CIFAR-100 dataset with 400 labeled examples, VCC reduces the classification error rate of FixMatch from 46.47\% to 43.31\% (with improvement of 3.16\%). On the SVHN dataset with 250 labeled examples, INFUSE achieves 2.61\% error rate using only 10\% unlabeled data, which is better than RETRIEVE (2.90\%) and the baseline with full unlabeled data (3.80\%). Putting all the pieces together, the combined VCC-INFUSE plugins can reduce the error rate of FlexMatch from 26.49\% to 25.41\% on the CIFAR100 dataset (with improvement of 1.08\%) while saving nearly half of the original training time (from 223.96 GPU hours to 115.47 GPU hours).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies semi-supervised learning (SSL). This paper points out two issues of existing SSL methods, including 1) the incorrect pseudo labels caused by calibration error, 2) the huge computation cost in training. To address the first issue, this paper proposes Variational Confidence Calibration (VCC), a variational method to obtain the calibrated confidence scores for pseudo-label selection. To address the second issue, this paper proposes the INfluence Function-based Unlabeled Sample Elimination (INFUSE) method, which uses the influence function to compute the importance of each unlabeled example. The two methods can be combined together to achieve high prediction accuracy with lower training costs. Experimental results demonstrate the effectiveness of the proposed methods.

### Strengths
- The writing is very clear.
- The proposed two methods are reasonable. There is an important advantage of VCC, i.e., it can be plugged into existing SSL methods to enhance their performance.
- Experimental results and ablation studies support the proposed methods.

### Weaknesses
 - The proposed methods seem not novel enough, because they are only adapted from existing techniques, i.e., Variational Auto Encoder and Influence Function. It is intuitive that such a combination method can work well and thus I cannot see any important insights brought by the two methods. Specifically, the VCC method appears to be a straightforward application of a VAE to model the distribution of pseudo-labels, which is not a novel approach in itself. Similarly, the use of influence functions for data selection is a well-established technique, and its application to unlabeled data in SSL, while practical, does not present a significant conceptual leap.
- I do not think it is a good strategy to address two independent problems of SSL together, which may not increase the contributions of this paper. A good paper is supported by an important finding/contribution. Two independent minor contributions to address different issues may not form a single significant contribution. The connection between the two methods, as presented, seems superficial. Simply stating that both methods aim to reduce resources does not establish a deep, meaningful link. A more compelling argument would be needed to justify combining these two distinct approaches into a single paper. It would be more impactful to focus on a single, significant problem and provide a more in-depth and novel solution.
- In some tables, only a single result (without using mean$\\pm$std) is provided. I suggest further providing standard deviations.

### Questions
Please check the above weaknesses.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new semi-supervised learning technique which is based on "variational confidence calibration" (for calibrating the predictions on unlabeled examples) and "unlabeled sample elimination" (for pruning data with the goal to decrease the running time of the method). The main contributions of this paper are as follows:

(i) The authors propose the Variational Confidence Calibration (VCC) method, which aims to obtain well-calibrated scores for pseudo-label selection. The method is based on computing three different scores (ensemble consistency, temporal consistency view consistency), appropriately combining them, and feeding them to a (trainable) variational auto encoder  to get the final calibrated score. The resulting score can be used in combination with other standard/SOTA semi-supervised learning techniques.

(ii) The author propose the INFUSE method, which can dynamically prune unimportant unlabeled examples, in order to speed up  the convergence and reduce the computation costs in training.

(iii) Extensive experimental evaluation showing the competitiveness of the proposed method with respect to other SOTA methods.

### Strengths
— This is a well-written paper that proposes an interesting approach to semi-supervised learning. 

— The use of the VAE in the computation of the calibrated scores is a novel and intriguing idea.

— Extensive experimental evaluation showing SOTA results in various datasets. In a few cases the performance gains (in terms of test-accuracy) are quite significant, e.g. in the CIFAR-100 dataset with 400 labeled examples VCC reduces the classification error rate of FixMatch from 46.47% to 43.31% (with improvement of 3.16%).

### Weaknesses
— The performance gains of using the method (in terms of test-accuracy) are typically somewhat mild, and often times less than 0.5%. While the authors demonstrate improvements on CIFAR-100 with limited labels, the general trend across various datasets and label settings shows only marginal gains in accuracy. This raises concerns about the practical significance of the method in scenarios where high accuracy is paramount, as the computational overhead might not justify the small improvements in many cases.

— The method seems to be a bit involved, especially given the typical overall benefit. The introduction of a variational autoencoder (VAE) for calibrating scores, combined with the dynamic pruning of unlabeled examples, adds complexity to the training pipeline. This increased complexity might make the method less appealing for practitioners seeking simpler and more efficient solutions, especially when the performance gains are not consistently substantial.

### Questions
Have the authors tried to apply their method in larger datasets like Imagenet? (I know that many of the SOTA semi-supervised learning approach suffer in the case of many classes/ large scale datasets this is why I am asking.)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes two methods, VCC and INFUSE, to improve semi-supervised learning by better utilizing unlabeled data. The effectiveness of these methods is demonstrated through experiments on multiple datasets. Overall, these methods offer promising solutions for improving the efficiency and accuracy of SSL.

### Strengths
Originality:
- The manuscript proposes two novel methods, VCC and INFUSE, to improve semi-supervised learning by better utilizing unlabeled data. These methods are designed to address the challenges of leveraging large-scale unlabeled data in SSL, and they offer promising solutions for improving the efficiency and accuracy of SSL.

Quality:
- The manuscript provides a thorough and well-organized presentation of the proposed methods, including detailed descriptions of the models, algorithms, and experiments. The experiments are conducted on multiple datasets and in various settings, and the results demonstrate the effectiveness of the proposed methods.

Significance:
- The proposed methods have the potential to significantly improve the efficiency and accuracy of SSL, which is an important and challenging problem in machine learning. The manuscript discusses the potential for extending the proposed methods to other SSL tasks, suggesting that they have broad applicability and potential impact in real-world scenarios.

### Weaknesses
1. The manuscript has some issues with the expression of details, making it difficult to follow. For example, the article does not provide an introduction to the first two loss terms in Eq. (11). Specifically, it is unclear what the exact form of the cross-entropy loss is for both the labeled and unlabeled data, and how pseudo-labels are generated and used in the unlabeled loss term. The lack of clarity makes it difficult to reproduce or fully understand the method.
2. The latter part of the method involving INFUSE in the manuscript, and the earlier part on confidence calibration, seem to address two completely different problems, giving the paper a scattered feel and failing to highlight the main focus of the work. This leaves an impression of breadth over depth. The connection between the two is not well-motivated, and it is unclear why these two seemingly disparate techniques are combined in a single framework. The paper would benefit from a more cohesive narrative that ties these components together.
3. The author mentions that 'INFUSE uses the influence function from Koh & Liang (2017) to compute the importance of each unlabeled example', which implies that the solution to the second issue addressed in the manuscript merely references someone else's strategy. Both the problem itself and the method of solving it lack novelty. The paper does not adequately explain how the influence function is adapted to the semi-supervised setting, and how it differs from the original formulation, beyond a high-level mention of using unlabeled data. The specific modifications and their impact should be detailed.
4. The part on VIEW CONSISTENCY seems somewhat strained. Firstly, obtaining multiple views is difficult, and moreover, the EMA in the manuscript doesn't really have any connection with multiple views. EMA has already been showcased in the TEMPORAL CONSISTENCY section. The use of EMA to generate different views is not well-justified, and the connection to the concept of 'views' is tenuous. The paper should clarify how the EMA models are sufficiently different to be considered as distinct views, and why this approach is superior to other multi-view learning techniques.
5. There is an issue in the reconstruction loss, where $\tilde{r}$ is treated as ground-truth; this itself is not accurate enough. The paper does not address the potential inaccuracies introduced by using a noisy reconstruction target, and how this might affect the overall performance of the method. The use of a VAE to address this is mentioned but not detailed, and the paper should provide more information on how the VAE mitigates the problem of inaccurate reconstruction targets.

### Questions
1. I don't quite understand “we argue that the optimizing function in RETRIEVE only considers the loss on the labeled training set, which may lead to a deviation from the desired results (i.e. minimizing the loss on the validation set)”, could you please explain it in detail?
2. The author mentioned that " Although both consider the problem from the perspective of time, our temporal-consistency method is very dissimilar from the time-consistency method proposed by Zhou et al. (2020)." in Sec 3.2. Please give a detailed explanation and analysis.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study centers on pseudo labeling within the context of semi-supervised learning. To tackle the issue of inaccurate confidence scores and abundant unlabeled examples without data pruning, the author proposes two strategies of variational confidence calibration (VCC) and influence-function-based unlabeled sample elimination (INFUSE). Empirical assessments conducted on widely-adopted benchmark datasets demonstrate the efficacy of these proposed strategies. Notably, VCC yields a remarkable 3.16% reduction in error rates when compared to FixMatch.

### Strengths
1. The proposed strategies bolster pseudo labeling by addressing two key facets: computing dependable confidence scores and judiciously selecting a subset of the unlabeled dataset. These innovations result in a significant enhancement of generalization performance while also substantially reducing computational overhead in practical applications.
2. The writing is commendable, making the method easily comprehensible. The author offers ample experimental details, thereby facilitating the reproducibility of the study.

### Weaknesses
1. The novelty of the method appears somewhat constrained. Several components of the approach, such as Monte-Carlo Dropout, temporal consistency, exponential moving average, variational auto-encoder, and influence functions, are established techniques in the field. The combination of these techniques, while potentially effective, does not represent a significant conceptual leap. The core idea of using consistency measures for calibration is not entirely new, and the specific implementation using VAEs, while interesting, does not fundamentally change the landscape of semi-supervised learning.
2. The effectiveness of the Variational Autoencoder (VAE) implementation raises questions. VAE's main advantage lies in introducing randomness, and the efficacy of its calibration may require further substantiation. Specifically, the use of VAEs for confidence calibration seems to rely on the assumption that the latent space captures the uncertainty of the model, which is not always guaranteed. Additionally, the improvements achieved through VAE, as evidenced in Table 7, seem marginal at best, and it is not clear if the added complexity of the VAE is justified by the performance gains.

### Questions
1. The author's proposal to generate ground-truth labels using a mixup-based method raises a valid concern about the dataset's stability during training. It's essential to verify whether the constructed labeled dataset remains invariant throughout the training process.
2. Table 9 in Appendix F.2 highlights the dominance of temporal scores in the experiments. It would be beneficial if the author could provide an explanation for this observation, shedding light on the reasons behind the temporal score's strong performance.
3. Suggestions for improvement: 1) Placing the table title above the table itself would enhance the document's readability. 2) Updating the template, especially for the page header, would contribute to a better presentation of the work.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
