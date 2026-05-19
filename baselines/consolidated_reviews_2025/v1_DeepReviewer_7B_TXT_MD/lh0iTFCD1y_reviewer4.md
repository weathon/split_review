### Summary

This paper proposes LUMA, a benchmark dataset for learning from uncertain and multimodal data. It includes image, audio, and textual data across 50 classes. The dataset is designed to evaluate the robustness of multimodal deep learning models in the presence of uncertainties. The authors also provide baseline models with three uncertainty quantification methods and a Python package for generating multiple variants of the dataset with controllable uncertainties.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important research problem by introducing a multimodal dataset that includes aleatoric and epistemic uncertainties, which is crucial for advancing robust and trustworthy multimodal learning.

2. The authors provide a well-structured Python package that enables the generation of multiple variants of the dataset with controllable uncertainties.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of how the uncertainties were generated. For example, in the audio modality, it is unclear how the noise was added, and the specific parameters used for the noise generation process are not detailed. This lack of clarity makes it difficult to assess the validity and reproducibility of the uncertainty modeling.

2. The paper does not provide a detailed analysis of the impact of the generated uncertainties on model performance. While the authors mention that the dataset is designed to evaluate model robustness, there is no in-depth analysis of how different types of uncertainties affect model behavior. For instance, it is unclear how the aleatoric and epistemic uncertainties interact and influence the model's predictions. A more thorough analysis, including ablation studies and visualizations, is needed to understand the impact of each uncertainty type.

3. The paper does not provide a comprehensive comparison with existing multimodal uncertainty benchmarks. While the authors mention that their dataset is unique, they do not provide a detailed comparison with other datasets that incorporate uncertainty. This makes it difficult to assess the novelty and significance of the proposed dataset. A thorough comparison with existing datasets, highlighting the differences in data distribution, uncertainty modeling, and evaluation protocols, is necessary to justify the contribution of this work.

### Suggestions

The authors should provide a detailed description of the uncertainty generation process for each modality, including the specific parameters used for each method. For the audio modality, the type of noise (e.g., white noise, colored noise), the signal-to-noise ratio, and the method used to inject the noise into the audio signals should be clearly specified. For text data, the method used to generate biased samples and the parameters used to control the degree of bias should be detailed. This level of detail is crucial for ensuring the reproducibility of the results and for allowing other researchers to build upon this work. Furthermore, the authors should justify the choice of noise parameters and explain how these parameters relate to real-world scenarios. Without this information, it is difficult to assess the validity and relevance of the generated uncertainties.

To address the lack of analysis on the impact of uncertainties, the authors should conduct a more in-depth analysis of how different types of uncertainties affect model performance. This should include ablation studies to assess the individual contributions of aleatoric and epistemic uncertainties. For example, the authors could train models on datasets with varying levels of aleatoric noise and evaluate their performance on clean and epistemic noisy data. Similarly, they could train models with varying levels of epistemic uncertainty and evaluate their performance on clean and aleatoric noisy data. Visualizations, such as heatmaps or scatter plots, could be used to illustrate the relationship between uncertainties and model predictions. Additionally, the authors should provide a more detailed discussion of the interaction between aleatoric and epistemic uncertainties and how they influence the model's behavior. This analysis should go beyond simply reporting performance metrics and should provide insights into the underlying mechanisms of uncertainty in multimodal learning.

Finally, the authors should provide a comprehensive comparison with existing multimodal uncertainty benchmarks. This comparison should include a detailed analysis of the data distribution, the types of uncertainties modeled, and the evaluation protocols used in each dataset. For example, the authors could compare their dataset with other multimodal datasets that incorporate uncertainty, highlighting the differences in the types of modalities, the methods used to generate uncertainties, and the evaluation metrics used. This comparison should not only focus on the differences in data but also on the differences in the way uncertainty is modeled and evaluated. A thorough comparison with existing datasets will help to justify the novelty and significance of the proposed dataset and will provide a clear understanding of its unique contributions to the field.

### Questions

Please refer to the weakness part.

### Rating

5

### Confidence

3

**********
