# KambaAD: Enhancing State Space Models with Kolmogorov–Arnold for time series Anomaly Detection

- Decision: Reject
- Scores: 5, 6, 3, 6, 6

## Abstract
Time series anomaly detection is critical in numerous practical applications, yet existing deep learning methods often fall short of real-world demands. These models fail to swiftly filter out physically implausible anomalies, insufficiently address distributional shifts, and lack a comprehensive approach that integrates both global and local perspectives for anomaly detection. Moreover, most successful models rely on channel-dependent methods that tend to treat all features at the same timestamp as a single token and then focus on finding relationships between these tokens. This approach overlooks the unique periodicities, trends, and lagged relationships between different features, leading to suboptimal performance. To address these limitations, we propose KambaAD, a model comprised of an Encoder and Reconstructor. The Encoder integrates the strengths of the Kolmogorov-Arnold Network (KAN), the attention mechanism, and the Selective Structured State Space Model (MAMBA). Specifically, KAN is employed to swiftly enforce data consistency, enabling rapid detection of anomalies that violate physical laws. The attention mechanism ensures balanced processing of global information while enhancing the representation of key data characteristics. We leverage MAMBA's capability as a sequence model to capture anomalies caused by local variations. Additionally, its internal selection mechanism allows the model to effectively handle distribution shifts, ensuring robustness and adaptability in the presence of changing data distributions. Additionally, the framework incorporates a time-series-specific Reconstructor, which reduces computational complexity through patch-based operations that exploit local consistency in time series data. It also employs channel-independent linear reconstruction to prevent interference between different features. Through extensive experiments on multiple multivariate datasets, KambaAD consistently outperforms state-of-the-art models, demonstrating its superior performance in anomaly detection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author proposed KambaAD, which uses KAN for fast and effective preliminary anomaly screening, and then combines attention and MAMBA for anomaly detection to detect global patterns and local changes simultaneously.

### Strengths
The author proposed KambaAD, which uses KAN for fast and effective preliminary anomaly screening, and then combines attention and MAMBA for anomaly detection to detect global patterns and local changes simultaneously. The author uses KAN for fast and effective preliminary anomaly screening to capture global patterns and long-term dependencies. MAMBA is used to focus on capturing subtle local changes and distribution changes. The experimental results of the article are good.

### Weaknesses
In the abstract, the author emphasized that the existing methods are all channel-related, which leads to the neglect of the unique periodicity, trend and lag relationship between different features. However, there are many methods that consider channel independence and even combine channel independence with channel correlation to capture the relationship between features. And the author explained in the Introduction that the current method does not integrate local and global perspectives. However, as far as I know, there are many methods that process local and global information at the same time, such as TranAD, Dcdetector, etc. And there are many methods that have studied the problem of model robustness in non-stationary data, such as Dynamic Decomposition with Diffusion Reconstruction, etc. The author does not explain the unique innovation of his own method enough, and it seems that he has not solved the problems unique to time series data.

The author needs to further sort out the logic of the article. For example, in the description of the current research status in the Introduction, a description of cloud devices suddenly appeared, which is not sufficiently relevant to the general anomaly detection algorithm. Cloud device anomaly detection is only a small sub-item, and the author did not further explore it. I did not understand the significance of the description of cloud devices.

The author proposed the Kolmogorov-Arnold Network for preliminary screening, but the significance and role of the preliminary screening in the article were not clearly introduced. My understanding is that KAN is used to perform preliminary anomaly detection on the whole, but after the results are detected, what operations need to be performed and what is the role of this step. I think it needs to be further explained in the article.

### Questions
I want to know what is the purpose of the KAN proposed by the author, and what operations are performed after the preliminary screening results? And I think the author needs to further elaborate on the innovation of the method proposed in the article.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a method called KambaAD for time series anomaly detection.

### Strengths
1. The paper is well organized. 

2. The architecture of KambaAD is clearly presented. 

3. The proposed KambaAD is validated via extensive experiments.

### Weaknesses
1. Related work is missing, such as the paper entitled "Joint Selective State Space Model and Detrending for Robust Time Series Anomaly Detection".
2. Lack of guidance on how to choose hyperparameters in KambaAD.
3. Table 1 has errors, such as the results of ImDiffusion detector on MSL dataset.
4. Lack of comparison with recently published detectors, such as those from the following papers.

Donghao Luo and Xue Wang. Moderntcn: A modern pure convolution structure for general time series analysis. In The Twelfth International Conference on Learning Representations, 2024.

Youngeun Nam, Susik Yoon, Yooju Shin, Minyoung Bae, Hwanjun Song, Jae-Gil Lee, and Byung Suk Lee. Breaking the time-frequency granularity discrepancy in time-series anomaly detection. In Proceedings of the ACM on Web Conference 2024, pp. 4204–4215, 2024.

### Questions
please see above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces KambaAD, a model designed to improve anomaly detection in time series by integrating the Kolmogorov - Arnold Network (KAN) with attention mechanisms and the Selective Structured State Space Model (MAMBA). Specifically, the model incorporates different components (KAN, attention mechanisms, and MAMBA) into an encoder - decoder framework to detect anomalies. The paper conducts experiments on multivariate time series datasets, demonstrating a 5% improvement in F1 score over existing baselines.

### Strengths
- The paper considers both global and local anomalies, with the attention mechanism captures long range dependencies, while MAMBA focuses on local temporal dynamics. 
- The integration of KAN into encoder-decoder structure is relatively novel, but has limitations.
- The model performance improves over existing baselines.

### Weaknesses
The paper has some fundamental limitations:

- Although the integration of KAN, attention mechanism and MAMBA are relatively novel, all those individual components are established techniques. The paper could benefit from a deeper exploration and justification on how this specific combination uniquely addresses challenges in anomaly detection. Without this theoretical-based exploration to provide a thorough understanding, the paper is seemingly a typical applied paper that tries to combine existing components to handle an existing task, which does not have not enough novelties and contributions for a conference like ICLR. Specifically, the paper lacks a clear explanation of why KAN is preferred over other potential network architectures for capturing physical constraints, and what specific problems it addresses that other methods cannot. The justification for using attention mechanisms and MAMBA is also weak, without a detailed explanation of how they address the specific challenges of long-range dependencies and distribution shifts in time series anomaly detection, respectively. The paper needs to provide a more rigorous analysis of the theoretical underpinnings of this specific combination.

- The paper needs a more thorough comparison with state of the art models, such as TranAD [1], GDN [2], TadGAN [3], MTAD-GAT [4], to assert the advantages and potential limitations of proposed model, and make clearer its position in comparison with the current SoA methods. The current comparison lacks a detailed analysis of the performance differences, and does not sufficiently justify why the proposed model is superior to these existing methods. The paper should also include a more diverse set of baselines, including models that use different approaches, such as GAN-based methods like TadGAN, to provide a more comprehensive comparison.

- The paper lacks a detailed analysis of scalability where it examines high-dimensional datasets. The current experiments are limited to relatively small datasets, and there is no analysis of how the model performs on larger, more complex datasets. This is a critical limitation, as real-world time series data is often high-dimensional and large-scale, and the model's performance on these datasets is crucial for its practical applicability. The paper should include experiments on larger datasets to demonstrate the scalability of the proposed model.

- While KambaAD achieves strong results, the paper does not thoroughly analyze the sensitivity of key parameters (e.g., window size, patch size, and model layers) on model performance. Without understanding how sensitive KambaAD is to parameter choices, its robustness and adaptability to diverse datasets or unseen conditions remain unclear. A detailed sensitivity analysis would help practitioners better configure the model for specific applications. The paper should include a more detailed analysis of how the model's performance varies with different parameter settings, and provide guidance on how to choose appropriate parameter values for different datasets.

- KambaAD lacks the discussion of interpretability and explainability, especially, which component is responsible for detecting specific types of anomalies. The paper would benefit from visualizing or explaining the anomaly detection process by showing the relative contributions of KAN, attention, and MAMBA components in making the prediction. The paper should include a more detailed analysis of the model's decision-making process, and provide insights into how each component contributes to the final prediction.

### Questions
- Could the authors elaborate on the unique advantages of combining KAN, attention, and MAMBA specifically for time series anomaly detection? What specific problems does each component address, and why is this integration particularly effective?

- How does KambaAD perform in terms of computational efficiency and scalability, especially for high-dimensional or large-scale time series data? 

- How does KambaAD handle noisy, sparse, or incomplete data? 

- How sensitive is KambaAD to hyperparameter tuning? Are there recommended settings for its main components, and how would performance vary with suboptimal hyperparameters?

- Given the complexity of the model, how can users interpret KambaADs detection results? Is there a way to identify which component contributes most to identifying an anomaly? Could the authors provide an ablation study to evaluate the impact of each component independently?

- How does KambaAD compare with more recent listed models above? Could the authors include these models in their evaluation?

- How does the performance of KambaAD vary with different sequence lengths or time window sizes? How to choose these parameters?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper integrates KAN, Transformer, and MAMBA to encode the input series. In the reconstruction step, the paper uses patch-based data division, channel-independent (CI) processing and linear layers. Integrating KAN, attention mechanism, and MAMBA in KambaAD enables effective global anomaly filtering and local variation recognition across temporal scales. The paper provides a detailed explanation of the model framework and provides performance comparison experiments and ablation experiments.

### Strengths
1.	The paper applies advanced deep learning methods to time series anomaly detection.
2.	It explains the entire inference process of the model clearly.
3.	The model demonstrates advanced algorithms could improve the performance in anomaly detection tasks due to their feature capture ability.
4.	Rich experiments have been conducted.

### Weaknesses
1.	On why the algorithm can succeed, the author only describes the roles of each part in the Introduction. The author has not further explained how each part plays a role in anomaly detection nor provided more reasons to demonstrate how this model outperforms others.
2.	The advantage of the hyperparameter patch_len is not precise.
3.	There are English writing issues.
4.	There is a concern about using point adjustment (PA) for experimental evaluation, which can lead to faulty performance evaluations. As stated in [3], incorporating PA, the Random model outperforms all state-of-the-art models. Did this paper use the PA technique for the experimental evaluation?

### Questions
1.	The model integrates 3 deep learning algorithms and the experiments used 4 A800 GPUs. How much average running time it takes under that hardware configuration? If running on that hardware configuration requires a lot of time, then the cost of this model will be too high.
2.	In Table 1, the performance of KambaAD is compared with 23 baseline models. However, some baseline models’ results are quoted directly from papers (for instance, LSTM-VAE and BeatGAN in Table 1, Dcdetector in Table 2). It would be better to clarify which ones were cited.
3.	In Figure 2, patch_len is set to {1 2 4 8 16 32} in parameter sensitivity studies. Meanwhile in Table 8 patch_len is set to 96. Should the values of the former be taken around 96? Besides if patch_len = window_size, can the patch partition step be abandoned? In Figure 2, one can see that the performance does not change much as patch_len varies. 
4.	The original name is Affiliation Metrics (Huet et al., 2022) rather than Affiliation Score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces KambaAD, a model for time series anomaly detection that incorporates an Encoder network with (1) a Kolmogorov-Arnold Network (KAN), (2) a Selective Structured State Space Model (MAMBA), and (3) an Attention mechanism. The hybrid encoder employs a two-stage feature extraction process: After the sequence is processed by KAN, it is sent to the subsequent Attention and Mamba modules for further feature extraction. There is also a simple Reconstructor network for linear reconstruction from extracted features using channel independence and patch partition. Experimental results demonstrate the benefits of the proposed solution against several baselines on multiple datasets.

### Strengths
- The main ideas are clearly presented, and the writing is easy to follow.  
- The model performance is very promising on multiple multivariate datasets.   
- This paper also provides a series of ablation experiments to test the effect of each design.

### Weaknesses
 - The proposal is a fusion of existing ideas, for example, KAN, MAMBA, and attention. Taking channels independently and breaking them into patches are also well-known techniques in the time series domain [1]. While it looks like the integration is executed somehow effectively, the paper itself offers limited innovation.

[1] Nie, Yuqi, et al. "A time series is worth 64 words: Long-term forecasting with transformers."

- The discussion of the experimental results is inadequate, and the ablation experiments are not sufficient to highlight the necessity of the model design.

### Questions
(1) It is necessary to elaborate more on the interpretation of the tables and plots. For example, in Table 2 KambaAD performs less well in GECCO dataset under Aff-R. What is the reason behind this phenomenon? What does this indicate? In Table 4, why does the Reconstructor perform better than the integration with GECCO, and why does Encoder perform better with Mulvar? 

(2) Section 4.3.5 compares the performance of CI and CD methods. How does the CD method work? It is better to analyze the reason why the CD negatively impacts the overall results.

(3) The experiments mainly compare the accuracy of KambaAD with the baselines. However, the authors did not provide any result on the running speed of KambaAD. Could the authors include a runtime analysis or comparison to evaluate the efficiency of KambaAD？

(4) From Section 1: “Meanwhile, MAMBA focuses on detecting local, context-specific anomalies.” The statement claims that Mamba is mainly used for local anomaly detection, but the experiments did not demonstrate this. In fact, research [2] shows that Mamba is more suitable for long sequence modeling. I would like to know how the authors view this problem. If Mamba and attention have overlapping effects, then considering Mamba's lower complexity, why not just use two Mamba modules instead? It would be more convincing if the author could include an ablation study to demonstrate the superiority of the Mamba-attention design.

[2] Yu, Weihao, and Xinchao Wang. "MambaOut: Do We Really Need Mamba for Vision?."

(5) Similarly, the KAN in MambaAD is designed to capture evident physical anomalies. However, from Eqn. (3) in Section 3.2.1, it is difficult to find out how X_{KAN} can capture such anomalies in the data. The experiments did not demonstrate this as well. Could the author include an example or visualization demonstrating how X_{KAN} captures the anomalies? I also suggest an ablation study comparing the performance with and without KAN to show its effect in MambaAD.

(6) As shown in Table 4, the performance of a single reconstructor is quite good, while its total parameters should be much lower than that of the encoder or/and KambaAD. Can the authors provide additional comparisons under the same model size?

### Soundness
2

### Presentation
3

### Contribution
3
