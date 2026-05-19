### Summary

This paper introduces a novel framework called Neuro2Semantic, designed to reconstruct semantic content from intracranial EEG (iEEG) signals. The framework consists of two phases: the first aligns neural signals with pre-trained text embeddings, and the second generates continuous text from these aligned embeddings. This approach overcomes the limitations of previous methods that rely on predefined vocabularies or require constrained text generation. The authors demonstrate that Neuro2Semantic achieves remarkable performance with as little as 30 minutes of neural data, significantly outperforming baseline methods in low-data settings. Additionally, the framework shows promising zero-shot generalization capabilities, suggesting its potential for real-world applications in brain-computer interfaces and neural decoding technologies.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed two-phase training process is innovative, leveraging transfer learning to align neural signals with pre-trained text embeddings and then generating continuous text from these embeddings. This approach is novel and effectively addresses the challenge of decoding semantic content from neural signals.
2. The paper is well-organized and clearly presented. The authors provide a thorough description of the methods, experimental setup, and results, making it easy for readers to follow and understand the proposed framework.
3. The authors provide extensive quantitative results and qualitative examples, demonstrating the effectiveness of Neuro2Semantic in reconstructing semantic content from neural signals. The comparisons with baseline methods and the analysis of performance under different conditions further strengthen the validity of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. While the authors claim that Neuro2Semantic can reconstruct semantic content from as little as 30 minutes of neural data, the paper does not provide a detailed analysis of how the amount of training data affects the performance of the model. Specifically, it is unclear how the model's performance scales with increasing data, and whether there is a point of diminishing returns. A more thorough investigation into the data efficiency of the model is needed.
2. The authors do not provide a comprehensive comparison of their method with other state-of-the-art neural decoding techniques. While they compare their method with one baseline, a broader comparison with other relevant methods would help to better position the contribution of this work. This comparison should include methods that use different neural data modalities and decoding approaches to provide a more complete picture of the model's performance relative to the field.
3. The authors do not provide a detailed analysis of the model's performance across different semantic domains. It is important to understand whether the model generalizes well to unseen semantic content or if it is limited to the specific domains it was trained on. This analysis should include a quantitative assessment of the model's performance on out-of-domain data, as well as a qualitative analysis of the generated text to identify any systematic biases or limitations.
4. The authors do not provide a detailed analysis of the model's performance across different electrode locations. It is important to understand whether the model's performance is consistent across different electrode locations or if it is biased towards certain regions of the brain. This analysis should include a quantitative assessment of the model's performance on different electrode subsets, as well as a qualitative analysis of the generated text to identify any systematic biases or limitations.

### Suggestions

To address the lack of detailed analysis on the impact of training data size, the authors should conduct a more comprehensive study that systematically varies the amount of training data used for the model. This could involve training the model on subsets of the available data, ranging from very small amounts (e.g., 10 minutes) to the full dataset. The performance of the model should be evaluated on each subset using a variety of metrics, including both quantitative measures (e.g., BLEU score, ROUGE score) and qualitative assessments of the generated text. This analysis should also include a comparison of the model's performance across different semantic domains, to assess its generalization capabilities. Furthermore, the authors should investigate the impact of different data augmentation techniques on the model's performance, as this could potentially improve its robustness and generalization ability. This would provide a more complete understanding of the model's data efficiency and its ability to generalize to new data and domains.

To strengthen the comparison with other state-of-the-art neural decoding techniques, the authors should include a broader range of baseline methods in their evaluation. This should include methods that use different neural data modalities (e.g., MEG, EEG) and decoding approaches (e.g., classification-based, generative-based). The comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated text, to assess the semantic accuracy and coherence of the model's output. The authors should also consider using a more diverse set of evaluation datasets, to assess the model's performance across different experimental conditions and semantic domains. This would provide a more comprehensive and robust evaluation of the model's performance relative to the state-of-the-art.

Finally, to address the lack of analysis on the impact of electrode locations, the authors should conduct a more detailed investigation into the model's performance across different electrode subsets. This could involve training the model on different combinations of electrodes and evaluating its performance on each subset. The authors should also investigate the impact of different electrode selection strategies on the model's performance, as this could potentially improve its robustness and generalization ability. Furthermore, the authors should provide a more detailed analysis of the model's performance on different types of semantic content, to assess its ability to generalize to unseen domains. This analysis should include both quantitative and qualitative assessments of the generated text, to identify any systematic biases or limitations. This would provide a more complete understanding of the model's strengths and weaknesses and its potential for real-world applications.

### Questions

1. How does the amount of training data affect the performance of Neuro2Semantic? Are there any diminishing returns when using larger datasets?
2. How does Neuro2Semantic compare with other state-of-the-art neural decoding techniques in terms of performance and efficiency?
3. How well does Neuro2Semantic generalize to unseen semantic content or different domains? Are there any systematic biases or limitations in the model's performance?
4. How does the performance of Neuro2Semantic vary across different electrode locations? Is the model biased towards certain regions of the brain?

### Rating

3

### Confidence

4

**********
