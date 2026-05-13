# Bayes Conditional Distribution Estimation for Knowledge Distillation Based on Conditional Mutual Information

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
It is believed that in knowledge distillation (KD), the role of the teacher is to provide an estimate for the unknown Bayes conditional probability distribution (BCPD) to be used in the student training process. Conventionally, this estimate is obtained by training the teacher using maximum log-likelihood (MLL) method. To improve this estimate for KD, in this paper we introduce the concept of conditional mutual information (CMI) into the estimation of BCPD and propose a novel estimator called the maximum CMI (MCMI) method. Specifically, in MCMI estimation, both the log-likelihood and CMI of the teacher are simultaneously maximized when the teacher is trained. Through Eigen-CAM, it is further shown that maximizing the teacher's CMI value allows the teacher to capture more contextual information in an image cluster. Via conducting a thorough set of experiments, we show that by employing a teacher trained via MCMI estimation rather than one trained via MLL estimation in various state-of-the-art KD frameworks, the student's classification accuracy consistently increases, with the gain of up to 3.32\%. This suggests that the teacher's BCPD estimate provided by MCMI method is more accurate than that provided by MLL method. In addition, we show that such improvements in the student's accuracy are more drastic in zero-shot and few-shot settings. Notably, the student's accuracy increases with the gain of up to 5.72\% when 5\% of the training samples are available to the student (few-shot), and increases from 0\% to as high as 84\% for an omitted class (zero-shot).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work  builds upon the insights from the previous study on knowledge distillation [1], which implies that producing a good teacher model 
similar to the optimal Bayes class probability $P^{*}_{X}$, is crucial for enhancing the performance of the student model. To convey this message, the authors propose a new training objective for the "teacher model" by introducing the empirical estimate of conditional mutual information as a regularizing term (MCMI). 

The authors provide empirical evidence between MCMI and the accuracy of the student model; as the MCMI attains higher values, the the corresponding teach model obtains the highest accuracy. Furthermore, when using the teacher model trained with the MCMI regularizer, the corresponding teacher exhibits improved accuracy in most existing knowledge distillation algorithms. The proposed regularizer leads to improved performance of the student model in zero-shot and few-shot classification tasks  as well.

[1] A Statistical Perspective on Distillation - ICML 21

### Strengths
### Simple idea:

> In implementation sense, the idea looks simple and easy to implement this idea; introducing a estimate of the MCMI in Eq (2) is additionally necessary.

### Empirical improvement:
> It seems that the proposed objective for the teacher model can be integrated with existing knowledge distillation algorithms which mainly focus on the distillation objective in view of "student" model. The proposed regularizer for the 'teacher' model seems to be effective in enhancing the performance of the 'student' model trained with existing knowledge distillation algorithms.

### Weaknesses
### Less elaboration on relationship between conditional mutual information $I(X , \hat{Y} | Y)$ and optimal bayes classifier $P^{*}_{X}$

> While it is intuitively clear that using the conditional mutual information as the regularizer term can capture the contextual information of $X$ (Image) and provide additional information to a student model, the direct connection between conditional mutual information and the optimal Bayes classifier is less explained. I believe explaining this connection is important because this approach is motivated from the importance of optimal classifier $P^{*}_{X}$. Specifically, the paper does not provide a clear explanation of how maximizing the conditional mutual information $I(X, \hat{Y}|Y)$ leads to a teacher model that better approximates the optimal Bayes classifier $P^{*}_{X}$. The intuition provided is that it captures contextual information, but a more rigorous argument is needed to link this to the properties of $P^{*}_{X}$. For instance, it is unclear how the proposed regularizer ensures that the teacher's output distribution is not only informative but also calibrated to reflect the true underlying probabilities of the classes given the input, which is a key characteristic of the optimal Bayes classifier. Furthermore, the paper lacks a discussion on the potential limitations of using an empirical estimate of conditional mutual information, particularly in scenarios with limited data or high dimensionality, where such estimates can be unreliable.



### Questions
* Q1.  Could you elaborately explain why minimizing $I(X , \hat{Y} | Y)$ can make the teacher model $f$ to be more similar to the optimal bayes classifier ? 



* Q2. It seems that the proposed regularizer requires the pre-trained model as the teacher model and apply the further training to the teacher model with the proposed objective of Eq. (14). How do we set the number of iterations further training? Based on my understanding, since we expect this regularizer to make the teacher model contain additional information as well as to be properly certain (not overconfident), setting the number of iterations is important hyperparameters and might significantly affect the performance of student model.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method which aims to train the teacher to optimise the student. This is achieved through maximising the conditional mutual information between input and predicted label, conditioned on the true label. The approach demonstrates improved knowledge distillation on CIFAR100 and Imagenet using varies CNN architectures.

### Strengths
* The paper is very simple to understand and implement, which only a simple regulariser added to the training of the teacher model, which minimises the KL between the predicted probability and the average probability. 
* The results are conclusive and well presented on ImageNet using plenty of architectures. 
* The extension to few and single-shot experiments are nice.

### Weaknesses
In terms of weaknesses:
* I'm interested to read more about what the role of the CMI regulariser actually does, is it just decreasing the variance of the predictions? Or leading to a distribution with higher entropy? Does this method work just as well if you add an entropy regulariser? Specifically, it's unclear how the CMI regularizer affects the feature space and the resulting probability distributions. Does it encourage more compact clusters for each class, or does it lead to more dispersed representations? It would be beneficial to understand the impact on the geometry of the feature space, and whether this is the key to the improved distillation performance. Furthermore, it's not clear if the CMI regularizer is simply acting as a form of label smoothing or if it has a more fundamental effect on the learned representations. A comparison with a standard label smoothing approach would be beneficial.
* As far as I can tell, the value $T$ is not defined, is this for the softmax?

### Questions
* What is the value of $T$? 
* Does the CMI loss just reduce the entropy?
* If so, is it possible that the same effect can be achieved by simply running this method with temperature scaling? I.e. drop the CMI term?
* With regards to 6.2. my understanding is that this is using the negative scores during training, so is this really zero-shot classification? Why do you expect this?
* Did you try varying different classes to drop? 
* In Figure 3, why is the heat map on the terrier not on the body of the animal? Bottom, third from left.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new distillation technique which is based on training teacher models so that they are well-suited for conveying information to the student models. Towards that end, the authors introduce a"conditional mutual information"(CMI) objective into the training process of the teacher model, whose goal is to improve the teacher's Bayes conditional probability estimates (via its soft-labels) — according to recent knowledge-distillation literature, more accurate Bayes conditional probability estimates result in better student's performance.

Overall:

(i) The authors argue that the so-called dark knowledge passed by the teacher to the student is the contextual information of the images which can be quantified via the conditional mutual information.
(ii) They provide evidence that temperature-scaling in KD increases the teacher's CMI value
(iii) They provide evidence that show that models with lower CMI values are not good teacher's, even if they're more accurate.
(iv) They provide experiments on CIFAR-100 and Imagenet datasets showing evidence that their method helps in improving the student's performance, compared to other standard distillation techniques.
(v) They show that their technique is especially effective in few-shot and zero-shot settings.

### Strengths
This is a well-written paper that presents a novel approach to knowledge distillation. They authors have provided extensive experimental evidence.

### Weaknesses
— The role of the teacher as a "provider of estimates for the unknown Bayes conditional probability distribution" is a theory for why distillation works that applies well mainly in the context of multi-class classification, and especially in the case where the input is images. (Indeed, there are other explanations for why knowledge distillation works, as it can be seen as a curriculum learning mechanism, a regularization mechanism etc see e.g. [1])

In that sense, I feel that the author should either make the above more explicit in the text, i.e., explicitly restrict the scope of their claims to multi-classifcation and images, or provide evidence that their technique gives substantial improvements on binary classification tasks in NLP datasets (but even in vision datasets).

— One of the main reasons why knowledge distillation is such a popular technique, is because the teacher can generate pseudo-labels for new, unlabeled examples, increasing the size of the student's dataset. (This is known as semi-supervised distillation, or distillation with unlabeled examples, see e.g. [2, 3]. )  It seems that, in order to apply the current approach, one requires the ground-truth labels and, thus,  one has to give up a big part of the power of knowledge distillation as a technique.)

To be clear, I still like the paper and I am leaning towards acceptance even if the scope of the paper is more limited, but I think it would be beneficial to the research community if the above comments were addressed.

### Questions
— Does the proposed method and theory works well/applies in NLP datasets/binary classification contexts? 
— Is there a way to apply this technique in the context of semi-supervised distillation?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
