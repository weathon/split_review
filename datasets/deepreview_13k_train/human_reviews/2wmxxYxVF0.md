# SEE: See Everything Every Time - Broader Light Range Image Enhancement via Events

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Event cameras, with a high dynamic range exceeding $120dB$, significantly outperform traditional cameras, robustly recording detailed changing information under various lighting conditions, including both low- and high-light situations.
However, recent research on utilizing event data has primarily focused on low-light image enhancement, neglecting image enhancement and brightness adjustment across a broader range of lighting conditions, such as normal or high illumination.
Based on this, we propose a novel research question: how to employ events to enhance and adjust the brightness of images captured under broader lighting conditions.
To investigate this question, we first collected a new dataset, \textbf{SEE-600K}, consisting of 610,126 images and corresponding events across 202 scenarios, each featuring an average of four lighting conditions with over a 1000-fold variation in illumination.
Subsequently, we propose a framework that effectively utilizes events to smoothly adjust image brightness through the use of prompts.
Our framework captures color through sensor patterns, uses cross-attention to model events as a brightness dictionary, and adjusts the image's dynamic range to form a broader light-range representation (BLR), which is then decoded at the pixel level based on the brightness prompt.
Experimental results demonstrate that our method not only performs well on the low-light enhancement dataset but also shows robust performance on broader light-range image enhancement using the SEE-600K dataset.
Additionally, our approach enables pixel-level brightness adjustment, providing flexibility for post-processing and inspiring more imaging applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SEE-Net, a framework for image brightness adjustment using event cameras across a broad range of lighting conditions. It also presents the SEE-600K dataset, containing event-image pairs under various lighting scenarios. The model employs cross-attention to fuse event and image data, enabling prompt-based brightness control. Experimental results suggest SEE-Net’s improved performance over baseline methods on the SDE and SEE-600K datasets.

### Strengths
- The SEE-600K dataset expands upon previous datasets, offering more diverse lighting scenarios, which could be useful for broader experimentation in event-based imaging.

- The lightweight architecture of SEE-Net (1.9M parameters) suggests computational efficiency, which may be beneficial in practical applications.

### Weaknesses
 - The proposed problem of enhancement with event cameras across  broader brightness is not particularly novel. Prior works on event-based HDR (Cui et al., 2024; Yang et al., 2023; Messikommer et al., 2022) have already explored similar concepts, partially addressing the needs this paper claims as unique. The distinction in this paper’s approach does not clearly add new knowledge to the field.
    
- Also, the problem’s importance is unclear, especially given that established techniques can already perform exposure adjustments during enhancement. Techniques like [1, 2] allow exposure control with brightness factor as prompts. The paper does not demonstrate how SEE-Net outperforms these approaches when combined with event-based imaging theoretically and empirically.
    
- The core methodology of using cross-attention to merge event and image data is not new and has been applied extensively in similar tasks [3, 4]. Furthermore, the proposed cross-attention module and prompt mechanism are insufficiently justified. There is no clear rationale for why these choices improve performance over simpler fusion techniques, such as concatenation, or why they surpass existing multi-modal enhancement frameworks. The theoretical foundations for the encoding and decoding processes are limited, leaving the importance of each component unclear.
    
- The SEE-600K dataset is primarily an expanded version of SDE (Liang et al., 2024), constructed with similar strategies and devices, and addressing a similar problem. Although it extends certain aspects through refined engineering techniques, these modifications alone do not constitute a significant novelty or research contribution.
    
- The SEE-600K dataset shows quality issues, particularly in the normal-light images. Figures 6 and 12 exhibit noticeable artifacts, such as blurriness (e.g., the tree textures in Row 3 of Figure 12, toy contours in Row 1), saturation (e.g., the toys in Row 1), noise (e.g., grass behind bicycles in Row 4), and other visual defects (e.g., ground in Row 1 of Figure 13). These issues detract from the dataset’s value as a high-standard resource and raise questions about its suitability for rigorous research.

### Questions
1. Why is broader brightness adjustment using event cameras necessary when exposure control can be achieved through established techniques? How does SEE-Net theoretically outperform these approaches?
    
2. What specific performance gains justify the choice of cross-attention over simpler fusion techniques in the context of this problem?
    
3. Could the authors provide quantitative metrics or examples to verify the SEE-600K dataset’s consistency and quality, addressing the observed artifacts?

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
This paper proposes an image enhancement and brightness adjustment method using SEE-600K, a carefully captured dataset spanning different brightness levels. 
The SEE-600K dataset is significantly larger than existing datasets and was captured under diverse lighting conditions, making it well-suited for both low-light enhancement and HDR imaging applications. 
The proposed enhancement method uses cross-attention to fuse events and images, while the brightness adjustment method leverages brightness prompts to produce results tailored to different brightness levels. 
The proposed approach achieves superior results compared to previous methods.

### Strengths
1. The SEE-600K dataset is carefully designed and captured, which is also suitable for other low-light enhancement and HDR reconstruction methods to test their results.
2. The brightness adjustment methods take brightness prompt into consideration, which reduces the difficulty of recovering actual brightness level without prior knowledges.

### Weaknesses
1. The results of the proposed method are not good enough for over-exposed areas. Some details are missing in saturated areas, e.g., Figure 19 and Figure 20. They are also not good enough for under-exposed areas, e.g., Figure 5.
2. The results of different methods in Figure 5 are not well-aligned. If these results are from different frames, the comparison may not be fair.
3. In Figs. 9, 21, and 22, some details in over-exposed areas are actually recorded by events, while the SEENet cannot recover it.
4. As noted by reviewer aQ36, the SEE dataset has relatively low image quality, which results in the low quality results of SEENet. For instance, SEENet’s results appear more blurry in Figs. 5, 17, 19, 20, and 23 compared to other methods.

### Questions
In Table 2, the proposed method shows the worst results when trained on SED for both high light and normal light but achieves the best results when trained on SEE. Which part of the proposed method contributes to this significant improvement for high light and normal light? 
Additionally, I noticed that some methods trained on SED are missing when trained on SEE. What is the reason for removing these methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel dataset comprising RGB frames and synchronized event data captured across various scenarios. To simulate diverse lighting conditions, the RGB frames are collected using four distinct ND filters, each representing a unique lighting intensity. Additionally, the authors present a network designed to recover normally exposed images from inputs under varying lighting conditions, leveraging the ND-filtered data. A notable feature of the proposed method is its capacity to control the brightness of output images through a brightness prompt.

### Strengths
•	This paper proposed a dataset that contains images different light conditions, which may contribute to the event-based vision community. 

•	The appendix is detailed with dataset samples, additional results, and explanation of the proposed network.

### Weaknesses
•	The contribution seems incremental, resembling an extension of previous work, specifically Liang et al.’s SDE Dataset (CVPR24). While the authors introduce some novel components, the dataset and approach appear to build closely on existing work without clear distinctions in scope or objectives.

•	The quality of the normally lit images in the proposed dataset is suboptimal. The dataset relies on APS frames from the Color DAVIS sensor, which suffers from dynamic range limitations. As a result, these frames lead to a notable disparity in quality. This limitation is visible in the normal-light images presented in Figure 13 (c), where details captured by the event sensor are underrepresented.

•	The motivation for designing specific position and Bayer pattern embeddings within the network architecture is not adequately justified. The authors introduce these components, but it remains unclear how they enhance the model’s performance or if they address particular challenges within the task. Clarifying their role and potential benefits would improve understanding and transparency.

•	The proposed method’s loop function may result in long processing times, which could hinder its usability, particularly in real-time or low-latency applications. Without detailed analysis of the computational demands and latency, it is challenging to assess the network’s practicality in deployment scenarios. Although the size of the proposed network is small (1.9M), the FLOPs is pretty high (405.72).

•	In Figure 5, the output of the proposed method appears visibly blurred, especially when compared to the sharpness of baseline methods like EvLowLight (Liang et al., ICCV23) and EvLight (Liang et al., CVPR24). This blurring is particularly noticeable around edges, such as those of the box under the desk, which could impair the network’s effectiveness in applications requiring high-detail preservation.

•	Table 3, case #6, reveals that disabling the prompt merge component results in a slight PSNR decrease but a corresponding SSIM increase. This discrepancy suggests that while prompt merging contributes to maintaining overall pixel-level fidelity (PSNR), it may slightly compromise structural similarity (SSIM). Further analysis of this trade-off could provide insights into the optimal configuration for different scenarios.

### Questions
•	Since B controls the brightness of the output image, it is not related to the input images. Consider a case, if I want to reconstruct a bright image (set B=0.8), but with two different input images (one is bright, one is dark), how the result images will be?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper collects a dataset named SEE-600K, consisting of 610126 images and corresponding events across 202 scenarios, each featuring an average of four lighting conditions with over a 1000-fold variation in illumination. Besides, it proposed a framework effectively utilizes events to smoothly adjust image brightness through the use of prompts.

### Strengths
* The dataset is the first event-based dataset covering a broader luminance range. 
* The proposed method achieves the state-of-the-art performance. I like the idea about adjusting the brightness of images across a broader range of lighting conditions.

### Weaknesses
 * It seems that the proposed method cannot reconstruct HDR images, \ie, the output images are still LDR. However, in Line52, the authors mention the weakness of the event-based HDR reconstruction, but do not provide a solution. I think since the event camera could have some HDR properties, the output image should also have some HDR properties.

* The comparisons may not comprehensive enough. Please compare to more methods designed for event-based low-light enhancement such as [a,b,c]. Besides, it seems that the compared methods are not trained with the same loss function used in this paper, which could be not that fair enough. In addition, please also evaluate the results in the dataset used in EvLowlight.

* The writing quality can be further improved. There are some typos (\eg, line 234, cna --> can) need to be fixed, and the conference names in Ref should be unified (\eg, for CVPR, the authors use both " Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition" and " Proceedings of the IEEE/CVF conference on computer vision and pattern recognition").

  [a] Event-Guided Attention Network for Low Light Image Enhancement

  [b] Low-light video enhancement with synthetic event guidance

  [c] Exploring in Extremely Dark: Low-Light Video Enhancement with Real Events

### Questions
* The proposed dataset contains some artifacts, such as defocus blur (the normal light one in the first group of Fig12), false color (the normal light one in the first group of Fig13), \etc. I wonder why the authors do not consider to remove them. In addition, please analyze the influence of such kinds of artifacts to the performance of the proposed method and the compared methods.
* Does the proposed method consider the dynamic scenes? Does the proposed dataset contain frames with motion blur? Please analyze the influence of motion blur to the performance of the proposed method and the compared methods.
* Could you please show some examples with different  prompts (\ie, for each example, let us set multiple different B and check the results) and compare with other methods?

### Soundness
3

### Presentation
3

### Contribution
3
