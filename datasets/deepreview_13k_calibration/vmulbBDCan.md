# Revolutionizing EMCCD Denoising through a Novel Physics-Based Learning Framework for Noise Modeling

- Decision: Accept
- Avg Score: 5.33
- Scores: 3, 5, 8

## Abstract
Electron-multiplying charge-coupled device (EMCCD) has been instrumental in sensitive observations under low-light situations including astronomy, material science, and biology. 
Despite its ingenious designs to enhance target signals overcoming read-out circuit noises, produced images are not completely noise free, which could still cast a cloud on desired experiment outcomes, especially in fluorescence microscopy.
Existing studies on EMCCD's noise model have been focusing on statistical characteristics in theory, yet unable to incorporate latest advancements in the field of computational photography, where physics-based noise models are utilized to guide deep learning processes, creating adaptive denoising algorithms for ordinary image sensors.
Still, those models are not directly applicable to EMCCD.
In this paper, we intend to pioneer EMCCD denoising by introducing a systematic study on physics-based noise model calibration procedures for an EMCCD camera, accurately estimating statistical features of observable noise components in experiments, which are then utilized to generate substantial amount of authentic training samples for one of the most recent neural networks.
A first real-world test image dataset for EMCCD is captured, containing both images of ordinary daily scenes and those of microscopic contents.
Benchmarking upon the testset and authentic microscopic images, we demonstrate distinct advantages of our model against previous methods for EMCCD and physics-based noise modeling, forging a promising new path for EMCCD denoising.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a physics-based noise model for EMCCD cameras. The statistical model includes some typical noise components for EMCCD sensors, and a calibration method is proposed for adaptation this noise model on each sensor. Through careful noise modeling and calibration, the authors synthesize realistic EMCCD noise data for training, and effectively improve the learning of deep denoisiers in both macroscopic testset and microscopic testset.

### Strengths
- The paper introduces the first EMCCD denoising method utilizing physics-based noise modeling method.
- The overall writing of this paper is good and easy to follow.

### Weaknesses
 - This paper proposes the first noise modeling method for EMCCD sensors, and there are indeed some new adaptations on this sensor type. However, the main idea borrows many contributions from the similar task of CMOS noise modeling, and seems to be a EMCCD-version of ELD [1]. Specifically, the entire pipeline, i.e., physics-based noise modeling ->  calibration -> synthesis -> denoise pipeline is the same with ELD. The noise components and calibration process are also similar with ELD. In addition, the modeling of FPN and pre-processing operation comes from PMN [2] .
- For Fig. 7, why ELD presents banding patterns, even after calibration using the target device? ELD calibrates row noise using bias frames, and the variance for row noise would be close to zero on sensors without obvious banding patterns if correctly calibrated. I wonder why ELD still causes such row patterns on EMCCD sensors.
- There should be more comparisons with sota methods, for both noise modeling and self-supervised denoising methods. For example, [3] proposes a general noise modeling method which uses poisson sampling for signal-dependent noise and GAN for signal-independent noise. I think [3] can also handle EMCCD sensors. Stronger baselines for self-supervised methods are also recommended to compare [4].
- I concern that it is not rigorous to use SID clean images to synthesize noisy pairs for training. Different from EMCCD sensors, SID dataset uses Sony cameras with CMOS sensors. Each sensor type has its own unique recipe for generating RAW data; even using clean images from one type of CMOS sensor to generate synthetic noisy pairs and then testing on real data from a different CMOS sensor can lead to negative effects, not to mention EMCCD data. Therefore, I believe that SID clean data is not a suitable choice for this application.
- Section 2.3 is not necessary since no deep denoiser architecture is proposed.

### Questions
Why ELD presents banding patterns in Fig. 7?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on EMCCD noisy data and denoising. The authors propose a physics-based noise model specifically for EMCCD cameras, which generates synthetic noisy images based on both the camera's properties and EMCCD-specific noise characteristics. This method makes the data clorser to real-life scenarios. They then train a deep learning model, Uformer, on these noisy image pairs for denoising. The Uformer model achieves better denoising results comparing to other methods.

### Strengths
1. Proposed the first dataset specific to EMCCD.
2. Provides a detailed and clear explanation of the noise model, including settings and parameter estimation.
3. The experiments compare the proposed method to other state-of-the-art methods.

### Weaknesses
1. For important equations, such as Eq. (1) and (5), the dimensions of each parameter are not provided, especially for N_p, f, and I. It is unclear if these are scalar values or matrices, and if matrices, what their dimensions are. The lack of clarity makes it difficult to reproduce the noise model and understand the underlying physics. Furthermore, in Eq. (1), the operation 'X' is not defined; it is unclear if this represents a matrix multiplication, element-wise multiplication, or another operation.
2. The denoising model, Uformer, should be discussed more thoroughly, with additional details explaining its design, such as the key differences compared to the Uformer model from Wang et al., 2024. The current explanation is insufficient to understand the specific adaptations made for EMCCD data. The paper should detail the specific modifications to the architecture, such as changes in the number of layers, filter sizes, or activation functions, and justify these choices.
3. The total number of image pairs is 224, which is relatively small, and the use of only 24 images for fine-tuning could lead to overfitting. The paper does not provide any analysis of the potential for overfitting, such as learning curves or validation set performance. The small dataset size raises concerns about the generalizability of the trained model to unseen EMCCD data.

### Questions
1. Could you provide the dimensional details of the variables in the key equations listed in the paper? It would help in understanding if you state that 'X' represents the inner product in Eq. (1).
2. It seems that adding N_r and N_q makes the image blurry. Could you visualize both N_r and N_q?
3. I feel that the proposed noise addition might be similar to the negative binomial low-photon noise. Could you explain the key differences between them?
4. In line 076, could you elaborate on the differences between the EMCCD and other models, if possible?
5. Could you provide a big-map plot or additional explanation of your Uformer model? What is the novel design aspect of this denoising model, and how does it differ from Wang's model?
6. Did you use any method to measure whether the results indicate overfitting? Will using data augmentation techniques to generate more data improve the model's accuracy? Perhaps training the model on simulated data and testing it on the original true data could be a way to assess the quality of the simulated data.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a novel approach to denoising images captured by electron-multiplying charge-coupled devices (EMCCDs) by introducing a physics-based noise model and a calibration procedure tailored for EMCCD-specific noise characteristics. The proposed method synthesizes authentic training data for a deep learning framework, enhancing denoising performance in fluorescence microscopy and achieving state-of-the-art results compared to existing methods. Additionally, they establish a comprehensive pipeline that connects noise parameter calibration with advanced neural network training strategies. This work paves the way for improved image quality in sensitive imaging applications across various scientific fields.

### Strengths
1. The introduction and the method of this paper are clear and easy to understand. Even readers who may not be familiar with EMCCD can grasp the motivation behind the noise model.

2. The novelty of this work is commendable. While many key designs are inspired by existing research, they incorporate unique adjustments specific to the characteristics of EMCCD sensors. The analysis of FPN, blooming effects, and readout noise heatmaps is particularly impressive.

3. The experiments presented in this paper are excellent, and I believe they will significantly contribute to sensitive imaging applications across various scientific fields.

### Weaknesses
1. In Eq. (5), D' includes $N_r$ and $N_q$; however, this seems unreasonable from a formulaic perspective. I suggest explaining why $B^{-1}$ doesn't affect $N_r$ and $N_q$. For instance, it might be beneficial to analyze the expected interactions between these two components. Specifically, the blooming effect, which is a charge overflow phenomenon, should not directly impact the readout noise ($N_r$) or the quantization noise ($N_q$), which are introduced during the analog-to-digital conversion. The equation implies that the inverse blooming correction is applied to these noise components, which is physically inconsistent. A more detailed explanation of the physical model and the calibration process is needed to justify this formulation.

2. Figure 3(b) appears to exhibit some abrupt transition points (e.g., log(time) = -7, -4), and the explanation provided in L252-255 seems insufficient to cover this phenomenon. Please confirm the reproducibility of these data and clarify why an S-shaped curve is used instead of multiple piecewise functions. The S-shaped curve, while providing a smooth fit, may not accurately capture the underlying physical processes, especially if these transitions are due to distinct circuit behaviors. If these transition points are related to circuit switching, a piecewise function fitting, similar to what has been reported in PMN, should be employed. The lack of a clear justification for the S-shaped curve raises concerns about the accuracy of the FPN model, particularly at these transition points.



### Questions
### Original Question
The relationship between the ablation study and the proposed method in this paper is unclear. 

As it stands, I find it difficult to directly correlate the FPNt, blooming effect, and readout noise heatmap with the ablation learning presented. Additionally, the current preprocessing appears to resemble contributions from PMN rather than from this work. 

I suggest clarifying the incremental contributions of the proposed method in the experiments to emphasize the original contributions of this paper.

### After Rebuttal
The authors have addressed my concerns.

I found the authors’ response to reviewer e1uJ very well-written. This work stands out because it takes a practical, problem-specific approach, using appropriate innovations to solve a real-world task. Looking at recent noise modeling research, I consider LLD [1] and PNNP [2] to be practical, while LRD [3] seems less so. LRD faces challenges with the data dependency problem, whether **paired data or noise models come first**, and the instability of the GAN-based training strategy. As a result, GAN-based noise modeling methods like LRD, CA-GAN, and Starlight often overfit the training data.  
For example, LRD, which includes a **Fournier Transformer Discriminator**, leaves visible row patterns in *Scene-07_IMG-0010* of the ELD dataset that are more noticeable than those in the ELD baseline, even though LRD achieves higher PSNR and SSIM scores. For this reason, I believe reviewer e1uJ’s initial rejection of this work was not well-founded.

In conclusion, I acknowledge the contributions of this paper and am inclined to keep my current rating.

**Reference**  
[1] Y. Cao, M. Liu, S. Liu, X. Wang, L. Lei, and W. Zuo, ‘Physics-Guided ISO-Dependent Sensor Noise Modeling for Extreme Low-Light Photography’, in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023, pp. 5744–5753.  
[2] H. Feng, L. Wang, Y. Huang, Y. Wang, L. Zhu, and H. Huang, ‘Physics-guided Noise Neural Proxy for Practical Low-light Raw Image Denoising’, arXiv preprint arXiv:2310. 09126, 2023.  
[3] F. Zhang et al., ‘Towards General Low-Light Raw Noise Synthesis and Modeling’, in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2023, pp. 10820–10830.

### Soundness
3

### Presentation
4

### Contribution
3
