# R2Det: Exploring Relaxed Rotation Equivariance in 2D Object Detection

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Group Equivariant Convolution (GConv) empowers models to capture equivariant features and explore underlying symmetries in data, improving performance. However, real-world scenarios often deviate from ideal symmetric systems caused by physical permutation, characterized by non-trivial actions of a symmetry group, resulting in asymmetries that affect the outputs, a phenomenon known as symmetry breaking. Traditional GConv-based methods are constrained by rigid operational rules within group space, assuming data remains strictly equivariant under limited group transformations. This limitation makes it difficult to adapt to Symmetry-Breaking and non-rigid transformations. Motivated by this, we mainly focus on a common scenario: rotational Symmetry-Breaking. By relaxing strict group transformations within Strict Rotation-Equivariant group $\mathbf{C}_n$, we redefine a Relaxed Rotation-Equivariant group $\mathbf{R}_n$ and introduce a novel Relaxed Rotation-Equivariant GConv (R2GConv) with only a minimal increase of $4n$ parameters compared to GConv. Based on R2GConv, we propose a Relaxed Rotation-Equivariant Network (R2Net) as the backbone and develop a Relaxed Rotation-Equivariant Object Detector (R2Det) for 2D object detection. Experimental results demonstrate the effectiveness of our R2GConv in natural image classification, and R2Det achieves excellent performance in 2D object detection with improved generalization capabilities and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces R2Det, a novel object detection model that explores Relaxed Rotation-Equivariance (RRE) to handle real-world scenarios where strict rotational symmetries are often violated. RRE is incorporated into group convolution by introducing the Relaxed Rotation-Equivariant Filter (R2EFilter) and the Relaxed Rotation-Equivariant Group Convolution (R2GConv). The paper further proposes R2Net for image feature extraction and R2Det for 2D object detection, achieving improved convergence and performance with fewer parameters.

### Strengths
This work makes a valuable contribution to the field of object detection by addressing the limitations of traditional, strictly rotation-equivariant models and exploring the potential of RRE through ER2GConv. 
This work presents a significant contribution to the field of object detection by addressing a crucial limitation in handling real-world scenarios, where strict rotational symmetries are rarely observed. The authors introduce a novel approach, Relaxed Rotation-Equivariance (RRE), which effectively addresses this limitation. The proposed R2Det model leverages RRE to achieve remarkable performance with a significantly reduced parameter count compared to other leading models. This showcases the model's efficiency and its ability to achieve high accuracy while requiring fewer computational resources. The paper further strengthens its arguments with a rigorous mathematical framework, providing theoretical underpinnings for RRE's effectiveness. Moreover, the plug-and-play nature of the proposed ER2GConv layer allows for seamless integration into existing object detection models, making it a versatile and readily applicable technique. This combination of novelty, theoretical soundness, efficiency, and integration capabilities makes this research highly valuable for advancing the field of object detection.
However, the paper lacks sufficient exploration of the key parameter b, which controls the perturbation factor Δ. While the paper mentions that b=0.1 yields the best results, more extensive experiments with intermediate values of b would strengthen the argument for the necessity of this perturbation parameter and provide a deeper understanding of its influence on performance. Additionally, it would be beneficial to investigate the performance of R2Det in larger configurations, such as “R2Det-L”, and compare its performance to the corresponding “Large” versions of YOLO models. This would provide a more complete assessment of the model's scalability and potential limitations in handling more complex and computationally demanding tasks. The clarity and persuasiveness of the paper can be further enhanced by addressing these specific concerns, and by providing concise explanations for abbreviations like SO(2) (Special Orthogonal Group in 2D space) and ER2GCBA (Efficient Relaxed Rotation-Equivariant Group Convolution plus -BA, where -BA likely refers to a specific architectural component or technique).

* This work makes a valuable contribution to the field of object detection by addressing the limitations of traditional, strictly rotation-equivariant models and exploring the potential of RRE through ER2GConv.
* The authors introduce a novel approach, Relaxed Rotation-Equivariance (RRE), which effectively addresses the limitation of handling real-world scenarios where strict rotational symmetries are rarely observed.
* The proposed R2Det model leverages RRE to achieve remarkable performance with a significantly reduced parameter count compared to other leading models, showcasing the model's efficiency and ability to achieve high accuracy while requiring fewer computational resources.
* The paper further strengthens its arguments with a rigorous mathematical framework, providing theoretical underpinnings for RRE's effectiveness.
* The plug-and-play nature of the proposed ER2GConv layer allows for seamless integration into existing object detection models, making it a versatile and readily applicable technique.

### Weaknesses
 * The paper lacks sufficient exploration of the key parameter b, which controls the perturbation factor Δ, and more extensive experiments with intermediate values of b would strengthen the argument for the necessity of this perturbation parameter.
** In page 8, Figure 4(a) and Table 1, the results presented demonstrate a minimal improvement in AP when (b=0.1) compared to (b=0). 
** Performance deteriorates when (b>0.1), and it would be beneficial to conduct more thorough experiments, especially within the interval [0, 0.1], e.g., 0.02, 0.05, to provide a more definitive analysis of the value of b and its impact on the model’s performance. 
* It would be beneficial to provide concise explanations for abbreviations like SO(2) (Special Orthogonal Group in 2D space) and ER2GCBA (Efficient Relaxed Rotation-Equivariant Group Convolution plus -BA, where the meaning of -BA remains undefined).
* It would be beneficial to investigate the performance of R2Det in larger configurations, such as 'R2Det-L', and compare its performance to the corresponding 'large' versions of YOLO models, to provide a more complete assessment of the model's scalability and potential limitations in handling more complex and computationally demanding tasks.
* It would be beneficial to include a comparative study with more recent and advanced object detection models, such as YOLOv11 and other models, to provide a broader context and demonstrate the model's performance relative to the state-of-the-art.
* I noticed an interesting discrepancy in the results presented on page 8, specifically in Table 1 and Table 2. While both tables use the VOC test dataset, the reported AP scores for the SRE (b=0) model in Table 1 (C4) differ from the reported SRE scores in Table 2 (C4).
** In Table 1, the AP50(%) and AP50:95(%) for b=0 are 83.8 and 64.4 respectively, whereas in Table 2, the SRE AP50(%) and AP50:95(%) for C4 are 82.9 and 64.2.
** This discrepancy raises a question regarding potential differences in the implementation of SRE versus the b=0 setting, or if it could be due to variations in the experimental runs. The authors may please comment on this interesting observation and clarify the reasons behind the difference in AP scores.

### Questions
* The paper lacks sufficient exploration of the key parameter b, which controls the perturbation factor Δ, and more extensive experiments with intermediate values of b would strengthen the argument for the necessity of this perturbation parameter.
* Performance deteriorates when (b>0.1), and it would be beneficial to conduct more thorough experiments, especially within the interval [0, 0.1], e.g., 0.02, 0.05, to provide a more definitive analysis of the value of b and its impact on the model’s performance. 
* It would be beneficial to provide concise explanations for abbreviations like SO(2) (Special Orthogonal Group in 2D space) and ER2GCBA (Efficient Relaxed Rotation-Equivariant Group Convolution plus -BA, where the meaning of -BA remains undefined).
* It would be beneficial to investigate the performance of R2Det in larger configurations, such as 'R2Det-L', and compare its performance to the corresponding 'large' versions of YOLO models, to provide a more complete assessment of the model's scalability and potential limitations in handling more complex and computationally demanding tasks.
* It would be beneficial to include a comparative study with more recent and advanced object detection models, such as YOLOv11 and other models, to provide a broader context and demonstrate the model's performance relative to the state-of-the-art.
* This discrepancy raises a question regarding potential differences in the implementation of SRE versus the b=0 setting, or if it could be due to variations in the experimental runs. The authors may please comment on this interesting observation and clarify the reasons behind the difference in AP scores.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper points out that symmetry breaking often occurs in the real world. However, traditional GConv-based methods are limited by strict operational rules in group space, ensuring strict equivariance of features only under a limited set of group transformations, making them difficult to adapt. The paper defines the relaxed rotation-equivariant group R4 based on the strict rotation-equivariant group C4 and proposes the relaxed rotation GConv (R2GConv). The paper constructs R2Det using GConv and its derived convolutional structures, achieving excellent results on the PASCAL VOC and MS COCO 2017 datasets, and also verifies the good performance of R2Det in classification and segmentation tasks.

### Strengths
1. The paper introduces a novel relaxed rotation-equivariant group convolution (R2GConv), which extends existing equivariant neural networks (ENNs). Additionally, the resulting model, R2Det, shows strong performance across various datasets and tasks.

2. The authors enhance the R2GConv module by incorporating depth-wise and point-wise convolution, and conduct extensive comparative and ablation experiments to confirm its positive impact on the outcomes.

3. The paper is well-written and easy to understand.

### Weaknesses
1. Dataset Limitation: The selected datasets, PASCAL VOC and MS COCO 2017, do not emphasize rotation characteristics, which reduces the impact and relevance of the experimental results. To better highlight the effects of SRE and RRE modeling, rotation-specific object detection datasets should be used. The lack of explicit rotational variance in these datasets makes it difficult to isolate and evaluate the benefits of the proposed relaxed rotation-equivariant group convolution. The experiments may not fully demonstrate the method's ability to handle objects with arbitrary orientations, which is a key motivation for the proposed approach.

2. Insufficient Baseline Comparison: it would be beneficial to include comparisons with established models in rotation object detection, such as ReDet and FRED, to strengthen the evaluation and provide more convincing evidence. The absence of comparisons with these models, which are specifically designed for rotation-invariant or equivariant object detection, makes it difficult to assess the relative performance and advantages of the proposed R2Det. Without such comparisons, it is unclear whether the improvements observed are due to the relaxed rotation equivariance or other factors.

### Questions
1. In Figure 1 on the left, the input in the lower left corner mapped to the output in the upper right corner should use the relaxed rotation-equivariant function.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper first discusses a limitation of strict equivariance for real-world applications (i.e. symmetry breaking) and then introduces building blocks and architectures for relaxed rotation equivariance. It focuses mostly on 2D object detection.
More specifically, the authors introduce a relaxation of the group operations on the $n$-order cyclic rotation group $C_n$ by adding learnable perturbations to existing (strict) rotation equivariant filters. They then design different relaxed rotation-equivariant group convolutional modules that serve as building blocks for two architectures: the relaxed rotation-equivariant network (R2Net) and object detector (R2Det).

Experimentally, the paper compares different perturbation levels and shows that a small perturbation leads to stronger performance than strict equivariance (i.e., with no perturbation) on 2D detection datasets (PASCAL VOC and COCO). The new method is also compared to the YOLO series detectors and achieves much higher performance-compute trade-offs. Finally, the R2Net and R2Det methods are evaluated respectively on image classification and instance segmentation.

### Strengths
- The method demonstrates impressive performance-compute trade-offs on the object detection task.
- The authors evaluated the effect of the main contribution (i.e., the learnable perturbation) on performance. Furthermore, its effect on the learned features is well illustrated in Figure 5.

### Weaknesses
1. The provided background and naming of methods are misleading and partially incorrect. Indeed, **relaxed** equivariance is defined in [1] as a relaxation that allows breaking the symmetry of inputs and mapping to arbitrary orbit types when necessary. Note that the output of the function is still predictable under the transformation of the input. While in R2Det, the relaxed equivariance is mistakenly defined (definition 1, line 161) using the definition of **$\epsilon$-approximate** equivariance (despite referring to the definition from [2] which correctly names it **$\epsilon$-approximate** equivariance). Furthermore, the introduced filter is called a "relaxed rotation-equivariant filter" but is implemented by allowing for some learnable perturbation, which is therefore **NOT** a **relaxed** rotation-equivariance module. The learnable perturbation, denoted as $\Delta$, allows for deviations from strict equivariance. However, the degree of this deviation, controlled by $\Delta$, should be quantified to understand how closely the model adheres to the properties of relaxed equivariance as defined in [1]. Without a clear measure of this deviation, it is difficult to assess the extent to which the proposed method aligns with the theoretical framework of relaxed equivariance. Figure 1a also incorrectly illustrates the problem being tackled in the paper. Notably, relaxed equivariance was introduced as an alternative to noise-injection methods: "offering an alternative to the noise-injection methods" (see the abstract from [1]). The above-mentioned problems make the paper's claims incorrect and could lead to important misunderstandings of already established concepts.
2. The paper is not easy to read, mainly because of: the abundant use of abbreviations and acronyms (ENN, GConv, RRE, SRE, NRE, R2Filter, R2Lift, R2GConv, DR2GConv, PR2GConv, ER2GConv, ER2GCBA, ...), multiple typos  ("Rotationa-Equivariant" line 25, "we further exploring" line 62, "More analysis can refer to" line 167, "converge when 66-epoch" and  "converges at about 198 in the epoch" lines 401-402, ...) and over-loaded illustrations (e.g., Figure 2 and 3).

### Questions
Suggestions:
- (Weaknesses 1.): The reviewer suggests that the authors fix the mistakes in the preliminary section, and rename the methods and claims accordingly.
- (Weaknesses 2.): The reviewer suggests the authors to fix typos, to reduce the number of acronyms in plain text (e.g., define only R2GConv and call its variants "point-wise R2GConv", "efficient R2GConv", ...), and to only include *simple* and *intuitive* figures in the main article to simplify the reading. The more detailed diagrams could then be moved to appendix.

Questions:
- The performance gap between different $n$-norder cyclic rotation groups is substantial (Table 3). What is the reason for such a gap? Is it only due to the "newer equivariant angles"? How would the introduced architecture perform without equivariance? Also, is there an intuitive explanation for why it is beneficial for 2D object detection (with non-rotating bounding boxes, like on COCO) to use $C_8$ instead of $C_4$, despite the output (bounding boxes) only having symmetries in the $C_4$ group?
- Experiments showed that on both PASCAL VOC and COCO, performance with strict equivariance is inferior to that with the approximate equivariance introduced in the paper. For intuition, could the authors provide specific (intuitive or experimental) examples of 2D object detection in which it is beneficial to break the strict rotation equivariance?

I am willing to raise my rating if my concerns are addressed.

### Soundness
4

### Presentation
3

### Contribution
3
