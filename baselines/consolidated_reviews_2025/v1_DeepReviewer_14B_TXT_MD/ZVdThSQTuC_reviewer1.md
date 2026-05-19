### Summary

This paper presents an EEG dataset designed to capture brain responses at the word level for semantic text relevance. Participants read texts categorized as either semantically relevant or irrelevant to self-selected topics, resulting in 23,270 time-locked EEG recordings. The dataset supports research into psycholinguistics and brain-computer interface (BCI) applications, particularly for real-time language relevance detection. The authors provide benchmark experiments and emphasize the dataset’s potential for advancing relevance-based systems in human-computer interaction.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The dataset captures word-level EEG responses, which is valuable for psycholinguistics and semantic relevance research.
2. The authors conduct thorough benchmark experiments with multiple models, establishing a solid foundation for future work.
3. The paper provides a detailed description of the experimental setup and data collection process.

### Weaknesses

#### Some Related Works


#### comment

1. The study uses a fixed 700ms window for word presentation, which may not account for variations in cognitive processing time for different words or sentence structures. This fixed window could truncate the EEG signal for words that elicit later cognitive responses, potentially leading to a loss of relevant information and affecting the accuracy of relevance classification, especially for complex or ambiguous words.
2. The subjectivity of relevance assessments could introduce variability, as relevance is annotated based on individual annotator judgment without accounting for nuanced or context-specific interpretations. The lack of inter-annotator agreement metrics beyond a simple majority vote makes it difficult to assess the reliability of the relevance labels. Furthermore, the annotation process does not seem to consider the degree of relevance, treating all relevant words as equally relevant, which is a simplification that may not reflect real-world semantic processing.
3. The paper lacks a discussion of how well the dataset generalizes to diverse populations, as the participants are primarily students from a limited demographic. This raises concerns about the generalizability of the findings to other populations with different linguistic backgrounds or cognitive styles. The limited demographic scope may introduce biases that could affect the performance of models trained on this dataset when applied to more diverse populations.
4. While the paper provides a comparison of the dataset with existing ones in terms of recording techniques, it lacks a thorough discussion on how this dataset addresses gaps in the current landscape of EEG datasets for language processing research. A more detailed comparison should highlight the specific limitations of existing datasets that this dataset overcomes, such as the lack of word-level annotations or the absence of a controlled relevance paradigm.
5. The paper does not provide a detailed analysis of the potential confounding effects of word frequency or predictability on the EEG signals. High-frequency or predictable words might elicit different brain responses compared to low-frequency or unpredictable words, which could confound the relevance effects. The absence of a control for these factors makes it difficult to isolate the neural correlates of semantic relevance.
6. The authors do not explore the potential impact of task-related cognitive load on the EEG recordings, which could introduce noise or bias into the relevance classification tasks. The cognitive load associated with the reading task itself could vary across participants and influence the EEG signals, making it difficult to isolate the neural correlates of semantic relevance. A lack of consideration for task-related cognitive load could lead to misinterpretation of the results.

### Suggestions

The study should address the limitations of using a fixed 700ms window for word presentation by exploring alternative methods for handling variable word presentation times. One approach could involve using a dynamic windowing technique that adapts to the length of each word, ensuring that the entire EEG signal is captured. Another approach could be to investigate the use of recurrent neural networks or other time-series models that can handle variable-length input sequences. Additionally, the study should consider the potential impact of word length on the EEG signal and control for this factor in the analysis. This could involve including word length as a covariate in the model or using a word length-matched control condition. By addressing these issues, the study can ensure that the EEG signals are accurately captured and that the relevance classification is not affected by the fixed presentation window.

To improve the reliability and validity of the relevance annotations, the study should implement a more rigorous annotation process. This could involve calculating inter-annotator agreement metrics such as Cohen's kappa or Krippendorff's alpha to assess the consistency of the annotations. The study should also consider using a multi-label annotation scheme that allows for nuanced interpretations of relevance, rather than a simple binary relevant/irrelevant classification. This would enable the study to capture the degree of relevance, which could be important for understanding the neural correlates of semantic processing. Furthermore, the study should provide clear guidelines for annotators to ensure that the annotations are consistent and reliable. This could involve providing examples of relevant and irrelevant words, as well as detailed instructions on how to handle ambiguous cases. By implementing these measures, the study can improve the quality of the relevance annotations and ensure that they accurately reflect the semantic content of the texts.

The study should also address the potential confounding effects of word frequency and predictability on the EEG signals. This could involve collecting word frequency data from a large corpus and including it as a covariate in the analysis. The study should also consider using a word predictability measure, such as surprisal, to control for the effects of word predictability on the EEG signals. Additionally, the study should explore the use of a control condition that involves reading non-relevant texts with similar word frequency and predictability profiles. This would enable the study to isolate the neural correlates of semantic relevance from the effects of word frequency and predictability. Furthermore, the study should investigate the potential impact of task-related cognitive load on the EEG recordings. This could involve measuring cognitive load using a secondary task or a subjective rating scale. The study should also consider using a control condition that involves reading non-relevant texts under the same cognitive load conditions. By addressing these issues, the study can ensure that the EEG signals are not confounded by word frequency, predictability, or task-related cognitive load.

### Questions

1. How does the fixed 700ms window for word presentation affect the EEG signal for words that might require longer cognitive processing times? Could this impact the accuracy of relevance classification?
2. How did the authors ensure consistency in relevance annotation across different annotators? Could the authors provide inter-annotator agreement metrics to validate the reliability of the relevance labels?
3. What measures were taken to control for confounding factors such as word frequency or predictability, which could influence brain responses independently of semantic relevance?
4. How does the dataset account for individual differences in reading speed or cognitive processing, and how might these differences affect the results?
5. Could the authors elaborate on the potential impact of task-related cognitive load on the EEG recordings? Were there any measures in place to mitigate this effect?
6. How well does the dataset generalize to diverse populations, given that the participants are primarily students from a limited demographic? Could the authors discuss any plans for expanding the dataset to include more diverse participants?

### Rating

3

### Confidence

4

**********
