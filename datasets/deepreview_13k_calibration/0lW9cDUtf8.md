# FairReweighing: density estimation-based reweighing framework for improving separation in fair regression

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
There has been a prevalence of implementing machine learning technologies in both high-stakes public-sector and industrial contexts. However, the lack of transparency in these algorithmic solutions has raised concerns over whether these data-informed decisions secure fairness against people from all racial, gender, or age groups. Despite the extensive research and work that emerged on fairness-aware machine learning, up till now, most efforts on solving this issue have been dedicated to binary classification tasks. In this work, we propose a density estimation-based pre-processing algorithm to train regression models satisfying the separation criterion $\hat{Y} \perp A \mid Y$. Evaluated by the ratio estimation of separation via probabilistic classification on both synthetic and real world data, we show that the proposed algorithm outperforms existing state-of-the-art regression fairness solutions in terms of maintaining high predicting accuracy while improving separation in fair regression.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposes a density estimation-based preprocessing algorithm to train regression models, with the goal of reducing the bias of the original data before the entire training process. This method is more efficient and has lower overhead. This method has no parameters and can be automatically tuned to achieve a balance between all specified protected attributes. The experimental results also indicate that the algorithm proposed by the author improves separation in fair regression while maintaining high prediction accuracy, and its performance is superior to the most advanced existing schemes.

### Strengths
The paper includes a comprehensive summary of related work. The ideas of the paper are clearly presented. The author proposes a universal preprocessing framework, which is a training framework based on density estimation. By adjusting the impact of each data item through weight allocation to achieve fairness, classification and regression models can be effectively trained. This article extends the fairness issue in classification problems to regression problems based on previous studies.

### Weaknesses
Lack of analysis on the robustness and stability of the algorithm: The paper did not analyze the robustness and stability of the algorithm. In practical applications, algorithms need to be able to handle various uncertainties and noise while maintaining stable performance. The analysis of the robustness and stability of algorithms can provide a more comprehensive evaluation.

1. The paper did not provide specific details and implementation methods for the kernel density estimation algorithm and lacked transparency in the algorithm to verify its effectiveness.
2. Lack of comparison with other methods: There are relatively few existing classification fairness methods in the paper, making it difficult to determine the advantages and disadvantages of this method in classification tasks.
3. The paper mentioned some fairness measures but did not provide a detailed discussion on the selection and applicability of these measures. The selection of fairness measures is crucial for evaluating the fairness of algorithms and requires more in-depth discussion and explanation.
4. The paper provides evaluation results for both synthetic and real-world data but does not provide validation for practical application scenarios. The data in practical application scenarios may be more complex and diverse and is the weight allocation method proposed in the paper still effective in improving fairness.

### Questions
1. The paper did not provide specific details and implementation methods for the kernel density estimation algorithm and lacked transparency in the algorithm to verify its effectiveness.
2. Lack of comparison with other methods: There are relatively few existing classification fairness methods in the paper, making it difficult to determine the advantages and disadvantages of this method in classification tasks.
3. The paper mentioned some fairness measures but did not provide a detailed discussion on the selection and applicability of these measures. The selection of fairness measures is crucial for evaluating the fairness of algorithms and requires more in-depth discussion and explanation.
4. The paper provides evaluation results for both synthetic and real-world data but does not provide validation for practical application scenarios. The data in practical application scenarios may be more complex and diverse and is the weight allocation method proposed in the paper still effective in improving fairness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors describe a technique for achieving group fairness in regression tasks. Their approach is a simple preprocessing technique that weights samples based on the observed joint distribution of protected attributes and the target variable, in order to nudge the model trained on the weighted dataset towards satisfying the standard separation fairness constraint $\hat{Y} \perp A \mid Y$, where $A$ is the protected attribute, $Y$ the target variable, and $\hat{Y}$ the model's prediction. In several simple tabular test cases, the proposed method compares favorably with other fair regression techniques.

### Strengths
Regression fairness has received only negligible attention compared to classification fairness, and any progress on this important topic is highly welcome. The presented approach is very straightforward - that being a good thing -, easy to implement, and very general and widely applicable to all kinds of models and training schemes. The paper is well-written and easy to read.

### Weaknesses
As outlined above, I consider the topic important and the solution proposed by the authors straightforward and generally promising. I do, however, sadly see quite a few significant weaknesses in the present manuscript.

Firstly, I am honestly quite confused about what it is that the authors actually implemented, and how that matches the textual description. Sections 1 and 2 suggest strongly that the authors implement a scheme to achieve separation, i.e., $\hat{Y} \perp A \mid Y$. However, the weighting scheme (section 3) seems to me to be constructed such that $p(y \mid a_1) = p(y \mid a_2)  \forall y$ - which has nothing to do with separation (note that the algorithm's predictions do not even occur) and, instead, creates a synthetic (reweighted) dataset that fulfills *demographic (or statistical) parity*, i.e., $Y \perp A$? It is completely unclear to me how this would help achieve separation for the classifier trained on such a reweighted dataset. (Note that, in any case, reweighting a training set, while possibly empirically useful, can never provide any *guarantees* about the resulting classifier having a certain property.) The authors should clearly state how the proposed reweighting scheme relates to the separation notion of fairness. Furthermore, a more rigorous explanation of how the weighting scheme affects the conditional probabilities and the resulting model predictions is needed.

Secondly, it might have been easier for me to infer what the method is actually doing if the experimental results were analyzed more comprehensively and the experiments and metrics better described. How do the trained models perform on the two protected groups separately in all of the experiments? What are the "Convex", "AOD" and "DP" metrics? (I am sure the latter is a demographic parity-related metric, but how exactly is this computed?) Why is R-Squared so abysmally low in the Law School dataset; are these all typos? What are the base rates $p(y \mid a)$ and TPR/FPR in the classification test cases? What are the actual regression models being fit; is it linear regression? Also, for the classification cases, standard equalized odds / equal opportunity classification fairness techniques as per Hardt. et al. should be included as baselines. The authors need to provide a much more detailed description of their experimental setup, including precise definitions of all evaluation metrics and a more thorough analysis of the results for each protected group.

Thirdly, there are various statements throughout the manuscript that convey a shallow conception of "fairness" and "bias". To provide a few specific examples:
- "Separation [...] promises that a perfect predictor will always be considered the most unbiased." Separation doesn't "promise" anything. Also, "perfect" predictors can be completely biased if the target variable is noisy or biased, the dataset suffers from sampling biases, etc. Cf. e.g. Petersen et al. [6] for a recent discussion of these issues.
- "The underlying assumption is that the unfairness we observed in machine learning models already includes discrimination rooted in training data." While data is an important source of bias, it is not the only one. Cf. e.g. Hooker [4] and Hall et al. [3]
- "To ensure a dataset is unbiased, the sensitive characteristics A have to be statistically independent of the ground-truth label Y. [...] Such discrepancies would lead to a biased regressor or classifier." Again, this describes a notion of statistical / demographic parity on the dataset level, not separation. Is a breast cancer dataset in which women have breast cancer more often than men "biased"? And, equivalently, is a classifier which predicts breast cancer more often for women than for men "biased"?

The authors should revise these statements to reflect a more nuanced understanding of fairness and bias in machine learning.

Fourthly, given that this is an immediate application of widely used standard techniques, the discussion of and references to prior relevant work are quite sparse.
- Weighting and over/undersampling techniques are widely used throughout the algorithmic fairness literature, see e.g. Caton and Haas [2].
- This is essentially an application of covariate shift adaptation techniques as per Sugiyama et al., with the "target population" being the one where a desired notion of group fairness is satisfied.
- While prior work on fair regression is discussed quite well, there are a few further methods that might be relevant to mention, such as Komiyama et al. [5] and Calders et al. [1]. In particular Calders et al. [1] use a propensity score-based approach, which is very closely related to what the authors are describing here; the differences should be spelled out clearly.

### Questions
- The authors correctly point out that direct density estimation is known to be more efficient than estimating the two likelihoods separately (a reference on this statement would also be appropriate) - and then they proceed to estimate the two likelihoods separately and do *not* do direct density estimation?
- I believe Eq. (4) is missing an expectation? (Currently, it does not evaluate to a number.)
- I believe in Eq. (7), the ratio is inverted compared to Eq. (4)?
- Which of the two discussed density approximation methods is used for the results in Fig. 1, and for the further results? Also, "this suggests that our methods can correctly estimate the density of any given variable" is a very strong claim given that the method was evaluated on exactly one very simple test case.
- What is "Models = Ground Truth" in Table 1?
- I assume the tau in all tables should be a tauhat?
- Where can I find the results for the described experiments with continuous protected attributes?
- The authors write that "FairReweighting" is "essentially equivalent" to the previously proposed Reweighting method - isn't it precisely, mathematically, identical?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper considers the fairness criterion known as separation in the regression setting.  It proposes using KDE to audit/measure the violation of separation from finite samples (recall that separation involves conditioning on $Y\in\mathbb R$, whose values may be unique in a given samples).  Then, it extends the instance reweighting technique previously proposed for achieving fairness in the classification setting to regression, also via KDE (the author also consider binning and radius neighbors).

### Strengths
- The motivation is clear, and the criterion of separation in regression problem receives relatively less attention in the fairness literature.
- The presented material is clear and easy-to-follow.

### Weaknesses
1. This paper uses KDE to deal with difficulties in using finite samples to achieve fairness, but does not provide any analysis for the proposed procedures for auditing and bias mitigation.

	- What is the convergence rate of $\hat r_\mathrm{sep}$ to $r_\mathrm{sep}$ (eqs. 4 and 7)?
	- Similarly, what is the convergence rate of $\widehat W(A,Y)$ to $W(A,Y)$ (eq. 9), when estimated and inferred from finite samples using KDE/radius neighbors/binning?  Specifically, how does the choice of bandwidth for KDE, the radius for radius neighbors, or the bin size for binning affect the convergence rate and the resulting fairness metric?  The paper lacks any discussion on the sensitivity of these hyper-parameters, which are critical for the practical application of the proposed method.

2. Although an intuition is provided for the proposed FairReweighting procedure (in paragraphs surrounding eq. 8), critically, no proof or guarantees is provided for it.  Why should I trust that a regressor trained using FairReweighting would satisfy separation?

	- Under what assumptions would a regressor trained using FairReweighting satisfy separation?  Beyond toy examples?  Would it depend on the capacity/expressiveness of the regressor, or the optimization algorithm? For instance, if the regressor is a highly expressive model, it might simply memorize the training data and not generalize the desired fairness property. The paper should provide theoretical justification for the effectiveness of the proposed reweighting scheme under specific conditions.
	- It is known that overparameterized neural networks can fit arbitrary training examples, and the effects of instance reweighting is empirically observed to be weakened [1].  Would the proposed procedure still work?  The paper should address the potential limitations of the proposed method when used with overparameterized models.
	- Is there a tradeoff between performance and fairness?  Such tradeoffs have been observed in fair classification via reweighting [2]. The paper needs to investigate and quantify this trade-off in the regression setting.  How does the choice of reweighting method (KDE, radius neighbors, binning) affect this trade-off?
	- I expect some theorem upper bounding $r_\mathrm{sep}$ of regressors trained using the FairReweighting procedure, likely involving the complexity of the regressor and the number of samples.  Without such a guarantee, the practical utility of the method is questionable.

3. Claims that the proposed FairReweighting is "free of parameters and tuned automatically" are wrong.  KDE involves specifying the variance of the Gaussian bumps, and radius neighbors needs to provide the radius and metric. These are crucial parameters that significantly affect the performance of the method and require careful tuning. The paper should acknowledge this and provide guidance on how to choose these parameters effectively.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a bias mitigation method called FairReweighing for regression tasks. FairReweighing extends the preprocessing approach by Kamiran & Calders for classification to also work for regression by using k-nearest neigbors or kernel density estimation instead of frequenty counting to estimate density. Experiments show that model trained after using FairReweighing are significantly less biased.

### Strengths
* Unfairness mitigation for regression is indeed relatively understudied.
* The fair reweighing extension seems simple and practical.

### Weaknesses
 * The technical contribution seems marginal. The core issue seems to be how to estimate density. Compared to a classification setup where we can use frequency counts, the idea is to use k-nearest neighbors or kernel density estimation instead for regression. This looks like a straightforward generalization of Kamiran & Calders, but not substantial enough for a full paper.

* It is not clear why RQ2 is important. FairReweighing's goal is to improve fairness for regression, so why is it critical to validate its performance on classification problems? Instead, there should be other important research questions regarding regression. For example, how does pre-processing approaches compare to or complement in-processing approaches? How efficient is the unfairness mitigation? And so on. 

* It is not clear why the inconsistency in (8) leads to unfairness as described in the paper. The authors say that the model would "prioritize these data points and produce more accurate predictions while disregarding" the other examples, but there does not seem to be any theoretical or empirical evidence. Therefore, it is difficult to understand why the weighting in (9) solves the problem.

* Satisfying a single fairness measure seems a bit limited, and the contributions would be stronger if other fairness measures in the literature proposed by Jiang et al. (2022) and Narasimhan et al. (2020) are also supported.

* It is not clear how accurate the approximation in (7) is. 

* In Section 4.1.1, concluding that the density estimation approximation is accurate only based on synthetic data is not convincing.

* In Sections 4.1.2 and 4.2, only using two real datasets for the performance comparisons does not seem extensive enough.

### Questions
Same as the weak points above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor
