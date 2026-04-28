# Toward Foundation Model for Multivariate Wearable Sensing of Physiological Signals

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Time-series foundation models have the ability to run inference, mainly forecasting, on any type of time series data, thanks to the informative representations comprising waveform features. 
Wearable sensing data, on the other hand, contain more variability in both patterns and frequency bands of interest and generally emphasize more on the ability to infer healthcare-related outcomes. The main challenge of crafting a foundation model for wearable sensing physiological signals is to learn generalizable representations that support efficient adaptation across heterogeneous sensing configurations and applications. In this work, we propose NormWear, a step toward such a foundation model, aiming to extract generalized and informative wearable sensing representations. NormWear has been pretrained on a large set of physiological signals, including PPG, ECG, EEG, GSR, and IMU, from various public resources. For a holistic assessment, we perform downstream evaluation on 11 public wearable sensing datasets, spanning 18 applications in the areas of mental health, body state inference, biomarker estimations, and disease risk evaluations. We demonstrate that NormWear achieves a better performance improvement over competitive baselines in general time series foundation modeling. In addition, leveraging a novel representation-alignment-match-based method, we align physiological signals embeddings with text embeddings. This alignment enables our proposed foundation model to perform zero-shot inference, allowing it to generalize to previously unseen wearable signal-based health applications. Finally, we perform nonlinear dynamic analysis on the waveform features extracted by the model at each intermediate layer. This analysis quantifies the model's internal processes, offering clear insights into its behavior and fostering greater trust in its inferences among end users.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces NORMWEAR, a foundation model for multivariate wearable physiological signals. NORMWEAR uses continuous wavelet transforms and channel-aware attention to learn robust representations from diverse sensor types. Evaluated on various downstream healthcare tasks, it outperforms existing baselines. A novel fusion mechanism enables zero-shot inference for custom health applications. The authors also provide an interpretability analysis using feature visualization and nonlinear dynamics.

### Strengths
- The paper tackles the important and under-explored area of foundation models for multivariate wearable physiological signals. Existing foundation models for time series often struggle with the specific challenges of this data type, such as variability in patterns, frequency bands, and sensor combinations.

- The proposed NORMWEAR model incorporates thoughtful design choices, including CWT-based multi-scale representations, channel-aware attention, and a zero-shot inference mechanism. These components appear well-suited to address the complexities of wearable physiological data.

- The authors evaluate their model on a diverse set of downstream tasks spanning mental health, body state inference, biomarker estimation, and disease risk evaluation. This provides a holistic assessment of the model's capabilities.

- The paper emphasizes model interpretability through feature visualization and nonlinear dynamic analysis. This is a crucial aspect for building trust and understanding the model's behavior in healthcare applications.

- NORMWEAR demonstrates superior performance compared to Chronos, a state-of-the-art language-based foundation model, and a vision-based ViT baseline.

### Weaknesses
 - Limited size of the pre-training dataset: The relatively small size of the pre-training dataset (around 37,000 samples with a limited number of subjects in several datasets) raises concerns about the model's ability to generalize effectively. Similar works often utilize significantly larger datasets with tens or hundreds of thousands of participants. This limitation needs to be acknowledged and addressed more thoroughly. How does this limited dataset size impact the robustness of the learned representations?

- Lack of simple statistical baselines: While comparison with Chronos and ViT provides valuable context, the inclusion of simpler statistical feature baselines would strengthen the evaluation and help establish a lower bound on performance. Also, comparisons with existing self-supervised baselines like BYOL, TF-C, or SimCLR would position this work better within the literature. This would give a clearer picture of the added value provided by the complex architecture.

- Insufficient information on dataset selection: The rationale behind the selection of pre-training and downstream datasets is not clearly articulated. Why were certain larger datasets reserved for downstream evaluation only? The paper mentions limited information on one of the datasets (BP with 1000 users) and should clarify its origin (self-collected or public). The provenance of all datasets should be explicitly provided, ideally with inline references within Tables 3 and 4.

### Questions
1. Impact of dataset size: Could the authors elaborate on the potential impact of the limited pre-training dataset size on the model's generalization performance? Are there plans to expand the pre-training dataset in future work?

2. Model Release: Given the lack of openly released models in this domain, I strongly encourage the authors to publicly release their model and code to facilitate future research and comparisons.

3. Tokenization terminology: The use of "tokenization" might be confusing, given its association with language models. "Pre-processing" or "feature extraction" might be more suitable terms in this context. Could the authors clarify their usage of this term?

### Soundness
3

### Presentation
2

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
The paper introduces NORMWEAR, a foundation model designed to address challenges in processing multi-modal wearable sensing data for healthcare applications. NORMWEAR can process diverse physiological signals, such as ECG, EEG, and PPG, by leveraging an innovative tokenization approach and a channel-aware attention mechanism, which together enable it to handle multivariate data efficiently. Additionally, NORMWEAR is capable of zero-shot inference, achieved through a representation alignment technique. This allows the model to interpret and apply its insights to new health-related applications without needing to be retrained, making it highly adaptable to different contexts. Through an evaluation across 12 different health downstream tasks, NORMWEAR has shown improvements over baseline time-series models.

### Strengths
* The fusion approach is interesting and well studied. There are multiple ablations showing the strength of each of these approaches, and they are well thought through and explained. This addresses an important problem within the space, in which the type and # of modalities will be inconsistent.
* The tokenization approach is interesting and well-justified, using prior work from the biosignal space to justify each of the steps. This addresses an critical problem within our space to identify better time-series tokenization methods. Further experimentation and ablations on the tokenization method would have been appreciated though.
* Good results on many datasets. The multitude of very different tasks shows a generalization zero-shot performance of the model, which is quite notable.

### Weaknesses
 * Semantic alignment training procedure is unclear
	* After pre-training the backbone encoder, the embedding space is aligned with the semantic text. However, I cannot seem to understand how this is done nor what datasets are used (i.e. are they the same as the pre-training datasets?). This seems to be a critical aspect of the model in order to enable zero-shot performance, but little detail is given. Two papers are cited, Zhang et al., 2024; Liu et al., 2024, but they do not seem to imply one specific approach. 
* Insufficient baselines
	* It is argued that chronos is a SOTA method, however, as noted, chronos was designed for time-series forecasting, which none of the downstream tasks are.
	* The ViT baseline is not well explained in how it is set up to do zero-shot downstream, including it's learning objective.
	* Ideally, the baselines should encompass the SOTA method for a given task, so as to understand how this model compares against each task specifically. The scope of the paper is "towards" a foundation model so this isn't a hard requirement, but would be nice. 
* Many model components in the Memory Stream Inspired Mechanism in Sec 2.4 are not clearly explained
	* In MSiTF, it is argued that the representations are optimized for human sensing, how does this occur, specifically? This is not justified clearly. In Fig. 3, standard deviation and mean are used, but this does not seem to be explained in this section.
	* How is recency score important? It is stated that the further the time-step to the most recent time step, the lower te score, what time steps are being considered here? It is not clear, especially because the query is text and key/values are embedding time-series, and thus on different time scales.
	* Importancy score seems to act as a gate for the inputs time stamps, but it is not explained how the gate determined to be on or off.
	* The text states that final score is a summation, but how are scores used? According to Fig. 3., it looks like the scores operate independently from each other in different model components, rather than being summed together. 
	* In Eq. 1, it seems like there are two loss components, a l1 loss and cosine distance. Why are they both used together when they both work towards increasing similarity between Y and \hat{Y}? There is no text nor empirical results justifying this.
* Experimental results are somewhat lacking
	* No experimental results showing the strength of their tokenization method compared to a simple Conv1d tokenizer.
	* Only having one metric reported makes it difficult for us to understand whether the performance gain is consistent.
	* In Fig. 4a), t-SNE clusters of the different classes being different is not too surprising, as each signal is quite different, so it would be nice to understand visualize and understand how the model is able to capture differences among specific classes or specific risk levels. 
	* In Fig. 4b), it is unclear what the visualizations extracted by the intermediate layer imply and how they show that the model has learned meaningful information.
* Lack of a prior work section makes it very difficult for readers to understand where this work sits within the greater foundation model space. 
* Figures are hard to follow. Some ideas are introduced in the figures, but do not seem to be explained in the main text.
	* In Fig. 3, Mean/Standard Deviation + Likelihood Parameters are not explained in the main text.

### Questions
Please seek weaknesses above.

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces NormWear, a common foundation model for various physiological signals such as PPG, ECG, EEG, GSR and IMU. Authors have pre-trained NormWear on a dataset containing these different physiological modalities, and performed several downstream comparisons with off-the-shelf time-series and image encoders. They have also investigated different components of NormWear, different modality fusion techniques, and a way to align NormWear embeddings with text embeddings for zero-shot classification.

### Strengths
* The idea proposed in this paper is interesting: to have one common foundation model for various physiological signals.
* Authors investigated different components of NormWear in terms of dynamics in different layers, visualizations of features and embeddings.
* Authors investigated different fusion techniques to fuse multi-modal tokens/embeddings.

### Weaknesses
 * In general, I believe the quality of the writing, presentation and conclusions in the paper can improve significantly. There are several unbacked claims and missing details throughout the paper (see below), which make the paper very hard to follow. I highly suggest authors consider revising the manuscript write up to provide a better flow and additional information. I have done my best to provide several examples in below, but I’m sure there are more improvements that can be made. 

* The number of subjects in the pre-training and evaluation datasets makes the conclusions intransferrable to large datasets for claims of “NormWear as a foundation model”. A foundation model is really a generalist model that can perform well on a variety of corner cases and downstream applications. Some modalities (e.g. EEG) have less than 50 pre-training/evaluation subjects, for example, their evaluation of “Driver Fatigue detection” has only 12 * 20% = [2-3] subjects in the test set, which is very low to conclude generalizable performance and conclusions for health applications. I believe this weakens the conclusion of NormWear being “[the first] *foundation model* specifically designed for wearable sensing data, capable of processing any number of multivariate signals from sources such as the heart, skin, brain, and physical body.”. I recommend the author revise the language or provide additional empirical back up for NormWear being a foundation model.
* There are a variety of inadequate references and claims throughout the paper. I recommend authors take a pass through the claims in the paper and revisit them as needed. I provide some examples below:
    * “Despite the great potential of these works across various tasks such as forecasting, anomaly detection, and classification, they are not easily transferable to wearable health applications for two main reasons“: Transformers with images or spectrograms, have been previously used for physiological signals, so authors may reconsider this claim [1], [2]. 
    * “When modeling this type of data, relying solely on modality-specific backbone feature encoders, such as RNNs (Yu et al., 2019) or transformer-based (Vaswani et al., 2023) neural networks, is insufficient. Therefore, it becomes essential to incorporate established signal processing techniques, such as the short-term Fourier transform (Brigham, 1988) and wavelet transform (Torrence & Compo, 1998)”. It would be great if authors justify these claims. To the best of my knowledge, Transformers (without Fourier transforms) are widely used for physiological signals, and it is not clear to me how transforming the time-series to frequency domain, can remove modality-to-modality variations. If authors provide theoretical/empirical justification for this, it can improve the motivation. 
    * “Nevertheless, this method completely ignores information in the frequency domain, leading to significant information loss and suboptimal performance in downstream tasks.“: In my opinion, this is incorrect. Just because a model is trained on time domain, does not mean it *completely ignores information in frequency domain* as there’s a duality between frequency and time domain. I suspect authors may have meant to claim that it’s easier to capture certain frequency-related information if the input in frequency domain is directly given to the model. If yes, it’s a different claim, but please note that a powerful enough encoder with enough data, should be able to capture frequency-related information from time-domain input as well. I recommend authors provide more empirical/theoretical evidence for this claim, or reconsider the writing. 
    * “Another important point to consider is that although empirical studies (Nie et al., 2023; Abbaspourazad et al., 2023) show that channel-independent structures effectively capture local patterns, they fail to account for relationships across channels.”: Please provide reasoning for such claims, it’s not clear to me how these conclusions are made from these prior papers.  
    * “In order to stay consistent with the literature on foundational representation learner (Devlin et al.,2019; Dosovitskiy et al., 2020; Gong et al., 2021), the backbone of our proposed model consists of a convolutional patching layer followed by 12 standard Transformer blocks (Vaswani et al., 2023).”, there are a lot of different representation learning approaches (masked auto encoder, variational auto encoders, contrastive learning, autoregressive pre-training, ...), so perhaps authors can more accurately rewrite this sentence. 
    * “With the state-of-the-art (SoTA) back- bone model for modeling time series data, each intermediate layer will output tensors that contain the timestamp dimension”, what does this mean? Can authors provide back up for this claim or provide more information?
    * “Such a visualization pipeline can assist researchers and clinicians by offering insights into how the model reaches its final predictions” It’s not clear to me whether these visualizations provide any gradient signal or they’re random. To the best of my knowledge, the relationship between PPG and diabetes is not well-understood, so not sure if I can directly conclude that the shown results match with the well-known concepts in the literature. It would be great if the authors can relate this to the literature and present the efficacy of their visualization method.
    * “However, recent works have shown that features extracted from deep learning methods generally outperform handcrafted features in most cases (Yan et al., 2023a; Krizhevsky et al., 2012; Luo et al., 2024).”. I’m not sure how AlexNet is relevant to tokenization discussion in Section 2.2 here, also not very recent :). Can the authors reconsider the discussion here. 


* Many important details of technical implementation is missing from the paper, I recommend the authors incorporate all necessary information to aid the reader. I provide few examples below:
    * Information about how patches are selected and how many patches are there for each segment, appear to be missing.
    * Architectural hyperparameters regarding the tokenizer, the reconstruction module (de-tokenization), the details of the encoder/decoder transformer (token dimension, number of attention heads, positional encoding, dimension of MLP hidden layer, normalization, ...) appear to be missing.
    * The details regarding the downstream evaluations (linear probing) appear to missing 
    * The details about how sentences are chosen in Section 3.2, what language model (or encoder) was used to get the “question semantic” embeddings appear to be missing.
    * Hyperparameters of equation 1/2 and L295-311 appear to be missing from the paper.
    * Details of masking strategies in Table 8 are missing.
* Several major claims in the paper seem overstated. For example, the delta between NormWear and Chronos in Table 1 seems very small considering that Chronos is not even a proper foundation model on physiological signals (Chronos is just a model trained on some time-series datasets, and to the best of my knowledge, there’s no prior work showing that Chronos is even close to SOTA for physiological signals such as PPG/ECG/EEG). Despite this shortcoming for Chronos, its difference between NormWear in the first 8 evaluations is very small, and in some cases it is even better. Similarly, authors make several big claims about processing frequency domain and CWT (see examples above), however, in Table 9, they show that the difference between processing with CWT vs. raw input is not that much (76.25 vs. 78.27). I recommend authors provide further explanation/discussion regarding these claims.
* It would be great if the authors provide details about how confidence bounds are selected in Tables, e.g., Table 1. It is surprising that they get such narrow confidence bounds with such small N (e.g., 2/3 for Driver Fatigue detection if I understand correctly)? 
* Please consider fixing typo and formatting issues, for example:
    * L42: missing space
    * L157: missing space. 
    * Table captions not being above the tables.

### Questions
* What is the justification for two hyperparameters in equation (1)? Is this loss used in conjunction with another loss, and if not, it appears that one hyperparameter is enough? 
* It appears that Table 10 was not referred to in the text, can authors provide more information about it?

### Soundness
2

### Presentation
1

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
This paper presents and evaluates a general methodology for pre-training foundation models (intended for use with physiological signal streams) that can accept multivariate inputs and output model embeddings that are useful for multiple downstream tasks, all related to physiological measurements.   The model family (NormWear) is novel and original in that it is specifically intended to accept multiple signal inputs and behavior in a signal-agonistic manner.   

Downstream performance evaluation is reported for 12 different tasks using several different publicly-available data sets.  Additionally, the authors describe a method for using NormWear in a zero-shot learning context and report performance for the 12 downstream tasks.  Lastly, the authors describe two strategies aimed at enabling model interpretability:  analyzing ‘Feature Associations’ and ‘Time Step Relevance’, as well as nonlinear dynamics (chaos system analysis) within the model layers using different signal inputs.

### Strengths
This paper represents strong contributions in the following areas: 

**Originality:** This idea is novel among publications related to physiological/biological sensing.  I have not seen any past published examples of work (in this domain) aimed at developing foundation models for a variety of multi-modal signal inputs. 

**Clarity:**  The authors clearly communicated their methods and objectives for evaluating performance on downstream tasks.  


**Additionally the authors should be commended for two important things:**
1. They leveraged public and freely-available data sets and provided enough information/references for a reader to locate the corresponding data, making it straightforward for a reader to obtain the data and do their own analysis on it.  
2. They shared their codebase directly in the submission, making it possible for the reader to understand in detail how they did the performance evaluations on each downstream task.

### Weaknesses
## Issue 1: Weak Baselines 

In Section 3.1 and Table 1, the authors report that NormWear achieves the best performance across tasks.  However, this is limited in part by their choice of baseline models (and general modeling approaches) to compare against NormWear.    This makes it very difficult to determine whether the novel method (NormWear) actually represents a meaningful improvement in downstream task performance vs. representing a small or negligible improvement over a poor reference baseline.  


### Potential ideas addressing this issue:
In general, novel modeling approaches should be compared against simple baseline methods such as logistic regression, random forest, or even constant predictor (“guessing the mean”), in addition to comparing against SOTA methods). In regression tasks, the performance for a mean predictor can indicate the “floor” for performance without utilizing any modeling. 

## Issue 2: Poor model performance compared to simple baselines 

Fortunately, the authors utilized open and freely-accessible data sets for their downstream evaluation. This made it possible for me to spot check the performance of very simple baseline models on several of the tasks.  Due to time limitations I could not do this analysis for every task, but was able to do it for a majority of tasks (7 of the 12 tasks listed in Table 1).  I took care to use the same data set (sourced from the authors’ reference list in Appendix A) and used identical performance metrics reported by the authors (leveraging their accuracy metrics calculations for regression and classification tasks as shown in the evaluate() function on lines 123-138 of engine_linprob.py).  For the following tasks and datasets I observed equivalent or superior performance to what is reported in Table 1, using a very simple method in each case: 

Hemoglobin Estimation (regression): I observed accuracy = 88.68 using a constant (mean) predictor. This is significantly better than the best NormWear model, indicating that NormWear performs worse than simply guessing the mean.  

Fetal Heart Rate Estimation (regression): I observed accuracy = 96.31 using a constant (mean) predictor.  It is also possible to achieve accuracy=96.38 using a single value (140.0) that I obtained by googling “what is typical fetal heart rate at 20 weeks”.  Both of these are higher accuracy than the best NormWear model.  

Blood Pressure Estimation (classification):  I observed accuracy = 91.49 (statistically equivalent to the best NormWear model) using a simple bivariate linear regression model with terms for Age and BMI . 

For the following 4 Risk Evaluation tasks I used a simple logistic regression model (sklearn.linear_model.LogisticRegression) with only demographic inputs (Age, BMI, sex): 

Hypertension Risk Evaluation (4-class classification): ROC AUC = 0.720, significantly better than the best NormWear model.
Diabetes Risk Evaluation (binary classification): ROC AUC = 0.672 (not as good as NormWear with CLS attention, but significantly better than all other baselines). 
Brain Stroke Risk Evaluation (binary classification): ROC AUC = 0.792, significantly better than the best NormWear model.
Brain Disease Risk Evaluation (3-class classification): ROC AUC = 0.779, significantly better than the best NormWear model.


Additionally, in the zero-shot performance (Table 2) for several tasks even the best model does not perform much better than random guessing.  For example in the ‘Heartbeat abnormal Detection’ task all models achieve ROC AUC <0.5 (worse than guessing).  For Emotion Classification, Valence-Arousal Prediction, Driver Fatigue Detection, Hypertension Risk Evaluation and Diabetes Risk Evaluation no models achieve ROC AUC>0.60.  For hemoglobin estimation and fetal heart rate estimation, all zero-shot models perform significantly worse than simply guessing.  

This poor level of performance suggests that the models may not actually be learning anything relevant for zero-shot inference. 

### Potential ideas to address this issue:
Choose an adequately strong and simple/interpretable baseline model for each task-- for example, this could even be as simple as using a mean predictor on the regression tasks, or using an age-based predictor for the classification tasks.  Then compare the performance of each new model against the simple baseline. Highlight cases that represent significant performance improvements over the simple baseline.  For downstream tasks that show no improvement over the baseline, consider removing these from the paper (or doing additional experiments and development on the model until it significantly outperforms the baseline). 

 
## Issue 3: Lack of discussion relating to visualization/interpretability

In figure 4 the authors present a graphical summary of their visualization and model interpretation analysis.  However, the discussion does not provide any evidence that the interpreted features are useful.  For example, in Figure 4b the Feature Associations and Time Step Relevance (for a Diabetes PPG sample) do not appear to relate to either the input PPG signal or do diabetic physiology.   There is no discussion providing guidance on how to relate the visualized features to the model’s prediction or the target class.   

### Potential ideas to address this issue (feature associations and time step relevance):
The authors should provide a more comprehensive analysis of the model interpretability.  For the PPG risk evaluation tasks, this should consist of comparing feature associations for all PPG examples in the PPG data set, split according to the target task.  If the feature associations differ significantly and quantiatively for two target tasks (for example hypertension classification vs. diabetes classification) that would provide some evidence that the model utilizes different PPG features for different objectives.  For the Time Step Relevance, perform some analysis using all PPG examples indicating quantiatively whether the Time Step Relevance consistently highlights known PPG features (for example diastolic foot or systolic rise in the waveform).  

In Figure 4a, the T-SNE plot of the embeddings of the [CLS] special tokens for each signal type show clear clustering by type.  However, the authors do not link this in a quantitative way that explains why this clustering makes the model “signal agnostic”.  This clustering according to signal type that is displayed may also be achievable with a short list of signal-level metrics such as signal mean, standard deviation, skew/kurtosis, or power content in several frequency bins.  It would be helpful if the authors could provide some quantitative (or even visual) comparison of clustering using an alternative approach (such as manual feature engineering), in order to demonstrate that the model embeddings are superior.  

### Potential ideas to address this issue (T-SNE):
It would be helpful if the authors could provide some quantitative (or even visual) comparison of clustering using an alternative approach (such as manual feature engineering), in order to demonstrate that the model embeddings are superior.  



## Issue 4: Small scale of data sets used for pre-training
Adding up the total number of data examples in Appendix A Table 3, I count only ~37,500 examples used for pre-training.  These samples are just 6 seconds long, so the total pre-training data volume is only 62 hours of data (from <1100 subjects).  Given that this data is used to pre-train a model with many millions of parameters, there is a significant risk of overfitting.  The data scale and complexity may not be well suited for the chosen model complexity. 

Additionally, for some signal types the total number of unique subjects represented in pre-training is very small— for example all EEG data in pre-training comes from only 45 unique subjects.  This seems likely to introduce some limitations to the pre-training data domain, and increase likelihood of significant domain shift when the model is applied to other small-N independent data sets in downstream tasks.


### Potential ideas to address this issue:
At a minimum, include discussion of the limitations associated with the relatively small data set used for developing a multi-modal foundation model, and the potential impact on generality.  Alternately, provide some quantitative evidence (for example, experiments showing performance as a function of model parameters) indicating that the model complexity is well suited to the available training data.  

For downstream tasks that involve data sets containing a small number of subjects (such as Driver Fatigue Detection, N=12) consider utilizing k-fold cross-validation stratified by subject ID to report performance, rather than using a fixed 20% test set.



## Performance table should have consistent content throughout the document.  

References should match with the data source, and be shown in the table.  For example Table 1 lists the reference for the data source in the table (this is preferred), but Table 2 does not.  Appendix A Tables 3 and 4 list the references for the data source only in the table caption, but this should be within the table as done for Table 1. 

Include a note (in the performance tables) indicating whether the task is classification vs. regression.  Ideally also include a list of the input data signals that have been used for each task, since this may not always match the full set of signals in that data set (as listed in Tables 3 and 4).  

## Several references contain insufficient information 
Examples: Liang 2018, Bousseljot 1995, Jianliang Min 2017.  At a minimum, references should include ae DOI or URL. Preferably, cite the primary journal article (if available) in standard citation format. 

## Label y-axis plots with numeric values and units (even if units are arbitrary, label these as A.U.)
The reconstruction plots in Appendix Section F should include units on the y-axes. For some examples (e.g. accelerometer) it is clear that the y-scale is likely much different from other examples, but this is impossible to know for sure because the axes are not labeled with units. 

## Data preprocessing details are too sparse
Include more information on data preprocessing.  What bandpass filtering parameters were used, if any?   What were the de-trending and gaussian smoothing parameters?  Were these identical for all data sets? 

Discuss the limitations of resampling to 65Hz for ECG signals (this loses some meaningful physiological information).

### Questions
I have the following comments for their authors regarding presentation style and content: 

## Performance table should have consistent content throughout the document.  

References should match with the data source, and be shown in the table.  For example Table 1 lists the reference for the data source in the table (this is preferred), but Table 2 does not.  Appendix A Tables 3 and 4 list the references for the data source only in the table caption, but this should be within the table as done for Table 1. 

Include a note (in the performance tables) indicating whether the task is classification vs. regression.  Ideally also include a list of the input data signals that have been used for each task, since this may not always match the full set of signals in that data set (as listed in Tables 3 and 4).  

## Several references contain insufficient information 
Examples: Liang 2018, Bousseljot 1995, Jianliang Min 2017.  At a minimum, references should include ae DOI or URL. Preferably, cite the primary journal article (if available) in standard citation format. 

## Label y-axis plots with numeric values and units (even if units are arbitrary, label these as A.U.)
The reconstruction plots in Appendix Section F should include units on the y-axes. For some examples (e.g. accelerometer) it is clear that the y-scale is likely much different from other examples, but this is impossible to know for sure because the axes are not labeled with units. 

## Data preprocessing details are too sparse
Include more information on data preprocessing.  What bandpass filtering parameters were used, if any?   What were the de-trending and gaussian smoothing parameters?  Were these identical for all data sets? 

Discuss the limitations of resampling to 65Hz for ECG signals (this loses some meaningful physiological information).

### Soundness
2

### Presentation
3

### Contribution
2
