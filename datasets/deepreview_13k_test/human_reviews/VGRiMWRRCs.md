# Learn from Known Unknowns: A Unified Empirical Bayesian Framework for Improving Group Robustness

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
The lack of group robustness has emerged as a critical concern in machine learning, as conventional methods like Empirical Risk Minimization (ERM) can achieve high overall accuracy while yielding low worst-group accuracy in minority groups. This issue often stems from spurious correlations—non-essential features that models exploit as shortcuts—which can compromise deep learning models in high-stakes applications. Previous works have found that simply retraining classifiers with reweighted datasets or rebalanced samples could significantly improve robustness. However, existing methods lack a unified framework, as they often exhibit inconsistent performance across datasets, and sometimes rely heavily on hyperparameter tuning, making them impractical for real-world datasets. In this work, we first argue that existing methods can be unified as one Empirical Bayesian framework, where a priori of group information is not specified. We then propose our method \textit{Learn from Known Unknowns} under this framework by quantifying the epistemic uncertainty of biased ERM models and introducing a selective reweighting technique for retraining. Our empirical results demonstrate that this approach improves group robustness across diverse datasets and reduces reliance on hyperparameter tuning, offering a more efficient and scalable solution to spurious correlations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a unifying framework through which they view group robustness algorithms that operate without group information. The framework, based on Empirical Bayes, first infers group information p(g|x,y) and then optimizes a conditional label distribution. The paper demonstrates that the method falling out of this interpretation performs well on a set of standard group robustness benchmarks.

### Strengths
The paper studies an important problem and uses a well-motivated statistical framework. On the practical side, the results are undoubtedly better than the baselines they consider, and the method seems very promising for improving group robustness.

### Weaknesses
I had trouble following the paper after Section 4. In particular, I did not understand the connection between the Empirical Bayes framework and "evidential deep learning," which the paper does not do enough to explain. I suggest that the authors dedicate more time to explaining the connection between the two concepts and illustrating how their perspective makes such an approach the obvious one.

I was also somewhat underwhelmed by the theoretical result, which seems to be a restatement of Tweedie's formula with the variables replaced using the context of the paper. The authors can improve this section by (a) highlighting what is new/different between their result and Tweedie's formula, and more importantly (b) experimentally verifying to what extent the assumptions of their theorem hold in practice.

Finally, the paper consistently claims to be more robust to hyperparameters than other methods, but I did not see a study of hyperparameter robustness in the main text or in the appendix. The introduced method does seem to require hyperparameters (e.g., the evidence regularization strength) that seem like they would be important, so I am not sure the authors do enough to back up the claim that their method is more robust to hyperparameters than baselines.

### Questions
None beyond the weaknesses above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a new method for the problem of group-wise distributionally robust optimization (group DRO) without group labels. At a high-level, the idea is to learn weights so that reweighted empirical risk minimization emulates the effects of group DRO. The authors support their method with computational results on a variety of distribution shift datasets in which certain spurious correlations in the training data disappear in the test data.

### Strengths
It is hard for me to assess the originality, quality, and significance of the paper because it's (lack of) clarity prevents me from assess its strengths.

### Weaknesses
The main weakness of the paper is the lack of clarity. After reading the paper three times, I'm still unclear on some details of the proposed method. Without properly understanding the paper, it is hard for me to assess its weaknesses.

### Questions
1. What is the role of S3? It seems nothing is lost if S3 is omitted from the paper. What role does Thm 3.1 play in the developments in S4 and S5? It is not referred to in S4 and S5.
2. What are the evidence values for each class (the $e_k(x)$'s)? Please define them mathematically.
3. What is $u(x_i)$ that appears on l.333? In the context of the weighted ERM objective (on l.333) it appears $u(x_i)$ is a scalar, but on l.326, it is defined as a probability distribution.
4. Although the method does not require group labels, does it require knowledge of the set of possible groups? (eg for waterbirds, does the method need to know that the set of possible groups are land bird-land bg, land bird water bg, water bird, land bg, and water bird-water bg)?

I may have more questions for the authors once I get a better grasp of the proposed method. Once I better understand the method, I'm likely to change my score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The scope of the paper is to improve group-robustness of classification models. Group is defined as a combination of a target variable for the classification, along with some attribute variable. Target and attributed variables are spuriously correlated under the training set, however this might not be the case during inference. We want to train models that achieve equally good classification accuracy for all groups. We measure this by worst-group accuracy.

Past methods that simply retraining the last network layer on reweighted losses or resampled data achieves good worst-group accuracy. However, results are inconsistent across datasets, and methods exhibit high sensitivity to selected hyperparameters.

The authors present an alternative group-unsupervised training algorithm (Learn from Known Unknowns), which estimates the epistemic uncertainty of biased models, in order to discover majority/minority groups in a group-unsupervised way and to reweight per-sample loss during retraining (of a group-robust classifier).     

## Claims
1. Popular reweighting/resampling methods can be cast as instances of a unified empirical Bayes framework.
2. The proposed method improves across datasets.
3. The proposed method reduces reliance on hyperparameter tuning.

### Strengths
The paper introduces a novel method for group-robustness. It utilizes uncertainty estimation to discover majority-minority groups and consequently reweight their contributions during robust retraining. It establishes empirically through experiments the efficacy of this method, surpassing prior art on Waterbirds, MultiNLI and CivilComments, while being competitive on CelebA. At the same time, they hint qualitatively that high prediction uncertainty in classifiers correlates with the classifier relying to spurious features for predictions.

### Weaknesses
Presentation of proposed method is relatively clear there are some parts however that can be further elaborated:
1. It is not clear why the prior probability on model parameters $p(\theta)$ refers to parameters of trained ERM models. Usually from a MAP estimation perspective, $p(\theta)$ translates usually into a regularization loss on the model parameters (like weight decay, if the assumed prior is gaussian) and a maximization of the $\prod_i p(y_i|x_i, \theta)$, which can be equivalently cast as minimization of the negative log-likelihood. Not sure about Table 1. Can also other classes of probabilistic-inspired methods be interpreted under this perspective? For example logit adjustment for group robustness [1,2].

[1] Liu et al., “Avoiding spurious correlations via logit correction”, ICLR 2023
[2] Tsirigotis et al., “Group Robust Classification Without Any Group Information”, NeurIPS 2023

2. While the paper operates under group-agnostic assumptions, they proceed to develop reasoning given that group variables come from an unknown distribution. Assumptions about the structure of that distribution are needed for the derivations of the paper. In particular, we can infer that the group variable is treated as a binary variable for “majority”-class or “minority”-class; an assumption which is not explicit in the paper.

3. About the result in Section 3.3: According to Appendix D, the derivation relies on two unstated strong modelling assumptions about the exponential distribution of $p(y|x,\theta,g)$. Namely,  that $h(y)$ is constant and that the natural parameter vector is just a product $\theta \cdot g$. Are these assumptions impairing the generality of the statement? In my reading, I think yes. Also, the last step of the proof is not clear; how do we go from the exact to the approximation using “the mean of $g$” and “the variance $sigma^2$ of $T(y)$”? Please expand.

4. Section 3.3 result seem unused in the paper. At the end of the method’s development, the authors decide to estimate $p(g | x, \theta) = u(x)$. Is this decision informed by the theory of Section 3.3? How is this decision motivated?

5. Please elaborate on the Evidential Second-Order Risk Minimization. How do we use the model to compute the non-negative evidence values per class $e_k(x)$? What does regularizing with Evidence Regularization do to the model outputs?

Further details about experimental evidence is needed to support the claims of the paper about the proposed method:
6. Details about model selection are missing. Group-robustness methods (and more generally OOD robustness methods) are not only sensitive to hyperparameter selection, but also to model selection during training [3]. Please provide the following details for the reproducibility of the experiments: a. “Model selection is based on the highest average accuracy on the validation set”. Is the validation set group-balanced or does it follow the same distribution as the training set?, b. Please provide training curves for the robust model, following the validation criterion and reported performance on the test set (worst-case accuracy and average accuracy) for example on Waterbirds across training steps.

[3] Gulrajani et al, “In Search of Lost Domain Generalization”, ICLR 2021

### Questions
1. What does $p(y|x,\theta,g)$ mean intuitively? One model per group? Please introduce the decomposed terms more clearly to build intuition.
2. Why does high epistemic uncertainty on samples lead to identification of the minority group?
3. Regarding the result on CelebA, how would your method perform if you were finetuning instead a network pretrained with SSL on CelebA? How would applying the proposed method compare to CnC then?
4. Why does the evidential ERM training have weight decay, while the group-robust retraining does not?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses avoidance of spurious correlations when training data contains examples with and without the spurious correlation, but their group association is unknown.
They attempt to (1) unify the previous methods under a Bayesian framework, and (2) propose a revised algorithm that also models the uncertainty in the example-to-group assignment.
The paper evaluates on four datasets and a synthetic dataset.
Their proposed algorithm contains two steps (similar to the previous methods): (a) train "evidential" ERM to better capture the uncertainty in label prediction, (b) retrain the last-layer of the previously trained model while up-weighting the loss of uncertain examples.  

The paper has technical inconsistencies, and did not support many of their claims.

### Strengths
Summarising the many existing methods on how they differ from each other in Table 1 is insightful.

### Weaknesses
**Technical inconsistencies or notation challenges**

In Eqs. 5-7 present how the model accumulates the posterior on g inference for refining the model. Previous works and theirs differ in how they use the group labels:
(a) $p(g\mid x, \theta)$ is incorrect since the group labels are estimated and frozen when training $\theta$, (b) there is no marginalization of probabilities involved but only weighted average of the losses.

g is defined as (y, a) but different methods only identify the majority vs minority, which need not identify the label (y) or g.

For the above reasons, I am not convinced of their unifying Bayesian framework. Also, Table 1 introduces undefined terms, e.g. $g_\theta(x)$ for SELF and contrastive learning for CnC.

**Unsupported Claims or missing ablations**

They started motivating their method to derive $\Pr(g\mid x, \theta)$ in a more principled manner without resorting to any heuristic (like in previous methods) as stated in lines 256-258.
But they plainly introduce uncertainty in label predictions as a proxy for the group label probability (in line 324).

One of their contribution is also that their method reduces dependence on hparam tuning (in Lines 93-95) but that is not supported in the main content.

Synthetic experiment visualized and exposit ERM vs theirs, but I am not convinced how their method is better than some of the previous methods. I believe uncertainty is just as informative as say JTT.
Another missing ablation is to use SELF (or other methods that only tune the last layer), etc. with the evidential ERM as the backbone. 

**Irrelevant Theorem 3.1**

I do not see Thm 3.1's contribution to the paper.

### Questions
Why is in Table 3, "Class 0, Color 1" group has much higher accuracy than "Class 1, color 0"? If the model has color as a spurious correlation, shouldn't they both have equal but low accuracy?

For many of the sub-population shift datasets that use the worst-group accuracy metric, large deviation is expeted owing to the small minority group population even in the test set.
Reporting std. dev is expected in Tables 4, 5. 

Also, please address questions from the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
