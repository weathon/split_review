# Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Diffusion distillation methods aim to compress the diffusion models into efficient one-step generators while trying to preserve quality. Among them, Distribution Matching Distillation (DMD) offers a suitable framework for training general-form one-step generators, applicable beyond unconditional generation. In this work, we introduce its modification, called Regularized Distribution Matching Distillation, applicable to unpaired image-to-image problems. We demonstrate its empirical performance in application to several translation tasks, including 2D examples and I2I between different image datasets, where it performs on par or better than multi-step diffusion baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Authors proposed a modified extension of DMD that includes transport cost for unpaired I2I task. They established connection to optimal transport and showed that solution of the soft-constrained RDMD converges to that of the hard-constrained Monge problem. Experimental results on several datasets also prove the effect of the model.

### Strengths
Authors prove that solution of the soft-constrained RDMD converges to that of the hard-constrained Monge problem. The proof seems complicated and unfortunately I do not have the mathematical background to fully verify all steps.

### Weaknesses
Authors fail to mention related works such as OTCS (Optimal Transport-Guided Conditional Score-Based Diffusion Model). Experiments are also simple and did not outperform baseline in some metrics. Qualitative evaluations are very hard to judge given the 64x64 generated image resolution. Overall it is hard to verify the effectiveness of the proposed method based on the limited experiment results, especially when very related work is missing in the comparison. The lack of comparison to methods that explicitly leverage optimal transport for conditional generation is a significant oversight. Furthermore, while the authors establish a connection to optimal transport, the practical benefits of this connection are not fully demonstrated, especially given the limited scale of the experiments. The reported metrics do not consistently show a clear advantage over existing methods, raising concerns about the practical impact of the proposed approach. The choice of 64x64 resolution for the primary experiments is also questionable, as it limits the visual complexity and makes it difficult to assess the quality of generated images. This is particularly problematic when evaluating image-to-image translation tasks where fine details are crucial.

### Questions
I wonder if there is potential limitations of the method that led to the use of 64x64 image resolution, which is much lower than the standard 256x256 for most of those dataset. Could there be efficiency or computation challenge for scaling up?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study proposes distilling a pre-trained diffusion model into a one-step generative model to efficiently address unpaired Image-to-Image (I2I) translation. The method uses distribution matching distillation, effective in image generation, and regularizes it for unpaired I2I tasks. The proposed approach achieves good results and is significantly efficient in the sampling phase, requiring only one generation step.

### Strengths
- Applying distribution matching distillation (DMD) to efficiently tackle unpaired I2I translation is an interesting approach.
- Empirical results indicate that the proposed method is effective.

### Weaknesses
 - The contribution feels incremental, as it primarily extends existing distribution matching distillation from text-to-image generation (where the prior distribution is Gaussian) to unpaired I2I by simply substituting the Gaussian prior with a source image distribution and adding the transport constraint. Please provide deeper justifications for this approach if any exist.

 - While the use of a transport constraint for regularization is sound, I am concerned about the choice of the squared difference norm for adapting DMD to unpaired I2I tasks. This transport cost may be too simple and fail to capture semantic details between the generated images from the one-step generator and the source images. A more robust cost function, such as the Energy function in EGSDE, could enhance translation capacity.

 - This issue may lead to output images with low L2 loss (high faithfulness) but less realism (potentially high FID), as observed in your experiments. In the experimental section, I suggest that the authors use FID computed based solely on the target distribution, rather than both the source and target as in the current design. This adjustment would better reflect the translation performance of the proposed method, given that other metrics do not adequately capture translation quality.

 - Additionally, the paper lacks references to relevant work on accelerating diffusion models without additional training, such as [1, 2, 3]. There are also unpaired I2I translation methods, like [4, 5, 6], that could utilize these acceleration techniques to generate samples more efficiently, offering alternative baselines to your method. The paper could be more comprehensive if the study regarding these baselines is included.

 - Although the sampling efficiency is evident with the one-step approach, the training phase requires an additional fake model. Could the authors provide an analysis of the training resources needed for the proposed framework?
 
- Is it challenging for both models to converge with the proposed loss function? Could the authors provide training curves for the loss functions of both the one-step generator and the fake diffusion model?

### Questions
Please refer to the Weaknesses section for my concerns and questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper perform unpaired image-to-image translation through adding quadratic regularization term on the existing distribution matching distillation method.

### Strengths
- Experiments were conducted on various data and resolutions in both pixel-space and latent diffusion.

### Weaknesses
I find the contribution of this paper to be somewhat limited.

- The method mainly introduces a quadratic regularization term, $\| x - G_\theta (x) \|^2 $, into existing distillation approaches. This is a very simple method. Moreover, in Equations 9-11, the paper replaces the Gaussian input $p_{noise}$ with $p_{source}$, and re-train $G_\theta(x)$ with $x\sim p_{source}$. Since they no longer put noise into $G_\theta$, this approach seems more like re-training $G_\theta$ by leveraging a well-pretrained diffusion model than a distillation method. So, this method should be seen as a fully-retrained model, not a distillation method. However, the paper only compares with zero-shot diffusion-based methods or classifier-learned-based methods. I suggest authors to compare with other methods that fully train a new I2I model with the help of diffusion models. Or I suggest the authors to compare with the GAN-based methods [1] and some of the optimal-transport-based methods [2,3,4,5].

- Overall, it currently lacks a theoretical foundation and does not appear to bring substantial methodological improvements. Moreover, the comparisons are extremely weak. Even with this weak comparison, the performance is not convincing. I believe there needs big improvements in concept, literature, experimental design, and comparison groups to strengthen the paper.

### Questions
- In the implementation, do this method use LPIPS as a loss term in training process as Distribution Matching Distillation (DMD) does?

- CycleDiff, DDIB needs to be defined and cited in somewhere in the paper.


[1] T. Park et al., Contrastive Learning for Unpaired Image-to-Image Translation, ECCV, 2020.

[2] J. Fan et al, Scalable computation of monge maps with general costs, NeurIPS, 2021.

[3] J. Choi et al, Generative Modeling through the Semi-dual Formulation of Unbalanced Optimal Transport, NeurIPS, 2023.

[4] Y. Shi et al., Diffusion Schrodinger Bridge Matching, NeurIPS, 2023.

[5] N. Gushchin et al., Adversarial Schrodinger Bridge Matching, NeurIPS, 2024.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
- This paper proposes a diffusion model distillation method for a one-step generator, called Regularized Distribution Matching Distillation (RDMD). RDMD introduces an additional cost regularizer into the previous Distribution Matching Distillation approach. The proposed method is evaluated on the image-to-image translation task, where this cost-minimization regularizer is desirable.

### Strengths
- This paper provides the relationship between RDMD and the optimal transport map in Thm 1.
- This paper is easy to follow.

### Weaknesses
 - The technical novelty of the proposed method is incremental.
- The proposed method is not compared with the optimal transport models.

- The assumptions required to guarantee the bijectivity of the Monge map are not clearly stated, making it difficult to assess the theoretical validity of the approach.
- The lack of quantitative results for the toy experiments in Figure 2 makes it hard to evaluate the effectiveness of the proposed regularizer. Specifically, the transport cost and Wasserstein distance between the generated and target distributions should be provided.
- In Table 1, SDEdit and DDIB achieve competitive FID results and inferior transport costs compared to RDMD. The paper does not provide any visual examples to justify the trade-off between FID and transport cost. This makes it difficult to understand the practical benefits of the proposed method.
- It is not clear if all models in Tables 1 and 2 share the same backbone networks, except for the pixel-space EGSDE. This lack of clarity makes it difficult to compare the results fairly.
- The paper lacks a comparison with optimal transport models trained from scratch on the image-to-image translation task. Specifically, the paper should compare against methods like NOT and OTM, which have been shown to achieve competitive FID results with large backbone networks.

### Questions
- Could you provide details for the assumptions to guarantee the bijectivity of the Monge optimal transport problem in Line 179?
- Could you provide the quantitative results on the toy experiments in Figure 2? Evaluating the transport cost and Wasserstein distance between the generated and target distribution would strengthen the experimental results.
- In Table 1, SDEdit and DDIB achieve competitive FID results and inferior transport costs compared to RDMD. Since the transport cost and FID metric should be considered together, could you provide the translation examples for these models?
- Do all the models in Tables 1 and 2 share the same backbone networks, except for the pixel-space EGSDE?
- Could you provide a comparison with optimal transport models trained from scratch on the image-to-image translation task? [1] reported that NOT and OTM can achieve competitive FID results with the large backbone network, DDPM++. Could you clarify the advantages of RDMD over these approaches?

[1] Choi, Jaemoo, Yongxin Chen, and Jaewoong Choi. "Improving Neural Optimal Transport via Displacement Interpolation." arXiv preprint arXiv:2410.03783 (2024).

### Soundness
2

### Presentation
2

### Contribution
1
