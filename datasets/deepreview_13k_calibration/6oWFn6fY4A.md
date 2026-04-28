# Towards Understanding Why Label Smoothing Degrades Selective Classification and How to Fix It

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Label smoothing (LS) is a popular regularisation method for training neural networks as it is effective in improving test accuracy and is simple to implement. ``Hard'' one-hot labels are ``smoothed'' by uniformly distributing probability mass to other classes, reducing overfitting. 
    Prior work has suggested that in some cases \textit{LS can degrade selective classification (SC)} -- where the aim is to reject misclassifications using a model's uncertainty. In this work, we first demonstrate empirically across an extended range of large-scale tasks and architectures that LS \textit{consistently} degrades SC. 
    We then address a gap in existing knowledge, providing an \textit{explanation} for this behaviour by analysing logit-level gradients: LS degrades the uncertainty rank ordering of correct vs incorrect predictions by regularising the max logit \textit{more} when a prediction is likely to be correct, and \textit{less} when it is likely to be wrong.
    This elucidates previously reported experimental results where strong classifiers underperform in SC.
    We then demonstrate the empirical effectiveness of post-hoc \textit{logit normalisation} for recovering lost SC performance caused by LS. Furthermore, linking back to our gradient analysis, we again provide an explanation for why such normalisation is effective.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the impact of label smoothing (LS) on selective classification (SC), showing that while LS is a popular regularization technique for improving classification accuracy, it degrades SC performance. The authors empirically confirm this degradation across various models and tasks, then analyze the cause at a gradient level, finding that LS suppresses the highest logit differently based on prediction correctness. They propose post-hoc logit normalization as a solution, showing it effectively recovers SC performance degraded by LS.

### Strengths
**Originality**

The paper addresses a unique gap by investigating LS's unintended effect on SC. The logit-level gradient analysis provides a fresh perspective on why LS interferes with SC, helping bridge theoretical understanding with observed results.

**Quality** 

The experiments are well-designed, involving diverse datasets (e.g., ImageNet, Cityscapes) and model architectures (e.g., ResNet-50, ViT) to thoroughly validate the findings. The analysis at both empirical and gradient levels strengthens the rigor, making the results compelling.

**Clarity** 

The paper is well-organized, with clear visuals that illustrate LS’s effect on SC. Figures showing SC degradation and the effects of logit normalization make complex points more accessible.

### Weaknesses
My only concern is about the novelty of the contributions.

**Novelty concern**

*   As admitted by the authors (Line 212), some of the core conclusions in the main paper are based on previous empirical observations (```for a single value of alpha LS degrades SC for CNN-based image classification```). And the introduced ```broader investigation``` draws the same conclusion as the literature.

*   As specified by the authors (Line 416), another main contribution of the paper (```Logit Nomarlisation Improves the SC of LS-Trained Models```) also follows from the literature that ```logit normalization can improve the SC performance of many (but not all) pretrained models```.

### Questions
**Q1:** As observed by the authors, LS consistently leads to degraded SC performance, even if it may improve accuracy. What do authors think about the connection between NLS and SC, where NLS refers to Negative Label Smoothing introduced in R1.

**Q2:** In Line 132, it would be beneficial to include the definition of Kronecker delta.

**References:**

R1: To smooth or not? when label smoothing meets noisy labels. ICML 2022.

### Soundness
3

### Presentation
3

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
This paper shows how label smoothing (LS) can negatively impact selective classification (SC) by combining empirical analysis on large-scale tasks with theoretical insights on logit-level gradients. The authors show that the degradation in SC performance worsens with increased LS strength, and they propose post-hoc logit normalization as an effective method for recovering SC performance lost due to LS.

### Strengths
- The paper provides a well-rounded analysis, both theoretical and experimental, demonstrating how LS degrades SC. By analyzing logit-level gradients, it addresses why LS has this adverse effect on SC, filling an important gap in understanding.
- Visualizations in the paper effectively illustrate the results, providing an intuitive understanding of how LS impacts SC performance.
- The findings have practical impact. By showing that LS leads to consistent degradation in SC, the paper suggests that it may partially explain the findings of strong classifiers surprisingly underperform on SC. They further shows that logit normalization can recover the degradation. This could be useful especially in the high-risk tasks like medical or robotics tasks.

### Weaknesses
The experimental analysis is limited to image classification and segmentation tasks, using only two specific datasets. This raises questions about the generalizability of the findings to other domains, such as text or tabular data, where label smoothing and selective classification may behave differently. Expanding the analysis to include diverse data types would strengthen the claim that label smoothing consistently degrades SC performance across various domains.

### Questions
- The experimental analysis is primarily focused on image classification and segmentation tasks, using two specific datasets. Could these findings generalize to other domains, such as text or tabular data?
- In Figure 3, the degradation impact of LS on SC decreases at high coverage. Is it possible to identify a threshold at which the effect of LS on SC begins to diminish?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explains why logit nomalisation improves SC performance for models trained with label smoothing.

### Strengths
1. I enjoy reading the paper. The presentation and organization look great.
2. This work provided both empirical and theoretic analysis to answer a research problem and considerably contributed to the field.

### Weaknesses
1. While the authors provided detailed experiments to demonstrate the properties of LS. I think it is also important to quantitatively compare the LS+logit normalisation with other existing solutions under the experimental setting used in this work to demonstrate the effectiveness of such a combination. Specifically, it would be beneficial to see a comparison against other methods that also aim to improve selective classification performance, such as temperature scaling or other post-hoc calibration techniques, under the same experimental conditions. This would help to contextualize the contribution of the proposed method and highlight its advantages or disadvantages compared to existing alternatives.

2. In figure 7(a), it is hard to find the "CE logit norm". The color choice makes it difficult to distinguish this line from others, hindering the visual comparison of different methods.

### Questions
N.A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Label smoothing (LS) is a popular regularization technique that improves test accuracy, yet previous research has shown that the LS models achieve degraded performance of selective classification (SC)
By comparing the formulation of Cross Entropy (CE) model and LS model, this work provides an explicit explanation on why this performance degradation is happening.
Building on the identified reasons for this degradation, the authors further discuss the impact of logit normalization and why it significantly improves SC performance of LS models but not that of CE models.
The primary contribution of this paper is the theoretical clarification of a previously unresolved issue. The experimental results are consistent with the theoretical findings presented in the paper.

### Strengths
Originality: the paper provides a very detailed and theoretic explanation for the unresolved issue of why label smoothing degrades selective classification.
Quality & Clarity: their explanations appear to be very reasonable. The theoretical gradient descent expressions align with the actual experimental results, making their work seem like a solid theoretical piece rather than some far-fetched guess.
Significance: The authors' explanation addresses a research gap and is likely to be valuable and insightful for future studies in selective classification.

### Weaknesses
While the authors present most of the logic and theory in an understandable and clear manner, unfortunately, the confusion in notation and concepts keeps me oscillating between being confused and understanding. The authors probably need to clarify some logic that they consider obvious but which I find uncertain. These points include:

1. Line 318: I would like to know more clearly the connection between the regularization in Equation 13 and the regularization gradient in Equation 14. Because, in my view, regularization refers to -\alpha/K, which is an item in L_LS, but the regularization gradient includes \alpha \bar{\pi}_k - \alpha/K, which is the result of L_LS - L_CE. The relationship between these two needs to be explicitly identified when they have similar names.
2. Line 319: There is a typo after the second equals sign in the formula.
3. Line 353: 'This directly impacts softmax-based U such as MSP', but I am not very clear on how. In fact, starting from Part 4.2, I completely lost track of the concepts of uncertainty, various expressions of pi, regularization, and P_error. This makes me feel like I understand but I don't. Specifically, the connection between the suppression of the maximum logit and the resulting impact on uncertainty measures like MSP is not clearly articulated. The authors should provide a more detailed explanation of how the changes in the logit space translate to changes in the probability space and consequently affect the uncertainty scores.
4. Line 371: Again, due to the confusion on the concepts, 'v_max is more strongly suppressed for lower P_error' is not intuitive to me. The authors need to clarify why the suppression of the maximum logit is dependent on the probability of error, and how this relationship is derived from their theoretical framework. A more detailed explanation of the underlying mechanism is needed to make this point more accessible.
5. The caption for Figure 4 is confusing. Which one is the left, and which one is the right?
6. The caption for Figure 5 is confusing. What is the purpose of Figure 3? What does it illustrate? It is not clear.

### Questions
All my confusions have been listed under the weaknesses section. I welcome the authors to provide clarifications on points 1, 3, and 4.

### Soundness
3

### Presentation
2

### Contribution
3
