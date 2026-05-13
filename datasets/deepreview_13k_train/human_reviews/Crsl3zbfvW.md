# Single-View 3D Representations for Reinforcement Learning by Cross-View Neural Radiance Fields

- Decision: Reject
- Scores: 3, 5, 3, 5, 6

## Abstract
Reinforcement learning (RL) has enabled robots to develop complex skills, but its success in image-based tasks often depends on effective representation learning. Prior works have primarily focused on 2D representations, often overlooking the inherent 3D geometric structure of the world, or have attempted to learn 3D representations that require extensive resources such as synchronized multi-view images even during deployment. To address these issues, we propose a novel RL framework that extracts 3D-aware representations from single-view RGB input, without requiring camera calibration information or synchronized multi-view images during the downstream RL. Our method employs an autoencoder architecture, using a masked ViT as the encoder and a latent-conditioned NeRF as the decoder, trained with cross-view completion to capture fine-grained, 3D geometry-aware representations. Additionally, we utilize a time contrastive loss that further regularizes the learned representation for consistency across different viewpoints. Our method significantly enhances the RL agent’s performance in complex tasks, demonstrating superior effectiveness compared to prior 3D representation-based methods, even when using only a single, uncalibrated camera during deployment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an interesting approach to utilize NeRF based pretraining to bake in viewpoint awareness into an RL system. The authors first pretrain a representation using cross-view completion objective visa NeRF rendering using time contrastive learning objective for scene regularization. The authors then use the pretrained scene encoder for downsteam reinforcement learning task. Relevant experiments are designed which demonstrate viewpoint awareness of the system in a synthetic setup.

### Strengths
In my opinion, below are the strengths of the approach:

1. Designing relevant experiments and showcasing improvement numbers that highlight the method is invariant to the viewpoint and camera matrices. Slight perturbation in the cameras from the reference views shows the learned policies are invariant to disturbances. 

2. The writing and flow of the paper is nice, and the presentation is clear. 

3. Strong qualitative improvement results against competing baselines.

### Weaknesses
In my opinion, the weakness of the paper is as follows:

1. The paper misses various key recent results both for 3D representation learning using NeRFs [1] and for baking in viewpoint awareness for policy learning [2,3]. Specifically, the paper does not adequately address how its method compares to approaches that learn generalizable 3D representations, or methods that explicitly use novel view synthesis for policy learning. The lack of comparison to these methods makes it difficult to assess the novelty and contribution of the proposed approach.

2. The paper doesn't show any real-world evaluation results while both [2,3] show real-world results. The absence of real-world experiments raises questions about the practical applicability of the method. It is unclear if the method's performance in simulation would translate to real-world scenarios, especially given the complexities of real-world environments, such as sensor noise, lighting variations, and dynamic objects. Is it an inherent limitation of the method that it only works in simulation?

3. Follow-up to point 1. While the paper shows qualitative comparison to recent NeRF-based methods, how does the result compare to zero-shot generalizable NeRF-based method i.e. ZeroNVS (zero-shot vs. finetuned on their data) and NeRF representation learning method i.e. NeRF-MAE trained on their data? The paper should provide a more thorough comparison, including quantitative results, to demonstrate the advantages of the proposed method over existing approaches.

4. What is the pretraining data mix and how does it impact OOD policy learning? Can the model generalize to OOD in sim i.e. sim2sim generalization or OOD real i.e. sim2real generalization? The paper lacks a discussion on the generalization capabilities of the proposed method. It is important to understand how the method performs when faced with unseen environments or variations in the training data.

### Questions
Please see my questions in the weakness section above. I look forward to author's responses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a framework that generates 3D-aware representations from single-view camera inputs, which can be rendered into observations for training RL models. The 3D reconstruction model uses an autoencoder architecture, with a masked ViT as the encoder and a latent-conditioned NeRF as the decoder, trained with cross-view completion objectives. Experimental results demonstrate that the proposed method greatly improves the RL agent's performance for complex tasks.

### Strengths
* The proposed method can reconstruct 3D scene representation from single-view images, eliminating the need for multi-sensor setup and calibration for learning downstream RL algorithms.
* By using an autoencoder architecture to learn the NeRF representation, it bypasses the time-consuming optimization required in classical NeRF reconstruction methods and potentially predicts occluded regions, unlike traditional NeRF approaches.
* The authors conduct extensive experiments to demonstrate that the proposed methods achieve superior performance for both volume rendering and downstream RL algorithms such as DrM.

### Weaknesses
 * The time contrastive loss (Eqn. 3) repulses state features at different timesteps. However, this does not hold for static scenes where the actor remains stationary between timesteps $t$ and timestep $t\prime$. This is a significant limitation, as the contrastive loss may inadvertently push apart representations of the same scene state when the agent is not actively moving, thus hindering the learning of a consistent state representation.
* The 3D encoder-decoder model $\Omega_\theta$ is trained on multi-view images, with scene representation $z_t = \Omega_\theta(O_{t-2:t}^i, O_{t-2:t}^{r_1}, \cdots, O_{t-2:t}^{r_K})$. How can it generalize when the inputs are from the same viewpoint, as in $z_t = \Omega_\theta(O_{t-2:t}^i, [O_{t-2:t}^i,] * K)$ (line 291)? The paper does not adequately address how the model handles the lack of viewpoint diversity during inference, which is a critical aspect for its practical application.
* Table 1 claims that the proposed method does not require camera calibration. However, camera poses are needed to render multi-review reconstruction from $z_t$, making this claim inaccurate. The need for camera poses during the pre-training phase, even if not during deployment, should be explicitly acknowledged and discussed, as it limits the applicability of the method in scenarios where such calibration is not readily available.
* In the volume rendering experiments, the authors should also include comparisons with NeRF baselines for sparse views, such as RegNeRF, pixelNeRF, etc. The lack of comparison with these methods makes it difficult to assess the performance of the proposed approach in the context of existing techniques for novel view synthesis from sparse inputs.
* The RL experiments are conducted on toy environments. It would be valuable to see the method's performance in real-world robotic settings. The generalization of the proposed method to more complex and realistic scenarios remains unclear, limiting the practical impact of the work.

### Questions
See the weakness above.

### Soundness
3

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
Summary
This paper introduces a 3D representation reinforcement learning (RL) framework that utilizes a single view for inference. The downstream RL process leverages the latent code derived from the single image as input for the RL tasks.

### Strengths
Strengths

The results of the proposed method demonstrate superior performance compared to previous relative methods.

### Weaknesses
Weaknesses

The writing quality requires improvement, for example in line 300, where the meaning is unclear. The preceding sentence discusses a reinforcement learning (RL) algorithm, but the subsequent sentence shifts focus to data shuffling, creating a disjointed narrative. Additionally, this sentence is ambiguous  and difficult to comprehend (eg, why `randomize viewpoint` but not `random pick a viewpoint` ).

In line 93, the authors do not clarify the concept of a calibrated camera, both in this section and in subsequent ones. Additionally, the process for computing the (x,d) values during rendering is not explained. Therefore, the claim that the proposed method operates 'without requiring camera calibration' is misleading; instead, it could be interpreted that 'camera calibration is addressed through overfitting.' It appears that the authors are utilizing an absolute camera pose along with a fixed intrinsic matrix. Consequently, the image encoder and neural radiance fields (NeRF) are effectively learning a fixed RGB->pose mapping. This principle is referenced in [1] and may lead to poor generalization. Furthermore, recent multi-view stereo (MVS) reconstruction models demonstrate that a calibration matrix is not essential for creating MVS 3D models. The authors should explore relevant literature in the domains of lightweight regression models (LRM), single-view LRMs, LRM with Gaussian distributions, and indoor LRM-like methodologies.

The image encoder and NeRF appear to be overfitting to the given dataset, similar to previous dynamic NeRF approaches that attempt to learn a mapping of f(x,d,t)=c,\rho. The latent variable z in the proposed method effectively serves as a latent code encompassing (t, action, state, pose, intrinsic parameters, and object). For instance, in Figure 3, if the proposed method utilizes only view V3 as input, it can accurately recover the clearly marked red annotation on the box, which is not visible in view V3. To the best of my knowledge, no existing methods—whether single view to 3D, MVS to 3D, learning-based, diffusion-based, for objects, indoors, or outdoors— can achieve it whtiout overfitting.

Several baseline comparisons are missing. Since the proposed method aims to illustrate the effectiveness of a single-view latent 3D representation for RL processes, it is essential for the authors to include baselines that utilize explicit 3D representations, such as depth maps or 3D volumes, as presented in the recent conference proceedings.

### Questions
1. The author should explain more details about the camera calibration.
2. The author should add some baselines with explicit 3d reapresentation in RL.
3. The visualization result of snerl looks much worse than it original paper, it will be great to see the visualization on the same env and setting.

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
2

### Summary
This paper presents SinCro, a framework for learning 3D-aware representations for reinforcement learning that can operate with single-view inputs during deployment. The key innovation is combining a masked ViT encoder with a latent-conditioned NeRF decoder, trained through cross-view completion and time contrastive learning. The method enables single-view 3D representation inference without requiring camera calibration during deployment, while previous approaches typically needed multi-view inputs or calibrated cameras.

### Strengths
- The technical approach is well-motivated and addresses a practical limitation of existing 3D representation learning methods for RL - the requirement for multi-view or calibrated cameras during deployment
- The empirical results demonstrate the method works as intended, achieving comparable performance to multi-view baselines while requiring only single-view input

### Weaknesses
My primary concerns are:

- The evaluation is limited to MetaWorld environments, which are relatively simple by 2024 standards. Testing on more complex manipulation scenarios would strengthen the paper. There are a lot of other simulated environments like RLBench. The use of MetaWorld, while common in some prior works, does not adequately demonstrate the robustness of the proposed approach in more complex, cluttered, and dynamically changing environments. The tasks within MetaWorld are often well-defined and lack the variability that would be present in real-world robotic manipulation tasks. This raises concerns about the generalizability of the learned representations.
- The quantitative results in Figure 3 show an apparent contradiction - NeRF-RL achieves higher PSNR despite producing visibly blurrier reconstructions. This needs better explanation. The higher PSNR for NeRF-RL, despite the visual blurriness, suggests that the metric might not be fully capturing the relevant aspects of reconstruction quality for downstream RL tasks. PSNR is known to be sensitive to pixel-level differences and may not correlate well with perceptual quality or the usefulness of the reconstruction for control. The fact that NeRF-RL has sharper boundaries in non-salient areas, as mentioned, further emphasizes the limitations of relying solely on PSNR as an evaluation metric.

Some additional comments

- The figures could be improved - Figure 2 is a PNG instead of vector graphics which reduces quality

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
A 3D-aware representation learning approach is presented in which posed multiview data is leveraged to learn view-invariant representations from images. These representations can be used as auxiliary input to an RL policy, where it is shown they achieve superior performance relative to other such baselines.

### Strengths
Learning viewpoint invariant embeddings is an important problem in robotics as prior work has shown the sensitivity of robot policies to out-of-domain camera viewpoints. 

The experimental evaluation and ablation study as well as qualitative analysis are quite thorough and nice to see.

### Weaknesses
 * The proposed representation requires synchronized multiview video data to be trained, so it can only be trained on limited data. It would be good to compare against embeddings such as DinoV2 which do not have explicit geometry-aware nature but can be trained on a lot more data and probably have a notion of “view-invariance” to some degree due to their training strategy.

* Table 1 is a bit misleading. While during deployment the proposed algorithm can indeed be run on single view input, if I’m not mistaken during training of the actual embedding the requirement is still for posed multiview data. Perhaps it would be better to disentangle the deployment and training stages in this Table for the proposed method and for baselines as applicable. 

* I think the paper focuses slightly too much on the few- or single-view reconstruction results visually and wr.t. view synthesis metrics, which I don’t think is particularly informative. Single- and few-view reconstruction is a huge field by itself and there are much stronger baselines to compare against if this is the goal such as PixelNeRF, NeRDi, GS-LRM, ZeroNVS, Cat3D, Reconfusion, etc. etc. The goal of the paper is not to solve single or few view 3D reconstruction but to learn 3D-aware representations for downstream RL.

### Questions
Of course, it’s not necessary to compare, but it may be good to discuss some concurrent related works, such as Dreamitate, VISTA, RoVi-AUG, which leverage generative models to learn view-invariant RL policies.

### Soundness
3

### Presentation
4

### Contribution
3
