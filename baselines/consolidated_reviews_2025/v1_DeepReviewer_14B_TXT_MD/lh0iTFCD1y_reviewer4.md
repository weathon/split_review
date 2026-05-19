### Summary

The paper presents LUMA, a new benchmark dataset designed for evaluating multimodal deep learning models under uncertainty. LUMA combines audio, image, and text modalities, building upon CIFAR-10/100 with added audio from three audio corpora and text generated using the Gemma-7B Large Language Model. The dataset includes mechanisms for controlled injection of aleatoric and epistemic uncertainties, allowing researchers to benchmark model robustness and uncertainty quantification methods. Baseline models and uncertainty quantification methods are provided, including Monte-Carlo Dropout, Deep Ensemble, and Reliable Conflictive Multi-View Learning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel multimodal dataset (LUMA) that integrates audio, image, and text modalities, which is a valuable resource for the research community.
2. The dataset includes mechanisms for controlled injection of aleatoric and epistemic uncertainties, allowing researchers to systematically evaluate model robustness under various noise conditions.
3. The paper provides baseline models and uncertainty quantification methods, which serve as a starting point for further research and development.
4. The authors address potential biases in the generated text data and take steps to mitigate them, demonstrating a commitment to ethical considerations in dataset creation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the dataset's characteristics, such as the distribution of data across different classes and modalities. This information is crucial for understanding the dataset's structure and potential biases.
2. The paper does not compare LUMA with other existing multimodal datasets, which would help to contextualize its contributions and limitations.
3. The paper does not provide a thorough evaluation of the baseline models and uncertainty quantification methods on the LUMA dataset. More comprehensive experiments and comparisons with state-of-the-art methods are needed to demonstrate the dataset's utility.
4. The paper does not discuss the potential biases or ethical considerations associated with the dataset, which is important for ensuring responsible use of the data.

### Suggestions

The authors should provide a detailed analysis of the dataset's characteristics, including the distribution of data across different classes and modalities. This should include not only the overall distribution but also the distribution within each modality (image, audio, text). For example, are some classes overrepresented in certain modalities? Are there any imbalances that could affect model training and evaluation? Furthermore, the authors should analyze the diversity of the data within each class and modality. This could involve calculating metrics such as the intra-class variance for images, the phonetic diversity for audio, and the semantic diversity for text. Such analysis would provide a more comprehensive understanding of the dataset's structure and potential biases, enabling researchers to use the dataset more effectively and avoid potential pitfalls.

To better contextualize the contributions of LUMA, the authors should compare it with other existing multimodal datasets. This comparison should not only focus on the size and modality types but also on the quality of annotations, the availability of uncertainty annotations, and the mechanisms for injecting uncertainty. For example, how does LUMA compare to datasets like CMU-MOSI or AudioSet in terms of the complexity of the data and the types of tasks that can be performed? A detailed comparison would help researchers understand the unique value proposition of LUMA and its suitability for different research questions. The authors should also discuss the limitations of LUMA compared to other datasets, such as the lack of real-world complexity or the potential for biases in the generated text data. This would provide a more balanced perspective on the dataset's strengths and weaknesses.

Finally, the authors should provide a more thorough evaluation of the baseline models and uncertainty quantification methods on the LUMA dataset. This should include a wider range of models and methods, as well as a more detailed analysis of their performance under different levels of injected uncertainty. For example, how do different uncertainty quantification methods perform when the data is corrupted with different types of noise? The authors should also investigate the sensitivity of the models to different hyperparameters and training strategies. Furthermore, the authors should compare the performance of the baseline models on LUMA with their performance on other datasets. This would provide a more comprehensive understanding of the dataset's difficulty and the effectiveness of the proposed methods. The evaluation should also include metrics that are relevant to uncertainty quantification, such as calibration error and sharpness.

### Questions

1. How does LUMA compare to other existing multimodal datasets in terms of size, diversity, and quality?
2. What are the specific characteristics of the dataset, such as the distribution of data across different classes and modalities?
3. How do the baseline models and uncertainty quantification methods perform on the LUMA dataset, and what are the key findings from this evaluation?
4. What are the potential biases or ethical considerations associated with the dataset, and how can they be addressed?

### Rating

6

### Confidence

3

**********
