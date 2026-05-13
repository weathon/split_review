# AugKD: Ingenious Augmentations Empower Knowledge Distillation for Image Super-Resolution

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Knowledge distillation (KD) compresses deep neural networks by transferring task-related knowledge from cumbersome pre-trained teacher models to more compact student models. However, vanilla KD for image super-resolution (SR) networks only yields limited improvements due to the inherent nature of SR tasks, where the outputs of teacher models are noisy approximations of high-quality label images. In this work, we show that the potential of vanilla KD has been underestimated and demonstrate that the ingenious application of data augmentation methods can close the gap between it and more complex, well-designed methods. Unlike conventional training processes typically applying image augmentations simultaneously to both low-quality inputs and high-quality labels, we propose AugKD utilizing unpaired data augmentations to 1) generate auxiliary distillation samples and 2) impose label consistency regularization. Comprehensive experiments show that the AugKD significantly outperforms existing state-of-the-art KD methods across a range of SR tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method for knowledge distillation for image super-resolution. The authors propose using auxiliary training samples by zoom in and zoom out operations on the training images, and apply label consistency regularization by data augmentation and inverse augmentation.

### Strengths
The motivation makes sense that for image super-resolution knowledge distillation, the guidance of the teacher model is shaded by the ground truth. So the authors propose a specific knowledge distillation training paradigm for image super-resolution.
Experiments show that the proposed method surpasses scratch training and 7 baseline knowledge distillation methods.
The ablation studies verifies that the proposed auxiliary distillation samples and label consistency regularization improve student model performance.

### Weaknesses
The question answered by the paper is not a major one, as it is a knowledge distillation method specifically for the image super-resolution task. Does it also apply to other low-level tasks? The method's applicability to other low-level vision tasks such as denoising or deblurring is not thoroughly explored, which limits the impact of the work. The paper would benefit from a more detailed discussion on how the proposed auxiliary sample generation and label consistency regularization could be adapted to these other tasks, including specific examples of augmentation strategies.
The image super-resolution models used for experiments are not state-of-the-art. EDSR is from 2017 and RCAN is from 2018. SwinIR is newer from 2021 but only "Scratch" and "KD" is compared with the proposed method for SwinIR. As the proposed method is claimed to be model-agnostic, it is supposed to be applied to more advanced models to demonstrate the effectiveness. The choice of older models like EDSR and RCAN raises concerns about the relevance of the experimental results to current state-of-the-art super-resolution research. While SwinIR is included, the limited comparison to only "Scratch" and basic KD methods does not fully demonstrate the method’s potential. A more comprehensive evaluation using recent, high-performing models and comparison against more advanced knowledge distillation techniques is needed to substantiate the claims of model-agnosticism and effectiveness.

### Questions
For the zoom out operation, we have the ground truth for I_LR_zo, and given the analysis in Section 3.2, the teacher model output for I_LR_zo would be shaded by the ground truth. So there seems to be additional complexity for this path to go through the teacher model.

### Soundness
3

### Presentation
3

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
The paper proposes AugKD, a new knowledge distillation method for image super-resolution. AugKD contains two special designs, auxiliary
distillation sample generation, and label consistency regularization. By comparing with other distillation counterparts on four benchmark datasets, AugKD shows its superiority.

### Strengths
1. The paper has a deep insight into super-resolution tasks and its method is simple and effective.
2. The code is also provided for reproduction.

### Weaknesses
1. **The paper writing could be further improved.** For instance, the authors claim the motivation - *'the teacher's output contains barely extra information exceeding GT, thus the “dark knowledge” of the teacher being hardly transferred to the student model through KD'* in Line #76-78 in the Introduction part. However, in Section 3.2 (Motivation) and Figure 2, the authors show the motivation by measuring the PSNR of outputs between the teacher and the student. It seems that the two statements are a little bit contradictory, as the former one indicates that the teacher's outputs can not be good learning materials but the second one leverages the the teacher's outputs as the reference for evaluating whether KD method is good or not. Such circumstances make it hard to understand the central idea of the paper.

2. **The paper lacks further deep analysis of where the performance gains are from.** From the results in Figure 2, it seems that the gains are from improving the fidelity between the teacher and the student. A further question is *Why AugKD can improve the fidelity?* And in Lines #521-529, the authors compare AugKD with data expansion. Thus, a question arises *Does the improvement of fidelity from the expansion of the training set by augmentation?* From another perspective, the question is *how does the augmentation strength affect the fidelity and the final distillation results?* By answering such a series of questions, the paper can help the readers understand the intrinsic mechanism of AugKD.

3. **A minor question about the design of the method.** Although I think the design of the inverse augmentation is clear and plausible, I'm still curious about what would happen if we dropped the inverse augmentation and added the augmentation at the end of the teacher's model in the training stage and still utilized the same architecture as the method in the inference stage.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores an improved augmentation strategy for knowledge distillation (KD) specifically in image super-resolution (SR). It introduces AugKD, which uses unpaired data augmentations to create auxiliary distillation samples and enforce label consistency. This approach addresses limitations in traditional KD methods by enhancing the student model’s learning process through diverse training samples, aiming to improve efficiency and effectiveness in SR tasks.

### Strengths
- **Motivation**: The paper provides a clear motivation for improving data augmentation strategies in knowledge distillation (KD) for super-resolution (SR), highlighting the unique challenges in SR tasks.
- **Comprehensive Ablations**: Extensive ablation studies test various experimental setups for KD in SR, demonstrating a thorough examination of the method's effectiveness under different conditions.

### Weaknesses
 - **Modest Improvements**: Results in Figure 2 and Tables 2–4 show only slight gains, questioning the practical value of AugKD over existing methods.
- **Limited Insight on Augmentation Impact**: Ablation studies explain augmentation effects but don’t clarify *why* this strategy improves KD. Further detail on what specific features AugKD captures would be helpful.
- **Augmentation Benefits Unclear**: It’s unclear how augmentations help representations learned through KD or why prior methods failed to capture these.
- **Potential Architecture Constraints**: While AugKD is claimed to be generalizable, performance with some architectures (like SwinIR) suggests possible limitations.

### Questions
- Please see weakness.

### Soundness
2

### Presentation
2

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
This paper introduces AugKD, a novel method aimed at improving image super-resolution (SR) by leveraging data augmentations to generate auxiliary distillation samples and enforce consistency regularization. This work analyzes the mechanisms of KD for SR and propose AugKD adapted to the unique task with label consistency regularization. Extensive experiments on various SR tasks are presented across multiple datasets to validate the proposed approach.

### Strengths
1. The paper thoroughly analyzes the mechanics and distinct challenges of knowledge distillation (KD) in the context of SR, proposing the use of data augmentations to enhance distillation.
2. The AugKD strategy is adaptable to different SR models and tasks, yielding substantial performance improvements across several networks and settings.
3. The well-organized structure and clearly described method facilitates reproducibility.

### Weaknesses
1. The visualization in Fig. 2 is unclear. Replacing it with a bar plot may improve readability and convey the idea more effectively.
2. Although lines 241-244 highlight that the adaptive selection of zoom-in samples is ineffective, it lacks sufficient experiments to support this claim. 
3. The motivation by using label consistency regularization is unclear.

### Questions
1. How does AugKD affect training efficiency in comparison to other KD techniques?
2. What's the rationale behind the specific choice of zoom-in and zoom-out augmentations for AugKD?
3. Given that some other image augmentations, such as translation, are also invertible, would it be beneficial to include them in the consistency regularization module?
4. What is the motivation of using label consistency regularization for SR? Is it also also suitable for other low-level tasks?
5. Does the proposed method also adapt to other backbones, like Mamba?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes AugKD, an innovative knowledge distillation (KD) technique specifically designed for image super-resolution (SR). AugKD incorporates zooming augmentations and label consistency regularization to enhance the training process. In this approach, both randomly cropped high-resolution (HR) patches and their down-sampled low-resolution (LR) counterparts are fed into a pre-trainedd teacher model to generate target labels. These labels are then used to guide the training of the student model. To further improve the robustness and generalization of the student model, consistency regularization is applied through a series of invertible data augmentations. Extensive experiments have been conducted across multiple public image super-resolution datasets, demonstrating the effectiveness and versatility of the proposed method.

### Strengths
1. A novel KD method is proposed in this paper. AugKD improves the training process by using zooming augmentations and label consistency regularization. To make the student model more robust and versatile, consistency regularization is applied using a series of invertible data augmentations. Extensive quantitative experiments and qualitative analysis are provided to demonstrate the validity of the methodology
2. Compared with previous methods, the performance is improved on models with multiple scales. For instance, compared with training from scratch, the performance of RCAN on x4 scale is improved by 0.25dB on Urban dataset.
3. AugKD is general and effective, easy to follow, and convenient for reproducing the method.
4. Paper is well written and organized.

### Weaknesses
1. This paper proposed multiple effective improvements, while I'm curious that, besides zooming augmentations, could other data augmentation methods improve performance? Specifically, the paper does not explore the impact of augmentations that introduce more significant distortions, such as elastic transformations or perspective changes, which could potentially enhance the robustness of the student model to a wider range of real-world degradations. It's unclear if the choice of zooming is optimal or if other augmentations could provide complementary benefits.
2. The ablation of the label consistency is not sufficient. Have the authors tried other non-invertible ways of regularization? The current implementation only considers invertible transformations like flipping and rotation. It would be beneficial to explore non-invertible augmentations, such as random cropping or patch shuffling, to understand their impact on label consistency and the overall performance. The paper lacks a comprehensive analysis of how different regularization techniques affect the student model's learning process and generalization ability.

### Questions
1. Referred to Tab.9 in the paper, could you explain the reason why the performance of the combination of FAKD and AugKD is lower than AugKD?
2. The performance of AugKD on the X4 scale RCAN model is presented in Tab.3, why is it better than the result of heterogeneous distillation in Tab.5?
3. Does $L_{dukd}$ in Fig. 1 indicate the same with the $L_{augkd}$ computed in Fig.4?

### Soundness
2

### Presentation
4

### Contribution
3
