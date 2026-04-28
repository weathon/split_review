# Sort-free Gaussian Splatting via Weighted Sum Rendering

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Recently, 3D Gaussian Splatting (3DGS) has emerged as a significant advancement in 3D scene reconstruction, attracting considerable attention due to its ability to recover high-fidelity details while maintaining low complexity. Despite the promising results achieved by 3DGS, its rendering performance is constrained by its dependence on costly non-commutative alpha-blending operations. These operations mandate complex view dependent sorting operations that introduce computational overhead, especially on the resource-constrained platforms such as mobile phones. In this paper, we propose Weighted Sum Rendering, which approximates alpha blending with weighted sums, thereby removing the need for sorting. This simplifies implementation, delivers superior performance, and eliminates the ``popping'' artifacts caused by sorting. Experimental results show that optimizing a generalized Gaussian splatting formulation to the new differentiable rendering yields competitive image quality. The method was implemented and tested in a mobile device GPU, achieving on average $1.23\times$ faster rendering.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a sort-free Gaussian Splatting pipeline, which reduces the computational overhead of rendering to adapt to scenarios with limited computing resources. The key insight of this paper is that the view dependent sorting in the vanilla 3DGS involves a lot of computational overhead and is difficult to port to mobile devices. Therefore, the authors proposed to use weighted sum and view-dependent opacity to approximate alpha-blending. Experiments demonstrate that proposed method achieves comparable rendering quality and faster rendering speed than the original 3DGS on mobile devices.

### Strengths
- The author provides a clear analysis of the tile-based sort in the vanilla 3DGS, explains its impact on rendering speed, and explains why it is difficult to implement on other devices.
- The proposed method speeds up rendering while ensuring rendering quality, and has been verified on consumer mobile devices.
- The proposed weighted sum approximation alleviates the *pop* phenomenon caused by inconsistent sorting results under different view-directions in the vanilla 3DGS.

### Weaknesses
 - The proposed method gets rid of the costly sorting, but a more complex weight and view-dependent opacity are used. Although the author points out in the paper that a general scheme for learning scene representations is bound only by the mathematical constraints of the scene model. According to the experimental results in the paper, the use of simple weighted-sum and view-independent opacity cannot achieve satisfactory rendering results. Does this mean that for rendering processes that are not physically and optically, more complex models must be used, such as introducing more learnable parameters as in the paper?
- In the conclusion part of the paper, the author mentioned some recent research on compact Gaussian Splatting. According to my understanding of these works, since the methods proposed in these works obtain more compact 3D Gaussian representations, they can reduce the sorting overhead and speed up rendering to a certain extent. Therefore, I think the author should add a comparison of rendering quality, speed and memory usage between the proposed method and these works, such as Compact 3DGS[1], LightGaussian[2] and Compressed 3DGS[3] in the experimental evaluation section.

### Questions
In the paper, the author points out that for some complex scenes, since a large number of 3D Gaussians are needed for representation, the sorting process will exhaust the resources of mobile devices, making real-time rendering impossible, such as the bicycle scene in Mip-NeRF 360 dataset. However, I tried to visualize the bicycle scene using a gsplat-based webgl viewer on my phone (iPhone 15 Pro Max), and was surprised to find that it achieves real-time rendering, about 20-30fps. This seems to indicate that some optimizations to the 3DGS rendering pipeline (gsplat uses some tricks) can increase the rendering speed on mobile devices without more complex designs. I would like to know the author's opinion on my point of view and more analyses of the key differences that enable real-time performance on mobile devices. And they can test the performance of gsplat on Snapdragon® 8gen3 chipset and compare with their proposed method.

Here is the link of gsplat webgl-viewer https://gsplat.tech

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
3

### Summary
The authors propose a novel rasterization backend for 3D Gaussian splatting (3DGS) that addresses the computational and memory overhead associated with depth sorting. Their primary contribution is replacing traditional alpha blending with a weighted sum rendering approach. The rendering is achieved through direct weighted summation of Gaussians, where weights are determined by a parameterized truncated linear function applied to the product of color and opacity. Additionally, they introduce view-dependent optimizable opacity for individual Gaussians, modeled using spherical harmonics.
Their weighted sum rendering (WSR) technique demonstrates comparable rendering quality to conventional 3DGS. To validate the advantages of their sort-free approach, the authors implement both vanilla 3DGS and WSR on the Vulkan API and evaluate performance on mobile GPU hardware, achieving a 1.23x speedup.

### Strengths
- The paper aims to address a fundamental bottleneck in 3DGS rendering by proposing a sort-free pipeline, distinguishing itself from previous approaches that primarily focused on reducing Gaussian counts.
- The investigation of various weight derivation functions (direct sum-up, exponential weighted, and linear correction weighted) demonstrates a relative comprehensive experimental analysis effort.
- Implementation and evaluation on mobile devices effectively demonstrates the practical benefits of the sort-free approach in resource-constrained environments.
- The method appears to mitigate "pop" artifacts, a persistent challenge in volumetric rendering, providing an additional benefit beyond computational efficiency.

### Weaknesses
 - The theoretical foundation for replacing alpha blending with an algebraic function requires stronger justification. While the proposed representation achieves good results, it lacks the physical insights inherent in traditional alpha blending, which models light obstruction during propagation. The introduction of view-dependent opacity appears necessary for acceptable rendering quality, but the paper would benefit from a more rigorous analysis of why this combination works, rather than empirical validation alone. Specifically, the paper does not adequately address how the parameterized truncated linear function, used to determine the weights, relates to the underlying principles of light transport and how it might introduce artifacts not present in traditional alpha blending.
- The preference for linear weights over exponential weights raises questions about robustness. When considering camera movement along viewing rays, exponential weights (with β ≈ 1) should theoretically provide more consistent mixing ratios between Gaussians. Linear weights may introduce color shift artifacts due to distance-dependent mixing ratio variations. While the authors claims "some artifacts remain visible" then selected linear weight rather than exponential weight, these issues warrant more detailed examination. It is unclear how the specific parameters of the linear function are chosen and how these choices affect the final rendering quality, particularly in scenarios with varying Gaussian densities and depths.
- The method's generalizability is limited by the transformation of opacity into a view-dependent "black box" variable. This fundamentally alters the role of opacity, which traditionally serves as a crucial signal for pruning and densification in many 3DGS applications, potentially limiting compatibility with existing and future research in this domain. The paper does not explore the implications of this change on existing pruning and densification algorithms, nor does it propose alternative strategies that could maintain the geometric and physical interpretability of opacity.

### Questions
- Does the method exhibit color shift artifacts during camera movement along the z-direction, as suggested by the concerns regarding linear weighting?
- Since opacity is not capped at 1, how did you enforce the data range of final color, simply clamp?
- How do other Gaussian attributes maintain their geometric meaning in this framework? Specifically: Does the mean of Gaussians still correspond to point cloud locations? How about depth extraction?
- While traditional 3DGS implementations employ culling to manage computational complexity, does this approach require weighted summation of ALL Gaussians? What are the implications for scalability?
- Please clarify the memory usage analysis: does it encompass only Gaussian attributes or include runtime memory requirements?
What is the memory overhead of spherical harmonics coefficients for view-dependent opacity compared to vanilla 3DGS?
- Regarding Table 2, could you elaborate on the starred data points showing significantly higher values? How does resource exhaustion due to sorting impact subsequent pipeline stages?
- Given the potential for hardware-accelerated sorting methods specifically designed for 3DGS, possibly through hardware-software co-design, how might this work adapt to or complement such future developments?

### Soundness
2

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
3

### Summary
This paper proposes a sort-free variant to the 3DGS algorithm. Because 3DGS is a semi-transparent representation, it requires sorting of all primitives which leads to higher running time, more hardware requirements, and lower compatibility on edge devices. Learning from the traditional sort-free rendering algorithm which replaces the sorting with an estimated weight from depth, this paper proposes to eliminate the sorting process of 3DGS completely. 

This paper further proposes a view-dependent opacity to better simulate the occlusion effect. By learning spherical harmonics to represent the opacity, it allows the 3D Gaussians to appear and disappear at different angles, which could further mimic the occlusion effect.

As a result, this paper achieves a slightly higher rendering speed and lower GPU memory footprint, better compatibility on edge devices, and comparable rendering quality than 3DGS.

### Strengths
**Motivation**
* The motivation of this paper is very clear. It clearly illustrates the drawbacks of the sorting requirement of 3DGS and the possible benefit of removing it. Sort-free transparent object rendering is also a well-studied direction in traditional rendering. Combining the algorithms from traditional computer graphics with 3DGS is well-motivated.

**Method**
* The proposed method transformed the traditional depth-based weighted rendering to a learnable version to better suit the per-scene optimization used in 3DGS, which provides significant performance improvement. 
* The proposed view-dependent opacity is an innovative approach that mimic the occlusion effect. Because this SH parameters are optimized together, it compensates for some performance loss from incorrect occlusion estimation without sorting.

**Experiments**
* The performance on normal desktop GPU demonstrates a small improvement in rendering speed and comparable rendering speed. In fact, it is already remarkable that a sort-free rendering algorithm can match the performance of a sorting-based rendering algorithm in a scene full of semi-transparent primitives.
* The performance improvement on the edge device shows a more significant improvement because of the demanding sorting step.

### Weaknesses
 ** Motivation **
* As shown in the paper, the sorting step is usually considered slow, but actually contributes to only 25% of the total rendering time. The real problem preventing 3DGS based method from matching the rendering speed of traditional methods is the alpha blending step. Although this paper removes the sorting step, it still needs the per-pixel alpha blending of Gaussians of calculated weights. As a result, the speed improvement is rather insignificant. Furthermore, the paper does not sufficiently address the potential overhead introduced by the view-dependent opacity calculation, which could negate some of the gains from removing sorting. A more detailed analysis of the computational cost of each stage is needed to justify the overall performance benefit.
* Rather than removing the sorting step, many works have proposed to removing the redundant Gaussians directly. These methods seem to provide much more significant speed boost. Of course these two method can be run in parallel, but it still weaken the importance of the proposed method. The paper should more clearly articulate the unique advantages of the sort-free approach compared to methods that focus on Gaussian reduction, especially considering the relatively small speedup achieved on desktop GPUs. A more thorough comparison with these alternative approaches is necessary to contextualize the contribution.

** Method **
* The proposed method is largely borrowed from the traditional sort-free methods. I think this is acceptable because of the long history of sort-free rendering research in traditional computer graphics, it does negatively affect the novelty of the proposed method slightly.

** Experiments**
* As mentioned above, the improvement on standard desktop GPU is rather insignificant. Since sort-free rendering is essentially an approximation of the sort-based rendering, it might not be a good idea to choose this method for such a small improvement while there is a possibility of very bad performance on some scenes. The paper should provide a more in-depth discussion on the trade-offs between rendering quality and speed, especially on desktop GPUs where the speed improvement is marginal. A quantitative analysis of the quality degradation compared to the original 3DGS is needed to justify the use of the proposed method.
* Continuing from the last point, sort-free approximations are usually inaccurate on small and thin structures. For example, I noticed that the proposed method on the bicycle scene in MipNeRF-360 dataset is somewhat lower than the original 3DGS method. This scene contains very thin and fine structures on the bicycle which could be a better illustration of whether the proposed method suffers from similar artifacts like the traditional methods. The paper should include a more detailed analysis of the performance on scenes with fine structures, and provide a quantitative comparison of the rendering quality in these challenging cases.
* Despite the significant rendering speed improvement on the edge devices, the paper lacks a detailed explanation of how the edge device running out of resources leads to such a big decrease in rendering speed. The paper should provide a more detailed analysis of the specific bottlenecks on edge devices, such as memory bandwidth limitations or computational constraints, that cause the original 3DGS to perform poorly. This would help to better understand the practical benefits of the proposed method.

### Questions
1. Can the authors provide some qualitative results on the Bicycle scene?
2. Can the authors provide some videos showing the removal of the popping effect?
3. Can the authors show some failure cases of the proposed approximation?

I really want to give a positive rating to this paper, because I know it is very difficult to make a sort-free rendering to achieve the same quality as the sort-based version. However, the marginal speed improvement diminishes the significance of this paper. Furthermore, I hope the authors can demonstrate some failure cases of such approximation methods, as they are quite common in traditional sort-free algorithms. Doing this could give the reader a more comprehensive understanding of the proposed method.

### Soundness
3

### Presentation
2

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
This work attempts to solve a key problem with current Gaussian Splatting techniques, the computational load that occurs during rendering as a result of the non-commutativity of the opacity calculation needed during the rendering process. The authors achieve this by a novel weighting of term added to each Gaussian to replace the traditional opacity term. The weighting term allows for an order independent formulation of the computation of the final colour of the a rendered ray through the field. View-dependence is obtained by the introduction of a spherical harmonic based formulation to the new weighting term similar to that currently used in prior-art Gaussian Splatting methods for view-dependent colour. Performance is evaluated against prior-art techniques.

### Strengths
This work solves a crucial problem in real-time rendering of Gaussian Splatting based radiance fields. By removing the need for depth-based sorting of the Gaussians before rendering, critical memory requirements are reduced enabling the implementation of the methodology on mobile devices or other applications with limited computational capacity. So I feel that the work represents a strong contribution to the field. Other strengths include:
1. Clear and easy to read figures and tables clearly detailing the benefits of the proposed method.
2. A detailed and clear explanation of the proposed method. It is clear what has been done, how this is motivated by previous literature.
3. A strong experimental validation. Comparisons are made against well-recognized metrics and a the latest state-of-the-art methods. The experimental results support well the conclusions reached.

### Weaknesses
This work solves a crucial problem in real-time rendering of Gaussian Splatting based radiance fields. By removing the need for depth-based sorting of the Gaussians before rendering, critical memory requirements are reduced enabling the implementation of the methodology on mobile devices or other applications with limited computational capacity. So I feel that the work represents a strong contribution to the field. Other strengths include:
1. Clear and easy to read figures and tables clearly detailing the benefits of the proposed method.
2. A detailed and clear explanation of the proposed method. It is clear what has been done, how this is motivated by previous literature.
3. A strong experimental validation. Comparisons are made against well-recognized metrics and a the latest state-of-the-art methods. The experimental results support well the conclusions reached.

This work is of quite a high quality. I do not see any specific weaknesses in the methodology or the experimental results. There is one specific minor weakness in the experimental section wherein I would like further information on the memory requirements of the proposed method. I detail the exact question I have in the "Questions" section below.
One final minor issue is the presence of minor grammar errors in the text as I mention in the "Questions" section below.

### Questions
1. In section 4.3 the authors reveal that view-dependent opacity is obtained by the addition of a new set of spherical harmonics related to the depth weighting introduced by the authors. In the experimental section, the authors show that this doesn't impact memory usage during rendering and a rationale given in the removal of the sorting step and the potential reduction in the number of Gaussians. However, this appears to be referring to instantaneous memory requirements. How does the introduction of the new set of spherical harmonics for each Gaussian affect post-training storage requirements of the radiance field? Is a greater storage footprint needed for the radiance fields produced by the proposed methods?
2. Line 53 "maintain rendering differentiable" should be "maintain rendering differentiability".
3. Line 141 "Chris Wyman provide a good survey on these methods" should be "Chris Wyman provides a good survey on these methods"
4. Line 273, "However, DIR-WSR does not work well for the complex scenes, " should be "However, DIR-WSR does not work well for complex scenes, "
5. Line 307 ends with an additional full stop.

### Soundness
3

### Presentation
4

### Contribution
4
