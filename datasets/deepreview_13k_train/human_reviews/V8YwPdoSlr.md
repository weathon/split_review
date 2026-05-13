# Capturing Static, Short-Term, and Long-Term Dynamics Through Self-Supervised Time Series Learning: CHRONOS

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Time series data presents a rich tapestry of temporal patterns, encompassing both enduring static trends that persist throughout the entire temporal sequence and dynamic patterns that define its evolving nature. To advance the field of Self-Supervised Learning (SSL) in time series analysis, it is essential to adopt a comprehensive approach that considers these distinct temporal facets. In this paper, we introduce Contrasting Heads Represent Opposed Natures of Signals (CHRONOS), a novel SSL methodology which drives the model to understand three distinct temporal attributes – static, short-term dynamics, and long-term dynamics. This is achieved by projecting the representations into two separate spaces, employing contrasting heads. Furthermore, a selective optimization leads distinct model units to be specialized in different temporal natures. To evaluate the effectiveness of CHRONOS, we applied this methodology to the analysis of electrocardiagram (ECG) signals across four distinct downstream tasks, utilizing four independent datasets. Our study demonstrates the consistent performance of CHRONOS across all tasks, surpassing state-of-the-art methods for time series data analysis. CHRONOS serves as a testament to the importance of capturing diverse temporal aspects of time series data for driving versatile models capable of consistently excelling in a wide spectrum of downstream tasks

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new self-supervised learning (SSL) approach called CHRONOS for time series analysis, aimed at capturing static, short-term, and long-term dynamics in time series data. CHRONOS distinguishes itself by projecting data representations into two spaces and optimizing selective model units for each temporal aspect. The method has been evaluated on electrocardiogram (ECG) signal tasks such as arrhythmia detection, gender identification, and age estimation, showing it can surpass existing methods.

Key concepts include the identification of unique static patterns as biometric identifiers, the volatility in short-term dynamics for immediate physiological changes, and the gradual change observed in long-term dynamics related to slow-evolving characteristics like age or cholesterol level. CHRONOS extends the DEBS approach by using three types of loss functions for distinct temporal representations and captures the evolution over significant time gaps, enhancing the ability to understand and utilize physiological signal patterns for diverse health-related analyses.

### Strengths
1/ The authors introduce a new self-supervised learning method that incorporates observations about the nature of temporal data on medical ECG-based tasks which show three different major characteristics: static, short-term dynamics and long-term dynamics. By introducing multiple projection heads for contrasting the static and dynamic characteristics the model is able to learn more about the importance of different features for multivariate time series predictions.
2/ The authors explain the implementation and evaluation setup in detail, showing empirical performance comparisons that have an increase in performance against previous work.

### Weaknesses
1/ The authors frame the work as generalizing to other applications besides medical ECG however it seems most of the motivation for the design of CHRONOS is very grounded in the specifics of ECG datasets and the provided tasks with references to medical-specific features, model selection, and dataset characteristics. The claim of generalizability is not sufficiently supported by the current evaluation. An expansion of the evaluation to standard time series benchmarks like the UCR archive, or the FD-a and FD-b tasks used to evaluate TF-C, is necessary to demonstrate the broader applicability of the proposed method. The current evaluation is limited to ECG data and tasks, making it difficult to assess the true potential of CHRONOS for other time series domains.
2/ There are a number of existing time-series specific transformer applications. FormerTime (Cheng, et. al., 2023), for example, also focuses on multi-scale time series dynamics for multivariate time series classification, albeit without self-supervised learning. The authors should consider evaluations against these time-series specific transformer models such as Formertime and Informer to see if their proposed method continues to add benefit or if simply updating the encoder they use could lead to improvements across all the tasks evaluated using standard self-supervised learning. The lack of comparison with these state-of-the-art time series models makes it difficult to assess the relative contribution of CHRONOS.
3/ The figures with feature importance and overlap of features for the static and dynamic cases could benefit for my explication of which features were included (e.g. by including the feature name instead of its number). Without knowing what the features represent, the interpretation of the feature importance and overlap is limited. The lack of feature names makes it difficult to understand the specific aspects of the time series that the model is learning.

Nits:
1/ All the references are improperly included in the text. I believe you should change from using `citet` to `citep` in most cases. References should include the author names in the sentence (e.g. “Additionally a SHAP Analysis *as proposed by* Lundberg & Lee (2017) is carried out”) or by including the author names in the citation (e.g. “Additionally a SHAP Analysis (Lundberg & Lee, 2017)...”). Please read the “Citations in Text” part of the provided LaTeX template for more information.
2/ “Short-term” vs “short term” and “long-term” vs “long term”.

### Questions
1/ Could the authors expand on the implications of the ablation study conducted in section 5? For example: it’s not clear why the removal of the long term loss was only evaluated when the time scale ratio was set to 25/50/25 (basides this being the ratio chosen during selective optimization). Would the long term loss add more benefit in the case where the long-term ratio is higher than 25?
2/ As an additional ablation, have the authors considered removing the selective optimization and randomly selecting a loss function at each step of the pre-training process? 
3/ In the SSL time series literature, pre-training on the Sleep Heart Health Study is quite common. Why do the authors believe this dataset is more or less useful for pretraining given the tasks at hand? Have the authors tried pre-training on any other datasets?

### Soundness
2 fair

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
The manuscript introduces the CHRONOS framework, which integrates self-supervised learning with the teacher-student paradigm for knowledge transfer, incorporating insights from novel pretraining approaches such as BYOL. The goal of CHRONOS is to extract three types of temporal information, static, short-term, and long-term, to analyze ECG signals. The authors tested their method on four tasks, including gender identification, age regression, AFib Classification, and the Physionet Challenge. The authors report a comparable performance and, in some cases, outperform the methods of Mixing-Up, TF-C, PCLR, BYOL, and DEBS.

### Strengths
The manuscript provides genuine ideas that have the potential to contribute significantly to the field. Concerning originality, the CHRONOS framework innovatively integrates self-supervised learning with the teacher-student paradigm for knowledge transfer, incorporating insights from novel pretraining approaches such as BYOL. Modeling, static, short-term, and long-term dynamics are not fully explored in the literature, and it might be interesting to explore the framework for other application domains, like video analysis, where temporal information is crucial.

Overall, the quality of the work is adequate, with details in the presentations, guidance to the reader, and a definition of the experimental design. CHRONOS was assessed across four independent datasets and an array of downstream tasks, showing versatility and robustness. On the other hand, despite some improvements discussed in the weakness section, the manuscripts communicate complex ideas and provide a framework that knowledgeable readers of the field can understand.

### Weaknesses
While the manuscript brings some exciting concepts, considerable deficiencies impact its overall quality and academic contribution. These concerns range from fundamental issues in writing and clarity to more profound matters regarding structure, content authenticity, and methodology. Below, I detail these weaknesses to provide clear guidance for necessary improvements and to ensure the work aligns with the high standards of the conference.

The manuscripts present some details related to structure and content, including:
•	The introduction lacks citations, crucial for situating the research within the existing body of knowledge.
•	The related work section needs to include more details of the current state of the field, failing to discuss current challenges and the advantages and disadvantages of existing methods. Its brevity and lack of depth need to adequately show how this new approach contributes to or differs from the state-of-the-art.
•	The absence of intuitive explanations for the proposed methodology's expected effectiveness is a significant omission.
•	The caption of the figures could be improved to be self-contained.


The manuscript must be revised since minor typos and grammar mistakes impact its presentation. Also, the structure of some sentences and fluency make them difficult to follow. For example:

•	In the abstract, the authors use the word "electrocardiagram"; it should be "electrocardiogram."
•	The phrase "throughout the entire temporal sequence" is somewhat redundant. "entire" and "throughout" imply the full length of the time series. It might be more concise to say "throughout the temporal sequence" or "throughout the entire sequence."
•	The phrase: "In this paper, we introduce the Contrasting Heads Represent Opposed Natures of Signals (CHRONOS), a novel..." can be slightly improved for clarity and flow to "In this paper, we introduce the 'Contrasting Heads Represent Opposed Natures of Signals' method, hereafter referred to as CHRONOS." or "In this paper, we introduce CHRONOS (Contrasting Heads Represent Opposed Natures of Signals), a novel..."
•	The authors define the SSL and CHRONOS acronyms in the abstract, but it is considered good practice to redefine them upon their first use in the main text of the document.
•	"a SSL methodology" should be "an an SSL methodology". Remember that the choice depends on the sound that immediately follows.
•	The hypothesis is wordy and can be simplified for clarity.
•	In the introduction, the authors state "timeseries data", while it should be "time series data".
•	The phrase "...patterns belonging to three distinct temporal dynamics; static, ..." the ";" should ":".
•	Some statements are vague and biased. For example, "achieve excellent performance" and "attain good results" do not clearly understand what excellent and good means in this context and reflect the authors' opinion.

Throughout the document, several sentences need refining to improve the manuscript's clarity. While it is impractical to address each one through this medium, a comprehensive review of the entire document is recommended to improve readability and precision.

Furthermore, it would greatly benefit the manuscript to include a clear description of sections in the introduction, providing readers with a roadmap of what to expect in each area and linking it to each subsection. A short introduction in each section, especially Sections III and IV, is welcome to clarify the reader's expectations.

The manuscript has similarities with previous studies, especially the DEBS study. Can you clarify the novel aspects of CHRONOS that distinguish it from the prior work? What specific innovations does CHRONOS introduce?

It has been noted that certain sections closely resemble sections of the DEBS paper on ArXiv without clear referencing. How do you address this similarity, and can you ensure that all reused content is properly credited?

### Questions
The manuscript must be revised since minor typos and grammar mistakes impact its presentation. Also, the structure of some sentences and fluency make them difficult to follow. For example:

•	In the abstract, the authors use the word "electrocardiagram"; it should be "electrocardiogram."
•	The phrase "throughout the entire temporal sequence" is somewhat redundant. "entire" and "throughout" imply the full length of the time series. It might be more concise to say "throughout the temporal sequence" or "throughout the entire sequence.
•	The phrase: "In this paper, we introduce the Contrasting Heads Represent Opposed Natures of Signals (CHRONOS), a novel..." can be slightly improved for clarity and flow to "In this paper, we introduce the 'Contrasting Heads Represent Opposed Natures of Signals' method, hereafter referred to as CHRONOS." or "In this paper, we introduce CHRONOS (Contrasting Heads Represent Opposed Natures of Signals), a novel..."
•	The authors define the SSL and CHRONOS acronyms in the abstract, but it is considered good practice to redefine them upon their first use in the main text of the document.
•	"a SSL methodology" should be "an an SSL methodology". Remember that the choice depends on the sound that immediately follows.
•	The hypothesis is wordy and can be simplified for clarity.
•	In the introduction, the authors state "timeseries data", while it should be "time series data". 
•	The phrase "...patterns belonging to three distinct temporal dynamics; static, ..." the ";" should ":".
•	Some statements are vague and biased. For example, "achieve excellent performance" and "attain good results" do not clearly understand what excellent and good means in this context and reflect the authors' opinion.

Throughout the document, several sentences need refining to improve the manuscript's clarity. While it is impractical to address each one through this medium, a comprehensive review of the entire document is recommended to improve readability and precision.

Furthermore, it would greatly benefit the manuscript to include a clear description of sections in the introduction, providing readers with a roadmap of what to expect in each area and linking it to each subsection. A short introduction in each section, especially Sections III and IV, is welcome to clarify the reader's expectations.



The manuscript must be revised since minor typos and grammar mistakes impact its presentation. Also, the structure of some sentences and fluency make them difficult to follow. For example:

•	In the abstract, the authors use the word "electrocardiagram"; it should be "electrocardiogram."
•	The phrase "throughout the entire temporal sequence" is somewhat redundant. "entire" and "throughout" imply the full length of the time series. It might be more concise to say "throughout the temporal sequence" or "throughout the entire sequence.
•	The phrase: "In this paper, we introduce the Contrasting Heads Represent Opposed Natures of Signals (CHRONOS), a novel..." can be slightly improved for clarity and flow to "In this paper, we introduce the 'Contrasting Heads Represent Opposed Natures of Signals' method, hereafter referred to as CHRONOS." or "In this paper, we introduce CHRONOS (Contrasting Heads Represent Opposed Natures of Signals), a novel..."
•	The authors define the SSL and CHRONOS acronyms in the abstract, but it is considered good practice to redefine them upon their first use in the main text of the document.
•	"a SSL methodology" should be "an an SSL methodology". Remember that the choice depends on the sound that immediately follows.
•	The hypothesis is wordy and can be simplified for clarity.
•	In the introduction, the authors state "timeseries data", while it should be "time series data". 
•	The phrase "...patterns belonging to three distinct temporal dynamics; static, ..." the ";" should ":".
•	Some statements are vague and biased. For example, "achieve excellent performance" and "attain good results" do not clearly understand what excellent and good means in this context and reflect the authors' opinion.

Throughout the document, several sentences need refining to improve the manuscript's clarity. While it is impractical to address each one through this medium, a comprehensive review of the entire document is recommended to improve readability and precision.

Furthermore, it would greatly benefit the manuscript to include a clear description of sections in the introduction, providing readers with a roadmap of what to expect in each area and linking it to each subsection. A short introduction in each section, especially Sections III and IV, is welcome to clarify the reader's expectations.


The manuscript has similarities with previous studies, especially the DEBS study. Can you clarify the novel aspects of CHRONOS that distinguish it from the prior work? What specific innovations does CHRONOS introduce?

It has been noted that certain sections closely resemble sections of the DEBS paper on ArXiv without clear referencing. How do you address this similarity, and can you ensure that all reused content is properly credited?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an approach for feature learning from ECG signals. Specially, the author proposed to decompose the signal into three separate components: static, long-term, and short-term via a formulated contrastive loss.  Four datasets obtained from varying sources were used in their evaluation.

### Strengths
+ Efforts made to study learned features from their dynamics across recordings and importance in predicting for different types of learning tasks. 
+ Ablation study was performed for some of the components in the proposed model

### Weaknesses
 - The writing of the paper is very confusing. The authors described two distinct spaces, static and dynamic. However, Eq. (5) involves the calculation of the inner product between vectors from the two spaces, which indicates there is in fact only one space. Also, based on the description, it seems that the authors attempted to differentiate three types of temporal dynamics: static, short-term, and long-term. However, the proposed model only learns two types of representations, static and short-term.

 - The description of the proposed method lacks clarity. For example, what is the relationship between projector and predictor and that between teacher and student networks. The proposed architecture includes encoder(s), projectors, and predictor. What exactly the representation used in downstream prediction task is not clear.

 - The loss functions are not clearly motivated, or least need more explanation. For example, why two different records are used and why projection and prediction are compared while not both projections in Eq. (2). What are i and j in Eq. (3)? Hyperparameters? How were they determined?

 - It seems to me that the proposed set of loss functions is problematic, leading to representation that has no discriminative capability across recordings. Eq (2) and Eq (3) drive similarity only and Eq (5) only encourages difference in learned dynamic and static features. What really helping here may be the covariance loss function (Eq. (6)), which needs more explanation and deserves an ablation study.  

 - The empirical results are relatively weak across the board. Statistic tests are needed in Table 1 (small difference in mean but with large variance) to show whether the differences have statistic significance.

### Questions
Refer to the list of weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a new self-supervised method for medical time series. Their method, CHRONOS, aims to separate features with different temporal granularity explicitly. For that, they propose three objectives, static, short-term, and long-term dependency, using different projection heads between static and dynamic features. The authors also come up with a specific regularization scheme at training called "selective optimization" relying on masking the lowest quantile of features (or highest depending on the objective) in terms of similarity with the anchor when computing the objective. They evaluate their method on ECG data on tasks specifically relying on static or dynamic features.

### Strengths
### Overall useful, positive and well detailed experiments

- The experiment section (except for the feature analysis) is clear and well-organized. 
- The overall performance gain with respect to the considered baseline is noticeable. 
- The authors proposed an ablation study with respect to their long-term term and the usage of selective optimization
- The evaluation of tasks requiring different types of features is a great idea.

### Some interesting ideas in the method

- I appreciate the idea of using different "predictors" for different temporal granularity to better handle adversarial objectives.

### Weaknesses
Unfortunately, this work presents some major weaknesses which lead me to recommend for rejection.

###  Grossly insufficient related work
The literature review effort of the field from the authors is extremely small.
Between their introduction and their related work, the authors **only cited four works**. However, the field of SSL for time series is much richer. To cite a few:
- Franchesci et al. Unsupervised scalable representation learning for multivariate time series NeurIPS, 2019
- Cheng et al. "Subject-aware contrastive learning for biosignals", 2020
- Mohsenvand  et al. "Contrastive representation learning for electroencephalogram classification", Machine Learning for Health, 2020
- Tonekaboni et al. "Unsupervised representation learning for time series with temporal neighborhood coding" ICLR 2020
- Kiyasseh et al. "Clocs: Contrastive learning of cardiac signals across space, time, and patients" ICML, 2021
- Yeche et al. "Neighborhood contrastive learning applied to online patient monitoring" ICML, 2021
- Eldede et al.  "Time-series representation learning via temporal and contextual contrasting", IJCAI, 2021
- Fan et al. "Semi-supervised time series classification by temporal relation prediction" ICASSP, 2021

### Clarity in the method 

- The authors don't have a part where they introduce precise notations even though the authors use a lot of different notations. This contributes to making the reading quite complicated and leaves some parts of the method unclear to me.


- In addition, the figures don't have descriptive captions. Typically, except for the colors, no description is given for the numerous components of Figure 1. Conversely, in Figures 2 and 3, no explanation is given regarding the coloring scheme.

### Some missing experiments

- The authors use a covariance loss borrowed from VICReg but do not provide ablation for that component. Hence it's impossible to know if performance improvement comes from the disentanglement of the dynamic and static features proposed by the authors or this additional regularization. 
- Similarly, the authors propose to use two projection spaces instead of one because of the adversarial nature of their objectives. Unfortunately, they do not provide an experiment justifying this choice over a unique space.
- The authors introduce a window parameter for their short-term loss. They don't provide ablation for it.

### Questions
I have the following questions:

- Why report specificity and sensitivity and not AUROC directly? Using AUROC prevents the performance from being biased by potential miscalibration of a model. 
- What is the meaning of the colored bars in Figures 2 and 3?
- Why carry constants in your loss terms that will have no impact on gradient?  "1 +  " or  "1 -"

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
