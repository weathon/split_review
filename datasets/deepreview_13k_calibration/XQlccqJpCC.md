# Going Beyond Static: Understanding Shifts with Time-Series Attribution

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
Distribution shifts in time-series data are complex due to temporal dependencies, multivariable interactions, and trend changes. 
However, robust methods often rely on structural assumptions that lack thorough empirical validation, limiting their practical applicability. 
In order to support an empirically grounded inductive approach to research, we introduce our Time-Series Shift Attribution (TSSA) framework, which analyzes problem-specific patterns of distribution shifts. Our framework attributes performance degradation from various types of shifts to each *temporal data property* in a detailed manner, supported by theoretical analysis of unbiasedness and asymptotic properties. Empirical studies in real-world healthcare applications highlight how the TSSA framework enhances the understanding of time-series shifts, facilitating reliable model deployment and driving targeted improvements from both algorithmic and data-centric perspectives.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a data-driven framework to mitigate the distribution shift in time series data. The framework is designed based on characterizing metrics for behavioral properties of time series and attributing the performance degradation to those metrics. Paper provides empirical and theoretical analysis of the proposed method.

### Strengths
1) The paper addresses a very important yet underexplored problem. Not many existing works are designed to study and mitigate the distribution shift in time series data, despite the importance of time series models in real-world applications.

2) The paper provides both theoretical and empirical analysis of the proposed method, which makes the model trustworthy and desirable for deployment in real-world applications.

3) The proposed method demonstrates good performance.

### Weaknesses
1) The paper is not well-structured. It introduces many ill-defined concepts, without introducing them or justifying what they mean. For instance, what does the paper mean by "shift within shift"?

2) As a follow up to the previous point, the paper also makes several claims which is not justified throughout the paper. For example, the paper claims the the proposed approach analyzes "application-specific" patterns. However, it is unclear why the proposed metrics are application-specific, as they seem to be mostly focused on general properties of time series.

3) In the first part of the framework, the paper introduces four categories of desiderata for time series metrics and proposed different metrics for each category. It is not clear what are the criteria for selecting metrics in each category? Can different metrics be used?  

4) The contribution of the paper is incremental to some extent, as it is mainly built upon similar frameworks designed for the static setting[1,2].

### Questions
1)  Why is the proposed method based on analyzing "application-specific" patterns? What does the paper mean by "application-specific"?

2) What is the reason behind selecting metrics in each category of desiderata?  Can different metrics be selected?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper builds a distribution shift explainer based on a rigorous Double Robustness estimator, applied to various extracted statistics. They provide theoretical justification of the estimator formulation, and experiments show how causes of shifts can be correctly identified and how the risk regions of the original model can be assessed.

### Strengths
The paper is very clear, with adequate contextualization (with both reference to ML community studies and medicine-focused studies), easy to understand preliminaries and properties, precise experiment protocol and separate experiments takeaways.

The experiments are strong evidences of the method relevance, as correct domain knowledge on well known datasets is infered.

The theory is sound and easy to verify (concise, clear, and refers to the relevant reference).

### Weaknesses
My understanding is that no code was provided for results reproducibility.

Otherwise, I can only say that the weakness of this paper are beyond my abilities to review. The only weakness I could think of would be how much of a strong evidence the risk assessment would be to a medical practitioner. But I do not focus on the medical field, so I cannot be sure if this is an actual limitation.

Wouldn't the shared representation space of the neural network compromise the double robustness by associating estimation of Pi and mu? It is likely that if one is wrong, the other is also due to their association ; hence negating the double robustness benefit. Would it be possible to test the reliability of double robustness in such conditions?

(39) assumes iid data ==> It would be good to make explicit in the main body of the paper the assumption (X,Y) iid. As the work deals with time series, I wasn't sure if repeated measures for a patient, for instance, could be used as several samples. It appears that it is not the case, and should be put in preliminaries paragraph 1.

### Questions
Wouldn't the shared representation space of the neural network compromise the double robustness by associating estimation of Pi and mu? It is likely that if one is wrong, the other is also due to their association ; hence negating the double robustness benefit. Would it be possible to test the reliability of double robustness in such conditions?

(39) assumes iid data ==> It would be good to make explicit in the main body of the paper the assumption (X,Y) iid. As the work deals with time series, I wasn't sure if repeated measures for a patient, for instance, could be used as several samples. It appears that it is not the case, and should be put in preliminaries paragraph 1.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this paper, the authors propose a novel approach, Time-Series Shift Attribution (TSSA), to address distribution shift issues in time-series data. This method is designed to analyze application-specific patterns of distribution shifts. The authors begin by outlining desirable characteristics for time-series metrics, examining factors such as Global Characteristics, Local Dynamics, Structural Changes, and Inter-series Relationships. Following this, they introduce a performance drop attribution strategy based on the Augmented IPW and prove that their estimator is unconfounded, unbiased, and consistent. The paper concludes with case studies that validate the effectiveness of the TSSA approach.

### Strengths
1. The topic is highly relevant to the themes of the ICLR conference.
2. The problem addressed is critical for real-world applications and holds substantial potential for future use.
3. The proposed attribution strategy is intuitive and well-suited to the problem.

### Weaknesses
1. **Insufficient Baseline Comparisons**: The experimental section lacks sufficient baseline comparisons, which would further validate the effectiveness of the proposed approach. Specifically, the paper does not adequately compare against existing time-series shift detection or attribution methods.  A more thorough evaluation should include comparisons with methods that address similar problems, such as domain adaptation techniques for time series or other relevant shift detection algorithms.
2. **Convergence Property**: In optimization, demonstrating uniqueness (and potentially consistency) is often followed by a proof of convergence properties [1]. It appears that convergence analysis is missing in this manuscript. The paper should include a discussion of the convergence properties of the optimization algorithm used, including a proof or at least a detailed analysis of its behavior. This should include considerations of the learning rate, batch size, and other relevant parameters.
3. **Font Size**: Some font sizes in Figure 5 are too small, making the content difficult to read.
4. **Error Bars in Figure 7**: The presentation of Figure 7 is inconsistent with Figures 4 and 5(a), where error bars are provided. Should this discrepancy be addressed?

### Questions
1. Is Equation (21) derived using the tower property?
2. The frequency is involved as discrepancy metric in Section 3.1. Is it justified in the proposed framework. For example, the distribution discussed in this paper is supported on $\mathbb{R}$.

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
The paper presents methods for understanding and attributing predictive performance drops in time series classification models due to temporal data properties.

### Strengths
- The paper gathers and systematizes metrics to attribute performance shifts in time series.
- The paper present four different case studies on clinical scenarios with distribution shifts.
- The paper uses real-world healthcare data with a large patient population.
- The paper discusses methods to identify the specific temporal factors driving prediction error, providing interpretability and guidance for targeted domain adaptation methods.

### Weaknesses
1. Clarity Regarding Prior Work: This paper introduces a Sufficiency Measure and a method for performance drop attribution, claiming to be the first to analyze detailed shift patterns in time-series data. However, distribution shifts in time series are not a new topic. A clearer discussion of prior work, specifically addressing how this study differs from existing approaches, would better position and motivate the contribution. The related work should explicitly address methods that handle non-stationary time series data and not just anomaly detection or static data shifts.

2. Novelty Concerns: The novelty of the methods appears limited. For instance, neither the metrics predicting classification error nor the models used are new. The primary innovation seems to lie in the combined use of these metrics to predict and understand performance drops (i.e., using them as inputs to a model that estimates the prediction error of another model). The non-stationary properties are encoded as static features using summary statistics (e.g., mean, max, slope), which are then used as features to predict the model's prediction error. This approach lacks a clear demonstration of methodological novelty beyond feature engineering. Additionally, the formulation of the attribution problem as an average treatment effect (ATE) estimation problem is concerning. The paper treats aspects of the vitals themselves as “treatments” to predict outcomes that could be defined based on these same vitals, conflating causality and potentially violating key assumptions of causal inference. This requires more discussion and justification.

3. Utility of the Sufficiency Measure: The Sufficiency Measure is introduced to assess the optimal predictive power of the metrics, with empirical studies reporting values of around 0.16 for mean squared error and 0.25 for mean balanced 0-1 loss. This information would be better suited to the results or case study sections. Additionally, it is unclear what constitutes a "good" sufficiency measure. Experiments comparing various sufficiency measures and their ability to identify ‘safe’ and ‘risk’ regions (Case Study 1) would help motivate this proposed measure. The current ablation study on the sufficiency measure only shows a correlation between the number of features and the worst-case accuracy, which is not a standard metric. A more rigorous comparison with traditional metrics is needed.

4. Clarity in Case Studys:
- The case studies lack clear explanations of key methodological details, such as the transformer model architecture, model, hyperparameters, and evaluation metrics. Including summary paragraphs in the Methods section for the patient cohort, models/model training, and evaluation used across all four case studies would enhance clarity.
- Case Study 3: The data partition strategy is unusual, with the validation set (the last 24 hours) occurring temporally after the test set (the first 24 hours). The practicality of this experiment is unclear, given the unrealistic and artificial temporal shift. The rationale for this temporal split is not well-justified, especially given the claim of simulating early diagnosis. It is unclear how a model trained on later-stage data can generalize to earlier-stage data in a realistic setting.

5. Utility of the Approach/Lack of Baselines:
- The lack of baseline comparisons or ablations studies makes it challenging to evaluate the contributions of the proposed methods. The work advocates for identifying specific temporal factors that contribute to performance decline, as opposed to solely applying robust methods or fine-tuning on new test data. However, the results do not compare this approach with other common methods, such as fine-tuning, used to adapt data to new distributions. Including such comparisons would strengthen the motivation for this approach, particularly by illustrating potential computational benefits and performance trade-offs relative to fine-tuning. Additionally, the interpretability of performance drop attribution appears valuable for guiding data reweighting or balancing techniques for certain features (e.g., demographic features in Case Study 2). However, it remains unclear what interventions would be applied to address these temporal factors or whether these identified factors would be deemed clinically useful by experts.

### Questions
Questions:
1. Case Study 2: The authors mention reweighting the data based solely on the inverse density ratio. Which dataset is this applied to? 
2. The paper mentions prior work on performance drop attribution using Shapley values designed for static data (line 127). However, if the temporal properties discussed include summary statistics of a time series, such as mean, variance, or trend, could Shapley values then be used?

Suggestions:
- Clinical expert feedback on the relevance and actionability of identified temporal data properties would help motivate the proposed approach in practice.
- Including distribution plots of the training and test set features could help illustrate the distribution shifts for readers.

### Soundness
3

### Presentation
2

### Contribution
2
