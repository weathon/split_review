# HR-Extreme: A High-Resolution Dataset for Extreme Weather Forecasting

- Decision: Accept
- Scores: 5, 8, 6, 8

## Abstract
The application of large deep learning models in weather forecasting has led to significant advancements in the field, including higher-resolution forecasting and extended prediction periods exemplified by models such as Pangu and Fuxi. Despite these successes, previous research has largely been characterized by the neglect of extreme weather events, and the availability of datasets specifically curated for such events remains limited. Given the critical importance of accurately forecasting extreme weather, this study introduces a comprehensive dataset that incorporates high-resolution extreme weather cases derived from the High-Resolution Rapid Refresh (HRRR) data, a 3-km real-time dataset provided by NOAA.
  We also evaluate the current state-of-the-art deep learning models and Numerical Weather Prediction (NWP) systems on HR-Extreme, and provide a improved baseline deep learning model called HR-Heim which has superior performance on both general loss and HR-Extreme compared to others. Our results reveal that the errors of extreme weather cases are significantly larger than overall forecast error, highlighting them as an crucial source of loss in weather prediction. These findings underscore the necessity for future research to focus on improving the accuracy of extreme weather forecasts to enhance their practical utility.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Extreme weather forecasting is a crucial problem for the whole world. With the rise of deep learning-based weather forecasting models, the effectiveness of them on extreme weathers are not well analyzed.  This paper targets on providing a new benchmark for extreme weather forecasting. Authors employ the HRRR data and utilize the extreme events record in three sources to crop the extreme feature from the original HRRR dataset. Experiments are conducted with four baselines to show the performance.

### Strengths
Pros: 

1. Extreme weather forecasting evaluation is an important research problem. 
2. The provided dataset introduces 17 extreme events, which are comprehensive. 
3. Authors also release the code for generating the data.

### Weaknesses
Cons:

1. It is not clear how the HR-heim model is trained. Specifically, details regarding the training dataset, loss function, optimization algorithm, and hyperparameter settings are missing. This lack of information makes it difficult to reproduce the results or to understand the model's behavior.
2. Considering the dataset is a processed version of HRRR, it would be helpful to provide the geo-location of the extreme data to facilitate more diverse use from users. While the index file is mentioned, it is not clear how to convert the index to geo-location, and the specific format of the index file is not provided. It is essential to provide a clear mapping between the index and the actual geographic coordinates.
3. While the dataset is valuable, there is almost no analysis are present, especially compared to the ERA5 dataset, which is not insightful. The paper lacks a detailed analysis of the dataset's characteristics, such as the distribution of extreme events, the spatial and temporal variability, and the correlation between different variables. A comparison with ERA5, even if not used for dataset creation, could provide valuable context and highlight the unique aspects of the HRRR-based dataset.

### Questions
please refer to the weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work utilizes high-resolution HRRR data to create the HR-Extreme dataset, which encompasses a comprehensive set of 17 extreme weather types. The aim is to provide a more specialized dataset for evaluating the performance of weather forecasting models. To achieve this goal, the authors employed unsupervised clustering and manual filtering methods to develop a complete feature map of extreme events in a machine learning-ready format for the continental United States. The dataset was then used to assess the 1-hour forecasting capabilities of existing medium-range prediction models in comparison to the HR-Heim model proposed in this study.

### Strengths
1. **Significance**: It fills the gap in benchmarking for extreme weather assessment in deep learning-based medium-range weather forecasting tasks.

2. The dataset is clearly introduced, and it will be fully open-sourced.

3. The authors present comprehensive experiments and baseline results.

### Weaknesses
1. The description of the dataset generation process lacks clarity in some areas: a more detailed introduction of the clustering method is needed, including how records from different sources are handled and the hyperparameters of the algorithm. Specifically, the choice of DBSCAN needs further justification, including a discussion of why other clustering methods were not suitable. The description should also clarify how the spatial coordinates of the user reports are preprocessed before being fed into the clustering algorithm and how the density parameter (epsilon) and minimum points parameter were chosen. Furthermore, the handling of records from different sources needs more detail, particularly if these sources have different levels of accuracy or reporting biases. 

2. There are also unclear aspects in the experimental description:  
   a) The baselines are models trained on globally coarse-resolution grids; Was there any further fine-tuning on this dataset? What preprocessing steps were taken? It is unclear if the baseline models were directly applied to the HR-Extreme dataset or if any preprocessing steps were performed to align the input data with the models' expectations. The lack of clarity on this point makes it difficult to assess the fairness of the comparison.  
   b) What is the training strategy for HR-Heim? Does it use the same hyperparameter settings on the original dataset and HR-Extreme? The description of the training process for HR-Heim is insufficient. It is not clear whether the model was trained from scratch or fine-tuned on the HR-Extreme dataset. Furthermore, the hyperparameter settings used for training HR-Heim should be explicitly stated, and it should be clarified whether these settings were the same as those used for training on the original HRRR data.

### Questions
1. Was the result of the clustering algorithm verified by domain experts? Is there corresponding uncertainty detection and assessment?

2. What is the basis for the "types of events without specific ranges or those not related to obvious variations in feature map predictions"?

3. Can data from different sources be used separately?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a new dataset of labelled extreme weather events over the continental US based on a high resolution (3km) numerical forecast product. They compare the events from a numerical weather prediction (NWP) model as well as two baseline ML based weather models and a newly proposed variant. The authors claim improved skill in their new variant compared to the other baselines.

### Strengths
The constructed dataset could provide a useful evaluation of extreme events in new ML based weather prediction models which tend to be evaluated on larger scale statistics, potentially hiding biases in such events. It is based on an operational high-resolution dataset with a mixture of automated and manual labelling.

### Weaknesses
There are a number of technical and fundamental weaknesses that undermine the above strengths.

Major issues:
1) Extreme events are, by definition, rare. While a database of such events derived from a high-resolution reanalysis product could provide a useful starting point for evaluation, the specific events are much less useful without a probabilistic understanding or measure of their likelihood at different lead times. i.e. It is probably more likely that any of the given events *wouldn't* have happened given a similar atmospheric state if the conditions were encountered again. Without a probabilistic understanding of the probability of an event (based on lots of comparable events that weren't extreme), this dataset has very little value as presented.
 2) This leads to my second concern regarding the evaluation setup. Given the dataset extracts the atmospheric state at t=0, -1 and -2 hours, I presume the evaluations happen from an atmospheric state of t=-2 hours and run forward? This is no longer forecasting, but nowcasting and quite a different task. Since the atmospheric state already has the extreme event and the model just needs to advect it correctly. I have no idea how the NWP model is compared in this setting since presumably the authors don't run this explicitly with the extracted state? Or perhaps they do? Also, since the authors use the same NWP as was used to create the HRRR dataset, why doesn't it perform as well as the other models? At what resolution are the models run, are they run globally, over the US, or only over the event region? Are the global Fuxi and Pangu models retrained for these regions?
 3) Related to this, to what extent is this dataset used to train the different models? Does HR-Helm get to see some or any extreme event data during training? Given the issues described in (1), how do you avoid overfitting?

One more minor issue is that I would like to see Figure 4 presented for the same day for all 4 models, with a separate figure for the other day for all 4 models in the appendix. Currently it's impossible to fairly compare the skill of the models (although it seems like the NWP already does better than HR-Helm across the two examples).

### Questions
Please provide specific responses to each of the concerns and questions raised above in the weaknesses.

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
4

### Summary
This paper introduces a high-resolution dataset, called HR-Extreme, for numerical weather forecasting under extreme weather conditions, an area often overlooked in weather forecasting literature. The authors also present a baseline deep learning model alongside the dataset, called HR-Heim, which outperforms state-of-the-art weather models in extreme weather conditions.

### Strengths
* The authors provide a high-resolution dataset for numerical weather forecasting under extreme weather conditions. The need for such dataset has been evident for some time, as highlighted by the low performance analysis of SOTA weather forecasting models.
* The construction of the dataset is well-motivated, and the authors provide a clear and thorough explanation of both the data collection and construction processes.
* Additionally, the authors provide a baseline deep learning model called HR-Heim, which is inspired by a SOTA numerical weather forecasting model, to specifically excel and outperform SOTA models under extreme weather conditions.

### Weaknesses
 * In Section 2.2, the authors discuss some datasets that share similarities (to a certain extent) with the proposed one. It would have been beneficial to illustrate the performance of the SOTA models and the proposed HR-Heim on some of these datasets. Specifically, the last dataset introduced by Liu et al., which also includes certain extreme weather conditions, could have been included in the experiments to support the need for HR-Extreme and support the performance of HR-Heim. Given that HR-Heim outperforms SOTA methods in HR-Extreme, we would expect to see similar results on other datasets with extreme weather conditions.
* As the authors also state as a limitation, this kind of study should include more than just a single-step prediction analysis. Given the increased difficulty of predicting extreme weather events in the long term, an accuracy comparison between HR-Heim and SOTA methods across varying time horizons could be valuable.

### Questions
* Could you extend the dataset analysis to include predictions for more than a single hour ahead?
* As an extension to the previous question, could you analyze and compare the performance of state-of-the-art models and HR-Heim for both short-term and long-term forecasting?
* Could you further evaluate the performance of HR-Heim on a similar extreme weather dataset?

### Soundness
2

### Presentation
2

### Contribution
3
