# TVNet: A Novel Time Series Analysis Method Based on Dynamic Convolution and 3D-Variation

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
With the recent development and advancement of Transformer and MLP architectures, significant strides have been made in time series analysis. Conversely, the performance of Convolutional Neural Networks (CNNs) in time series analysis has fallen short of expectations, diminishing their potential for future applications. Our research aims to enhance the representational capacity of Convolutional Neural Networks (CNNs) in time series analysis by introducing novel perspectives and design innovations. To be specific, We introduce a novel time series reshaping technique that considers the inter-patch, intra-patch, and cross-variable dimensions. Consequently, we propose TVNet, a dynamic convolutional network leveraging a 3D perspective to employ time series analysis. TVNet retains the computational efficiency of CNNs and achieves state-of-the-art results in five key time series analysis tasks, offering a superior balance of efficiency and performance over the state-of-the-art Transformer-based and MLP-based models. Additionally, our findings suggest that TVNet exhibits enhanced transferability and robustness. Therefore, it provides a new perspective for applying CNN in advanced time series analysis tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces TVNet, a novel time series analysis method that addresses the limitations of CNNs in capturing complex temporal dynamics by converting 1D time series data into 3D tensors and applying dynamic convolution. This approach achieves state-of-the-art performance across various time series tasks while maintaining efficiency.

### Strengths
1. The paper introduces TVNet, a novel method for time series analysis that leverages dynamic convolution and 3D transformation, offering a fresh perspective in the field by converting 1D time series data into 3D tensors through a 3D-Embedding technique.
2. The paper demonstrates the capacity of the model across five critical time series analysis tasks, including long-term and short-term forecasting, imputation, classification, and anomaly detection, showcasing the model's generalization capabilities.
3. The paper is well-organized, with a logical flow , making it easy to follow and understand.

### Weaknesses
1. Although the paper mentions the efficiency of the model, it does not discuss in detail the consumption of computational resources when running on datasets of different scales. Additionally, different methods have different training strategies, making the training time a poor reflection of the true time consumption of the model. It is recommended to present the inference time and computational load of the model under the same settings. Specifically, the paper should detail memory usage and FLOPs for varying input sequence lengths, which is a critical factor in time series analysis, and compare these metrics against baselines under identical hardware and software configurations. This would provide a more comprehensive view of the model's practical efficiency.
2. The experimental results show long-term forecasting, but it seems that the prediction lengths = {24, 36, 48, 60} do not reflect the setting of 'long-term.' It is suggested to follow the same settings as the original dataset, such as: {96, 192, 336, 720}. The use of shorter prediction lengths, especially for datasets where longer horizons are standard, makes it difficult to assess the model's true long-term forecasting capabilities. This discrepancy raises concerns about the generalizability of the reported results.
3. In Table 1, it is a very serious error that the values for weather and traffic are identical.
4. The article's claim of "achieves top-tier performance across five pivotal analytical tasks" is overclaimed because the results on long sequences show that the method did not achieve state-of-the-art (SOTA) on multiple datasets, and the improvement in results that did achieve SOTA is very limited (approximately 0.85% to 2.36% on MSE). The paper needs to more accurately reflect the model's performance relative to existing state-of-the-art methods, especially in scenarios where the improvements are marginal.
5. Although the paper proposes a powerful model, more explanation may be needed to justify its complexity, especially in the experimental analysis, where more demonstration of its performance in terms of inter-patch, intra-patch, and cross-variable interpretability is needed. The paper should include visualizations or quantitative analysis to show how the model captures these dependencies, such as attention maps or feature importance scores, to provide a deeper understanding of the model's internal mechanisms.

### Questions
1. It is recommended to present the inference time and computational load of the model under the same settings.
2. To effectively demonstrate the capability of long-term forecasting, it is recommended to follow the same settings as the original dataset, for instance: {96, 192, 336, 720}.
3. More explanation may be needed to justify its complexity, especially in the experimental analysis, where more demonstration of its performance in terms of inter-patch, intra-patch, and cross-variable interpretability is needed.

### Soundness
3

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
The manuscript introduces TVNet, a dynamic convolutional network for time series analysis, employing 3D embedding and convolution mechanisms to handle inter-patch, intra-patch, and cross-variable dependencies. TVNet aims to improve CNN performance in time series tasks and demonstrates its utility across multiple tasks, including long-term and short-term forecasting, classification, anomaly detection, and data imputation.

### Strengths
- The modular design of TVNet is scalable and easily extensible
- Maintains computational efficiency comparable to CNNs while achieving superior results.
- Comprehensive experiments covering many tasks, baselines and analysis

### Weaknesses
 - **Lack of Strong Motivation**: The paper's motivation could be strengthened. While it aims to “enhance the representational capacity of CNNs for time series analysis,” it does not adequately explain **why** this enhancement is necessary, given the strong performance of RNNs and Transformers for such tasks. It is well understood that different network architectures are suited for different input modalities, based on the inductive biases they introduce [1]. Therefore, further justification is needed to clarify the specific gaps that CNNs can fill in time series analysis. Specifically, the paper needs to articulate scenarios where the inherent limitations of RNNs, such as vanishing gradients in long sequences or the computational overhead of attention mechanisms in Transformers, make CNNs a more suitable choice. The motivation should clearly define the niche that CNNs, particularly with the proposed enhancements, can effectively address in time series analysis, rather than simply stating an intention to improve CNN performance.
- **Insufficient Emphasis on Novelty**: Although the introduction of **3D-embedding** is a core idea, the rationale for choosing the specific three embeddings (inter-patch, intra-patch, and cross-variable) is not adequately explained. A deeper discussion is necessary to understand why these dimensions were prioritized and how they contribute to improved performance. This would help highlight the **novelty** and distinctiveness of the proposed method. The paper should provide a more detailed explanation of how these specific embeddings capture the temporal dependencies and multivariate relationships in time series data. For instance, it would be beneficial to discuss how inter-patch embeddings capture periodicity, how intra-patch embeddings capture local stationarity, and how cross-variable embeddings capture the interdependencies between different time series. Without this, the choice of these three embeddings appears arbitrary and lacks a strong theoretical or empirical foundation.

### Questions
- **Motivation**:
    - Can the authors elaborate on the specific limitations of RNNs and Transformers in time series analysis that CNNs aim to address? Given the well-known success of Transformers and RNNs, what makes CNNs uniquely suitable for time series tasks?
- **Rationale Behind 3D-Embedding**:
    - Why were the inter-patch, intra-patch, and cross-variable embeddings selected? Are there theoretical or empirical justifications for these choices? Could alternative embeddings have been explored, and how would the performance be affected by such variations?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents TVNet, a dynamic convolutional network for time series analysis, utilizing a 3D-Embedding technique and dynamic convolution to capture intra-patch, inter-patch, and cross-variable dependencies. TVNet is evaluated on five tasks and shows state-of-the-art performance, better efficiency than some models, and good transferability and robustness.

### Strengths
1. The proposed 3D-Embedding technique and the consideration of different types of dependencies (intra-patch, inter-patch, cross-variable) are novel and well-motivated.
2. The experimental evaluation is comprehensive, covering multiple tasks and comparing with a wide range of state-of-the-art models. The consistent top performance across these tasks is a significant strength.

### Weaknesses
1. Some parts of the method description could be made clearer. For example, the generation function for the time-varying weight could be explained in more detail. Specifically, the mechanism by which the dynamic convolution kernels are generated and how they adapt to different time steps is not sufficiently elaborated. The relationship between the input features and the generated weights, as well as the specific mathematical operations involved, require more clarity. Furthermore, the role of the 3D-Embedding in facilitating this dynamic weight generation could be better explained.
2. The paper does not compare with some of the latest models such as TimeMixer[1] and recent models combined with large language models (e.g., S2 IP-LLM[2], TimeLLM[3]). This omission may lead to an incomplete understanding of the relative performance and novelty of TVNet in the context of the most recent research trends. The lack of comparison with these models, especially those leveraging large language models, makes it difficult to assess the true state-of-the-art standing of the proposed approach. The absence of these comparisons is particularly concerning given the rapid advancements in time series analysis using transformer-based architectures and LLMs.

### Questions
1. Can the authors provide more details about the choice of hyperparameters and their impact on performance? 
2. Why was there no comparison with some of the latest models such as TimeMixer and models combined with large language models (e.g., S2 IP-LLM, TimeLLM)? What could be the potential implications of such comparisons for the evaluation of TVNet?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper propose a method called TVNet. TVNet can capture intra-patch,inter-patch and cross-variables features by converting 1D time series data into 3D shape tensor.

### Strengths
To sum up, this is a good paper. They proposed TVNet.
TVNet captures intra-patch,inter-patch and cross-variables features by converting 1D time series data into 3D shape tensor.
TVNet implements consistent state-of-the-art performance time series analysis tasks across multiple mainstreams, demonstrating excellent task generalization.

### Weaknesses
1. 3D-EMBEDDING
This is your innovation, but you did not tell it  clearly. For example: 
"stride S to divide into N patches($X_{emb} ∈ R^{N×P ×C_m}$)" 
It is hard for me to know how do you achieve this. Almost the whole process in this part is confused. You should give explanations.


### Questions
The same to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
