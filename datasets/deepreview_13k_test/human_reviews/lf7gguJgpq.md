# UniINR: Unifying Spatial-Temporal INR for RS Video Correction, Deblur, and Interpolation with an Event Camera

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Images captured by rolling shutter (RS) cameras under fast camera motion often contain obvious image distortions and blur, which can be modeled as a row-wise combination of a sequence of global shutter (GS) frames within the exposure time. 
Naturally, recovering high-frame-rate GS sharp frames from an RS blur image needs to simultaneously consider RS correction, deblur, and frame interpolation.
Tacking this task is nontrivial, and to the best of our knowledge, no feasible solutions exist by far.
A naive way is to decompose the whole process into separate tasks and simply cascade existing methods; however, this results in cumulative errors and noticeable artifacts. 
Event cameras enjoy many advantages, \eg, high temporal resolution, making them potential for our problem. To this end, we propose the \textbf{first} and novel approach, named \textbf{UniINR}, to recover arbitrary frame-rate sharp GS frames from an RS blur image and paired event data. Our key idea is \textit{unifying spatial-temporal implicit neural representation (INR) to directly map the position and time coordinates to RGB values to address the interlocking degradations in the image restoration process}. 
Specifically, we introduce spatial-temporal implicit encoding (STE) to convert an RS blur image and events into a spatial-temporal representation (STR).
To query a specific sharp frame (GS or RS), we embed the exposure time into STR and decode the embedded features pixel-by-pixel to recover a sharp frame.
Our method features a lightweight model with only \textbf{$0.379 M$} parameters, and it also enjoys high inference efficiency, achieving $2.83 ms/frame$ in $31 \times$ frame interpolation of an RS blur frame.
Extensive experiments show that our method significantly outperforms prior methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method that recovers HFR and sharp global shutter frames from a rolling shutter blur image with the assistance of events. The authors propose an implicit neural representation to map the position and time coordinates to RGB image values. The experimental comparison with existing methods shows its effectiveness.

### Strengths
(1) Compared with the existing algorithms, the efficiency of the proposed algorithm is greatly improved.
(2) The experimental comparison shows that the proposed method exceeds the existing algorithms on both selected simulated and real dataset samples.

### Weaknesses
(1) A comprehensive performance comparison with EvShutter[1] is suggested, which has been published in CVPR2023.
(2) Both EvShutter and Evunroll demonstrate the performance of the proposed algorithms for eliminating the RS effect caused by fan rotation. To verify the robustness of the proposed method for different scenes, it is suggested to add similar experiments on real fan data.
(3) In Figure 5, it seems unfair and unnecessary to compare the running time of the proposed algorithm with the combination of EU and TL.
(4) The Evunroll also seems to take into account image deblurring and high frame-rate video output.

[1] Julius Erbach, Stepan Tulyakov, Patricia Vitoria, Alfredo Bochicchio, Yuanyou Li; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023, pp. 13904-13913.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a method named UniINR that interpolates arbitrary sharp global shutter (GS) frames from a single rolling shutter (RS) frame with the assistance of an event camera. The proposed model unifies the spatial-temporal implicit neural representation (INR) to address the interlocking degradations in the process of image restoration. Experimental results show that the proposed method outperforms other comparing methods in both quality evaluations and efficiency evaluations.

### Strengths
- The authors proposed the first novel yet efficient learning framework that can recover arbitrary frame-rate sharp GS frames from an RS blur image with corresponding event signals.

- The network is light-weighted with only 0.379M parameters, which is much smaller than EvUnroll model. Furthermore, the efficiency of this model is evident in its remarkably swift inference time, outperforming previous methods by a substantial margin.

- The performance of the proposed method is better than the state-of-the-art methods in both quantitative evaluations such as PSNR, SSIM, LPIPS, and visual results. The videos provided in the supplementary materials show the better performance of the proposed method.

### Weaknesses
- In the fusion of RS frames and event streams, there is no specific modules or design that focus on the domain gap between these two modalities. Since the format and information recorded by the intensity values and event signals are quite different.

- The event signals directly record the coordinates of events triggered at that time. Unlike the intensity frames, in one event voxel tensor, not all the pixels contain event signals. As a result, directly applying INR to event voxel tensor doesn’t consider the sparsity of event signals.

### Questions
- The comparison of the methods in this paper is a crucial aspect of evaluating its contributions. However, it has come to my attention that the performance of the compared methods in this submission does not appear to match the results presented in their original papers. It is imperative that a fair and comprehensive evaluation of the methods is conducted to ensure the validity of the comparisons and the reliability of the conclusions drawn in this work. Specifically, the performance of EvUnroll and JCD are worse than their original papers in some metrics and qualitative evaluations. Did the authors retrained their models in a different way?

- The authors claim for multiple times that they are the first to achieve arbitrary frame interpolation from an RS blur image and events. I think it is not that convincing. Because EvUnroll is also able to reconstruct multiple GS sharp frames.

- In the supplementary code, I found that in the SCN module, the input images and events are multiplied to get a feature called ‘x1’. I wonder what the meaning of multiplication is.

- In experimental part, this paper does not utilize optical flow for frame interpolation, unlike methods such as VideoINR [1] and MoTIF [2], which use INR to predict optical flow and then perform frame interpolation. However, in this paper, optical flow is not employed, and it seems that there is no dedicated comparison with optical flow methods in the conducted ablation experiments.

[1] Chen et al., VideoINR: Learning Video Implicit Neural Representation for Continuous Space-time Super-resolution, CVPR 2022.

[2] Chen et al., MoTIF: Learning Motion Trajectories with Local Implicit Neural Functions for Continuous Space-Time Video Super-Resolution, ICCV 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
In this paper, an event-based RS video correction, deblur, and interpolation method is proposed. Different from existing methods that decompose the whole process into multiple tasks, the authors take advantage of the high temporal resolution of event cameras to recover arbitrary frame-rate sharp GS frames from an RS blur image and paired event data. The key idea is unifying spatial-temporal implicit neural representation (INR) to directly map the position and time coordinates to RGB values to address the interlocking degradations in the image restoration process. Several experiments have been conducted to demonstrate the validity of the proposed method.

### Strengths
1.	The question of using event cameras for unified RS image enhancement makes sense, although event cameras have been explored on separate tasks. This is the first attempt.
2.	To this end, the authors propose a series of modules to perform the proposed task

### Weaknesses
1. Although the question raised is forward-looking, the technical details given by the authors are not very innovative, like some stacking of existing models. This makes it harder for reviewers to capture what the real contribution are. It is recommended that authors summarize the contribution visibly.
2. A more important issue is that of experimental validation. Overall experimental validation is not sufficient to prove the validity of the proposed methodology. The authors mention the use of two different experimental settings:
 (I) the single GS sharp frame restoration, i.e., the RS correction and deblurring. However, the EvUnroll is only the event-guided RS correction method, and eSL-Net is only the event-guided deblurring method. The target algorithm that the authors should be comparing should be correction+deblurring simultaneously. Thus, it is recommended that the authors use a combination of correction + deblurring algorithms for experimental comparisons, including but not limited to EvUnroll +eSL-Net, there are many event-guided deblurring algorithms available.
(II) a sequence of GS sharp frames restoration, i.e., the RS correction, deblurring and interpolation. However, the DeblurSR is the event-guided deblurring and interpolation method and does not target the correction. Therefore, the experimental comparison is not very fair. Meanwhile, the combination of EvUnroll and TimeLens does not target the deblurring.
Overall, the authors are advised to conduct a fairer and more comprehensive experimental comparison
3. Whether the algorithms being compared are using pre-trained models or re-trained? Reviewers noted that the compared methods were significantly lower than the proposed methods.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to recover arbitrary frame-rate sharp GS frames from an RS blur image and events. To this end, the authors introduce the spatial-temporal implicit neural representation (INR) to recover the sharp GS frames by mapping the position and time coordinates to RGB values. The input RS blur image and events are fused to construct a spatio-temporal representation and extract features from them at any time and position. This method has a lightweight and fast network structure, and also achieves high image reconstruction performance.

### Strengths
1. The authors thoroughly explain the framework and the proposed INR representation is experimentally verified for its ability to represent spatio-temporal features. 
2. This method has a lightweight and fast network structure, and also achieves high image reconstruction performance.

### Weaknesses
1. The fusion of events and images is completely end-to-end, with no explicit connection between the exposure time and the timestamp in events. This looks like a whole black box and lacks interpretability. There are established methods that associate exposure time, optical flow, and events, which is more intuitive, but of course introduces more computation, which is a key claim of this method.
2. Visual comparisons on real dataset does not show significant differences. Are there more obvious samples in the dataset? Otherwise I don't think it can support the generalizability of the model.
3. In C.5 of the Supplementary Material, the author mentions that concat can perform better than addition, so why does the author continue to use only addition?

### Questions
The authors have done a lot of explanations and experiments and have also fully demonstrated the effectiveness of the INR representation for RS deblurring and corr. However, I don't see much new from the model design. This is neither the first application of the INR representation to event-based vision, nor is it an exciting one. My opinion is borderline reject.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
