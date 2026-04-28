# Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Deep learning for time series forecasting has seen significant advancements over the past decades. However, despite the success of large-scale pre-training in language and vision domains, pre-trained time series models remain limited in scale and operate at a high cost, hindering the development of larger capable forecasting models in real-world applications. In response, we introduce \method, a scalable and unified architecture designed to pre-train larger, more capable forecasting foundation models while reducing inference costs. By leveraging a sparse mixture-of-experts (MoE) design, \method enhances computational efficiency by activating only a subset of networks for each prediction, reducing computational load while maintaining high model capacity. This allows \method to scale effectively without a corresponding increase in inference costs. \method comprises a family of decoder-only transformer models that operate in an auto-regressive manner and support flexible forecasting horizons with varying input context lengths. We pre-trained these models on our newly introduced large-scale data \dataset, which spans over 9 domains and encompassing over 300 billion time points. For the first time, we scaled a time series foundation model up to 2.4 billion parameters, achieving significantly improved forecasting precision. Our results validate the applicability of scaling laws for training tokens and model size in the context of time series forecasting. Compared to dense models with the same number of activated parameters or equivalent computation budgets, our models consistently outperform them by large margin. These advancements position \method as a state-of-the-art solution for tackling real-world time series forecasting challenges with superior capability, efficiency, and flexibility.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new architecture designed to improve time series forecasting by utilizing large-scale foundation models! It addresses key challenges in time series data, like complexity and distribution shifts, which require strong forecasting solutions across fields such as finance, energy, and climate. TIME-MOE adopts a sparse mixture-of-experts (MoE) approach, activating only a subset of parameters during inference! This reduces computational demands while preserving performance! A notable focus is on scaling laws, which have seen success in language and vision research! By applying these principles to time series forecasting, the authors show that expanding model size and training data leads to substantial improvements, positioning TIME-MOE as a leading model that surpasses traditional dense architectures. The flexible design of TIME-MOE supports variable forecasting horizons and input context lengths, making it suitable for diverse applications! The paper also includes a thorough reproducibility statement detailing the architecture, implementation, and data processing steps, highlighting the authors' dedication to transparency and collaborative research! This work not only advances time series forecasting but also paves the way for future studies on scalable, efficient forecasting architectures!

### Strengths
The originality of this work shines through its novel approach to applying MoE architecture in time series forecasting! By adopting a sparse framework, the authors not only boost computational efficiency but also extend the potential of large-scale models in this field! This unique integration of MoE principles, previously effective in fields like NLP and Computer Vision (CV), offers a new perspective, tailored to tackle the distinctive challenges of time series data! 

The work stands out for its rigorous methodology, which supports a reliable, in-depth analysis of the TIME-MOE architecture! The authors carefully describe each component, training process, and evaluation metric! This level of detail strengthens the study's findings, ensuring they are both robust and reproducible, an essential foundation for advancing knowledge and encouraging future work in the field!  

The paper stands out for its clarity, presenting complex ideas in a way that's easy to follow! The authors organize their work with well-defined sections, clear plots, and tables that effectively highlight the model's performance metrics! This structure makes it easier to understand the proposed architecture and broadens the paper's appeal, helping both experts and newcomers engage with the context! The study is particularly important because it tackles a crucial gap in time series forecasting research! By scaling a foundation model up to 2.4 billion parameters and showing significant accuracy gains, the authors demonstrate that larger models can boost performance without overwhelming computational demands! This insight is valuable for practical applications, indicating that organizations can adopt high-performance forecasting models without excessive resource costs! 

The paper's contributions go beyond theoretical insights, opening doors to practical applications across fields like finance, energy, and climate science! TIME-MOE's capability for universal forecasting and flexibility across different time horizons make it a valuable tool for improving decision-making in various industries! This potential for tangible impact highlights the paper's importance and its value to both researchers and industry professionals!

### Weaknesses
(1) The originality of the model is somewhat limited by the lack of a detailed comparison with other SOTA models beyond the chosen benchmarks. While the authors report promising improvements, the analysis would benefit from a broader comparative study that includes contemporary forecasting models, such as [1] and [2]. Specifically, it would be helpful to compare aspects like model architecture, data handling techniques, and feature processing methods in these SOTA models to highlight where TIME-MOE uniquely contributes. For instance, a detailed comparison of the attention mechanisms used in Temporal Fusion Transformers (TFT) versus the MoE routing in TIME-MOE would be beneficial. Additionally, incorporating ablation tests that isolate the impact of each component in the TIME-MOE architecture, such as the specific gating mechanism or the expert network size, could clarify which elements drive its performance gains. This would strengthen the claims of superiority over existing models and enhance the overall rigour of the evaluation!

(2) The paper highlights the benefits of sparsity and computational efficiency in the MoE architecture but overlooks certain limitations, notably the risk of underfitting when only a limited number of experts are activated. This issue is particularly relevant in time series forecasting, where the variability across datasets demands a careful approach to expert selection. I suggest that the authors provide an analysis examining how the number of activated experts impacts model performance across diverse time series datasets. For example, an analysis showing the performance variation when activating 2, 4, or 8 experts would be insightful. This would directly address the concern of potential underfitting and add valuable insights. Additionally, referencing studies like [3] that discuss specific challenges in MoE models, such as load balancing issues and the potential for expert specialization collapse, would strengthen the discussion!

(3) The experimental evaluation is limited by the narrow selection of datasets, primarily focusing on a restricted set of benchmarks. This approach may not capture the model's performance across diverse time series characteristics. To strengthen the study, I recommend that the authors consider expanding their dataset choices to include more varied features, such as seasonality, trend, and noise levels. Adding datasets like M4, those from the UCI time series repository, the Monash dataset [4], and LOTSA as used in [5] could offer a broader perspective on the model’s adaptability and robustness. Furthermore, a detailed analysis of how the model performs on datasets with varying degrees of seasonality or trend would be valuable. Additionally, I encourage the authors to clarify their rationale for selecting the current benchmarks. Specifically, explaining how these datasets reflect a range of time series characteristics would help assess whether the chosen datasets sufficiently represent the intended applications or whether a more comprehensive selection is warranted. This would either justify their current dataset choice or highlight areas where further dataset diversity could enhance the model’s generalizability!

(4) The interpretability of the TIME-MOE model could be significantly strengthened by providing more detailed insights into expert activations for various types of time series inputs. Given the complexity of MoE architectures, it would be valuable for the authors to visualize which experts are activated for specific predictions across diverse input scenarios. For instance, heatmaps showing expert activation patterns for different time series characteristics, such as high-frequency vs. low-frequency data, would be beneficial. Additionally, an ablation study illustrating how different experts contribute to predictions for various data types would offer a clearer understanding of each expert’s role. These additions would not only improve transparency but also increase the model's reliability and applicability in real-world settings!

(5) The paper mentions the efficiency of the TIME-MOE model but lacks specific, detailed analysis on computational costs, which would be essential for understanding its practical impact. I would recommend that the authors provide concrete metrics, such as training time per epoch, GPU memory usage, and inference time across different model sizes. Furthermore, providing a breakdown of the computational cost associated with the MoE layer versus the rest of the network would be useful. Additionally, a direct comparison of these metrics with baseline models, such as TFT and N-BEATS, would add valuable context for practitioners, especially those working in resource-constrained environments, who need a clear understanding of the computational demands before implementing the model!

(6) The authors could strengthen their exploration of real-world implications by including a practical case study or detailed scenario demonstrating how TIME-MOE could be applied in a specific industry, such as energy forecasting or financial market prediction. Highlighting potential benefits and challenges within a concrete example, such as predicting energy consumption patterns or stock market trends, would provide a clearer picture of how TIME-MOE fits into current forecasting practices, making the research more relatable and actionable. This approach would help bridge the gap between the theoretical aspects of their work and its practical implementation, enhancing the paper’s overall impact!

### Questions
Please check the Weaknesses part!

### Soundness
3

### Presentation
3

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
The article titled "TIME-MOE: Billion-Scale Time Series Foundation Models with Mixture of Experts" introduces a scalable, efficient time series forecasting model known as TIME-MOE, designed to handle large datasets with diverse domains and flexible forecasting requirements.

### Strengths
1. Scalability and Efficiency: By using sparse MoE, TIME-MOE achieves improved performance and efficiency, especially for larger models. It reduces the computational cost significantly compared to dense models of similar scale, enabling inference on hardware with lower memory requirements.
2. Multi-Resolution Forecasting: The multi-resolution forecasting component allows the model to handle various forecasting horizons efficiently. This flexibility is critical in real-world applications where forecasting requirements vary widely.
3. Empirical Validation Across Benchmarks: The model shows substantial improvements over state-of-the-art dense models in both zero-shot and fine-tuned settings across multiple time series datasets, providing robust evidence of its performance.

### Weaknesses
1. Complexity in Routing and Expert Selection: The process by which TIME-MOE assigns tokens to experts in the MoE layer lacks detailed explanation, particularly regarding the criteria for expert selection and load balancing across experts. Specifically, it would be helpful to include the mathematical formulation of the gating mechanism used to select the top-k experts, along with any thresholds or conditions applied during this process. Furthermore, could the authors clarify the techniques employed to prevent expert collapse, such as auxiliary loss functions or dynamic routing strategies? Including these details would provide a clearer understanding of how TIME-MOE maintains balanced and effective specialization among experts.
2. Dependence on Data Quality in Time-300B: The data-cleaning pipeline for Time-300B is briefly mentioned, but additional details on the metrics used to assess data quality before and after cleaning would provide valuable insights. Could the authors specify which metrics (e.g., missing data rate, outlier detection thresholds, signal-to-noise ratio) were used to evaluate the dataset’s quality at each stage? Additionally, it would be beneficial to understand if different domains in Time-300B required unique preprocessing strategies, given that they may have distinct characteristics (e.g., varying degrees of stationarity, seasonality, or noise levels). For instance, were there specific thresholds or criteria applied differently for stationary versus non-stationary time series, or domain-specific noise reduction techniques? Clarifying these details would help illustrate how the pipeline handles domain-specific data imbalances and noisy observations, which is crucial for the model’s generalizability across diverse applications.
3. Positional Encoding and Temporal Coherence: The paper’s use of rotary positional embeddings is interesting, but it would be beneficial to see a comparative analysis of rotary embeddings against other positional encoding methods (e.g., sinusoidal or learned embeddings) specifically for long-term forecasting. Could the authors provide performance metrics—such as error metrics over extended forecast horizons, robustness to long-range dependencies, and computational efficiency—across these encoding types? Additionally, were there specific challenges or performance trends observed when using rotary embeddings over extended timeframes? For example, did rotary embeddings show advantages or disadvantages in terms of capturing the temporal continuity needed in long-term forecasting, compared to sinusoidal or learned encodings? Providing these comparisons and insights would clarify why rotary embeddings were chosen and how they impact forecast accuracy and computational costs over long sequences.

### Questions
1. Expert Routing in MoE Layers: Could you provide more details on the gating mechanism and expert selection criteria? Specifically, how does the model ensure a balanced load across experts, and what mechanisms are in place to prevent routing collapse?
2. Handling Domain Imbalances in Time-300B: Given the wide range of domains in Time-300B, how does TIME-MOE adapt to data imbalances? Are there any mechanisms to ensure that underrepresented domains do not disproportionately impact model performance?
3. Choice of Rotary Positional Embeddings: Could the authors explain the choice of rotary embeddings over other positional encodings? Additionally, have the authors conducted ablation studies to assess the impact of this encoding on forecasting accuracy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Time-MoE, a scalable foundation model for time series forecasting that leverages a sparse mixture-of-experts (MoE) architecture. This approach enhances computational efficiency by selectively activating a subset of expert networks for each prediction. The model was pre-trained on a newly proposed large-scale dataset, Time-300B, comprising over 300 billion time points/tokens from nine different domains. Time-MoE's decoder-only structure supports flexible forecasting horizons, and it scales up to 2.4 billion parameters without significant increases in inference costs. The paper demonstrates substantial improvements in forecasting accuracy, positioning Time-Moe as a state-of-the-art solution for time series forecasting.

### Strengths
**Originality**: Introducing a sparse Mixture-of-Experts model for time series forecasting is, as far as I know, novel. This work provides the first large-scale configuration of sparse architectures for time series models, addressing efficiency issues as well as overfitting seen in dense approaches.

**Quality**: The manuscript includes multiple experiments, with good evaluation across zero-shot and fine-tuning settings on multiple (but limited domains) benchmarks (compared to multiple llms and pre-llm models), showcasing the generalizability and effectiveness of the approach. I really like that the authors conducted an scalability analysis with their model as well as the dense counterpart, which can also be seen as a contribution due to its sheer parameter size.

**Clarity**: The paper is clearly written and easy to follow, making it accessible to a broad audience. The use of detailed and easy-to-follow figures (e.g., Figure 2) supports understanding of complex architectural components.

**Significance**: Scaling time series forecasting models has traditionally been challenging due to high computational costs and the lack of proper training data. This work shows significant performance improvements over existing dense models as well as prior LLM-based approaches. Furthermore, due to similarities in its components, it represents a good step towards broadening time series research across research communities (i.e., NLP research).

### Weaknesses
While I liked the paper there are some areas which can be improved

### Areas for Improvement 
**W1**: The usage of rotary positional encoding is mentioned but not clearly represented in Figure 2. This leads to some confusion (i.e. at a first glance i thought the authors constructe a set transformer); it would be helpful to clarify this, possibly adding an explicit label to ensure better understanding.

**W2**: The recent work by Liu et al. (2024), which proposes a new one-for-all benchmark, is missing. Given its relevance, including this benchmark would provide a more comprehensive assessment of the model’s generalizability. In general, discussing differences in the related work would be a good idea.

**W3**: In my opinion, it is not necessary to prove again that flash attention is fast and BF16 is reasonable to use (the trade-off). These evaluations could be moved to the appendix for interested readers. Instead, I think it would be a good idea to see model performances over the course of the training with different data sampling strategies.

**W4**: There is limited ablation on certain design choices, specifically around the multi-resolution head and expert allocation/configuration strategies. This could strengthen the papers claims (see more in the questions 1,2,4,5)

**W5**: The lack of standard deviations weakens the paper's results and claims

**W6**: The forecastability table needs to proper reference its origin (Wang et al., 2024)

**W7**: I think it is not enough to evaluate on two domains i.e. Temperature and Weather which are already kind of related.

### Limitations
- I did not find any addressed limitations regarding their proposed dataset collection and what impact it would have to have datasets with Spurious correlations  in the collection such as P2S (Kraus et al.,)
- Currently, the decision on which datasets were excluded from the Time-300B collection appears somewhat arbitrary, without strong justification provided for the selection criteria.

Liu et al., AutoTimes: Autoregressive Time Series Forecasters via Large Language Models (NeurIPS 2024)

Wang et al., TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting (ICLR 2024)

Kraus et al., Right on Time: Revising Time Series Models by Constraining their Explanations (2024)

### Questions
1. While point-wise tokenization is reasonable, neighboring time steps often encode similar information. Did you consider tokenizing multiple time steps as a unit? This might improve context efficiency and extend the effective sequence length.

2. Following from the above, would a hybrid tokenization (mixing single time step and multiple time step tokens) be feasible? Effectively increasing the vocabulary? As far as I see the vocab size is of size 10?

3. Could you present MAE results, particularly for ablations? Seeing those values would help evaluate the robustness of different configurations.

4. Regarding the ablation on loss functions: while L2 loss was tested, other simple losses (like L1) could have been competitive. Did you consider these alternatives before settling on Huber loss?

5. The inference speed results in Table 5 indicate that removing resolution layers increases speed. Could you clarify why retaining multi-resolution layers results in faster inference? This seems counterintuitive.

6. There appears to be some variability in performance between different model sizes (e.g., Time-MoE_large performing worse in some 100B cases than dense models). Do the authors have an intuition for why this happens?

### Soundness
3

### Presentation
4

### Contribution
3
