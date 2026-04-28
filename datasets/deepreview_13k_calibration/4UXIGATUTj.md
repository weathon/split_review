# Forecasting Whole-Brain Neural Activity from Volumetric Video

- Decision: Reject
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
Large-scale neuronal activity recordings with fluorescent calcium indicators are increasingly common, yielding high-resolution 2D or 3D videos. Traditional analysis pipelines reduce this data to 1D traces by segmenting regions of interest, leading to inevitable information loss. Inspired by the success of deep learning on minimally processed data in other domains, we investigate the potential of forecasting neuronal activity directly from volumetric videos. To capture long-range dependencies in high-resolution volumetric whole-brain recordings, we design a model with large receptive fields, which allow it to integrate information from distant regions within the brain. We explore effects of pre-training and perform extensive model selection, analyzing spatio-temporal trade-offs for generating accurate forecasts. Our model outperforms trace-based forecasting approaches on ZAPBench, a recently proposed benchmark on whole-brain activity prediction in zebrafish, demonstrating the advantages of preserving the spatial structure of neuronal activity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel method for neural activity forecasting of zebrafish that works on the raw volumetric video instead of using standard preprocessing that reduces the original 4D space to 1D (trace matrix) and disregards spatial relationships between neurons. To do this, a u-net architecture is employed, taking advantage of a large scale neural dataset and performing extensive ablations for model selection. Multiple measures were taken to enable scaling the architecture for this computationally expensive problem, such as using the temporal context dimension as input channels, lead-time conditioning, and distributed training. The ablation results show that (1) pretraining on other specimens does not help, (2) there is a trade-off between spatial and temporal context, and (3) that downsampling input resolution up to 4x is beneficial to performance. Compared to the best trace-matrix models, the proposed multivariate model achieves 10% reduction in MAE for the short context forecasting setting in both the test and the holdout sets, while it is comparable to the trace-matrix models for long-context forecasting in the test set and 12% better in the holdout set.

### Strengths
The paper is original in the sense of creative combinations of existing ideas (the components of the model that enable scaling), application to a new domain (forecasting on minimally preprocessed / raw data from weather to neural data), as well as removing limitations from previous works (removing dependency on segmentation mask accuracy and avoiding loss of information caused by conversion to trace-matrix). Writing style is very high quality, and all the methods and results get across in a relatively clear manner to the reader. To the specific line of research (forecasting neural data), the method proposed seems to be a significant step forward in the field’s development, moving from hand-crafted to learnable features.

### Weaknesses
There are some presentation issues that impact the understanding of a reader that is not very familiar to forecasting neural data.
* These are mainly in the abstract and introduction, while once entering section 2 all misunderstandings of this reader were resolved. Nevertheless it would be beneficial for the paper to have them fixed. (1) Until section 2 it was not very clear that the goal is to predict future steps from previous steps, and not one neural modality (e.g. electrical signal) from another (e.g. blood oxygen). (2) It was not clear that the neuron segmentation mask is applied in both the trace models and the proposed model, but at different points in the pipeline, i.e. in the latter the forecasting itself is done on the volumetric video and afterwards the mask is applied before computing the error - without knowing this it is not clear how the two methods can be compared fairly. It would also help if in Figure 1 the same notation was used between orange (trace) and blue (proposed) in the segmentation mask block, i.e. instead of “Extract Neurons” and “Mask Neurons” say “Apply segmentation mask” in both cases. (3) In the abstract the phrase “we design a model to handle the high resolution and large receptive fields…” is structured in a confusing way where the reader does not understand if the large receptive fields are an aspect of the model or the recordings. (4) Minor - the footnote on page 2 is not so much footnote information, but rather more suitable for the main text.
* Additionally, Figure 2 should have a more informative caption that explains better what is shown, e.g. it is not clear what the colored blobs are, segmentation masks?
* Is H=32 the only setting that is tested and why? Not sufficiently described in the paper.
* In the conclusion, calling the findings counterintuitive seems excessive; there is no reason to assume that high input resolution, pretraining, or increased model capacity works well for all domains and applications. Results sufficiently showcase enough reasons why these sometimes useful settings might lead here to overfitting, distribution shifts, etc.

### Questions
Could "scaling the field of view of the network so the size remains constant while increasing to full resolution" make the full-resolution model handicapped in terms of field of view? There is a chance this is already answered in the paper but the reader missed it.
Other than that, fixing the presentation issues in the previous section.

### Soundness
4

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
This paper proposes a new approach to neuronal response modeling by predicting/forecasting the volumetric video instead of the per-neuron calcium trace (dF/F) or spike train, which is the norm in neural response prediction. This approach allows the model to take advantage of the inter-cell activity and spatial organization of the population that is typically discarded when deconvolving the volumetric video to individual response traces. The authors evaluated a range of video and trace-based models on ZAPBench and showed that the video-based model outperforms trace-based models in short temporal context length conditions.

### Strengths
- To my knowledge, neural response prediction/forecasting directly from volumetric video is novel. This allows minimal preprocessing of the data which can be beneficial to deep learning-based methods.
- A wide range of training and evaluation conditions are compared, including trade-offs of spatial and temporal resolution, pre-training vs direct training, and training set size and combinations. These empirical results can guide future work in modeling neural responses.

### Weaknesses
A key motivation of this work, as stated by the authors in Section 2, is that the typical deconvolution step to convert volumetric video to dF/F response traces can lead to loss of information, such as cell spatial organization, inter-cell activities, etc. However, while the video-based model appears to outperform the trace-based model in short temporal context-length conditions (though similar performance in longer context length), it is unclear whether or not this is due to the additional information that exists in the raw data and that the video-based model is indeed taking advantage of such information. Specifically, the paper does not sufficiently isolate the impact of spatial information from other factors, such as potential artifacts introduced by the deconvolution process or the loss of inter-cell activity information when using trace-based methods. The experiments should more directly test if the spatial organization of cells is the key factor driving the performance difference.

MAE might not be the most intuitive metric for getting a sense of how the (video and traced-based) models are performing. For instance, I am not sure if an MAE value of 0.02 is good or bad, or how big of a difference is an MAE of  0.02 to 0.04? In particular, I believe ZAPBench is a new dataset and we don’t have any other models to compare against these MAE values, other than the single trace-based model provided. Without a clear understanding of the typical range of calcium signals and the expected variability, it is difficult to interpret the MAE values in a meaningful way. It would be beneficial to include metrics that are more commonly used in the field of neural response prediction, which would allow for a better comparison to existing literature.

Unclear trade-off in computation cost between video-based and trace-based models. The paper mentions the use of 16 A100 40GB GPUs for training the video-based model and ~5k GPU hours for the loss ablation experiment. However, it does not provide a clear comparison of the training time and computational resources required for the final, best-performing models of both video-based and trace-based approaches. This makes it difficult to assess the practical feasibility of the proposed video-based method, especially considering the potential for increased computational demands.

### Questions
Major
- It would be nice to test whether or not the trace-base model performed (relatively) poorly due to the lack of inter-cell activities or imperfect masking as suggested in Section 2 and Figure 2. I suggest applying the segmentation masks to the video, i.e. set regions outside of the identified cells as background, and train the video-based model on the masked videos. This should give us a sense of the influence of inter-cell activities and imperfect masking, and isolate the influence of spatial organization of the cells. 
- I suggest the authors include metrics that are commonly used in neural response prediction so that readers can have a sense of how well these models are performing, such as normalized correlation ($CC_\text{norm}$) [1], or fraction of explainable variance explained (FEV) [2], basically metrics that takes trial-to-trial variability into account.
- Can the authors comment on the computational cost of the models? The authors stated in the hyperparameter search section and appendix A.3 that 16 A100 40GB GPUs are used to train the video-based model, and ~5k GPU hours (so ~300 hours in wall-time) was used in the loss ablation experiment in Figure 4, which is a considerable amount of computational time and cost. Can the authors share the time it took to train the final (best) video-based and trace-based models? I believe the authors should discuss the trade-off between the two approaches in computation cost if they are indeed substantially different. To clarify, I think it is fine for the method to be more computationally expensive than other methods, but it is important to point it out.

Minor
- What is the frame rate of the video? 
- Why and how are the two temporal context lengths (4 and 256) selected? Does it make sense to predict the future 32 frames from only 4 frames?
- In the hyperparameters section and Figure 1, it is stated that the models optimize the trace-based MAE. Does this include the video-based model? Since the video-based model inputs and outputs a video, does it make a difference to optimize the recorded and predicted video MAE?
- How are the hyperparameters selected? Hand-picked or via some form of hyperparameter search (random search, bayesian search, etc.)

[1] Schoppe, Oliver, et al. "Measuring the performance of neural models." Frontiers in computational neuroscience 10 (2016): 10.

[2] Cadena, Santiago A., et al. "Deep convolutional models improve predictions of macaque V1 responses to natural images." PLoS computational biology 15.4 (2019): e1006897.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript proposes the utilization of deep learning techniques for the prediction of neuronal activity recordings with fluorescent calcium, asserting superior performance over previous baselines. A series of ablation studies have revealed practical insights into model pre-training and hyperparameter tuning.

### Strengths
1.This paper employs a deep learning approach based on U-Net to directly process 4D neural activity recordings, circumventing complex preprocessing methods that may introduce performance degradation.

2.A series of ablation studies have revealed practical insights into model pre-training and hyperparameter tuning.

After reading the authors' rebuttal and the comments from Reviewer 5NDV, I agree that neural response prediction/forecasting directly from volumetric video is novel. This approach allows for minimal preprocessing of the data, which can be advantageous for deep learning-based methods.

### Weaknesses
1.The authors fail to elucidate the significance of this study anywhere within the main text, which raises questions about the necessity of forecasting whole-brain neuronal activity. The authors are encouraged to provide additional context in the abstract or introduction section.

2.This paper primarily utilizes the initial frames of neuronal activity recordings with fluorescent calcium indicators to predict subsequent frames, representing an application of U-Net in a specific domain. It does not offer additional insights or novel perspectives to advance the field of artificial intelligence. Therefore, this manuscript would be more appropriately submitted to conferences or journals focused on neuroscience or medical image processing, as it does not align with the thematic scope of ICLR.

3.The paper presents a limited comparison with only one baseline, namely the "trace-based model," as shown in Figure 6. It raises the question whether ZAPBench, as a benchmark, evaluated only this single model type. The authors are encouraged to include additional baselines for comparison to substantiate the superiority of the proposed method.

4.On line 308, the authors refer to a "segmentation mask," yet on line 68, they claim that their method can directly process 4D data. The authors are requested to clarify the apparent contradiction in their narrative.

5.In the fourth contribution (line 108), the authors state that their proposed method is the "only approach that consistently benefits from multivariate information." However, I did not encounter any experimental justification related to multivariate information in the main text. If such experiments were conducted, please direct me to the relevant sections within the paper.


6.The description of temporal dimension processing on line 200 is unclear. I would like to confirm whether the authors' approach involves merging the temporal dimension with the batch dimension, such as transforming the data shape as follows: (batch, 2048, 1152, 72, T) --> (batch*T, 2048, 1152, 72). If not, please provide clarification on their methodology.

7. As shown in Figure 6, under the conditions of Test C = 256 and Holdout C = 256, the proposed method shows almost no improvement over the baseline (Trace). Under the condition of Holdout C = 4, the performance of the proposed method is notably weaker than the baseline (Trace) when the number of steps exceeds 5. Therefore, the practical advantage of the proposed method is not clearly demonstrated.

### Questions
1.On line 308, the authors refer to a "segmentation mask," yet on line 68, they claim that their method can directly process 4D data. The authors are requested to clarify the apparent contradiction in their narrative.

2.In the fourth contribution (line 108), the authors state that their proposed method is the "only approach that consistently benefits from multivariate information." However, I did not encounter any experimental justification related to multivariate information in the main text. If such experiments were conducted, please direct me to the relevant sections within the paper.


3.The description of temporal dimension processing on line 200 is unclear. I would like to confirm whether the authors' approach involves merging the temporal dimension with the batch dimension, such as transforming the data shape as follows: (batch, 2048, 1152, 72, T) --> (batch*T, 2048, 1152, 72). If not, please provide clarification on their methodology.

### Soundness
2

### Presentation
2

### Contribution
3
