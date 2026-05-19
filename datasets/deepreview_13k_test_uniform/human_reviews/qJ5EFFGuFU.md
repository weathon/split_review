# SAIR: LEARNING SEMANTIC-AWARE IMPLICIT REPRESENTATION

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Implicit representation of an image can map arbitrary coordinates in the continuous domain to their corresponding color values, presenting a powerful capability for image reconstruction. 
Nevertheless, existing implicit representation approaches only focus on building continuous appearance mapping, ignoring the continuities of the semantic information across pixels.  
As a result, they can hardly achieve desired reconstruction results when the semantic information within input images is corrupted, for example, a large region misses. 
To address the issue, we propose to learn \textit{semantic-aware implicit representation (\textsc{SAIR})}, that is, we make the implicit representation of each pixel rely on both its appearance and semantic information (\eg, which object does the pixel belong to).
To this end, we propose a framework with two modules: (1) building a semantic implicit representation (SIR) for a corrupted image whose large regions miss. Given an arbitrary coordinate in the continuous domain, we can obtain its respective text-aligned embedding indicating the object the pixel belongs. (2) building an appearance implicit representation (AIR) based on the SIR. Given an arbitrary coordinate in the continuous domain, we can reconstruct its color whether or not the pixel is missed in the input.
We validate the novel semantic-aware implicit representation method on the image inpainting task, and the extensive experiments demonstrate that our method surpasses state-of-the-art approaches by a significant margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel implicit representation learning method to tackle the limitations of existing approaches which learn the mapping function heavily relying on the appearance information. The core of the proposed method is the Semantic-Aware Implicit Representation learning procedure, consisting of a Semantic IR module which learns pixel-wise semantic features with aggregated information from neighbors, as well as an Appearance IR which reconstruct the RGB values based on both semantic and appearance information. Experiments are conducted on CelebAHQ and ADE for image inpainting task, demonstrating the effectiveness of the proposed SAIR.

### Strengths
- the motivation and the corresponding solution is easy to follow
- the experiments validate the contributions of different components of SAIR

### Weaknesses
- How to understand the claim that the $f_\theta$ of SIR learns the **text-aligned** embeddings (Eq (4))? 
    - though the operation similar with MaskCLIP dose not alter the text-aligned feature space, these features are then processed by learnable $\theta$, there is no guarantee that the embedding space is text-aligned.
    - why do the authors highlight the **text-aligned** embeddings? If I understand correctly, the embedding space is just an enhanced pixel-wise semantic feature space.
- Why mapping the original CLIP feature space by $f_\theta$ performs better than the original CLIP feature space? Furthermore, the details about how to implement '*models without SIR block*' is not clear. 
- there is the lack of experimental details about ablation study, like which dataset is incorporated for ablation?
    - in section "*Study on the models with/without SIR block.*" of 5.3, why not directly use the GT segmentation maps instead of calculating by CLIP features?
- the figures 1 and 2 are duplicated, they demonstrate the almost same information.
- is the propose SAIR robust/generalizable for other degraded images, like raining or noised images.

### Questions
please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new implicit representation named SAIR, shorted for Semantic-Aware Implicit Representation. SAIR uses MaskCLIP to extract pixel-level semantic features from CLIP model, and combine the representation with LIIF to learn an implicit representation conditioned on the semantic features. Authors evaluate the semantic aware implicit function by reconstructing the masked regions on CelebAHQ and ADE20K dataset. The proposed methods outperforms prior works like LIIF.

### Strengths
1. I like the idea of introducing CLIP feature into LIIF. Although the model is conditioned on the masked image input, the CLIP feature is high-level enough to capture the semantic information in the image. 
2. The inpainting results outperform both LAMA (inpainting-based method) and LIIF (implicit representation method) by a reasonable margin.

### Weaknesses
1. Some reference format is not correct. For example, CelebAHQ, ADE20K in the introduction. 
2. Some equations are not consistent across the paper. In Eqn(2), SIR takes I, M, p as input, but in Eqn(4)(5), SIR only takes I, p as the input. I would suggest authors to make notations consistent and clear. 
3. AppEncoder is not clearly defined in Section 4.3. I think it is sometimes mixed with SIR. 
4. The result in Table 5 is confusing. Authors trying to study the effect of SIR block, but after removing SIR, the network is just AppEncoder ConvNet. Authors didn't explain clearly how to evaluate ADE20K mIoU with AppEncoder alone.  
5. Figure 1 is kind of confusing. The green arrow and red arrow point to "Hair" and "Eye". But I don't think the proposed model will predict the text label of the masked pixel. 
6. One key ablation I would suggest authors add in both Table 1 and Table 2, is that compare SAIR without CLIP and with other networks other than CLIP, e.g. ImageNet pre-trained models.

### Questions
1. In the dataset section, authors states CelebA and ADE20K have 19 and 150 classes respectively. Are these semantic labels of the dataset used during training and testing?
2. In Section 5.3, authors state " we used CLIP_T to filter the image feature CLIP_I". The term filter is not very clear or straightforward. Are authors trying to imply "dot product"?
3. Is there a loss for semantic feature reconstruction? If not, how could SIR reconstruct the semantic features, as stated in Section 5.3. 
4. Is there any comparison with mask ratio 0? Just compare to the original LIIF on super-resolution tasks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an implicit representation method to tackle the task of image inpainting. Semantic information across pixels is introduced to help produce better reconstruction results. Specifically, two main modules are constructed, i.e. a semantic implicit representation to obtain text-aligned embeddings with CLIP and an appearance implicit representation that incorporates the semantic embedding. The proposed method achieves superior performance than previous works.

### Strengths
- The idea of incorporating CLIP-based text-assisted semantic information is reasonable to obtain higher-quality reconstructed images. The shown performance promotion over compared methods is also significant.
- Extensive experimental studies are provided to demonstrate the effectiveness of the proposed method.
- The code is also provided for reproducing.

### Weaknesses
- One main concern comes from the application of this stream of methods. In other words, the current evaluation benchmark is made manually and may be too theoretical. I wonder if any real-life application cases can be shown, e.g. recovering objects that are occluded or blurred via dramatic camera motions. If there are more proper real application cases, there is no need to be limited to the ones I list.
- Another concern lies in the computation cost. It is suggested to compare the inferring and training cost with previous methods, as it seems the two-module framework may be costly.

### Questions
- What is the main advantage of the coordinate-based implicit representation method over diffusion-model ones for image inpainting? Diffusion models have shown great power in recent generation tasks, also including inpainting. It is suggested to discuss this question and include necessary related works, which will determine the significance of the contribution.
- Can the proposed method apply to any in-the-wild images, not limited to the used datasets? If yes, it is better to show some samples.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an image inpainting approach. The authors addressed the shortcomings of existing implicit representation approaches that tends to ignore overall semantics of the image and only looks to preserve appearance. The authors proposed an implicit representation that adds semantic information of pixels through alignment with CLIP text features.

### Strengths
- The paper is well written and easy to follow. 
- The motivation of the work is clearly outlined. 
- The integration of semantic information in preserving certain structures in the image during inpainting is intuitive and the experimental results demonstrate the effectiveness.

### Weaknesses
- I believe the technical novelty of the approach is limited since the improvement mainly comes from the rich representations of the clip embeddings. CLIP embeddings have been extensively used in many zero-shot tasks that exploit the strong semantics learned by the clip embeddings e.g. ZegClip (CVPR 2023), Hierarchical Text-Conditional Image Generation with CLIP Latents (arXiv 2022), NUWA-LIP (CVPR 2023). 
- None of the approaches that authors compare against use text embedding alignments. In particular, I believe a similar text-based alignment can be made with the implicit representations of LIIF. 
- Lack of comparison with recent approaches like NUWA-LIP.
- How does the authors' approach compare against powerful generative models like diffusion model which are excellent at image impainting as well.

### Questions
Please take a look at the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
