# Effective and Efficient Time-Varying Counterfactual Prediction with State-Space Models

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6

## Abstract
Time-varying counterfactual prediction (TCP) from observational data supports the answer of when and how to assign multiple sequential treatments, yielding importance in various applications. Despite the progress achieved by recent advances, e.g., LSTM or Transformer based causal approaches, their capability of capturing interactions in long sequences remains to be improved in both prediction performance and running efficiency. In parallel with the development of TCP, the success of the state-space models (SSMs) has achieved remarkable progress toward long-sequence modeling with saved running time. Consequently, studying how Mamba simultaneously benefits the effectiveness and efficiency of TCP  becomes a compelling research direction. In this paper, we propose to exploit advantages of the SSMs to tackle the TCP task, by introducing a counterfactual Mamba model with Covariate-based Decorrelation towards Selective Parameters (Mamba-CDSP). Motivated by the over-balancing problem in TCP of the direct covariate balancing methods, we propose to de-correlate between the current treatment and the representation of historical covariates, treatments, and outcomes, which can mitigate the confounding bias while preserve more covariate information. In addition, we show that the overall de-correlation in TCP is equivalent to regularizing the selective parameters of Mamba over each time step, which leads our approach to be effective and lightweight. We conducted extensive experiments on both synthetic and real-world datasets, demonstrating that Mamba-CDSP not only outperforms baselines by a large margin, but also exhibits prominent running efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a Time-shared Heterogeneity Learning from Time Series (THLTS) method which infers the shared part of latent factor across time steps with a variational auto-encoders (VAE), the method could capture the hidden heterogeneity by recovering the hidden factors and incorporate it into the outcome prediction. This method can be a flexible component to be easily inserted into arbitrary counterfactual outcome forecast models. The authors demonstrate the effectiveness of THLTS on (semi-)synthetic data in capturing shared patterns by combining several existing counterfactual outcome forecast methods to improve their performance.

### Strengths
A substantive assessment of the strengths of the paper, touching on each of the following dimensions: originality, quality, clarity, and significance. We encourage reviewers to be broad in their definitions of originality and significance. For example, originality may arise from a new definition or problem formulation, creative combinations of existing ideas, application to a new domain, or removing limitations from prior results. You can incorporate Markdown and Latex into your review. See https://openreview.net/faq.

Originality
The paper proposes a novel approach to capturing hidden heterogeneity in time series based counterfactual prediction, which is a significant domain problem in causal learning. The proposed Time-shared Heterogeneity Learning from Time Series method is a novel method that addresses this specific challenge by encoding the shared time-aware latent confounder and then utilizing them for counterfactual outcome forecasting.

Quality
The paper provides a clear and well-structured presentation of the proposed method, including a detailed explanation of the shared latent confounder variable encoding process via VAE and how to adapt to time series data.
The experimental results basically demonstrate the effectiveness of the proposed method in improving the performance of mainstream models. 

Clarity
The paper is well-written and easy to follow, with clear explanations of technical concepts and methods. The authors provide an informative context in each section that effectively organizes the story and summarizes the paper contributions.

Significance
The proposed THLTS method has the potential to improve the accuracy of counterfactual outcome in time-series data scenarios. The capture of hidden heterogeneity across time domains is a common challenge in many fields. The proposed method is flexible and can be easily inserted with arbitrary causal modeling framework, making it a valuable contribution to the field.

### Weaknesses
 (1) My major concern is notation and presentation of the paper: The paper has too many overloading of notations-- for example, "a" or the actions are giving variable A_t but the system parameter is also A. This has been quite confusing to me for sometimes.  

(2) Re. experiments: I am not sure, results of Table 2 are statistically significant: I was looking for paired t test to see how well their method is effective with respect to baselines.

### Questions
Please list up and carefully describe any questions and suggestions for the authors. Think of the things where a response from the author can change your opinion, clarify a confusion or address a limitation. This is important for a productive rebuttal and discussion phase with the authors.



Besides RMSE, it would be good to add other ablation study such as distribution analysis of the counterfactual prediction from utilizing the proposed method vs. baselines, which would provide more evidence to validate the the effectiveness of introducing the shared latent factor as illustrated in Figure 1
In table1 and table2, could the author elaborate on more details of the baseline THLTS(v)? Why author think this would be fair baseline to justify the rationality of learning shared part of latent factors compared to the proposed method
In Algorithm 1, what is the difference between forecast model pρ() and gρ()?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper works with a time varying counterfactual prediction method using STATE-SPACE model.  It introduces methods that de-correlate between current treatment and historical covariates. They claimed that their model is effective and lightweight. Finally, they performed experiments on several datasets to highlight the efficacy of their method.

### Strengths
(1) New problem on TCP on state-space model

(2) Design of novel de-correlation mechanism to reduce confounding bias.

### Weaknesses
1. Theoretical Analysis:

-Limited theoretical justification for why CDSP works better than traditional balancing

-Could benefit from more formal analysis of the bias-variance trade-off, specifically addressing how the decorrelation mechanism impacts both bias and variance in the counterfactual predictions. It is unclear how the selective parameter decorrelation avoids over-balancing, and a more rigorous explanation is needed.

2.Empirical Validation:

-Could benefit from more diverse real-world datasets, particularly those with varying degrees of confounding and different temporal dynamics. The current datasets might not fully capture the range of challenges in real-world time-varying counterfactual prediction.

-Limited discussion of failure cases, specifically when and why the method might underperform compared to existing methods. It would be useful to understand the conditions under which the CDSP mechanism is less effective.

-More detailed hyperparameter sensitivity analysis needed, especially regarding the decorrelation threshold and its impact on the model's performance across different datasets and sequence lengths. The current analysis lacks a systematic exploration of how these parameters affect the bias-variance tradeoff.

### Questions
See above.

### Soundness
2

### Presentation
2

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
This paper introduces Mamba-CDSP, a novel approach for time-varying counterfactual prediction (TCP) using state-space models. The key innovation lies in combining the Mamba architecture (a recent advance in state-space modeling) with a new Covariate-based Decorrelation towards Selective Parameters (CDSP) mechanism. The method addresses two major challenges in TCP: computational efficiency and the over-balancing problem. The authors demonstrate superior performance over existing methods like Causal Transformer and G-Net on both synthetic and real-world datasets.

### Strengths
1. Technical Innovation:

-Novel combination of Mamba architecture with TCP

-Well-designed CDSP mechanism that addresses known limitations

-Efficient implementation with linear time complexity

2. Practical Value:

-Better handling of long sequences

-Improved computational efficiency

-Real-world applicability demonstrated on MIMIC-III dataset


3.Experimental Design:

-Comprehensive ablation studies

-Multiple evaluation scenarios

-Reasonable baseline comparisons

### Weaknesses
1. The novelty and technical contribution of this paper are not enough. This paper claims to address the deconfounding and over-balance issues in the TCP task, but these issues are not first proposed by this paper. Below, I will further explain my opinion.
2. The authors claim that they are the first to consider the step-by-step deconfounding in the TCP task. However, to my knowledge, there are several existing works that achieve a similar goal, such as [1] and [2]. The authors should illustrate the difference between them.
3. Why would the linear correlation between $a_t$ and $h_{t-1}$ lead to the over-balancing issue while the non-linear correlation would not, as you remark in line 292? Can you provide a rational analysis regarding this method?
4. This method seems to simply replace the transformer with the Mamba model by slightly tailoring the backbone, which lacks technical contribution.
5. The sizes of the datasets used in the experiments are quite small; for example, there are only 5,000 patients in the MIMIC-III real-world dataset, which cannot adequately reveal the efficiency of replacing the Transformer with the Mamba model.

### Questions
1. How sensitive is the CDSP mechanism to the choice of decorrelation threshold?
2. Could the authors provide more insight into the computational complexity trade-offs between CDSP and traditional balancing methods?
3. How does the method perform on extremely long sequences (e.g., >1000 timesteps)?

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
3

### Summary
The paper presents a novel approach to TCP using a Counterfactual Mamba model with Covariate-based Decorrelation towards Selective Parameters (Mamba-CDSP). It addresses the limitations of current methods, particularly those based on LSTM and Transformer architectures, in capturing long-sequence interactions effectively and efficiently. The proposed Mamba-CDSP aims to mitigate confounding bias by decorrelating current treatments from historical covariates and outcomes. The authors provide empirical experiment over both synthetic and real-world datasets, demonstrating that Mamba-CDSP significantly improves prediction performance and running efficiency compared to existing methods.

### Strengths
1. The motivation of this paper is well claimed.
2. The writing of this paper is good and easy to follow. The preliminaries part is particularly clear.
3. The experiment part is comprehensive, consisting of synthetic and real-world datasets.

### Weaknesses
1. Limited theoretical analysis of why covariance decorrelation works better than traditional balancing approaches. The paper lacks a rigorous theoretical justification for the proposed covariance decorrelation mechanism. While the method shows empirical improvements, the absence of a theoretical framework makes it difficult to understand the underlying principles that drive its performance. Specifically, the paper does not provide a clear explanation of how the decorrelation mechanism addresses the limitations of existing balancing methods, or why it is superior in the context of time-varying counterfactual prediction. A more detailed theoretical analysis, perhaps involving risk bounds or convergence analysis, would significantly strengthen the paper.

2. While performance improvements are shown, deeper analysis of where/why the improvements come from would strengthen the paper. For instance, Table 2 shows substantial gains from CDSP on the MIMIC-III real-world dataset, but this is puzzling since we cannot observe counterfactuals in this data and thus confounding bias should have minimal impact on evaluation. The authors should explain why CDSP shows such dramatic improvements if the test metrics don't actually measure counterfactual prediction ability. This suggests the gains might come from other aspects of the method beyond bias correction, which deserves further investigation. It is unclear if the improvements are due to better bias correction, better feature representation, or other factors. A more detailed ablation study or analysis of the learned representations would be beneficial.

3. A more thorough literature review on temporal counterfactual estimation would enhance the paper by incorporating recent works like,
   - Chen et al, A Multi-Task Gaussian Process Model for Inferring Time-Varying Treatment Effects in Panel Data
   - Wu et al, Counterfactual Generative Models for Time-Varying Treatment
   - Wang et al, A Dual-module Framework for Counterfactual Estimation over Time
   - Berrevoets et al, Disentangled counterfactual recurrent networks for treatment effect inference over time

4. The paper lacks sufficient implementation details for reproducibility. While the model architecture is described, key details such as hyperparameters (hidden dimensions, number of layers), the decorrelation coefficient, and dropout rates are not specified. These details are crucial for reproducing the reported results. The description of the decorrelation mechanism is also somewhat vague, lacking specific details on how it is implemented and optimized. The paper should provide a more detailed explanation of the implementation process, including the specific optimization algorithms and parameters used.

The reference for domain adversarial learning on line 269 is incorrect, for example Lim 2018 did not use domain adversarial learning strategy

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Mamba-CDSP, a novel approach for time-varying counterfactual prediction (TCP) based on state-space models (SSMs). The key contribution is adapting the Mamba architecture with a covariate-based decorrelation mechanism to handle sequential confounding bias while preserving covariate information. The authors demonstrate superior performance compared to existing methods on synthetic and real datasets.

### Strengths
1. Novel application of SSMs (specifically Mamba) to TCP, showing promising results in both effectiveness and efficiency. The paper leverages state-space models for counterfactual prediction, achieving significant improvements in both prediction accuracy and computational speed compared to existing methods.

2. Well-motivated decorrelation approach that addresses key limitations of existing balancing methods. The proposed CDSP mechanism offers a novel solution to the over-balancing problem in sequential settings, effectively balancing between confounding bias correction and preservation of important covariate information.

3. Comprehensive empirical evaluation across multiple datasets and settings.

### Weaknesses
1. Limited theoretical analysis of why covariance decorrelation works better than traditional balancing approaches.

2. While performance improvements are shown, deeper analysis of where/why the improvements come from would strengthen the paper. For instance, Table 2 shows substantial gains from CDSP on the MIMIC-III real-world dataset, but this is puzzling since we cannot observe counterfactuals in this data and thus confounding bias should have minimal impact on evaluation. The authors should explain why CDSP shows such dramatic improvements if the test metrics don't actually measure counterfactual prediction ability. This suggests the gains might come from other aspects of the method beyond bias correction, which deserves further investigation.

3. A more thorough literature review on temporal counterfactual estimation would enhance the paper by incorporating recent works like,
   - Chen et al, A Multi-Task Gaussian Process Model for Inferring Time-Varying Treatment Effects in Panel Data
   - Wu et al, Counterfactual Generative Models for Time-Varying Treatment
   - Wang et al, A Dual-module Framework for Counterfactual Estimation over Time
   - Berrevoets et al, Disentangled counterfactual recurrent networks for treatment effect inference over time

4. The paper lacks sufficient implementation details for reproducibility. While the model architecture is described, key details such as hyperparameters (hidden dimensions, number of layers), the decorrelation coefficient, and dropout rates are not specified. These details are crucial for reproducing the reported results.

The reference for domain adversarial learning on line 269 is incorrect, for example Lim 2018 did not use domain adversarial learning strategy

### Questions
1. Is CPSD on line 316 a typo?

2. Which dataset was used for Table 3?

3. How sensitive is the method to the choice of decorrelation hyperparameters?

### Soundness
2

### Presentation
3

### Contribution
3
