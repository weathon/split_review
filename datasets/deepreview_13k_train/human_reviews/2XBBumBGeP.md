# sRGB Real Noise Modeling via Noise-Aware Sampling with Normalizing Flows

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Noise poses a widespread challenge in signal processing, particularly when it comes to denoising images. Although convolutional neural networks (CNNs) have exhibited remarkable success in this field, they are predicated upon the belief that noise follows established distributions, which restricts their practicality when dealing with real-world noise. To overcome this limitation, several efforts have been taken to collect noisy image datasets from the real world. Generative methods, employing techniques such as generative adversarial networks (GANs) and normalizing flows (NFs), have emerged as a solution for generating realistic noisy images. Recent works model noise using camera metadata, however requiring metadata even for sampling phase. In contrast, in this work, we aim to estimate the underlying camera settings, enabling us to improve noise modeling and generate diverse noise distributions. To this end, we introduce a new NF framework that allows us to both classify noise based on camera settings and generate various noisy images. Through experimental results, our model demonstrates exceptional noise quality and leads in denoising performance on benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a system to generate realistic sRGB noise with noiseflow. The idea is to encode noise from multiple cameras into the same common latent space. For an unseen camera, a sample noise is encoded and a new noise is draw from a gaussian mixture model of learned noise. Multi-scale encoding schemes are employed to model long range spatial correlation of noise. Experiments show that a denoising network trained on generated noise works better than comparison techniques. Ablation study is provided and shows the importance of each of the proposed components.

### Strengths
I think the technical contribution of this work is solid. The proposed method works well with multiple camera models without the need for retraining. With different proprietary processing, noises from different cameras can have very different characteristics. The idea to encode different noise into different gaussian in a common latent space is convincing, and the result seems to suggest that this works well. The comparison was done convincingly to account for differences in how the comparison methods should be applied (for example, the best value was reported for the NeCA models where it needed to be trained per-camera).

### Weaknesses
Despite being successful in learning noise from SIDD dataset, I find the noise being generated to be far from realistics. Modern cellphone cameras apply heavy denoising in the chrominance channel that chromatic noise is never visible. Examples shown throughout the paper (e.g. in figure 4) shows heavy chromatic noise. Further, SIDD dataset only contain images from 10 scenes, so there is not a lot of diversity in the data. This limits how much generalization we can expect to real world cameras. While this is largely a limitation of the SIDD dataset, I think it is very important for the author to acknowledge this point in their manuscript.

As an alternative, it may be interesting for the authors to look at other dataset. There is a technical report by Jaroensri et al. (“Generating Training Data for Denoising Real RGB Images via Camera Pipeline Simulation”) that provides a dataset of raw-processed pairs that, in my opinion, is the most realistic among the raw-processed datasets available. The author should also consider applying processing from raw-only datasets such as those from Chen et al (“Learning to See in the Dark”) to achieve a more realistic noise distribution. Having included more dataset (especially in evaluation) could also be helpful in providing signal for generalization to the real world.

### Questions
Please see my weakness section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a sRGB real noise modeling based on noise-aware sampling and normalized flow. Specifically, the proposed method includes (1) a new NAFlow framework with the Noise-Awar algorithm (NAS), which allows the use of Gaussian mixture models from multiple noise distributions to synthesize real sRGB images with noise without the need for metadata. (2) a multi-scale modeling method to capture the noise correlations with different scales.

### Strengths
1. The paper looks technically sound and describes the algorithm clearly.
2. Experimental results demonstrate the advantages of NAFlow compared to some previous methods.
3. The Noise-Aware Sampling (NAS) algorithm eliminates the need to input noisy image metadata during inference which is novel to me.

### Weaknesses
1.This paper combines the normalized flow generation of Flow-sRGB with the multi-scale spatial correlation of NeCA. In my opinion, the author draws more on the flow-normalized noise generation method of Flow-SRGB and further uses multi-scale noise modeling to improve performance. I want to know the effect of adding multi-scale noise modeling on Flow-sRGB, and related ablation experiments should be added.
2.Writing errors, such as “NECA-W”, ” NAflow”, et al.

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a normalizing flow-based framework NAFlow for realistic noisy image generation. The generated images are used to adapt real denoisers and boost their performance. With the proposed Noise-Aware sampling algorithm, NAFFow learns and effectively manages the diverse noise distributions originating from various camera settings.

### Strengths
(i) The idea of using the Normalizing Flow to model the in-camera setting distribution is interesting. Previous methods mainly focus on designing a generative adversarial network for noise modeling.

(ii) The results on self-supervised image denoising are good and solid.

(iii) The presentation is good and easy to follow.

(vi) The appendix provides lots of visual results to show the advantages of the proposed method.

(v) The ablation study is sufficient to demonstrate the effectiveness of the approaches.

### Weaknesses
(i) The motivation is unclear. Why using Normalizing Flow is not explained. Because using GAN, Auto-encoder, DeFusion Model, etc., can also model the noise distribution. So, what's the difference? It's not sufficient to state that NF is used for its precise likelihood estimation capabilities without further elaboration on why this is specifically advantageous for noise modeling compared to other generative approaches. The paper needs to clarify the specific benefits of the invertible mapping property of NFs in the context of noise generation, and how this property is exploited to better model complex noise distributions, particularly when compared to the latent space representations of GANs or VAEs.

(ii) The paper proposes a normalizing flow (NF) for noise generation. However, normalizing flow for noise generation has been proposed in NoiseFlow. What is the difference and your contributions? The novelty of the proposed method in relation to existing NF-based noise modeling techniques like NoiseFlow is not clearly articulated. The authors should explicitly detail the architectural differences and methodological advancements that distinguish their approach, particularly focusing on how their method addresses limitations or challenges not covered by NoiseFlow. It is crucial to highlight specific technical contributions beyond simply applying a generic normalizing flow.

(iii) The proposed method has some technical drawbacks.

[1]  The normalizing flow-based framework requires a statistic, i.e., the mean of the specific normal distribution for the configuration c. This is a very strong priori condition. In real application, this statistic may not be given. The dependence on a specific mean for each noise configuration is a significant limitation, especially given that real-world noise is often highly variable and may not conform to predefined distributions. The authors need to address how their method would handle situations where the mean of the noise distribution is unknown or varies significantly, as this assumption could limit the applicability of their approach to real-world scenarios.

[2] The proposed method is trained on SIDD, even the pre-trained denoiser. However, the noise distribution varies across different datasets (like DND, PloyU, Nam) since they are captured by different hardware. The training may make the noise generator overfit on the SIDD dataset and not fit well with other noise distributions. Then how to solve this issue? The reliance on the SIDD dataset for training raises concerns about the generalizability of the approach, given the known limitations of SIDD in representing the full spectrum of real-world noise characteristics. The authors should demonstrate how their method avoids overfitting to the specific noise profiles in SIDD and how it can be adapted to datasets with different noise distributions, such as those captured by different camera sensors or under varying lighting conditions. The potential for overfitting to the SIDD dataset needs to be rigorously addressed with empirical evidence.


(iv) The experiments need to be improved.

[1] Experiments on other noisy image datasets should be provided to resolve my concerns in (iii) [2]. The experimental validation should include a broader range of datasets beyond SIDD to thoroughly assess the method's robustness and generalization capabilities. The paper should include experiments on datasets with different noise characteristics, such as the DND, PolyU, and Nam datasets, to demonstrate the method's ability to adapt to diverse noise distributions. This will provide a more comprehensive evaluation of the proposed approach.

[2] The comparisons should also be improved. The metric KLD may not be suitable for noise generation. Why not follow the metric PSNR Gap in DANet or Maximum Mean Discrepancy (MMD) to measure the domain gap? The choice of evaluation metrics needs to be justified more rigorously. While KLD provides insights into the divergence between distributions, it may not be the most appropriate metric for assessing the quality of generated noise. The authors should include additional metrics like PSNR Gap and MMD, which are commonly used in noise modeling, to provide a more comprehensive evaluation of the proposed method. The paper should also justify the selection of KLD over these metrics, or demonstrate that the conclusions are consistent across different metrics.

[3] The adaptation now is conducted in a self-supervised manner. What about its performance in a fully supervised manner? And what about its performance on the SOTA denoising methods like Restormer? Since some noise generation methods like PNGAN can still improve the performance of Restormer. The evaluation should include a comparison with state-of-the-art denoising methods, such as Restormer, to demonstrate the practical utility of the generated noise. The authors should also investigate the performance of their method in both self-supervised and fully supervised denoising settings, as this will provide a more complete picture of its capabilities. It is important to show how the proposed noise generation method can improve the performance of existing denoisers.

[4] The comparison between the proposed NAFlow and other SOTA noise generation algorithms should be added in the main paper, including DANet, PNGAN, GDANet, CycleISP, C2N, etc. A more comprehensive comparison with state-of-the-art noise generation methods is needed to contextualize the performance of the proposed method. The paper should include a direct comparison with methods like DANet, PNGAN, GDANet, CycleISP, and C2N, using consistent evaluation metrics, to demonstrate the advantages of NAFlow over existing approaches. This will provide a clearer understanding of the contribution of the proposed method.

(v) Reproducibility: The network and the method (Meta-train and Fast Adaptation) are pretty complicated. It is difficult for other researchers to reproduce the whole method. Since the code and models are not provided, the reproducibility cannot be checked.

### Questions
What are the advantages of your method when compared with other NF image denoising algorithms? Show experiments to support this.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a new normalizing flow framework (i.e., NAFlow) for noise modeling and synthesis. For noise modeling, NAFlow learns to map noise of various smartphone types and gain settings to different Gaussian distributions. For noise synthesis, NAFlow uses the Gaussain mixture model of learnt distributions to generate accurate yet diverse noisy images. Experiment results on real-world denoising datasets show the superiority of NAFlow over existing methods.

### Strengths
1. The idea of learning the noise distribution implicitly without metadata is reasonable. It is practical to model the noise of devices that is hard to accquire metadata, such as smartphones.
2. The proposed NAFlow outperforms baseline methods by a large margin on both noise modeling and noise synthesis.
3. The paper is well organized and written.

### Weaknesses
1. The comparison with C2N is unfair. C2N is trained with only noisy images, while other methods are trained with paired images. This training setting should be pointed out in the experiments.


### Questions
1. (This question is not critical to rating) What are the applications of noise synthesis and modeling methods? These methods apply paired noisy-clean images for training, then synthesize new pairs from clean images for training denoiser. However, the denoiser trained with synthesized pairs shows inferior performance than trained with original real paires. Could the authors explain the applications of proposed method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
