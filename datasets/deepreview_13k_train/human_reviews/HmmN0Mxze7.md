# Temporal Visiting-Monitoring Feature Interaction Learning for Modelling Structured Electronic Health Records

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Electronic health records (EHRs) contain patients’ longitudinal visit records, and modelling EHRs can be applied to various clinical prediction tasks. Previous works primarily focus on visit sequences and perform feature interaction on visit-level data to capture patient states. Nonetheless, incorporating finer-grained monitoring sequences simultaneously in structured EHRs, where each visit involves multiple monitoring sessions, can improve prediction performance. However, these studies have not accounted for the relationships between visit-level and monitoring-level data. To fill this gap, we propose an EHRs modelling method aimed at modelling the dynamic interaction between visit-level and monitoring-level data and capturing finer-grained health trends. We first capture the dynamic influence between medical data, and then perform a visiting-monitoring feature interaction on the relationships between visit data and monitoring data, to obtain the representation of patients' state for clinical prediction. We conducted extensive experiments on disease prediction and drug recommendation tasks, with MIMIC-III and MIMIC-IV datasets, demonstrating that our method outperforms state-of-the-art models significantly.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method (CrossMed) to model visit-level and finer-grained monitoring-level EHR data simultaneously. 
The method first builds a cross-level interaction temporal graph for each visit at monitoring-level. 
A temporal network then aggregates the temporal graph into a visit embedding for further downstream tasks.
Evaluation on disease prediction and drug recommendation tasks shows that CrossMed outperforms current state-of-the-art models.

### Strengths
The proposed approach is able to integrate both visit-level and monitoring-level data in EHRs, which allows it to capture finer-grained health trends.

The authors demonstrate the effectiveness of the proposed modules through several ablation studies.

### Weaknesses
The size of the temporal graph could become large if there are many monitoring sessions during a single visit, which would significantly increase the computational cost.

Some parts of the proposed model are not well-introduced or the explanation is unclear, making this paper somewhat hard to follow.
For example, the visit-to-patient stage is also not well explained in the main text. 
It is unclear how the patient representation and visit representation are combined.
These details are important to understand how the authors derive the final patient representation $h_H$.
I would suggest including the content in Appendix B.4 in the main text and elaborating on it in more detail.

It seems that in the cross-level interaction temporal graph, all monitoring event-disease pairs are the same, represented by the aggregate value generated from the relationship discovery module. 
Why not use the unaggregated values to give different monitoring event-disease pairs different weights? (same question for m-P and m-R pairs)

### Questions
It seems that in the cross-level interaction temporal graph, all monitoring event-disease pairs are the same, represented by the aggregate value generated from the relationship discovery module. 
Why not use the unaggregated values to give different monitoring event-disease pairs different weights? (same question for m-P and m-R pairs) 

How do the authors choose $\alpha$ as mentioned in Eq 3? Is $z_i$ in Eq 4 a trainable parameter, or is it a fixed value?

What does the "temporal recurrent component in feature interaction" refer to in the ablation study? Does it refer to the GRU structure used to aggregate $h_vt$ or the feature interaction on cross-time edges.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the authors propose an EHR modeling method focusing on utilizing multi-level interactions. The experiments are conducted using MIMIC-III and IV datasets with two tasks.

### Strengths
The paper is well-written, and the experiments are comprehensive.

### Weaknesses
My major comments are:

1. The current methodology contribution and insights are somewhat incremental. Multi-level EHR data modeling is not a new topic; for example, [1] and some of its subsequent works are not discussed in this paper.
[1] MiME: Multilevel Medical Embedding of Electronic Health Records for Predictive Healthcare

2. What are the causal assumptions in this work? Why are there only responses from visit to monitoring events? What outcomes are used as targets, and what features are used as confounders? How are such causal assumptions proposed?

3. Can the dataset reflect the insights? MIMIC-III and MIMIC-IV are ICU datasets. The monitoring events are within each ICU stay. Do the monitoring events in one ICU stay affect the next visit?

4. Some experiment results are very close. P-values should be reported.

5. The major contribution of this work is about cross-level interactions. However, the authors did not provide any analysis of the interaction results. The information in the t-SNE plot is not straightforward. Why does sparser indicate better results? I would assume forming subclusters is more useful in practice. Besides, the difference in the patient representation plot looks the same to me.

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces CrossMed, a method for modeling EHRs that enhances disease prediction and drug recommendation by integrating both visit-level and monitoring-level data, and they claim incorporating finer-grained monitoring sequences simultaneously in structured EHRs, where each visit involves multiple monitoring sessions, can improve prediction performance. CrossMed’s cross-level feature interaction approach captures dynamic patient health trends. it is tested on MIMIC-III and MIMIC-IV datasets for both diagnosis prediction and drug recommendations.

### Strengths
1. One of the few papers focusing on combining visit-level EHR discrete code sequence data with continuous monitoring measurements, providing a finer-grained view of a patient's medical information.
2. Comprehensive experimentation on both diagnosis prediction and drug recommendation tasks.

### Weaknesses
1. The explanation of "monitoring data" is unclear. It mentions “monitoring-level events, such as lab test results reflecting the patient’s health state.” Are these continuous signals like ECG (time series), imaging data like MRI, or simply numerical lab test results? A clearer definition is needed. Furthermore, if these are lab test results, it's important to specify which types of lab tests are included (e.g., blood glucose, cholesterol, etc.) and how they are represented (e.g., raw values, normalized values, or categorical bins). The lack of clarity makes it difficult to assess the scope and applicability of the method.
2. The methodology formulation could be enhanced with a detailed figure to improve understanding. Current figures only depict the high-level concept. Figure captions require more detail to be self-explanatory (e.g., Figure 3). Specifically, a detailed diagram illustrating the data flow, the specific transformations applied to both visit-level and monitoring-level data, and the interaction mechanisms between these two levels would be beneficial. The current figures do not provide sufficient detail to understand the technical implementation.
3. If monitoring data includes lab signals and measurements, this would classify the work as multimodal. Comparisons should then be made with works using similar data modalities. However, the baselines used here only involve EHR data (sequences of discrete codes, such as diagnoses, prescriptions, and procedures, inside hospital visits). If the monitoring data is indeed lab results, the baselines should include methods that can handle both discrete EHR codes and continuous or numerical lab values. The current baselines are not sufficient to demonstrate the superiority of the proposed method in a multimodal setting.

### Questions
Please clearly explain monitoring data with examples. Do all the patients contains these information (Provide statistics)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper seeks to improve the ability to make predictions on electronic health record data by constructing a graph between features and then using a graph neural network. The key insight is that we can split EHR data features into two categories, monitoring events (where we measure something about the patient) and visit events (where we do something about those recordings) and carefully construct the graph to take advantage of the relationship between the two. The result is improved predictive performance.

### Strengths
-  Well written paper, with very nice text, figures and appendix
-  Good evaluation task and metric selection

### Weaknesses
 - There are very minimal details on how hyperparameter selection was done for this method and the baselines. (I don’t see any details at all for the baselines?) Ideally we want a table of the optimal hyperparameters and the hyperparameter search grid (or if random search, the distributions searched) for every model, including your proposed model and baselines. Did you dedicate roughly equal time to hyperparmeter searching for both your method and your baselines?

- Almost all (except 2) of the baselines are missing monitoring event features, which is a very significant limitation. I think it’s necessary to have at least one simple baseline that has both monitoring events and visit events as features. Based on the fact that most of your sequences have length 1 (and your experiments that show that sequence length doesn't really matter), a very simple feedforward neural network that has access to all features would be a great baseline.

- These are very small datasets, 15k for MIMIC-III and 19k for MIMIC-IV. I am skeptical that this method will continue to provide benefits for larger datasets, as in theory with enough data a deep neural network should be able to automatically learn these interactions. This ties into how even the authors note that the dataset is so small that a single graph layer performs best.

- A major part of the data processing code “preprocess.drug_recommendation_mimic34_fn” and “preprocess.diag_prediction_mimic34_fn” is missing. This will make this paper more challenging to reproduce and makes it difficult for me to fully review / understand this paper.

- The improvements in performance are small, and (if I am reading table 1 correctly) are often within a standard deviation of the baselines.

### Questions
See weaknesses

### Soundness
1

### Presentation
4

### Contribution
3
