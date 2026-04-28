# Right on Time: Revising Time Series Models by Constraining their Explanations

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
The reliability of deep time series models
  is often compromised by their tendency to rely on confounding factors, which may lead to incorrect outputs.
  Our newly recorded, naturally confounded dataset named \data from a real mechanical production line emphasizes this. To avoid ``Clever-Hans'' moments in time series, i.e., to mitigate confounders, we introduce the method \rrtfull (\rrt).
 \rrt enables, for the first time interactions with model explanations across both the \textit{time} and \textit{frequency} domain. Feedback on explanations in both domains is then used to constrain the model, steering it away from the annotated confounding factors.
  The dual-domain interaction strategy is crucial for effectively addressing confounders in time series datasets.
  We empirically demonstrate that \rrt can effectively guide models away from the wrong reasons in \data as well as popular time series classification and forecasting datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a right for the right reason method (RRR) for time series data, which they refer to as Right On Time RioT. Similar to the RRR method, the method involves first extracting explanations for the model's predictions. They use IG for explanations, and then, using human feedback, they add a loss to penalize the model for looking at the incorrect locations. Since they do this for time series, they propose adding two losses, one for the time domain and one for the frequency domain. RioT reduces the model's reliance on confounding factors during training. The paper introduces a new dataset called PRODUCTION PRESS SENSOR DATA (P2S), which captures sensor readings from an industrial high-speed press in the sheet metal working industry. This dataset is characterized by naturally occurring confounders that can lead to inaccurate predictions when used for training models to detect production faults. P2S provides explicitly annotated confounders, P2S can be used for testing and comparing methods to mitigate the impact of confounders on real-world data.

## RioT

1- *Explain* The paper proposes using IG to extract model explanations for classification problems. The paper uses a modified version of IG with the input magnitude and not the input sign to compute the IG attribution equation 1; for forecasting, the paper uses the average over the forecasting window as an explanation, as shown in equation 2. To get explanations in the frequency domain, the paper transforms the explanations from the time domain to the frequency domain using the Fourier transformation.

2- *Obtain* The paper assumes the user provides annotations of cofounders, resulting in a mask {0,1} mask where 1 represents the presence of a confounder.

3-*Revise* An additional loss term is added to the objective that penalizes the model for looking at the wrong location. This is done by multiplying the explanation produced by the IG with the annotation mask. They propose adding a loss term for both frequency and time domains.

## Experiments

# Datasets

- The paper introduces P2S, which is annotated with confounders. It is a classification dataset. In this dataset, the paper refers to the run speed as a confounder, and experts highlight regions in the time series where there is a difference in the time series due to the difference in the run speed, not in the label itself.

- The paper evaluates UCR/UEA datasets to test whether RioT can help mitigate confounders by adding spatial or frequency shortcuts to the datasets. These confounders result in false correlations between patterns and class labels or forecasting signals within the training data, which do not appear in the validation or test data. An annotation mask is created to simulate human feedback based on the confounder's region or frequency.

# Models

- For classification, they use RioT on FCN and OFA models.

- For regression, they evaluate adding RioT to the TiDE, PatchTST, and NBEATS models.

# Results

- For classification: The paper showed that adding RioT helps improve the accuracy when the data has spurious correlations present in the training dataset but not in the test data across 4 datasets in both spatial and frequency domains.

- For forecasting: The paper showed that adding RioT for confounding datasets reduces MSE in some cases, giving MSE even better the the unconfounded datasets.

- On P2S: They showed that even with partial human feedback, RioT could help the model focus on the correct regions in the input data, resulting in better overall accuracy.

- Multiple confounders: The paper investigates when confounders exist in both frequency and spatial domains; it shows that using the aggregate loss functions with both frequency and spatial feedback gives the best results in this case.

- Human Feedback: The paper shows that even with a small amount of feedback, 5% of the original dataset significantly boosts accuracy. The paper also shows RioT is robust to noisy feedback. They showed that with even 50% noisy feedback, using RioT can still result in some performance gains.

### Strengths
## Originality

- The application of RRR methods to time series data is novel.
- Introducing two RRR loss terms for spatial and time domains is novel.
- The P2S dataset is a new contribution, featuring confounder annotations that can be utilized for future method evaluations.
- The unique approach to adding confounders to the UCR/UEA datasets is original; this dataset can serve a similar purpose to DomainBed in image analysis (https://github.com/facebookresearch/DomainBed) for future model evaluations.

## Quality

- The application of RRR in this context is well-justified.
- The paper presents robust empirical results.
- It explores various scenarios where feedback was either incomplete or incorrect, demonstrating that RioT remains effective in such cases.
- The paper is well-written and easy to understand.

## Significance

- With the introduction of the new P2S dataset and the proposed setup for UCR/UEA, this work is quite significant. It provides valuable resources that the machine learning community can use and build upon.

### Weaknesses
## Novelty:
-  RioT itself is not novel, it is just applying RRR to time series data.
## Clarity:
- Some minor clarity issues; please see the question section.

### Questions
- What is $\bar{x}$ in equation 1? if it's the reference point, please clarify and discuss how you choose the reference point for time series data.

- In equation 2, how is $e'_i(x)$ calculated?

- In line 249, why is the second-order derivative required? IG traditionally uses first-order derivatives.

- In Figure 4, it is difficult to see the attribution colors.

- In the experiment "Removing Multiple Confounders at Once," are the masks (that mimic human feedback) given in both spatial and frequency domains? i.e., different masks for different domains? If this is not the case, I am not sure why applying RRR in both frequency and time domains will necessarily help. Since one is the transformation of the other. What is your intuition as to why this might be the case?

### Soundness
4

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
4

### Summary
The paper titled introduces a novel method named RioT for mitigating confounding factors in time series models. The authors emphasize the importance of addressing 'Clever-Hans' moments in time series models where spurious correlations may compromise model performance. The key contributions are:
1. Introduction of a new real-world dataset P2S containing annotated confounders from industrial sensor data.
2. Proposal of RioT, a feedback-based technique that operates across both time and frequency domains to mitigate confounders.
3. Empirical evidence showcasing that RioT improves the generalization of time series models across multiple datasets and scenarios.

### Strengths
1. High practical relevance: The focus on confounders in industrial sensor data highlights the method's real-world applicability.
2. Novel dual-domain feedback: Operating across both time and frequency domains is an innovative extension to existing XIL paradigms.
3. Empirical rigor: The experiments span across multiple datasets, models, and configurations, adding robustness to the findings.

### Weaknesses
1. Dependency on human feedback: The method requires expert annotations, which may be costly and challenging to acquire at scale. This reliance on human-provided masks is a significant limitation, particularly in scenarios where such expertise is scarce or expensive. The annotation process itself is also not well-defined; the paper does not specify the level of granularity or the specific criteria used by experts to identify confounders, making it difficult to assess the reliability and consistency of the feedback.

2. Training cost: Incorporating feedback through gradient-based explanations adds computational overhead. The paper does not provide a detailed analysis of the computational cost associated with the feedback mechanism, making it difficult to assess the practical scalability of the proposed method. Specifically, the additional backpropagation steps required for the gradient-based explanations could significantly increase training time, especially for large-scale models or datasets. A more thorough analysis of the time and memory requirements would be beneficial.

3. Limited exploration of feedback noise impact: Although robustness tests are performed, more exploration of noisy annotations could be useful to assess real-world viability. While the paper mentions robustness tests, it lacks a comprehensive evaluation of the impact of varying degrees of noise in the annotations. In real-world scenarios, annotations are likely to be imperfect, and the method's sensitivity to such noise is a critical factor in its practical applicability. A more rigorous analysis, including different types of noise (e.g., random, systematic) and varying noise levels, is needed.

### Questions
1. In Figure 1, it is unclear how annotations on the pretraining data are handled. Can the authors clarify if the feedback on pretraining is incorporated into final model updates?
2. Could you elaborate on any instances within which incorporating frequency domain feedback negatively affected performance? It would be particularly insightful to explore scenarios where the frequency domain annotations might conflict with those in the time domain.
3. Given the increased training cost, what strategies can practitioners use to balance the feedback quality and computational efficiency?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces RioT, a method to mitigate confounders in time series analysis. The authors adapt established explanatory interactive learning (XIL) methods for time series analysis. XIL includes human-in-the-loop approaches that provide feedback on model explanations, particularly penalising model decisions based on confounding factors such as artifacts and noise. Evaluations across various architectures and downstream applications indicate that integrating human feedback into the training process may help reduce confounding factors in time series analysis.

### Strengths
1. The paper is well structured.

2. The paper is clearly written.

3. The authors conduct various experiments including different model architectures and downstream applications to evaluate their method.

4. The authors provide their code to support reproducibility.

### Weaknesses
1. Table 1 to Table 4 as well as the statement "we evaluate on [...] popular datasets [...] with 70% / 30% train / test splits" (ll. 268-269) indicate that the authors did not use a validation set, i.e. tuned their models on the test set. The authors should follow good practice and adhere to established procedures, e.g. as introduced by [1] for forecasting (train/val/test split of 60/20/20 for ETTm1, and 70/10/20 for Energy and Weather). 

2. The proposed approach requires human feedback for each downstream application, which is expensive as domain knowledge is required. Furthermore, the authors claim that "RioT is well-equipped to manage the practical challenges associated with human feedback" (ll 475-476). However, such human-in-the-loop approaches are vulnerable to adversarial attacks, i.e. intentionally poisoned feedback, which the authors do not address in their work. 

3. The approach focuses on uni-variate time series analysis. Since the authors do not explain how to extend their method to multi-variate time series, its applicability to real-world scenario remains limited. Additionally, the authors further constrain their approach by excluding "datasets with time series of different length or missing values" (l. 752), focusing on "datasets with less than 10 classes" (l. 769), and omitting "all datasets with less than 1000 training samples" (ll. 771-772) from their analysis. These constraints, especially the first and last, rule out applications in domains with limited data availability, e.g. medicine.

4. The authors use integrated gradients [2] to provide explanations $e(x)$, assuming that labels are available, e.g. for classification tasks, and of good quality. For forecasting tasks, pseudo-labels are created by computing an explanation for each time step $w$ in the forcasting horizon $W$ and creating a single representative explanation using global average pooling over all $W$ explanations, which requires further investigations to rule out points of failure. 

5. The methodology section requires clarification, as the authors introduce variables, including $\bar{x}$, $\tilde{x}$, and $\alpha$ in Equation (1), without providing definitions.

6. The reproducibility is not fully supported, as the authors did not describe how they tuned the models for the experiments.

### Questions
1. How to provide feedback for medical domains and domains which might contain non-trivial confounders? Does the approach translate well across domains such that feedback might not be required for specific applications?

2. How to evaluate whether the human feedback is of good quality? Is there a way to quantitatively measure feedback quality other than training the model with the respective human feedback and eventually evaluating the downstream performance?

3. How is the human-in-the-loop supposed to identify the confounders in the real and imaginary part within the frequency domain? Could the authors further elaborate on this and provide visual examples for clarity?

4. The model needs to be trained to derive the explanations using integrated gradients. How many iterations of training, i.e. explanations $e(x)$, and successive feedback, i.e. $a(x)$, are required to achieve a sufficiently good model? How does the downstream performance evolve as the number of iterations increase?

5. Could overfitting on confounders be mitigated by carefully selecting the validation set? As the authors assume that "confounders [...] are absent in [the] test set" (ll. 309-310), why not construct a validation set with non-confounded samples and use an early stopping criterion on the validation metric to prevent overfitting? This experimental setup would demonstrate how the proposed RioT performs in comparison to cheap early stopping techniques, that do not require human feedback.

6. The authors investigate fully supervised settings. Have they considered to analyse whether pre-trained models, i.e. models that are trained using self-supervised methods, are less prone to overfitting on confounders?

7. Do the authors "report average and standard deviation over 5 runs" (l. 305) across different seeds set during fine-tuning?

8. The authors "add spatial (sp) or frequency (freq) shortcuts to the datasets from the UCR and Darts repositories" (l. 308). For visualisation purposes, could they also provide examples of representative data samples before and after adding these shortcuts?

9. Could the authors add a qualitative analysis of the learned latent space to visualise how confounders may influence the model prediction?

### Soundness
2

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
This paper proposed a method named Right on Time (RioT), which can enable human interactions with the time series model explanations in both time and frequency domains. The authors also created a confounded dataset named P2S from a real scenario and conducted detailed experiments on both synthetic datasets and this real-world datasets for evaluation.

### Strengths
* The idea of human-in-the-loop for removing confounding factors in time series modelling is interesting.
* The published confounded dataset will be beneficial to the research community.

### Weaknesses
 * The proposed method seems to be not very practical in real world applications. Firstly, the proposed method relies on human annotations for the whole datasets, which will require huge labelling costs. Secondly, for many real-world applications, the confounders are often unknown, so that human labelling may not be trivial, especially in frequency domain. 
* The proposed method assumes that all the confounders could be lablled by human experts. First, if all the condounders are known, it will be very convenient to apply causal learning based methods to avoid these confounding effects. Second, the proposed method penalizes the confounding factors by a penality term, which can only reduce their effects but cannot completely remove their effects. Directly removing the confounding factors from the input seems to be more effective than the proposed penality term in my opinion.
* The frequency domain explanation seems to be a trivial Fourier transformation of the time domain explanation according the descriptions in line 186/187. This means that the two types of explanations are essentially the same thing with different format, which may not be the optimal cases in my opinion. I am not sure if it would be better to directly learn frequency domain explanation independently, i.e., tranforming the input data into frequency domain and then applying IG for obtaining explanations.
* The presentation should be significantly improved. Here are a few examples:
    * line 34: in practice Geirhos et al. (2020) -> in practice (Geirhos et al., 2020)
    * line 124: casual analysis -> causal analysis
    * line 149: Given is a dataset - > Given a dataset

### Questions
For the major questions, please refer to my comments above.

Here are some additionl questions:
1. For Table 1, will the accuracy be the same as the unconfounded case if you directly remove all the confounders from the synthetic dataset? If so, a penality term will be unnecessary.
2. In line 200, you mentioned "apply the same annotation mask to many samples". How did you do that automatically?
3. Would it be possible to apply other unconfounding/causal learning/robust learning methods on the P2S datasest? It would be helpful to compare with other types of methods in addition to comparing different variants of the proposed method.

### Soundness
2

### Presentation
1

### Contribution
2
