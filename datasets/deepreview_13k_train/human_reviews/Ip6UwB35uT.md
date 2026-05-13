# Conditional Testing based on Localized Conformal $p$-values

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
In this paper, we address conditional testing problems through the conformal inference framework. We define the localized conformal $p$-values by inverting prediction intervals and prove their theoretical properties. These defined $p$-values are then applied to several conditional testing problems to illustrate their practicality. Firstly, we propose a conditional outlier detection procedure to test for outliers in the conditional distribution with finite-sample false discovery rate (FDR) control. We also introduce a novel conditional label screening problem with the goal of screening multivariate response variables and propose a screening procedure to control the family-wise error rate (FWER). Finally, we consider the two-sample conditional distribution test and define a weighted U-statistic through the aggregation of localized $p$-values. Numerical simulations and real-data examples validate the superior performance of our proposed strategies.\vspace{3ex}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces localized conformal $p$-values and applies them to several conditional testing problems, including conditional outlier detection, conditional label screening, and two-sample conditional distribution testing.

### Strengths
This paper presents the concept of localized conformal $p$-values and demonstrates their application to some interesting testing problems. The authors conduct appropriate experiments to illustrate the performance of their method.

### Weaknesses
Please refer to the questions below.

### questions:
 1. Could the authors provide a rigorous proof of the density ratio of $X_{2j}$ and $X_{1i}$ conditional on $\tilde{X}_{2j}$.

2. Where is $d$ defined?

3. In different applications of conditional testing, what are the score functions $V$?

4. Please clarify the statement "This indicates that using the LCP for data selection can lead to a more balanced selection result since the PSER inflation for different sub-groups is bounded", and the statement related to fairness.

5. Avoid using abbreviations before introducing them, such as PRDS.

6. In conditional outlier detection, what are the theoretical and empirical performances if $P_{1,X} \neq P_{2,X}$?

7. From my understanding, the theoretical results do not account for the estimation errors. Moreover, kernel functions can lead to the curse of dimensionality, which hinders application in high-dimensional settings.

8. How do the tuning parameters in kernel functions affect the performance, and how should these parameters be chosen in practice?

9. Why does the method in two-sample conditional distribution testing not require randomization? Does the proposed method in this context require the marginal density ratio? Moreover, why does the type I error increase with sample size in Figure 7?

### Questions
1. Could the authors provide a rigorous proof of the density ratio of $X_{2j}$ and $X_{1i}$ conditional on $\tilde{X}_{2j}$.

2. Where is $d$ defined? 

3. In different applications of conditional testing, what are the score functions $V$?

4. Please clarify the statement "This indicates that using the LCP for data selection can lead to a more balanced selection result since the PSER inflation for different sub-groups is bounded", and the statement related to fairness.

5. Avoid using abbreviations before introducing them, such as PRDS.

6. In conditional outlier detection, what are the theoretical and empirical performances if $P_{1,X} \neq P_{2,X}$?

7. From my understanding, the theoretical results do not account for the estimation errors. Moreover, kernel functions can lead to the curse of dimensionality, which hinders application in high-dimensional settings. 

8. How do the tuning parameters in kernel functions affect the performance, and how should these parameters be chosen in practice?

9. Why does the method in two-sample conditional distribution testing not require randomization? Does the proposed method in this context require the marginal density ratio? Moreover, why does the type I error increase with sample size in Figure 7?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors introduce a novel (conformal) p-value by converting an existing conformal prediction method that is locally valid, asymptotically conditionally valid, and computationally advantageous. They further discuss the applicability of this approach in various multiple conditional testing problems. From an application perspective, their contributions are four folds: balanced data selection, conditional outlier detection, conditional label screening, and a two-sample conditional distribution test. Each application is rigorously justified through theoretical analysis, and the utility of the proposed methods is empirically demonstrated via extensive numerical experiments.

### Strengths
The most notable strength of this work lies in the variety of applications presented. The proposed applications of LCP are all promising, largely due to the LCP’s ability to effectively address conditional testing. In particular, the authors contextualize each application; for instance, in the case of the conditional label screening problem, they suggest that this application could be used to ensure the factuality of large language models, thereby justifying its utility.

Furthermore, the authors thoroughly discuss the theoretical justification of the proposed applications. They rigorously prove how each problem controls specific quantities (e.g., FSER, FDR, and FWER) by synthesizing a considerable amount of literature to support their claims. This strength, the ability to creatively adapt existing methodologies and introduce multiple new applications, demonstrating an original contribution to the field.​

### Weaknesses
While they have successfully introduced locally conformal p-values and thoroughly demonstrated their various applications and theoretical properties, their work seems limited in terms of novelty. Specifically, the locally conformal p-values appear to be derived from directly converting the prediction intervals proposed by Hore & Barber (2023), and their application seems to involve integrating these p-values into several already established methods.

Meanwhile, one of the main contributions of their work lies in achieving the asymptotically conditional super-uniform property of the new conformal p-values. Specifically, Theorem 4 and Theorem 7 provide theoretical justification for this, though the authors merely mention that a specific choice of $g(x)$ renders the covariate shift problem equivalent to conditional validity, which is not clear. While this approach poses no issue in terms of soundness, as previously discussed by Hore & Barber (2023), it may lack readability in this regard.

### Questions
1. In the application of conditional outlier detection, the goal was to control the FDR using the BH procedure, whereas in the conditional label screening problem, LCP guarantees FWER control. Is there any reason behind controlling different quantities in each case? What motivated the decision to adhere to FWER control instead of FDR control in conditional label screening despite this conservativeness?
  
  2. In Section 3.1, within the balanced data selection problem, it is assumed that the response variable is not observed. In this case, how is $V_{2j}$ specifically obtained? My understanding is that both $X_{2j}$ and $Y_{2j}$ are required for this, but $Y_{2j}$  is not observed. In this case, is an arbitrary value of $Y_{2j}$ (i.e., any y which is not in $\mathcal{A}$) satistfing $\mathbb{H}_{0j}$ used?
  
  3. Could you provide more detailed explanation or intuition for how the specific choice of g(x) makes the covariate shift problem equivalent to conditional validity?

  4. In Section 3.3, the context of large language models’ factuality is introduced to frame the conditional label screening problem. However, the numerical study presents results only on more structured synthetic and real datasets. I was wondering if any numerical study reflecting the natural language processing context described in the paper has been attempted. If so, what were the outcomes of those experiments? If not, what additional research would be necessary to conduct such studies?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces localized conformal p-values for conditional testing problems.
Specifically, the authors inverting the prediction intervals which are constructed by
 existing works to adapt to the conditional distribution of the response. They establish theoretical results on the fundamental properties of their defined p-values, as well as applications of these p-values to conditional testing. The empirical results demonstrate the effectiveness of their proposed methods.

### Strengths
The paper presents a clear problem statement, solid theoretical results, and the experimental results effectively reflect the efficiency of their proposed method.

### Weaknesses
The structure of paper could be better. The authors could give concise and appropriate names to the important theorems to summarize their meanings, and mark the others as lemmas. There are many theorems in the main text of the paper, so presenting the theorems this way would make them more intuitive and help readers better understand the meaning of the theorems.

### Questions
1.What circumstances the "average FDP above nominal level" shown in Figure 1 would become negative?

2.Based on the experimental results in the paper, it is observed that in many cases, LCP-od exhibits greater fluctuations compared to CP. How can this phenomenon be explained?

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
This work investigates the possible application of localized conformal p-values, which can be naturally constructed from recent localized conformal prediction methods.

### Strengths
This work extends the localized conformal prediction methods to a broader range of inferential targets.

### Weaknesses
I believe the writing and presentation should be improved, and more effort needs to be made to demonstrate the usefulness of the results.

I believe the writing and presentation should be improved, and more effort needs to be made to demonstrate the usefulness of the results.

I believe the writing and presentation should be improved, and more effort needs to be made to demonstrate the usefulness of the results.

1. Could the authors provide clarifications on the goal of Theorem 3? It feels somewhat distracting from the main focus of this work, as it essentially presents an 'asymptotic property under additional assumptions,' while the main point of the conformal prediction framework is the finite-sample theory without distributional assumptions.

2. Regarding Section 3.2, 'Conditional Outlier Detection,' I'm not sure if the hypothesis (3.1) is what is actually being tested. Specifically, isn't the p-value super-uniform under a weaker condition than $H_{0,j}$ in (3.2), since it is marginally valid?

My understanding is that the localized conformal prediction method from Hore and Barber basically achieves the marginal coverage guarantee, while the conditional miscoverage rates are "likely to be small" if we frame everything in a distribution-free sense.

Thus, I feel that the outlier detection counterpart of the localized conformal prediction framework controls the FDR for testing marginal outliers, but conditional outliers are more likely to be detected—rather than directly detecting conditional outliers with a distribution-free guarantee. Am I missing something?

3. (continued from point 2) In Theorem 5, is the goal of the condition $P_{1,X}=P_{2,X}$ to claim that any detected distribution shift is a label shift rather than a covariate shift, i.e., that any outlier is a conditional outlier? My confusion is that under the condition $P_{1,X}=P_{2,X}$, the null hypothesis in (3.1) is essentially equivalent to stating that the marginal distribution $P_{(X,Y)}$ is the same for the test point and the calibration set, since it is the combination of "$P_X$ is the same" and "$P_{Y|X}$ is the same".

So, to me, Theorem 5 sounds like "Algorithm 1 controls FDR for testing marginal outliers. But if we additionally assume that $P_X$ is the same, then an outlier means $P_{Y|X}$ is different, implying that it is a conditional outlier", which is not very interesting compared to directly detecting the conditional outliers.

Therefore, as mentioned in point 2, for a more useful result, shouldn't the statement be something like: "The procedure detects marginal outliers, but conditional outliers are likely to be better detected if we use the localized conformal p-values"?

4. Could the authors provide explanations for the terms in Theorem 4 and 7, since it's difficult to see how small they are?

5. minor comment: "independency" -> "independence" in page 28

### Questions
1. Could the authors provide clarifications on the goal of Theorem 3? It feels somewhat distracting from the main focus of this work, as it essentially presents an 'asymptotic property under additional assumptions,' while the main point of the conformal prediction framework is the finite-sample theory without distributional assumptions.

2. Regarding Section 3.2, 'Conditional Outlier Detection,' I'm not sure if the hypothesis (3.1) is what is actually being tested. Specifically, isn't the p-value super-uniform under a weaker condition than $H_{0,j}$ in (3.2), since it is marginally valid? 

My understanding is that the localized conformal prediction method from Hore and Barber basically achieves the marginal coverage guarantee, while the conditional miscoverage rates are "likely to be small" if we frame everything in a distribution-free sense.

Thus, I feel that the outlier detection counterpart of the localized conformal prediction framework controls the FDR for testing marginal outliers, but conditional outliers are more likely to be detected—rather than directly detecting conditional outliers with a distribution-free guarantee. Am I missing something?

3. (continued from point 2) In Theorem 5, is the goal of the condition $P_{1,X}=P_{2,X}$ to claim that any detected distribution shift is a label shift rather than a covariate shift, i.e., that any outlier is a conditional outlier? My confusion is that under the condition $P_{1,X}=P_{2,X}$, the null hypothesis in (3.1) is essentially equivalent to stating that the marginal distribution $P_{(X,Y)}$ is the same for the test point and the calibration set, since it is the combination of "$P_X$ is the same" and "$P_{Y|X}$ is the same". 

So, to me, Theorem 5 sounds like "Algorithm 1 controls FDR for testing marginal outliers. But if we additionally assume that $P_X$ is the same, then an outlier means $P_{Y|X}$ is different, implying that it is a conditional outlier", which is not very interesting compared to directly detecting the conditional outliers.

Therefore, as mentioned in point 2, for a more useful result, shouldn't the statement be something like: "The procedure detects marginal outliers, but conditional outliers are likely to be better detected if we use the localized conformal p-values"?

4. Could the authors provide explanations for the terms in Theorem 4 and 7, since it's difficult to see how small they are?

5. minor comment: "independency" -> "independence" in page 28

### Soundness
3

### Presentation
2

### Contribution
3
