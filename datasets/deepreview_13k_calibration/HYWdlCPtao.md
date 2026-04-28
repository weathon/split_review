# Curvature Enhanced Manifold Sampling

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Over-parameterized deep learning models, characterized by their large number of parameters, have demonstrated remarkable performance in various tasks. Despite the potential risk of overfitting, these models often generalize well to unseen data due to effective regularization techniques, with data augmentation being one of the most prominent methods. This strategy has proven effective in classification tasks, where label-preserving transformations are applicable. However, the application of data augmentation in regression problems remains underexplored. Recently, a new *manifold learning* approach for sampling synthetic data has been introduced, and it can be viewed as utilizing a first-order approximation of the data manifold. In this work, we propose to extend this direction by providing the fundamental theory and practical tools for approximating and sampling general data manifolds. Further, we introduce the curvature enhanced manifold sampling (CEMS) data augmentation method for regression. CEMS is based on a second-order encoding of the manifold, facilitating sampling and reconstruction of new points. Through extensive evaluations on multiple datasets and in comparison to several state-of-the-art approaches, we demonstrate that CEMS is superior in in-distribution and out-of-distribution tasks, while incurring only a mild computational overhead.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method data generation for regression problems. Different from existing methods that use the first-order scheme to sample data, this paper uses second-order schemes. The authors use multiple datasets to evaluate the performance.

### Strengths
This method has a strong theoretical basis.

### Weaknesses
1. The motivation is designing data augmentation for regression problems. What are the differences and challenges between the method and methods for classification? It is unclear.

2. For me, the experiments are weak. In Table 1, the experiments are conducted on several datasets that are not familiar to me, and the improvements are marginal.

3. There are also data augmentation methods on Riemannian manifolds, such as [a]. The authors should add more comparisons with them.
[a] Hyperbolic feature augmentation via distribution estimation and infinite sampling on manifolds. NeurIPS 2022.

### Questions
See the above weakness.

### Soundness
3

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
3

### Summary
The authors introduce a data augmentation method tailored for regression tasks. It leverages second-order manifold approximations to better capture the curvature and structure of data, improving upon first-order methods. Through comprehensive experiments on various datasets, CEMS demonstrates its effectiveness in both in-distribution and out-of-distribution scenarios, often outperforming existing state-of-the-art techniques.

### Strengths
1.Novelty: The paper introduces Curvature Enhanced Manifold Sampling (CEMS), an interesting method in data augmentation. CEMS utilizes second-order manifold approximations, providing a more accurate representation of the data's intrinsic geometry compared to first-order methods.

2.Empirical Validation: The authors extensively evaluate CEMS across nine diverse datasets, demonstrating its competitive performance against state-of-the-art techniques in both in-distribution and out-of-distribution tasks. This robust empirical validation strengthens the credibility of CEMS as an effective data augmentation technique.

### Weaknesses
1.Computation Complexity: The paper acknowledges that the linear system in CEMS is preferably over-determined, which constrains the number of neighbors to be proportional to the square of the intrinsic dimension. This requirement can become expensive for high-dimensional data. The analyzed complexity results require more comprehensive comparisons with other competitors. Specifically, the paper does not provide a clear breakdown of the computational cost associated with each step of the CEMS algorithm, such as the neighbor selection, Hessian estimation, and sampling process. This lack of granularity makes it difficult to assess the true computational bottleneck and compare it fairly with other data augmentation methods. Furthermore, the analysis should consider not only the asymptotic complexity but also the practical runtime, especially when dealing with large-scale datasets.

2.Memory Inefficiency: The Singular Value Decomposition (SVD) computation needed for CEMS demands significant memory, especially for datasets with many features, which may limit its applicability in scenarios with limited memory resources. Thus it’s kindly suggested to analyze the space complexity, and point out some scenarios where CEMS works well. The paper should provide a more detailed analysis of the memory footprint of the SVD computation, including the size of the matrices involved and the memory required to store intermediate results. It is also important to discuss how the memory requirements scale with the batch size, the number of features, and the intrinsic dimension of the data. Additionally, the paper should explore potential strategies to mitigate the memory overhead, such as using low-rank approximations or iterative SVD algorithms.

### Questions
1.Can CEMS be adapted to handle datasets with high intrinsic dimensions more efficiently, in terms of computational complexity or memory usage? Especially for estimating the Hessian matrix, could the authors discuss some potential techniques to approximate the second-order counterpart and accelerate the computation?

2.As stated in the title and introduction, the manifold information is introduced to investigate the underlying geometric information like manifolds. How does CEMS compare to other manifold learning techniques in terms of bias-variance trade-offs and its ability to capture complex, non-linear relationships in data?

3.This work is stated to provide the foundational theory, where only the computation complexity is analyzed. 

So what are the theoretical guarantees of CEMS in terms of generalization, algorithmic convergence? As for DA task, how to theoretically analyze the quality of generated samples compared to some baselines? 

4.It’s suggested to provide the standard variance information of these repeated experiments instead of merely averages.

### Soundness
2

### Presentation
3

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
The paper introduces a new data augmentation method based on manifold learning specifically designed for regression problems. It is grounded in manifold learning and uses a second-order approximation of the data manifold to capture the underlying curvature and structure of the data more accurately than previous first-order methods. Therefore, it generates new examples by sampling from a second-order representation of the data manifold, which allows for better capture of nonlinearities and complex structures that first-order methods might miss.Through extensive evaluations on multiple datasets and comparison with several state-of-the-art approaches, it demonstrates superior performance in both in-distribution and out-of-distribution tasks, while incurring only a mild computational overhead.

### Strengths
1.  Data augmentation for regression is often overlooked previously. The paper positions data augmentation for regression as a manifold learning problem and provides foundational theory and practical tools for approximating and sampling general data manifolds.
2. The method is domain-independent, and fully differentiable, making it applicable to various data forms such as time series, tabular data, images, and more.

### Weaknesses
1. Lack of comprehensive discussion of related work, e.g, [1] also used the tangent space sampling for out-of-distribution problem. I suggest adding a paragraph for manifold learning and second-order sampling.

2. Lack of computation cost discussion of the proposed framework. The second-order sampling might not be feasible for high dimensional data.

3.  CEMS prefers an over-determined system of equations for the linear system in Equation 6, which constrains the number of neighbors to be O(d^2), where d is the intrinsic dimension. For larger values of d, this requirement can become expensive and impractical.

### Questions
1. Are there any plans to extend CEMS to handle other types of learning tasks, such as classification or reinforcement learning?
2. Could you provide more insights into how CEMS performs on datasets with different levels of complexity and curvature?
3. How does CEMS handle non-linear transformations and high-dimensional data effectively?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This submission focuses on improving the generalization ability of the model with data augmentation (DA). Specifically, the sample generation framework for extending the training set is considered. For existing advances in DA, e.g., linear interpolation in Euclidean space under MixUp framework and manifold sampling under the first-order approximation of data manifold, a common challenge is to ensure the validity of sampling for continuous output spaces and highly nonlinear structure, e.g., regression. This work proposes a noise robustness framework on the manifold, which generates noise-perturbed samples on the tangent space via second-order approximation, and projects them back to the manifold via retraction. A fast computation algorithm is developed to reduce the complexity of the second-order approximation with gradients and Hessians. Compared with SOTA in-distribution/out-of-distribution generalization method, the proposed method achieves superior performance in different benchmarks.

### Strengths
+ The motivation is clear, where the main challenge is to characterize a complex manifold structure that lies in the complex output space.

+ The method is technically sound, which employs the second-order approximation formulation with gradients and Hessian to sample new points in the tangent spaces. 

+ The superior experiment results over SOTA DA methods on different generalization learning tasks.

### Weaknesses
W1. Methodology. The fast computation with the designed neighborhood extraction strategy seems to be sensitive to the data structure where further justifications are needed. Specifically, the reliance on a fixed neighborhood size $N_z$ for all points may not be appropriate for datasets with varying densities or complex manifold structures. The method assumes a consistent local geometry within each $N_z$, which may not hold true, particularly in regions of high curvature or sparse data. The use of k-nearest neighbors might not be optimal for capturing the true underlying manifold structure, especially if the data is not uniformly distributed.

W2. Clarity of Presentation. Though the sampling framework is clearly presented, it seems that the learning process with the generated samples is not clearly stated. The paper does not explicitly describe how the generated samples are integrated into the training process. It is unclear whether the generated samples are used in every training epoch, or if they are used in a specific way, such as a curriculum learning approach. The interaction between the original data and the augmented data during training needs to be clarified.

W3. Significance. Though the steps of existing first-order method FOMA is discussed, the difference between FOMA and proposed second-order method CEMS is not formally discussed, i.e., there seems no rigorous results or in-depth analysis on the fundamental advantages of DA with second-order approximation from mathematical aspects. While the empirical results demonstrate the superiority of the second-order method, the theoretical justification for this improvement is lacking. The paper does not provide a formal analysis of the approximation error for both first and second-order methods, nor does it discuss the conditions under which the second-order approximation is expected to perform better.

### Questions
Q1. As far as I understand the proposed neighborhood extraction strategy, once neighbor set $N_z$ is computed for $z$, this set will be shared by all points in $N_z$; consequently, the manifold sampling operation, e.g., projection for tangent space and retraction for generation, will be identical for points in $N_z$. 1) As such a partition of $N_z$ seems to boil down to a clustering process, will the quality of generated samples be sensitive to $N_z$? 2) Could such a partition process be replaced by more reliable clustering algorithms? 

Q2. Following Q1, if $N_z$ contains the sample with high diversity w.r.t outputs, the generation process seems could be error-prone. For example, considering the classification scenarios with discrete output space, if $N_z$ contains multiple inter-class samples while they still share the same projection basis, it could induce discriminability degradation on patterns.

Q3. As mentioned in the motivation, the primary goal is to ensure the generation quality in a highly nonlinear space. According to the fast computation pipeline in lines 278-286, all points in $N_z$ are projected onto the tangent space in $\mu$, i.e., the mean of $N_z$. If the structure near $N_z$ is highly nonlinear, how to ensure the generation and local structure characterization of points $u_l \in N_z$ are still valid? 

Q4. Following Q3, for the generation process in Line 285, it seems that the generation points are distributed around $\mu$ while not $u_l$, i.e., it seems to be equivalent to the random sample $\eta \sim \mathcal{N}(0,\sigma I_d)$ for $N$ times ($N$ is the number of samples) and then substitute them into Eq. (2). Compared with the point-wise computation on each $u_l$, the fast computation saves time while losing the sample information. Moreover, it seems that there would be only a few real samples (i.e., ignoring the noise $\mu$ in the sampling process) generated samples (i.e., the means $\mu$ over different $N_z$). In-depth analysis is highly expected.

Q5. How to justify the advantage of second-order approximation for sampling from a mathematical aspect? Specifically, compared with the first-order approximation, how can the proposed method ensure better quality? Though empirical observation is provided, i.e., Fig. 1, it would be apricated to justify them from fundamental aspects, e.g., the differences between employing Eq. (2) (second-order) and lines 294-304 (first-order).

Q6. The essential of CEMS is ensuring the robustness w.r.t noise on manifold space, while the term 'manifold sampling' in tile could be inappropriate since it seems that CEMS can only guarantee sampling in a local area with the Taylor expansion. Thus, it would be interesting to discuss the CEMS with the geodesic-based sampling methods that can generate unseen samples along the manifold spaces globally. 

Q7. Possible typos: DTI metric of CEMS in Tab. 2, where the average value 5.11 is significantly larger than other methods.

### Soundness
2

### Presentation
2

### Contribution
3
