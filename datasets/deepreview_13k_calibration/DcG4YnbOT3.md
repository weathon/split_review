# Vision-Enhanced Time Series Forecasting by Decomposed Feature Extraction and Composed Reconstruction

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Time series forecasting plays a crucial role in various domains, such as power and weather forecasting. In recent years, different types of models have achieved promising results in long-term time series forecasting. However, these models often produce predictions that lack consistency with the style of the input, resulting in reduced reliability and trust in the forecasts. To address this issue, we propose the Vision-Enhanced Time Series Forecasting by Decomposed Feature Extraction and Composed Reconstruction (VisiTER), which leverages the rich semantic information provided by the image modality to enhance the realism of the predictions. It consists of two main components: the Decomposed Time Series to Image Generation and the Composed Image to Time Series Generation. In the first component, the Decomposed Time Series Feature Extraction Model extracts periodic and trend information, which is then transformed into images using our proposed time series to vision transformation architecture. After converting the input time series into images, the resulting images are used as style features and concatenated with the previously extracted features. In the second component, we use our proposed TimeIR along with the previously obtained feature set to perform image reconstruction for the prediction part. Due to the rich information provided, the reconstructed images exhibit better consistency with the input images, which are then transformed back into time series. Extensive experiments on seven real-world datasets demonstrate that VisiTER achieves state-of-the-art prediction performance on both traditional metrics and new metrics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses time series forecasting from the view of image modal. The authors propose a novel model called VisiTER, which leverages image modality to enhance the realism and consistency of time series predictions. The experimental results show that VisiTER present promising performance.

### Strengths
1.	The paper introduces a novel approach to time series forecasting by framing the problem within the image modality, offering a fresh perspective.
2.	The model structure is clear and appears logically sound.
3.	The presentation is well-organized and easy to follow.

### Weaknesses
1.	The motivation behind the paper is that existing models often produce predictions that lack consistency with the "style" of the input. However, the concept of “style consistency” is not clearly defined, weakening the argument for this motivation. The notion of style remains vague, making it difficult to assess whether the proposed method truly addresses this issue. A more rigorous definition, perhaps involving specific statistical or geometric properties, is needed to validate the claim of improved style consistency.
2.	The rationale for using Vision Transformers (ViT) for time series feature extraction is not well-explained. Specifically, it is unclear what key differences between image and time series modalities justify the use of ViT. For instance, while the order/position of image patches is irrelevant, the temporal order of time series data is crucial. This distinction needs further elaboration. The paper should discuss how the positional embeddings used in ViT are adapted to capture the temporal dependencies inherent in time series data, and whether this adaptation is sufficient to justify the use of ViT over other time-series specific architectures.
3.	The paper omits some commonly-used datasets, such as Traffic and Solar-Energy. Including results from these datasets would strengthen the evaluation of the proposed model. The absence of these standard benchmarks makes it difficult to compare the performance of the proposed method with existing state-of-the-art time series forecasting models.
4.	The paper does not provide the source code, which is critical for reproducibility. Given that the reported results claim state-of-the-art performance, evidence supporting this claim is necessary. Without access to the code, it is impossible to verify the implementation details and reproduce the reported results, which is a significant barrier to the acceptance of the work.

### Questions
Please answer the concerns of W1 and W2, and supplement the materials of W3 and W4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces VisiTER, a novel method for time series forecasting that leverages the rich semantic information contained in images by converting time series data into visual representations. The proposed method consists of two primary components: the decomposition of time series data into images and the prediction of time series through three image inputs. In the first component, a feature extraction model decomposes the time series to isolate periodic and trend information, which is then transformed into images. In the second component, the authors employ the TimeIR module to perform time series forecasting via image reconstruction. Experimental results on seven real-world datasets demonstrate that VisiTER achieves state-of-the-art performance in both traditional and novel evaluation metrics.

### Strengths
1.Compared to traditional methods that directly map time series data to scatter plots and then reconstruct them, this paper proposes the T2V method. By diffusing and continuousizing the scatter points, the generated images are more suitable as inputs for image models. Additionally, the introduction of multiple Swin Transformer Blocks in the TimeIR model allows the model to better focus on the detailed information of the time series. This approach leverages the rich information in the image modality, enabling the model to capture complex relationships more effectively.

2.The paper introduces the DTFE module, which effectively extracts periodic and trend features, thereby enhancing the model's performance. This module can efficiently handle the periodic and trend characteristics of time series data and convert them into image form for reconstruction, improving the accuracy and stability of the reconstruction results.

3.The introduction of the TimeIR model enables more efficient utilization of periodic, trend, and style features for image reconstruction, which is crucial for time series prediction. This model enhances the overall predictive capabilities of the system.

4.Experimental results show that the VisiTER model achieves state-of-the-art performance across multiple datasets. Moreover, the authors use the SSIM metric to evaluate the similarity between the generated time series images and the actual time series. The results indicate that the VisiTER model also performs exceptionally well in terms of SSIM, demonstrating its robustness and effectiveness.

### Weaknesses
1.Lack of Motivation for Image Transformation. The authors do not provide sufficient justification for the advantages of converting time series data into images for the forecasting task. There is a lack of ablation studies to explore the motivation behind this transformation, which weakens the argument for its necessity.

2.The concept of "style features" in the context of time series tasks is somewhat abstract and not clearly defined. This lack of clarity makes it difficult for readers to understand the relevance and reasonableness of these features, potentially undermining the credibility of the approach.

3.The introduction of the SSIM metric seems to lack a strong rationale. While SSIM is useful for evaluating image quality, its relevance and significance in the context of time series prediction are not well justified. This raises concerns about the appropriateness of using such an image-based metric for this specific task.

4.The authors could enhance the robustness of their method by treating the image reconstruction component as a plug-in module and applying it to other existing baseline models. This would help to determine whether the image reconstruction approach can improve the performance of different models, providing stronger evidence for its effectiveness.

### Questions
Please refer to Weaknesses.

### Soundness
2

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
4

### Summary
This paper presents VisiTER (Vision-Enhanced Time Series Forecasting), a new framework integrating image-based approaches to enhance time series forecasting. VisiTER consists of two main components: Decomposed Time Series to Image Generation and Composed Image to Time Series Generation. The approach transforms time series data into images to capture richer semantic information and generate consistent predictions with greater fidelity.

### Strengths
Good set of figures (fig 1, 2, 3) that roughly show the proposed idea

### Weaknesses
 - Writing: The author should revise the comprehension and linking of ideas. For example:
    - line 47→55: Linking words choices (The first challenge … → Additionally, … → The second challenge …) can be improved.
    - line 47→49: Ambiguous connection: Why the complexity in image transformation can be explained with the latter idea of direct scatter plots causing information loss?
- Method:
    - from the text description (Sec. 3.2) and figures (1, 2), the idea is seem to linked with extraction of periodic and trend components of input data, while from the loss, the modules try to predict the these component for output instead. The authors should clarify this point and reflect it in the manuscript.
    - T2V module: why expanding in Y-dimension can help with reconstruction process?
- Experiment:
    - The overall pipeline involves DTFE, V2T which have their own transformer blocks inside. The author should have experiments calculating the computational overhead of proposed method, in comparison with its performance gain.

### Questions
Please refer to Weaknesses for related questions.

### Soundness
2

### Presentation
3

### Contribution
2
