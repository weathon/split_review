# MissScore: High-Order Score Estimation in the Presence of Missing Data

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
The first order derivative (score) of data density, typically estimated via denoising score matching, has emerged as an effective tool for modeling data distribution and generating synthetic data. Extending this concept to higher-order scores could uncover more detailed local information of the data distribution, enabling new applications. However, learning these high-order scores usually requires complete data, which is often unavailable in real-world scenarios such as healthcare and finance due to privacy and cost constraints. In this work, we introduce MissScore, a novel score-based framework for learning high-order scores from observations with missing data. We derive objective functions for estimating high-order scores under different missing data mechanisms and propose a new algorithm to handle missing data effectively. Our empirical results demonstrate that MissScore efficiently and accurately approximates high-order scores with missing data, while enhancing sampling speed and data quality, as validated through several downstream tasks, including data generation and causal discovery.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method called MissScore that estimates high-order scores with missing data, under both MCAR and MAR settings for second-order scores. The paper proves that the under appropriate assumptions, MissScore indeed estimates the score of the observed data. The paper compares MissScore with baselines on two applications of high-order score estimation.

### Strengths
The method and theory the paper introduces are novel to my knowledge, and address an important problem. The method outperforms alternatives in the experiments of the paper. The experiments are documented thoroughly.

### Weaknesses
The main weakness of the paper is the lack of realistic experiments. Only one real dataset is used, on only the sampling experiment. In the MAR experiments of the paper, the likelihood of each datapoint being observed is estimated with the same model that the missingness is assigned with. This is unlikely to be true in practice, so these should use different models in at least some experiments. Of course, even better would be using a real dataset with missing values, so there would be no need to artificially introduce missingness.

The paper claims that their results show that some baselines are introducing bias, since those baselines achieve worse results than MissScore. However, I don't think this is strong evidence of bias, since there could be other reasons for worse performance.

Minor points:
- Several spelling errors throughout the paper, for example fidelity, Langevin and Ozaki in Table 2.

### Questions
- The statements of Theorems 3-7 exclude the case where the probability of a missing value is 0, so all values are observed. What happens to the theory in this case? Do the theorems fail?
- The paper does not contain a theorem for $k$th order scores with $k > 2$ under MAR. Were you not able to prove this type of theorem? If so, what are the difficulties that make the general $k$ case harder in the MAR setting than the MCAR setting?
- What exactly is the fidelity metric measuring?
- How do you aggregate the utility metric values from the different predictive models?
- Is the number of iterations in Figure 2 the number of iterations for training the score models, or the number of iterations of Langevin dynamics?
- Why do the utility metrics for MissScore in Table 5 only decrease significantly with increasing missingness under MCAR, but not MAR or MNAR?

### Soundness
2

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
3

### Summary
This paper presents a score estimation framework, namely MissScore, which aims to learn first and higher-order score functions in the presence of missing data. The key contribution of this paper is to provide theoretical results supporting the use of a score-based loss function for estimating higher-order scores in the presence of missing data. Based on the theory, the paper introduces an estimation methodology and demonstrates its effectiveness through a series of simulations and real data analyses.

### Strengths
The main strength of this paper lies in its reinforcement of the existing method with a more robust theoretical foundation. A similar loss function for estimating higher order score function was introduced earlier in Ouyang et al. but with no theoretical guarantees. This paper shows that (a variant of) the loss function is theoretically justified.  Based on theoretically justified, the authors built a method that outperforms other methods in the presence of the missing data.

### Weaknesses
One of this paper's key weaknesses is its presentation of theory. I have one major question, which I have listed below (in the Questions section). Other than that, the presentation needs to be involved. All the theorems can be viewed as an extended version of the score-matching theorems (both for the first order and the higher order score) in the presence of missing data. Hence, it is helpful to provide some remarks for readers with less technical background to clarify how these new theorems relate to the previous ones. Specifically, it would be useful to explain how you modify the earlier theorems to account for missing values and why these changes are intuitively reasonable.



### Questions
1. All the theorems (Theorem 1 - Theorem 7) are stated in terms of the joint distribution of $(x, \tilde x, m)$. However, we only have the distribution of $(x_{\rm obs}, \tilde x_{\rm obs}, m)$. Are all the theorems valid under this observed distribution? 

2. What is the key difference between your method and the Missdiff of Ouyang et al.? 

3. It is not immediate from the experiment section how your method performs compared to MissDiff. Can you present some real data analysis (say using Census data) to compare your method with MissDiff?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a framework, MissScore, for estimating high-order scores in the presence of missing data, addressing a gap in data modeling with missing entries. The proposed method effectively integrates score-based models with missing data and provides theoretical guarantees under different missing mechanisms. Empirical results demonstrate that MissScore not only enhances the quality of data generation but also accelerates sampling, making it a competitive option for practical applications. However, I believe this manuscript, in its current form, requires further refinement.

### Strengths
MissScore integrates score-based models for data with missing entries, specifically focusing on higher-order scores. This provides a new perspective, enhancing data generation quality and sampling speed, which could benefit real-world applications. This framework also offers theoretical guarantees for different missing data mechanisms (e.g., MCAR and MAR), providing confidence in the approach's robustness and applicability under varying conditions. The empirical results validate the efficacy of MissScore, showing improvements over existing methods.

### Weaknesses
Limited Contribution over Existing Methods: this paper appears to primarily extend the work by Meng et al. (2021) [1] by adapting it to scenarios with missing data. Experiments are limited to second-order scores (i.e., the Hessian of log density). Extending the analysis or at least discussing applications for higher-order scores (e.g., third-order scores) would enhance the practical relevance of the framework and could inspire broader applications. Additionally, the experiments rely exclusively on logistic regression for likelihood estimation, raising concerns about potential model misspecification and its impact on the results. The details can be found in the questions.



### Questions
1. In my view, this paper primarily extends the method proposed by Meng et al. (2021) to learn $n$-th order gradients of the log density (of perturbed data) in the presence of missing data. As is well known, under MCAR mechanism, it is often sufficient to use only complete-case data without applying imputation, and the resulting estimator remains consistent with the oracle estimator. (see Little and \& Rubin (2019)). It is unclear why the authors have chosen to focus on the MCAR mechanism specifically. A direct comparison between their proposed method and the approach by Meng et al. (2021), based solely on complete case data, would provide more meaningful insight. I hold a conservative opinion about the contribution
made by this paper.

2. In the conditions outlined for Theorems 6-7 under the MAR mechanism, there is no mention of the conditional propensity score function. Typically, with the IPW method under MAR, where the missing mechanism depends on observed variables, it is essential to assume that the conditional probability of missingness for each element lies strictly between 0 and 1, rather than imposing this requirement unconditionally. For example, what happens in Theorem 6 when $\mathbb{P}[m=0|x=x]\rightarrow 0$.

3. The experiments in this paper are limited to second-order scores (specifically, the Hessian of the log density). Could the authors suggest any practical applications where higher-order scores, such as third-order scores, might be useful?

4. In Section 3, it is unclear how to determine the tunable coefficient $\omega$.  At a minimum, the authors should provide guidelines for practitioners on how to select this parameter and perform a sensitivity analysis to evaluate its impact.

5. For missing data, it is common to consider the potential misspecification of the missing mechanism. However, in the experiments, the authors rely exclusively on logistic regression to estimate the likelihood. It would be valuable for the authors to conduct experiments that assess the impact of possible model misspecification.

References

[1] Meng, C., Song, Y., Li, W., \& Ermon, S. (2021). Estimating high order gradients of the data distribution by denoising. Advances in Neural Information Processing Systems, 34, 25359-25369.

[2] Little, R. J., \& Rubin, D. B. (2019). Statistical analysis with missing data (Vol. 793). John Wiley \& Sons.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present MissScore, a score-based framework for learning high-order scores directly from incomplete data without imputation. They derive objective functions for different missing data mechanisms and demonstrate the framework's effectiveness in approximating second-order scores. They show MissScore improves sampling speed and data quality in generation tasks with missing data, and propose a new causal discovery method.

### Strengths
1. The proposed approach addresses limitations in other models (e.g., GANs or VAEs) that fail to estimate high-order scores naturally, especially under missing data conditions. By deriving objective functions suited for missing data mechanisms and focusing on second-order scores, MissScore can improve accuracy and efficiency in approximating high-order scores.

2. The paper proposes a causal discovery method that leverages MissScore’s second-order score model, effectively handling incomplete data. Unlike traditional imputation-based methods, this model integrates high-order score information directly, preserving data structure and reducing potential inaccuracies.

### Weaknesses
• The authors' claim that "imputation methods can compromise data quality, potentially leading to biased results and significantly degrading performance in downstream tasks" (also repeated in the Conclusion and Appendix A) would benefit from clarification. Specifically, the cited Ouyang (2023) paper focuses on an **"impute-then-generate"** pipeline where imputation may reduce generation quality by introducing biases. However, **"impute-then-predict"** pipelines often show improved predictive accuracy for downstream classification and regression tasks, as established in works such as:

    •  Poulos, J. and Valle, R. (2018). Missing data imputation for supervised learning. Applied Artificial Intelligence 32, 186–196
    • Jäger, Sebastian, Arndt Allhorn, and Felix Bießmann. "A benchmark for data imputation methods." Frontiers in Big Data 4 (2021)
    • Perez-Lebel, Alexandre, et al. "Benchmarking missing-values approaches for predictive models on health databases." GigaScience 11 (2022)
    • Shadbahr, T., Roberts, M., Stanczuk, J. et al. The impact of imputation quality on machine learning classifiers for datasets with missing values. Commun Med 3, 139 (2023).
    • Paterakis, George, et al. "Do we really need imputation in AutoML predictive modeling?." ACM Transactions on Knowledge Discovery from Data 18.6 (2024): 1-64.

• To address the statement on imputation methods not accounting for uncertainty in missing data, it would benefit the authors to include multiple imputation (MI) as an alternative that does incorporate uncertainty in imputed values. The work of Van Buuren & Groothuis-Oudshoorn (2011), which introduces a popular MI algorithm (MICE), is cited in Appendix A but not contextualized. MI can be applied with deep learning models like GAIN and MIDA to generate multiple plausible imputed datasets by rerunning these models with varying random initializations, thus capturing uncertainty. Wang et al. (2022) compare MI methods, including deep learning approaches like GAIN and MIDA, finding that MICE with classification trees often outperform deep learning methods in terms of imputation quality, especially in survey data.

    • Gondara, L., & Wang, K. (2018). "MIDA: Multiple imputation using denoising autoencoders." *Advances in Knowledge Discovery and Data Mining: PAKDD*.
    • Wang, Z., Akande, O., Poulos, J., & Li, F. (2022). "Are deep learning models superior for missing data imputation in surveys? Evidence from an empirical comparison." *Survey Methodology*, 48(2), 375-399.

• The differences between MissScore and MissDiff are not entirely clear. To clearly differentiate their contributions, the authors could explicitly state that, unlike MissDiff, which focuses on a first-order diffusion-based approach for data generation, MissScore introduces a framework for learning high-order scores from incomplete data without imputation, specifically targeting the Hessian to enhance downstream performance. The authors should emphasize that MissScore integrates a new causal discovery method, contrasting with MissDiff's focus on unbiased data synthesis.

• To strengthen the conclusion, the authors could acknowledge a few limitations of MissScore. While MissScore performs efficiently in high-dimensional settings, its accuracy in second-order score estimation (measured by SHD) slightly declines as dimensionality increases, particularly for complex causal structures (e.g., d = 50 in Figure 4). While the model maintains high fidelity and utility with moderate missing ratios (\alpha = 0.1 or \alpha = 0.3), its performance appears to degrade at higher missing ratios (alpha = 0.5 or greater), especially under MNAR conditions (Figure 1 and Table 1). Table 1 indicates that the effectiveness of MissScore decreases significantly without variance reduction at lower noise levels (\sigma = 0.01), particularly for second-order scores, suggesting challenges in low-noise or high-missingness scenarios.

### Questions
• Pg. 2 typo: “We derives”

• Pg. 22 - What are the various synthetic data generation methods used to generate synthetic records in the TSTR?

• Could the authors comment on the observed instability of MissDAG and MissDiffAN in higher dimensions (d = 50), as seen in Figure 12? 

• What might explain MissForest’s occasional competitiveness in certain conditions, in Figures 6-8?

### Soundness
3

### Presentation
3

### Contribution
3
