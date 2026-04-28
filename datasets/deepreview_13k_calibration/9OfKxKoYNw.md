# DiffusionGuard: A Robust Defense Against Malicious Diffusion-based Image Editing

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent advances in diffusion models have introduced a new era of text-guided image manipulation, enabling users to create realistic edited images with simple textual prompts.
However, there is significant concern about the potential misuse of these methods, especially in creating misleading or harmful content.
Although recent defense strategies, which introduce imperceptible adversarial noise to induce model failure, have shown promise, they remain ineffective against more sophisticated manipulations, such as editing with a mask.
In this work, we propose \metabbr, a robust and effective defense method against 
unauthorized edits by diffusion-based image editing models, even in challenging setups.
Through a detailed analysis of these models, we introduce a novel objective that generates adversarial noise targeting the early stage of the diffusion process.
This approach significantly improves the efficiency and effectiveness of adversarial noises.
We also introduce a mask-augmentation technique to enhance robustness against various masks during test time.
Finally, we introduce a comprehensive benchmark designed to evaluate the effectiveness and robustness of methods in protecting against privacy threats in realistic scenarios.
Through extensive experiments, we show that our method achieves stronger protection and improved mask robustness with lower computational costs compared to the strongest baseline. Additionally, our method exhibits superior transferability and better resilience to noise removal techniques compared to all baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes DiffusionGuard, an image-cloaking algorithm to defend against malicious diffusion-based text-guided inpainting. Compared to previous works, it has two main proposals. First, instead of optimizing any denoising step using either image-space loss or reconstruction loss, DiffusionGuard only optimizes at the early stage (t = T) and aims to increase the norm of the noise. Second, it employs mask augmentation to improve the robustness of the proposed algorithm for different mask variations at test time. Experiments verified that DiffusionGuard outperforms the previous baselines on this task.

### Strengths
- The proposal of mask augmentation is sensible.
- DiffusionGuard outperforms the baselines in all metrics. Qualitative figures show that it often causes the inpainting models to generate plain and blurry inpainted output backgrounds.

### Weaknesses
 - The title is misleading. The work only focuses on diffusion-based text-guided inpainting, e.g., Stable Diffusion Inpainting. It does not consider other diffusion-based image editing methods such as Instruct-Pix2Pix, MasaCtrl... The authors should revise the title to better specify the scope of the work.
- The work only tests with Stable Diffusion Inpainting variants. Recent inpainting models, e.g., MagicBrush [1], should be mentioned and tested. It is unclear if the proposed method would generalize to other inpainting architectures or training procedures.
- L191-200: the mentioned "unique behavior" of inpainting models sounds misleading. In the early denoising stage, the fine details only appear on the unchanged region, which is basically copied from the input. The inpainting regions, i.e., the background, still do not have fine details and behave as in normal diffusion models. The claim of a unique behavior is not well-supported by the evidence provided.
- L200: The reason for targeting the early steps is not convincing. From the presented results, the proposed method affects only the inpainting regions outside of the face, which have similar behavior as in normal diffusion models. In the ablation studies, the author should add an extra experiment to test the case when Eq (4) is applied in all time steps instead of only in the early one. The current justification lacks a strong empirical basis.
- In mask augmentation, the mask is shrunk to be smaller. What happens if the mask used at test time is bigger? The paper does not explore the robustness of the method to larger masks, which is a practical concern.
- The PSNR metric used in Table 1 and Fig. 5 is not reliable. Given the same image and mask, we can have different editing results that match the input prompt. Hence, a small PSNR does not necessarily imply a successful defense; good editing can still produce a low PSNR score. The paper should include metrics that better capture the semantic similarity between the edited and original images.
- The test set is small, with only 42 images. It is better to test on a much larger set of images. The limited size of the test set raises concerns about the generalizability of the results.
- The authors ran experiments with 5 masks per testing image. From Fig.4, the masks are pretty similar; hence, the effect of changing the mask is not significant. I would trade the number of masks and prompts to have more testing images. The current experimental design does not sufficiently explore the impact of mask variations.
- The authors should provide a qualitative figure showcasing the cloaked images to see whether the added noise is obvious or not. Quantitative numbers (PSNR, SSIM) for it are also recommended. The lack of visualization of the cloaked images makes it difficult to assess the perceptual impact of the defense.
- Fig.4: The first 3 examples are very good; the inpainted backgrounds are plain and blurry. However, the last example does not show that behavior. The authors should explain why. Fig.5a confirms that DiffusionGuard is not always that good and still loses to Photoguard 22-25% of the time.

### Questions
See weaknesses.

### Soundness
2

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
The paper proposes a effective and robust method against malicious diffusion-based image editing. The method is interesting and insightful. With the proposed benchmark, the paper shows the superior results compared to baseline methods.

### Strengths
1. The observations, that the inpainting models produce fine details of masked region at early steps, are interesting and insightful. 

2. Using augmented masks is a reasonable and effective method to improve robustness.

3. The paper proposes a benchmark to evaluate different methods. Extensive results show the effectiveness and robustness of the method.

### Weaknesses
There are two main concerns.

1. Did the authors try some specifically designed purification methods for such perturbations in diffusion models? Such as the method in [1].

2. Only focusing on mask-based image editing may be a little limited. Currently many editing methods do not require such masks, such as InstructPix2Pix[2]. Can the proposed method be used in these methods? Will the proposed method still be more effective and robust?

### Questions
1. Will different editing prompts have effects on the results? Are the perturbations generated with a single prompt or several different text prompts?

For other questions, please see the Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work reveals that inpainting models generate fine details in the very early stages of the denoising process, leading to the development of a defense method against unauthorized image inpainting. A mask augmentation technique is proposed to enhance robustness. Additionally, a benchmark is introduced to evaluate the effectiveness of protection against unauthorized image inpainting.

### Strengths
1. An insight is provided that inpainting models generate fine details during the very early stages of the denoising process.
2. A new objective specifically designed to prevent image inpainting is introduced.
3. A benchmark is introduced.

### Weaknesses
1. The mask augmentation is achieved by shrinking the contours inward. If malicious users provide masks larger than those used during training, will this affect performance?

2. The diffusion model's sampling can begin from different timesteps, and various sampling schedulers may start at different timesteps. For example, when sampling with 50 steps of DDIM, T is typically around 981, whereas for 25 steps of DPM-Solver, T might be around 961. If the user uses a different sampler from the one used during training, or the same sampler but starts from a different timestep T, will the proposed algorithm still work in this case?

3. The problem setting may be somewhat narrow. While the title suggests it is "against image editing," the method is only effective for a specific type of editing—image inpainting. It remains unclear whether the method can prevent other forms of editing that don't involve masks, such as instruction-guided editing [1][2].

4. Several recent references [3,4,5] on harmful concept removal are missing.

### Questions
Please refer to the weaknesses.

If the authors address my concerns during the rebuttal, I would be open to adjusting my score.

### Soundness
4

### Presentation
4

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
The author proposed an attack method that targeting the LDM-based inpainting task. The method came with a new loss fucntion, and a new data agumentation for inpainting mask. The author also proposed a new benchmark for evaluate the anti-inpainting methods. The experiments showed the good performance. Generally it's a complete work.

### Strengths
1. The author captured the key problem that the global adversarial perturbation will loss its adversarial semantic in inpainting due to the mask
2. The proposed method only need to run one step of U-Net in each attack step
3. The experiment is quite comprehensive

### Weaknesses
 1. The motivation for the loss is not clear. It's unclear why maximizing the L2 norm of the predicted noise in the early diffusion step is effective. While the authors propose this loss for a PGD-like attack, there's no theoretical justification or connection to the underlying diffusion process that explains why this specific norm is chosen over others like L1 or total variation. The lack of a clear rationale makes it difficult to understand the method's effectiveness beyond empirical observation.
2. There is no ablation study for the hyperparameters. While the authors ablate the number of attack steps, they do not explore the impact of the early step `t` on the attack performance. The choice of `t` could significantly impact the attack's effectiveness, as different timesteps in the diffusion process represent varying levels of noise. Furthermore, the learning rate choice is not explored, and it's possible that a larger learning rate, as suggested by some previous works, might lead to better performance, which is not investigated. The lack of ablation for these crucial parameters limits the understanding of the method's sensitivity and optimal configuration.
3. regarding the line 175 to 183, the authors mention that they only apply perturbations in sensitive areas most commonly used by malicious users. This is reasonable in most cases, but if a malicious user only wants to edit the eyes in a face photo, and wants to change the shape of the pupil or the position where the line of sight is focused, will inpainting be successful in this case? I would be inclined to think that editing or inpainting would still succeed in this case. Therefore, I would like to ask the author to make a demo. For example, in a face image, the facial features are masked separately for attack, and then a perturbation composed of several sub-perturbations will be obtained. I want to see how effective a certain sub-perturbation is in this case. Whether the inpainting of the sub-entity will be successful and whether the editing of the entire entity will be successful.
    I expect the author can take series of experiments and show me the results, and it would be better if it could be analyzed quantitatively.
4. Some figures are too tiny to read such as Figure 7a, author may prefer to make the 7a wider to have a better visualization.

### Questions
1. In line 242, the author wrote "by minimizing the following loss ...". Should it be minimizing or maximizing? I was a little bit confused. I hope the author could clearify this.
2. The author proposed a new objective or loss function for the PGD-like attack. Could the author tell me why you choose to maximize the L2 norm of the predicted noise in the earlier step? Why not L1 or total variation or focal norm? I didn't see any explaination of why max(L2) works.
3. The author didn't show that the influence of different early step `t`. For example, from 1 to 10, there is no ablation about it. I'd like to see what's the influence of different `t`, and why.
4. Although the author has done the ablation for attack steps (comp. budget), the author didn't do the ablation for learning rate choice. Some previous papers mentioned the larger learning rate choice may cause better performance when attacking the generation task in some cases, which is counter-intuitive. I hope the author can do the ablation for this as well, to find the best hyperparameters settings.
5. regarding the line 175 to 183, the authors mention that they only apply perturbations in sensitive areas most commonly used by malicious users. This is reasonable in most cases, but if a malicious user only wants to edit the eyes in a face photo, and wants to change the shape of the pupil or the position where the line of sight is focused, will inpainting be successful in this case? I would be inclined to think that editing or inpainting would still succeed in this case.
    Therefore, I would like to ask the author to make a demo. For example, in a face image, the facial features are masked separately for attack, and then a perturbation composed of several sub-perturbations will be obtained. I want to see how effective a certain sub-perturbation is in this case. Whether the inpainting of the sub-entity will be successful and whether the editing of the entire entity will be successful.
    I expect the author can take series of experiments and show me the results, and it would be better if it could be analyzed quantitatively.
6. Some figures are too tiny to read such as Figure 7a, author may prefer to make the 7a wider to have a better visualization.

### Soundness
3

### Presentation
3

### Contribution
3
