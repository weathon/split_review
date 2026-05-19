### Summary

This paper proposes a new benchmark dataset for multimodal learning, which includes 101,000 images, 135,000 audio recordings, and 6,000 text samples, across 50 classes. The authors also provide baseline models with three uncertainty quantification methods and a Python package that generates multiple variants of the dataset with controllable uncertainties.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors provide a detailed description of the dataset construction process, including the extraction of deep features from each modality and the computation of inverse distances to the center of each class. The use of the t-SNE visualization to demonstrate the effectiveness of the diversity control method is also helpful.
2. The authors provide a comprehensive analysis of the dataset's properties, including the distribution of data points across classes, the impact of label noise, and the performance of baseline models with different uncertainty quantification methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of how the uncertainties were generated. For example, in the audio modality, it is unclear how the noise was added, and the specific parameters used for the noise generation process are not detailed. This lack of clarity makes it difficult to assess the validity and reproducibility of the uncertainty modeling.
2. The paper does not provide a detailed analysis of the impact of the generated uncertainties on model performance. While the authors mention that the dataset is designed to evaluate model robustness, there is no in-depth analysis of how different types of uncertainties affect model behavior. For instance, it is unclear how the aleatoric and epistemic uncertainties interact and influence the model's predictions. A more thorough analysis, including ablation studies and visualizations, is needed to understand the impact of each uncertainty type.
3. The paper does not provide a comprehensive comparison with existing multimodal uncertainty benchmarks. While the authors mention that their dataset is unique, they do not provide a detailed comparison with other datasets that incorporate uncertainty. This makes it difficult to assess the novelty and significance of the proposed dataset. A thorough comparison with existing datasets, highlighting the differences in data distribution, uncertainty modeling, and evaluation protocols, is necessary to justify the contribution of this work.

### Suggestions

The authors should provide a detailed description of the uncertainty generation process, including the specific parameters used for each modality. For the audio modality, the type of noise (e.g., white noise, colored noise), the signal-to-noise ratio, and the method used to inject the noise into the audio signals should be clearly specified. For text data, the method used to generate biased samples and the parameters used to control the degree of bias should be detailed. This level of detail is crucial for ensuring the reproducibility of the results and for allowing other researchers to build upon this work. Furthermore, the authors should justify the choice of noise parameters and explain how these parameters relate to real-world scenarios. Without this information, it is difficult to assess the validity and relevance of the generated uncertainties.

To address the lack of analysis on the impact of uncertainties, the authors should conduct a more in-depth analysis of how different types of uncertainties affect model performance. This should include ablation studies to assess the individual contributions of aleatoric and epistemic uncertainties. For example, the authors could train models on datasets with varying levels of aleatoric noise and evaluate their performance on clean and epistemic noisy data. Similarly, they could train models with varying levels of epistemic uncertainty and evaluate their performance on clean and aleatoric noisy data. Visualizations, such as heatmaps or scatter plots, could be used to illustrate the relationship between uncertainties and model predictions. Additionally, the authors should provide a more detailed discussion of the interaction between aleatoric and epistemic uncertainties and how they influence the model's behavior. This analysis should go beyond simply reporting performance metrics and should provide insights into the underlying mechanisms of uncertainty in multimodal learning.

Finally, the authors should provide a comprehensive comparison with existing multimodal uncertainty benchmarks. This comparison should include a detailed analysis of the data distribution, the types of uncertainties modeled, and the evaluation protocols used in each dataset. For example, the authors could compare their dataset with other multimodal datasets that incorporate uncertainty, highlighting the differences in the types of modalities, the methods used to generate uncertainties, and the evaluation metrics used. This comparison should not only focus on the differences in data but also on the differences in the way uncertainty is modeled and evaluated. A thorough comparison with existing datasets will help to justify the novelty and significance of the proposed dataset and will provide a clear understanding of its unique contributions to the field.

### Questions

1. How are the uncertainties generated in the proposed dataset? Specifically, what methods are used to inject noise or biases into each modality, and how are the parameters for these methods chosen?
2. How does the proposed dataset compare with existing multimodal uncertainty benchmarks? What are the key differences in terms of data distribution, uncertainty modeling, and evaluation protocols?
3. How does the performance of models trained on the proposed dataset compare with models trained on other multimodal uncertainty benchmarks?

### Rating

3

### Confidence

3

**********
