# Characterizing Robust Overfitting in Adversarial Training via Cross-Class Features

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Adversarial training (AT) has been considered one of the most effective methods for making deep neural networks robust to adversarial attacks. However, AT can lead to a phenomenon known as robust overfitting where the test robust error gradually increases during training, resulting in a large robust generalization gap. In this paper, we present a novel interpretation of robust overfitting from the perspective of feature attribution. We find that at the best checkpoint of AT, the model tends to involve more cross-class features, which are shared by multiple classes, in its decision-making process. These features are useful for robust classification. However, as AT further squeezes the training robust loss, the model tends to make decisions based on more class-specific features, giving rise to robust overfitting. We also provide theoretical evidence for this understanding using a synthetic data model. In addition, our understanding can also justify why knowledge distillation is helpful for mitigating robust overfitting, and we further propose a weight-average guided knowledge distillation AT approach for improved robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of robust overfitting in adversarial training (AT), where during adversarial training, the test robust accuracy of a model gradually decreases after a certain epoch (checkpoint) although the training robust accuracy continues to increase. This leads to a large robust generalization gap. The paper first provides a novel explanation for this phenomenon from the perspective of feature attribution. They divide the features learned by a model (robust DNN classifier) into `class-specific or exclusive features` and `cross-class features`. As their names suggest, class-specific features are informative for the prediction of a specific class, whereas cross-class features are informative for the prediction of multiple classes. 

They provide empirical evidence to show that models trained using AT tend to rely more on cross-class features when observed at the best checkpoint (epoch where the test robust accuracy is highest). However, when robust overfitting occurs at later epochs/checkpoints, they observe that the model tends to rely less on cross-class features and more on class-specific features. In order to quantify the cross-class feature usage, they propose a feature attribution vector (per sample and per class) and a feature attribution correlation matrix. The feature attribution correlation matrix helps visualize the extent to which a model depends on cross-class features, and it is summarized by a metric named class attribution similarity (CAS). By observing the correlation matrix and CAS metric and at the best checkpoint and the final checkpoint across a number of datasets, architectures, and norm types, they conclude that there is consistently a higher dependence on cross-class features at the best checkpoint, but this dependence decreases at the final checkpoint, leading to robust overfitting. Therefore, it is crucial to preserve the model’s dependence on cross-class features to mitigate this phenomenon. 

They provide a theoretical analysis to back this observation, based on a simple linear model with Gaussian class-conditional distributions and decoupled class-specific and cross-class features. Finally, they show that knowledge distillation can be effective at preserving the cross-class features. Therefore, they propose a knowledge distillation based adversarial training method where a weight-averaged model acts as the teacher for knowledge distillation. This method is shown to have improved adversarial robustness in their experiments.

### Strengths
1. The explanation for robust overfitting based on cross-class and class-specific features is intuitively clear and is backed well by empirical results. 

2. The visualization of robust overfitting using the feature attribution correlation matrix and the CAS metric are useful tools for understanding this phenomenon. Sections 3.2 and 3.3 do a good job of considering multiple scenarios to understand the effect of cross-class features, and have pointers to the Appendix for additional results.

3. The weight average guided knowledge distillation method for adversarial training mitigates the issue  of robust overfitting and has improved performance on multiple datasets and architectures.

### Weaknesses
1. The theoretical analysis section is weak for the following reasons: lack of clarity in the presentation and theorem statements. The synthetic model is quite simple and can be presented in a better way (see my comments in the `Questions` section).

2. The proposed weight average guided knowledge distillation method (WAKE) is not clearly described. Is the weight-averaged model $\bar{\theta}$ created on the fly during adversarial training, similar to the self ensemble adversarial training (SEAT) method of (Wang & Wang, 2022)? The piecewise linear scheduling for $\lambda$ should be described precisely. More clarity is needed on these aspects, and an algorithm block would also be helpful (appendix can be used if space is limited).  

3. Minor: experiments in the main paper are limited, and only two baselines are used for comparison. However, there are more experiments and other baselines like TRADES in the appendix. 

4. Code has not been made available. 

Would consider raising my score if Sections 4 and 5 are improved.

**UPDATE:** Increased my score to 6 after reading the author responses and revised paper.

### Questions
1. In Eqn (3), the max over the perturbation $\delta$ should include all three loss terms. It seems like the max is only over the cross-entropy loss term. Please make it clear by moving the $(1 - \lambda_1 - \lambda_2)$ term inside the max and using parentheses around the three loss terms. 

2. The terms $\ell_{CE}$ and $\mathcal{KD}$ in Eqn (3) should be defined as the cross entropy loss and the Kullback-Leibler divergence respectively. 

3. Nit: the $\times$ operator is not needed in Eqn (4).

4. First paragraph of section 3.1:
    - The notation $f(\cdot) = W \circ g(\cdot)$ seems incorrect. It should be $f(\cdot) = W g(\cdot)$, i.e. a matrix multiplication. 
    - Please define the notation that $W[i]^T$ is the $i$-th row of $W$. 
    - The dot is not needed for inner products and scalar products. For instance, it can be $f(x)_i = W[i]^T g(x)$ rather than $f(x)_i = W[i]^T \cdot g(x)$. Similarly, it can be $g(x)_j \\,W[i, j]$ rather than $g(x)_j \cdot W[i, j]$.

5. Referring to the subsection `Knowledge distillation mitigates robust overfitting`, the following statement is not clear: “. . . using knowledge distillation can preserve the weight of these features by smoothing the labels of the overlapping classes”. 

### On Section 4
The description of the synthetic model is not clear in Section 4.1. Some suggestions below:

6. Use of $i$ to index the class is confusing. Instead, $y$ could be used to denote the class and $i$ or $j$ to index the features.

7. It is mentioned that the data distribution $\mathcal{D}_i = \\{ x\_{Ej}, x\_{Cj} \\,|\\, 1 \leq j \leq 3 \\} \in \mathrm{R}^6$. How can the data distribution be a set of features which lives in $\mathrm{R}^6$? I can follow what is implied, but it is not formally correct.

8. In Eqn (7), the probability distributions are actually **class-conditional** rather than marginal. That is, for the exclusive features: $x\_{Ej} \\,|\\, y = i \sim \mathcal{N}(\mu, \sigma^2)$ when $j = i$ and $0$ when $j \neq i$. Similarly, for the cross-class features: $x\_{Cj} \\,|\\, y = i \sim \mathcal{N}(\mu, \sigma^2)$ when $j \neq i$ and $0$ when $j = i$. Specifying it this way makes it clear why these features are defined as exclusive and cross-class.

9. In Eqn (9), it would be better to say the outer expectation is over the class prior distribution since $\mathrm{E}_i[\cdot]$ is pretty vague. 

10. In Eqn (9), it is not clear how the cross-entropy loss simplifies to the term $\max_{j \neq i} f_w(x + \delta)_j - f_w(x + \delta)_i$. It seems. to me that if we simplify the cross-entropy loss, it reduces to $\log(\sum_j e^{f_w(x + \delta)_j}) - f_w(x + \delta)_i$. Same question applies to Eqn (10).

11. What is the significance of introducing the regularization term in this objective?

12. In Section 4.2, 2nd line: should it be `abandon $x_C$` rather than `abandon $x_E$`?

13. The statements of theorem 2 and theorem 3 are vague. They could be stated more formally. In theorem 3, what is $\epsilon_0$? 
 
14. In the subsection `Knowledge distillation preserves cross-class features`, could the authors clarify how label smoothing applies here due to symmetry? And what does symmetry refer to here?

### On Section 5
15. As pointed out in point 2 under `Weaknesses`: 
Is the weight averaged model $\bar{\theta}$ created on the fly during adversarial training, similar to the self ensemble adversarial training (SEAT) method of (Wang & Wang, 2022)? The piecewise linear scheduling for $\lambda$ should be described precisely. More clarity is needed on these aspects, and an algorithm block would also be helpful (appendix can be used if space is limited). 

16. In Eqn (11), please clarify that the max over $\delta$ applies to both the loss function terms. 

17. What is the temperature parameter $T = 2$ referred to in section 5.2 under settings?

18. Finally, the number of references seems to be small given the breadth of literature in this area.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the effects of cross-class features and specific-class features to the performance of adversarial training. The conclusion is that the cross-class features are more robust and important to the robust accuracy.

### Strengths
- The empirical finding is interesting and possibly helpful in practice to improve the performance of adversarial training.

### Weaknesses
- The theories developed are very restrictive and under extremely unrealistic assumptions
   -  Data have 6 features and each features follow a Gaussian with mean zero.
   -  It only considers a linear model with two parameters $w_1$ for the exclusive feature and $w_2$ for the shared feature.

- The theoretical results obtained are humble and do not really reflect the empirical finding. Moreover, the statement of Theorem 2 is ambiguous. It is not clear what it does mean by "a larger w2 increases the possibility of the model distinguishing the adversarial examples from any other given class".

- When taking average of feature vectors for a class to visualize the matrix $C$ and CAS, this cannot reflect the tendency/behavior of each feature vector. To me, a better way is to compute and visualize instance-wisely.

- The proposed practical method lacks novelty and does not have a strong connection to theory developed and experiments are humble.

### Questions
What does it mean by "a larger w2 increases the possibility of the model distinguishing the adversarial examples from any other given class" in Theorem 2?

Can you compute and visualize C and CAS instance-wisely? For example, do it for a pair of feature vectors in class i and class j, and then take average.

### Soundness
2 fair

### Presentation
2 fair

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
As claimed in this paper, robust overfitting, which although has been widely discussed, has not been fully understood. In this paper a new interpretation in the view of feature attribution is proposed and then a follow-up method is designed.

### Strengths
Robust overfitting is an interesting phenomena happened in adversarial training. Investigating it in the view of feature attribution may bring new understanding for it.

### Weaknesses
- Robust overfitting is specific to adversarial training. Thus, the discussion should be emphasized more on special properties of adversarial attack/examples/training. However, the idea given in this paper fails in this aspect: in regular training, it is also the case that the model first learn cross class information and then focusing on a specific model, e.g., the well-known neural collapse saying that the features of examples of one class will collapse to a direction.

- The unclearness to the regular training also could be observed in their proposed method: stochastic weight averaging (SWA) is a standard technique to enhance generalization capability in regular training. In the current experiment, it is hard to say the advantage of the proposed WAKE comes from SWA or it comes specific property of adversarial training, then now it cannot well support the main contribution.

- Another weakness is that the metric used to support the conclusion is not very convincing. For example, it is believed that features in different layers capture different information, e.g., cross-class or in-class information. Simply put all features together seems too weak.

### Questions
- I want to see specific properties in adversarial training. Thus, could I see the performance of the same experiment but on regular training?

- There are many metric that can measure the information about class and examples learned by DNNs. Could the authors use other metric and also observe the similar phoneme as measured by CAS？

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors primarily concentrate on addressing the robust overfitting problem. In pursuit of this objective, they identify intriguing properties within both cross-class and class-specific features. Then, both empirical and theoretical evidence show that knowledge distillation helps mitigate robust overﬁtting by preserving the observed properties. The experiments further verify this.

### Strengths
1. Understanding robust overfitting via cross-class and class-specific features is interesting.
1. The empirical and theoretical evidence could support the recent common sense that knowledge distillation is beneficial to mitigate robust overfitting.
1. The experiments show that a weight-average guided knowledge distillation method can boost robustness.

### Weaknesses
1. In Eq. 10, the authors use label smoothing to simulate knowledge distillation. I am wondering if this simulation is reasonable. The authors only said that ''due to symmetry'', but it is difficult to understand. 

1. On page 6, the authors claimed that "... derive a large enough logit" and "... Since the final checkpoint makes decisions based only on these limited features, the logit for the correct class is not large enough". These two conclusions are very difficult to understand because I find it challenging to infer them from the existing experiments. Figure 4 only shows the correlation matrix which cannot reflect the logit information.

1. In Equation 7, why do the class-specific or cross-class features only appear in robust features?

1. The results shown in Section 4.2 are somehow weak I think. For example, it is difficult to see that feature $x_{E,i}$ will dominate the whole training objective when $w_1>0$.

1. There are many adversarial robust distillation methods in previous works, so it's better to compare them in details like [a].

[a] Revisiting Adversarial Robustness Distillation: Robust Soft Labels Make Student Better. ICCV 2021.

### Questions
Apart from the issues mentioned in the Weaknesses section, there is another concern: this paper mainly focuses on robust overfitting. How about catastrophic overfitting in Fast-AT?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
