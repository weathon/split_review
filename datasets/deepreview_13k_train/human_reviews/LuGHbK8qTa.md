# Dynamic Gaussians Mesh: Consistent Mesh Reconstruction from Monocular Videos

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Modern 3D engines and graphics pipelines require mesh as a memory-efficient representation, which allows efficient rendering, geometry processing, texture editing, and many other downstream operations. However, it is still highly difficult to obtain high-quality mesh in terms of structure and detail from monocular visual observations. The problem becomes even more challenging for dynamic scenes and objects. To this end, we introduce Dynamic Gaussians Mesh (DG-Mesh), a framework to reconstruct a high-fidelity and time-consistent mesh given a single monocular video. Our work leverages the recent advancement in 3D Gaussian Splatting to construct the mesh sequence with temporal consistency from a video. Building on top of this representation, DG-Mesh recovers high-quality meshes from the Gaussian points and can track the mesh vertices over time, which enables applications such as texture editing on dynamic objects. We introduce the Gaussian-Mesh Anchoring, which encourages evenly distributed Gaussians, resulting better mesh reconstruction through mesh-guided densification and pruning on the deformed Gaussians. By applying cycle-consistent deformation between the canonical and the deformed space, we can project the anchored Gaussian back to the canonical space and optimize Gaussians across all time frames. During the evaluation on different datasets, DG-Mesh provides significantly better mesh reconstruction and rendering than baselines.
\keywords{Dynamic Scene Reconstruction \and Surface Reconstruction \and Neural Rendering}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The proposed method uses two representations jointly to model a 3D object over time from forward-facing monocular video to produce state of the art results on publicly available datasets. The method produces a volumetric representation anchored to a mesh and can be used to track the deformation of the object over time. The tracked mesh can then be manipulated such as editing the texture. To achieve this, the proposed method uses Gaussians anchored to a canonical mesh using a forward / backward deformation field and Gaussian merging / creation rules based on mesh vertices. The method uses DPSR, DiffMC and laplacian regularization to generate intermediate meshes.

### Strengths
The paper is well written and follows a fairly intuitive and novel approach to generating both a deformable mesh and gaussian representation in parallel leveraging the benefits of both representations in the loss functions. The method performs at interactive speeds during inference while producing high quality results both qualitatively and quantitatively for both the mesh and Gaussian representations. The paper is evaluated on a variety of both real-world and synthetic datasets and produces tracked results using the forward / backward deformation of a canonical mesh. This is likely a significant improvement in learning deformable 3D scenes.

### Weaknesses
 - The paper demonstrates that using both Gaussians and meshes improves the overall quality of novel view synthesis. There are several qualitative examples of higher quality meshes but it is unclear how / if appearance improves between the baselines and the proposed method when the underlying geometry is of similar quality.
- There is a lack of rigorous quantitative evaluation for several key decisions such as choosing the initialization, DMTet/DiffMC/FlexiCubes, mesh anchoring frequency and the training methodology and relies on qualitative observations. While these qualitative observations likely hold up well, having quantitative evaluations of various modules is desirable.

### Questions
- What's the intuition behind the improvement when using both Gaussian and mesh rendering losses?
- How would the method handle a synthetic large textured but planar surface such as a checkerboard where there might not be enough vertices to anchor gaussians to?
- In the attached supplementary materials, the anchored gaussians are represented as blue dots. What do these blue dots represent - is it just the mean positions?
- How is the "canonical" frame chosen given that the input video sequence is monocular and the scene is not static? Can you share more details about about the (frozen) initialization of the forward / backward deformation networks when training the canonical Gaussians and the SfM initialization?
- Are there any qualitative observations relating to decomposition of geometry / appearance information between the mesh representation and the gaussians?
- How do you arrive at running mesh anchoring every 100 iteration? Is it possible to perform differentiable mesh anchoring?

### Soundness
4

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
The paper introduces Dynamic Gaussians Mesh (DG-Mesh), a novel framework designed to reconstruct time-consistent, high-fidelity meshes from monocular video footage. Utilizing 3D Gaussian Splatting (3DGS), the framework ensures temporal consistency and superior mesh reconstruction quality. Innovations such as Gaussian-Mesh Anchoring and cycle-consistent deformation significantly enhance the distribution and stability of 3D Gaussians across frames.

### Strengths
1. The manuscript is well-structured, with fluent writing and a clear explanation of methods, making it easy for readers to understand.

2. This method combines the advantages of Mesh and 3D GS and achieves remarkable improvements in surface detail and rendering quality in dynamic object reconstruction.

3. The experiment is thorough, with comprehensive benchmarks against established methods, demonstrating significant enhancements in both mesh quality and image rendering.

### Weaknesses
1. The integration of 3D Gaussians with mesh surfaces is good, yet the paper does not explore the potential benefits of using 2D Gaussian Splatting for surface and image reconstruction accuracy. Could a 2D representation be more effective or efficient when Gaussians lie on the mesh surface?

2. The method involves separate rasterization processes for Mesh and 3D Gaussians. However, the paper lacks a detailed explanation of how color information is harmonized between these components. How is color from the 3DGS sh presentation passed to the mesh during rasterization?

3. Binding a single Gaussian to each mesh face raises questions about the distribution logic. Why was this strategy chosen? Did the authors consider alternatives, such as placing multiple Gaussians on a single mesh face or varying the number of Gaussians based on mesh face properties?

4. Table 1 only presents PSNRm metrics; however, standard PSNR metrics for direct 3DGS rendering results are absent. Could the authors clarify the reason for this omission?

5. The paper does not address how varying the number of mesh surfaces extracted from the same scene affects rendering accuracy and computational efficiency.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a method for using deformable Gaussian Splatting to generate dynamic meshes for each frame of a monocular video. It employs a set of canonical Gaussians, deforming them at each timestep with an MLP. These deformed Gaussians are then used to construct a mesh for each frame through Poisson Reconstruction and Marching Cubes. The mesh serves as an anchor for the Gaussians, ensuring a one-to-one correspondence between mesh faces and Gaussians. Instead of textures, vertex colors are applied to the mesh, which is rendered as an image for supervision.

The paper is clear and straightforward, though it does have some limitations. The resulting mesh is a per-frame set rather than a truly deformable mesh. Additionally, the mesh is colored using vertex colors instead of a high-resolution UV map. These constraints raise concerns about the method’s applicability.

### Strengths
The paper sets an ambitious goal: reconstructing dynamic meshes from monocular videos, a critical challenge in graphics and vision. It begins with a baseline approach using Deformable GS to model the dynamic scene. Mesh reconstruction is then applied to each frame, incorporating an anchoring constraint on the Gaussians through the mesh. This approach helps achieve a smooth surface but can adversely affect the rendering results.

### Weaknesses
Here are the weaknesses of the paper:

1.  **Mesh Representation:** The method produces a set of per-frame meshes rather than a deformable mesh. Although mesh representations are known for their rich operations and memory efficiency, the paper does not demonstrate how to register each frame to a unified mesh. This per-frame approach is not memory-efficient and makes editing geometry and textures cumbersome, as changes cannot be easily propagated across frames without manual effort. Specifically, the lack of a consistent mesh topology across frames prevents the application of standard mesh processing techniques, such as mesh smoothing or remeshing, which typically rely on stable vertex connectivity. Furthermore, without a unified mesh, it is difficult to track surface points across time, hindering tasks like motion analysis or temporal feature tracking.

2.  **Detail Preservation:** The mesh optimization and anchoring mechanism do not preserve details effectively, as demonstrated in Table 1. While meshes efficiently represent low-frequency geometry, high-frequency textures should ideally be stored in a UV map. This method colors the mesh at vertices, limiting its ability to capture high-frequency details. The one-to-one mapping between mesh faces and Gaussians necessitates a high-resolution mesh to accommodate the large number of Gaussians needed for rich texture and geometry representation. However, the mesh number is limited by the resolution of Marching Cubes and is hard to increase as much as needed Gaussians. This results in inefficient memory use, as mesh faces are not effectively utilized for storing detailed textures. The vertex coloring approach also suffers from interpolation artifacts, especially in areas with sparse vertex distribution, leading to a loss of fine-grained texture details.

3.  **Missing Related Works:** The paper omits several closely related works:
   - "SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes" by Huang et al.
   - "Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis" by Li et al.
   - "Neural Parametric Gaussians for Monocular Non-Rigid Object Reconstruction" by Das et al.
   
   It is recommended to compare with **SC-GS** in Table 1, as it is the current state-of-the-art method in this area. It's not necessary to overwhelm its result since the focus of the two papers differs.

### Questions
1. Is there a way to unify the per-frame meshes into a deformable mesh? Once unified, this mesh could be optimized with a UV map to capture rich texture details. Neural temporal textures might also be useful, as they can address inaccuracies in deformation correspondence across frames by providing time-dependent texture adjustments.

2. Can DG-Mesh be used to obtain a skeleton and skinned mesh? Extracting animatable assets from dynamic videos is crucial. This could be suggested as a potential enhancement in the future work section. The paper can articulate how it advances the field toward this goal to some extent.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a method to extract high-quality mesh from image inputs in monocular/ efficient multiview setups. The authors propose a Gaussian-Mesh anchoring method and cycle-consistent deformation loss to enhance the upper bounds of DG-Mesh representations. The authors propose many downstream tasks to demonstrate the widely applications of DG-Mesh.

### Strengths
1. This study presents a novel framework that enables the reconstruction of high-fidelity, time-consistent meshes from monocular videos. Generating meshes for dynamic scenes is a challenging yet critical task, and the author makes a significant contribution in addressing it.

2. The proposed approach includes a Gaussian-Mesh anchoring technique that produces uniformly distributed Gaussians in each frame, enhancing the effectiveness of mesh reconstruction. Cycle-consistent deformation loss adjusts the deformed Gaussians, offering a new method for densification in deformation-based 3D Gaussians.

### Weaknesses
1. **Baseline Selection:** I suggest that the authors consider incorporating additional baselines such as Spacetime-GS (Li et al., CVPR 2024), 4DGS (Yang et al., ICLR 2024), and 4D-GS (Wu et al., CVPR 2024), given the recent advancements in Dynamic Gaussian representations. It would also be helpful to include some NeRF baselines in the supplementary materials.

2. **Color Prediction:** As mentioned in Section 4.2, the mesh is extracted using Nvdiffrast. How do the authors handle the color extraction for the mesh? Is the DG-Mesh representation used for this purpose? If so, why? I find it challenging to apply this approach in real-world scenarios.

3. **Real-World Monocular Scenes:** In my opinion, DG-Mesh is still difficult to apply in real-world settings, as the original 4D representations struggle to maintain multi-view space-time consistency. While the results appear satisfactory in training views, they might deteriorate in novel views or the final extracted mesh. I recommend that the authors emphasize the robustness of multi-view videos rather than focusing solely on monocular videos. In terms of monocular dynamic scene reconstruction, there are several relevant works (e.g., MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds, Dynamic Gaussian Marbles, Shape of Motion, Dreamscene4D, MoDGS) that have yet to deliver satisfactory results. Claiming effectiveness in monocular videos might be an overstatement.

### Questions
Please refer to weakness. 
Overall, I think this is a pioneer work and My main consideration is weakness2,3.

### Soundness
3

### Presentation
4

### Contribution
3
