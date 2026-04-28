# Empirical Study on Enhancing Efficiency in Masked Image Modeling Pre-training

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3, 5

## Abstract
The combination of transformers and masked image modeling (MIM) pre-training framework has shown remarkable potential in various vision tasks. However, the high computational cost of pre-training hinders the practical application of MIM.
   This paper introduces \emph{FastMIM}, a simple and versatile framework that expedites masked image modeling through two steps: (i) pre-training vision backbones using low-resolution input images and (ii) reconstructing Histograms of Oriented Gradients (HOG) feature instead of original RGB values of the input images.
   Furthermore, we propose \emph{FastMIM-P}, which progressively increases the input resolution during the pre-training stage to improve the transfer learning performance of models with high capacity. We point out that: (i) a wide range of input resolutions during pre-training can result in similar performances in fine-tuning and downstream tasks such as detection and segmentation; (ii) the shallow layers of encoder are more important during pre-training, and discarding the last few layers can speed up the training process without affecting fine-tuning performance; and (iii) HOG is more stable than RGB values when transferring resolution. Equipped with \emph{FastMIM}, any type of vision backbone can be efficiently pre-trained. For example, using ViT-B/Swin-B as backbones, we achieve 83.8\%/84.1\% top-1 accuracy on ImageNet-1K. Compared to previous approaches, our method can achieve better top-1 accuracy while accelerating the training procedure by 5×.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FastMIM, a framework that accelerates masked image modeling (MIM) by using low-resolution input images and Histograms of Oriented Gradients (HOG) features for pre-training, achieving improved efficiency and accuracy in transfer learning tasks. The authors demonstrate that FastMIM achieves superior top-1 accuracy on ImageNet-1K and speeds up training by approximately 5×, with additional insights on resolution variation, layer importance, and the stability of HOG features over RGB values.

### Strengths
1.	The paper identifies and leverages low-resolution input images to significantly reduce both the pre-training time and memory usage.
2.	By reconstructing Histograms of Oriented Gradients (HOG) features, the method preserves crucial texture information that is often lost with lower resolutions.
3.	The proposed FastMIM framework is validated through extensive experiments.

### Weaknesses
1.	Risk of Information Loss: By reducing the resolution and replacing RGB pixels with HOG features, some fine-grained details may be lost, potentially affecting performance in tasks that require precise image analysis. Specifically, the reliance on HOG features, which capture edge and gradient information, might discard crucial color-based or subtle texture variations that are essential for tasks like fine-grained classification or medical image analysis where minute differences are critical for accurate diagnosis. The method's effectiveness may be limited in scenarios where high-frequency details are paramount.
2.	Task-Specific Adaptability: While HOG features perform stably in general vision tasks, they may not be suitable for tasks that require precise texture or color information, such as image generation or super-resolution reconstruction. The inherent loss of color information when using HOG features poses a significant limitation for tasks where color plays a vital role, such as in artistic style transfer or material recognition. Furthermore, the method's performance in tasks requiring the reconstruction of high-resolution images is questionable due to the initial downsampling.
3.	Limitations of Method Generality: The performance of this method during pre-training depends on the stability of HOG features, and it may not be suitable for model architectures or specialized tasks that require a broader range of features. The reliance on HOG features might not generalize well to architectures that are designed to process raw pixel data or other feature representations. This limitation could restrict the applicability of the pre-trained models to a subset of vision tasks and architectures, potentially hindering its broader adoption.

### Questions
1.	The method is well-suited for a wide range of vision tasks, particularly in environments with limited computational resources. However, considering its general applicability and performance across all tasks, especially those requiring high-detail image analysis, further improvements may be necessary to minimize information loss. If the above limitations can be overcome, particularly the issues with task-specific adaptability, this work holds great potential.

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
5

### Summary
The paper introduces FastMIM, a framework that speeds up masked image modeling (MIM) pre-training by using low-resolution images and reconstructing HOG features instead of RGB values. FastMIM-P further improves performance by progressively increasing input resolution during pre-training. This approach maintains good performance and accelerates training compared to previous methods.

### Strengths
1. Speedup in Pre-training: By using low-resolution input images, FastMIM significantly reduces pre-training time.
2. High Accuracy: Despite accelerating the training process, FastMIM maintains high accuracy.
3. The paper provides detailed experimental results, which help in understanding the robustness and reliability of the proposed method. The writing is clear and logically structured, making it easy to follow the methodology and results.

### Weaknesses
The contribution is limited. The paper improves MIM by using low-resolution images as input and HOG features as learning targets, with the advantages of HOG features already validated in the maskfeat work. Using low-resolution image input can accelerate the pre-training process without causing significant performance degradation, which indeed can serve as an acceleration trick for MIM pre-training. However, since model pre-training does not occur frequently in practical applications, the time cost of pre-training is acceptable. The main purpose of pre-training is to obtain better foundational model representations. Furthermore, the observed performance degradation as the model scales up with reduced resolution is an expected trade-off, not a novel finding. The method does not demonstrate any clear performance advantages in scaling up, beyond the reduction in training time. The use of HOG features as a superior target for masked image modeling compared to RGB values has also been previously established, thus the core methodology lacks significant novelty.

### Questions
1. The caption is incorrect in Figure 4, the text in the top left corner of the figure should annotate the line segment as HOG instead of pixel.
2. How does the method perform compared to other methods on larger pretraining datasets such as IM-21K or with longer pretraining epochs? If it can be demonstrated that Fast-MIM has better scaling-up capabilities, then its accelerated training would be more advantageous.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Masked Image Modeling (MIM) is a type computaional intentive pre-training methods. To  reduce the computational overhead of MIM, this paper proposed FastMIM to speeds up pre-training through two main strategies: (i) using low-resolution input images and (ii) reconstructing Histograms of Oriented Gradients (HOG) features instead of the original RGB values. FastMIM is compatible with both hierarchical and non-hierarchical transformer models. Experiments on ImageNet-1k, MS COCO and ADE20K are conducted.

### Strengths
- The visual analysis presented in Figure 3 is clear and compelling.

-  The paper demonstrates a strong motivation for the work, introducing efficient strategies to mitigate the high computational cost associated with MIM pre-training.

-  The proposed method shows promising results on the MS COCO object detection task, highlighting its potential effectiveness.

### Weaknesses
 - From Figure 4, the accuracy does not demonstrate a clear saturation trend. Providing the fine-tuning accuracy after 1600 pre-training epochs would make the results more convincing.

- Missing citation: In lines 190–200 (Encoder depth in pre-training), the observation that discarding the last several layers (blocks) in pre-training yields nearly the same performance has been previously noted in MIRL [1].

- While the reviewer acknowledges the efficiency of the proposed method, the performance gains of FastMIM on ImageNet-1K and ADE20K are marginal.

- Experimental results for ViT-L are not provided.

### Questions
- Please refer to the Weaknesses.
 
- Additionally, the reviewer is concerned about the effectiveness of FastMIM for large-scale models such as ViT-L and Swin-L, as these models tend to be more data-hungry. Reducing the input size decreases the number of visual tokens, which in turn significantly reduces the totall number of possible mask patterns. This is equivalent to a reduction in input diversity. 

If the authors can address the reviewer's questions one by one, the reviewer is willing to consider raising the score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces FastMIM, a simple and versatile framework that accelerates masked image modeling pre-training through two steps: (i) pre-training vision backbones using low-resolution input images, and (ii) reconstructing Histograms of Oriented Gradients (HOG) features instead of original RGB values. FastMIM-P, a variant, progressively increases input resolution during pre-training. Additionally, it emphasizes the importance of shallow layers during pre-training and suggests discarding the last few layers to speed up training without affecting fine-tuning performance. FastMIM enables efficient pre-training of any vision backbone, and has made lots of verification experiments.

### Strengths
The paper provides valuable insights into the design of MIM frameworks, including the importance of input resolution, the role of shallow layers during pre-training, and the stability of HOG features when transferring resolution.

### Weaknesses
1. The main contributions of the proposed method, i.e., the HOG reconstruction target and low-resolution input, have been extensively discussed in previous papers such as MaskFeat and SimMIM. This makes the proposed method appear less novel.
2. The empirical study mainly focuses on input resolution, training epochs, prediction targets, and the number of decoder/encoder layers. However, these aspects are common knowledge in MIM research, thus providing limited contribution to the community.
3. When verifying the importance of shallow layers during pre-training, the linear probing accuracy is missing, making the argument less convincing.

### Questions
See weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work conducts an empirical study on enhancing training efficiency in masked image modeling (MIM). The authors introduce a simple and versatile framework that expedites MIM by using low-resolution images and reconstructing HOG features.

### Strengths
1. Improving the efficiency of MIM pre-training is a good topic and has significant practical value. 
2. This paper contains numerous experiments and reveals some interesting findings. For instance, the authors find that discarding the last few layers can speed up the training process without affecting fine-tuning performance.

### Weaknesses
1. My main concern lies in the lack of novelty. The problem of low efficiency in MIM has been pointed out by previous works as the paper stated. The idea of using low-resolution images to expedite training is too simple and has been implemented in previous works. Additionally, the superiority of reconstructing HOG features has been demonstrated by its original paper. 

2. The proposed method has small gap for the performance of models with high capacity, e.g., 0.3% for Swin-L. It significantly diminishes the advantages of the proposed approach as one may just reduce training epochs to achieve this trade-off. For smaller models, it is more efficient to reconstruct features of pre-trained larger models like a kind of knowledge distillation. 

3. The proposed FastMIM-P progressively increases resolution to alleviate the above problem. However, the technical novelty of this approach is still limited. And the resolution and training schedule need to be carefully designed to achieve a better space-time trade-off as the authors stated. 

4. In Table 4, it can be seen that the authors try to demonstrate the generalization across different visual backbones. Nevertheless, the performance gain on some backbones lags behind recent MIM works due to the lack of integration of advanced technology such as masked convolutions.

### Questions
In Table 4, it is more meaningful to compare total training time, including the pre-training time and fine-tuning time.

### Soundness
3

### Presentation
3

### Contribution
2
