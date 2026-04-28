# Learned Data Transformation: A Data-centric Plugin for Enhancing Time Series Forecasting

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Data-centric approaches in Time Series Forecasting (TSF) often involve heuristic-based operations on data. This paper proposes to find a general end-to-end data transformation that serves as a plugin to enhance any arbitrary TSF model's performance. Our idea is to generate transformed data during an approximating process and to co-train a predictor for evaluating data with the transformation. To achieve this, we propose the Proximal Transformation Network (\model{}), which learns effective transformations while maintaining proximity to the raw data to ensure fidelity. When orthogonally integrated with popular TSF models, our method helps achieve state-of-the-art performance on seven real-world datasets. Additionally, we show that the proximal transformation process can be interpreted in terms of predictability and distribution alignment among channels, highlighting the potential of data-centric methods for future research. Our code is available at \href{https://anonymous.4open.science/r/PTN-2FC6/}{https://anonymous.4open.science/r/PTN-2FC6/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a Proximal Transformation Network to learn effective transformations while maintaining proximity to the raw data to ensure fidelity. The model includes a convolution-based Encoder and an attention-based Encoder that provide transformation on different levels of proximity. The training involves a co-optimization of the proximity of the transformed data and forecasting accuracy. The method achieves state-of-the-art performance on seven real-world datasets. Additionally, the paper shows that the proximal transformation process can be interpreted in terms of predictability and distribution alignment among channels.

### Strengths
* The traditional time series prediction task has been redefined as a "two-step problem," the goal is to learn predictions on the transformed data and align them with the raw series, showcasing innovation.

* The proposed method achieves state-of-the-art performance on seven real-world datasets. The ablation experiments are comprehensive.

* The effectiveness of the proposed module is demonstrated through the distribution of data on the loss surface, revealing its ability to categorize time series into predictable and unpredictable groups in a self-supervised manner, with a particular focus on enhancing performance for the former.

### Weaknesses
 * When the predictor is a linear model, the complexity of PTN seems to far exceed that of the predictor itself. It is suggested to provide the time and memory complexity analysis of the proposed module. Additionally, for predictors that include modules capturing channel-wise and patch-wise correlations, the proposed PTN appears redundant, which may affect its generalizability. Specifically, the paper lacks a detailed analysis of the computational overhead introduced by the PTN, particularly in scenarios where the base predictor is computationally lightweight, such as a linear model. The attention mechanisms within PTN, while potentially beneficial, could introduce significant computational costs, especially with longer time series or larger channel dimensions. Furthermore, the paper does not adequately address the potential for redundancy when PTN is used with predictors that already incorporate similar mechanisms for capturing channel-wise and patch-wise correlations. This overlap in functionality raises concerns about the necessity of PTN in such cases and its impact on overall model efficiency and generalizability.

* Based on the results in Table 10, the PTN module appears to enhance performance primarily for simple linear models, while its effectiveness on more complex models, such as iTransformer and PatchTST, varies against the dataset. Considering that the main objective of this paper is to propose a general plugin, it is essential to select a sufficient range of predictors for experimentation. The inconsistent performance gains across different model architectures and datasets raise questions about the robustness and general applicability of the proposed PTN module. The fact that PTN seems to be most effective with linear models, while exhibiting variable performance with more complex models, suggests that its benefits may be limited to specific scenarios. A more thorough investigation is needed to understand the conditions under which PTN is most effective and to explore potential modifications that could improve its generalizability across diverse model architectures and datasets.

* The article contains several errors that require careful proofreading. For example, "Encoder" in line 65 should be corrected to "Decoder," and the shape of the matrix in line 129 needs clarification. Additionally, there are concerns regarding Figure 2(b), where $l_{\text{raw}}$ decreases as $l_{\text{pred}}$ increases, which seems counterintuitive and requires further explanation. The presence of such errors detracts from the overall clarity and credibility of the paper. The lack of precision in describing the matrix shape in line 129 makes it difficult to fully understand the proposed method. The counterintuitive behavior of $l_{\text{raw}}$ and $l_{\text{pred}}$ in Figure 2(b) requires a more detailed explanation to ensure that the reader can fully grasp the underlying mechanisms of the proposed approach.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Proximal Transformation Network (PTN) as a data-centric plugin for enhancing time series forecasting. The proposed PTN aims to find optimal data transformations that improve model performance while preserving data fidelity. Extensive experiments demonstrate state-of-the-art results when the method is integrated with various forecasting models. The key contributions include a reformulation of the time series forecasting problem, the introduction of PTN, and successful performance on seven real-world datasets. The approach highlights the potential of data-centric methods in advancing time series forecasting research

### Strengths
1.The paper is well-organized and easy to understand.
2.The proposed model can be widely applied.
3.The proposed model achieves SOTA performance.

### Weaknesses
1.In section 3.2, while two losses are considered, what are the motivations/insights of the losses. The reason why they have an influence on the results should be explained.
2.As a plug-and-play model, whether it is lightweight and easy to use is an important criterion, but the experiment does not analyze the time and space complexity of the proposed model.
3.While the performance of the model is not promising enough, the authors don’t analyze the results or explain the pattern.

### Questions
1.What is the motivation of losses in section 3.2?
2.Please study the time and space complexity of the proposed model.
3.Why the performance is not stable compared with baselines?

### Soundness
3

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
3

### Summary
The paper proposes the Proximal Transformation Network (PTN), a plugin for improving time series forecasting (TSF) by learning general, data-centric transformations that enhance model performance while preserving proximity to the original data. PTN, which combines a convolutional encoder and attention-based decoder, can integrate with any TSF model, optimizing both data fidelity and forecasting accuracy. Through experiments on seven real-world datasets, PTN achieves state-of-the-art results, showing its effectiveness across linear and non-linear models and its ability to adapt data distributions for better predictability. Additionally, PTN supports interpretability and transferability, offering potential applications in other time series tasks, like anomaly detection and classification.

### Strengths
1. PTN offers a general, model-agnostic approach to improve time series forecasting across diverse datasets.

2. It achieves state-of-the-art results, enhancing accuracy and robustness for both linear and non-linear models.

3. This paper conducts too many experiments to show the effectiveness of their framework.

### Weaknesses
1. The paper’s abstract and introduction do not clearly convey the overall research idea and process, making it difficult to understand the framework. Specifically, the motivation for learning a transformation of the input data, rather than directly using the raw data for forecasting, is not well-articulated. The role of the 'proximity' constraint in the transformation process is also unclear, and the connection between this constraint and the goal of improved forecasting accuracy is not explicitly stated. It is difficult to grasp the core contribution of the proposed Proximal Transformation Network (PTN) from the initial sections.

2. The authors mention that PTN shows potential to make time series forecasting more interpretable. However, the enhanced embedding is latent, produced by deep learning. It is unclear how this actually enhances interpretability. The paper lacks a clear explanation of how the learned transformations, which are inherently complex and non-linear, can be interpreted in a way that provides meaningful insights into the underlying time series data. The claim of interpretability seems to be based on the visualization of the transformed data, but this does not necessarily translate to a deeper understanding of the forecasting process itself.

3. The authors provide a caption for the framework, but it does not help clarify the framework’s procedure. It's unclear how the transformed embedding is involved in enhancing the prediction task. The description of the framework lacks sufficient detail on how the transformed data is actually used by the forecasting model. It is not clear whether the forecasting model is trained on the transformed data alone, or if the original data is also used in some way. A more detailed explanation of the data flow within the framework is needed to understand the contribution of the PTN.

### Questions
See Weaknesses

### Soundness
3

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
This paper proposes a data transformation model to support long-term time series forecasting. Specifically, it first obtains a transformation of the raw data using Proximal Transformation Networks (PTNs) and then uses the transformed data to train a predictor. Each PTN consists of a convolutional encoder and a decoder with intra-patch attention, channel-wise attention, and a point-wise linear head. Experiments on several benchmark datasets are conducted to evaluate the effectiveness of the proposed model.

### Strengths
1. The idea is relatively novel and is supported by some theoretical insights.
2. Extensive experiments from various perspectives are provided.
3. The motivations behind the proposal are well introduced.

### Weaknesses
1. The comparison with baselines in Table 9 for look-back length 512 appears to be unfair. For instance, iTransformer should also use a look-back length of 512, and the results of PatchTST in this table are much worse than those reported in the PatchTST paper (PatchTST/64 in Table 3 of its paper).

2. The proposed model does not seem to perform well on complex datasets, such as Traffic. It would be beneficial to provide results on more complex datasets, such as the PEMS datasets used in the iTransformer paper.

3. It would be helpful to include Mean Squared Error (MSE) results in Table 4.

4. It seems inappropriate to claim that MoE is used without a gating network. Additionally, the method for selecting an appropriate number of PTNs, as well as the specific values used in the paper, is unclear.

5. There is no complexity analysis when adding the proposed model to the base models.

6. There are also many unclear points and typos in the paper, such as:

+
Figure 1 is not well explained, e.g., the meaning of "7/8".

+
It is unclear how the outputs of intra-patch attention and channel-wise attention are combined.

+
It is unclear how the prediction process is conducted after training. Should the raw data be directly input to the trained predictor?

+
"An attention-based Encoder" should be "An attention-based Decoder" on Page 2.

+
"Piece-wise Linear Head" should be "Point-wise Linear Head" in Figure 3.

### Questions
Same as the weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
