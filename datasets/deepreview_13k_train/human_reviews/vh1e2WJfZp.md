# High-Precision Dichotomous Image Segmentation via Probing Diffusion Capacity

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In the realm of high-resolution (HR), fine-grained image segmentation, the primary challenge is balancing broad contextual awareness with the precision required for detailed object delineation, capturing intricate details and the finest edges of objects.
Diffusion models, trained on vast datasets comprising billions of image-text pairs, such as SD V2.1, have revolutionized text-to-image synthesis by delivering exceptional quality, fine detail resolution, and strong contextual awareness, making them an attractive solution for high-resolution image segmentation.
To this end, we propose \mymethod, a diffusion-driven segmentation model that taps into the potential of the pre-trained U-Net within diffusion models, specifically designed for high-resolution, fine-grained object segmentation.
By leveraging the robust generalization capabilities and rich, versatile image representation prior of the SD models, coupled with a task-specific stable one-step denoising approach, we significantly reduce the inference time while preserving high-fidelity, detailed generation.
Additionally, we introduce an auxiliary edge generation task to not only enhance the preservation of fine details of the object boundaries, but reconcile the probabilistic nature of diffusion with the deterministic demands of segmentation.
With these refined strategies in place, \mymethod serves as a rapid object mask generation model, specifically optimized for generating detailed binary maps at high resolutions, while demonstrating impressive accuracy and swift processing. 
Experiments on the DIS5K dataset demonstrate the superiority of \mymethod, achieving state-of-the-art results through a streamlined inference process.
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a model named DiffDIS for high-resolution binary image segmentation, incorporating strategies like single-step denoising, edge-assisted generation, and multi-scale conditional injection to enhance segmentation accuracy and inference speed. The authors validate DiffDIS’s performance on the DIS5K dataset, showing promising results. While the design is sound and experimental results are clearly presented, the paper’s novelty and certain implementation details could benefit from further clarification. In the rebuttal, the author addressed these concerns.

### Strengths
1.	Multi-level Design Innovations: The paper combines single-step denoising, edge-assisted generation, and multi-scale conditional injection to address the challenges of high-resolution segmentation, balancing speed and detail retention effectively.
2.	Comprehensive Experiments: The experimental setup on the DIS5K dataset is thorough, with comparisons to multiple specialized and general segmentation models. Ablation studies illustrate each component’s contribution, supporting the rationale behind the model design.
3.	Clarity: The paper is well-organized, with clear descriptions of the model and results, making it accessible to readers.

### Weaknesses
1.	Clarify Novelty of the Single-Step Denoising: While the single-step denoising strategy indeed boosts inference efficiency, a similar concept has been explored in models like GenPercept. I suggest that the authors clarify if DiffDIS’s single-step denoising incorporates task-specific optimizations for DIS tasks, to better highlight its originality.
	2.	Elaborate on the Edge-Assisted Generation’s Distinctiveness and Adaptation for High-Resolution Segmentation: The edge-assisted generation approach in DiffDIS appears similar to the edge-guided inpainting technique used in EdgeConnect, albeit applied in segmentation rather than inpainting. To avoid the impression that this is a simple adaptation from inpainting, I suggest the authors discuss any specific adjustments or optimizations made for high-resolution segmentation in DiffDIS.
	3.	Advantages of Joint Edge and Mask Prediction with Experimental Validation: DiffDIS performs joint edge and mask prediction, unlike stage-wise processing. Further discussion on the specific advantages of joint prediction, especially in handling fine details and complex boundaries, would strengthen this choice. Additionally, including experimental comparisons between joint prediction and stage-wise prediction would provide valuable insights into its effectiveness.
	4.	Comparative Analysis of Training Time: While DiffDIS’s inference time is shown to be efficient, comparative analysis of training times is absent. Including training time comparisons would provide a more holistic view of DiffDIS’s computational efficiency.

### Questions
please see the weakness part

### Soundness
3

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
4

### Summary
The authors proposed a method for dichotomous segmentation using a Stable Diffusion prior, finding that introducing edges into the segmentation task can enhance performance. They introduced the BDE and DBIA modules, which can distinguish between different tasks and achieve better detail generation capabilities. The method efficiently utilizes one-step sampling and shows significant improvement over previous methods across multiple test projects.

### Strengths
1. The author discovered that the introduction of edges can enhance the detail and performance of segmentation. They used batch discriminative embedding to distinguish between edges and segmentation. This is a novel method.
2. The author provided detailed experiments that demonstrate the method's strong performance across multiple aspects, and also included an ablation study to prove the effectiveness of each module.

### Weaknesses
 1. The description of the one step inference is not comprehensive enough, please see Q2
 2. For dichotomous segmentation, using an RGB 3-channel VAE to encode a single-channel segmentation mask might be a bit overkill. As an advancement in dichotomous segmentation, some earlier works have used diffusion models for matting, which also achieved very good results. However, considering that it can produce decent results in just one step, it is acceptable.

### Questions
1. In emu-edit, they introduced a method called task embedding, it is a learnable embedding added to the time step embedding, to distinguish the different task in multi-task training. As your Batch-Discriminative Embedding contains more detailed design, do you have any performance comparison between your Batch-Discriminative Embedding and the task embedding?
2. For the one step mask sampling, in 4.4 and the fig 5 only state that it is building upon the established DDPM, but no more detailed description and implemented the one step sampling, could you please provide more details on it?
3. From the paper, it shows that the author used SD2.1 and SD turbo as initialization weights, and there is a channel-wise concat operation before feeding into the UNet, which changes the number of channels in the input layer. I would like to know how the pretrained weights are handled for the input layer when they are used (eg. duplicate/zero).

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper address the problem of Dichotomous Image Segmentation (DIS) with a generative foundation model, StableDiffusion, by modifying with several key modules.

### Strengths
1. The proposed method reaches SOTA performance and beat other concurrent diffusion-based approach on DIS datasets.
2. This is an early attempt that uses a pre-trained generative model for challenging DIS task.
3. The method is efficient in comparison to the line of work that follows SegDiff, which runs diffusion process for more time-steps.
4. The ablation studies include both quantitative numbers and qualitative visualizations, which are helpful for understanding how the whole framework is designed.

### Weaknesses
1. The application scenario seems limited. The task setting is only limited to Dichotomous Image Segmentation. It could be more convincing if the authors can also address the applicability of this approach in more settings, e.g. image matting, foreground object segmentation, edge detection.
2. Running diffusion for one-step for segmentation is not a great contribution. This paper might miss some related work that is in the line of DDPM-Seg [1]. A lot of recent work that uses StableDiffusion for unsupervised semantic segmentation and open-vocabulary segmentation is indeed one-step in inference time.
3. The methods are not novel. From the ablation studies, the most prominent modules are Batch-Discriminative Embedding and Detail-Balancing Interactive Attention (DBIA). However, Batch-Discriminative Embedding is proposed by previous work and this work is more of applying that module for DIS task. DBIA is a modified attention module but specifically designed for DIS.

### Questions
1. Latent diffusion models such as SD would map the original image into low-dimensional latents e.g. 32x32x4 for 512x512x3 input. I do not understand well how the low dimensional latent is decoded to high-resolution mask.
2. I would like to see if the proposed methods can be transferrable to other architectures, e.g. pixel-space diffusion UNets and latent DiT.

The followings seem typos or grammar issues, which do not affect my ratings:
1. line 64, "in balance receptive field expansion" should be "in balancing ..."
2. line 72, "It’s power is" should be "Its power is"
3. line 363, "conloution" should be "convolution"
4. line 530, "attmpt" should be "attempt"

### Soundness
3

### Presentation
3

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
This paper proposes a DiffDIS framework based on SD V2.1 to tackle the fine-grained dichotomous image segmentation task. The proposed DiffDIS finetunes the diffusion U-Net in the VAE-encoded latent space and introduces several modifications to enhance the edge perception, including:  1) The edge-assisted training strategy introduces batch-discriminative embedding to enable the mask and edge prediction in a single SD model and conducts interactive attention between the mask and edge branches, 2) Add to zero convolution to enhance the condition injection at different scales. The paper is easy to follow. The proposed method only uses single-step denoising to enhance efficiency and achieves SoTA performance on all the benchmarks.

### Strengths
+ The proposed method is technically sound and streamlined, unleashing the dimension-reduction ability of VAE and the representation capacity of diffusion U-Net in the perceptional task.
+ The paper is well-organized and easy to follow.
+ The proposed method achieves superior performance gains on the benchmark datasets.
+ Some experimental observations, such as the restorative capacity of VAE (Tab. 1) and the influence of time-step (Tab. 4) might be valuable to the community.

### Weaknesses
 + Some concerns about the technical contribution should be clarified: see Q4 and Q5.
+ Some concerns about the robustness and model efficiency should be addressed: see Q2 and Q6
+ Some other concerns about the methodology should be tackled: see Q1 and Q3

### Questions
1. In Algorithm 1, the authors finetune diffusion U-Net by only considering t=T and directly optimizing with $x_0$  instead of noise, where the diffusion UNet seems to degenerate into a common UNet and is inconsistent with SD. Why did the authors not train the diffusion U-Net using the consistent objective with SD and deploy an efficient ODE solver to enable efficient inference?
2. Considering the randomness of the noise sampling process, is the model sensitive to the sampled noise in the inference stage? It is suggested that an analysis of the performance be made using varied noise.
3. Can this performance be improved by sending some text embedding given by the caption model instead of using the empty text embedding?
4. What is the difference between the proposed Detail-Balancing Interactive Attention (Eqn.6) and the common cross-attention deployed between the mask and edge feature?
5.  The multi-scale injector introduces condition signals into blocks. There lacks a comparison with the common condition/signal injection methods, such as the cross-attention in SD.
6. Since VAE contains a large number of parameters, the authors should give a comparison in terms of the inference speed and parameters with state-of-the-art methods.

### Soundness
3

### Presentation
3

### Contribution
3
