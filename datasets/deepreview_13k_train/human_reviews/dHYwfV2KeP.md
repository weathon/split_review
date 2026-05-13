# Locality-aware Gaussian Compression for Fast and High-quality Rendering

- Decision: Accept
- Scores: 6, 8, 6, 3

## Abstract
We present LocoGS, a locality-aware 3D Gaussian Splatting (3DGS) framework that exploits the spatial coherence of 3D Gaussians for compact modeling of volumetric scenes.
To this end, we first analyze the local coherence of 3D Gaussian attributes, and propose a novel locality-aware 3D Gaussian representation that effectively encodes locally-coherent Gaussian attributes using a neural field representation with a minimal storage requirement.
On top of the novel representation, LocoGS is carefully designed with additional components such as dense initialization, an adaptive spherical harmonics bandwidth scheme and different encoding schemes for different Gaussian attributes to maximize compression performance.
Experimental results demonstrate that our approach outperforms the rendering quality of existing compact Gaussian representations for representative real-world 3D datasets while achieving from 54.6$\times$ to 96.6$\times$ compressed storage size and from 2.1$\times$ to 2.4$\times$ rendering speed than 3DGS. Even our approach also demonstrates an averaged 2.4$\times$ higher rendering speed than the state-of-the-art compression method with comparable compression performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper tackles the high storage demands associated with 3D Gaussian Splatting by introducing an effective compression method. The core idea is to exploit local similarity within Gaussian attributes, representing them through compact, well-encoded local features. The authors start by conducting a statistical analysis of 3D Gaussian Splatting (3DGS) attributes and proceed to design a local feature that captures and encodes these similar patterns within a given region. By combining carefully structured steps—such as pruning, point cloud initialization, quantization, and entropy encoding—the proposed method achieves substantial compression of the 3DGS field. Remarkably, this compression is achieved while maintaining, or even enhancing, the rendering quality and fidelity relative to the original setup.

### Strengths
1. The overall solution is comprehensive, incorporating careful designs for initialization, pruning, and compression schemes for different components. 
2. The paper is well-written with a clear logical flow.
3. The dense initialization demonstrates an interesting improvement in compression.
4. The analysis of storage size in Tab.3 provides a valuable indication for the community about the current bottlenecks in compression.

### Weaknesses
1. Number of Gaussians in Variants: It would be beneficial to provide the number of Gaussians for different variants, as Ours-Sparse has a lower FPS compared to Ours-Small and Ours. Understanding whether the final number of Gaussians influenced the results is important. Including the point number counts along the training iteration would help illustrate the influence of different initializations. Additionally, it would be interesting to see if such an initialization design could improve the performance of previous approaches.
2. The method still takes extra training time to compress a 3DGS, which will be a limitation in some real applications.

### Questions
1. Please include the number of Gaussians for the different ablation versions in Tab.3 to understand the main reason for high FPS.
 
2 Decoding Time: Including the decoding time would help readers understand the applicability of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper aims to achieve both high rendering speed and reduced storage size for 3D Gaussian Splatting-based scene representations. To this end, it analyzes the local coherence of Gaussians across several scenes and proposes exploiting multi-resolution hash grids. More specifically, Gaussians now have only base scale, positions, and base color, while hash grids fill in the details. In addition, the paper employs adaptive SH bandwidth, pruning, dense initialization, quantization, and encoding. With all these methods, the paper demonstrates significant performance improvement.

### Strengths
The concept of locality is not novel in 3D Gaussian Splatting, but the paper effectively illustrates this through graphs. Moreover, it clearly addresses the differences between other locality-based methods (anchor-based methods), explaining why the proposed method is important and highlighting key points for readers already familiar with anchor-based representation.

The performance improvements in terms of size, rendering speed, and rendering quality are significant.

Additionally, the paper includes many technical details for adopting various techniques, especially during quantization and encoding, which will benefit those working in this research areas.

### Weaknesses
As I mentioned in the strength section, the idea of utilizing locality in 3D Gaussian Splatting is not novel.

While the paper could be beneficial for those working on compressing 3D Gaussian Splatting (3DGS), I still have concerns about the novelty of exploiting locality. The related works section currently focuses mainly on anchor-based methods' aspects like quality and storage but does not adequately address the locality-related properties of them.

To strengthen the paper, it would be helpful to clearly highlight the differences between the proposed method and locality-exploiting methods more properly.

### Questions
How did you calculate cosine similarity of opacities?
I would also like to know how and why three explicit attributes were selected.

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
4

### Summary
LocoGS analyzes the local coherence of the attributes of Gaussian primitives and introduces a novel representation that incorporates locality information. By utilizing the locality-aware 3D Gaussian representation along with other compression methods, such as quantization and encoding schemes, LocoGS achieves state-of-the-art compression performance and rendering FPS compared to existing compression methods.

### Strengths
1. LocoGS carefully analyzes the relationships among 3D Gaussian attributes and introduces a locality-aware representation based on these relationships.
2. The paper is well written and easy to follow, with an excellent categorization of compression methods.
3. LocoGS outperforms existing methods in both compression performance and rendering speed.

### Weaknesses
1. Dense initialization is not related to compression; it is merely a warm-up trick. It would be unfair for the authors to use this trick since all of the baselines still initialize with COLMAP points.
2. As we know, the training time for Nerfacto is significantly longer than for 3DGS. Why do the authors choose to use Nerfacto for warm-up instead of 3DGS? Both methods can generate coarse depth maps, which can then be used to create an initialization point cloud. Additionally, how many iterations do the authors train Nerfacto for dense initialization?
3. In the limitations section, the authors describe that LocoGS requires one hour more training time than the baselines. Which components affect the training efficiency—is it the dense initialization?
4. No demos submitted.

### Questions
1. I would like to understand the reason why the rendering performance of LocoGS is lower than that of Scaffold-GS. Aside from the quantization and encoding schemes, do the authors discard the view input of the MLP when obtaining each attribute of the 3D Gaussians?
2. How about the performance in large-scale datasets, like Mega-NeRF, Urbanscene3D or MatrixCity?

If the authors solve these questions, I’ll raise the score.

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
5

### Summary
The paper introduces "LocoGS," a locality-aware 3D Gaussian Splatting (3DGS) framework designed for fast and high-quality rendering. This framework capitalizes on the spatial coherence among 3D Gaussians to offer a compact, efficient representation that significantly reduces storage requirements and enhances rendering speed without sacrificing quality. 

Key contributions include:
1. A new locality-aware 3D Gaussian representation that efficiently encodes locally-coherent Gaussian attributes.
2. Implementation of additional components like dense initialization, Gaussian pruning, adaptive spherical harmonics bandwidth scheme, and tailored encoding schemes to maximize compression performance.
3. Demonstrated superior performance over existing methods in terms of compression ratio and rendering speed, verified through extensive experiments.

### Strengths
1. The locality-aware strategy for Gaussian attribute representation is a novel approach that leverages spatial coherence effectively.
2. The paper includes detailed comparisons with existing methods, showing improvements in storage efficiency and rendering speed. The reduced storage and increased speed facilitate the practical application of 3DGS in real-time scenarios, like mobile devices.
3. The motivation and clarity of the paper are commendable.

### Weaknesses
1. The multiple components introduced (e.g., multi-resolution hash grids, and adaptive SH bandwidths) might complicate the implementation and tuning of the framework.
2. The paper could benefit from more discussion on any potential trade-offs or limitations, particularly in different or more challenging rendering environments. e.g. metal and lighting area. The performance on large scenes is not thoroughly addressed, especially considering that 3DGS compression is most critical for large-scale scenarios. The paper lacks a detailed analysis of performance trade-offs in such environments, where memory and computational constraints are more pronounced.
3. The analogy between local coherence of Gaussian attributes and pixel values in natural images, while intuitive, lacks a rigorous mathematical justification. This analogy, while helpful for understanding, needs more concrete backing to solidify the claim, especially given the different nature of 3D Gaussians and 2D pixel values. The paper does not provide sufficient evidence to support the claim of local coherence beyond visual examples.
4. The paper details different encoding schemes for various attributes but does not clearly compare these methods against potential alternatives or justify why these particular methods were chosen. Providing comparisons or rationale might strengthen this section, especially in terms of efficiency or error rates associated with each method.

### Questions
1. Are there scenarios or conditions under which the proposed method might not perform as expected? e.g. large scenes.
2. Could you provide more detailed explanations or pseudo-codes for complex components like the adaptive SH bandwidth and pruning strategy? Are you going to publish your code?
3. Does your model also perform better in larger scenes? Can you please add more experiments on how it performs in larger scenes? e,g. Miller-19 dataset.

### Soundness
3

### Presentation
3

### Contribution
2
