### Summary

This paper investigates the relationship between deep language models (DLMs) and human brain activity during language comprehension. The authors use electrocorticography (ECoG) data from participants listening to a podcast while a high-performing DLM processes the same audio. They extract contextual embeddings from different layers of the DLM and use linear encoding models to predict neural activity. The study finds that the layer-wise accumulation of contextual information in DLMs mirrors the temporal processing of neural activity in high-level language areas. This suggests a connection between the internal sequence of computations in DLMs and the temporal dynamics of neural processing in the brain.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The study combines DLMs with ECoG data, providing a novel approach to understanding the relationship between artificial and biological language processing systems.
2. The authors provide a thorough explanation of their methodology, including the selection of electrodes, embedding extraction, and linear encoding models. This clarity enhances the reproducibility and understanding of the study.
3. The findings contribute to the growing body of research on the alignment between DLMs and the human brain, suggesting that the hierarchical structure of DLMs may be aligned with the temporal processing of neural activity.

### Weaknesses

#### Some Related Works


#### comment

1. The study focuses on a single language (English) and a specific type of neural recording (ECoG). It is unclear whether the findings generalize to other languages or neural recording techniques. Specifically, the reliance on ECoG, which measures electrical activity, raises questions about the applicability of the results to other modalities like fMRI, which measures blood oxygenation level dependent signals. The study does not explore whether the observed layer-wise accumulation of contextual information is consistent across different neural representations.
2. The study uses a relatively simple model (GPT-2 XL) and a single dataset. It is unclear whether the findings are specific to this model or dataset or whether they generalize to other models or datasets. The choice of GPT-2 XL, while a common benchmark, does not explore the full spectrum of DLM architectures, and it is possible that other models with different architectures or pre-training objectives might exhibit different temporal dynamics. Furthermore, the use of a single podcast dataset limits the generalizability of the findings to more diverse linguistic contexts and speaking styles.
3. The study does not compare the results with other methods for analyzing neural data, such as functional magnetic resonance imaging (fMRI) or electroencephalography (EEG). It is unclear whether the findings are specific to ECoG or whether they are consistent with other methods for analyzing neural data. The absence of comparisons with other neuroimaging techniques makes it difficult to assess the uniqueness of the observed temporal dynamics in ECoG data. It is possible that similar temporal patterns could be observed in other modalities, and the study would benefit from a comparative analysis.
4. The paper does not discuss the potential implications of the findings for cognitive neuroscience or the development of language models. The authors should clarify how their findings could inform our understanding of language processing in the brain and whether the insights gained from this study could be used to improve the development of more biologically plausible language models. The lack of discussion on the broader implications limits the impact of the study.

### Suggestions

The authors should consider expanding their analysis to include multiple languages and different types of neural recordings. For example, they could investigate whether the observed layer-wise accumulation of contextual information in DLMs mirrors the temporal processing of neural activity in high-level language areas across different languages, such as Spanish or French. This would require collecting new datasets for these languages and using the same methodology as in the current study. Furthermore, they should explore the use of other neural recording techniques, such as fMRI or EEG, to see if the findings are consistent across different modalities. This would involve adapting the current methodology to the specific characteristics of each recording technique, such as the spatial and temporal resolution of fMRI and EEG. Such an approach would provide a more comprehensive understanding of the relationship between DLMs and neural activity in language processing.

To address the limitation of using a single model and dataset, the authors should explore the use of other deep language models with different architectures and training data. For example, they could compare the results obtained with GPT-2 XL to those obtained with other models such as BERT or RoBERTa. This would help determine whether the findings are specific to GPT-2 XL or whether they are more general to the class of deep language models. Additionally, they should consider using multiple datasets to assess the robustness of their findings. This could involve using different podcasts or different types of language tasks. For example, they could use a dataset of children reading stories or a dataset of people listening to lectures. This would help determine whether the findings are specific to the specific podcast used in the study or whether they are more general to different types of language processing.

Finally, the authors should discuss the potential implications of their findings for cognitive neuroscience and the development of language models. They should clarify how their findings could inform our understanding of language processing in the brain and whether the insights gained from this study could be used to improve the development of more biologically plausible language models. For example, they could discuss how the hierarchical structure of DLMs might be related to the hierarchical organization of the brain's language processing areas. They could also explore how the temporal dynamics of neural activity in high-level language areas could be used to inform the development of more efficient and robust language models. This would help bridge the gap between artificial and biological language processing systems and contribute to a deeper understanding of both.

### Questions

1. How do the results of this study compare with other studies that have used different methods for analyzing neural data, such as functional magnetic resonance imaging (fMRI) or electroencephalography (EEG)?
2. How do the findings of this study generalize to other languages or neural recording techniques?
3. What are the limitations of using a single model and dataset, and how might these limitations affect the generalizability of the findings?
4. How do the findings of this study inform our understanding of language processing in the brain, and what are the potential implications for cognitive neuroscience or the development of language models?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
