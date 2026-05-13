# Progressive Multi-scale Triplane Network for Text-to-3D Generation

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
The challenge of text-to-3D generation lies in accurately and efficiently crafting 3D objects based on natural language descriptions, a capability that promises substantial reduction in manual design efforts and offers an intuitive interface for user interaction with digital environments. Despite recent advancements, effective recovery of fine-grained details and efficient optimization of high-resolution 3D outputs remain critical hurdles. Drawing inspiration from the efficacious paradigm of progressive learning, we present a novel Multi-scale Triplane Network (MTN) architecture coupled with a tailored progressive learning strategy. As the name implies, the Multi-scale Triplane Network consists of four triplanes transitioning from low to high resolution. This hierarchical structure allows the low-resolution triplane to serve as an initial shape for the high-resolution counterparts, easing the inherent complexity of the optimization process. Furthermore, we introduce the progressive learning scheme that systematically guides the network to shift its attention from prominent coarse-grained structures to intricate fine-grained patterns. This strategic progression ensures that the focus of the model evolves towards emulating the subtlest aspects of the described 3D object. Our experiment verifies that the proposed method performs favorably against contemporary methods. Even for the complex and nuanced textual descriptions, our method consistently excels, delivering robust and viable 3D shapes where other methods falter.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a multiscale triplane architecture for coarse-to-fine SDS text-to-3D generation. SDS losses are applied at each scale of the network, with the triplane’s resolution varying at different scales. During training, a specific time-step sampling and reduction of camera radius are used to help generate high-frequency details.

### Strengths
1.	The paper presents a multiscale coarse-to-fine triplane architecture for SDS optimization. The coarse-to-fine design is reasonable.

### Weaknesses
1.	The baseline comparison is not convincing enough. Using MVDream with the SDS method could yield much better results. It's much more robust and achieve better results compared to the current baseline (stable-dreamfusion). MVdream-SDS could be added to the Table 1 with the R-Precision.   
2.	The texture frequency of the shape still appears insufficient sometimes. In Figure 7, the results seem to exhibit higher texture frequency; however, in Figure 2, many shapes still appear blurry, with some having very uniform color (motorcycle and the train, and the body of the corgi and bunny). Any idea why this the difference of quality is this large?

### Questions
1.	If you render the shape from the triplane at different scales, what do they look like? Is the model truly able to disentangle different structural scales into separate triplanes? It may provide more insight if you could visualize the shape at different scales.
2.	Currently, the highest resolution is 512. Could you scale it further to 1024?
3.	What is the resolution of the rendered image at each scale?

### Soundness
2

### Presentation
2

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
The paper introduces the Progressive Multi-Scale Triplane Network (MTN) for text-to-3D generation, a method designed to improve the efficiency and detail quality of 3D objects derived from text descriptions. The MTN operates using a multi-scale triplane network with four hierarchical triplanes progressing from low to high resolution, enabling the model to progressively refine from global to fine details. Additionally, a progressive learning strategy is applied, where both camera radius and time step in the diffusion process adjust dynamically to shift focus from broad structures to intricate details. The approach aims to address the challenges of high-resolution optimization and fine-grained details in 3D object generation. Experimental results indicate that MTN achieves better text alignment, texture quality, and shape precision compared to existing models like Latent-NeRF and DreamGaussian.

### Strengths
1.MTN's multi-scale triplane architecture enables efficient generation by progressing from low to high resolutions. This structured approach improves global coherence and local detail quality in the final output, allowing it to achieve a high degree of alignment with textual prompts.

2.The model’s progressively reducing camera radius and time step enables it to refine details incrementally, addressing a common limitation in text-to-3D generation where models often struggle with balancing global structure and fine-grained textures.

### Weaknesses
1. Omission of LucidDreamer and Similar Works: The paper does not consider LucidDreamer (CVPR 2024) in its evaluations, a notable omission given that LucidDreamer also applies SDS-based multi-view generation with a focus on geometry extraction. Including LucidDreamer would provide a more complete and comparative assessment of MTN’s effectiveness in capturing fine details. Furthermore, the paper lacks a discussion of other recent multi-view diffusion-based methods that also aim to improve 3D generation quality, which limits the scope of the comparison and the understanding of MTN's relative advantages and disadvantages.

2. The claim of not using 3DGS as a representation sounds weird. The authors mentioned, " Though faster, these approaches often 
 compromise the high-quality characteristic of NeRF-based methods and require post-processing to  convert Gaussian representations into NeRF or meshes, adding computational overhead." However, triplane representation also needs to be converted to mesh if someone wants to use it as an explicit 3D model. Also, 3DGS-based methods are 10x faster than MTN, which is clearly greater than the time required to convert 3DGS into a mesh (if you use marching-cube as the converting algorithm). The argument about computational overhead is misleading since any explicit 3D representation requires a conversion step for mesh extraction, and the speed difference between 3DGS and MTN is substantial enough to outweigh the conversion cost. The authors should provide a more nuanced comparison of the trade-offs between speed and quality.

3. In Figure 4, the third case contains a weird prompt "zoomed out DSLR photo". Since the input prompt only controls the rendered image but not the camera position itself, your result shows a smaller pancake pile and a smaller rabbit, which means your result is physically smaller. I think this is a little weird. This result implicitly implies that the generated objects might differ in terms of the object size, and this would hinder the practicability of this work since one will always need to check if your result needs to be resized, while other methods generally generate objects with the same size. The fact that the generated object's size is influenced by the rendering prompt raises concerns about the consistency and reliability of the method for practical applications where object size should be independent of rendering parameters.

### Questions
1. Please address the issue mentioned in the weakness part.
2. Why did the results of DreamGaussian look much worse than the results in their paper and project page? Is there any specific reason?
3. Why are there no limitations to this work discussed?

### Soundness
3

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
5

### Summary
In this work, the authors propose a text-to-3D generation method based on Score Distillation Sampling (SDS). Their key contribution is leveraging a multi-scale triplane representation, which is progressively upsampled during the optimization process. They also introduce a progressive learning scheme that samples different diffusion time steps across training iterations. The authors claim their proposed framework achieves favorable performance compared to existing methods.

### Strengths
- The experimental results (both quantitative and qualitative comparisons) demonstrate that the proposed framework achieves comparable, and in some cases slightly better, performance than Latent-NerF, Stable-Dreamfusion, and DreamGaussian.
- The ablation studies highlight the effectiveness of various components in this work, including the multi-scale triplane network (MTN) and the progressive training schemes.

### Weaknesses
Despite the paper's contributions, several weaknesses and concerns remain:

- Limited Technical Novelty:
    - Multi-scale representation in 3D generation is already well-explored:
        - XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies. CVPR 2024.
        - Locally Attentional SDF Diffusion for Controllable 3D Shape Generation. SIGGRAPH 2023.
    - Two-stage optimization for SDS-based 3D generation was previously explored in:
        - Magic3D: High-Resolution Text-to-3D Content Creation. CVPR 2023.
    - Given these existing works, the multi-scale representation approach does not appear to be a significant contribution. Moreover, these works are not sufficiently discussed in the manuscript. The use of a triplane representation, while effective, is not novel in itself, and the specific hierarchical structure needs more justification beyond simply stating it addresses texture and geometry issues. The paper lacks a detailed analysis of how the proposed multi-scale triplane network (MTN) specifically overcomes the limitations of existing multi-scale approaches, such as those using sparse voxel hierarchies or attention-based SDFs. The claimed benefits of progressive optimization are not sufficiently supported by a rigorous comparison to alternative optimization strategies.
    - The progressive learning scheme, explored in Dreamtime [ICLR 2024], lacks novelty. The combination of adaptive time-step reduction with progressive camera radius adjustment, while potentially beneficial, is not presented with sufficient technical depth to demonstrate a clear advancement over existing progressive learning methods. The specific implementation details of how these adjustments are made and their impact on the final 3D generation quality are not thoroughly analyzed.
- Inadequate Comparisons:
    - The evaluation omits important baselines, including some cited in the related work section. High-quality 3D generation frameworks like Fantasia3D and MVDream are not compared. This omission weakens the claim that the proposed framework achieves favorable performance compared to existing works. The lack of comparison with these state-of-the-art methods makes it difficult to assess the true contribution of the proposed approach. The paper should include a more comprehensive evaluation against a wider range of baselines to provide a more robust assessment of its performance.
    - The comparison with ProlificDreamer is only qualitative, and the difference seems minimal. Including evaluation metrics as in Figure 5 and Table 1 is necessary to support the claim. The qualitative comparisons are not sufficient to demonstrate a clear advantage over ProlificDreamer. The paper needs to include quantitative metrics to substantiate the claim of comparable or superior performance. Without these metrics, the comparison is subjective and lacks the necessary rigor to support the authors' claims.

- Unclear Ablation Setting:
    - The resolution of the triplane used in a single triplane is not specified. The number of iterations for training the single triplane network is also unclear.
    - Without this information, it is difficult to assess whether the current ablation adequately validates the effectiveness of the modules. It is recommended to clarify these settings.

### Questions
- Unclear Ablation Setting:
    - The resolution of the triplane used in a single triplane is not specified. The number of iterations for training the single triplane network is also unclear.
    - Without this information, it is difficult to assess whether the current ablation adequately validates the effectiveness of the modules. It is recommended to clarify these settings.

Overall, this work presents a new text-to-3D generative framework using Score Distillation Sampling. While the proposed framework achieves comparable, and in some cases better, performance compared to certain baselines, the novelty of employing multi-scale representations appears limited. Furthermore, the experimental results are insufficient to fully support the current claims, and some important settings are not clearly described. Given these concerns, I am inclined to recommend rejection of this work.

### Soundness
2

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
3

### Summary
This paper introduces a Multi-scale Triplane Network coupled with a progressive learning strategy to generate 3D objects with fine-grained details that align with input text. The generated 3D objects are suitable for 3D printing with minimal additional post-processing.

### Strengths
1. The generated meshes are suitable for 3D printing, as shown in Figure 9.

2. The progressive learning strategy can be generalized to other SDS-based text-to-3D generation models. In SDS-based methods, it is a common phenomenon that 3D objects generated with a closer camera radius exhibit more fine-grained but less plausible overall geometry, whereas a larger camera radius results in the opposite.

### Weaknesses
1. The results presented in Figure 2 are not satisfactory. For example, the "corgi" lacks fine-grained texture.

2. Figure 4 lacks comparisons with more recent works, such as GSGEN [1]. The DreamGaussian model performs poorly in text-to-3D tasks, making it an unsuitable baseline. The performance of ProlificDreamer in Figure 4 appears inferior to that reported in the original paper.

3. The paper lacks references to other related works on Triplane-based 3D generation.

### Questions
1. In Figure 2, are there results with more realistic color for "motorcycle" and "a cake in the shape of a train"? What specifically does "automatic color rendering is applied when a common color is applicable for such a category" mean?

2. Why is random sampling timestep applied at the end of training? The claim that "It reintroduces randomness to maintain the vibrancy of the coloration of the 3D model" needs supporting evidence. Please provide specific examples or experimental results.

### Soundness
2

### Presentation
2

### Contribution
3
