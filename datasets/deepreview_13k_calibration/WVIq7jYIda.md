# Manifold Kernel Rank Reduced Regression

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
The Kernel Rank Reduced Regression (KRRR) technique works well on highly dependent dataset with a latent variable structure.
When we extended the KRRR to the Reproducing Kernel Hilbert Space (RKHS), the powerful kernel presentation and  reproducing ability can enhance the regression ability. But previous research always work on Euclidean space with vector data presentation, which omit the intrinsic geometric shape of the data distribution. If the whole dataset can be thought as a manifold, the regression result will only rely on the intrinsic  data distribution instead of the extrinsic frame. So we present the manifold kernel rank reduced regression model (MKRRR).
We fist give the definition of the MKRRR model. Then with leveraging Kendall shape space for representing sample manifold data, we derive the closed-form solution of the regression model and prediction result. Moreover, we discuss the convergent and robust ability of the model, with presenting the robustness proof. At last, the we present a skull repair application by the MKRRR model for 3D mandibular reconstruction. The experiment result validate effective of our model even on the data with high-level noise.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposed manifold kernel rank reduced regression model (MKRRR) as the combination of both kernel rank reduced regression (KRRR) and geometric manifold structure. In particular this MKRRR utilize a specific type of Riemannian manifold framework, i.e., Kendall shape space. 

The algorithm and the closed-form solution are present for MKRRR with the robustness proof in appendix. 3D point cloud reconstruction experimental results for Chinese skull models datasets are given with different settings and compared with few alternative methods.

### Strengths
The core idea of combining kernel rank reduced regression and manifold framework is convincing and make sense, and the introduced concept of Kendall shape space is interesting too. 

Also good to see some related works been discussed in section 2. Closed-form solution is nice too and this additional robustness proof is helpful.

Reference 1: Q. Wu, F. M Wong, Y. Li, Z. Liu, and V. Kanade. Adaptive reduced rank regression. Advances in Neural Information Processing Systems, 33:4103–4114, 2020.

Reference 2: L. Yan, X. Wang, and Z, Wu. Example-oriented full mandible reconstruction based on principal component analysis. Multimedia Tools and Applications, 81(23):34009–34026, 2022

### Weaknesses
Equation 12 as the closed-form solution is nice and clean and should be helpful with more insight to present and how it is different from previous close-form solutions. 

Good to see the experimental results in section 5 for real 3D data though seems with only 1 data set may not enough, and the comparison to alternative works limited to PCA and PGA seems less ideal, i.e., it should be good to include more. 

It seems there are decent number of previous works in the area of kernel regression plus manifold learning, e.g., R3 is one of them and will be helpful if this work to try more comprehensive survey. 
 
Reference 3: J. Nilsson, F. Sha, and M. I. Jordan. Regression on manifolds using kernel dimension reduction. International Conference on Machine Learning (ICML), pages 697–704, 2007

### Questions
Question 1: only Figure 5 with experimental results compared to alternative methods?

Question 2: section 2 "Ashin Mukherjee and Ji Zhu (Mukherjee & Zhu, 2011)extend" here need a space before "extend."

Question 3: section 3.1 "In order to utilize the correlation between the dependent variables yi" here yi seems need format change.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study expands upon the Kernel Rank Reduced Regression (KRRR) method, introducing it to the realm of the Kendall shape space manifold.

Nonetheless, the scope of the contribution appears somewhat constrained. The main result, the formula provided in equation (12) appears to have a generic applicability to various kernel regression approaches, rendering the results not particularly novel.

Additionally, one of the principal findings, pertaining to the robustness of our approach, lacks a rigorous mathematical definition, and I expect a theoretical analysis with more precise and well-defined explanations.

### Strengths
It aim to solve a problem with real applications.

### Weaknesses
1. the formula in (12) appears to be a standard solution, not novel.

2. no theoretical definition of the claimed "robustness" in the paper, and no rigorous proof as well.

### Questions
Could you please clarify the meaning of "shapeRepresentation" within the algorithm?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors describe a method called manifold rank reduced regression and apply it on skull data.
The method combines elements from Riemannian geometry and linear algebra (reproducing kernel Hilbert space).
They study algorithmic aspects, provide a closed form solution and investigate robustness.

### Strengths
The authors seem to have a good knowledge of their domain.

### Weaknesses
The paper is not properly written.
The work lacks some general context and motivation and finally delve into an application for which the objectives are not clear either.
The authors should contextualize more their work and possibly provide more applications (and possibly mainstream applications that would appeal to a broader audience).

### Questions
What is the actual purpose of the experiment? Is it to recreate artificially a missing mandible?
If you focus on a specific application, how can the achieved accuracy be interpreted from the applicative side (archeology? are the archeologists satisfied with the numbers you achieve? or not?).
Can you clarify eq. 11? How do you justify going from left-hand side to right-hand side?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Manifold Kernel Rank Reduced Regression (MKRRR) model as an extension of the Kernel Rank Reduced Regression (KRRR) technique. KRRR enhances regression capabilities for highly dependent datasets with latent variable structures. However, prior research focused on Euclidean space with vector data representation, neglecting the inherent geometric shape of data distribution. The MKRRR model addresses this issue and relies on the intrinsic data distribution, treating the dataset as a manifold.

The authors define the MKRRR model and derive a closed-form solution for regression and prediction. Finally, the authors present an application of the MKRRR model in 3D mandibular reconstruction for skull repair, demonstrating its effectiveness even on noisy data.

### Strengths
The authors apply MKRRR to 3D mandibular reconstruction which seems to be novel and original.

### Weaknesses
The authors present the KRRR as something novel, whereas it is already well-established in the community. For example, section 4.2 derives the closed form solution ok KRRR. This solution is already available in "Reduced Rank Ridge Regression and Its Kernel Extensions" A. Mukherjee et al. from 2011. The proof is very similar, and there is no novelty in the paper.

Furthermore, the MKRRR extension is simply using a Gaussian kernel and replacing the Euclidean distance by a Riemannian one. This should be stated in a clearer manner and more straightforwardly.

The application is not very convincing. The figures 3 and 4 are very noisy. The figure 4 is not readable and the figure 5 is barely presented. Hence, it is hard to draw conclusions from the experimental section. Furthermore, the hyper parameters seem to have been tuned on the test set.

### Questions
In the theoretical part:
1) What is new in your proof of the solution of KRRR compared to the one of "Reduced Rank Ridge Regression and Its Kernel Extensions" A. Mukherjee et al. from 2011?
2) Is MKRRR just replacing the Euclidean distance with a Riemannian one in the kernel?
3) Does a positive definite kernel with a Riemannian distance exist for your problem? The three proposed in table 1 are either not geodesic distances or not positive definite.

In the numerical experiments:

1) What do you mean by "each point corresponds to one by one"?
2) From figure 4, the rank value seems to have no effect on the performance. Can you comment on that?
3) Can you explain the comparison in figure 5? How do you compare PCA, PGA to MKRRR? The first two are only preprocessing steps while MKRRR does a regression.
4) What is the noise in figure 5? Do you add a Gaussian noise to data?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
