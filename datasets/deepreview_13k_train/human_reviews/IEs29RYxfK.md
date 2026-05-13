# VisionTS: Visual Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
Foundation models have emerged as a promising approach in time series forecasting (TSF). Existing approaches either repurpose large language models (LLMs) or build large-scale time series datasets to develop TSF foundation models for universal forecasting. However, these methods face challenges due to the severe cross-domain gap or in-domain heterogeneity. This paper explores a new road to building a TSF foundation model from rich, high-quality natural images. Our key insight is that a visual masked autoencoder, pre-trained on the ImageNet dataset, can naturally be a numeric series forecaster. By reformulating TSF as an image reconstruction task, we bridge the gap between image pre-training and TSF downstream tasks. Surprisingly, without further adaptation in the time-series domain, the proposed \ours could achieve superior zero-shot forecasting performance compared to existing TSF foundation models. With fine-tuning for one epoch, \ours could further improve the forecasting and achieve state-of-the-art performance in most cases.  Extensive experiments reveal intrinsic similarities between images and real-world time series, suggesting visual models may offer a ``free lunch'' for TSF and highlight the potential for future cross-modality research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper titled "VISIONTS: VISUAL MASKED AUTOENCODERS ARE FREE-LUNCH ZERO-SHOT TIME SERIES FORECASTERS" introduces a approach to time series forecasting (TSF) by leveraging pre-trained visual masked autoencoders (MAEs) on natural images. The key idea is that the pixel variations in images can be interpreted as temporal sequences, which share intrinsic similarities with time series data. The authors reformulate TSF as an image reconstruction task, allowing the pre-trained MAE to perform zero-shot forecasting without further adaptation. Extensive experiments demonstrate that VISIONTS achieves superior zero-shot forecasting performance compared to existing TSF foundation models and can further improve with minimal fine-tuning. The findings suggest that visual models may offer a "free lunch" for TSF and highlight the potential for future cross-modality research.

### Strengths
1. The authors provide extensive experimental results across 43 TSF benchmarks, demonstrating VISIONTS's effectiveness in zero-shot and few-shot settings. 

2. The paper offers a theoretical analysis of the similarities between images and time series, providing a solid foundation for the proposed method. This contributes to a deeper understanding of cross-modality transferability.

3. The paper is well-written, with clear explanations of the methodology, experiments, and results. The figures and tables are informative and support the narrative effectively.

### Weaknesses
1. The current approach is limited to univariate forecasting, which may restrict its applicability in real-world scenarios where multivariate time series are common. This limitation could be a barrier to broader adoption. Specifically, the method treats each time series channel independently, neglecting potential inter-channel dependencies which are crucial for accurate forecasting in many real-world multivariate datasets. This naive approach may not capture the complex relationships between different time series variables, leading to suboptimal performance in practical applications.

2. While the use of pre-trained models is a strength, it also introduces a dependency on external datasets for performance, which may not always be ideal or ethically sound. The reliance on pre-trained visual models, while avoiding the need for large time series datasets, shifts the dependency to potentially biased or domain-mismatched image datasets. This raises concerns about the generalizability of the approach, particularly if the characteristics of the image data do not align well with the time series data being forecasted. Did you use EVA-CLIP?

3. The paper does not fully address how VISIONTS scales with larger and more complex time series datasets, which is a critical consideration for practical applications. While the authors demonstrate results on a number of datasets, the paper lacks a detailed analysis of the computational cost and memory requirements as the length and dimensionality of the time series increase. This is a critical consideration for real-world deployment, where time series can be extremely long and high-dimensional.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a new perspective that treating time series forecasting problems as image reconstruction problems. And directly take the pretrained MAE model to conduct such tasks. Specifically, the paper just performs segmentation, normalization and alignment to transform 1D time series data into 2D data, and predict masked tokens for TSF tasks. The results shows that this algorithm has decent performance under both zero-shot and full-shot settings.

### Strengths
1. This paper provides a novel view for TSF problems, and explain with reasonable motivations in Fig.2.
2. The method part provides sufficient details about the proposed method, making it easy to read and follow.
3. This paper provides experiments on a wide range of tasks to validate the proposed method.

### Weaknesses
1. In the alignment step, the scaling process is influenced by both the context length $L$ and the prediction length $H$. It seems that the forecasted result at $L+1$ may change due to whether we will predict $L+2$ or not, which is counter-intuitive.

Since the method map any-length series to a fixed resolution, I suppose it requires the model to understand patterns of different frequency. This might be hard for a pretrained vision model. It is trained only with natural images, which cannot cover drastic changes such as noises.

2. If the similarity between image and TSF holds true, maybe the authors should try other image inpainting models for the TSF tasks. We may assume that thoses models can have a better performance for image reconstruction.

3. In full-shot experiments, the authors decide to tune all the LN parameters. It is uncommon for the validation in vision pretrain model. Usually we either finetune the full model or only the last linear layer (e.g. linear probe). I wonder the reason that the authors prefer the LN tuning.

### Questions
My main concerns are listed in weaknesses. Regarding these comments, I would like the authors to check if MAE is suitable for TSF.

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
This paper proposes using MAE, a masked autoencoder pretrained on 2D images with mask modeling pretraining, as a zero-shot forecasting model for time series data. The proposed method reformulates the time series forecasting task into a reconstruction task. Experimental results show that this method can perform zero-shot forecasting and achieve state-of-the-art performance in most cases after fine-tuning.

### Strengths
- This paper provides an interesting view of using MAE pretrained on vision tasks as a zero-shot time series forecasting model. 
- Results show that this model is better than text-based time series forecasting in zero-shot settings. 
- An interesting approach is proposed to achieve this transformation from image to text.

### Weaknesses
 # After reading the rebuttal:
I appreciate the authors' feedback on my concerns. However, as the responses still fail to resolve my concerns, I have decided to maintain my initial score.

- The statement, “VisionTS can work well for multivariate forecasting by using the channel independence strategy,” does not demonstrate that VisionTS effectively handles the relationships among multivariate data. While employing a channel independence strategy for multivariate handling is straightforward, it is not necessarily the optimal approach. Achieving good performance with this strategy might be more indicative of limitations in the benchmark rather than evidence that multivariate relationships are unnecessary.

- I appreciate that the authors provided some possible explanations for why MAE can be used for zero-shot learning on time series. However, none of these explanations serve as solid evidence. For instance, the motivation and case study could equally apply to other models, such as LLMs and time series. Additionally, the Modality Analysis and Figure 6 highlight the dissimilarity between images and most time series data, which contradicts the claim of “a relatively small gap between images and some time series.”

- The authors use LaMa as an example of another vision model. Given that LaMa employs a relatively weak vision backbone, I wonder whether using a vision model with stronger representation capabilities would result in better performance. Alternatively, carefully tuning the introduced hyperparameters might allow other models, such as LLMs or randomly initialized models, to achieve comparable performance.

- I appreciate the authors’ explanation regarding the tuning of hyperparameters. However, these results remain empirical and lack theoretical analysis.

# Initial review:
- Using MAE for forecasting only works for univariate forecasting, while the more challenging and important multivariate forecasting is not supported.
- It doesn't really make sense that MAE, which is pretrained solely on images, can perform reasonable zero-shot forecasting, as no time series information is encoded in the MAE pretraining. This work only transforms the format of time series data to make it compatible with MAE.
- The transformation between a univariate input X and the image-like 2D matrix is unclear. The explanation of how P is selected should be provided. How is P obtained from sampling frequency and Fast Fourier Transform? Why is this the right way to select P, or is P not important for the final performance?
- There are tricks and hyperparameters involved in aligning MAE with time series forecasting, but the explanations are unclear.
  - The standard deviation of the input is controlled by a hyperparameter r. While an initial explanation is given, more detailed experiments and justification should be provided for the choice of this value.
  - Why does setting c = 0.4 perform well, aside from the experimental results?
- Given the many tricks and unclear explanations, I doubt whether MAE can truly perform zero-shot time series forecasting or if it merely overfits to these time series datasets to achieve a favorable evaluation number.
- The inference cost comparison is only provided for these LLM-time series models, while a comparison with native time series models should also be included.

### Questions
- Why does MAE work for zero-shot learning on time series data?
- How do these tricks work, and why are these hyperparameters chosen aside from experimental results?- 
- For more questions, please refer to the weakness sections.

### Soundness
2

### Presentation
1

### Contribution
2
