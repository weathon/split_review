# Neural implicit mapping via nested neighborhoods: real-time rendering of neural SDFs with textures

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
We introduce the nested neighborhood model, a framework to address the problem of real-time joint estimation of surface geometry and its attributes (normals and textures) from neural SDFs.
This problem was only partially approached by previous works, which do not support attributes nor dynamic surfaces in real-time.
The framework is built on the nesting condition, which establishes a criteria for the neighborhoods of zero-level sets of a sequence of neural SDFs to be nested. This allows mappings between such neighborhoods, enabling the definition of the multiscale sphere tracing, the neural attribute mapping, and the GEMM-based analytical normal computation algorithms, composing the nested neighborhood model.
Our framework does not use spatial data-structures and its components can be used to augment meshes with smooth neural normals and textures. The normal GEMM-based computation does not depend on auto-differentiation nor computational graphs, resulting in real-time performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tries to achieve real-time rendering of neural signed distance fields (SDF) with attribute mapping, like normal map and texture map. The core of its algorithm is multi-scale sphere tracking through nested fields with level-of-details. It claims to accelerate the computation of surface normal using an efficient GEMM-based implementation. The paper also extends the same set of tools for dynamic neural SDF.

### Strengths
- This paper considers lots of useful aspects of neural rendering, level-of-details, texture mapping, normal mapping, and multi-scale sphere tracing without spatial data structure. And this paper uses the concept of nested neighbors to combine these concepts together, making it interesting to read.
- The proposed algorithm is fast and capable of rendering high-resolution details, as demonstrated through several overfitting experiments.

### Weaknesses
 - Some extra experiments can be added to provide more insight into the proposed method: 
    - The author does not provide an evaluation of the speedup or the proposed GEMM-based implementation of surface normal computational. It's unclear how much the GEMM implementation accelerates normal computation compared to standard auto-differentiation, which also leverages GEMM. A direct comparison of computation time is needed to substantiate this claim.
    - In general, this algorithm uses more memory (coarse surfaces and finer surfaces) to trade speed. So, how does the speed compare with using extra spatial data structures, like bounding volume hierarchy for faster Ray surface intersection? The paper should benchmark against methods using spatial acceleration structures to understand the trade-offs between memory usage and rendering speed. Without these comparisons, it's hard to assess the practical advantages of the proposed approach.
    - It is better to replace the MSE metric with PSNR when evaluating the image reconstruction quality, for example, in Table 8. MSE does not directly reflect perceptual image quality, making it difficult to judge the visual fidelity of the reconstructions. PSNR would provide a more interpretable measure of image quality.
- The author needs further evidence to justify the concept of "nested SDF sequence" in this paper. There are two crucial question related to this concept
    - The author does not explicitly bound the sequence of SDF, neither through training regularization nor some explicit normalization. The concept of nested SDF sequence is only mentioned in deriving the algorithm, but in the experiments, it is not guaranteed to be nested. Does it mean that for most of the popular neural SDF with level-of-detail design, without any explicit control of the bound of nested SDF, the proposed algorithm will always converge effectively? The lack of explicit bounds or regularization could lead to unpredictable behavior and convergence issues. It is necessary to show that this approach is stable across different network architectures and training parameters.
    - The tightness of the bound and how the tightness affects the algorithm is not analyzed and demonstrated. The paper needs to explore how different bounds influence the performance of the algorithm, including rendering speed and accuracy. Without this analysis, it's hard to determine the optimal configurations for the nested SDFs.

### Questions
- I don't understand why the GEMM-based implementation will accelerate the normal computational. I thought auto-diff will also use GEMM to compute derivatives. Can you explain it more? Also, measuring the speed of normal computations will make this point more solid. 
- In most of your experiments, you only use two nested SDF. What if you use more? Like, 3 to 5, even to 10 neural SDF?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a nested neighborhood model for real-time neural SDF rendering, emphasizing the efficiency of their normal computation method, based on General Matrix Multiply (GEMM) operations, which eliminates the need for auto-differentiation and computational graphs. The evaluation focuses primarily on Instant NGP and offers intuitive visualizations of the rendering results.

### Strengths
1. The concept of normal computation using GEMM operations without relying on auto-differentiation or computational graphs holds promise for real-time rendering applications.
2. The paper is well-written and includes mathematical analysis, although as a reviewer without a strong background in computer graphics, I cannot thoroughly evaluate the rigor of the mathematical aspects.
3. The evaluation against Instant NGP provides compelling evidence of efficiency, and the visualizations are visually impressive.

### Weaknesses
The major concern is the lack of reproducibility due to insufficient implementation details.

### Questions
1. The details provided may make it challenging to reproduce the results. Providing an implementation or a demo for readers to run would enhance the paper's credibility and make the results more accessible.
2. Table 4 suggests that a larger MLP leads to a more accurate zero-level set. It would be beneficial to discuss the theoretical limits or boundaries for achieving perfect results with different MLP sizes.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of real-time rendering for neural SDFs. It has 3 major contributions.
First, since neural SDFs are expensive to evaluate, the sphere tracing algorithm becomes too time-consuming. This work introduces multiscale sphere tracing where simpler MLPs are used to represent coarser SDFs which can be used for earlier iterations of sphere tracing.
Next, the paper introduces neural attribute mapping to allow normals and textures encoded in space to be mapped onto SDF or mesh surfaces. This techniques enable higher quality rendering.
Next, the paper improves normal computation for MLP-based neural SDFs with a GEMM-based algorithm.

### Strengths
- The paper introduces a novel acceleration method for sphere tracing of neural SDFs and a fast implementation for MLP gradients.
- The concepts and theories of multiscale sphere tracing and nested SDFs are explained clearly.
- The method does not rely on spatial data structures, thus is more suitable for representing dynamic neural surfaces.

### Weaknesses
 - The paper does not make the setups of experiments sufficiently clear.
  - The method and experiments section of this paper explains the architecture of the proposed nested SDF representation, however, it is hard to see what are the inputs to the experiments and what are the losses without reading appendix (A.3).
- The comparison with Instant-NGP (Table 2) seems misleading.
  - If I understand the setting of the experiment correctly, the proposed method is trained with ground-truth SDF and color supervision, while the Instant-NGP is trained with multi-view image supervision. These are drastically different settings.
  - The images for Instant-NGP are generated with a renderer, thus COLMAP should not be required since it is used for camera pose estimation. Thus the speed comparison seems to be misleading.
- Missing comparisons with other representations.
  - Instead of comparing with Instant-NGP, the proposed nested SDF representation should be compared to a SDF representation with spatial data structure. For example, NanoVDB from the OpenVDB package.
- No performance comparison with the original mesh representation.
  - Ideally, the paper should show the advantages of the proposed representation over triangle meshes in rendering captured objects. However, the training data seem to come from mesh data.
  - Even though multiscale sphere tracing is 2x faster than sphere tracing with the original high resolution SDF, ~40 FPS still seems unusable in real applications compared with mesh-based representations.

### Questions
Most of my questions are described in the Weaknesses section. In addition, I have a few technical questions.
- Where does the speedup of the proposed GEMM normal computation come from compared to a autodiff framework? Is there improvements in algorithmic complexity, or it is mainly a reduction in overhead (e.g., better use of GPU resources)
- Is the GEMM normal computation differentiable to be used in an optimization framework?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to use a neural implicit shape representation with multi-level of details, which allows fast sphere tracing: coarse, fast levels are traced first, followed by finer levels. Attributes, such as colors or normals can be transferred from one detailed level to a coarse level, for improved renderings in a constrained computational budget.

### Strengths
The idea of using multiple levels of details for efficiency is underexplored in the literature. Transferring details such as normals to a coarse surface is nice, and emulates the use of normal maps in the classical graphics methods.
Efficiency: The multiscale sphere tracing algorithm focuses on minimizing iteration time by using coarse approximations in earlier iterations. This can lead to faster rendering times and more efficient computations.
Analytic Normal Calculation: The paper proposes a fast algorithm for analytic normal calculation for MLPs, which can improve shading performance and accuracy during rendering.

### Weaknesses
The “neural attribute mapping” simply consists in evaluating a neural field on a given surface, for textures or normals. To be more formal, given a surface point s on surface S, and a neural field f:
- Case 1: if f encodes an RGB color, then s is colored with f(s).
- Case 2: if f encodes a surface, then s is given the normal ∇f(s). This case is interesting when S has a low level of details: by transferring the normals of the 0-levelset of f to S, one can render S with more details. But this is simply a nearest-neighbor assignment, no need for elaborate mathematics.

Both cases are very simple, and do not require the unnecessarily complex (pretentious?) formalism of “delta-nested neighborhood”, “integrating along the gradients”, “restriction of ∇f to S and mapping the normal along a path” presented in the paper. 

Furthermore:
- Case 1 was already exploited in past papers, for example Texture Fields (Oechsle et al, ICCV 2019), GET3D ( Gao et al., NeurIPS 2022). It is very straightforward, and “achieving SOTA by uncoupling appearance from geometry in a compositional manner” is an overstatement. Additionally, the comparison to Instant NGP is irrelevant, as the problem setting is vastly different: Instant NGP learns a scene representation from images only. Here, the proposed method already has access to a supervision signal for the 3D geometry and for the RGB texture.
- Case 2 should be compared to a straightforward rendering of the more precise representation f, instead of transferring it. The speed benefits of a transfer of a high resolution field to a coarse surface should be exemplified. The only table reporting a speedup is Tab. 5, and it does not display a quality metric - only speedups.

The multi-scale sphere tracing algorithm is similar to the extension of marching cubes to multi-LOD presented in BACON. Its speed should be compared to extracting the surface (once) with marching cubes, and then rendering it with a rasterizer.

The GEMM implementation of normals computations should be compared to standard backpropagation in pytorch or tensorflow. This is a component-wise computation of the normal vectors. The acronym GEMM is used several times without being defined, nor the concept. NeuS2 (Wang et al, ICCV 2023) also has a fast normal computation algorithm, it might be worth adding the reference.

Section 3.3 is supposed to “describe approaches to create sequences of neural SDFs with nested neighborhoods”. In fact, given any sequence of SDF networks, by choosing the epsilons large enough, we can nest them. The bounds derived in this section are very loose and can apply to any sequence, even for unrelated objects or surfaces. It would also work for levels of details in any order. In other words, saying that a sequence of neural surfaces is “nested” without characterizing the threshold for which it is nested has very little value: given any sequence, I can consider it as nested.

In the experiment section, when reporting training time vs NGLOD and IDF: which neural network architecture is used? Why call it “ours”? The whole method and contributions are about rendering neural fields with multiple levels of details, never about a new architecture or a faster training procedure. Why compare training times then?
Moreover, it is unclear if SIRENs or BACONs are used. A whole paragraph of the method section is dedicated to nesting BACONs, is it used here? The datasets should also be clarified in the main text.

Minor: when reporting MSE, scaling the values to improve readability and avoid all metrics starting with “0.00” would be better.

Clarity: the introduction is a bit of a circular definition: “the nested neighborhood model […] is a novel framework […] based on nested neighborhoods” is not explaining what “nested neighborhoods” are. Moreover, in many places the term "S is nested on the delta-neighborhood of S_theta" could simply be replaced by "S is in the delta-neighborhood of S_theta".



In conclusion, the idea of exploring multiple levels of details is Interesting, but its presentation uses overelaborate mathematics for very simple ideas that have already been exploited (learning a color field for texture for example).
Moreover, experimental results are not convincing. Comparisons with a traditional pipeline are lacking: since rendering speed is the main motivation, the approach should also thoroughly compared to a mesh rasterizer - and a one time execution of a CUDA implementation of marching cubes (like https://github.com/tatsy/torchmcubes).
While the method presents a formalism for “nesting” an arbitrary number of levels of details, most results are provided with a single network or 2 networks. Finally, clarity should be improved too (see questions and weaknesses).

### Questions
In which practical application should one consider using this multiscale SDF over a mesh rasterizer?

Could the definition of “nested surfaces” be simplified? For example, using a single threshold delta. I believe the following definition is equivalent to the one proposed:
“say that f_theta_2 is nested in f_theta_1 for threshold delta > 0 if S_theta_2 is contained in the delta-neighborhood of S_theta_1”

At the end of the first paragraph of Sec 5.1 : “the attribute g is constant along the path since ||∇f|| = 1”: why does a gradient with constant norm implies a constant gradient?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
