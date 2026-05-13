# SITReg: Multi-resolution architecture for symmetric, inverse consistent, and topology preserving image registration using deformation inversion layers

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Deep learning has emerged as a strong alternative for classical iterative methods for deformable medical image registration, where the goal is to find a mapping between the coordinate systems of two images. Popular classical image registration methods enforce the useful inductive biases of symmetricity, inverse consistency, and topology preservation by construct. However, while many deep learning registration methods encourage these properties via loss functions, none of the methods enforces all of them by construct. Here, we propose a novel registration architecture based on extracting multi-resolution feature representations which is by construct symmetric, inverse consistent, and topology preserving. We also develop an implicit layer for memory efficient inversion of the deformation fields. Our method achieves state-of-the-art registration accuracy on two datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is about a new deformable image registration method which is able to extract multi-resolution features that are symmetric, inverse consistent, and topology-preserving. The new framework is new and symmetric and inverse consistent by construct. Based on the deep equilibrium network framework, a new deformation inversion layer is proposed.

### Strengths
The paper is well written with good introduction and descriptions of symmetric, inverse consistent, and topology-preserving registration methods. 

The proposed DL architecture is inverse consistent and symmetric by construct, rather than by using loss functions. 

The use of deformation inversion layers seems interesting, based on the deep equilibrium network framework.

### Weaknesses
Although the new framework is interesting, as listed in Table 2, the accuracy improvement is not significant. 

As shown in Table 3, the computation efficiency and memory usage have not improved.

### Questions
1.	In Figure 1, the images x_1 and x_2 are not defined previously and are unclear to me.

2.	Cannot find Figure 3.2 in Section 3.2

3.	Is the image registration framework diffeomorphic?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the deformable medical image registration with symmetric, inverse consistent, and topology-preserving properties, which is achieved by construction via a multi-resolution deep neural network. The proposed method is compared with three existing methods, i.e., SYMNet, VoxelMorph, and cLapIRN. The experimental results demonstrate the effectiveness of the proposed approach.

### Strengths
This paper works on an interesting research problem. It integrates existing strategies to achieve all the symmetric, inverse consistent, and topology-preserving properties in one network using an end-to-end training.

### Weaknesses
1. Insufficient study on related work. Unlike what is stated in the paper, the LDDMM method has been used in deep learning, such as DeepFlash[1], NODEO[2], R2Net[3], etc. Also, the inverse consistency by construction using multistep deep registration [4], which is quite close to this paper, is missing in the related work and experimental comparison.

[1] Wang and Zhang, DeepFLASH: An Efficient Network for Learning-based Medical Image Registration, CVPR 2020. 
[2] Wu et al., Nodeo: A neural ordinary differential equation based optimization framework for deformable image registration, CVPR 2022. 
[3] Joshi and Hong, R2Net: Efficient and flexible diffeomorphic image registration using Lipschitz continuous residual networks, Medical Image Analysis, 2023. 
[4] Greer et al., Inverse Consistency by Construction for Multistep Deep Registration, MICCAI 2023. 

2. Unclear presentation with unexplained statements. Such as, 1) "However, SYMNet does not guarantee symmetricity by construct", why? How to draw this conclusion? 2) Denoting the feature extraction network by h, how is this feature extraction network designed? Do we need to pretrain it or train together with the following network? 3) Squaring and scaling are not enough to guarantee the diffeomorphic property of deformations, we need an additional loss term or strategies to enforce the smoothness of the initial velocity fields first. However, this paper uses the same loss term on the smoothness of deformations in non-diff VoxelMorph, is it a reasonable choice?

3. Insufficient experimental results. This paper should compare the two most related works, i.e., [Iglesias 2023] that is mentioned in the introduction and the above [Greer 2023] that is missing in the paper, and some traditional methods, like SyN in ANTs and Symmetric LDDMM. Also, can you show more qualitative results to demonstrate the improvement of the proposed method and analyze the contribution of each design accordingly?

4. All the strategies used in this paper are what were used before, so, what are the challenges of this work? Is it necessary to have such a complicated network in practice?

### Questions
Please check the weakness section for the questions.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a deep learning-based approach to deformable image registration, which enforces symmetry, inverse consistency, and topology preservation. In contrast to previous approaches, which enforce these constraints via loss functions, the approach proposed here achieves this via construction. Additionally, the paper uses a multi-resolution feature representation for image registration. The approach is evaluated on the tasks of inter-subject brain MR registration, evaluated on the LPBA40 and Oasis datasets.

### Strengths
The paper addresses an important topic in biomedical image analysis. Developing robust and reliable methods for image registration is still an unsolved problem. The paper contains a good summary of the state-of-the-art in terms of previous publications. Similarly, the proposed method is compared against a number of strong baselines, including VoxelMorph, SYMNet and cLapIRN.

### Weaknesses
The symmetric formulation proposed in section 3.1 seems not entirely new. Indeed, the authors acknowledge this by stating that a similar approach has been used in recent registration methods (Estienne et al., 2021; Young et al., 2022). The multi-resolution formulation proposed in section 3.2 seems rather natural (also in the symmetric setting), so I am unclear on how this is different from standard multi-resolution formulations, which are ubiquitous in image registration settings.

The evaluation of the registration accuracy is limited to the assessment of Dice overlap and Hausdorff distance after registration. It would have been good if the authors had used some additional non-brain datasets which have landmarks (e.g. lung CT images from the EMPIRE10 challenge) and thus allow the calculation of quantities such as the target registration error. Furthermore, the improvements in registration accuracy seem rather than marginal. No visual examples of the registrations are provided.

### Questions
- What is the key novelty in section 3.2? How is this different from the traditional multi-resolution (except the symmetric formulation)?
- Can you comment on the significance of the improvement of the registration results?
- The advantage of symmetry and inverse consistency over loss-based approaches is not clear, as all methods seem to provide symmetric and inverse consistent registrations apart from numerical accuracy. Can you comment on this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
