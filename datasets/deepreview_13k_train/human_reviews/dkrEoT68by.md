# Gaussian Splatting Lucas-Kanade

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
Gaussian Splatting and its dynamic extensions are effective for reconstructing 3D scenes from 2D images when there is significant camera movement to facilitate motion parallax and when scene objects remain relatively static. However, in many real-world scenarios, these conditions are not met. As a consequence, data-driven semantic and geometric priors have been favored as regularizers, despite their bias toward training data and their neglect of broader movement dynamics.

Departing from this practice, we propose a novel analytical approach that adapts the classical Lucas-Kanade method to dynamic Gaussian splatting. By leveraging the intrinsic properties of the forward warp field network, we derive an analytical velocity field that, through time integration, facilitates accurate scene flow computation. This enables the precise enforcement of motion constraints on warp fields, thus constraining both 2D motion and 3D positions of the Gaussians. Our method excels in reconstructing highly dynamic scenes with minimal camera movement, as demonstrated through experiments on both synthetic and real-world scenes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This is a paper about the fundamental question of how to derive the velocity of Gaussian means in Gaussian splatting from the finite forward warp transformation. 
It assumes that these transformations are small and that one can live with a first-order Taylor expansion. 

This involves the derivative of the Gaussian parameters after the motion with respect to the Gaussians in the canonical frame and the warp Jacobian.
Then, assuming that scaling and directional reflectivity do not change, one can derive the Jacobian with respect to the mean and the Jacobian with respect to the orientation.

### Strengths
+ Deriving analytical solutions is elegant and makes an approach interpretable. 

+ The analytical derivation enables a sound application of the flow term in the Dynamic Gaussian case. 

+ The paper is a pleasure to read.

+ A direct flow regularization makes a network overfit on viewpoints.

+ The idea of flow supervision in Gaussian splatting increases performance.

### Weaknesses
While it is nice for a paper to be self-contained, everything 
in this paper until eq. (10) is identical to the "Flow supervision for Deformable NeRF" paper. Eq. (12) is the same as Eq. (7) in the latter. Optical flow rendering is same as in GaussianFlow. The reader is wondering, what exactly is the contribution of this paper when the main ingredients are in the Flow Supervision and the GaussianFlow paper. It really hurts to say that because any reader would enjoy such elegant analytical derivations. Please explain in your response.

### Questions
Q1: Given the analytical form of the derivation, it would be interesting to study classic optical flow problems for Gaussian flow: What is the aperture problem in the Gaussian case. What happens when the Gaussian covariance is rank deficient? What scene structures would cause an ambiguous flow? 

Q2: What would happen when the spherical harmonic coefficients would change? 

Q3: What happens with a local deformation like scale change or shear?

Q4: What exactly is the difficulty of including second-order terms?

Q5: How is the method's sensitivity to the choice of canonical frame? DGS methods have been proposed that do not require a choice of canonical frame.

### Soundness
4

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
The paper addressed the problem of Gaussian Splatting estimation in dynamics scene and with small movements of the camera or the objects. The authors propose an analytical solution to the deformable warp field used to regularize the estimation instead of a learnable  field or offset-values as applied in the state of the art approaches. 
The key contribution is to provide a detailed derivation and stable estimation, basically a a Gaussian Splatting warp field regularization by scene flow. The approach is then evaluated on various datasets and show improvements compared to the existing solutions.

### Strengths
The strength of the paper is to propose a direct analytical solution to the problem of the estimation of the warp field. The solution is mathematically transparent and provides superior results compared to a purely data-driven approach. 
It is a fully new solution which is very relevant for dynamic gaussian estimation and related applications. It is strongly inspired by Lucas-Kanade point tracking and has the same level of generality.

### Weaknesses
 - A reference implementation should be provided since the approach is very relevant to the community and may include many small details, which have their importance and not detailed in the paper.
- The method relies on external algorithms to provide depth and optical flow information, which are used to supervise the scene flow regularization. The appendix discusses experiments with different depth and flow estimation methods. However, this introduces an additional source of potential error and highlights the importance of using high-quality depth and flow estimation techniques.
- EMF is not explained when it was mentioned but later in the text.
- One reference is missing
- "Sensivity to noise". What is the behavior under noise? is that possible to further reduce the effect of noise?
- Computational complexity and related aspects are not mentioned at all. What is the advantage of the approach? (compared to pure learning approaches) 
- The paper mentions a motion masking step. How is the threshold defined? Do theses parameters generalize?

### Questions
Three limitations are mentioned in the paper. 
I would like to add:
- "Sensivity to noise". What is the behavior under noise? is that possible to further reduce the effect of noise?
- Computational complexity and related aspects are not mentioned at all. What is the advantage of the approach? (compared to pure learning approaches) 
- The paper mentions a motion masking step. How is the threshold defined? Do theses parameters generalize?

### Soundness
3

### Presentation
2

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
This paper proposes a novel dynamic Gaussian splatting approach based on an analytical velocity field formulation. Similar to Lucas-Kanade, the method linearizes the warp function at specific time intervals and approximates it with a first-order expansion. This approach effectively regularizes scene flow, resulting in improved dynamic reconstruction performance on benchmark datasets.

### Strengths
- The analytical formulation of the vector field is interesting.
- More tractable than fully MLP-based Deformable 3DGS or other 2D prior-based supervision approaches.
- Competitive benchmark performance.
- The paper is clearly written and easy to follow.

### Weaknesses
 - Limited evaluation dataset. Since the method builds on Deformable GS, it would be beneficial to evaluate on the same benchmark datasets, such as DNeRF, HyperNeRF, and NeRF-DS.
- While the method claims tractability as an advantage due to the analytical formulation, reliance on a black-box MLP weakens this claim. The analytical formulation is only used to regularize the output of the MLP, not to replace it. This means the computational cost is still dominated by the MLP, and the method does not offer a significant advantage in terms of tractability.
- The video supplementary does not show particularly impressive results; there is noticeable unnatural blurring in the GSLK_network video

### Questions
- What exactly is the network architecture of the warp field?
- Compared to fully MLP-based Deformable 3DGS, grid-based warp fields such as 4DGS should struggle less with incorrect motion correlations triggered by a single global MLP representation. How much improvement does the proposed method offer for 4DGS-type warp fields?

### Soundness
2

### Presentation
2

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
This paper tackles the challenges posed by dynamics and the lack of motion parallax that Gaussian Splatting methods face in real-world settings. The author proposes an analytical solution that adapts Lucas-Kanade method to dynamic Gaussian splitting. The proposed method leverages the forward warp field and derives an analytical velocity field for accurate scene flow computation. The experiment shows that “GAUSSIAN SPLATTING LUCAS-KANADE” outperforms state-of-the-art methods on both synthetic and real-world scenes, and demonstrates accurate reconstructing capability in complex scenes with minimal camera movement.

### Strengths
The proposed method analytically derives the expression of warp field velocities and provides better tractability compared to directly supervising the flow field as the difference in estimated deformations between consecutive frames. Besides, the method is applicable to forward warp field techniques, and ensures accurate Gaussian trajectories throughout the sequence.
In real-world application, the author demonstrates that the warp field regularization accommodates deformations in complex scenes with minimal camera movement, achieving results.
The paper is well-written, concise, and has excellent formatting of figures and formulas.

### Weaknesses
Despite the authors' efforts to derive an analytical velocity field and incorporate flow and depth supervision to regularize the Gaussian optimization, I have identified several questions that require attention.

1. The author suggests that the velocity field can be derived from the forward warp field by utilizing a modified Lucas-Kanade expression, and computing the fields corresponding to the displacement and rotation of Gaussians. Nevertheless, I argue that this claim is not entirely accurate. A crucial oversight in the authors' derivation is that optical flow or warp fields are inherently tied to both camera pose and Gaussian motion. Yet, the analysis seems to only consider the scenario flow resulting from the motion of the Gaussian alone, as evident in equations[8][11]. The motivation behind the authors' decision is unclear, but it is likely that incorporating camera pose variations into the Jacobian expression would lead to improved outcomes.

2. The authors should provide a more comprehensive explanation of their implementation, as the description of time integration on the velocity field in Section 4.2 remains unclear. Specifically, what is the value of the time step ∆t employed by the authors, and how is it determined? Furthermore, does the method still satisfy the small motions assumption stated in Line 273 when ∆t is large?

3. The proposed algorithm's reliance on computationally intensive operations, such as the (N × d) pseudo-inverse and time integration, raises concerns about its efficiency. To facilitate a more comprehensive assessment of the method's practical viability, it would be beneficial for the authors to provide a detailed analysis of the time complexity for each algorithmic component, as well as the overall memory requirements. This is essential for evaluating the algorithm's real-world applicability.

4. In my opinion as a reader, the paper's formulas are somewhat verbose, as the Autodiff library is leveraged for efficient gradient and Jacobian computations, obviating the need for manual CUDA implementation. Consequently, it may not be essential to include the detailed derivation process in the main body of the paper.

5. Although the paper's experimental design is thorough, it still exhibits some limitations. The experimental setup is somewhat brief and insufficient. I believe that relevant methods, such as [1,2], should be included as baselines to more thoroughly validate the effectiveness of this method. Additionally, I highly recommend that the authors incorporate a comparison with PhotoSLAM to further bolster the experimental setup.

### Questions
1. The author should provide more details about the experimental setup, e.g., time step ∆t  in Eq.12. Please clarify how is it determined? does the method still satisfy the small motions assumption stated in Line 273 when ∆t is large?

2. The authors highlight in Section 6 that their method is sensitive to SfM initialization. Nevertheless, in my experience, 3DGS can still produce high-quality renderings even when initialized with random point clouds. I find it puzzling that the authors emphasize this aspect, and I would appreciate it if they could provide a more in-depth explanation for this claim.

3. It would be beneficial if the authors could furnish a detailed analysis of the time complexity for each component of the algorithm, as well as the memory requirements during the training process. This information is essential for assessing the algorithm's efficiency and scalability.

Currently, I would rate this paper as borderline. However, I am willing to reconsider my evaluation if the authors can provide additional clarifications and engage in a more in-depth discussion to address the concerns I have raised.

### Soundness
3

### Presentation
3

### Contribution
2
