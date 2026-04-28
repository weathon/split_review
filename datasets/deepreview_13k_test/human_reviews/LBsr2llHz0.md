# More Space Is All You Need: Revisiting  Molecular Representation Learning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Molecular representation learning (MRL) has become pivotal in leveraging limited supervised data for applications such as drug discovery and material design. While early MRL methods relied on 1D sequences and 2D graphs, recent advancements have incorporated 3D conformational information, focusing predominantly on atomic interactions within 3D space. However, we argue that the space beyond atoms is also crucial for MRL, which is overlooked by prior models. To address this, we propose a novel transformer-based framework, dubbed SpaceFormer, which incorporates additional 3D space beyond atoms to enhance molecular representation ability. 
SpaceFormer introduces three key components: (1) Precision-Preserved Gridding, which discretizes continuous 3D space into grid cells while preserving precision; (2) Grid Sampling, which employs an importance sampling strategy to improve efficiency; and (3) Linear-Complexity 3D Positional Encoding, which extends Rotary Positional Encoding to 3D space to capture pairwise directions and utilizes random Fourier features to efficiently encode pairwise distances. Extensive experiments show that SpaceFormer significantly outperforms previous 3D MRL models across various tasks, validating the benefit of leveraging the additional 3D space beyond atoms in MRL models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel architecture for point-cloud molecular data based on the PCA normalization followed by a space transformer. The results seems to be on the SOTA level. However, the Reproducibility Statement is missing and the code is not attached. It's therefore very hard to evaluate the model.
Technically, the innovations are controversial. A lot of stress in the paper is put on SE3 invariance with respect to global rotation/translation. However, after the PCA, the input representation is already invariant. Another stress is put into absolute positional encoding in SE3. Here, no prior work on geometric attention/transformers is cited, where the same problem has been already solved for point cloud and graph representations. Also, the proposed solution is not rigourosly correct. Finally, I question the gridding technique, why it is needed here as the main blocks operate on continuous positions? Again, sampling additional points in geometric/graph attention and transformer architectures have been well studied in the literature, and must be properly cited.

### Strengths
The paper is well written and presents a model that outperforms the state of the art. The author even retrained and experimented with the SOTA architecture Uni-Mol.

### Weaknesses
The Effective Cuboid for Gridding -- the PCA vectors have arbitrary sign, and also uncertainty in the directions if two or more eigenvalues are close in value. As a result, you may have instability, at least with respect to the sign of the frame. This issue has to be at least discussed. Ideally, more experiments need to be run with sign flip of the PCA vectors.

3D Angular Positional Encoding with RoPE is very misleading. You seem to operate on directions from an arbitrarily chosen coordinate center, and measure relative angles with respect to this center. Does it make any sense? It wouldn't make sense even in 2D... Could you please draw the 2D geometry and explain what will be this angle?
The relative angle is indeed invariant to an in-plane rotation. However, it will change with a different choice of rotation plane, and it will also change with a different choice of the coordinate system (the center of rotation).

The Gaussian kernel approximation has to be validated and explained better, it's very nontrivial why a non-periodic function can be decomposed through products of periodic functions. Even the original paper states "For the Gaussian kernel, k(δ) is not convex, so k is not everywhere positive and δk(δ) is not a probability distribution, so this procedure does not yield a random map for the Gaussian."

More generally, your representation is rather similar to the point-cloud representation with some additional sampling points (which have been studied in the literature), as you are using continuous coordinates as input and full-length attention. Could you please clearly identify the benefits of additionally encoding grid-related parameters?

Sampling empty grids is similar to constructing virtual or aggregation nodes in point-cloud or graph representations. It will be useful to discuss it. Another analogy is stochastic sampling strategy to compute attention better than in N^2, which is used in some recent architectures, please discuss it too.

### Questions
We incorporate FlashAttention (Dao et al., 2022), reducing the memory cost from O(n2) to linear complexity - this statement is not fully correct. The FalshAttention paper states : We analyze the IO complexity [1] of FlashAttention, proving that it requires 𝑂(𝑁^2𝑑^2 𝑀^-1) HBM accesses where 𝑑 is the head dimension and 𝑀 is the size of SRAM.
So, it will only scale linearly when the cache size is bigger than Nd (or, formally, is a function of (ND). Which is not the case if the size of your system grows bigger.
The linear scaling is questionable even looking at the experiments (table 6). Models no 13-14 have an increase in the number of cells by 15%, but the time doubles -- this probably indicates the regime when you saturate the SRAM. Please correct the statements.

"Second, in 3D MRL models, SE(3)- invariant positional encoding" - you already claim to work in invariant frames (after the PCA), the SE3 invariance is not needed here it seems. Motivate the SE3 invariance better please. Maybe you simply gain in performance because of the PCA normalization?

"While the above RoPE-based encoding ... it may be unstable when the entire system undergoes global rotations.", well, it is not supposed to be unstable by design, this was the main idea of RoPE. If it is unstable, please clearly explain why. More generally, you are already using the pose normalization method (PCA), you are INVARIANT to global rotations and translations. So, I believe, this argument is not valid.

"utilizing a 3D positional encoding that is invariant to global rotation and translation" - again, you are in the PCA frames, why do you discuss it?.

In 3D, the actual rotation depends on the sequence of 3 individual rotations (see Euler angle conventions, for example).. Which one do you use? How do you decompose a 3D rotation into 3 rotations about different axes? Does it make any difference? How stable the result will be if you remove the PCA normalization?

Some minor points:
"which is inspired from microscopic physics where regions near atoms are more crucial." - more crucial for what?
"regions close to atoms exhibit higher electron density" - better say close to atom centers, or to nuclei centers
"in computational simulations, coarse-graining is commonly applied to regions farther from atoms to reduce computational cost." - please explain it better and more rigorously
"Therefore, our sampling strategy is based on the distance from the nearest atom cells." - you can motivate it in a simpler way.

Can the learned representations (Figure 2) be connected to the way you sample empty space using the importance sampling? What will be the representations using uniform or other types of samplings?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
I appreciate the opportunity to review this manuscript on "More Space Is All You Need: Revisiting Molecular Representation Learning."
The paper presents SpaceFormer, a transformer-based framework for molecular representation learning that aims to demonstrate how leveraging 3D space beyond atoms can enhance molecular representations. The work introduces grid-based sampling and combines RoPE and RFF techniques.

### Strengths
- Novel combination of RoPE and RFF techniques
- Innovative grid-based sampling approach for spatial representation
- Interesting comparison with Uni-Mol using randomly sampled empty points
- Technical innovation in spatial representation methodology

### Weaknesses
Reproducibility Concerns
A critical issue that must be addressed immediately is the lack of code availability. This significantly hampers reproducibility - a cornerstone of scientific research. The code should be considered an extension of the experimental setup, and its absence makes proper evaluation challenging. Without access to the implementation details and the ability to reproduce the results, it becomes difficult to fully validate the claims and insights presented in the paper.

Fundamental Research Question and Historical Context
A significant concern lies in the paper's central research question: "Will leveraging the 3D space beyond atoms improve molecular representation learning?" This framing overlooks substantial existing work in the field. Models like ANI and SchNet have already definitively demonstrated the value of considering complete 3D space through their use of Behler-Parrinello symmetry functions and sophisticated spatial representations. These established approaches already:
- Capture the complete local chemical environment
- Incorporate radial and angular features describing inter-atomic spaces
- Map the entire local 3D space around atoms into feature vectors
- Consider continuous space rather than just discrete atomic positions
Therefore, the more appropriate research question should focus on finding novel, potentially more efficient ways to represent and process 3D spatial information, rather than questioning whether such spatial consideration is beneficial.

Technical Innovation and Comparative Analysis
While the paper's technical approach using grid-based sampling shows innovation, the comparative analysis raises concerns. The baseline model selection appears inadequate, particularly given the availability of established models that already leverage 3D space effectively. The manuscript's results show that SchNet frequently outperforms the proposed SpaceFormer model on the QM9 dataset. The absence of comparisons with models like ANI2 or SchNet requires justification, especially given their relevant capabilities and established performance.

Technical Implementation Concerns
The use of PCA for coordinate system alignment presents potential issues that need addressing. PCA axes can flip when eigenvalues are similar, potentially leading to arbitrary axis assignments. This could be particularly problematic for molecules with different conformations. The manuscript should address:
- Whether this possibility was investigated
- The proportion of affected molecules in the dataset
- Potential solutions, such as augmentation approaches involving random rotation and translation of voxel boxes

Visualization and Explainability
Two significant improvements would enhance the manuscript:
- The latent space structure after pre-training needs thorough examination through ablation studies. Understanding what the model actually learns would improve transparency and help readers better grasp the embeddings' potential applications in downstream tasks.
- Figure 1's representation of the gridding and grid sampling approach should more clearly demonstrate its 3D nature to avoid ambiguity.

### Questions
1. How do you address PCA axis flips when eigenvalues are similar?
2. Why were comparisons with ANI2 and other established models omitted?
3. Can you provide ablation studies examining the latent space structure (what has been learned)?
4. How will you ensure reproducibility through code availability?
5. What percentage of molecules in your dataset are affected by PCA alignment issues?
6. How do you justify the model's performance given e.g. SchNet's superior results on QM9?

(For more details look at the strengths and weaknesses above)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SpaceFormer model for molecular representation learning which is based on transformer. Compared to previous methods which focus solely on atom/graph level information, SpaceFormer aims to capture spatial information more precisely by taking into account the 3D space beyond just atomic positions. For this purpose, the paper introduces methods for discretizing 3D space for computational efficiency while preserving precise atomic information and benchmarks the model on multiple downstream property prediction tasks.

### Strengths
1. The paper is well-motivated with physical principles and to my knowledge, introduces a novel MRL framework to explicitly capture the 3D spatial information beyond atomic positions. This allows the model to capture subtle spatial interactions between atoms that maybe crucial for molecular property. 
2. To handle the infinite nature of 3D space and the computation costs associated with processing grid based representations of molecules, the authors propose extensions of several techniques known in different domains. For example,  the discretization procedure, the 3D angular positional encoding with RoPE and 3D radial positional encoding with RFF are sensible extensions of known techniques for the problem at hand.
3. The model is tested on multiple downstream tasks, demonstrating SpaceFormer’s effectiveness across a range of MRL applications.
4. The paper is well-written and easy to read.

### Weaknesses
1. Although grid discretization captures spatial information efficiently, it does inherently divide continuous 3D space into discrete cells. Could this lead to a loss of spatial continuity, especially when atoms or interactions lie near cell boundaries?
2. Can the proposed model handle irregular molecular shapes? The experiments considered in the paper are on simpler molecules. When extending it to irregularly shaped molecules, I wonder if the cuboid might include substantial regions without atoms, which could reduce efficiency?
3. The approach relies heavily on accurate atomic positions and bond distances, which might not always be readily available or precise for all molecular structures, especially in experimental or noisy datasets. Have the authors studied this aspect?
4. Do I understand it correctly that the proposed method uses a fixed grid size within the effective cuboid, which may not adapt well to regions with varying atomic densities. For densely packed regions, the chosen grid size might be too coarse, while for sparsely packed regions, it may be overly fine? 
5. The paper studies the model performance under two kinds of data splits: In-Distribution Split, where the sets are randomly partitioned, and Out-of-Distribution Split, where the sets are divided based on fingerprint similarity. The Out-of-Distribution Split is somewhat realistic setting however in real-world drug discovery applications, much more common splitting strategies are scaffold split or temporal split. I would be curious to see how the model performs under such settings.
6. The paper mentions several related works but the baselines compared against SpaceFormer are rather limited. How does the proposed model compare against works such as NoisyNodes, GraphMVP, 3D-InfoMax etc.?

### Questions
I have listed my questions in the weaknesses section already. To summarize:
1. Could the discretization process lead to a loss of spatial continuity, particularly when atoms or interactions lie near cell boundaries? How does the model account for this, if at all?
2. Can the proposed model efficiently handle irregularly shaped or large molecules? 
3. Given that the model relies heavily on accurate atomic positions and bond distances, how does it perform on experimental or noisy datasets where such information may be less precise or unavailable?
4. Does the use of a fixed grid size within the effective cuboid limit the model’s adaptability to regions of varying atomic density? I may have misunderstood this aspect.
5. Could the authors comment on how SpaceFormer might perform under more real-world splitting strategies (temporal and scaffold splits) for training and evaluation?
6. Could the authors provide comparisons to how the model performs relative to other recent works, such as NoisyNodes, GraphMVP, or 3D-InfoMax?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes SpaceFormer, a transformer-based model for Molecular Representation Learning (MRL) that incorporates information from the 3D space beyond atomic positions. The authors argue that this empty space contains valuable information relevant to molecular properties. SpaceFormer receives as input the discretized 3D space around a molecule as a grid of cells, where cells containing atoms are distinguished from non-atom cells. For better computational efficiency, the non-atom cells are subsampled using an importance sampling strategy. The authors conduct experiments to assess the performance of SpaceFormer on several benchmarks for molecular property prediction.

### Strengths
+ The authors perform ablation studies to analyze the contribution of each component of SpaceFormer, providing insights into the importance of each design choice. The ablation studies on grid sampling are particularly informative, showcasing the trade-off between performance and efficiency.

+ The authors extend the Uni-Mol baseline by incorporating randomly sampled empty points, allowing for a direct comparison between an existing atom-based models with and without empty space consideration. This strengthens the claim that SpaceFormer's approach of explicitly modeling empty space within a grid structure is more effective.

### Weaknesses
- The benchmark results for QM9 shown in Table 1 suggest that the performance of SpaceFormer would be SOTA, but this is not the case. Several published atom-based models designed for regression on molecular properties achieve significantly better results (see e.g. http://proceedings.mlr.press/v139/schutt21a/schutt21a.pdf for an already 3 year old model that is better). Further, the authors should explicitly report the units (I simply assumed that the default QM9 units are used), otherwise no meaningful comparisons to published work are possible.

- While the paper reports performance on QM9, this is a quite old and rather simple benchmark (perhaps comparable to MNIST in computer vision) and the field has since moved to more sophisticated benchmarks, e.g. MD17, MD22, or QM7-X. I think additional experiments and comparisons to SOTA models on (at least one of) these datasets would be very insightful.

- The ablation studies and the comparison to an atom-only model is a good start, but I believe they are flawed: Since the atom-only model processes significantly fewer tokens, it has in a sense "less internal FLOPs" compared to models that also process tokens for empty space. It would be more insightful to see results for an experiment where this is controlled for, for example by increasing the width/depth of the atom-only model to achieve "compute-parity". This would allow to see whether the empty space tokens are useful conceptually, or whether they simply increase the amount of compute the model can leverage.

- The resemblance between electron density and the learned representations shown in Figure 2, as well as the conclusions drawn from it (e.g. that this is evidence that SpaceFormer learns meaningful physical relationships) is questionable. It is trivial to produce a surface that resembles electron density simply by using the distance to the atoms. For example, just take the $\sum_{i=1}^{N} \lVert \vec{r} - \vec{r}_i \rVert^{-2} = 1 a_0^{-2}$ isosurface and you will get something that resembles the electron density much more closely than the representations learned by SpaceFormer. (Here, the sum runs over the $N$ atoms in the structure, $\vec{r}_i$ is the position of the $i$-th atom, $\vec{r}$ is the "query point" in 3D space, and $a_0$ means Bohr, i.e., the atomic unit of length.)

- While the authors motivate incorporating empty space by mentioning some physical principles/facts (e.g. that electric fields and electron density extend beyond atoms), the paper lacks a formal theoretical analysis of why and how this information contributes to better molecular representations. A theoretical foundation would significantly strengthen the paper's contributions.

### Questions
* Can you provide a quantitative comparison between the learned representations and the corresponding electron density maps? As a baseline, something like a distance-based isosurface (see above) would be useful (the used isovalue should of course be optimized, I just put $1 a_0^{-2}$ for simplicity).

* How do you choose the coordinate system in cases where the eigenvectors determined by PCA are degenerate (for example for molecules with $\mathrm{T_d}$ or $\mathrm{O_h}$ symmetry)?

* The authors mention that the encoding of angular directions may be unstable when the entire system undergoes global rotations. I don't see how this can happen if you choose a coordinate system based on PCA eigenvectors (this should give a sort of "canonical orientation"). Can the authors elaborate?

* How does the performance of SpaceFormer vary with different grid resolutions? Have you experimented with adaptive gridding strategies to address potential limitations for larger molecules or systems with varying densities?

* What are the specific challenges you anticipate in extending SpaceFormer to larger systems like proteins, and what potential mitigation strategies are you considering?

**Additional Feedback:**

* Consider adding a discussion about the computational cost of SpaceFormer during training and inference, compared to other 3D MRL models.

* The paper mentions future work on extending SpaceFormer to larger systems like proteins. However, the current grid-based approach could face scalability issues with larger systems due to the cubic growth in the number of cells. Discussing potential strategies for mitigating these challenges would be helpful.

### Soundness
2

### Presentation
3

### Contribution
2
