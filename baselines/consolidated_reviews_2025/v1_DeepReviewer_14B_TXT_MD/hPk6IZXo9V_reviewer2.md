### Summary

This paper proposes a two-step framework to reconstruct perceived speech from intracranial EEG. The first step is to train an LSTM-based adapter to align neural representations with text embeddings. The second step is to train a corrector module to convert these aligned embeddings into continuous text. The framework shows strong performance in both low-data and zero-shot settings.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed framework shows strong performance in low-data and zero-shot settings.
2. The paper is clearly written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this work is limited. The proposed framework is a straightforward application of existing approaches to neural data.
2. The comparison against the baseline is unfair. The proposed framework leverages pre-trained models, while the baseline does not.

### Suggestions

The paper's primary weakness lies in its limited novelty. While the authors have applied existing techniques to a new domain, the core methodology lacks significant innovation. The use of an LSTM adapter to align neural representations with text embeddings, followed by a corrector module for text generation, is a relatively standard approach in the field of neural decoding. The paper would benefit from a more in-depth exploration of the specific challenges posed by iEEG data and how the proposed framework uniquely addresses these challenges. For example, the authors could have investigated the impact of different neural features or explored more sophisticated alignment techniques that are tailored to the temporal dynamics of iEEG signals. Furthermore, a more detailed analysis of the limitations of existing methods when applied to iEEG data would strengthen the justification for the proposed approach. The current presentation makes it seem like a direct application of existing methods, rather than a novel contribution to the field.

To address the concern about the unfair comparison, the authors should provide a more detailed justification for their choice of baseline. While the baseline is a relevant method in the field, the use of pre-trained models in the proposed framework gives it a significant advantage, especially in low-data regimes. A more robust comparison would involve either adapting the baseline to also leverage pre-trained models or using a different baseline that does not rely on pre-training. The authors could also consider performing an ablation study to quantify the contribution of the pre-trained models to the overall performance of the framework. This would help to isolate the specific benefits of the proposed architecture from the benefits of pre-training. Additionally, the authors should provide a more detailed analysis of the performance of the baseline, including the specific parameters used and the training procedure. This would help to ensure that the comparison is as fair as possible.

Finally, the paper would benefit from a more thorough analysis of the results. While the authors report performance metrics, they do not provide a detailed analysis of the types of errors made by the framework. For example, it would be useful to know whether the framework struggles more with specific types of words or phrases. This would provide valuable insights into the limitations of the approach and suggest directions for future research. The authors should also consider performing a qualitative analysis of the reconstructed text to better understand the strengths and weaknesses of the framework. This could involve comparing the reconstructed text to the original text and identifying any patterns or trends in the errors. A more detailed analysis of the results would strengthen the paper and provide a more complete picture of the performance of the proposed framework.

### Questions

Please see the weaknesses.

### Rating

3

### Confidence

3

**********
