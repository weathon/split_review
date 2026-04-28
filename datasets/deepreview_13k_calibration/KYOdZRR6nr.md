# GALA: Geometry-Aware Local Adaptive Grids for Detailed 3D Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
We propose GALA, a novel representation of 3D shapes that (i) excels at capturing and reproducing complex geometry and surface details, (ii) is computationally efficient, and (iii) lends itself to 3D generative modelling with modern, diffusion-based schemes. The key idea of GALA is to exploit both the global sparsity of surfaces within a 3D volume and their local surface properties. \emph{Sparsity} is promoted by covering only the 3D object boundaries, not empty space, with an ensemble of \dd{tree root voxels}. Each \dd{voxel} contains an octree to further limit storage and compute to regions that contain surfaces. \emph{Adaptivity} is achieved by fitting one local and geometry-aware coordinate frame in each \dd{non-empty leaf node}. Adjusting the orientation of the local grid, as well as the anisotropic scales of its axes, to the local surface shape greatly increases the amount of  detail that can be stored in a given amount of memory, which in turn allows for quantization without loss of quality. With our optimized C++/CUDA implementation, GALA can be fitted to an object in less than 10 seconds. Moreover, the representation can efficiently be flattened and manipulated with transformer networks. We provide a cascaded generation pipeline capable of generating 3D shapes with great geometric detail.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a storage-efficient new representation of 3D triangle surface meshes, GALA, which can be used for 3D generation trained by a transformer. To create the proposed representation, voxel tree root nodes are initialized over the surface of the mesh using FPS. In the local adaptive grid extraction step, the grid orientation is aligned with the geometric structure using PCA on the local normal vectors, and the grid is rescaled using a histogram. With this representation, the authors show that 3D reconstruction and generation can be performed using cascaded diffusion models. Experiments demonstrate the effectiveness of the proposed method in 3D reconstruction and generation, both quantitatively and qualitatively.

### Strengths
(1) The proposed representation has a low number of parameters, fast fitting time, high precision, and quick mesh extraction time, implemented using pure CUDA and LibTorch.

(2) Initially, I think that the proposed representation is sensitive to the FPS results regarding the number of root tree nodes ($N_o$) and overlap ratios ($\alpha$), so I doubt whether it can effectively cover the thin parts of meshes. However, the authors conduct numerous ablation studies on design choices to achieve optimal performance for general meshes.

(3) The results show that the proposed method achieves SOTA performance on reconstruction and generation with a few number of parameters compared to existing baselines.

(4)  The paper has high writing quality which makes it easy to understand.

### Weaknesses
 (1) As shown in the Sec. C. Failure Cases, the proposed representation cannot cover the long thin mesh parts.

### Questions
I found that the authors have currently created an anonymous repository, and I am curious whether the authors intend to make the code public in the future.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a new geometric representation based on storing optimized SDF values of a shape on an adaptive, overlapping grid of optimally scaled and rotated cells. This representation can be very efficiently generated for any shape and enables diffusion-based generation tasks.

### Strengths
I congratulate the authors for their submission. They build on existing work to propose a non-trivial, novel geometric representation that is particularly useful for detailed 3D generative tasks. While I am not an expert in 3D generative modeling, it seems clear that this work outperforms the state of the art in resolutive power, and outperforms its main competitor (Mosaic-SDF) on reconstruction tasks. There is little doubt in my mind that this work would be received positively in the neural geometric processing community.

### Weaknesses
The main weaknesses of this work are in the magnitude of the contribution and the clarity of the writing:

Contribution. It could be argued this work is limited to being an adaptive version of Mosaic-SDF, and that most choices made in the algorithm are the same choices any researcher would made if attempting to extend M-SDF to an adaptive realm (the authors of M-SDF themselves even mention “adding local coordinate frames” as a potential future work avenue). The authors of this work address this and also mention the cascading generation strategy as a difference with M-SDF; however, the magnitude of this contribution is not particularly explored: what would have happened if they used an identical flow-matching strategy to the one in M-SDF? It remains unclear how much of the performance gain is attributable to the adaptive grid structure versus the cascading generation strategy. A more thorough ablation study is needed to isolate the impact of each component.

Clarity of writing. Several key aspects of the work are missing or unclear, to the point in which I don’t believe I understand important sections of the algorithm (see “Questions” below). Additionally, perhaps due to LaTeX template changes, groups of citations that should be grouped in parentheses are not, making reading difficult (e.g., 053, 080). The code link also seems to be missing.

Nonetheless, I do not think these weaknesses justify rejecting this work, which undoubtedly outperforms the state of the art and will definitely save authors’ time if they wish to improve the M-SDF performance in the future.

### Questions
- How is each grid subdivided? As far as I can tell, the only explanation of this subdivision is “we recursively deduce the further levels of tree nodes in an overlapping way where we slightly expand the divided spaces at each level by ratio α.” Which is far from enough detail for a reader to replicate the results. Which cells are subdivided? According to which logic? Along which axis?
- How is a mesh extracted from this adaptive grid? Are the authors setting up some regular grid and interpolating values at grid cells using Eq. (2), and then using Marching Cubes or some other reconstruction algorithm? Or are they somehow extracting a mesh directly from the stored SDF data at the adaptive cells? The latter seems very non-trivial and would be an important contribution on its own.
- What does “the weighting function which is defined by the infinity ball centered at the grid center pig and rotation matrix Oi” mean? Isn’t \omega(x,i) just Eq. (3)?
- It was very hard for me to follow Sec. 3.2., I think partly because of the notation used: Are x_v (lowercase) and X_V (uppercase) the same thing? Am I right in understanding that in this cascading scheme, given an initial tree X_0, the grid configuration X_V and the SDF values at those points will not be affected by the conditioning? Since the class label is only involved in Step 1.

### Soundness
4

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
4

### Summary
The paper proposed GALA, a novel method for representing 3D shapes using local adaptive grids.  GALA's core concept is to leverage the global sparsity of surfaces within a 3D volume and their local surface properties. The representation enhances the local details by covering only the boundaries of the 3D object with a set of tree root voxels, rather than the empty space, with each voxel containing an octree to limit storage and computation to regions containing surfaces. By adjusting the orientation of the local grid and the anisotropic scales of its axes to the local surface shape, GALA can store a greater amount of detail within a given memory budget compared with Mosaic-SDF and other representations. The advantages of GALA are: (1) it effectively captures and reproduces intricate geometric and surface details, (2) it is computationally efficient, and (3) it is compatible with modern 3D generative modeling techniques, particularly those based on diffusion schemes.

Furthermore, the authors provide a cascaded generation pipeline that is capable of generating 3D shapes with significant geometric detail, demonstrating the practical application and potential of GALA in the field of 3D generation.

### Strengths
Originality:

1. This work's main contribution is to proposed a novel 3D shape representation which can preserve the local details by using local adaptive grids, while previous methods like Mosaic-SDF using regular grids.
2. The proposed representation is simple and efficient, achieving a good compression ratio with very little storage space and quantization operations.
3. Moreover, the authors also did comprehensive evaluation and application  like 3D shape diffusion to validate the effectiveness of the proposed representation.


Clarity:

1. This pipeline in this submission is technically sound and is largely clearly written and well organized.
2. For the comparison, the numerical results and the visual figures show a significant performance improvement over the baseline method in ShapeNet. But only a few subset with simple geometry (airplane and chair) is evaluated.
3. For the ablation study, the authors show the importance of some designs like determining orientation by bounded normals and rescaling with histogram.

### Weaknesses
1. While this proposed expression can enhance the details of the reconstruction, I think it is very challenging for diffusion networks to generate the explicit parameters for the root node, grid values, and grid configuration step by step. If some parameter predictions are incorrect, it can greatly affect the quality of the geometry in the subsequent steps. According to the figures in the supplementary, some structures of the generated meshes are noisy. This also limits the practical application of this expression in generative models. It would be better to discuss in the conclusion, or analyze how the errors propagate in the steps and ultimately affect the geometry's quality.

2. I think the authors have omitted some relevant citations regarding XCube and OctTree. XCube employs sparse convolution to achieve high-quality reconstruction and geometric compression, and it has also demonstrated its applicability to generative models. It would be beneficial to include additional quantitative and qualitative experiments and discussions focused on reconstruction quality, compression efficiency, and the applicability to 3D generative models.

3. The authors only tested on some simple geometric details of ShapeNet; it would be better if they could show some more complex results, like objects in Objaverse or Thingiverse.

### Questions
1. I noticed that the paper lacks a comparison with the reconstruction results of Mosaic-SDF, only comparing the generation results with it in Table 3. After reading the paper of Mosaic-SDF and I found that they also lack this experiment. However, my understanding is that "Ours w/o A" in Table 2 should be a structure similar to Mosaic-SDF. Are there any other differences?


2. In Figure 7, when comparing the results with Mosaic-SDF, I didn't notice much difference. Can you provide more representative examples in the revised version? Or is this the maximum performance gap compared with Mosaic-SDF?

### Soundness
4

### Presentation
4

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
This paper describes a 3D shape representation based on trees. The input shape is initially discretized into voxels, and the location of the voxel is decided through Furthest Point Sampling (FPS). Then, each voxel is further discretized into an octree which represents the surface details. Each octree uses a local adaptive grid, with adjusted orientation and scale, to encode the local surface.
To further compress the representation, the octree and voxel information ($X_0, X_\bar{v}, X_v$) is quantized.
Finally, $X_0, X_\bar{v}, X_v$ can be generated by a diffusion model in a coarse to fine manner (first $X_0$ for the voxels, then $X_\bar{v}$).

### Strengths
The proposed representation is memory efficient thanks to the quantization. It cleverly exploits a combination of SDF and Octrees. Furthermore, thanks to its structure, it is possible to flatten it out and use generative models to encode it.

### Weaknesses
There are aspects of this method that do not convince me. I hope the authors can clarify them.
1. The main benchmark is Shape-Net, however, this dataset is known to be axis-oriented. It would be more convincing if the authors used additional datasets.
2. How well does this method scale with large shapes (e.g., shapes from the Stanford dataset)?
3. The authors claim to introduce a 3D representation, yet, they rely on a generative model to encode and decode shapes. The soundness of the representation is never evaluated. It seems that the representation is a convenient tool for model generation. If so, I would suggest the authors should reword the text.

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
3

### Contribution
3
