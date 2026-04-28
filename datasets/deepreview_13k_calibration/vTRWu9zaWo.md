# Using Stochastic Gradient Descent to Smooth Nonconvex Functions: Analysis of Implicit Graduated Optimization

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 3, 3, 5, 5

## Abstract
The graduated optimization approach is a heuristic method for finding global optimal solutions for nonconvex functions by using a function smoothing operation with stochastic noise. We show that stochastic noise in stochastic gradient descent (SGD) has the effect of smoothing the objective function, the degree of which is determined by the learning rate, batch size, and variance of the stochastic gradient. Using this finding, we propose and analyze a new graduated optimization algorithm that varies the degree of smoothing by varying the learning rate and batch size, and provide experimental results on image classification tasks with ResNets that support our theoretical findings. We further show that there is an interesting correlation between the degree of smoothing by SGD's stochastic noise, the well-studied ``sharpness'' indicator, and the generalization performance of the model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a heuristic approach for solving nonconvex optimization problems by combining a smoothing technique. The authors demonstrate that stochastic gradient noise impacts the smoothing of the objective function, with the extent of this effect determined by three factors: the learning rate, batch size, and the variance of the stochastic gradient. Building on these insights, the authors introduce a new graduated optimization method. Theoretical analysis and numerical results confirm the effectiveness of the proposed method.

### Strengths
The paper offers a novel perspective on the smoothing effect of stochastic gradient descent (SGD) and its implications for optimizing nonconvex functions.

The connection between smoothing by SGD and generalization performance is a contribution to this field. The correlation between the degree of smoothing, sharpness of the objective function, and generalization performance is convincingly shown, enhancing the credibility of the theoretical insights.

### Weaknesses
While the experiments with ResNets on CIFAR100 provide valuable insights, they may not fully generalize to other types of neural networks or more complex datasets.

A more comprehensive discussion on the practical implementation of the proposed implicit graduated optimization algorithm would further enhance its applicability and understanding.

### Questions
How do different optimizer variants (e.g., Adam, RMSprop) impact the smoothing effect observed with SGD?

What strategies can practitioners use to effectively set the initial values and decay rates for learning rate and batch size to maximize the advantages of implicit graduated optimization?

Could this framework be extended to analyze optimization in graph neural networks or manifold learning?

What computational trade-offs might be associated with implementing the proposed algorithm, such as increased training time or memory usage?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the convergence of stochastic gradient descent (SGD) in the context of nonconvex optimization. The authors aimed to show that the gradients help the objective by smoothing it through the noise injected by sampling functions. The claim that SGD smoothes the objective is shown by assuming that the gradients are distributed according to isotropic Gaussian distribution, which I find to be a trivial result. Moreover, since the work is written from the perspective of giving a new theory for SGD specifically, I find this to be very misleading. The authors also present experiments on CIFAR100 to study the numerical properties related to generalization such as sharpness, which serve as a secondary contribution. Next, the authors propose a new method for $\sigma$-nice functions that runs gradient descent on a smoothed objective with varying parameters and they explain why the method works. Finally, the authors run several variations of SGD on training ResNet-34 on ImageNet to show that increasing batch size helps SGD converge.

### Strengths
1. I think a theory for SGD and an explanation why noise helps to train neural networks is highly desired. It is a great topic and if the results were good, I'd have considered this an important contribution.
2. The numerical evaluations are reasonable.

### Weaknesses
1. My main concern about this work is the unrealistic assumption that the noise from sampling gradients follows Gaussian distribution with identity covariance matrix and variance that does not change over the course of training. What's worse, this assumption is not stated as clearly as other assumptions, instead it's introduced in the text and a couple of references are given to experimental papers that justify normality of the gradients. Those papers, however, do not show that gradients have exactly the same distribution throughout training. It's also never discussed in the paper why the assumption should hold or what happens if it doesn't. And what we should expect here, in contrast, is that the noise level changes every iteration and its variance is a random variable that depends on the iterates and previously sampled gradients.
2. Since the gradient noise is assumed to be exactly gaussian and consntant, the paper fails to deliver what the abstract promises, namely to "show that stochastic noise in stochastic gradient descent (SGD) has the effect of smoothing the objective function", because the authors essentially *assume* that the noise smoothes the objective. I usually refrain from calling a result trivial.
3. Since the results in this work assume Gaussian noise, it means that prior papers on injecting noise inside gradients immediately apply to SGD in this setting. However, there is no comparison to related work on this topic, such as Orvieto et al. "Anticorrelated Noise Injection for Improved Generalization" and Vardhan & Stich, (2021). The latter paper is only mentioned in passing as showing that noise helps escape saddle points, but the authors do not explain what novelty their paper has to offer.

### Questions
1. In what sense do the authors "show" that noise in SGD helps? I see no theory for this, it all seems to follow from assuming Gaussian distribution of gradient noise and prior literature.
2. Can the assumption on Gaussian noise be removed?
3. It appears to me that log scale in Figure 2 in x-axis is actually not helpful as most growth seems to happen for larger values on the x-axis, especially in Figure 2 (B). Can you show us the figure with the x-axis not scaled logarithmically?

### Soundness
3

### Presentation
3

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
This article discusses how Stochastic Gradient Descent (SGD), in its essence smoothens nonconvex functions while optimizing them theoretically analysis is provided here to show that the degree of smoothing ($\delta$) can be calculated using the formula $\delta= \eta C/\sqrt{b}$ where $\eta$ represents the learning rate and $C$ relates to variance while $b$ signifies the batch size. Additionally, it is theoretically and experimentally demonstrated that this smoothing effect clarifies findings in deep learning such as the reason behind poor generalization often observed with large batch sizes. The paper presents three contributions:
1. A mathematical model is offered to explain the smoothing effects of descent (SGDs).
2. There is a link between the level of smoothing and how the model performs overall; the best range for smoothing is between $0.1$ and $1.0$. 
3. Introducing a graduated optimization technique that adjusts the level of smoothing by modifying the learning rate and batch size dynamically throughout the training process.

### Strengths
1. Introduce an innovative approach by showing that SGD’s inherent stochasticity can smooth nonconvex functions, it allows it to function as an implicit form of graduated optimization. This study leverages SGD’s existing stochasticity for the same purpose.
2. This paper offers a framework that explains the impact of learning rate adjustment and batch size variability on the level of smoothing in stochastic gradients. Its theoretical analysis is thorough and well supported by proofs. Clearly defined assumptions that provide a strong basis, for their assertions.

### Weaknesses
 1. This work is constrained by the assumption that gradient noise follows a normal distribution, which will be expected for a broader category beyond normal distribution.
2. Analysis only focused on image classification tasks with CNN-based models.
3. The proof of convergence only applies to $\sigma$-nice functions, which is a restricted class of nonconvex functions.
4. Experiments are insufficient, mainly conducted on CIFAR100 with ResNet architectures, and no experiments on other domains beyond image classification.
5. Lack of discussion of computational overhead compared to standard SGD.
6. No discussion of how the method scales to relatively large models or datasets.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

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
This paper proposes the degree of smoothing notion in stochastic gradient descent and studies its relation with sharpness and generalization. From the proposed notion along with empirical studies, the paper observes that controlling the batch size and learning rate affects the degree of smoothness and therefore proposes a graduated optimization algorithm to gradually decrease the degree of smoothing by increasing the batch size and increasing the learning rate.

### Strengths
1. It is an interesting observation to view the update of SGD as smoothing.
2. The proposed degree of smoothing offers another intuitive explanation for decreasing learning rate and increasing batch size along the way of optimization and establishes its connection to graduated optimization.

### Weaknesses
1. The proposed degree of smoothing is somewhat obvious and simple, falling directly out of the variance/noise assumption of mini-batch SGD. Its correlation with concepts like sharpness is also straightforward because their definitions are somewhat similar already, with sharpness measuring the discrepancy of the function $f$ w.r.t. some $\delta$ neighborhood while the degree of smoothness the discrepancy of gradient $\nabla f$ w.r.t. some noisy disturbance $\omega$. Specifically, the degree of smoothing, as defined, is essentially a measure of the magnitude of the stochastic gradient noise, which is well-understood in the context of SGD. The connection to sharpness is not novel, as both are related to the curvature of the loss landscape, and the proposed degree of smoothing does not offer a fundamentally new perspective on this relationship.
2. The numerical result is not quite informative as the effect of decreasing the learning rate or increasing the batch size has been studied and verified in previous optimization and learning theories like mini-batch SGD and sharpness-aware optimization. The experiments essentially demonstrate well-known phenomena, such as the effect of batch size on gradient noise and the impact of learning rate on convergence speed and stability. The paper does not present any novel experimental findings that would justify the introduction of the degree of smoothing as a new concept.

### Questions
Is there any new insight/advantage the degree of smoothing offers other than decreasing the learning rate or increasing the batch size?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors first analyzed the relationship between the batch size, learning rate, and test accuracy, showing that there is a correlation between $\frac{\eta C}{\sqrt{b}}$ and test accuracy.
Then, using these observations, the authors proposed Implicit Graduated Optimization, which changes the learning rate and batch size during the training.
The authors provided the convergence rate of Implicit Graduated Optimization and experimentally examined the effectiveness of their proposed method.

### Strengths
* The authors analyzed the relationship between test accuracy, learning rate, and batch size.

* Based on this relationship, the authors proposed Implicit Graduated Optimization that adjusts the batch sizes and learning rate during the training.

### Weaknesses
Overall, the reviewer feels that the proposed method itself is similar to that presented in previous studies, e.g., [1], and the clear advantage of the proposed methods over [1] has not been shown in this paper.
Designing the scheduler of batch sizes and learning rates from the perspective of graduated optimization seems to be novel, while the reviewer feels that the relationship between test accuracy and $\frac{\eta C}{\sqrt{b}}$, derived as a conclusion, does not appear to be very novel.
See below for a detailed comment.


* The reviewer does not think the relationship between $\frac{\eta C}{\sqrt{b}}$ and accuracy presented in this paper is very new since it is well-known that large batch sizes and small learning rates degrade test accuracy. While showing this relationship is a good motivation for designing the proposed method, the reviewer does not think that showing this relationship in itself is a major contribution.

* The reviewer does not understand the difference between the proposed method and existing methods, e.g., [1]. Changing the batch size during training has already been proposed in [1].

* All methods achieved approximately 60% in Figure 4. However, by comparing the results reported in the existing papers [1,2], 60% appears to be too low. Thus, the reviewer is wondering if the results are reliable.



### Questions
See the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
