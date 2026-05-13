# Distance-Based Tree-Sliced Wasserstein Distance

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
To overcome computational challenges of Optimal Transport (OT), several variants of Sliced Wasserstein (SW) has been developed in the literature. These approaches exploit the closed-form expression of the univariate OT by projecting measures onto one-dimensional lines. However, projecting measures onto low-dimensional spaces can lead to a loss of topological information. Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL) has emerged as a promising alternative that replaces these lines with a more intricate structure called tree systems. The tree structures enhance the ability to capture topological information of the metric while preserving computational efficiency. However, at the core of TSW-SL, the splitting maps, which serve as the mechanism for pushing forward measures onto tree systems, focus solely on the position of the measure supports while disregarding the projecting domains. Moreover, the specific splitting map used in TSW-SL leads to a metric that is not invariant under Euclidean transformations, a typically expected property for OT on Euclidean space. In this work, we propose a novel class of splitting maps that generalizes the existing one studied in TSW-SL enabling the use of all positional information from input measures, resulting in a novel Distance-based Tree-Sliced Wasserstein (Db-TSW) distance. In addition, we introduce a simple tree sampling process better suited for Db-TSW, leading to an efficient GPU-friendly implementation for tree systems, similar to the original SW. We also provide a comprehensive theoretical analysis of proposed class of splitting maps to verify the injectivity of the corresponding Radon Transform, and demonstrate that Db-TSW is an Euclidean invariant metric. We empirically show that Db-TSW significantly improves accuracy compared to recent SW variants while maintaining low computational cost via a wide range of experiments on gradient flows, image style transfer, and generative models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Distance-based Tree-Sliced Wasserstein (Db-TSW) distance, which addresses limitations in existing Tree-Sliced Wasserstein on Systems of Lines (TSW-SL) by improving Euclidean invariance and preserving positional information in optimal transport (OT). Unlike traditional Sliced Wasserstein (SW) distances, which can lose topological information, Db-TSW incorporates tree structures and a novel class of E(d)-invariant splitting maps to maintain metric consistency under Euclidean transformations. This approach also includes a new tree sampling method for efficiency, enabling GPU-friendly implementations. Through rigorous theoretical analysis and empirical experiments, Db-TSW is shown to outperform recent SW variants on tasks such as gradient flows, image style transfer, and generative modeling, while remaining computationally efficient​.

### Strengths
* Paper is very-well written and clear.
* Through extensive experiments, authors show the effectiveness of Db-TSW and compare it with existing benchmarks.
* Authors propose a novel variant of Radon transform on Systems of Lines which generalizes the invariant splitting mapping of the previous works.

### Weaknesses
 * Although Db-TSW is optimized for GPU implementation, the method’s reliance on high-dimensional Euclidean distances for each point-line relationship could still pose challenges for scalability in very high-dimensional settings. This could result in increased computation times or memory usage for large datasets, particularly when fine-grained positional information is necessary. I would like to see a thorough runtime comparison of Db-TSW with respect to the number of samples and dimensionality of the data. Specifically, the computational cost of calculating distances between all points and all lines scales linearly with both the number of points and the number of lines, which could become a bottleneck for very large datasets or high-dimensional spaces. The paper should include a detailed analysis of how the memory footprint and runtime scale with increasing dimensionality and number of samples, especially in scenarios where the number of points significantly exceeds the number of lines, or vice versa.

* The root-concurrent structure for sampling tree systems, though efficient, limits Db-TSW’s flexibility in capturing diverse spatial arrangements. I am curious about how effectively Db-TSW captures these spatial variations. Is there a way to demonstrate this? Could you provide an example where Db-TSW might fail to capture them? The use of root-concurrent trees, while simplifying the sampling process, may not be sufficient to capture complex spatial relationships present in the data. For example, consider a scenario where data points are arranged in a non-convex shape or a spiral pattern; the root-concurrent structure might not provide enough degrees of freedom to accurately represent the underlying geometry. It would be beneficial to see a demonstration of Db-TSW's performance on datasets with such complex spatial arrangements, and a discussion of the limitations of the root-concurrent structure in these cases.

### Questions
* The root-concurrent structure is computationally efficient, but it may affect the transform's injectivity, especially in cases with overlapping or closely aligned lines. How does this design ensure that unique positional information is retained across sampled trees, and are there any trade-offs in injectivity or stability in high-dimensional data?

* How does Db-TSW handle cases where the Euclidean distance between points and tree lines is nearly uniform across lines, potentially reducing the distinctiveness of the splitting map?

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
The paper introduces a distance-based variant of the tree-sliced SW on a system of lines (TSW-SL) [1]. The core contribution lies in generalizing the class of splitting maps used to project measures onto tree systems while preserving Euclidean invariance. The authors provide theoretical results for their method, including proofs of metric properties and injectivity of the associated Radon transform. They also introduce a simplified tree sampling process that with efficient GPU implementation. Various experiments including gradient flows, image generation, and color transfer show competitive or better performance in certain hyperparameter settings.

[1] Tran, Viet-Hoang, et al. "Tree-Sliced Wasserstein Distance on a System of Lines." arXiv preprint arXiv:2406.13725 (2024).

### Strengths
S1: Generalization of splitting maps addresses a limitation in previous work [1].

S2: Efficient implementation thanks to the proposed simplified tree sampling process.

S3: The writing is well-written and easy-to-follow. 

S4: Good empirical results within the given setups.

### Weaknesses
W1: It would be nice to have an explicit discussion of computational/memory complexity.

W2: For setups that aggregate results from multiple runs (e.g., gradient flow), the paper should include both mean and std/variance (instead of just the means). Additionally, it may be a good idea to use plots to better present the results in Table 2,3 (visually). Both of these are good practices in general, and also used in [2], which is cited in the paper.

W3: The paper would benefit from a detailed discussion on various instances of tree systems and especially splitting maps (which are directly related to the primary contributions). For instance, using $k$ concurrent lines with shared root is fast but what are we sacrificing? Are they quantifiable? Softmax works well as an E(d)-invariant splitting map but what are some other instances (along with pros and cons)?  Along those lines, a stronger ablation section would be helpful. It should clearly demonstrate that any performance gain is due to the novel technical contributions to support the paper's claims throughout (is it the invariance or the proposed tree structure that gives better performance?). How much is the gain if one adjusts $L,k, \delta$ for datasets of varying complexity? What about root sampling? Since the design space includes various components, that would help practitioners in making sensible design choices for their applications.

W4: The paper would be strengthened if explicitly discussing sample/projection complexity, and also error bounds, convergence rate for MC approximation.

W5: What are the authors' rationales for not using a consistent set of baseline methods to evaluate relative performance across tasks? Moreover, is it a good idea to compare against non-linear slicing methods like GSW, ASW? Why or why not?

### Questions
Q1: Can any component of this framework be made learnable? That would probably enable various interesting extensions.

Q2: Are there instances where prior knowledge on the data allows a good/optimal tree design?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Paper proposes aims at enhancing the Tree-Sliced Wasserstein on a System of Line (TSW-SL) by defining a specific splitting maps (that are parts of the radon transform on systems of lines) that takes into account the distance to the lines. The method is coined Dd-TSW and it can be shown that it preserves some invariances (that are also preserved in $W_2$ or sliced-Wasserstein). By construction, it allows taking into account the distance to the lines and provides varying mass distributions. A variant that samples orthogonal lines, allowing to better cover the space, is also provided. Experiments show improved performances in several settings with similar computational timings.


**Note**: I have also reviewed the paper that introduces TSW-SL.

### Strengths
Dd-TSW is an extension of TSW-SL, in which the splitting map is refined and a more efficient method for sampling lines is provided. As such, the originality is fair. The definition of Dd-TSW is well-grounded and the experimental section shows that it yields competitive results in several scenario, even in one specific challenging scenario of high dimensional setting (GF experiment in 20d).

### Weaknesses
The main weaknesses of the paper lie in: 

- Unsufficient analysis of its various parameters. The settings of some parameters are not discussed (e.g., the number of lines $k$ and the value of the inverse temperature parameter $\delta$). Specifically, the impact of these parameters on the convergence rate and the final performance is not thoroughly investigated. The paper would benefit from a more detailed ablation study, exploring a wider range of values for $k$ and $\delta$, and analyzing their effects on the method's behavior, including computational cost.
- In the gradient flow experiment, differences in ground costs (e.g., $L_2$​ and tree metric) between methods make it challenging to compare results at a fixed number of iterations for a fixed LR. The lack of a common ground cost makes it difficult to isolate the effect of the proposed method from the influence of the different metrics. This complicates the interpretation of the results and the assessment of the method's effectiveness.
- Competitors are not consistent between the different experiments. The choice of baseline methods varies across the different experiments, which makes it difficult to have a clear comparison of the proposed method with the state-of-the-art. A consistent set of baselines across all experiments would allow for a more robust evaluation of the method's performance.

### Questions
- The trees are recommended to be sampled close to the means of the target distributions. Does this relate to numerical instabilities that can occur for large values of $\delta$, such as those considered in the paper ($ \delta = 10$), to avoid excessively large distances?
- The $\delta = 10$ parameterization should lead to a very sparse splitting map. Could you provide an ablation study on this parameter and discuss why large values should be considered?
- Does the new method of sampling lines affect the performance of Dd-TSW, or is its definition justified only by computational issues?
- It seems (on the Gaussian 20D dataset) that Dd-TSW performs better in higher-dimensional cases than other SW variants. Is this result also true in higher-dimensional settings, and can you provide an explanation for this interesting behavior?
- It is stated in the introduction that Dd-TSW enables a highly parallelizable implementation, and in Section 6, it mentions "*that enables an algorithm with linear runtime and high parallelizability, keeping the wall-clock time of Dd-TSW and Dd-TSW⊥ approximately equal to that of vanilla SW and surpassing some SW variants*." Do the reported timings in section 6 relate to the parallel implementation?
- In the conclusion, it is mentioned that improved performance is expected by adapting recent advanced sampling schemes or techniques from SW to TSW-SL. However, it seems that the extension is not straightforward: can you provide concrete examples that could be adapted to Dd-TSW?

### Soundness
3

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
4

### Summary
This work proposes a variant of the TSW-SL distance. It is observed that the latter is not invariant w.r.t translations and rotations (Euclidean transformations), and that the splitting map used in TSW-SL does not take into account the trees but only the positions of the samples. Thus, the authors propose to take these two observations into account in order to define a new projection (Radon transform) on trees with a splitting map which is invariant w.r.t translation and rotations, and which takes into account the trees. Their new Radon transform is shown to be injective provided that the splitting map is invariant w.r.t Euclidean transformation. Then, they propose a splitting map which satisfies this, as well as two new more efficient ways to sample trees. Finally, they validate their new distance on several tasks such as diffusion models, gradient flows and color transfer.

### Strengths
This paper first identifies some drawbacks of the TSW-SL distance, and proposes to overcome them with a splitting map which depends on the trees sampled and which is Euclidean invariant. These new choices are well motivated and make sense.

Then, the authors provide the new Radon transform to project measures on trees using these splitting maps. They show that it is injective, and that the counterpart TSW distance is well an invariant distance. They also introduce a suitable splitting map, which they use in practice, and propose a new way to sample trees.

Finally, they experiment on challenging tasks such as generative modeling on high dimensional images with Diffusion, and demonstrate that their distance outperforms all previous Sliced-Wasserstein variants.

### Weaknesses
There is no statistical analysis of the new method. One could wonder how the distance evoluates w.r.t. the number of samples or the number of projections.

Another weakness is the lack of an ablation study, which would help us to see what really make it better than TSW-SL. Is it the new way of sampling trees which makes a big difference? Or is it because the distance is $E(d)$-equivariant? Or is it because the splitting map depends now on the distance to the lines?

There is an abuse of notation in equation (2), $Rf_\mu$ is not a probability. In equation (8), $R_{\mathcal{L}}^{\alpha}\mu$ is used, but $R_{\mathcal{L}}^{\alpha}$ is only defined on $f\in L^2$ in Equation (7).

In Section 5.2, when suggesting to sample orthogonal directions, it is stated that it is "to ensure that the sampled tree systems do not include similar directions". While I understand what is meant here; the goal is to have different directions to better capture the topology of the data; the sentence is not very clear as in practice, we would have $\theta_i\neq \theta_h$ almost surely. Note also that it was proposed e.g. in [1] to sample orthogonal directions for Sliced-Wasserstein and in [2] for a max-Sliced-Wasserstein variant, but these references are missing.

I do not think I saw the step size used for each variant of SW in the gradient flow experiment. I believe that using the same step size might not always be fair as they do not necessarily have the same scale/smoothness properties (although I would agree that it is complicated to use a different step size for each method).

Typos:
- In legend of Figure 2, the two last sentences are almost the sames.
- Line 371: "$\mathcal{L}$ is a tree system consists"
- Line 476: "Db-TSW and $\mathrm{Db-TSW}^\top$ is"

### Questions
In equation (2), $Rf_\mu$ is not a probability. So I think there is an abuse of notation. In equation (8), $R_\mathcal{L}^\alpha\mu$ is used, but $R_\mathcal{L}^\alpha$ is only defined on $f\in L^2$ in Equation (7).

In Section 5.2, when suggesting to sample orthogonal directions, it is stated that it is "to ensure that the sampled tree systems do not include similar directions". While I understand what is meant here; the goal is to have different directions to better capture the topology of the data; the sentence is not very clear as in practice, we would have $\theta_i\neq \theta_h$ almost surely. Note also that it was proposed e.g. in [1] to sample orthogonal directions for Sliced-Wasserstein and in [2] for a max-Sliced-Wasserstein variant, but these references are missing.

I do not think I saw the step size used for each variant of SW in the gradient flow experiment. I believe that using the same step size might not always be fair as they do not necessarily have the same scale/smoothness properties (although I would agree that it is complicated to use a different step size for each method).


Typos:
- In legend of Figure 2, the two last sentences are almost the sames.
- Line 371: "$\mathcal{L}$ is a tree system consists"
- Line 476: "Db-TSW and $\mathrm{Db-TSW}^\top$ is"

[1] Rowland, M., Hron, J., Tang, Y., Choromanski, K., Sarlos, T., & Weller, A. (2019, April). Orthogonal estimation of Wasserstein distances. In The 22nd International Conference on Artificial Intelligence and Statistics (pp. 186-195). PMLR.

[2] Dai, B., & Seljak, U. (2020). Sliced iterative normalizing flows. arXiv preprint arXiv:2007.00674.

### Soundness
4

### Presentation
4

### Contribution
3
