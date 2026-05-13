# Unleashing the Potential of ConvNets for Query-based Detection and Segmentation

- Decision: Accept
- Scores: 8, 8, 5, 6

## Abstract
Transformer and its variants have shown great potential for various vision tasks in recent years, including image classification, object detection and segmentation. 
Meanwhile, recent studies also reveal that with proper architecture design, convolution networks (ConvNets) also achieve competitive performance with transformers, \eg, ConvNeXt. 
However, no prior methods have explored to utilize pure convolution to build a Transformer-style Decoder module, which is essential for Encoder-Decoder architecture like Detection Transformer (DETR).
To this end, in this paper we explore whether we could build query-based  detection and segmentation framework with ConvNets instead of sophisticated transformer architecture.
We propose a novel mechanism dubbed InterConv to perform interaction between object queries and image features via convolutional layers. 
Equipped with the proposed InterConv, we build Detection ConvNet (DECO), which is composed of a backbone and convolutional encoder-decoder architecture. We compare the proposed DECO against prior detectors on the challenging COCO benchmark.
Despite its simplicity, our DECO achieves competitive performance in terms of detection accuracy and running speed. Specifically, 
with the ResNet-18 and ResNet-50 backbone, our DECO achieves $40.5\%$ and $47.8\%$ AP with $66$ and $34$ FPS, respectively. The proposed method is also evaluated on the segment anything task, demonstrating similar performance and higher efficiency.
We hope the proposed method brings another perspective for designing architectures for vision tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an InterConv mechanism to facilitate interaction between object queries and image features via a convolutional layer, resulting in the Detection ConvNet (DECO). DECO is composed of a backbone and a convolutional encoder-decoder architecture. Results on COCO detection demonstrate that DECO achieves a decent accuracy-speed trade-off.

### Strengths
- The DECO method requires only standard convolutions, making it computationally efficient and more compatible with low-end AI chips compared to DETR-based methods.

- The designs of self-interconv and cross-interconv are extremely simple and effective, indicating that the paper captures the essence of DETR and presents an elegant pure-conv replacement.

### Weaknesses
 - Clarity: In the method section, the Fusion operation is crucial; however, the paper fails to discuss it adequately. In the experiment section, the paper presents different fusion methods and query map upsampling strategies, but they remain unclear. These important details should be clearly stated and explained in the method section.

- The paper is missing some important references, such as the large kernel CNN paper and the SparseInst paper, which is also a pure-conv query-based object detection/segmentation method.

### Questions
Please help to address the clarity issues.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a query-based end-to-end Encoder-Decoder architecture, i.e., DECO with pure CNN modules for object detection, built upon a mechanism dubbed InterConv for the interaction between object queries and image features. Experimental results show that the proposed method without complicated components achieves competitive performance and efficiency over the DETR series.

### Strengths
1. The proposed InterConv consisting of pure convolutional layers can help the encoder and decoder capture long-range details without attention mechanisms and also help the decoder interact with object queries.
2. Without many complicated designs, DECO achieves comparative performance and efficiency over DETR.
3. DECO can be further improved to DECO+ by introducing the multi-scale design from Deformable-DETR.

### Weaknesses
1. On Lines 074-075, within the scope of object detection, the statement ``whose weights and inputs are both generated during runtime'' is unclear, as the only ones dynamically generated are intermediate variables (including attention weights). The statement lacks precision, as convolutional weights are determined by the training process and are not generated during runtime, while attention weights are indeed dynamically computed based on input features. This distinction is crucial and needs to be clarified.
2. The performance can be further improved using more convolutional-based techniques like deformable convolutions. While the paper mentions the potential of deformable convolutions, it does not explore the different variants (v1-v4) and their specific benefits, which could significantly impact performance and efficiency.

### Questions
1. Can the denoising training technique in DN-DETR and DINO be introduced into convolutional-based DECO?
2. To further improve the performance, it may be practical to introduce the deformable convolution (v1-v4) into the encoder and decoder. What about the efficiency?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a new approach to object detection and segmentation using Convolutional Neural Networks (ConvNets), challenging the dominance of transformer-based architectures in these fields. This paper introduces InterConv, a mechanism that mimics the interaction between object queries and image features, traditionally handled by attention mechanisms in transformers, but using only convolutional layers. This paper presents Detection ConvNet (DECO), an end-to-end object detection framework that replaces transformers with ConvNets. The proposed DECO obtains comparable results compared to transformer-based methods.

### Strengths
1. This paper presents InterConv which mimics attention mechanism with convolutional layers, and formulates Self-Interaction Module and Cross-Interaction Module (CIM) as self-attention and cross-attention.
2. This paper explores a convolution-based DETR framework with the proposed InterConv.
3. The proposed DECO obtains comparable performance compared to DETR.

### Weaknesses
1. Although this paper presents the convolution-version DETR which replaces attentions with convolutions, the overall performance is inferior to recent transformer-based methods, such as DINO, Co-DETR, and Stable-DINO[1], showing the limitations of using convolutional architectures.
2. In Tab. 2, it shows that DETR achieves better performance than DECO on both R50 and ConvNeXt-T while the improvements in inference speeds are not significant. In addition, DETR can be further optimized for acceleration therefore obtaining better inference speed and accuracy. Hence, the effectiveness of the proposed method in this paper is rather limited.
3. This paper lacks experimental comparisons with many recent works, such as Stable DINO[1], RT-DETRv2[2], DDQ[3], and SpeedDETR[4], in terms of both accuracy and speed.
4. It's hard to transfer the well-established techniques of recent DETR variants, such as denoising queries and deformable attention, into DECO for better performance.
5. The proposed object queries require prior knowledge to determine the best shape/layout, for example, 30x10 queries for the COCO dataset. I'm very concerned about whether the pre-trained detector DECO can perform well on the other datasets with different aspect ratios, such as datasets with 1:3 aspect ratios.
6. The details of extending DECO to segmentation tasks are unclear.

### Questions
1. I'm concerned about the initialization of the object queries. Could the object queries be random initialized variables for different images?
2. In Sec. 4.4, does this paper combine DECO with TinySAM?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduced a CNN-based end-to-end detection architecture, DECO. DECO contains an encoder and a decoder with pure convolutions nad is easy to implement. The experimental results demonstrate the effectiveness.

### Strengths
+ The paper is well-written and easy to follow.
+ Experiments are strong, demonstrating the effectivenss of CNN-based model.

### Weaknesses
 +  My main concern is the use of cross-scale feature-fusion module which is proposed in RT-DETR, which weakens the contribution. It would make the paper more strong if the authors could further discuss the difference. Specifically, the paper does not adequately detail how the proposed fusion mechanism differs from RT-DETR's approach, beyond a high-level claim of a different combination strategy. A more granular comparison, perhaps at the level of the mathematical operations or the specific network layers involved in the fusion, would be necessary to establish the novelty of the contribution.
+ There are many recent studies speeding up transformers, it would be nice to discuss more on using convolutions. Claims in L073-L074 are not convincing to me. The paper's argument for using convolutions over transformers for efficiency lacks a detailed analysis of the computational bottlenecks in both architectures. While the paper mentions the potential for faster inference with convolutions, it does not provide a thorough comparison of FLOPs, memory access patterns, or hardware utilization characteristics that would support this claim. Furthermore, the discussion does not consider recent advancements in transformer optimization, such as quantization or pruning, which could mitigate the speed disadvantages.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
