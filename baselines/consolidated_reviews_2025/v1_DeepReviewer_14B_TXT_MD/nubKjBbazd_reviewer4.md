### Summary

This paper proposes a novel adversarial attack method, namely, the Adversarial Perturbation Dropout (APD), that can achieve significant transferability of adversarial examples. The APD method adopts the dropout mechanism on a set of adversarial images to break the synergy of the perturbations across different attention regions, which can maintain the attack effect for the target model even part of the perturbations are not in its attention regions. To improve the effectiveness of the APD attack method, we incorporate class attention maps to determine the midpoint of dropped regions with different dropped region sizes. Our approach offers a new perspective on improving transferability by reducing the interaction between different regions, which can produce robust perturbations to the target model. Through extensive experimentation, we demonstrate the superior performance of APD compared with the state-of-the-art methods. Our method can also be seamlessly integrated into existing iteration-based attack methods, which can provide great inspiration for improving the adversarial transferability.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple and effective. The experimental results are good.
3. The proposed method can be seamlessly integrated into existing iteration-based attack methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is limited to the image classification task. It is unknown whether it can be applied to other tasks, such as object detection and semantic segmentation.
2. The proposed method requires a correct prediction from the surrogate model to generate effective perturbations. However, this condition is not always true in practice since the surrogate model may misclassify the input image. Therefore, the proposed method may not be able to generate perturbations for all the input images.
3. The proposed method is limited to ℓ∞ attacks. However, there are many other attack types such as ℓ2 attacks. It is unclear whether the proposed method can be generalized to other attack types.
4. The proposed method may not be efficient since the authors propose to ensemble multiple perturbed images to update the adversarial image. The computational overhead may be very high.
5. The transferability of adversarial examples has been extensively studied in the literature. The authors should discuss the relationship between the proposed method and the existing literature.

### Suggestions

The paper introduces an interesting approach to enhance the transferability of adversarial examples by applying a perturbation dropout mechanism guided by class activation maps. However, the current evaluation is limited to image classification tasks, and it is unclear how well this method would generalize to other tasks like object detection or semantic segmentation. These tasks have different output spaces and model architectures, which could significantly impact the effectiveness of the proposed dropout strategy. For instance, in object detection, perturbations might need to be more localized to specific object parts or bounding boxes, and the class activation maps used in image classification may not directly translate to effective dropout regions. Further investigation is needed to explore the applicability of APD in these more complex scenarios, potentially requiring modifications to the dropout mechanism or the guidance from class activation maps. It would be beneficial to see experiments on benchmark datasets for object detection and semantic segmentation to validate the broader applicability of the method.

Furthermore, the reliance on a surrogate model for generating perturbations raises concerns about the practical applicability of the method. The requirement for a correct prediction from the surrogate model is a significant limitation, as real-world surrogate models may not always provide accurate predictions, especially when dealing with adversarial examples or out-of-distribution data. This could lead to situations where the proposed method fails to generate effective perturbations, limiting its robustness. The authors should explore strategies to mitigate this issue, such as using an ensemble of surrogate models or incorporating a mechanism to detect and correct misclassifications. Additionally, the paper should provide a more detailed analysis of the sensitivity of the method to the choice of surrogate model and the impact of using different models on the transferability of the generated adversarial examples. It would be valuable to see experiments with different surrogate models and an analysis of how the performance of APD varies with the accuracy of the surrogate model.

Finally, the paper should address the limitations of the proposed method regarding the attack type and computational efficiency. The current method is limited to ℓ∞ attacks, and it is unclear whether it can be generalized to other attack types, such as ℓ2 attacks. The authors should explore the possibility of extending the method to other attack types and discuss the challenges and potential benefits of such extensions. Moreover, the computational overhead of ensembling multiple perturbed images to update the adversarial image is a concern, especially for high-resolution images or real-time applications. The authors should provide a more detailed analysis of the computational cost of their method and compare it to existing methods. It would also be helpful to see experiments with different numbers of ensembled images and an analysis of the trade-off between computational cost and attack performance. The authors should also discuss the potential for optimizing the computational efficiency of their method, such as by using more efficient ensembling techniques or by reducing the number of ensembled images without sacrificing performance.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
