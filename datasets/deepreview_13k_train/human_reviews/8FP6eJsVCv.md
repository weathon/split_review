# Explanation Shift: How Did the Distribution Shift Impact the Model?

- Decision: Reject
- Scores: 5, 5, 3, 8

## Abstract
As input data distributions evolve, the predictive performance of machine learning models tends to deteriorate.
In practice, new input data tend to come without target labels. Then, state-of-the-art techniques model input data distributions or model prediction distributions and try to understand issues regarding the interactions between learned models and shifting distributions.
We suggest a novel approach that  models how explanation characteristics shift when affected by distribution shifts.
We find that the modeling of explanation shifts can be a better indicator for detecting out-of-distribution model behaviour than state-of-the-art techniques.
We  analyze different types of distribution shifts using synthetic examples and real-world data sets. We provide an algorithmic method that allows us to inspect the interaction between data set features and learned models and compare them to the state-of-the-art. We release our methods in an open-source Python package, as well as the code used to reproduce our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work proposes a method to detect distribution shifts that matter to a model. The central proposal is to study changes in output of an explanation method (like SHAP) between the shifted datasets. This change is quantified using classifier two-sample test, the output of which is used to detect distribution shifts that matter. Through extensive experiments, the proposed test based on explanation outputs is argued to be more sensitive than multiple baselines.

### Strengths
- Paper is written well with all relevant background explained in main text.
- The idea of detecting relevant distribution shifts through their effect on explanations is original and interesting.
- Work provides intuitive examples to show which distribution shifts can be detected by explanation shifts.
- It tackles a significant problem. Interpretability of distribution shifts, including their effect on model behavior, is an under-studied problem.

### Weaknesses
 - Motivation for considering shifts in explanation is not convincing. This, I believe, is because the goal is not stated concretely to then motivate the solution. The stated goal of investigating interaction between distribution shifts and learned model needs to be further characterized in quantifiable forms. 
I agree that not every type of distribution shifts are important to detect. The ones that change model behaviour in some meaningful way are important. However, it is unclear to me why explanations, that too Shapley values, is a meaningful or useful summary of model behavior to consider. Say, we care about AUC or any metric of choice to summarize model behavior, we can directly detect shifts in this metric using the same classification pipeline as proposed. If the reason for using explanations is for the interpretability of the shift in model behavior, the problem and solution needs to be stated differently.
I think that some of this is addressed in the Appendix by pointing to related work that uses explanations for model debugging, drift detection, or other tasks. This could be used in Introduction to more clearly motivate the approach. 
- Evaluation setup can be improved in terms of quantifying evaluation metrics like sensitivity. 
The magnitude of AUC does not matter that much I believe. Authors are right in asking for sensitivity in the method but it is not directly evaluated. For instance in Figure 2, it is unclear between (ours) and (B7) methods in the left figure and between (ours) and (B2) which one is better. All seem sensitive in the sense that different correlation coefficients result in different AUCs.
- Presentation of experiment can be improved. The case study on ACS data in Sec 5.2.2 is a good place to showcase how the question in the paper title (how the shift impacted the model) is addressed by the method. The findings are stated in a matter-of-fact way. These could be contextualized in the data making the significance of the method and its results more apparent. The questions asked through the experiments could be described at the start of Sec 5 and what we learned from the results could be described more directly at the end of the section.

### Questions
1. Please clarify the problem statement more formally. What aspects of the model behavior under distribution shifts (interaction between distribution shift and learned model) is of interest? 

2. Please motivate the approach (focus on explanations) in terms of the problem statement. How does Shapley values capture the desired aspects of the model behavior?

## Minor (no response is requested)

The success of the method depends on how powerful the classifier in the two-sample test is, since a powerful enough classifier can detect relevant shifts just from a combination of input data and predictions without requiring explanations. Explanation method, in the proposed approach, helps in creating better and more relevant features for use by the classifier. Therefore, consider describing how to choose the classifier and the explanation method.

Explain C2ST (which I believe is classifier two-sample test?) in Experiments on Page 7.

Explain the reasoning for choosing novel group shift in Sec 5.2.1 and discuss the results in more detail.

Geopolitical -> geographical in Section 5.2.2

On the use of Shapley values, the claim that they account for co-variate interactions (compared to univariate tests) depends on the payoff function (interventional vs observational) used in computing Shapley values (reference Kumar et al. 2020 Problems with Shapley-value-based… https://proceedings.mlr.press/v119/kumar20e.html). Discussion in Appendix H could be highlighted in main text.

For completeness, please define the crossed \sim notation. Does this mean that the population-limits of the  empirical distributions are not the same?

The definition of perf(D) is potentially missing a division by number of data points in Sec 2.1.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use distribution shifts in "model explanations" such as Shapley values to attribute/identify distribution shifts across domains. The problem is phrased as that of running two-sample tests/conditional independence tests on explanations generated in the training domain and the target domain. The conditional independence test is operationalized using classifier two sample tests. 

Example cases motivate how univariate (feature-level) two-sample tests will not pick up conditional covariate shifts, and that for an optimally trained model with uninformative features in the training set, a univarite feature-level two sample test will detect distribution shift, while the explanations will not have a shift. 

Other example cases showing that: explanation shift does not always imply a shift in the predictive distribution (this example is not clear to me as terms are not well defined). 

Finally a negative result showing the concept shift cannot be indicated by an explanation shift is presented. 

Empirical evaluation consists of synthetic data analysis: Here, sensitivity of classifier two-sample tests and metrics of evaluating distribution shifts are considered. This evaluation suggests NDCG may be unstable as a test-statistic for evaluating distribution shifts.

Real-world analysis: UCI Adult Income demonstrates AUCs of the two-sample test proposed in the paper with multiple choices of model families used to train the original classifer as well as the explanation classifier. 

Spatio-temporal shifts are evaluated using this data along with interpretation of the linear coefficients of the explanation shift detector model.

### Strengths
1. The overall paper is well written. Understanding how distribution shifts affect ML model performance is important. 

2. The hypothesis that distribution shifts in explanations generated for a model could give a hint about overall distribution shifts and their impact on model performance is a good one and should be explored

### Weaknesses
1. The authors provide some interesting case studies and examples of the utility of Shapley based explanations in identifying distribution shifts. One aspect of this discussion that could be done better is trying to emphasize what additional assumptions could be required so that explanations such as Shapley can indeed be used for detecting, say, concept shift. This is not an impossible task for other methods, see for example: Liu et al [1]. See also experiments in this paper. Specifically, the paper does not clearly articulate the limitations of using Shapley values for concept shift detection, and what specific conditions would be necessary for such an approach to be valid. The discussion should include a more nuanced treatment of when and why explanation shifts might not correspond to concept shifts, and what alternative methods might be more appropriate in those cases.

2. The example on "uninformative features" is valid but unrealistic, shortcut learning is real in ML and hoping a model is trained optimally is kind of unrealistic. Also may be best state explicitly that $X_1 \perp X_2$. The paper should acknowledge that in practice, models often rely on spurious correlations and that the assumption of an optimally trained model is a strong one. This assumption significantly limits the practical applicability of the proposed method. The authors should discuss how the presence of shortcut learning or suboptimal training would affect the validity of their approach. Furthermore, while the independence assumption $X_1 \perp X_2$ is implicit, stating it explicitly would improve clarity.

3. The overall empirical evaluation, in my view is weak. May be at least discuss how general the approach will be (can it be used on other data-modalities, beyond tabular data?) The empirical evaluation is limited to tabular data and does not address the generalizability of the proposed approach to other data modalities such as images or text. The authors should discuss the challenges and potential modifications required to apply their method to these other data types. The current evaluation lacks sufficient breadth to demonstrate the practical utility of the method in diverse real-world scenarios.

### Questions
1. What is $\alpha_i$ in Example 4.3? I am not sure this example is valid based on what I think $\alpha_i$ will be in this example. Can authors clarify?

2. Why aren't methods that don't actually need a causal graph such as [2] compared to in the paper? 

3. In fact it is possible to also compare to other methods of Budhatoki et al, Zhang et al that the authors cite with minimal assumptions that $X \to Y$ or $Y \to X$ to highlight limitations of these methods. 

4. I see a discussion on using LIME as a possible explanation for addressing the same, however, I am not sure whether crucial properties of Shapley are necessary for this method to succeed. I think additional discussion on which explanations have the desirable properties for use in detecting explanation shifts will make the paper stronger. 

[2] Namkoong, Hongseok, and Steve Yadlowsky. "Diagnosing Model Performance Under Distribution Shift." arXiv preprint arXiv:2303.02011 (2023).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors tackle the problem of detecting whether distributions shift between some labelled source dataset and an unlabelled target dataset. In particular, they focus on detecting shifts that affect the behavior of a particular model trained on the source data. Instead of comparing distributions of features directly between source and target, they propose a method based on comparing the distribution of _explanations_ generated using Shapley Values for the given model. This comparison is done using a binary classifier trained to predict the domain from the explanations. They compare their method with a variety of baselines on synthetic and real data, finding that their method has greater sensitivity to data shifts.

### Strengths
- The paper is generally easy to read and well-written.
- The paper provides a nice formulation of the problem.
- The paper tackles an important real-world problem.
- The authors provide theoretical analyses for a few simple synthetic cases.

### Weaknesses
1. I am not convinced that the results demonstrate the empirical superiority of the proposed method relative to the baselines. The authors only compare to the baselines in Figure 2. Here, there are several other methods that are competitive with explanation shift. In addition, the authors do not show confidence intervals in this figure. I also contest that "good indicators should follow a progressive steady positive slope", as if the goal is distribution shift detection, the only thing that should matter is the outcome of the hypothesis test.

2. All of the datasets considered are tabular datasets. How would the authors adapt their method to images (where X could be pixels) and text (where X is a sequence of tokens and f is an LLM)? It seems like Shapley values would be less meaningful and harder to compute in these settings.

3. In the real-world datasets, it is unclear what the ground truth should be, and so it is hard to say whether the proposed method is behaving as intended. For example, how do we know in Section 5.2.2 that the distribution in CA18 is actually different than CA14, in a way that affects model performance?

4. One important aspect of distribution shift detection is to isolate the shift to particular distributions (i.e. particular shifts in Definitions 2.1-2.5). This is underexplored in most of paper. The authors do explore this by examining the feature importances in Section 5.2.2, but this seems quite ad-hoc and should be characterized further. For example, how would this behave theoretically in the covariate shift case in Example 4.1?

5. The authors should consider examining the scenario where the number of samples on the target domain is limited, both empirically and theoretically. How does the power of the two-sample test scale with the number of target domain samples?

6. The authors have missed several important prior works [1-2], which should be baselines.

7. (minor) There are many typos in the paper, including "taks" in Section 4.1, "datasests" in Section 5.1, "Sensitivy" in Figure 2, and an extra bracket in Efficiency Property.

### Questions
Please address the weaknesses above, and the following questions:
1. How does the runtime of the algorithm compare to the baselines? I believe that Shapley values may be time consuming to compute especially when there are a lot of features.

2. Have the authors tried any other tests to distinguish between the two explanation distributions, other than the classifier based approach?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a model for detecting data shift by modeling and quantifying the shift in explanations rather than model performance shift or data distribution shift directly. “Explanations” are defined in terms of a feature-level contribution to the (relative) model output, e.g. Shapley values. The distribution of explanations between the training and the evaluation/new data sets are quantified to get a measure of the explanation shift. The measure of shift is based on a two-sample test where a classifier predicts whether the explanation come from the training or new distribution.

### Strengths
The idea to focus on changes in explanation distribution allows for detecting shift even when there is no effect on model predictions (P(f(D))=P(f(D^{new})), and without making assumption about the type of shift to detect. This formulation allows for detecting covariate, prediction, concept, and novel group shift as long as the explanation values change. 

The above is well supported by experiments of multiple types of shifts and compared to several shift-detecting baselines as well as alternative distributions in the two-sample test. 

Experiments and analytical examples showcase the settings where alternative shift detection approaches fail and explanation shift detection can succeed.

### Weaknesses
Computing explanation vectors with Shapley values limits the number of features that can be considered or, if using TreeShap for efficiency, limits the models that can be used to tree-based. 

Results are sensitive to choice of prediction model and detector model

### Questions
Is there some way to know which predictor and detector model should be used based on prior assumptions about the data itself or the expected shift, if any, that you are trying to detect? Do you have any insights into when different models agree/disagree, for example?

Top of page 8 referencing Figure 4 says the PR18 is the most disparate. Should this be KS18 as it results in the largest AUC for the shift detector? Or what is meant by “disparate” here? Can you comment on the difference between the results shown in Figure 4 and those from Figures 6-8 in Appendix E? It seems employment, travel time, and mobility follow similar patterns, but differ from Figure 4. 


Minor comments  
Is the line for g_\phi=Input, f_\theta=Log missing in Figure 3 middle? Or is it overlapping with the XGBoost line?  

“vii” on page 7 below Figure 2 should be “B7”.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
