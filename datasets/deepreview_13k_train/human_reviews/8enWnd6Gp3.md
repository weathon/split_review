# TetSphere Splatting: Representing High-Quality Geometry with Lagrangian Volumetric Meshes

- Decision: Accept
- Scores: 6, 8, 8, 8, 8

## Abstract
We introduce \rep, a Lagrangian geometry representation 
designed for high-quality 3D shape modeling.
\lowerrep leverages an underused yet powerful geometric primitive -- volumetric tetrahedral meshes.
It represents 3D shapes by deforming a collection of tetrahedral spheres, with geometric regularizations and constraints that effectively resolve common mesh issues such as irregular triangles, non-manifoldness, and floating artifacts.
Experimental results on multi-view and single-view reconstruction highlight \lowerrep's superior mesh quality while maintaining competitive reconstruction accuracy compared to state-of-the-art methods.
Additionally, \lowerrep demonstrates versatility by seamlessly integrating into generative modeling tasks, such as image-to-3D and text-to-3D generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a method for reconstructing 3D geometry from multiview images. The geometry is represented by Tetrahedral meshes of sphere topology that are optimized in standard fashion w.r.t a rendering loss, along with two geometric regularizes - the biharmonic energy to ensure a smooth deformation, and a barrier term that prevents tetrahedra from inverting.

### Strengths
The paper revisits the idea of using meshes for 3D reconstruction, and reaffirms that an explicit representation is extremely efficient in producing high quality 3D geometry from images. The paper is written in a clear way and is easy to understand.

### Weaknesses
1. My main concern with the paper is its novelty and contribution: the paper essentially proposes to deform a mesh w.r.t a visual loss which is standard (e.g., [Nicloet et al. 2021]), while using two standard regularizes to guarantee a "good" deformation (smooth and without inversions). This is a very standard approach. The only part that seems less explored is the use of tetrahedra instead of triangles, however this of course has been explored extensively outside of the context of differentiable rendering, hence the only part I can deem truly novel is "using tetrahedra instead of triangles in tandem with multiview reconstruction". This feels like a marginal contribution. It could be argued to be a very practical approach which may convince me to champion it, however that leads me to my second concern:
2. Evaluation seems somewhat selective, and the methods compared to do not strike me as the immediate alternatives. Namely, I find [Nicolet et al. 2021] as a main contender, as well as "Continuous remeshing for inverse rendering" which is uncited. Many other techniques that cite [Nicolet et al. 2021] can be considered. 
3. The argumentation for the use of a volumetric mesh instead of a triangle mesh needs to be justified further through experiments. It seems the only argument for a full discretization of the *volume* (as opposed to the surface via a triangle mesh), is to regularize the volumetric deformation with the two losses. This seems like a significant overkill, as simpler regularizers could be employed on the triangle mesh (again, e.g., Nicolet et al. 2021) to ensure it behaves well.

### Questions
- can you explain why did you choose to not compare to [Nicolet et al. 2021] and methods that adopted it later? 
- you do not cite "Continuous remeshing for inverse rendering" - how do you think your method would fair in respect to it?
- are there other advantages to using a tetrahedral mesh as opposed to triangle, except the two regularization losses?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a shape reconstruction method that takes a set of images as input and fits a 3D model with reflectance properties to them. In line with a large body of recent work, it combines a rendering loss with shape regularization to directly optimize a 3D scene representation by "simple" numerical descent. The problem is particularly challenging as the paper uses a "Lagrangian" representation, specifically, a tetrahedral mesh that co-moves with the surface points obtained.

As recent work, such as [Nicolet 2021] has pointed out, the success of such an approach critically hinges upon suitable regularization, as the rendering loss is ambiguous and it is easy to get stuck in a bad local minimum with nonsensical mesh structures (which has been an issue for a long time in attempting such direct shape optimization against relatively weak data constraints).

The key contribution of this paper is to use a volumetric representation, a tet-mesh, with a penalty against inversion of elements along with an incrementally applied smoothness regularizer (a bi-harmonic energy applied to deformation gradients of the current mesh) that promotes changes in low-frequency shape first.

The paper provides very convincing results and shows a number of interesting applications, some of which only made it into the appendix.

### Strengths
I think that the main strength of the paper is the idea itself: Regularization is important to avoid bad mesh structure, and a volumetric representation intuitively gives much more leeway to regularization over a pure thin-shell / surface model (the inductive bias of this being a solid is stronger than regularizing details on thin surface). The proposed setup with inversion constraints and smoothness looks plausible and seems to work very well in practice. I should add that I am not actively working in this area, so I might miss some related work; but if this kind of approach has not yet been tried, the approach itself seems worth publishing.

The results are also convincing in terms of quality and versatility. The paper is very well written, nicely illustrated and enjoyable to read. Comparisons against some related recent method also underline the quality of the results quantitatively.

### Weaknesses
In my opinion, the main downside is that the paper is rather light on analysis: Why does it use the bi-harmonic energy on deformation gradients? What does this actually mean (application to derivatives should create higher-order smoothness, or in terms of a Fourier-perspective, add an additional high-pass filter in front of the regularizer)? What happens, if other regularizers are used? How important is the non-inversion term, and how brittle are parameter choices? It would also be interesting to discuss the relation to other attempts at stricter regularization, such as Nilcolet et al.'s work. I would guess that the volumetric approach is strictly superior, if fully exploited; showing something like this experimentally would make the paper much stronger.

Some of the limitations could also been discussed more clearly. For example, the paper only produces piecewise meshes, which are overlayed; it does not solve the problem of globally fitting a single tet-mesh. Comparisons in mesh quality should take this into account. Further, this also shows implicitly that the method is still to brittle to handle strong deformations during optimization; otherwise, one could just fit a single sphere globally. In this context, as well as in general, it would be instructive to show how to break the method by slowly stepping outside its "convergence radius" where good results can be obtained into cases where results are unsatisfactory. My criticism here is not that there are limitations but that the paper could be strengthened by studying them more in depth.

Finally, the paper seems like a better fit to a conference on computer vision or graphics in terms of methods and problems, but I would consider the topic close enough not to exclude it.

### Questions
When does the method break? At which point does the proposed machinery fail to fit a reasonable geometry to data, and how do the problems look like / introduce themselves? Which conceptual or technical challenges would be needed to overcome to fix this?

Does the method have fundamental advantages over previous representations? If so, can you make a formal or experimental argument to convince the reader? If the differences are more nuanced, what are the key trade-offs one has to make here?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The manuscript introduces a framework named TetSphere Splatting, which can be used to reconstruct 3D meshes from multi-view images. TetSphere uses tetrahedron spheres to represent an object. During optimization, deformation field is predicted to relocate vertex points to minimize cost. Experiments in multi-view reconstruction, image/text to 3D shows potential applications of TetSphere Splatting.

### Strengths
-	The problem is of interest to the research community.
-	The formulation of TetSphere Splatting is novel, and an interesting theoretical perspective from prior work.
-	The experiments setup is diverse, including many applications.

### Weaknesses
Overall, the paper is quite interesting. However, my concern about the paper is its claim, where experimental results cannot back up.

- TetSphere is claimed to have superior surface quality due to the fact Marching Cubes is not needed. However, all qualitative results seem to suggest that the TetSphere needs to be sufficiently dense to produce detailed structures. This leads to unnecessarily dense triangles, which can also be achieved by very dense marching cubes resolution. What is the advantage in this case? Specifically, the claim that TetSphere avoids the need for Marching Cubes implies a fundamental advantage in surface quality. However, the visual results indicate that a high density of TetSpheres is necessary for capturing fine details. This raises the question of whether the resulting dense triangle mesh offers a tangible benefit over a high-resolution mesh generated by Marching Cubes. A more rigorous comparison, perhaps varying the density of TetSpheres against different resolutions of Marching Cubes, would be necessary to substantiate this claim.

- Moreover, while the manifoldness of TetSphere is guaranteed, the baselines compared are all Eulerian representations without sufficient regularization. Approaches such as NeuS and VolSDF use volume rendering to achieve manifold meshes. While I understand the faster optimization process aspect, can authors comment on TetSphere’s advantage over NeuS/VolSDF from the quality perspective? The paper asserts that TetSphere guarantees manifoldness, which is a desirable property. However, the comparison against Eulerian methods that lack proper regularization might not be entirely fair. It would be helpful to understand how TetSphere compares to methods like NeuS and VolSDF, which employ techniques to ensure manifold outputs, in terms of surface quality metrics beyond just manifoldness. For instance, a comparison of surface smoothness or the presence of artifacts could provide a more comprehensive evaluation.

- Lastly, the claimed superior surface quality is not backed up by smaller Chamfer Distance, such as in Table 2. Can authors provide more explanation? The paper highlights superior surface quality as a key advantage of TetSphere. However, the reported Chamfer Distance in Table 2 does not seem to support this claim. A clarification on why Chamfer Distance is not a suitable metric in this context, or an explanation of the discrepancy between the claimed superior surface quality and the Chamfer Distance values, would be beneficial.

### Questions
-	When supervised purely based on depth/mask, the interior TetSphere not visible to any images will not receive gradients, except for regularization. Is this the main reason manifoldness is maintained?

-	Mosaic SDF [a] is one missing work that also follows the Lagrangian framework, where a set of volumes are moved in space. 

[a] Yariv, L., Puny, O., Gafni, O., & Lipman, Y. (2024). Mosaic-sdf for 3d generative models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4630-4639).

-	Clarification needed, below variables are not properly defined:
 - L265: what is N?
 - L266: what is T?
 - L309: what is n?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a Lagrangian geometry representation based on TetSpheres, volumetric tetrahedral spheres that deform to fit the desired geometry. Key applications of TetSphere splatting are demonstrated in monocular and multiview reconstruction. The deformation of TetSpheres is formulated as an energy optimization problem with geometric constraints that prevent the generation of irregular surfaces. Experiments are proposed to compare TetSpheres with state-of-the-art methods based on both Eulerian and Lagrangian geometry representations.

### Strengths
The paper is generally well-written, conveying complex concepts and methods in a concise style. 

The state-of-the-art is clearly explained and appears to be up-to-date.

The proposed primitive is original and effectively addresses common issues in other Lagrangian geometry representations, such as irregular triangles, non-manifoldness, and floating artifacts.

The energy optimization process for splatting is well-designed and effective, with a convincing initialization algorithm.

The accuracy in monocular and multiview reconstruction applications is competitive with current methods while achieving higher surface quality. This approach is also lighter than other Lagrangian representations in terms of memory and computational complexity.

### Weaknesses
The paper proposes a new Lagrangian primitive that is notably more complex than the primitives used in previous methods, such as 3D Gaussians or triangles. Each TetSphere consists of a collection of N tetrahedra, with an apparent trade-off between N and the total number of TetSpheres needed to represent the surface. This trade-off seems to be overlooked in the experimental section, as specific values for the number of TetSpheres and tetrahedra in each experiment are not provided. Furthermore, the analysis lacks a clear explanation of how this trade-off impacts both the reconstruction quality and computational cost. A more detailed exploration of this parameter space is needed to fully understand the method's efficiency and limitations.

The surface is represented as a union of TetSpheres. Due to the proposed splatting optimization, TetSpheres may intersect, leading to artifacts at the intersection points. However, the paper does not specify how intersections between tetrahedra are managed. This is a critical omission, as uncontrolled intersections could lead to significant surface irregularities and topological inconsistencies. The lack of a clear strategy for handling these intersections raises concerns about the robustness of the method, especially when dealing with complex geometries.


### Questions
The proposed optimisation does not appear to prevent non-uniform deformation of TetSpheres. However, the resulting reconstruction Aspect Loss Ratio (ALR) is higher than in other methods, suggesting that the tetrahedra within each TetSphere largely preserve their original volume. Is there any factor specifically contributing to the high ALR?


What are the values of N (number of tetrahedra) and M (number of TetSpheres) used in the experiments? How does the trade-off between these values affect reconstruction quality and computational complexity?

More details on the image-to-3D and text-to-3D generation pipelines are needed to ensure the experiments can be reproduced.
Figures 8 to 10 would benefit from captions with additional information about the experimental setup.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper uses tetrahedral spheres to represent three-dimensional shapes and constructs its corresponding differentiable inverse rendering process, which improves tasks such as single-view, multi-view reconstruction, and text to 3d shapes.

### Strengths
I think it’s a good idea to use tetrahedrons to represent shapes, which is very common in classical geometry processing. I’m excited to see that the authors were able to combine computer vision and geometry processing and make good progress on multiple tasks.

This new method surpasses or catches up with Sota methods on multiple data sets, and because it is based on the tetrahedron geometric primitive, it seems to be able to achieve better topology preservation, manifold preservation and better triangulation quality.

### Weaknesses
The implementation details of this paper are not enough for me, and many questions come to my mind when I read this paper.

1. The author does mention the problem of tetrahedron inversion, and cites theories from other papers to show that it is useful. I think it would be easier to understand if there is a simple ablation experiment.
2. The paper does not seem to mention how to extract the surface mesh from the tetrahedral mesh, which I think is also an important part of the whole pipeline. At the same time, how to ensure that there is no non-manifold when extracting the surface is also a problem. 
3. How to ensure that the topology is correct? If I understand correctly, this seems to be strongly related to "silhouette coverage", which must be consistent with the topology of GT. I would like to see an analysis of the Euler characteristic (Genus) in the tables.
4. This paper introduces many metrics to evaluate the quality of the mesh, but no corresponding references or mathematical definitions are given, like Manifoldness Rate and Connected Component Discrepancy. I hope to see their mathematical definitions in the appendix, which will make it easier for readers to understand. 
5. Regarding mesh quality, first of all, do all compared methods have similar resolution/triangle numbers? If mesh quality is to be compared, giving the triangle numbers is a must. It would be great if the authors could provide a metric for triangle quality, such as the Edge Chamfer Distance in NMC [Chen and Zhang. 2021] and TriangleQ in CWF [Xu et al. 2024].
6. In addition, since your initialization is multiple tetrahedralized spheres, what is the connection between the spheres? Are they multiple independent connected branches? If so, how to deal with the intersection between them, and how to ensure that the final mesh is an independent and connected one?
7. Citation problem, I found multiple citations of same paper in several places, such as One-2-3-45 line 648-653, Syncdreamer line 657-662 etc.

### Questions
My main doubts lie in the topological and manifold guarantees claimed by the authors, and I hope to see more detailed analyses and experiments to prove their method. I am also curious about the mesh extraction method and the number and quality of triangles. And if the code is attached, it will also increase the credibility of this paper.

Overall, I like this idea, but it seems to have a lot of minor issues. If the authors can address these issues during rebuttal, I will increase my rating.

### Soundness
3

### Presentation
3

### Contribution
3
