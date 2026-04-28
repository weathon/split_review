# Distribution Aware Active Learning via Gaussian Mixtures

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 6, 3

## Abstract
In active learning (AL), the distribution of labeled samples in a latent space is often dissimilar to that of unlabeled samples, depending on various factors such as labeled set size or data selection strategy. This distributional discrepancy hampers both evaluation and estimation of informativeness on unseen data, and remains an important issue in AL. In this paper, we propose a robust distribution-aware learning and sample selection strategy that employs Gaussian Mixture Model (GMM) to effectively encapsulate both labeled and unlabeled sets for AL. By utilizing the GMM statistics derived from all available data, the proposed approach is able to construct a more diverse feature representation, thereby reducing the risk of overfitting to limited patterns. Specifically, we propose a regularization method that supervises GMM posteriors under the concept of metric learning, and introduce a semi-supervised learning method that feeds GMM statistics into an adversarial discriminator to prevent memorization of samples. Furthermore, we propose a new informativeness metric that utilizes GMM likelihoods to detect overfitted areas in the latent space, and then devise a hybrid sample selection strategy that takes advantage of the properties of different informativeness metrics. Extensive experimental results demonstrate that our GMM-based method outperforms existing works on various balanced and imbalanced datasets, and can be readily integrated with other AL schemes to further improve the performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new active learning strategy that addresses the issue of mismatched distributions between labeled and unlabeled samples by incorporating a Gaussian Mixture Model (GMM). The strategy combines various informativeness metrics for sample selection. Tests on different datasets show that this GMM-based method performs better than existing approaches and can be combined with other active learning methods to enhance results further.

### Strengths
This paper introduces a new active learning strategy by incorporating a Gaussian Mixture Model (GMM). This strategy aims to address the issue of mismatched distributions between labeled and unlabeled samples.

This GMM-based method performs better than existing approaches on several datasets.

### Weaknesses
If I understand correctly, in Section 3.2, two GMMs are fitted for the labeled and unlabeled data, respectively. Is this correct? Equation (2) provides a means to compare two Gaussian distributions, but it is not immediately clear how this extends to the comparison of two GMMs, and whether the weight of each Gaussian component in the mix is considered in this comparison.

Regarding Equation (3), the purpose of the optimization seems to be to minimize the disparity between the unlabeled data, $X_{UL}$, and the labeled data, $X_{L}$, within the embedding space. If the model is trained effectively, it appears that $X_{UL}$ and $X_{L}$ would become indistinguishable in the embedding space. It raises the question of whether this is the intended outcome, as it would seem important for the embedding space to retain the information that differentiates $X_{UL}$ from $X_{L}$. Specifically, if the distributions are forced to be too similar, the method may lose its ability to select informative samples from $X_{UL}$ that are different from $X_L$.

The combination method outlined in Equation (5) is not entirely convincing as the best approach. An alternative sampling strategy might involve drawing from each of the three separate rankings and then using the highest-ranked samples from each ranking as the data set for annotation. It would also be insightful to see the results of an ablation study where each component of Equation (5) is used independently as the final selection criterion. Furthermore, the weighting of the three components in Equation (5) is not justified; it is unclear why equal weights are optimal, and an analysis of the sensitivity of the results to these weights would be valuable.

In Equation (5), it seems that only $I_{Ent}$ leverages the labels from previous iterations. The other two components are influenced by $X_{UL}$ and $X_{L}$ but are label-independent. It may be beneficial for the authors to make this point clearer in their writing. It would also be helpful to understand how the method would perform if the label information was incorporated into the other two components.

### Questions
1. Are two GMMs fitted for the labeled and unlabeled data, respectively?
2. How does Equation (2) extend to the comparison of two GMMs?
3. What is the rationale behind Equation (3)?
4. Why Equation (5) is a good way to combine the information?
5. In Equation (5), is $I_{Ent}$ the only component that leverages the labels from previous iterations, but the other components label-independent?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces Gaussian Mixtures of labeled and unlabeled dataset to facilitate the model training, regularization, sample selection for active learning.

### Strengths
1. the improvement in performance over baselines is significant. 
2. well-organised and easy to follow and understand, though there are many componenets in the proposed method. 
3. The idea is original and it uses classific GMM to facilitate model training, as well as for high-quality and diverse sample selection for active learning.

### Weaknesses
1. The main concern would be the computation burden it introduces. With a batch, within each optimization iteration, there are 10 EM runs for both labelled and unlabelled samples. So it would be very time-consuming, even though there are some tricks used to reduce it. So both theoretical and experimental analysis about time complexity would be expected. 

2. Some details about loss functions are missing to better understand the training. For example, there is a trade-off parameter $\alpha$ to balance cross-entropy loss and regularization loss. The value for this constant was not given. Besides, there is another loss for adversarial learning. How to balance with this function is not clear to me. 

3. Some intuitive explanation to demonstrate the superiority would be great. For example, with each active learning cycle, for each class, how the selected samples from the proposed method are different from the ones from baselines? Or use the selected samples to verify the claim of 'high quality and diverse'.

### Questions
see above weakness points.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a robust distribution-aware learning and sample selection strategy that employs Gaussian mixture model (GMM) to effectively encapsulate both labeled and unlabeled sets for AL.
A regularization method and an informativeness metric are further proposed to detect overfitted areas. Experiments on mulltiple datasets including balanced and imbalanced datasets demonstrate the validity of the proposed method.

### Strengths
(1) The solution of applying distribution alignment for active learning is valid.
(2) Multiple datasets including balanced and imbalanced datasets are evaluated to show the advantages of the proposed method.

### Weaknesses
(1) It seems that the paper pose a relatively strong assumption that the data follows Gaussian mixture model (GMM) and derive the statistics from GMM. However, the author fails to show that GMM is a good model to approximate the data distribution in active learning. Actually, because of the nature of active learning, there are frequently samples from new classes that does not follow the estimated GMM model. In that case, the estimation based on GMM will not be accurate. This is a significant limitation, as real-world active learning scenarios often involve complex, non-Gaussian distributions, and the introduction of novel classes during the learning process can invalidate the GMM approximation. The paper needs to provide a more robust justification for this assumption, especially when dealing with the evolving nature of the labeled set in active learning.
(2) The novelty of the paper is limited as the distribution alignment has been widely studied in the previous work:
(i) Zhang et al “Distribution Alignment: A Unified Framework for Long-tail Visual Recognition”. CVPR 2021
(ii) “Agreement-Discrepancy-Selection: Active Learning with Progressive Distribution Alignment”, AAAI 2021
The reference (ii) also mentioned distribution alignment with adversarial learning but under a more general setting without GMM assumption. Thus, it seems this paper is talking about an existing method under some special conditions. The paper's approach appears to be a specific instantiation of a broader concept, lacking substantial novelty in its application of distribution alignment. The use of GMM, while a specific choice, does not inherently introduce a new theoretical or practical contribution that significantly advances the field beyond existing distribution alignment techniques.

### Questions
As metioned in the weakness, the fundament problem of this paper is that it is merely a special case of a solved general problem, which makes the novelty of the paper very limited. Without detailed discussion of the difference from the existing work as listed, the novelty of the paper does not stay on a safe ground.

Moreover, the author needs to show why the GMM model is a good approximation of the data distribution in active learning as there can be many outliers and unknown classes. How about if the data is a long-tail distribution. The assumption of the paper is a bit too strong.

Last but not least, the paper did not any new insights of this field. The results are merely a small extension and special cases of existing approaches.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
