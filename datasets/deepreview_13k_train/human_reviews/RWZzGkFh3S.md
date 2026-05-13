# Outlier Gradient Analysis: Efficiently Identifying Detrimental Training Samples for Deep Learning Models

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
A core data-centric learning challenge is the identification of training samples that are detrimental to model performance. Influence functions serve as a prominent tool for this task and offer a robust framework for assessing training data influence on model predictions. Despite their widespread use, their high computational cost associated with calculating the inverse of the Hessian matrix pose constraints, particularly when analyzing large-sized deep models. In this paper, we establish a bridge between identifying detrimental training samples via influence functions and outlier gradient detection. This transformation not only presents a straightforward and Hessian-free formulation but also provides insights into the role of the gradient in sample impact. Through systematic empirical evaluations, we first validate the hypothesis of our proposed outlier gradient analysis approach on synthetic datasets. We then demonstrate its effectiveness in detecting mislabeled samples in vision models and selecting data samples for improving performance of natural language processing transformer models. We also extend its use to influential sample identification for fine-tuning Large Language Models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Identifying detrimental samples is one of the core tasks in data-centric machine learning. While there exist various approaches to estimating the influence of data points on the model performance, Influence functions present a unique advantage in that it does not require re-training to assess data influence. Unfortunately, computing Influence functions requires calculating the inverse of the Hessian matrix, limiting their applicability to over-parameterized deep models. This paper draws a connection between Influence functions and outlier detection on the gradient space. Then, the authors hypothesize that an outlier gradient analysis can be utilized as Hessian-free proxies to Influence functions. The preliminary experimental results on linear and non-linear synthetic datasets validate the effectiveness of gradient-based outlier detection in identifying mislabeled detrimental samples. The efficacy of the outlier gradient-based detrimental sample selection is further demonstrated on various noisy regimes and in combination with Large Language Model training as well.

### Strengths
- The paper explores an important research problem: identifying detrimental training samples. The proposed method dramatically reduces the computational cost of detrimental sample selection by circumventing the need to calculate the Hessian and is more effective than methods that rely on Hessian approximation.

- Although the proposed method mostly relies on an existing outliner detection algorithm, the authors do uncover a previously overlooked application of existing algorithms.

- The proposed method is demonstrated to be effective across various domains and tasks. However, since the major benefit of the proposed method appears to be its computational efficiency, I would have appreciated more experiments and analyses regarding its application to LLMs. More details on this are elaborated in the Weaknesses section.

### Weaknesses
 - As mentioned in the Strengths section, the method is a simple re-interpretation of existing methods. While I do not think this is always a reason to accept or reject a paper, as of now, the authors do not present sufficient theoretical analysis or support behind why the outlier detection algorithm works in this specific context. Yes, they do discuss conceptually (on a very superficial level) how these two research areas bear resemblance, but their hypotheses lack theoretical analysis to be convincing. Shedding light on why and how the first-order gradient is enough to anticipate the influence of training samples would be a much more significant contribution than a series of empirical evidence, which can easily be curated, that does no more than repeatedly showcase the existing algorithm's new potential application.
- One of the major traits of Large Language Models is their transferability and generalization ability to various downstream tasks. Can this method be utilized to predict how they would fare across various downstream tasks as well?
- It seems counter-intuitive that a method that only uses first-order information would be more accurate than methods that at least partially take second-order information via approximation. Do authors have any insight into why this could be the case?
- Is the proposed method only effective at identifying distribution shifts and outliers induced by label noises? Can it identify covariate shifts on inputs data?

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Outlier Gradient Analysis, a novel approach for identifying detrimental training samples that avoids the computationally intensive inverse Hessian calculation typically associated with influence functions. By reframing influence estimation as an outlier detection problem in the gradient space, the authors develop a framework for scalable, Hessian-free detection of detrimental samples across diverse model types. They validate this approach on both synthetic datasets and real-world applications, including vision (CIFAR datasets), NLP (GLUE tasks), and fine-tuning for large language models (LLMs), where it achieves performance on par with or surpassing other influence-based methods.

Overall, if certain theoretical and experimental clarifications are provided, this paper presents a practical approach to identifying detrimental samples in a data-centric framework, effectively bypassing the computational limitations of influence functions for large models. I would be willing to increase the score if the author response addresses the concerns.

### Strengths
1. This paper is well-written and easy-to-follow.
2. The proposed method offers a significant computational advantage by eliminating the need for the Hessian matrix, which is especially important for deep learning models.
3. The method is adaptable across various domains, including vision and NLP, and shows promising results in fine-tuning tasks for LLMs.
4. Extensive experiments are conducted and the empirical results are competitive.

### Weaknesses
1. The differences between the proposed approach and previous gradient-based, Hessian-free methods for detecting detrimental samples, such as Gradient Tracing [1], need to be discussed in better detail. Currently, the two approaches appear very similar. Specifically, the paper needs to clarify how the outlier detection algorithm applied to the gradient space differs fundamentally from simply using the gradient information directly, as done in TracIn. The core distinction seems to be the application of an outlier detection algorithm, but the paper does not sufficiently justify why this is a more principled approach than directly using the gradient information. For instance, it is unclear if the outlier detection algorithm is simply identifying samples with large gradient magnitudes, which could be achieved without the additional complexity.
2. Most experiments appear to be conducted on datasets with artificially corrupted labels, which may not fully capture the complexity of real-world noise. It would be valuable to see the proposed method tested on real-world noisy datasets to verify its robustness in more realistic conditions. The paper should include experiments on datasets where the noise is not simply a label flip, but rather more complex forms of noise, such as those arising from ambiguous or subjective annotations. Furthermore, visualizing the most detrimental samples identified within a large-scale, real-world dataset like ImageNet, with real-world noise, could better demonstrate the method's practical effectiveness and provide more convincing evidence of its utility. The current experiments do not adequately demonstrate the method's ability to handle the nuances of real-world noisy data.

### Questions
1. How does the proposed method handle scalability challenges with LLMs where gradient dimensionality can be extremely high?

### Soundness
3

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
2

### Summary
Summary:
This paper studies the outlier detection problem using influence function. By connecting the influence functions with outlier gradient detection, the authors propose a Hessian-free approach to avoid the computational burden of calculating the inverse of Hessian matrix, which is claimed to benefit large-scale machine learning applications. Some theoretical analyses are provided to support the claim. Moreover, demonstrative examples are provided to show the effectiveness of the proposed method, which is further evaluated on real-world datasets.

### Strengths
Strengths:
- The computational improvement brought by Hessian free outlier detection is a good contribution.
- The performance improvement is satisfactory. According to the experimental results, the proposed method surpasses most of the baseline methods.
- Various models and tasks are considered in the experiment.

### Weaknesses
Weaknesses:
- The writing of this paper does not meet the standard of an ICLR paper. There are too many unprofessional and unnatural words, which makes the paper not easy to comprehend.
- The authors claim that the proposed method is Hessian-free, thus benefiting large-scale machine learning. However, the experiment only considered small-scale dataset.
- The title of this paper is confusing. Outlier analysis seems to be related to anomaly detection or OOD detection, however, label noise is another problem which contains noise on Y, not data X. So, what is the general goal of the proposed method? It would be helpful to clarify it.
- It is not clear why the proposed method can use the gradient to replace Hessian, more intuitive explanations are needed.

### Questions
Please see the weaknesses part.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript highlights the decisive role of the gradient with respect to model parameters, $\nabla\_\theta \ell(z;\theta)$, in influence estimation. Building on this insight, the authors propose using outlier detection algorithms, such as iForest, on sample gradients as an alternative to influence estimation, thereby avoiding the high computational cost of calculating the inverse Hessian matrix. They demonstrate the effectiveness of their method in tasks such as noisy label correction, data selection for NLP, and data identification for LLMs.

### Strengths
1. This manuscript is well-written.
2. The idea of using outlier detection algorithms as an alternative for influence estimation is innovative.
3. The proposed method is time efficient.

### Weaknesses
1. While the authors experimentally demonstrate the effectiveness of using outlier detection methods for influence estimation, identifying a sample as an outlier does not necessarily indicate that it is harmful to the validation loss or has a negative influence score. Some meaningful outliers may represent rare but valuable patterns within the training set and should not be excluded. Furthermore, the method relies on the assumption that samples with large gradient norms are more likely to be harmful, which lacks theoretical justification and may not hold true in practice. It is possible that some samples with large gradient norms are actually beneficial to training, especially in complex, non-convex loss landscapes.
2. The experimental results on data selection for fine-tuning NLP models using LiSSA and DataInf may not fully reveal their performance. Although the authors compute influence for these methods using only the training set for fair comparison, reliable influence estimation typically requires a validation set, according to the definition of influence functions. Furthermore, methods that do not require a validation set, such as Self-LiSSA, demonstrate similar performance to outlier detection methods. The comparison is therefore not entirely conclusive, and the advantage of the proposed method over existing influence estimation techniques remains unclear.
3. Since the experimental settings primarily follow those of DataInf, it is unclear why text-to-image generation tasks were not included in the experiments. In DataInf, the AUC and Recall for class detection in text-to-image generation tasks are reported as 0.865 and 0.315, respectively. Compared to sentence transformation and math problems, which approach 1.000 for both AUC and Recall, text-to-image tasks appear more challenging and could better highlight the advantages of the proposed method. The absence of these experiments limits the generalizability of the findings.

### Questions
1. Regarding Figure 1-H, since the model is an MLP and we are computing the gradient with respect to the parameter space, $\nabla\_\theta \ell (z;\theta)$, why are the plotted features only two-dimensional?

### Soundness
2

### Presentation
3

### Contribution
2
