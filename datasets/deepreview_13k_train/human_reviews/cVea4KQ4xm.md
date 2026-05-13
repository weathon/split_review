# Beyond Demographic Parity: Redefining Equal Treatment

- Decision: Reject
- Scores: 6, 3, 5, 8, 3

## Abstract
Liberalism-oriented political philosophy reasons that all individuals should be treated equally independently of their protected characteristics.
Related work in machine learning has translated the concept of \emph{equal treatment} into terms of \emph{equal outcome} and measured it as \emph{demographic parity} (also called \emph{statistical parity}).
Our analysis reveals that the two concepts of equal outcome and equal treatment diverge; therefore, demographic parity does not faithfully represent the notion of \emph{equal treatment}.
We propose a new formalization for equal treatment by (i) considering the influence of feature values on predictions, such as computed by Shapley values decomposing predictions across its features, 
(ii) defining distributions of explanations, and (iii) comparing explanation distributions between populations with different protected characteristics. We show the theoretical properties of our notion of equal treatment and devise a classifier two-sample test based on the AUC of an equal treatment inspector. We study our formalization of equal treatment on synthetic and natural data. We release \texttt{explanationspace}, an open-source Python package with methods and tutorials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an Equal Treatment Inspector that identifies features responsible for the equal treatment fairness violation. 
The authors perform experiments using LIME and Shapley explanation methods and use xgboost for the models and logistic regression for the inspectors.

### Strengths
The authors identify an interesting problem in fair predictive decision-making. 
They propose a feasible solution and perform various experiments. 
In addition, authors operationalize their method, which is rare.

### Weaknesses
Operationalized tool: ``explanationspace `` https://explanationspace.readthedocs.io/en/latest/auditTutorial.html
- I tried out the code, and while I found it impressive, several issues made the test hard.  
  - When I investigated an example: https://explanationspace.readthedocs.io/en/latest/audits.html,  I realized that installing ``explanationspace`` from  https://pypi.org/project/explanationspace/#description was effective whereas the provided step in the installation doc didn't work (https://explanationspace.readthedocs.io/en/latest/installation.html)
  - The Fairness Audits: Equal Treatment example uses ``fairtools. detector import ExplanationAudit``. I couldn't find the documentation for the functions from https://pypi.org/project/FAIRtools, and the described functions directly below the example correspond to ``explanationspace.audits.ExplanationAudit``. I changed other aspects of the code(``from fairtools.detector import ExplanationAudit`` to ``from explanationspace import ExplanationAudit`` and ``detector.fit(X, y, Z="var4")`` to ``detector.fit(X, yu, Z=X["var4"])`` and .get_auc_val() to predict_proba).
- Authors should please improve the documentation in terms of ``all`` the required packages to install (requirements.txt) and the description of results in the tutorial to facilitate easy usage and adoption.  

Paper structuring and related works: 
- While the authors propose an interesting perspective, the paper's structuring makes it hard to appreciate their contributions. The crucial and informative information that could have made the paper stronger is relegated to the appendix. 
For example, the better experiments, presentation, explanation of results, and the description of explanation functions used, among others, are in the appendix. 

- In the introduction and section 2, several introduced ideas are not well connected or explained.  There are so many ideas, it's easy to miss the gist. Additionally, the paper is more oriented towards using explanation methods (SHAP and LIME) to investigate disparities in feature importance across protected groups. However, the authors provide insufficient related work in the area and problem background.  For example, there are lots of similarities between this work and other works; ``Model Explanation Disparities as a Fairness Diagnostic``: https://arxiv.org/pdf/2303.01704.pdf, ``Explanability for fair machine learning``:https://arxiv.org/pdf/2010.07389.pdf.

Methodology
- To me, some proofs and examples seem limited and don't explore corner cases. For example, I think that the statistical independence of Z from the explanation of features is a necessary but not sufficient condition for the statistical independence of the model from Z. Additionally, in example 4.3, feature X_{3} not being statistically independent of Z and the function being a linear model makes it easy to do the proof through zeroing out that features.  In most cases, the function/model might not be linear, and the relationship between features might be complex and causal graphs hard to uncover. It seems like maybe the tool being diagnostic instead of a fixture might be a better point of view. 
- Given that one might not have access to test data, would it be better to apply the ET inspector as a diagnostic on the train/val data instead? 

Discussion and Experiments in the main body
- It's hard to appreciate authors' experiments and results because of the following reasons; 
  - The experiment setup of 3 features and one with varied dependence on Z makes it hard to appreciate the author's contributions.
  - The authors don't provide sufficient explanations or discussion of the results.
  - Authors could have compared their experimental results to other related works and shown the impact on ET inspector and explanations on fairness on the different groups (something similar to table 5 in the appendix). 

Minor or okay to address later
- Having an algorithm or bulleted procedure could have improved readability.
- For novelty, authors use AUC rather than accuracy in their C2ST instead of accuracy as previously done.  This is a bit of a tradeoff, and while the scale invariance might be good, it is damaging when inspecting other cases of fairness where one might, for example care more about false positives than false negatives. 
- Given the importance of understanding the features of fairness, I think it might be important to distinguish between protected and sensitive attributes.  Not all protected features are sensitive attributes. For example, gender plays a key role in admission to single-sex schools, or age plays a crucial role in admission to age-range sports or activities. 
- Reliance on Z as a binary variable is restrictive, especially since there are lots of intersectionalities. 
- The explanation highly relies on f_{\theta}. It might be informative to also look at features independent of the model.

### Questions
While the proposed method has several similarities with ``Explanability for fair machine learning`` and ``Model Explanation Disparities as a Fairness Diagnostic`` papers, operationalizing their model has positively influenced my score.  
However, issues in the writeup and code documentation negatively influenced my score. Authors should please address these issues in the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper highlights the issue with current fairness notions, which emphasize equal outcomes rather than equal treatment. The philosophical definition of fairness aligns more closely with the principle of equal treatment. The paper delves into the theoretical relationship between equal treatment and equal outcomes and introduces a methodology for assessing equal treatment.

### Strengths
High-level Idea is simple and intuitive.

### Weaknesses
 - [Major] I remain unconvinced that 'equal treatment' is a superior notion of fairness. The paper advocates for the use of Shapley values to distribute explanations when defining equal treatment. However, the rationale for this preference is unclear to me. A notable limitation of this fairness notion is its potential indirect correlation with protected attributes like Z. For example, height is often closely associated with gender. Therefore, a model's Shapley values may not depend on the protected attribute Z and might predominantly base predictions on height equally across different gender groups, which superficially appears gender-neutral and meets the paper's fairness criteria, yet it may still result in substantial unfairness. I welcome corrections if my understanding of Shapley values is inaccurate.
- [Major] The paper omits a critical discussion on related work. There appears to be a study, specifically on individual fairness [1], that resonates with the motivations of this paper. Individual fairness emphasizes that individuals with similar backgrounds (e.g., salary, job status) should receive similar treatment. However, this paper does not draw any comparisons with its own concept of fairness to that of individual fairness.
- [Medium] The motivation presented within the paper is somewhat unclear, and it is concerning that significant discussions related to the work are relegated to the appendix. This decision diminishes the visibility and importance of such discussions.
- [Medium] I cannot agree with the authors that equal opportunity could lead to reverse discrimination and overcorrection. As far as I know, equal opportunity is proposed to address these limitations you mentioned which suffered by demographic parity. Can you cite the corresponding works that draw this conclusion?
- [Medium] Although Shapley values are central to defining 'equal treatment', they are introduced late in the appendix. It is my suggestion that the authors reconsider the organization of the paper, as many pivotal elements seem to be understated by their placement in the appendix.

### Questions
See the weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper questions the traditional approach of equal outcome and demographic parity as a measure of fairness and proposes a new formalization for equal treatment. The authors measure equal treatment by accounting for the influence of feature values on model predictions. They formalize equal treatment by considering the distributions of explanations and comparing them between populations with different protected features. The paper proposes a classifier two-sample test based on the AUC (Area Under the Curve) of an equal treatment inspector, which compare the degree of equal treatment between different groups. The application on synthetic and real datasets show that this new equal treatment definition might actually yield higher AUCs for downstream classifiers than when using demographic parity.

### Strengths
- The paper is well-written and well-structured.
- It appears to be the first clear attempt to connect explanations with algorithmic fairness through the introduction of the new "equal treatment" definition. While other approaches have used explainability as a proxy for fairness, none have established such strong foundations as presented by the authors.
- The examples with simple linear models effectively illustrate potential impacts and counterexamples.
- The experiments provide compelling evidence of the potential implications of this novel "equal treatment" definition.

### Weaknesses
The main weaknesses I can observe are (a) practical implications of the new equal treatment definition and (b) the novelty and implication of using a classifier-two-sample test.

(a) I agree with the authors that in the case of exact demographic parity (independence), then this definition of equal treatment works (Lemma 4.2). However, my concerns arise in cases where the demographic parity is violated only by a small amount, which is the case in practice; no (useful) algorithm has a demographic parity of exactly zero, and most of the decision making algorithms usually have a small violation tolerance. Can the authors comment how equal treatment can be used on bounding demographic parity, or whether there exists any relationship there? This scenario is important for e.g., credit lending scenarios; in the U.S., the Equal Credit Opportunity Act [2] enforces no discrimination *on the outcomes* of the decision-making algorithm. From a law standpoint, one might not necessarily mind different explanations as long as the outcomes are not too dissimilar (i.e., low demographic parity).

(b) First of all, unfortunately using AUC as a test statistic for classifier-two-sample test is not novel, see [1] for example (the good thing is that AUC is a relatively well behaved statistic, so that does not change the framework). By using a C2ST in the framework, we introduce (i) a data-driven algorithm to judge the level of equal treatment in the data but also (ii) an additional notion of uncertainty in our fairness definition. For (i), in practice this means that this approach is not necessarily low-sample-size friendly (as it does not use permutations), the complexity of the classifier directly affects type I and type II error and results may vary considerably according to which classifier is chosen (which the authors have actually explored in the Appendix). For (ii), we are rejecting the null-hypothesis with a certain probability threshold, as opposed to provide a single (deterministic) number as in demographic parity. That is, we are now guaranteeing that "up to a level 1-\alpha" the algorithm is providing equal treatment. Citing again the equal credit opportunity act of 1961, such a definition of fairness would not be admissible in a credit lending scenario, which puts into question once again the practical feasibility of this new definition of equal treatment.

[1] Model-independent detection of new physics signals using interpretable SemiSupervised classifier tests, Chakravarti, Purvasha and Kuusela, Mikael and Lei, Jing and Wasserman, Larry, The Annals of Applied Statistics, 2023
[2] https://www.justice.gov/crt/equal-credit-opportunity-act-3#:~:text=prohibits%20creditors%20from%20discriminating%20against,under%20the%20Consumer%20Credit%20Protection

### Questions
I have included two points in the "Weaknesses" section above, so I'd be grateful if the authors would post their comments to those.

Minor points:
- The word "natural data" sounds a bit weird, as usually the machine learning community uses "real data".
- Figure 2 is a bit too small overall, increase the font size and marker size would go a long way.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new fairness definition motivated by the pursuit of equal treatment. The authors first showed that it is insufficient to use statistical measures of equal outcome, e.g. demographic parity, to evaluate equal treatment. They then defined Equal Treatment (ET) as requiring indistinguishable explanation distribution for the non-protected features between populations with different protected features. The explanation distribution relies on an explanation function, for which Shapley value is used as the example in the paper, to quantity how non-protected features affect the trained model. Based on the new ET definition, they also designed a Classifier Two Sample Test (C2ST) to test whether a ML model provides equal treatment based on the AUC of the model. In numerical experiments, the authors demonstrated that the new ET definition is more effective at inspecting treatment equality in a model, and their method could provide explanation for the underlying causes of treatment inequality.

### Strengths
The proposed Equal Treatment is a novel method that combines fairness and explainability. These two goals are both important components in the broad domain of ethical machine learning, and they are typically studied separately. The Equal Treatment Inspector workflow from this paper examines both issues and can answer the useful question of what causes unfairness. 

The paper is well-written and follows a well-thought-out flow. The examples provided throughout the paper are helpful for understanding the concept. The related works (majority in appendix) are thoroughly reviewed to help position the paper in literature.

### Weaknesses
I disagree with some statements that the paper used to motivate the research question. For example, the abstract states “Related work in machine learning has translated the concept of equal treatment into terms of equal outcome and measured it as demographic parity (also called statistical parity)”. To my understanding, it is well-recognized in the fair ML literature that equal treatment and equal outcome are different concepts. While I agree that equal outcome is often measured with statistical measures, I think it is inaccurate to frame equal outcome as a convenient proxy of equal treatment. Instead, one simplified interpretation of equal treatment is “fairness through unawareness” or “colorblindness”. Rather than relying on the distinction between ‘equal outcome vs. equal treatment’, which can refer to much more high-level philosophical differences than what is captured in this paper, I would find it clearer to simply focus on equal treatment (new definition) vs. demographic parity.

I also have concerns about the practical application of the theoretical analysis. The theoretical analysis in Section 4 relies on the assumption that exact Shapley values are available. This assumption is not realistic in most real-world scenarios, where we deal with non-IID data and non-linear models. The computation of exact Shapley values is often intractable in these cases, and approximations are necessary. The paper does not discuss how the theoretical results would be affected by the use of approximate Shapley values, which is a critical point for the practical applicability of the proposed method.

Finally, while the paper mentions LIME as another explanation function, it does not fully explore the space of potential explanation functions. The choice of explanation function is crucial, as it directly impacts the definition of Equal Treatment. The paper does not provide sufficient guidance on how to select the most appropriate explanation function for a given task, nor does it discuss the potential limitations or biases that different explanation functions might introduce. The discussion of alternative explanation functions is limited to a brief mention in the appendix, which is insufficient given its importance.

### Questions
1.	In Section 4, the theoretical analysis relies on assuming exact calculations of Shapley value are available. How realistic is this assumption in practice? When we do not have access to exact Shapley values, how will the theoretical results be affected?

2.	What are other explanation functions that can be used in the framework? In the appendix, another example is given, but I wonder is there a large set of options or is designing an effective explanation function an open question itself? If there are multiple candidate explanation functions, what makes one function better than another?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new notion of equal treatment (ET) which requires the model’s explanations to be independent from the sensitive attribute, as opposed to the demographic parity (DP) that require the independence of model prediction and sensitive attribute. Given the proposed notion, the paper first explores the relation between ET and DP, and then proposes a method to inspect ET via statistical independence test.  Such an inspector may further help interpret the sources of unequal treatment.

### Strengths
1. Inspecting whether a model violates fairness and explaining the sources that cause unfairness is an important and interesting problem. 
2. The paper proposed a new notion of fairness based on explanation distribution, which is novel to the best of my knowledge. 
3. The paper validates the proposed inspector on both synthetic and real data.

### Weaknesses
1. The main concern I had was the novelty of the paper, which I think is not sufficient. Specifically, using model attribution methods such as Shapley values to interpret model unfairness has been explored in prior works; the idea of using the two-sample test to examine the independence of two sets of variables has also been studied. While the settings are not the same, the techniques are somehow similar. The paper does not adequately differentiate its approach from existing methods that use similar techniques for fairness analysis, particularly in how it leverages explanation methods and statistical tests.
2. Because the notion of equal treatment is strictly stronger than the demographic fairness notion, it can be much more challenging to attain ET in practice than DP. Moreover, the trade-off between fairness and accuracy may make ET less suitable for real applications. While the paper has compared the two notions, it is still not convincing why equal treatment is a superior notion. It is helpful if authors can provide more justification with a real example. The paper needs to provide a more compelling argument for why the stricter equal treatment is necessary, especially given the potential for reduced model performance and the practical difficulties in achieving it. A real-world example would be beneficial to illustrate the limitations of demographic parity and the necessity of equal treatment.
3. While the settings with non-linear models and non-i.i.d. data are considered in experiments, most theoretical results and illustrating examples are limited to linear models and i.i.d. data. Moreover, the synthetic data used in the evaluation is also very simple: logistic model with Gaussian distributed data. The theoretical analysis and illustrative examples should be expanded to cover more complex scenarios, including non-linear models and non-i.i.d. data. The current reliance on linear models and simple synthetic data limits the generalizability of the findings.
4. The paper is not using the ICLR template.

### Questions
1. It seems that the sources of unequal treatment can only be explained for linear models (as illustrated in Example 4.4 and Figure 3). How can the method be generalized to non-linear cases? 
2. Since ET can be much more difficult to achieve, can you provide a real example to illustrate why equal treatment is a more appropriate notion than demographic parity?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
