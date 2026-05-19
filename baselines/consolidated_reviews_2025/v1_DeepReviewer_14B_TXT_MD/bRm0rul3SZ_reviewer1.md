### Summary

This paper propose a method for image-to-image translation where the source domain is equirectangular panoramic images and the target domain is pinhole images. The proposed method is based on InstaFormer (CVPR 2022) with several modifications such as using deformable convolution in the encoder, spherical positional embedding, distortion-free discrimination, and sphere-based rotation augmentation.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

S1. This may be the first paper on image-to-image translation where the source and target domains have significantly different geometric structures, e.g., pinhole images and equirectangular panoramic images.

S2. The proposed method seems to work well and outperforms several baseline methods.

### Weaknesses

#### Some Related Works


#### comment

W1. The proposed method is a direct extension of InstaFormer with several modifications. Although the authors claim that the proposed method outperforms InstaFormer, the core architecture and methodology heavily rely on the existing framework. The modifications, while potentially beneficial, do not represent a fundamental shift in approach or a novel conceptual contribution. The performance gains, while appreciated, seem incremental rather than transformative.

W2. The proposed method is limited to translate images between panoramic and pinhole domains. This limits the general applicability of the method. The paper does not explore or provide any mechanism for translating between other types of image domains, which significantly restricts the scope of the work. The lack of flexibility in handling diverse image types is a notable limitation.

W3. The proposed method is limited to translate images between outdoor street scenes. The training data and experiments are focused solely on outdoor street scenes, which raises concerns about the method's ability to generalize to other types of environments or subjects. The lack of evaluation on diverse datasets limits the practical utility of the method.

### Suggestions

The authors should more clearly articulate the novelty of their approach beyond incremental improvements to InstaFormer. While the modifications are interesting, the core architecture remains largely unchanged. A more detailed analysis of the specific contributions of each modification, perhaps through ablation studies, would be beneficial. Furthermore, the authors should explore how their method could be extended to handle more general image-to-image translation tasks, rather than being limited to panoramic and pinhole images. This could involve exploring different network architectures or loss functions that are less specific to the characteristics of the chosen domains. The current approach seems very tailored to the specific input types, which limits its broader applicability.

To address the limitations in domain specificity, the authors could investigate techniques for domain adaptation or meta-learning that would allow the model to generalize to new image domains not seen during training. This could involve incorporating domain-specific parameters or using a more flexible feature representation that is less sensitive to the specific characteristics of the input images. Additionally, the authors should consider evaluating their method on a more diverse set of datasets, including indoor scenes, different weather conditions, and different types of objects. This would provide a more comprehensive assessment of the method's generalization capabilities and identify areas for improvement. The current evaluation is too narrow to fully validate the robustness of the method.

Finally, the authors should consider the practical implications of their method. While the current focus on street scenes is understandable, the authors should discuss how their method could be applied to other real-world scenarios. This could involve exploring different applications of panoramic image translation, such as in virtual reality or robotics. The authors should also discuss the computational cost of their method and how it could be optimized for real-time applications. A more thorough discussion of the practical aspects of the method would enhance the impact of the work.

### Questions

Q1. I would like to ask the authors to compare the proposed method with InstaFormer more directly. For example, what would happen if we apply sphere-based rotation augmentation and its ensemble technique to InstaFormer? Or what would happen if we use spherical positional embedding (SPE) and/or deformable convolution to InstaFormer? 

Q2. The authors may consider applying the proposed method to more general image-to-image translation tasks, e.g., let the source domain be a collection of images from AP-22K and the target domain be panoramic images. This may address my concern in W2 and W3.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
