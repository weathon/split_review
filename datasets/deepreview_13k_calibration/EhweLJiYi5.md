# LCEN: A Novel Feature Selection Algorithm for Nonlinear, Interpretable Machine Learning Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 1, 5, 5, 5

## Abstract
Interpretable models can have advantages over black-box models, and interpretability is essential for the application of machine learning in critical settings, such as aviation or medicine. LASSO and elastic net, the most commonly used interpretable methods, are limited to linear predictions and have poor feature selection capabilities. Other important interpretable methods, such as tree-based or generalized additive models, are nonlinear but have limited performance in some scenarios. In this work, we introduce the LASSO-Clip-EN (LCEN) algorithm for the construction of nonlinear, interpretable machine learning models. LCEN is tested on a wide variety of artificial and empirical datasets, frequently creating more accurate, sparser models than other models, including those for building sparse, nonlinear models. LCEN is robust against many issues typically present in datasets and modeling, including noise, multicollinearity, data scarcity, and hyperparameter variance. LCEN is also able to rediscover multiple physical laws from empirical data and, for processes with no known physical laws, LCEN achieves better results than many other dense and sparse methods -- including using 10.8-fold fewer features than dense methods and 8.1-fold fewer features than EN on one dataset, and is comparable to or better than ANNs on multiple datasets.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces the LASSO-Clip-EN (LCEN) algorithm, which combines lasso with feature expansions (including quadratic, cubic, and interaction terms), elastic net, and hard-thresholding steps. The method maintains interpretability due to its foundation in lasso-type techniques and its emphasis on sparse feature selection.

### Strengths
Both high-dimensional statistics and interpretable machine learning are fundamental tasks.

### Weaknesses
1. The proposed method offers minimal novelty. The clip step is essentially a hard-thresholding step. To remove irrelevant variables, adaptive lasso (Zou 2006) or adaptive elastic (Zou and Zhang 2008) net could be used instead, as they function as two-step methods that impose higher weights in the second step, penalizing features with smaller coefficients identified in the first step. These approaches are more flexible and robust than a straightforward hard-thresholding step. The combination of lasso with various thresholding approaches is not a surprising idea.
2. The authors should discuss and compare their method with existing techniques like SCAD and MCP, which specifically address the lasso's tendency to over-select features. Added features could be more effectively managed using spline-based methods (natural or B splines) or sparse generalized additive models (Ravikumar et al 2009, Haris et al, 2022), which are better suited for high-dimensional settings. The literature review in this paper is notably insufficient. Both theoretical and numerical comparisons between the proposed method and adaptive elastic net with the splines are necessary.
3. High-dimensional statistics papers typically include solid theoretical foundations due to the simplicity of the models. This paper lacks any theoretical analysis. The author should provide convergence guarantees, consistency results, or bounds on estimation error for the proposed method.
4. The experimental validation is limited. The authors should conduct extensive experiments to assess performance in feature selection. Specifically, besides MSE and MAD, the authors should also consider false positive and false negative rates for feature selection. It is not enough to only show the number of features selected. Comprehensive analysis using extensive benchmark datasets is also necessary to demonstrate the efficacy of the proposed method. The authors can use the benchmark data from UCI with a focus on high-dimensional data where the number of features is over 1000.

### Questions
No additional questions. See the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces LASSO-Clip-EN (LCEN), a supervised learning algorithm with built-in feature selection and non-linear feature effects through a deterministic feature expansion scheme including polynomial transformations, interaction effects, and basic non-linear transformations such as log or inverse and combinations of the aforementioned. The final estimator is obtained as a hard-thresholded elastic net estimator on an expanded feature set. The hyperparameters for the feature expansion scheme are first determined using cross-validation on a lasso model with additional hard thresholding, after which the elastic net hyperparameters are tuned using the feature expansion scheme determined in the lasso step. This results in a sequential algorithm that produces sparse linear coefficients of deterministic non-linear feature transformations, with the complexity of the transformations determined in a first step.

### Strengths
This paper demonstrates several notable strengths. 

- **Originality**: While the individual components (LASSO/EN, feature transformations, hard thresholding) are well-established techniques, their combination and sequential application in that order represents an original contribution that helps bridge the gap between classical linear models and more powerful black-box approaches. 
- **Technical details and Experiments** The paper shows strengths in its detailed algorithm description and sound experimental evaluation, as well as an appropriate choice of competitor models for the experiments. The experimental methodology is well-structured, progressing from artificial data (to validate basic properties) to known physical laws (to verify feature selection properties) and real-world applications. The presentation of results is very thorough and detailed. 
- **Significance**: Further, the work addresses the important challenge of creating interpretable models with non-linear effects that maintain competitive performance, with the demonstrated ability to recover known physical laws while being computationally cheap. 
- **Reproducibility**: The code appears to be well-written and correct, although I did not run it.

### Weaknesses
## Major weaknesses

This first part contains the most important concerns that I would expect the paper to answer in order to be relevant for the general ML audience. These major weaknesses, however, might require well-justified additional explanations and/or notable additional work on both contextualizing/establishing theoretical results and a more varied experimental evaluation.

1. **Motivation/Soundness**: While the method itself is well-described, the only motivation for its construction is given by the ablation study comparing it against other possible approaches combining the feature-expanded lasso and elastic net sequentially with or without hard thresholding. A proper motivation of the method should give some hints regarding:
    * **A**: Why does LCEN use a sequential procedure for determining the complexity of the feature transformations and the elastic net hyperparameters separately? Why not perform one big hyperparameter search for both the degree/lag hyperparameters of the transformations and the EN alpha and l1_ratio of EN (and then hard threshold the selected coefficients once)?
    * **B**: Why use a hard thresholding step at all after having obtained already sparse estimates from lasso or elastic net? If the aforementioned support recovery conditions for lasso are met and the lasso successfully identifies the true features, then this additional post-thresholding/clip step might remove relevant features with non-zero effects and thus harm both feature selection and likely predictive performance. If the conditions are violated, the lasso is known to overselect irrelevant features, which can be alleviated by such a hard-thresholding operation of the lasso estimates (Zhou, 2010, Meinshausen and Yu, 2009). If this is the case this motivation should be mentioned more explicitly in the paper.
    * **C**: Why does the final step also include a hard-thresholding step? Typically, hard-thresholding after the lasso (or equally elastic net) improves support recovery but slightly harms estimation error. Hence, the literature revolving around sequential lasso estimation with hard thresholding (Zhou, 2009;2010;2023, van de Geer et al., 2011) uses this approach only in the first step to identify the relevant features, and in the final step fits an OLS model on the reduced feature set to counteract the shrinkage bias introduced by L1 and L2 regularization in the coefficients (van de Geer et al., 2011, Belloni and Chernozhukov, 2013). Such a debiasing step at the end is missing from LCEN, whose goal decidedly is not only to select the correct features but also produce the correct coefficients.
    * **D**: Why does the first step use a different regularizer (lasso) than the second step (elastic net)? I suspect this will produce some theoretical inaccuracies, as parts of the hyperparameters were tuned toward another objective than the others.

2. **Technical soundness**: The paper does not provide any theoretical results motivating or justifying the method, nor does it establish results under which conditions the algorithm can perform support recovery, i.e., select the true (transformed) features involved in the data-generating process with high probability, or achieve estimation consistency. In the sparse estimation literature, various classical conditions such as restricted isometry/eigenvalue/nullspace, irrepresentability, or mutual incoherence conditions are discussed to this end (e.g., van de Geer and Bühlmann, 2009). Moreover, the relative coefficient magnitudes, in particular the smallest non-zero coefficient, are important quantities in these analyses (e.g., Zhou, 2010). This is important for the thresholding/clipping step, whose success depends strongly on the relative magnitude of the smallest non-zero coefficients. The relationship of LCEN’s ability for support recovery should be related to these concepts, at least in the form of a discussion of their applicability or what changes under LCEN instead of (multi-stage) thresholded lasso/EN (formally would be better).

    I think for LCEN to be properly presented and analyzed for the broader machine learning audience, answering questions roughly similar to the given references is expected for an extension/variation of the multi-stage thresholded lasso (Zhao, 2009). Under which conditions can LCEN select the true transformed features? Under which conditions is the estimator consistent? How does the algorithm’s runtime and complexity scale with increasing $n$ and $p$ and “degree”, and at which point does it become infeasible on a CPU? How does it perform on varied tasks with different amounts of sparsity and ratios of samples to features (in particular, experiments in a high-dimensional setting are missing where $p>>n$ - however these are usually most important sparse regression)

3. **Numerical experiments**: While the experiments are numerous and well executed, they are insufficient to show the general effectiveness of the method as well as to corroborate the investigated claims. The first two experiments, aimed at showing the robustness of LCEN against increasing noise levels and multicollinearity, are insufficient to convince the general reader since they are overly simplistic toy examples using a simple additive data-generating process with a handful of variables at best. The relativistic energy example also includes only two coefficients to be estimated. In the comparison against the ALVEN algorithm - which uses a similar feature expansion scheme, but employs F-tests for feature selection - 30 training data points are simulated from a fourth-degree univariate polynomial with additive noise. Although this setting was reproduced from the ALVEN paper, superiority on this simple example is not convincing to establish superiority of LCEN over ALVEN in a more general sense. The three subsequent experiments on recovering known physical laws from data involve data sets with ($n=293, p=2$), ($n=6, p=1$), ($n=8, p=1$) observations and (original, unexpanded) features, respectively. For the classical ML datasets, Diesel Freezing Point data has $n=395$ samples and $p=401$ features, Abalone has $n=4177$ samples and $p=8$ features, Boston Housing has $n=506$ samples and $p=13$ features, Concrete Compressive Strength has $n=1030$ samples and $p=8$ features. Finally, GEFCom 2014 is a time-series prediction task. Together, these set-ups seem inappropriate for a thorough empirical evaluation of the proposed method. For example, all but one method select all $8$ features on the Abalone data set. An adequate experimental evaluation should include datasets with varying properties, for example, {small n, large n}x{small p, large p}x{low ground truth sparsity, high ground truth sparsity}x{low complexity of data-generating process, medium complexity, high complexity}. Moreover, the experimental results should come with reported uncertainties of the performance metrics, particularly in model comparisons (e.g., mean+standard deviation over 10 splits).

4. **Related literature/Novelty**: The paper lacks a discussion of previous thresholded-lasso works, and particularly the established theoretical results therein, almost entirely (below references are a starting point). In my opinion, this should be an important part of the related literature section of the LCEN paper, as LCEN is very similar to the thresholded lasso with refitting, but using a deterministically expanded feature set instead of the raw features and using another regularized model, again with hard thresholding, instead of OLS in the second step.

Together, these points would require the inclusion of new theoretical results or at least a detailed discussion of existing results, a more extensive contextualization in the related literature of sparse estimation with thresholding and refitting, and more convincing, less simplistic experiments to corroborate their claims, e.g., typical high-dimensional sparse applications.

## Minor weaknesses

The second part on minor weaknesses contains straightforwardly actionable items that can potentially be resolved by answering them satisfactorily in the discussion period and including the relevant parts in the paper’s main text, or, by running smaller additional experiments.

1. The clipping step seems to be an important part of LCEN looking at the experimental results. However, in the method’s description and the accompanying algorithm, the cutoff value for hard thresholding is simply taken as a given hyperparameter. Only in line 367 in the experimental section is it mentioned that the cutoff was increased “from the validation-optimal value”. Its choice should be made clearer, since it clearly is not a robust/insensitive hyperparameter, except for cases where the true non-zero coefficients are far away from 0 and the cutoff is near 0. Other works on the thresholded lasso derive concrete values recommended for the cutoff (e.g., Belloni and Chernozhukov, 2013; Zhou, 2023).
2. The paper claims to propose a non-linear method, but this is somewhat misleading. The final result is a model that is linear in its parameters, but non-linear in its features due to the deterministic feature expansion. Their expressivity naturally limits the expressivity of LCEN, so that it might not be well suited for many real-world applications, where no specific polynomial term should be selected as in the physical law experiments. Highlighting better how LCEN is particularly suited for certain kinds of applications where you would expect simple algebraic expressions to occur in the data-generating process could improve the clarity of the exposition. Similarly, it should be highlighted that in general use cases, the complex non-linear feature transformations hinder meaningful interpretability. If more than a handful transformed features are selected, including potentially higher-order interaction terms, polynomial expansions and fixed non-linear transforms.
3. As touched on in the previous point, the paper also claims to yield an interpretable model. However, the interpretability is strongly impaired through the use of the deterministic feature transformations and interaction effects. If the model is not extremely sparse, any meaningful interpretability is quickly lost in the presence of feature transformations such as $\log(X_1)/X_1^2$ or $X_1^3 \cdot X_2^2$.
4. The lengthy and overly detailed description of the results, as well as their repetition in the discussion section, is in large part irrelevant for the general machine learning audience. The results in the main text should be stated concisely, with verbose descriptions of the obtained results and lengthy discussions of these results moved to the appendix.
5. It is odd that the focus of the experiments is often on precise parameter estimation of a sparse subset of transformed features, while using only shrinkage-inducing regularizers at each step of LCEN without an explicit debiasing strategy (e.g., through a final OLS fit), as commonly used for hard thresholded lasso (Zhou, 2023, Meinshausen and Yu, 2009, Belloni and Chernozhukov, 2013).

### Questions
The following list contains both questions (Q) as well as suggestions (S). More questions can be found under “Weaknesses”, points 1, A-D.

1. (Q) The algorithm does not clearly state what is meant by “scaled training data” in line 191. I assume this is supposed to be the scaled expanded data set using the transformation hyperparameters from the lasso step except those transformed features removed by the lasso-clip step? Somewhat confusingly, in the cross-validation part of the EN step, all feature expansions explicitly only happen temporarily and within the loop but not outside of it, so it should be clarified which scaled training data line 191 refers to.
2. (Q) The noise is given as a percentage value (of what?) instead of the standard deviation of the simulated additive noise. The meaning of this percentage should either be clearly stated, or the standard deviation used in this setting simply stated instead.
3. (Q) The term “high hyperparameter variance” is not explained and its meaning is not clear to me. Does it mean “uncertainty about the correct hyperparameter values”?
4. (Q) The caption of Table 4 states that the CV-optimal number of features for FS-GAM was 2 out of 401 features, which oddly results in the highest test RMSE of all FS-GAM models at different sparsity levels displayed in Table 4 (8.32 vs minimum 5.09). This suggests something potentially went wrong in the cross-validation procedure.
5. (S) Using the Boston Housing dataset has been discouraged in the ML community for a few years due to inherent biases in the dataset. It is generally recommended to replace it with, e.g., the California Housing data.
6. (S) The words models and architectures are used interchangeably in the paper. However, methods like lasso or elastic net are usually not referred to as architectures, as this term typically applies to different neural network architectures.
7. (S) The paper contains some claims I find too bold or without the necessary context, e.g., that lasso or elastic net “have poor feature selection” (support recovery) properties, which is at least misleading. 
8. (S) The abstract states that the paper introduces an “algorithm for the creation of nonlinear, interpretable, machine learning models.” This could be understood as if LCEN can transform existing methods into interpretable, non-linear algorithms. Rather, LCEN is a specific algorithm involving an elastic net-regularized linear model with a tuned deterministic set of transformed features determined in the first step.
9. (S) The experiment investigating the effect of multicollinearity on LCEN would benefit from including a direct comparison of the behaviors of plain lasso, to show the stated behavior of selecting only one of the correlated features and how this effect differs from LCEN under different noise levels.
10. (S) The term “y features” appears first without explanation in the main text. It would help highlighting that this is only relevant for the time-series application and may be disregarded otherwise.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents LASSO-Clip-EN(LCEN), a machine learning algorithm designed to generate interpretable, non-linear models. The algorithm begins with LASSO to perform feature selection, retaining only features with coefficients that exceed a defined threshold in the selected model. These filtered features are then used to fit an ElasticNet model, which undergoes a similar thresholding process to retain only significant features. The final model, consisting solely of the ElasticNet, is then used for prediction. The algorithm achieves good RMSE on artificial and real-world datasets.

### Strengths
- The method proposed by the author is simple.
- The empirical results look good in many cases.

### Weaknesses
 - The scope of this paper's contribution is not clearly and correctly defined. The argument the authors made in the abstract "The most commonly used interpretable architectures, such as LASSO or elastic net, are limited to linear predictions and have poor feature selection capabilities" is overly strong. There exists a plethora of interpretable architectures, such as Concept Bottleneck Models [1], Regression/Decision Trees [2], GAMs [3] and so on. These algorithms (as well as their improved versions) can all perform feature selection and non-linear predictions. Furthermore, the authors later acknowledge on lines 44-45 that "nonlinear models may also be made sparse, and even interpretable" and even include a comparison with GAM in their experiments. I believe the statement in the abstract needs to be edited for clarity and correctness.

- Writing of this paper needs to be significantly. Section 2 covers the entire method in just two paragraphs: one paragraph describes the hyperparameters, and the other, spanning 30 lines, explains the entire algorithm. I believe separating these paragraphs into smaller, more consistent pieces could improve the readability. Additionally, the Methods section lacks any discussion on the rationale behind the design choices.

- While the algorithm provided is simple, using LASSO for feature selection itself is not new, as the author has noted in the introduction line 68-98. The method proposed in this work, which is using features selected from LASSO for ElasticNet thus lacks significant originality. The novelty of combining LASSO and Elastic Net is not sufficiently justified, especially given that both methods rely on similar principles of regularization. The paper does not adequately explore why this specific combination is superior to other possible combinations of feature selection and regression techniques. The authors should provide a more in-depth analysis of the theoretical underpinnings and potential benefits of their chosen approach compared to alternatives.

### Questions
- Line 171, how can data be set such that its standard deviation = 0? It seems to be a typo since on line 141-142 the standard deviation is set to 1, instead of 0.

- Given the current formulation of the algorithm, it makes me wonder why the author has chosen to perform the feature selection with LASSO and EN, but not other algorithms such as Ridge Regression and many others. It could easily lead to a family of algorithms that combines the feature selection for multiple algorithms. More explanation and experimental results on the effect of switching underlying algorithm components could be beneficial to this paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the LCEN (LASSO-Clip-EN) algorithm, a novel method for feature selection in nonlinear, interpretable machine learning models. LCEN employs two cross-validation steps: the first determines the complexity of the nonlinear terms, and the second defines the complexity of the final linear model. The authors show that LCEN improves both feature sparsity and accuracy compared to traditional approaches.

### Strengths
The method outperforms the previous paper ALVEN in showing better performance in feature selection and accuracy.

### Weaknesses
*[Poor Organized Introduction and Irrelevant works]* Starting from the first paragraph of the paper, too many concepts are shown all at once: "statistical models", "causal hypothesis," etc. without definitions and without clearly linking them together. There is also weak transformation going from the "statistical models" to "many model architectures". Also, each of the paragraph in the introduction sections is missing a conclusion sentence to give users an idea on what they would like to give out. I am not sure why some of the paragraph are explained within this section: for example, the L_1/group Lasso regularization for neural network and the following methods seems to be a regularization for the complexity of the neural network to me (or in other words, keep the robustness of the neural network by reducing parameters) instead of really doing a feature selection to give out the useful features for the model. I am confused about why those methods should be mentioned here. This also connects to my question about the definition of sparsity here.

*[Missing symbolic regression work reviews]* In the paper, the author mentioned about doing feature expansions to the original features and see how the performance would go by expanding and selecting the most useful features. The key idea for the methodology consists of data expansion and interaction term generations for the model. Therefore, I think the symbolic learning reviews should also be mentioned within the introduction and compared/discussed within the experimental sections since both methods tend to provide non-linear features/relationship for better prediction of the datasets [1, 2] (I just put two papers here, but there are a whole field working on this).

*[Missing the ablation tests for the algorithm]* In the Lasso-Clip-EN, the feature selection can be separated into three steps, and I am not sure how each step would contribute to the model performance, it would be nice to show how each step are contributing to the feature selection process so that the paper would be clearer and more understandable instead of directly explain what the algorithm is.

*[Unfair Comparison between the LCEN and other methods]* In the experiment section, the authors compare LCEN with other non-linear methods or linear methods and prove that it surpasses many other methods. I am not sure it is a fair comparison to compare those methods with the feature selected EN algorithm. For the other linear and non-linear methods, they can also do forward/backward feature selections based on their feature importance in the training dataset so as to get a better performance [3], and make the model more robust (The author have also mentioned stepwise regressions within the related work section), but none of them is discussed within the experiments selection for validations. It seems to unfair to compare a feature selection workflow to the other single machine learning model.

### Questions
*[The definition of Sparsity]* In the second paragraph of the introduction section, the author mentioned that: "It should be noted that nonlinear models may also be made sparse, and even interpretable, as described later in this section and the rest of this work." The definition of sparse here seems not to be clear to me. For the decision trees, it might be the number of leaves, for the additive models, it might be the number of non-zero coefficient terms, and for the non linear models, it is not clear to me what the definition of sparsity here means. Are you referring to the number of non-zero terms or the number of features that is used to construct the model? Different definitions might lead to different conclusions to your model design and experiment analysis. Also, in Table 4, for LCEN, are the feature number be the number of non-zero terms after feature transformation or the number of the original features? In other words, are $x$ and $\log(x)$ considered as two variables or one?

*[The noise level addition]* In the paper, the noise level $\epsilon$ is not clearly defined starting from the second step of the relativistic energy. I am not sure what the noise level is really defined for 20%, what are the real difference for the feature values be when the noise level change from 20% to 30%? Is this noise similar to the experimental error distribution?

*[The definition of interpretability]* In the paper, the author mentioned that the sparsity of the model is leading to a better explanation/interpretability to the model. Here, I would like to asked for a clarification the interpretability of the model since, from my perspective, there are also interactive terms within the model which reduces the explanability of the model, I am worried about when the final equation is given, can it really explain why the equation term should be $x^2 \log x$ instead of $x \log x$? Is there any verification step for those discovered variables? On the other hand, in the LCEN, you will have different cutoff for the feature selection as you have shown in Table 4, how can you determine which cuttoff is the one that the real physics is?

*[Algorithm or Workflow]* The paper title says that it is a novel feature selection algorithm for the machine learning, but in the paper, it is emphasizing that LCEN prediction is showing the lowest MSE, which seems to be the metric for a good predictor. Therefore, I am wondering whether the author is considering LCEN as a feature selection workflow, or a machine learning algorithm? If it is a feature selection workflow, can it be applied to other ML models after the feature is extracted? If it is an ML algorithm for regression and real value prediction, the introduction section seems to be inconsistent since it is focusing on the feature selection techniques comparison.

### Soundness
1

### Presentation
1

### Contribution
2
