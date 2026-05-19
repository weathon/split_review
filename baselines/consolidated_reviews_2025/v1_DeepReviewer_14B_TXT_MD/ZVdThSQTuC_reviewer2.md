### Summary

This paper presents a new EEG dataset for word-level semantic relevance detection. The dataset contains 15 participants, 120 topics, and 360 sentences. The authors also provide a detailed description of the data collection and processing procedures, as well as a benchmark evaluation of several machine learning models for word and sentence relevance classification tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The dataset is novel in its focus on semantic text relevance and its word-level EEG recordings. 
2. The data collection and processing procedures are clearly described and seem rigorous. 
3. The benchmark experiments provide a useful baseline for future research on the dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The dataset size is relatively small, with only 15 participants and 360 sentences. This may limit the generalizability of the findings and the performance of machine learning models trained on the dataset. The number of participants is indeed low compared to other EEG datasets, and the number of sentences per topic (24) might not be sufficient to capture the full range of semantic relevance variations. This could lead to overfitting when training models, especially those with a large number of parameters.
2. The tasks are limited to word and sentence relevance classification, which may not fully capture the complexity of semantic text relevance. The relevance classification is a binary task (relevant or irrelevant), which might oversimplify the nuanced nature of semantic relevance. The dataset does not account for degrees of relevance, which could be important for a more comprehensive understanding of semantic processing.
3. The paper does not provide a detailed analysis of the limitations of the dataset, such as potential biases or confounding factors. For example, the study does not discuss the potential impact of individual differences in reading speed, working memory, or prior knowledge on the EEG data. Furthermore, the instructions given to participants might introduce a bias towards selecting certain types of information as relevant.

### Suggestions

The authors should consider expanding the dataset to include more participants and a greater variety of texts. Increasing the number of participants would improve the statistical power of the study and enhance the generalizability of the findings. Adding more texts, especially those with varying lengths and complexities, would allow for a more robust evaluation of the models. Furthermore, the authors should explore the possibility of including a wider range of topics to ensure that the dataset is not biased towards specific domains. It would also be beneficial to include a more diverse participant pool, considering factors such as age, education, and cultural background, to make the dataset more representative of the general population. This would help to mitigate potential biases and improve the applicability of the dataset to different contexts.

To address the limitations of the binary relevance classification task, the authors should consider incorporating a more nuanced approach to relevance labeling. This could involve using a Likert scale to rate the degree of relevance, or including multiple levels of relevance (e.g., highly relevant, moderately relevant, slightly relevant, and irrelevant). This would allow for a more fine-grained analysis of semantic processing and enable the development of models that can capture the complexity of relevance. Additionally, the authors could explore other tasks related to semantic relevance, such as identifying the most relevant sentence in a paragraph or ranking sentences based on their relevance to a given topic. This would provide a more comprehensive evaluation of the dataset and its potential for various applications.

Finally, the authors should conduct a more thorough analysis of the limitations of the dataset, including potential biases and confounding factors. This could involve collecting additional data on participant characteristics, such as reading speed, working memory capacity, and prior knowledge of the topics. The authors should also investigate the impact of different instructions on the EEG data and explore methods for mitigating any potential biases. Furthermore, it would be beneficial to analyze the EEG data for artifacts and outliers, and to develop methods for handling these issues. A detailed discussion of these limitations would provide a more complete picture of the dataset and its potential applications, and would help researchers to use the dataset more effectively.

### Questions

1. How does the dataset compare to other publicly available EEG datasets in terms of size, quality, and applicability to semantic text relevance detection? 
2. What are the limitations of the dataset in terms of generalizability to different types of texts, topics, and populations? 
3. How can the dataset be used to advance research on language relevance, psycholinguistics, and brain-computer interface devices?

### Rating

5

### Confidence

3

**********
