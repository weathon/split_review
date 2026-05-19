### Summary

This paper introduces a novel EEG dataset designed to capture semantic text relevance through time-locked word presentation. The dataset consists of 23,270 EEG recordings from participants who read text that was either semantically relevant or irrelevant to self-selected topics. The authors present benchmark experiments on two tasks: word relevance classification and sentence relevance classification, using five different models. The dataset and code are openly released, aiming to advance research in psycholinguistics, brain-computer interfaces, and information retrieval systems.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The dataset is novel in its focus on semantic text relevance and its word-level EEG recordings.
2. The data collection and processing procedures are clearly described and seem rigorous.
3. The benchmark experiments provide a useful baseline for future research on the dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The dataset size is relatively small, with only 15 participants and 360 sentences. This may limit the generalizability of the findings and the performance of machine learning models trained on the dataset.
2. The tasks are limited to word and sentence relevance classification, which may not fully capture the complexity of semantic text relevance.
3. The paper does not provide a detailed analysis of the limitations of the dataset, such as potential biases or confounding factors.

### Suggestions

The authors should consider expanding the dataset to include more participants and a greater variety of texts. This would improve the statistical power of the study and allow for more robust conclusions. Specifically, increasing the number of participants would help to reduce the variance in EEG data and improve the generalizability of the findings across different individuals. Furthermore, including a wider range of text types (e.g., different genres, lengths, and complexities) would make the dataset more representative of real-world scenarios and allow for the development of more robust models. The current dataset, while valuable, is limited in its scope and may not be sufficient to capture the full complexity of semantic relevance detection.

To address the limitation of the tasks, the authors could explore more complex tasks that involve semantic text relevance. For example, they could include tasks that require participants to identify the most relevant sentence in a paragraph or to rank sentences based on their relevance to a given topic. This would provide a more comprehensive evaluation of the dataset and its potential for various applications. Additionally, the authors could investigate the use of more sophisticated machine learning models that can capture the nuances of semantic relevance, such as models that incorporate contextual information or models that can handle hierarchical structures in text. The current benchmark experiments, while useful, may not fully capture the potential of the dataset for more advanced applications.

Finally, the authors should provide a more detailed analysis of the limitations of the dataset, including potential biases and confounding factors. For example, they should discuss the potential impact of individual differences in reading speed, working memory, and prior knowledge on the EEG data. They should also consider the potential for biases in the selection of stimuli and the design of the experiment. A thorough discussion of these limitations would help researchers to use the dataset more effectively and to interpret the results with caution. Furthermore, the authors should consider providing guidelines for how to address these limitations in future research, such as by collecting additional data or by using specific analysis techniques.

### Questions

1. How does the dataset compare to other publicly available EEG datasets in terms of size, quality, and applicability to semantic text relevance detection?
2. What are the limitations of the dataset in terms of generalizability to different types of texts, topics, and populations?
3. How can the dataset be used to advance research on language relevance, psycholinguistics, and brain-computer interface devices?

### Rating

6

### Confidence

3

**********
