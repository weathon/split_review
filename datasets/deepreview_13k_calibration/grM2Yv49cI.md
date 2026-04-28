# Model aggregation: minimizing empirical variance outperforms minimizing empirical error

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Whether deterministic or stochastic, models can be viewed as functions designed to approximate a specific quantity of interest. We propose a data-driven framework that aggregates predictions from diverse models into a single, more accurate output. This aggregation approach exploits each model's strengths to enhance overall accuracy. It is non-intrusive—treating models as black-box functions—model-agnostic, requires minimal assumptions, and can combine outputs from a wide range of models, including those from machine learning and numerical solvers.
We argue that the aggregation process should be point-wise linear and propose two methods to find an optimal aggregate: Minimal Error Aggregation (MEA), which minimizes the aggregate's prediction error, and Minimal Variance Aggregation (MVA), which minimizes its variance. While MEA is inherently more accurate when correlations between models and the target quantity are perfectly known, Minimal Empirical Variance Aggregation (MEVA), an empirical version of MVA—consistently outperforms Minimal Empirical Error Aggregation (MEEA), the empirical counterpart of MEA, when these correlations must be estimated from data.
The key difference is that MEVA constructs an aggregate by estimating model errors, while MEEA treats the models as features for direct interpolation of the quantity of interest. This makes MEEA more susceptible to overfitting and poor generalization, where the aggregate may underperform individual models during testing. We demonstrate the versatility and effectiveness of our framework in various applications, such as data science and partial differential equations, showing how it successfully integrates traditional solvers with machine learning models to improve both robustness and accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors study the problem of model aggregation where one intends to learn to combine the predictions given by different models. The authors study two variants, Minimal empirical error aggregation and Minimal empirical variance aggregation, both of which differ mainly with respect to the loss functions used. The former penalizes the error w.r.t. the aggretage function, while the latter takes into account the errors of the individual models. The authors study two applications: aggregating models in housing price prediction and learning aggregated solvers for PDE, the motive being illustrating that the MEVA learns to pick the model with low error for any given input.

### Strengths
- The paper is written well, easy to follow. The key ideas are articulated nicely. 
- The contributed solutions seem significant more in the context of PDE solvers, where the metrics for the aggregated model outperform that of the baselines.

### Weaknesses
It is not very clear in the data-science settings when the aggregated models would be useful. Few more experiments migt add more clarity to that. For instance, the ensemble methods such as random forests achieve similar performance to that of the propsoed schemes. Would there be any advantage in using these aggregate schemes upon the existing benchmarks in data-science problems ?

While the proposed formulations differ mainly with respect to the loss function, what may be the data assumptions which would help us understand the performance differences of one loss over other better ? Specifically, when do we expect the loss function (5) to be better than (13) and vice versa ? Some analysis w.r.t. the underlying data assumptions may help understanding them better.

Would learning the functions in the pathological examples be valid if the input samples are chosen randomly rather than in the specific patterns ? Does this mean that the failure of learning the underlying model is partly due to the choice of the points which are presented for learning ?

It was mentioned that MEVA doesn't improve the performance in settings when P not equals Identity, (line 263), what is the implication of that in practical cases ? How practical is the assumption that expect multiple models' errors to be independent ?

### Questions
Would learning the functions in the pathological examples be valid if the input samples are chosen randomly rather than in the specific patterns ? Does this mean that the failure of learning the underlying model is partly due to the choice of the points which are presented for learning ?

It was mentioned that MEVA doesn't improve the performance in settings when P not equals Identity, (line 263), what is the implication of that in practical cases ? How practical is the assumption that expect multiple models' errors to be independent ?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper compares two different approaches to model aggregation: the first approach is called Minimal Empirical Error Aggregation (MEEA), which minimizes (over $a$): $\sum_{i=1}^N\left|Y^i-a\left(X^i\right)^T M\left(X^i\right)\right|^2+\lambda\|a\|_{\mathcal{H}}^2$, where $(X^i, Y^i)$ are $N$ data points, $\mathcal{H}$ is a set of functions used for the approximation, and $\lambda \geq 0$. In this approach, models $M\left(X^i\right)$ are treated as if they are features in regression. Section 3 gives pathological examples that show that this approach may produce an unreasonable aggregation. The second approach called Minimal Empirical Variance Aggregation (MEVA) has the same form of linear weights but $\alpha(x)$ is obtained differently: i.e., $\alpha(x)^T M(x)$, where the $i$-th element of $\alpha(x)$ equals $\exp(-\lambda_i(x))/[\sum \exp(-\lambda_k(x))]$, where summation is over $k$. To obtain $\lambda_i$, first write $e^i$ for the vector with entries defined as the sample errors $\left(e^i\right)_k=M_k\left(X^i\right)-Y\left(X^i\right)$. Then, $\lambda$ minimizes (over $l$): $\sum \sum \left(\exp(l_k\left(X^i\right))-\left(e^i\right)_k^2\right)^2$ plus some penalty term, where double summation is over $i$ and $k$. The numerical experiments consider aggregation using the Boston housing dataset as well as aggregation of PDE solvers.

### Strengths
- MEVA seems an interesting idea and can be potentially impactful when model aggregation is necessary. 
- It sounds neat to cast numerical PDE as combining Partial Differential Equation (PDE) solvers through model aggregation.
- The paper is professionally edited and written.

### Weaknesses
 - It is unclear what the benchmark is in the literature. The method called MEEA may not be commonly used in the literature and there is no clear sense that this paper improves the current state-of-the-art. Specifically, the paper does not adequately position MEEA within the broader context of model aggregation techniques, making it difficult to assess the novelty and significance of the proposed MEVA method. The paper would benefit from a more thorough discussion of existing aggregation methods, such as Bayesian model averaging or stacking, and a clear explanation of how MEEA relates to these established approaches. Without this context, it is hard to evaluate the necessity of introducing MEVA.
- There is no theoretical result that guarantees the superior performance of MEVA relative to MEEA or simple averaging (that is, $\alpha(x) = 1/n$ uniformly over $x$). While empirical results are presented, the lack of theoretical justification raises concerns about the robustness and generalizability of the proposed method. A theoretical analysis, even if limited to specific conditions, would significantly strengthen the paper's claims. For example, establishing conditions under which MEVA converges to the optimal aggregation or providing bounds on its error would be valuable.
- There is a hyper parameter to be tuned (e.g., the penalization parameter $a$ in equation (13)), but it is unclear how to choose it. The paper lacks a clear methodology for selecting the hyperparameter, which is crucial for the practical application of the method. The absence of a systematic approach for hyperparameter tuning makes it difficult to reproduce the results and limits the usability of the proposed method. The paper should provide guidelines or recommendations for choosing this parameter, possibly through cross-validation or other established techniques.

### Questions
- Perhaps I missed this, but it is unclear how to specify the $l(\cdot)$ function in equation (13). It would be useful to provide a concrete example of this, after stating equation (13).
- What are the most popular or best performing methods in PDE solvers? It might be good to indicate how well the propose method works relative to the most popular or best performing methods in practice.
- Would it be possible to provide computational speed or difficulties as aggregation would take more time than using only one individual model?

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
This paper presents a data-driven framework designed to consolidate predictions from various models, thereby improving overall accuracy by capitalizing on their unique strengths. This approach is non-intrusive and model-agnostic, treating the contributing models as black boxes and allowing for the integration of outputs from a wide range of methodologies, such as machine learning techniques and conventional numerical solvers. The authors introduce a point-wise linear aggregation method and investigate two strategies for optimizing this aggregation:

The first, Minimal Error Aggregation (MEA), aims to directly minimize prediction errors, while the second, Minimal Variance Aggregation (MVA), seeks to lower variance by estimating the errors of the models. Although MEA is theoretically optimal when the correlations between models and the target are perfectly understood, its empirical counterpart, Minimal Empirical Error Aggregation (MEEA), frequently encounters issues with overfitting due to inaccuracies in correlation estimates. The authors illustrate that the empirical variant of MVA, termed Minimal Empirical Variance Aggregation (MEVA), consistently surpasses MEEA by effectively estimating model errors and aggregating the results. This method mitigates the risk of overfitting and improves generalization capabilities. The efficacy of MEVA is validated through various applications, including the Boston Housing dataset and the resolution of partial differential equations (PDEs) such as the Laplace and Burgers' equations. In these tests, MEVA demonstrates superior performance compared to individual models and MEEA, leading to a more resilient and precise aggregate model.

### Strengths
The paper introduces an innovative methodology for model aggregation that shifts the emphasis from the conventional goal of minimizing empirical error to the more nuanced objective of minimizing empirical variance. This approach is relatively uncommon in existing literature. Traditional ensemble techniques, such as bagging and boosting, primarily concentrate on reducing variance or bias through averaging or additive strategies. In contrast, this study highlights the importance of variance minimization via error estimation, a perspective that has not been extensively investigated.

The theoretical underpinnings of the proposed methods are robust, featuring comprehensive derivations and justifications. The authors conduct an in-depth examination of scenarios where the Model Error Estimation Aggregation (MEEA) falters while the Model Error Variance Aggregation (MEVA) excels, offering valuable insights into the benefits of focusing on variance minimization. This discussion is pertinent to the well-documented challenges of overfitting associated with empirical risk minimization, where models that prioritize empirical error reduction may struggle with generalization.

The organization and clarity of the paper are commendable, as it effectively presents complex ideas in an accessible manner. Necessary definitions are provided, and the step-by-step explanations aid in comprehension. The use of illustrative examples, figures, and comprehensive descriptions of experimental methodologies further enhances the work's readability and transparency.

By illustrating that a focus on minimizing empirical variance can yield superior aggregation performance compared to merely minimizing empirical error, this paper makes a good contribution to the field of ensemble learning. The capacity to aggregate a variety of models, including those derived from different methodologies and domains, underscores the versatility of this approach. This has important implications for numerous fields where the integration of multiple predictive models is advantageous, such as climate modeling, where ensemble methods are employed but often rely on simplistic aggregation techniques.

### Weaknesses
The methodology is predicated on the premise that individual models serve as unbiased estimators of the target variable. However, in real-world applications, models may demonstrate bias stemming from systematic errors or incorrect model specifications. This concern is well-documented in the context of model averaging, as highlighted by Claeskens and Hjort (2008), where the presence of biased models can detrimentally influence the overall aggregation. Although the paper acknowledges this limitation, it does not delve deeply into the implications of such assumption violations on the aggregation process or propose modifications to accommodate biased models.

2. The experiments conducted, while illustrating the efficacy of MEVA in certain scenarios, exhibit a degree of limitation in their breadth. The Boston Housing dataset, being relatively small, may not adequately capture the complexities associated with larger and more intricate datasets. Furthermore, while the PDE examples are pertinent, they could be enhanced by incorporating additional real-world applications to better demonstrate the method's applicability across various contexts. Recent advancements in operator learning, as discussed by Kovachki et al. (2023), tackle complex PDEs in higher dimensions, and evaluating MEVA within these frameworks would bolster the validity of its claims.

3. In the experiment utilizing the Boston Housing dataset, the enhancements offered by MEVA over alternative methods appear to be modest, particularly regarding mean squared error (MSE). This observation prompts a reevaluation of the practical significance of the method's purported benefits in conventional machine learning tasks. Established ensemble techniques, such as gradient boosting, have demonstrated substantial improvements in these areas, suggesting that a more comprehensive comparison of MEVA's performance against these well-regarded methods would be advantageous.

### Questions
The inquiry into the handling of biased models raises significant questions regarding the assumption of individual model impartiality. It is essential to explore whether the MEVA method can be adapted to include biased models and what specific alterations would be required for such an extension. Additionally, it is important to consider how the existence of bias within the models might influence the overall performance of the aggregation process.

The presence of correlated model errors in practical applications necessitates an understanding of how MEVA addresses these correlations. It is pertinent to evaluate the sensitivity of aggregation performance to such error correlations and to consider whether incorporating off-diagonal elements in the covariance matrix could enhance the model's robustness.

A comparative analysis of MEVA against other established aggregation methods, such as stacking, weighted averaging, or contemporary ensemble techniques, would provide valuable insights into its relative performance and practical benefits.

Lastly, the selection of function spaces, such as Reproducing Kernel Hilbert Spaces (RKHS), and the tuning of regularization parameters are critical components of the method. Practical guidelines or heuristics for these selections, as well as an assessment of how sensitive the method's performance is to these hyperparameters, would be beneficial for practitioners.

### Soundness
3

### Presentation
4

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
This paper focuses on model aggregation by minimizing empirical variance rather than empirical bias, which can lead to better generalization. By making appropriate assumptions about the error model, the authors present a tractable aggregation scheme using nonparametric methods. They evaluate their approach on a housing dataset and two PDE solver problems, demonstrating its accuracy and effectiveness.

### Strengths
1. This paper highlights the drawbacks of current aggregation approaches that focus on minimizing prediction error, using extensive discussions and interpretable examples to provide valuable insights into model aggregation.
2. The proposed Minimal Empirical Variance Aggregation method is intuitive and performs effectively in certain model aggregation tasks.
3. The implementation on PDE solvers is both interesting and practically useful.

### Weaknesses
1. There is a lack of rigorous theoretical discussion on the superiority of MEVA over MEA. Including some theoretical investigations would be preferable. Besides, the implementation of MEVA requires certain approximations. Some theoretical guarantee for the final performance of MEVA towards MVA should be considered.
2. The derivations of MVA and MEVA rely heavily on assumptions about the error model, which may not hold in practice. The authors should address the issue of misspecification in the paper. Specifically, the assumption of unbiased errors, while simplifying the derivation, needs more justification, especially given that model errors are often biased in real-world scenarios. The impact of this assumption on the final performance should be analyzed, and potential methods to mitigate the effects of misspecification should be discussed.
3. The experiments using real-world data are not comprehensive, as only a single housing dataset is evaluated. It is necessary for the authors to include more experiments to further demonstrate MEVA's performance if the paper is accepted. The current experiments do not sufficiently demonstrate the generalizability of the proposed method to diverse datasets and problem settings.
4. Although I am not familiar with the background of model aggregation, I noticed the absence of a literature review and comparison with relevant benchmarks. The cited literature in the related work section consists mainly of reviews and some unrelated papers in scientific computing, and there is no specific model aggregation approaches compared in the real-data experiments. More comparing benchmarks should be discussed and evaluated in the paper. For example, in econometrics, there is extensive literature on model averaging [1,2], which also uses linear combinations of models to improve predictions. The authors should discuss these approaches and include comparative experiments.

### Questions
1. Figure 2. It appears that MEVA does not outperform the random forest model in the housing data experiment. Can the authors explain the reasons for this outcome? And I have a minor comment on Figure 2. The labels in x-axis are too small to see them clearly. It is better to arrange this.
2. Can the authors discuss the robustness of the approximation of $A(x)$ mentioned in Line 258? Is it reasonable to expect this approximation to hold in practice, and what are the potential impacts if the underlying assumptions are incorrect? A discussion on this issue, along with references to relevant literature, would be appreciated.

### Soundness
3

### Presentation
3

### Contribution
3
