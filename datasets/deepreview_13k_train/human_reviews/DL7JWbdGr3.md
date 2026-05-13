# PEMs: Pre-trained Epidemic Time-Series Models

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Providing accurate and reliable predictions about the future of an epidemic is an important
problem for enabling informed public health decisions.
Recent works have shown that leveraging data-driven solutions that utilize advances in deep learning methods
to learn from past data of an epidemic often outperform traditional mechanistic models.
However, in many cases, the past data is sparse and
may not sufficiently capture the underlying dynamics.
While there exists a large amount of data from past epidemics,
leveraging prior knowledge from time-series data of other diseases is a non-trivial challenge.

Motivated by the success of pre-trained models in language and vision tasks, we tackle the problem
of pre-training epidemic time-series models to learn from multiple datasets from different diseases and epidemics.
We introduce Pre-trained Epidemic Time-Series Models (\modelp)
that learn from diverse time-series datasets of a variety of diseases by formulating pre-training as a set of self-supervised learning (SSL) tasks.
We tackle various important challenges specific to pre-training for epidemic time-series such as dealing with heterogeneous dynamics
and efficiently capturing useful patterns from multiple epidemic datasets by carefully designing the SSL tasks to learn important priors about the epidemic dynamics that can be leveraged for fine-tuning to multiple downstream tasks.
The resultant \model outperforms previous state-of-the-art methods in various downstream time-series tasks
across datasets of varying seasonal patterns, geography, and mechanism of contagion including the novel Covid-19 pandemic unseen in pre-trained data
with better efficiency using smaller fraction of datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to explore the pre-training of time series models for epidemic data. The proposed model is the first-ever pre-trained time series model for epidemic analysis tasks. Unlike SSL for images or texts, this paper presents four SSL tasks to capture various aspects of epidemic dynamics. Extensive experiments over real-world epidemic datasets verify the effectiveness of the proposed model.

### Strengths
1. The paper addresses an essential problem in time series domain.
2. The paper conducts extensive experiments to verify the effectiveness of PEM.
3. The experiments have verified the effectiveness of PEM, especially in comparison with those without SSL.
4. The experiments also cover a discussion over data efficiency and generalization to novel diseases.

### Weaknesses
1. The related work should be expanded. To the best of my knowledge, a series of papers [1] have been studied on SSL for general time series, also including epidemic analysis. However, they're rarely mentioned or considered as baselines for a fair comparison.
2. The technical novelty against previous SSL approaches is somewhat limited. The proposed masking strategies, while adapted for time series, draw heavily from existing techniques in NLP and general time series. The introduction of PEAKMASK and SEASONDETECT, while potentially useful, lacks a strong theoretical justification and a thorough ablation study to demonstrate their unique contribution beyond standard masking.
3. The baselines listed on Page 7 are insufficient. More SSL methods, particularly for general time series, should be included as baselines. For example, it would be interesting to see if PEM can outperform recently developed SSL methods in time series analysis. The current baselines do not provide a comprehensive comparison against state-of-the-art SSL techniques, making it difficult to ascertain the true advantage of the proposed method.
4. It would greatly enhance reproducibility if the authors provide the source code for their approach.
5. I highly recommend that this paper provide more results on few-shot or zero-shot learning for epidemic data, as it is typically characterized by sparse data.

### Questions
If I have misunderstandings in the weaknesses, please clarify them in the rebuttal phase. Thank you.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a pre-training machnism for using transformers to make time series forecasting for epidemics. The pre-training is self-supervised learning through multiple tasks: randmask, lastmask, peakmask, seasonselect. Similar to large language model pre-training, the proposed pre-training method for time series forecasting learn general patterns from multiple disease datasets. Then fine tune the pre-trained model to a specific disease forecasting task. The method is demonstrated on several real world epidemic forecasting tasks and outperforms the baselines.

### Strengths
The idea of pre-train a time-series epidemic forecasting model is very interesting and new. This has not been done before. The method is technically sound and the writing is clear. The experimental design is reasonable and results show superior performance compared with the baselines.

### Weaknesses
1. The baselines in this paper do not represent the SOTA performance. Also, the baselines are not "easy-to-replicate" methods whose code is not provide. This makes me a bit concern about the effectiveness of the comparison results.
2. There is no uncertainty quantification analysis of all the methods. It seems the transformer-based models are so large so may have large predicting variance.

### Questions
1. In section SEASONDETECT, the paper first mentions that the year is divided into 4 seasons Season 1 (Dec-Feb), but later, it also says the peak season is s_1(d). Could you clarify this in a more consistent way?
2. Data normalization, will the normalized data be reversed before computing the loss error during training? 
3. Why perform linear probing before fully fine-tuning?
4. What's the pre-training cost?

### Soundness
3 good

### Presentation
3 good

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
- novel application of SSL and fine-tuning on broad epidemic data to get PEMs, which they use to forecast various diseases, as well as various other epidemic dynamics such as peak weeks and onset weeks.

- interesting experiments of generalization to novel diseases in appendix D

### Strengths
- originality: This is a new application domain for SSL as far as I know, but the methodology is not particularly new.

- quality: The submission is well written and formatted, with strong experimental results and ablations.

- clarity: most of the training details are there, though much is relegated to the appendix.

- significance: the work is significant as an application of SSL to a specific domain with greater performance, and finds relevance in the current post-pandemic context.

### Weaknesses
 - sounds like your segments of time series is basically patching, similar to (Nie et al. 2022). If so, why do you achieve so much better results than PatchTST? Is it just the finetuning?

- I'm not sure I understand why inputting each time step as a single token would lack "semantic meaning", seeing as the output representations of a transformer for a given token are influenced by all the other tokens in the input sequence (i.e. "contextual embeddings")

- How do you normalize the training process of your method wrt baselines? How can you disentangle the architecture's influence from the influence of the training process and the influence of using additional compute?

- unclear what is being evaluated in appendix D table 6 since it's not known how the baselines are trained. For example, it is clearly remarked that no pre-training is performed for the PT baseline, but not why.

- why are the results around one of the contributions (Significant improvement in data and training efficiency and adaptability to novel epidemics) only in the appendix?

### Questions
- There might be bleed between the influenza data from 2001 to 2010 and the crypto data from 2006 to 2012 given the temporal alignment, but I'm not knowledgeable enough to judge how strong the overlap could be. Is the argument that, since influenza and crypto have different inherent dynamics, they shouldn't influence each other?

- How do you choose the value of T, i.e. the length of the input time series?

- How do you justify the default choice of gamma = 0.1 for lastmask ? Seems like 0.2 performs well too.

Overall, I am rating this a 5 (marginally below acceptance) before discussion, since it is hard to disentangle the impact of the supervised pre-training from the architectural design choices and the increased compute/data. There are no details on how the baselines are trained, so these comparisons do not properly motivate which components of PEM lead to its superior performance. I am very amenable to changing this rating given discussions around how the baselines were implemented for fair comparisons.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose Pre-trained Epidemic Models (PEMs) that is capable of learning pattern across multiple datasets and multiple diseases using self-supervised learning.  They demonstrate the success of their method in the task of forecasting. Their approach maintains or even
surpasses the performance of other strong deep-learning models.

### Strengths
1. The paper is well-presented and easy to understand.
1. PEM is a novel model that uses an array of self-supervised learning (SSL) tasks shown to be effective in learning from cross-disease datasets.
1. PEM demonstrates efficiency in utilizing multiple training datasets while maintaining or even surpassing the performance of other strong deep learning models. This showcases its ability to adapt to downstream tasks with limited data, which is particularly beneficial in real-world
scenarios where complete datasets may not be readily available, especially in the case of unseen diseases.

### Weaknesses
 1. __Limitations in Model Compared__: While the paper compares PEM with FUNNEL, a mechanistic model, it does not explore simpler disease-focused mechanistic models or even basic auto-regressive models. Additionally, the absence of testing the performance of simpler models on unseen diseases, like COVID-19, limits the model's generalization claims. Over the years many experts have submitted forecasts for COVID-19 and influenza in real-time (e.g., US COVID-19 Forecast Hub, EU COVID-19 Forecast Hub). The paper already refers to a paper on one of the hubs (Cramer 2022). Without comparison against the models used by the community, it is hard to judge how much value the proposed approach adds. Further, for COVID-19 and epidemiological data in general, there is frequent data revision and backcorrection. The data that is available today is a much cleaner version compared to what was available at the time a forecast was made. Especially for COVID-19 the data revision history is available, therefore, the authors should test the dataset with the appropriate version, not the latest version. It is not clear if the authors have done so.

 2. **Data Preprocessing Details**: The paper lacks information on the data preprocessing steps performed, such as data smoothing and temporal alignment. Preprocessing often has a significant impact on real-time forecasting, especially, when there is a lot of backcorrection.

 3. **Ablation Studies**:   
    1. Performance compared to simple transfer learning or doing some training on a single disease dataset (such as pre-training on just past flu data if the disease of interest is flu) would have been good. Randmask does not perform nearly as well as the others, so does adding this into the combination of tasks contribute meaningfully?
    1. The choice of hyperparameters matches the best-performing ones in the "ablation studies". Can the authors verify that the hyperparameter selection was done on a validation set and not on the test set?

1. **Additional Comments**:  
    1. Lower RMSE Values for Flu in the US: The remarkably low RMSE values for Flu in the US  looks unusual. Some more context or explanations for these results would be useful. Was this normalized somehow (like per 100k)?

    1. Consolidation of Appendix Results: While it's useful to have supplementary information in the appendix, the paper might benefit from incorporating key results from Q2, Q3, Q4, and Q6 into the main text to provide a more comprehensive overview of the model's capabilities.

    1. Presentation issues: While easy the writing is easy to understand, the paper has many typos; it will benefit from a pass for presentation.

### Questions
Addressing the following, especially the first one, will significantly improve my evaluation:

1. Have the authors compared their results against models that were used by the epidemic forecasting community during COVID-19 and ILI forecasting tasks? (These forecasts are publicly available)

1. Was there any data pre-processing involved? How does that impact the results?

1. Can the authors verify that the hyperparameter selection was done on a validation set and not on the test set?

1. Why is RMSE for the US so low?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
