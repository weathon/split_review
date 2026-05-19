### Summary

This paper presents a novel EEG dataset focused on semantic text relevance, collected from 15 participants reading Wikipedia documents. The authors aim to advance research in language relevance and psychophysiological studies by providing a benchmark for machine learning models to predict word and sentence-level relevance. The dataset is designed to capture semantic relevance through time-locked EEG responses, offering a unique perspective on how the brain processes information based on relevance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The dataset’s focus on semantic relevance is a fresh perspective in EEG research, addressing a gap in existing datasets that primarily focus on natural language processing tasks without explicitly considering semantic relevance.
2. The authors provide a comprehensive comparison of five machine learning models, establishing a benchmark for future research and demonstrating the dataset’s utility in predictive modeling.

### Weaknesses

#### Some Related Works


#### comment

1. The dataset’s focus on a single participant limits its generalizability. Expanding the dataset to include more participants would enhance the robustness and applicability of the findings.
2. The paper lacks a detailed discussion on potential ethical considerations related to the use of EEG data, which is crucial for ensuring responsible research practices.

### Suggestions

The authors should consider a more rigorous approach to evaluating the generalizability of their dataset. While the inclusion of multiple participants is a step in the right direction, the current sample size of 15 participants may still be insufficient to draw broad conclusions about the generalizability of the findings across diverse populations. A more robust approach would involve a power analysis to determine the minimum sample size required to detect statistically significant effects, given the expected effect size and variability within the population. Furthermore, the authors should consider the potential impact of individual differences in cognitive abilities, reading habits, and cultural background on the dataset's applicability. For example, participants with different levels of expertise in the topics covered by the Wikipedia documents might exhibit different EEG patterns, which could affect the model's performance. The authors should also consider using techniques such as cross-validation to assess the robustness of the model's performance across different subsets of the data, which can help to mitigate the impact of individual variability.

To address the ethical concerns, the authors should provide a more detailed discussion of the data collection and analysis procedures, including specific information on the consent process, data anonymization, and data security measures. The authors should also discuss the potential risks associated with the use of EEG data, such as the possibility of artifacts or noise, and how these risks were mitigated during the data collection and analysis process. Furthermore, the authors should consider the potential impact of their research on individuals who may be vulnerable to the use of EEG technology, such as those with cognitive impairments or those who are susceptible to anxiety or stress. The authors should also discuss the potential for misuse of their dataset, such as for training models that could be used to discriminate individuals based on their cognitive abilities or emotional states. A thorough discussion of these ethical considerations is essential to ensure that the research is conducted in a responsible and ethical manner.

Finally, the authors should consider the limitations of their dataset in terms of the specific topics covered by the Wikipedia documents. The current dataset may not be representative of all types of text, and the authors should acknowledge this limitation and discuss the potential impact of this limitation on the generalizability of their findings. For example, the topics covered by the Wikipedia documents may be biased towards certain types of content, such as news articles or scientific papers, and the authors should consider how this bias might affect the model's performance on other types of text. The authors should also consider the potential impact of the specific reading task on the dataset's applicability. The current reading task may not be representative of all types of reading tasks, and the authors should discuss the potential impact of this limitation on the generalizability of their findings. For example, the authors should consider how their dataset might be used to study the neural correlates of different types of reading tasks, such as reading comprehension or reading fluency.

### Questions

1. How do the authors plan to address the limitations of the dataset in terms of generalizability, especially given the small sample size and the focus on a single participant?
2. What ethical considerations should be taken into account when using this dataset, particularly regarding the use of EEG data?
3. Could the dataset be extended to include more participants and different types of text to enhance its generalizability and applicability?

### Rating

3

### Confidence

4

**********
