# Matérn Kernels for Tunable Implicit Surface Reconstruction

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
We propose to use the family of \Matern kernels for \textit{tunable} implicit surface reconstruction, building upon the recent success of kernel methods for 3D reconstruction of oriented point clouds.
As we show, both, from a theoretical and practical perspective, \Matern kernels have some appealing properties which make them particularly well suited for surface reconstruction---outperforming state-of-the-art methods based on the \textit{arc-cosine} kernel while being significantly easier to implement, faster to compute, and scaleable.
Being stationary, we demonstrate that the \Matern kernels' spectrum can be tuned in the same fashion as Fourier feature mappings help coordinate-based MLPs to overcome spectral bias. 
Moreover, we theoretically analyze \Matern kernel's connection to \textsc{Siren} networks as well as its relation to previously employed arc-cosine kernels. 
Finally, based on recently introduced Neural Kernel Fields, we present \textit{data-dependent} \Matern kernels and conclude that especially the Laplace kernel (being part of the \Matern family) is extremely competitive, performing almost on par with state-of-the-art methods in the noise-free case while having a more than five times shorter training time.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper enumerates the use of a class of kernels that can be constructed with two interpretable parameters: bandwidth and smoothness. Specific choices of these parameters lead to well-known kernels like Laplace and Gaussian kernels. 
This paper elaborates both on theory and experimental evaluation. Specifically, one can derive certain expressions for bounds on the eigenvalue decay rate (EDR), and reconstruction error. More interestingly the authors also draw a connection to neural networks and show  that Matern kernels mimic the computation of two-layer SIRENs if the layer width approaches infinity. 

On the practical side, a range of experiments is provided on surface reconstruction on ShapeNet and SRB (SHape Reconstruction Benchmark). The experiments show favorable metrics for certain fixed and learnable Matern Kernel choices. The comparison is drawn to prior methods like NKF, SPSR, and Neural Splines on challenging metrics like performance with noise, and convergence speed.

### Strengths
- Overall I found the paper compiled quite well and tells an story of how Matern Kernels can be interesting theoretically and practically useful. The exposition focussing on this class of kernels is quite comprehensive.
- I particularly liked the connection to SIRENS
- I found the experiments to be well made. Reconstructions and evaluations are indeed favorable in comparison to their competing methods

### Weaknesses
 - Despite a well-made submission, I found it hard to appreciate a strong take-home message. A lot of the material on Matern Kernels appears to be well-known from statistics and I don't find it surprising that they can be tuned well in practice by modulating the bandwidth and smoothness parameters. In this sense, I am a bit disappointed about a direct novel result (other than the relation connecting to SIRENS)
- I did not fully understand and appreciate the excessive focus on bettering the arc-cosine kernel

### Questions
figure on page 6 needs labels and a quick caption

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper promotes the use of the Matérn kernel family for implicit surface reconstruction, emphasizing the kernel’s adaptability through two parameters that control its tendency to fit high-frequency details. These claims are substantiated through both theoretical analysis and empirical evidence. The approach is validated on standard surface reconstruction benchmarks.

### Strengths
The paper is well-organized and clearly written, with a sufficient amount of background material to make it self-contained.

The incorporation of Matérn kernels appears to be a valuable contribution, supported by theoretical analysis on their ability to capture high-frequency details effectively.

Both quantitative and qualitative comparisons are provided, highlighting key properties of the proposed method.

### Weaknesses
Unclear Benefits of Matérn Kernel Properties

Section 3.1 describes Matérn kernel properties, yet it’s unclear how differentiability and stationarity specifically benefit surface reconstruction. More specifically,
  Differentiability: Should the differentiability of the kernel be related to the (unknown) ground truth function of the surface reconstruction? what are some typical cases/assumptions, for which the kernel differentiability class is appropriate? For instance, if the ground truth surface has sharp edges or corners, a kernel with limited differentiability might be more suitable, but this is not discussed. It is also unclear how the choice of differentiability impacts the reconstruction quality in the presence of noise.
Stationarity: How does stationarity improve reconstruction in this context? While translation invariance is mentioned, the practical benefits beyond simply centering the input data are not clear. Some empirical evidence would help clarify its usefulness. Additionally, given the local support property, wouldn’t we expect symmetric parts, such as the chair legs in Figure 6, to yield consistent reconstruction results? The lack of symmetry in the reconstruction suggests that the local support is not the only factor at play, and this needs further explanation.

The Role of Local Support

Since the product of two kernels remains a kernel, could any kernel be multiplied by a locally supported kernel to achieve local support? Why is this a specific property of the Matern kernel? NKSR, for example, multiplies the dot product kernel by a locally supported kernel. Additionally, would using a kernel with a tunable support radius (like NKSR) allow for similar control over high-frequency detail? If so, the added value of using a two-parameter Matérn kernel remains unclear. The paper does not explore the relationship between the Matérn kernel's parameters and the effective support radius, making it difficult to assess its advantage over other locally supported kernels.

Comparison Quality

Comparison with Arc-Sine Kernels. The chosen baseline is the arc-sine kernel. Why not compare it to the dot-product kernel with local support, as used in NKSR? The arc-sine kernel is not a standard baseline for surface reconstruction, and a comparison with a more relevant method would strengthen the paper. 

Comparison with Gaussian Kernel. In Table 1, the Gaussian kernel $(\nu = \inf)$ is presented as inferior. However, how does a two-parameter kernel like  $\nu \exp(-\tau^2/h)$  perform? What specific benefits does a Matérn kernel offer over this one? Is there an advantage in tuning Matérn kernel parameters over this form? The paper does not provide a clear justification for why the Matérn kernel is superior to a scaled Gaussian kernel with a tunable bandwidth.

Unclear Connection to SIREN

Theorem 3 seems more like a property of SIREN than the Matérn kernel. It appears that the spectral density of any (stationary) kernel could satisfy the conditions in line 329, so the theorem might hold more generally than just for Matérn kernels. Could the relevance of this theorem to the Matérn kernel specifically be clarified?

### Questions
I would appreciate any response to the questions stated above.

### Soundness
3

### Presentation
4

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
This paper proposes using the family of Matérn kernels for implicit surface reconstruction, targeting the 3D reconstruction of oriented point clouds. Leveraging the recent advances in kernel-based reconstruction, the authors demonstrate that Matérn kernels possess theoretical and practical advantages that make them highly suitable for surface reconstruction tasks. They argue that these kernels surpass state-of-the-art methods based on the arc-cosine kernel, offering improved simplicity, computational efficiency, and scalability.

Key contributions include:
1.Highlighting the Matérn kernels’ stationary properties, which allow tunable spectral properties similar to Fourier feature mappings, addressing spectral bias issues in coordinate-based MLPs.
2.Providing theoretical insights into the Matérn kernel’s relationship with SIREN networks and its distinctions from arc-cosine kernels previously used in surface reconstruction.
3.Introducing data-dependent Matérn kernels based on Neural Kernel Fields and showing that the Laplace kernel (a member of the Matérn family) performs competitively with state-of-the-art methods in noise-free settings while significantly reducing training time.

### Strengths
(1) The paper presents a tunable implicit surface reconstruction method based on Matérn kernels. The tunability of the method allows users to adjust parameters based on specific application needs, optimizing reconstruction performance in different scenarios, which is crucial in practical applications.
(2) Matérn kernels are widely used in statistics and machine learning, and the paper effectively leverages their favorite mathematical properties, making the proposed method more rigorous and interpretable theoretically.
(3) The paper is well-structured and logically coherent, making it easier for readers to understand the methods and results. The theoretical proofs and experiments in this paper are relatively sufficient.

### Weaknesses
 (1) Lacks comparison with the latest implicit surface reconstruction algorithms.
(2) Some figures are missing ground truth.

### Questions
(1) SIREN is a work from 2020, and there have been many recent improvements based on SIREN. The authors should consider these in their comparative experiments to showcase the advantages of Matern kernels in implicit reconstruction.
(2) In the sparse surface reconstruction, in addition to quantitative results, including visualizations of the sampled points would make the effects more intuitive.

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
4

### Summary
This work proposes to use Matern kernels -- a unified family of kernel functions -- for 3D reconstruction of shapes from sparsly sampled points. A key property of these kernels is tunability, in that the sharpness of these kernels can be controlled. The authors claim this can help to overcome the known implicit bias in MLPs against the reconstruction of high-frequency features. The contributions of this paper are mostly techincal. The authors provide a theoretical investigation of Matern Kernels, including several toy experiments in support of derivations.

### Strengths
Overall, the authors investigation into the suitability of Matern kernels for surface reconstruction in section 4 is the standout. 

While the experimental details are unclear, the analysis of the eigenvalue decay exposes the mechanics of how the kernels can address spectral bias and supports the authors claims.

The discussion of the reconstruction error is compelling, and the highlight of the paper. The authors cleverly derive an upper bound on the reconstruction error in terms of the kernel parameters (h, $\nu$), and expose a canonical threshold (Equation 13).

To the best of my knowledge, the mathematical formulations are sound, though I did not check them closely.

### Weaknesses
1). Despite the contribution of the paper being technical, the way the math is introduced and discussed is unintuitive and confusing. Section 3 contains significant mathematical "filler" e.g. equations (5-8) could be moved to the appendix.  The RKHS norm is introduced early without context. Only a page later, in Equation (12), does its purpose become clear in supplying the upper bound for the reconstruction loss. Even then, it is not clear that it is necessary to reproduce the explicit form of the RHKS norm in the main text (this can be moved to the supplement).  I question the necessity of section 3, as none of the math introduced is the authors' own work and makes it less clear what their contributions are. I think most of it can be removed, and combined with section 4, with the appropriate math introduced in the main text only as it relates to Eqs. 12-13 and the rest left to the supplement. 

Additionally, I'm on the fence about whether 4.2 should be kept in the main paper or moved to the supplement. These insights are nice to know, but don't necessarily have any effect on the implementation, unlike the discussion in 4.1.

The extra space gained by condensing the above should give the authors more room to both A). make clear exactly what their own contributions are (e.g. the derivations of the upper bound, etc.) and B). provide more room for experiments and discussion.

2). The biggest weakness of the paper are the experimental results. Overall, the authors proposed approach performs only comparably relative to competing methods and does not distinguish itself. This is unfortunate, because the insights in section 4.1 are very nice and had me rooting for the method, but they don't seem to provide a significant increase in performance over existing methods. Overall, the proposed method is not substantially different from prior methods like NKF & NKSR in that it is using just a different choice kernel for surface reconstruction. In general, this is OK, and the authors provide a very nice theoretical investigation into the kernel properties, but in such a case its necessary to show unambiguous, generally uniform improvements over previous similar methods to justify the approach. 

Another important question left unanswered is scalability. Experiments are shown in which simple surfaces are reconstructed from 1000 points. How does the kernel reconstruction perform from sparse samples of 10K or 100K points? I am concerned that the Cholesky factorization is not scalable in these cases, though this does not seem fundamental to the method and the CG could be used. It should be noted that JAX has a very scalable, efficient, and differentiable implementation of the CG solve for sparse systems, and this may be of interest to the authors.

In a similar vein, no results are shown comparing performance with sampling irregularity. How does the method perform with uniformly distributed samples vs varying degrees of non-uniformly sampled points?

Together, scalability and robustness under sampling irregularity are two potential axes for comparison against other methods that could allow the proposed method to more obviously stand out. Additionally, what about reconstructing a complex texture on a surface (e.g. from an Objaverse mesh)? A complex texture is itself a high-frequency signal that could help to distinguish the authors approach.

### Questions
In the eigenvalue decay experiments, the authors should state explicity they are considering the eigenvalues of the kernel K(x, y). Assuming I understand this correctly, how many points are used and how are they distributed in this experiment? What shapes (if any) do they represent? 

Can h* in equation 13 be computed or estimated from the sampled points so as to give an exact way to recover the optimal h value given $\nu$?

### Soundness
3

### Presentation
2

### Contribution
2
