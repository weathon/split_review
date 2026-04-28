# Pathformer: Multi-scale Transformers with Adaptive Pathways for Time Series Forecasting

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Transformers for time series forecasting mainly model time series from limited or fixed scales, making it challenging to capture different characteristics spanning various scales. We propose Pathformer, a multi-scale Transformer with adaptive pathways. It integrates both temporal resolution and temporal distance for multi-scale modeling. Multi-scale division divides the time series into different temporal resolutions using patches of various sizes. Based on the division of each scale, dual attention is performed over these patches to capture global correlations and local details as temporal dependencies. We further enrich the multi-scale Transformer with adaptive pathways, which adaptively adjust the multi-scale modeling process based on the varying temporal dynamics of the input, improving the accuracy and generalization of Pathformer. Extensive experiments on eleven real-world datasets demonstrate that Pathformer not only achieves state-of-the-art performance by surpassing all current models but also exhibits stronger generalization abilities under various transfer scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a variation of PatchTST architecture in the context long-horizon time series forecating.

### Strengths
- An interesting study that makes an incremental step towards making transformers effective at long-horizon forecasting task
- Paper is clearly written and topic is important for the ICLR audience

### Weaknesses
- "Recent advances for time series forecasting are mainly based on Transformer architectures". I would say this statement is not aligned with the most recent empirical results and contradicts existing facts. Having read the following papers one could argue that the transformer based models in time series forecasting have been basically a disaster in the recent years, mainly because authors of papers based on transformer-driven models disregarded including some basic baselines in their studies. Please rewrite intro and related work accordingly.
    - Challu et al. N-HiTS: Neural hierarchical interpolation for time series forecasting. AAAI'23
    - Zeng et al. Are transformers effective for time series forecasting? AAAI'23
    - Li et al. Do Simpler Statistical Methods Perform Better in Multivariate Long Sequence Time-Series Forecasting? CIKM'23
- Not all datasets are present in the study. Please include additional results on ILI and Traffic from PatchTST
- Please include results from Zeng et al. Are transformers effective for time series forecasting? AAAI'23 in your table and you will see that your results are not state of the art. This makes the results unconvincing, because basically a very complex model is not able to use the same inputs as very simple models in an effective way. Transformer based papers have consistently failed to include appropriate baselines in the studies creating a large gap in methodology and undermining the ultimate reliability of these studies. The work can be interesting if authors show that with the proposed modifications a transformer based model can be more effective than much simpler and faster models presented in Zeng et al. and Li et al.
- The model seems to borrow conceptually very heavily from the PatchTST model without explicitly recognizing the source of inspiration. Without a detailed explanation of the actual difference between the two architectures the proposed architecture appears to be a minor perturbation of the original PatchTST.

### Questions
- When talking about multi-scale processing in related work please discuss relation to Challu et al. N-HiTS: Neural hierarchical interpolation for time series forecasting AAAI'23, which seems to be relevant work on multi-scale modelling

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new multi-scale Transformer architecture for long-range time series modeling.The Discriminant Fourier Transform (DFT) is utilized to determine the patch sizes so as to divide the input time series into patches of different sizes, thus enabling cross-scale information fusion. In the multiscale transformer block, intra-patch attention and inter-patch attention mechanisms are utilized to perform attentional operations, thus enhancing the processing of temporal information.Experiments show the proposed method achieves state-of-the-art performance among existing models and exhibits superior generalization capabilities across different transfer scenarios.

### Strengths
1.The paper is well written and well-motivated.
2.The Multi-Scale Router combines the advantages of patch division and seasonality decomposition.
3.Dual attention helps to harmonize operations between intra-patch and inter-patch components, allowing the transformer to efficiently process time series data.

### Weaknesses
Time-series Dense Encoder (TiDE) is also a popular long-term time-series forecasting benchmark.But the paper does not include experiments comparing the proposed method to TiDE.

### Questions
Why is there a gap between the benchmark data in the paper and the original paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes multi-scale transformers with adaptive pathways. The proposed method integrates both temporal resolution and temporal distance for multi-scale modeling. It further enriches the multi-scale transformer with adaptive pathways. Experimental results showed the efficacy of proposed method and state-of-the-art performance.

### Strengths
1)  It's novel to propose multi-scale transformers with adaptive pathways. 

2) It's novel to integrate both temporal resolution and temporal distance for multi-scale modeling.

3) The experiments showed state-of-the-art performance.

### Weaknesses
1.The current time series forecasting datasets are pretty small, and performance may be satuated or over-fitting. Could the method be used for larger datasets?

2. Scalformer [1] also uses the multi-scale nature of time series data, this paper didn't mention and compare the similarities and differences with Scalformer.

[1] Shabani, Amin, et al. "Scaleformer: iterative multi-scale refining transformers for time series forecasting." ICLR (2023).

### Questions
1. The current time series forecasting datasets are pretty small, and performance may be satuated or over-fitting. Could the method be used for larger datasets?

2. Scalformer [1] also uses hierarchical design and the scales of time series data, Could this paper compare the similarities and differences with Scalformer.

[1] Shabani, Amin, et al. "Scaleformer: iterative multi-scale refining transformers for time series forecasting." ICLR (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
