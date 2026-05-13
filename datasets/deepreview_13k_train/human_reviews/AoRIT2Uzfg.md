# DRMGuard: Defending Deep Regression Models against Backdoor Attacks

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
Deep regression models are used in a wide variety of safety-critical applications, %Examples such as %driver and pedestrian attention monitoring. %driver attention monitoring and navigation of autonomous vehicles. Unfortunately, they 
but are vulnerable to backdoor attacks. Although many defenses have been proposed for classification models, they are ineffective as they do not consider the uniqueness of regression models. First, the outputs of regression models are continuous values instead of discretized labels. Thus, the potential infected target of a backdoored regression model has infinite possibilities, which makes it impossible to be determined by existing defenses. Second, the backdoor behavior of backdoored deep regression models is triggered by the activation values of all the neurons in the feature space, which makes it difficult to be detected and mitigated using existing defenses. To resolve these problems, we propose {\name}, the first defense to identify if a deep regression model in the image domain is backdoored or not. {\name} formulates the optimization problem for reverse engineering based on the unique output-space and feature-space characteristics of backdoored deep regression models. We conduct extensive evaluations on two regression tasks and four datasets. The results show that {\name} can consistently defend against various backdoor attacks. We also generalize four state-of-the-art defenses designed for classifiers to regression models, and compare {\name} with them. The results show that {\name} significantly outperforms all those defenses.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a backdoor defense method named DRMGuard to tackle backdoor attacks of deep regression models. The core technique is to optimize the variance of feature representations when the cadidate outputs are uncountable. The authors conduct extensive experiments to demonstrate the effectiveness of DRMGuard.

### Strengths
1.	The research problem is of great significance
2.	The paper is well-structured and easy to follow.
3.	The idea is novel and inspiring.

### Weaknesses
1.	Time complexity. I notice that the authors did not report the running time of DRMGuard. I am not sure whether the variance calculation is time-consuming and could be scaled to higher dimensional conditions. Specifically, the variance calculation involves computing the covariance matrix of the deep feature representations, which can be computationally expensive, especially with high-dimensional feature vectors and large batch sizes. The authors should provide a detailed analysis of the computational cost associated with this step, including the time complexity with respect to the input dimensionality and batch size.
2.	Extension to classification models (not very important). In my opinion, the key of this work is that we could use the variance of deep representations for trigger inverse optimization when the candidate labels are uncountable. I think this method could be extended to deep classification models. I suggest the authors conducting this method in classification experiments. It would be beneficial to explore how the variance of the softmax output probabilities behaves under trigger and non-trigger inputs. The authors should investigate whether a similar variance minimization approach can be applied to the probability vectors of classification models, and discuss the potential challenges and modifications needed for such an extension. 
3.	Typos. In Table 8, MRT -> MTR.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
3 good

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
This paper proposed a model-level backdoor defense which tries to reverse-engine the trigger signal from backdoored model. Specifically, the authors considered a new scenario, i.e., deep regression task, where the output of the model is a vector instead of discrete output in the deep classification task. For instance, in a deep regression task, called gaze estimation, the deep regression model will output a vector to represent the direction of one person view. In this new scenario, the existing related work will not work since some of them [(Wang et al., 2019] recovered a suspect trigger signal for each class, and then determine the true trigger from all suspects. However, the existing works cannot be directly used in deep regression tasks since the defender cannot the infinite outputs. The main contribution of this work solves this problem.

### Strengths
The authors proposed new reverse engineering method to recover the backdoor attack in the deep regression task.

### Weaknesses
The main idea to reconstruct the trigger is based on the generative model, which has been exploited following references:
[1] Zhu, Liuwan, et al. "Gangsweep: Sweep out neural backdoors by gan." Proceedings of the 28th ACM International Conference on Multimedia. 2020.
[2] Chen, Huili, et al. "DeepInspect: A Black-box Trojan Detection and Mitigation Framework for Deep Neural Networks." IJCAI. Vol. 2. No. 5. 2019

Secondly, the new proposed method proposed a new regularization, which is $r_{f}$ shown in Equation 5. This regulation is only designed based on the empirical results, i.e., the angle of poisoned inputs is more concentrated than the benign data. There is not any theoretical proof to support this.

### Questions
Is it possible to compare the ABS method, which is only mentioned in the introduction but isn’t as a state-of-the-art to compare. The reason why I raise this question is that the ABS directly analyze the middle layer feature to reconstruct the trigger. It is will not affected by the infinite of output influence made by deep regression task.

### Soundness
1 poor

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
This paper proposes a model-based backdoor defense method against the deep regression model. This paper proposes to leverage trigger reverse to detect and remove backdoors from the deep regression models. The experiments demonstrates its effectiveness.

### Strengths
1.This paper investigates backdoor defense in deep regression model, which has not been explored before.

### Weaknesses
1. The novelty is limited. The trigger reverse method is similar to Neural Cleanse.
2. This paper should emphasize the importance of the backdoor in the regression models. Why is it important in the regression area?
3. The number of categories of compared methods and backdoor attacks is clearly below ICLR acceptance threshold.

### Questions
Why is backdoor defense important in the regression area?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
