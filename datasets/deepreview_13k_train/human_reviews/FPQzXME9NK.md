# Spherical Tree-Sliced Wasserstein Distance

- Decision: Accept
- Scores: 6, 6, 8, 6, 6

## Abstract
Sliced Optimal Transport (OT) simplifies the OT problem in high-dimensional spaces by projecting supports of input measures onto one-dimensional lines, then exploiting the closed-form expression of the univariate OT to reduce the computational burden of OT. Recently, the Tree-Sliced method has been introduced to replace these lines with more intricate structures, known as tree systems. This approach enhances the ability to capture topological information of integration domains in Sliced OT while maintaining low computational cost. Inspired by this approach, in this paper, we present an adaptation of tree systems on OT problem for measures supported on a sphere. As counterpart to the Radon transform variant on tree systems, we propose a novel spherical Radon transform, with a new integration domain called spherical trees. By leveraging this transform and exploiting the spherical tree structures, we derive closed-form expressions for OT problems on the sphere. Consequently, we obtain an efficient metric for measures on the sphere, named Spherical Tree-Sliced Wasserstein (STSW) distance. We provide an extensive theoretical analysis to demonstrate the topology of spherical trees, the well-definedness and injectivity of our Radon transform variant, which leads to an orthogonally invariant distance between spherical measures. Finally, we conduct a wide range of numerical experiments, including gradient flows and self-supervised learning, to assess the performance of our proposed metric, comparing it to recent benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper is a natural extension of sliced spherical OT to incorporate tree systems. The authors propose a topological space on spheres called spherical trees by connecting spherical rays with a common root. They then adapt Radon transform onto the spheres and slice the trees which is equivalent to slicing the spheres with trees. After showing that spherical tree are metric spaces, the authors followed classic approach of adapting the OT computation in the tree-sliced spheres. They provided comprehensive theoretical and empirical results to support their theories.

### Strengths
The motivation is justified and the narrative follows standard ones when substituting simpler structures with more sophisticated variants for solving specific OT problems. Claims have been proved by theoretical results and verified by empirical results.

### Weaknesses
While I didn't find major weaknesses in the paper, the authors didn't provide sufficient theoretical explanation in several critical places. The proposed STSW outperforms baselines in all most all metrics. First, why did the variances in Table 1 so small, smaller than one tenth of other methods in most lines, under Monte Carlo sampling? Why did STSW outperforms other baselines in terms of runtime? The theoretical complexity the authors provided cannot explain it. Why didn't the better runtime translate to a similar margin in reducing the training time in Table 2? Another point is that the authors attributes the better performances to "the ability to capture topological information of integration
domain" of STSW but they didn't show a direct connection in the paper. The results from the CIFAR dataset are not that impressive and the visualization didn't help either in explaining them.

### Questions
419: "STSW outperforms the baselines in all metrics and achieves faster convergence." Why is that? Is this result theoretically predictable? 

466: "We also conduct experiments with $d=2$ to visualize learned representations." Why don't we directly project the learned features in the original image space to a sphere, rather than redoing the experiments on the sphere?

443: The variances from STSW are quite small. What's the explanation of that? Why doing tree-slicing on spheres is more robust (against different sampling?)?

We have seen spherical trees in the following article, although it's for a different application and the construction of the trees is different as well. Is there any connection between this work and that? 

Meng, Yu, Yunyi Zhang, Jiaxin Huang, Yu Zhang, Chao Zhang, and Jiawei Han. "Hierarchical topic mining via joint spherical tree and text embedding." In Proceedings of the 26th ACM SIGKDD international conference on knowledge discovery & data mining, pp. 1908-1917. 2020.

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
This paper introduces the Spherical Tree-Sliced Wasserstein (STSW) distance, an efficient optimal transport (OT) metric for measures on a spheres. By leveraging a novel spherical Radon transform that integrates over spherical tree structures, it provides closed-form OT solutions and maintains computational efficiency. Theoretical analysis and experiments, including gradient flows and self-supervised learning, confirm STSW’s effectiveness and its performance against recent benchmarks.

### Strengths
* Paper is very well-written.
* Through extensive experiments, the effectiveness of the STSW has been investigated.
* Paper introduces a novel Radon transform for the measures on the spherical trees.

### Weaknesses
 * While STSW aims to be efficient, the spherical Radon transform and tree-slicing require considerable computation, especially as the number of edges or the dimension of the hypersphere increases. This could limit scalability for very high-dimensional or densely-sampled spherical data, impacting runtime in large-scale applications. Although I understand that the authors have provided extensive runtime comparisons, I would like to see the scalability of the method on higher-dimensional tasks beyond CIFAR, MNIST, and similar datasets. Specifically, the computational cost of generating and processing spherical trees, which involves operations like geodesic distance calculations and tree traversals, should be analyzed more rigorously. The paper should include a breakdown of the time complexity associated with each step of the STSW calculation, particularly how these scale with the dimensionality of the sphere and the number of tree edges.

* The effectiveness of STSW relies on the quality of sampled spherical trees, which introduces variability in metric accuracy. If the sampling process fails to capture diverse spherical structures adequately, STSW’s results might be inconsistent, especially in complex distributions where more refined tree structures are necessary. I would like to see which strategies (e.g., Markov Chains, Random Paths, etc.) could be applied here to sample more informative slices. Furthermore, the paper lacks a discussion on how the choice of tree structure (e.g., balanced vs. unbalanced, depth, branching factor) impacts the performance of STSW. It is unclear how the tree topology influences the ability of STSW to capture the underlying geometry of the data distribution on the sphere. A more detailed analysis of the relationship between tree structure and STSW performance is needed.

### Questions
* I was wondering if incorporating a Markov chain over the distributions of the slices, instead of using a uniform distribution, could help in generating more informative tree-slices.

* I am interested in understanding the topology of the tree corresponding to the most informative slice in spherical trees and compare its effectiveness to the most informative slice in SSW, and essentially comparing them to the most informative slice in SWD. (By the most informative slice I mean Max-slice). This can be done on a chosen benchmark.

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
3

### Summary
This paper introduces the Spherical Tree-Sliced Wasserstein (STSW) distance, a novel metric designed for optimal transport on spherical domains. The key innovation lies in the integration over spherical trees as the domain, rather than traditional one-dimensional lines or great semicircles used in existing spherical Sliced Wasserstein approaches. This change allows STSW to better capture the underlying topology of spherical data, offering closed-form solutions that enhance both performance and computational efficiency.

The authors introduce a variant of the spherical Radon Transform tailored for spherical trees and prove its injectivity. Defining the STSW in terms of this transform is essential for establishing the metric properties of the distance, including its invariance under the action of the orthogonal group.

### Strengths
The paper is well-structured, presenting clear objectives and a comprehensive review of related work. 
The efficiency of the new metric is well presented in the experiments. 

Leveraging on the ideas presented in Tran et al. (2024b), as said before, this reviewer things that the key innovation of this article (over articles as Bonet et al. (2022) and Tran et al. (2024a)) lies in the integration over spherical trees for defining the new metric between spherical probability measures.

### Weaknesses
The approach builds on previous work by Bonet et al. (2022) and Tran et al. (2024a), in the sense that uses the same hight-level ideas. 
However, while the research incrementally follows the line of previous studies by Bonet et al. (2022), Tran et al. (2024a), and Tran et al. (2024b), it offers meaningful advancements by developing a metric specifically adapted for spherical data analysis.
Also, the experiments closely follows experiments previously presnted in papers as Bonet et al. (2022).

### Questions
Besides the experimental comparisons of the new STSW with SW, SSW, and S3W variants, are there any analytic comparisons among them? Which are the differents in the topologies defined by these different approach?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a variant of the Wasserstein distance for distributions defined on the hypersphere. The proposed metric, called the Spherical Tree-Sliced Wasserstein (STSW) distance, adapts the Tree-Sliced Wasserstein distance to be applicable to the hypersphere by defining a novel spherical Radon transform. The proposed metric is invariant to orthogonal transformations, and can be computed efficiently.

### Strengths
* The paper is well-written. 
* The paper proposes an efficient extension of the Sliced Wasserstein distances applicable to hyperspheres and the construction of the Radon transform is well-motivated.
* The authors also show desirable properties of their proposal, such as invariance to orthogonal transforms.
* On the practical side, the authors propose an efficient way to compute such a metric and show its effectiveness and superior performance in various experiments.

### Weaknesses
 * The proposed metric is limited to hyperspheres. The paper's contributions appear to be incremental, primarily combining previously established concepts (tree systems and Sliced Wasserstein distances) and extending them to the sphere setting.
* One of the claimed contributions is a bit misleading. Specifically, the authors claim to derive a closed-form expression; however, its computation still relies on approximations: first, due to the need for sampling trees, and second, by considering only discrete distributions in the explanation of how it is computed. This should be clarified, as the current claim gives the impression that the distance can be computed exactly due to the closed-form expression.
* Line 65 states that the use of tree systems enhances the capture of topological information. However, it is not so clear to me why is this the case. An experiment demonstrating this advantage would be useful.

### Questions
- **Impact uniformity loss**: How should we understand $STSW(z^A,\nu)$ in eq. 20?  $z^A$ is a single point, so I assume we are considering a Dirac distribution at $z^A$. Theoretically, the distance from a Dirac distribution to a uniform distribution in the sphere is constant regardless of where the Dirac distribution is placed, due to invariance to rotations, right?  Why does this term favour uniformity if it is a constant term? Or am I misunderstanding something?
- **Radon Transform measure preservation**: Why does the proposed Radon transformation in eq. 8 transform a probability distribution $\mu$ defined on $\mathbb{S}^d$ into a probability distribution defined on $\mathcal{T}$? This is mentioned in lines 332-333, but in line 268 it says that $||\mathcal{R}_{\mathcal{T}}^{\alpha}f||\leq||f||_1$.  So it does not immediately follow that the Radon transform preserves the measure.
- **STSW Computation on continuous measures**: In section 5 you explain how to compute STSW in practice, but it is assumed that the probability distributions are discrete.Is it possible to get a closed form analogous to that in eq. 19 for non-discrete distributions? 
- **Injectivity of the radon transform**: In Theorem 4.3 it is proved that if the splitting map is $\mathcal{O}(d+1)$-invariant, then the spherical Radon transform is invariant. What would be the consequences of using a non-injective spherical Radon transform? What structure might be missed?

**Minor & Typos:**  
- l. 170 "be **a** positive"
- l. 372 $\nu(x)=\sum_{j=1}^n$ 
- In l. 322 change notation of $\delta$ to other letter, in order to avoid possible confusion with the Dirac delta function.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel way to measure distances between probability distributions on hyperspheres, coined Spherical Tree-Sliced Wasserstein (STSW). The core technical contribution lies in adapting tree-based structures from [1] to work on spheres (spherical trees) and defining a new type of Radon transform for these structures. The authors prove this approach leads to closed-form solutions for optimal transport problems and show that STSW is a valid distance metric on $\mathcal{P}(\mathbb{S}^d)$. Through various experiments including gradient flows, density estimation, and self-supervised learning, they show that STSW can perform competitively with/better than the baselines while having faster runtime.

---

[1] Tran, Viet-Hoang, et al. "Tree-Sliced Wasserstein Distance on a System of Lines." arXiv preprint arXiv:2406.13725 (2024).

### Strengths
S1. This method addresses an important problem of comparing distributions on the sphere, which has applications in many fields.

S2. Extending the tree-sliced concept to spherical domains is novel and non-trivial.

S3. The writing in the main paper is rigorous, coherent, and easy to follow.

S4. STSW is proved to be a proper metric (compared to SSW [2] which is only known to be pseudometric) with a novel splitting maps that preserve orthogonal invariance.

S5. STSW appears to outperforms various baselines in terms of runtime and other quantitative metrics.

S6. The algorithm is straightforward to implement.

---

[2] Bonet, Clément, et al. "Spherical sliced-wasserstein." arXiv preprint arXiv:2206.08780 (2022).

### Weaknesses
W1. Sampling: In the algorithm, the authors propose sampling uniformly from R^{d+1} and then normalizing to get points on S^d, which does not produce a uniform distribution on the sphere. Would this induce a bias (and implications)? 

W2. Ablation: The paper would be strengthened if there are more insights provided via ablations on different design choices (i.e., rays, trees). How does the current tree structure help capture the data better than existing methods? Are there limitations, theoretical issues, or numerical instability associated with different components of the method (i.e., S3W [3] has the north pole issue). Can the splitting maps be learned? etc.

W3. Runtime and Complexity: It would be nice to have an explicit discussion of the computational/memory complexity (this is aside from the information provided in Appendix B).

W4. Experiments: This may be a minor point, but setup and hyperparameters could be better documented for all methods. In addition, there is no comparison with Vertical SW in appropriate setups. For generative experiments, there are no samples, of quantitative measures of the quality of images (i.e. the FID score).

### Questions
- What makes STSW run faster than S3W [3], and in some cases, SW?

- The tree structure is supposed to capture 'richer' topological information per the authors' claim. How does that translate to practical results? Have the authors explored different hyperparameters to confirm that the superior performance in these setups is due to the tree component of the method? Traditional trees in euclidean spaces often have a hierarchical structure; here, it appears that our design choice is not hierarchical? If so, then what are the concrete benefits?

- Are there relationships to the OT distance on the spheres?

### Soundness
3

### Presentation
3

### Contribution
2
