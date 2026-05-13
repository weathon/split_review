# Smooth Real-time Rendering via Implicit Nested Neighborhoods

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Implicit neural representations (INRs) for surfaces have been mostly used as intermediary representations before triangle mesh extraction. Extracting meshes is not a real-time task and introduces unnecessary discretization to rendering, making it difficult to fully use the smoothness of INRs in applications. Smooth INRs are broadly used for approximating surface \textit{signed distance functions} (SDFs) through an implicit regularization (Eikonal equation) using their available high-order derivatives. Such property also makes it easier to integrate those INRs in pipelines that explore differentiable properties of the underlying surface. The current real-time state-of-the-art approach uses grid-based data-structures that introduce discretization, resulting in a non-smooth representation.

We propose an end-to-end smooth ($C^{\infty}$) INR framework to represent and render surfaces in real-time using neural SDFs endowed with smooth attributes such as normals and textures. Our approach leverages from a novel localized SDF training based on nested neighborhoods, a multiscale surface representation, and residual training. The framework does not depend on spatial data-structures, nor surface extraction. We show that our representation renders detailed smooth surfaces in real-time while the previous works can only render coarse non-smooth surfaces. We also present applications of our representation, including integration with a pipeline for dynamic surfaces and a way to improve performance of surface extraction via marching cubes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a method for learning implicit neural representation of smooth closed surfaces (like small objects) with texture and normal, initialized with point cloud and normals. The proposed method is end to end differentiable allowing direct use of the INR for rendering, avoiding the need to extract explicit triangle meshes. 

This is achieved by learning the surface representation as multiscale SDF and rendering with multi-scale sphere tracing. The multiscale SDFs are defined in a nested manner, coarse surface S1 - coarsest SDF f1, S2 is nested in the neighborhood of f1, and so on. The nested SDFs are rendered using proposed multiscale sphere tracing. The authors also show analytical computation of normals using GEMM which is fast (does not need auto-grad). 

The results are shown on classic toy dataset, single objects like Armadilo, Buddha, Bunny, etc. and compared with two methods IDF and NGLOD.

### Strengths
Originality and quality: The paper proposes a sound multiscale SDF representation and show how such a representation can be effectively learned and used for real-time rendering. The paper builds on top of concepts from previous works, but to the best of my knowledge, the specific proposed representation and corresponding learning framework (loss formulation, nested neighborhoods, attribute mapping) are novel and well-grounded. Experiments provide decent validation but conducted on a small number of simple synthetic objects. 

Clarity: The paper is generally written well and provides adequate level of detail with clear notation, however the explanation can be made clearer (more on this in Weaknesses). 

Significance: While the results are evaluated on toy dataset with pristine inputs, the author show one example of real-world usecase in Fig 13. The limitation of smooth surfaces (cannot represent sharp edges) is somewhat limiting for real-world objects but in my opinion the community will find value in the proposed approach and such limitations can perhaps be overcome by future works.

### Weaknesses
 - The paper is decently written but the authors can improve the writing and flow of information better to make it easier to follow. I had to go back and forth a few times to get to the key ideas. Section 3.1 Overview can be used to provide gist of the framework since notations are subsequently introduced in good detail. Section 3.5 can also be explained more clearly.   

- It is mentioned in the abstract: "Extracting meshes is not a real-time task and introduces unnecessary discretization to rendering". There are many advantages of explicit triangle meshes, while extracting meshes is not a real-time task, learning SDFs is also not a real-time task. I don't find this motivation fully convincing and I would be curious to know how the method fares with respect to explicit meshing from SDF in terms of rendering quality and performance. 

- A relevant work is Deep Marching Tetrahedra (Shen et al) that learns implicit surface representation and extracts a mesh in a differentiable manner. There are also follow up works. I think this class of methods are worth discussing and comparing against.

### Questions
- Did you experiment with more complex real-world datasets such as ShapeNet or 3D objects from Objaverse? 
- Given the end-to-end differentiable nature of the proposed approach, will this method be applicable for image based surface representation learning? [similar to VolSDF (Yariv et al) and follow ups]

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents some novel ideas for implicit 3D representation and rendering: nested implicit surfaces for multi-level surface details, neural attribute mapping for highly detailed normals and colors, and a corresponding multiscale sphere tracing algorithm to render these surfaces in realtime. The authors demonstrate a couple of useful applications of their representation for surface morphing and speeding up marching cubes.

### Strengths
The nested implicit functions, where next level is within a small shell of the previous level, is a natural and convenient way to achieve multiple scales of detail. Mapping attributes from an even higher-detail implicit than the surface is a good way to increase detail while keeping the sphere-tracing time shorter.

### Weaknesses
The writing could be improved to read more smoothly. I will outline major feedback here and more detailed comments under Questions.

The abstract does not clearly present the gist of this work. The first paragraph seems to serve only as related work overview, but is missing motivation. 1) Why do we care about surface representation -- the proposed representation can encode enough visual detail for rendering in games/movies and can easily be integrated into ever-improving ML algorithms? 2) Why do we care about realtime rendering -- the proposed algorithm can be used to speed up training (when minimizing an error between a rendering and a target image), and/or is somehow more suitable for interactive applications (games) than triangles? The second paragraph is clear until the very end where some applications are listed  -- does this representation unlock new applications, or is it just applicable in these applications along with other representations? You may want to just say "we demonstrate the utility of our representation in several real-world applications."

The paper mentions "normals and textures" several times. This should probably be "normals and colors" as those are the attributes it learns to represent and compute at each point. Texture invokes traditional "texture mapping" where a coarse surface representation can use texture coordinates to interpolate much higher-resolution (and not necessarily smooth) colors from an image.  I think the paper would be clearer if it says color instead of texture.

It seems that effort has been put into squeezing as much as possible into the 10 page limit, which results in a busy layout and no references to figures tables in the text. This complicates the flow of the paper, as we do not necessarily know when to refer to a certain figure.

Figure 2: How come q1 is not on the surface s1? If q2 is on S2 and q3 is on S3, it would feel more consistent if q1 was on S1. Is this because the view ray needs to be traced until the most detailed surface point is reached (which is on S2), and then a different normal ray can be traced to find the point on S3 that only contributes the attribute value (not position)? In that case, N2 is unnecessary and only clutters the image.  In addition, looking at algorithm 1, even q2 should not lie on S2, because for j < 3 we trace until Sj-dj. Maybe more work is needed to reconcile the figure and the algorithm.

Finally, I believe a more suitable venue for this would would be a vision or graphics conference (e.g. CVPR, ICCV, Siggraph).

### Questions
Line 049: "GEMM-based normal computation" should be accompanied by the GEMM reference, as it is the first mention of it.

First line of Overview should spell out "Sphere Tracing (ST)" as its initial definition is deep in the dense previous work paragraphs.

Figure 1: By "normal mapping algorithms" did you mean to say a more general "attribute mapping algorithms"?

Line 153: Phrase "compute it first intersection point q2" should be fixed to "compute its S2 intersection point q2".

Figure 3: Should "using too large d1 == d2" instead say "using too large d1 or d2"? Does it matter that they are equal, or does it matter that they are too large?

Reference to "Local Deep Implicit Functions for 3D Shape" by Genova et al. could be added as an example of using multiple smaller implicit representations to increase detail of the whole representation.

Section 4, why don't you just let (N, d) mean MLP with "d" hidden layers? Why the need to add 1, it only adds confusion.

Figure 7: Could you add shaded surfaces, so that we can judge how good the normals are? It is hard to judge the normal visualization.

Figure 9 is quite confusing as it covers multiple concepts. What does the left-side vs right-side of the middle image (armadillo) mean? Is one a mesh and the other a mesh with neural normal mapping?

### Soundness
3

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
The paper proposes to accelerate sphere tracing using hierarchical SDFs achieving real time performance. The neural SDFs are trained based on nested neighborhood efficiently. The paper also proposes a GEMM-based normal computation. The experiments show that textured 3D models are able to be rendered in real time without surface extraction.

### Strengths
The work generalizes sphere tracing method to multiscale sphere tracing. Taking advantage of the multiscale SDFs, the method is able to accelerate the sphere tracing.

The method is also able to render highly fidelity textures. The results look good in the experiments.

The method is highly efficient. It accelerates the rendering efficiency several times than SOTA.

### Weaknesses
To use more neural SDFs increases the training time and storage space. It is also slow for mesh extraction. Moreover, the residual SDFs are not stable to learn, which may result in artifacts. Specifically, the training time increases linearly with the number of residual SDFs, and the memory footprint grows as well. The mesh extraction process, which relies on iterative refinement, becomes computationally expensive with multiple SDFs, particularly when high-resolution meshes are desired. The instability of residual SDFs can manifest as oscillations or discontinuities in the reconstructed surface, leading to visible artifacts, especially in regions with high curvature or complex geometry.

The parameters $\theta_i$ may be sensitive. Smaller ones may result in errors, but larger ones affect the efficiency. How to trade off them? Is it appropriate to use global $\theta_i$? Perhaps, location varying $\theta_i$ is a better choice. The choice of $\theta_i$ directly impacts the accuracy and performance of the sphere tracing algorithm. If $\theta_i$ is too small, the sphere tracing may terminate prematurely, leading to inaccurate surface intersections. Conversely, if $\theta_i$ is too large, the algorithm may take excessive steps, increasing the computational cost. Using a global $\theta_i$ may not be optimal for all regions of the surface, as some areas may require finer or coarser steps. A location-varying $\theta_i$ could potentially adapt to the local surface complexity, but it also introduces additional computational overhead.

### Questions
I wonder the geometric accuracy of the rendering surface. This is an important factor to evaluate the method.

IDF took about 40 mins for training, but it took only 100s in this work. The proposed method took about 150s for training, which is also efficient. How does the work achieve such improvement?

The rendering results are glossy. Does the method support BRDF material for rendering.

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
The paper proposes a method for representing and rendering 3D shapes using implicit neural representations (INRs). Starting from an oriented and colored point cloud, it fits an SDF network with color and normal information. The network operates at three levels of detail to accelerate sphere tracing: a coarse, fast network for regions far from the surface, and more precise, slower networks when closer to the surface. An orthogonal projection maps surface normals and colors from detailed to coarser representations, preserving visual details, and accelerating rendering. Additionally, the paper introduces a GEMM (general matrix multiplication)-based approach for computing surface normals, which is twice as fast as PyTorch autograd.

### Strengths
* Introduces a multi-level network approach to accelerate sphere tracing.
* Employs orthogonal projection to transfer visual details to coarser representations.
* Proposes a GEMM-based method for faster computation of surface normals.
* Overall, many aspects of surface implicit rendering are discussed

### Weaknesses
 * The purpose and practical use cases of the pipeline are not clearly defined:
    * If rendering speed is the main purpose, how does it compare to simply rendering a mesh? Meshes are discarded very early because they are “not efficient, nor continuous, nor scalable” (line 40). But the presented approach requires roughly 150 seconds to process a moderately complex input geometry (Armadillo, table 1), on an RTX 3090, so scalability is also a concern. At least, there is a tradeoff between rendering speed, memory consumption, and pre-processing. That should be mentioned and quantified. Furthermore, the claim that meshes are not continuous is misleading, as a mesh can represent a continuous surface, although its representation is discrete. The authors should clarify that they are referring to the lack of differentiability of the mesh representation, not its continuity.
    * One motivation is to “fully use the smoothness of INRs”, but this is never quantified or motivated. When do we need shapes to be very smooth? Ironically, the “lack of sharp features” is cited as a limitation of the method. Therefore I struggle to get the motivation about smoothness. The authors should provide specific examples of applications where high-order derivatives of the surface are required, and explain why meshes are not suitable for those cases. The current explanation lacks concrete use cases and a clear justification for the smoothness requirement.
    * Demonstrations are limited to a few synthetic examples. Applicability to real, noisy RGB point clouds is uncertain. The paper should include experiments with real-world data, demonstrating the robustness of the method to noise and varying point densities. The current experiments do not provide sufficient evidence of the method's practical applicability.


* Some contributions, like the acceleration of marching cubes (Sec 4.5), are already established in existing literature - see BACON (Lindell et al.). The paper should clearly acknowledge that the acceleration of marching cubes is not a novel contribution, and instead focus on the specific aspects of their method that are unique.
* One important technical mistake: In sec. 4.5, the interpolation between genus 0 and genus 1 shapes is presented as a “demonstration that [the] representation can be integrated into differentiable pipelines”. But this is pure interpolation, not driven by any gradient descent. The authors should correct this claim and clarify that the interpolation is not a result of a differentiable process, but rather a simple blending of two shapes.


* Clarity can be improved:
    * About the GEMM-based acceleration of normal computations:
        * Section 3.6 is not motivating it. Why is it required for the paper’s objective of fast rendering? How much would the frame rate drop? The authors should provide a clear explanation of the bottleneck that the normal computation addresses, and quantify the performance gain achieved by the GEMM-based approach. Without this, the contribution seems arbitrary.
        * It also fails to convey an intuition as to why the method is faster than pytorch: less FLOP? Fused operation? The authors should provide a more detailed explanation of the computational advantages of the GEMM approach, including a comparison of the number of floating-point operations and memory access patterns with the PyTorch autograd method. A more in-depth analysis of the performance characteristics is needed.
    * The abstract and introduction uses confusing terminology without proper upfront definitions. For example, the abstract mentions “localised SDF training based on nested neighborhoods”, but the reader cannot  know what it means before having read the paper. So this is not descriptive, whereas a “network ensemble with 3 levels of details” would be clearer. The authors should revise the abstract and introduction to use more accessible and descriptive language, avoiding jargon that is not immediately understandable to the reader.

* Minor issues:
    * delayed acronym definitions of GEMM (used on line 53, defined on line 80)
    * misplacement of tables and figures disrupt reading flow: for example Tab. 5 is mentioned on page 7, but appears on page 10.

Overall, the paper reads like a collection of techniques that are not really novel or insightful, and are sometimes poorly explained or unmotivated. The aggregate of these techniques does not fulfil a clear cut objective.

### Questions
Based on the above weaknesses:
* What are the intended purposes and practical scenarios for this pipeline? Can the method work on real, noisy RGB point clouds, or is it limited to synthetic data?
* How does this method compare to traditional mesh rendering techniques in terms of efficiency and scalability?
* When is the smoothness of INRs necessary?
* Why is the GEMM approach faster than PyTorch autograd? Does it reduce computations, use fused operations?
* What specific problem does the GEMM-based acceleration address? How much does the frame rate drop without it?

### Soundness
2

### Presentation
2

### Contribution
2
