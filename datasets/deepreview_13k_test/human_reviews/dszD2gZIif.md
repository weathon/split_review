# Long-term Time Series Forecasting with Vision Transformer

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Transformer has been widely used for modeling sequential data in recent years. For example the Vision Transformer (ViT), which divides an image into a sequence of patches and uses Transformer to discover the underlying correlations between the patches, has become particularly popular in Computer Vision. Considering the similarity of data structure between time series data and image patches, it is reasonable to apply ViT or its variations for modeling time series data. In this work, we explore this possibility and propose the Swin4TS algorithm. It incorporates the window-based attention and hierarchical representation techniques from the Swin Transformer, a well-known ViT algorithm, and applies them to the long-term forecasting of time series data. The window-based attention enables the algorithm to achieve linear computational complexity, while the hierarchical architecture allows the representation on various scales. Furthermore, Swin4TS can flexibly adapt to channel-dependence and channel-independence strategies, in which the former can simultaneously capture correlations in both the channel and time dimensions, and the latter shows high training efficiency for large datasets. Swin4TS outperforms the latest baselines and achieves state-of-the-art performance on 8 benchmark datasets. More importantly, our results demonstrate the potential of transferring the Transformer architecture from other domains to time series analysis, which enables research on time series to leverage advancements at the forefront of other domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper adapts the idea of using Vision Transformers (ViT) to the problem of time series forecasting. Vision transformers divide an image into patches and perform attention on the patches in order to attend to the whole image and yield a prediction. The idea is adapted to the problem of multivariate time series forecasting where the time series are divided into multiple windows and the windows are further divided into multiple patches. Attention layers are applied to the patches within a single window known as window attention. Shifted window attention is window attention on the time series shifted by half a window. The final architecture is a sequence of window and shifted window attentions for processing a particular scale. The model processes at multiple scales by feeding the downsampled output from the output of scale K as the input for scale K+1. The final predictions are derived using a linear layer on the flattened output from each of the scales.

Experimental results show superior performance compared to other neural network based approaches including transformer based approaches.

### Strengths
The main contribution of this paper is an approach for long term forecasting of time series using a transformer based approach.
- The proposed method can efficiently scale to very long time series due to a ViT like architecture dividing the time series into multiple windows and patches.
- The model is able to attend to various scales in the time series by virtue of the downscaling steps between different scale blocks.
- The CD variant of the proposed method can efficiently model the correlation between multiple time series.
- Experimental results show improved performance for long term prediction problems.

As summarized in table 4, the proposed model is computationally and memory efficient compared to the other approaches, while being able to model the correlations between multiple time series.

### Weaknesses
The paper does not seem to have any significant weaknesses. Some minor issues:
- Novelty: The main idea of the paper is derived from the existing Swin transformer idea, which slightly weakens the novelty of the paper.
- The confidence intervals are missing from the MSE and MAE values in the results tables.

### Questions
What is the strategy for selecting the hyper-parameters of the architecture? Were the hyper-parameters selected for each dataset individually using the validation set? Or were the hyper-parameters selected globally for all the problems simultaneously?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes use Swin Transformers (popularly used as vision transformers) for long-term time-series forecasting (ltsf). The paper proposes both channel independent and channel dependent models for multivariate LTSF forecasting. It shows that the the models can be beat or match prior transformer based baselines. More over the time-complexity does not scale quadratically with the total number of patches as in PatchTST because of the use of shifted window based attention.

### Strengths
1. I think the SWin transformer idea fits well into LTSF tasks because it reduces the number of self attention operations which is useful for long concepts and hierarchical representations are logically the right choice for extracting multi time-scale features from time-series data.

2. For the CD model, the SWin transformer concept can again be applied to have not so expensive cross series attention although I have some questions in this regard.

3. The time-complexity is understandably better than other transformer based models.

4. The performance on the model is more often than not better than PatchTST which is the next best transformer based model.

4. The paper is easy to read.

### Weaknesses
1. The paper does not compare to non-transformer based baselines which are computationally more efficient.

2. The ordering of the series should matter for the CD model which not a desirable property.

3. The last layer of the CD model is not fully clear.

4. The model performance is not monotonically increasing with size of context in some corner cases which is not the case with other SOTA models.

5. Is the ablation of varying hierarchical design done in the correct manner? As I understand more hierarchies also mean more layers? Is it not better to keep the number of layers the same and just have hierarchy in one model while the scales are fixed in all layers in the ablation one?

6. What would be the strategy to handle static and dynamic covariates ?

Overall I believe the paper is well written and the use SWin is logical at least in the CI case. The architecture is not novel but nevertheless has not been used for time-series before. I would like to see the answers of my questions before deciding on the final score. It would also be good if the authors can think of some way to show whether the different scales in the hierarchy extract different types of information like long term trends vs local seasonality.

### Questions
1. Can the authors elaborate what the last layer looks like for the CD model? is it just mapping the flattened version of all output tokens to the future of all M time-series. In this case is this layer not too big? There might be better designs that map only specific patches to specific output predictions.

2. For vision models contiguous patches in the window are visually close in the image. This is not the case for the channel dimension in the CD time-series case. In other words does the order of the time-series matter? It should not matter in the ideal case. Can the authors show this experimentally?

3. Since the paper has a section on time-complexity it would be wise to compare with non transformer methods like TiDE (https://arxiv.org/pdf/2304.08424.pdf) and N-HiTS (https://arxiv.org/pdf/2201.12886.pdf). These methods are much faster and have comparable or better performance. For instance the numbers reported in the traffic dataset for the TiDE model are better than the ones reported in the paper. It would be good to cite and compare to these MLP based works.

4. It seems that for some horizon lengths in Figure 6 the performance decreases a little bit with increasing context. This does not seem to be the case for PatchTST and TiDE. Any intuition on why this might be happening?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to transfer the success of vision transformer to time series forecasting. The proposed method incorporates window-based attention and hierarchical representation from Swin Transformer to long-term time series forecasting. Experimental results showed state-of-the-art performance.

### Strengths
1. It's novel to incorporate the window-based attention and hierarchical representation from Swin Transformer to time series forecasting.

2. The performance is better than baselines.

### Weaknesses
1. The current time series forecasting datasets are pretty small, and performance may be satuated or over-fitting. Could the method be used for larger datasets?

2. Scalformer [1] also uses hierarchical design and the scales of time series data, this paper didn't mention and compare the similarities and differences with Scalformer.
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

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a model called Swin4TS for long-term time series forecasting. Swin4TS adopts SwinTransformer with native window-based attention and hierarchical representations adapted for the time series modality, which has shown powerful capability in CV. The paper provides two variants, Swin4TS/CD and Swin4TS/CI, which can adapt to channel-dependent and channel-independent strategies, respectively. The experiments show that the model outperforms existing baselines on eight benchmark datasets.

### Strengths
1. Swin4TS achieves improved performance on multiple benchmark datasets.

### Weaknesses
1. The paper is somewhat not well-organized. The figures (1, 2, and 4) are not rough to convey enough insights and are unportable. The tables (2, 3, and 4) for many experiments are incomplete on the dataset. Some notations can be not so rigorous (\hat_x may be better to denote the model predictions). Thus, this paper essentially needs further polishing. 
2. The contributions of the paper can be not enough, which is the most fatal point. Swin-transformer modules are adapted for the time series. It's like lowering the dimension of attention directly on 1D time series representations. Is this more motivating than design models considering time series properties? How does inductive bias like shift invariance help time series forecasting? Without considering the gap between the two modalities, I think it has not contributed much to the research field.
3. The performance incremental is marginal. The forecasting result of Swin4TS over PatchTST can be small. And I think the ablations should be conducted on more extensive datasets. Also, I suggest that experiments such as hyperparameter effects are more suitable to be placed in the appendix, and more experiments exploring the helpful inductive bias should be considered.
4. Unsolved contribution: "We successfully apply techniques from ViT to LTSF", which does not "indicate the potential of connecting time series with other domains within the Transformer architecture". What does the 'connection' mean? The author provides no experiments to validate the results of cross-domain/modality transfer.

### Questions
1. SwinTransformer in computer vision are commonly leveraged for high-level feature extraction, which is widely applied on tasks such as image classification. The time series forecasting task, on the contrary, belongs to a typical generative task and needs to learn low-level feature representation for time point reconstruction. How does the proposed model cope with the gap between tasks and representation granularity? 
2. Is it an advantage that being able to combine CI/CD mechanisms? Previous forecasting models are commonly implemented by CD, but they can also be easily incorporated with CI, no matter Transformers or non-Transformers.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
