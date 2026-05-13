# Depth Pro: Sharp Monocular Metric Depth in Less Than a Second

- Decision: Accept
- Scores: 6, 10, 3, 8, 6

## Abstract
We present a foundation model for zero-shot metric monocular depth estimation. Our model, Depth Pro, synthesizes high-resolution depth maps with unparalleled sharpness and high-frequency details. The predictions are metric, with absolute scale, without relying on the availability of metadata such as camera intrinsics. And the model is fast, producing a 2.25-megapixel depth map in 0.3 seconds on a standard GPU. These characteristics are enabled by a number of technical contributions, including an efficient multi-scale vision transformer for dense prediction, a training protocol that combines real and synthetic datasets to achieve high metric accuracy alongside fine boundary tracing, dedicated evaluation metrics for boundary accuracy in estimated depth maps, and state-of-the-art focal length estimation from a single image. Extensive experiments analyze specific design choices and demonstrate that Depth Pro outperforms prior work along multiple dimensions

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a new approaches for estimating a depth map from a single image. The paper claims many advantages of the method over competing approaches, in particular the ability to estimate absolute scale under all conditions (i.e., without metadata), high resolution, and speed. The approach includes a transformer-based architecture, hybrid training approach, and focal length estimation to address scale issues. Extensive experimental results are presented.

### Strengths
- Important task (monocular depth estimation)
- impressive visualizations (e.g. figure 1)
- Achieves an averaged best performance on multiple datasets and demonstrated great generalization for open-world images.
- Excels  in distinguish boundaries
- Evaluation across a large number of data sets/ablations. Of particular note is the difficulty of avoid cross-data set contamination (test samples appearing in training, etc.) and restricted access.

### Weaknesses
 - Method section is not clear enough. Missing model details.
- How are features 3-6 obtained since the images are splits into {1x,3x,5x} 384^2 and none of them matches the feature resolution at 48^2 and 96^2?
- what's the architecture of the patch encoder?
- What's the detailed architecture of the focal length head? How does this module fuse both multi-scale features and the features from the extra "image encoder for local length"? The role of the this estimation piece is critical in understanding how it is possible for the method to achieve absolute depth estimation even when camera parameters are absent but the description is lacking.
- Overall, the writing of this paper is poor. It's hard to follow both the proposed method and the experimental evaluation though the results are impressive.

### Questions
- the proposed method excels in detecting boundaries. Do the authors have a sense why this happens? Due to the multi-scale derivative objective? Ablations about the reason are encouraged.
- Fig. 4 is only mentioned in l457-458. No details are provided unless in their caption. It's hard to understand how DepthPro helps novel view synthesis.
- How does the proposed model handle images of an arbitrary scale?
- One claim of this paper is the efficient inference. Running time numbers should be reported. Currently they are only demonstrated in Figure 1.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper introduces a foundational model for single-image depth estimation, trained on a large collection of datasets. The approach results in high-resolution depth maps with sharp object boundaries and enables the estimation of camera intrinsic parameters. The model outputs metric-scale depth predictions and demonstrates its effectiveness across multiple datasets, outperforming previous methods in both quantitative and qualitative evaluations. The contributions of this work are significant, with the pre-trained model holding substantial potential for a range of downstream tasks.

### Strengths
1. High-Resolution Predictions: The model produces depth maps at resolutions as high as 1536 x 1536, attributed to its multi-scale vision transformer architecture.

2. Comprehensive Training: The use of extensive depth estimation datasets for training and testing demonstrates substantial effort in data processing. The pre-trained model is valuable to the community and holds potential for multiple downstream tasks.

3. Camera Intrinsic Estimation: The model can estimate camera intrinsic parameters and shows strong zero-shot generalization due to its training on diverse datasets, which is crucial for real-world scenarios where camera calibration is challenging.

4. Visual and Quantitative Superiority: The qualitative results clearly show better object boundary preservation compared to previous methods, and the quantitative evaluations across datasets highlight the model's excellent zero-shot performance. The evaluation on downstream tasks like image synthesis showcases the model’s adaptability.

### Weaknesses
1. Limited Novelty: Although effective, the proposed method's novelty is somewhat constrained as it leverages existing approaches. The loss functions and training strategy draw heavily from DPT (Ranftl et al., 2022), and the metric depth estimation follows ideas from Metric3D (Yin et al., 2023). More discussion on the unique aspects would strengthen the paper. Specifically, while the multi-scale vision transformer architecture enables high-resolution outputs, the core architecture and training methodology do not present a significant departure from prior work. The paper would benefit from a more detailed analysis of the architectural differences and a more in-depth discussion of how the specific combination of existing techniques leads to the observed performance gains. The claimed efficiency gains should be supported by a more thorough ablation study that isolates the impact of each architectural component.

2. Depth Consistency in Videos: While single-image results are impressive, depth consistency across video frames is not explored. Given the model’s metric-scale depth predictions, it would be valuable to assess its utility in video-based tasks such as visual SLAM, camera pose estimation, and 3D reconstruction. The lack of temporal consistency analysis is a notable gap, especially given the potential of metric-scale depth for these applications. The paper should at least acknowledge the limitations of the current approach in handling temporal coherence and suggest future research directions to address this issue.

### Questions
See weakness

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The proposed Depth Pro model employs a ViT architecture for zero-shot metric monocular depth estimation, targeting applications such as novel view synthesis. By employing patch-based, multi-scale processing, Depth Pro achieves high-resolution depth predictions while preserving real-time performance and edge sharpness. This paper introduces a two-stage training approach that integrates synthetic and real-world datasets, enhancing depth boundary accuracy. Furthermore, the model includes boundary evaluation metrics and a focal length estimation component, improving its robustness in handling images lacking metadata.

### Strengths
1. Structured Training Curriculum: The curriculum is specifically tailored to handle the unique strengths and weaknesses of synthetic and real-world datasets, resulting in a model that generalizes effectively while producing fine boundary details in depth maps.

2. Enhanced Boundary Evaluation Metrics: New metrics for evaluating depth boundaries address a gap in existing benchmarks by focusing on boundary precision, which is critical for applications like view synthesis that demand fine details.

### Weaknesses
1. Dependence on pretrained ViT with Limited Architectural Innovation: Depth Pro benefits from pretrained ViT backbones, yet its architecture primarily builds on existing elements rather than introducing fundamentally new mechanisms for depth estimation, which limits its architectural novelty. While the use of a ViT backbone is efficient, the paper does not explore alternative architectures or modifications to the ViT itself that could potentially lead to more accurate or robust depth predictions. The reliance on a pretrained model also raises questions about the transferability of the model to domains significantly different from those used for pretraining.

2. Heavy Reliance on Synthetic Data for Boundary-Sensitive Training: The model’s second-stage training emphasizes synthetic datasets for boundary sharpness. This reliance on synthetic data could impact generalization to real-world environments, particularly in complex or unstructured settings where boundaries are less distinct. The paper does not adequately address the potential for overfitting to the specific characteristics of the synthetic data, such as the idealized lighting and object shapes, which may not translate well to the variability found in real-world scenes. Furthermore, the evaluation of boundary sharpness on real-world data is not sufficiently detailed to fully validate the effectiveness of the synthetic data-based training.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces Depth Pro, a model for zero-shot metric monocular depth estimation that generates high-resolution depth maps with precise boundary details at sub-second processing speeds. Key innovations include a multi-scale vision transformer architecture, a mixed training regimen with real and synthetic data for improved accuracy, and a dedicated evaluation approach for boundary sharpness. The model also features state-of-the-art focal length estimation without the need for camera metadata. Depth Pro outperforms prior approaches in accuracy and efficiency, making it suitable for applications like novel view synthesis.

### Strengths
- The model demonstrates strong zero-shot performance for metric depth estimation, effectively handling diverse input images without fine-tuning.
- It achieves superior focal length estimation accuracy, which enhances depth map scaling and generalization across different image conditions.
- Comprehensive ablation studies are provided to analyze the impact of key architectural and training choices, showcasing the robustness of the proposed method.
- The experiments are conducted on a wide range of datasets, underscoring the model’s effectiveness and applicability across various scenarios.
- Detailed training procedures are described, allowing for reproducibility and providing insights into the model’s development process.
- The method exhibits higher edge accuracy compared to conventional techniques, maintaining competitive inference times.
- It outperforms state-of-the-art approaches, such as DepthAnything, DepthAnything v2, and Marigold, with clear comparative analysis highlighting these advancements.

### Weaknesses
The most critical components that influence performance and boundary accuracy among various technical contributions are not clearly highlighted, leaving ambiguity about which elements contribute most to the model's success.

### Questions
1. If the loss function were designed using depth instead of canonical inverse depth, would the results differ? Have you conducted any experiments to compare these approaches?
2. Among the various technical contributions (e.g., curriculum learning, focal length estimation, and the patch encoder with multiple scales), which components most significantly affect the overall performance metrics (e.g., abs_rel, δ_1) and boundary accuracy, respectively? Although multiple technical contributions are mentioned, it is unclear which are the most impactful.
3. Is there any tradeoff between overall performance and boundary accuracy related to certain hyperparameters in the deep neural network or the training loss?
4. For calculating the final depth, does the proposed method use the predicted inverse depth C, the predicted focal length f_px, and the ground-truth width w, as in the equation D = f_px / (wC)?
5. As I understand it, all experiments were conducted with evaluation using metric scale depth, without median-scaling evaluation. Is my understanding correct?
6. Have you conducted experiments on fine-tuning the proposed model (DepthPro)? If so, is there a significant performance improvement between the zero-shot setting and fine-tuning?
7. What is the training time and GPU resources required to train the proposed method?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework for high-resolution metric depth estimation, demonstrating both excellent organization and a well-articulated motivation. The qualitative outcomes are impressive, and the quantitative results also demonstrate the state-of-the-art performance. The authors assert four main contributions: (1) an innovative network architecture, (2) a newly proposed evaluation metric for boundary tracing, (3) newly designed loss functions, and (4) the capacity to estimate camera focal length.

### Strengths
- This paper is well-written and motivated.
- The proposed method demonstrates impressive performance.
- It addresses the metric monocular depth estimation problem, a crucial task with significant application prospects.
- The method estimates camera focal length, eliminating the need for image metadata—a practical advancement.
- The experiments detailed in the main text and appendix are comprehensive and solid.

### Weaknesses
There are some minor issues:
- There are a few unclear statements regarding Figure 3:
  - Along which dimension does the concatenation operation perform?
  - What is the specific implementation of the Merge operation?
- At Line 234, the statement "produces a feature tensor at resolution 24 × 24 per input patch (features 3 – 6 in Fig. 3)" seems to not coincide with the figure label.

### Questions
- Marigold and Depth Anything have demonstrated that using synthetic training data can effectively improve details in depth prediction. Depth Pro also uses synthetic data to enhance high-frequency details in the depth map, yet its predicted boundaries are significantly better than those of existing methods. What is the main reason for this?significantly better than the existing methods. What is the main reason for this?
- Comparative methods such as Depth Anything and Marigold are trained with low-resolution images, while Depth Pro is trained with high-resolution images. Is this the reason why Depth Pro achieves better detail in depth prediction?
- According to Table 13, Depth Pro appears to use more training data than other competitors. Can you compare the scale of training data used by Depth Pro with that of other competitors?
- According to Table 1, Depth Pro has a significant gap with the best performing methods on some datasets (such as ETH3D). Can you analyze the reasons for this discrepancy?

### Soundness
4

### Presentation
4

### Contribution
3
