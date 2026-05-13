# Optimal transport based adversarial patch to leverage large scale attack transferability

- Decision: Accept
- Scores: 5, 6, 6, 6, 8

## Abstract
Adversarial patch attacks, where a small patch is placed in the scene to fool neural networks, have been studied for numerous applications. Focusing on image classification, we consider the setting of a black-box transfer attack where an attacker does not know the target model. Instead of forcing corrupted image representations to cross the nearest decision boundaries or converge to a particular point, we propose a distribution-oriented approach. We rely on optimal transport to push the feature distribution of attacked images towards an already modeled distribution. We show that this new distribution-oriented approach leads to better transferable patches. Through digital experiments conducted on ImageNet-1K, we provide evidence that our new patches are the only ones that can simultaneously influence multiple Transformer models and Convolutional Neural Networks. Physical world experiments demonstrate that our patch can affect systems in deployment without explicit knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a framework based on optimal transport for crafting patch attacks that are highly transferable to unknown networks. This framework is based on the idea of attacking feature distributions, which is claimed to be less model-dependent than relying on decision boundaries and more robust to optimization artifacts than the feature point method.

### Strengths
I believe the main strength of this article is that it provides an implementation based on optimal transport for distribution matching-based transfer methods.

### Weaknesses
I believe the main drawback of this article is that it does not discuss other methods based on distribution matching.
The article's main claim is somewhat ambiguous; is it advocating that distribution-matching methods are superior, or that methods based on optimal transport are superior? A comparison with other distribution-matching methods would make the paper more compelling.
Another issue is that the article's statements are not sufficiently rigorous. The statements seem to suggest that the method presented can relax dependency on specific models. However, in reality, the method still relies on a particular model, even though it exhibits better transfer performance in experiments.

### Questions
1. Compare with other distribution-matching methods, such as algorithms other than OT (Optimal Transport).
2. Revise the description concerning model dependency.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a distribution based approach for adversarial patch attacks. Instead of optimizing the patch to cross decision boundaries or converge to a specific point, the proposed method uses optimal transport to push the feature distribution of attacked images towards a known distribution. The paper demonstrates that this distribution-oriented approach leads to better transferable patches that can influence multiple models and can be effective in physical world experiments. The paper provides comprehensive digital, hybrid, and physical experiments to validate the effectiveness and transferability of the proposed method.

### Strengths
The paper introduces a novel approach for designing adversarial patch attacks based on optimal transport and distribution, which is a unique and innovative idea.

The author conducted comprehensive experiments, including in virtual, hybrid, and physical environments. The results demonstrate that the method outperforms the baseline in terms of transferability.

The paper is well-structured and provides a thorough review of APA, giving readers a clear understanding of the background and related work.

### Weaknesses
Limited technical contribution: While I acknowledge that optimizing patches based on optimal transport theory has some novelty, the technical contribution of this paper seems rather minimal. I believe that the method's use of Wasserstein and its variants as a loss metric is a straightforward application of existing techniques. Additionally, the usage of EOT and TV Loss is common. Thus, I'm concerned that the technical contribution of this paper might be too weak for ICLR.

The experimental results lack discussions and explanations: For instance, why is it that in the experiments, the Sliced-Wasserstein distance (SW) always underperforms compared to the Wasserstein ones (W)? What causes this? I'm concerned about whether the settings for the two proposed methods are fair. Moreover, I believe there needs to be a more comprehensive ablation study and explanation regarding the choice of target layers. The authors only investigated the impact of the last three feature layers. Why did adding J-2 significantly affect performance?

Physical experiments are somewhat weak: I believe this paper fails to demonstrate the superiority of its method in physical experiments, especially since the author claims that the method provides better transferability but only compares it to a weaker baseline (L2). Additionally, could you investigate the robustness of your method when facing physical transformations? For instance, under variations in camera angles and distances.

### Questions
see the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the setting of a black-box transfer attack on image classification where an attacker does not know the target model. Instead of forcing corrupted image representations to cross the nearest decision boundaries or converge to a particular point, this paper proposes a distribution-oriented approach and relies on optimal transport to push the feature distribution of attacked images towards an already modeled distribution. This work shows that the proposed new distribution-oriented approach can lead to better transferable patches.

### Strengths
1. This work introduces a new framework based on optimal transport for creating patch attacks that are highly transferable to unknown networks. This framework is based on the idea of attacking feature distributions, which is less model-dependent than relying on decision boundaries and more robust to optimization artifacts than the feature point method.
2. This work shows that the proposed attack works for the most extensive spectrum of deep networks considered in the patch attack literature, such as various versions of Convolutional Neural Networks, Transformers, and adversarially trained models. The proposed method also shows transferability superiority through extensive experiments.

### Weaknesses
1. For qualitative experiments, this paper gives some results by selecting three objects present in ImageNet-1K (banana, cup, keyboard) and recording videos of them when one patch is placed or not next to the object. Yet, the performance of model in the physical world may be affected by the different angles or intensities of light. Thus, it would be more meaningful if this paper could provide the performances of the proposed approach with the change of angles or lights for the qualitative evaluation. Specifically, the paper lacks a systematic evaluation of how the patch's effectiveness degrades under varying real-world conditions such as different camera angles (e.g., 15, 30, 45 degrees off-axis), distances (e.g., 0.5m, 1m, 2m), and lighting conditions (e.g., indoor, outdoor, low-light). This is crucial because the transferability of adversarial patches in real-world scenarios is highly dependent on these factors.
2. For digital experiments, the authors select from the previously defined families the following models and measure the attacking transferability when the resulting patch is used to fool the remaining models. The results show that the proposed approach can generate the stronger patch attack than its counterparts. Yet, the visual perception to human vision should also be considered. It would be more convincing if the image with the generated adversarial patch with the proposed method and its counterparts can be evaluated with the PSNR or SSIM as the evaluation metrics for the degree of recognition for human vision. While the paper focuses on fooling deep networks, the perceptual impact on humans is also relevant. Metrics such as PSNR and SSIM, while not directly measuring adversarial effectiveness, could provide insight into the magnitude of the perturbation introduced by the patch and whether it is likely to be noticeable to a human observer. This is important for understanding the practical implications of the attack.
3. According to the table of computation time in the Appendix of this work, the proposed approach with sliced version SW and the normal W can achieve comparable efficiency with the previous methods. Note that the computation of optimal transport may need more time than those methods without OT, the authors may explain why the approach with OT to generate the adversarial patch can achieve the efficiency without the drop of performance. The paper does not provide a detailed analysis of the computational complexity of the optimal transport (OT) calculation, especially in relation to the number of samples used for the source and target distributions. It is important to understand how the computational cost scales with the size of these distributions and why the proposed method, which involves OT, can achieve comparable efficiency to methods without OT. A more thorough explanation of the implementation details and optimizations used to achieve this efficiency is needed.

### Questions
This work designs a new patch attack with optimal transport to narrow the distribution gap in the generation of adversarial patch and achieve the superior performance with empirical evidence. Yet, it would be better for this work to provide more details and explanations.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper leverages the p-Wasserstein distance and the sliced-Wasserstein distance between the corrupted image distribution and the target distribution to generate transferable adversarial patches for attacking ViTs and CNNs. In this way, the proposed method pushes the corrupted feature distribution towards a target feature distribution. The authors attack a diverse set of victim models, including CNNs, ViTs, and adversarially trained models.

### Strengths
This paper is well-written.   
The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses
The authors utilize the Wasserstein distance between the corrupted and the target distributions to optimize adversarial patches. This method is too simple, and there is no theoretical contribution in this paper. Besides, this paper should discuss why are distribution-based methods better than decision boundaries-based methods, feature point-based methods, and generation-based methods (e.g.TTP). Why is the Wasserstein distance suitable in optimizing adversarial patches compared to KL? Additionally, the authors convert the generative methods (TTP) to iterative ones. Thus, the iterative targeted attacks should be also compared [1][2].    
In summary, I think the contribution of this paper is under the acceptance threshold.

### Questions
How to obtain the target distribution $\mathcal{v}_y^{(l)}$.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is interested in generating an adversarial patch, i.e., a small patch placed in a scene that changes the prediction of a neural network. The paper introduces an approach based on optimal transport to generate a patch, such that the estimated feature distribution of corrupted source images becomes close to the distribution of features from the target class, using either the Wasserstein and Sliced-Wasserstein distance. The black-box transferability of the attack is compared to state-of-the-art attacks for the Image Classification task on ImageNet-1K, on a broad set of networks. Qualitative results with a printed patch are also presented to demonstrate the real-world applicability of the attack.

### Strengths
- **Broad Model Evaluation:** The paper offers a comprehensive evaluation of attacked models, ranging from classical Convolutional Neural Networks (CNNs) to the more contemporary Vision Transformers. This large coverage is important, as it shows the adaptability and effectiveness of the proposed attack across diverse neural network architectures. Furthermore, as mentioned in the paper, recent networks and training recipes are both naturally more robust than older CNNs, it is then fundamental to evaluate against them as well. From the results, we can see that attacks optimized for a specific category of models does not transfer as efficiently to all other categories.
- **High Transferability Results:** The proposed approach demonstrates strong transferability results, outperforming in general both state-of-the-art patch and non-patch attacks. Notably, the approach accomplishes this while maintaining a similar level of computational efficiency as other existing methods.
- **Clarity and Reproducibility:** The paper is well written and easy to follow, with a clear description of the proposed approach and of the experiments. Additionally, the code is available as supplementary material which helps reproducibility.

### Weaknesses
 - **Data Dependency:** One limitation currently not discussed in the paper is the target data requirements. The proposed attack method relies on a substantial number of target examples to generate the patch to accurately approximate the target class distribution. This means that the attack has access to a lot more information compared to attacks that matches a single feature point. This data dependency could be an important limitation in practice. Specifically, while the paper mentions 40,000 images are used to train the patches, it is unclear how many of these are source images and how many are target images used to estimate the target distribution. This is a crucial detail, as the number of target images directly impacts the quality of the estimated target distribution, and thus the effectiveness of the attack. The practical implications of this are significant: an attacker would need a large number of target class images to craft an effective adversarial patch, which may not always be feasible in real-world scenarios where the attacker does not have access to the training data of the target model. This contrasts with feature-point based attacks that only require a single image from the target class.

### Questions
I would like to see a study on the strength of the proposed attack, depending on the number of target images used to approximate the target distribution. How many target images are used to generate the patches in the experiments ? The paper mentions 40000 images to train the patches, but I assume that they are also split into source and target images.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
