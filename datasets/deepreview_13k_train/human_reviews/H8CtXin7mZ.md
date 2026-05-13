# A Neural-preconditioned Poisson Solver for Mixed Dirichlet and Neumann Boundary Conditions

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
We introduce a neural-preconditioned iterative solver for Poisson equations with mixed boundary conditions.
Typical Poisson discretizations yield large, ill-conditioned linear systems.
Iterative solvers can be effective for these problems, but only when equipped with powerful preconditioners.
Unfortunately, effective preconditioners like multigrid \citep{brandt:1977:multi} require costly setup phases that must be re-executed every time domain shapes or boundary conditions change, forming a severe bottleneck for problems with evolving boundaries.
In contrast, we present a neural preconditioner trained to efficiently approximate the inverse of the discrete Laplacian in the presence of such changes.
Our approach generalizes to domain shapes, boundary conditions, and grid sizes outside the training set.
The key to our preconditioner's success is a novel, lightweight neural network architecture featuring spatially varying convolution kernels and supporting fast inference.
We demonstrate that our solver outperforms state-of-the-art methods like algebraic multigrid as well as recently proposed neural preconditioners on challenging test cases arising from incompressible fluid simulations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a new data-driven preconditioner for Poisson problems with mixed boundary conditions with a MAC discretization. The PDE arises from the moving boundary of a multiphase flow, thus traditional AMG is unfavorable in terms of the MG hierarchy rebuilding. The key method is built upon the work in Kaneda et al ICML 2023. The authors also tackles a difficulty through the optimizer that the DNN preconditioning approach is non-symmetric, which achieves better result than approaches such as `BLOPEX` in hypre. From the perspective of someone who worked in the business of traditional multigrid solvers/preconditioners for PDEs, the PDE discretization is nothing new, the methodology used is pretty predictable, and there are a few unclear things, however, I still think this is overall a solid work.

### Strengths
- In the context of traditional approaches of multigrid, either solver or preconditioner, either geometric or algebraic, imposing (nonhomogeneous) Neumann BC can be challenging and is usually an ad-hoc business.
- The study, from preconditioning pov, is quite well-motivated by introducing the ever-changing BCs for the Poisson problem through the multiphase flow, since traditional AMG has to rebuilt the AMG hierarchy each time step.
- The phase variables as channels are neat practices, which is nicely motivated by the ever-changing phase in simulation. But references should be given (e.g., arXiv:1707.03351).
- The spatially varying kernel (or instance-dependent kernel) is an extremely nice practice, and rightfully so motivated by the mathematical nature of the problem. This is highly connected to attention (even though it is nonlinear) applied to PDE problems (where attention is viewed as a kernel integral), please consider giving a few references in this regard.
- I ran the code myself, and was amazed by the excellent reproducibility of it. However, the instruction of how to install `AMGCL` is problematic in `README.md` for someone with existing header files for `AMGCL`.

### Weaknesses
 - Personally, I am quite uncomfortable to impose Dirichlet boundary conditions on the pressure variable for the fluid problems among many formulations I have played with for NSE or Stokesian flow. While the temporal discretization of NSE presented on page 3 is a standard splitting scheme (aka "projection method" or "pressure-correction scheme"), the reference given is likely not the right one. In Chorin's 1967 JCP paper, he proposed the famous pressure marching scheme to impose divergence free condition at $(n+1)$-th time step (implied by (4) in the paper), but did not solve a PDE for pressure. I checked Temam's book as well as J. Shen (Temam's student)'s review paper on projection methods, and the scheme featured in this paper is probably attributed to Chorin's 1968 Math. Comp. paper (equation (21) therein for pressure). However, therein, only the Neumann BC is imposed for the pressure. So please give the reference, preferably with equation numbers that where does the Dirichlet part comes from.
- The current presentation of the overall iterative procedure is unclear in section 4. For example, in Figure 1, only $\mathbf{r}\mapsto \mathcal{P}^{\text{net}}(\mathcal{I}, \mathbf{r})$ is shown. I suggest move A.1 to the main part.
- The biggest weakness is perhaps that the "CNN" used is linear, then it is nothing but a single parametrized convolution, as stacking convolutions without nonlinearity is still a convolution just with a different kernel sizes.
- Maybe this is up to debate, that the authors said "AMG setting up stage takes too long". I think this is an unfair comparison, on a fixed mesh, AMG hierarchy has to be set up only once, and for GMG it is automatic. Moreover, AMG setting up is automated on any mesh and (mostly) robust for specific PDEs that needs no training stage. Another counterpoint would be that the current approach (based on CNN) is limited to Cartesian mesh-based discretization such as MAC.



### Questions
- The targeted audience who works in the solver business would usually not know what "PIC/FLIP blend transfer scheme" is, I suggest elaborate it somewhere in the context of this paper, especially considering a similar acronym IC stands for incomplete Cholesky.
- Judging by the name of Harlow 1964 Meth. Comp. Phys. paper, it is the ref for PIC? The correct origin of MAC should be Harlow and Welch's 1965 paper in The Physics of Fluids, some people like to cite this tech report as well (https://www.osti.gov/biblio/4563173).
- Page 4: "The PSDO algorithm can be understood as a modification of standard CG that replaces the residual with the preconditioned residual as the starting point for generating search directions and, consequently, cannot enjoy many of the simplifications baked into the traditional algorithm". This sentence is somewhat too long in reviewer's humble opinion, and up to the authors' judgement, I suggest rewrite it a little. Meanwhile, please consider spending a few words to explain the reason why PSDO cannot achieve CG's automatic $A$-conjugate directions. It says that PSDO does "an exact line search", so it does not a subspace search like the CG does?
- Page 5-6, the default behavior of upsampling using the interpolation in `nn.functional` is `nearest` which gives a piecewise constant function that is unfavorable in this context, please test `bilinear` which is MG prolongation.
- The single-precision for NN and double for the CG is a good practice. However, it would be interesting to see whether this combination can reach relative residual `1e-8` (cf. those in Figure 5).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach to construct preconditioner for Poisson equations based on neural networks. The architecture is to mimic the geometric multigrid. The approach has the capability to handle arbitrary shape of the fluid and mixed boundary conditions embeded in a rectangle or cube.

### Strengths
The neural network can effectively approximate the inverse of the stiffness matrix from the Poisson equation such that the resulting iterative solver is much faster than the existing methods.

### Weaknesses
- The primary contributions of the paper, including the understanding of convolution as a smoother, pooling as the restriction, and the connection between multigrid and convolutional neural networks, have been extensively explored in the following reference:

  Juncai He and Jinchao Xu. "Mg-Net: A unified framework of multigrid and convolutional neural network." arXiv:1901.10415, 2019.

- It appears that the comparison in the paper is limited to iterative solvers and does not account for the time required to train the preconditioner. This approach may not provide a fair assessment. It's worth noting that the setup time for AMG can be comparable to the training time. If one considers the extended matrix on the uniform grid, a fixed hierarchy can be used, and the learning task could focus on the prolongation and restriction operators for different $\mathcal I$. The approach outlined in the following paper may offer valuable insights:

  Alexandr Katrutsa, Talgat Daulbaev, Ivan Oseledets. "Deep Multigrid: learning prolongation and restriction matrices." [arXiv:1711.03825](https://arxiv.org/abs/1711.03825).

- The data generation process described on the bottom of page 6 needs further clarification. It's not entirely clear whether it involves variations in the domain geometry. If it does, it would be helpful to specify the nature of the randomness associated with the geometry. Additionally, the presentation seems to only consider two types of discretization sizes. If that's the case, it's important to explain how this approach can be applied to systems with different discretization sizes. Does the neural network need to be retrained for each new size? Furthermore, more details about the randomness involved in generating the right-hand side of the equations would be appreciated.
- The paper does not adequately address the potential of a standard geometric multigrid (GMG) approach on an extended domain. By embedding the irregular domain within a rectangular one, a fixed GMG hierarchy could be employed. The spatially varying kernels used in the proposed method closely resemble the smoothers used in multigrid methods, which can be determined by the modified stencil. The paper fails to explore the performance of such a baseline, which could potentially achieve similar results without the need for training a neural network. This is a significant omission, especially given the computational cost associated with training the neural network.
- The paper lacks a clear explanation of what the neural network truly learns to maximize iterative solver performance. It remains unclear whether the network is primarily learning the smoother, the prolongation operator, or both. This ambiguity makes it difficult to understand the role of the neural network in enhancing solver performance and limits the generalizability of the approach. It is essential to have a more precise understanding of the learned parameters and their impact on the iterative process.
- Is it necessary to fix the levels of coarsening in the proposed approach?

### Questions
- The data generation process described on the bottom of page 6 needs further clarification. It's not entirely clear whether it involves variations in the domain geometry. If it does, it would be helpful to specify the nature of the randomness associated with the geometry. Additionally, the presentation seems to only consider two types of discretization sizes. If that's the case, it's important to explain how this approach can be applied to systems with different discretization sizes. Does the neural network need to be retrained for each new size? Furthermore, more details about the randomness involved in generating the right-hand side of the equations would be appreciated.
- Could the authors provide an explanation of what the neural network truly learns for an iterative solver to maximize its performance? Specifically, does it focus on learning the smoother or the prolongation operator, or both? Clarity on this aspect would be valuable for understanding the role of the neural network in enhancing solver performance.
- Is it necessary to fix the levels of coarsening in the proposed approach?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a neural network architecture inspired by multigrid to learn an approximate inverse of the discrete Laplace operator, which serves as a preconditioner for an iterative PDE solver. The key contributions are: 1) Handling mixed Dirichlet and Neumann BCs, which prior works cannot; 2) A novel network structure that incorporates boundary information through spatially-varying convolutions; 3) State-of-the-art performance vs AMG, IC and other baselines on fluid simulation examples.

### Strengths
1. The network design that encodes boundary information through spatially-varying convolutions is novel and well-motivated. This likely contributes significantly to the method's success in addressing mixed BCs.

2. Comprehensive empirical evaluation on simulation benchmarks demonstrates clear superiority over optimized baseline methods on problems. Statistical analysis provides convincing evidence of the method's benefits.

### Weaknesses
1. While the spatially-varying convolutions encode boundary data effectively, their implementation as CUDA kernels is noted to be a computational bottleneck. Further optimization could yield additional speedups. Specifically, the overhead of computing the spatially varying kernel weights and applying them likely dominates the computation, particularly for smaller problem sizes. A more detailed breakdown of the computational cost, including the time spent on weight calculation versus convolution, would be valuable.

2. Enforcing symmetry and positive-definiteness of the preconditioning operator was not achieved, limiting the method to a generalization of CG instead of CG itself. This is a significant limitation as it prevents the use of standard CG convergence guarantees. The lack of positive definiteness also raises questions about the stability of the preconditioner, especially for ill-conditioned problems.

3. The network does not yet leverage sparsity, so may not scale gracefully to extreme sparse problems with many empty grid cells. This is a critical concern for real-world applications where computational domains are often highly sparse. The method's performance on problems with varying degrees of sparsity should be investigated, and the potential for incorporating sparse convolution techniques should be explored.

4. Only isotropic problems were considered - extending the approach to anisotropic or nonlinear problems is an open question. The assumption of isotropy is a significant limitation, as many physical systems exhibit anisotropic behavior. The method's applicability to problems with heterogeneous material properties or non-linear PDEs is unclear.

5. Training data generation from Lanczos vectors is costly. Finding cheaper alternatives while maintaining accuracy could be valuable for certain applications. The computational cost of generating the Ritz vectors using Lanczos iterations is a significant overhead. The authors should explore alternative methods for generating training data or consider using a smaller number of Lanczos vectors, while still maintaining the quality of the preconditioner.

6. Proving theoretical convergence properties like those of standard multigrid would strengthen understanding, though difficult given the learned nature. The lack of theoretical guarantees makes it difficult to assess the robustness and reliability of the method. Establishing convergence bounds or analyzing the spectral properties of the learned preconditioner would be valuable.

7. Quantitative ablation of design choices like coarsening levels, memory usage, etc. could provide further insights. A thorough ablation study is needed to understand the impact of various hyperparameters on the method's performance. This should include the number of coarsening levels, the size of the convolution kernels, and the memory usage of the network.

8. While extensive, the benchmark set considers a subset of potential problem domains - generalizing to new classes would reinforce claims. The current benchmark set is limited to fluid simulation problems. Evaluating the method on other types of PDEs, such as heat transfer or structural mechanics, would provide a more comprehensive assessment of its generalization capabilities.

### Questions
1. Can you exploit sparsity directly in the network/algorithm to better handle extremely sparse problems that arise in practice

2. Can you investigate enforcing symmetry and positive-definiteness of the preconditioner to allow use of standard CG?

3. Can you explore non-Euclidean/anisotropic problem settings to broaden the method's scope?

4. Can you develop cheaper training data generation techniques or consider self-supervised learning alternatives?

5. Can you perform sensitivity studies on architectural hyper-parameters like coarsening levels, memory usage, etc?

6. Can you attempt theoretical analysis of convergence properties to strengthen understanding of the method?

7. Can you broaden empirical evaluation to new problem classes to further validate generalization abilities?

I would like to improve my score if the concerns above are well addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript uses a neural network to construct a preconditioner for solving Poisson equations on various geometries with varying boundary conditions. The neural network takes 5-7 days to train before it is a reasonable preconditioner across various geometries. It then provides a modest speed-up over some of the existing preconditioning techniques. The biggest gap in the manuscript is that the preconditioner is not symmetric positive definite, and a highly nonstandard iterative method is advocated that will be challenging to develop a general convergence theory. The multigrid preconditioner remains a good choice for fixed geometries, but here, the neural network preconditioner seems beneficial when applied to a range of geometries.

### Strengths
The Deep Conjugate Direction Method (DCDM) is a novel approach that leverages deep learning to approximate the solution of large, sparse, symmetric, positive-definite linear systems of equations. This manuscript is improving on this solver for the setting of Poisson on various geometries. The practical simulations (supplementary) are relatively impressive, demonstrating the effectiveness of their preconditioner. 

After training, the constructed preconditioner for Poisson's equation is surprisingly effective at reducing the number of iterations of the DCDM-variant for various geometries.

### Weaknesses
Without a positive definite preconditioner, it is likely that the simulations in Figure 2 become unstable (or unphysical) if run for long enough. I think the authors should carefully consider both the computational cost per time step and the numerical stability of the time-stepping scheme when using various preconditioners. This direction is mentioned as a future work, but I think the paper's contribution is compromised without ensuring symmetric positive definiteness.

The lack of theoretical convergence analysis of the preconditioner and iterative solver means that the solver is of limited general use. Since the preconditioner is not positive definite, I suspect that the theoretical convergence of the iterative scheme is extremely difficult to understand.  

Training the neural network with a large memory requirement takes a very long time before it can be successfully used in time simulations.

### Questions
Can the method be used to construct a neural network-based positive definite precondition? If so, then it at least takes into consideration that the original problem is symmetric, positive-definite linear systems of equations.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
