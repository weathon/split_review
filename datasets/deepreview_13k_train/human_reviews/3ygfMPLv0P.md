# Tailoring Mixup to Data for Calibration

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Among all data augmentation techniques proposed so far, linear interpolation of training samples, also called \emph{Mixup}, has found to be effective for a large panel of applications. 
  Along with improved performance, Mixup is also a good technique for improving calibration and predictive uncertainty.
  However, mixing data carelessly can lead to manifold intrusion, i.e., conflicts between the synthetic labels assigned and the true label distributions, which can deteriorate calibration.
  In this work, we argue that the likelihood of manifold intrusion increases with the distance between data to mix. 
  To this end, we propose to dynamically change the underlying distributions of interpolation coefficients 
  depending on the similarity between samples to mix, \rev{and define a flexible framework to do so without losing in diversity.} We provide extensive experiments for classification and regression tasks, showing that our proposed method improves performance 
  \rev{and calibration of models, while being much more efficient.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel Mixup framework that employs a Similarity Kernel (SK) called SK Mixup to achieve a stronger interpolation between similar points while reducing interpolation otherwise. As a motivation of this study, the authors defined the concept of manifold mismatch, which can negatively impact the calibration of confidence in Mixup. They conducted experimental validation to assess the impact of this phenomenon on the distance between points to mix. Following the presentation of SK Mixup, the effectiveness of the proposed approach in alleviating the manifold mismatch was demonstrated through extensive experiments in classification and regression. Nevertheless, the extension to more complex tasks and theoretical analysis on the regularization effect of SK Mixup still need to be undertaken -- This is why the authors did not receive the highest score in *Contribution*.

### Strengths
* The proposed approach was well motivated by targeting the appropriate research problem of calibration-driven Mixup methods in classification and regression: Manifold mismatch. Furthermore, this problem was theoretically defined and proved with the supplement materials.

* The proposed method was in a clear and well-organized manner, and the proof was provided in a manner that supported its conclusions.

* The research problem was validated through experimental results; a comparison was made with the baseline.

* Comprehensive experiments in classification and regression, with a particular focus on performance and computational cost, demonstrated the efficacy of the proposed approach.

### Weaknesses
There is no weakness in the paper that would justify its rejection.

### Questions
**Question 1.** Why did not SK RegMixup be applied to ViT in Table 4? Is there any potential challenges or limitations of applying SK RegMixup to ViT architectures?

**Question 2.** [line 976-978] In the proof of the first part in Theorem 3.1., whatever the value of $\lambda\_{1}$ is, $\lambda$ can be 0. When $\lambda=0$, then $\tilde{\mathbf{x}}(\lambda)=\mathbf{x}\_{l} \in \mathcal{M}\_{j}$, not $\mathcal{M}\_{i}$, and so does symmetrical case. In my opinion, it would be $\forall \lambda \geq \lambda\_{1},~\tilde{\mathbf{x}}(\lambda)=\lambda \mathbf{x}\_{k}+(1-\lambda)\mathbf{x}\_{l} \in \mathcal{M}\_{j}$. The authors are kindly requested to examine and fix them if there is an error.

---

**Things to improve the paper that did not impact the score:**

* Figure 4 caption: there is no result about *Circles* toy datasets. The mention of it from the caption would be removed if it's not intended to be included

* [line 442] The ECE and AECE of MIT-A in ImageNet-R would be in bold. The authors have to double-check their result highlighting in Table 4 to ensure consistency and accuracy.

*  In Table 4, is there any reason why ECE and AECE are exactly same in OOD settings? The authors are kindly requested to explain why ECE and AECE are identical in OOD settings or, if this is unexpected, verify whether there might be an error in the reporting or calculation of these metrics.

* The experimental results show that the SK RegMixup is an effective method. However, Table 6 does not provide the efficiency of the SK RegMixup in terms of computational cost. It is recommended to include computational cost metrics for SK RegMixup in Table 6, similar to what they've provided for other methods.

* [line 879] Typo: cccross

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper first demonstrates that distance between the data used in mixup can impact the likelihood of manifold mismatch (a phenomenon where mixed samples lie outside of the class manifolds of the original data used for mixing). It then proposes an efficient framework to mitigate the occurrence of manifold mismatch. The key idea is to dynamically change the distributions of mixing coefficients via a similarity kernel that measures the distance between the mixed samples. Empirical results are provided to demonstrate the effectiveness of the proposed method.

### Strengths
- Overall the paper is well written and is easy to follow
- An innovative yet efficient method is proposed to improve mixup so that manifold mismatch likelihood is reduced, and better calibration and accuracies can be achieved
- Adequate empirical results on both classification and regression tasks are provided to demonstrate the proposed method

### Weaknesses
 - While Theorem 1 shows the existence of manifold mismatch, it does not tell us anything about the assumption (which is used in the paper) that the higher the distance between two points, the more likely their convex combination will fall outside of the original manifolds, and thus, the more likely a model would assign a different label than the original labels of the two points. Some theoretical results in establishing the validity of such assumption would further strengthen the paper. 
- There are some missing papers that could be worth mentioning in the related work. In particular, mixup related works such as [1,2,3]. 
- For the experiments, it is not clear how the proposed method would compare with the method proposed by [1,2,3], and also how would it perform for more complex datasets like ImageNet, ImageNet-C, ImageNet-R and ImageNet-P.

### Questions
- In Eq. (3), there is a -1 inside the exponential. Why not absorb it into $\tau_{max}$? Are there any reasons why it is presented that way? 
- In the classification scenario where the data samples (but not the labels) are noisy and corrupted, thus blurring the true distance between the samples used in mixing, how would the proposed method perform?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper has come up with a concept called manifold mismatch, which is a phenomenon in Mixup that can harm the generalization and calibration performance of the trained models. The paper also show that such a manifold mismatch behavior is correlated to the distance between the data points being paired and mixed in Mixup. Then, by applying a similarity kernel, the paper proposes a variant training algorithm of Mixup that can dynamically adjust the mixing coefficient depending on the distance of the data points being mixed. Finally, the authors have empirically verified the effectiveness of the proposed algorithm on various models and tasks.

### Strengths
1. It's a novel idea to summarize several observed phenomenons or properties of Mixup into one unified terminology: manifold mismatch
2. The correlationship between data points pair distance and the occurence of manifold mismatch is carefully derived.
3. The proposed algorithm is meant to balance the diversity and the uncertainty of the virtual examples in Mixup, which is meaningful and helpful

### Weaknesses
1. Poor presentation
2. Doesn't clarify the connection between manifold mismatch and calibration. 
3. The core claim that distance impacts manifold mismatch is too simple to be seen, and it's actually under-justified since there seems to be much more necessary conditions of manifold mismatch like data distribution, structure of learned features and manifolds, etc.. In fact, the idea of improving Mixup by forcing more mixtures between closer points is not novel, like k-mixup [1]
4. The idea of dynamically adjust the mixing coeffecient is also not new, like AdaMixup [2].

### Questions
1. Line 011 or 012 on page 1. "Along with improved performance", what performance, please make it specified
2. Line 012 or 013 on page 1. "improving calibration and predictive confidence", from my understanding they are the same thing, no need to use "and" here in my opinion.
3. Line 014. Infact in this line the paper has mentioned "calibration of confidence", what is calibration of "confidence", again, in my opinion it's just calibration.
4. Line 019 to 020. Again, please specify what "performance" it is when mentioning "improve performance".
5. Line 054. Here the paper mentions "label noise", can the authors provide a brief description of it like the way they have described manifold intrusion in previous text?
6. Line 140. Again, please specify the term "performance".
7. Is there and related research works about calibration-driven Mixup methods in regression tasks?
8. Line 161. If possible it's much better to turn this title to the next page, it would look better.
9. Line 162 to 169. The notation preliminaries in this paragraph feel a bit too simple and careless. For example, when defining a dataset, one may want to first define a data space and label space, indicating that these spaces are subspaces of some vector spaces of certain dimensions, and then indicate that the training dataset is of some size with the examples being drawn from some data distribution over the data space, etcs.. Putting those details in one single line feels careless. Also, what is $M$? Many would of course just simply take it as the number of classes in the classification problems, but it also needs to be specified in the paper. 
10. Line 162 to 169. There is also some notations that are inconsistent. The paper first indicates that the labels are $M$-dim vectors, then what is the input and output dimension of the encoder $h_\phi$? The way it is presented make the model output $f_\theta(\text{x})$ feels like a scalar, while it should be a vector the same dimension as the labels since $\hat{y}:=f_\theta(\text{x})$.
11. Line 193 to 194. "bounded support $\mathcal{M}_m\subset\mathcal{H}$". Is this also how the manifolds are defined in this paper?
12. Line 194 to 195. To assume that classes are separated, it means all samples belonging to "different classes manifolds" should disjoint, is that correct?
13. Line 208. Why would the mixed points' belonging "to no vlass manifold at all" be a bad thing? In my opinion, when using Mixup for training, especially when the data dimension is high, it's actually mostly the case that the mixed point fall into the "void" areas in the entire data space.
14. Line 212. "the higher the distance between two points, the more likely their convex combination will fall outside of the original manifolds". Here is a counter example. Suppose we have two classes of points in $\mathbb{R}^2$. Suppose their manifolds are two separated line segments on the horizontal axis. If we combine the rightest point from the left manifold and the leftest point from the right manifold, the mixed points will almost all fall into the middle area which is outside both the original manifolds. If we combine the leftest points from both manifold, the fact is, a much bigger proportion of mixed points would fall inside the left manifold. But, the distance between the points in the second case is much larger than that in the first case.
15. Line 215. "Using a Resnet18 trained ...", is it trained using ERM or Mixup?
16. How to choose $\tau_{std}$ and $\tau_{max}$?
17. How does SK Mixup help improve calibration? The derivation of the algorithm only suggests that SK Mixup can help mitigate manifold mismatch, but is manifold mismatch the necessary reason, or even the real reason, of bad calibration?
18. In the process of trading off between diversity and uncertainty, how would calibration and generalization behave? Will they behave like a up-side-down U curve such that there is a sweet spot?
19. The page number of page 7, and the header "under review" line in page 8, there are some strange hyperlinks around the text.
20. Theorem 3.1 (i). "$\lambda\in]\lambda_1,\lambda_2[$", it should be $[\lambda_1,\lambda_2]$ right?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to improve different mixup methods by adjusting the probability distribution to sample interpolation weights according to the distance between a given sample pair. Using the proposed method, sample pairs that are far from each other are less likely to be mixed. Empirical results on different tasks and data sets demonstrate the effectiveness of the proposed method.

### Strengths
The proposed method is clearly introduced and easy to understand

### Weaknesses
 - The motivation of proposed method can be strengthened
- Some baseline methods seem missing, which can make the empirical comparison not supportive enough

### Questions
- Instead of using a similarity kernel introduced in this paper, a simple implementation is to divide sample pairs based on their distances (like the case in Figure 2) and use two different Beta distributions to sample the interpolation weights. How will this baseline perform compared to the proposed method? Such comparison can further verify the motivation and support the proposed method. 
- While the authors have mentioned that non-linear interpolation methods have several disadvantages (larger computational cost, limited application) in section 2.1, some empirical comparison on their performance for image data sets in Table 2-4 should still be necessary. In addition, the authors may also include some of these interpolation methods in Table 6 to verify that their computational cost are muchh larger compared to linear mixup methods. 
- Moreover, can the proposed method be combined with these non-linear interpolation methods as well? I suppose such combination will be straight-forward, as we only need to change the sampling distribution of interpolation weights for different sample pairs. Some discussion (possibly with some empirical results) will be welcome here. 
- I am a bit puzzled by the performance of different methods on ImageNet-A in Table 4. None of them has an accuracy higher than 3%, which seems worse than most methods reported in [1]. Is this due to some discrepancies in experimental setup (e.g., less training epochs)? If so, the authors may need to clarify that such discrepancies are not in favor of their proposed method. 
- Also, how are the baseline methods chosen in Table 6? From my perspective, I suppose we need to compare the time cost of SK Mixup against Mixup or some other baseline methods with rather good performance. Nevertheless, it seems either of the above cases applies, and some explanation may be needed here. 

## References
[1] On Feature Normalization and Data Augmentation. CVPR 2021

### Soundness
2

### Presentation
3

### Contribution
2
