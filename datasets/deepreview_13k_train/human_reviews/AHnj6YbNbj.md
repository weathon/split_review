# Coordinate In and Value Out: Training Flow Transformers in Ambient Space

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Flow matching models have emerged as a powerful method for generative modeling on domains like images or videos, and even on unstructured data like 3D point clouds. These models are commonly trained in two stages: first, a data compressor (\ie a variational auto-encoder) is trained, and in a subsequent training stage a flow matching generative model is trained in the low-dimensional latent space of the data compressor. This two stage paradigm adds complexity to the overall training recipe and sets obstacles for unifying models across data domains, as specific data compressors are used for different data modalities. To this end, we introduce \textbf{Ambient Space Flow Transformers} (\model), a domain-agnostic approach to learn flow matching transformers in ambient space, sidestepping the requirement of training compressors and simplifying the training process. We introduce a conditionally independent point-wise training objective that enables {\model} to make predictions continuously in coordinate space. Our empirical results demonstrate that using general purpose transformer blocks, {\model} effectively handles different data modalities such as images and 3D point clouds, achieving strong performance in both domains and outperforming comparable approaches. {\model} is a promising step towards domain-agnostic flow matching generative models that can be trivially adopted in different data domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces an Ambient Space Flow Transformer (ASFT), a flow-matching generative model designed to operate directly in the ambient space. The core innovation lies in eliminating the practical complexities of training latent space generative models, such as the reliance on domain-specific compressors for different data domains or the tuning of data compressor hyperparameters (e.g., adversarial weights, KL terms). Moreover, experimental results on both image and point cloud domains demonstrate competitive performance.

### Strengths
This paper effectively tackles the challenge of simplifying the training process for flow matching models. The proposed method is innovative and well-supported by experiments conducted on diverse datasets, including images and point clouds. The clear presentation of the problem, method, and results makes the paper easy to follow.

### Weaknesses
The novelty of the proposed method in this paper is questionable, as it appears to be relatively straightforward. Additionally, the experimental results are not sufficiently compelling. The use of only the ShapeNet dataset for point cloud modality limits the generalizability of the findings. More diverse datasets should be employed to validate the effectiveness of the proposed approach. Furthermore, the improvement over existing methods is not substantial, and a more comprehensive comparison with state-of-the-art methods, using a wider range of metrics, is necessary. Lastly, the visualizations in Figures 1 and 2 are unclear and do not provide a satisfactory explanation of the proposed method.

### Questions
The following suggestions could enhance the paper: 1) Figures 1 and 2 should be refined to provide a clearer visualization of the proposed method; 2) The experimental evaluation could be strengthened by employing a more diverse range of image and point cloud datasets to demonstrate the generalizability of the proposed approach; 3) Incorporating additional novel ideas could further enhance the distinctiveness and advancement of the proposed method.

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
The paper presents Ambient Space Flow Transformer (ASFT), a flow matching generative model working with an implicit representation of the data (INR), instead of a latent one. A modified version of PerceiverIO used as a backbone allows both images and 3D point clouds to bo modeled without any design changes.

### Strengths
1. The novelty is good - single stage generation via flow matching on function space without any pretrained encoder-decoder models.
2. On images, ASFT beats function space approaches on FID.
3. On 3D point clouds, the method is better or on par with other models.
4. Due to the independence of the input coordinates, the model allows sub-sampling of point clouds and super-resolution of images.
5. The writing is very good. The information flow is maintained and all of the ideas are clearly explained.

### Weaknesses
1. The image results presented are in low resolution only - 128x128 and 256x256. The use of such low resolutions makes it difficult to assess the practical applicability of the method. Specifically, the 128x128 results are not a strong indicator of the model's potential, and the 256x256 results, while better, still lag behind many existing baselines, especially those utilizing domain-specific architectures and pre-trained models. This raises concerns about the model's ability to scale to more practical, high-resolution scenarios.
2. The overall image results are not very convincing - 128x128 images are not a solid proof for superiority of the model. Meanwhile, results on 256x256 are worse than many baselines (even though domain-specific and using pretrained models). The performance gap at 256x256, despite the model's domain-agnostic approach, is a significant weakness. The lack of competitive results at this resolution undermines the claim of the model's effectiveness, especially when compared to methods that leverage pre-training and domain-specific inductive biases.


### Questions
1. Why is the unified representation important? From the practical point of view, it doesn't make that much of a difference to have two domain-specific backbones instead of a shared one (at least for images and point clouds). If we sacrifice the unification, is there any better backbone choice, especially for images that would result in better results and/or scalability?
2. The model is shown only for images and 3D point clouds. What about other modalities? Are there any additional challenges?
3. Does the image model scale to higher resolutions?
4. Figure 2 may suggest both image and 3D coordinates are passed to the network at the same time. The authors should consider clearly separating them in the figure and updating the caption to highlight this.
5. In Figure 3 (b) color palette is hard to read - the differences should be more visible.
6. It would be interesting to see a comparison with standard image upscaling in Figure 4 (a).
7. In introduction, citations for VAE, VQVAE, VQGAN, transformers, PointNet, UNet are missing.
8. "UNet" and "U-Net" used - please pick one.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces **Ambient Space Flow Transformers (ASFT)** as a novel approach to generative modeling that simplifies the training process by eliminating the need for latent space data compressors. ASFT works directly in the ambient space (i.e., the original data domain), aiming to be a domain-agnostic model applicable across different types of data, such as images and 3D point clouds.

### Strengths
- **Simplicity and Efficiency**: ASFT's single-stage training process is simpler than traditional two-stage models, making it easier to implement and tune.
- **Versatility**: It is designed to work across multiple data types without modifications, unlike models that require domain-specific architectures.
- **Resolution Scalability**: The ability to generate high-resolution outputs from lower-resolution training data provides flexibility and potential computational savings.
- **Competitive Results**: Despite its simplicity, ASFT achieves strong performance metrics comparable to state-of-the-art models across images and point clouds.

### Weaknesses
 - **Potential for Lower Fidelity in Complex Domains**: ASFT may not match latent space models in specific metrics, such as Fréchet Inception Distance (FID), particularly when latent space models are pre-trained on extensive datasets. This is a significant concern, as FID is a widely accepted metric for evaluating generative model quality, and a lower FID score often indicates better perceptual quality. The paper should more thoroughly investigate the specific types of complex data where ASFT underperforms and provide a more detailed analysis of the reasons for this discrepancy.
- **Dependence on Model Size for Best Results**: The model's performance improves significantly with scale, which may lead to high computational costs for larger ASFT versions, particularly in comparison with models leveraging pre-trained compressors. This dependence on model size raises questions about the practical applicability of ASFT in resource-constrained environments. The paper needs to explore the trade-offs between model size, computational cost, and performance more rigorously, and perhaps investigate techniques to improve efficiency without sacrificing quality.
- **Challenges with High Dimensional Data**: For very high-resolution applications, ASFT’s point-wise approach might face optimization difficulties due to the increased complexity in decoding large numbers of coordinate-value pairs. The paper does not explore the limitations of this approach in detail, particularly how the computational cost scales with increasing dimensionality and resolution. The paper should also investigate the potential for optimization issues, such as vanishing gradients or slow convergence, when dealing with very high-dimensional data.

### Questions
Despite it is a domain-agnostic model, are there any possible way to include domain-specific knowledges to further boost the quality?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper claims that building latent-space diffusion models have several shortcomings such as non-end-to-end optimization and the requirement of domain-specific compression (e.g., VAE) models, and thus designs an ambient-space flow transformer (ASFT) architecture for generative tasks.

### Strengths
1. The analyses of the potential shortcomings of existing latent diffusion models are presented. Based on the motivations, this paper constructs a single-stage learning model, 
2. Learning over coordinate-value pairs facilitates data-agostic processing. In this way, an image is actually treated as a "colored point cloud".

### Weaknesses
1. Although the authors analyzed some aspects of potential drawbacks of latent-space diffusion models, it is hard to be convinced that ambient-space (e.g., pixel-space, point-space) learning is a more promising direction: 
-- First, I don't think training domain-specific data compressors is a cumbersome practice that should be criticized. When some powerful VAEs are already trained and released, the community can directly use them. There aren't that many types of data modalities. Building compressors for each type of data (e.g., image, video, point cloud, mesh) is totally acceptable.
-- Second, the current mainstream practice is to separately train the data compressor and the subsequent latent diffusion model, but it does not mean that such training workflow cannot be made end-to-end. We can't say it is a drawback just because we haven't explored it. Generative models evolve so fast. I think making it end-to-end is not impossible.
-- Third, anyway, for now the great success of various latent diffusion models seems to demonstrate the superiority of learning in the latent space instead of the ambient space.

2. Building generative models with coordinate-value pairs may essentially restrict its application scenarios and conditional generation capabilities. For 3D generation, point cloud is apparently not the final choice. What we want is the continuous surface, together with textures. Existing 3D generative models either use meshes or implicit fields. However, the proposed method faces difficulties in generating such data. Besides, I notice that the proposed method is only implemented with class label conditioned generation, which is quite out-of-date. Its conditional generation capabilities (e.g., text-guided, image-guided) are questionable. 

3. The experimental settings are not very persuasive. For image generation, the model is trained on ImageNet. For point cloud generation, the model is trained on ShapeNet. The experimental results cannot demonstrate the potential of the proposed method for learning from larger-scale high-quality data, such as LAION and Objaverse datasets. It can be observed that the diversity and quality of the generated images obviously cannot catch up the current state-of-the-art latent image diffusion models. The generated point clouds are also noisy and lack details, especially when compared with state-of-the-art 3D native diffusion models (like CLAY).

### Questions
1. Does the proposed generation framework support more practical conditioning mechanism (e.g., guided by text or single image)?
2. Can the proposed learning model be scaled up using larger-scale high-quality datasets such as LAION and Objaverse?
3. The authors are suggested to provide further explanations about how the latent variable z_{f_t} for context encoding is obtained.

### Soundness
2

### Presentation
2

### Contribution
2
