# Ghost on the Shell: An Expressive Representation of General 3D Shapes

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
\vspace{-0.8mm}
The creation of photorealistic virtual worlds requires the accurate modeling of 3D surface geometry for a wide range of objects. For this, meshes are appealing since they 1) enable fast physics-based rendering with realistic material and lighting, 2) support physical simulation, and 3) are memory-efficient for modern graphics pipelines. Recent work on reconstructing and statistically modeling 3D shape, however, has critiqued meshes as being topologically inflexible. To capture a wide range of object shapes, any 3D representation must be able to model solid, watertight, shapes as well as thin, open, surfaces. Recent work has focused on the former, and methods for reconstructing open surfaces do not support fast reconstruction with material and lighting or unconditional generative modelling. 
Inspired by the observation that open surfaces can be seen as islands floating on watertight surfaces, we parameterize open surfaces by defining a manifold signed distance field on watertight templates. With this parameterization, we further develop a grid-based and differentiable representation that parameterizes both watertight and non-watertight meshes of arbitrary topology. Our new representation, called \emph{Ghost-on-the-Shell} (\gshell), enables two important applications:  differentiable rasterization-based reconstruction from multiview images and generative modelling of non-watertight meshes. We empirically demonstrate that \gshell achieves state-of-the-art performance on non-watertight mesh reconstruction and generation tasks, while also performing effectively for watertight meshes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new representation, G-Shell, for 3D data. Existing papers mostly focus on modeling solid, watertight shapes, while the modeling of thin, open surfaces has not been widely studied. To fill this gap, this paper proposes a parameterization and develops a gruid-based method for both watertight and non-watertight meshes of arbitrary topology. Experiments show that G-Shell achieves state-of-the-art performance on non-watertight mesh reconstruction and generation tasks, while achieving competitive results for watertight meshes.

### Strengths
1. The topic studied in this paper is interesting and important.
2. Being able to model thin, open surfaces will be useful for a couple of applications.
3. The proposed method is technically sound.
4. Experiments show that the proposed method is effective in modeling non-watertight meshes.

### Weaknesses
1. While the proposed method is faster than other methods as shown in Table 3, 3 hours is still too long. The practical applicability of the method is limited by this long processing time, especially when compared to methods that achieve similar results in minutes or even seconds. This makes it difficult to iterate on design or use the method in real-time applications.

2. The thin shape examples in Figure 4 and Figure 7 don't have complicated geometry. If there is a more complicated geometry, how well would the proposed method perform in reconstructing / modeling? For instance, when dropping a cloth onto an object, the cloth will have a lot of folds, wrinkles and even a lot of self-contacts. Can the proposed method deal with this case? The lack of evaluation on complex, highly detailed surfaces raises concerns about the method's robustness and generalizability. Specifically, the claim that the method can handle arbitrary topology needs to be demonstrated with more challenging examples to be fully convincing.

### Questions
Please see questions above

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new representation for surfaces with boundary (open surfaces) geared toward inverse rendering and surface reconstruction. The representation views an open surface as a sub-level set of a function on a closed surface, which is in turn represented as a level set of a function in the ambient space. The two functions are discretized together on a background grid, and an extended marching-tetrahedra lookup table enables extraction of a mesh for the open surface. The advantages of the representation are demonstrated for reconstruction from images as well as generative modeling by a diffusion method.

### Strengths
The basic idea is elegant, and it avoids the problems of unsigned distance fields. The comparisons to previous work are also compelling. The generative modeling results look cool, though it would be nice to see some examples other than clothing if other datasets are available.

### Weaknesses
The authors claim this is the first work to propose a differentiable representation suitable for both open and closed surfaces. Though they mention representations for open surfaces based on unsigned distance fields, they should also include citations to the following two works, which offer alternative approaches:
- D. Palmer, D. Smirnov, S. Wang, A. Chern, and J. Solomon, “DeepCurrents: learning implicit representations of shapes with boundaries,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022, pp. 18665–18675.
- T. V. Christiansen, J. A. Bærentzen, R. R. Paulsen, and M. R. Hannemose, “Neural Representation of Open Surfaces,” 2023, doi: 10.1111/cgf.14916.

The exposition could use some polishing. In addition to general copy-editing, some details of the method require further elaboration. Most prominently, the mesh extraction algorithm, which is a main contribution of the paper, is described only very briefly in section 4.2, and the lookup table for G-shells is only explained pictorially in figure 3. It would be helpful to readers to include at least a little more explanation of what is going on in that figure and why (even if it has to go in an appendix or supplemental material). Specifically, the paper lacks a clear explanation of how the extended marching tetrahedra lookup table is constructed and how it handles the transitions between different surface regions defined by the sub-level set. The description should also clarify how the method ensures consistent orientation of the extracted mesh, especially at the boundaries.

The description of the generative modeling approach in the paragraphs following eq. (2) is unclear. What does "unevenly weighted prediction" mean? What is the naïve diffusion loss, and what are you replacing it with? Why does predicting the linear interpolation coefficient instead of the value of $\nu$ help? Is there any tradeoff in doing this? If the normalization of SDF values is an issue, would there be an advantage to using more general implicit functions instead? If you are going to extend MeshDiffusion, it would be helpful to include at least a brief summary of how that method works. The paper does not adequately explain why the specific choice of predicting the interpolation coefficient is beneficial over directly predicting the SDF values, especially considering the potential for increased memory consumption. The authors should also discuss the limitations of their approach and whether it introduces any biases into the generative process.


### Questions
The paper shows a lookup table for a marching-tetrahedra approach for G-shells. Is there also an extended version of marching-cubes?

The "hole-opening" loss in eq. (1) sounds like it really promotes hole-closing. In any case, it requires more explanation. What does the parameter $\epsilon$ do? How should one set it? The paper refers to "topological holes" but I assume what is meant here are boundaries, not handles.

The appendix lists many more loss terms with free parameters, and it is unclear whether all of these terms are necessary. As usual, it would be helpful to add an ablation study. Some of the descriptions of the loss terms are cryptic and could do with elaboration. E.g., how does (12) reduce "floaters" and "inner geometry"? Why do you need a second SDF regularization after imposing the eikonal regularization? Would it be helpful to include some form of eikonal regularization on $\nu$ as well—ideally taking the gradient along the surface?

## Minor quibbles:
- p. 2: "generation modeling" -> "generative modeling"
- p. 3: What does "validity value" mean?
- p. 4: referring to a curve as a "2D mesh" and a surface as a "3D mesh" is confusing. It would be better to say "polygonal curve" and "surface mesh," respectively, or something similar.
- p. 5: "pose-processing" -> "post-processing"
- 6.2: "winding number" should really be "generalized winding number." Also, I am not sure what it means to look at the generalized winding number on the surface when it is a function in the ambient volume that has a sharp jump at the surface.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends the 3D grid representation by introducing an additional mSDF field defined on grid vertices for the modeling of open surfaces.  This new representation can be used in the reconstruction and generative modeling of open 3D surface meshes.

### Strengths
1. A nice extension of 3D grid representation that can handle open surface meshes. 
2. Impressive experimental results on open surface reconstruction and generation.

### Weaknesses
While the experimental results are impressive, it is not clear whether the proposed modified marching cube or tetrahedra with mSDF value can guarantee the correct topology of the 3D mesh. For example, an isolated edge with no incident triangles.



### Questions
1. The ability to handle specular surfaces is emphasized in the experimental results. However, the experimental setting to handle the specular surfaces is not clear enough.  Do you simultaneously reconstruct lighting, geometry and material properties from the captured images?  or you assume lighting condition is known. 

2. How is the performance of the proposed method when reconstructing open surfaces that are homeomorphic to donuts or other complex surfaces with many topology handles?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel mesh representation called Ghost-on-the-Shell (G-SHELL). This representation parametrizes non-watertight surfaces by defining a manifold signed distance field on watertight templates. It enables reconstruction from multiview images and generative modeling of both watertight and non-watertight meshes of arbitrary topology. The paper demonstrates that G-SHELL performs well in tasks related to non-watertight mesh reconstruction and generation while also being effective for watertight meshes.

### Strengths
The paper introduces an original approach to implicitly modeling non-watertight 3D meshes. Treating open surfaces as entities floating on watertight surfaces is a novel idea with significant advantages over other methods that require unsigned distance fields (UDF). It leads to the development of a manifold signed distance field (mSDF) on the watertight template, which is a sound contribution.

In terms of quality, the methodology is well-described, and the authors offer a clear rationale for their Ghost-on-the-Shell (G-SHELL) implicit modelling approach. The paper also provides empirical evidence of the advantages of G-SHELL in tasks such as mesh reconstruction and generation, which enhances the overall quality of the work.

The paper is well-written and the contributions are cleary presented. The authors effectively communicate complex concepts.

In terms of significance, G-SHELL is a differentiable and efficient implicit representation for both watertight and non-watertight meshes which broadens its impact. Besides it has the potential to be easily adopted in computer graphics pipelines.  G-SHELL applications in reconstruction and mesh generation problems are notable. In particular, G-SHELL’s enables reconstruction methods where the topology, material and lighting are jointly optimized which is crucial for scaning 3D assets from images. 

Overall, this paper presents an original, high-quality, clear, and significant contribution to deal with non-watertight surfaces and demonstrating practical applicability through empirical validation.

### Weaknesses
G-SHELL inherits common disadvantages of implicit surface representation methods. Mainly, since it employs a regular grid, surfaces with high and unbalanced entropy will require many grid elements, which can be inefficient and limiting for real applications. Specifically, the memory footprint and computational cost will scale poorly with the complexity of the surface, making it challenging to represent intricate details or large-scale scenes. This is particularly concerning for non-watertight surfaces which often exhibit complex boundaries and fine-grained features. 

G-SHELL uses a marching cubes-like algorithm to extract the surface. Even though this method is highly parallelizable, it also represents a burden in computation compared to explicit methods. The computational cost of extracting the mesh from the implicit representation can become a bottleneck, especially when high-resolution meshes are required, limiting the real-time applicability of the method. Furthermore, the quality of the extracted mesh is dependent on the grid resolution, which can introduce artifacts if not chosen carefully.

G-SHELL does not model self-intersecting and non-orientable surfaces. This limitation restricts its applicability to a subset of real-world scenarios where such complex topologies are common. For example, modeling intricate folds in clothing or complex organic shapes with self-intersections would not be possible with the current formulation.

### Questions
Regarding the experiments in mesh generation, G-SHELL is compared against other implicit  SDF based methods that can only represent watertight surfaces. Since the experiments are only conducted with a dataset of non-watertight surfaces (clothes), it is thus expected that G-SHELL is going to be better at the job than the rest of methods. How well MD w/ G-SHELL performs with watertight surfaces compared with MeshDiffusion?   


PolyGen [40] is regarded on page 3 as ineffective for high vertex counts. Although this is probably accurate, it is worth clarifying in the paper that methods like PolyGen generate non-uniform meshes and use the vertices more efficiently than the regular grid used in G-SHELL.  Comparing vertex counts between the two methods does not seem fair. 


The paper lacks experiments on real data, especially in reconstruction. It would be interesting to compare G-SHELL + differentiable rasterizers against the baselines based on volume rendering or even vanilla NERF + marching cubes. Do the authors plan to include such experiments in the camera-ready version?


It would be illustrative to visualize the watertight template being estimated jointly with the open surface in some of the experiments.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
