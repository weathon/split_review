# Time Series Representation Models for Multivariate Time Series Forecasting and Imputation

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
We introduce a multilayered representation learning architecture called Time Series Representation Model (TSRM) for multivariate time series forecasting and imputation. The architecture is structured around hierarchically ordered encoding layers, each dedicated to an independent representation learning task. Each encoding layer contains a representation layer designed to capture diverse temporal patterns and an aggregation layer responsible for combining the learned representations. The architecture is fundamentally based on a Transformer encoder-like configuration, with self-attention mechanisms at its core. The TSRM architecture outperforms state-of-the-art approaches on most of the seven established benchmark datasets considered in our empirical evaluation for both forecasting and imputation tasks while significantly reducing complexity in the form of learnable parameters. The source code is available at https://anonymous.4open.science/r/TSRM-D7BE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel architecture called Time Series Representation Model (TSRM) for multivariate time series forecasting and imputation. The TSRM architecture is based on a Transformer encoder-like configuration with hierarchically ordered encoding layers.  The TSRM architecture integrates representation learning within a multilayered model, where each layer features a distinct representation learning module. Each representation learning layer independently captures representations at a different hierarchical level, restoring the original input dimensions to enable hierarchical stacking of layers independent of the input dimension. The proposed approach achiever similar or better performance than state-of-the-art approaches on forecasting and imputation tasks while significantly reducing complexity in the form of learnable parameters.

### Strengths
- The paper focuses on an important problem of time series forecasting and imputation which can be useful in several practical use cases.
- Experiments show that the framework is able to outperform baselines on multiple datasets on the time series forecasting task.
- The paper is easy to follow.

### Weaknesses
 - One major concern is the motivation behind certain architectural choices, such as the introduction of merge layers and the inclusion of representation layers in each hierarchical level. The ablation studies in Figure 2 show that removing the merge layers results in only a minor drop in performance  (0.379 -> 0.382 and 0.161 -> 0.165) compared to other ablation experiments, which raises questions about their necessity. Specifically, the role of the merge layer in restoring dimensions is not clearly justified, as other methods might achieve the same without a dedicated layer. Additionally, it is unclear whether having multiple representation layers is more effective than using a single set of CNN layers at the beginning of the Transformer architecture, as is common in computer vision. The paper lacks a comparative analysis against such a baseline. Without clear evidence of performance improvements, the novelty of the proposed approach appears marginal.
- Furthermore, the claim that each representation learning layer captures representations at a different hierarchical level requires qualitative analysis to support it. The current analysis does not provide any evidence that the representation layers are learning different levels of abstraction, and it is unclear how this is achieved in practice.
- The paper's claim of achieving state-of-the-art performance on imputation tasks is not supported by the results in Table 2. The results on the ETT datasets are clearly below the state-of-the-art, and the claim should be revised to reflect this.
- How are masks handled in CNN layers (representation block)? It is not clear how the masking value -1 is processed by the CNN layers, and whether this value is treated differently from other values. This could impact the performance of the model on imputation tasks.
- Does the proposed approach need to be trained separately for different prediction horizons and different missing ratios or is it generalizable? The paper does not provide sufficient information on the generalizability of the proposed approach, and it is unclear whether the model needs to be retrained for different prediction horizons and missing ratios.

### Questions
Listed above in the weaknesses section.

### Soundness
3

### Presentation
2

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
The paper introduces a multilayered representation learning architecture called TSRM designed for multivariate time series forecasting and imputation. TSRM utilizes hierarchical encoding layers, each with a representation layer to capture diverse temporal patterns and an aggregation layer for combining learned representations. Based on a Transformer encoder-like configuration with self-attention mechanisms, TSRM outperforms SOTA approaches on seven benchmark datasets.

### Strengths
1. The article emphasizes model interpretability which is crucial for understanding and trusting its predictions.
2.  The article includes links to the source code, enabling researchers to reproduce the results.
3. The article demonstrates the model's effectiveness and generalization capabilities by testing it on datasets from various domains.

### Weaknesses
Generally, the technique of the manuscript is partially sound, and some major concerns are listed below:

1. The title of this paper could be clearer. It does not convey the specific techniques or strengths used, nor does it highlight the unique aspects of the work. The authors claim that this method can better handle different time scales, so perhaps emphasizing this could be beneficial. And this is just a suggestion.
2. The paper emphasizes that the targeted tasks are forecasting and imputation. However, the representation learning method in this paper does not specifically address forecasting and imputation, which may require additional clarification. Alternatively, future work could explore extending the method to other tasks.
3. There are too many subsections in the related work, leading to some redundant content. In particular, the "Few/zero-shot learning" subsection covers methods unrelated to this paper, so it could be appropriately condensed.


### Questions
Generally, the technique of the manuscript is partially sound, and some major concerns are listed below:
How is the kernel size chosen—is it based on specific criteria, such as the period length, or selected empirically? What about the sensitivity of this parameter? The results using $K$ independent 1D CNN layers with varying kernel sizes have not been compared to those with a uniform kernel size, even in the ablation study, which seems more important than discussing $N$.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces new architecture for forecasting/imputation of time-series. Overall, it introduces encoder blocks comprising of a Representation layer and Merge layer with self-attention in between. The representation and merge layers have no non-linearities and consist of convolution/transposed-convolution layers respectively. The models are evaluated on forecasting/imputation tasks.

### Strengths
* Clear presentation and informative figure 1.
* Experiments on both forecasting/imputation. 
* TSRM are lighter than popular models such as TimesNet/Patch-TST in terms of parameter-counts.

### Weaknesses
 * The paper introduces a lot of hyperparameters. Based on Appendix A.4, the paper searches over 13 possible EncLayers $\times$ 5 possible attention-heads $\times$ 5 possible feature-embedding sizes $\times$ 2 possible attention-functions $\times$ (at least) 4 possible CNN configurations = 2600 configurations! This extensive hyperparameter space, while potentially allowing for fine-grained optimization, raises concerns about the practical feasibility of deploying this model in real-world scenarios. The sheer number of configurations to explore makes the hyperparameter search computationally expensive, and it is unclear if the performance gains justify this cost.
* From the table having best hyperparameters, sparse-attention seems to be the best combination across all datasets. But, there seems to be significant variation across different datasets/horizons. Even for the same dataset, different horizon seems to have a different optimal configuration. This suggests a lack of robustness in the model's architecture, as the optimal configuration is highly dependent on the specific dataset and forecasting horizon. This makes it difficult to generalize the model's performance across different time-series datasets.
* Although TSRM is lighter than other models and this may help accelerate the search, the computational cost of picking the right hyperparameters cannot be ignored. Also, I couldn't find any analysis of wallclock times (train/inference) in the paper. The absence of wall-clock time analysis makes it difficult to assess the practical efficiency of the proposed model, especially when compared to other models with potentially higher parameter counts but optimized implementations. The paper should include a detailed analysis of training and inference times to provide a complete picture of the model's computational cost.
* Table 7 reports the Mean/Std across 5 runs of ETTh2 and weather. From my understanding, this mean/std is computed for running the model with optimal configuration for 5 times. In practice, the hyperparameters should be selected based on 5 runs and then, the corresponding test-performance should be reported. However, this may be very expensive given the hyperparameter space. This approach to reporting the mean and standard deviation may lead to an overly optimistic view of the model's performance, as the hyperparameter selection is not part of the reported variance. The paper should clarify whether the hyperparameter selection process is included in the reported variance.
* TimesNet seems to be uniformly better than TSRM on the imputation task. Also, PatchTST is not considered for the imputation task. The lack of a comprehensive comparison with PatchTST on the imputation task is a significant limitation, as it is a relevant baseline for time-series imputation. The paper should include a comparison with PatchTST to provide a more complete evaluation of the model's performance.
* The model is trained on forecasting/imputation tasks only. Self-supervised learning may also be explored to establish the generality of this architecture. However, the hyperparameter-search may make this expensive. The absence of self-supervised learning experiments limits the assessment of the model's generality and its potential for transfer learning. The paper should explore self-supervised learning to demonstrate the broader applicability of the proposed architecture.
* Given the huge hyperparameter space of TSRM, it may be fairer to allow PatchTST to select its patch-size/input-length. Under optimal Patch-TST performance, does TSRM still perform favorably?

### Questions
Please see weaknesses.
1) What is $\alpha$ in Eq 4?
2) How does TSRM generalize to different missing ratios at test time?

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
4

### Summary
This paper proposes a multilayered representation learning architecture for multivariate time series forecasting and imputation, achieving superior performance on seven public datasets.

### Strengths
The methodology presentation is clear, the code is provided, and the performance surpasses multiple models.

### Weaknesses
1. **Unclear motivation:** The paper does not discuss which limitations of existing methods it aims to address, lacking a direct explanation in this regard.  
2. **Limited scope of tasks:** Although the paper proposes a representation learning approach, it is only applied to forecasting and imputation, which are tasks of the same nature. I hope to see applications in classification and anomaly detection as well.  
3. **Lack of discussion and discussion on most related works:** The paper compares only with end-to-end models, but it misses comparisons with the most relevant representation-based methods, such as Cost[1]. Additionally, recent foundation models, such as MOMENT[3] and Moirai[2], could also be leveraged as representations. Please discuss differences and make comparisions.

### Questions
Please check limitations.

### Soundness
2

### Presentation
2

### Contribution
2
