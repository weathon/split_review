# EXCOST: Semi-Supervised Classification with Exemplar-Contrastive Self-Training

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Similar to the way of human learning, the aim of semi-supervised learning (SSL) method is to harness vast unlabeled data alongside a limited set of labeled samples. Inspired by theories of category representation in cognitive psychology, an innovative SSL algorithm named Exemplar-Contrastive Self-Training (EXCOST) is proposed in this paper. This algorithm ascertains pseudo-labels for unlabeled samples characterized by both substantial confidence and exemplar similarity, subsequently leveraging these pseudo-labels for self-training. Furthermore, a novel regularization term named Category-Invariant Loss (CIL) is applied for SSL. CIL promotes the generation of consistent class probabilities across different representations of the same sample under various perturbations, such as rotation or translation. Notably, the proposed approach does not depend on either the prevalent weak and strong data augmentation strategy or the use of exponential moving average (EMA). The efficacy of the proposed EXCOST is demonstrated through comprehensive evaluations on semi-supervised image classification tasks, where it attains state-of-the-art performance on benchmark datasets, including MNIST with 2, 5 and 10 labels per class, SVHN with 25 labels per class, and CIFAR-10 with 25 labels per class.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a semi-supervised learning (SSL) algorithm called Exemplar-Contrastive Self-Training (EXCOST).  EXCOST determines pseudo-labels for unlabeled data with high confidence and exemplar similarity for self-training. The paper also presents a novel regularization term known as Category-Invariant Loss (CIL) to enhance the consistency of class probabilities across different representations of the same sample under various perturbations. The paper achieves state-of-the-art results on semi-supervised image classification tasks across various benchmark datasets, such as MNIST, SVHN, and CIFAR-10.

### Strengths
1. The paper is easy to follow and well-structured.
2. The proposed components; Category-Invariant Loss and exemplar-contrastive self-training is novel to some extent.
3. The experiments, including the appendix, are thorough and well-designed, providing comprehensive results across all settings.
4. The listed performance demonstrates the effectiveness of the proposed method, significantly improving performance compared to the previous one.

### Weaknesses
1. One potential limitation of the Category-Invariant Loss (CIL) is its sensitivity to the choice of the threshold parameter. The text acknowledges that the threshold is introduced to manage the influence of irrelevant or outlier samples. However, determining the appropriate threshold value may not be straightforward and can significantly impact the loss function. Specifically, the paper does not provide a clear methodology for selecting this threshold, and it is unclear how the performance would vary with different threshold values, especially across diverse datasets with varying class distributions and complexities.

2. The exemplar-contrastive self-training algorithm involves several hyper-parameters, including thresholds, margin values, and labeling rates. The sensitivity of these hyper-parameters could present challenges during practical implementation, as selecting the right values may require thorough experimentation and tuning. The paper lacks a detailed analysis of how these parameters interact and influence the final performance. For instance, the interplay between the confidence threshold and the exemplar similarity threshold in determining pseudo-labels is not thoroughly explored, which could lead to instability or suboptimal performance if not carefully tuned.

3. While the paper mentions that the computational burden is reduced by deferring the computation of exemplar feature vectors until the labeling phase, it lacks a comprehensive analysis of the algorithm's computational efficiency. The practical implications and potential computational overhead of the entire algorithm should be subject to in-depth investigation and evaluation. The paper does not provide a detailed breakdown of the time complexity of each step, such as the exemplar feature vector computation, the pseudo-label generation, and the CIL calculation. This makes it difficult to assess the scalability of the method for larger datasets or more complex models.

### Questions
Please address my concerns

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a semi-supervised learning (SSL) algorithm called Exemplar-Contrastive Self-Training (EXCOST) with the aim of enhancing the quality of pseudo-labels for unlabeled samples. Additionally, they propose a Category-Invariant Loss, which encourages the model to produce consistent class probabilities for the same sample under different perturbations.

### Strengths
The idea of Exemplar-Contrastive Self-Training is interesting to me.  It generates more reliable pseudo-labels by combining measures of confidence and exemplar similarity.

### Weaknesses
1.	Effectiveness: While the concept is interesting, the paper falls short in terms of performance when compared to SOTA methods. Notably, the proposed method exhibits considerably higher error rates on CIFAR-100 in comparison to other techniques. The performance gap on CIFAR-100 is a significant concern, suggesting the method may not generalize well to more complex datasets or that the hyperparameter tuning was insufficient for this particular dataset. The paper should include a more detailed analysis of why EXCOST underperforms on CIFAR-100, perhaps investigating the impact of the increased number of classes or the higher image complexity. Furthermore, the paper lacks a discussion on the computational cost associated with EXCOST compared to other methods. This is important for practical applications, as a method that achieves good performance but is computationally expensive may not be suitable for all scenarios.
2.	Writing Quality: The clarity of the paper's presentation could be improved. For instance, in Table 1, there's a mix of reporting styles, with some methods providing the median error rate of the last 20 epochs, while others report the minimum error rate across all epochs. This inconsistency makes it challenging to make direct comparisons. The lack of a standardized evaluation protocol hinders a fair comparison between the proposed method and existing techniques. The paper needs to clearly state the evaluation method used for each reported result, and justify the choice of using different evaluation methods for different baselines. This makes it difficult to assess the true merit of the proposed approach.
3.	Experiment Setup and Results: To enhance the paper's organization, it's advisable to present the primary results in the main paper, while relocating additional details, like the results of the ablation study, to the appendix. This will streamline the main paper and maintain a focused narrative. The current structure of the paper makes it difficult to quickly grasp the core contributions and performance of the proposed method. The reader has to sift through the ablation study results to understand the overall performance of the method. The main results should be presented clearly and concisely in the main body of the paper, with the ablation study results moved to the appendix to support the main claims.

### Questions
Please see Weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Semi-supervised learning (SSL) is a hot topic in machine learning. To generate high-quality pseudo-labels for unlabeled data, this paper proposes an Exemplar-Contrastive Self-Training (EXCOST) method along with a category-invariant loss for the model’s training.

### Strengths
+ An exemplar-contrastive self-training method for SSL is proposed to achieve trust-worthy pseudo-labeling.
+ A category-invariant loss is designed to encourage models to produce the similar probability distribution for different-view samples. 
+ Experiments on several benchmarks have demonstrated the effectiveness of the proposed method.

### Weaknesses
 - The motivation is not clear. Why combine prototype and exemplar information to improve the quality of pseudo-labels? The first paragraph does not explain well the role of this combination in semi-supervised learning. Specifically, the paper lacks a clear explanation of how the complementary strengths of prototypes (generalization) and exemplars (specificity) are leveraged to overcome limitations in existing pseudo-labeling approaches. The connection to cognitive psychology is mentioned but not convincingly translated into a concrete technical argument for the proposed method.
- The novelty of this manuscript seems to be limited. The authors should discuss the relation between existing methods and the proposed method in details. The paper needs to more clearly articulate how the proposed method differs from existing self-training and consistency regularization techniques. A more thorough comparison with methods like UDA, MPL, and FixMatch is needed, with a focus on the specific technical differences and advantages of the proposed approach.
- The organization and the writing of this manuscript should be largely improved for a clear understanding. The paper lacks a clear and concise narrative, making it difficult to follow the technical details and understand the overall contribution. The structure should be revised to improve the logical flow of ideas and to enhance the readability of the paper.
- The authors claim that as training progresses, more pseudo-labeled samples are incorporated into the learning process. However, there are no results to prove the point. The paper needs to provide empirical evidence to support this claim, demonstrating the increase in pseudo-labeled samples over the course of training. This could be done via a plot or a table showing the number of pseudo-labels used at different training stages.
- The ablation study is confusing. Moreover, most of the results in Table 1 remain blank. The ablation study needs to be significantly improved, with a clearer explanation of the different ablation settings and comprehensive results for all settings. The absence of results for many baseline models on MNIST raises questions about the completeness of the experimental evaluation.
- Some experimental details are missing, e.g., the threshold in Eq. (1). The paper needs to include all necessary experimental details, including the specific values for hyperparameters and the implementation details of the proposed method. The lack of this information makes it difficult to reproduce the results.

### Questions
Please refer to the Weaknesses.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel semi-supervised learning (SSL) algorithm called Exemplar-Contrastive Self-Training (EXCOST). The primary goal of this algorithm is to enhance the reliability of pseudo-labels by considering both high confidence and exemplar similarity. Additionally, the paper presents a unique regularization term known as Category-Invariant Loss (CIL), which aims to encourage consistent class probabilities for the same sample under various perturbations.

### Strengths
1. The proposed approach is independent of prevailing weak and strong data augmentation strategies and does not rely on the use of exponential moving averages.
2. The effectiveness of the proposed EXCOST is demonstrated through comprehensive evaluations in semi-supervised image classification tasks.

### Weaknesses
1. Integrating the concept of contrastive learning into semi-supervised learning is not a novel approach, and several similar studies have been conducted previously [1,2,3,4]. The authors should analyze and experimentally compare their method with these previous approaches.

2. As mentioned in the previous question, the Related Work in this paper is not comprehensive, lacks a summary and analysis of prior work, and fails to highlight the contributions of this paper.

3. The experimental section lacks an introduction to baseline methods, and many experimental results are missing from Table 1. It would be preferable for the authors to mark the missing results with horizontal lines.

4. The author's expression is inconsistent. In the first paragraph of the Introduction, the author states that the exemplars theory emphasizes the uniqueness of different samples within the same category. However, in Section 3.2, the author claims that the exemplars theory suggests that samples of the same class should be similar, and pseudo-labels are calculated based on the similarity between samples and exemplars. It is unclear how the uniqueness of samples is reconciled with this.

5. The nomenclature in this paper should be more standardized. For instance, do ${\Phi _c}$ and ${\phi _c}$ represent the same thing?

6. The article is difficult to understand, and the authors should restate the motivation of this paper and clarify the relationship between motivation and the proposed method. For example, how are prototype theory and exemplar theory reflected in the methodology, and what role does the typicality gradient play in this paper?

### Questions
Please refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
