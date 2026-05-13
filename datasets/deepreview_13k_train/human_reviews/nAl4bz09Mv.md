# DilateQuant: Accurate and Efficient Diffusion Quantization via Weight Dilation

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Diffusion models have shown excellent performance on various image generation tasks, but the substantial computational costs and huge memory footprint hinder their low-latency applications in real-world scenarios.
Quantization is a promising way to compress and accelerate models.
Nevertheless, due to the wide range and time-varying activations in diffusion models, existing methods cannot maintain both accuracy and efficiency simultaneously for low-bit quantization.
To tackle this issue, we propose DilateQuant, a novel quantization framework for diffusion models that offers comparable accuracy and high efficiency.
Specifically, we keenly aware of numerous unsaturated in-channel weights, which can be cleverly exploited to reduce the range of activations without additional computation cost. Based on this insight, we propose Weight Dilation (WD) that maximally dilates the unsaturated in-channel weights to a constrained range through a mathematically equivalent scaling. 
WD costlessly absorbs the activation quantization errors into weight quantization. The range of activations decreases, which makes activations quantization easy. The range of weights remains constant, which makes model easy to converge in training stage.
Considering the temporal network leads to time-varying activations, we design a Temporal Parallel Quantizer (TPQ), which sets time-step quantization parameters and supports parallel quantization for different time steps, significantly improving the performance and reducing time cost.
To further enhance performance while preserving efficiency, we introduce a Block-wise Knowledge Distillation (BKD) to align the quantized models with the full-precision models at a block level. 
The simultaneous training of time-step quantization parameters and weights minimizes the time required, and the shorter backpropagation paths decreases the memory footprint of the quantization process.
Extensive experiments demonstrate that DilateQuant significantly outperforms existing methods in terms of accuracy and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed DilateQuant framework to quantize the diffiusion model. First, they propose Weight Dilation (WD) that maximally dilates the unsaturated in-channel weights to a constrained range through a mathematically equivalent scaling.  Then they propose  Temporal Parallel Quantizer (TPQ), sets time-step quantization parameters and supports parallel quantization for different time steps. Finally, they propose Block-wise Knowledge Distillation (BKD) to align the quantized models with the full-precision models at a block level.

### Strengths
The authors have conducted extensive experiments on diffusion model tasks. We can see the proposed methods performs consistently well as compared to SOTA baselines. Besides, they conducted ablation studies to check the impact of each component and do efficiency analysis.

### Weaknesses
1) Ideas of scaling from activations to weights have been proposed in other papers.

2) Abalation studies is not convincing, details can be seen in Questions section.

3) I am doubting whether the module of BKD can be applied to large-scale diffusion models without training.

### Questions
1) For the scaling from activation to weight idea, it has been proposed in the paper AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration. It would be good if can compare with this paper. 

2) For the ablation studies in table 3, it lacks of one combination: WD(Yes) TPQ(No) BKD(Yes). Besides, comparing last two rows, seems the module WD doesn't bring significant contributions. This makes me doubt about the contributions of both WD and TPQ to the final performance. I just doubt maybe the BKD contributes most and nearly all to the performance improvement. Can you conduct one more experiment on the combination:  WD(No) TPQ(No) BKD(Yes)? Thanks.

3) For table 4, can you compare with baselines mentioned in Table 2 for Efficiency comparisons? The baselines in Table 4 seems out-dated.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a QAT framework dubbed DilateQuant for diffusion models, which consists of three components, i.e, Weight Dilation (WD), Temporal Parallel Quantizer (TPQ), and Block-wise Knowledge Distillation (BKD). The core contribution of the paper is the WD, which reduces the difficulty of activation quantization via equivalent scaling like SmoothQuant, and constrains the scaling intensity based on the maximum values of the output channels.

### Strengths
- The idea of the proposed Weight Dilation is novel and interesting.
- The paper is well-written and easy to understand.

### Weaknesses
 - The contributions of TPQ and BKD appear to be modest, especially for BKD, which is well explored in the previous quantization and neural architecture search literature.
- According to the ablation study (Table. 3), most of the improvement owes to knowledge distillation (BKD). Adding the WD to the BKD only improves the FID from 9.63 to 9.13. So is the key component actually the BKD?
- The paper only validates the method on Unet-based models, however, given that DiT-based diffusion models (e.g., SD3, Pixart, FLUX) have predominated, the reviewer believes doing experiments on DiT-based models can enhance the paper. Besides, there are some papers adopting the equivalent scaling for DiT quantization[1,2], the proposed method might need to be compared with them to show the superiority of the proposed equivalent scaling method (WD).
- The reviewer is confused about the motivation of WD. The paper states that outliers exist in all channels, so equivalent scaling methods of LLMs are not suitable for DMs, which is also illustrated by Figure 2b. However, since there are “outliers” in all channels, can we still call this “outlier” an outlier? It seems that the difference in activation values of DMs across input channels is not much less salient than LLMs.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Quantization is one of the most important method to reduce the model size and improve the computing efficiency. This manuscript proposes a novel quantization framework (DilateQuant ) for diffusion models, which offers comparable accuracy and high efficiency. The main contribution of the manuscript is that it introduces Weight Dilation (WD) that costlessly absorbs the activation quantization errors into weight quantization. In addition, a Temporal Parallel Quantizer (TPQ) and a Block-wise Knowledge Distillation (BKD) are further proposed to improve the quantization quality. However, the main issue is that this paper innovation. It combines a few existing methods to achieve a good quantization effect.

### Strengths
The most innovative point of this paper is the proposed Weight Dilation (WD) technology, which maximally expands the weight in the unsaturated channel to the restricted range by equivalent scaling mathematically. WD can absorb activation quantization error into weight quantization with no extra cost. The activation range is reduced, making it easy to quantify the activation. The weight range remains the same, which makes it easy for the model to converge during the training phase. DilateQuant is significantly superior to existing methods in terms of accuracy and efficiency.

### Weaknesses
1. It can be seen from Table 3 that the biggest innovation in this paper, WD, has little improvement on performance.
2. The full text lacks innovation. For example, TPQ and BKD in this paper are not innovative.
3. Setting the scale factor for the out-channel of weights is not a new method, which has been widely used in the channel-wise quantization.
4. The paper lacks the effect of image generation at higher resolution (i.e., 1024x1024).

### Questions
1. Please add the results of delta'x/delta x in Table 8
2. This work is strongly correlated with other equivalent scaling algorithms. Please add the results of W6A6 in Table 9 to demonstrate the generalization ability.
3. Please explain the difference between TPQ in this article and TLSQ in EfficientDM[1]. It seems that the training process is the only difference that each time step has different activation quantization parameters.
4. Please explain the block splitting method of BKD. In addition, please explain the difference between BKD and the related work BK-SDM[2].
5. If possible, please supplement the comparison results with PTQD[3] and TFMQ-DM[4].

[1] He Y, Liu J, Wu W, et al. Efficientdm: Efficient quantization-aware fine-tuning of low-bit diffusion models[J]. arXiv preprint arXiv:2310.03270, 2023.
[2] Kim B K, Song H K, Castells T, et al. Bk-sdm: A lightweight, fast, and cheap version of stable diffusion[J]. arXiv preprint arXiv:2305.15798, 2023.
[3] He Y, Liu L, Liu J, et al. Ptqd: Accurate post-training quantization for diffusion models[J]. Advances in Neural Information Processing Systems, 2024, 36.
[4] Huang Y, Gong R, Liu J, et al. Tfmq-dm: Temporal feature maintenance quantization for diffusion models[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 7362-7371.

### Soundness
3

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
The paper introduces DilateQuant, a quantization framework designed for diffusion models that enhances efficiency while preserving accuracy. It consists of three key components: Weight Dilation (WD), Temporal Parallel Quantizer (TPQ), and Block-wise Knowledge Distillation (BKD). WD scales activations to be more quantization-friendly without introducing additional quantization difficulty to weights. TPQ adapts to time-varying activations by setting specific quantization parameters for different temporal stages. BKD employs a block-level distillation strategy, transferring knowledge from a full-precision model to its quantized version, which reduces the backpropagation path and memory demands. Comprehensive experiments demonstrate that DilateQuant surpasses existing methods in reducing quantization errors and improving efficiency across diverse models and configurations.

### Strengths
The paper is written with exceptional clarity. The motivation is well-articulated and compelling. The proposed weight dilation introduces a novel technique for adjusting in-channel weights to minimize activation range while avoiding added complexities in weight quantization.

### Weaknesses
1. The proposed weight dilation method successfully maintains the max-min values of each out-channel weight unchanged, thereby avoiding additional quantization difficulties. However, there are potential limitations to consider. For example, if the index of an activation outlier coincides with the in-channel index corresponding to these max-min values, the method might struggle to effectively manage these outliers. In such scenarios, the proposed technique could encounter challenges in achieving its intended quantization effectiveness. It is not clear how frequently activation outliers coincide with max-min weight indices in diffusion models, and this could be a significant limitation if such coincidences are common.

2. The constraint in the proposed weight dilation method, which aims to maintain the max-min values of each out-channel weight unchanged, might be overly restrictive. A slight adjustment of these max-min values could potentially introduce minimal quantization errors while providing a more flexible approach to manage the issues noted in the previous point. This adjustment could enable the method to handle cases where the activation outlier index coincides with the in-channel index of max-min values. For instance, considering both the activation quantization error and weight error simultaneously could help determine the most effective channel-wise scaling. The current approach does not explore this possibility, which could limit its effectiveness in certain scenarios.

3. The proposed weight dilation method calculates channel-wise scaling based solely on the magnitude of weights, without considering activations. This approach might not sufficiently mitigate extreme activation outliers. A more comprehensive strategy that takes into account both the magnitudes of activations and weights could potentially offer a more balanced and effective solution for managing these outliers. The paper does not adequately compare the proposed weight dilation with existing methods that jointly consider the magnitudes of activations and weights to determine channel-wise scaling, such as SmoothQuant [1] and Outlier Suppression [2]. This lack of comparison makes it difficult to assess the relative merits of the proposed approach.

4. The novelty and contributions of the proposed Temporal Parallel Quantizer (TPQ) and Block-wise Knowledge Distillation (BKD) appear to be limited. Specifically, the TPQ’s methodology of assigning unique quantization parameters for each time step has already been addressed in prior works [3,4]. Furthermore, the use of block-wise reconstruction in BKD, although effective, follows a well-known path in the post-training quantization (PTQ) of diffusion models as in [3], [5], and [6]. The primary distinction lies in BKD’s approach: instead of relying solely on calibration, it updates weight parameters and quantization parameters through gradient-based methods. However, this distinction alone may not be sufficient to establish significant novelty.

### Questions
1. The formulations presented in Eqs. (10) and (11) may encounter issues if the denominator becomes zero, leading to undefined results. A safeguard or modification in these equations to handle zero denominators is necessary to ensure their correctness and stability under all conditions. For instance, adding a small epsilon value to the denominator could prevent such undefined outcomes.

2. The comparison of calibration sample numbers between DilateQuant and EfficientDM in Tables 1 and 2 seems inaccurate. EfficientDM operates as a data-free method that does not depend on traditional training data; instead, it employs random Gaussian noise to generate images for network-wide reconstruction. Therefore, the number of calibration samples for EfficientDM should be indicated as zero. It’s possible the authors intended to reference the number of training steps instead.

3. The ablation studies presented are inadequate. For instance, the performance impact of using Weight Dilation (WD) alone (without TPQ and BKD) is not clearly isolated in Table 3. It would be beneficial to provide specific results demonstrating the effect of implementing WD independently to better understand its individual contribution to the overall performance enhancements.

### Soundness
3

### Presentation
3

### Contribution
2
