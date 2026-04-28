# Orthogonal Representation Learning for Estimating Causal Quantities

- Decision: Reject
- Scores: 3, 6, 8

## Abstract
Representation learning is widely used for estimating causal quantities (e.g., the conditional average treatment effect) from observational data. While existing representation learning methods have the benefit of allowing for end-to-end learning, they do not have favorable theoretical properties of Neyman-orthogonal learners, such as double robustness and quasi-oracle efficiency. Also, such representation learning methods often employ additional constraints, like balancing, which may even lead to inconsistent estimation. In this paper, we propose a novel class of Neyman-orthogonal learners for causal quantities defined at the representation level, which we call OR-learners. Our OR-learners have several practical advantages: they allow for consistent estimation of causal quantities based on any learned representation, while offering favorable theoretical properties including double robustness and quasi-oracle efficiency. In numerous experiments, we show that, under certain regularity conditions, our OR-learners improve existing representation learning methods and achieve state-of-the-art performance. To the best of our knowledge, our OR-learners are the first work to provide a unified framework of representation learning methods and Neyman-orthogonal learners for causal quantities estimation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript introduces a new approach to estimating causal quantities by learned representation. With a carefully chosen target risk, a Neyman-orthogonal learner is proposed. Although claiming the theoretical guarantees, the authors do not provide any theoretical analysis. In addition, there is no foundation for some claims (see details in the questions). Lastly, there is still a large room for improvement in the writing to achieve a publication level.

### Strengths
The authors raise an interesting question, although the solution can still be improved.

### Weaknesses
The author may want to present some evidence for some claims in the manuscript. In addition, combining existing ideas may not be interesting enough. The writing can be much improved.

### Questions
1) The manuscript claims that any representation can work. However, proving $Y(0), Y(1)\perp Z|\Phi(X)$ is not easy, and the conditional independence does not hold for any representation. With this condition, the downstream analysis is biased. 

2) Formula (10) does not include $g$

3) What is the difference between $V$ and $\Phi(X)$?

4) Estimating nuisance functions can be difficult sometimes. How does the accuracy in estimating nuisance functions affect the final estimation?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on an important problem of estimating causal quantities, including effects and potential outcome mean. This paper proposes to use representations, instead of using original covariates, to learn the causal quantities in the second second stage of DR-learner/R-learner. This paper also provide detailed discussion on the advantages compared with original representation learning methods.

### Strengths
1. The paper provides a three-stage causal quantities estimation method, which achieves the DR property.
2. Experimental results verify the effectiveness of the proposed method.

### Weaknesses
1. A very key and similar work related to this paper is [1]. My biggest concerns are:
   1. [1] is not well discussed in the main part of the paper. If I understand correctly, the difference between this paper and [1] is that [1] uses original covariates to learn target parameters and this paper uses representations. Could you clarify the advantages compared with [1]?
   2. In experiments, $V=X$ can be seen as an implementation of [1] (please correct me if I misunderstand). However, the conducted experiments only use 1 hidden layer FC, which may explain why the improvement of $V=X$ is much less than $V=\Phi(X)$. It would be fairer and better to use more deep neural networks.
2. It would be better to provide the theoretical improvement that OR-learner brings.
3. It could be better to move Figure 6 to the main body of the paper.

I would be very happy to raise my score if the authors could address my concerns well.

[1] Curth A, Van der Schaar M. Nonparametric estimation of heterogeneous treatment effects: From theory to learning algorithms[C]//International Conference on Artificial Intelligence and Statistics. PMLR, 2021: 1810-1818.

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper builds on former work on representation learning for treatment effect estimation and pseudo-outcome-based meta-learners satisfying Neyman orthogonality to propose OR-learners, a general meta-learner framework where the pseudo-outcome is learnt not with the original covariates as input features, but with representations that are learnt beforehand using canonical representation learning for treatment effect methods. Intuitions to justify the contribution of the procedure are given, which are further demonstrated in experiments.

### Strengths
Originality : It is indeed the first time that I see a contribution on using a two-stage learner, where the two stages are 1) learning a representation to be used as an input for treatment effect estimation, 2) feeding it to pseudo-outcome learning  (with nuisance functions to fit separately) for treatment effect estimation.

Quality&Signifiance: The paper provides an extensive review of the previous literature, and provides an interesting taxonomy of representation learning for treatment effect estimation methods (e.g. without balancing constraints, (non-)invertible with balancing constraints). Experiments seem extensive and able to justify that the method does improve over former baselines.

Clarity : The paper is generally clear in its introductory parts up to Section 3 and in Appendices. I also appreciate the extensive use of figures.

### Weaknesses
EDIT Nov 13 : apologies, looks like links did not work! I have re-entered them.

EDIT Dec 1 : edited the score due to author-reviewer discussion.

Originalty&Signifiance : while it is the first work I see learning representations in a "treatment effect estimation friendly" way (i.e.using treatment and/or outcome information together with covariates) to be fed into pseudo-outcome learning, it is not the first method that generally feeds such representations to any treatment effect estimation, even doubly robust methods. More specifically, the submission seems to ignore the extensive and more classical, non-DL literature on such representations, and their use of inputs of treatment effect estimation methods. See for example [propensity scores](https://academic.oup.com/biomet/article/70/1/41/240879), [prognostic scores](https://www.jstor.org/stable/20441477), [sufficient dimension reduction](https://www.tandfonline.com/doi/full/10.1080/07350015.2019.1609974), and [deconfounding scores](https://arxiv.org/pdf/2104.05762). Note that the last reference explicitly feeds a learnt representation into AIPW, a classical doubly-robust method.

Quality&Clarity : besides this former work, what I find is really missing is a mathematical analysis of the proposed method, which is critical as 1) the paper explicitly says that the method "offer[s] favorable properties of Neyman-orthogonality", which are typically demonstrated mathematically, and might be contradicted if the learnt representation is degenerate (e.g. constant), 2) the performance of the method would generally depend on special cases of the representations, e.g. a) it is a constant, as mentioned before, b) it has RICB different from 0, c) it has RICB zero or converging to zero, d) it converges or is equal to a perfect balancing score (predicts treatment assignment) or prognostic score (predicts outcome regression). Instead, the submission uses textual "intuitions" that I find might lack substance, justification or clarity (see questions)

### Questions
(Please note that I am very open to increase my score if the above weaknesses and below questions are addressed)

> l.234 : Also, for CATE estimation, we can consider an overlap-weighted MSE alternative of 

A reference is missing here.

> l.304-306 : "This can be formalized with the notion of (Holder) smoothness (Ohn & Kim, 2019): Each layer induces a new space in which the ground-truth regression function becomes smoother and thus easier to estimate."

I do not understand exactly where in the reference the claim is justified?

> l. 310-316 

Any mathematical or bibliographical justification for why these methods "can be also considered asymptotically valid"? and why specify a dimension of 2 or more?

> l.319-320 : "Therefore, the second-stage model $g(\phi)$ uses additional propensity information and achieves more efficient estimation."

Do you have a mathematical and/or bibliographical (i.e. a reference) justification?

> l.365-367 : "Then, in order to minimize the original MSE loss, the representation network would scale up the parts of space to increase the smoothness of ..."

Do you have a mathematical and/or bibliographical (i.e. a reference) justification?

> l.381-384 : "Our OR-learners then will effectively try to “undo” the effect of balancing, as they reintroduce the propensity weighting. Specifically, DR-learners would “re-focus” the target models on the parts of the representation space with the lack of overlap, while R-learner would ignore them fully"

By balancing, you generally mean minimizing the difference between the distributions of the representation between both groups, right? (Please be specific, as propensity weighting is generally considered balancing!) Also, can you elaborate on this re-focusing will be done? Indeed, with $\Phi(X) = 0$, we have perfectly balanced and overlapping representation, but it cannot be used for any form of estimation!

l> .396-398 : ", but also to fold it, project it, etc. When balancing is applied, non-overlapping parts of the space could be simply folded together or projected onto some subspace, so that they become balanced."

What do you mean exactly by "fold"? That the representation is not injective?

> l.404-405 : "Asymptotically, our OR-learners will help to remove the RICB so that we can consistently estimate representation level CAPOs and CATE."

Justification? Especially if $\Phi(X) = 0$ (which seems to be encapsulated by this section), then the RICB will just never disappear!

> l.407-410 : "On the other hand, in the finite-sample setting, our OR-learners will “undo” the effect of balancing by employing the covariate propensity score. Therefore, our OR-learners on the one hand can “undo” the benefit brought by balancing (if there is such a setting), and, on the other, partially fix the damage after applying too much balancing." :

Tied to the above on l.381-384, but also : can you mathematically or bibliographically justify that this happens in finite-samples?

> l.531-534 : "Informally, balancing assumes that the lack of overlap implies a lack of potential outcomes/treatment effect heterogeneity." 

Any mathematical or bibliographical justification?

### Soundness
2

### Presentation
3

### Contribution
2
