# Adapting Prediction Sets to Distribution Shifts Without Labels

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Conformal prediction (CP) enables machine learning models to output prediction sets with guaranteed coverage rate, assuming exchangeable data. Unfortunately, the exchangeability assumption is frequently violated due to distribution shifts in practice, and the challenge is often compounded by the lack of ground truth labels at test time. Focusing on classification in this paper, our goal is to improve the quality of CP-generated prediction sets using only unlabeled data from the test domain. This is achieved by two new methods called \ecp~and \eacp, that adjust the score function in CP according to the base model's uncertainty on the unlabeled test data. Through extensive experiments on a number of large-scale datasets and neural network architectures, we show that our methods provide consistent improvement over existing baselines and nearly match the performance of supervised algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel approach to enhance the robustness of set-valued predictions, specifically Conformal Prediction (CP), in the face of distribution shifts without relying on test-time labels. The authors introduce two primary methods, ECP (Entropy scaled Conformal Prediction) and EACP (Entropy base-adapted Conformal Prediction), which leverage the uncertainty revealed by the base model to adjust prediction sets accordingly. Through extensive experiments on large-scale datasets and various neural network architectures, the paper demonstrates that these methods can significantly improve upon existing baselines and nearly match the performance of fully supervised methods.

### Strengths
The investigation presented in this paper on Conformal Prediction (CP) under distribution shifts is of considerable value, addressing an area that has received relatively little attention in existing studies.

### Weaknesses
The motivation behind this paper is that, under distribution shifts the overall output confidence of models tends to decrease, thereby affecting the performance of CP. However, there are several aspects in the method design that currently fail to convince me, such as:

1. Figure 1 observes the relationship between the model's output confidence and entropy, using this relationship as a key observation to guide the method design. But isn't this correlation trivial? Entropy and confidence are both indicators of model output uncertainty, especially when considering average entropy and confidence, as the method proposed in [1] treats both as indicators of model confidence.

2. The authors, through preliminary experimental observations, designed a method to enlarge the model's output under Out-Of-Distribution (OOD) conditions. I believe caution is needed for this design, as **existing research has widely pointed out that models face a more severe over-confidence phenomenon under OOD settings compared to In-Distribution (ID) settings**, and continuing to enlarge model outputs will inevitably exacerbate this issue. From this perspective, is the method in this paper reliable? Would a more over-confident model (which is certainly also more miscalibrated) be beneficial for CP?

3. Why do the authors use the quantile mechanism shown in Equation (3) to enlarge the model's output? This seems to lack insight. Assuming that the strategy to enlarge model confidence is correct (however, as mentioned in point 2, this assumption may not be correct), shouldn't we directly use a method like temperature scaling to align the model's average output on OOD and ID datasets?

I believe there are still many aspects of this paper that fail to fully convince the readers and require further clarification from the authors.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel conformal prediction method under distribution shift without using any labels from a shifted distribution. The key idea is rescaling a scoring function based on entropy, which measures a degree of shifts. Also, this paper updates the scoring function using test-time adaptation to enhance the efficiency of conformal sets. The proposed methods are evaluated over variations of ImageNet for distribution shifts.

### Strengths
This paper attacks an important problem of learning conformal sets under distribution shifts. The observation is simple and intuitive. It demonstrated the efficacy of the proposed method by using at least 6 shifted datasets.

### Weaknesses
I think the main concern of this paper is that the proposed method does not provide any theoretical guarantee, which is the crux of conformal prediction. Including this, see the following for additional concerns.

* The proposed method is heuristic, which does not align with paper trends of conformal prediction. Can you provide a theoretical coverage guarantee (i.e., the coverage probability bound) of the proposed method under the covariate shift assumption?
* For achieving a desired coverage, the method introduced two tuning knobs: \beta, f. \beta set to 1-\alpha, but choosing them is anyway very tricky in distribution shifts without labels. This suggests the proposed method is less practical. Could you suggest an adaptation method to learn f by only using unlabeled examples?
* In demonstrating the efficacy of the proposed method, it would be great if oracle results and no-shift results are included. In particular, you can consider SplitCP with access to labeled examples from a shifted distribution – this is an oracle result, which forms a empirical desired coverage / set size for the proposed method. Also, under no shift, the proposed method should work – this is also demonstrated to show the efficacy of the method as we don’t know whether there is a shift or not. 
* An important baseline is missing. The main competitor of this paper is conformal prediction under covariate shift (i.e., Tibshirani et al., 2019). The comparison should be conducted. Could you apply your method to visualize the second plot with oracle weights in Figure 2 of Tibshirani et al. (2019) and compare an empirical coverage along with average prediction set size?

### Questions
* Can you provide a coverage guarantee of the proposed method?
* Can you add oracle results and no-shift results to justify the efficacy of the proposed method?
* Can you compare the proposed method with Tibshirani et al., 2019?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Conformal Prediction intends to predict confidence set predictions rather than point predictions. This paper studies to improve the performance when there is domain shift for testing. First, this paper proposes ECP, which addaptively controls the perdiction set size by utilizing the uncertainty evaluation of the base model itself. Second, being motivated by the concept of TTA, this paper uses entropy minimization for optimizing the uncertainty. Without label annotation, this paper shows good performances.

### Strengths
The preliminaries are well formulated.

### Weaknesses
Please refer to the questions below

- What is resp. in the first paragraph of introduction section? It is not desirable to use undefined abberviation term without explaining it.
- Why there are cases when entropy optimization shows worse performance than the original ECP?
- The problem setting suggested by the authors cannot be solved by the foundation model, e.g. CLIP or LLMs?

### Questions
- What is resp. in the first paragraph of introduction section? It is not desirable to use undefined abberviation term without explaining it.
- Why there are cases when entropy optimization shows worse performance than the original ECP?
- The problem setting suggested by the authors cannot be solved by the foundation model, e.g. CLIP or LLMs?

### Soundness
3

### Presentation
3

### Contribution
2
