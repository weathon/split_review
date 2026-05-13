# Segmentation using efficient residual networks with attention-fusion modules

- Decision: Reject
- Scores: 3, 5, 1, 5

## Abstract
Fusing global and local semantic information in segmentation networks remains
challenging due to computational costs and the need for effective long-range
recognition. Based on the recent success of transformers and attention mechanisms,
this research applies attention-based methods of attention-boosting modules
and attention-fusion networks in enhancing the performance of state-of-the-art
segmentation networks, such as InternImage and SERNet-Former, addressing
these challenges. Integrating attention-boosting modules into residual networks
generates baseline architectures like Efficient-ResNet, enabling them to extract
global context feature maps in the encoder while minimizing computational costs.
Attention-based algorithms can also be applied to networks utilizing vision transformers
and convolutional layers, such as InternImage, to improve the existing
results of state-of-the-art networks. In this research, SERNet-Former is deployed
on the challenging benchmarking datasets such as ADE20K, BDD100K, CamVid,
and Cityscapes by depending on the attention-based methods with new implementations
of the network, SERNet-Former v2. Our methods have also been implemented
for InternImage-XL and improved the test performance of the network on
the Cityscapes dataset (85.1 % mean IoU). Respectively, the results of the selected
networks developed by our methods on the challenging benchmarking datasets are
found worth considering: 85.1 % mean IoU on the Cityscapes test dataset, 59.35
% mean IoU on ADE20K validation dataset, 67.42 % mean IoU on BDD100K
validation dataset, and 84.62 % mean IoU on the CamVid dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a transformer with an encoder-decoder structure to fuse the global and local information from the image for semantic segmentation. The proposed method improves the semantic segmentation on multiple datasets, demonstrating its effectiveness.

### Strengths
The proposed method improves the segmentation results based on the transformer architecture, which is lightweight.

### Weaknesses
1. It should be noted that IEEE CVMI has accepted the manuscript "SERNet-Former: Segmentation by Efficient-ResNet with Attention-Boosting Gates and Attention-Fusion Networks." Although CVMI has not yet provided the official version of the accepted paper, the author has provided a GitHub repository, which indicates that CVMI has accepted the paper. Furthermore, the figures and experimental results in the GitHub repository with arXiv and CVPRW versions are the same as those in the paper submitted to ICLR. The author should clarify this.

2. Apart from the above point, I find that this paper's presentation is of low quality. It lacks the motivation to propose a new method of fusing local and global semantics, which has been well-known for improving semantic segmentation performance. I suppose this motivation is presented in the introduction, which is missed in every part of the paper. Though the performances have been compared in the experimental section, I still cannot figure out why the proposed method yields better results. Furthermore, the presentation of the method lacks the necessary information. The critical Figure 2 fails to provide a clear illustration of the method. The relationship between Figure 2 and the equations is also unclear. This fact further disallows the reader to understand the insight behind the method.

3. Though the proposed method improves the segmentation results, it still lags behind other methods on important datasets (see test set on Cityscapes in Tab 4).

### Questions
See the "Weaknesses" above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper "SERNet-Former: Segmentation by Efficient-ResNet with Attention-Boosting Gates and Attention-Fusion Networks" introduces an innovative segmentation framework that leverages advanced attention mechanisms within a robust network architecture. The authors provide comprehensive experimental results that validate their approach against existing methods, demonstrating its effectiveness across multiple datasets. However, the manuscript could be improved by addressing the limitations of the method, expanding the discussion of the ablation studies, and including a broader range of comparative benchmarks. Overall, this work represents a significant contribution to the field of image segmentation. 

**However**, I noticed that this paper has already been accepted by IEEE CVMI 2024, titled "SERNet-Former: Segmentation by Efficient-ResNet with Attention-Boosting Gates and Attention-Fusion Networks." You can view the acceptance list for the conference at https://cvmi2024.iiita.ac.in/AcceptedPapers.php. After comparing the version in the GitHub repository (https://github.com/serdarch/SERNet-Former) with the version submitted by the authors to ICLR, it appears that there are only minimal differences between the two.

### Strengths
- **Innovative Approach**: The paper presents a novel method, SERNet-Former, which combines Efficient-ResNet with attention mechanisms, demonstrating a promising advancement in segmentation tasks.
- **Comprehensive Experiments**: The authors conduct extensive experiments across various datasets, showcasing the effectiveness of their approach and providing a thorough comparison with existing methods.
- **Clear Presentation**: The manuscript is well-organized, with a logical flow that makes the methodology and results easy to follow, enhancing the overall readability.

### Weaknesses
 - **Limited Discussion on Limitations**: The paper could benefit from a more in-depth discussion of the limitations of the proposed method, particularly in relation to different types of data or specific segmentation challenges. For example, the paper does not address how the method would perform on datasets with significant variations in object scale, lighting conditions, or occlusion. Furthermore, the limitations regarding computational resources and training time are not discussed, which are crucial for practical applications.
- **Insufficient Detail in Ablation Studies**: While the authors present some ablation studies, additional detail on the impact of each component in the network would strengthen the understanding of their contributions. The ablation studies should include a more granular analysis of the attention-boosting gates and attention-fusion networks. For instance, it is not clear how the performance changes when different numbers of attention heads are used or when the fusion strategy is altered. A more thorough exploration of the hyperparameter space is needed to fully understand the contribution of each component.
- **Comparative Analysis**: The comparison with state-of-the-art methods could be more robust, particularly by including more recent benchmarks to provide a clearer context for the performance claims. The paper should include a comparison with more recent transformer-based segmentation models, which have shown significant performance improvements in recent years. Additionally, the paper does not provide a detailed analysis of the computational cost of the proposed method compared to other state-of-the-art approaches, which is important for practical deployment.

### Questions
I noticed that this paper has already been accepted by IEEE CVMI 2024, titled "SERNet-Former: Segmentation by Efficient-ResNet with Attention-Boosting Gates and Attention-Fusion Networks."

Additionally, I have a question regarding:

1. **What specific metrics were used to evaluate the performance of SERNet-Former compared to existing segmentation methods, and how do these metrics support the claims made by the authors regarding its effectiveness?**

2. **Can the authors provide more details on the design choices behind the attention mechanisms used in SERNet-Former and how they contribute to the model's overall performance in segmentation tasks?**

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
-

### Strengths
-

### Weaknesses
Considering that this paper has already been accepted by IEEE CVMI, I think it should be rejected.

### Questions
-

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes AbGs,AfNs to fuse global and local semantic information in segmentation. Attention-fusion networks are desined in the decoder part to improve the efficiency.

### Strengths
1.This paper has made useful explorations in the fusion of global and local information, bringing some inspiration to this field.
2.Experimental results show that this method has some advantages

### Weaknesses
1.The writing of this article is poor. Many sentences are not clear and not easy to understand. Some sentences are too long and difficult to understand. e.g. line 125: The multi-scale problem in computer vision can be described as the discrepancy in integrating the different sizes of spatial and channel-based semantic information of an object acquired from the global and local contexts of segmentation networks.
line 203：It is aimed at developing an encoder-decoder architecture with additional attention mechanisms to get efficient segmentation networks fusing semantic information from different contexts by regarding the multi-scale problem.

2.The method in this article lacks insight, and many designs are tricky.  e.g. Why are there two consecutive layers (AbM4, AbM5) in H/8 and W/8 resolutions? For another question, please refer to Question 2.

3.The experimental analysis is not enough, and the ablation experiment is not very sufficient. More details can refer to Question 4.

4.This paper seems to have multiple submissions，which was accepted by IEEE CVMI previously.

### Questions
1. Why is the sigmoid function used as the activation function in the AbG module? Will it aggravate the gradient vanishing problem during training? Have you tried other activation functions?
2. Dilation-based convolution is used in DbN module, why not use dilation convolution in encoder and decoder part?
3. During upsampling, the image size changes from H/4, W/4 to H, W. Why not use progressive upsampling?
4. From Table 3 and Table 4, your performances are not as good as InternImage and VitAdapter-L(test mIoU). What are the parameters and inference speed(e.g millisecond) of these two methods? How do they compare to yours?

### Soundness
2

### Presentation
1

### Contribution
2
