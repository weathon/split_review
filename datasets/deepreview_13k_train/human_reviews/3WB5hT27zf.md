# Partial Optimal Transport for Open-set Semi-supervised Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Semi-supervised learning (SSL) is a machine learning paradigm that leverages both labeled and unlabeled data to improve the performance of learning tasks. However, SSL methods make an assumption that the label spaces of labeled and unlabeled data are identical, which may not hold in open-world applications, where the unlabeled data may contain novel categories that were not present in the labeled training data, essentially outliers. This paper tackles open-set semi-supervised learning (OSSL), where detecting these outliers, or out-of-distribution (OOD) data, is critical. In particular, we model the OOD detection problem in OSSL as a partial optimal transport (POT) problem. With the theory of POT, we devise a mass score function (MSF) to measure the likelihood of a sample being an outlier during training. Then, a novel OOD loss is proposed, which allows to adapt the off-the-shelf SSL methods with POT into OSSL settings in an end-to-end training manner.
Furthermore, we conduct extensive experiments on multiple datasets and OSSL configurations, demonstrating that our method consistently achieves superior or competitive results compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on studying the problem of Open-Set Semi-Supervised Learning (OSSL). The authors present a novel framework that transforms the OSSL problem into the Partial Optimal Transport (POT) problem. The authors aim to leverage the benefits of POT to detect the OOD samples. Empirically, POT achieves competitive performance on various benchmarks.

### Strengths
-	This paper is straightforward and well-written. It is quite easy to follow.
-	The paper solves Open-Set Semi-Supervised Learning (OSSL), an important ML problem in practice.
-	Empirical results demonstrate that POT can achieve SOTA results on several benchmarks.

### Weaknesses
- Based on the description provided, the proposed approach appears to be fundamentally similar to auxiliary OOD classifier methods, such as those employed in MTCF, T2T, and OpenMatch. The core idea seems to involve training a binary classifier to distinguish between in-distribution (ID) and out-of-distribution (OOD) samples. However, the paper lacks a clear and detailed comparative analysis that differentiates the proposed method from these existing approaches. For instance, how does the utilization of Partial Optimal Transport (POT) offer advantages over the one-vs-all classifiers used in T2T and OpenMatch, particularly in scenarios with a large number of classes? Additionally, while MTCF also uses a binary OOD classifier, it incorporates a curriculum learning framework. Does the proposed method offer any benefits in terms of avoiding error accumulation, a potential issue with MTCF's Otsu thresholding for sample selection?

- The paper does not sufficiently justify the effectiveness of POT in detecting OOD samples. While the concept of minimizing transport cost is mentioned, a deeper explanation is needed. For example, how does the distribution of transport mass among ID and OOD samples contribute to their differentiation? Does the inherent nature of POT, with its focus on transporting only a fraction of the mass, inherently favor ID samples and thus facilitate OOD detection? A more rigorous theoretical or empirical analysis is required to substantiate this claim.

- The paper overlooks a crucial discussion regarding the connections and distinctions between the proposed method and existing applications of POT in related domains, such as Open-set Domain Adaptation and Positive-Unlabeled Learning [1,2,3]. For instance, how does the challenge of estimating the transport ratio in OSSL differ from its estimation in Positive-Unlabeled Learning as addressed in [1]? Moreover, how does the proposed method's use of redundant mass as a robust parameter compare to the mean cost of transport approach in [2] or the approximate estimation method in [3]?  Furthermore, what specific adaptations or novel designs have been incorporated into the proposed method to tailor it specifically for the OSSL task, as opposed to other tasks like PU learning or Open Set Domain Adaptation? A thorough comparative analysis would significantly strengthen the paper's contribution.

- The paper does not provide a satisfactory explanation for the superior performance of the FixMatch algorithm compared to certain OSSL methods. While it is acknowledged that FixMatch might still generate high-quality pseudo-labels for ID samples, this does not fully address why it outperforms methods specifically designed for OSSL. A more detailed analysis of the interplay between FixMatch's pseudo-labeling and the presence of OOD samples is needed. For example, does the consistency regularization in FixMatch play a role in mitigating the negative impact of OOD samples?

- The paper lacks crucial experimental details. For instance, what are the specific parameter settings used for FixMatch, including the confidence threshold for pseudo-labeling? What are the implementation specifics of the T2T algorithm, such as the architecture of the one-vs-all classifiers? Providing these details is essential for reproducibility and a fair comparison with other methods.

- Table 3 is missing some of the comparative algorithms included in Table 1. To ensure a comprehensive evaluation, all relevant methods should be included in both tables.

- There is an inconsistency in the notation of 'k' in Algorithm 3. This should be clarified to avoid confusion.

- On page 8, in the experimental section,  $L_{ood}$ should be corrected to $\lambda_{ood}$.

- The term "graph" in the last sentence of Subsection 2.2 is unclear and requires further explanation. What does "graph" refer to in this context?

### Questions
Please see the weakness for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the open-set semi-supervised learning (OSSL) challenge, specifically aiming to frame the treatment of out-of-distribution data (OOD) as a partial optimal transport (POT) problem. It introduces a mass score function (MSF) designed to evaluate the likelihood of a sample being an outlier during training. Additionally, the paper presents an OOD loss, allowing conventional semi-supervised learning methods to be adapted for OSSL scenarios via end-to-end training. The authors compare their proposed method against MTCF, T2T, and OpenMatch, on CIFAR10, CIFAR100, and Imagenet-30, showing superior performance.

### Strengths
* Semi-supervised learning is a significant area of research in machine learning, aiming to enhance performance by effectively utilizing both labeled and unlabeled data. 

* The OOD angle used in the paper makes it interesting to a broader audience.

* Incorporating (partial) optimal transport as a framework is a novel and innovative aspect of this work.

### Weaknesses
 * Respectfully, the novelty of the method is limited and the paper overclaims novelty.
   *  For instance, one main contribution of this paper is the introduction of the "novel" MSF score. The score function essentially corresponds to what is commonly referred to as "barycentric projection," a concept well-documented in both classical and contemporary optimal transport (OT) theory literature (for reference, please see sources such as [Ambrosio et al.](https://link.springer.com/book/10.1007/b137080)). In this context, it is more appropriate to state that the paper utilizes classical concepts from OT theory to address new application challenges. The sentence “we devise a new score function” is more or less misleading.

* The parameter $k$, which deals with the amount of redundancy, plays a crucial role in the methodology presented in the paper. Varying the value of k leads to significant variations in the outcomes of ODD detection. It would enhance the paper's quality if it delves into the process of determining this value. Specifically, the paper could explore methods for assessing the amount of data that should be classified as outliers before initiating the algorithms. 

* Some implementation details and important ablation studies are missing from the paper. For instance, the utilized batch size and the effect of having a small batch size (which presumably reduces the performance of the proposed method) are missing from the paper. 

* The rationale behind the decision to use (10) instead of the original constraint (7), i.e., enforcing all mass from $\mathcal{L}$ to be transported to a subset of $\mathcal{U}$, is not well presented. Couldn't the unsupervised data be missing an entire class? In that case, the missing classes in $\mathcal{L}$ must be destroyed, i.e., not transported, and the constraints in (7) would allow that. I believe this can easily happen in minibatch training. 

* Some of the very relevant references are missing from the paper: 
   * Rizve, M.N., Kardan, N. and Shah, M., 2022, October. Towards realistic semi-supervised learning. In European Conference on Computer Vision (pp. 437-455). Cham: Springer Nature Switzerland.
   * Xu, R., Liu, P., Zhang, Y., Cai, F., Wang, J., Liang, S., Ying, H. and Yin, J., 2020. Joint Partial Optimal Transport for Open Set Domain Adaptation. In IJCAI (pp. 2540-2546).
   * Yang, Yucheng, Xiang Gu, and Jian Sun. "Prototypical Partial Optimal Transport for Universal Domain Adaptation." (2023).

### Questions
* For Algorithm 2, in the line of OOD score, shouldn't the formula be $Score_\{\mathcal{U}\}=\mathbf{T}^T\mathbf{1}_n$?

* The transportation cost is set to "Cosine distance." The definition  "d(x,y)=1-Cosine(x,y)"  is only a true metric if $x,y\in \mathbb{S}^{d-1}$, i.e., $x$ and $y$ are unit vectors. Is your backbone returning unit vectors? Even if that is the case, and for the sake of mathematical rigor, I suggest adhering to the Euclidean distance, which is equivalent to the cosine distance when $x$ and $y$ are unit vectors and is still sensible when they are not!

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers an open-set semi-supervised learning where there potentially are “outliers” in the unlabeled data distribution. The paper provides a novel loss function inspired by Partial optimal transport to handle OOD detection and demonstrates the effectiveness and robustness of the proposed method on multiple datasets.

### Strengths
1. Strong empirical performance
2. Various ablations suggest that the method is robust and has a lower computation time and other baselines.
3. A connection to optimal transport is intuitive

### Weaknesses
1. Lack of clarity in writing.  I found it hard to understand what is the main idea of the paper up until page 6. The author mentions in the abstract/ introduction that a mass score function (MSF) to measure the likelihood of unlabeled samples being outliers, yet I did not mention how this is related to OT/POT and it’s not clear to me how OT is beneficial to the OSSL task. The following sentence is helpful for me to understand the idea,  “we can utilize the transport mass as a reliable OOD score, where a sample with a smaller value of mass score function tends to be an OOD sample”. However, it is mentioned on page 6. It would be nice if one could provide something like this earlier in the paper and provide a clear problem setting early on.


2. Many definitions and acronyms are used before being defined (see questions)

3. The definition of distribution in equation 8) is not mathematically valid? By adding a factor of k, the sum of the probability mass is greater than 1 and therefore is not a valid probability distribution.

### Questions
1. OSR is not defined, MSR is mentioned before it is defined in section 2.2.
2. Section 4.1, the distribution L and U are not defined.
3. Section 4.1, “the features of these d-dimensional samples”, do you mean the features or samples that has d-dimensional ?
4. Notation in equation 7) is not clear. Does this means T1_{\mathcal{L}} \leq \mathcal{L} point-wise less than or equal to ?
5. In algoirthm3, L_x and L_u is not defined in the main text ?
6. What is the number 50, 100, 500 for in Table 5 ?
7. “magnituWde” -> “magnitude” ?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent
