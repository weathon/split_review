# Injecting Inductive Bias to 3D Gaussian Splatting for Geometrically Accurate Radiance Fields

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
3D Gaussian Splatting (3DGS) has significantly advanced high-fidelity, real-time novel view synthesis. However, its discrete nature limits the accurate reconstruction of geometry. To address this issue, recent methods have introduced rendering and regularization of depth and normal maps from 3D Gaussians, leading to plausible results. In this paper, we argue that computing normals from independently trainable Gaussian covariances contradicts the strict definition of normals, which should instead be derived from the distribution of neighboring densities. To address this, we introduce an inductive bias into 3DGS by explicitly parameterizing covariances of Gaussians using principal axes and variances of distribution computed from neighboring Gaussians. These axes and variances are then regularized to ensure local surface smoothness. Our approach achieves competitive performance on multiple datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a method called IBGS that "injects Inductive Bias to 3D Gaussian Splatting". The key idea is computing normals from the distribution of neighboring densities instead of from independently trainable Gaussian covariances. This paper also proposes geometry regularization methods to help form smooth local surface. Experiences on multiple datasets show that the proposed method achieves state of the art in surface reconstruction tasks among 3DGS-based methods while maintaining faster training time compared to implicit neural representation-based methods.

### Strengths
1. The key idea is well-motivated and novel. 3DGS-based methods have been a promising direction for faster surface reconstruction algorithms. A few papers have been trying to improve the normal calculation from 3D Gaussians. This paper brings a new perspective and proposes a novel normal calculation approach, aiming to predict more coherent surface. The new calculation also comes with novel regularization techniques for the normals.

2. Quantitative and qualitative results on multiple datasets demonstrate the effectiveness of the proposed method -- it achieves new state of the art in surface reconstruction among 3DGS-based methods while maintaining faster training time compared to implicit neural representation-based methods.

3. The paper is overall well-written and easy to follow. Implementation details sufficiently discussed.

### Weaknesses
1. The rationale behind calculating normals form neighboring Gaussians is well explained. Some of the regularization / splitting techniques used in this paper look very similar to the techniques applied in methods that optimize individual Gaussians. Could the authors help explain the difference and share some ablation studies (e.g., if they happen to have done these comparisons) for readers to better understand the effects of these techniques?

(1) This paper minimizes the smallest Eigen value lambda_3 (Sec. 3.3. 1, Eq. 8), this looks similar to (Sec. 3.2.1, Eq. 7) of NeuSG [1] that minimizes the smallest component of each Gaussian's three scaling factors. It's unclear how minimizing the smallest eigenvalue of the covariance matrix derived from neighboring Gaussians differs fundamentally from minimizing the smallest scale of individual Gaussians, as both seem to encourage flattening. The paper would benefit from a more detailed explanation of this distinction, perhaps with a visualization of how the two approaches affect Gaussian shapes and distributions.

(2) The sparsity-aware adaptive density control of this paper (Sec. 3.4) seems very similar to VCR-GauS [2] Sec. 3.4 that tries to split large Gaussians in the textureless areas by placing new Gaussians that evenly divide the maximum scale of the old Gaussian. While the paper mentions sampling new Gaussians between neighbors, the core idea of splitting based on size in textureless regions is shared with VCR-GauS. A more thorough discussion of the differences in implementation and the impact of these differences on the final surface reconstruction is needed. For instance, how does the method determine 'textureless' regions, and how does this differ from the approach in VCR-GauS?


### Questions
The improved surface quality is well illustrated in the results. I was wondering if there are some remaining failure cases / limitations of the proposed approach. For example, the training speed seems a bit slower than other 3DGS-based methods, is it caused by the overhead of computing properties among K nearest neighbors?

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
The paper proposes to improve the geometry quality of GS reconstruction by incorperating an inductive bias in GS covariance parameterization. The author claim that the proposed method reaches the state-of-art.

### Strengths
1) The presentation and writing is clear and easy to understand.
2) The proposed method regard every splat is not independent in cov computing process, which is intuitively reasonable. 
3) The sparsity-aware density control strategy is interesting and useful.
4) The geometries of the demonstrated samples are impressive.

### Weaknesses
1) As shown in Table 1, although the proposed method maintains the faster training speed compared with the implicit reconstruction method, it takes longer time to train compared all listed explicit methods. However, the fast training  is one of the main advantages of GS. The proposed method need over 6 times of training time compared with the original GS.
2) The proposed method uses adjacent Gaussians for covariance parameterization. In different scenes with different scales, how to select K neighbours as "adjacent Gaussians"  is a question.
3) No failure cases are discussed.

### Questions
1) Have you investigated that which part of the proposed GS variant cost too much time in training? 
2) Any ablations on the K neighbours of Gaussian for cov parameterization?
3) Any failure cases?
4) Since the GS pointclouds are sparse, with shape of "Splat". The surface reconstruction quality may lies in any part of the whole chain of reconstruction. For example, how do you integrate depth to TSDF volume? Do the listed methods for comparison use same method for mesh extraction?

### Soundness
3

### Presentation
3

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
This paper focuses on constructing high-quality geometric surfaces in 3D Gaussian Splatting (3DGS) representation, with depth and normal learning being key aspects. Unlike existing methods that learn normals for each Gaussian individually, this paper proposes deriving normals using the distribution of neighboring Gaussians. Validated across multiple datasets, this approach enables the paper to achieve smoother local surfaces.

### Strengths
● This paper is a comprehensive work that starts by addressing issues arising from existing methods that optimize each Gaussian individually. It proposes a normal expression based on local regions and designs several regularization methods based on this normal computation. 

● The starting point of the paper is indeed one of the key differences between the existing 3DGS framework and traditional surface reconstruction, making it quite insightful. Traditional surface reconstruction places greater emphasis on the distribution of point clouds in the neighborhood, while existing 3DGS frameworks rely more on 2D rendering loss, often overlooking 3D continuity.

● The experimental validation in this paper is thorough, including both quantitative and qualitative comparisons with existing methods on mainstream datasets, as well as ablation studies of the proposed regularization losses.

● The paper’s presentation is very clear and easy to read.

### Weaknesses
● With the use of the proposed covariance design and additional regularization losses, the improvement over the existing optimal solution is not significant; on the DTU dataset, the Chamfer Distance (CD) only improves by 0.02 compared to RaDe-GS, while the training time is 75 minutes longer (more than five times that of RaDe-GS).

● The paper does not sufficiently explore the sensitivity of the kNN parameter 'k'. While the authors mention using k=5, there's no discussion on how this value was chosen or whether it's optimal across different scenes with varying levels of geometric complexity. The impact of 'k' on the quality of the computed normals and, consequently, the final surface reconstruction, is not thoroughly investigated. This is a crucial aspect, as an inappropriate 'k' value could lead to either over-smoothing or under-smoothing of the surface, directly affecting the accuracy of the reconstruction.


### Questions
● If the PCA-based regularization on local regions proposed in the paper is directly introduced into the existing 3DGS framework, can it also achieve similar smoothing effects as described in the paper?

● As far as I know, in traditional point cloud-to-surface reconstruction, the size of the local region has a significant impact on the final reconstruction results. Does the value of k in the kNN used in the paper also have a substantial influence? Should it be individually adjusted for scenes with varying levels of surface complexity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to overcome the limitations of 3DGS in geometry reconstruction, with a focus on regularization techniques. Previous methods independently define each Gaussian novel vector and only used screen space regularization. However, the paper argues that the normal vector of a Gaussian should depend on its local neighbors. To incorporate structural priors (also referred to as inductive bias in the paper), the paper proposes to parameterize the covariance of each primitive based on its neighborhood. Several regularizations based on the parameterized covariance are then integrated. Experiments suggest that this approach achieves state-of-the-art geometry reconstruction results across multiple datasets.

### Strengths
1. The paper is well-written and easy to follow. The results seem reproducible given sufficient details.

2. Using local neighbors to compute the orientation seems original and reasonable for achieving better results. The visualization also consistently suggests that the proposed regularizations alleviate some holes presented in previous methods.

### Weaknesses
1. The significance of the proposed method appears to be limited as it is built upon RaDeGS with additional regularization. However, it only results in a 0.02 gain in the DTU dataset while being five times slower than RaDeGS.

2. I understand that the normal vector should ideally be derived from the density distribution of the superposition of Gaussian functions.  However, However, I believe that the current method doesn't address the core issue. From a geometric view, the normal vector should not depend on the viewing angle. In Section 3.1, the normal is calculated by determining a plane formed by the intersection point and the center of the Gaussian, which is view-dependent. Consequently, the definition of the normal may contradict the argument based on the density distribution and the orientation defined by the covariance obtained through local neighbors.

3. Lastly, constructing local covariance using KNN may pose challenges. Each Gaussian represents a three-dimensional signal, not a zero-dimensional point, so we should consider its anisotropic nature when taking neighbor information into account. For example, a 3D Gaussian with a density that encompasses a point but with its mean located away from that point.

### Questions
1. What is the cause of lower training efficiency? Is it because of the regularization? What is the number of primitives? 

2. How can you address the problem mentioned in the weakness or if the impact is negligible in practice?

### Soundness
3

### Presentation
3

### Contribution
2
