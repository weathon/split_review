### Summary

This paper proposes a framework for reconstructing perceived speech from intracranial EEG (iEEG) recordings. The framework consists of two main components: an LSTM-based adapter that aligns neural signals with pre-trained text embeddings, and a corrector module that generates continuous text from these embeddings. The authors demonstrate that their approach outperforms a recent state-of-the-art method in low-data settings, achieving strong performance with as little as 30 minutes of neural data.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel framework, Neuro2Semantic, which combines an LSTM-based adapter with a corrector module to reconstruct perceived speech from iEEG recordings. This approach leverages transfer learning to achieve strong performance in low-data settings, which is particularly valuable in neuroscience where data is often limited.
2. The paper is generally well-written and easy to follow. The authors provide a clear description of their methodology, including the two-phase training process and the use of contrastive and triplet loss functions to align neural embeddings with text embeddings. The experimental setup and results are also presented in a straightforward manner.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of related work. While the authors mention some relevant studies, they do not provide a comprehensive review of existing approaches in neural decoding and semantic reconstruction. This makes it difficult to assess the novelty and significance of their contribution. Specifically, the paper should discuss methods that use similar neural data (iEEG) for language decoding, and those that employ sequence-to-sequence models for text reconstruction from neural signals. A more detailed comparison with these methods is needed to contextualize the proposed approach.
2. The evaluation metrics used in the paper (BLEU, WER, ROUGE) are primarily designed for machine translation and may not fully capture the semantic accuracy of the reconstructed text. While the authors also report BERTScore, which is a better measure of semantic similarity, they should consider incorporating other metrics that are more sensitive to semantic nuances, such as metrics based on contextualized word embeddings or semantic role labeling. Furthermore, the paper should provide a more detailed analysis of the types of errors made by the model, going beyond aggregate scores.
3. The paper does not provide a detailed analysis of the model's limitations. For example, it is unclear how the model performs on different types of speech (e.g., spontaneous speech vs. scripted speech) or in the presence of noise or artifacts in the iEEG data. The paper should also investigate the model's sensitivity to the quality and placement of electrodes, and how this might affect its performance across different subjects. A more thorough investigation of these factors is needed to understand the practical applicability of the proposed approach.
4. The paper lacks a detailed description of the dataset used in the experiments. Information about the size of the dataset, the characteristics of the speakers, and the recording conditions is missing. This makes it difficult to assess the generalizability of the results and to compare them with other studies. The paper should also specify how the data was preprocessed, including any filtering or artifact removal steps.

### Suggestions

The authors should significantly expand the related work section to include a more comprehensive review of existing methods for neural decoding and semantic reconstruction, particularly those using iEEG data and sequence-to-sequence models. This should include a detailed comparison of the proposed approach with these methods, highlighting the specific advantages and disadvantages of each. For example, the authors should discuss how their LSTM-based adapter compares to other methods for aligning neural data with text embeddings, such as those based on canonical correlation analysis or other dimensionality reduction techniques. They should also discuss how their corrector module compares to other sequence-to-sequence models used for text reconstruction, such as those based on transformers or other recurrent neural networks. This would provide a more solid foundation for assessing the novelty and significance of their contribution.

To address the limitations of the evaluation metrics, the authors should incorporate additional metrics that are more sensitive to semantic nuances. This could include metrics based on contextualized word embeddings, such as ELMo or BERT embeddings, which can capture the meaning of words in context. They could also consider using metrics based on semantic role labeling, which can assess the accuracy of the reconstructed text in terms of its semantic structure. Furthermore, the authors should provide a more detailed analysis of the types of errors made by the model, going beyond aggregate scores. This could include a qualitative analysis of the reconstructed text, identifying common errors such as word substitutions, omissions, or additions. This would provide a more nuanced understanding of the model's strengths and weaknesses.

Finally, the authors should conduct a more thorough analysis of the model's limitations, including its performance on different types of speech, its sensitivity to noise and artifacts in the iEEG data, and its dependence on electrode quality and placement. This could involve experiments with different types of speech, such as spontaneous speech and scripted speech, as well as experiments with simulated noise and artifacts. The authors should also investigate the model's performance across different subjects, and how this might be affected by differences in electrode placement and data quality. This would provide a more realistic assessment of the model's practical applicability and its potential for generalization to new datasets.

### Questions

1. Could the authors provide more details about the dataset used in the experiments, including the size of the dataset, the characteristics of the speakers, and the recording conditions? This information is crucial for assessing the generalizability of the results.
2. How does the proposed approach compare to other state-of-the-art methods for neural decoding and semantic reconstruction? The authors should provide a more detailed comparison with existing methods, including a discussion of the advantages and disadvantages of each approach.
3. What are the computational requirements of the proposed framework? The authors should provide more details about the training time, memory usage, and other computational aspects of their approach. This information is important for assessing the practicality of the method.
4. How does the model perform on different types of speech (e.g., spontaneous speech vs. scripted speech)? The authors should investigate the model's performance on different types of speech to assess its robustness and generalizability.
5. How sensitive is the model to the quality and placement of electrodes? The authors should investigate the model's sensitivity to these factors, as they can vary significantly across subjects and recording sessions.

### Rating

5

### Confidence

3

**********
