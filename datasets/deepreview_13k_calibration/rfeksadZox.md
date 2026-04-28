# High-quality Text-to-3D Character Generation with SparseCubes and Sparse Transformers.

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Current state-of-the-art text-to-3D generation methods struggle to produce 3D models with fine details and delicate structures due to limitations in differentiable mesh representation techniques. This limitation is particularly pronounced in anime character generation, where intricate features such as fingers, hair, and facial details are crucial for capturing the essence of the characters.

In this paper, we introduce a novel, efficient, sparse differentiable mesh representation method, termed SparseCubes, alongside a sparse transformer network designed to generate high-quality 3D models. Our method significantly reduces computational requirements by over 95% and storage memory by 50%, enabling the creation of higher resolution meshes with enhanced details and delicate structures. We validate the effectiveness of our approach through its application to text-to-3D anime character generation, demonstrating its capability to accurately render subtle details and thin structures (e.g. individual fingers) in both meshes and textures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel method to produce detailed 3D generation with less computational cost and training time. Specifically, the authors propose a sparse differentiable mesh representation called SparseCube to enable more efficient modeling of 3D subjects. Correspondingly, a sparse transformer network is designed to replace tri-plane to accommodate the proposed 3D representation. Through extensive evaluations, the novel 3D representation is demonstrated to be better than DMTet, implicit representation, and voxels. Meanwhile, the experiments showcase the best performance of the proposed method and the effectiveness of each component.

### Strengths
+ The paper introduce a novel 3D representation, called SparseCube. It's capable of capturing the details while largely decreasing the computational cost and training time.

+ The proposed method is demonstrated to perform better than existing techniques.

+ Extensive experiments have been provided to demonstrate SparseCube's superiority over DMTet, voxels, and implicit representations.

### Weaknesses
 - The paper would benefit from further refining the paper structures and polishing the writings.

- The geometry quality in Fig. 1 and Fig. 5 is not good.

- What are the results and comparisons in general 3D avatars like "people wearing daily outfits" or movie characters like "Iron Man"?

- There are no comparisons with human-specified methods like Human-LRM or more recent 3D generative methods like 3DTopia, 3DTopiaXL, etc.

- The design of the features within SparseCube is not well-justified.

### Questions
Considering the above strengths and weaknesses, I currently still lean toward a positive rating. I would like to hear from the other reviewers and the authors during the rebuttal.

### Soundness
3

### Presentation
2

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
This paper introduces SparseCubes, a new method for improving text-to-3D generation of anime characters. SparseCubes uses a sparse mesh representation that cuts computational needs by over 95% and storage by 50%, allowing for better detail in 3D models. The authors demonstrate its effectiveness in accurately rendering delicate features in anime character generation.

### Strengths
1. This paper presents the SparseCubes representation, which can capture fine details like fingers and hair.

2. A corresponding transformer network is designed for the SparseCubes representation

3. A significant efficiency improvement compared to previous methods

### Weaknesses
Method:

1. High-resolution voxels have already been used to generate smooth meshes in DMTet and FlexibleCube. Improving efficiency and increasing resolution through a sparse design is a straightforward idea, which somewhat affects the novelty of the work. The core idea of using a sparse voxel representation to reduce computational overhead, while beneficial, lacks significant innovation beyond existing voxel-based methods. The paper does not adequately address how its specific sparse implementation differs fundamentally from other sparse voxel techniques, especially in the context of 3D mesh generation.

Experiments:

1. The paper lacks a comparison of results using FlexibleCube as a post-processing step. It is unclear how the proposed method compares to a baseline where a dense voxel method like FlexibleCube is used as a post-processing step, which could provide a more direct comparison of the benefits of the sparse representation. 

2. The experimental results are somewhat confusing: First, the quantitative improvements in PSNR and SSIM on the anime avatar dataset are quite small, and an explanation for this is needed. Additionally, the qualitative comparisons provided for the LVIS subset make it difficult to discern clear differences. The paper should provide a more in-depth analysis of why the quantitative metrics show only marginal improvements, and the qualitative results need to be presented in a way that makes the differences more apparent. The lack of clear visual differences in the LVIS subset raises concerns about the practical impact of the proposed method in real-world scenarios.

3. The paper lacks a comparison with the current state-of-the-art method, CharacterGen[1], including both qualitative and quantitative comparisons. The absence of a direct comparison with CharacterGen[1], which is a relevant and recent method in the field, makes it difficult to assess the true advancement of the proposed method. This comparison is crucial to establish the significance of the contribution.

4.  For the qualitative results of the anime avatar dataset, the main text focuses on only a few selected IDs. It would be beneficial to include comparisons for more IDs in the experiments. The limited number of qualitative examples in the main text makes it hard to generalize the findings. A more comprehensive set of comparisons would strengthen the validity of the results.

### Questions
1. Is the entire training process conducted in stages, or is it an end-to-end process?

2. The results on the real human dataset only include quantitative metrics and lack qualitative results for comparison.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper targets to solve the high-resolution mesh generation problem with text prompts. 
It argues the current text-to-mesh methods are mainly bottlenecked by the cubical memory usage to generate high-resolution meshes,
which leads to the limitation of the mesh resolution, and the quality of the generated meshes.
This problem is believed to be in particular severe for human-like/character-based meshes, like fingers, hair, fur, etc.

To solve this problem, this paper introduce the sparseCube and the sparse transformer. 
It first generates a low-resolution (32x32x32) grid to obtain a mesh in a differentiable manner, and then sparsifies the grid to get a sparse grid.
Finally, it uses a sparse transformer to generate the high-resolution mesh from the sparse grid.
This paper compares the proposed method on objaverse and human character datasets, and demonstrating the effectiveness of the proposed method.

### Strengths
1. The overall pipeline is sound and reasonable. Utilizing the sparsity of voxel grid, we can pursue the high-resolution meshes (using FlexiCubes), leading to high-resolution 3D assets generation. 
2. This paper is well written: the story and method is easy to follow and understand.
3. Results look great.

### Weaknesses
Overall, the contribution of this project is OK but mild. 
This paper utilizes the idea of Flexicubes to train a model to predict the 3D voxels for a mesh, and renders the 2D images from the 3D mesh in a differentiable manner, which is a still in the scope of Flexicubes.
The main contribution of this paper should be utilizing a sparse transformer to do refinement or upsampling for the 3D voxels after pruning. 
This is a sound idea while not novel. 

Some weakness: 

1. I think there are some baselines missing. In particularly, XCUBE [XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies]. Although XCUBE uses diffusion model for generation and its output voxel grids are supervised by 3D loss, but it also highlights a sparse voxel grid solution (a novel data structure and companying network to process it). I am curious can you use XCUBE's sparse voxel grid method (fvdb) to do the same thing as yours? And compare the speed, memory and performance difference? I am very curious about how the proposed method. is compared again the XCUBE's backbone. Also, SparseConv-Unet might be another reasonable  backbone to compare against the Sparse Transformer. 

2. In table 1, the proposed method takes 20 s to generate, which is slower than InstantMesh. I am curious as a feed-forward model, why it is slower? And what's the time using ratio of each component?

### Questions
1. I am a little bit confused about the relationship between 3D character generation and sparse CUBE/Transformer. For sparse cube/transformer, it seems they can work on any 3D content generation without any specific constraints like character. So I am curious why this paper mainly argues about 3D character generation? I can understand 3D character has some very thin structures like hair, fingers, but I still think generating high-quality 3D mesh would be a common interest for 3D generation, whatever the objective is. 
2. Just for clarification, the renderer (from 3D mesh to image) is the same as FlexiCubes or not?
3. For sparse transformer, do you apply position encoding (more specifically, the 3D location/index of occupied cubes) ? If so, how do you do that?
4. It would be helpful to evaluate the results just after the coarse proposal network, and after prunning, to show how much gains we get from the sparse Transformer as a refinement stage.

### Soundness
2

### Presentation
3

### Contribution
1
