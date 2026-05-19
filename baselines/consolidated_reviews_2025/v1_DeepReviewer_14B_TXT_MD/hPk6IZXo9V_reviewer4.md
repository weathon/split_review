### Summary

The paper presents Neuro2Semantic, a framework designed to reconstruct the semantic content of perceived speech from intracranial EEG (iEEG) recordings. The authors propose a two-phase approach: first, an LSTM-based adapter aligns neural signals with pre-trained text embeddings; second, a corrector module generates continuous, natural text directly from these aligned embeddings. The framework demonstrates strong performance, particularly in low-data settings, and shows promise for applications in brain-computer interfaces and neural decoding technologies.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The use of transfer learning to map neural activity to text is a significant advancement, especially in low-data scenarios.
2. The framework's ability to generalize in zero-shot settings is a notable strength, distinguishing it from models limited by specific training sets and vocabularies.
3. The paper is well-structured and clearly written, with detailed descriptions of the methodology, model architecture, and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The model's performance is heavily dependent on the accuracy of the Vec2Text corrector, which may limit its effectiveness in handling domain-specific or rare vocabulary. This dependency could lead to issues when the model encounters words or phrases that are not well-represented in the training data of the corrector module, potentially causing it to generate semantically incorrect or nonsensical text. The reliance on a single corrector module also introduces a single point of failure, which could be problematic in real-world applications.
2. The generalizability of the model may be affected by variability in neural recordings across subjects or different brain regions. The model's performance could degrade significantly when applied to new subjects with different neural patterns or when analyzing data from brain regions not included in the training set. This lack of robustness to inter-subject and inter-regional variability is a major concern for the practical application of the model.
3. The framework's reliance on pre-trained text embeddings and the Vec2Text corrector introduces potential biases inherent in these models, which could affect the accuracy and reliability of the text reconstruction. The pre-trained embeddings may not fully capture the nuances of the semantic space, and the corrector module may introduce its own biases, leading to skewed or inaccurate text reconstructions. This could be particularly problematic when dealing with complex or ambiguous semantic content.

### Suggestions

To address the dependency on the Vec2Text corrector, the authors should explore methods to make the model more robust to out-of-vocabulary words and domain-specific terms. This could involve incorporating a mechanism for handling unknown words, such as using sub-word embeddings or a character-level model, or fine-tuning the corrector module on a more diverse dataset that includes a wider range of vocabulary. Additionally, the authors could investigate the use of ensemble methods, where multiple corrector modules are trained and their outputs are combined to improve robustness and reduce the impact of individual module biases. This would also help to mitigate the single point of failure issue.

To improve the generalizability of the model across subjects and brain regions, the authors should consider incorporating techniques for domain adaptation or transfer learning. This could involve training the model on a larger and more diverse dataset that includes data from multiple subjects and brain regions, or using adversarial training methods to learn representations that are invariant to subject-specific and region-specific variations. Furthermore, the authors could explore the use of meta-learning techniques, which allow the model to quickly adapt to new subjects or brain regions with minimal fine-tuning. This would significantly enhance the practical applicability of the model in real-world scenarios.

To mitigate the potential biases introduced by pre-trained text embeddings and the Vec2Text corrector, the authors should conduct a thorough analysis of these biases and their impact on the model's performance. This could involve evaluating the model's performance on different types of text and identifying any systematic biases in the reconstructed text. The authors could also explore the use of debiasing techniques, such as adversarial training or re-weighting the training data, to reduce the impact of these biases. Furthermore, the authors should consider using multiple pre-trained embeddings and corrector modules to reduce the reliance on a single model and improve the robustness of the framework.

### Questions

1. How does the model handle out-of-vocabulary words or domain-specific terms that may not be well-represented in the pre-trained embeddings?
2. What measures have been taken to ensure that the model is not overfitting to the specific characteristics of the training data, especially given the limited dataset size?
3. How does the model perform when applied to data from brain regions not included in the training set, and what steps could be taken to improve its generalizability across different brain regions?

### Rating

6

### Confidence

3

**********
