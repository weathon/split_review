# RelitLRM: Generative Relightable Radiance for Large Reconstruction Models

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
We propose RelitLRM, a Large Reconstruction Model (LRM) for generating high-quality Gaussian splatting representations of 3D objects under novel illuminations from sparse (4-8) posed images captured under unknown static lighting. Unlike prior inverse rendering methods requiring dense captures and slow optimization, often causing artifacts like incorrect highlights or shadow baking, RelitLRM adopts a feed-forward transformer-based model with a novel combination of a geometry reconstructor and a relightable appearance generator based on diffusion. The model is trained end-to-end on synthetic multi-view renderings of objects under varying known illuminations. This architecture design enables to effectively decompose geometry and appearance, resolve the ambiguity between material and lighting, and capture the multi-modal distribution of shadows and specularity in the relit appearance. We show our sparse-view feed-forward RelitLRM offers competitive relighting results to state-of-the-art dense-view optimization-based baselines while being significantly faster. Our project page is available at: https://relitlrm.github.io/.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a method to generate a relighable 3D representation using 3DGS for the geometry and a diffusion based model to get the illumination dependent appearance parameters for those Gaussians.
The geometry is predicted in form of per pixel Gaussians from the sparse input views (4 - 16) in a single Transformer forward step. The tokens of the geometric representation is concatenated with HDR features extracted from the illumination given as environment map and the noise target views. After denoising the tokens for everything except the input gaussians are discarded. The remaining tokens are decoded into the appearance (SH) of the Gaussians. The Gaussians are then rasterized into any novel view. The diffusion model is trained such that the lighting of the rendered Gaussians should match the lighting of the input environment map. During inference this environment map and the target view camera pose can be arbitrarily be chosen, thus a scene can be reconstructed from sparse views and then relit.

### Strengths
* Pseudocode in A.1clarifies all misunderstandings from the text descriptions. I can not stress enough how much I like this way of communicating the pipeline.
* The approach uses a diffusion process instead of a multi-view optimization, which is exceptionally fast in direct comparison.
* Trained on a rich dataset with a huge variety of lighting conditions.
* Light representation (input) is a simple environment map. Changing lighting is therefore very simple (no complicated neural light representation)

### Weaknesses
 * Knowing only even a fraction of the research and work that has gone into disentangling the ambiguity between lighting and shading it rubs me the wrong way to read something that suggests it solved it without actually addressing the core problem. The method does not really decompose a scene into geometry, lighting and shading and is not usable if the use case would require extracting or editing reflectance properties. The way I see it this paper does relighting by decomposing a scene into geometry and appearance, however this is very different to what methods which explicitly extract reflectance and illumination do. The problem statement is profoundly different if you have to produce a explicit, reflectance representation which represents some underlying physical property of the surface, compared to just estimating the product of light and reflectance. I don't think much has to be changed to show respect for this difference: In 2.1 it should be mentioned that the method models the appearance under arbitrary illumination without an explicit reflectance representation. In the introduction the claim that the ambiguity between shading and lighting, is overcome should be phrased more carefully or be clarified. As far as I understand this paper estimates appearance as the integrated product between the unknown shading and a given lighting in form of a view dependent SH. This is really great work, but should not be confused with reflectance decomposition.


### Questions
* In the tables with the numbers for metrics please highlight the best numbers (bold)
* What hardware was used for training the model? Training time, memory requirements. Add to A.4
* In theory the method should work for objects that traditionally have challenging reflectance properties such as hair or fur. I am not sure if hair and fur were part of the training dataset, but it still might be interesting to see if it works.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper tackles the task of reconstructing relightable 3D objects from sparse images. For this, the authors extend the idea of GS-LRM to incorporate the generation of a relightable appearance. Specifically, they feed the geometry feature from GS-LRM through a diffusion process based on the transformer architecture. The transformer attends to the target illumination and outputs appearance tokens. The combination of the appearance tokens from the newly added transformer and the geometry tokens from the original GS-LRM transformer concludes the generation of Gaussian Splats. Experiments on the Stanford-ORB and Objects-with-Lighting real-world benchmark as well as the TensoIR synthetic benchmark demonstrate the effectiveness of the proposed approach.

### Strengths
- originality-wise: I appreciate the proposed end-to-end transformer-based architecture for relightable 3D object reconstruction. 
- quality-wise: when taking into the efficiency of the proposed approach, I think quantitatively the performance is good.
- clarity-wise: the paper is well-written and easy to follow.
- significance-wise: the task of relightable 3D object reconstruction is vital for many downstream applications, e.g., AR/VR and robotics.

### Weaknesses
## Concerns about the architecture

I think the authors missed an important question to answer: why do we choose the current architecture? Essentially, the mechanism of discarding many tokens (L231) is wasting the model's capability. Specifically, after the final transformer block, tokens corresponding to the environment maps and noisy image patches are discarded, keeping only the appearance tokens. While the transformer processes all tokens, the discarding operation raises questions about the necessity of processing these discarded tokens, and whether a more efficient architecture could be designed. The root question is why do we need to use self-attention instead of cross-attention? Why do the environment maps and the denoised images need to be treated the same as the appearance tokens, especially since only the appearance tokens will be used for the Gaussian Splats rendering? The use of self-attention across all modalities, instead of a more targeted cross-attention between appearance tokens and environment maps, seems like an inefficient use of the model's capacity, potentially limiting the feature extraction capabilities for environment maps.

## Not enough understanding of the current model

Even though with the current architecture, I do not think the authors provide enough analysis. Specifically, have the authors visualized the attention maps of the transformer? What does the transformer learn? Does it attend to some specific areas in the environment map that cause the specular effects in the rendering? How does the transformer attend to those denoised images? Without visualizing and analyzing the attention maps, it is difficult to understand the model's internal mechanisms and how it achieves relighting. The lack of analysis on how the transformer processes different modalities and their contribution to the final rendering is a significant weakness.

## Concerns about the qualitative results

In Fig. 3.(a), the produced Pepsi can's color is quite different from the ground truth. A similar thing happens to the gnome's colors. Further, the characters on the Pepsi can are quite blurry compared to NVDiffRec-MC / ground-truth. Additionally, in Fig. 3.(c), the RelitLRM produces quite different shows from the ground truth. However, the shadows are correctly predicted by both InvRender and TensoIR. The color discrepancies and blurriness in the Pepsi can, and the inaccurate shadows in the Lego and hotdog examples, suggest that the model struggles with fine details and accurate shadow casting. The differences in shadow quality compared to methods like TensoIR, which explicitly model shadows, highlight a potential limitation of the proposed approach. Why is this the case? Have the authors carefully studied the causes? Whether increasing the number of views will help? Will 16 views mitigate these issues as the authors state that "performance saturates around 16 views" (L525)? If even 16 views cannot resolve the issue, what are the intrinsic shortcomings of the proposed model?

I hope the authors can provide a systematic analysis for a good understanding of the model.

## Missed important baselines

I think the authors missed several quite related as well as important baselines, e.g., [a, b]. They both use the idea of diffusion-based relighting model to tackle the task of relightable reconstruction.

Especially IllumiNeRF [b], which directly tackles the task of relightable object reconstruction and competes on the benchmark of Stanford-ORB and TensoIR. Frankly speaking, [b] outperforms the proposed approach on both benchmarks quantitatively:
- PSNR-H / PSNR-L / SSIM / LPIPS: 24.67 / 31.52 / 0.969 / 0.032 (RelitLRM) vs 25.42 / 32.62 / 0.976 / 0.027 ([b] on Stanford-ORB)
- PSNR / SSIM / LPIPS: 29.05 / 0.936 / 0.082 (RelitLRM)) vs 29.709 / 0.947 / 0.072 ([b] on TensoIR)

[a] A Diffusion Approach to Radiance Field Relighting using Multi-Illumination Synthesis. EGSR 2024.

[b] IllumiNeRF: 3D Relighting without Inverse Rendering. ArXiv 2024.

## Concerns about the novelty claim

On L088, the authors claim the first contribution as "a regression-based geometry reconstructor followed by a diffusion-based appearance synthesizer". Though I appreciate the end-to-end transformer architecture, I may not be convinced that the idea is entirely novel since the above-mentioned IllumiNeRF has already proposed an almost exact idea. I would recommend modifying it to correctly position the work.

## Missed training details

What is the hardware setup required to train the model? How long does it take to complete the training, hours or days?

## Incorrect description about the benchmark

In L356, the authors state that the Stanford-ORB benchmark has "60 training views and 10 test views per lighting setup". This is not true. Please correct it.

## Typos

L290: "is involves" -> "involves"

### Questions
See "weakness".

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method trained end-to-end on synthetic multi-view renderings of objects under varied, known illuminations. The approach is able to generate high-quality Gaussian splatting representations of 3D objects under novel illuminations from sparse input images (4-8 views) captured in unknown, static lighting conditions.

### Strengths
- The method models geometry and rendering independently, akin to NeRF’s modeling architecture. It first constructs geometry from multi-view images, then generates the rendering by combining geometry features with environmental maps.
- The method is practical as it only requires 4-8 views as input. It is able to effectively reconstruct relightable objects without per-scene optimization.
- On both synthetic and real-world datasets, the method offers competitive relighting results, requiring much fewer input views than other methods.

### Weaknesses
 - In the paper, the authors claim that performance plateaus at around 16 views. However, as shown in Table 5, there is only a marginal improvement in image quality on the TensoIR-Synthetic dataset when increasing from 8 views to 16 views. The lack of substantial improvement with increased views suggests a potential bottleneck in the model's ability to effectively utilize additional information, possibly due to limitations in the attention mechanism or the method for merging per-view 3D Gaussians.
- The novelty of the approach needs clearer articulation. The authors state that their method differs from Neural Gaffer (Jin et al., 2024) by not being limited to single-view inputs. However, this advantage seems to stem from the use of GS-LRM (Zhang et al., 2024a). It is important to clarify how their application of diffusion for relighting distinguishes their method from existing techniques. The paper needs to more clearly articulate how the diffusion process is integrated into the Gaussian splatting framework and how it contributes to the relighting capabilities beyond what can be achieved by directly predicting relit Gaussians. The specific design choices in the diffusion model, such as the architecture and the noise schedule, and their impact on the final relighting quality should be discussed in more detail.
- This method separates geometry from rendering, but the paper does not show results of the decomposed geometry. It is unclear how good or bad the quality of the reconstructed geometries is. The absence of a quantitative evaluation of the reconstructed geometry makes it difficult to assess the quality of the geometric representation and its impact on the relighting performance. It is important to understand if the geometry is accurately reconstructed, or if the good relighting performance is achieved through compensating errors in the rendering stage.

### Questions
- In the paper, the authors provide the rendering performance. However, I cannot find the training time. Please provide more specifics on the training setup, such as the number of GPUs used and total training hours. 
- A more thorough analyais and discussion of why performance plateaus between 8 to 16 views would enhance the paper's quality.
- Please provide quantitative evaluations of the extracted geometries.
- In the object insertion image (Figure 1(c)), how is illumination in the scene accounted for? Did you sample on the position of the object to capture the surrounding environment and incorporate the environment map into your model? Additionally, how do you account for the indirect light from another object produced by your RelitLRM in the scene?
- The method still takes 2 to 3 seconds to render. In contrast, the geometry and textures obtained from other methods can be rendered using many real-time rendering techniques. Moreover, in current industrial applications, it is challenging to abandon triangle meshes and textures. Therefore, this method cannot be considered a viable solution for 3D digital assets. However, if this approach could be extended to scene relighting, its applicability could be significantly broadened.
- Is the number of Gaussians predicted by the model sufficient for capturing different topologies and structures across diverse objects?

### Soundness
3

### Presentation
3

### Contribution
2
