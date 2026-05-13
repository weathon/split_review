# Universal Guidance for Diffusion Models

- Decision: Accept
- Scores: 6, 6, 3, 6

## Abstract
Typical diffusion models are trained to accept a particular form of conditioning, most commonly text, and cannot be conditioned on other modalities without retraining. 
In this work, we propose a universal guidance algorithm that enables diffusion models to be controlled by arbitrary guidance modalities without the need to retrain any use-specific components.
We show that our algorithm successfully generates quality images with guidance functions including segmentation, face recognition, object detection, and classifier signals.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a universal guidance algorithm to make the diffusion model condition on multiple modalities without retraining the model. The core idea is to use the estimated clean image in the intermediate step to provide the classifier guidance. The experiments demonstrate the effectiveness of the proposed method.

### Strengths
1) The proposed method enables the pretrained diffusion model to condition multiple modality controls without any retraining.

2) The paper is well-written and easy to follow.

3) The experiment demonstrates the effectiveness of the proposed method.

### Weaknesses
1) The method uses the predicted clean image as the input of the conditioning model. Would the inaccurate predicted clean image affect the performance? It's unclear how the error in the predicted clean image propagates through the guidance process, especially in the early denoising steps where the prediction is likely to be noisy. This could lead to unstable or suboptimal guidance.

2) Some previous work [1, 2, 3] on the conditional diffusion model should be discussed. The paper lacks a thorough comparison with existing conditional diffusion methods, particularly those that also aim to control generation through external modalities. The absence of this discussion makes it difficult to assess the novelty and advantages of the proposed approach.

### Questions
The method uses the predicted clean image as the input of the conditioning model. Would the inaccurate predicted clean image affect the performance? The authors need to study this issue.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Sampling images from pretrained diffusion models using conditions is now a very hot topic and plays very important roles in many application scenarios. There are two categories of methods for conditional generation: 1) retraining with new conditions, such as Control-Net; 2) using a guidance function to optimize a latent in the pretrained image space. Considering the cost of re-training, this paper targets a universal guidance strategy for conditional sampling. The experiments demonstrate the results of many different conditions: classifier label, human identity, segmentation maps and object locations etc.

### Strengths
- The motivation is very clear and the writing is very easy-to-follow. 
- Evenly the idea seems simple, it is novel and reasonable. 
- The experiments contain many different condition scenarios and the results are visually good.

### Weaknesses
My major concern is on the experiments:

* It lacks ablation: as claimed in Sec 3.1, "directly replacing fcl and lce with any off-the-shelf guidance and loss functions does not work in practice". I think it is needed to include an experiment to support this claim. In addition, only "object location guidance" in Sec 4.2 provided the ablation of forward and backward guidance, the results for at least more than one tasks are helpful. Specifically, the claim that directly using off-the-shelf guidance fails needs more rigorous backing. It's unclear what specific functions were tried and why they failed. A more detailed analysis of the failure modes would be beneficial. For example, what happens to the generated image when using a standard classifier gradient as guidance? Does it lead to mode collapse, or does it simply not adhere to the condition? Furthermore, the ablation of forward vs. backward guidance should be extended beyond object location to other conditions like segmentation and text, to understand if the effectiveness of forward guidance is consistent across different tasks.

* I appreciate the experiments on conditional stable diffusion in Sec4.1 and unconditional imagenet diffusion in Sec 4.2. However, I am curious why not also conducting segmentation map guidance in 4.2. I think including same task in both 4.1 and 4.2 can be helpful for readers to understand the differences between the two diffusion models. It would be beneficial to see how the proposed method performs on the same task across different diffusion models, allowing for a more direct comparison of the model's behavior and the impact of the underlying diffusion process. The absence of segmentation guidance in 4.2 makes it difficult to ascertain whether the method's efficacy is consistent across different model architectures and training data.

* My primary concern is: all presented visual results are not diverse - dogs are everywhere. I also checked all results in the supplemental, it is similar. How about other cases? The lack of diversity in the generated images is a significant concern. While the method might work well for dogs, it's unclear if it generalizes to other object categories. The supplemental material also seems to lack diversity, raising questions about the robustness of the approach. It would be helpful to see results with a wider range of object categories and scenes to better assess the method's generalization capabilities.

### Questions
See weakness part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission deals with designing a universal guidance for diffusion models that can adapt to various guidance modalities such as segmentation masks, bounding boxes, in a plug-and-play fashion without any retraining from the scratch or any finetuning. To solve the problem, it proposes to add a loss gradient term to the denoising score function. Let c be the guidance that is the output of some function c=f(z0) for the unknown sample z0. Then the loss is defined to be defined between c and f(\hat{z}), where \hat{z} is an estimate for the z0 based on noisy observation zt based on MMSE estimation. This approximation has been commonly used in the diffusion literature e.g., in DDIM, DPS [Chung et al’22 ], PGDM [Song et al’22]. Experiments show that this loss-guidance works to properly guide stable diffusion sampling. 

[Song et al’22] Song, Jiaming, Arash Vahdat, Morteza Mardani, and Jan Kautz. "Pseudoinverse-guided diffusion models for inverse problems." In International Conference on Learning Representations. 2022.

[Chung et al’22 ] Chung, Hyungjin, Jeongsol Kim, Michael T. Mccann, Marc L. Klasky, and Jong Chul Ye. "Diffusion posterior sampling for general noisy inverse problems." arXiv preprint arXiv:2209.14687 (2022).

[Song et al’23] Song, Jiaming, Qinsheng Zhang, Hongxu Yin, Morteza Mardani, Ming-Yu Liu, Jan Kautz, Yongxin Chen, and Arash Vahdat. "Loss-Guided Diffusion Models for Plug-and-Play Controllable Generation." (2023).

### Strengths
Controllable generation from diffusion models without re-training or finetuning is an important problem

### Weaknesses
The idea in this work doesn't seem to be novel. Loss guidance for diffusion models for the same purpose has been studied in previous works that have not been cited; see [Song et al’23]. Also, the idea of using \hat{z} to approximate z0 based on the score has been used several times in the samping diffusion models for example for inverse problems as in PGDM [Song et al’22], and DPS [Chung et al’22 ].

Specifically, the paper fails to adequately differentiate its approach from existing loss-guided diffusion methods. The core concept of applying a loss gradient to the denoising score function, while effective, is not unique. The approximation of z0 using \hat{z} based on MMSE estimation is also a standard technique in diffusion model sampling, particularly in the context of inverse problems. The paper lacks a clear explanation of how the proposed method offers a substantial advancement over these established techniques. The use of a loss between the guidance output on the estimated clean image and the target guidance is a direct application of existing loss-guided diffusion methods, and the paper does not provide sufficient justification for its novelty.

### Questions
The authors need to clarify the contributions of this work compared with previous works, especially the ones in PGDM [Song et al’22], DPS , and [Song et al’23]. I am willing to change my score if the author could clarify the contributions and differences from the work in [Song et al’23].

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel method to control generation process by diffusion models using arbitrary guidance functions without any retraining. The proposed method comprises two types of guidance: forward guidance and backward guidance. In the forward guidance, an estimated clean data is used to compute the guidance function, and its gradient is directly employed to adjust the estimated noise at each timestep. On the other hand, in the backward guidance, the adjustment is obtained by multiple step gradient descent, which leads to more faithful results to the constraint incurred by the guidance. The exprimental results show that the proposed method works well across various types of guidance.

### Strengths
- The proposed method can be applied to a wide variety of conditional generation tasks without retraining the base diffusion model.

- In the experimetns, the proposed method performs well in terms of the quality of the generated images. It is also impressive that the proposed method allows for a variety of conditional generation.

- Overall, the manuscript is well-written and easy to follow.

### Weaknesses
<Major ones>

- The novelty in methodology is marginal.
  - In the forward guidance, the loss function is computed based on the clean data predicted from the noisy data at each timestep, and its gradient with respect to the original noisy data is used for the guidance. This approach is quite similar to that employed in DPS and FreeDoM [R1]. Specifically, the use of a predicted clean image to compute the guidance gradient is a core component of DPS, and the proposed method seems to directly adopt this strategy. The authors should clarify the differences in the gradient calculation and how it avoids simply replicating DPS.
  - In addition, the stepwise refinement is also similar to time-travel strategy in FreeDoM. The authors should provide a more detailed comparison of the refinement process, highlighting the differences in the optimization procedure and the specific update rules used at each step. It is not clear how the proposed method's refinement differs fundamentally from the time-travel approach, which also iteratively refines the generated sample by moving along the diffusion trajectory.
    - [R1] "FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model," ICCV 2023.

- The advantage of the proposed method over existing methods is not clear. The experiments lack comparison with baseline methods, though several related studies are refered in Section 2. Specifically, Diffusion Posterior Sampling (and FreeDoM as well) is closely related to this work and should be compared qualitatively and quantitatively. The absence of a direct comparison makes it difficult to assess the true contribution of the proposed method. It is crucial to demonstrate that the proposed method offers a significant improvement over existing techniques, not just comparable performance.


<Minor ones>

- As any kind of guidance function can be used in the proposed method, it would be interesting to see how its performance varies according to the design of the guidance function. For example, in the case of segmentation map guidance, we may have a lot of publicly-available segmentation models that can be utilized for the guidance. In this case, can we simply choose the best performing model? This point is not clear in the manuscript, because only single model is examined for each conditional generation task.

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
