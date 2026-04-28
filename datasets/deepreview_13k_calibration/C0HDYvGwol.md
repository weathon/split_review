# 3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 5, 6, 6

## Abstract
Multi-view image diffusion models have significantly advanced open-domain 3D object generation. However, most existing models rely on 2D network architectures that lack inherent 3D biases, resulting in compromised geometric consistency. To address this challenge, we introduce 3D-Adapter, a plug-in module designed to infuse 3D geometry awareness into pretrained image diffusion models. Central to our approach is the idea of \emph{3D feedback augmentation}: for each denoising step in the sampling loop, 3D-Adapter decodes intermediate multi-view features into a coherent 3D representation, then re-encodes the rendered RGBD views to augment the pretrained base model through feature addition. We study two variants of 3D-Adapter: a fast feed-forward version based on Gaussian splatting and a versatile training-free version utilizing neural fields and meshes. Our extensive experiments demonstrate that 3D-Adapter not only greatly enhances the geometry quality of text-to-multi-view models such as Instant3D and Zero123++, but also enables high-quality 3D generation using the plain text-to-image Stable Diffusion. Furthermore, we showcase the broad application potential of 3D-Adapter by presenting high quality results in text-to-3D, image-to-3D, text-to-texture, and text-to-avatar tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces 3D-Adapter, a plug-in module aimed at improving 3D consistency in multi-view diffusion models for 3D generation. By integrating a combination of 3D representation and ControlNet for depth conditioning into the denoising framework, 3D-Adapter enhances 3D structure coherence across views without modifying the core model's topology / weights. The authors present two 3D-Adapter variants: a fast feed-forward method using Gaussian splatting (GRM) and a flexible, training-free approach utilizing NeRF optimization. Extensive evaluations across text-to-3D, image-to-3D, and text-to-texture tasks demonstrate that 3D-Adapter improves geometry quality and coherence over prior methods, providing a robust solution for multi-view 3D generation tasks.

### Strengths
By integrating depth conditioning via ControlNet, the 3D-Adapter provides a straightforward yet effective solution to incorporate 3D priors within 2D diffusion frameworks as a part of denoising process.

The paper presents extensive quantitative and qualitative evaluations across multiple configurations and baselines.

The proposed 3D-Adapter outperforms several prior methods in 3D generation quality, demonstrating improvements on widely used metrics like CLIP score and aesthetic score.

### Weaknesses
The paper’s scope is broad, which obscures the clarity of its main contributions and makes it challenging to pinpoint specific innovations with reusable community value. Instead of covering multiple branches, e.g., GRM vs. NeRF optimization, a more focused examination on a single GRM pipeline could provide deeper insights, making the contribution more accessible and actionable for the community. Some comparisons and insights appear irrelevant, e.g. the text-to-avatar section, as the paper primarily addresses general 3D consistency issues rather than avatar-specific issues. This creates confusion regarding the paper’s core contributions.

Introducing per-step 3D → depth → ControlNet prediction comes with computational overhead. The paper could explore strategies to mitigate this, such as reducing the frequency of applying the adapter or skipping initial steps. Since per-step VAE decoding is probably the main bottleneck, adopting a lightweight VAE alternative, e.g. TinyAE, could yield substantial speed gains.

Some design choices around the ControlNet addition appear understudied. Introducing depth ControlNet itself may add a substantial 3D prior, but this effect is not adequately considered and is instead attributed mainly to ControlNet's role in denoising. Additionally, in the GRM branch, ControlNet is trained from scratch, which seems counterintuitive and is not supported with ablation studies.

The paper was fairly difficult to read and navigate, primarily due to its broad scope and, to a lesser extent, its writing style.

### Questions
(1) What is the rationale behind the significant drop in metrics in Table 1 when adding IO sync and GRM finetuning to the two-stage baseline? Also GRM finetuning does not appear to be evaluated in the 3D-Adapter case.

(2) The SOTA selection in Table 2 seems debatable; could the authors clarify the choice of methods over more recent approaches?

(3) How does the output quality compare to I/O sync + tiled ControlNet, and how critical is ControlNet’s role during denoising relative to the 3D prior that could be introduced simply by depth conditioning in IO mode?

### Soundness
2

### Presentation
2

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
The paper suggests a novel approach by introducing the 3D feedback augmentation adapter. It presents methods for applying this adapter to both feed-forward 3D generation and pretrained 2D models. The design incorporates a comprehensive 3D rendering process and a fine-tuning stage utilizing ControlNet to enhance the model's 3D awareness and multi-view consistency. Through experiments, the paper demonstrates the superior performance of the 3D-Adapter by applying it to various tasks and diverse base models, showcasing its effectiveness and versatility across different applications.

### Strengths
1. The idea behind the 3D-Adapter is conceptually novel. It incorporates a lightweight 3D rendering pipeline within the diffusion sampling process through a mechanism that balances computational efficiency and multi-view consistency.


2. While there may be limitations in terms of generalizability, the 3D-Adapter has demonstrated significant versatility through its application across various tasks and base models, as shown through comprehensive experiments.

### Weaknesses
1. Clarity of exposition: A more comprehensive explanation of the relationship between GRM and models such as Instant3D and Zero123++ would greatly enhance the reader's understanding. It is particularly important to elucidate whether GRM builds 3D representations from the views generated by Instant3D and Zero123++ and whether fine-tuning of GRM is involved in this process.

2, Limitations in the scalability of 3D-Adapter: 
- According to Equation 2, it appears that the 3D-Adapter could potentially be applied to other I/O sync-based pretrained models. However, it is necessary to discuss whether incorporating ControlNet into I/O sync pretrained models beyond GRM would yield similar results, and why Training Phase 1 is essential. If Training Phase 1 is a crucial step for optimizing the performance of 3D-Adapter, including GRM, it should be examined whether this phase is equally necessary when applied to other models.

- Despite utilizing various 3D representation techniques and loss functions, such as NeRF and DMTet, ensuring global semantic consistency remains challenging. This inherent limitation highlights the need for additional conditions to achieve robust 3D generation. Consequently, this raises concerns about the 3D consistency of 3D-Adapter in more general text-to-3D or image-to-3D tasks outside of specialized domains, such as avatar generation.

### Questions
- The role of augmentation guidance appears to be significant. Could you provide visual evaluations in addition to Table 1 to better illustrate this effect?
- Please include a dedicated pipeline figure specifically for the process described in Section 4.2 (line 289) to enhance clarity.
- What are the results of using the optimization-based 3D-Adapter without additional conditioning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose 3D-adapter, a method to improve quality and 3d-consistency of existing text-to-multiview and text-to-image models by having a branch which reconstructs an object in 3D, then applies trained controlnet on rendered rgb and depth.

### Strengths
* Improved quality in downstream tasks over previous state-of-the-art
* Extensive final metrics in text-to-3d evaluation

### Weaknesses
 * The quality improvement in the main text-to-3D task is 1) marginal and 2) visuals are not convincing enough to justify complicating the training pipeline. For instance, in Fig. 1, image-to-3D visuals are comparable b/w 3D-Adapter and "two-stage pipeline"
* The paper lacks significant novelty, as the use of 3D representations for synchronization has been explored before (e.g. NerfDiff). The main contribution appears to be the placement of the adapter in the parallel branch rather than at the input/output stage of the diffusion UNet. However, this seems more like a technical choice, as is the decision to train ControlNet on intermediate outputs.
* Some visuals (e.g. Fig. 3, column 5) raise concerns about the correctness of the implementation.
* The explanation regarding the disruption of residual connections due to 3D reconstruction is unclear. If the 3D reconstruction is applied either before or after the UNet denoising stage, the residual connections within the UNet should not be affected. The paper needs to clarify how the 3D reconstruction process specifically interferes with these connections.
* The claim that two-stage approaches specifically suffer from blurry textures is not adequately supported. The paper needs to provide concrete evidence or examples demonstrating this issue, rather than stating it as a general problem. The term "texture seams" is mentioned, but this is different from "blurry textures" and needs further clarification.
* The meaning of "linearity" in the context of the synchronization process is not clear. The paper needs to provide a more precise definition of what is meant by linearity and how it relates to the synchronization methods used.
* The I/O-sync implementation in Tables 1 and 5 raises concerns. Specifically, the significant drop in performance from A0 to A1 in Table 1, coupled with the seemingly broken visuals in column 5 of Fig. 3, despite a high CLIP score, suggests potential issues with the evaluation or implementation. The discrepancy between the visual quality and the CLIP score needs further investigation.
* The justification for using ControlNet over other methods, such as pure latent fusion, is not well-explained. The paper should provide a more detailed comparison of these approaches and explain why ControlNet is the preferred choice.

### Questions
1. Please clarify the following:
  > However, 3D reconstruction and rendering are lossy operations that disrupt residual connections.

  Since residual connections shouldn’t be disrupted if 3D reconstruction is applied before or after the UNet denoising stage, I’m unclear why this is described as a problem. Could you explain?

2. (line 142)

> A common issue with two-stage approaches is that existing reconstruction methods, often designed for or trained under conditions of perfect consistency, lack robustness to local geometric inconsistencies. This may result in floaters and **blurry textures**.

Please provide evidence that two-stage approaches specifically suffer from blurry textures.

3. (line 198)

> assuming linearity

Could you clarify what you mean by "linearity" in this context?

4. Regarding concerns over some visuals: Could you provide a detailed explanation of the I/O-sync implementation in Tables 1 and 5? Table 5 shows a slight improvement when using I/O-sync in the "baseline" model, but in Table 1, there's a significant drop from A0 to A1. The visuals in column 5 appear broken and clearly worse than those in, for example, LGM, yet the CLIP score is significantly higher. Please double-check these evaluations.

5. Could you justify the use of ControlNet? How does it compare to using pure latent fusion?

6. 
> During the sampling process, the adapter performs NeRF optimization for the first 60% of the denoising steps. It then converts the color and density fields into a texture field and DMTet mesh, respectively, to complete the remaining 40% denoising steps. All optimizations are incremental, meaning the 3D state from the previous denoising step is retained to initialize the next. As a result, only 96 optimization steps are needed per denoising step. Alternatively, for texture generation only, multiview aggregation can be achieved by backprojecting the views into UV space and blending the results according to visibility

It's quite complex and specific training process, it would be great to hear about the reasoning/ablations behind these numbers.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This submission introduces 3D-Adapter, a novel module to address challenges in 3D geometry consistency synchronization in multi-view image diffusion models. 
This submission identifies the fundamental limitation of existing synchronization methods working on input and output domains. Then, the authors propose to add a synchronization mechanism to the intermediate feature level (like ControlNet) to encourage 3D consistency in existing multi-view image diffusion models, instead of input and output levels.
The key idea of the mechanism is that, at each denoising step, intermediate latent representations are decoded, 3D-reconstructed, and projected back to 2D representations (RGBD), where improved 3D consistency is re-encoded, called 3D feedback augmentation.

The study explores two variants of the 3D-Adapter: a feed-forward version using a Gaussian Splatting-based model (GRM) with fine-tuning and a training-free version utilizing neural fields and meshes depending on application scenarios. The extensive experiments across text-to-3D, image-to-3D, text-to-texture, and text-to-avatar tasks demonstrate that 3D-Adapter improves generation quality in existing pre-trained models like Instant3D and Zero123++.


Overall, the submission is deemed to be well-prepared and positioned.

The proposed method itself would not be very innovative, but this reviewer found that the motivation and its theory behind the motivation are interesting. Although the researchers have been empirically aware of the limitation of the I/O sync method, the authors clearly presented the gap, which grounds the motivation of the proposed approach well.

However, some weaknesses remain that may improve the submission further.

### Strengths
- Clear contributions and positioning among existing research
- Clear demonstration of the limitation of I/O sync
- Resource-efficient design (training data efficient and training resource-efficient)
- Demonstration of various applications
- Noticeable improvements in terms of geometry and visual fidelity
- Clarity and presentation. The paper is well-organized and clearly presented

### Weaknesses
 - **Lack of information on computation and memory overhead for competing methods**

  Although the authors briefly address computaitonal overhead in "Text-to-Texture Generation" and "Text-to-Avatar Generation" applications, the authors do not explicitly compare overheads in "Text-to-3D" and "Image-to-3D" cases. While it is not neccessary to win every competing method, providing these comparisons would help readers better understand the position of this work in terms of computation demands. Specifically, the lack of detailed profiling, such as per-stage memory usage and inference time, makes it difficult to assess the practical applicability of the proposed method compared to existing approaches. A breakdown of time spent on each component of the 3D-Adapter (e.g., feature extraction, 3D reconstruction, and feedback augmentation) would be beneficial.

- **Missing related work**

  The paper is well-position among the existing work, but some recent works are missing. Since this field is very competitive and timely, it would be beneficial to acknowledge recent developments as well so that readers gains a clearer understanding of the current landscape and to discern similarities and differences. 

  [C1] EpiDiff: Enhancing Multi-View Synthesis via Localized Epipolar-Constrained Diffusion, CVPR 2024

  [C2] LRM: Large Reconstruction Model for Single Image to 3D, ICLR 2024

- **Lack of comparison with recent methods in Sec. 5.4 "Text-to-Texture Generation"**

  Texture generation researches have been developed to enhance multi-view consistency quite well. A few samples of the following works are not concurrent but the past researches. The authors missed these very relevant work and only compared with past researches. 

  [C3] DreamMat: High-quality PBR Material Generation with Geometry- and Light-aware Diffusion Models, SIGGRAPH 2024

  [C4] TexPainter: Generative Mesh Texturing with Multi-view Consistency, SIGGRAPH 2024

  [C5] Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering, CVPR2024

  [C6] Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models, CVPR2024

  In addition, for the Text-to-3D generation, [C1] released their code, but the authors did not compare with this closely related work.


- **Confusing notation of the proposed method in the tables**

  3D-Adaptor is not a standalone model. The notation "3D-Adaptor" could mislead readers to perceive it as a standalone model. The authors are recommended to change the notations of the proposed method across all the parts: e.g., "3D-Adaptor (ours)" => "Instant3D + 3D-Adaptor (ours)" to clarify the integration.

### Questions
- The analysis in Appendix A helps to clarify the motivation of this work. On the other hand, the result is something that has been known in the community. Have any similar results been discussed previously in different domains? It would be convincing to add references to discuss consistency across different works in different applications.

- How much training data should be used to train GRM? As stated in the training details of Sec. 4.1, the authors fine-tuned 2000 iterations with 16 objects in a single batch, i.e., 32000 objects. Considering that a single object yields many views, it seems to be a lot for fine-tuning. What is the minimal training data to make the proposed method work? This question can also be rephrased as why the authors picked 2000 and 4000 iterations for the Instant3D and Zero123++ cases, respectively.

- Extending analysis: The authors showed why I/O sync may be bad, which is interesting. Then, another question naturally arises: why ControlNet-like feature addition (feedback augmentation) used in this work is effective? It is more interesting because the proposed method also does not guarantee a reduction of the gap in Eq. (7).

- Lines 286-288: The authors mentioned two ControlNets for superresolution and depth. Does it mean the authors use both ControlNet or is the depth ControlNet replaced with the super-resolution ControlNet? Then, how can we feed depth rendering to the superresolution ControlNet encoder without training?

- Line 287: Please provide the URL for the superresolution ControlNet as a footnote to give proper credit and to enhance the reproducibility. 

- Line 485 - "texture field optimization": What is texture field optimization referred to? Is the texture field optimization applicable to the other competing methods, TEXTure, Text2Tex, and SyncMVD, in Table 6? Was it applied to them already?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel plug-in module, 3D-Adapter, which enhances multi-view diffusion models to improve the quality of 3D geometry generation. By integrating 3D feedback augmentation, it infuses 3D geometry awareness into pretrained image diffusion models. The 3D-Adapter operates in two main variants: a fast feed-forward version and a flexible training-free version using neural fields and meshes. The proposed method addresses the limitations of previous two-stage approaches by maintaining the original network topology and augmenting the base model through feature addition. Extensive experiments show improvements across various tasks, including text-to-3D, image-to-3D, text-to-texture, and text-to-avatar generation.

### Strengths
1. The 3D feedback augmentation approach and the architecture's integration with diffusion models present a novel contribution that extends beyond typical 2D-to-3D adaptation techniques.
2. The figures effectively demonstrate the qualitative improvements of the proposed approach, particularly in challenging cases.
3. The broad applicability of 3D-Adapter to text-to-3D, image-to-3D, and text-to-texture tasks indicates potential for further research and practical applications.

### Weaknesses
1. **Claims About Existing Methods**: The assertion (L046-L053) that I/O sync methods degrade residual connections and cause texture quality issues is confusing and not adequately supported. More specific explanations with these methods are necessary. The claim that these methods disrupt residual connections is vague; it's unclear how operations like rendering and 3D reconstruction inherently interfere with the residual connections within a neural network's architecture. The paper needs to clarify the specific mechanisms by which these I/O sync methods are thought to degrade performance, perhaps by detailing how the backpropagation of gradients is affected by the insertion of these operations.
2. **Inadequate Definitions**: The paper lacks clarity on the a) components of the 3D-Adapter (I understand that it includes VAE Decoder, ControlNet, and 3D Reconstruction Model) and b) the “I/O sync” baselines compared in Fig.1. Explicitly listing the modules included and the compared methods or baseline settings would aid understanding. For the 3D-Adapter, a detailed breakdown of how each component contributes to the overall process is needed. For the baselines, the specific configurations and training procedures should be described to allow for a fair comparison.
3. **Comparison Gaps**: The image-to-3D generation experiments do not include comparisons with CRM[1], SV3D[2], InstantMesh[3]. The text-to-texture experiments do not include metrics like FID, KID or comparisons with some established methods such as Paint3D[4] and FlashTex[5]. The absence of these comparisons makes it difficult to assess the relative performance of the proposed method against state-of-the-art techniques. The paper should include a more comprehensive evaluation to demonstrate the advantages of the 3D-Adapter.
4. **Limitation Discussion**: Although the paper mentions the concerns about inference efficiency and shows the metric in the Appendix, more discussions about training efficiency would strengthen the paper, because it requires fine-tuning reconstruction model while keeping the multi-view diffusion model in memory. The paper should include a detailed analysis of the computational resources required for training, including memory usage and training time, to provide a complete picture of the method's practical limitations.
5. **Insufficient References and Discussion of Prior Work**: a) The paper lacks citations for relevant multi-view generation methods such as Free3D[6], EpiDiff[7], and SPAD[8]. b) Additionally, it does not discuss highly relevant works like IM3D[9] and Carve3D[10]. c) While Ouroboros3D[11] and Cycle3D[12] may be considered concurrent work, it would still be valuable to include a discussion, as there are differences between these methods and the 3D-Adapter that merit discussion.

### Questions
1. Could the authors elaborate on how 3D-Adapter's 3D feedback augmentation differs fundamentally from existing I/O sync techniques? Specifically, in the claim made around L051, the paper categorizes methods such as Nerfdiff, DMV3D, and VideoMV under synchronizing the denoised outputs, suggesting that these approaches disrupt residual connections and result in poor texture quality. This assertion is somewhat confusing and not evidently supported. For example, DMV3D uses a 3D reconstruction model as a multi-view denoiser, and VideoMV employs a stage-wise re-sampling strategy to fuse 3D reconstruction information. It is unclear how these methods would interfere with the residual connections in the network design. The claim requires further justification or supporting evidence to be convincing.
2. Additionally, it is recommended that the authors consider showing intermediate results during the denoising process, such as outputs from the 3D reconstruction model at various stages. This could help readers better understand the contributions of the proposed method.

### Soundness
3

### Presentation
2

### Contribution
3
