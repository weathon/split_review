# Leveraging Object Detection for Diverse and Accurate Long-Horizon Events Forecasting

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Long-horizon event forecasting is critical across various domains, including retail, finance, healthcare, and social networks. Traditional methods, such as Marked Temporal Point Processes (MTPP), often rely on autoregressive models to predict multiple future events. However, these models frequently suffer from issues like converging to constant or repetitive outputs, which limits their effectiveness and general applicability. To address these challenges, we introduce DeTPP (Detection-based Temporal Point Processes), a novel approach inspired by a matching-based loss function from object detection. DeTPP employs a unique matching-based loss function that selectively prioritizes reliably predictable events, improving the accuracy and diversity of predictions during inference. Our method establishes a new state-of-the-art in long-horizon event forecasting, achieving up to a 77% relative improvement over existing MTPP and next-K methods. Furthermore, DeTPP enhances next-event prediction accuracy by up to 2.7\% on a large transactions dataset and demonstrates high computational efficiency during inference.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors aim to address the issues of wrong matching and repetitive outputs in long-horizon events forecasting. This work transfers some ideas and architectures from the field of object detection to the events forecasting, achieving superior results. The authors have open-sourced their code, which enhances the reproducibility and data reliability of this work.

### Strengths
1. The authors have leveraged some advantages of DETR and adapted it to the events forecasting, addressing certain shortcomings of autoregressive methods and Next-K approaches.
2. The authors have open-sourced their code, which enhances the reproducibility of the paper.

### Weaknesses
1. Lack of innovation. The authors have adopted the Hungarian matching from DETR with minimal modifications and made few targeted improvements (see Q.1, Q.2).
2. There is a lack of comparison with some advanced methods. Certain recent works, such as ContiFormer$^{[1]}$, have not been mentioned or compared.
<!-- 3. Insufficient evaluation. Although the authors state in Section 2.3 (Line 125-126), "In this work, we use all mentioned metrics to assess the performance of our proposed method," they only utilize OTD and T-mAP. They do not employ MAE and MSE, both of which are also widely used metrics. -->

### Questions
1. The authors emphasize that an important difference between their method and DETR$^{[2]}$ is the introduction of alignment loss ($L_{BSE}$, Eq.(4)); however, this alignment loss does not seem significantly different from the first term $-log(\hat{p}_{\hat{\sigma}(i)}(c_i))$ in Eq.(2) of DETR. The main distinction is that DETR and its variants$^{[3,4]}$ treat "no object" as a special class, handling it equivalently to the trivial class when predicting logits. In contrast, this work separates "no event" from trivial events. If the authors consider this operation to be a key improvement, they should provide justification and corresponding experiments.

2. The authors use binary cross-entropy loss as the alignment loss, but many DETR-like methods$^{[3,4,5,6]}$ consider Focal Loss$^{[7]}$ to be more suitable because, during the decoding process, the number of positive samples is typically much smaller than that of negative samples. Using BCE loss may lead the model to be more inclined to classify samples as negative. Why was Focal Loss not used in this work? Generally, what is the ratio of positive to negative samples among the K predictions of this method?

3. What does the "conservative probability estimation" in Section 4.4 refer to? Does it mean that the probability of classifying samples as negative is higher?

4. The most recent method compared to this work is from 2022. Why is there no comparison with the latest methods, such as ContiFormer$^{[1]}$? 

5. Figure 1(c) requires more clarification. What do the different shapes and colors represent? In the three rows of legends for each method, what does each row represent—ground truth, predictions, or do all three rows together form a single output?

6. The authors highlight the generation of more diverse outputs as an advantage and provide some qualitative analysis. However, a more in-depth theoretical explanation of why the DeTPP loss enables the generation of diverse outputs is needed.

[2] Carion, Nicolas, et al. "End-to-end object detection with transformers." European conference on computer vision. Cham: Springer International Publishing, 2020.
[3] Zhang, Hao, et al. "Dino: Detr with improved denoising anchor boxes for end-to-end object detection.".
[4] Zhu, Xizhou, et al. "Deformable detr: Deformable transformers for end-to-end object detection." 
[5] Shi, Dahu, et al. "End-to-end multi-person pose estimation with transformers." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.
[6] Yang, Jie, et al. "Explicit box detection unifies end-to-end multi-person pose estimation."
[7] Ross, T-YLPG, and G. K. H. P. Dollár. "Focal loss for dense object detection." proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Long-horizon event forecasting is critical in various domains such as retail, finance, healthcare, and social networks. Traditional methods like Marked Temporal Point Processes (MTPP) often rely on autoregressive models, which can converge to constant or repetitive outputs, limiting their effectiveness. To address these issues, we introduce DeTPP (Detection-based Temporal Point Processes), a novel approach inspired by object detection techniques from computer vision. DeTPP uses a unique matching-based loss function that prioritizes reliably predictable events, improving prediction accuracy and diversity. This method achieves up to a 77% relative improvement over existing MTPP and next-K methods and enhances next event prediction accuracy by up to 2.7% on a large transactional dataset. Notably, DeTPP is also among the fastest methods for inference.

### Strengths
The paper's innovative approach, DeTPP, addresses the unique challenges of long-horizon event forecasting by leveraging a novel matching-based loss function and parallel prediction. This results in significant improvements in prediction accuracy, diversity, and efficiency, making it a valuable tool for various real-world applications.

### Weaknesses
 - DeTPP relies on a fixed horizon size, which is selected based on the hyperparameters of the OTD (Optimal Transport Distance) and T-mAP (Temporal Mean Average Precision) metrics. This fixed horizon size can be a limitation because changes in the evaluation metric typically require adjusting DeTPP’s parameters. Specifically, the method's performance is intrinsically tied to the chosen horizon length, and there's a lack of discussion on how to adapt the model when the desired prediction horizon changes, which is a common scenario in real-world applications. The paper does not explore the sensitivity of the model to different horizon lengths, which could reveal potential weaknesses or limitations.

- The paper does not provide detailed explanations of the evaluation metrics used, such as T-mAP (Temporal Mean Average Precision). This lack of detail can make the paper feel disorganized and less accessible to readers who are not familiar with these metrics. Including clear definitions and explanations of the metrics would enhance the clarity and readability of the paper. For example, you could add a separate paragraph in Section 5 to introduce the metrics you used and the meanings of the abbreviations in your paper. You can consider using a comparison table for clarity. The absence of a formal definition of T-mAP, including its mathematical formulation and how it differs from standard Average Precision, makes it difficult to fully assess the significance of the reported results. Furthermore, the paper does not discuss the potential biases or limitations of using T-mAP for evaluating long-horizon event forecasting.

- The writing style of the paper is somewhat informal, which can detract from its academic rigor and professionalism. The main text of the entire article does not reach 10 pages. The introduction in Section 2 (Related Work) lacks a coherent narrative. The evaluation part does not need to be a separate subsection; it can be integrated into the discussion of different models. In addition, the subheadings in Section 2 are not parallel in nature. The lack of a clear narrative in the related work section makes it difficult to understand the context and motivation for the proposed method. The paper would benefit from a more structured and formal presentation of the related work, highlighting the gaps that DeTPP aims to address.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Paper proposes a novel event forecasting method which predicts multiple events in parallel. Most tradtional methods predict events in sequences. This can lead to error propogration and other issues, like over-uniformity. The method claims to be inspired by transformer-based object detection methods. There are several enhancements/variants of the approach to address different limitations of the base model. The experimental results compare favourably with many SOTA methods.

### Strengths
1. Paper proposes a novel method to predict long horizon events in parallel and obtain good empirical results.
2. The loss function design is sound and logical.
3. From the experimental results, the proposed base method appears to have overcome some limitations of existing SOTA. In Table 2, the method outperforms 6 other methods 9 out of 10 comparisons (5 datasets with 2 metrics: OTD/T-mAP)
4. There are several enhancements/variants of the base method to address the limitations of the original model.

### Weaknesses
1. Paper is difficult to read for readers without much background in this problem. For example, Line 258-259, "We set the horizon H to align with that of the T-mAP metric, ensuring consistency in evaluation." It's not clear how a hyperparameter can be "aligned" with the metric. Does this mean that different H value were experimented on, and the H value is set based on the best T-mAP?

2. The enhancements/variants appears to be ad-hoc. This can be seen in Table 3. The empirical results are mixed for the different datasets. There is no clear advantage of one variant over the rest. Each variant appear to be empirical tweaks and not designed based on sound theorical principles.

3. (minor) The paper's main claim that the method is inspired by object detection method. But there is no single object detection approach. Object detection is still an open research problem and there are other competing methods, besides transformer-based approach. In fact, the paper only cited one reference (Carion et al, 2020). Further, the paper does not mention exactly which part of their proposed method is directly inspired by Carion et al. The reader has to read between the lines and be quite familiar with Carion et al paper to draw their inference of the inspiration.

### Questions
1. Please consider if all variants are necessary to demonstrate the strengths of the proposed approach. As of the current state of the paper, the variants are actually diluting the core contribution by introducing unnecessary tweaks and make the paper difficult to read and appreciate. I suggest the paper to introduce DeTPP+ as the base model and performs ablation study with ablated model like DeTPP. 

2. The exclusion of the other variants can free up space to elaborate on the experimental setup design. In the current state of the paper, the Section on the various parameters values is too brief. The Calibration process also appears to be a key component of the proposal and should be left in the main paper, rather than in the Appendix.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper highlights key limitations of autoregressive models in long-horizon prediction, including error accumulation over time, which results in repetitive or constant outputs, and limited inference parallelism due to dependency on previous predictions. To overcome these issues, the authors propose DeTPP, a novel model inspired by object detection techniques that can predict multiple future events in parallel. DeTPP introduces a matching loss function that bypasses some events and focuses instead on accurately predicting more reliable ones. This approach achieves state-of-the-art performance in long-horizon forecasting, outperforming both autoregressive and next-K models. Additionally, an extension that integrates elements of traditional methods with DeTPP enhances next-event prediction quality, especially on large datasets like Transactions

### Strengths
The paper archives competitive results on multiple datasets for event forecasting. Additionally, it shows improved inference speed over most of the evaluated datasets. The proposed method exhibits greater diversity in its predictions.

### Weaknesses
The paper has several significant issues regarding method novelty, presentation, and experimental design.

**1. Methodology**
- **Lack of Novelty**: The paper’s claimed contributions to method development are unclear, as it appears to simply modify next-K models (Karpukhin et al., 2024). Thus, the claim of addressing autoregressive limitations in long-horizon prediction may not be entirely valid. Limited inference parallelism is inherent to autoregressive models and doesn’t represent a distinct limitation of previous methods; replacing the autoregressive model naturally addresses this issue to some degree. I suggest the authors explain how their approach differs from or improves upon next-K models in addressing autoregressive limitations. Specifically, the core novelty regarding the matching of predictions to ground truth events is not clearly articulated, and the connection to the specific loss function is not well explained. The paper needs to clarify how the matching process and the loss function contribute to improved performance compared to standard next-K models.
- **Object Detection Inspiration**: Although the authors claim that DeTPP (Detection-based Temporal Point Processes) is inspired by object detection techniques in computer vision, they don’t provide a clear rationale for why these techniques are beneficial in this context. The paper lacks a detailed explanation of how concepts like bounding box regression or non-maximum suppression, common in object detection, are adapted or replaced in the temporal point process setting. A discussion on the specific parallels and adaptations from object detection to event sequence prediction would strengthen this claim.
- **Method Description**: The method section is incomplete and lacks structure. It begins with “4.1 Probabilistic Event Model,” describing loss functions without first introducing input and output notations. Key details, like the neural network used, are missing. If the model only includes what is described in Section 4.3, what does “Backbone” represent in Figure 2? Furthermore, there’s no explicit mention of object detection inspiration within the methodology. The description lacks a clear definition of the input event sequence format, the output prediction format, and the specific transformations applied to the input data before it enters the model. The architecture diagram in Figure 2 is not sufficiently detailed, and the flow of information through the network is unclear.

**2. Experimental Design**
- **Missing Ablations**: Several important ablation studies are missing, including:
  - The impact of the losses outlined in Sections 4.1 and 4.2. Specifically, there is no analysis on how the individual loss components contribute to overall performance, such as the matching loss, the classification loss, and the time prediction loss. A breakdown of the contribution of each loss component is needed.
  - The effect of adjusting the loss weights. Without this, it is difficult to understand the sensitivity of the model to different loss weight configurations and whether the chosen weights are optimal.
  - The influence of model architecture choices, such as alternative methods for combining Queries and Embeddings (e.g., cross-attention) as seen in Figure 3. The paper should explore other architectural choices to justify the current design. For example, the use of a simple concatenation versus cross-attention should be evaluated.
  - An ablation study on the number of queries. The impact of varying the number of prediction heads on model performance is not clear.
- **Performance on Next-Event Prediction**: Section 5.2 points out that the model struggles with next-event prediction. Even with the addition of the IFTPP loss function, results (Figure 4) on datasets like StackOverflow, Retweet, and MIMIC-IV show little improvement over the IFTPP method, suggesting limited effectiveness in this regard. The paper does not offer a clear explanation for why the model struggles with next-event prediction despite the inclusion of the IFTPP loss. It's not clear whether this is due to the model architecture or the training procedure.

**3. Inference Speed**
- **Variation in Requests Per Second (RPS)**: The Requests Per Second (RPS) for sequence generation varies across datasets, as shown in Figure 6. The proposed method is the fastest on all datasets except Transactions, which is slower than IFTPP. The authors attribute this to computational overhead related to the prediction head but don’t explain why this issue affects only the Transactions dataset. The authors could offer a more detailed explanation of why the computational overhead of the prediction head impacts the Transactions dataset differently than the other datasets. It would be beneficial to analyze the specific characteristics of the Transactions dataset that cause this performance bottleneck, such as the sequence length, event density, or feature dimensionality, and how they interact with the prediction head.

### Questions
See weakness.

### Soundness
2

### Presentation
1

### Contribution
1
