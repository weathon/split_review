# Invariant Convolutional Layers for Time Series

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Machine learning for time series has recently garnered considerable attention. Indeed, automatically extracting meaningful representations from large and complex time series data is becoming imperative for several real-world applications. Neural architectures tailored to time series are often built upon sequential modules, such as convolutional, commonly employed in text or vision. Unfortunately, the potential of standard layers in capturing invariant properties of time series remains relatively underexplored. For instance, convolutional layers often fail to capture underlying patterns in time series inputs that encompass strong deformations, such as linear trends. However, invariances to some deformations may be critical for solving complex time series tasks, such as classification, while guaranteeing good generalization properties.
To address these challenges, we mathematically formulate and technically design efficient *invariant convolutions* for specific group actions applicable to the case of time series.
We construct these convolutions by considering two sets of deformations commonly observed in time series, including (i) *offset shift and scaling* and (ii) *linear trend and scaling*.
We further combine the proposed invariant convolutions with standard (or variant) convolutions in a single embedding layer of an example architecture, the so-called *InvConvNet* method, and showcase the layer capacity to capture complex invariant time series properties.
Finally, *InvConvNet* is experimentally proven to achieve superior performance against common baselines in relevant time series tasks, including classification and anomaly detection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces INVCONVNET, a novel approach addressing time series analysis through mathematically-grounded invariant convolutions. The authors formulate a theoretical framework for handling common deformations in time series data, specifically targeting offset shifts, scaling, and linear trends. The key technical contribution lies in their construction of group action-based invariant operations, which they effectively combine with standard convolutions in a hybrid embedding layer. The work bridges theoretical foundations of invariant representations with practical architectural design, demonstrating applications in both classification and anomaly detection tasks. The authors provide mathematical formulations of their invariant convolutions and validate their approach experimentally against baseline methods.

### Strengths
1. Theoretical Foundation: The authors provide formal mathematical definitions of time series deformations in terms of group actions, creating a theoretically sound framework rather than just an empirical solution.
2. Structured and Explicit Design: Rather than relying on implicit learning of invariances through data augmentation or contrastive learning, they develop an explicit, structured approach to incorporating invariance properties directly into the architecture. This makes the solution more transparent and controllable.
3. Practical Problem with Clear Motivation: They demonstrate their approach through concrete examples like the ECG case, where standard convolutions fail with linear trends masking important patterns, showing clear real-world applicability.

### Weaknesses
- Fixed Kernel Bias: The initial motivation using a pre-defined kernel creates a biased comparison, without adequately addressing whether standard CNNs with learned kernels could naturally adapt to these deformations.
- Missing Comparative Analysis with Contrastive Learning: The authors don't compare their architectural approach against the simpler alternative of using these deformations (offset, trend) as augmentations in a contrastive learning framework, which could potentially achieve similar invariance properties with more flexibility.
- Incomplete Novelty Justification: The paper lacks proper positioning against existing relevant work on invariant architectures, particularly:
    - Jacques, Brandon G., et al. "A deep convolutional neural network that is invariant to time rescaling." *International conference on machine learning*. PMLR, 2022.
    - "Truly shift-invariant convolutional neural networks" A comparison with these works is crucial to establish the novelty and advantages of their approach.
- Contradictory Results to Core Motivation: The paper's fundamental premise is that invariance to deformations (offset, trend) is crucial for time series analysis. However, Table 3 directly contradicts this claim, showing InvConvNet-N (without invariance) performs best in 3 out of 4 clean datasets. This raises serious questions about the paper's core motivation and the necessity of architectural invariance.

### Questions
Check the Weakness Section

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tackles the challenge of developing invariant convolutional layers tailored for time series. It begins by introducing a mathematical framework for invariant convolution in time series, followed by the design of specific architectural blocks that ensure invariance to offset shifts, scaling, and linear trends. These invariant blocks are then integrated with convolutional layers. The proposed approach is evaluated through experiments on both univariate and multivariate time series, covering tasks such as classification and anomaly detection.

### Strengths
- S1. The paper addresses the compelling problem of designing invariant deep learning models for time series, which is valuable for tasks where invariance to certain properties, such as offset, is essential. This is particularly relevant in applications like classification, where only specific patterns are informative. 

- S2. Additionally, the paper explores a relatively uncharted area of geometrical deep learning for time series, providing valuable insights into this underdeveloped research area. 

- S3. The appendices are thorough and greatly enhance the reader’s understanding of the model architecture and the processes used in the supervised tasks, especially Appendix A.2 ("InvConvNet: Architectural Details"), which contains essential architectural details. 

- S4. The experimental evaluation is comprehensive, covering two key supervised tasks (classification and anomaly detection) and providing a broad perspective on the model’s performance.

### Weaknesses
- W1. The positioning of the work is somewhat unclear, as it focuses exclusively on specific invariance properties for time series without connecting to the broader research in convolutional neural network invariances. Invariance is a well-studied area in deep learning (e.g., CNN shift-equivariance, see [1]), and discussing this literature could enrich the context and impact of the paper. 
- W2. The paper is challenging to follow: 
    - The extensive two-page mathematical formalism on invariant embeddings for time series may not aid reader comprehension as intended.
    - The architecture description lacks clarity; key elements are dispersed and essential components are placed in the appendices (such as in Appendix A.2), making it difficult to grasp the model’s structure. Reorganizing and detailing the architectural explanations would enhance readability. 
    - Consider moving the content of Appendix A.2 to the main body and placing the formalism of invariant embeddings in the appendix to streamline the presentation of contributions. 
 
- W3. The experimental results are not stellar. In the classification tasks, the InvConvNet model does not significantly outperform ResNet and Rocket on the UEA archive datasets (Table 1 and Table 9). Furthermore, on four selected UCR datasets, InvConvNet performs worse than its variant without invariant blocks (Table 3), despite showing some robustness to deformation. 
- W4. The practical value of the proposed InvConvNet architecture is unclear. It may be beneficial to focus on specific datasets where invariance to offset and trend is particularly desirable, which could demonstrate the model's relevance in applied scenarios.

### Questions
- Q1. The description of the Transfer Learning Experiment is unclear. Could you provide a more detailed explanation of this experimental setup ?

- Q2. Could you please discuss other invariance like shift invariance?

- Q3. Could you address the concerns raised in the weaknesses section ?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach to handling time series data by developing convolutional layers that are invariant to specific types of deformations commonly found in time series, such as offset shifts, scaling, and linear trends. The author mathematically formulate invariances for time series using group theory, designed invariant convolutions that can handle these deformations. The effectiveness of the proposed method is empirically validated through classification and anomaly detection tasks.

### Strengths
1. The overall paper is clearly written and easy to understand, the paper structures are well organized.

2. The mathematical formulation standardize the invariant definition for certain time series properties

3. Efficient implementation of invariant convolutions using FFT

### Weaknesses
1.	My major concern is the gap from theoretical definition of time series invariants to the actual empirical improvement on time series tasks. For CNN base time series model, the major factor to improve classification task performance is tuning multi-scale convolution kernel sizes (check paper: https://arxiv.org/abs/2002.10061). This reviewed paper seems also using this “Pool of convolutions” (line 302). Without more detailed ablation studies for each of the components, it is hard to justify where the actual contribution come from.

2.	Following the above discussion, for time series classification tasks, the SOTA models are still cnn based not transformer based. Therefore, it is more meaningful to use cnn based time series models such as TimeNet or Omni-scale CNN as baselines instead of transformer based models.

3.	The invariant convolution layer implementation is not very clear. Upon checking the appendix, there still lacks a detailed description of neural network architectures such as layer number/ kernel size for each specific layer.

### Questions
1.	How does the choice of kernel sizes affect the model's ability to capture different types of invariances? Is there a systematic way to select optimal kernel sizes based on understanding of “invariants”?

2.	Can you show some quantitative results that the computation efficiency gain of FFT-based convolution layer over classical kernel with longer time series?

3.	How is the proposed new invariant feature linked to/different from some standard normalization treatments in ML? i.e. the example in line 256 looks like very similar to kernel normalization.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a new type of convolutional neural network layer, invariant convolutional layers, which are designed for time series data. The layer can capture invariant features by taking into account common deformations in time series, such as shifts, scaling, and linear trends. This paper proposes an architecture called INVCONVNET, which combines standard and invariant convolution to improve the performance of time series classification and anomaly detection. The experimental results show that INVCONVNET outperforms existing baseline methods on multiple datasets with better generalization and computational efficiency.

### Strengths
This paper contains a large number of mathematical proofs, showing that convolution can capture time series invariance, and sufficient experiments in time series classification and anomaly detection demonstrate the importance of the proposed invariant convolution.

### Weaknesses
The INVCONVNET model presented in the paper, while excellent at time series classification and anomaly detection tasks, may have some limitations.Among the existing methods for capturing time series invariance, linear models and frequency-domain models （Dlinear and FITS) perform well and are not compared with them in this paper.

### Questions
1.The time series itself contains variable features and time invariant features, so why design only for time invariant features?
2.As the conversion of time series to frequency domain proves to be a suitable method for capturing time-invariant features, why does this paper not consider converting time series to frequency domain for learning by convolution first?
3. I find that there are many research about Time-invariant convolution,please further clarify the contribution of this article
[1]. Chaman, A., & Dokmanic, I. (2021). Truly shift-invariant convolutional neural networks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 3773-3783).
[2].Chen, X., Cheng, Z., Cai, H., Saunier, N., & Sun, L. (2024). Laplacian convolutional representation for traffic time series imputation. IEEE Transactions on Knowledge and Data Engineering.

### Soundness
3

### Presentation
3

### Contribution
3
