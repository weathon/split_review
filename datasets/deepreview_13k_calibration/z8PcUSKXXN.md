# Random Is All You Need: Random Noise Injection on Feature Statistics for Generalizable Deep Image Denoising

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Recent advancements in generalizable deep image denoising have catalyzed the development of robust noise-handling models. The current state-of-the-art, Masked Training (MT), constructs a masked swinir model which is trained exclusively on Gaussian noise ($\sigma$=15) but can achieve commendable denoising performance across various noise types (*i.e.* speckle noise, poisson noise). However, this method, while focusing on content reconstruction, often produces over-smoothed images and poses challenges in mask ratio optimization, complicating its integration with other methodologies. In response, this paper introduces RNINet, a novel architecture built on a streamlined encoder-decoder framework to enhance both efficiency and overall performance. Initially, we train a pure RNINet (only simple encoder-decoder) on individual noise types, observing that feature statistics such as mean and variance shift in response to different noise conditions. Leveraging these insights, we incorporate a noise injection block that injects random noise into feature statistics within our framework, significantly improving generalization across unseen noise types. Our framework not only simplifies the architectural complexity found in MT but also delivers superior performance. Comprehensive experimental evaluations demonstrate that our method outperforms MT in various unseen noise conditions in terms of denoising effectiveness and computational efficiency (lower MACs and GPU memory usage), achieving up to 10 times faster inference speeds and underscoring it's capability for large scale deployments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper revisits the challenge of generalizable image denoising, focusing on a training process that utilizes only Gaussian noise while testing encompasses various noise types. The authors reveal that models trained on different noise distributions yield distinct feature distributions. To enhance generalization capabilities, they introduce a novel neural network architecture that effectively handles multiple noise distributions when trained on white Gaussian noise. Central to this innovation is a noise injection block that integrates random noise into the features processed through the network layers.

Specifically, the architecture employs a U-Net type encoder-decoder structure, incorporating down and up convolutions, normalizations, ReLUs, and skip connections between the encoder and decoder. The noise injection blocks are strategically placed after each downsample bundle, which consists of Downsampling Convolution, Normalization, and ReLU.

In their experiments, the authors train the proposed network on white Gaussian noise with a sigma of 15, demonstrating its ability to generalize to various non-Gaussian noises, including (1) Speckle noise, (2) Salt & Pepper noise, (3) Poisson noise, (4) a mixture of noises (1)-(3) at different levels, (5) Image Signal Processing Noise, and (6) Monte Carlo rendered image noise.

### Strengths
- **Innovative Approach**: The paper offers a fresh perspective on the problem of image denoising.

- **Thorough Experimental Analysis**: The experimental analysis is extensive and well-structured.

- **Generalization Capability**: The proposed architecture effectively generalizes across various noise distributions, even when trained exclusively on white Gaussian noise. In the experiments conducted, it consistently outperforms competing methods in denoising performance. I believe that the concept of noise injection to enhance the generalization capabilities of image-denoising architectures holds significant potential and could attract interest from the research community.

### Weaknesses
I believe the most critical aspect of this task is its generalization capability. While the authors included the SIDD dataset in their experiments, they did not incorporate additional real-world noise datasets. The absence of these datasets limits the conclusions that can be drawn regarding the method's practical applicability. Specifically, real-world noise often exhibits complex spatial correlations and signal dependencies, which are not fully represented by the synthetic noise types used in the experiments. Furthermore, the evaluation could be strengthened by including a broader range of real-world noise scenarios, such as those arising from different camera sensors or environmental conditions. Without this, the claim of superior generalization remains somewhat unsubstantiated.

### Questions
In real-world scenarios, noise is highly spatially correlated and dependent on signal intensity, which inevitably incorporates image information, making it challenging to eliminate. From a theoretical standpoint, can Gaussian denoisers truly address the complexities of real noise?

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
- This paper enhances the generation performance of denoising by injecting random noise into the feature space, resulting in performance improvements over exisiting SOTA methods.

### Strengths
- Performance is improved simply by adding noise in the feature space.
- Builds upon existing experiments, effectively demonstrating the impact of this approach.

### Weaknesses
 - The techincal contribution is quite incremental.
- Although noise injection at the feature level is effective, it is not particularly novel.
- For example. while Appendix A.3 theorectically demonstrates the effect of this approach, applying random noise to input data across various training datasets might yield similar results. In this regard, it may be challeging to assert that this method is definitively more effective than previous SOTA methods.
- While noise injection at the feature level in encoder can induce more nonlinearity in the noise distribution compared to input-only injection, claming this as a major technical strength might be an overstatement.
- This method seems applicable to most encoder-decoder architectures, which might be a strength over proposing a completely new architecture.

### Questions
- Aside from the noise injection module, are there other technical contributios that could be highlighted as strengths of the model?
- How does the model perform when noise is injected only into the image space (input)?
- Real-wolrd noise adaptation (e.g., LAN[1*]) is already in use. How does the model generalize to real-world noise? For instance, how does a model trained on SIDD peform on PolyU[2*] or NAM[3*] dataset?
- I consider the techinical contribution to be limited, but the performance is sufficiently high, so I gave it a rating of 5. I would consider increasing the rating if it can be shown to generalize well to real-world noise.
---
[1*] Kim, Changjin, Tae Hyun Kim, and Sungyong Baik. "LAN: Learning to Adapt Noise for Image Denoising." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
[2*] Jun Xu, Hui Li, Zhetong Liang, David Zhang, and Lei
Zhang. Real-world noisy image denoising: A new benchmark. arXiv preprint arXiv:1804.02603, 2018
[3*] Seonghyeon Nam, Youngbae Hwang, Yasuyuki Matsushita,
and Seon Joo Kim. A holistic approach to cross-channel image noise modeling and its application to image denoising.
In CVPR, 2016.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces RNINet, an architecture designed to improve generalization in deep image denoising. Unlike traditional denoising methods that often overfit specific noise types, RNINet incorporates a noise injection block to inject random noise into feature statistics during training, enabling the model to adapt to unseen noise types. RNINet enhances both denoising performance and computational efficiency, surpassing the Masked Training (MT) method. Extensive experiments demonstrate RNINet's superiority in handling various noise conditions while maintaining lower computational cost and achieving faster inference speeds.

### Strengths
- The paper presents a denoising model, RNINet, which achieves higher denoising performance than MT.
- RNINet demonstrates strong performance across diverse synthetic out-of-distribution (OOD) noise settings, highlighting its robustness beyond standard training conditions.
- RNINet demonstrates improved efficiency, operating at 0.1x the runtime of MT, an essential advantage as image denoising often precedes various downstream computer vision tasks.
- The paper is well-written and accessible, offering clear explanations and comprehensive ablation studies that enhance understanding.
- Authors provided the model to reproduce the results.

### Weaknesses
 - The approach of injecting random noise into feature maps for enhanced generalization has been explored previously, and the addition of feature statistics such as mean and variance feels incremental rather than novel.
- If the primary objective is generalizable denoising, the model’s practicality in real-world scenarios should be further substantiated. Real-world evaluation is limited to the SIDD dataset, where performance metrics are relatively poor (although superior to the other methods in the table). Additionally, Figure 8 displays only a single, easy-to-denoise image that lacks sufficient visual details, making it unconvincing as evidence of real-world noise removal capabilities.
- While the paper emphasizes RNINet’s superiority over MT, there is insufficient theoretical explanation regarding how RNINet addresses MT’s limitations.
- The visual outcomes in Figure 5 do not appear substantially improved compared to MT, raising questions about the perceptual gains claimed. To enhance the clarity and persuasiveness of visual comparisons, could each visual example include quantitative metrics (e.g. PSNR, SSIM)?

### Questions
Please refer to Weaknesses section for major questions.

- Given that generalization to real-world conditions is the ultimate goal of the work, could the authors provide additional quantitative and qualitative results on various real-world benchmarks, such as the DND, Poly, CC datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces RNINet, an architecture for generalizable deep image denoising. The key innovation is the noise injection technique, which injects random noise into feature statistics and alters them to represent potential unseen noise domains. This allows the model to generalize well despite being trained only on Gaussian noise. The authors demonstrate RNINet's performance across multiple noise types and levels compared to both specialized and generalizable denoising methods. They also provide an analysis of the feature statistics to validate their approach.

### Strengths
+ The paper introduces a noise injection technique that directly manipulates feature statistics, which is an approach to improving generalization in image denoising.
+ This work surpasses previous methods, such as masked training denoising, on both in-distribution and some out-of-distribution datasets.
+ The authors used Deep Degradation Representation (DDR) for further analysis to evaluate the network's generalization capabilities.

### Weaknesses
 - PSNR and SSIM have limitations in their accuracy of assessment in some aspects; the authors might consider adding more metrics, such as LPIPS.
- The paper could benefit from including more ablation studies to further explore the proposed method.

### Questions
- Regarding the experimental setup, the authors could try to train the model on a more general training set, rather than fixed Gaussian noise, and then compare the generalization ability.

### Soundness
3

### Presentation
3

### Contribution
3
