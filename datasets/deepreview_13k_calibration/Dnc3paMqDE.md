# DeepSPF: Spherical SO(3)-Equivariant Patches for Scan-to-CAD Estimation

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
Recently, SO(3)-equivariant methods have been explored for 3D reconstruction via Scan-to-CAD.
Despite significant advancements attributed to the unique characteristics of 3D data, existing SO(3)-equivariant approaches often fall short in seamlessly integrating local and global contextual information in a widely generalizable manner.
Our contributions in this paper are threefold.
First, we introduce Spherical Patch Fields, a representation technique designed for patch-wise, SO(3)-equivariant 3D point clouds, anchored theoretically on the principles of Spherical Gaussians.
Second, we present the Patch Gaussian Layer, designed for the adaptive extraction of local and global contextual information from resizable point cloud patches.
Culminating our contributions, we present Learnable Spherical Patch Fields (DeepSPF) – a versatile and easily integrable backbone suitable for instance-based point networks.
Through rigorous evaluations, we demonstrate significant enhancements in Scan-to-CAD performance for point cloud registration, retrieval, and completion: a significant reduction in the rotation error of existing registration methods, an improvement of up to 17\% in the Top-1 error for retrieval tasks, and a notable reduction of up to 30\% in the Chamfer Distance for completion models, all attributable to the incorporation of DeepSPF.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper suggests a network design aiming at providing SE(3) equivariant features consisting of local and global spatial neighborhoods. The neighborhoods are modeled using spherical Gaussian representations.  The size of the patches is adjustable by learnable elements in the proposed network.
The method is mainly evaluated on 3D scan2cad tasks: registration, retrieval, and completion.

### Strengths
The work tackles the challenging goal of learning the correct spatial receptive field for features.

I appreciate the effort to evaluate the method on three different tasks. In addition qualitative results are also provided.

### Weaknesses
The main weaknesses of the paper are related to its exposition and readability qualities.
In particular, the authors should strive to reduce the level of technical detail in the main text and aim for a clearer presentation of the key concepts. Furthermore, the paper could benefit from the inclusion of more intuitive explanations. 

Some examples:
i)  “ conventional SO(3)-equivariant methods do not sufficiently investigate the correlation between global and local structures”. Is it specifically true for equivariant methods? SO(3) symmetries? 
ii) Figure 1 is unclear. It is unclear how the caption relates to elements in the figure itself.
iii) There is no clear analysis provided (proposition, theorem, etc.) that supports the claim that the proposed network is equivariant. 
iv) Some equations are not clear, e.g. it is not clear what is z in eq. (3).

In summary, it seems the writing quality is such that the paper is not ready yet for publication. The paper lacks a sufficient level of "self-containment," making it challenging to comprehend critical aspects such as:

* What is absent in prior works addressing this problem.

* The proposed formulation of the method.

* How the formulation aligns with the specified requirements.

Here are some examples:

**Introduction Section**

The third paragraph in the introduction attempts to highlight issues with previous works. However, I find that this essential objective is only partially fulfilled. For instance, the statement, "These methods often treat the issues of local and global SO(3)-equivariance separately, leading to an insufficient investigation of SO(3)-equivariance between global and local structures," is not entirely clear. The meaning of "separately" in this context and the specific problem with the previous designs of the pooling layer of SO(3) equivariant features remain ambiguous. How is the question of the definition of a feature receptive field, and/or pooling layers specifically related to SO(3) Equivariant features? Is it different than, let's say, translation equivariant features? 

**Method Section**

Numerous details lack clarity. For example:

In equation (1), $p$ is in $\mathbb{R}^3$. In equation (2), $p\in \mathbb{R}^{N \times 3}$. It is unclear in (2) whether it is a function of $p$ or $\nu$ and how exactly the parameter $\nu$ is calculated.

The formulation of equation (2) is vague. The equation suggests that $E$ is defined as a maximum over a discrete set (choices of triples $(x_i,x_j,x_o)$) plus a continuous set $\mathbb{R}^{|\nu|\times 3}$. However, it appears that this might not have been the original intention. Regardless, a substantial amount of prior knowledge seems necessary to understand the precise definition here.

### Questions
No specific questions. I would appreciate a response with respect to the weaknesses stated above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose Spherical Patch Fields (SPF), a point cloud representation based on Spherical Gaussian (SG) to generate many spherical patches to obtain local and global information, and proposed PG-Layer to improve the learnable SPF representation using low-frequency information and adaptive patches. Besides, the authors verified its effectiveness on three public datasets and their proposed method achieved competitive results.

### Strengths
The idea is somehow novel and interesting. The writing of the entire paper is fine in general, and the paper is easy to read.

### Weaknesses
1. More recent related works should be compared, such as Section 4.4, which does not compare with the latest rotation-invariant method: Rotation-invariant transformer for point cloud matching[1]. Section 4.6 does not compare the state-of-the-art point cloud completion methods: Diverse point cloud completion with Geometry-Aware Transformers[2]. Specifically, the lack of comparison with [1] is a significant oversight, as it directly addresses rotation invariance, a core claim of the proposed method. Similarly, the absence of a comparison with [2] in the point cloud completion task leaves the reader unsure of the relative performance of the proposed method against a strong baseline.

2. In Table 3, the proposed method does not perform well in some classes and reasons should be analyzed and discussed. The lack of detailed analysis for the per-class performance is a critical weakness. It is not sufficient to simply present the results; the authors need to investigate and explain why the method struggles with certain object categories. This could point to limitations in the representation or the learning process that need to be addressed.

3. Some sentences are not clear. For example, the red arrow in Figure 1 is ambiguous, and the lower-right circle in the SPF part lacks an arrow. In Section 5, typo: ``resizeable'' ⇒ ``resizable''. The ambiguity in Figure 1 makes it difficult to understand the proposed method. The lack of clarity in the figure undermines the explanation of the core concepts. The typo in Section 5, while minor, detracts from the overall polish of the paper.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an integrable backbone for SO(3)-equivariant point-cloud learning, called Learnable Spherical Patch Fields (DeepSPF).
The proposed method is based on a patch-wise representation obtained using spheres, introduced as Spherical Patch Fields. 
The method aims at seamlessly integrating local and global contextual information, adaptively extracted by the presented Patch Gaussian Layer. The experimental validation of the proposed model focuses on Scan-to-CAD (S2C) — a sub-task of reconstructing indoor environments, including point cloud registration, retrieval, and completion — and provides a considerable improvement over the baseline models.

### Strengths
S1. The provided illustrations are neat and facilitate the reader’s understanding of the method. 

S2. The proposed DeepSPF successfully tackles an important problem of equivariant local and global feature extraction, by enabling multiple-layer learning of the spherical representations. 

S3. The effectiveness of the proposed DeepSPF backbone is demonstrated on various point cloud tasks with clear improvement over the baselines, both quantitatively and qualitatively.

### Weaknesses
W1. Unclear presentation.
The manuscript relies heavily upon the related and prior work, which makes in particular Section 3 hard to follow for readers less familiar those works. The important components from the related work, e.g., Vogel (1979), Wang et al. (2018), and Salihu & Steinbach (2023), could be presented in more detail in the Appendix.

W2. SO(3)-equivariance is at the heart of the paper, as the title, Abstract, and Introduction imply. However, the method section is missing the crucial part of the equivariance discussion, which is instead placed in the Appendix.

W3. A more detailed complexity analysis is required (see the Questions), as the brief mention in the conclusion does not suffice.

### Questions
Q1. Section 3

•	after equation 1: Was $v \in \mathcal{S}^3$ meant to be $v \in \mathcal{R}^3$ or $v \in \mathcal{S}^2$? 

•	after equation 7: since we are in 3D, why is the sphere $\mathcal{S}^3$ and not $\mathcal{S}^2$?

Q2. Section 3.2: 

•	Which “previous work” is meant in the second line in the first paragraph and the first line of page 5?

Q3. Is the proposed method SPF also equivariant to reflections? I.e., is the entire O(3) group covered?

Q4. Can the proposed method generalize to dimensions higher than 3?

Q5. How sensitive is the model with respect to the number of spheres |v|?

Q6. It would be useful if the authors summarized all the learnable parameters of SPF.

Q7. What is the total number of parameters of the DeepSPF models used in the experiments?
How does this compare to the baselines?

Q8. What is the computational complexity of the DeepSPF compared to the baselines? 
Could the authors provide a speed comparison?

Minor:

•	Equation 4: Should $l$ be $i$ in the {} under the max?

•	Punctuation between the equations is missing, e.g., 9 and 10. 

•	Equation 12 is a part of equation 11.


In the rebuttal, my questions were addressed appropriately, thus the assessment is updated.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
