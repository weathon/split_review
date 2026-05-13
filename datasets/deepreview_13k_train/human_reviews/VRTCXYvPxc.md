# VIDEOGUARD: PROTECTING VIDEO CONTENT FROM UNAUTHORIZED EDITING

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
With the rapid development of generative technology, current generative models can generate high-fidelity digital content and edit it in a controlled manner. However, there is a risk that malicious individuals might misuse these capabilities for misleading or unlawful activities. Although existing research has attempted to shield photographic images from being manipulated by generative models, there remains a significant disparity in the protection offered to video content editing. To bridge the gap, we propose a protection method named VideoGuard, which can effectively protect videos from unauthorized malicious editing. This protection is achieved through the subtle introduction of nearly unnoticeable perturbation that interferes with the functioning of the intended generative diffusion models. Different from images, videos consist of sequential frames, containing not only visual content but also motion dynamics. Due to the redundancy between video frames, and inter-frame attention mechanism in video diffusion models, simply applying image-based protection methods separately to every video frame can not shield video from unauthorized editing. To tackle the above challenge, rather than optimize perturbation in a frame-wise manner like image-based methods, we adopt joint frame optimization, treating all the video frames as an optimization entity. Furthermore, we extract video motion information and fuse it into optimization objectives. Thereby, these alterations can effectively compel the models to produce outputs that are implausible and inconsistent. We provide a pipeline to optimize such a perturbation. Finally, we use both objective metrics and subjective metrics to demonstrate the efficacy of our method, and the results show that the protection performance of VideoGuard is superior to all the baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes VideoGuard to protect video content from unauthorized editing by diffusion-based video editing models.  VideoGuard introduces a two-stage optimization pipeline, including Optimizing DDIM Inversion Latent and Optimizing Video Perturbation.

### Strengths
1. This work regards the video and its inversion as a whole, instead of using an image-based approach and processing it frame by frame. It's reasonable.
2. Experimental results demonstrate the effectiveness of the two-stage approach.

### Weaknesses
 **Novelty:** While this work is a pioneering attempt to counter unauthorized manipulation in video editing models, the proposed method demonstrates limited innovation. The two-stage learning approach lacks specific insights tailored to this task. Specifically, in both stage 1 and 2, the authors apply PGD to learn the perturbated latent code and protedcted videos. However, PGD is published in 2018, which is outdated. I suggest the authors to customize a new temporal attack method for the task. 

 **Motivation:** The authors propose that their method prevents unauthorized video editing, yet it essentially functions as a targeted attack, meaning the input video can still be manipulated. Namely, the goal of preventing unauthorized video editing is not fully achieved in this work. Additionally, the resulting videos align more closely with a target latent rather than the input prompt. Furthermore, the method requires full access to the model's architecture, presenting a significant limitation. Although cross-model results are reported in experiments, the method shows poor transferability to unseen models. In real-world scenarios, the transferability to unseen models and datasets is crucial. More transferability evaluations are expected to enhance the quality of this work.

 **Methodology:** Stage 1 uses first-order difference to capture motion information, while Stage 2 aims to align the latent code of protected videos with an anchor code. However, these techniques are too simple and lack insights to the task of video protection. The authors do not fully use the temporal information in sequential signals. 

 **Experiments:** The method exhibits limited quantitative and qualitative improvements. In Table 1, its performance is only slightly better than the random noise baseline. This work fails to compare with SOTA attack methods, such as BSR [a] and ILPD [b]. The effectiveness of the qualitative results is not clearly demonstrated.

### Questions
Please demonstrate the superiority of the proposed method through more sufficient experiments.

### Soundness
3

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
2

### Summary
This paper proposes VideoGuard to protect videos from unauthorized editing. VideoGuard consists of two-stage pipelines. In the first stage, the authors use DDIM inversion process to get an initial noise latent from the original video. Then, the method optimizes the latent so that the denoising from the latent will result in a disrupted video, and therefore the video editing will be unsuccessful.  In the second stage, the method tries to find a perturbation that after adding it on top of the source video it can make the inversion of the video close to the optimized latent from stage 1. In addition, the added perturbation is required to be imperceptible. Therefore, VideoGuard can produce a similar source video that is free of unauthorized editing.

### Strengths
1. The proposed approach is interesting and reasonable to achieve the goal of protecting videos from unauthorized editing.
2. VideoGuard is to protect the video in the video pixel space, and the enhanced video is similar to the source video with extra shield.
3. The method treats the video as a whole without needing to process each frame individually.

### Weaknesses
My major concern is the results of VideoGuard. Although VideoGuard is a reasonable approach, seems the performance is not very effective. 

First of all, the video editing used seems not good. The edited videos are not very realistic from the examples shown in the paper. If the video editing method is not strong enough, it might be easy to protect the source video from effective editing.

Second, the protection result of VideoGuard is not good. As shown in the second row of Fig.3, VideoGuard fails to protect the source video. The immunized video is successfully changed by the prompt. Also, as shown in Fig. 5, the edited video protected by VideoGuard changed a lot, deviating a lot from the source video.

For the quantitative result, compared to the baseline without protection, the number did not make a large difference. I suppose the metric number will be very difference when comparing with and without protection.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces VideoGuard, a method designed to protect videos from unauthorized editing by generative diffusion models. Unlike prior efforts that primarily focus on images, VideoGuard specifically addresses the unique challenges posed by video content, including the sequential structure of frames and the presence of motion dynamics. The approach involves adding imperceptible perturbations across frames, which disrupt the generative model's operations without compromising the visual quality of the video. The paper presents a pipeline for implementing these perturbations and validates VideoGuard's effectiveness using various metrics.

### Strengths
This work represents the first attempt to prevent unauthorized manipulation of videos, paving the way for future research in this area.

### Weaknesses
**Novelty:** While this work is a pioneering attempt to counter unauthorized manipulation in video editing models, the proposed method demonstrates limited innovation. The two-stage learning approach lacks specific insights tailored to this task. Specifically, in both stage 1 and 2, the authors apply PGD to learn the perturbated latent code and protedcted videos. However, PGD is published in 2018, which is outdated. I suggest the authors to customize a new temporal attack method for the task. 

**Motivation:** The authors propose that their method prevents unauthorized video editing, yet it essentially functions as a targeted attack, meaning the input video can still be manipulated. Namely, the goal of preventing unauthorized video editing is not fully achieved in this work. Additionally, the resulting videos align more closely with a target latent rather than the input prompt. Furthermore, the method requires full access to the model's architecture, presenting a significant limitation. Although cross-model results are reported in experiments, the method shows poor transferability to unseen models. In real-world scenarios, the transferability to unseen models and datasets is crucial. More transferability evaluations are expected to enhance the quality of this work.

**Methodology:** Stage 1 uses first-order difference to capture motion information, while Stage 2 aims to align the latent code of protected videos with an anchor code. However, these techniques are too simple and lack insights to the task of video protection. The authors do not fully use the temporal information in sequential signals. 

**Experiments:** The method exhibits limited quantitative and qualitative improvements. In Table 1, its performance is only slightly better than the random noise baseline. This work fails to compare with SOTA attack methods, such as BSR [a] and ILPD [b]. The effectiveness of the qualitative results is not clearly demonstrated. 

[a] K. Wang, X. He, W. Wang, and X. Wang. Boosting adversarial transferability by block shuffle and rotation. In Proc. IEEE Int’l Conf. Computer Vision and Pattern Recognition, 2024.
[b] Q. Li, Y. Guo, W. Zuo, and H. Chen. Improving adversarial transferability via intermediate-level perturbation decay. Proc. Annual Conf. Neural Information Processing Systems, 2023.

### Questions
What datasets are used in training and testing? It seems the testing data only comprises 80 text-video pairs. I concern that the data size is too limited to demonstrate the effectivenss of the proposed approach.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a protection method called VideoGuard, designed to safeguard videos against unauthorized malicious editing. The optimization process involves analyzing all frames collectively, with the differences between frames extracted as motion information for optimization purposes.

### Strengths
1. This work adopts adversarial attack techniques from the field of image attacks into the video field to safeguard video editing methods that require the DDIM inversion step.

### Weaknesses
1. The video editing methods tested are quite outdated. Many contemporary video editing models, such as [1, 2, 3], do not require the DDIM inversion steps. In this case, does the method still remain effective?

2. The method appears to merely adopt techniques from the field of image attacks, but applied in a higher-dimensional space that includes the timestamp.

3. From Figure 3, it appears that the protection is ineffective, as the identities of Biden and Trump remain quite evident, with only minor color distortions present. To prevent the generation of these identities, methods for concept erasure, such as those described in [4, 5, 6, 7], could be considered. A brief discussion on concept removal in the related work section would be expected.

5. The layout of the main pipeline figure (Figure 2) is poorly arranged. The text and formulas should be enlarged for improved readability.

6. The citation format is incorrect, further diminishing readability. The authors have mistakenly used integral citations instead of non-integral citations. Please correct this.

---
[1] Consistent Video-to-Video Transfer Using Synthetic Dataset

[2] Video Editing via Factorized Diffusion Distillation

[3] Fairy: Fast parallelized instruction-guided video-to-video synthesis.

[4] Erasing Concepts from Diffusion Models

[5] Ablating Concepts in Text-to-Image Diffusion Models

[6] MACE: Mass Concept Erasure in Diffusion Models

[7] Separable Multi-Concept Erasure from Diffusion Models

### Questions
Please refer to the weaknesses.

If the authors adequately address my concerns during the rebuttal, I am open to adjusting my score.

### Soundness
3

### Presentation
1

### Contribution
1
