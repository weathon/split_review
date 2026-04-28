# A General Feature Attribution Framework under a Black-box Setting

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 3, 6

## Abstract
Feature attribution is widely accepted as a form of explanation for reasoning machine decisions, indicating the proportion of each feature's contribution to an inquired decision. 
While most efforts have focused on determining attributions through exact gradient measurements, recent work has adopted gradient estimation to derive explanatory information requiring only query-level access – a restricted yet more practical accessibility assumption known as the black-box setting. 
Following this direction, this paper extends the idea of utilizing estimated gradients to a broader framework and introduces GEFA (Gradient-Estimation-based explanation For All). Unlike the previous attempt that focused on explaining image classifiers, the proposed explainer derives feature attributions in a proxy space, making it generally applicable to arbitrary black-box models, regardless of input type. 
In addition to its close relationship with Integrated Gradients, we find, surprisingly, that our approach – a path method built upon estimated gradients – outputs unbiased estimates of Shapley Values. By avoiding the potential information waste sourced from computing marginal contributions, it improves the quality of derived explanations, as demonstrated by our quantitative evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper derives a black-box feature attribution method that only asks for queries. The key idea is to state feature importance in terms of probability of presence of each feature. This turns out to produce an equivalent of Shapley values.

### Strengths
- Interesting way to generalize "gradients"
- clean derivation and presentation
- sound results and theoretical connections
- Important deviation from noising-based estimation of attribution.

### Weaknesses
The metric of choice is not fully explained. I get that the removing supposedly relevant inputs should lead to larger AOPC. However, the model that is being used to predict the label needs to be retrained to ensure that the input  has not gone output of support to what the model was trained on. Hooker et al. point this out.

Both https://arxiv.org/abs/1806.10758, https://arxiv.org/abs/2103.01890 point this out. Am I missing that the model for the scoring was retrained or trained in a special way? I'm very skeptical of what the results say without fixing this issue. Further, there is also the problem of encoding which is mentioned in the second paper (that is formally shown to make removal based evaluations improper, https://arxiv.org/abs/2411.02664). The first two papers need to be discussed. The latter is more of a reference.

Can the authors say more about how their APOC evaluation is sufficient? If not, is there a possibility to retrain the scorer model and recompute AOPC? Otherwise, I am not sure how much to trust the numbers in the tables.

### Questions
See weaknesses.

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
This paper presents GEFA (Gradient-estimation-based Explanation For All), which extends previous work on gradient estimation-based model explanations to handle both discrete and continuous features. The key innovation is introducing proxy variables that represent feature presence probabilities, allowing the method to work with any input type. It is proven that GEFA produces unbiased Shapley value estimates and introduce a variance reduction technique using control variates. The method is evaluated on both text and image classification tasks.

### Strengths
I think the paper's strengths are best contextualized as a follow up on GEEX. GEEX focused on continuous features and image classifiers, using gradient estimation in the original feature space with Gaussian noise perturbations. It proved alignment with Integrated Gradients but lacked variance reduction.

GEFA handles both discrete and continuous features through proxy variables representing feature presence probabilities. It uses binary mask sampling, proves unbiased Shapley Value calculation, and introduces feature correlation-based variance reduction. By operating in a proxy space rather than the original feature space, GEFA overcomes GEEX's continuous-only limitation. While GEEX was tested only on images, GEFA demonstrates broader applicability through evaluations on both image tasks (InceptionV3 on ImageNet) and text data (BERT on Amazon reviews), effectively bridging gradient-based and Shapley approaches.

### Weaknesses
 - I think the analysis could benefit from more diverse text tasks beyond sentiment analysis, and on tabular datasets.
- A thorough review of computational complexity would be appreciated.
- What happens when the assumption about feature presence correlation is violated?
- Why this proxy path? This could use more detail.
- Optimal beta values assume feature independence which usually does not hold in the real world.

### Questions
- How sensitive is the method to baseline image? Why use blurred images, instead of black? What about other domains?
- Do you think the control variate assumption about correlation between number of present features and model outputs is justified?
- Have you explored other proxy paths beyond the straightline? What are the tradeoffs?
- Could we apply the variance technique on other black box explanation methods?
- Is there a good way to detect when the feature presence correlation is violated?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors propose a feature attribution method based on an estimator of the gradient of the model.

They propose to construct a sequence of mask and compute the gradient of the model following this path.
They construct an estimator which is the Shapley value.

### Strengths
The computations  described in the paper are correct.

### Weaknesses
Many authors have provided different ways to explain. In this paper the authors propose another one but according to me the most important work is not achieved: 
1/ the authors provide an estimation on line 233 but the quality of such approximation depends on many factors, in particular on smoothness property of the evaluation of \tilde{f}. The gap between quantity is written using \approx but how the estimators coincide should deserve a proper treatment
2/ in the same way Theorem 3 provides the unbiasedness of the estimator. For me the definition is incorrect since \tilde{\xi} is not random in its construct. In the proof the authors claim that they want to prove that \xi=\tilde{\xi} but bias referes to the mean behaviour. I am quite lost in the objective of the proof.
3/ \tilde{\beta} is defined as the optimal parameter which is selected for the simulations. Yet its expression involves unknown quantity since it requires the knowledge of the distribution the way it is defined in line 802. How to compute it ?

### Questions
How do you select the parameters ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new framework for feature attribution that can be applied across modalities. Their main idea is use a proxy variable to control feature perturbations with the final outcome being an attribution score through averaging of the results of the perturbations. The proposed approach is for the more general black-box setting. They also theoretically show that their approach satisfies desirable properties such as completeness, insensitivity, linearity, symmetry.

### Strengths
- Important problem
- Interesting approach using proxy variables
- Prove that their approach satisfies multiple desirable properties an explanation should have
- Reported empirical results are promising

### Weaknesses
 - Some related work missing
- Presentation could be improved
- Timing and sample complexity experiments missing
- Experiments on only 2 datasets using simple models
- Not clear how to choose base values
- Only one metric used for evaluation

### Questions
I think the approach is interesting, however, I have some concerns with the current manuscript.

*Missing related work:* There are a lot of works on model explanation in the black-box setting also considering linear (proxy) explanation functions (i.e. variants of LIME and SHAP), like the current manuscript, that must be discussed in my opinion. I point to some of these works in [1-7] below.

*Improved presentation:* Equations 6 and 8 seem to be the critical equations in terms of the algorithm to estimate attributions. However, this is lost in the text. Maybe an algorithm can be added using the latex algorithm environment to highlight the main contribution. This will also make clear the computational burden of the algorithm.

*Computational complexity:* The method seems as computationally intensive as SHAP. It would be nice to have some timing comparisons in the experimental section as well as some convergence plots in terms of how the accuracy of attributions approaches the best achieved accuracy with increasing number of samplings. It is not clear intuitively to me why this is a better approach than existing ones like SHAP etc.


*More challenging experiments:* The experiments use small and somewhat outdated models such as BERT. Given the plethora of capable LLMs (viz. mistral, llamma series, etc.) it would be nice to have experiments on more state-of-the-art models. Also only 2 datasets are used. How about at least experimenting on the GLUE benchmark for the LLMs.

*Base values and evaluation:* Not clear how the base values are chosen for the method. I understand that this is an issue for even SHAP etc. but I would like some description of how they chose those in their experiments. Evaluating using ablations is fine. However, there are other metrics for explanation evaluation such as stability, fidelity, etc. [8].

[1] C. J. Anders, P. Pasliev, A.-K. Dombrowski, K.-R. Muller, and P. Kessel. Fairwashing explanations with off-manifold detergent. ICML, 2020.

[2] A. Dhurandhar, K. Ramamurthy, K. Ahuja, and V. Arya. Locally invariant explanations: Towards stable and unidirectional explanations through local invariant learning. NeurIPS, 2023.

[3] T. Botari, F. Hvilshøj, R. Izbicki, and A. C. P. L. F. de Carvalho. Melime: Meaningful local explanation for machine learning models, 2020.

[4] C. Frye, C. Rowat, and I. Feige. Asymmetric shapley values: incorporating causal knowledge into model-agnostic explainability. NeurIPS, 2020.

[5] T. Heskes, E. Sijben, I. G. Bucur, and T. Claassen. Causal shapley values: Exploiting causal knowledge to explain individual predictions of complex models. NeurIPS, 2020.

[6] A. Dhurandhar, K. Ramamurthy, K. Shanmugam. Is this the right neighborhood? Accurate and Query Efficient Model Agnostic Explanations. NeurIPS, 2022.

[7] A. Shrotri, N. Narodytska, A. Ignatiev, J. Marques-Silva, K. S. Meel, and M. Vardi. Constraint-driven explanations of black-box {ml} models, 2021.

[8] QV Liao, Y Zhang, R Luss, F Doshi-Velez and A Dhurandhar. Connecting Algorithmic Research and Usage Contexts: A Perspective of Contextualized Evaluation for Explainable AI. HCOMP, 2022.

### Soundness
3

### Presentation
2

### Contribution
3
