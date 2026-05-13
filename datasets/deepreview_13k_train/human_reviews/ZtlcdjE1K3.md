# DECOUPLE QUANTIZATION STEP AND OUTLIER-MIGRATED RECONSTRUCTION FOR PTQ

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Post-training quantization (PTQ) is a popular technique for compressing deep learning models due to its low cost and high efficiency. However, in some extremely low-bit settings, PTQ still suffers from significant performance degradation. In this work, we reveal two related obstacles: (1) the setting of  weight's quantization step has not been fully explored, and (2) the outlier activation beyond clipping range are ignored in most methods, which is especially important for lightweight models and low-bit settings. To overcome these two obstacles, we propose \textbf{DOMR}, to (1) fully explore the setting of weight's quantization step into five cases through \textbf{D}ecoupling, based on the ignored fact that integer weight (different from integer activation) can be obtained early before actual inference deployment, (2) save outliers into the safe clipping range under predefined bitwidth with \textbf{O}utlier-\textbf{M}igrated \textbf{R}econstruction, based on the nature of CNN structure and PTQ's clipping operation. More outliers saved equals to breaking the bitwidth shackle of a predefined hardware thus brings better performance. Extensive experiments on various networks demonstrate that DOMR establishes a new SOTA in PTQ. Specifically, DOMR outperforms the current best method by 12.93\% in Top-1 accuracy for W2A2 on MobileNet-v2. The code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method for improving the performance of Post-training Quantization (PTQ). The authors identify two key obstacles to overcoming the performance drop of PTQ in extremely low-bit settings: (i) Separate quantization step-size scale factors for weight tensor. The authors propose a method called DOMR, which decouples the scale factors of weights at quant/dequant processes, considering the fact that integer weights can be obtained early in the process before actual deployment. (ii) Handling outliers: Most existing methods ignore outliers in model activations that fall outside the clipping range, particularly in lightweight models and low-bit settings. The authors introduce a technique called Outlier-Migrated Reconstruction to save outliers within a pre-defined bitwidth. The experimental results demonstrate that DOMR outperforms existing methods and establishes a new state-of-the-art approach in PTQ. Specifically, it achieves a 12.93% improvement in Top-1 accuracy for the W2A2 configuration on MobileNet-v2. The authors also mention that they will release the code associated with their work, which is rather important considering the complexity of the proposed method.

### Strengths
- The paper is exceptionally well-crafted, featuring clear and insightful illustrations that greatly aid readers in comprehending the presented concepts. 
- The authors conducts sufficient experiments. 
- The authors provide intriguing and valuable insights, particularly in the idea of enhancing both weights and activations quantization. The decoupling of weight step-sizes for optimization is a noteworthy contribution, and the notable performance enhancements achieved by introducing a single additional step-size in each layer is quite interesting.

### Weaknesses
 - The paper would benefit from improved clarity in its notations. The use of variables such as w_l, w_u, x_l, and x_u in Equation 2 is not well-defined. It's crucial for the authors to provide clear explanations and definitions for these lower and upper bounds of weights and activations, specifically detailing how these bounds are determined and their relationship to the quantization process, especially in the context of different activation functions.
- The authors base their Outlier-Migrated Reconstruction (OMR) method on the assumption that the activation function is ReLU. However, it's essential to discuss the applicability of OMR to models that use non-ReLU functions. For instance, MobileNetV3 employs h-swish, and ViT utilizes GeLU. A more comprehensive discussion about the adaptability of OMR to such activation functions, including specific modifications or limitations, is needed. The paper should also address how the outlier migration strategy would be adapted for activations that can be both positive and negative, not just positive like ReLU.
- The paper mentions that OMR involves duplicating channels for both weights and activations. This duplication may introduce additional computational overhead, but the paper lacks an in-depth analysis of this aspect. Providing a more detailed examination of the computational costs, including a breakdown of the increased memory access, FLOPs, and potential impact on latency, is crucial. A comparison with other methods in terms of computational cost would also be beneficial.
- The inclusion of an overall cost breakdown in Table 11 is appreciated. However, it would be even more informative if the authors could provide a specific breakdown of the runtime costs associated with Quant Time in the Fake Quantization process. This would offer a more granular view of the computational expenses involved in the proposed method, contributing to a deeper understanding of its practical implications. This breakdown should include the time spent on each sub-step of the fake quantization process, such as the initial step-size calculation, outlier identification, and the actual fake quantization operation.

### Questions
It seems that using decoupled step sizes for weights can also generalize to quantization-aware training, have the authors experimented with this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the Post-training quantization (PTQ) of deep learning models. Two main methods are proposed for weight and activation PTQ. For weight PTQ, DJOS is proposed to use a fixed quantization step for quantization and a learned step size for de-quantization. For activation PTQ, Outlier-Migrated Reconstruction (OMR) is proposed to split a channel into multiple channels to solve the outlier activations. The proposed methods are evaluated on ImageNet task and COCO task across various networks and bitwidth settings.

### Strengths
1. The authors fully explore different settings of weight’s quant-step into five cases, and study the performance of different settings.
2. The Outlier-Migrated Reconstruction is straight-forward and effective for PTQ given a pre-defined bit-width.

### Weaknesses
1. My main concern is about the novelty. The proposed Outlier-Migrated Reconstruction is well studied by previous works [1].
2. It is hard for me to understand why DJOS works. If the quant-step is fixed and the dequant-step is learnable, it is the same with the learning process of BN. In other words, network quantization with BN has already a mechanism of learned dequant-step.
3. In the experiments, the baselines of different methods are not the same, making the comparison unfair.
4. It is better to study weight-only quantization (DJOS) and compare with previous methods to evaluate the effectiveness of DJOS.

### Questions
1. What's the performance of weight-only quantization using the proposed method?
2. Which pretrained models are used as baseline?
3. Could you provide the detailed quantization algorithm?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
PTQ (Post-Training Quantization) is a technique that exports a pre-trained full precision neural network into low-bit. It is a promising way to reduce size of neural networks and costs of inference. However, PTQ can cause accuracy degradation with extremely low-bit settings. To solve this problem, the paper proposes two methods that are for improving PTQ process. 

In the quantization process, weight parameters of a target network are quantized before inference. The paper tackles that there isn’t any previous work that focuses on how to quantize weight parameters better. With a simple yet clear experiment, the paper shows that decoupling quant step and dequant step, and fine-tuning dequant step only lead to performance gain. In addition, the paper points out that outlier activation values that are clipped out after quantization affect performance a lot. To utilize these outlier values, the paper proposes OMR (Outlier-Migrated Reconstruction) that adds several channels to filters and operates them with outlier values which are shifted into safe clipping ranges. It has the same effect as increasing the number of bits.

The paper surpasses other previous works only with the decoupling quant step and dequant step. In addition, with OMR, the paper shows that higher accuracy can be obtained by sacrificing efficiency.

### Strengths
- The paper explains the proposed method well with several figures and formulas.
- The paper shows performance improvement with simple methods that are easy to follow.
- The paper presents various experiments for presenting the efficiency of the proposed method.

### Weaknesses
 - OMR leads to enlarging the size of neural networks. Therefore, the application of the proposed method can be limited. However, the paper doesn’t provide analysis in terms of costs which helps in understanding the trade-off between the size of a model and its performance.
- It doesn’t seem appropriate that the arrangements and citations of figures and tables. For instance, the first citation of Figure 2 is on page 2, and Figure 2 is on page 5.

### Questions
- In Outlier-Migrated Reconstruction, how can the sensitivity of each channel be measured, if only a portion of channels will be added?
- It seems that OMR is designed to mitigate outlier of activations and outlier of weight parameters can’t be utilized with this method. Does OMR help mitigate outlier of weight parameters?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
