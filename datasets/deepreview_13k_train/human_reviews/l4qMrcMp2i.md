# Symmetric Space Learning for Combinatorial Generalization

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Symmetries on representations within generative models have shown essential roles in predicting unobserved combinations of semantic changes, known as combinatorial generalization tasks. However, these efforts have primarily focused on learning symmetries from only training data, and thus, the extension of trained symmetries to unseen samples remains uncontrolled. A potential approach for generalizing the symmetries is leveraging geometric information on manifolds that contain functional semantic structures for unseen data, but it still falls short of supporting symmetry learning. In this paper, we address this $\textit{symmetry generalization}$ by forcing $\textit{symmetric space}$ on latent space for utilizing semantic structures from symmetry and manifold perspectives. We clarify an equivariance-based constraint that restricts symmetry generalization, and prove that: 1) enforcing the homogeneous space property of symmetric space onto the data manifold eliminates this constraint, 2) a homogeneous latent manifold induces the data manifold through diffeomorphic data-to-latent mapping, and 3) the isometry property of symmetric space extends neighbor symmetries of a point to another within the space. For practical implementation, we propose a method to align sampled points from symmetric space with their explicitly trained geodesic. We verify the method in a detailed analysis on a toy dataset and enhance combinatorial generalization on common benchmarks. This work represents the first effective effort to align symmetries with manifolds for combinatorial generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose a method to enforce the latent space to be symmetric in order to generalize combinatorially to symmetries. By first learning the symmetric latent space from training data, the network can generalize to combinations of symmetries at inference. Specifically, they learn the geodesics of the latent manifold and extrapolate points on the geodesic by reflection. The authors provide theoretical results on how enforcing homogeneity and isometry on the latent space and using an equivariant map induces the data manifold to also be symmetric. Experiments on MorphoMNIST and dSprites show better results than baselines.

### Strengths
- The authors clearly define a symmetric space and provide proofs on how properties of the symmetric space lend themselves to unseen combinations of symmetries
- The practical implementation seems relatively straightforward and is clearly described.
- The experiments show favorable results compared to MAGANet and BetaVAE.

### Weaknesses
 - The theoretical results seem somewhat obvious and have been shown before [1]. Furthermore, there seems to be a disconnect between the theory and the practical implementation. Could the authors clarify how enforcing the various loss terms ensures that the encoder is an equivariant diffeomorphism? Specifically, the paper claims that the encoder is an equivariant diffeomorphism, but it is unclear how the loss terms enforce this property. The GLOW architecture itself is a diffeomorphism, but it is not clear how it is equivariant to the group action. The paper should provide a more detailed explanation of how the loss terms enforce the equivariance of the encoder.
- The experiments were done on somewhat toy domains. In particular, I feel that the 3D-Shape dataset shows the objects in different colors relative to the background, making the task easier. What would happen if the 3D-Shapes dataset did not include hue? The use of color as a distinguishing feature in the 3D-Shapes dataset makes the task easier than it would be if color were not a factor. The authors should consider experiments on datasets where color is not a distinguishing feature or conduct an ablation study to show how much color contributes to the results.
- Baselines: MAGANet seems to be the only baseline that aims to learn the symmetries directly. It would have been nice to consider other methods that learn symmetries [2], [3]. The authors should consider other baselines that learn symmetries, such as those that use group convolutional networks or other methods that explicitly model symmetries. The current set of baselines does not fully explore the landscape of methods that learn symmetries.

### Questions
- Figure 3: are the black lines the true geodesic? How were they computed?
- How do you find the anchor for geodesics?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method for symmetry generalization -extending trained symmetries on observed data to unseen data for combinatorial generalization. In this approach, the latent space manifold is enforced to be a symmetric space, and homogeneous conditions on the data manifold as well as the latent manifold are present. The sampling method proposed here explicitly learns geodesic symmetry, which helps reduce the computational costs for sampling and induces symmetric space for latent manifolds. 
The paper presents empirical experiments through qualitative and quantitative analysis on datasets like MNIST, dSprites and 3D-Shapes.

### Strengths
1. The paper presents a well-defined idea to build a non-rigid approach to building symmetries and uses this for combinatorial generalization. 

2. The proposed method builds a local structure in the latent manifold which can therefore be used for geodesic symmetries. I believe this approach can be useful for different tasks like latent disentanglement.

### Weaknesses
1. The proposed method uses one object per data sample, be it MNIST, dSprites, or 3Dshapes, such that the geodesic symmetry approach works with any issues of entanglement. It would be interesting to show how this extends in multi-objects set-up.

2. The homogeneity conditions proposed for both data manifold and latent manifold, might not strictly hold in the case of 2 or more objects in a sample.

### Questions
1. How does strict permutation invariance in latent generative models compare to this approach? 
2. Previous works like [1,2] are capable of representing invariant shapes as latent. How does this explicit and exact symmetry equivariant VAEs compare to this work?
3. Can this approach be extended to hierarchical latent models like NVAE? 



[1] Continuous Kendall Shape Space VAEs, Vadgama et al

[2] EqVAE:Equivariant Priors for Compressed Sensing with Unknown Orientation. Kuzina et al.

### Soundness
3

### Presentation
3

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
This paper addresses the problem of combinatorial generalization onto unseen data by enforcing the latent space to be a symmetric space. To achieve this, the paper proposes several loss terms to enforce the geodesic symmetry in the learned latent. The method is tested on standard datasets for combinatorial generalization, including dSprites and 3D Shapes.

### Strengths
The paper discusses an interesting topic, combinatorial generalization using symmetry-based representation learning.

### Weaknesses
The paper is poorly written. It contains many grammatical errors, confusing phrases, and informal statements, and it lacks coherence overall. As a result, the goal and the contribution of this paper are totally unclear to me, which is my main concern before all others. As far as I can understand, the authors are trying to address the problem in combinatorial generalization that symmetry transformation may take data points outside the training domain. This problem is indeed valid, but I fail to see how the theories in Section 3 or the method in Section 4 can solve it. In particular,
* It seems that the idea of this paper is to learn a latent space which is a homogeneous space by enforcing the model to align with the geodesic symmetry (please correct me if this is wrong). But there is not enough explanation as to why this would work. I notice Thm 3 does mention something related, but it is stated informally and vaguely (e.g. What does it mean by "make symmetric space **enough**"? ) and the proof is missing.
* The method involves approximating the geodesic. It simply parameterizes an arbitrary path in the ambient and penalizes its length in the interval $t \in [0, 1]$ and the reversal symmetry error at a single point $t=-1$. There is no justification for why (1) this would result in a path that stays on the latent manifold (moreover, the latent manifold itself has not been identified anywhere in the discussion), (2) the learned path function would generalize to $t<0$, and (3) the geodesic symmetry would hold for all $t$ instead of only at $t=1$.
* The role and properties of the anchor $a$ are also not adequately explained. It is unclear whether any constraint needs to be enforced for this learnable anchor to make sure its properties match those in the definition of symmetric space.
* I am also confused by the fact that, generally in symmetry-based representation learning, the symmetry transformations represent the factors of variations, and depending on specific data generation procedures there should be different symmetry groups, while this paper seems to only consider the geodesic symmetry as defined in Defn 3.

Some other less major concerns, mainly about presentation and organization of the paper:
* Definitions in Section 2: instead of making a separate paragraph title (e.g. symmetric space), you can specify the terminologies right after the definition header (e.g. Definition 3 (symmetric space)).
* Definition 3: is there a confusion between $o$ and $a$? Should it be $T_a \mathcal M$? Also, what does it mean by "$U$ can be extended to the entire manifold"?
* Section 3 can be made more concise. The proofs are too verbose. Statements like Prop 2 and Thm 1 just directly follow from definitions.
* Thm 1: Let $X, X'$ be partitions of a manifold $\mathcal M$. This statement is misleading. Partition can mean different things according to context. If the authors mean these two sets are disjoint and their union is the entire manifold, a better way to phrase it may be ``$\{X, X'\}$ is a partition of $\mathcal M$''.
* The training objective, Eq (9), involves a base loss from another paper called MAGANet. This name came out of nowhere for the first time in L315. The authors should explain this in more detail, or at least reference the original paper here. Also, the authors should discuss whether the proposed method can only be applied to MAGANet, which would be a potential limitation.

### Questions
* What is $\epsilon$ in Eq (2)? Is it a random noise? What is the reason for adding a noise component to the path $\gamma$?
* Can the proposed method be applied to models other than MAGANet?
* Why do the results in Table 1 have such large differences? Does a BCE of 3000+ indicate total failure? Also, for the 3D Shapes dataset, $\beta$-VAE ($\beta=2$) seems to perform best in all cases. Why is your method highlighted then?
* In Fig 1 caption: Why is the volume form related to the likelihood?
* Can you elaborate on why you need to exclude three specific combinations of factors?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the symmetry generalization problem in the latent space of a dataset. Specifically, the authors assume the data manifold and its latent space are homogeneous with some group actions, then the unseen samples can be generalized by some group actions on the existing samples as the group is assumed to act transitively.

### Strengths
The authors propose a novel approach through learning the symmetry in the latent space to solve the combinatorial generalization problem in the data space.

### Weaknesses
1. The paper is not carefully written with several grammatical errors. For example, the first sentence of Proposition 2; between line 172-173, "However, encoding data onto a latent manifold enables data to be handled in lower dimensional and easy-to-compute data."

2. Condition 3 is the key assumption of this paper, but it is too strong without any justification. Specifically, the assumption that the group action in the latent space perfectly aligns with the data manifold's symmetries is not generally true. There is no discussion about the potential for misalignment or how the method would perform if this condition is not met, which is likely in real-world scenarios.

3. I'm confused by the last sentence between line 174-175, is $\mathcal{N}\subset\mathcal{Z}$ or vice versa?

4. The math part is presented in a redundant way. I think the authors can make it more clear by clarifying all the assumptions at once. Also, the propositions and theorems are trivial, and they are essentially the mathematical formulations of the assumptions. The core issue is that the paper lacks theoretical novelty; the 'theorems' are simply restatements of the assumptions in mathematical terms, offering no new insights into the properties or behavior of the proposed Geodesic Symmetries. The mathematical formulations do not provide any deeper understanding beyond the initial assumptions.

5. Condition 4 is also a very strong assumption, and it requires $\mathcal{M}$ to have the same dimension as $\mathcal{N}$, so why is $\phi$ an encoder? The requirement that the mapping $\phi$ be invertible, differentiable, and diffeomorphic is overly restrictive. This limits the applicability of the method to a very specific class of mappings and does not account for more general, non-invertible encoders that might be more suitable for complex data manifolds. The assumption that the latent space has the same dimensionality as the data space is also a significant limitation, as dimensionality reduction is a key motivation for using latent spaces.

### Questions
See Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
1
