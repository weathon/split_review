# Denoising with a Joint-Embedding Predictive Architecture

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Joint-embedding predictive architectures (JEPAs) have shown substantial promise in self-supervised representation learning, yet their application in generative modeling remains underexplored. Conversely, diffusion models have demonstrated significant efficacy in modeling arbitrary probability distributions. In this paper, we introduce Denoising with a Joint-Embedding Predictive Architecture (D-JEPA), pioneering the integration of JEPA within generative modeling. By recognizing JEPA as a form of masked image modeling, we reinterpret it as a generalized next-token prediction strategy, facilitating data generation in an auto-regressive manner. Furthermore, we incorporate diffusion loss to model the per-token probability distribution, enabling data generation in a continuous space. We also adapt flow matching loss as an alternative to diffusion loss, thereby enhancing the flexibility of D-JEPA. Empirically, with increased GFLOPs, D-JEPA consistently achieves lower FID scores with fewer training epochs, indicating its good scalability. Our base, large, and huge models outperform all previous generative models across all scales on class-conditional ImageNet benchmarks. Beyond image generation, D-JEPA is well-suited for other continuous data modeling, including video and audio.

Project page: \url{https://d-jepa.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the JEPA framework—a masked-image-based self-supervised representation learning model—to image generation by incorporating an additional MLP head that operates on image patches. This design unifies representation learning and image generation within a single framework, demonstrating improved image generation quality over recent state-of-the-art methods in specific model configurations.

### Strengths
(1) This paper introduces a straightforward and effective approach to enhance generation quality by bridging representation learning and image generation.
(2) In the appendix, the authors offer an in-depth analysis of the model design, including additional insights on representation learning as well as applications in video and audio generation, showcasing the versatility of the proposed methods across multiple tasks.
(3) The presentation is clear, and the ideas are easy to understand.

### Weaknesses
 (1) The performance is comparable to similar approaches like MAR, which does not use the JEPA loss. In Table 1, the proposed method requires more training epochs (1400 vs. 800 for D-JEPA-B VS ) to achieve similar results to MAR-B. While D-JEPA-L/H outperforms MAR-L/H, it also involves more parameters. Similar trends are observed in Table 2.
(2) There is no comparison to baseline methods, such as the effect of removing the JEPA loss.
(3) How does the model perform in unconditional generation tasks or on more complex datasets, such as COCO?

### Questions
My main concerns with this paper relate to its performance compared to the similar approach, MAR. The absence of ablation studies on model components and evaluation on other datasets makes it challenging to assess the impact of each design choice.

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
5

### Summary
The proposed D-JEPA is the combination of Joint-embedding Predictive Architecture (I-JEPA) with MAR's dfiffusion parts, ie, leveraging a feautre from JEPA as the condition of diffusion parts.  Good generative performance is achieved by the proposed model.
And authors provide the exps over multi-modalities.

### Strengths
1. Suffieicnt experiments, including generative reuslts on Imagenet-256, sufficient abaltion studies and the exps about representation learning.

2. Authors present the effectiveness of D-JEPA  over multi-modalities including videos, images and audio.

3. Authors provide a theretical support about the proposed models.

4. Beyond the generative results, authors provides the empirical study about the linear performance of the proposed D-JEPA with the pixel/latent-level inputs.

### Weaknesses
1. The organization and the structure of the current version should be improved. The writing of chapter 3 is very confusing for me. And some important results and discussions should be re-located in the main paper not the appendix.

2. The novelity is limited:
 It seems that this work just replace the MAGE parts of MAR. The simple combination of I-JEPA and MAR's dfiffusion parts. It doesn't solve the core issue between the gap of representation learning and generative modeling.
Such an archecture cannot bring huge improvement on representation learning with latent-level input (Results in AppendixE over  down-stream tasks are good, just for pixel-level inputs), and the corresponding performance are very poor.
Could you please provide the similar settings for MAR? Use both the pixel-level and latent-level inputs to check the representation performance? I think your design with JEPA cannot solve the inherent limitation (latent input -> bad representation results) of such an TOKEN learning + diffusion framework.

3. The core of I-JEPA is the small-block-wise masks to perform the feature-level augmentation to achieve the better linear performance without the help of data-level augmentation. But in your work, the random mask strategy with high ratio is applied. Could you please provide some empirical evidence and intuitions about such a design？


4. Line 200： “It is important to note that training in latent space is not a necessity for D-JEPA; it can be trained in raw space and still achieve excellent results.” WHERE is the corresponding generative results？ I haven't found it.

5. It is unfair to compare Huge scale models in Table1 and 2. The parameters of the proposed D-JEPA is not aligned with MAR-H. 

6. How about the D-JEPA-H linear and finetuning performance in Table 7/8.

7. Please provide the exps on Imagenet-512x512 to compare with  SOTAs in a more comoutation situation.

### Questions
Listed in Weakness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The author describes a JEPA based architecture which combines a prediction loss and a diffusion loss.
* The prediction loss learns to predict the representation of the mask tokens
* The diffusion loss learns to predict the raw pixels (or the latent representation of the patch in case of VAE)

The architecture itself is based on a three ViTs:
* The context encoder takes the unmasked tokens and outputs Y
* The feature predictor takes Y, pad it, and learns to reconstruct the full representation Z
* The target encoder takes all tokens (no masking) and produces the target representation Z'
* The prediction loss is a smooth l1 loss between Z and Z'
* The diffusion loss takes Z as input and tries to predict the pixels / latents
* The target encoder is itself an EMA of the context encoder

The paper explores this architecture and shows that:
1) The diffusion loss prevents the collapse of traditional JEPA architectures
2) This architecture is scalable, as the results improves with increased compute budget
3) At inference, instead of predicting all unmasked tokens, we can predict a subset of them, as do MaskGIT, to provide better results
4) They reach SOTA performance on class conditional generation on ImageNet 256x256, equating the results of MAR with CFG

### Strengths
* Interesting combination of JEPA representation learning with generative AI, showing that representation learning can help generative AI
* Strong SOTA results on ImageNet 256x256, better or equal than MAR
* When applied for representation learning, the context encoder achieves good results on ImageNet classification
* Experiments showing generalization to text conditioned image generation (and not just class conditioned)
* Experiments showing that it works with audio as well, class conditioned video generation, and CFG

### Weaknesses
 * It would be interesting to have generation results at higher resolution than 256x256 px to see if inference speed suffers when bi-directional attention meets lots of tokens

### Questions
n/a

### Soundness
3

### Presentation
2

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
The paper, D-JEPA, explores a novel approach by merging joint-embedding predictive architectures with generative modeling. It applies masked image modeling as a generalized next-token prediction strategy for autoregressive data generation. D-JEPA employs a combination of diffusion losses and MAE loss to model token distributions effectively. It aims to enhancing generative tasks across various domains like images, videos, and audio. Extensive experiments demonstrate the model's scalability and effectiveness, claiming state-of-the-art performance on ImageNet class-conditional benchmarks.

### Strengths
The ideas tha integrating joint-embedding predictive architectures(e.g. MAE and MIM) with diffusion-based generative modeling makes sense. 

The experiments in the paper are robust, covering a wide range of applications, which showcases the versatility of the D-JEPA model. This extensive experimental validation strengthens the paper's claims about the model's effectiveness across different types of generative tasks.

### Weaknesses
However, the paper presents a significant methodological oversight—it appears as a mere combination of existing MAE (Masked Autoencoder) and MAR (Masked Autoregressive Model) methods without a critical analysis or ablation study showing how the MAE branch impacts the AR branch. Specifically, the absence of experiments where the MAE branch is removed casts doubt on the incremental benefit of this integration.

The representation learning capability of D-JEPA is also questionable. According to Table 7, the best ImageNet accuracy is obtained when the model is trained on pixel-level data, while the generative experiments focus on a D-JEPA trained on VAE latent space. This discrepancy points to a lack of a truly unified model approach, as the performance seems to depend heavily on the training specifics rather than the model architecture itself.

### Questions
1. Could the authors provide an ablation study that isolates the MAE branch to elucidate its specific impact on the AR branch's performance?

2. How does the model's performance on representation learning tasks vary between training in pixel space and latent space, and what does this indicate about the model's ability to serve as a unified architecture?

3. It’s interesting to see from Tables 1 and 2 that D-JEPA has more parameters than MAR. I’m curious—shouldn’t these models have similar architectures? Can the authors explain why D-JEPA is larger? What additional components does D-JEPA include that MAR doesn't?

### Soundness
2

### Presentation
3

### Contribution
2
