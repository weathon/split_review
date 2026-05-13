# Revisiting PCA for Time Series Reduction in Temporal Dimension

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Deep learning has significantly advanced time series analysis (TSA), enabling the extraction of complex patterns for tasks like classification, forecasting, and regression. While dimensionality reduction has traditionally focused on the variable space—achieving notable success in minimizing data redundancy and computational complexity—less attention has been paid to reducing the temporal dimension. In this study, we revisit Principal Component Analysis (PCA), a classical dimensionality reduction technique, to explore its utility in temporal dimension reduction for time series data. It is generally thought that applying PCA to the temporal dimension would disrupt temporal dependencies, leading to limited exploration in this area. However, our theoretical analysis and extensive experiments demonstrate that applying PCA to sliding series windows not only maintains model performance but also enhances computational efficiency. In auto-regressive forecasting, the temporal structure is partially preserved through windowing, and PCA is applied within these windows to denoise the time series while retaining their statistical information. By preprocessing time series data with PCA, we reduce the temporal dimensionality before feeding it into TSA models such as Linear, Transformer, CNN, and RNN architectures. This approach accelerates training and inference and reduces resource consumption. Notably, PCA improves Informer training and inference speed by up to 40% and decreases GPU memory usage of TimesNet by 30%, without sacrificing model accuracy. Comparative analysis against other reduction methods further highlights the effectiveness of PCA in enhancing the efficiency of TSA models. Code is provided in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript revisits Principal Component Analysis (PCA) to explore its utility in reducing the temporal dimension of time series data, as a novel area of focus, because PCA has traditionally been applied mostly on the variable space. The paper posits that PCA, when applied to sliding series windows, not only maintains model performance but also enhances computational efficiency. Extensive experiments across time series classification, forecasting, and extrinsic regression tasks substantiate these claims. The paper suggests that PCA preprocessing results in reduced training and inference times without compromising on model effectiveness across various deep learning-based time series analysis models.

### Strengths
S1. This paper attempts to improve the efficiency of time series analysis tasks, which can be very useful for resource-constrained scenarios including edge computing.

S2. The evaluation was conducted on three different tasks, i.e., time series classification, forecasting, and extrinsic regression, demonstrating the versatility of the proposed methods.

S3. The paper is easy-to-parse.

### Weaknesses
W1. It is still hard to conclude from this paper that PCA before feeding into deep neural networks is a versatile solution that should be suggested to time series analysis tasks under resource constraints. Briefly speaking, neural networks, especially the early layers of neural networks, are considered as feature extraction as well as dimension adjusting. This overlaps a bit with the purpose of PCA. Specifically, the paper does not adequately address the potential redundancy introduced by applying PCA prior to deep learning models, which are themselves capable of learning complex feature representations. The authors should provide a more thorough justification for why PCA is beneficial given the inherent dimensionality reduction capabilities of neural networks, especially in the context of time series data where temporal dependencies are crucial and may be disrupted by PCA.

W2. There are more dimensional reduction techniques for time series or high-dimensional vectors, rather than PCA itself. For example, DWT, FFT, etc. Although have been briefly discussed, it would still be very important to compare PCA with other deep model-agnostic dimension reduction techniques. The discussion should include a more detailed analysis of the trade-offs between PCA and other methods in terms of computational cost, information loss, and impact on model performance. For instance, frequency-based methods like FFT and DWT might preserve temporal information better than PCA, which focuses on variance, and this should be explored in more detail.

### Questions
Q1. The discussions provided in section 3.2 are not really theoretical analysis. The section title is a bit misleading. I would suggest to either break this section down to the motivation of the work, or rename it to some candidates like intuitional justification.

Q2. In line 340, why only 5 datasets from the UEA is selected, out of 30+ multivariate datasets? Also, the five datasets are finally precessed into univariate datasets, in which case why the original 100+ univariate datasets are excluded?

Q3. The accuracy reported in table 2 is pretty low on the first two datasets. And the differences with or without PCA are huge on some cases, e.g., FEDformer and TimesNet on SelfRegulationSCP1. Could the authors provide justification for these numbers? Otherwise, this would damage the versatility of the proposed approach.

Q4. What is the backbone model for the results in Table 5?

Q5. I am not sure if I fully understood line 302-304, “For example, if all positive trends…” Could the authors further explain a bit on this for me? Thanks!

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the application of Principal Component Analysis (PCA) for dimensionality reduction of the temporal dimension. The authors argue that PCA's ability to reduce dimensionality enables the extraction of essential features underlying time series, thereby improving the efficiency of downstream tasks. Experimentally, the study applies forecasting, classification, and extrinsic regression tasks to the PCA-learned representations. The results show significant improvements in computational time and memory consumption compared to purely supervised approaches applied directly to the raw time series.

### Strengths
- S1. I think it is interesting to use unsupervised learning as a first step to reduce memory and computation time for downstream supervised tasks. This approach could be particularly beneficial when dealing with large amounts of time series data with numerous timestamps.

- S2. The paper is well written and easy to follow, making the concepts and methods presented clear and accessible to the reader.

- S3. The experimental results show that PCA accelerates both the training and inference processes while reducing the GPU memory usage for the considered downstream tasks.

### Weaknesses
 - W1. A significant weakness of the paper is its lack of discussion and comparison with other representation learning methods.
     - Several claims in the paper appear to be inaccurate, such as: "To the best of our knowledge, there has been no systematic method for compressing time series data in the temporal dimension while preserving critical information" and "far less attention has been given to reducing the temporal dimension, despite the potential benefits of alleviating the burdens associated with processing long time series." In recent years, various unsupervised time series methods have effectively addressed this issue. For example, T-Loss [1] was one of the first models to fully compress the temporal dimension by leveraging contrastive learning and an encoder-only architecture. Another contrastive method, TS2Vec [2], learns representations that can be used for forecasting and classification in subsequent stages. Additionally, methods based on autoencoders with vector quantization [3,4] have demonstrated the ability to compress the temporal dimension by learning the core features of time series data.      
    - The use of PCA representation does not appear to enhance the performance of the supervised model. While the authors argue that PCA representation accelerates training and inference (and reduces memory usage), the omission of other representation learning methods—such as a basic convolutional encoder-decoder—makes it difficult to fully evaluate the contribution of this paper.


- W2. From an experimental perspective, several aspects seem questionable.
    - For the classification tasks, the authors selected a few datasets from the UEA and applied PCA pairs with models that are primarily known as forecasting baselines (except for TimesNet). The reported results, whether with or without PCA, do not represent state-of-the-art performance. It would have been beneficial to include models like InceptionTime or a simple ResNet for comparison.      
    - In the forecasting tasks, the authors focused solely on the ETT datasets, which are recognized for their difficulty in forecasting. It would be more insightful to conduct similar experiments on datasets such as traffic or electricity, which may provide additional context and validation for the proposed methods.

### Questions
- Q1. Could you please include a comparative analysis section in their paper, directly comparing PCA's performance, computational efficiency, and memory usage against the methods you mentioned (T-Loss, TS2Vec, and autoencoder-based approaches). This would provide a clearer context for evaluating PCA's contribution relative to recent advances in the field.

- Q2. Coud you please include state-of-the-art classification models like InceptionTime and ResNet in their comparison for the classification tasks, providing a stronger baseline for evaluating PCA's impact.

- Q3. I Believe that it would be valuable to expand the forecasting experiments to include additional widely-used datasets such as traffic and electricity, alongside the ETT datasets. Suggest specific datasets that are commonly used in the field for benchmarking.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose an innovative approach for preprocessing time series data by applying Principal Component Analysis (PCA) to data within sliding windows. This method aims to extract the principal components from the data, effectively reducing dimensionality before feeding it into a deep learning network. Traditionally, it is commonly believed that applying PCA along the time dimension can disrupt temporal dependencies inherent in time series data. Contradicting this notion, the authors suggest that applying PCA to sliding sequence windows can preserve model performance while enhancing computational efficiency. They support their claims with experiments conducted on three primary tasks: time series classification, prediction, and regression.

### Strengths
The idea of applying PCA within sliding windows offers a fresh perspective on dimensionality reduction for time series data. By reducing the dimensionality of the input data, the proposed method can decrease computational load, which is particularly beneficial for deep learning models dealing with large-scale or high-frequency time series data.

### Weaknesses
The study exhibits several weaknesses. Firstly, it lacks clarity on dimensionality reduction along the time dimension, focusing instead on feature dimension reduction without reducing time steps, which contradicts its stated goal. Secondly, the application of PCA to the test data in classification tasks is ambiguous; applying PCA to test data is inappropriate, but without it, the claimed acceleration in inference time lacks justification. Thirdly, the study misrepresents related work by critiquing standard practices designed to prevent information leakage, and its theoretical analysis fails to support the core claim of time dimension reduction. Additionally, the experiments lack statistical validation and parameter exploration, relying on single runs with fixed principal component numbers, raising concerns about generalizability and potential overfitting. The authors make overgeneralized and absolute claims about the benefits of PCA without sufficient evidence, ignoring observed performance degradation in certain datasets. Furthermore, limited dataset diversity suggests results may be dataset-specific, and discrepancies in reported data raise doubts about reliability. Lastly, the study challenges established concepts in time series analysis without adequate empirical support, and methodological inconsistencies, such as varying the number of principal components without clear rationale, hinder reproducibility and limit the applicability of the findings.

1. The paper does not seem to demonstrate whether the number of time steps is reduced or to what extent. It only generally mentions at the beginning that applying PCA will compress the time series, but it is unclear whether the compression target is the time steps or the data component features within the sliding window. In the Introduction, the authors state that dimensionality reduction techniques for time series data mainly focus on the variable dimension, and they intend to apply PCA for dimensionality reduction along the time dimension. However, from the overall description, the authors appear to only apply PCA to the time-step data within the sliding window to extract local features. This method extracts feature information from each window, but the number of time steps within the window seems to remain unchanged. 

2. It is currently unclear whether the authors also applied PCA to the test set in the classification task. If the authors used PCA to preprocess the test set, this would be unreasonable because the test data should be assumed to be unknown beforehand. If the authors did not apply PCA to the test set, maintaining the original data format and attributes while keeping the network unchanged, then theoretically, there should not be a significant acceleration in inference time. 

3. There is an issue with unreasonable descriptions in the related work section. The authors discuss the limitations of Xu et al.'s work titled "Transformer multivariate forecasting: Less is more?" In their second point, they state: "Secondly, it is designed for scenarios where a multivariate series forecasts a univariate series, focusing on reducing the variable dimension of covariate series without preprocessing the target variable series, even if the covariate series may have minimal association with the target series."

4. In the theoretical analysis section, as shown in Figure 3, the authors only demonstrate the effectiveness of PCA in reducing dimensionality along the feature dimension. However, they do not address dimensionality reduction along the time dimension (i.e., the compression of the number of time steps). 

5. It appears that the experimental results presented in Figure 3 are based on a single experiment. The authors did not verify the generalizability of their results by experimenting with different numbers of principal components, k. Without varying k, there's a risk that the chosen value might be a "lucky number" that coincidentally yields favorable results. 

6. The experimental results may be influenced by the characteristics of the specific dataset used. The smoothing effect observed in Figure 3 might only be applicable to the current dataset and may not represent the performance on other time series data. Including experiments on a variety of datasets could improve the credibility of the conclusions. 

7.The authors propose that "Specific trends and periodic patterns in historical series may not be crucial for the learning of TSA models." In the field of Time Series Analysis (TSA), traditional viewpoints and a large body of research emphasize the importance of trends and periodic patterns. These elements are critical for understanding the inherent structure of the data and for predicting future values. 

8. The authors' statement, "Therefore, although PCA may alter the trend or periodicity, it introduces new coherent patterns—such as the main directions of variation, denoised low-dimensional representations, and latent features—that benefit TSA model learning without negatively impacting predictive performance," is overly absolute. Claiming that there are no negative impacts is too definitive. In practical applications, any data transformation can potentially have both positive and negative effects on model performance; the specific outcome depends on the characteristics of the data and the type of model employed.

9.  It seems that the experiments presented in Tables 2, 3, and 4 are based on single runs without any statistical significance testing. There is no indication of whether the results are consistent across multiple trials or if they could be due to random chance. Furthermore, in each experiment, the number of principal components (k) selected for PCA is based on a single value, and this value differs across different datasets.

10.  In Table 2, concerning the Time Series Classification (TSC) experiments, the authors conclude based on the results: "These results reveal PCA’s efficacy in extracting series information for TSC tasks without performance loss, enabling faster training/inference." However, the results presented in Table 2 indicate that applying PCA on certain datasets and networks can lead to significant performance degradation. For example, on the SelfRegulationSCP1 dataset, the accuracy of the TimesNet network decreased by 23.2% after applying PCA. This substantial drop contradicts the authors' absolute assertion of "without performance loss." Out of the 20 metrics reported, only 10 show performance improvement when PCA is applied, which amounts to just 50%. This proportion raises doubts about the claim made in the abstract that applying PCA to sliding sequence windows can maintain model performance.

11.The authors state in Table 3: "The results of Linear are adapted from the study (Zeng et al., 2023)." However, upon reviewing the cited paper by Zeng et al. (2023), I was unable to locate the specific data presented by the authors. This discrepancy raises concerns about the reliability and accuracy of the data used in their experiments.

### Questions
1. The paper does not seem to demonstrate whether the number of time steps is reduced or to what extent. It only generally mentions at the beginning that applying PCA will compress the time series, but it is unclear whether the compression target is the time steps or the data component features within the sliding window. In the Introduction, the authors state that dimensionality reduction techniques for time series data mainly focus on the variable dimension, and they intend to apply PCA for dimensionality reduction along the time dimension. However, from the overall description, the authors appear to only apply PCA to the time-step data within the sliding window to extract local features. This method extracts feature information from each window, but the number of time steps within the window seems to remain unchanged. 

2. It is currently unclear whether the authors also applied PCA to the test set in the classification task. If the authors used PCA to preprocess the test set, this would be unreasonable because the test data should be assumed to be unknown beforehand. If the authors did not apply PCA to the test set, maintaining the original data format and attributes while keeping the network unchanged, then theoretically, there should not be a significant acceleration in inference time. 

3. There is an issue with unreasonable descriptions in the related work section. The authors discuss the limitations of Xu et al.'s work titled "Transformer multivariate forecasting: Less is more?" In their second point, they state: "Secondly, it is designed for scenarios where a multivariate series forecasts a univariate series, focusing on reducing the variable dimension of covariate series without preprocessing the target variable series, even if the covariate series may have minimal association with the target series." 

4. In the theoretical analysis section, as shown in Figure 3, the authors only demonstrate the effectiveness of PCA in reducing dimensionality along the feature dimension. However, they do not address dimensionality reduction along the time dimension (i.e., the compression of the number of time steps). 

5. It appears that the experimental results presented in Figure 3 are based on a single experiment. The authors did not verify the generalizability of their results by experimenting with different numbers of principal components, k. Without varying k, there's a risk that the chosen value might be a "lucky number" that coincidentally yields favorable results. 

6. The experimental results may be influenced by the characteristics of the specific dataset used. The smoothing effect observed in Figure 3 might only be applicable to the current dataset and may not represent the performance on other time series data. Including experiments on a variety of datasets could improve the credibility of the conclusions. 

7.The authors propose that "Specific trends and periodic patterns in historical series may not be crucial for the learning of TSA models." In the field of Time Series Analysis (TSA), traditional viewpoints and a large body of research emphasize the importance of trends and periodic patterns. These elements are critical for understanding the inherent structure of the data and for predicting future values. 

8. The authors' statement, "Therefore, although PCA may alter the trend or periodicity, it introduces new coherent patterns—such as the main directions of variation, denoised low-dimensional representations, and latent features—that benefit TSA model learning without negatively impacting predictive performance," is overly absolute. Claiming that there are no negative impacts is too definitive. In practical applications, any data transformation can potentially have both positive and negative effects on model performance; the specific outcome depends on the characteristics of the data and the type of model employed.

9.  It seems that the experiments presented in Tables 2, 3, and 4 are based on single runs without any statistical significance testing. There is no indication of whether the results are consistent across multiple trials or if they could be due to random chance. Furthermore, in each experiment, the number of principal components (k) selected for PCA is based on a single value, and this value differs across different datasets.

10.  In Table 2, concerning the Time Series Classification (TSC) experiments, the authors conclude based on the results: "These results reveal PCA’s efficacy in extracting series information for TSC tasks without performance loss, enabling faster training/inference." However, the results presented in Table 2 indicate that applying PCA on certain datasets and networks can lead to significant performance degradation. For example, on the SelfRegulationSCP1 dataset, the accuracy of the TimesNet network decreased by 23.2% after applying PCA. This substantial drop contradicts the authors' absolute assertion of "without performance loss." Out of the 20 metrics reported, only 10 show performance improvement when PCA is applied, which amounts to just 50%. This proportion raises doubts about the claim made in the abstract that applying PCA to sliding sequence windows can maintain model performance.

11.The authors state in Table 3: "The results of Linear are adapted from the study (Zeng et al., 2023)." However, upon reviewing the cited paper by Zeng et al. (2023), I was unable to locate the specific data presented by the authors. This discrepancy raises concerns about the reliability and accuracy of the data used in their experiments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper investigates using Principal Component Analysis (PCA) to reduce the temporal dimensionality of time series data in deep learning models for tasks like classification, forecasting, and regression. Traditionally, PCA has been applied to reduce variable dimensions, but this study applies PCA across time windows, aiming to maintain temporal structure while reducing redundancy and computational costs. Results show that PCA preprocessing can accelerate training and inference by up to 40% in some models, like Informer, and reduce memory usage by 30% in models like TimesNet without compromising accuracy. PCA also proves effective in noise reduction, retaining essential statistical characteristics and supporting efficient learning across different deep learning models.

### Strengths
- It clearly introduces the problem of temporal dimensionality reduction in time series data and provides a solid rationale for using PCA.
- The experimental setup is thorough, covering various time series tasks (classification, forecasting, and regression) and a range of model types (Linear, Transformer, CNN, RNN), which effectively illustrates the generalizability of the approach.
- The paper strengthens its argument by presenting concrete metrics, such as GPU memory reduction and speed improvements.

### Weaknesses
 - The intuition behind why PCA is specifically suitable for time series dimensionality reduction is not clearly explained. Many studies have shown that using orthogonal bases (e.g., FFT, wavelets, Legendre polynomials) can improve performance and reduce dimensionality, yet the paper does not address how PCA differs or why these methods were not included in comparisons. Specifically, the paper lacks a discussion on the spectral properties of the time series and how PCA's projection aligns with or differs from frequency-based decompositions. A more detailed analysis of how PCA preserves or discards temporal information, compared to methods that explicitly target frequency components, is needed.
- Adding comparisons with modern compression techniques, beyond linear methods and downsampling, could make the evaluation more robust. For instance, techniques like dictionary learning, or more recent deep learning-based compression methods, could provide a more comprehensive picture of PCA's effectiveness. The current evaluation is limited to linear methods and basic downsampling, which does not fully explore the landscape of dimensionality reduction techniques.
- Some sections, particularly on the theoretical underpinnings of PCA’s use for time series, could benefit from clearer explanations to aid reader comprehension. The paper should delve deeper into the mathematical properties of PCA when applied to time series data, explaining how the principal components capture temporal dependencies. A more rigorous treatment of the assumptions and limitations of applying PCA in this context would be beneficial.
- Each table could benefit from explanations of the metrics used, clarifying what constitutes a “good” or “bad” result (e.g., lower MSE is better), which would help readers interpret the results more easily. Without this context, it is difficult for the reader to fully understand the implications of the reported numerical values. For example, the tables should explicitly state that lower MSE/MAE values indicate better performance for forecasting tasks, and higher accuracy is better for classification tasks.
- More detailed visualizations, such as diagrams showing PCA’s effects on time series structure and feature retention, could enhance clarity. For example, visualizing the time series before and after PCA transformation, along with the corresponding principal components, would provide a more intuitive understanding of the method's impact. This would also help in assessing how PCA affects the temporal patterns and information content of the data.

### Questions
What makes PCA particularly effective here? Is there something unique about the space spanned by its vectors?

How does the dimensionality affect the results? A graph showing MSE versus the number of dimensions (n) would be helpful.

When selecting the first n eigenvalues, do you choose the largest, the smallest, or select them randomly?

### Soundness
3

### Presentation
3

### Contribution
2
