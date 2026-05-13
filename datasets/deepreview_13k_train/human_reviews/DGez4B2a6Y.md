# A Plug-and-Play Image Registration Network

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Deformable image registration (DIR) is an active research topic in biomedical imaging. There is a growing interest in developing DIR methods based on deep learning (DL). A traditional DL approach to DIR is based on training a convolutional neural network (CNN) to estimate the registration field between two input images. While conceptually simple, this approach comes with a limitation that it exclusively relies on a pre-trained CNN without explicitly enforcing fidelity between the registered image and the reference. We present \emph{plug-and-play image registration network (PIRATE)} as a new DIR method that addresses this issue by integrating an explicit data-fidelity penalty and a CNN prior. PIRATE pre-trains a CNN denoiser on the registration field and \emph{``plugs''} it into an iterative method as a regularizer. We additionally present PIRATE+ that fine-tunes the CNN prior in PIRATE using deep equilibrium models (DEQ). PIRATE+ interprets the fixed-point iteration of PIRATE as a network with effectively infinite layers and then trains the resulting network end-to-end, enabling it to learn more task-specific information and boosting its performance. Our numerical results on OASIS and CANDI datasets show that our methods achieve state-of-the-art performance on DIR.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new deformable registration framework for medical imaging. Their main contribution is the inclusion of a "plug and play" prior into the registration framework. A novelty of the work is using a denoiser to specify priors over registration fields. They also propose an additional model (PIRATE+) that fine-tunes the CNN prior in PIRATE using deep equilibrium models (DEQ). The authors then evaluate their work on standard brain MRI datasets used in the registration literature.

### Strengths
The paper seems to be the first at using plug-and-play priors for registration, which could be a useful contribution in this already rich space. 

The work obtains good quantitative results on standard benchmarks for deformable medical image registration.

### Weaknesses
My main issue is with the writing and presentation of this paper:

- There was virtually no intuitive explanation of what plug-and-play does, why it is useful compared to other approaches, etc. Given that one of the reported contributions of the paper is to show that denoising priors can be used for registration, the lack of any explanation of why denoising is appropriate, how it works, etc. is quite conspicuous. The paper should elaborate on the theoretical justifications for using a denoiser as a prior, and how this relates to the statistical properties of plausible deformation fields. For example, is the assumption that the noise in a deformation field is Gaussian? If so, why is this a reasonable assumption?

- What is the main drawback with current deformable image registration models that this current approach is addressing? Why might plug and play be better than other forms of priors for registration? The introduction does not address this. The paper needs to clearly articulate the limitations of existing methods and how the proposed plug-and-play approach offers a solution. It should also discuss why plug-and-play is advantageous over other regularization techniques, such as smoothness priors, in the context of registration.

- The methods section is poorly written, without high-level insights presented before details. For example, the methods starts immediately with the PIRATE iteration updates instead of presenting what the objective being optimized is, what the prior is capturing, etc. The paper should begin with a clear statement of the optimization problem and then explain how the plug-and-play prior is incorporated into the objective function. It should also explain the specific role of the denoiser within this optimization process.

- It is unclear what issue PIRATE+ is trying to improve upon. The methods section simply says "PIRATE+ uses DEQ to fine-tune the regularizer D in the PIRATE iteration by minimizing...", but there was no explanation of why the regularizer might not be accurate in the first place. The paper needs to explain the limitations of using a generic denoiser as a prior, and how fine-tuning it with DEQ addresses these limitations. What are the specific characteristics of the registration task that the fine-tuned regularizer is capturing?

- The method section would benefit by using pointers back to Fig. 1 and explaining the various steps of that figure.

### Questions
1. What advantages do you think plug and play priors offer for registration ?

2. Why might denoising be appropriate as a prior for registration?

3. I am not able to understand what PIRATE+ addressing? The methods says "PIRATE+ fine-tunes the AWGN denoiser into a task-specific regularizer using DEQ" but this is quite opaque to me. What does "task-specific regularization" mean in this case?

4. Are there any limitations of the method compared to traditional CNN-based deformation models like VoxelMorph in terms of usability, training time, etc.?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
They proposed a new DIR method which is the plug-and-play approach that trains a CNN-based denoiser on the registration field. With
this denoiser as a regularizer within iterative methods, deep equilibrium learning is used as a fixed point iterator. The authors use a pre-trained denoiser for such regularization problems. The proposed method achieved the best performances on OASIS & CANDI datasets with reasonable qualitative results corresponding to quantitative results.

### Strengths
+ The proposed method used the DEQ approach for iterative registrations. The adapting approach is unique and reasonable. Their training loss looks going down well on the datasets.
+ DEQ approach successfully addressed registration problems with PnP(plug-and-play) method with appealing gain in Tables 1 & 2.

### Weaknesses
 + I didn't understand the motivation of using pre-trained denoisor for regularizations. Why isn't the trainable denoiser used for this task? Specifically, the paper lacks a clear explanation of why a pre-trained denoiser, trained on a generic denoising task, is suitable for regularizing registration fields. The connection between the statistical properties learned by the denoiser and the desired characteristics of a good registration field is not well established. This raises concerns about whether the pre-trained denoiser is actually providing a meaningful regularization or just adding an arbitrary constraint. 
+ No ablation studies about the necessity of the usage of a pre-trained model. The paper does not provide any ablation study to justify the usage of pre-trained model. It's unclear if the performance gain is due to the pre-training or some other factors. It is necessary to compare the performance with a model that does not use any pre-trained model, or with a randomly initialized denoiser for a fair comparison. 
+ Less analysis on the DEQ model : I would like to see the convergence of the number of function evaluation(NFE) along with the training iterations. The paper should provide a more detailed analysis of the DEQ model's behavior. The convergence of NFE is crucial for understanding the efficiency and stability of the deep equilibrium approach. Without this analysis, it's difficult to assess if the model is converging to a stable solution. 
+ In general, the result section is short of significant experiments to support their claim. For example, Figure 3 is a single instance analysis rather group analysis. The reliance on single-instance analysis in Figure 3 is insufficient to support the claims made. The paper needs to include group analysis to demonstrate the generalization capability of the proposed method. The results should be statistically significant and not just based on a single case. 
+ Generalization needs to be validated with group analysis.

### Questions
+ What is the corner case for the proposed method?
+ Memory consumption needs to be reported according to fixed size of datasets.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of deformable (non-rigid) image registration in the context of biomedical image analysis. In particular, it proposes two methods (PIRATE and PIRATE+) for the regularisation of the deformation field. In contrast to existing deep learning approaches to image registration, the approach presented here explicitly integrates a data-fidelity penalty as well as a CNN prior (this is pre-trained and acts as regularizer for the deformation field). The authors argue that this improves the fidelity between the registered image and the reference image. The second approach, PIRATE+, is similar to this but uses a CNN prior that is trained using deep equilibrium models.

### Strengths
The proposed methods (PIRATE and PIRATE+) are novel methodological contributions which is positive. Additionally, the proposed framework is compared to a number of different methods, including DL and non-DL methods, which is very good. This also includes the best-performing method from recent comparative studies (Mok and Chung, CVPR 2020, MICCAI 2020). The results reported outperform this method in terms of registration accuracy. Another strength of the paper is the careful review of the state-of-the-art in the field. This is well done and comprehensive, allowing the reader to place the proposed work in the context of the SOTA.

### Weaknesses
The weaknesses are mainly related to the evaluation of the proposed framework:

- The methods compared in the paper use very different loss or cost functions as well as different models for the parameterization of the deformation field. This makes the papers' comparison of the registration accuracy in terms of voxels with negative Jacobian very difficult to come across methods. Registration accuracy measured in terms of Dice is more meaningful. At the same time, it would have been good if the authors had used some additional non-brain datasets which have landmarks and thus allow the calculation of quantities such as the target registration error. One such dataset is from the EMPIRE10 challenge...

- The run-time of the proposed framework is significantly higher than those of other DL methods. This is a significant disadvantage for clinical applications.

### Questions
- The paper proposes two methods, PIRATE and PIRATE+. I am a bit unclear on what are the conclusions: Is PIRATE+ is better than PIRATE? When should PIRATE be used? When should PIRATE+ be used?

- How are the parameters in the other registration methods chosen, especially in the context of trading off registration accuracy and regularisation of the deformation field?

- The run-time of the proposed framework is significantly higher than those of other DL methods. What are the reasons for this?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new deformable image registration (DIR) method called Plug-and-play Image Registration Network (PIRATE). PIRATE offers a new approach to DIR by integrating explicit data fidelity and a CNN prior. The paper also presents an extended version, PIRATE+, that fine-tunes the CNN prior using deep equilibrium models (DEQ). Both methods are validated on the OASIS and CANDI datasets, with results indicating state-of-the-art performance in DIR.

### Strengths
- Deformable image registration is a challenging task in medical image analysis, and the authors' approach of using a plug-and-play method to address this challenge is commendable.

- There is a comprehensive coverage of related work, which provides a solid foundation and context for the proposed method.

- The introduction of learned denoisers for regularizing the registration fields and the use of DEQ to fine-tune the regularizer within PnP iterations are innovative contributions.

- The extensive validation on two widely used datasets, OASIS and CANDI, highlights the robustness and general applicability of the proposed methods.

- The qualitative visual results presented in the paper convincingly demonstrate the superiority of PIRATE and PIRATE+ compared to existing deep learning and iterative methods.

### Weaknesses
 - The incremental improvements in results, especially in the second decimal place, raise concerns about the practical implications of such minor improvements, particularly for downstream tasks, especially that the proposed method is an iterative optimization-based approach that significantly increases inference time compared to deep learning based methods. The gains, while numerically present, may not justify the added computational cost and complexity, especially if the downstream task is not highly sensitive to such small registration differences. It would be beneficial to see a more thorough analysis of the trade-off between accuracy gains and computational overhead.

- The paper makes heavy use of acronyms, which affects readability. Notably, the acronym "DU" is mentioned without a clear definition. The lack of a comprehensive list of acronyms makes it difficult to follow the technical details, and the reader is forced to constantly refer back to previous sections to understand the meaning of each acronym. This significantly hinders the readability of the paper.

- While the paper's focus on brain MRI datasets is appreciated, it would have been beneficial to see the adaptability of PIRATE and PIRATE+ to other anatomies and imaging modalities. The current evaluation is limited to a single anatomical region and imaging modality, which limits the generalizability of the proposed method. It is unclear whether the method would perform equally well on other types of medical images, such as CT scans or images of different body parts.

### Questions
- How do the minor improvements in quantitative results translate to real-world applications, especially considering the potentially longer inference time of the iterative optimization-based approach?

- Is registration performed on the full 3D scan, or are 2D slices of roughly pre-aligned images used?

- How does PIRATE and PIRATE+ compare in terms of computational efficiency and scalability?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
