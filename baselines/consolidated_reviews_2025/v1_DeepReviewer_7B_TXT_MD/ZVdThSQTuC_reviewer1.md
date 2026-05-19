### Summary

The authors present a new dataset of EEG recordings of participants reading text, with annotations for semantic relevance of each word to a topic. They benchmark a few models on two classification tasks: relevance of a single word, and relevance of a sentence.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well written, and the figures are clear. The authors provide a new dataset, which will be of interest to the ICLR community. The authors compare their results to previous work, and provide a thorough discussion of their results.

### Weaknesses

#### Some Related Works


#### comment

The authors do not describe the dataset in sufficient detail. The authors do not provide a link to the dataset repository, and it is unclear whether the dataset will be made publicly available. The authors do not provide a clear description of the experimental design, and it is not clear how the authors ensured that the data was not contaminated by artifacts. The authors do not provide a clear description of the preprocessing steps applied to the EEG data, and it is not clear how the authors handled artifacts. The authors do not provide a clear description of the machine learning models used, and it is not clear how the authors selected the hyperparameters. The authors do not provide a clear description of the evaluation metrics used, and it is not clear how the authors handled class imbalance. The authors do not provide a clear description of the limitations of their work, and it is not clear how these limitations might affect the generalizability of their results.

### Suggestions

The authors should provide a detailed description of the dataset, including the number of participants, the number of words and sentences, and the number of EEG channels. They should also provide a link to a public repository containing the dataset, or at least a detailed description of the data format and structure. The authors should describe the experimental design in detail, including the stimuli used, the order in which the stimuli were presented, and the procedure used to collect the EEG data. They should also describe how they ensured that the data was not contaminated by artifacts, such as eye movements or head movements. The authors should provide a detailed description of the preprocessing steps applied to the EEG data, including the filtering, artifact removal, and channel selection. They should also describe how they handled artifacts, such as bad trials or bad segments. The authors should provide a detailed description of the machine learning models used, including the architecture, the loss function, and the optimization algorithm. They should also describe how they selected the hyperparameters, and they should provide a justification for their choices. The authors should provide a detailed description of the evaluation metrics used, including the metrics used to evaluate the performance of the models, and they should describe how they handled class imbalance. The authors should also discuss the limitations of their work, and they should suggest directions for future research. For example, they could discuss the potential impact of the limited number of participants on the generalizability of their results, or the potential impact of the limited number of words and sentences on the generalizability of their models. They could also discuss the potential impact of the specific experimental design on the results, or the potential impact of the specific machine learning models on the results.

### Questions

What is the number of participants? What is the number of words? What is the number of sentences? How many EEG channels were used?

### Rating

3

### Confidence

5

**********
