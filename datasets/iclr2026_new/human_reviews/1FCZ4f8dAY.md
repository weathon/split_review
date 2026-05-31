## Human Reviewer 1

### Summary
The paper claims to provide a full characterisation of G-equivariant polynomial functions from tuples of tensors to tensor outputs, where the group G is a classical Lie group. The authors apply their characterisation in a number of numerical experiments where the input data is a tuple of vectors.

### Strengths
- This is a very strong paper, both in its theoretical contributions and practical results. I commend the authors for such a well-written, densely packed presentation. I felt like I learned a lot as I got into the weeds while reading it.
- To the best of my understanding, I can see that the authors have characterised O(d)-equivariant polynomial functions from tuples of tensors to a tensor output, and have also considered the particular case where the input is a tuple of tensors instead (so that this can be used in their experiments for practical reasons, as the authors state in the paper). I can also see that they have extended this to O(s, d-s) and Sp(d) equivariance for entire functions too. (I say best of my understanding as I haven't gone through every single line of the proofs but I have gone through a decent amount of it + with my background in this area I can see that it is clearly correct.)
- I particularly enjoyed the authors explaining complex equations in words immediately after they are introduced (e.g after Corollary 1). I will be stealing this idea for my own papers in the future.
- The results are clearly significant and deserve top billing at ICLR.

### Weaknesses
It is hard to come up with too many weaknesses, but I think the authors should consider the following:

- I think the claim that the authors make in lines 49-50 is too strong (this is repeated in lines 475-476). "General" sounds like it could be used for any group, which I don't think is what the authors are claiming. 
- The theory looks at the generic O(d) group action, allowing p to be +1 or -1, which is extended to other classical Lie groups. However the practical experiments only consider the O(d) case for the +1 case, which (to the uninitiated) might make the theory somewhat "overkill". Are there any practical uses of their theory in the -1 case?
- Whilst the related work is pretty comprehensive, I think they are missing a reference to the potential related work [1] which looks at characterising O(d) and Sp(d) equivariant functions between tensors, exactly of the form they have considered when the input tuple is of length 1. Could the authors perhaps comment on the differences between the two papers beyond this?

[1] Pearce-Crump, E. - Brauer's Group Equivariant Neural Networks (ICML 2023).

### Questions
Beyond the questions asked in the Weaknesses section:

- The authors note that their Theorem 1 is impractical for computing purposes. Could they clarify further why that is, and if they have thought of any ways to mitigate this so that the theorem in all its glory could be employed in neural networks?
- I might have missed this but where are the non-linearities included in the characterisation/paper?


Other minor questions/points:
- Should there be a standard deviation reported for their model in Table 2 for O(d)?
- I think in their Example 1 equation (13), there should be a delta after beta_1<a, a> - do the authors agree?
- In line 253 I think they should refer directly to (107) instead of Appendix D for the definition of G_4 - I originally thought it was a typo for S_4.
- I think the authors in their Definition section should introduce the plus/minus notation where they write e.g 2_(+), just so that it is 100% clear to everyone. There is a lot going on and since it is used a lot (in place of p = +1, -1), I think the notation should be introduced explicitly.
- Anything else they can do (e.g in the Appendix) to make their examples even clearer (say, by providing more steps) would be useful in helping the reader to understand all of the concepts that are introduced in Section 2.

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
10

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper develops equivariant neural network architectures for tensor-valued data under orthogonal, Lorentz, and symplecticsymmetries. The method constructs outputs as linear combinations of outer products of inputs and isotropic tensors, with coefficients given by learnable scalar functions $q_{t,\sigma,J}$. These scalar functions are implemented as MLPs acting on the set of pairwise invariant inner products between input vectors, ensuring equivariance under the chosen group without relying on Clebsch–Gordan tensor products. The framework generalizes previous O(d) methods to indefinite orthogonal and symplectic groups, and experiments on stress–strain tensors, path signatures, and sparse recovery demonstrate flexibility and improved inductive bias.

Overall, this is a strong and well-motivated contribution that provides a clean, general, and computationally efficient formalism for building equivariant networks under multiple symmetry groups. The theoretical construction is sound and practically valuable, but the manuscript would benefit from clearer explanations of indexing, permutation handling, and the role of the $q_{t,\sigma,J}$ functions.

### Strengths
* Provides a unified theoretical construction of equivariant tensor functions across orthogonal, Lorentz, and symplectic groups.  
* Avoids Clebsch–Gordan contractions by using invariant scalar functions and tensor assembly, leading to simpler implementations.  
* The mathematical framework (Theorem 1, Corollaries 1–3) is general and connects to isotropic tensor theory.  
* Demonstrates practical versatility across physics, geometry, and learning tasks.  
* Empirical results show strong improvements over non-equivariant baselines.

### Weaknesses
1. **Notation clarity:** The paper should explicitly distinguish permutation indices (e.g., $i,j,k,l$) from “rotational” or group indices (e.g., $a,b,c,d$). Figure 1 blurs this distinction, making it hard to track which quantities are equivariant to which symmetries.  

2. **Parameterization of $q_{t,\sigma,J}$:**  
   It would be helpful to more clearly explain how the MLPs are used in practice on the collection of inner product of input vectors. I understand that each $q_{t,\sigma,J}$ outputs a scalar coefficient that modulates a tensor built from outer products and isotropic components, but I'm not sure how the MLP handles the permutation indices on the inner product "tensor". 

3. **Permutation handling:**  
   Related to above, my understanding is that the $q_{t,\sigma,J}$ are not permutation-equivariant functions; they are invariant with respect to the rotational/Lorentz/symplectic group but labeled by specific index tuples $(t,\sigma,J)$.  
   In theory, Corollary 1 sums over all permutations $\sigma \in S_{k'}$, but in practice the implementation collapses equivalent $\sigma$ into isotropy classes (Appendix D), so only a small subset of unique tensor structures is instantiated. It would be good to clarify what is a helpful an analytical indexing device vs. how things are practically implemented.

4. **Isotropic tensors:**  
   Clarify whether isotropy is defined only with respect to the group action or also includes permutation symmetries (e.g., $a_{ij}=a_{ji}$).  
   For rank-4 tensors relevant to the neo-Hookean example, an explicit enumeration of independent isotropic components under partial or full permutation symmetry would help readers connect this to classical elasticity theory.  

5. **Related work:**  
   It would be good to discuss Cartesian-tensor–based equivariant methods that similarly use inner/outer product constructions to add to the context of your methods:
  * https://www.nature.com/articles/s41467-024-51886-6
  * https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9711441 (which while for a only the rank 1 case, does generalize to higher dimensions)
  * perhaps https://dl.acm.org/doi/10.5555/3666122.3667745

6. **Comparison to irrep-based models:**  
   A short discussion on expressivity, i.e., whether the span of inner/outer-product constructions matches the space of irreducible-tensor interactions for O(3), would contextualize how complete the representation is relative to Clebsch–Gordan–based methods.  

7. **Minor:** Corollary 1 refers to Figure 3, but this appears to correspond to Figure 1.

### Questions
1. How are the $q_{t,\sigma,J}$ implemented in code, e.g. shared across $\sigma$ or instantiated per isotropy class?  
2. Does Eq. (11) enforce any permutation equivariance among input vectors, or is equivariance only with respect to the underlying group?  
3. For the neo-Hookean example, what precise symmetry assumptions on the rank-4 tensor (e.g., $ijkl=klij$) are encoded?  
4. How does the proposed construction’s expressive span compare to that of CG-based O(3) models?

### Soundness
4

### Presentation
3

### Contribution
4

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper studies the representation of equivariant mappings between tensors to tensors under various symmetry groups. In particular, they characterize equivariant polynomials for general rank input and output tensors under $O(d)$, $O(s, d-s)$ and $Sp(d)$ symmetries. In the case of vectors and symmetric matrices (ie, rank 1 and rank 2 tensors) under $O(d)$ symmetry, their general characterizations specialize to those known in the literature (eg. Villar, et al. 2021). They derive an extension of their results to algebraic groups. Finally, they report empirical results using their characterization compared to existing models on predicting stress-strain relationships, path signature prediction and sparse vector estimation.

### Strengths
I am a big fan of this work. The paper is very well-written, and generalizes several existing results. While the most general constructions are not practically implementable, the authors derive specializations in specific practical settings which are practical to implement.
I think the field will benefit from having these general characterizations in one place.

### Weaknesses
The empirical comparisons could be strengthened (see comments below).

### Questions
* Do you think there is a way to additionally incorporate permutation equivariance (eg. when dealing with sets of vectors, not sequences) into your characterizations?
* Do you have thoughts on parametrizing $SO(d)$-equivariant polynomials, such as those considered in Villar, et al. 2021 for vectors (where now cross-products come into play)?
* Do you have thoughts on how one can predict $O(d)$-isotropic rank-$k$ tensors?
* Can you add an experiment with existing E3NN baselines such as NequIP for the $O(d)$ equivariance experiments? For example, you could take a look at the e3tools repository: https://github.com/prescient-design/e3tools/blob/main/examples/models/conv.py for an existing PyTorch implementation. My understanding is that those models are performing pairwise tensor products but are explicitly permutation equivariant as well.
* Do you perform data augmentation for your MLP baseline, to approximately obtain G-equivariance? If not, can you add those results?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper provides a general mathematical characterization and construction of tensor-to-tensor functions equivariant to orthogonal, Lorentz, and symplectic groups. It gives explicit parameterizations, extends invariant-theory results, and demonstrates the approach in three domains (materials science, path signatures, sparse vector estimation), with consistent improvements over non-equivariant baselines.

### Strengths
**Originality**

Extending equivariance theory to Lorentz and symplectic groups in a unified tensor framework is new and meaningful.

**Quality**

The theoretical development seems mathematically rigorous, consistent, and well-supported by references in invariant theory.

Empirical results, though synthetic or semi-synthetic, convincingly show the advantage of symmetry-aware architectures across different domains.

**Clarity**

Despite mathematical density, definitions and proofs are clearly stated, and appendices support reproducibility.

**Significance**

The proposed general framework could influence how equivariance is implemented for high-order tensor data—a major area of emerging interest in scientific ML.

Potentially impacts ML applications in materials modeling, physics simulation, and tensor decomposition problems.

Provides a foundation for future architectures extending GNN and geometric deep learning paradigms to more general symmetry groups.

### Weaknesses
All data are synthetic or toy (the stress–strain task uses the Garanger et al. (2024) dataset, which if I understood correctly is still a simulated material data), no large-scale, real-world or high-dimensional experiments.

No complexity or scalability discussion, crucial for practical adoption.

Comparative evaluation is narrow. Competes mostly with MLPs and one prior symmetry-enforcing method, no comparison to modern equivariant neural architectures (E3NN, LieConv, TFN). Without these, it’s hard to judge whether improvements are due to the new theory or simply to enforcing symmetry at all.

### Questions
How does the proposed method scale computationally compared to established equivariant architectures (e.g., E3NN)?

Can you demonstrate results on a real dataset involving Lorentz or symplectic symmetry (e.g., physical simulation or robotics)?

Is there a formal or empirical ablation isolating the gain from the new isotropic-tensor formulation vs. standard equivariant parameterizations?

How large are the MLPs used for $q_{t,σ,J}$ (remark 1)? Are they a computational bottleneck?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3