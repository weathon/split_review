# Preventing Unintended Memorization by Covering with Over-Memorization

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
From the advances of deep learning, the privacy concerns of deep neural networks are in the limelight. A particular concern is  privacy of the training data, which is often compromised by the model's inherent memorization capabilities. Suppressing such memorization can enhance privacy but introduces two main challenges: 1) removing a memorized instance from the training dataset will result in the model to memorize another instance instead, and 2) the memorization is essential for improving the generalization error. To address these challenges, we propose an over-memorization method that involves training the model with both the standard training set and a set of redundant, non-sensitive instances. Our method leverages the model's limited memorization capacity to focus on irrelevant data, thereby preventing it from memorizing the training data. Our empirical results demonstrate that this method not only enhances protection against membership inference attacks but also minimizes the loss of utility by effectively redirecting the model's generalization efforts towards non-sensitive instances.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper designs a new approach to mitigate the privacy-utility trade-off of ML models. Specifically, the authors propose to first synthesize a dummy dataset that can simulate the properties of the original training dataset, and then train ML models on this synthesized dummy dataset. The authors claim that since the dummy dataset does not contain original training samples, thus it can protect the privacy of original training data. Besides, since the dummy dataset can simulate the original training dataset well, models trained on it can also gain strong enough generalizability. Experiments are conducted on the image classification task and the text generation tasks and evaluated with a memorization metric and a membership inference attack (i.e., LiRA).

### Strengths
1. This paper is well-written and easy to follow.

2. Experiments are conducted not only on simple image classification tasks but also on language generation scenarios, which I appreciate.

### Weaknesses
1. I have two main concerns related to "dataset condensation" [r1]:
    - The idea of using synthesized dummy datasets to simulate real-world datasets is very similar to the concept of "dataset condensation" (or say "dataset distillation") which first appeared in 2021 [r1]. See also a survey [r2] for more details. So I think the authors should discuss what is the difference between their dummy dataset method and dataset condensation and also add several recent dataset condensation methods as baselines for comparison [r1, r3, r4]. Specifically, the authors should clarify how their method differs in terms of the optimization objective, the nature of the synthesized data (e.g., discrete vs. continuous, constrained vs. unconstrained pixel values), and the computational cost. Furthermore, the comparison should include a quantitative analysis of the trade-offs between privacy and utility compared to these methods, such as the performance of the dummy dataset under different levels of compression or synthesis. 

    - Another main concern is using a synthesized training dataset (or say using "dataset condensation") to preserve privacy has already been studied in 2022 by [r4]. Worse still, [r5] further shows that [r4] might not be able to protect data privacy as the method by [r4] does not have correct DP-based privacy accounting and simple privacy attacks can easily defeat it. Given that the proposed dummy dataset method does not even have any privacy accounting but only empirical analysis with privacy attacks, I don't have enough confidence that it can indeed enjoy a strong privacy-preserving ability (since it may be defeated by another privacy attack as it does not have any theoretical privacy-preserving guarantee). The authors need to address the lack of formal privacy guarantees and provide a more rigorous analysis of potential privacy vulnerabilities, especially considering the findings of [r5]. The empirical evaluation should also include more sophisticated attacks beyond basic membership inference, such as attribute inference or model inversion attacks.

2. In the experiments, since the proposed dummy dataset method is a kind of privacy-preserving method, I think in Table 2 and Table 3 the authors should compare their proposed method with DP-SGD baselines. This comparison is crucial to understand the relative performance of the proposed method against a well-established privacy-preserving technique. It would be beneficial to see how the accuracy and privacy trade-offs of the dummy dataset method compare with those achieved by DP-SGD under various privacy budgets.

3. I think the authors should add experiments similar to Table 2 and Table 3 for the CIFAR-100 dataset. This would demonstrate the robustness and generalizability of the proposed method across different datasets with varying complexities and number of classes.

4. In Line#4 of Algorithm 2, why do you need to update the model parameter $\tilde \theta$ with gradients calculated on the dummy set $S_d$? I think it is necessary to include an intuitive explanation and an ablation study on this gradient term. Specifically, it is unclear why the model parameter \(\tilde{\theta}\) which is only used to train the dummy set needs to be updated using the dummy set itself. An ablation study should examine the impact of this update on the quality of the dummy dataset and the final model performance. It would be helpful to see how the performance changes when this update is removed or replaced with different update mechanisms.

5. In Table 2, why the test accuracy of clean-trained ResNet-18 on the CIFAR-10 dataset is as low as 87.58%? To the best of my knowledge, one can easily train a ResNet-18 on CIFAR-10 that achieves a test accuracy of over 90%. Please comment. The authors need to clarify the training procedure for the baseline ResNet-18 model to ensure a fair comparison. The reported accuracy is significantly lower than expected, which raises concerns about the experimental setup and the validity of the comparisons.

6. Again, although the authors claim that the dummy trainset can protect privacy, I think such a claim is incorrect and will only provide a false sense of security to the ML S&P community. The main flaw is that the proposed method is just an empirical method and does not have any theoretical privacy-preserving analysis/guarantee. [r5] has already shown how easy it is to break a privacy protection method that does not enjoy strong theoretical privacy-preserving accounting. Maybe this paper can focus more on explaining ML memorization rather than protecting ML privacy.

### Questions
See **Weaknesses** for details.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the use of a dummy training set to reduce privacy leakage from model memorization. The dummy set is initialized with random noise, and beyond training the model to memorize this set, the authors introduce an additional step: optimizing the dummy set itself to enhance memorization. Experimental results indicate that training with this dummy set can mitigate privacy leakage, as measured by membership inference attacks.

### Strengths
1. The idea of using a dummy set to counteract the memorization of private data is novel and intriguing.

2. The paper is well-organized and presented clearly.

### Weaknesses
Weaknesses:

1. Optimizing the dummy set itself to facilitate memorization may counteract its ability to consume model capacity effectively. The authors claim that this optimization can "improve generalization performance" (line 248). However, this assertion is neither supported by experimental evidence nor intuitively clear, as it is not evident why optimizing the loss of the dummy set would lead to better generalization. Specifically, the optimization process might lead the dummy samples to resemble each other or the training data, reducing the diversity needed to effectively occupy the model's memorization capacity. This could result in the model learning a compressed representation of the dummy set, which would not prevent the model from memorizing the actual training data. Furthermore, the lack of a clear mechanism explaining the generalization improvement makes this claim questionable.

Follow-up questions:

(1) Can the authors provide a comparison of membership inference attack accuracy with and without dummy set optimization?

(2) Can the authors report the test accuracy results with and without this optimization?

2. The reductions in memorization scores shown in Table 1 are not substantial. While it is commendable that the authors report standard deviations, the variability appears larger than the observed decrease in scores. This raises concerns about the statistical significance of the reported reductions. The wide variance suggests that the memorization scores are highly sensitive to individual samples, and the reported average reduction might not be a consistent effect across different training runs or datasets. A more rigorous statistical analysis, such as reporting confidence intervals or performing hypothesis testing, would be necessary to validate the effectiveness of the proposed approach.

3. The improvement in resistance to membership inference attacks is not pronounced. For CIFAR-10, the AUROC only decreases from 0.6373 to 0.5995, while for Wikitext-103, it drops from 0.9688 to 0.7972. These reductions, especially for CIFAR-10, are quite small and leave the model vulnerable to membership inference attacks. The AUROC for Wikitext-103, while showing a larger drop, is still relatively high, indicating that the model is still memorizing a significant portion of the training data. It is unclear how this level of protection compares to other privacy-preserving techniques.

Follow-up question: What would the attack AUROC be when employing conventional regularization techniques such as dropout or label smoothing?

4. How would the optimal size of the dummy set scale with model size? For instance, would larger models necessitate proportionally larger dummy sets?

### Questions
Please see weaknesses.

### Soundness
1

### Presentation
3

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
This paper proposes an interesting method to decrease model memorization by introducing an additional dummy set composed of redundant and non-sensitive samples. The approach involves optimizing this dummy set on a separate model. Specifically, the dummy set is designed to fulfill two requirements: decreasing generalization error and avoiding correlation with training samples. Several experiments are conducted to demonstrate the efficacy of the proposed method on both image and text data.

### Strengths
1. The topic of decreasing memorization by introducing an additional dummy set is both interesting and significant in the field of machine learning.

2. The authors conduct several experiments to validate the performance of their method, including tests on various datasets encompassing image and text data.

### Weaknesses
1. When generating the dummy set, only the generalization error is controlled. The correlation between dummy samples and training samples is not adequately addressed, which may lead to leakage of training data through the dummy samples. A detailed analysis of these correlations would enhance the paper. Specifically, the paper should investigate the mutual information or other statistical measures between the dummy set and training set to quantify the degree of correlation. The authors should also explore methods to minimize this correlation during the dummy set generation process, such as adversarial training or explicit decorrelation constraints.

2. The paper lacks comprehensive experiments on potential side effects of the generated dummy set. For instance, investigating how the dummy set affects the model's robustness, prediction uncertainty, or fairness would provide valuable insights. The authors should evaluate the model's performance under adversarial attacks, analyze the model's confidence scores on both in-distribution and out-of-distribution samples, and assess whether the dummy set introduces any bias that could lead to unfair predictions for certain groups. These experiments would provide a more complete picture of the method's impact.

3. The performance of the model is affected by the size of the dummy set, which may limit the practicality of the proposed method in real-world applications. The authors should provide a more detailed analysis of the relationship between dummy set size and model performance, including the computational cost associated with larger dummy sets. Furthermore, the paper should explore methods to optimize the size of the dummy set, such as adaptive sampling or early stopping criteria, to achieve a better balance between performance and computational efficiency.

4. There is no theoretical guarantee provided regarding the reduction of memorization after employing the dummy set. The paper should provide a theoretical analysis of how the dummy set affects the model's learning dynamics and its ability to memorize training data. This analysis could involve using tools from information theory or statistical learning theory to quantify the reduction in memorization. Without such a theoretical foundation, the effectiveness of the method remains somewhat unclear.

5. There are some typos and inconsistencies in the manuscript, such as the notation inconsistency between $S_t \cup S_d \setminus \{z_t\}$ and $S_t \cup S_d \setminus z_t$.

### Questions
1. As claimed in the paper, the dummy set can occupy the network’s memorization capacity. Could you provide additional results to support this claim? For example, presenting memorization scores or performing Membership Inference Attacks (MIA) on both training samples and dummy samples to observe their differences would strengthen your argument.

2. Could you include some figures of the final obtained dummy samples? It would be interesting to see whether they resemble natural images or appear more like random noise. 

3. In line 200, you state that “adding $S_d$ to $S_t \cup S_d$ should not cause a significant change.” Is this a typo, and should it instead be “adding $S_d$ to $S_t $” ? Also, please provide additional details on why this should hold and whether this is a strong assumption for your method.

4. During model training, did you employ data augmentation techniques? If not, what would be the effect of applying them on memorization?

5. Please provide a clear definition of unintended memorization and clarify the differences between normal memorization.

6. What is the number of reference models used in the Membership Inference Attacks, and how do you choose the data used to construct these reference models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new approach to prevent the model from memorizing sensitive training data by introducing a dummy set—a collection of redundant, non-sensitive instances. The model is trained on both the actual training set and this dummy set. Since neural networks have limited memorization capacity, the dummy set absorbs most of the memorization, reducing the leakage of sensitive data.

### Strengths
- The topic of overcoming neural network overfitting and unintended memorization is a critical area.
- The paper presents multiple experiments across diverse tasks (e.g., image classification and language modeling) to evaluate the effectiveness of the proposed over-memorization method.
- The presentation is clear and well-organized, making it easy to follow.

### Weaknesses
1. The manuscript overlooks important related work on mitigating neural network memorization, which is the key focus of the paper.

2. While the paper presents an interesting approach using dummy data to prevent memorization, there are studies working on introducing dummy data during training to overcome overfitting by inserting (such as [2-4] and some other citations mentioned in [1]). The authors should clarify how their method advances these existing approaches.

3. While the authors evaluated training data privacy using LiRA-based MIA methods with metrics such as TPR@FPR, per-sample evaluations are missing, such as the mean success rate of the attack. It is crucial to determine whether the proposed methods can effectively defend against attacks targeting easily memorized samples.

4. The authors use randomly initialized samples as dummy data, optimized via SGD. However, this approach could raise concerns about model utility. It would be beneficial to provide further discussion and experimental results to assess the potential impact on utility.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
1
