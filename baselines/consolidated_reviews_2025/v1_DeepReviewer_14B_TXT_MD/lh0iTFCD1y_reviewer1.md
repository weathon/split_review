### Summary

This paper introduces LUMA, a new benchmark dataset for learning from uncertain and multimodal data. The dataset includes image, audio, and text modalities across 50 classes, with controlled injection of aleatoric and epistemic uncertainties. The authors also provide baseline models and uncertainty quantification methods to serve as a starting point for benchmarking.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses the important problem of uncertainty in multimodal learning, which is crucial for real-world applications.
- The dataset is reasonably large, with 101,000 images, 135,096 audio recordings, and 62,875 text passages.
- The authors provide a Python package for generating dataset samples with varying levels of noise and uncertainty, which can be useful for research in this area.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear explanation of how the proposed dataset and benchmark address the challenges of multimodal uncertainty quantification. It is not clear how the dataset can be used to evaluate the performance of multimodal learning algorithms under different types of uncertainty.
- The paper does not provide a thorough analysis of the proposed dataset and benchmark. For example, it does not provide any insights into the characteristics of the dataset, such as the distribution of uncertainty levels, the correlation between modalities, and the impact of different types of noise on the performance of multimodal learning algorithms.
- The paper does not compare the proposed dataset and benchmark with existing datasets and benchmarks in terms of size, diversity, and quality. It is not clear how the proposed dataset and benchmark improve upon existing resources in the field.
- The paper does not provide a clear explanation of the baseline models and uncertainty quantification methods used for benchmarking. It is not clear how these methods were selected and how they perform on the proposed dataset.
- The paper does not provide a clear explanation of how the proposed dataset and benchmark can be used to advance the field of multimodal uncertainty quantification. It is not clear what new insights or discoveries can be made using the proposed dataset and benchmark.

### Suggestions

The paper needs to provide a more detailed explanation of how the LUMA dataset is specifically designed to address the challenges of multimodal uncertainty quantification. The authors should clarify how the controlled injection of aleatoric and epistemic uncertainties allows for a nuanced evaluation of multimodal learning algorithms. For instance, they should explain how different levels of noise in each modality affect the overall performance and how the dataset can be used to study the robustness of models under various uncertainty conditions. It would be beneficial to include a discussion on how the dataset enables the analysis of uncertainty propagation across modalities and how it can be used to develop methods that effectively combine information from different sources while accounting for their individual uncertainties. Furthermore, the authors should provide concrete examples of research questions that can be addressed using LUMA, such as investigating the impact of specific types of noise on different modalities or developing novel uncertainty-aware fusion techniques.

To enhance the analysis of the proposed dataset, the authors should include a comprehensive characterization of its properties. This should include a detailed analysis of the distribution of uncertainty levels within each modality and across the dataset as a whole. The authors should also investigate the correlation between modalities under different uncertainty conditions, providing insights into how noise in one modality affects the others. Furthermore, the paper should include a thorough evaluation of the impact of different types of noise on the performance of various multimodal learning algorithms. This analysis should not only focus on overall performance metrics but also on how uncertainty quantification methods behave under different noise conditions. The authors should also explore the potential biases or limitations of the dataset, providing a clear understanding of its scope and applicability. This detailed analysis will help researchers understand the dataset's characteristics and how to effectively use it for their research.

Finally, the paper should provide a more thorough comparison with existing datasets and benchmarks for multimodal learning and uncertainty quantification. The authors should clearly articulate how LUMA differs from existing resources in terms of size, diversity, and the types of uncertainties it encompasses. A detailed comparison should highlight the unique contributions of LUMA and its advantages over existing datasets. The authors should also provide a more detailed explanation of the baseline models and uncertainty quantification methods used for benchmarking, including the rationale behind their selection and a detailed analysis of their performance on the LUMA dataset. This should include a discussion of the strengths and weaknesses of each method and how they relate to the specific characteristics of the dataset. This will help researchers understand the benchmark results and how to effectively use them to evaluate their own methods.

### Questions

Please refer to the weaknesses.

### Rating

3

### Confidence

4

**********
