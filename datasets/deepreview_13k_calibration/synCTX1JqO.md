# RaCNN: Region-aware Convolutional Neural Network with Global Receptive Field

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
Recent Convolutional Neural Networks (CNNs) utilize large-kernel convolutions (e.g., 101 kernel convolutions) to simulate a large receptive field of Vision Transformers (ViTs). 
    However, these models introduce specialized techniques like re-parameterization, sparsity, and weight decomposition, increasing the complexity of the training and inference stages. 
    To address this challenge, we propose Region-aware CNN (RaCNN), which achieves a global receptive field without requiring extra complexity, yet surpasses state-of-the-art models. 
    Specifically, we design two novel modules to capture global visual dependencies. 
    The first is the Region-aware Feed Forward Network (RaFFN). 
    It uses a novel Region Point-Wise Convolution (RPWConv) to capture global visual cues in a region-aware manner. 
    In contrast, traditional PWConv shares the same weights for all spatial pixels and cannot capture spatial information. 
    The second is the Region-aware Gated Linear Unit (RaGLU). 
    This channel mixer captures long-range visual dependencies in a sparse global manner and can become a better substitute for the original FFN. 
    Under only 84\% computational complexity, RaCNN significantly outperforms the state-of-the-art CNN model MogaNet (83.9\% vs. 83.4\%). 
    It also demonstrates good scalability and surpasses existing state-of-the-art lightweight models. 
    Furthermore, our RaCNN shows comparability with state-of-the-art ViTs, MLPs, and Mambas in object detection, instance segmentation, and semantic segmentation.  
    All codes and logs are released in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Region-aware CNN (RaCNN), a novel architecture that achieves a global receptive field without added complexity, outperforming state-of-the-art models. RaCNN features two key modules: the Region-aware Feed Forward Network (RaFFN) using Region Point-Wise Convolution (RPWConv) to capture global visual cues, and the Region-aware Gated Linear Unit (RaGLU) for capturing long-range dependencies. With only 84% of the computational complexity, RaCNN surpasses the performance of MogaNet (83.9% vs. 83.4%) and demonstrates strong scalability, excelling in object detection, instance segmentation, and semantic segmentation.

### Strengths
1. RaCNN includes two critical modules: the Region-aware Pointwise Convolution (RPWConv) for capturing global visual information and the Region-aware Gated Linear Unit (RaGLU) for capturing long-range dependencies.
2. RaCNN outperforms state-of-the-art models like MogaNet, achieving higher performance (83.9% vs. 83.4%) with only 84% of the computational complexity.
3.  The model demonstrates excellent performance across various tasks, including object detection, instance segmentation, and semantic segmentation.The paper provides a thorough comparison with other methods across multiple downstream tasks, showcasing the robustness and effectiveness of RaCNN.

### Weaknesses
1. While RaCNN shows improvements over existing models, the performance gains might be considered incremental. 
2. The ablation experiments are insufficient, lacking further analysis on the effectiveness of the proposed modules. For example, the dynamic PWconv use cosine distance to measure similarity instead of inner-product, how about the difference affect the performance ?
3. From the definition of the dynamic PWconv and RaGLU in the paper, and its implementation in the code, the proposed method does not capture the global receptive field of imagesm which is inconsistent with the paper's title.  Since the dynamic PWconv are improvement upon the basic of Pointwise Convolution, the dynamic wieghts generated for different region just provide different ways for gatherring features along the channel dimension.  The region attention in RaGLU is also a kind of channel attention .All the operation about the spatial gathering remains conventional 3x3 convolution. So where the global receptive field exhibits?

### Questions
The questions have been listed in the Weaknesses.

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
3

### Summary
The paper titled "RaCNN: Region-Aware Convolutional Neural Network with Global Receptive Field" proposes a new CNN model, RaCNN, that enhances the receptive field to capture global visual dependencies without increasing computational complexity. The key innovations of RaCNN include two modules: the Region-aware Feed Forward Network (RaFFN) and the Region-aware Gated Linear Unit (RaGLU).

RaFFN uses Region Point-Wise Convolution (RPWConv) to capture global cues by dividing spatial feature maps into sparse global regions, allowing it to dynamically adjust weights per region. Meanwhile, RaGLU serves as a channel mixer, capturing long-range dependencies in a sparse, global manner, improving spatial information aggregation. Compared to conventional CNNs, RaCNN demonstrates state-of-the-art performance, surpassing models like MogaNet, while requiring fewer computational resources.

### Strengths
1.	The paper proposes region-aware CNN. The author suggest RaCNN captures both local and global information to better feature extraction
2.	Experiments show RaCNN achieves better results on various tasks, including image classification (ImageNet-1K), object detection (COCOval2017), instance segmentation (COCOval2017), and semantic segmentation (ADE20K).

### Weaknesses
1.	It is confused to figure out how RaCNN captures global information. For instance, Region PWConv in figure 4c takes dilated windows and Region Attention in figure 5 averages spatial feature in a dilated manner. However, dilation is not equivalent to the so-called ‘global’. From my point of view, it is more proper to say it captures a larger local receptive field. The use of dilated windows, while expanding the receptive field, still operates within a localized context. The method samples from these dilated regions, but this sampling does not inherently equate to a global understanding of the image. The term 'global' implies an awareness of the entire image context, which is not fully achieved through dilated sampling alone.
2.	The author suggests RaCNN is better because it captures local and global information. However, in figure 2 we can see SLak, UniRepLKNet, and InceptionNeXT all captures local and global receptive field, even with a more ‘global’ field. Therefore, I am suspecting local and global receptive field is not the true reason for RaCNN performance. The argument that RaCNN's performance stems from capturing both local and global information is not sufficiently supported. Figure 2 indicates that other models also achieve this, some with even larger receptive fields. This raises doubts about whether the local and global receptive field is the primary factor driving RaCNN's performance. The novelty of RaCNN might lie elsewhere, such as in the specific way it processes information within these receptive fields, rather than the mere presence of both local and global views.
3.	For figure 1, there is no margin between the figure 1 caption and main text. 
4.	More tasks [1] should be added to verify the effectiveness of RaCNN, such as 2D and 3D human pose estimation, and video prediction. 


### Questions
Question: While RaCNN claims to achieve a global receptive field without additional complexity, it would be beneficial to understand the exact computational trade-offs compared to recent models with large-kernel convolutions. Could the authors provide further detail on any specific optimizations that contribute to this efficiency?
Suggestion: Including a breakdown of computational complexity relative to specific design choices (like RPWConv and RaGLU) and a comparison against representative models would enhance clarity on how RaCNN maintains low computational cost.
Scalability Across Tasks and Architectures:

Question: RaCNN demonstrates strong performance across multiple vision tasks. How does its performance and efficiency vary when scaling to larger or smaller model variants, particularly in dense prediction tasks? Are there configurations where RaCNN’s advantages diminish?
Suggestion: It would be helpful if the authors provided more details on the model's performance when scaled to different architectures and task demands, particularly in cases where efficiency gains may be less pronounced.
Impact of Region Size and Sparse Global Regions:

Question: RaCNN’s RPWConv operates on sparse global regions, which raises questions about the impact of different region sizes on performance and the possibility of information loss. Could the authors clarify how they determine optimal region sizes and the robustness of RaCNN to varying region granularity?
Suggestion: An ablation study on the impact of different region sizes and sparsity levels on accuracy and computation might help clarify the balance between global context capture and computational efficiency.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents the RaCNN for vision recognition. The proposed RaCNN achieves a global receptive field with two designs: the region-aware FFN that uses a variant of dilated attention to model global relations, and the region-aware GLU that uses DWConv and a regional SE module to improve model capacity. The model is evaluated on widely used visual recognition benchmarks and compared to recent SoTA methods.

### Strengths
- The method achieves competitive performance on various visual recognition tasks including classification and dense prediction. The throughput also looks good.

- The authors conducted extensive experiments to verify the model.

### Weaknesses
 - The proposed model actually is not a convolutional neural network. A convolution operation should be transition-equivariant. The proposed operation is closer to a variant of local attention instead of convolution. The authors may consider changing the name of the model and some claims in the paper to avoid misunderstanding.

- The proposed design is a mixture of some existing techniques.  The Region Point-Wise Convolution is not a convolutional operation and it is very similar to [r1]. The RA operation is a variant of the SE module. Although the paper shows that the mixture can achieve good performance, the technical contribution is quite limited. 

- The motivation of the paper is not quite clear. According to the abstract, the paper wants to propose a new solution because "these models introduce specialized techniques like re-parameterization, sparsity, and weight decomposition, increasing the complexity of the training and inference stages". However, I think the proposed solution also introduces many complex operations and may make the solution less general. 

- The presentation of the paper needs improvement. Many claims are not clear. For example, in the caption of Figure 1, it is mentioned that some existing methods "could capture long-range dependency but introduce excessive visual noises". I don't found there is evidence to show these methods can introduce extra noise. Besides, the descriptions of the core contribution: RPWConv and RA, are quite confusing. Figure 4 didn't clearly the RPWConv operation. Equations 5-7 are also misleading since both "x \dot x" and "xw" actually are matrix multiplication. I need to check the provided code to clearly understand how the operation actually works.

### Questions
Please refer to my comments above. Considering there are many issues about the presentation, positioning, technical contribution, and motivation, I cannot recommend acceptance for this paper.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents RaCNN, a convolutional neural network designed to capture both long-range dependencies and local contextual information in images. The architecture introduces two key components: the Region-aware Feed Forward Network (RaFFN) and the Region-aware Gated Linear Unit (RaGLU). RaFFN employs a specialized Region Point-Wise Convolution (RPWConv), which divides spatial feature maps into global regions and applies dynamic weights within each, allowing for the capture of both global and local features. RaGLU enhances spatial information mixing through region-specific attention mechanisms. The authors claim that RaCNN outperforms state-of-the-art models such as MogaNet and Swin Transformer in tasks like image classification, object detection, and instance segmentation, while maintaining computational efficiency. Extensive experiments and ablation studies are provided to validate RaCNN's effectiveness.

### Strengths
RaFFN and RaGLU introduce a novel region-based dynamic weighting approach in CNNs, allowing RaCNN to capture multiscale spatial dependencies compared to traditional convolutional methods more effectively.

The experimental results across multiple vision tasks, such as object detection and instance segmentation, demonstrate RaCNN's robustness. This approach efficiently captures global dependencies while maintaining computational efficiency, representing an advancement over previous CNNs and ViTs.

RaCNN demonstrates scalability across various model sizes and tasks.

### Weaknesses
The claim that RaCNN "can capture long-range dependencies and local context features simultaneously without excessive noise" is based on a single ERF visualization. However, visualizations from a single layer are insufficient to support such broad conclusions about noise reduction and contextual feature capture, as ERF patterns vary across layers in complex networks. A more comprehensive analysis across multiple layers or the use of additional metrics, such as analyzing the spectral properties of the feature maps or using occlusion sensitivity analysis, would be necessary to fully substantiate this claim.

Although the paper highlights RaCNN’s computational efficiency, it lacks a detailed comparison of how this efficiency holds up against similar models in real-world scenarios, such as inference time, memory usage, and power consumption on different hardware platforms. The reported FLOPs and training throughput are insufficient to assess the practical efficiency of the model.

The RPWConv design, which divides the spatial feature map into predefined regions, may limit flexibility across different image types. Fixed partitioning could reduce generalizability for diverse visual tasks that benefit from more adaptive receptive fields. For instance, images with objects of varying scales or complex spatial arrangements might not be optimally processed by fixed regions. Further investigation into alternative partitioning strategies, like adaptive region sizes based on image content or learned region boundaries, would strengthen the proposed approach.

While the ablation studies focus on the impact of individual components (e.g., RPWConv, RaGLU), they do not sufficiently explore the interactions between these modules. For example, the impact of RaGLU on the features extracted by RPWConv is not analyzed. Expanding the ablation studies to analyze how these components interact, such as by varying the depth or number of channels in each module, could provide deeper insights into RaCNN’s overall design.

The paper’s focus on FLOPs as the primary metric for efficiency may overlook other crucial factors, such as memory access patterns, memory footprint, and inference time on various hardware. These metrics are critical for real-world deployment, and their inclusion would provide a more balanced perspective on RaCNN’s efficiency. For example, a model with lower FLOPs might still be slower in practice due to inefficient memory access.

### Questions
1. Could the authors provide additional evidence to support RaCNN’s claims of noise resistance and contextual feature capture? Specifically, how does the ERF visualization change across different layers of RaCNN, and would deeper layer results reinforce the conclusions drawn from Figure 2?

2. How does RaCNN perform in terms of inference speed and memory usage compared to models like Swin Transformer and MogaNet in real-time applications?

3. Have the authors considered exploring alternative region partitioning strategies for RPWConv, such as using adaptive region sizes, to enhance flexibility across different image types?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel convolutional neural network (CNN) model called Region-aware CNN (RaCNN), designed to simulate a large receptive field with minimal computational overhead. RaCNN achieves this by replacing the standard feedforward neural network (FNN) with RaGLU and the original depthwise convolution (DWConv) with Region PWConv (RPWConv), allowing the model to capture long-range visual dependencies. The paper demonstrates the effectiveness of RaCNN through experiments on classification, detection, and segmentation tasks.

### Strengths
The motivation of the paper is valuable. The high computational complexity of large kernel size is indeed a barrier in the field of computer vision.

The proposed RaCNN model shows effectiveness across various tasks, as evidenced by the experimental results.

### Weaknesses
The contribution of this work is not particularly groundbreaking. Compared to previous methods like [], the advantages of RaCNN are not significantly clear.

Some expressions in the paper lack precision. For example, the distinction between “FLOPS” and “FLOPs” on page 8, line 421, is not handled correctly. I recommend a thorough review of the manuscript.

Equation (6) appears to be incorrect; “x·x” cannot be computed as written. Please verify all equations.

### Questions
The paper lacks detailed explanation regarding the advantages of dilated windows in Region PWConv. Could you provide more clarification on this?

What would be the impact of using Dynamic PWConv instead of Region PWConv? Additional ablation studies would strengthen the validation of your method.

In my view, Figure 2(e) does not effectively demonstrate RaCNN’s ability to capture long-range dependencies.

In Table 8, row 4 (which uses both ReFFN and RaGLU) reports fewer FLOPs and parameters than rows 2 and 3, which is puzzling. Could you explain this discrepancy?

### Soundness
3

### Presentation
2

### Contribution
2
