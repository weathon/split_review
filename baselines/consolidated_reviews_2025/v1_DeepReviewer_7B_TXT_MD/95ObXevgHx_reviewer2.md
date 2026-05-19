### Summary

The authors used electrocorticography (ECoG) to record neural activity from participants listening to a podcast while simultaneously feeding the same podcast into a high-performing deep language model (GPT-2 XL). They then extracted contextual embeddings from the different layers of the model and used linear encoding models to predict neural activity. They found that the layer-wise accumulation of contextual information in DLMs mirrors the temporal processing of neural activity in high-level language areas.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The study uses a novel approach by combining electrocorticography (ECoG) with deep language models (DLMs) to investigate the temporal dynamics of language comprehension in the human brain.
2. The findings provide valuable insights into the relationship between DLMs and the brain's processing of language, suggesting that the hierarchical structure of DLMs may be aligned with the temporal processing of neural activity.

### Weaknesses

#### Some Related Works


#### comment

1. The study is limited to a single language (English) and a single type of neural recording (ECoG). It is unclear whether the findings generalize to other languages or neural recording techniques.
2. The study uses a relatively simple model (GPT-2 XL) and a single dataset. It is unclear whether the findings are specific to this model or dataset or whether they generalize to other models or datasets.
3. The study does not compare the results with other methods for analyzing neural data, such as functional magnetic resonance imaging (fMRI) or electroencephalography (EEG). It is unclear whether the findings are specific to ECoG or whether they are consistent with other methods for analyzing neural data.

### Suggestions

The authors should consider expanding their analysis to include multiple languages and different types of neural recordings. For example, they could investigate whether the observed layer-wise accumulation of contextual information in DLMs mirrors the temporal processing of neural activity in high-level language areas across different languages, such as Spanish or French. This would require collecting new datasets for these languages and using the same methodology as in the current study. Furthermore, they should explore the use of other neural recording techniques, such as fMRI or EEG, to see if the findings are consistent across different modalities. This would involve adapting the current methodology to the specific characteristics of each recording technique, such as the spatial and temporal resolution of fMRI and EEG. Such an approach would provide a more comprehensive understanding of the relationship between DLMs and neural activity in language processing.

To address the limitation of using a single model and dataset, the authors should explore the use of other deep language models with different architectures and training data. For example, they could compare the results obtained with GPT-2 XL to those obtained with other models such as BERT or RoBERTa. This would help determine whether the findings are specific to GPT-2 XL or whether they are more general to the class of deep language models. Additionally, they should consider using multiple datasets to assess the robustness of their findings. This could involve using different podcasts or different types of language tasks. For example, they could use a dataset of children reading stories or a dataset of people listening to lectures. This would help determine whether the findings are specific to the specific podcast used in the study or whether they are more general to different types of language processing.

Finally, the authors should compare their results with other methods for analyzing neural data, such as functional magnetic resonance imaging (fMRI) or electroencephalography (EEG). This would involve adapting their methodology to the specific characteristics of each recording technique. For example, they could use fMRI to measure the blood oxygenation level dependent (BOLD) signal or EEG to measure the electroencephalogram (EEG) signal. This would help determine whether the findings are specific to ECoG or whether they are consistent with other methods for analyzing neural data. Furthermore, they should compare their results with other studies that have used different methods for analyzing neural data. This would help determine whether the findings are consistent with the existing literature.

### Questions

1. How do the results of this study compare with other studies that have used different methods for analyzing neural data, such as functional magnetic resonance imaging (fMRI) or electroencephalography (EEG)?
2. How do the findings of this study generalize to other languages or neural recording techniques?
3. What are the limitations of using a single model and dataset, and how might these limitations affect the generalizability of the findings?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
