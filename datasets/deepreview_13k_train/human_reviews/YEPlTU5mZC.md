# Implicit Gaussian process representation of vector fields over arbitrary latent manifolds

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Gaussian processes (GPs) are popular nonparametric statistical models for learning unknown functions and quantifying the spatiotemporal uncertainty in data. Recent works have extended GPs to model scalar and vector quantities distributed over non-Euclidean domains, including smooth manifolds appearing in numerous fields such as computer vision, dynamical systems, and neuroscience. However, these approaches assume that the manifold underlying the data is known, limiting their practical utility. We introduce RVGP, a generalisation of GPs for learning vector signals over latent Riemannian manifolds. Our method uses positional encoding with eigenfunctions of the connection Laplacian, associated with the tangent bundle, readily derived from common graph-based approximation of data. We demonstrate that RVGP possesses global regularity over the manifold, which allows it to super-resolve and inpaint vector fields while preserving singularities. Furthermore, we use RVGP to reconstruct high-density neural dynamics derived from low-density EEG recordings in healthy individuals and Alzheimer's patients. We show that vector field singularities are important disease markers and that their reconstruction leads to a comparable classification accuracy of disease states to high-density recordings. Thus, our method overcomes a significant practical limitation in experimental and clinical applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Gaussian processes is a popular Bayesian method that easily incorporates prior knowledge and provides good uncertainty quantification. GP is originally defined in Euclidean space which limits its application in certain domains. In this paper, the author proposes the Riemannian manifold vector field GP (RVGP) which extends GP to learn vector signals over latent Riemannian manifolds with the use of connection Laplacian operator. Experiment results show RVGP can encode the manifold and vector field's smoothness as inductive biases and have good performances on electroencephalography recordings in the biological domain.

### Strengths
- Extending GP to vector-valued signals is novel. The proposed method also removes the common assumption that the manifold is known in non-Eucleadian GP, which expands GP's applicability.
- The paper is well written.

### Weaknesses
 - One advantage of GP is data efficiency. In section 5.1's superresolution experiment RVGP is trained using vectors over 50% of the nodes, I would be interested to see the results when trained with less data. Specifically, it would be valuable to understand how the performance degrades as the percentage of observed nodes decreases, perhaps down to 10% or 20%, to better assess the method's data efficiency in sparse data scenarios.
- In section 5.2 the authors compare RVGP with interpolation methods, which might be a too simple baseline comparison. The RVGP's performance is also close to linear prediction. It is concerning that the performance of RVGP is so close to linear prediction, which suggests that the method may not be fully exploiting the complex structure of the data. A comparison against a more sophisticated method, such as a kernel method or a neural network-based approach, would provide a more rigorous evaluation of the proposed method's capabilities.
- A section discussing the limitations of the proposed method would be good. This section should include a discussion of the computational cost of the method, the sensitivity to hyperparameter settings, and any assumptions about the data that may limit its applicability. For example, how does the method perform when the underlying manifold is highly non-linear or when the vector field is not smooth?

### Questions
See weakness above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper looks at performing Gaussian Process regression over vector fields on unknown manifolds.

The underlying manifold and tangent space is estimated by combining a proximity graph approach to modelling the underlying manifold, and approximating the tangents space by taking the highest singular values of the matrix of directions to neighbours.

The discretised connection Laplacian on these tangent spaces is then used to construct a kernel by projecting the spectral decomposition of the connection laplacian onto the estimated tangent spaces.

This kernel is then used in a number of experiments, from some simple inpainting and super-resolution tasks to superresolution of real EEG data, and show improved diagnostic capabilities using this method.

### Strengths
- The method is clean and simple
- The method demonstrably works in the single task presented
- Most of the paper is easy to follow

### Weaknesses
 - I found the section "Vector-field GP on arbitrary latent manifolds" difficult to follow. For example it is not clear to me what $(U_c)_i$ is. To me this would denote the $i'th$ row, but it clearly is not as it is the wrong shape. Also in equation 15, $\Phi(\Lambda_C)^{-2}$ is a $\mathbb{R}^{mn \times mn}$ matrix, but is being producted with $P_v$, a $\mathbb{R}^{d\times k}$ matrix?

 - I am still unsure about the precise construction of the kernel. While the authors describe it as analogous to the scalar case, the details of how the connection Laplacian's spectral decomposition is projected onto the estimated tangent spaces remains unclear. Specifically, how are the eigenvectors of the connection Laplacian, which are vector fields, actually used to construct the kernel?  It seems like there is an implicit operation being performed that is not fully explained.

 - It is not clear how the method handles the case where the estimated tangent spaces are not perfectly aligned with the true tangent spaces. The method relies on the accuracy of the tangent space estimation, and it would be beneficial to understand the sensitivity of the method to errors in this estimation. For example, what happens if the singular value decomposition does not perfectly capture the true tangent space directions, and how does this impact the resulting kernel and the performance of the Gaussian process?

### Questions
- Can you explain the procedure of constructing the kernel in "Vector-field GP on arbitrary latent manifolds"? 
- How does this kernel differ from using the method of Hutchinson et. al. more directly? I.e. Using the scalar kernel defined by the graph laplacian, $k(i,j)$, from this creating a diagonal kernel $ K(i,j) = k(i,j) * I_{d\times d}$, and then restricting this to the estimated tangent spaces, $\mathbb{K}(i, j) = \mathbb{T}_i K(i,j)  \mathbb{T}_j$
- Presumably one needs to know the dimension of the unknown manifold ahead of time?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a Riemannian manifold vector field Gaussian process (RVGP), a generalization of Gaussian processes (GPs) for learning vector signals over latent Riemannian manifolds. The core of the idea is to use positional encoding derived from the connection Laplacian. The authors demonstrated the effectiveness of the proposed method via super resolution and inpainting for the vector field on a 3D mesh and EEG analysis.

### Strengths
- The theoretical part is mostly well written and technically sound.
- Related work is well addressed.
- Practicality is well demonstrated on real data.

### Weaknesses
Lack of precision in some statements.
- V is defined multiply: for vectors and for the nodes of the graph. One of the important statements "While G approximates M it will not restrict the domain to V" becomes unclear.
- The shape of $O_{ij}$ is unclear. It seems to be $m \times m$ for eq. 11, but it seems to be $d \times d$ for eq.12. (The rank of $O_{ij}$ will be m.) The shape of $L_{c}$ is also unclear. It is clearly defined as $nd \times nd$ in eq. 12, but it is inconsistent with $\Lambda_{c},U_{c} \in R^{nm\times nm}$. Maybe something is wrong.
- A quantitative evaluation and analysis is missing for 5.1. I could not judge whether "smoothly resolved the singularity by gradually reducing the vector amplitudes to zero" is okay or not. Does this mean that the result is different from the ground truth? A quantitative evaluation is also appreciated.

Detailed comments:
- Something wrong: {($x_i$}), $\hat{v} = \|_{i=0}^{n}\hat{v}_{i}$
- I could not understand what the authors were doing: "We then sampled corresponding vectors {$v_{i}$} from a uniform distribution on the sphere".
- $S^{3}$ should be $S^{2}$

### Questions
1. The reviewer has a question about the statement "vector field on latent Riemannian manifolds". I suppose two interpretations; each of the vector itself should lie on the manifold, or the domain of the field is enclosed on the manifold but the vector can be out of the manifold. In the experimental result (Fig. 2C), the authors point out the "vectors that protrude the mesh surface". For the former, this should be an undesirable result, but for the latter, it is okay. An example of the latter case is the normal vector of the Stanford bunny for Figure 2. It is also possible to consider such a problem, but I'm curious if the proposed method can model it. At least I expect the proposed method to work for $m=n-1$ (2D manifold in 3D space), but I doubt it for $m<n-1$ because the Levy-Civita connection is insufficient to address the complementary subspace of the tangent space.

2. The reviewer has some doubts about the term "unknown manifold". For 5.1, the training data is dense enough to approximate the manifold well. For 5.2, the authors "constructed RVGP kernels using the connection Laplacian eigenvectors derived from a k-nearest neighbour graph (k = 5) fit to mesh vertices". It seems that the Laplacian was computed from 256 vertices, not n=61. If I understand correctly, this violates the prerequisite of "unknown manifold". Is there no value in analyzing the relationship between the coverage of the data for the manifold and the accuracy of the vector field prediction? I'm also curious about the analysis of the predicted vector field for out of the manifold to check for regularity.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
