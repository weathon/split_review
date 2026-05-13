# Towards Marginal Fairness Sliced Wasserstein Barycenter

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
The Sliced Wasserstein barycenter (SWB) is a widely acknowledged method for efficiently generalizing the averaging operation within probability measure spaces. However, achieving marginal fairness SWB, ensuring approximately equal distances from the barycenter to marginals, remains unexplored. The uniform weighted SWB is not necessarily the optimal choice to obtain the desired marginal fairness barycenter due to the heterogeneous structure of marginals and the non-optimality of the optimization. As the first attempt to tackle the problem, we define the marginal fairness sliced Wasserstein barycenter (MFSWB) as a constrained SWB problem. Due to the computational disadvantages of the formal definition, we propose two hyperparameter-free and computationally tractable surrogate MFSWB problems that implicitly minimize the distances to marginals and encourage marginal fairness at the same time. To further improve the efficiency, we perform slicing distribution selection and obtain the third surrogate definition by introducing a new slicing distribution that focuses more on marginally unfair projecting directions. We discuss the relationship of the three proposed problems and their relationship to sliced multi-marginal Wasserstein distance. Finally, we conduct experiments on finding 3D point-clouds averaging, color harmonization, and training of sliced Wasserstein autoencoder with class-fairness representation to show the favorable performance of the proposed surrogate MFSWB problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The traditional Sliced Wasserstein Barycenter (SWB) employs uniform weights between the barycenter and its marginals, leading to imbalances in the distances between them. This paper introduces the Marginal Fairness Sliced Wasserstein Barycenter (MFSWB), which aims to equalize these distances, ensuring a fairer representation. The authors propose three algorithms to address the MFSWB formulation and conduct experiments on synthetic Gaussian distributions, 3D point clouds, color harmonization, and generative models. The results demonstrate that the proposed method is highly effective, validating the authors' claims.

### Strengths
This paper addresses an important problem that has been overlooked. In traditional SWB, the weights between barycenter and marginals are uniform. However, this uniform weights actually leads to non-uniform distances between the barycenter and the marginals. The authors have a simple experiment demonstrating that in the paper. To ensure equal distances, they propose the MFSWB to address this problem. They define MFSWB such that the average distance to be within an $\epsilon$.

The proposed MFSWB is hard to solve. The authors proposed three surrogate definitions for MFSWB. The first one, called s-MFSWB, aims to minimize the maximal distance from the barycenter to the marginals. Yet, the s-MFSWB is biased. To rectify this, they proposed the second unbiased surrogate, us-MFSWB. They show that us-MFSWB's objective is an upper bound of s-MFSWB, meaning that minimizing us-MFSWB implicitly minimizes s-MFSWB. Furthermore, They also show that the approximation error of the gradient estimator of us-MFSWB reduces at the order of $\mathcal{O}(L^{−1/2})$. Since s-MFSWB and us-MFSWB both use the uniform distribution as the slicing distribution, which can empirically result in non-optimal in statistical estimation, the authors proposed the energy-based surrogate MFSWB (es-MFSWB) which considers the importance of the sampling directions. 

The authors conducted extensive experiments evaluating the proposed methods and comparing the methods against the conventional SWB. The results are convincing. Using the synthetic Gaussian data, they showed that SWB produced the barycenter with non-uniform distances from the marginals, whereas the proposed methods yielded barycenters with approximately equal distances from the marginals. The authors also performed experiments on the 3D points clouds, Color Harmonization, and generative models with both quantitative results and qualitative results showing the effectiveness of the proposed method. The proposed es-MFSWB appears to be the best among all three proposed methods. 

The authors shows the potential of using the proposed method in learning conditional generative models as an inverse barycenter problem.

### Weaknesses
I didn't really catch any weakness of this paper. The paper is complete with clear motivation, effective solutions and sufficient experimental results.

### Questions
Did you have a typo in line 506? Should $P_{f(X_k)}$ be equal to $\frac{1}{M} \sum_{i=1}^M \delta_{f(X_{ki})}$?

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
This paper aims at achieving marginal fairness sliced wasserstein barycenter (MFSWB). To tackle the problem, the authors define the MFSWB as a constraint SWB problem. Due to the computational disadvantages of the formal definition, the authors propose two hyperparameter-free and computationally tractable surrogate MFSWB problems that implicitly minimize the distances to marginals and encourage marginal fairness at the same time. To further improve the efficiency, the authors perform slicing distribution selection and obtain the third surrogate definition by introducing a new slicing distribution that focuses more on marginally unfair projecting directions. The experimental results demonstrate the favorable performance of the proposed MFSWB performance.

### Strengths
1. The paper is well-organized and the writing is good.
2. The paper has solid theoretical proofs.
3. The story line is easy to follow.

### Weaknesses
Please refer to questions.

### Questions
1. Can the authors elaborate on the significance of MFSWB? The description in current version is somewhat high-level.
2. Can the authors provide a clearer description about the formulation in line 148?
3. What does the symbol $\sharp$ in Eq.(1) denote?
4. What does the $x_i(y_i)$ in line 144 denote?
5. What does the $\pi$ in line 144 denote?
6. What modification to the methodology presented in this paper are necessary to replace SWD with GSWD [1] or ASWD [2]?

[1] Kolouri, Soheil, et al. "Generalized sliced wasserstein distances." Advances in neural information processing systems 32 (2019).

[2] Chen, Xiongjie, Yongxin Yang, and Yunpeng Li. "Augmented sliced Wasserstein distances." arXiv preprint arXiv:2006.08812 (2020).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the marginal fairness sliced Wasserstein barycenter (MFSWB) problem. The goal of MFSWB is to achieve fairness of barycenter to marginals. To solve the problem, the Lagaragian format and three surrogate formulations are proposed, from biased estimation to unbiased estimation. Both time and space complexities are analyzed. 

For the experiments, Gaussian toy data is utilized for verification. Then, point cloud, color hamonization, and SWAE experiments are conducted on more realistic data.   
Both fairness metirc and barycenter metrics are reported.

### Strengths
- The presented problem is novel and reasonable. If fairness of barycenter can be achieved w.r.t. marginals, then varous future applicaiton can be conducted e.g. ensuring fairness of ML algorithms. 
- The paper organization, problem definition and writing is good and easy to follow. If audience has some Sliced Wasserstein knowledge, then it will be easy to follow the idea. 
- The Lagaragian formulation as well as three surrogates are proposed to deal with the Fairness barycenter estimation with unbiased gradient estimator.   
The space and time complexity analysis show that the proposed e-MFSWB has good space and time complexity compared with conventional SWB.

### Weaknesses
 - Most of the experiments conducted are simple or on simple dataset, such as Gaussian, Simple Color Hamonization of two images or point cloud of only two shapes, AE on simple MNIST dataset.   
I am wondering the scability and real application of the proposed method. For example, if more than two (e.g. >5) images or point clouds are adopted, what might be the results?   
Or are there more realistic potential appplications of the proposed method? If related work or potential applications are discussed, it would be better. For example, CelebA dataset results or Fairness generation [R1]. 
- USWB first appears in Figure 1 and used in several places. But it is not defined. 
- I can understand the F-metric is significantly improved with the proposed solution. But for W-metric why it is also improved. Are there feasible explanation or insights? Can you provide an explanation or discussion on why the W-metric improves along with the F-metric? This would be valuableto better understand the proposed method. 

### Questions
- What does USWB stand for in the paper? 
- Can the method extended to settings with more than two images or point cloud?

### Soundness
3

### Presentation
3

### Contribution
3
