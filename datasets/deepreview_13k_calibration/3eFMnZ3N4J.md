# Efficient-3Dim: Learning a Generalizable Single-image Novel-view Synthesizer in One Day

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
The task of novel view synthesis aims to generate unseen perspectives of an object or scene from a limited set of input images. Nevertheless, synthesizing novel views from a single image still remains a significant challenge in the realm of computer vision. Previous approaches tackle this problem by adopting mesh prediction, multi-plain image construction, or more advanced techniques such as neural radiance fields. Recently, a pre-trained diffusion model that is specifically designed for 2D image synthesis has demonstrated its capability in producing photorealistic novel views, if sufficiently optimized on a 3D finetuning task. Although the fidelity and generalizability are greatly improved, training such a powerful diffusion model requires a vast volume of training data and model parameters, resulting in a notoriously long time and high computational costs.
To tackle this issue, we propose \textbf{Efficient-3DiM}, a simple but effective framework to learn a single-image novel-view synthesizer. 
Motivated by our in-depth analysis of the inference process of diffusion models, we propose several pragmatic strategies to reduce the training overhead to a manageable scale, including a crafted timestep sampling strategy, a superior 3D feature extractor, and an enhanced training scheme. When combined, our framework is able to reduce the total training time from 10 days to less than \textbf{1 day}, significantly accelerating the training process under the same computational platform (one instance with 8 Nvidia A100 GPUs). Comprehensive experiments are conducted to demonstrate the efficiency and generalizability of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce Efficient-3DiM to accelerate diffusion models for single-image novel view synthesis, such as Zero123. Specifically, they employ a crafted timestep sampling strategy, a superior 3D feature extractor (DINO-v2), and an enhanced training scheme. Experimental results demonstrate that the proposed method could retain the performance metrics of the baseline but accomplish this with a remarkable 10x speed increase.

### Strengths
1. I really like the idea of integrating a self-supervised Vision Transformer for image conditions since the clip image feature only contains high-level semantic meaning. Figure 4 and Figure 5 also showcase the superiority of DINO-v2 over CLIP.
2. An in-depth and smart analysis is provided for the denoising process, and then the author proposes to sample more for larger timesteps to learn geometry, which accelerates the training process.

### Weaknesses
1. I am not persuaded by the motivation from comparing training image classifiers and generative models, which are not comparable. Moreover, we usually treat Zero123 as a foundation model which does not need retraining. Under this circumstance, I think the value of the proposed Efficient-3DiM diminishes.
2. The section "ENHANCED TRAINING PARADIGM" contains several well-known tricks, such as mix-precision training. I would like to suggest the authors should not emphasize this too much in their contribution.
3. I expect the proposed method with a more advanced 3D feature extractor to achieve better performance than Zero123. It is suggested to apply 3D reconstruction (e.g., Neus) on the generated views to compare Efficient-3Dim and Zero123.
4. Could you elaborate more on how to "conduct several different spatial interpolation processing"? And why do you only inject the features to the encoder of the UNet denoiser? I also suggest including more details on how to conduct feature amalgamation (e.g., feature shape and resolution).

### Questions
1. It is suggested to include more related work for "Novel View Synthesis from a Single Image", such as [a-d]

[a] Geometry-Free View Synthesis: Transformers and no 3D Priors. ICCV 2021. 

[b] Look Outside the Room: Synthesizing A Consistent Long-Term 3D Scene Video from A Single Image. CVPR 2022.

[c] SynSin: End-to-end View Synthesis from a Single Image. CVPR 2020.

[d] PixelSynth: Generating a 3D-Consistent Experience from a Single Image. ICCV 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Efficient-3DIM is an efficient framework for single-image novel view synthesis through diffusion models. The proposed method reduces the training time from 10 days to a single day while generating photorealistic and geometrically reasonable novel views.

### Strengths
Strengths:

The authors build their work on 3DIM and integrate three pivotal contributions: a modified sampling strategy departing from traditional uniform sampling, an integration of a self-supervised Vision Transformer replacing the conventional CLIP encoder, and an enhanced training paradigm. While all those steps taken are empirical, they each carry certain contextual novelty and together yield strong training performance:
For the modified time step sampling, although similar ideas were explored before, the authors take a new angle since the major phase of 3DIM’s training is essentially characterized as a finetuning paradigm as the adopted novel-view synthesizer is initiated from a pre-trained text-to-image diffusion model.
Incorporating multi-scale representations produced by the DINO-v2 encoder, in place of the CLIP encoder, significantly improves the dense prediction and correspondence.
While the authors transit from full-precision to 16-bit mixed-precision training, they add another layer normalization before sending the DINO-v2 feature to the diffusion model, to mitigate the numerical errors.

### Weaknesses
Weaknesses:

(1)   I do not fully understand why LN can mitigate numerical errors, in the third part of Efficient-3DIM

(2)   The major goal of this work is to trim down the training time without spending more costs on the total training resources (e.g., taking large-batch via a distributed system). Could the authors elaborate on how the proposed method could be integrated with distributed training, and whether its speedup benefits may diminish in the (more scalable) distributed training setup?

(3)   Figure 8: I need help seeing how Zero 1-to-3 falls short of producing multi-view consistent visual outputs. All displayed results have valid visual quality to me.

(4)   Minor: “neurallift-360” paper was incorrectly cited twice in reference.

### Questions
Please refer to the Weaknesses

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses the challenge of synthesizing novel views from a single image in computer vision. It introduces "Efficient-3DiM," a framework designed to significantly reduce the training time and computational costs required to train such a model, achieving a training time reduction from 10 days to less than 1 day while maintaining efficiency and generalizability through innovative strategies like non-uniform timestep sampling and improved feature extraction.

### Strengths
This paper was developed to enhance the training efficiency of diffusion models for single-image novel view synthesis. Core Strategies include:
- Revised Timestep Sampling: A novel strategy for selecting diffusion timesteps, and optimizing training.
- Self-Supervised Vision Transformer: Integration of a self-supervised Vision Transformer to improve the incorporation of high-level 3D features better than CLIP.
- Enhanced Training Paradigm: A refined training recipe that adopt low-precision training while addressing the numerical errors via extra layer normalization.

All strategies are grounded in motivating observations. When applied altogether, the speedup is quite significant: a 14x reduction in training time compared to the original zero 1-to-3 approach, enabling rapid iterations.

### Weaknesses
 - Would this proposed approach be generalizable to accelerating training other image-to-3D models, such as Zero 1-to-3 and Syncdreamer? Why or why not?
 
- The evaluation is solely conducted using the Objaverse dataset. Although this dataset is extensive and newly introduced, relying solely on a single dataset with potential biases and limited coverage could obscure any issues that the proposed method might have in the wild. It would be beneficial if the authors could also showcase results on additional datasets for a more comprehensive assessment. Specifically, the Objaverse dataset, while large, may not fully represent the diversity of real-world object appearances and complexities. The lack of evaluation on other datasets makes it difficult to ascertain whether the reported performance gains are specific to the characteristics of Objaverse or if they generalize to other scenarios.

### Questions
Please kindly refer to the weakness section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed Efficient-3DIM, a novel approach to single-image novel-view synthesis that aims to generate unseen perspectives of an object or scene from a limited set of input images. The proposed method reduces the training overhead to a manageable scale through several pragmatic strategies. Comprehensive experiments were conducted to demonstrate the efficiency and generalizability of the proposed method on common benchmarks.

### Strengths
Efficient-3DIM differs from previous approaches by proposing a simple yet effective efficient training framework. This is achieved through several pragmatic strategies, including a crafted timestep sampling strategy, a superior 3D feature extractor, and an enhanced training scheme. 

The crafted timestep sampling strategy reduces the number of timesteps required for training, while the superior 3D feature extractor improves the quality of the learned features. The enhanced training scheme includes a self-supervised Vision Transformer and a modified sampling strategy, which are evaluated and shown to be effective in generating photorealistic novel views. 

The proposed strategies significantly accelerate the training process, reducing the total training time from 10 days to less than 1 day, while shown to be effective in generating photorealistic novel views.

### Weaknesses
The study employs the Objaverse dataset as the sole testbed, which contains 800k three-dimensional objects. While this is a substantial dataset, its diversity and representativeness could be a limitation. I wonder if the authors would be able to demonstrate similar results on ScanNet or MVImagenet as well. Additional results on real scenes would be valuable and welcome too.

The authors mentioned that each object in the dataset underwent a procedure where 12 viewpoints are sampled. Are all comparison methods adopting the same fixed number of viewpoints?

The work itself follows the line of works by (Watson et al., 2022) and (Liu et al., 2023b), and mainly studied training efficiency improvement. The contribution is solid yet not fully substantial.

### Questions
Please see the weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
