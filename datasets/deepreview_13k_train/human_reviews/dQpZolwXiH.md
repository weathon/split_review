# Intrinsic Explainability of Multimodal Learning for Crop Yield Prediction

- Decision: Reject
- Scores: 3, 3, 3, 3, 6, 5

## Abstract
Multimodal learning enables various machine learning tasks to benefit from diverse data sources, effectively mimicking the interplay of different factors in real life events. While the heterogeneous nature of these modalities may necessitate the design of complex architectures, their interpretability is often overlooked. In this study, we leverage the intrinsic explainability of Transformer-based models to explain multimodal learning frameworks. We utilize the self-attention mechanism alongside model-specific feature attribution techniques, comparing these against post-hoc methods. Our detailed analysis focuses on the challenging task of crop yield prediction, exploiting the characteristics of the modalities and the data to aggregate local explanations at multiple levels. Our findings indicate that Transformers significantly outperform other architectures in yield prediction, making them well-suited for further intrinsic interpretability analysis. Among the modalities, satellite data emerged as the most influential but requires deeper layers for effective feature extraction due to its complex structure. Additionally, we observed that the Attention Rollout method is more robust than Generic Attention, aligns more closely with Shapley-based attributions and shows reduced sensitivity to minor input variations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on developing a model for crop yield prediction by exploring various model architectures and feature engineering to effectively create and merge feature representations from multiple modalities. The authors also experiment with different explainability techniques to analyze patterns between the model's internal representations and its predictions, specifically examining how these relate to the nature of each data modality.

### Strengths
The model development and analysis are thorough.

### Weaknesses
The paper lacks a clear novel contribution, as it primarily involves constructing a model for crop prediction and testing different model architectures and feature engineering methods. The authors identify a transformer-based architecture as the best-performing model and use various XAI methods, such as linear probes across layers and attention weights attribution, to investigate the relationship between internal representations and predictions based on data modality.

The experiments appear somewhat disjointed, with individual assumptions tested in isolation rather than in service of a coherent, high-level research question. Since the paper centres on explainability, it would be valuable to provide clear takeaways from these analyses, mainly to guide model builders, decision-makers, and practitioners in understanding the practical implications of the findings.

Overall, while the paper is sound, its contribution feels limited. It may be better suited for a more specialized venue focused on applied machine learning or exploratory studies rather than the conference's main track.

1. Lines 46–47: You state, "Intrinsic explanations are inherently more faithful and less prone to errors introduced by surrogate models." I am not sure about the truthfulness of this claim.  Could you provide references that support it?

2. What is the rationale behind comparing the attention-based attribution and Shapley Values? Are you treating SV as a ground truth for attribution?

3. Table 1: Given the close performance metrics, including standard deviations for each metric would help determine if there are statistically significant differences between model performances.

### Questions
1. Lines 46–47: You state, "Intrinsic explanations are inherently more faithful and less prone to errors introduced by surrogate models." I am not sure about the truthfulness of this claim.  Could you provide references that support it?

2. What is the rationale behind comparing the attention-based attribution and Shapley Values? Are you treating SV as a ground truth for attribution?

3. Table 1: Given the close performance metrics, including standard deviations for each metric would help determine if there are statistically significant differences between model performances.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This research paper explores intrinsic explainability techniques for multimodal learning, specifically focusing on crop yield prediction. The authors employ Transformer-based architectures to integrate diverse data sources, including satellite imagery, weather information, soil characteristics, and terrain data. The study evaluates various neural network designs, such as 1D-CNN, LSTM, ALSTM, and Transformer models. To interpret the model's decision-making process, the authors analyze learned representations across layers using linear probes, examine attention weight distributions within fields and across layers, and compare intrinsic attribution methods like Attention Rollout and Generic Attention with post-hoc techniques such as Shapley Values. The findings reveal that Transformer-based models not only excel in performance but also offer inherent interpretability benefits without sacrificing accuracy.

### Strengths
* This research paper presents a comprehensive analysis of a wide range of analytical approaches through a detailed ablation studies to compare various model architectures. Further, layer-wise analysis using linear probes provides insights into the evolution of learned representations across the model's depth.  Finally, exploration of attention weight distributions and comparison across multiple attribution methods is done.
* Evaluation on real-world data for three different crops results in direct applications in agriculture and remote sensing demonstrating that interpretability doesn't compromise performance.

### Weaknesses
 * Choice of baseline models can be improved. For example, ConvLSTM [1], STATT [2], 3D-CNN [3] seems more suitable for satellite image time-series data.
* The focus on a dataset from Argentina raises questions about generalizability to other regions and crop types. Including experiments on datasets from various geographic regions would strengthen the model's applicability and reliability.
* It would be better if the interpretability results are accompanied with hypothesis/explanations derived from the domain knowledge (field/agronomic knowledge). For example, the modality impact scores does not match with agronomic significance, which makes it difficult to trust the internal mechanisms of the model.
* The temporal layer-wise attention are hard to interpret, where there doesn’t seem to be any correspondence with growing/harvesting season of the studies crops. The authors did a commendable job of dissecting the modern deep learning architectures, however the results does not seem to provide any meaningful insights.

### Questions
1. Could you provide more validation of the interpretability results? For example, comparing the identified important temporal periods with known critical growth stages of crops?
2. The weighted modality activations and Shapley values show quite different results for modality importance. What's your hypothesis about these differences, and which method do you think is more reliable?
3. How do the interpretability results vary across different crops? Are there consistent patterns that align with known agricultural principles?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addressed a crop yield prediction task in a multi-modal learning setting using multiple types of data such as satellite images and weather information.
In some prediction models, the paper showed that a transformer-based model achieved better predictive accuracy. 
To understand the behaviors of the transformer model, it attempted to apply various existing explanation methods to the model.

### Strengths
- In the literature on crop yield prediction, efforts related to the explainability of this research may be novel.
- Comparative experiments and analyses have been conducted extensively.

### Weaknesses
 - The importance of the crop yield prediction task is not adequately stated. Therefore, the usefulness and impact of the analysis results are not conveyed. The paper does not sufficiently articulate why accurate crop yield prediction is a critical problem, especially given the computational resources required for complex models like transformers. The lack of a clear problem statement makes it difficult to assess the practical value of the presented explanation methods.
- The technical contributions of this research are unclear. Although the data may be unique, the prediction model and explanation methods used are existing techniques and appear to be merely applied to crop yield prediction. The paper does not demonstrate any novel adaptation or modification of the transformer architecture or the explanation methods (SVS, AR, and GA) to address the specific challenges of multi-modal crop yield prediction. The application of these methods seems to be a straightforward implementation without any significant technical innovation.

### Questions
- Compared to other studies on explainability in multimodal learning, where do you believe the novelty lies?
- Are you predicting the yields of the three types of crops in a multi-task manner? For the results in Table 1, what crop yield values are considered the ground truth for evaluation?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a framework based on Transformer models for crop yield prediction, emphasizing multimodal learning by integrating diverse data sources (e.g., satellite imagery, weather, and soil data) to improve prediction accuracy. A central contribution is the use of self-attention mechanisms within Transformers to achieve intrinsic interpretability, setting it apart from traditional post-hoc methods. The study finds that Transformer models not only enhance interpretability but also outperform other architectures in prediction accuracy.

### Strengths
- The paper introduces an original approach to crop yield prediction using Transformer-based models, a relatively novel application in this field. Its emphasis on intrinsic interpretability in multimodal learning stands out, offering a fresh alternative to the commonly used post-hoc methods in agricultural and environmental modeling.

- The methodology is robust, featuring extensive experimentation across multiple neural network architectures (e.g., LSTM, CNN, and Transformer) to identify the most effective model. Additionally, the study's comparative analysis of interpretability techniques—such as Attention Rollout, Generic Attention, and Shapley values—adds considerable depth, enhancing the understanding of the model’s interpretability from multiple perspectives.

- The paper is well-organized, with clear, accessible explanations of complex methodologies, complemented by visual aids that clarify the technical content and make intricate processes more intuitive for readers.

- The model’s capability to provide accurate, interpretable predictions at the sub-field level holds significant implications for agriculture, where trust in predictive models is crucial for effective decision-making.

### Weaknesses
 - Although the study compares Transformer models with LSTM, ALSTM, and CNN architectures, including more contemporary multimodal learning approaches could further enhance the analysis. For instance, comparisons with models such as Multimodal Variational Autoencoders or Multimodal Contrastive Learning frameworks would provide a more comprehensive evaluation of the Transformer's effectiveness relative to recent innovations in multimodal integration.

- The Transformer model, with its 109,345 parameters, demonstrates an improvement in R² from 0.41 (ALSTM’s performance) to 0.46 and a reduction in MAE from 2.00 to 1.90. However, this comes with a significant increase in model complexity compared to ALSTM’s 38,017 parameters. A discussion on the computational costs, including inference time and resource requirements, would offer a balanced view of the model’s practicality, especially in resource-constrained settings.

- While the authors focus on a qualitative evaluation of interpretability, the assessment could be strengthened by incorporating functionally-grounded evaluation metrics. Adding objective measures such as fidelity and sparsity would provide a more comprehensive and robust assessment of the model's interpretability.

- Testing the model's adaptability across various crops and regions would help demonstrate its robustness. Expanding the dataset to incorporate diverse agricultural contexts or conducting transferability experiments across different geographic regions would offer insights into the model's broader applicability and generalization capacity.

### Questions
The primary issues were outlined in the weaknesses section, but there are additional questions and suggestions:

- Providing a more detailed description of the preprocessing steps for each data type would significantly enhance the reproducibility and transparency of the approach.

- Could you elaborate on how you determined the optimal balance between model complexity (e.g., number of Transformer layers and parameters) and interpretability? Insights into this decision process would clarify the rationale for the chosen model configuration.

- Attention to formatting and typographical consistency would improve readability. For example, there is a missing reference link in line 1122 ("same procedure described in Section ??"). A careful review for similar issues would enhance the paper’s presentation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper assesses how varied interpretability and explainability techniques can be combined in a comprehensive approach to understand model-wise / layer-wise / time-wise / modality-wise behaviour of the learned model. In particular, it evaluates both representations and attention scores at the level of layers, compared to Attention Rollout and Generic Attention on each modality.

### Strengths
- This paper is well structured and understandable.
- It has thoroughly referred to related paper, both in establishing existing approaches and problem significance, and to corroborate the results of the study.
- Each of the interpretability evaluation provides visualisations, which can be leveraged to suggest either particularities of the model architecture or qualities of the data that might influence the model.
- The dataset used is very large, and authors make sure that the analysis benefit from geographical units within the dataset (fields, farm, subfields).
- A systematic analysis uses multiple techniques to analyze each model component individually or globally.

### Weaknesses
 - Only one dataset is used, with no variation on modalities or indicators within each modalities. Even within the dataset, the authors do not truly enter a discussion on concept drift between the different fields, despite observing variability. Time-wise drift is not evaluated, despite years going from 2017 to 2023. How generalizable the approach is to other regions and future years is unknown. The lack of diversity in the dataset limits the scope of the conclusions, as the observed model behaviors might be specific to the particular combination of modalities and indicators used. A more comprehensive analysis would require testing the approach on datasets with different modalities (e.g., weather data, soil composition) and indicators (e.g., different crop types, vegetation indices). Furthermore, the absence of a concept drift analysis is a major limitation, as the model's performance and interpretability might vary significantly across different fields and time periods. The authors should have explored the potential impact of spatial and temporal variations on the model's learned representations and attention mechanisms.
- Expert understanding is missing from the evaluation, hence several of the explanations that the authors provide about data influence on the model cannot be verified. Sections after lines 371, 416, 460, and 501 lack this expert confirmation on data behaviour. Additionally, assertion line 419 could have been verified experimentally by computing attention distributions on 5 days averages, or 5 days min and max, instead of daily series. This would require fitting a new model on the modified data. The interpretations provided by the authors regarding data influence on the model's behavior are speculative without expert validation. For instance, the authors should have consulted with agricultural experts to confirm if the observed patterns in attention scores align with known agricultural practices or environmental factors. The claim about the impact of daily series could have been strengthened by comparing attention distributions on aggregated time series, which would provide more robust evidence for the proposed explanation.
- No statistical significance, despite seemingly a lot of samples. If not samples (pixels), subfields could have been used to conduct statistical tests over distribution means. The lack of statistical analysis makes it difficult to determine if the observed differences in attention scores and representations are statistically significant or simply due to random variations. The authors should have performed statistical tests, such as t-tests or ANOVA, to compare the distributions of attention scores across different layers, modalities, and time periods. This would provide a more rigorous assessment of the model's behavior and allow for more reliable conclusions. The use of subfields as statistical units would have been a good approach to analyze the variability of the model's behavior.
- Despite actionability being mentionned in introduction, no such claims were produced in experiments. The paper introduces actionability as a goal, but fails to demonstrate how the proposed interpretability techniques can lead to actionable insights. The authors should have provided concrete examples of how the model's explanations can be used to improve agricultural practices, such as optimizing irrigation or fertilization strategies. Without such examples, the practical value of the proposed approach remains unclear.
- I could not find the corresponding code. Hence, this work cannot be considered as demonstration for comprehensive codebase on interpreting multimodal networks with transformer architecture.

### Questions
- 264: due to sampling, it is unclear if the training data from Transformer model training is used as test data for linear probing. This cannot be the case, to avoid evaluating overfit representations. Can this be confirmed?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper examines the intrinsic explainability of Transformer-based models for multimodal crop yield prediction, using satellite, weather, soil, and digital elevation map data. By focusing on explainability, the study addresses the challenge of understanding model decisions in agriculture. It uses self-attention layers to make predictions more interpretable and explores both intrinsic and post-hoc methods like Attention Rollout and Shapley values for feature attribution. The paper suggests that transformer models outperform alternatives like LSTM and CNN in yield prediction accuracy and interpretability, especially for satellite data, which was identified as the most influential modality.

### Strengths
The paper is well-written. The clarity in structure and flow makes complex concepts, such as the attention mechanism and the distinctions between interpretability methods, accessible.

The results indicate practical utility, with a focus on regions like Argentina and crops such as corn and soybean, making the findings potentially valuable for real-world applications in crop yield forecasting.

### Weaknesses
w1: The paper highlights discrepancies between the weighted modality activations and Shapley values for feature importance. For instance, soil features receive the highest weight with the regression head method (37.8%) but are less prominent in Shapley-based scores, which prioritize satellite data at 72.3% for corn yield predictions. This inconsistency can lead to ambiguity for practitioners who rely on model interpretation, as it’s unclear which modality consistently influences predictions. The lack of alignment between intrinsic and post-hoc methods raises concerns about the reliability of the explanations, especially given that the model's decisions are based on complex interactions between multiple input modalities. It is unclear if the model is truly leveraging soil data or if the high weight is an artifact of the regression head's architecture.

w2: The proposed model shows variability in capturing yield variance between different fields. In Field-B, where the Transformer model struggled, it still outperformed other architectures, yet error maps reveal inconsistencies in how yield variance is captured compared to Field-A. This suggests the model may not generalize well across varying field conditions, especially in geographically diverse regions. The error maps indicate that while the model can predict yield, it does not consistently capture the spatial patterns of yield variability within a field. This is a critical limitation, as understanding these patterns is important for precision agriculture applications.

### Questions
Q1: Given the varying significance of the satellite and weather data, could you provide more on how attention allocation informs actionable decisions for farmers or agronomists?


Q2: You use weather-based decision trees to identify high-attribution events. Could these temporal attributions be further refined to identify specific agricultural milestones (e.g., planting, harvesting)?

Q3: While this study is focused on crop yield, could the interpretability framework be adapted to other agricultural applications, such as disease detection or segmentation tasks?

### Soundness
3

### Presentation
3

### Contribution
2
