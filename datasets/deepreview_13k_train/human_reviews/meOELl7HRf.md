# Long-LRM: Long-sequence Large Reconstruction Model for Wide-coverage Gaussian Splats

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
We propose \methodname{}, a generalizable 3D Gaussian reconstruction model that is capable of reconstructing a large scene from 
a long sequence of input images. Specifically, our model can process 32 source images at 960$\times$540 resolution within only 1.3 seconds on a single A100 80G GPU. Our architecture features a mixture of the recent Mamba2 blocks and the classical transformer blocks which allowed many more tokens to be processed than prior work, enhanced by efficient token merging and Gaussian pruning steps that balance between quality and efficiency. 
Unlike previous generalizable 3D GS models that are limited to taking 1$\sim$4 input images and can only reconstruct a small portion of a large scene, \methodname{} reconstructs the entire scene in a single feed-forward step. 
On large-scale scene datasets such as DL3DV-140 and Tanks and Temples, our method achieves performance comparable to optimization-based approaches while being two orders of magnitude more efficient. Project page: \url{https://arthurhero.io/projects/llrm/}%\kz{Our project page is available at: xxxx}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Long-LRM, a feed-forward model for large-scale 3D Gaussian reconstruction that can process 32 high-resolution (960×540) input images in just 1.3 seconds on a single A100 GPU. The key innovation lies in its hybrid architecture combining Mamba2 and transformer blocks, along with efficient token merging and Gaussian pruning strategies to handle long sequences and memory constraints. The model achieves 600× faster reconstruction than optimization-based 3D Gaussian Splatting while maintaining comparable or better quality, as demonstrated through comprehensive evaluations on DL3DV and Tanks and Temples datasets.

### Strengths
1. Enhance feed-forward scene reconstruction methods, eg, GS-LRM to more input views.

2. The usage of hyrbid network of Mamba and transformer is reasonable for handling extreme long-sequence tokens, though it is not the first paper in this field that introduce Mamba.

3. Practical solutions for memory efficiency through token merging and Gaussian pruning, enabling scaling to high resolutions (960x540) where other variants fail.

4. The ablation study is comprehensive, well demonstrating the effectiveness of each component, with clear metrics on performance gains.

### Weaknesses
1. Lack of novelty. The core contribution of this paper seems a combination of GS-LRM and Hamba, Gamba  and MVGamba. 

2. The lack of discussion on the above Mamba-based 3D reconstruction models, which have been publicly available more than half years, is not acceptable.

3. While this paper presents several practical innovations in memory optimization, it may be more suitable for computer vision conferences rather than ICLR.

### Questions
While the work on token merging and Gaussian pruning for memory efficiency is valuable, these engineering optimizations better fit computer vision venues like CVPR. Despite the technical advances,  could you justify how this work aligns with ICLR's focus on fundamental machine learning methodology rather than computer vision conferences?

### Soundness
2

### Presentation
3

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
This paper proposed a generalizable 3D reconstruction framework for a long range of input images. 3D Gaussian Splatting is used as the 3D representation like many previous works. The network architecture is design as mixture of Mamba2 and transformer layers to process input tokens with long length.  The whole model is trained in single stage and can reconstruct large scale 3D secenes on DL3DV-140, Tanks and Template datasets.

### Strengths
1. Extends the application of feed-forward 3D scene reconstruction to longer-range inputs.
2. Sound network architecture design by combining transformers and Mamba2 to process long token sequences.
3. Applies a token merging module to reduce computational overhead for processing long-range input views.
4. The author provides justification for using Mamba in Table 2, although the comparison with GS-LRM is somewhat unfair.

### Weaknesses
1. Insufficient justification for using Mamba. GS-LRM claims it can accept arbitrary input view numbers by downsampling images with large patch sizes to shorten the overall token length for global attention. The features after attention can then be upsampled to predict a large number of Gaussians. However, in Table 2, the authors provide the same patch size for both the 7M1T and GS-LRM architectures, leading to an unfair comparison. The core issue is not just the patch size, but also the lack of exploration into how GS-LRM's downsampling strategy interacts with different input view numbers. A more rigorous analysis of GS-LRM's limitations in handling long input sequences, beyond just empirical comparisons with a fixed patch size, is needed to justify the necessity of Mamba.

2. Why not cost volumes and abadon 3D inductive biases. Although the authors have argued that methods like MVSplat are prone to out-of-memory (OOM) issues, these challenges are largely engineering problems that can be addressed with techniques like FlashAttention or through lightweight network architecture design. The authors need to clarify this point; otherwise, this work may mislead the feed-forward 3D scene reconstruction community. The argument against cost volumes is not sufficiently justified, as the OOM issues are often a result of naive implementations rather than an inherent limitation of the cost volume approach. The authors should acknowledge the potential for efficient cost volume implementations and provide a more detailed analysis of why those aren't suitable for their specific task, beyond just citing memory concerns.

3. Lack of discussion on 3D reconstruction works utilizing Mamba. This work seems to overlook prior research utilizing Mamba for 3D reconstruction, such as Hamba, Gamba, and MVGamba, which have been publicly available for over six months. Discussing these related works is necessary to emphasize the motivation for this study. The absence of discussion on these methods leaves a gap in the literature review, as these works directly relate to the use of Mamba in 3D reconstruction. The authors need to contextualize their work within the existing body of research to properly highlight their contribution.

4. Limited technical contribution and insight. The technical contributions of this work are quite limited, as are its insights. It mainly extends previous 3D reconstruction efforts that use Mamba for scene reconstruction. Notably, combining Mamba and transformer blocks cannot be considered novel, as this setup was proposed in the Mamba v2 paper and has been widely adopted in various Vision Mamba works with Mamba v2. When evaluating the technical contributions, it is challenging to provide a positive rating, as nearly all modules in this paper have been widely used in numerous feed-forward 3D object reconstruction studies over the past year. Additionally, the claims regarding cost volumes contradict established practices in feed-forward 3D scene reconstruction.

### Questions
please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
They propose a generalizable 3D Gaussian reconstruction model that can reconstruct a wide -coverage scene from a long sequence of input images with Mamba2 blocks. Some validation results shows the effeciveness compared with original 3DGS.

### Strengths
1.Introducing a method able to infer the 3DGS for wide-coverage scenes.

2.Utilize Mamba2 architecture to model the long token relations.

### Weaknesses
1.The comparison is not enough. Only compared with naive 3DGS. There are recent 3DGS/NeRF variants designed for large scale scene modeling: Zip-NeRF: Anti-Aliased Grid-Based Neural Radiance Fields, Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering, Mip-Splatting: Alias-free 3D Gaussian Splatting.

2.Despite of the inference speed, it shows in the videos the floaters appear without further regularizations.

3.They main contribution is to use Mamba2 for long sequence modeling, which limits the technical contribution of the paper.

4.It is better to show the NVS comparison under sparse view setting compared with generalizable 3DGS methods like MVsplat and pixelSplat.

5.The method only shows the NVS results, it would be better to show some surface reconstruction results since with the development of "2DGS" and "High-quality Surface Reconstruction using Gaussian Surfels". Nowadays surface reconstruction with Gaussians already achieves very good results.

6.No regularization for aliasing effect is proposed.

### Questions
1.Is it able to seamlessly concat all sets of gaussians inferred by your models for large scale scenes which need hundreds of images? If so, how is it compared with city-scale reconstruction methods like CityGaussian and Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians, which are designed for real large scale scene reconstruciton.

### Soundness
3

### Presentation
3

### Contribution
2
