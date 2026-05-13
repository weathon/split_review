# Revisit, Extend, and Enhance Hessian-Free Influence Functions

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Influence functions serve as crucial tools for assessing sample influence. By employing the first-order Taylor extension, sample influence can be estimated without the need for expensive model retraining. However, applying influence functions directly to deep models presents challenges, primarily due to the non-convex nature of the loss function and the large size of model parameters. This difficulty not only makes computing the inverse of the Hessian matrix costly but also renders it non-existent in some cases. Various approaches, including matrix decomposition, have been explored to expedite and approximate the inversion of the Hessian matrix, with the aim of making influence functions applicable to deep models. In this paper, we revisit a specific, albeit naive, yet effective approximation method known as TracIn, and simplify it further, introducing the name Inner Product (IP). This method substitutes the inverse of the Hessian matrix with an identity matrix. We offer deeper insights into why this straightforward approximation method is effective. Furthermore, we extend its applications beyond measuring model utility to include considerations of fairness and robustness. Finally, we enhance IP through an ensemble strategy. To validate its effectiveness, we conduct experiments on synthetic data and extensive evaluations on noisy label detection, sample selection for large language model fine-tuning, and defense against adversarial attacks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed a simplified method (IP) for training data attribution. The method equipped a hessian-free method to avoid the large computational cost on the Hessian matrix and its inverse. The paper also proposes some tricks (e.g., ensemble) and more applications (e.g., change the target function to robustness/fairness). Some empirical studies are also proposed to show the efficiency improvement and performance.

### Strengths
- The paper is well written, and the reader can understand the main idea of the paper quickly in a short time.
- Efficiency has become a very important topic for TDA(training data attribution).

### Weaknesses
 - There is a large gap between the contribution claimed in this paper and actual literature. The major problem lies in the first and second contribution bullet point in section 1 (line 59 - line 62)
  - The Inner Product (IP) proposed by this paper (as a simplified version of TracIN) has long been proposed [1] and used in a large number of papers[2]. Specifically, [1] uses the gradient dot product (Grad-Dot, equivalent to the IP method in the reviewed paper) to evaluate the influence of one training sample on another, and applies it to noisy label detection. This method has also been used as a baseline in other works [2]. Therefore, the claim that IP is 'defined' by this paper is not accurate; a more appropriate framing would be 'revisited'.
  - Replacement of the loss gradient to some other metrics to fairness and robustness is also something tried for influence function or related methods[3].
- The experiment is not fully fair and may intentionally make other baseline methods to have lower results. Furthermore, the improvement is kind of trivial.
  - The dropout trick can also be used on other methods as well, what are their performance?
  - Some related gradient-based SOTA methods (e.g., TRAK) are ignored. Furthermore, random projection has been a very widely used method for efficiency, but it is also omitted in the paper.
 - The manually added noisy data for Figure 2 (D) seems to be cherry-picked. The negative performance of H^-1 seems to be very unlikely.

### Questions
- Could you elaborate on this “We believe that sample influence should be assessed using a fixed model; simply summing sample influences at different stages fails to capture the dynamics of model optimization.” more? It seems hard to understand.
- Noisy label detection and other downstream tasks that do not have a very large difference between each method. Maybe some counterfactual prediction evaluation metrics (e.g., LDS) are more suitable?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an approach for measuring influence of samples in trained models by defining it as the inner product between the gradient of a specific sample and the sum of gradients from all other samples. By substituting this gradient sum with a fairness measure, the method claims to capture the influence of a sample on the model's fairness. When this gradient sum is replaced with gradients of adversarially perturbed samples, the method is intended to reflect the impact on robustness. Additionally, the paper suggests enhancing the proposed measurement through an ensemble of models. Experiments were conducted for applications such as detecting noisy labels, curating fairness-sensitive samples, and improving resilience against adversarial attacks.

### Strengths
The paper includes a lot of experiments and provides statistical ranges for the reported results.

### Weaknesses
However, the paper lacks a clear problem statement and positioning of the method within existing approaches. The formula provided to describe the method is the TracIn formula, with the only difference being the reduction of calculations to the final trained model. This raises several questions: (i) the explanation of the benefits of this simplification is vague and could be questioned, (ii) the intuition behind this approximation rests on a comparison with a method involving the Hessian’s inverse and assumes cosine similarity between vectors without a clear justification, and (iii) there is no explanation of what this formula intuitively means in contexts of fairness or adversarial robustness. Furthermore, the paper does not formally define the process for generating ensembles to accumulate the influence scores.

A precise definition of the influence function and an explanation of the role and significance of the inverse Hessian in this context would improve the method’s description.

Section 4, which highlights differences between this approach and an influence method that incorporates the Hessian, presents results on synthetic data and a simple multi-layer perceptron. It shows that Hessian based method fails due to approximation errors. However, it does not clearly demonstrate or discuss the approximation errors, and it is unclear why a setup without approximation errors cannot be tested on more complex, non-linearly separable data. Figure 3 lacks sufficient explanation, diminishing clarity.

In subsequent experiments where the ensemble inner product method shows improvements, only the original method appears beneficial in terms of time complexity. Moreover, as the ensemble size increases, it closely approximates TracIn with multiple measurements, making the specific contributions of this paper unclear.

Section 6 presents improvements in fairness, yet the benchmarks primarily focus on accuracy, limiting the validity of the comparison. Finally, the approach appears to offer limited benefits in adversarial defense.

Minor Issues: The related work section includes descriptions of studies that do not effectively contextualize the current paper’s contributions.

### Questions
What is the precise role and interpretation of the influence function? How does the inverse Hessian factor into the formula?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a variation of TracIN called IP, where the ensembling over checkpoints is abandoned in favor of the converged model. 
As this particular variation has appeared several times as baseline in ablation experiments in prior works (e.g. in both TracIN and the original influence function paper), the authors attempt to revisit this formulation with new theoretical and experimental insights.
Some intuition is provided for why this simple setup might work through an argument for similarity to the inverse hessian influence function. Further extensions of IP in the application of fairness, and a more powerful ensemble version of IP, are also presented. Experimentally, the proposed method is competitive with prior art in the benchmarked tasks in terms of downstream performance.

+++++++++++++++++++++++++++++++++++++++++++++++++++++

I have read the author's rebuttal. While I agree with some of the points made by the authors, I'm opting to maintain my original review score as the contribution of the paper and the experimental evidence for impact is still unclear

### Strengths
1. The proposed method is particularly simple, easy to implement and efficient to compute.
2. The experimental evaluations presented in the paper are fairly thorough and rigorous, with appropriate repeat experiments to establish confidence intervals. 
3. The extension of influence estimation to algorithmic fairness metrics is interesting.

### Weaknesses
1. The order consistency argument for why IP is a good approximation to inverse hessian influence is quite weak. In figure 1, data points with vectors in regions I and III would not satisfy order consistency. The authors argue that since IP and IF both rate such points as beneficial/detrimental, the order doesn’t matter. This is clearly not true, as many applications of influence estimation involve determining set membership at the extreme ends of the influence spectrum (e.g. removing x% detrimental examples based on the most negative influence values or curating x% most beneficial examples for fine tuning based on the highest influence values). Changes to ordering in these regions are in fact more significant than changes to ordering within regions II and IV, which would be assigned neutral influence scores. Furthermore, the argument that the sign of the influence is the most important factor is not well justified, as the magnitude of influence is crucial for many applications, such as targeted data removal or augmentation. The paper does not provide a clear explanation of why the magnitude of the IP score should be considered a reliable proxy for the magnitude of the inverse Hessian influence. 
2. Furthermore, the conditions under which the angle alpha is small has not been discussed. The paper lacks a rigorous analysis of the relationship between the angle alpha and the properties of the loss landscape or the data distribution. It is unclear under what circumstances the cosine similarity between the gradient of a training sample and the gradient of the validation set would be a reliable indicator of influence. A more detailed discussion of the assumptions and limitations of this approximation is needed.
3. While the benchmarks on downstream utility are quite extensive, other quantitative metrics relating to similarity of predictions, such as correlation to the (inverse hessian) influence function, leave-one-out training, and precision-recall curves of label perturbation detection, are missing. The absence of these metrics makes it difficult to assess the quality of the influence estimates produced by IP. Specifically, the paper should include a comparison of the IP scores with the actual influence values computed using the inverse Hessian, even if it is only for a small subset of the data or a simplified model. This would help to validate the claims made about the approximation quality of IP. Furthermore, the paper should include a leave-one-out analysis to directly measure the impact of individual training samples on the model's performance. This would provide a more direct measure of influence than the downstream utility metrics.

### Questions
What does U(0, 0.01) on line 318 mean in the context of model parameter drop out? Are model parameters set to zero with a chance of 1%, with or without replacement?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors introduce Inner Product (IP), a metric that simplifies the classic influence function by dropping the inverse Hessian term to assess the influence of training samples. They validate IP through sanity checks on synthetic data and demonstrate its superior performance across various applications, including noisy label detection, fairness enhancement, and defense against evasion attacks.

### Strengths
- The sanity checks on synthetic data yield some interesting findings, e.g., for non-linear models, IP can separate corrupted samples from normal samples whereas influence function cannot
- The experiments are comprehensive and cover quite a few applications (nevertheless, I think the paper is mostly following Chhabra et al. 2024)

### Weaknesses
If IP is indeed as useful as the authors were suggesting in this paper, this would be a breakthrough for the field of influence function (and more broadly, data attribution), since the (inverse) Hessian term is indeed the main bottleneck of applying influence functions to large-scale models. Unfortunately, after reading the paper, I am not convinced that IP is a principled and useful metric. 

- The authors confused the relationship between influence function and TracIn, and incorrectly viewed TracIn as an approximation of influence function. Influence function is a first-order approximation of leave-one-out, which measures influence w.r.t. changes to the training set. On the other hand, TracIn is a first-order approximation of the change of loss, which measures the change in model parameters as a function of time. They are fundamentally different metrics since they have completely different definitions of "influence". The authors seemed to suggest that IP can be derived from both influence function (by replacing the inverse Hessian with identity), and TracIn (by only considering the last iteration). Regardless of whether such simplifications make sense or not, this makes IP hard to interpret --- the basic question is, what notion of "influence" is IP adopting, and what ground truth is it approximating?

- The analysis at the beginning of P4 is completely wrong, as there is no way that IP can preserve order even in specific regions. For instance, in Figure 1, one can easily construct two gradient vectors in Region II as follows: the first vector is orthogonal to the blue vector and has small norm, the second vector forms an acute angle with the blue vector and has large norm. By adjusting the norm, we can reverse the order. The main issue is: removing the inverse Hessian must lose information, and there is no analysis on why such information could potentially be useless. 

- The ensemble procedure is unclear and confusing. The procedure is not formally explained; I assume that the dropout is only applied to the final model checkpoint, since the authors mentioned "diverse models can be swiftly generated without necessitating model retraining". What is the rationale behind this approach? In the literature, people do multiple retraining and ensemble to reduce the inherent noise in training and influence function estimation. It is unclear to me that applying multiple dropout to the final model checkpoint would enjoy the same benefit. 

- Finally, regarding the experimental results, the improvement compared to existing approaches is very limited. In table 1, all methods look similar to me after taking into account the variance.  

There are also some minor points:

- I think the authors should read [1] carefully to develop a better understanding of the literature

- Some algorithms which have similar design (e.g., ensemble) are missing, for instance, TRAK [2]

- Some claims lack evidence, for instance, "We believe that sample influence should be assessed using a fixed model; simply summing sample influences at different stages fails to capture the dynamics of model optimization" --- it seems to me that the essence of TracIn is exactly being dynamic

### Questions
The paper clearly cannot be accepted in its current form, but I think a few results on synthetic data in Section 4 look interesting. The authors could explore the following question: under what circumstance (on data and/or model), the directions of $H^{-1}v$ and $v$ are close.

### Soundness
1

### Presentation
3

### Contribution
1
