### Summary

The paper presents Neuro2Semantic, a framework for reconstructing language from intracranial EEG (iEEG) data. This framework consists of two phases: aligning neural data with text embeddings using an LSTM adapter and reconstructing continuous text with a corrector module. The method is evaluated on a dataset of three participants who listened to 30 minutes of speech.

### Soundness

2

### Presentation

3

### Contribution

1

### Strengths

The paper is clearly written and the method is clearly described.

### Weaknesses

#### Some Related Works


#### comment

I have two main issues with the paper: the overly broad claims and the insufficient results.

1. The claims of the paper are too broad. The title states "continuous language", but the evaluation is performed on a listening task. The introduction discusses applications such as "developing more flexible and data-efficient neural decoding models, with potential applications in augmentative and alternative communication technologies," suggesting communication applications. However, these claims are based on a single listening task with three participants.

2. The results are not convincing. The BLEU scores are below 10%, indicating poor reconstruction quality. Additionally, there is no comparison with a more straightforward baseline, such as a language model conditioned on keywords from the listening task. The example outputs also show no similarity to the ground truth.

### Suggestions

The paper needs to significantly temper its claims regarding the capabilities of the proposed Neuro2Semantic framework. The current framing suggests a general solution for neural language decoding, while the empirical evidence is limited to a very specific listening task with a small dataset. The title should be revised to reflect the narrow scope of the current evaluation, perhaps focusing on the specific task of reconstructing listened speech rather than making broad claims about continuous language reconstruction. Furthermore, the introduction should clearly state the limitations of the current study and avoid suggesting immediate applications in augmentative and alternative communication technologies. It is crucial to acknowledge that the current results are a preliminary step towards these broader goals, rather than a demonstration of their immediate feasibility. The authors should also consider adding a discussion section that explicitly addresses the limitations of the current study and outlines the steps needed to achieve the broader goals they mention.

To improve the evaluation, the authors should include a more robust set of baselines. A simple keyword-based retrieval system, as suggested, is a minimum requirement for comparison. This baseline would involve identifying key words from the audio stimulus and using these to retrieve relevant sentences from a large corpus. This would provide a more grounded assessment of the proposed method's performance. Additionally, the authors should consider using more informative metrics beyond BLEU, such as ROUGE or METEOR, which may be more sensitive to semantic similarity. The authors should also provide a more detailed analysis of the reconstruction errors, identifying common types of errors and potential causes. This would provide valuable insights into the limitations of the current approach and guide future research. The example outputs should also be presented in a way that makes it easier to compare the reconstructed text with the ground truth, such as by highlighting the differences.

Finally, the paper should include a more detailed discussion of the limitations of the current study. This should include a discussion of the small sample size, the specific nature of the listening task, and the limitations of the evaluation metrics. The authors should also discuss the potential impact of these limitations on the generalizability of the results. It is important to acknowledge that the current results may not generalize to other tasks or datasets. The authors should also discuss the potential for bias in the data and the need for more diverse datasets in future research. By addressing these limitations, the authors can provide a more balanced and realistic assessment of the proposed method's capabilities.

### Questions

1. How does a simple retrieval-based approach perform? For example, given the audio stimulus, key words can be identified and used to retrieve K most relevant sentences from a large corpus.

2. Why is the evaluation performed on a listening task rather than a reading task, given that the title claims "continuous language"?

### Rating

3

### Confidence

4

**********
