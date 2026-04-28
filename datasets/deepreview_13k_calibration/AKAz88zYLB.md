# Conformal Prediction for Dose-Response Models with Continuous Treatments

- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 5, 3, 8, 5

## Abstract
Understanding the dose-response relation between a continuous treatment and the outcome for an individual can greatly drive decision-making, particularly in areas like personalized drug dosing and personalized healthcare interventions. Point estimates are often insufficient in these high-risk environments, highlighting the need for uncertainty quantification to support informed decisions. Conformal prediction, a distribution-free and model-agnostic method for uncertainty quantification, has seen limited application in continuous treatments or dose-response models. To address this gap, we propose a novel methodology that frames the causal dose-response problem as a covariate shift, leveraging weighted conformal prediction. By incorporating propensity estimation, conformal predictive systems, and likelihood ratios, we present a practical solution for generating prediction intervals for dose-response models. Additionally, our method approximates local coverage for every treatment value by applying kernel functions as weights in weighted conformal prediction. Finally, we use a new synthetic benchmark dataset to demonstrate the significance of covariate shift assumptions in achieving robust prediction intervals for dose-response models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a conformal prediction-based method for estimating uncertainty in the dose-response function, which defines the effect of continuous treatment on a continuous outcome, in the presence of confounders. Their method uses weighted conformal prediction, with weights based on generalized propensity scores. The presentation is exemplary and instructive throughout, including the motivation for and description of the proposed method. Experiments cover two established simulation settings and one new simulation setting. Results show that the resulting prediction intervals tend to be conservative, in the sense that empirical coverage of the true dose-response function is higher than intended.

### Strengths
- Reliable dose-response estimation from observational data is important in medicine and other settings.
- The writing style, mathematical notation and presentation, and explanations of concepts are outstanding throughout.
- The methodology is novel to my knowledge and builds on recent progress in conformal prediction and causal methods for continuous treatments.
- Experimental settings and baseline methods are appropriate.
- The proposed method consistently achieves better empirical coverage than comparator methods.

### Weaknesses
 - The evaluation is somewhat limited and focused almost entirely on empirical coverage.
- Error of the estimated CADRF is not presented except indirectly in Figure 2 for only one of the settings (Setup 3, Scenario 1).
- Empirical coverage is higher than desired in most cases and often very close to 1, and the prediction intervals are only shown for a single example.
- All this taken together makes me suspect that the method often yields excessively wide prediction intervals that may not be useful.
- The authors discuss the fact that the method yields conservative prediction intervals and provide brief explanations, but I think more discussion should be devoted to this given its central importance.
- I also think it is critical to provide figures akin to Figure 2 for more of the settings and compare error of the estimated CADRF between methods.

### Questions
My questions are implied by the weaknesses listed above. I'd like to see:
- more figures akin to Figure 2
- a comparison of error of the estimated CADRF between methods
- more commentary on why the method yields such conservative prediction intervals

Additionally:
- What are the implications of the conservative prediction intervals on usefulness of the method in practical settings?
- How might the method be improved subsequently to achieve ideal empirical coverage?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a new methodology for uncertainty quantification in dose-response models with continuous treatments using conformal prediction. ​ The approach leverages weighted conformal prediction, incorporating propensity estimation and kernel functions to address covariate shifts, ensuring coverage across all treatment values. ​ Building on the potential outcomes framework and generalized propensity scores, the method addresses some limitations in existing UQ techniques. ​ Experiments with synthetic data demonstrate its effectiveness, showing reliable prediction intervals with low treatment overlap. The practical implementation of this method can improve personalized dosing and interventions in various fields, enhancing decision-making by providing robust uncertainty quantification. ​

### Strengths
The paper introduces a novel approach using conformal prediction to uncertainty quantification in dose-response models. The use of weighted conformal prediction ensures coverage across all treatment values, even under covariate shifts. The methodology has practical implications for personalized healthcare, drug dosing, and other fields requiring individualized treatment decisions. ​

### Weaknesses
1. The accuracy of the method relies heavily on the quality of the propensity score estimation, which can be challenging in real-world scenarios. In Section 5.2, the paper discussed using both oracle and estimated propensity distributions. How robust are their results to potential errors or biases in propensity score estimation? A sensitivity analysis could provide insights into how variations in the quality of propensity score estimation impact the overall accuracy of their method. Specifically, it would be beneficial to explore how different propensity score estimation techniques (e.g., logistic regression, gradient boosting) affect the coverage and width of the prediction intervals, especially when the true propensity model is misspecified. Furthermore, the paper should investigate the impact of common issues such as positivity violations or near-positivity violations on the performance of the proposed method, as these are frequently encountered in real-world observational data. 

2. The experiments are conducted on synthetic data, and the method's performance in real-world applications remains to be fully validated. ​

### Questions
How does the method perform with real-world data? It will make the method become more impactful and convincing with real data application analysis. I understand that applying real data for treatment effect estimation can be challenging, especially for continuous dose scenario. However, I encourage the authors to suggest specific real-world applications related to optimal dose recommendation, as this is an area where their method could provide significant insights. Probably some real data application deal with optimal dose level recommendation and use offline reward/value/outcome function to evaluate the performance of the estimated decision rule?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In the manuscript, the authors propose a conformal prediction based method to obtain the interval estimation of the potential outcomes under continuous treatment. 
To achieve this, the authors use the weighted conformal prediction method. 
They also aim to provide a local guarantee for the proposed method via using the kernel weighting function.

### Strengths
1. The authors address a crucial issue in causal inference: estimating potential outcomes under continuous treatment. They also aim to provide a local guarantee for their proposed method, which is highly important in practical applications.

2. They have good literature review and make readers understand the background of the problem easily.

3. The method is relatively simple and easy to implement.

### Weaknesses
1. While the authors provide a method, they can not provide a theoretical guarantee for the proposed method. This is a significant drawback of the paper.

2. In my opinion, they do not illustrate the method well. The paper would benefit from more detailed illustrations for example an Algorithm or a flowchart.

3. The method relies on in my opinion a strong assumptions, that is interventional distribution is Uniform and there is not distributional shift between the training and test data in terms of $\mathbf{X}$.

4. The numerical experiments are not comprehensive enough and no real data application is provided.

### Questions
1. In the method, they mentioned they use Conformal Prediction System (CPS), however, I do not see it in the Method section. Only in the numerical experiments, they mention it.However, it is not clear how they use it.

2. The numerical experiments are confusing to me. They consider eight different methods for comparison, but it is not clear to me which methods are their proposed methods. What is the difference between these methods, such as WCP local and WCP global?


3. I think covariate shift is a very common issue in causal inference, why the authors assume there is no distributional shift between the training and test data in terms of $\mathbf{X}$?

4. Is the uniform distribution assumption for the interventional distribution realistic?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel methodology for conformal prediction (CP) in dose-response models with continuous treatments, aiming to provide uncertainty quantification (UQ) for individualized decision-making. The approach leverages propensity score estimation and weighted conformal predictive systems to generate prediction intervals across a continuous range of treatments, which is essential for personalized healthcare and other decision-critical fields. By incorporating covariate shift assumptions and using kernel-based weighting, the authors propose a robust solution for achieving local coverage of dose-response predictions. The paper is validated on synthetic datasets, demonstrating the effectiveness of the proposed method.

### Strengths
1. he paper presents an original application of conformal prediction to continuous treatment dose-response models, addressing an important gap in causal inference research. The integration of propensity score weighting and kernel-based adjustments to conformal prediction is a creative approach to ensure coverage under covariate shifts.
2. The paper is mostly clear, with well-structured sections that logically progress through the problem, related work, methodology, and experiments. The use of figures and visualizations to depict coverage is helpful for interpreting the results.
3. The problem of providing reliable prediction intervals for dose-response models has practical implications in many fields, such as personalized medicine, and this work represents a step forward in providing UQ in such contexts.

### Weaknesses
1. While the application is new, much of the methodology builds on existing CP and propensity score techniques without introducing fundamentally new theoretical contributions. The added value lies in the application context, but more could be done to differentiate this work from prior studies. Specifically, the paper does not delve deeply into the theoretical properties of the proposed weighted conformal prediction system under various covariate shift scenarios. The conditions under which the local coverage guarantees hold, and how these guarantees degrade with increasing covariate shift, are not rigorously explored, limiting the theoretical novelty.
2. The reliance on synthetic datasets raises concerns about the method's practical utility. A more thorough evaluation on real-world data would strengthen the paper’s claim of addressing practical challenges in dose-response modeling. The synthetic data, while useful for initial validation, may not capture the complexities of real-world data, such as non-linear relationships, unmeasured confounders, or complex interactions between covariates. This limits the generalizability of the findings.
3. Although the authors mention the efficiency improvements from weighted conformal prediction, the scalability of the method, particularly in real-time applications, remains unclear. Detailed analysis of the computational overhead, especially with large-scale data, would be beneficial. The paper lacks a detailed breakdown of the computational complexity of each step, such as propensity score estimation, kernel weighting, and conformal prediction interval construction. This makes it difficult to assess the method's feasibility for large datasets or real-time decision-making.

### Questions
1. How does the method perform when applied to real-world dose-response data, particularly in scenarios where confounding factors are not as easily modeled as in synthetic datasets?
2. Can the proposed method scale to larger datasets with higher-dimensional covariates and continuous treatments without a significant increase in computational time?
3. How robust is the propensity estimation in cases where the true propensity distribution is unknown or difficult to estimate? What are the limitations when using kernel density estimation (KDE) in practice?
4. Beyond healthcare, what other domains have been considered for the application of this method, and how would the assumptions about covariate shift differ in these contexts?

### Soundness
2

### Presentation
2

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
This paper addresses continuous treatment’s CATE via weighted conformal prediction.

### Strengths
This paper targets a significant and challenging task of considering uncertainty in CATE estimation when treatment is continuous.

### Weaknesses
-	Methodological contribution compared to prior work is incremental. The proposed idea of estimating counterfactual outcome interval using weighted conformal prediction has already been published by Lei et al. Lei et al. have proven that a generalized propensity score can be used for the weight in conformal prediction. The main difference between this paper and the similar work by Lei et al. is estimation targets (continuous CATE in this paper vs. discrete CATE in prior work).
-	Compared to another prior work by Schroder et al., this paper’s methodological contribution is also marginal. The discussion in Supplement C is not fully convincing in distinguishing this paper’s contribution from the prior work.  
-	Novelty is limited. This paper applies an existing method to an existing task. No new approach or new generalizable insight was provided.  
-	Validation is limited. Neither a formal theoretical guarantee nor empirical validation with real data were provided. I understand the lack of ground truth in the CATE world, but I would appreciate it if a theoretical guarantee could supplement the synthetic data validation. No comparison to baseline models.
-	Therefore, this paper does not have a broader impact on the following works in this field.

### Questions
Clarifying clear differences to prior similar works,
Convincing validation

### Soundness
3

### Presentation
2

### Contribution
1
