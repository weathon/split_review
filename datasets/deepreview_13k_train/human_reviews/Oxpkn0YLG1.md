# GTR: Improving Large 3D Reconstruction Models through Geometry and Texture Refinement

- Decision: Accept
- Scores: 5, 5, 6, 6, 6

## Abstract
\label{sec:abs}

We propose a novel approach for 3D mesh reconstruction from multi-view images. Our method takes inspiration from large reconstruction models like LRM~\cite{lrm} that use a transformer-based triplane generator and a Neural Radiance Field (NeRF) model trained on multi-view images. However, in our method, we introduce several important modifications that allow us to significantly enhance 3D reconstruction quality. First of all, we examine the original LRM architecture and find several shortcomings. Subsequently, we introduce corresponding modifications to the LRM architecture, which lead to improved multi-view image representation and more computationally efficient training.
Second, in order to improve geometry reconstruction and enable supervision at full image resolution, we extract meshes from the NeRF field in a differentiable manner and fine-tune the NeRF model through mesh rendering. These modifications allow us to achieve state-of-the-art performance on both 2D and 3D evaluation metrics, such as a PSNR of 28.67 on the Google Scanned Objects (GSO) dataset.
Despite these superior results, our feed-forward model still struggles to reconstruct complex textures, such as text and portraits on assets. To address this, we introduce a lightweight per-instance texture refinement procedure. This procedure fine-tunes the triplane representation and the NeRF's color estimation model on the mesh surface using the input multi-view images in just 4 seconds. This refinement improves the PSNR to 29.79 and achieves faithful reconstruction of complex textures, such as text. Additionally, our approach enables various downstream applications, including text/image-to-3D generation.  Our project website is at 
\url{https://snap-research.io/GTR/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents GTR, a model for improved 3D mesh reconstruction from multi-view images, which refines both geometry and texture to achieve state-of-the-art quality. It first finds several shortcomings of previous large reconstruction models (LRM) and introduces respective modifications to the LRM architecture, achieving improved quality and more efficient training. The modifications include using a new convolution encoder to replace the DiNO ViT used by previous work, replacing the deconvolution upsampling with a linear layer
followed by a pixelshuffle, etc. Additionally, it presents an efficient per-instance texture refinement process, leveraging input images to
enhance texture details. GTR significantly outperforms baseline models on datasets like GSO and OmniObject3D, supporting downstream tasks such as text/image-to-3D generation.

### Strengths
1. Rapid Texture Refinement: The per-object texture refinement is lightweight and achieves faithful texture reconstruction requiring a mere 4 seconds on an A100 GPU. 

2. Architecture Modifications: By replacing the DINO ViT transformer with a convolutional encoder and deconvolution layers with a linear layer followed by a pixelshuffle, GTR reduces artifacts of results and enhances high-frequency detail. These changes improve both the visual quality and efficiency of the model training. 

3. GTR achieves better results on major 3D reconstruction benchmarks including GSO and OmniObject3D datasets, showing clear quantitative and qualitative improvements over baseline models in 2D and 3D evaluation metrics.

### Weaknesses
1. Missing baseline: The paper does not compare with some stronger baselines, such as Mesh-LRM, which has released an online demo from its first author before the ICLR submission deadline. The lack of comparison with the Mesh-LRM demo is a significant oversight, as it represents a readily available and relevant benchmark. The authors should have included a direct comparison using the demo's outputs to properly contextualize their method's performance.

2. The mesh quality is not satisfactory. In the abstract, the authors said this approach was for "3D mesh reconstruction". However, according to the videos in the supplementary, the video quality is not satisfactory. The surfaces have a lot of bumpy and grid-like artifacts. These artifacts are not minor and appear consistently across different examples, indicating a fundamental limitation in the mesh generation process. The presence of these artifacts significantly detracts from the overall quality of the reconstructed 3D models.

3. The overall novelty is limited. The texture refinement part is not very attractive and has been explored in many other related 3D generation works, such as One-2-3-45++, Mesh-LRM, etc. The authors put forward some modifications to the original LRM in this paper.  The original team for the LRM paper has also released several follow-ups for the original LRM, including Mesh-LRM and GS-LRM. Mesh-LRN has shown better results than this work and its modifications seem simpler Therefore, the effectiveness of the proposed modifications should be compared with Mesh LRM's modification. Specifically, the single-layer convolutional encoder used in this work appears functionally similar to the "Patchify & Linear" operation described in Mesh-LRM, which raises questions about the novelty of this architectural choice. A more detailed comparison, including ablation studies, is needed to justify this modification.

### Questions
1. Please compare with Mesh-LRM

2. Considering Mesh-LRM has shown better results, I am curious about the actual effectiveness of this method's modifications to the original LRM, compared with Mesh-LRM's.
For example, Mesh-LRM replaces DINO ViT with a simple patchify operation; it uses simple "Linear &  Unpatchify" to attach the triplane; it also uses separate MLPs but its MLPs have smaller sizes.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed a feedforward method for extracting meshes from multi-view images 
based on large reconstruction models. The paper proposes several improvements in 
terms of network architecture, including replacing pretrained DINO encoder with
simple convolution image encoders to capture image details,  and replacing deconvolution 
layers with pixelshuffle layers. To extract meshes, the paper proposes to apply 
Differentiable Marching Cubes on the density grid. To improve geometry quality, the 
paper applies additional losses on depth and normal maps. The paper compares to 
previous methods such as LRM and InstantMesh and shows that the proposed method achieves 
better geometry reconstructions and renderings.

### Strengths
1. The paper proposes several designs that improve the quality of LRM.  The paper performs 
ablation studies to validate the effectiveness of such designs.

### Weaknesses
1. The overall pipeline of the paper is similar to that of InstantMesh, which also applies LRM for mesh reconstruction with differentiable iso-surface methods. Both papers apply
losses on depth and normal maps to improve the quality of the geometry.  While the proposed designs
are helpful, they do not provide very significant technical contributions. Recent works
such as MeshLRM, GS-LRM, and LGM have adopted similar strategies to improve the network design
and should be discussed here.  Specifically, the replacement of the DINO encoder with simpler architectures like patchify+linear has been explored in GS-LRM and MeshLRM, diminishing the novelty of this design choice. The paper fails to adequately acknowledge and differentiate its contributions from these existing works.

2. The paper does not provide quantitative evaluations on the effectiveness of the network
design choices such as pixelshuffle layers and encoders. Ideally, the numbers should be provided
for the ablation models in Table 1 for better clarity. The lack of specific metrics for each architectural modification makes it difficult to assess the true impact of these changes. For example, the performance difference between using pixelshuffle layers versus deconvolution layers, or the impact of different encoder architectures, should be quantified with metrics like PSNR or SSIM.

3. In the ablation models, is the DiNO encoder frozen or trainable during training? It's not
fully clear why the ViT cannot capture image details considering the existence of residual
connections. The paper should provide a more in-depth analysis of why the ViT encoder struggles to capture fine details compared to convolutional encoders, especially given the presence of skip connections. The inductive bias of the ViT and its impact on convergence should be discussed in more detail.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a novel approach for 3D mesh reconstruction from multi-view images. The authors improve upon the large reconstruction model LRM that use a transformer-based triplane generator and a Neural Radiance Field (NeRF) model trained on multi-view images. They introduce three key components to significantly enhance the 3D reconstruction quality. First of all, they examine the original LRM architecture and find several shortcomings. Subsequently, they introduce respective modifications to the LRM architecture, which lead to improved multi-view image representation and more computationally efficient training. Second, in order to improve geometry reconstruction and enable supervision at full image resolution, they extract meshes from the NeRF in a differentiable manner and fine-tune the NeRF model through mesh rendering. The method enables various downstream applications, including text/image-to-3D generation.

### Strengths
1. The results are good in terms of both qualitative and quantative result.
2. The experiments are solid. Many baselines are compared.
3. The paper in written very well.

### Weaknesses
1. This work has a large improvement in terms of quantative resutls. However, this work differs from previous works only from some incremental improvements in architecture. So what bring this such a large improvement? An ablation study of the proposed tricks will be very appreciated.
2. How long does it take to generate a single shape in total?
3. Will this work be open-sourced?
4. What is the common failure case of this method?
5. In table 1, some baselines has better results than yours (CD, IoU), however, you mark your results in bold font.

### Questions
See above

### Soundness
3

### Presentation
3

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
The paper proposed an improved 3D mesh geometry and texture refinement model based on large reconstruction model (LRM) structures.

The authors analyze the limitation of the LRM model and update this with modified LRM architecture, geometry refinement with NeRF initialization, and texture refinement stages.

### Strengths
The authors analyze and discuss well about why the previous LRM model has limitations and worse results. 

The qualitative results of the paper show improvement over the previous methods, especially for the text.

### Weaknesses
There are some typos.

In L. 66, theoptimization → the optimization

In L. 195, Lhuillier & Quan (2005)., → Lhuillier & Quan (2005),

In Fig. 4, LRM takes one front-view image, but GTR (the authors’ method) takes 4 views, which is not a fair comparison. The authors need to use the same front-view image.

The paper lacks discussion and limitations of their method. The authors need to discuss the limitations of their method and the possibilities for further development.

### Questions
In L. 91, the authors mention that “this enables us to render full-resolution images for supervision” for the advantage of the DiffMC pipeline. The reviewer wonders why it enables full-resolution images, and the authors need to add the reason; for instance, NeRF MLP needed heavy computation and was hard to use full-resolution, but mesh rasterization had effective computation.

In L. 97, the authors state, “fine-tune both the triplane representation and the color estimation model …”. The reviewer suggests replacing representation with feature, which is consistent with the word used later in the paper and less confusing with the triplane generator.

In L. 243, the reviewer wonders why the authors use Plucker coordinates for their camera ray embedding. Is there any insight or reason?

For the dataset, what is the source of an internal 3D asset dataset, and when retained, 26k superior assets of high quality are used?

In the qualitative results, IoU means 3D mIoU? The authors need to denote 3D if it is 3D metric. In Table 1 and Table 2, the left three columns for 2D metrics and the right two columns for 3D metrics are not specified. Authors need to add these details in the caption.

For the CD metric, the authors need to state their full name (maybe Chamfer Distance) first and use an abbreviation.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper builds on the LRM framework with three main improvements: modifications to the LRM model structure, end-to-end geometry refinement with NeRF initialization, and per-instance texture refinement. These enhancements contribute to improved geometry reconstruction and texture quality.

### Strengths
1. The proposed methods are well-grounded, and the ablation studies thoroughly support the authors' claims.
2. The visual results appear to achieve superior geometry and texture compared to previous methods.
3. The paper is well-written overall, making it easy to follow.

### Weaknesses
1. The approach involves multiple stages, which may require more time compared to the baseline.
2. The paper lacks evaluation metrics for generation quality, such as FID or CLIP scores; including these metrics would strengthen the evaluation.


### Questions
Aside from the mentioned weaknesses, I have the following questions:
1. Using DiffMC for geometry could be time-consuming. The paper highlights that the color refinement stage only takes 4 seconds, but it does not mention the time required for the geometry stage. I would like to see a breakdown of the time taken for each stage compared to the baseline.
2. In Section 3.2, where do the depth loss and normal loss supervision come from? If this is a single real-world image, how are depth and normal information obtained?
I would be glad to raise my rating if my concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3
