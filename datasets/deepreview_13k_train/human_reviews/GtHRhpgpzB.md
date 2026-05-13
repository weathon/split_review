# Learning Gain Map for Inverse Tone Mapping

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
For a more compatible and consistent high dynamic range (HDR) viewing experience, a new image format with a double-layer structure has been developed recently, which incorporates an auxiliary Gain Map (GM) within a standard dynamic range (SDR) image for adaptive HDR display. This new format motivates us to introduce a new task termed Gain Map-based Inverse Tone Mapping (GM-ITM), which focuses on learning the corresponding GM of an SDR image instead of directly estimating its HDR counterpart, thereby enabling a more effective up-conversion by leveraging the advantages of GM. The main challenge in this task, however, is to accurately estimate regional intensity variation with the fluctuating peak value. To this end, we propose a dual-branch network named GMNet, consisting of a Local Contrast Restoration (LCR) branch and a Global Luminance Estimation (GLE) branch to capture pixel-wise and image-wise information for GM estimation. Moreover, to facilitate the future research of the GM-ITM task, we build both synthetic and real-world datasets for comprehensive evaluations: synthetic SDR-GM pairs are generated from existing HDR resources, and real-world SDR-GM pairs are captured by mobile devices. Extensive experiments on these datasets demonstrate the superiority of our proposed GMNet over existing HDR-related methods both quantitatively and qualitatively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces Gain Map-based Inverse Tone Mapping (GM-ITM), focusing on estimating the Gain Map (GM) for SDR images rather than directly converting to HDR. The proposed dual-branch network, GMNet, effectively combines local and global information for accurate GM prediction. Extensive experiments on both synthetic and real-world datasets demonstrate GMNet’s advantages over existing HDR methods, showing improved performance in both quantitative and qualitative metrics. The paper also contributes new datasets for GM-ITM research, supporting future advancements in HDR image processing.

### Strengths
1. **Innovative Task Definition**: The paper introduces a novel task, Gain Map-based Inverse Tone Mapping (GM-ITM), which focuses on GM estimation rather than direct HDR prediction, leveraging a unique double-layer HDR format for enhanced up-conversion.

2. **Effective Network Design**: The proposed GMNet utilizes a dual-branch structure with Local Contrast Restoration (LCR) and Global Luminance Estimation (GLE) branches, effectively capturing both pixel-level and image-level information for accurate GM prediction.

3. **Comprehensive Dataset Contribution**: The authors provide both synthetic and real-world SDR-GM datasets, which are diverse and well-suited for evaluating GM-ITM, fostering further research in this field.

4. **Strong Experimental Validation**: Extensive quantitative and qualitative experiments demonstrate GMNet’s superiority over existing HDR-related methods, showcasing its potential in real-world applications.

### Weaknesses
1. **Limited Error Analysis**: The paper provides little insight into errors GMNet might produce in challenging conditions (e.g., extreme lighting, high contrast), which is crucial for understanding its limitations. Specifically, the analysis lacks a detailed breakdown of error types, such as color artifacts, haloing, or detail loss, under different lighting conditions and contrast levels. This makes it difficult to assess the robustness of the method in real-world scenarios where such conditions are common.

2. **Model Size Trade-Offs**: An ablation study on model size versus performance could reveal if a smaller GMNet version maintains accuracy with reduced resources, benefiting applications needing speed-accuracy balance. The paper does not explore the impact of reducing the number of layers or channels in the network on the final performance. Such an analysis would be crucial for practical deployment, especially in resource-constrained environments.

### Questions
1. **Insufficient Dataset Generation Information**: The process and diversity of the synthetic and real-world datasets are not fully detailed.
2.  **Lack of Real-Time Performance Evaluation**: The paper does not address GMNet’s computational efficiency or real-time processing capabilities, which are critical for practical HDR applications, especially on mobile devices.
3. **Scalability of the Model**: It’s unclear if GMNet can scale effectively with higher-resolution images, which is essential as HDR media often demands large image resolutions for detail preservation.

### Soundness
3

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
3

### Summary
The paper introduces a new task, Gain Map-based Inverse Tone Mapping (GM-ITM), to address the problem of converting standard dynamic range (SDR) images into high dynamic range (HDR) images using a Gain Map (GM). This work aims to improve HDR up-conversion by focusing on GM estimation instead of directly predicting HDR, leveraging a dual-branch network (GMNet) that includes Local Contrast Restoration (LCR) and Global Luminance Estimation (GLE) branches. To support the research, the authors also propose synthetic and real-world datasets to evaluate the method. The experiments demonstrate GMNet’s quantitative and qualitative superiority over existing methods for HDR-related tasks.

### Strengths
Novelty: The paper addresses an emerging area in HDR up-conversion by proposing the GM-ITM task, which is relatively unexplored and offers an innovative approach to inverse tone mapping. 

Method: The proposed dual-branch GMNet architecture is well-designed, with LCR and GLE branches targeting local and global image features respectively, which allows for improved GM estimation. 

Evaluation: The authors perform extensive quantitative and qualitative evaluations on synthetic and real-world datasets, benchmarking GMNet against well-established HDR methods and showing clear improvements. 

Dataset: The creation of both synthetic and real-world datasets for GM-ITM facilitates further research and addresses a gap in data availability, providing a valuable resource for the field. 

Ablation Studies: The paper includes thorough ablation studies on key components, such as spatial-aware modulation and GM resolution, to substantiate the effectiveness of GMNet’s design choices.

### Weaknesses
Limited Comparison Scope: The paper primarily compares GMNet with existing HDR and SDR-to-HDRTV up-conversion methods, but a comparison with more diverse or advanced inverse tone mapping techniques could strengthen the results. Specifically, the paper lacks comparison with methods that explicitly focus on detail preservation during inverse tone mapping, which is a crucial aspect of HDR reconstruction. Furthermore, the evaluation could benefit from including methods that employ different strategies for handling local contrast and global luminance, as this would provide a more comprehensive understanding of GMNet's performance relative to the state-of-the-art.

Complexity and Computation: The dual-branch network adds computational overhead, especially when processing high-resolution images. Discussion on efficiency or real-time applicability is limited, which could impact practical usage. The paper does not provide a detailed analysis of the computational cost associated with each branch of the network, making it difficult to assess the trade-off between performance and efficiency. A breakdown of the FLOPs and memory requirements for both training and inference would be beneficial. Additionally, the paper should discuss the potential for optimizing the network architecture to reduce computational demands, such as through model pruning or quantization.

Dependency on New Data Format: The proposed method relies heavily on the novel GM format, which is not yet widely adopted. This dependency could limit the method's applicability outside specialized devices or formats. While the paper introduces the Gain Map (GM) as an intermediate representation, it does not adequately address the practical challenges of generating or acquiring such data in real-world scenarios. The reliance on this specific format might hinder the method's adoption in existing HDR workflows that do not utilize GM. A more thorough discussion on the compatibility with existing HDR standards and the feasibility of integrating GM into current pipelines is needed.

Visual Comparisons in Real-World Scenarios: Although qualitative results demonstrate GMNet’s advantages, additional challenging real-world scenarios could better highlight its robustness. For instance, extreme lighting conditions or complex textures may expose limitations. The qualitative analysis could be enhanced by including more diverse scenes with varying degrees of complexity and lighting conditions. For example, scenes with strong backlighting, specular reflections, or intricate patterns could reveal potential weaknesses in the proposed method. A more rigorous evaluation of the method's performance under these challenging conditions is necessary to fully assess its robustness and generalizability.

### Questions
A more detailed discussion about the computation complexity would help understand the applicability of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
With recent advancements in display technology and the widespread adoption of HDR displays, a new dual-layer image format has emerged that is compatible with existing SDR displays. In response to this, the authors propose a new type of inverse tone mapping algorithm that infers a gain map applicable to adaptive HDR displays. Additionally, the authors construct an additional dataset for training and evaluating this type of network. Through experiments, the authors demonstrate that their method restores HDR images more effectively and reliably compared to other approaches.

### Strengths
* The authors' proposed inverse tone mapping algorithm, which takes real display environments into account, is both highly practical and innovative.
* The authors have effectively organized the existing methods in this field through Table 1. I believe this will be very helpful for future researchers studying this area.
* They have provided a formulation for the proposed method, which makes it easier to understand the approach proposed by the authors.

### Weaknesses
 * The authors need to conduct additional survey on SI-HDR. According to [A], SI-ITM is broadly divided into two branches of research: 1) methods that directly reconstruct HDR images and 2) methods that reconstruct bracketed exposures. In my opinion, there is a need to provide a detailed description of the differences between Learning from LDR stacks methods and generating a gain map. Specifically, the authors should clarify how their gain map approach differs from methods that explicitly generate multi-exposure stacks before HDR reconstruction, and discuss the potential advantages and disadvantages of each approach in terms of both reconstruction quality and computational complexity.

* Furthermore, the authors lack comparisons not only in terms of performance for learning from LDR stacks but also in terms of time efficiency with existing methods.
  * Like [B], it is possible to create images with relative EV +1 / -1 and expand the dynamic range. A discussion should be added on whether GM-ITM is more efficient than this case or not. The authors should provide a detailed analysis of the computational cost of their method compared to stack-based approaches, including both training and inference time. This should include a breakdown of the operations involved and a comparison of the number of parameters and FLOPs.

* As the authors propose a new type of network, they need to provide a detailed structure of this network. The description should include the number of layers, types of layers (e.g., convolutional, pooling, activation), kernel sizes, and the overall architecture of the network. This level of detail is crucial for reproducibility and understanding the method's complexity.

* There is a lack of validation on datasets commonly used in inverse tone mapping.
   - HDR-SYNTH + HDR-REAL: Yu-Lun Liu et al. Single-image hdr reconstruction by learning to reverse the camera pipeline. CVPR, 2020
   - HDREye: Hiromi Nemoto et al. Visual attention in ldr and hdr images. 9th International Workshop on Video Processing and Quality Metrics for Consumer Electronics (VPQM), 2015.
  - VDS: Siyeong Lee et al. Deep chain HDRI: Reconstructing a high dynamic range image from a single low dynamic range image. IEEE Access, 2018. The authors should evaluate their method on these datasets to demonstrate its generalizability and compare its performance with existing state-of-the-art methods. The evaluation should include both quantitative metrics (e.g., PSNR, SSIM, HDR-VDP) and qualitative visual comparisons.

### Questions
* Could the authors explain why the GM can be transmitted at a reduced resolution compared to the original SDR?
* Could you share experimental results for directly learning Q_max adjusted for the number of pixels?
* Would it be possible to release the code and data to ensure reproducibility?

* If I have misunderstood any part or if my concerns are adequately addressed during the review process, I would be more than willing to increase my score.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a dual-branch network GMNet to estimate the Gain Map for Inverse Tone-mapping. The paper also builts a synthetic and a real-world dataset from the existing HDR resources and mobile devices, respectively.

### Strengths
The idea of estimating the Gain Map instead of the HDR value is interesting, which can become a baseline for any future research.

### Weaknesses
The methods that were used for comparison in the paper are outdated.
The method is not really novel.
Lack of a common metric in HDR domain.
There are also some technical issues about loss function, data and models.

### Questions
Although the idea is interesting, it is not new and quite similar to estimating the transfer function which is well-known in image restoration domain. That said the contribution of the paper is limited. 

The literature reviews and compared methods are outdated which makes the paper less convincing. The latest method that was compared is from 2022 (KUNet) while the most recent one is DCDR-UNet: Deformable Convolution Based Detail Restoration via U-shape Network for Single Image HDR Reconstruction (based on Google Scholar).

In term of  PSNR in HDR domain, there is another metric which is more common than PNSR-NGM named mu-PSNR. The paper should consider running the evaluation on this metric too.

It is not clear about Q_max. Q_max value should not be in the range of [0,1], is that correct? If so, I_GM is not in the range [0,1] either. And can not normalize it as well, the reviewer wonder how the loss can be calculated and how the model was converged? 

Finally, as there is a upsampling function when estimating I_GM, the reviewer think that that I_GM might not represent the real I_GM precisely due to the interpolation function when applying upsampling (which can be either nearest neighbors or bidirectional).

### Soundness
2

### Presentation
2

### Contribution
2
