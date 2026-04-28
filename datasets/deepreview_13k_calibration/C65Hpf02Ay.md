# One-step Image-function Generation via Consistency Training

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Consistency models aim to deliver a U-Net generator to map noise to images directly and enable swift inference with minimal steps, even trained in isolation with consistency training mode. However, the U-Net generator requires heavy feature extraction layers for multi-level resolutions and learning convolution kernels with specific receptive fields, resulting in the challenge that consistency models suffer from heavy training resources and fail to generate images with any user-specific resolutions. In this paper, we first validate that training the original consistency model with a small batch size via consistency training mode is pretty unstable, which motivates us to investigate efficient and flexible consistency models. To this end, we propose to use a novel Transformer-based generator to generate continuous image functions, which can then be differentially rendered as images with arbitrary resolutions. We adopt implicit neural representations (INRs) to form such continuous functions, which help to decouple the resolution of generated images and the total amount of the parameters generated from the neural network. Extensive experiments on one-step image generation demonstrate that our method greatly improves the performance of consistency models with low training resources and also provides an efficient any-resolution image sampling process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors observe that with low training resources and small batch size, the training of UNet-based consistency model is unstable, and proposed a Transformer-based generator that generates network parameters as INR for consistency training. The authors show better training stability and lower FID metric than the original UNet-based consistency model in the low-resource training setting.

### Strengths
**Update after rebuttal:**

```
The authors have addressed my questions and I will keep my rating. The idea of using any-resolution representation for consistency models is interesting, while I agree with other reviewers that more solid comparisons to exsiting methods could be helpful (for efficient training or for any-resolution generation).

```

---

1. Using consistency training for image function generation is an interesting direction to explore. Since INRs are any-resolution decoders, it is natural to compute the consistency objective in the rendered patches.
2. The proposed reconstruction pre-training is simple and effective.
3. The authors show improved FID and other metrics. The training stability is also improved compared to the baseline UNet on common datasets.

### Weaknesses
1. It is not very clear that why modeling as INR can help improve the stability in low-resource training. With the Transformer generator and INR representation, is the input noisy image / target in training at fixed resolution or varied resolutions? More discussions about the intuition for the improvement might be helpful. Can the reconstruction pre-training also be applied for the UNet consistency model?
2. Despite showing many metrics, the FID values for both the baseline and proposed method are very high (though it is due to the training budget). The results will be more convincing and solid when the methods can achieve a generally better quality. It is unclear if the high FID is solely due to training budget or if there are other factors at play, such as the choice of architecture or training procedure. A more thorough investigation into the causes of the high FID values would be beneficial.
3. The claim the advantage of any-resolution generation, it is better to discuss and compare to more recent works that specifically works on any-resolution image generation, for example [1, 2]. The current discussion lacks a detailed comparison with these methods, particularly regarding the specific advantages and disadvantages of the proposed approach in the context of any-resolution image generation.

### Questions
It is shown in the supplementary that the generated INR has better quality than bilinear interpolation when decoding to high resolutions. Is the high resolution higher than the resolution in training? If it is the case of resolution extrapolation, is any artifact observed in high resolutoins?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses two main issues: the training instability of consistency models with small batch sizes and the limitation of generating images at fixed resolutions. To tackle these challenges, the authors propose using a Transformer-based generator along with implicit neural representations. Additionally, to improve training stability, they introduce an auxiliary task before training the consistency model, which leads to faster convergence and enhanced image generation quality. Experimental results show that this approach improves performance in one-step image generation with reduced training requirements and enables efficient, any-resolution image sampling.

### Strengths
A key strength of this paper lies in its innovative design of a consistency model that supports multi-resolution sampling, overcoming the fixed-resolution limitations of traditional models. The approach also effectively addresses training instability at low batch sizes, making it feasible to train with fewer resources.

### Weaknesses
While the paper presents improved training efficiency as a key contribution, there are two aspects that raise questions regarding this claim:

1. In comparison with Song et al.’s experimental setup, it seems expected that training with a smaller batch size would lead to lower performance. To convincingly demonstrate an improvement in training efficiency, comparing the proposed model with a consistency model trained on low batch sizes may be insufficient. Instead, it would strengthen the argument to show that the proposed method performs better than models trained with larger batch sizes. Specifically, the paper should compare the proposed method against a baseline consistency model trained with a batch size that achieves optimal performance for that baseline, not just a low batch size.
2. In Figure 8, it appears that pre-training is essential for reaching the convergence point of “Denoising Distance.” However, considering the overall training time, if an additional 30 epochs of pre-training are required compared to traditional methods, it may be worth questioning whether this approach can truly be considered efficient. The paper needs to provide a more detailed breakdown of the computational costs associated with pre-training, including the number of parameters in the pre-trained module and the time required for each pre-training epoch, to justify the claim of efficiency.

### Questions
1. Total Training Time: Could the authors clarify the total training time required for the model? While it is mentioned that 30 epochs were used for pre-training, it would be helpful to know the training duration for both CM-UNet and CM-Func models.

2. Evaluation in Table 2: The evaluation process for Table 2 is unclear, particularly regarding how the multi-resolution sampling FPS was measured for CelebA 64. Additional explanation on the methodology used for this metric would be appreciated.

3. Effectiveness with Larger Batch Sizes: It would be interesting to know if the proposed method continues to perform better than models trained with batch sizes larger than 32.

4. Related Works : Adding the following reference to the related work section would enhance the context of the study: Zhuang, Peiye, et al. "Diffusion probabilistic fields." The Eleventh International Conference on Learning Representations, 2023.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the limitations of using a U-Net generator with consistency models, i.e., the substantial computational resources required and the difficulty in generating images at user-specified resolutions. To address these challenges, the researchers propose replacing the U-Net generator with an implicit neural representation (INR), which demonstrates potential in producing images with scalable resolutions. The proposed method reduces training costs relative to the U-Net generator while achieving superior image quality as quantified by common evaluation metrics.

### Strengths
The proposed method is conceptually sound and effectively addresses the limitations of the U-Net-based consistency model.

Experimental results support the efficacy of incorporating INR within consistency models for improved image generation.

### Weaknesses
(1) Novelty: while INR is applied here for high-resolution image generation within the context of consistency models, INR is already a widely-used technique in other 2D image generation frameworks. The contribution appears to be somewhat incremental. The paper does not adequately distinguish its approach from existing INR-based methods, particularly in terms of training methodology and specific architectural choices. The novelty is further diminished by the lack of a clear explanation of how the proposed method addresses the inherent challenges of using INRs in a one-step generation process, such as the difficulty in fitting high-frequency noise.

(2) Related work: the review of related work on INR-based methods is somewhat insufficient, particularly in the context of high-resolution image generation. Additional discussion on alternative high-resolution generation strategies would be beneficial. The paper should include a more comprehensive review of methods that utilize patch-based generation or other techniques for scaling to high resolutions, and clarify how the proposed method compares to these alternatives in terms of both performance and computational cost. The discussion should also address the limitations of existing INR-based diffusion models, particularly those employing two-stage training pipelines, and how the proposed approach overcomes these limitations.

(3) Performance comparison: although the method shows reduced computational cost, its image quality appears less competitive compared to replacing UNet with DiT, as observed in Table 2. The paper lacks a clear demonstration of the advantages of using INR within the consistency model framework, as the reported image quality is only comparable to that of a Transformer-based generator. The evaluation should include a more detailed analysis of the trade-offs between computational cost and image quality, and explore the specific scenarios where the proposed method excels compared to other approaches.

(4) Computation cost comparison: it would be helpful to include a broader computational cost comparison with other methods listed in Table 2, rather than restricting comparisons solely to the CM-UNet model. The paper should provide a more comprehensive analysis of the computational cost, including training time, inference time, and memory usage, and compare these metrics with other state-of-the-art methods, such as those based on patch-by-patch generation. The comparison should also consider the impact of resolution on the computational cost of the proposed method and other alternatives.

(5) It would be clearer and more concise to use “Eq.” rather than “Eq. equation.” when referring to equations.

### Questions
See the limitations above, which detail the questions concerned, and it is expected to address these issues.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach to image generation through consistency models, aiming to improve efficiency in generating high-quality, variable-resolution images. By adopting a Transformer-based generator that leverages implicit neural representations (INRs), the authors propose an architecture allowing flexible resolution generation with reduced resource demands. The method addresses challenges associated with traditional U-Net models by decoupling image resolution from model parameters and incorporating a pre-training phase for enhanced consistency training.

### Strengths
1. The introduction of a Transformer-based generator that produces image functions is an efficient approach that enables any-resolution sampling. This is a significant step forward from fixed-resolution U-Net generators.
2. By decoupling image resolution from model parameters, the proposed method reduces computational overhead and GPU memory usage, allowing more accessible high-resolution image generation.
3. The pre-training task effectively enhances the consistency model’s performance, leading to faster convergence and better denoising capabilities compared to models trained from scratch.

### Weaknesses
1. The paper utilizes Transformers in a relatively straightforward way for image generation. While the INR-based function generator is effective, the paper could benefit from a clearer explanation of how it fundamentally diverges from other Transformer-based models in diffusion applications. Specifically, the paper should clarify how the proposed method addresses the limitations of existing Transformer architectures when applied to consistency models, particularly regarding the generation of consistent images across different resolutions, and provide a more detailed analysis of the architectural differences that enable this capability.
2. The pre-training phase, while beneficial, adds additional complexity to the training pipeline. It would be helpful to compare the training cost between this method and other approaches. The paper should provide a more detailed breakdown of the computational resources required for pre-training versus the main consistency training phase, including GPU hours and memory usage, and compare these costs with those of alternative methods, such as training consistency models from scratch or using distillation techniques.
3. The comparisons with existing one-step diffusion methods are missing. In fact, there are a lot of one-step methods, including ADD and DMD. The paper needs to include a more comprehensive comparison with existing one-step diffusion methods, including a discussion of the trade-offs in terms of sample quality, computational cost, and training stability. It should also clarify why the proposed method is advantageous compared to these alternatives, especially in scenarios requiring arbitrary resolution image generation.
4. Given that the method proposed by the authors is capable of generating images of arbitrary resolution, in the selection of datasets in Section 4.1, the authors should consider including more datasets with various resolutions beyond the current 64 and 128 to facilitate a comprehensive comparison. In fact, a larger resolution has become more popular, e.g. 512 and 1024. It is hard to justify whether this method can actually accommodate arbitrary resolution without reporting the results of high resolution image synthesis. The paper should include experiments on datasets with higher resolutions, such as 512x512 or 1024x1024, to demonstrate the effectiveness of the proposed method in generating high-resolution images. This is crucial for validating the claim of arbitrary resolution generation and assessing the method's scalability.
5. To evaluate the method, more metrics should be considered when comparing different methods, including NIQE, CLIPIQA, MUSIQ, LPIPS, MANIQA, DISTS. The evaluation should include a broader range of image quality metrics, such as NIQE, CLIPIQA, MUSIQ, LPIPS, MANIQA, and DISTS, to provide a more comprehensive assessment of the generated images. This is particularly important for evaluating the perceptual quality and fidelity of the generated images, in addition to the distribution-based metrics.

### Questions
More results are required and more methods should be compared.

### Soundness
2

### Presentation
2

### Contribution
2
