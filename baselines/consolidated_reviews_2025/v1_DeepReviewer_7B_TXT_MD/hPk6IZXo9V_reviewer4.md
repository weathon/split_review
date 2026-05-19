### Summary

This paper presents Neuro2Semantic, a framework for reconstructing continuous language from intracranial EEG (iEEG) signals. The approach uses a two-phase training process: first, an LSTM adapter aligns neural signals with pre-trained text embeddings, and second, a corrector module generates coherent text from these aligned embeddings. The model is trained on a dataset from three subjects listening to podcast-like conversations. It outperforms a baseline method in low-data settings and demonstrates zero-shot generalization capabilities. The framework achieves this without predefined vocabularies or constrained text generation, making it suitable for brain-computer interfaces and neural decoding.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written, with a clear presentation of the proposed method and its advantages. The authors provide a thorough description of the experimental setup, including the dataset, evaluation metrics, and comparisons with baseline methods. The results demonstrate that Neuro2Semantic outperforms the baseline, particularly in low-data settings, and exhibits promising zero-shot generalization capabilities. The authors also provide a detailed analysis of the model's performance across different percentages of training data and electrode usage, which highlights the data and resource efficiency of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

The paper does not address the potential impact of demographic factors, such as age and gender, on the model's performance. It is important to investigate whether the model's performance varies across different demographic groups. Additionally, the paper does not explore the model's performance in different language contexts, such as different languages or dialects. This is important because language understanding is highly dependent on cultural and linguistic variations. The authors should also consider the potential for bias in the model's performance, particularly if the training data is not representative of the broader population. Furthermore, the paper lacks a detailed discussion of the computational resources required for training and deploying the model, which is crucial for practical applications. The authors should provide information on the hardware and software requirements, as well as the training time and inference latency.

### Suggestions

To address the lack of demographic analysis, the authors should conduct experiments using a stratified dataset that includes age and gender as stratification factors. This would allow for a more granular understanding of the model's performance across different demographic groups. Specifically, the authors could analyze the model's performance on subsets of the data corresponding to different age ranges (e.g., <20, 20-40, 40-60, >60) and gender groups (male, female, non-binary). This analysis should not only focus on overall performance metrics but also on the consistency of the model's performance across these groups. Furthermore, the authors should investigate whether the model's performance is correlated with specific demographic characteristics, which could provide insights into the model's biases and limitations. This analysis should be presented with clear visualizations, such as bar charts or heatmaps, to facilitate understanding.

To address the limited exploration of language contexts, the authors should evaluate the model's performance on data from different languages and dialects. This could involve using a multilingual dataset or creating a dataset that includes text from different languages. The authors should also investigate whether the model's performance is affected by the linguistic features of the input text, such as sentence structure, vocabulary, and syntax. This analysis should include a comparison of the model's performance on different languages and dialects, as well as an analysis of the model's ability to generalize across different linguistic contexts. The authors should also consider the potential for language-specific biases in the model's performance, which could limit its applicability in real-world scenarios. This analysis should be presented with clear visualizations, such as scatter plots or line graphs, to facilitate understanding.

Finally, the authors should provide a detailed analysis of the computational resources required for training and deploying the model. This should include information on the hardware and software requirements, as well as the training time and inference latency. The authors should also discuss the scalability of the model and its potential for deployment on resource-constrained devices. This analysis should include a comparison of the computational resources required by the proposed model with those required by existing methods. The authors should also discuss the potential for optimizing the model's performance and reducing its computational footprint. This analysis should be presented with clear tables and figures to facilitate understanding.

### Questions

1. How does the model perform across different demographic groups, such as age and gender?
2. What is the impact of language context on the model's performance? How does the model perform on data from different languages or dialects?
3. What are the computational resources required for training and deploying the model?
4. How does the model's performance vary with different electrode placements?

### Rating

6

### Confidence

3

**********
