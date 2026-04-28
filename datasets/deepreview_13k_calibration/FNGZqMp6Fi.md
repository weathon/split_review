# MicroCrackAttentionNeXt: Advancing Microcrack Detection in Wave Field Analysis Using Deep Neural Networks through Feature Visualization.

- Decision: Reject
- Avg Score: 2.20
- Scores: 3, 3, 1, 3, 1

## Abstract
Micro Crack detection using deep neural networks(DNNs) through an automated pipeline using wave fields interacting with the damaged areas is highly sought after. However, these high dimensional spatio-temporal crack data are limited, moreover these dataset have large dimension in the temporal domain. The dataset presents a substantial class imbalance, with crack pixels constituting an average of only 5\% of the total pixels per sample. This extreme class imbalance poses a challenge for deep learning models with the different micro scale cracks, as the network can be biased toward predicting the majority class, generally leading to poor detection accuracy. This study builds upon the previous benchmark SpAsE-Net, an asymmetric encoder–decoder network for micro-crack detection. The impact of various activation and loss functions were examined through feature space visualisation using manifold discovery and analysis (MDA) algorithm. The optimized architecture and training methodology achieved an accuracy of 86.85\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MicroCrackAttentionNeXt, an advanced deep learning model designed to enhance microcrack detection in structural materials using wave field analysis. Traditional CNNs struggle with the complex spatio-temporal patterns and severe class imbalance (cracks constitute only 5% of data). The model uses an asymmetric encoder-decoder architecture with attention mechanisms, inspired by existing structures such as SpASe-Net, but optimized for micro-scale feature detection. The authors also explore the impact of various activation functions and loss strategies through Manifold Discovery and Analysis (MDA), aiming to improve feature separability and reduce overfitting. The proposed model achieves a significant accuracy of 86.85%, outperforming benchmark models in microcrack segmentation.

### Strengths
1. **Soundness of Claims:**
   - The study provides strong empirical evidence for the model's performance, demonstrated through experiments comparing *MicroCrackAttentionNeXt* against established benchmarks like 1D-DenseNet. The use of multiple activation and loss function combinations showcases the robustness of the approach.
   - The application of MDA for qualitative analysis adds depth to the understanding of the learned representations, illustrating the model's ability to separate complex features effectively.
   - The theoretical foundation, leveraging attention mechanisms and hierarchical feature extraction, is well-grounded in modern deep learning literature, enhancing the reliability of the results.

2. **Significance:**
   - The model addresses a critical problem in the field of structural health monitoring, where microcrack detection is vital for preventing catastrophic failures. The real-world implications of this work extend to various engineering applications, making it highly impactful.
   - The research introduces a nuanced solution to the issue of class imbalance, a common challenge in segmentation tasks, by experimenting with different loss functions tailored to emphasize minority classes.
   - The study's contribution lies in the integration of MDA, offering a new perspective on model interpretability and feature visualization, which can be valuable for future research in deep learning-based structural analysis.

3. **Novelty:**
   - The paper presents a novel architecture by combining a tailored asymmetric encoder-decoder design with specialized attention modules, enhancing the detection of small, complex features like microcracks.
   - The comprehensive analysis of activation functions, rarely explored in-depth in this context, brings a fresh approach to optimizing neural network performance for this task.
   - The proposed use of manifold analysis for qualitative feature evaluation is innovative and provides new insights into the model's inner workings, setting it apart from traditional performance metrics.

### Weaknesses
1. **Soundness of Claims:**
   - While the empirical results are compelling, the paper could benefit from a more extensive comparison with a broader range of models, including state-of-the-art transformer-based architectures, to validate the superiority of *MicroCrackAttentionNeXt*. The current comparison to 1D-DenseNet, while relevant, does not fully address the potential of other advanced architectures in this domain. A more rigorous benchmark would include models that also incorporate attention mechanisms or other techniques for handling spatio-temporal data, providing a more comprehensive performance evaluation.
   - The theoretical justification for the chosen architecture and specific configurations, such as the kernel sizes and pooling layers, lacks detailed mathematical support or ablation studies to isolate the effects of these choices. For example, the specific choice of kernel sizes in the convolutional layers and the number of pooling layers could be better justified with an analysis of their impact on feature extraction and computational cost. An ablation study systematically varying these parameters would strengthen the claims.
   - The MDA analysis, though informative, appears somewhat qualitative; incorporating more quantitative measures to assess feature separability could strengthen the argument. Metrics such as silhouette scores or inter-class distance could provide a more objective assessment of the feature space, making the analysis more rigorous.

2. **Significance:**
   - The model's performance improvement, while notable, is not groundbreaking when considering the field's rapid advancements. An increase from previous benchmarks may not justify the added architectural complexity. The reported 86.85% accuracy, while good, needs to be contextualized against the performance of other recent models, and the marginal improvement should be weighed against the complexity of the proposed architecture.
   - The study's reliance on synthetic data for training and validation could limit its applicability in real-world scenarios, as the dynamics of wave propagation in laboratory settings may differ from those in practical engineering contexts. The synthetic data generation process should be thoroughly validated against real-world data to ensure the model's robustness and generalizability.
   - There is a lack of discussion on how the proposed approach scales with larger datasets or more complex wave forms, which could limit its feasibility in extensive industrial applications. The computational cost and memory requirements for larger datasets should be analyzed, and the model's performance should be evaluated under more complex conditions.

3. **Novelty:**
   - Although the architecture is tailored for this application, many components are adaptations of existing methods, such as attention mechanisms and encoder-decoder networks. The paper does not significantly deviate from established deep learning paradigms. The specific combination of these components, while effective, does not introduce a fundamentally new approach to the problem.
   - The paper could explore more groundbreaking methodologies, such as incorporating graph-based networks for modeling wave propagation more naturally. Graph neural networks could potentially capture the underlying physics of wave propagation more effectively than standard convolutional approaches.
   - The novelty of using MDA is limited by the fact that it only provides interpretability benefits without contributing directly to performance enhancement. While interpretability is valuable, the MDA analysis does not directly improve the model's accuracy or efficiency.

### Questions
1. How does the model perform when tested on real-world datasets compared to synthetic wave field data?
2. Are there specific scenarios or material properties where *MicroCrackAttentionNeXt* performs poorly, and how can these be addressed?
3. Can the proposed model handle various noise levels in wave data, which are common in real-world applications?
4. What is the computational efficiency of the model during training and inference compared to simpler architectures?
5. How would the model's performance vary if it were extended to handle 3D wave propagation data?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the MicroCrackAttentionNeXt, a deep neural network model designed to enhance microcrack detection in materials using wave field data. Building upon SpAsE-Net, this model introduces an asymmetric encoder-decoder structure and leverages attention mechanisms to better capture spatio-temporal interactions critical for microcrack detection. Key elements include various activation functions and loss metrics, evaluated through the Manifold Discovery and Analysis (MDA) approach for feature visualization. The paper demonstrates that the combination of the Gaussian Error Linear Unit (GeLU) activation and Combined Weighted Dice Loss (CWDL) achieved optimal performance, resulting in an accuracy of 86.85%.

### Strengths
1.  The asymmetric encoder-decoder with attention mechanisms offers a promising approach to tackle the complexity of spatio-temporal data in microcrack detection.

2. The exploration of different activation functions and loss metrics provides valuable insights into model optimization for class-imbalanced data.

3. The application of MDA to visualize feature representations in higher dimensions is well-executed, giving a qualitative assessment of model behavior across layers and activation functions.

### Weaknesses
1. **Dataset and Class Imbalance**: The paper notes severe class imbalance, which could impact the generalizability of results. Although methods are employed to mitigate this, it remains a limitation without further exploration into data augmentation or synthetic generation techniques. The use of Combined Weighted Dice Loss (CWDL) is a step towards addressing the imbalance, but it does not fundamentally alter the distribution of the training data. The lack of data augmentation, particularly techniques that could introduce variations in crack morphology, orientation, and scale, is a significant oversight, potentially leading to a model that is overfit to the specific characteristics of the training set. This is especially concerning given the complex nature of microcrack patterns and the potential for significant variability in real-world scenarios.

2.  **Baseline Models**: While the paper references prior models, including SpAsE-Net, direct quantitative comparisons against other state-of-the-art microcrack detection models are limited, which may hinder assessing MicroCrackAttentionNeXt's performance gains. The absence of comparisons with established methods, particularly those that utilize different deep learning architectures or feature extraction techniques, makes it difficult to ascertain the true novelty and efficacy of the proposed model. A more comprehensive benchmark, including models that have demonstrated strong performance on similar tasks, would be necessary to validate the claims of improved performance.

3. **Resolution of Output Segmentation**: The paper mentions that the output segmentation suffers from low resolution, which may limit its applicability in scenarios demanding high-resolution segmentation for precise crack localization. This limitation is particularly problematic for applications requiring accurate crack geometry measurements, such as fracture mechanics analysis or material characterization. The low-resolution output may obscure fine crack details, leading to inaccurate assessments of crack length, width, and connectivity, which are crucial for understanding material behavior.

4. **Scalability and Computational Efficiency**: Although the model incorporates temporal downsampling to manage data size, the practical scalability of MicroCrackAttentionNeXt to larger datasets or higher-resolution scenarios could be further discussed. While temporal downsampling reduces computational load, it also potentially discards valuable temporal information that could be useful for crack detection. The paper lacks a detailed analysis of the trade-offs between computational efficiency and model performance, particularly with respect to the impact of downsampling on the accuracy of crack detection. Furthermore, the computational cost of the attention mechanisms, which can be significant, is not thoroughly addressed.

### Questions
1. **Model Generalizability Across Varying Conditions**: The dataset's severe class imbalance and limited temporal resolution are acknowledged but not adequately addressed. How can the authors justify the model’s generalizability in detecting microcracks under different material compositions or wave propagation scenarios, especially given the narrow dataset? Could this limit the model's application in real-world, diverse settings?

2. **Comparative Baselines**: Although the paper positions MicroCrackAttentionNeXt as an improvement over SpAsE-Net, it lacks direct quantitative comparison with a broader range of state-of-the-art models in microcrack detection. Without such comparisons, how can the authors substantiate claims of improved accuracy or efficiency?

3.  **Low-Resolution Segmentation**: The paper concedes that the segmentation output’s low resolution could lead to loss of detail in crack localization. Given this limitation, how does the model ensure precise identification of microcracks, particularly those close to the resolution limit? Could this restriction render the model ineffective for critical applications requiring high localization accuracy?

4. **Evaluation Metrics**: The paper predominantly relies on the accuracy and Dice Similarity Coefficient (DSC), but these may not fully capture the model’s capability in highly imbalanced, nuanced detection tasks. Why were more detailed metrics, such as precision-recall curves or area under the ROC curve (AUC), not included to provide a more comprehensive evaluation? Furthermore, was any statistical validation (e.g., confidence intervals) performed to ensure the robustness of the reported performance metrics?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In this paper, authors propose a MicroCrackAttentionNeXt model for the micro crack detection, and utilize a Manifold Discovery and Analysis (MDA) method to visualize the learned feature of the network.

### Strengths
The structure of this paper is clear.

### Weaknesses
This paper only applies an existing MDA method for the crack detection, and compares the performances of model with different activation and loss functions. It is lack of innovation. Additionally, the quantitative comparisons with other existing crack detection models are not provided.



### Questions
1. In Abstract, the motivation and innovation are not mentioned.
2. The advantage and disadvantage of the existing related works are not analyzed comprehensively. So, the motivation of this paper is not clear.
3. What is Figure X in Page 4? What is the relationship of MicroCrackAttentionNeXt model and Squeeze-and-Excitation layers in Page 5? Moreover, Figure 3-5 are not described in the paper.
4. The evaluation metrics are very important, but they are not mentioned in this paper. Since the quantitative detection results of the proposed MicroCrackAttentionNeXt and other state-of-the-art crack detection models are not given, it is difficult to define the contribution of this paper.
5. There are some grammatical mistakes, such as “The dataset presents a substantial class imbalance, with crack pixels constituting an average of only 5% of the total pixels per sample, this extreme class imbalance poses a challenge for deep learning models with the different micro scale cracks, as the network can be biased toward predicting the majority class, generally leading to poor detection accuracy.”

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study presents a network for crack detection using observed seismic data. An attention mechanism is incorporated to effectively map spatio-temporal data to spatial data. They compare accuracies across different loss functions for various crack sizes. The results demonstrate that the proposed method achieves satisfactory performance.

### Strengths
They considered the complex relationship between spatio-temporal seismic data to spatial detection result.

### Weaknesses
1. The experiments are insufficient, lacking an ablation study and visual comparisons.
2. The novelty is limited, as this work merely applies an attention-based network to crack detection.
3. No field tests are conducted, which raises concerns about the generalizability of the findings.
4. The dataset settings are unclear.

### Questions
How is the training dataset prepared? Is it collected from real data or generated synthetically?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This work presents a deep neural network architecture that is designed to output segmentation maps of micro cracks. Pixels that represent micro crack are scarce in the dataset (5%), so it is essential to deal with the class imbalance. This works extends the previous work 1D-DenseNet and presents improved performance results. In addition it offers MDA visualizations for its inner layers.

### Strengths
The paper written clearly and is easy to follow.
It offers an accuracy improvement from 83.68% to 86.85%.

### Weaknesses
1) The work is compared to only a single architectural alternative on a single dataset. The only comparison made is with the work that this study is heavily based on, and even this comparison is incomplete. What are the accuracies, DSC, and IoU in comparison to the other work? 
Please present a table or figure comparing accuracies, DSC, and IoU scores between the proposed method and the baseline.
Instead of extending the evaluation to different datasets or comparing it with other techniques, only a few ablation experiments were presented, focusing on different losses or activation functions. The authors are encouraged to evaluate/consider recent segmentation techniques or, at the very least, explain why recent architectures, such as those based on transformers, are excluded from the comparison. Recent segmentation techniques may have a much greater performance impact compared to the improvements derived from investigating different activation/loss functions.
For example, will an adaptation of SAM2 (or any other recent alternative) for your kind of data, might work?

1.5) It is stated in the related work that this study extends 1D-DenseNet and is heavily influenced by it, but it is unclear what the specific similarities are and what the extensions consist of. Additionally, it is not clear which modifications lead to the observed improvements.
It might be helpful if the authors provide a specific section or table that clearly outlines the similarities and differences between their proposed model and 1D-DenseNet, as well as explicitly linking each modification to its impact on performance.

2) While this work might contribute to scientific progress in the field of materials inspection, I couldn't identify any novelty in the field of machine learning. The work employs well-known components, such as convolutional layers and self-attention layers, in an architecture that is largely based on a previous work. It suggests using established loss functions and activation functions.

3) The use of MDA is not well explained. I don’t understand what contribution the MDA visualizations make. Specifically, how do they help to understand the model's inner workings or how it performs compared to other alternatives? Additionally, MDA evaluates the model based on another "black-box" DNN algorithm. Instead, a more concise approach would be to base the explanation on well-established metrics (such as DSC or accuracy) or straightforward visualizations from the model, such as attention maps, to demonstrate semantic understanding. From my perspective, simply demonstrating improved DSC or accuracy is more convincing for evaluating a segmentation model. This contrasts with what is stated in lines 77-78.

Technical Issues:

Line 205: "Figure X" needs to be specified.

A citation or definition for Squeeze-and-Excitation layers would be helpful.

Lines 50-53: The soundness of the claim is unclear. Your architecture also includes residual connections, and it’s not necessarily the case that UNet’s reliance on residual connections is the reason for its underperformance compared to attention layers.

Lines 66-69: The loss function description feels unnatural and could be presented more clearly.

Lines 340-347: I expected to see Focal Loss mentioned somewhere here.

### Questions
1) I did not understand whether 1D or 2D convolutional layers were used. If it is 1D, I don't understand the reason as the spatial data is 2D. 
If it is 2D, 1D is written in the conclusion.

2) What are the performance reports in the related work (lines 133, 143, 148)? Were all these tested on the same dataset and settings as this work? If so, you should present these comparison in the experiments section.

### Soundness
2

### Presentation
2

### Contribution
1
