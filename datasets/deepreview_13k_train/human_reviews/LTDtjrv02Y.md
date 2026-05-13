# Bringing NeRFs to the Latent Space: Inverse Graphics Autoencoder

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
While pre-trained image autoencoders are increasingly utilized in computer vision, the application of inverse graphics in 2D latent spaces has been under-explored. 
Yet, besides reducing the training and rendering complexity, applying inverse graphics in the latent space enables a valuable interoperability with other latent-based 2D methods.
The major challenge is that inverse graphics cannot be directly applied to such image latent spaces because they lack an underlying 3D geometry. 
In this paper, we propose an Inverse Graphics Autoencoder (IG-AE) that specifically addresses this issue.
To this end, we regularize an image autoencoder with 3D-geometry by aligning its latent space with jointly trained latent 3D scenes. 
We utilize the trained IG-AE to bring NeRFs to the latent space with a latent NeRF training pipeline, which we implement in an open-source extension of the Nerfstudio framework, thereby unlocking latent scene learning for its supported methods. 
We experimentally confirm that Latent NeRFs trained with IG-AE present an improved quality compared to a standard autoencoder, all while exhibiting training and rendering accelerations with respect to NeRFs trained in the image space.
Our project page can be found at \url{https://ig-ae.io}\ .

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of 3D-awareness into the latent space of autoencoders, through learning a latent NeRF and an Inverse Graphics AutoEncoder (IG-AE). The proposed latent NeRF is general and can be used as standard extension to different previous NeRF architectures, with implementation code in the supplementary. The proposed IG-AE jointly train latent NeRFs and standard AE to achieve 3D awareness in latent space, on both synthetic and real data. The experimental comparisons and analysis are mostly thorough and comprehensive, while still with some issues in justifying its motivations.

### Strengths
1. 3D-awareness of 2D image generation from autoencoders is an important issue, and this paper seems to be the first work to address it.
2. The proposed latent NeRF operates fully within the latent space, which is a standardized solution and can work as an open-source extension to established NeRF architectures. The authors submitted the code in the supplementary.
3. The training framework of latent NeRF and IG-AE is sensible, with detailed ablation study to justify the loss design.
4. The paper is very well-written and easy to follow, with method design and experiments to support its motivation and arguments.

### Weaknesses
Although I agree with the importance of 3D-awareness of 2D autoencoders and appreciate the authors' efforts, I still have some concerns/questions for the proposed method to address 3D-awareness with latent NeRF:
1. Is a latent NeRF really necessary? Does it bring more advantage or more damage to the standard 2D AEs, especially when the scenes are quite complicated? Learning a scene with a NeRF model tends to smooth out high-frequency details (easier to be 3D-inconsistent), which is also true for TV loss as discussed in Line 363. Is it possible that the latent NeRF learning and TV loss would force the encoder to remove high-frequency contents during joint training, which can not be recovered by the decoder? One example is the cake in Figure 6, IG-AE is over-smoothed comparing to RGB. Could you conduct quantitative evaluation to show the level of loss in high frequencies? Specifically, a quantitative comparison of high-frequency content, such as through a spectral analysis or by measuring the high-frequency PSNR, would be beneficial to understand the trade-offs.
2. Additionally, if the intension is to bring 3D-awareness to 2D autoencoders, why not add NeRF constraints on the final RGB images instead of the latents? Maybe this would cause less information loss? Is it possible to compare the trade-off between using latent NeRF and NeRF in final RGB space? It's unclear why the latent space is the most appropriate place to enforce 3D consistency, and a comparison with direct RGB supervision would help justify this design choice. The authors should explore the potential benefits and drawbacks of each approach.
3. On the condition of the lost high-frequency details, is this level of "3D-awareness" still helpful for the 2D autoencoders? The encoding and decoding reconstruction on natural images by 2D encoders seems to be fine for now, as shown in Figure 9 and other literatures. The problem emerges when it comes to novel image generation rather than simple reconstruction, which is untouched in this paper. The paper needs to clarify how this 3D-awareness in the latent space translates to improvements in downstream tasks, especially generative tasks, beyond simple reconstruction.
4. The experiments seem to be limited to simple objects? The Objaverse and Shapenet objects should be much simpler than the original domain of the pre-trained "Ostris KL-f8-d16" VAE. Is it possible to show the performance on more complicated scenes with rich high-frequency details? The choice of datasets does not fully demonstrate the method's ability to handle complex real-world scenes, and experiments on more challenging datasets are needed to validate its robustness.
5. If the focus is to to improve standard 2D autoencoders then the comparisons to AE should be the reconstruction of multiview images? The current comparison only shows single-view reconstruction, which does not fully evaluate the 3D-awareness of the latent space. A more comprehensive evaluation should include multi-view reconstruction to demonstrate the 3D consistency of the learned representations.
6. If the justification is novel view synthesis, the baseline methods should be other (latent) NeRF methods instead of AE? Since AE itself is not for this task. Table 5 does show some advantages in training and rendering time, but with significant sacrifice on NVS performance. The paper should compare against state-of-the-art latent NeRF methods to properly assess its performance on novel view synthesis, rather than just comparing against a standard AE which is not designed for this task.

### Questions
1. Is there any convergence issue during IG-AE training? Do you simply jointly train all modules with all losses?
2. I haven't checked the computation of latent NeRF, so I'm not sure if there would be any problems.
3. Is this paper an improved version of the one in the supplementary? There seems to be quite some similarities.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper propose a two-stage pipeline to train a latent space which is suitable for fitting NeRFs. In the first stage, a set of latent tri-planes are individually trained for each scene in the training data. The latent tri-planes are fitted by minimizing both the volumetric rendering error in latent space and the pixel difference in RGB space through a image decoder. In the second stage, an autoencoder is trained on all scenes in the training data, jointly with all individual tri-planes. The fidelity of the autoencoder is additionally regularized by training on additional real images. Experiments demonstrated that the proposed latent space is able to fitting NeRFs better than a image-based latent space.

### Strengths
- The paper attempts to research on an important problem of 3D-aware latent spaces.

- The proposed method overall makes sense: the introduce of individually trained latent tri-planes provides a auxiliary variable which serves as a "3D-aware" guidance for auto-encoded latents. 

- Experiments show that the proposed IG-AE is better for training NeRFs than vanilla AE.

- The method can easily integrated into NeRFStudio with an open-source extension.

### Weaknesses
My majority concerns are as follows:

(1) While the proposed method is interesting and makes sense, the claimed property of "3D-aware" latent space cannot be fully justified from the given experiment results:
- (a) The proposed method is only tested on dataset with limited variations. For evaluation NeRFs, ShapeNet dataset is not a best choice as it contains simple shapes and textures without any non-Lambertian effects. Additionally, the test dataset contains only three categories for Shapenet and Objeverse dataset. Evaulations on more complicated dataset with non-lambertian effects, such as Realistic Synthetic 360 [1] would help to more thoroughly demonstrate the "3D-aware" property of the latent space across a wider range of scenarios and make the results more convincing. The ShapeNet dataset, with its simple geometric primitives and uniform textures, does not provide a sufficient challenge to validate the 3D consistency of the learned latent space. The lack of complex lighting effects and intricate surface details in ShapeNet makes it difficult to assess whether the proposed method truly captures 3D structure or simply learns to reproduce simple 2D patterns. The limited number of categories and objects within those categories further restricts the generalizability of the findings.
- (b) Even under the limited test dataset, the performance of the proposed method are not convincing enough. Despite the IG-AE outperforms the vanilla AE counterpart, the quality degrades significantly compares to the RGB version. This raises the question that whether the image fidelity is enough for the IG-AE. The significant performance gap between the proposed method and direct RGB-based NeRF training suggests that the latent space may not fully capture the information necessary for high-fidelity novel view synthesis. The observed degradation in quality, even when compared to a vanilla autoencoder, calls into question the effectiveness of the proposed 3D-aware latent space in preserving crucial details.
- (c) The "3D-aware" property cannot be easily judged from given metrics and results in the paper. All quantitative results are averaged across views - it is hard to know whether the "consistency" between different synthesized views are preserved. One suggestion would be using some perceptal metrics to evaluate the consistency between different generated view, e.g., the CLIP feature similarity used in [2] and [3]. There are also very few qualitative results provided. Providing more qualitative results such as videos showing a rotated object can be also useful to visualize the view consistency. The averaging of quantitative metrics across views obscures potential inconsistencies in the synthesized views. A more detailed analysis of view-specific performance is needed to assess the true 3D consistency of the latent space. The lack of qualitative results, such as videos demonstrating object rotation, makes it difficult to visually assess the view consistency and identify potential artifacts.
- (d) The effect of the original auto-encoder utilized for training IG-AE is not well explored. As discussed in Section 3.2 in [4], a latent space with low channel-wise depth (e.g., down to 4) and a slightly higher (but still significantly lower than RGB input resolution, 32 or 64 for example) will encourage local dependency over the autoencoder’s image and latent spaces. Under such circumstance, the latent representation is a near patch level representation of its corresponding RGB image, making it nearly equivariant to spatial transformations of the scene. In other words, it automatically (at least to some extent) has the property of "3D-aware" for training NeRFs. I would suggest the paper add more discussion and/or experiments regarding the 2D autoencoder used. The paper does not adequately explore the impact of the base autoencoder's architecture on the resulting 3D-aware latent space. Specifically, the effect of latent space dimensionality and channel depth on the emergence of 3D-aware properties is not investigated. The paper should include experiments that vary these parameters to determine their influence on the quality and consistency of the learned latent space.

(2) There has been many attempts for training NeRFs (or similar implicit 3D representations) in a space with reduced resolution, followed with upsampler operations in 2D space. For example:
- Rodin [5] first generates a low-resolution tri-planes with 3D aware convolutions and an upsampler. 
- StyleNeRF [6] generates a low-resolution latent features using NeRF and then upsample these features in 2D space with a StyleGAN-like structures.

None of these related methods are discussed and compared in this paper, making the judgement of "our approach is the first to propose a 3D-aware latent space" difficult. The suggestion would be add more discussion to clarify how the proposed approach differs from or improves upon these existing methods that used reduced resolution spaces for modeling NeRFs.

### Questions
(1) In the first stage each latent tri-plane is trained individually, hence each tri-plane will have its own finetuned version of the image decoder. In section 4.2, when jointly training the IG-AE with the latent triplanes, which initialization is used for the decoder for IG-AE?

(2) Regarding the experiment setup: how many held-out scenes in each category (Cake, Figurine and House) for the Objeverse dataset? Does the same category appears in the training data of IG-AE ?

(2) In Table 5, it is shown that the InstantNGP exhibits both longer training time and rendering time paired with IG-AE (including the RGB decoding time for IG-AE). Given that the quality under IG-AE has no advantages, what are the advantages for the proposed IG-AE method compared with directly training NeRF using InstantNGP?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an Inverse Graphics Autoencoder (IG-AE) to explore the potential of inverse graphics in 2D latent spaces, which is relatively underutilized in computer vision. The authors highlight that inverse graphics applied in latent spaces can reduce both training and rendering complexity while enabling compatibility with other 2D latent-based methods. A key challenge addressed is that traditional image latent spaces lack 3D geometry, preventing direct application of inverse graphics. IG-AE addresses this by aligning the latent space of an image autoencoder with jointly trained latent 3D scenes. This enables a "latent NeRF" training pipeline, implemented within the Nerfstudio framework, making latent scene learning accessible for methods supported by the framework. Experiments show that latent NeRFs trained with IG-AE offer improved quality compared to conventional autoencoders, while also providing faster training and rendering compared to NeRFs trained in image space.

### Strengths
1. **Novel Use of Inverse Graphics in Latent Space**: The authors claim that they are the first to explore this direction, which explores the relatively untapped area of applying inverse graphics in 2D latent spaces, which reduces training and rendering complexity and offers compatibility with other latent-based 2D methods.

2. **Integration of 3D Geometry into Latent Spaces**: The authors address the issue of the lack of 3D geometry in standard image latent spaces by regularizing the autoencoder with 3D information, aligning its latent space with jointly trained 3D scenes. This approach enhances the representation capability of latent spaces for 3D scene understanding. From many perspectives, these efforts will be meaningful in this area.

3. **Latent NeRF Training Pipeline**: Two new training pipelines are proposed. By creating a latent NeRF training pipeline and integrating it within the Nerfstudio framework, the paper unlocks efficient latent scene learning and makes it accessible to a broader set of methods, providing a practical tool for further research.

4. **Open-Source Contribution**: The open-source extension to the Nerfstudio framework adds value to the research community by facilitating reproducibility and further experimentation, and the proposed method can naturally work on any new NeRF representations.

### Weaknesses
1. **The writing is pretty hard to follow.** I tried to understand this paper by reading over and over again, but still find it very hard to follow. Since this direction is relatively new, I strongly suggest the author to revise the writing in the later version for clearer elaboration. Specifically, the paper lacks clear definitions of key terms and the relationships between different components of the proposed method are not well-explained. For example, the exact meaning of a "3D-aware latent space" is not clearly defined, and it's unclear how this space is different from a standard image latent space beyond the fact that it is aligned with 3D information. The paper would benefit from more precise language and a more detailed explanation of the core concepts.

2. **The motivation of the proposed method is unclear.** From my understanding, the proposed method try to align the NeRF rendering to a pretrained autoencoder (Ostris KL-f8-d16 VAE here), but what are the benefits of doing this? Though promising PSNR/LPIPS metrics are achieved as in Tab. 1 and Tab. 2, does the proposed IG-AE / AE supports zero-shot novel view synthesis on the imagenet dataset? Regarding Tab. 2, I don't quite understand how the author evaluate the novel view synthesis pipeline here, since no visual results are included in the main paper. All the visual results are just reconstructing the input view. The paper needs to clearly articulate the advantages of performing novel view synthesis in the latent space compared to directly in the image space. The current explanation is insufficient to justify the added complexity of the proposed approach. The evaluation protocol for novel view synthesis needs to be much more transparent, and the lack of visual results for novel views makes it hard to assess the practical value of this method.

3. **Lack of comparison with existing methods**. Though the author claims this idea is quite novel and they are among the first to propose this solution, many existing methods have already shown similar spirits, including 

* SRT: Scene Representation Transformer.
* NeRF-VAE: A Geometry Aware 3D Scene Generative Model
* LN3Diff: Scalable Latent Neural Fields Diffusion for Speedy 3D Generation

Their 3D (V)AE models support 3D view synthesis on the open vocabulary single-view inputs. The discussions / comparisons with these methods are needed to demonstrate the soundness of the proposed pipeline.

### Questions
1. In section 3, is the same VAE used as in section 4? The implementation details have not mentioned this.
2. How is the "3D aligned" auto-encoder useful in the downstream tasks?
3. In Tab. 2, how is the NVS task performed? Given a view as the input to your encoder, then synthesis novel views directly? Would you include more visual results?
4. In your AE/VAE design, the latent space is still a "3D-aware" image, so why not using a truly 3D-aware latent such as the latent triplane in LN3Diff / Direct3D?

### Soundness
2

### Presentation
2

### Contribution
2
