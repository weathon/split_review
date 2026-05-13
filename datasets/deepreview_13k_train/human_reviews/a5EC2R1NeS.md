# Confidence Difference Reflects Various Supervised Signals in Confidence-Difference Classification

- Decision: Reject
- Scores: 5, 5, 6, 8

## Abstract
Training a precise binary classifier with limited supervision in weakly supervised learning scenarios holds considerable research significance in practical settings. Leveraging pairwise unlabeled data with confidence differences has been demonstrated to outperform learning from pointwise unlabeled data. We theoretically analyze the various supervisory signals reflected by confidence differences in confidence difference (ConfDiff) classification and identify challenges arising from noisy signals when confidence differences are small. To address this, we partition the dataset into two subsets with distinct supervisory signals and propose a consistency regularization-based risk estimator to encourage similar outputs for similar instances, mitigating the impact of noisy supervision. We further derive and analyze its estimation error bounds theoretically. Extensive experiments on benchmark and UCI datasets demonstrate the effectiveness of our method. Additionally, to effectively capture the influence of real-world noise on the confidence difference, we artificially perturb the confidence difference distribution and demonstrate the robustness of our method under noisy conditions through comprehensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies a special type of weakly-supervised learning known as confidence difference learning. This method leverages confidence differences between unlabeled data pairs to improve classifier training under noisy real-world conditions. By incorporating a noise generation technique and a risk estimation framework that includes consistency risk and regularization, ConfDiff classification demonstrates enhanced robustness and outperforms traditional methods in experiments on benchmark and UCI datasets. Theoretical analyses providing error bounds for the risk estimations further support the method's effectiveness.

### Strengths
1. The main theoretical contribution of this paper improved over [1] seems to be the incorporation of consistency regularization and its effect in error bound; based on my understanding, $C_{g}$  bounded the differences between $x$ and $x'$, so that under authors' setup, if the prediction of these data points is close enough, then the perceived generalization error should decrease, which is sensible.

2. After a very coarse examination, the proof of this paper seems to be correct.

3. Encourage instances with smaller confidence differences to produce similar outputs that seem intuitive and sensible, both theoretically and empirically.

[1] Binary classification with confidence difference, NeurIPS 2023.

### Weaknesses
1. It appears that the ConfDiff learning requires the classifier to be perfectly calibrated, which is usually infeasible in reality. I think it would be useful to incoperate the results on how different level of calibration error will influence the performance of ConfDiff learning. Specifically, the method relies on accurate posterior probability estimates to compute confidence differences, and any deviation in these estimates due to poor calibration could significantly impact the learning process. The paper should include an analysis of how miscalibrated probabilities affect the quality of the supervision signal and the overall performance of the method.

2. The implications of the theoritical results in this paper are not discussed, the authors simply present the bound as is, but fail to elaborate any new insights or messages we can draw from the error bounds - what are the dominant terms in the error bound? How is this related to the noisy supervision signal? What properties of your proposed method is related to this error bound? How this bound improves upon the existing bounds? Given the current form of the paper, the audience can only have a vague guess of the above questions. The theoretical analysis needs to be more thoroughly connected to the practical aspects of the method, explaining how the derived bounds inform the design choices and expected behavior of the algorithm under various conditions.

3. This paper appears to be unclear in many details, why negative risk can lead to overfitting? The explanation of why negative risk leads to overfitting is not sufficiently detailed. It would be beneficial to elaborate on the mechanism through which negative risk encourages the model to learn noise in the training data, rather than focusing on the true underlying patterns. A more concrete example or a step-by-step explanation of this phenomenon would be helpful.

4. Suppse we are given a supervision signal $\tilde{c}(x,x') < 0.5$ (smaller confidence difference), then by fitting this objective, wouldn't the $R_{CD}$ inherently encourages $x,x'$ to be similar? Hence making $R_{CRCR}$ trivial? The concern is that if the confidence difference is small, the $R_{CD}$ term might push the representations of $x$ and $x'$ to be similar, which would make the consistency regularization term, $R_{CRCR}$, redundant. The paper needs to clarify how the method avoids this potential issue, and why the consistency regularization is still necessary when the confidence difference is small.

Minor issues:

1. From line 210-212, shouldn't the $c(x,x')$ be $\tilde{c}(x,x')$ instead?

### Questions
How the noise is being defined and formulated in this paper is still a bit puzzling to me, I recommend the authors to improve the writing of the Section 3.1, and maybe considering adding some concrete examples ton make their points.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers weakly-supervised binary classification from noisy confidence difference annotations. It builds on the existing work of risk-estimation based approach and further analyze and modify the terms in the risk estimator. For the proposed risk estimator, error bound is derived and thorough experiments are conducted.

### Strengths
- The paper is overall well written. Phrases are generally easy to understand.
- The mathmetical prensentation is sound, and definitions are clear and easy to follow.
- Experiments are thoroughly conducted, with implementation codes attached.
- The background of the problem setting and related methods are well summarized. Authors show a good level of understanding of the problem.
- The problem of tackling noise in the confdiff weakly supervised settings is of high practical importance, and also a theoretically interesting problem.

### Weaknesses
 - The paper lacks a clear story of presentation of the motivation. There seems exist multiple concepts of "noise". At least there are two different noises: the noise of generated conf diff resulting inaccurate $c$, or the noise of model learned by $|c|<0.5$. They are not clearly described, thus resulting weak motivation for the proposed method.
  - Phrases such as "distribution influenced by real-world noise", "perturb the confidence difference distribution to better fit real-world scenarios", "we observe that the confidence difference values utilized for training in ConfDiff classification are frequently noisy, rather than exact difference between the posterior probabilities of two samples." clearly indicate the motivation is about the noise of the generated conf diffs.
  - At the same time, phrases such as "result in one of the data points being estimated in the opposite direction, introducing noise.
This leads to inaccurate predictive directions even in the absence of noise." seems to talk about another level of noise, noise of the model learned by $|c|<0.5$.
- The important part of consistency regularization term takes a too small part of the whole paper. The motivation and intuition of the modification and how the modification behaves if not clearly demonstrated.
- The other part of contribution, consistency risk of $D^S$ is not well motivated, thus seems irrelevant to the story.
- For Eq. 5, "general form of many commonly used losses" is suddenly introduced without further explanation, such as what specific loss functions belong to this form, or does not belong to this form.
- Too much space is spent on background methods, such as Section 2.

### Questions
- For Figure 1
  - What does proportion (x-axis) being more than 1.0 mean?
  - How to control the proportion with a fixed $\pi$? I assume the generation process is that two data points are first i.i.d. generated and then the conf diff is consequently calculated. Does changing the proportion mean that there is a selection mechanism exists during the data generation process, such resulting a skewed data distribution?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study a challenging weakly supervised task called confidence difference (ConfDiff) classification, where only the posterior probability differences for pairwise data points are accessible during training. To handle the influence of noise in ConfDiff, the authors introduce a method called CRCR, which partitions the training data into two subsets with different ConfDiff levels and applies a different strategy to each subset. Additionally, theoretical analyses of the proposed methods and experimental results on multiple benchmark datasets are provided.

### Strengths
1. This article treats ConfDiff as a soft label problem. It partitions the dataset using a threshold and applies different strategies to handle data with high and low ConfDiff levels. The effectiveness of this method in combating noise is verified through experiments.
2. The authors strengthen the analysis by conducting ablation studies to clarify the contributions of dataset partitioning and the consistency regularization term. These experiments significantly enhance the clarity and depth of the results, making it easier to understand the individual impact of each component.
3. Theoretical analyses are provided to demonstrate the theoretical guarantees of the proposed methods.

### Weaknesses
1.	There is a lack of descriptions of Theorem 1.
2.	It is recommended that the authors provide a detailed explanation of 'consistency' within the text.
3.	The manuscript requires careful revision to address various issues that currently detract from its clarity and academic rigor. For example, please consider revising the following sections of the manuscript to enhance clarity and accuracy:

* line 014: Consider revising the phrase ‘’significant research significance‘’ to avoid redundancy and enhance clarity. Perhaps ‘’considerable practical significance‘’ would be more appropriate.
* line 155 Eq. (3): The notation [L(x, x), L(x, x)] may need to be corrected to [L(x, x) + L(x, x)].
* Line 174: It might be appropriate to ‘substitute the form of the loss function from Equation 5 into Equation 3.’.
* Line 210: Please clarify the meaning of $\theta(D^S)$ and $\theta(D^C)$.
* Line 241: the term $R(\hat{g}{CRCR})$ should be corrected to $\hat{g}_{CRCR}$.
* Table 3, line 387: It appears there is a labeling error, as CRCR_RelLU (0.930) is noted to significantly outperform ConfDiffABS (0.940), which seems counterintuitive. Please verify and correct.

### Questions
see weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper deals with confidence-difference classification, a weakly supervised binary classification problem. In order to mitigate the noise contained in the confidence differences, a novel risk estimator using consistency regularization is employed to improve performance. Extensive experiments on benchmark datasets validate the effectiveness of the proposed method.

### Strengths
- The problem studied, i.e., confidence-difference classification with noise, is an interesting and promising problem.
- The motivation that different confidence difference values convey different information is valid and interesting, which has not been explored in the literature.
- The proposed consistency regularization term is valid, which can improve the performance when the confidence difference is small for some training data.
- The experiments are comprehensive and validation studies are also conducted to validate the effectiveness of the proposed method.
- The paper is clearly written and easy to understand.

### Weaknesses
 - One of my concerns is whether the noise is more pronounced when the confidence difference is small. When the confidence difference is large, noise can also be introduced. Although it does not affect the algorithm, which I think can work well even if no noise is introduced in the experiments. I think this point needs clarification and the paper can be polished as well. I think a more reasonable story is to use some terms like "clear" and "ambiguous" to replace data with and without noise. Some data pairs are more clear (larger confidence difference absolute values) and their labels can be (+1,-1) or (-1,+1) with a high probability. Some data are ambiguous (small confidence differences) and we cannot tell if they are both positive or negative. This story may be more reasonable from my point of view. To handle different types of data, the consistency regularization term is introduced to improve learning from ambiguous data pairs.

- The descriptions in Section 4.2 are not so clear. I cannot understand how the data is generated, such as the meaning of $c_{non-outlier}$. 

- There are some unclear notations and expressions that should be examined. For example, $\ell$ is missing in line 235. In line 241 it should be $\hat{g}$ instead of $R(\hat{g})$. In line 42-43, it seems to apply to general supervised learning instead of weak supervised learning? In line 89 it should read "difference". Also, more discussion should be added after Theorem 1. The space for the post text can be reduced. Also, the "_" notation for the methods can be replaced with "-".

### Questions
- Why do larger confidence differences contain less noise?

### Soundness
4

### Presentation
3

### Contribution
4
