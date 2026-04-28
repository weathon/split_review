# DiffPC: Diffusion-based High Perceptual Fidelity Image Compression with Semantic Refinement

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Reconstructing high-quality images under low bitrates conditions presents a challenge, and previous methods have made this task feasible by leveraging the priors of diffusion models.  However, the effective exploration of pre-trained latent diffusion models and semantic information integration in image compression tasks still needs further study. To address this issue, we introduce Diffusion-based High Perceptual Fidelity Image Compression with Semantic Refinement (DiffPC), a two-stage image compression framework based on stable diffusion. DiffPC efficiently encodes low-level image information, enabling the highly realistic reconstruction of the original image by leveraging high-level semantic features and the prior knowledge inherent in diffusion models. Specifically, DiffPC utilizes a multi-feature compressor to represent crucial low-level information with minimal bitrates and employs pre-embedding to acquire more robust hybrid semantics, thereby providing additional context for the decoding end. Furthermore, we have devised a control module tailored for image compression tasks, ensuring structural and textural consistency in reconstruction even at low bitrates and preventing decoding collapses induced by condition leakage. Extensive experiments demonstrate that our method achieves state-of-the-art perceptual fidelity and surpasses previous perceptual image compression methods by a significant margin in statistical fidelity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents DiffPC, a two-stage image compression framework leveraging stable diffusion models. In the first stage, a multi-feature compressor encodes essential low-level details using minimal bitrates, while a pre-embedding module captures robust hybrid semantics by combining textual and visual information. In the second stage, DiffPC employs IC-ControlNet to ensure structural and textural consistency during image reconstruction, mitigating issues such as condition leakage. Extensive experiments demonstrate that DiffPC achieves state-of-the-art performance in both perceptual and statistical fidelity across various benchmark datasets, outperforming existing neural compression methods.

### Strengths
DiffPC introduces an framework by integrating diffusion models with semantic refinement for image compression  and the paper conducts thorough quantitative and qualitative evaluations across multiple datasets and compares DiffPC with several state-of-the-art methods .The results consistently show superior performance in both perceptual metrics and statistical fidelity, particularly at ultra-low bitrates.

### Weaknesses
Multi-step inference combined with heavy ControlNet and pre-trained base models pose significant computational challenges for the decoding side. While pre-trained T2I diffusion models can enhance the quality of compressed images, their high computational cost makes them an unacceptable solution for image compression.

Although latent diffusion can enhance semantic details, it can also compromise some structural details, such as small faces and small text, which are not demonstrated in the paper.

### Questions
[1] Although latent diffusion can enhance semantic details, it can also compromise some structural details, such as small faces and small text, which are not demonstrated in the paper.

[2] I would like to understand the performance comparison between directly using VAE compression and DiffPC.

I will consider raising the score once all concerns are addressed.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a diffusion-based image compression framework, DiffPC, aimed to achieve high perceptual fidelity at low bit rates. This model leverages both low-level degraded image representation and high-level hybrid semantic representation to control pre-trained Stable Diffusion. Experimental results show that the proposed method surpasses existing methods across various benchmarks, delivering superior perceptual quality and statistical fidelity.

### Strengths
1. The usage of high-level hybrid semantic representation in diffusion-based image compression methods is novel. I appreciate the idea of extracting semantic information from $\hat{c}_x$.

2. The paper effectively communicates the purpose and rationale behind each module in the DiffPC framework, providing clear justifications for their functionality.

3. The paper includes thorough experiments with quantitative and qualitative metrics across multiple datasets, validating the effectiveness of DiffPC.

### Weaknesses
1. The paper lacks a thorough comparison and analysis of computational complexity. As diffusion models inherently introduce high decoding complexity, it is essential to evaluate and compare this aspect against previous SOTA methods, specifically detailing the inference time and memory requirements for both encoding and decoding stages. This analysis should include a breakdown of the computational cost associated with each module of the proposed DiffPC framework.

2. The paper has some issues related to writing clarity and accuracy of details. Please refer to questions 1-9 for specifics.

3. There are issues with citation formatting in certain parts of the paper. For instance, on page 2, line 079, the sentence ``… generative adversarial frameworks Mentzer et al. (2020); Muckley et al. (2023)`` should be formatted as ``… generative adversarial frameworks (Mentzer et al., 2020; Muckley et al., 2023).`` 

4. Other existing image compression methods [1, 2] could be discussed and compared. The discussion should not only focus on performance metrics but also on the architectural differences and the trade-offs made by each method.

### Questions
1. On page 2, line 097, ``Careil et al. (2023) ...`` PerCo was published in ICLR2024.

2. On page 3, line 138, in the sentence ``He et al. (2022), based on the orthogonality of features in channel and spatial dimensions, devised an asymmetric autoregressive entropy encoder..`` there are two periods at the end.

3. On page 4, line 183, there is a grammatical error in the sentence: ``Here, c and s respectively refer to low-level image controls (e.g., image contours, image degradation), with s denoting high-level semantic controls (e.g., textual descriptions of images, category label).``

4. On page 10, line 520, in the sentence ``(2) w/o TAC: Removing the TAC ...``, should `TAC` actually be `TAD`?

5. On page 11, line 545, ``En d-to-end optimized image compression.`` There is an extra space that should be removed.

6. Is Eq. (3) accurate? $\mathcal{DN}_{\theta}(z_t, t)$ is the predicting noise rather than the mean.

7. In Eq. (13), what does $\eta$ denote in $TAD_{\eta}$?

8. In Figure 10(a), it appears that an arrow from the conv3×3 layer to the Spatial Transformer is missing. In Figure 10(b), there are two instances of $\varepsilon$. Should they be represented by different symbols to avoid confusion?

9. On page 4, line 178, the introduction to Stable Diffusion is incomplete, as it does not explain how $\hat{z}_0$ is obtained within Stable Diffusion.

10. The authors mention that ``the importance-weighted loss assigns more bits to texture details, enabling a more precise reconstruction of these features.`` Could the authors provide a visualization result of the bit allocation to support this conclusion?

11. What impact do multi-scale features have on performance? In Eq. (12), the loss $L_{imp}$ is calculated based on the difference between $z_0$ and $c$, where multi-scale features do not appear to be necessary. Additionally, the authors have not demonstrated the role or necessity of multi-scale features in the ablation study. Clarifying these points would strengthen the paper’s argument for including multi-scale features.

12. In Eq. (13), how is the initial value of $w$, specifically $\sigma_{z_0}^2$, determined in practice? Additionally, how do you ensure that the trainable hyperparameter $w$ correctly learns to achieve precise bit allocation? 

13. This module adopts a pre-embedding approach that combines textual semantics with visual semantics. Could the authors clarify the individual roles of textual semantics and visual semantics? Additionally, what impact would using only textual semantics or only visual semantics have on performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
(1).This paper proposes a diffusion-based high-perceptual fidelity image compression with semantic refinement. 
(2).The proposed method uses the low-level image information to ensure fidelity reconstruction,  and uses high-level texture semantics and robust prior in pre-trained latent stable diffusion to ensure realism reconstruction. 
(3).Extensive experiments demonstrate its effectiveness in reconstructing images with high perceptual quality texture at extremely low bitrates

### Strengths
Originality: This paper explores the pre-trained latent diffusion model using semantic control signals for extreme image compression. This method clearly explains that two types of semantics, namely low-level image information (visual semantics) and high-level semantics (textual semantics), can support image compression.

Quality: The method is well designed and integrates the pre-trained latent diffusion model and semantic information for extreme image compression.

Clarity: The paper is generally well written and organized.

Significance: The significance of this work is profound as it addresses the extreme image compression using pre-trained latent diffusion models and semantic information.

### Weaknesses
(1). The authors do not describe some representative perceptual image compression methods corresponding to their work in the related work.  
[1]. Multi-modality deep network for extreme learned image compression. AAAI 2023.
[2]. Extreme Image Compression using fine-tuned VQGANs. Data Compression Conference 2024. 
[3]. Towards Extreme Image Compression with Latent Feature Guidance and Diffusion Prior. IEEE TCSVT 2024.
[4]. Consistency Guided Diffusion Model with Neural Syntax for Perceptual Image Compression. ACMMM 2024.
[5]. HybridFlow: Infusing Continuity into Masked Codebook for Extreme Low-Bitrate Image Compression. ACMMM 2024.
[6]. Neural Image Compression with Text-guided Encoding for both Pixel-level and Perceptual Fidelity. ICML 2024.

(2). In Figure 2, it is confusing that you use the same color of block to represent cross-attention layers. The pre-embedding module is not shown in Figure 2. The ICCN (i.e., IC-ControlNet) is not explained in Figure 2 or your paper.

(3). In Eq.(7), the c ̂_x is a degraded image instead of features, which is the input of an image encoder, as shown in Figure 2. You need to add the image encoder to your equation.

(4). In the part ``IC-ControlNet and Time-aware Decoupling” of section 3.2, the conditions are integrated with noise and processed through residual blocks before entering the main network. I cannot find any residual blocks as you say in Figure 9.

(5). In Section 3.3, the symbol 〖text〗_x should be shown in Figure 2. The semantic pre-embedding module should be marked in Figure 2 (the same as (2)). The blended semantic s_x should be added to Figure 2 for clarity.

(6). Please compare your method with VQGAN-based compression (DCC2024), TACO (ICML2024), and DiffEIC (IEEE TCSVT2024) and add them to Figures 4 and 5. VQGAN-based IC performs extreme image compression using codebook prior. TACO uses the text prior and DiffEIC uses the diffusion prior, which are very relevant to your work.

Reference papers:
[1]. Extreme Image Compression using fine-tuned VQGANs. Data Compression Conference 2024. 
[2]. Towards Extreme Image Compression with Latent Feature Guidance and Diffusion Prior. IEEE TCSVT 2024.
[3].Neural Image Compression with Text-guided Encoding for both Pixel-level and Perceptual Fidelity. ICML 2024.

(7). What is TAC in your ablation study?  I think it is the TAD module in your procedure.

(8). The text can assist image compression. I think you need to further analyze the text description for image compression. For example, you can use different caption methods to generate captions, which are used for your compression framework (test the text robustness of your method).

(9). The author should compare the proposed method with state-of-the-art methods in terms of model complexity.

### Questions
(1). Why do you need intermediate features f1 and f2 for a multi-feature compressor? Maybe using a simple compressor without multi-scale features is simple but effective. Please add an ablation study to validate its effectiveness for image compression.

(2). Could you give a visual comparison of using importance-weighted MSE and standard MSE? It ensures proper bit allocation as you describe in your paper. You can visualize the bit allocation map to explain this.

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
DiffPC is a novel two-stage image compression framework leveraging stable diffusion models to enhance perceptual fidelity at low bitrates. The model first compresses low-level image details and then integrates semantic features to reconstruct high-quality images. Using modules like a multi-feature compressor, IC-ControlNet, and a semantic pre-embedding module, DiffPC manages to maintain structural and textural consistency.

### Strengths
1. State-of-the-Art performance. Demonstrates superior perceptual and statistical fidelity at low bitrates compared to other image compression methods.
2. Efficient semantic integration. The pre-embedding module effectively combines textual and visual semantics, validating that optimizing semantic information has the potential to improve image reconstruction quality. This is a fascinating discovery.

### Weaknesses
1. It is recommended that the authors improve the clarity and accuracy of the equations to facilitate reader comprehension. In the "related work" section, some formulas are not precise. For instance, in Eq. 2 and Eq. 3, the variances for the forward and reverse processes are both represented by ${\beta}t$, which is incorrect. Notation such as $DN{\theta}$ is typically represented as $\epsilon_{\theta}$ in existing literature. If the authors are referencing prior work, it is advisable to adhere to standard conventions to improve readability. Additionally, $\textbf{c}$ generally denotes conditional controls, i.e., “text prompts”, which corresponds to $\textbf{s}$ for "textual descriptions" in Eq. 5.

2. For lines 78-87, using `\citep` allows multiple references to be embedded smoothly within a sentence without disrupting the structure. This improves readability, especially when citing multiple sources.

3. Similar works that fine-tune pre-trained diffusion models for low-quality image enhancement include:

   - [1] Lin, X., He, J., Chen, Z., Lyu, Z., Dai, B., Yu, F., ... & Dong, C. (2023) in "DiffBIR: Towards Blind Image Restoration with Generative Diffusion Prior".
   - [2] Wang, Y., Yu, Y., Yang, W., Guo, L., Chau, L. P., Kot, A. C., & Wen, B. (2023) in "ExposureDiffusion: Learning to Expose for Low-Light Image Enhancement" (ICCV).
   - [3] Ma, J., Zhu, Y., You, C., & Wang, B. (2023) in "Pre-trained Diffusion Models for Plug-and-Play Medical Image Enhancement" (MICCAI).

Could the authors further clarify how this manuscript differs from these related works?

### Questions
1. In Line 45, are *realism* and *perceptual fidelity* truly equivalent concepts, or could their distinctions be further explored?

2. The experimental section demonstrates that PSNR and SSIM metrics for generative models are not optimal. Could some insightful explanations be provided for why this is the case?

3. Lines 48-49: Are human perception and image semantic consistency necessarily aligned? Not all visual tasks require precise details; for instance, in certain scene understanding tasks, a lower bitrate may be sufficient to convey overall semantics without losing information essential to human perception.

4. The mentions of decoding collapse and condition leakage in the abstract are insightful explanations. Is there corresponding data analysis in the experimental section to support these claims?

### Soundness
2

### Presentation
2

### Contribution
2
