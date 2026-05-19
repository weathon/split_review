### Summary

This paper proposes a perturbation-dropping scheme for generating adversarial examples with higher transferability. The authors propose to leverage the class activation map to locate the dropped regions. Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The idea is intuitive and easy to understand.
- The experiments are extensive.

### Weaknesses

#### Some Related Works

[1] Decoupling direction and norm for efficient gradient-based l2 adversarial attacks.
[2] Towards deep learning models resistant to adversarial attacks.
[3] Theoretically principled trade-off between robustness and accuracy.
[4] Towards understanding and improving adversarial transferability.

#### comment

 - The proposed method seems to lack novelty since the concept of dropping perturbations has been investigated in the literature [1]. The authors should clarify the novelty and the difference between this paper and the prior work.
- The motivation is not convincing. In particular, the authors propose to use CAM to locate the dropped regions. However, CAM is a coarse approximation of the gradient. It is questionable that the CAM can accurately locate the dropped regions. 
- The proposed method requires a correct prediction from the surrogate model to generate effective perturbations. However, this condition is not always true in practice since the surrogate model may misclassify the input image. Therefore, the proposed method may not be able to generate perturbations for all the input images.
- The proposed method is limited to $\ell_{\infty}$ attacks. However, there are many other attack types such as $\ell_2$ attacks [1]. It is unclear whether the proposed method can be generalized to other attack types.
- The proposed method may not be efficient since the authors propose to ensemble multiple perturbed images to update the adversarial image. The computational overhead may be very high.
- The transferability of adversarial examples has been extensively studied in the literature [2-4]. The authors should discuss the relationship between the proposed method and the existing literature.

### Suggestions

The paper introduces an interesting idea of using perturbation dropout to enhance the transferability of adversarial examples. However, the current presentation lacks a thorough analysis of the method's limitations and its relationship to existing techniques. Specifically, the authors should provide a more detailed explanation of how the proposed method differs from previous work that also explores perturbation manipulation. The current discussion is too high-level and does not delve into the specific technical differences. For example, the authors should clarify how their method addresses the limitations of simply masking perturbations, and how the dropout mechanism leads to more independent perturbation components. A more rigorous analysis of the gradient space and how the dropout affects the optimization landscape would be beneficial. Furthermore, the authors should provide a more detailed justification for using CAM to locate dropped regions, given its known limitations as a coarse approximation of the gradient. It would be helpful to see a comparison with other methods for identifying important regions, such as saliency maps or gradient-based localization techniques. The authors should also discuss the potential impact of CAM's inaccuracies on the effectiveness of the proposed method. 

To address the limitations regarding the reliance on correct predictions from the surrogate model, the authors should explore strategies to handle cases where the surrogate model misclassifies the input image. One possible approach could be to use an ensemble of surrogate models or to incorporate a mechanism to detect and correct misclassifications. The authors should also investigate the sensitivity of their method to the choice of surrogate model and the impact of using different models on the transferability of the generated adversarial examples. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method. While the authors mention that the additional computation is negligible, they should provide a more rigorous analysis of the time complexity of their algorithm and compare it to existing methods. This analysis should include the time required for CAM generation and the ensembling of multiple perturbed images. It would also be helpful to see a comparison of the computational cost for different image sizes and perturbation parameters. The authors should also explore techniques to optimize the computational efficiency of their method, such as using more efficient CAM generation algorithms or reducing the number of ensembled images.

Finally, the authors should provide a more comprehensive discussion of the relationship between their method and existing literature on adversarial transferability. While the authors mention that their method is orthogonal to other techniques, they should provide a more detailed analysis of how their method interacts with other transferability-enhancing techniques. For example, the authors should investigate whether their method can be combined with other input transformations or attack algorithms to achieve even higher transferability. The authors should also discuss the limitations of their method and the potential for future research. This discussion should include the potential impact of different network architectures and datasets on the effectiveness of the proposed method. The authors should also explore the possibility of extending their method to other types of attacks, such as $\ell_2$ attacks, and discuss the challenges and potential benefits of such extensions.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
