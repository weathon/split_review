# Denoising as Adaptation: Noise-Space Domain Adaptation for Image Restoration

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
Although learning-based image restoration methods have made significant progress, they still struggle with limited generalization to real-world scenarios due to the substantial domain gap caused by training on synthetic data.
Existing methods address this issue by improving data synthesis pipelines, estimating degradation kernels, employing deep internal learning, and performing domain adaptation and regularization. Previous domain adaptation methods have sought to bridge the domain gap by learning domain-invariant knowledge in either feature or pixel space. However, these techniques often struggle to extend to low-level vision tasks within a stable and compact framework.
In this paper, we show that it is possible to perform domain adaptation via the noise space using diffusion models. 
In particular, by leveraging the unique property of how auxiliary conditional inputs influence the multi-step denoising process, we derive a meaningful \textit{diffusion loss} that guides the restoration model in progressively aligning both restored synthetic and real-world outputs with a target clean distribution. We refer to this method as \textit{denoising as adaptation}. 
To prevent shortcuts during joint training, we present crucial strategies such as channel-shuffling layer and residual-swapping contrastive learning in the diffusion model. They implicitly blur the boundaries between conditioned synthetic and real data and prevent the reliance of the model on easily distinguishable features.
Experimental results on three classical image restoration tasks, namely denoising, deblurring, and deraining, demonstrate the effectiveness of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The core of the method is a two-model setup: a restoration network and a diffusion model. The restoration network is trained to clean degraded images, while the diffusion model acts as a noise-space guide, enforcing an alignment between synthetic and real-world restorations and the clean target distribution. The authors validate their approach on tasks such as image denoising, deblurring, and deraining, showing it consistently outperforms both feature-space and pixel-space domain adaptation methods.

### Strengths
The strengths of this work lie in the following: 
- A novel approach for iteratively using a diffusion model as a proxy model for denoising in noise space 
- The authors introduce channel-shuffling and residual-swapping strategies, ensuring robust generalization. 
- The diffusion model is used only during training
- The final restoration model achieves SOTA results across multiple restoration tasks.

### Weaknesses
For de-raining results, the authors should show results where the background is not empty, e.g. where there is more content in the image besides a gray background as in Figure 5.

### Questions
Can the method be trained with multiple tasks simultaneously since it is technically (low-level) task agnostic?

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
3

### Summary
This paper presents an image restoration approach that utilizes diffusion models to address domain adaptation issues. The method adjusts restored results in the pixel-wise noise space, resulting in significant improvements in low-level visual appearance while operating within a compact and stable training framework. To avoid shortcut learning, the method employs channel index shuffling and a residual-swapping contrastive learning strategy. Experimental results demonstrate this approach outperforms existing feature-space and pixel-space domain adaptation methods across various tasks, such as image denoising, deraining, and deblurring.

### Strengths
1. The method enhances image restoration performance by effectively bridging the gap between synthetic and real-world data.

2. The approach can be easily integrated with various restoration networks, demonstrating improved performance even with more complex architectures.

### Weaknesses
1. The writing in this paper is not very clear, and I found the third section particularly confusing regarding how the proposed method leverages the mapping learned from synthetic datasets to be applied to real datasets. There must be some form of "information leakage" involved—this is a proactive "leakage" that helps bridge the gap between different domains. However, the authors do not provide a clear explanation of this process, and it appears that channel shuffling plays a key role in this function. A more explicit clarification from the authors would be beneficial.

2. The paper lacks runtime for the proposed method.

### Questions
Could the authors give concrete examples of situations where their proposed method fails to deliver the expected results?

I am impressed by the significant improvements reported by the authors. I wonder how the results would compare if the model were trained directly on a paired real dataset and then tested on corresponding real data.

I expect a direct and clear explanation from the authors regarding how the knowledge is "leaked" from the synthetic domain to the real domain in the proposed method.

### Soundness
3

### Presentation
2

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
The introduces an approach to improve the generalization of image restoration models by addressing the domain gap between synthetic and real-world data using noise-space adaptation with diffusion models. The method utilizes diffusion loss, which is optimized during joint training with the restoration network. Key strategies, such as channel-shuffling and residual-swapping contrastive learning, are employed to prevent shortcut learning, ensuring the model effectively restores images rather than relying on trivial cues. The diffusion model is then discarded, leaving a robust restoration network. Experimental results show the method outperforms existing domain adaptation techniques.

### Strengths
1. The idea of incorporating diffusion loss in domain adaptation for image restoration is novel.
2. The proposed method can be applied to a variety of restoration tasks, including denoising, deblurring, and deraining, with demonstrated performance gains in the experiments.
3. The use of channel-shuffling and residual-swapping to prevent shortcut learning is well-motivated, and ablation studies show that this technique is crucial for performance improvement.
4. The paper is well-written and easy to understand.

### Weaknesses
1. Although ground-truth images from the real dataset are not used for training, degraded images from the same dataset are presented during training, which blurs the distinction between the training and inference stages. To better validate the generalization ability of the proposed framework, driven solely by the inference stage, evaluation on fully unseen datasets (e.g., Nam or PolyU datasets for denoising) should be included.
2. The authors do not provide an analysis of training time, which seems to be a key limitation of the proposed approach. There should be a detailed comparison of training complexity with other models, not just comparisons of inference performance.
3. Ablation studies on the sensitivity to hyperparameters (e.g., beta, gamma) are lacking, particularly as the authors state that these values were chosen empirically.
4. The performance gains compared to Vanilla baseline (trained only with synthetic datasets), while present, are relatively small for deraining and deblurring tasks. Especially for deblurring task, gain is less than 0.2dB.

### Questions
Please refer to the Weaknesses for the main questions.

1. How does the model perform on synthetic degradations? Are there significant performance trade-offs due to the domain-adaptation process?
2. Would it be possible to provide quantitative metrics (e.g., PSNR) alongside the visual results (e.g., in Figures 4 and 5) to better illustrate the restoration performance?
3. The paper seems to mainly demonstrate the performance on denoising task, which shows the highest performance gain. Why does the proposed idea fit substantially better for denoising?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- While traditional domain-adaptation methods have focused on adaptation in the feature or pixel-space, this paper emphasizes adaptation in the noise space by leveraging the diffusion model process. 
- The training strategy using the diffusion process includes channel-shuffling and residual-swapping contrastive learning to prevent shortcuts learning. Additionally, during inference, only the restoration model is used independently from the diffusion model, making this approach memory-efficient as well.

### Strengths
- Domain adaptation in the noise space using the diffusion model process is innovative.
- Although this paper focuses on general restoration tasks such as denoising, deraining, and deblurring, it also potentially explains why the training method using synthetic data struggles to effectively address real data in the denoising problem, and why joint training with both types of data has been ineffective.
- The training strategy to prevent shortcuts is a novel contribution to the restoration task. In fact, shortcut phenomena can occur not only in restoration problems but also in tasks that involve predicting high-frequency components. While it raises the question of whether this strategy can be applied to general CNN networks as well as diffusion models, the paper demonstrates its effectiveness.

### Weaknesses
- The performance of the comparison methods used in the experiments is severely degraded. For example, the methods used for comparison in **Table 1** are either outdated or inappropriate. Although relatively recent methods such as **Ne2Ne** and **MaskedD** were used, since these methods do not target denoising using real data, it is questionable whether the results obtained by training these methods on real-world data are reasonable.
- Additionally, since the method presented in the paper uses extra data along with synthetic data for each task, it would be more appropriate to compare it with methods such as **PNGAN**[1*], which use the same training data, as seen in **Table 1**.
- The experiments in **Table 4** demonstrate that the noise sampling range of [1, 1000] is appropriate. Although the model does not require the diffusion process during inference, we believe this range imposes a significant burden during training. Considering this, for example, **DnCNN**[2*] can achieve a gain of approximately 35 dB on the SIDD test dataset with simple training using only L1 loss, even when trained directly on real data.
---
[1*] Cai, Yuanhao, et al. "Learning to generate realistic noisy images via pixel-level noise-aware adversarial training." Advances in Neural Information Processing Systems 34 (2021): 3259-3270.

[2*] Zhang, Kai, et al. "Beyond a gaussian denoiser: Residual learning of deep cnn for image denoising." *IEEE transactions on image processing* 26.7 (2017): 3142-3155.

### Questions
- This paper utilizes U-Net and U-Former for simplicity. In my opinion, the key contribution lies in applying the paper’s novel learning strategy to general restoration networks. Therefore, I am curious whether the proposed strategy also performs well on SOTA methods such as **Restormer** or **NAFNet**[1*], and whether these SOTA methods can surpass the performance on real-world data when trained with both real-world and synthetic data.
- Based on the SIDD test set, **NAFlow**[2*], **NeCA**[3*], and **sRGB-Flow**[4*] show much lower performance compared to the restoration achieved with DnCNN using synthetic datasets. According to the claim, the proposed method should be able to bridge the gap between synthetic and real data, thus delivering better performance. It would also be helpful if the paper provided performance results using DnCNN[5*] or other commonly used denoising networks to further validate the effectiveness of the approach.
---
[1*] Chen, Liangyu, et al. "Simple baselines for image restoration." European conference on computer vision. Cham: Springer Nature Switzerland, 2022.

[2*] Kim, Dongjin et al. "sRGB Real Noise Modeling via Noise-Aware Sampling with Normalizing Flows." The Twelfth International Conference on Learning Representations. 2024.

[3*] Fu, Zixuan, Lanqing Guo, and Bihan Wen. "sRGB Real Noise Synthesizing with Neighboring Correlation-Aware Noise Model." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

[4*] Kousha, Shayan, et al. "Modeling srgb camera noise with normalizing flows." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[5*] Zhang, Kai, et al. "Beyond a gaussian denoiser: Residual learning of deep cnn for image denoising." IEEE transactions on image processing 26.7 (2017): 3142-3155.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
* This work proposes to address domain adaptation in the noise space for image restoration 
* The authors propose channel shuffling and residual-swapping contrastive learning strategy to overcome the shortcut learning issue
* Experiments on image deraining, denoising and deblurring validate the effectiveness

### Strengths
* Generalization is a challenging and vital problem in image restoration. The paper proposes to work towards generalization using noise-space adaption.
* The work is well motivated. Especially in Figure 1, the authors find condition of diffusion models can serve as a proxy to discriminate clean distributions. This is interesting for me.
* The paper is well-written. The method is clearly claimed.

### Weaknesses
* It seems the paper lacks direct evidence to support diffusion loss is effective. That is, what is the performance if we replace the diffusion loss with perceptual loss, gan loss or nothing. I think this validation is important.
* I suggest to add some visual results of other compared methods in Figure A6-A8.
* Can you provide more details about the used diffusion model? What is the impact of the introduced diffusion loss on training dynamics(eg, loss, accuracy on validation set)? Whether the diffusion model can be extremely simplified (such as a single MLP layer like [1])
[1] Autoregressive Image Generation without Vector Quantization

### Questions
Please see weakness

### Soundness
3

### Presentation
3

### Contribution
3
