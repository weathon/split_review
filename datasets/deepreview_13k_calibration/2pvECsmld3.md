# SparseFormer: Sparse Visual Recognition via Limited Latent Tokens

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Human visual recognition is a \emph{sparse} process, where only a few salient visual cues are attended to rather than traversing every detail uniformly. 
However, most current vision networks follow a \emph{dense} paradigm, processing every single visual unit (\eg, pixel or patch) in a uniform manner.
In this paper, we challenge this dense paradigm and present a new method, coined \emph{{SparseFormer}}, to imitate human's \emph{sparse} visual recognition in an end-to-end manner.
SparseFormer learns to represent images using a highly limited number of tokens (down to $49$) in the latent space with sparse feature sampling procedure instead of processing dense units in the original pixel space. 
Therefore, SparseFormer circumvents most of dense operations on the image space and has much lower computational costs.
Experiments on the ImageNet classification benchmark dataset show that SparseFormer achieves performance on par with canonical or well-established models while offering better accuracy-throughput tradeoff.
Moreover, the design of our network can be easily extended to the video classification with promising performance at lower computational costs.
We hope that our work can provide an alternative way for visual modeling and inspire further research on sparse neural architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a sparse paradigm for visual recognition, and introduced a novel backbone named SparseFormer, which has a lower memory footprint and higher throughput compared to dense architectures, especially in the low-compute region.
Experiments show that the proposed method achieves a low memory and time cost while maintaining high performance.

### Strengths
1. The proposed SparseFormer is novel and solid.
2. While maintain the performance, SparseFormer has a low memory footprint and high throughout.
3. The experiments are solid.

### Weaknesses
None

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce SparseFormer, which comprises two main components: the Focusing Transformer and the Cortex Transformer. The Focusing Transformer addresses the challenge of extracting image features sparsely, decoding them into latent tokens, and adjusting token regions of interest (RoIs). The Focusing Transformer efficiently extracts image features with a computational complexity of O(N·P·C), where N is the number of latent tokens, regardless of the input image size. Evaluated on ImageNet, the authors demonstrated that the proposed method achieved 1.7x faster inference speed compared with Swin-T with small accuracy degradation. It also outperforms ResNet50 with a faster speed.

### Strengths
1. This paper is thoroughly motivated and exceptionally well-written. The concept of sparsifying input tokens holds paramount importance for vision transformers (ViTs) owing to the quadratic complexity with respect to sequence length in multi-head self-attention.

2. The authors have designed a functional solution, known as FocusTransformer, which improves upon the Perceiver method by introducing and dynamically adjusting regions of interest (RoIs). Experimental results compellingly demonstrate the effectiveness of this architecture on the ImageNet dataset.

3. The authors have not only illustrated how SparseFormer can reduce computational workload (measured in FLOPs), but they have also empirically shown a significant speedup on a V100 GPU under FP32 precision, further showcasing the efficacy of their proposed approach.

### Weaknesses
1. While the authors have put considerable effort into elucidating the disparities between SparseFormer and Perceiver, it remains challenging for me to find a fundamental difference between these two methodologies. In my estimation, the primary distinction appears to be the introduction of the FocusTransformer. However, upon examination of this architecture, I have also observed a clear similarity to DeformableDETR. Consequently, I find it challenging to pinpoint the truly innovative contributions of this paper.

2. The scope of the evaluation in this work appears somewhat limited. The presentation exclusively reports image classification results. However, Vision Transformers (ViTs) have showcased their efficacy across a diverse range of computer vision tasks, including object detection, semantic segmentation, and image generation. A majority of these applications typically demand high-resolution inputs, which makes the efficiency of reducing the number of visual tokens even more critical. My particular interest lies in understanding the applicability of the proposed approach to dense prediction tasks such as segmentation and image generation with diffusion models, given that the FocusTransformer seems to introduce token-level information loss.

3. The section on speed evaluation is extensive, but it may benefit from further solidity. The reliance on the V100 GPU, which is considered somewhat outdated, raises questions in the context of contemporary Deep Neural Network (DNN) inference, where there is a preference for using lower precision formats like INT8 and FP16 with a TensorRT backend. Even though the proposed architecture is light in terms of FLOPs, I am concerned about the potential efficiency of the DeformableDETR-like FocusTransformer when integrated with TensorRT. It would be great if the authors could provide relevant results in this regard.

### Questions
Please respond to my questions and concerns in "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the SparseFormer, which modifies the standard Transformer model by using a small number of tokens in latent space to reduce its size and computational complexity.

### Strengths
1. Provides an alternative sparse paradigm ($i.e.,$) for vision modeling compared to existing Transformers. Reduces computation by operating on limited tokens.
2. Token ROI adjustment mechanism is effective at focusing on foregrounds.
3. Visualizations show the model progressively focuses on discriminative regions.

### Weaknesses
1. While the paper demonstrates the effectiveness of SparseFormer on classification tasks. The reviewer has concerns about the generalization to more complex scenarios. Appendix A.1 also points out the inferior performance compared to the recent transformer network. The use of specific sparse attention patterns might limit the model's ability to capture certain types of long-range dependencies in the images for downstream tasks. The fixed sparse attention patterns, while computationally efficient, may not adapt well to varying image content and could lead to suboptimal feature aggregation, especially when global context is crucial. For instance, in scenarios with complex object arrangements or occlusions, the predefined receptive fields of the sparse attention might fail to capture the necessary contextual information.

2. In addition, the reviewer also has concerns about token ROI. Adjusting token ROIs lacks strong spatial supervision. Performance on dense prediction tasks ($i.e.,$ segmentation tasks) requiring precise localization may suffer. With complex images, the signal will be weak and may not focus on the meaningful pixels. The token ROI adjustment mechanism, relying on learned attention weights, might not be robust enough to handle noisy or cluttered backgrounds. Without explicit spatial guidance, the ROIs could potentially drift away from the actual object boundaries, leading to inaccurate segmentation masks. Furthermore, the lack of explicit spatial supervision could also hinder the model's ability to learn precise geometric relationships between different parts of an object.

### Questions
Overall, this paper presents a step towards sparse vision architectures by a novel token ROI approach. The reviewer has no further questions, please see the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces SparseFormer, an innovative vision transformer designed for efficiency, which encodes images into a select number of sparse tokens in a latent space. The efficacy and computational economy of SparseFormer are showcased through its performance in ImageNet and video classification tasks.

### Strengths
1. the SparseFormer model it introduces attains impressive results with a notable reduction in computational cost and latency, highlighting its efficiency and practicality in application.
2. it is composed with a clear presentation, making it accessible and understandable

### Weaknesses
The experimental validation does not appear to be solid, such as the detection results and the ablation. see details in Question part
The novelty of SparseFormer is somewhat constrained, as it does not substantially deviate from existing methods in the field.
There is an absence of comparative analysis with other efficiency-oriented techniques, such as token pruning

### Questions
Could you provide insight into why the detection results are not more favorable, especially considering that your Region of Interest (RoI) mechanism appears to be well-suited for detection tasks? 
Additionally, the paper does not include an ablation study on adjusting the RoI mechanism, which leaves its importance in the proposed method somewhat ambiguous. Could you clarify the necessity of the RoI mechanism within your framework?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
