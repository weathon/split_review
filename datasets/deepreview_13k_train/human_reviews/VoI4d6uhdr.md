# An Effective Theory of Bias Amplification

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Machine learning models may capture and amplify biases present in data, leading to disparate test performance across social groups. To better understand, evaluate, and mitigate these possible biases, a deeper theoretical understanding of how model design choices and data distribution properties could contribute to bias is needed. In this work, we contribute a precise analytical theory in the context of ridge regression, both with and without random projections, where the former models neural networks in a simplified regime. Our theory offers a unified and rigorous explanation of machine learning bias, providing insights into phenomena such as bias amplification and minority-group bias in various feature and parameter regimes. For example, we demonstrate that there may be an optimal regularization penalty or training time to avoid bias amplification, and there can be fundamental differences in test error between groups that do not vanish with increased parameterization. Importantly, our theoretical predictions align with several empirical observations reported in the literature. We extensively empirically validate our theory on diverse synthetic and semi-synthetic datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper considers the theoretical foundation of the bias amplification phenomenon. On a Gaussian mixture data generating distribution and ridge regression model, the authors derive the exact form of the bias and variance formula under a high dimensional limit. Using the theory, the authors show the relationship between bias amplification and the model size, label noise, number of features, regularization, and training dynamics.

### Strengths
The proposed theory is solid with the exact formulation of the limiting risk, and it provides a rigorous foundation on the bias amplification phenomenon and its relationship with various components in machine learning models. The discovery is novel and the contribution is important to deepen our understanding of the bias amplification in ML.

### Weaknesses
1. Although the authors present the exact formulation of the risk in the main text, it is complicated to understand the implications of those formulas. It would be helpful to include more discussion to explain each term to better understand the results. Specifically, the roles of the terms $h_1, h_2, h_3, h_4$ in Definition 3.2, and the fundamental constants $e_s, \tau_s, u_s, \rho_s$ in Definition F.1, are not immediately clear. The connection between these terms and the underlying data distribution and model parameters needs further elaboration. For instance, how do these terms relate to the degrees of freedom of the covariance matrices, and what is the intuition behind their specific forms?

2. The paper's main contribution is to examine the bias amplification phenomenon using the formula. However, a formal statement about how different components affect the bias amplification is lacking. I would suggest the authors write them in formal theorems. For example, it would be beneficial to have theorems that explicitly state how the bias amplification changes with respect to the label noise ratio, the model size, and the regularization parameter. These theorems should clearly specify the conditions under which bias amplification is exacerbated or mitigated.

3. It is unclear how these theoretical findings relate to real-world deep learning models, I would suggest the authors verify the conclusion about the label noise and model size on MNIST and CNN as well. The current theoretical analysis is based on a Gaussian mixture model and ridge regression, which are simplified models compared to the complex architectures used in practice. Therefore, it is crucial to demonstrate the relevance of the theoretical findings by conducting experiments on more realistic datasets and models.

### Questions
1. Is the bias amplification phenomena even in a low dimensional model, such as classical linear regression, or it is a special phenomenon on a high dimensional limit?

2. In Figure 1, the EDD plot has an extreme phase transition in the lower left corner, can the authors provide more discussion about this behavior? Moreover, the extreme case seems to mismatch with the ADD plot on the right-hand side. 

3. According to Figure 11, most of the metrics are monotone with respect to lambda, how do you conclude the optimal lambda in this case?

### Soundness
3

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
3

### Summary
Machine learning models can capture and amplify biases present in data. This paper develops an analytical theory within the context of ridge regression to better understand and address these biases. The theory provides insights into phenomena like bias amplification and minority-group bias, revealing that optimal regularization penalties or training times may help mitigate bias. Their theoretical predictions are supported by empirical validation on diverse synthetic and semi-synthetic datasets.

### Strengths
This paper examines bias amplification in ridge regression with random projections. Theoretical findings not only predict known bias amplification effects but also reveal new amplification phenomena under isotropic covariance. These findings are further validated through empirical analysis on a complex semi-synthetic image dataset.

### Weaknesses
 - It appears that the analysis of bias amplification heavily relies on an implicit assumption about the conditional dependence heterogeneity (e.g., $w_2\neq w_1$) between the two groups. What would happen if this assumption were relaxed or removed?

- The manuscript does not sufficiently justify the definition of “bias amplification.” I think more theoretical backing is needed for this definition. 

- More theoretical justification is needed to demonstrate that ridge regression with random projections serves as an effective approximation for neural networks (NN). Additionally, in Line 172, the one-hidden-layer NN model seems lacks a nonlinear activation function?

### Questions
- I have mixed feelings about the analysis of bias amplification. On one hand, the results are somewhat intuitive if we assume two groups, one with $y = x$ and the other with $y = -x$. On the other hand, the theoretical results are based on isotropic covariance, which is a simplified scenario. What would happen if the covariance structure were non-isotropic, for instance, if the covariance between $X_i$ and $X_j$ fixes or exponentially decays? 

- In real-world datasets, we often lack information about the detailed properties of each group such as $\Sigma_1$. How can we assess whether a machine learning model trained on such data is prone to bias amplification?

- Even if we identify bias amplification and attribute it to heterogeneous conditional dependencies, how can we design a practical criterion to select the optimal $\lambda$ or runtime? Additionally, could the heterogeneity itself be leveraged to develop a better machine learning model?

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
4

### Summary
The authors introduce a simple modeling framework for understanding the phenomenon of bias amplification, i.e. the observation of abnormal disparate model performance on communities unequally represented in the dataset. The setup encompasses a regression with a linear model (both a single-layer network and a linear two-layer network are considered) on a dataset with multiple modalities and different associated rules. This framework allows them to capture some key aspects of bias amplification and to make qualitative predictions on the possible regimes where over-parametrization can help or hinder the model's unbiasedness. The analytical results are derived with the tools of "operator-valued free probability theory", and corroborated with some empirical observations on standard benchmarks.

### Strengths
I believe the topic analyzed in this paper is very relevant, and theoretical contributions in this setting are crucial to understanding how to mitigate the pressing issue of bias amplification. In this context, it is interesting to understand and discuss whether the usual recipe of overparametrization could be more harmful than expected. 
The authors' analysis seems technically sound, although the methods required the introduction of some modeling assumptions that might be simplistic in some cases.

### Weaknesses
My main concern about this work is its extreme similarity, in goals, modeling setup, and some of the conclusions, with previous work ("Bias-inducing geometries: an exactly solvable data model with fairness implications" https://arxiv.org/abs/2205.15935), which is ignored in the present paper. Notice that this same reference is for example cited in ref. (Bell & Sagun, 2023) within this paper. While I can recognize some differences, reasonably motivating the present extension, there should be a clear discussion of the connections and differences.

Moreover, the authors do not discuss at length the limitations of some of their assumptions. For example, using a linear network as a proxy of a deep network, or using regularization intensity to approximate early stopping and to understand the training dynamics (without looking at the training dynamics). Although the assumptions might be "standard", the limitations should be discussed also in the present work.

Finally, some of the paragraphs on the results in figures are hardly readable because constantly refer to different values of the model parameters, often without providing a clear explanation of the "meaning" of the different regimes.

### Questions
MAJOR
1) As mentioned above, the authors should acknowledge and discuss the connection of their work to arxiv:2205.15935. Ignoring such similarity to a previous work is unacceptable for an ICLR paper. 
2) It seems plausible that much of the observed bias phenomenology in this paper is a direct effect of the double-descent / interpolation peak phenomenology, which is known to shift with the degree of over-parametrization of the network and to cause a critical sensitivity to input noise (hindering the generalization). Could the authors discuss this connection more in detail, and clarify if a different cause is at play? Is the linear activation assumption a confounding effect regarding this?
3) The imputation of the effect of early stopping in the training dynamics from the effect of a properly scaled regularization (1/t) might lead to simplistic conclusions. Can the authors discuss, for example, the connection to this previous work arXiv:2405.18296? In general, I believe mentioning optimal training time, and training dynamics both in the abstract and in the paragraph titles without specifying that this extrapolation hinges on a very simplistic approximation is misleading. 
4) Can the authors mention how, for example, their results can be used to "inform strategies to evaluate and mitigate unfairness in machine learning"?

MINORS
1) Not clear if in Fig. 1 the setting is with balanced groups, or if there is another figure for this.
2) The explanations e.g. in lines 311-317, 372-375, 400-403, 443-453, are hardly understandable if you are not extremely familiar with the model parametrization. Maybe a more effective way of presenting the results would be to state in words what setup is being considered, before looking at the parameter values.
3) I don't think it is fair practice to hide the error bars of Figure 3 in the supplementary. Moreover, the associated theoretical prediction seems very qualitative.


AFTER REVISION
Given the implemented changes, I will raise my score to a 6.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper develops a rigorous statistical framework with theory to explain and analyze model bias, particularly focusing on one of the most popular statistical methods, ridge regression, both with and without random projections (which model neural networks in a simplified regime). Its key contributions include:

Unified Theory of Bias: The paper provides a unifying theory to understand how model design choices and data distribution properties lead to bias, including phenomena like bias amplification and minority-group error. This framework explains how bias can emerge and be amplified in different feature and parameter regimes.

Bias Amplification: It analyzes how training a single model on combined data from different groups can amplify bias more than training separate models on each group’s data, even without group imbalance or spurious correlations. The theory also suggests that early stopping and tuning regularization can reduce this amplification.

Minority Group Error: The paper investigates how overparameterization and extraneous features negatively affect test performance for minority groups. It explicitly connects model size to error amplification for these groups.
Empirical Validation: The theoretical predictions are extensively validated using synthetic and semi-synthetic datasets, and the results align with empirical findings reported in prior literature.

Overall, the paper offers novel statistical theory and new insights into model bias and proposes avenues for mitigating it through informed model design and training choices.

### Strengths
**Originality**: This paper has originality. There are many works on model bias, but most of them are empirical work. A unified statistical theory of model bias is underexplored. Compared to previous work on model bias theory, this paper focuses on disparities in test error across majority and minority groups with different data distributions when models are trained on data from both groups. This paper does use existing tools based on random matrix theory from previous work, but the theory is not a special case of the existing ones. Therefore, I think the paper has its originality. 


**Quality**: This paper has good quality. The analysis using operator-valued free probability theory (OVFPT) and high-dimensional scaling limits look technically sound to me. Fixed-point equations and a detailed exploration of phase transitions (e.g., bias amplification at specific proportions of features to samples) are mathematically rigorous. Further, besides the theoretical analysis, this empirical section demonstrates how ridge regression models with random projections can amplify bias, even in balanced data without spurious correlations. This is an interesting finding. It offers a clear, empirical validation of theoretical predictions, demonstrating the impact of model size, label noise, and training dynamics on bias amplification. 

**Clarity**: The structure is clear. From preliminaries in section 2 to a detailed model analysis in section 3, and empirical study in section 4, they all manifest a well-organized and thoughtful presentation. 

**Significance**: This paper studies an important problem and provides a good contribution to the field. To be specific, this article tackles the critical issue of bias in machine learning, which can lead to unequal performance across demographic groups. It presents a new theoretical framework using operator-valued free probability theory to explain and predict bias amplification, unifying previous findings and offering a clearer understanding of bias mechanisms. The theory is validated in diverse empirical settings, showing practical relevance. Overall, this work makes a significant contribution by providing a structured approach to understanding and mitigating bias, with implications for fairer machine learning practices and future research directions.

### Weaknesses
There are no significant weaknesses in this paper. However, the following minor weaknesses can be improved. 

1. The connection between the theoretical analysis in this paper and the prior work in OVFPT is not discussed clearly enough. This paper mentions that the theory cannot be derived as a special case in Adlame et al., Tripuraneni et al., Lee et al., but does not provide a more involved explanation on why this is the case. It would thus be great if a paragraph discussing this point can be added.

2. Section 4.2 nicely addresses how regularization and training time influence bias amplification, but it lacks a bit of practical guidance on applying these insights in real scenario. After discussing the effects of regularization and training dynamics on bias amplification, the authors could add a bit more remarks or comments. This would be an ideal place to provide concrete guidance on setting regularization parameters or selecting optimal training durations for different dataset sizes and feature-sample ratios. For instance, they could suggest regularization ranges or early stopping criteria when $\psi$ is close to or above 1.

### Questions
Please see the **Weaknesses** section.

### Soundness
3

### Presentation
3

### Contribution
3
