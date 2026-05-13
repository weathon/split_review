# An EEG dataset of word-level brain responses for semantic text relevance

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Electroencephalography (EEG) can enable non-invasive, real-time measurement of brain activity in response to human language processing. Previously released EEG datasets focus on brain signals measured either during completely natural reading or in full psycholinguistic experimental settings. Since reading is commonly performed when considering certain content as more semantically relevant than other, we release a novel dataset for semantic text relevance containing $23{,}270$ time-locked (${\sim}0.7s$) word-level EEG recordings acquired from participants who read both text that was semantically relevant and irrelevant to self-selected topics. Using these data, we present benchmark experiments with two evaluation protocols: participant-independent and participant-dependent on two prediction tasks (word relevance and sentence relevance). We report the performance of five well known models on these tasks. Our dataset and code are openly released. Altogether, our dataset paves the way for advancing research on language relevance and psycholinguistics, brain input and feedback-based recommendation and retrieval systems, and development of brain-computer interface (BCI) devices for online detection of language relevance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The study introduces a new EEG dataset collected from 15 participants engaged in reading tasks with language processing requirement, designed to support NLP research in areas such as word and sentence relevance classification, while EEG signal can be cogntive GT. This dataset further supports exploring neural representations by complementing existing EEG-based reading tasks.

### Strengths
This study creates a new EEG-based dataset specifically designed for NLP tasks. Such a dataset is instrumental in advancing research on BCIs for decoding language processing for reading which could enhance our understanding and modeling of neural representations and expand to text extended-multimodality applications in the future.

### Weaknesses
The participant background is unclear; the authors briefly mention “high English fluency,” this indicates participants are non-native English speakers, so that standardized tests like IELTS or TOEFL would provide a more objective assessment of their reading proficiency, as language processing and brain activity can vary significantly between native and non-native speakers.

Regarding the dataset’s scale, while the total number of events and the recording duration are appreciated, the sample size of 15 participants appears comparable to, or even smaller than, existing studies, which may limit generalizability. 

The use of time-locked event recording could potentially induce stress in participants, particularly for non-native speakers (see my first concern). An analysis of the effects of this recording approach on participant responses would add depth to the study, possibly by examining trial-level data.

In EEG-based BCI studies, terms like “within-subject” and “across-subject” are more commonly used than “participant-dependent” and “participant-independent.” 

The intended purpose of this dataset could be more explicitly defined for ML-based classification (for section 5). Authors shall show that their dataset addresses the accuracy limitations observed in prior datasets. Studies like ZuCo have already demonstrated promising results in word relevance classification tasks, and a comparison or advancement upon those findings would strengthen the contribution of this dataset.

### Questions
See the above and the additional one below.

The ERP analysis lacks some clarity. Typical stimuli in previous EEG-based NLP research have been shown to elicit P300/N400 responses. It would be helpful to understand whether this study captures ERP responses across all words or only specific examples. Ideally, the study would present averaged or comprehensive ERP potentials for all words, with semantic labels serving as ground truth.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper releases an EEG dataset where the participants perform a Rapid Serial Visualisation Task, reading the words relevant/irrelevant to a preselected topic from Wikipedia. The work later benchmarks the performance of relevant word/sentence prediction from the EEG activity recorded during the task from 15 participants using 5 different prediction models in participant-dependent and independent scenarios.

### Strengths
The work plans to release the first public dataset for ERP analysis of semantic relevance in a RSV paradigm. The experimental paradigm and data collection is described with fair clarity. The dataset can significantly contribute to the domain as it opens up opportunities to build novel methods and benchmark performance on such tasks.

The work includes ERP analysis to validate the data with previous insights from literature and benchmarks 5 different architectures/models in both participation-independent and dependent scenarios.

### Weaknesses
It would be helpful to clearly define the novelty involved with this work. It is understood that while similar paradigms have been used before with different topics for the ERP analysis as cited by the authors, techniques/models are well known, novelty is limited to dataset availability and benchmark. 

The authors cite the limitation of the benchmark in terms of the models used that do not capture spatio-temporal features from the data. However, there are models available that have addressed such needs in recent literature, and a better state-of-the-art benchmark is a possibility. Authors may refer to : 
- STNet: https://torcheeg.readthedocs.io/en/v1.1.0/generated/torcheeg.models.STNet.html
Other models using Riemannian geometry:
- https://github.com/CECNL/MAtt
- https://github.com/zhiwu-huang/SPDNet

### Questions
While the work is explained with fair clarity, a few aspects need to be addressed:
1. The experimental paradigm can be explained with a diagram indicating the inter-stimulus interval. Authors mention each epoch as -200ms to 1000ms and later use 250ms to 950ms data for classification. It is confusing for the reader. This gives the impression that 200ms from previous trials/stimuli has been considered as the baseline.

2. It would be helpful to explain the shortest and the longest word and the font size. It is known that visual cues, including font size and style, impact ERP components as far as N400. While the work ignores the first 250ms, checking visual cues is also important.

3. For Figure 2a and 2b, the findings to be validated against insights from previous literature can be better represented with selective channels. As per the reference Eugster et al 2016:  "initial fronto-central positivity at 300 ms, relative to the onset of the word on the screen, followed by a centro-parietal positivity from 400 to 600 ms." The topography in Fig 2a and 2b are challenging to comprehend, while the figures in the appendix are a bit easier to comprehend and compare.

4. The applications' significance and outcomes can be elaborated in the discussion for the readers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an EEG dataset collected from participants as they read sentences presented word by word on a screen. In each trial, participants chose one of two randomly selected topics from a pool of 30 and read sentences from documents related to both topics in alternating order. They were instructed to focus on their chosen topic, anticipating that they would need to explain something about it afterward, thus encouraging attention to semantically relevant words. This precise, word-by-word presentation minimizes confounding factors like eye movements, capturing time-locked EEG responses at the word level. Unlike existing datasets, this dataset uniquely captures semantic relevance in EEG signals with controlled stimuli. The authors benchmarked two tasks—word relevance prediction and sentence relevance prediction—using five well-known EEG analysis models: Linear Discriminant Analysis, Logistic Regression, EEGNet, LSTM, and UERCM. For word relevance prediction, they aimed to determine whether a word is semantically relevant to the chosen topic based on time-locked EEG epochs, with ground truth labels assigned by majority vote from three annotators. For sentence relevance prediction, they predicted whether a sentence belonged to the participant's selected topic using aggregated EEG data from its words. This dataset and initial benchmarks aim to advance research in language relevance, psycholinguistics, and the development of brain-computer interface devices for online detection of semantic relevance.

### Strengths
- The authors implemented a rigorous data acquisition procedure to minimize confounding factors such as eye movements and task engagement. By presenting words one at a time with consistent timing, they enhanced the reliability and validity of the EEG recordings.

- The authors benchmark experiments using five well-known models on two classification tasks (word relevance and sentence relevance) offers valuable baseline results. This enables future research to compare new models against these benchmarks.

- The paper is overall well written and easy to follow. Methodology about the data acquisition is clear and through.

### Weaknesses
- The dataset emphasizes word-level EEG responses, but semantic understanding in the human brain is typically constructed over larger contexts, such as sentences or entire passages. This focus on individual words may not fully capture the continuous and contextual nature of semantic processing. As a result, the dataset might have limited applicability for studying natural language comprehension in real-world settings where context plays a crucial role.

- While the authors attempted to balance topic representation, the dataset still exhibits inconsistencies because participants selected different topics to focus on during the trials. Since each participant was presented with a unique combination of topics and chose their preferred topic from randomly selected pairs, the exposure to specific topics varies across participants. This variability can introduce inconsistencies in the dataset, as some topics may have more data associated with them than others, and participants may not have been equally distributed across all topics. To address this issue, the authors could have standardized the topic selection process to ensure that all participants are exposed to the same set of topics, or at least to a balanced and representative subset. 

- The annotation process for determining word-level semantic relevance does not seem appropriate. The guidelines provided to annotators were not detailed enough, which may have led to inconsistent labeling—especially for words like "contains" and "stated" (line 250) that can be relevant depending on context. Moreover, with only three annotators involved, there's a higher risk that personal biases could influence the results. To improve the reliability and consistency of the annotations, the authors should offer more detailed, context-aware guidelines to the annotators and consider increasing the number of annotators to reduce individual biases. Incorporating systematic methods, such as semantic similarity measures, could also help validate and refine the annotations, making the dataset more robust.

- The classification results (table 3), particularly in the participant-independent setting, are only slightly better than chance levels. Precision scores hover around 51–57%, which, given the class imbalance, indicates limited predictive power. This modest performance questions the practical utility of the models and suggests that decoding semantic relevance from EEG signals remains a significant challenge with the current approach/dataset. The authors could have explored more state-of-the-art models for their classification task or did some ablation studies and tune the hyperparameters for their training for the optimal result on their dataset.

- One area for improvement could be adding statistical significance testing to determine whether the observed results are meaningful or could have occurred by chance. This would make it easier to assess/compare the true effectiveness of the proposed models.

### Questions
-The LDA and LR models perform worse in the participant-dependent setting compared to the participant-independent setting, which is counterintuitive. Typically, models fine-tuned on individual participants' data should perform better due to personalization.  What could explain this?

- Although the authors state that the dataset and code are openly released, they were not made accessible during the review process. Is it possible to share it as a supplementary material for the sake of the review process?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel EEG dataset focused on semantic text relevance, comprising 23,270 word-level EEG recordings from participants reading texts that vary in semantic relevance to self-chosen topics. The dataset aims to bridge the gap between naturalistic reading studies and controlled psycholinguistic experiments. It provides a benchmark for evaluating models on tasks such as predicting word and sentence relevance. The dataset's contribution lies in advancing research on language relevance, psycholinguistics, and the development of brain-computer interfaces for detecting language relevance.

### Strengths
Originality
The manuscript presents a novel contribution by introducing an EEG dataset specifically designed for word-level semantic text correlation studies. The originality lies in its unique focus on capturing brain responses at the word level as opposed to broader natural reading or psycholinguistic paradigms commonly found in previous datasets. This is achieved through a carefully controlled experimental design where participants read sentences related or unrelated to personally chosen topics. The dataset's novelty is further emphasized by its potential to advance research in semantic processing and cognitive neuroscience.

Quality
The quality of the work is high, with meticulous attention given to the experimental setup, data collection methods, and preprocessing steps. The authors have conducted baseline experiments that include two evaluation protocols (participant-independent and participant-dependent) and two prediction tasks (lexical relevance and sentence relevance). They report benchmark performance using five established models, providing a solid foundation for future researchers to build upon. 

Clarity
The manuscript is well-structured and clearly written. Definitions of terms and descriptions of methodologies are presented in a manner that is easy to follow, facilitating understanding of the dataset's construction and usage. The clarity of the document is supported by appropriate use of figures, tables, and technical language that effectively communicate the complexity of the EEG data and analysis procedures.

Significance
The significance of this work lies not only in its immediate contribution to the field of cognitive neuroscience but also in its broader implications for the development of brain-computer interfaces (BCIs) and recommendation systems that utilize neural input and feedback. By enabling the detection of language relevance online, this dataset opens up new avenues for applications in personalized learning environments, adaptive interfaces, and other contexts where real-time cognitive state monitoring could be beneficial. Moreover, the dataset has the potential to stimulate interdisciplinary research efforts, bridging gaps between neuroscience, computer science, and linguistics.

### Weaknesses
In the experiment, the topic switching mode that was set is fixed, and this pattern might be easily discovered by the participants. If the participants can infer that the current sentence is unrelated to the chosen topic without reading the semantic content of the sentence, this would be detrimental to the experiment. Compared to alternately presenting sentences from different themes, would a random presentation be more appropriate?

### Questions
In ground truth annotation, if two adjacent words only carry thematic semantics when combined, would the word level annotation for such cases be inaccurate?

### Soundness
2

### Presentation
3

### Contribution
2
