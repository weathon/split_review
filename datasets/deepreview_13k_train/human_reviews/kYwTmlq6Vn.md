# PaPaGei: Open Foundation Models for Optical Physiological Signals

- Decision: Accept
- Scores: 8, 3, 8, 8

## Abstract
Photoplethysmography (PPG) is the most widely used non-invasive technique for monitoring biosignals and cardiovascular health, with applications in both clinical settings and consumer health through wearable devices. Current machine learning models trained on PPG signals are mostly task-specific and lack generalizability. Previous works often used single-device datasets, did not explore out-of-domain generalization, or did not release their models, hindering reproducibility and further research. We introduce \model{}, the first open foundation model for PPG signals. \model{} is pre-trained on more than 57,000 hours of 20 million unlabeled segments of PPG signals using publicly available datasets exclusively. We evaluate against popular time-series foundation models and other benchmarks on 20 tasks of 10 diverse datasets spanning cardiovascular health, sleep disorders, pregnancy monitoring, and wellbeing assessment. Our architecture incorporates novel representation learning approaches that leverage differences in PPG signal morphology across individuals, enabling it to capture richer representations than traditional contrastive learning methods. Across 20 tasks, \model{} improves classification and regression performance by an average of 6.3\% and 2.9\%, respectively, compared to other competitive time-series foundation models in at least 14 tasks. \model{} is more data- and parameter-efficient than other foundation models or methods, as it outperforms 70x larger models. Beyond accuracy, we also investigate robustness against different skin tones, establishing a benchmark for bias evaluations of future models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes two open foundation models for PPG signals, PAPAGEI-P (patient-aware) and PAPAGEI-S (morphology-aware). These models mainly differ in their training strategy—one uses a self-supervised approach to maximize agreement between embeddings of the same patient and the other maximizes the agreement between signal features across patients. The two models are tested on several datasets to evaluate their performance on different tasks, including binary and multi-class classification and regression, and they are compared with other general foundation models and SSL approaches. Ablation studies are carried out to understand the performance impact of the datasets used for pre-training, the impact of each model component, the effect of different levels of labeled data, and model size and scaling. Some case studies are also presented to evaluate different subject- and data-related aspects.

### Strengths
1. The paper claims to propose the first open foundation model for PPG signals, which tries to improve the current models' performances using publicly available data and data augmentation, while also being relatively light-weight (~5M parameters)
2. The paper is well-organized, rich in technical details regarding the data preprocessing, model architecture and training, and performs extensive testing on different tasks. It also includes ablation studies that prove the performance gains of each component. 
3. The methods and results are well explained and covered, and are accompanied by relevant tables and figures to facilitate comprehension and readability
4. The framework presented can have practical implications for cardiovascular monitoring and be used for several applications

### Weaknesses
1. While performing slightly better in some tasks relative to other foundation and SSL models, the proposed models lack comparison with task-specific non-SSL models. Despite including statistical feature models for baseline, which can give a basic comparison, state-of-the-art task-specific models, with or without engineered features, are not included. Such comparison would provide insights into whether the SSL approach yields better representations than supervised-learning ones. Specifically, the absence of comparisons against models explicitly trained for tasks like blood pressure estimation or sleep apnea detection, which are common applications of PPG, makes it difficult to assess the practical advantage of the proposed approach over existing, highly optimized solutions.
2. Task performances are evaluated using AUROC and MAE, but the manuscript doesn't seem to comment on the F1 scores and R2 in some tasks, which are often related to class imbalance and yield poor results. Addressing this topic or proposing a strategy to handle these cases would be appreciated. The lack of F1-score reporting is particularly concerning for classification tasks where class imbalance is likely, as AUROC can be misleading in such scenarios. Similarly, the absence of R2 values for regression tasks limits the understanding of the model's goodness-of-fit and predictive power beyond just the mean absolute error.

### Questions
1. Do you have any suggestions to improve the model's performance in tasks where performance is low or when class imbalance is an issue?
2. Regarding the out-of-domain datasets, do they all use different devices from the ones in the pretraining datasets?
3. And have you looked into other biases that could be present in the datasets (sex, age, gender, weight, health conditions)?

Some other suggestions:
- Report the train and validation training loss curves for both models would help understand the convergence stability in both approaches
- Make sure to reference all the appendices in the main text

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes foundational models for photoplethysmography (PPG) signals. The presented model is trained more than 57,000 hours of 20 million unlabeled segments of PPG signals using publicly available datasets. Authors evaluate the model on 20 tasks of 10 diverse datasets including cardiovascular health, sleep disorders, and pregnancy monitoring.

### Strengths
The motivation of the works regarding the open and public foundational models with datasets is important. The paper focuses on applications of healthcare with monitoring which is relatively less studied in machine learning community. The authors perform the skin tone analysis, which can be important to evaluate fairness.

### Weaknesses
The technical contribution of the paper is limited. All the components, extracted features, architectures, and augmentations, of the framework are not novel. Only the integrated loss values seem novel in training but there is no clear motivational evidence for this integration. Worse, extracting those features is not trivial for noisy PPG segments, especially the sVRI and IPA as they depend on the waveform. This limits the training to clean datasets, which are collected under very limited motion, including ICUs. For example, VitalDB, one of the datasets that authors used for pre-training, is collected during surgery. This is a significant drawback in terms of the generalization of the framework.

Second, the manuscript does not explain why this framework (extracting waveform features and using them during training) performs well. For example, DaLiA is a noisy dataset where extracting those morphology features is extremely prone to error. Although DaLiA is not used for training, the manuscript does not explain why these features help extract useful representations from noisy datasets.

Third, the extracted statistical features are extremely basic (mean, median, maximum, minimum, and percentiles), but their performance is very close to the proposed model in several tasks (most confidence interval overlaps). Compared to these features with a neural network of 5M parameters, the results are not significant, which makes the usefulness of the presented work controversial.

Fourth, SimCLR and BYOL are self-supervised learning frameworks that allow someone to change the encoder architecture. In the comparison, BYOL has 12M parameters. Why not explore other networks to match the parameter count and then compare? For example, the authors did an ablation study regarding the model size of their network and stated "As shown in 5c, the smallest model with 5M parameters performs best in all tasks except one, indicating that smaller models are better suited for PPG data." According to this statement, small models with other self-supervised baselines might perform better than the presented work. This statement by the authors raises significant questions about the fairness of the evaluation.

Fifth, some statements in the manuscript are too powerful, if they are not completely wrong. For example, the authors stated "PAPAGEI-S uses cropping (0.25) and Gaussian noise (0.25). PAPAGEI-S avoids augmentations that alter PPG’s morphology." Adding a Gaussian noise would change the morphology of the features. If the morphology refers to the waveform shape of the signal in the manuscript. All the applied transformations should have zero or linear phase response, Gaussian noise would change the phase values nonlinearly so the statement is wrong. Another statement "We propose PAPAGEI-P, a patient contrastive approach that maximizes agreement between signals from the same subject.", the subject/patient wise contrastive learning is already proposed by previous works (i.e., CLOCS,  ICML 21). Proposing a method that is already out might mislead the readers, the language of the manuscript needs a major revision.

### Questions
1) I checked the code, but I could not find the processing and evaluation of DaLiA. Could the authors specify the path to it? Thanks!

2) The authors stated that "Additionally, we did not perform an exhaustive evaluation of different augmentation settings but instead used transformations and values based on prior research  (Abbaspourazad et al., 2023; Tang et al., 2020).". The importance of the augmentations are well-known in self-supervised learning, especially depending on the application. The application of the second reference is inertial measurements instead of PPG signals. And, only the cropping and Gaussian noise are similar with the first reference. Is there a specific reason why PPG-based data augmentations are not explored?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides an open foundation model (open code, data, model) for a physiological signal, PPG. The authors have pre-trained a model on a combination of 3 open-source PPG dataset, and evaluated on various datasets for various downstream targets. The comparisons with some off-the-shelf time-series models, and pre-training algorithms have been presented, and several ablations studies regarding different components have been done.

### Strengths
* While pre-training foundation models for PPG has been done before with closed-source models/datasets some with open-source and some with closed-source code, this work presents the first open-source foundation model for PPG, trained on open datasets, with open-source code, that can foster the use of PPG for health applications and for health research. 
* The paper, in my opinion, is well-written. I enjoyed reading the paper, the comparisons are well-presented and the paper is easy to follow. I would like to thank the authors for their efforts in the quality of the analyses and presentations in the figures.  
* I really appreciate the level of details in the paper including the ablations studies; authors did a good job for providing good level of information and detailed ablations for a curious reader.

### Weaknesses
 * One of my main comments is regarding the novelty of the presented work, the language in the paper with respect to the prior work, and lack of comparison with the prior work in terms of performance. It appears to me that the idea in this paper resembles significant similarity to a prior work [1] (which is cited in this work multiple times) in terms of: 1) training a PPG foundation model on a large-scale dataset, 2) methodology in terms of loss, positive pairs, random augmentations, 3) evaluation across multiple targets, and demonstrating that one PPG foundation model is strongly predictive of a wide array of downstream health conditions. The main distinction of this work is openness of dataset, code and model. I do appreciate the openness aspect, however, the language in the paper sadly does not properly reflect the relationship to the prior work. For example, the only mention is in the introduction/related work is “Recent studies have shown promise in this area, as (Abbaspourazad et al., 2023) demonstrated that embeddings from ECG and PPG signals can generalize across multiple health-related tasks using proprietary Apple Watch data.”, which does not reflect the proper relationship between the two papers and the 3 points stated above. I highly recommend authors to reflect the appropriate relationship upfront for fairness:
    * It is also surprising to me that throughout the dataset/results, there’s no comparison table to the prior work [1] in terms of performance and choices of PaPaGei. Given the direct resemblance of the 2 works, my suggestion to the authors are: 
         * Putting a table/discussion in the methods/datasets for comparison of dataset used in this study with respect to the prior work for PPG foundation models [1] in terms of number of subjects, amount of data, openness vs. closedness, number (and kinds) of different devices and etc. In addition, comparison of the (only major) training choices, size of models, compression ratios (how many channels, how many seconds of input compressed to what embedding size). 
         * Putting a comparison results evaluation table/discussion for major downstream targets in comparison to reported numbers in [1], at the very least for demographics comparison such as age/sex/body mass index, whose evaluations are missing in the current manuscript (they are important!), and has not been compared to the closed work [1]. This will demonstrate the effectiveness of PaPaGei training/model, and provide the performance gap (if any) with closed source models (authors can note that evaluation datasets are different).
    * Also, the language with respect to another prior work [2] can be enhanced. Pre-training PPG models where positive pairs are with respect to signal quality was done prior to this work but there was no direct mention of this in the paper [2]. Moreover, this prior work has open-source code  (closed-source dataset) which was again not mentioned properly. I suggest authors consider citing these prior work properly. 
    * In addition, the idea of pre-training foundation models on other physiological signals on large datasets in the related work section is missing. Papers such as [3] for ECG and [4] for IMU (just examples) should be added. 
    
* One of my main concerns about the reported evaluations is the significance of the reported metrics in downstream comparisons. To provide an example, in Table 3, authors provide point estimates and confidence bounds, but for a lot of the targets, the confidence bounds are very wide and overlapping across methods. For instance, for “smoker”, it is not clear to me whether PaPaGei-P is significantly better than Chronos. My suggestion to the authors are:
    * This begs the question about the effectiveness of PaPaGei, given that an off-the-shelf time-series model that was not trained on PPG (Chronos), can capture similar amount of information regarding an important vascular target (smoking), therefore providing discussion would be valuable for the readers.
    *  Providing P-values and n for significance comparisons is essential. Similar comment for other comparisons such as Table 4, Figures 4, 5 and 6.
* In terms of comparison with SimCLR and BYOL, the authors can do a better job explaining the training choices and implementation, and demonstrate fair comparisons. They say “It is noteworthy that both BYOL and TF-C require multiple encoders and different projection heads, resulting in variations in model sizes. For these methods, we use existing implementations available online, but apply our encoder as the backbone to ensure consistency.”. I appreciate that they used similar encoder for fair comparisons, but other implementation details is not clear to be identical. My suggestions/questions to be clarified in the paper are:
    * What details are the same and what details are different? (for example positive pairs, augmentations, batch size, learning rate, and any other useful details to demonstrate fair comparisons). 
    * Also kinda related to this, there’s no mention of how and what temperature was selected.

### Questions
* Do all datasets contain single-channel PPG? If yes, it is worth mentioning in the paper.
* It is interesting that combining three pre-training datasets, does not provide much additional information regarding downstream targets. What’s the authors’ hypothesis? It is worth adding a discussion to the paper
* I am not sure about this statement: “Interestingly, in single datasets, MESA performs the best, despite having the fewest participants but the highest number of segments, echoing similar results in the language model domain (Dubey et al., 2024).”. Do the authors have a justification for why they think this is relevant to Llama3? If yes, please add to the paper, and if not, please consider changing the language. 
* What’s the authors hypothesis for PaPaGei-S being better than PaPaGei-P in general? I find it very surprising that defining the positive pairs based on quality of the segments (and not subjects) improve the performance. In fact, one could argue PaPaGei-S should have a slightly worse performance, because it does not leverage pairing good quality and bad quality segments. Did the authors investigate the performance of a few downstream targets, w.r.t the change in segment quality in PaPaGei-P vs. PaPaGei-S?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper reports on development and downstream testing of a pair of new foundation models (PaPaGei-P and PaPaGei-S) for photoplethysmography (PPG) signals in comparison to several pre-trained models and alternative pre-training methods.  All pre-training and downstream evaluation was accomplished using publicly-available PPG data sets, and the authors have shared their codebase to enable end-to-end reproducibility of the work reported in the paper.   In addition to the open codebase and use of public data sets for model development (which is itself new for published PPG foundation models) the novelty of this paper includes the incorporation of PPG-specific physiologically-informed loss functions during the pre-training phase.  

The authors perform evaluation of the PPG encoder generality and utility using a battery of 20 downstream tasks, some of which have been published previously (for example blood pressure estimation and hypertension classification) and others of which are new (for example gestational age estimation).   They report performance comparison for their models against a pair recently published time series foundation models (Chronos and Moment), against an existing PPG-specific pre-trained model (REGLE), against three well-established self-supervised learning methods (SimCLR, BYOL, and TF-C), and against a baseline approach consisting of simple signal statistics fed into random forest models. 

In addition to the performance comparison with other models and modeling approaches, the authors also report model size analysis, model sensitivity to skin tone, and systematic ablation analysis (evaluating the benefit of each source data set and PPG-specific loss function used in pre-training).

### Strengths
## This paper represents strong contributions in the following areas: 
### Originality: 
Although the idea of foundation models is not new, there have been few published examples of foundation model development and evaluation for physiological signals such as PPG.  Here, in addition to comparing the performance of multiple pre-trained time series foundation models, as well as adapting different contrastive and momentum-based SSL methods, the authors have also incorporated some PPG-specific elements into the pre-training (loss functions for SQI, sVRI and IPA) that have not been reported elsewhere.  

**Furthermore the authors should be commended for two important things which, combined, have not been published previously:**
1. They performed all training and downstream evaluation using data sets that are publicly available, enabling straightforward reproducibility and verification of their results (as well as use of their models by other researchers for future work).  
2. They shared their codebase directly in the submission, which is organized and sufficiently well-commented to understand in a reasonable amount of time. 

### Clarity
The paper is well written, with clear descriptions and explanations in several key areas: 
1. Data set provenance (Appendix B is very helpful), and the purpose(s) for which each data set was used;
2. Data pre-processing;
3. High-level strategy and technical details of the pre-training method and loss/objective functions;
4. Downstream task evaluation and performance reporting (the subset of cases that I checked were straightforward to evaluate and understand);
5. Analysis that was performed in addition to performance reporting on downstream tasks, such as dispersion of subject embeddings and sensitivity of some tasks to skin tone. 

### Significance 
1. The exploration of PPG-specific dimensions of the SSL training is valuable and important, as well as the authors’ comparison of their model with off-the-shelf time series foundation models and established (but not PPG-specific) self supervision methods.  This has the potential to impact work in other areas at the intersection of machine learning and physiological sensing. 
2. PPG foundation models, in particular open/reproducible foundation models, have the potential for high impact in both health research and practical applications. 

### Quality
Claims and conclusions were generally well-reasoned and justified, with some key exceptions (discussed in the following section).

### Weaknesses
 # Brief Summary #
This paper had some important weaknesses that are listed briefly below, with more detailed comments and some suggested steps to address these weaknesses following the list:
1. Absence of downstream evaluation on basic demographic targets such as age, height/weight, BMI or sex. 
2. [Most concerning] Inappropriate choice of baseline model (RF using basic signal statistics) for performance comparison with their models. 
3. In the Case Studies section discussing the downstream AHI regression performance, the authors do not provide good evidence indicating that the model captures the distribution tails well.



# Additional Discussion Details #

## Issue 1: Absence of downstream evaluation on basic demographic targets
PPG is known from past publications (including at least one cited by the authors) to capture information highly predictive of age, body mass index (BMI) and sex.  These demographic factors are also highly predictive of additional health targets, indicating that a data-driven model may use demographic features as prediction ‘shortcuts’, rather than utilizing features that are specific to the health target of interest.  Performance of the authors’ models (and other models) in predicting demographic targets can give an indication of how well the models capture information relevant to these tasks, as well as provide some clues as to whether the models may be using demographic-related features as ‘shortcuts’ for other downstream tasks. 


## Issue 2 [Most concerning]: Inappropriate choice of baseline model

The choice of baseline model consisting of RF with PPG signal statistics represents an inappropriately weak baseline.  In a few ways this approach is even weaker in practice than as stated in the paper (for example the signals are z-scored in pre-processing, meaning that the signal mean is guaranteed zero for all segments and therefore provides no information to the RF model).  Additionally, the section describing the additional PaPaGei-S objectives highlights the physiological relevance of the IPA, SVRI, and SQI (and the authors seem to have all the code/tools necessary to perform these calculations across a large number of PPG segments), which would provide a simple strategy to improve the statistics-driven baseline model. 

Lastly, as mentioned for the previous item (Issue 1) PPG is known to capture information highly predictive of age, body mass index (BMI) and sex, with the corresponding features then used by downstream models as ‘shortcuts’ for predicting a variety of targets that have demographic dependence.  It would be highly informative to include a simple baseline model that predicts each target value/class using the demographic factors as inputs (the model could be LR, or Ridge, depending on the target task).  

The reason that this incorporation of baseline models with demographic inputs (producing a ‘stronger’ baseline for comparison) is important is that it can help **reveal whether the PaPaGei models truly represent a meaningful breakthrough** or are simply equivalent to (or even worse than) much simpler established approaches.  


### My Findings regarding demographic (and constant/mean) predictor performance on a subset of the public PPG datasets: 

I appreciate that the authors utilized public and (in several cases) conveniently-accessible data sets for their downstream evaluation. This made it possible for me to spot check the performance of some simple baseline models on several of the tasks.  Due to time limitations I could not do this analysis for every task, but am reporting observations for tasks associated with the data sets PPG-BP (Liang, etc al. 2018), and ECSMP (Gao et al., 2021), which covers the following downstream tasks: SBP (R), DBP (R), Avg HR (R), Hypertension (C), Mood Disturbance (C).  For these tasks I was able to achieve the following performance using either a constant mean predictor (only for DBP regression task) or a demographics-based predictor incorporating Age, BMI, sex (where available): 

1. **DBP** Estimation (regression): I observed **MAE = 8.71** (identical to PaPaGei-S performance, **better than PaPaGei-P performance)** using a constant mean predictor; I observed **MAE = 8.07 (better than all models)** using a demographics-only predictor (OLS fit with age, sex, BMI up to quadratic terms). 
2. **SBP** Estimation (regression): I observed **MAE = 13.56 (better than evaluated models including PaPaGei)** using a demographics-only predictor (OLS fit with age, sex, BMI up to quadratic terms), and **MAE = 12.48** using demographics + heart rate (OLS fit)
3. **Avg HR** Estimation (regression): I observed **MAE =8.11 (much worse than any reported model)** with a demographics-only predictor. 
4. **Hypertension** (classification):  Using the same class grouping reported by the authors, I observed **ROC AUC = 0.78 (better than all evaluated models including PaPaGei)** with a demographics-only LR predictor (age, sex, BMI, HR up to quadratic terms)
5. **Mood Disorder** (classification):  Using the same class grouping reported by the authors, I observed **ROC AUC = 63 (better than all evaluated models including PaPaGei)** with a demographics-only LR predictor (age and sex up to quadratic terms)

I did not personally check any other data sets or tasks due to time limitations.  Despite the caveat that for the results above I did not split the data into train/test sets, for 4 our of 5 cases the performance from these much simpler models (at most 15 parameters) was better than the models having millions of parameters.  Combined with the knowledge that PPG captures significant demographic information, this finding is strongly suggestive that the models may simply be using demographic-related features as ‘shortcuts’ for the target task. 


## Issue 3:  Poor evidence for regression models capturing the distribution tails. 

I disagree with the authors that the analysis and plots in Figure 8 (particularly 8a) provide evidence that the predicted values match the distribution of the true values.  For the plots in Figure 8a the regression slope is clearly much less than 1.0, indicating that the models tend to over-predict for small True AHI data points and tend to under-predict for large True AHI values (i.e. significant model bias present)


### Questions
The paper is generally very well-written (in terms of both clarity and technical content) and overall I enjoyed reading it. I have a few additional comments/questions regarding style and content: 

1. Reporting the average MAE across tasks in Tables 3 and 4 (and in Figure 4) may not be the best way to summarize the regression performance, since the regression targets have several different units (e.g. mmHg, bpm, and weeks).   To provide a ‘fair’ summary across all the regression tasks with different units, it would make more sense to use a unitless metric such as mean absolute percent error or (possibly) the mean F-statistic across all tasks. 
2. In Figure 5a/b and 6, it is not obvious to the reader whether these differences are statistically significant.  Were any tests for significance performed?  If so, it would be helpful to report this briefly (simply using the name of the test and stating the significance level).
3. Expanding on Figure 5a/b (component ablation) it would be informative to see a summary of the performance changes across all downstream tasks, which may provide some insight into which PPG-specific pre-training losses are influential for certain tasks and not others.  This could be an additional appendix table (it doesn’t need to fit into the main text).   
4. Figure 5c shows that, on average, the middle-sized (35M) parameter model has the worst performance while the smallest (5M) parameter model has the best performance.  Were models smaller than 5M evaluated?  Including performance for models smaller than 5M (perhaps going as small as 0.07M , the size of REGLE) would give an indication of whether 5M truly represents the optimal model size.  This would also make the overall trend more clear (a non-monotonic trend for only 3 model sizes is hard to trust). 
5. I like the analysis of inter-participant embeddings (section 5.3 and Figure 7) since this is agonistic to subject-level tasks.  However, looking at Figure 7 it feels “wrong” that PaPaGei-S has some non-negligible density for distance <0.  Is this an artifact of distribution smoothing?   As an alternative to the pairwise distance distribution, it could also be informative to evaluate other measures of unsupervised embedding quality such as Rankme (or similar).  
6. I’m not sure if I understand some of the language used in the Skin Tone Analysis section, specifically the phrase “however, there are no significant differences across all models” in reference to Figure 9.    Does “no significant differences across all models” refer to a comparison of light skin tones vs. dark skin tones (grouping models), or does it refer to model-to-model differences for dark skin tones vs. light skin tones, or to something else?  It would help if this can be stated with more precise language.  
7. For Figure 9, it would also be informative to plot the confidence intervals as whiskers on the bar plot.  This would make it more clear (visually) whether the model-to-model differences are significant.

### Soundness
3

### Presentation
4

### Contribution
3
