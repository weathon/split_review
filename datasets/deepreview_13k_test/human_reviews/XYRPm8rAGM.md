# Agree to Disagree: Demystifying Homogeneous Deep Ensembles through Distributional Equivalence

- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Abstract
Deep ensembles improve the performance of the models by taking the average predictions of a group of ensemble members. However, the origin of these capabilities remains a mystery and deep ensembles are used as a reliable “black box” to improve the performance. Existing studies typically attribute such improvement to Jensen gaps of the deep ensemble method, where the loss of the mean does not exceed the mean of the loss for any convex loss metric. In this work, we demonstrate that Jensen’s inequality is not responsible for the effectiveness of deep ensembles, and convexity is not a necessary condition. Instead, Jensen Gap focuses on the “average loss” of individual models, which provides no practical meaning. Thus it fails to explain the core phenomena of deep ensembles such as the superiority to any single ensemble member, the decreasing loss with the number of ensemble members, etc. Regarding this mystery, we provide theoretical analysis and comprehensive empirical results from a statistical perspective that reveal the true mechanism of deep ensembles. Our results highlight that deep ensembles originate from the homogeneous output distribution across all ensemble members. Specifically, the predictions of homogeneous models (Abe et al., 2022b) have the distributional equivalence property – Although the predictions of independent ensemble members are point-wise different, they form an identical distribution. Such agreement and disagreement contribute to deep ensembles’ “magical power”. Based on this discovery, we provide rigorous proof of the effectiveness of deep ensembles and analytically quantify the extent to which ensembles improve performance. The derivations not only theoretically quantify the effectiveness of deep ensembles for the first time, but also enable estimation schemes that foresee the performance of ensembles with different capacities. Furthermore, different from existing studies, our results also point out that deep ensembles work in a different mechanism from model scaling a single model, even though significant correlations between them have been observed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper develops a theory to explain why homogeneous deep ensemble can improve the performance.

### Strengths
- The experiments of distributional equivalence property in Sections 4.1 and 4.2 are interesting.

### Weaknesses
- The setting and assumptions of the distribution $p_F$ which is crucial are not clear. All mentioned is $F \sim p_F$ is a trained model. I believe that this is important for the solidness of the developed theory. At least, we should have something to connect the min over $\mathcal{F}$ and the member function $F \sim p_F$. Otherwise, the theory is loosing. 
- The proof of Proposition 3.1 can not be found.
-  It seems to me that the definition of $\hat{f}(x)$ is not meaningful because it is associated with a function $f \in \mathcal{F}$ and it returns 1 if $f(x)$ is a correct prediction and $0$ otherwise. Therefore, $E_{F\sim \hat{p}_F}[F(X)]$ seems to be the percentage of the number of correct predictions when $F \sim p_F$. What is the meaning of applying $\phi$ to this average. Similar question to $\phi(\hat{f}(x))$ in Eq. (8).
-  I have checked the proof of Lemma B1 and Theorem 4.1. They require $E_{x \sim p_x}[\hat{f}(x)]$ = $E_{x \sim p_x}[\hat{g}(x)]$ for every $\hat{f}, \hat{g} \in \hat{\mathcal{F}}$ or the accuracies are equal for every $f,g \in \mathcal{F}$ which is weird for a general function space $\mathcal{F}$. Certainly, we can partly assume this with $f,g \sim p_F$ which is the distribution of well-trained models. However, the support of $p_F$ is only a subset of $\mathcal{F}$. Therefore, I reckon that the minimization in Theorem 4.1 should be over the support of $p_F$.

### Questions
Please address my questions in Weaknesses.

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
This paper challenges the common explanation for deep ensemble success, which attributes their effectiveness to Jensen’s inequality. The authors argue that this explanation is insufficient and propose a new perspective based on the **distributional equivalence property** of trained models. According to this view, although ensemble members may differ in their individual predictions, their output distributions (based on the predicted probability for the target class) are statistically identical across the dataset.

Through both theoretical analysis and empirical evidence, the paper demonstrates how this distributional equivalence property helps explain why deep ensembles consistently outperform single models. Additionally, the authors introduce estimation schemes to predict ensemble performance based on the number of members and model capacity, offering insights into the relationship between ensemble capacity and single-model scaling.

### Strengths
- The paper offers practical insights into the relationship between global diversity and ensemble performance improvement, as well as the distinct contributions of ensemble capacity versus single-model scaling. The estimation schemes, which allow practitioners to approximate ensemble performance using just two models, provide a computationally efficient approach that could inform more cost-effective system design.
- Beyond merely acknowledging the diversity of ensemble members, the paper provides an in-depth analysis of both **point-wise** and **global diversity**, emphasizing the latter as a key factor often overlooked in prior research.

### Weaknesses
- The main contribution, introducing distributional equivalence, may lack generalizability to other loss functions. Please refer to the question section for more details.
- The distributional equivalence condition, a foundational assumption underlying all theorems, seems overly restrictive. Specifically, in the proof of Theorem B.1, lines 692–695, the authors assert that “for arbitrary $\(\hat{f}, \hat{g} \in \hat{F}, P(\hat{f}(x)) = P(\hat{g}(x))\)$” holds  $\(\forall x \in X\)$, which is a strong assumption that I am still not convinced.

### Questions
1. Section 4.1’s findings on distributional equivalence focus on the predicted probability for the target class, without considering the full class probability distribution. Could the authors provide an additional analysis that incorporates more information, such as the difference $\(l = p(y) - p(\hat{y})\)$, where $\(\hat{y}\)$ is the predicted class and $\(p(\hat{y})\)$ is the highest probability across all classes? This could give a broader perspective on the consistency of distributional equivalence.

2. Which loss function was used to train the models in Section 4.1? My hypothesis is that the loss function has a significant influence on these findings. For instance, cross-entropy loss focuses on the probability of the target class, so models trained with this objective might naturally exhibit distributional equivalence on this specific metric. In contrast, a loss function such as label smoothing, which considers probabilities across all classes, might lead to different observations, potentially limiting the generalizability of the results in Section 4.1. Could the authors discuss or provide empirical insights on how these findings might vary with alternative loss functions?

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
The paper discovers that members of homogeneous ensembles have the distributional equivalence property. Based on this property, the paper answers the fundamental question that why deep ensembles work. Additionally, a way to estimate the performance of deep ensembles is proposed. The paper further discusses the bias-variance tradeoff in deep ensembles and compares the effectiveness of scaling a single model versus scaling deep ensembles. Comprehensive theoretical and empirical analyses are provided to support the claims in the paper.

### Strengths
1. Theoretical findings are fruitful and solid.
2. Insightful discussions about related works can effectively engage readers.

### Weaknesses
1. In Line 135 of the paper, aurthors mention that the unsatisfactory results of the majority vote classifier inspire them to explore overlooked conditions, which turns out to be the distributional equivalence property. Then, why is there no further effort to explain the majority vote classifier after finding the overlooked condition?
2. The distributional equivalence property is observed on CIFAR-10 dataset. However, on such small datasets, it's known that the trained DNNs tend to be quite overconfident, especially in the case where weak or even no regularization is adopted. Combined with the fact that DNNs are highly accurate on small datasets, the observed distributional equivalence is not surprising at all. To justify the distributional 
equivalence property in general cases, larger datasets and/or stronger regularization settings need to be considered. 
3. In Section 4.4, results are mainly derived for the Brier score, while those for NLL are missing.
4. In Fig. 6, it's better to include plots for error rate in additon to losses.
5. In Line 676, authors note that SGD is used without momentum or data augmentation. However, these techiques are crucial for DNNs to reach high performance. If they are not considered, the results of the paper could have limited practicality.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Previous theory of Deep Ensemble owing the benefit of ensembling to the diversity of ensemble members with "trivial" Jasen Gap of the losses without considering the data distribution. Instead, this paper introduces the distributional equivalence of the trained members from global data distribution, which further explains Deep Ensemble works with the equivalent output distribution globally but with distinct sample-wise predictions for a group of samples. Under this perspective, the paper further provides the theory of how sample-wise diversity and the number of members contribute to the performance. Besides, it provides a method to predict the ensemble performance with only two models.

### Strengths
1. The paper is easy to follow and well-organized. 
2. The introduced "distributional equivalence" that all members produce similar prediction distribution across a group of samples is novel, and has been neglected by previous works.
3. The theory is technically sound and the prediction of ensemble performance with only two models is also interesting.

### Weaknesses
1. What does the "only differ in the training stochasticity" actually mean? i.e., where does stochasticity come from? from the shuffled dataset? or random initialization?
2. An interesting question is why the homogeneous members demonstrate the "distributional equivalence" property. Does it come from the fixed dataset bias, fixed architecture, etc.?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper examines why deep ensembles are effective by proposing distributional equivalence, the idea that ensemble members produce predictions with identical distributions. The authors argue this property is key to the performance gains of deep ensembles, offering a new explanation beyond the Jensen gap. They validate this theory through experiments and introduce an estimation scheme that allows ensemble performance to be predicted using just two models, reducing evaluation costs and highlighting the unique benefits of deep ensembles over scaling single models.

### Strengths
1. This paper introduces a fresh theoretical perspective on deep ensembles by proposing the concept of distributional equivalence among ensemble members. This approach offers an alternative to the usual Jensen gap explanation, providing insight into why deep ensembles work by analyzing homogeneous model distributions.
2. The proposed method of estimating ensemble performance using only two models is a practical contribution that could streamline the application of ensembles in resource-constrained settings.
3. The authors have conducted comprehensive experiments across multiple datasets and architectures, providing strong empirical support for their theoretical claims.

### Weaknesses
1. The theoretical framework relies on assumptions about neural collapse, which may not apply universally across various datasets and model configurations. This reliance could limit the generalizability of the findings, especially in cases with limited data or high variability.
2.Deep ensembles are frequently applied to enhance uncertainty estimation, the paper mainly emphasizes performance improvements, leaving the effect of distributional equivalence on uncertainty quantification undiscussed.

### Questions
1. The experiments have included the CIFAR-10 and TinyImageNet, which may not represent the complexity of real-world data, such as text data or multi-modal data. Could the authors discuss how dataset complexity might affect the distributional equivalence property, especially for datasets with higher-dimensional or more variable features?
2. How sensitive is the distributional equivalence property to various training hyperparameters, such as learning rate or initialization seed? An analysis of this could help in understanding the robustness of it across different training configurations.
3. The paper introduces a method for performance estimation using two models. Could the authors comment on the potential for scaling this approach for ensembles of significantly larger capacity.

### Soundness
3

### Presentation
3

### Contribution
4
