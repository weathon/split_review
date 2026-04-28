# Generative Semantic Communication: Diffusion Models Beyond Bit Recovery

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Semantic communication is expected to be one of the cores of next-generation AI-based communications. One of the possibilities offered by semantic communication is the capability to regenerate, at the destination side, images or videos semantically equivalent to the transmitted ones, without necessarily recovering the transmitted sequence of bits. The current solutions still lack the ability to build complex scenes from the received partial information. Clearly, there is an unmet need to balance the effectiveness of generation methods and the complexity of the transmitted information, possibly taking into account the goal of communication. In this paper, we aim to bridge this gap by proposing a novel generative diffusion-guided framework for semantic communication that leverages the strong abilities of diffusion models in synthesizing multimedia content while preserving semantic features. We reduce bandwidth usage by sending highly-compressed semantic information only. Then, the diffusion model learns to synthesize semantic-consistent scenes through spatially-adaptive normalizations from such denoised semantic information.
We prove, through an in-depth assessment of multiple scenarios,  that our method outperforms existing solutions in generating high-quality images with preserved semantic information even in cases where the received content is significantly degraded. More specifically, our results show that objects, locations, and depths are still recognizable even in the presence of extremely noisy conditions of the communication channel.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tries to consider semantic communication and visual generation at the same time with a new framework. This framework enables more robustness to corrupted conditioning in generation while preserving the transmitted layout as possible. It can also be viewed as a communication-friendly or corruption-robust layout generation framework.

### Strengths
Overall, I think the targeted issue of this paper, generative semantic communication, is very interesting and of high industry values. It seems that this new framework have high potentials of being applied to semantic compression or coding for machines. 

The proposed framework is reasonable and clearly stated in this paper.

The experiments demonstrate the effectiveness of the proposed method on semantic segmentation.

### Weaknesses
Although this work has a very attractive starting point, it also has some obvious limitations：

1. It is not clear for the boundary/difference on the task settings between the target in this work and semantic compression. This work measures the fidelity of transmitted layout by comparing the accuracy of semantic segmentation under communication conditions with similar PSNR. However, it is puzzling why the transmission bit rate is not also one of the optimization targets of the model, like training a neural network based codec.

2. The work does not compare the performance of the proposed framework with directly using the transmitted layouts for semantic evaluation. It is unclear for the role of diffusion-based generative models from the perspective of communication.

3. It is somewhat overly simplistic for using the accuracy of semantic segmentation and the quality of generated images as the evaluation criteria for semantic communication. How about the optimization results for bit rates? And how about the effectiveness on other semantic downstream tasks?

### Questions
Please kindly see some detailed questions in the weakness part. I will adjust my final score based on author responses to my questions.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper primarily addresses the noise issue in semantic communication and proposes a generative method based on the diffusion model for the recovery of transmitted bit sequences. The method is mainly divided into two parts, firstly, an FDS block is designed to remove the noise from the semantic mapping, and then the denoising ability of the diffusion model is utilized to train on the noisy data. Experimental evaluations are conducted on two datasets, Cityscapes and COCO-Stuff, and the experimental results show that the proposed method is advantageous in strong-noise scenarios and can substantially compress the transmitted content to improve communication efficiency.

### Strengths
1. The novel introduction of the diffusion model in semantic communication has contributed to the richness of this research area.
2. The proposed Fast Denoising Semantic Block (FDS) seems to be simple but effective for channel noise.
3. The experimental evaluation is rigorous by assessing the quality of the recovered images in terms of several metrics such as mIoU, LPIPS, FID, and depth estimation.
4. The experimental results are inspiring, especially in strong noise scenarios (PSNR<10). In addition, the binary bit transmission substantially improves communication efficiency.

### Weaknesses
1. There are deficiencies in the setting of noise conditions. In this paper, the authors only used white Gaussian noise of different intensities to review the method. However, other noises such as Poisson noise or a mixture of varying noises may occur during the actual transmission and the authors need to further evaluate the real-world relevance of the method. Specifically, the impact of correlated noise, which is more representative of real-world channel impairments, is not explored. The method's robustness to impulsive noise, which can severely disrupt communication, is also not addressed. Furthermore, the noise model should consider the frequency characteristics of the channel, as different frequencies may be affected differently by the noise.
2. The novelty of the paper is relatively weak, because, except for the FDS module, the diffusion model and the classifier-free guidance are already existing methods. The authors need to highlight the improvements made to these two components. The paper does not sufficiently detail how the diffusion model is adapted for semantic communication, beyond simply using it as a generative model. The specific modifications or training strategies that make it suitable for this task are not clearly articulated. The classifier-free guidance, while effective, is a standard technique, and the paper does not present any novel adaptation or insights into its use within this framework.
3. The structure of the semantic diffusion model appears to be complex and fine-grained, and the recovery process of the data may consume a lot of computational resources, and its feasibility in real-world applications needs to be further discussed. The paper lacks a detailed analysis of the computational complexity of the proposed method, including the number of parameters, FLOPs, and memory requirements. This makes it difficult to assess its practical applicability, especially in resource-constrained environments. Furthermore, the paper does not discuss the inference time of the model, which is a critical factor in real-time communication systems.

### Questions
1. The classifier-free guidance should be added in ablation experiments to evaluate its effectiveness.
2. I would like to know the computational efficiency of the method, preferably in comparison with some typical generative and non-generative methods.
3. Since the FDC module seems to be simple and generic, could the authors combine it with other existing methods to validate the effectiveness of the module?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a framework for recovering images in semantic communication systems, by leveraging diffusion models. The semantic masks are sent, which are extracted from a semantic segmentation model. The mask may be altered because of noises during the communication. The images are synthesized using the semantic mask, according to a diffusion-based semantic image synthesis model. To further improve the synthesis performance, the proposed method first performs a fast denoising on the received semantic masks, which shows useful for better synthesis performance.

### Strengths
+ Overall, the idea to leverage a diffusion model to recover raw images to reduce communication costs sounds interesting.

+ The proposed method shows better synthesis results under the proposed setup, than several state-of-the-art semantic image synthesis models.

### Weaknesses
- The synthesis model is not novel. Diffusion models are popular nowadays. What are the new technical things in this work. Overall, the idea for fast denoising or training with noisy masks are not novel, which are straight solutions.

- In section 4.1, it is mentioned DETR is applied for evaluation. However, in the tables of experiments, mIoU is used to report the semantic similarity. In my understanding, mAP should be used for object detection and mIoU is for semantic segmentation. The paper should clarify how DETR is used and why mIoU is appropriate in this context.

- In section 4.1, depth estimation is mentioned for evaluation, however, which table does show the results of depth estimation? This is confusing for readers. The paper should explicitly state where the depth estimation results are presented, or remove the claim if no such results are provided.

- What is the performance for clean semantic mask as the input? The core component is this work is a semantic image generator, therefore, it is important to show the proposed method is better than previous semantic image generation method. The paper lacks a clear comparison of the proposed method against existing semantic image generation techniques when provided with clean semantic masks, making it difficult to assess its true contribution.

### Questions
How to handle one-to-many mapping in image generation? For example, some low-level information may be missing with this solution, such as the colors of objects are incorrect, comparing the raw images and synthesized images.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper incorporates denoising diffusion probabilistic models (DDPM) to a new application, the semantic communication using deep generative models. The semantic communication process cares about preservation of semantic meanings instead of all details. The authors design a system utilizing DDPM as the generative model to recover the transmitted bits that contain semantic meanings of an image. The experiments show promising results on transmitted recovered images.

### Strengths
+ The paper contributes to a new application of generative model, which seems to be quite important in the communication field.
+ The authors thoroughly explain the architecture details in the paper
+ The result show performance improvements over baselines

### Weaknesses
There are several questions I'm hoping the authors can address:

- Although the generative model aims to be semantic preserving, the training method still uses recovering original image (where every pixel matters) as the objective function. This seems to be conflicting with the motivation. The diffusion model's loss function, which minimizes the difference between predicted and true noise added to the image, inherently focuses on pixel-level reconstruction. This approach doesn't explicitly encourage the model to prioritize semantic features over pixel-perfect detail. A semantic loss, perhaps based on feature distances in a pre-trained network, would be more aligned with the stated goals.
- Pragmatic compression (preserving useful information in the bottleneck) [1] seems to be quite related. How would the authors compare with this line of work?
- In terms of writing, I feel it would be nice to have more overarching sentences explaining the model design instead of going into too details in the experiment section. There also seems to be a lack of explanation on the baselines in experiment section. This is especially important on less established benchmarks and tasks.
- There is no obvious modeling novelty on generative models or compression + diffusion algorithm.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
