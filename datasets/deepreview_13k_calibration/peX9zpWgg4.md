# Adaptive Shrinkage Estimation for Personalized Deep Kernel Regression in Modeling Brain Trajectories

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Longitudinal biomedical studies track individuals over time to capture dynamics in brain development, disease progression, and treatment effects. Estimating  trajectories of brain measurements in such studies is challenging due to biological variability and inconsistencies in measurement protocols (e.g. MRI scanner variations and upgrades). Herein, we introduce a novel personalized Deep Kernel Regression framework for forecasting longitudinal regional bran volumetric changes. Our approach integrates two key components: a population model that captures brain volume trajectories from a large and diverse cohort, and a personalization step that generates subject-specific models for individual trajectories. To optimally combine these predictive distributions, we propose the Adaptive Posterior Shrinkage Estimation technique, which effectively balances population-level trends with individual-specific data. We evaluate model's performance through predictive accuracy metrics, uncertainty quantification, and validation against external clinical studies. Benchmarking against state-of-the-art statistical and machine learning models—including Linear Mixed Effects models, Generalized Additive Models, and deep learning methods—demonstrates the superior predictive performance of our approach across a variety of experiments. Additionally, we apply our method on predicting trajectories of composite neuroimaging biomarkers, e.g. machine-learning patterns of brain structure related to aging and Alzheimer's Disease,  which highlights the generalizability of our approach to model the progression of longitudinal monotonic biomarkers. Furthermore, validation on three external neuroimaging studies confirms the generalizability and applicability of our method across different clinical contexts. These results highlight the versatility and robustness of our framework for predicting longitudinal brain volume changes. Overall, this framework effectively addresses the inherent challenges in longitudinal biomedical studies, providing a valuable predictive tool that can inform patient management decisions, clinical trial design and treatment effect estimation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new personalized deep kernel regression framework to predict brain volume changes over time. The framework combines a population model, which captures population-level trends in brain volume changes, with a subject-specific model that tailors predictions to each individual subject’s trajectories. The optimal combination coefficient is determined using a shrinkage estimator to achieve the best personalized brain trajectory predictions. The framework is validated through metrics of predictive accuracy, uncertainty quantification, and comparisons with existing statistical and deep learning models, demonstrating superior performance. Additionally, the authors validated the framework's generalizability on brain datasets not seen during training.

### Strengths
- This paper is overall well written and organized; hence it is easy for readers to follow.

- The motivation to develop a more precise predictive tool for diagnosing Alzheimer’s disease (AD) has strong clinical value.

- The proposed method is new in its approach to modeling both population-level and subject-specific brain trajectories. By combining these models to predict personalized brain volume changes over time through adaptive shrinkage estimation in a deep kernel regression framework, the author show a superior performance of the model compared with existing statistical and deep learning approaches.

### Weaknesses
 - While the approach of modeling population-level and individual-level trajectories for brain changes is promising, the current design, which trains these models separately, may be suboptimal. There is substantial research in computational anatomy [e.g., 1-3] demonstrating that individual trajectories should ideally be modeled as a hierarchical structure built upon the population-level mean. This approach naturally captures the hierarchical relationship between fixed group-level information and individual variability.

   [1] Hierarchical linear modeling (HLM) of longitudinal brain structural and cognitive changes in alcohol-dependent individuals during sobriety, 2007.

   [2] A hierarchical geodesic model for diffeomorphic longitudinal shape analysis, 2013.

   [3] Hierarchical multi-geodesic model for longitudinal analysis of temporal trajectories of anatomical shape and covariates, 2019.

- The connection between population-level trends and personalized trajectories in the proposed model is not clearly established.

### Questions
This reviewer is happy to adjust the score if the questions and concerns are well addressed. 

- If an individual ROI differs significantly from the population mean, would it be possible that the optimization of Eq. (17) become biased towards minimizing the error between $y_t$ and $(1-\alpha) y_{st} $, as $y_{st}$ is learned to be fitted to a personalized brain trajectory. In this scenario, the value of $\alpha$ would likely be low if the changes in a particular ROI are subtle or difficult for the network to detect, and vice versa. It would be good if the authors can provide either empirical evidence or theoretical justification on how the model balances between population and individual trends in such cases.

- In Eq. (11), the expectation term appears to be conditioned on the learned latent representation $z_p$ from the population level. However, this condition seems to be missing in the final formulation. Please clarify if this is a typo. 

- Could the authors clarify how the six brain ROIs were selected and extracted from the original images? Additionally, please specify what information about the ROIs is input into the model (e.g., volume, size, or full ROI data).

- It is challenging to well justify the results in Fig. 3. The differences between the population and personalized trajectories may depend heavily on the distribution of training data and examine whether it is biased toward cognitively normal individuals / mild cognitive impairment (MCI) / AD. Each experiment should ideally account for and justify this factor.

- To enhance clarity, it would be helpful if the authors could summarize the other personalized trajectories for each of the six different ROIs in Fig. 3.

- It would be helpful to increase the font size of the legend in Fig. 3.

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
The authors proposed a method to model brain-changing trajectories. The method can capture brain volume trajectories from a large and diverse cohort. They introduced a personalization step that generates subject-specific models for individual trajectories. The paper was well written and easy to follow, although the method and the results were interesting. However, several points are unclear in the manuscript.

### Strengths
The performance of the proposed method was evaluated on different neuroimaging data, which confirmed the generalizability and applicability of the method across different clinical contexts.

### Weaknesses
1. The paper lacks of providing a comprehensive discussion of the wider literature on disease progression modeling. The interpretation of the results from the experiments is inadequate, raising questions about the model’s practical implications. 
2. Adding a clear comparison of the simulation data set will help readers better understand the advantages of the approach. 
3. Interpretation and Presentation of Results: The authors should provide a thorough interpretation of these results and a clearer discussion of the model’s real-world implications and its utility. In particular, the authors should clarify the implications of the findings from the experiment and how the modeling informs participant-level monitoring of disease progression.
4. Context and Literature Review: The authors should expand the context and literature review to properly situate their work within the broader field of disease progression modeling. The discussion should include a comparative analysis with other relevant works.
5. The references in this paper are relatively old. Please add the literature review of the past two years.

### Questions
1. The subject-specific model ss-DKGP also used parameters of the population-level p-DKGP, how to guarantee the correctness of the predicted subject-specific results? If the answer is YES, why do we need to combine the prediction resultes of p-DKGP and ss-DKGP?
2. Expanding on the limitations of existing techniques would strengthen the positioning of your contribution.
3. The description of how external clinical studies were handled in the validation process could be clearer. Were there any preprocessing steps specific to the external datasets, and if so, how might these affect the generalization results?
4. The results demonstrate strong performance, but additional ablation studies would further strengthen the claims of the paper. For instance, how does the model perform when fewer ROIs are considered, or when different biomarkers are used? Additionally, could the method handle non-monotonic biomarkers, or is it limited to monotonic progressions?
5. The evaluation of external datasets is a strong point of the paper. However, it would be useful to see how the model handles missing data in longitudinal studies. What imputation strategies were employed, if any, and how did they impact the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a framework for personalized prediction to forecast longitudinal regional brain volumetric changes. Specifically, the authors provide a pipeline for integrating the population Deep Kernel Gaussian Process (DKGP) and the personalized DKGP by applying the Adaptive Posterior Shrinkage Estimation. The central innovation of this paper is the adaptive shrinkage mechanism, which could dynamically balance predictions from the population (p-DKGP) with the specific models (ss-DKGP) of the subject. Specifically, the authors propose an approach to learn the shrinkage parameter $\alpha$ to weigh the two models (as a linear combination). By combining these two models, this framework could make accurate predictions of brain volumes and could be stably generalized to diverse clinical populations. To sum up, the paper provides a flexible approach to modeling brain volume trajectories, which could offer a lot of potential applications in clinical settings.

### Strengths
1. The logic of the paper is very clear and easy to follow. The paper's structure is well organized. 
2. The combination of population and subject-specific models and its application on data generalization for brain-related disease (AD, brain aging patterns) is a valuable contribution to the existing literature in this field.

### Weaknesses
1. The contributions only have limited novelty. For example, a similar idea has already been proposed by Eleftheriadis et al., 2017. This paper already has a detailed demonstration of how the Gaussian Process can incorporate domain or individual-specific trends in a multi-task setup, which weakens the novelty of the proposed approach. Also, applying the machine learning techniques (like XGBoost) for weight estimation is also a common practice. The learning of the shrinkage parameters $\alpha$ might be a good application in the engineering field but is not a very novel way in ML research. A Bayesian Neural Network or probabilistic models that could provide more principled approaches for weight determination might be a better approach, such as *Weight Uncertainty in Neural Networks* by Blundell et al., 2015.

2. The usage of latent space is very limited. In the current setup, the latent space serves primarily as a way to reduce the dimensionality of the input data and capture basic non-linear interactions through the MLP. However, it doesn’t appear that the authors further analyze or interpret the latent space itself. It would be very interesting if the authors could explore the temporal dynamics and conduct trajectory analysis in the latent space. 

3. In the experiment parts, the authors only compared some very traditional models; it would be much better if the authors could compare their approach with some more advanced deep learning based techniques.

### Questions
1. Could you elaborate on the rationale for freezing the latent transformation (MLP) parameters in the subject-specific model?
2. Did you explore the latent space and do some related analysis, such as subpopulation analysis or clustering of subjects with similar disease/ brain-trajectory patterns? 
3. What is the rationale for the choice of XGBoost to learn the shrinkage parameter $\alpha$? Did you try with other models?
4. How sensitive is the model's performance with different $\alpha$?  Can you provide some exploration of the impact of $\alpha$ on the prediction accuracy? 
4. The proposed model combines the variance of the GPs under the assumption of independence. How do you justify this assumption?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors have developed a deep kernel regression model to predict longitudinal brain volume changes. The model is made for personalised predictions and has two parts, one population model for global prediction and one subject-specific model for personalised predictions. The model is compared to several commonly used models on two open data sets. The resulting models are further evaluated on three external test sets. The results are convincing, and the method appears to work well.

### Strengths
The paper is well-written and in general easy to follow. The method is straight-forward, clear, and appears to work well, and is applied with convincing results to real-world datasets. I really like that you evaluated on multiple external data; this strengthens the confidence in and validity of the results.

### Weaknesses
It is not entirely clear where the methodological novelty lies. Personalised GPs have been proposed before (as mentioned in the introduction) and weighting schemes have also been proposed before (also correctly mentioned in the introduction). The adaptive shrinkage is interesting, and appears to work well, but must also be considered a small contribution.

It is great that the method is evaluated on no less than three external test sets, but it would have been good/more convincing if it was also trained on more than just two training sets. The current training setup limits the generalizability of the learned model, as the population model and adaptive shrinkage are only trained on two datasets, which may not capture the full variability present in other datasets.

There should be an ablation for the personalisation (or, equivalently, presenting results with \alpha=1), to see if it actually improves the results over just having the population level model. Without this ablation, it is difficult to assess the true benefit of the personalized component of the model, and whether it justifies the added complexity. The current results do not clearly demonstrate the added value of the subject-specific adaptation.

There are not confidence intervals in the bar plots, which means it is not possible to compare those results. The lack of confidence intervals makes it hard to determine if the differences between the proposed method and the baselines are statistically significant, or simply due to random variation. The absence of this information limits the conclusions that can be drawn from the results.

There is a discrepancy in the use of \citet and \citep. The authors should use \citet when the author's name is part of the sentence and \citep when the citation is in parenthesis. This inconsistency makes the text less readable and professional.

The step on Line 12 of Algorithm 1 is not atomic. Split this up or explain clearly somewhere what is being done. The current description of the algorithm lacks the necessary detail to be fully reproducible. The lack of formalization in the algorithm makes it difficult to understand the exact steps being performed, and introduces potential ambiguities.

Some more LaTeX-related issues: Remove blank lines after equations to avoid indented sentences after. If an equation ends a sentence, put a full stop after it (or, as in Equation 7, put the comma after the equation, not at the beginning of the next sentence). In general, make equations parts of sentences. There is a lot of space between Equations 6 and 7 and between Equations 11 and 12, probably because of an empty line between them (but do make these equations part of the sentence instead!).

Equation 2: The \Phi has not been defined.

Lines 82-83: These should rather be tuples, and not sets, since the order matters.

Line 163: A \cdot is missing as a wildcard for the first argument.

Line 417: A space missing after the colon.

### Questions
Comments/questions/required changes:
 - How much data from individuals do you need for the personalised GP to be useful/to help in the predictions?
 - The step on Line 12 of Algorithm 1 is not atomic. Split this up or explain clearly somewhere what is being done.
 - It says the values in parentheses in Table 1 are standard deviations. Present the standard errors (standard deviations of the means) instead, so that the results can actually be compared properly.

Minor comments:
 - Do use \citet rather than \cite or \citep when you mention a reference in the body of the text, so that the names are not in parentheses in those cases.
 - Some more LaTeX-related issues: Remove blank lines after equations to avoid indented sentences after. If an equation ends a sentence, put a full stop after it (or, as in Equation 7, put the comma after the equation, not at the beginning of the next sentence). In general, make equations parts of sentences. There is a lot of space between Equations 6 and 7 and between Equations 11 and 12, probably because of an empty line between them (but do make these equations part of the sentence instead!).
 - Equation 2: The \Phi has not been defined.
 - Lines 82-83: These should rather be tuples, and not sets, since the order matters.
 - Line 163: A \cdot is missing as a wildcard for the first argument.
 - Line 417: A space missing after the colon.

### Soundness
3

### Presentation
3

### Contribution
2
