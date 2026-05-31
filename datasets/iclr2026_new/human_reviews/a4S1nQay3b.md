## Human Reviewer 1

### Summary
This paper addresses noisy correspondence in real-world multi-view clustering. The authors identify category-level mismatch and sample-level mismatch. The paper proposes a generative framework based on maximum likelihood estimation and optimized via an Expectation-Maximization algorithm. The framework infers a soft correspondence distribution in the E-step (guided by GMM-based marginals and optimal transport) and refines embeddings in the M-step. Experiments on four benchmark datasets demonstrate superior robustness under various noisy settings, including up to 80% mismatch rates.

### Strengths
1）The paper presents a thoughtful formulation by explicitly distinguishing two realistic types of noisy correspondence in multi-view data, namely, category-level mismatch and sample-level mismatch, providing a solid rationale for why existing contrastive MVC methods fall short under such conditions.
2）Instead of relying on pairwise contrastive learning, the authors shift to a generative modeling perspective, leveraging an Expectation-Maximization algorithm to uncover latent correspondences. This allows them to model complex many-to-many, probabilistic associations between samples across views.	
3）The method demonstrates consistently strong performance across diverse datasets and under various levels of noise and corruption.

### Weaknesses
1）The related work section does not adequately cover more recent progress, especially in areas concerning missing modalities and partially view-aligned representation learning.
2）Although warm-start and momentum updates are mentioned as strategies to stabilize training, the paper does not provide convergence curve analyses.
3）The paper does not include comparisons with recent methods that also employ optimal transport for multi-view clustering. Incorporating an experimental comparison with approaches such as “PROTOCOL: Partial Optimal Transport-enhanced Contrastive Learning for Imbalanced Multi-view Clustering” would strengthen the work.

### Questions
1）Could the authors provide a more comprehensive comparison with recent advances on incomplete multi-view and PVP problems, especially those published post 2022?
2）Can the authors provide quantitative or visual evidence (e.g., convergence plots) to support the stability and convergence behavior of CorreGen’s EM algorithm?
3）How does CorreGen compare with other OT-based multi-view methods in terms of robustness?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper addresses the challenge of noisy correspondence (NC) in multi-view clustering (MVC), which arises when data collected from the web contains misaligned or unmatchable samples. The authors distinguish two harmful types of NC: 1) Category-level mismatch: samples from the same class treated as negative; 2) Sample-level mismatch: mispaired or unalignable samples. To tackle this, they propose CorreGen, a generative EM-based framework that formulates correspondence discovery as maximum likelihood estimation. In the E-step, they estimate soft correspondence distributions using optimal transport constrained by GMM-guided marginals and augmented with virtual samples to absorb outliers. In the M-step, they update embeddings to maximize expected log-likelihood using these inferred correspondences. Extensive experiments on synthetic and real datasets show strong robustness with substantial improvements under both category- and sample-level mismatches.

### Strengths
1. This paper shifts from discriminative pairwise reweighting/realignment to a principled maximum likelihood framework, reducing reliance on noisy pre-defined pairs.
2. The proposed method consistently outperforms state-of-the-art baselines under varying mismatch and corruption rates, especially on the noisy UMPC-Food101 dataset.

### Weaknesses
1. While the EM-based optimal transport is elegant, they may introduce computational overhead when applied to very large-scale or high-dimensional datasets. The paper would benefit from a more detailed runtime analysis.
2. The paper should clarify why the posterior weight $Q_{ij}$ is defined as $\frac{\boldsymbol{P}_{ij}^*}{\boldsymbol{p}_i^{(v_1)}}$ in Equation (17).
3. In Equation (17), the matrix ${Q}$ appears to serve as a re-alignment signal that guides the model's learning. It would be informative to analyze what happens if ${Q}$ is replaced with an identity matrix, and how would performance change if ${Q}$ were substituted with the ground-truth correspondence matrix?
4. A minor presentation issue: on page 2, the text refers to Figure 2, but it seems this should be Figure 1.

### Questions
Please refers to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
Multi-view clustering (MVC) leverages cross-view consistency but suffers from noisy correspondence (NC), including category-level mismatch and sample-level mismatch. This paper proposes a generative framework, CorreGen, which formulates NC learning as maximum likelihood estimation of underlying cross-view correspondences, solved via an Expectation-Maximization (EM) algorithm. In the E-step, soft correspondence distributions are inferred using GMM-guided marginals to down-weight noisy samples; in the M-step, the embedding network is updated to maximize expected log-likelihood. Extensive experiments on synthetic and real-world datasets demonstrate superior robustness.

### Strengths
1.	This paper introduces a generative framework that reduces reliance on noisy predefined pairs by modeling latent correspondences, enabling more robust semantic structure learning.
2.	This method effectively handles both category-level and sample-level mismatch via GMM-guided marginals and virtual samples, outperforming baselines on complex datasets.
3.	Ablation studies show stable performance across varying curve-shaping parameters and noise rates, reducing hyperparameter tuning burden.

### Weaknesses
1.	This method may incur higher computational cost due to EM iterations, GMM fitting, and optimal transport computations, potentially limiting scalability to very large datasets.
2.	This method relies on GMM assumptions, which may fail to model non-Gaussian embedding distributions, leading to suboptimal marginal estimates in complex data.
3.	The experiments focus on two-view settings, limiting generalization to multi-view scenarios where correspondence inference becomes more complex.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper tackles noisy correspondence in multi-view clustering, arguing that real-world, web-crawled pairs contain (i) category-level mismatches (same class but treated as negatives) and (ii) sample-level mismatches including both alignable mispairs and truly unalignable samples. It proposes a generative objective that maximizes the (marginal) joint likelihood over latent cross-view correspondences and optimizes it with an EM procedure: the E-step estimates a soft, many-to-many coupling via entropy-regularized optimal transport subject to GMM-guided marginals and augmented with a virtual node to absorb outliers; the M-step maximizes a weighted log-likelihood implemented with similarity-normalized scores, unifying InfoNCE as a special case.

### Strengths
The paper treats cross-view links as latent variables and optimizing a likelihood bound provides a clean alternative to ad-hoc pair reweighting strategy. The design explicitly handles category-level relations (many-to-many couplings) and unalignable samples (virtual node), which prior methods largely ignore. 

Experiments on Scene15, LandUse21, Caltech101, and UMPC-Food101 show consistent gains under varying mismatch and corruption rates; visualizations indicate the learned posteriors approach class-level ground truth during training.

### Weaknesses
1.The proposed method depends on several manually tuned hyperparameters, such as the virtual mass $\rho$ and the number of Sinkhorn iterations. The paper lacks a sensitivity analysis showing how performance varies with these values.

2.While the paper qualitatively visualizes the estimated correspondences in Figure 3, it does not provide any statistics about the intrinsic mismatch level of the datasets used. Without knowing the original category- or sample-level mismatch rate, it is difficult to judge how challenging the benchmark setting is. 

3.The introduced EM-style framework, particularly the Sinkhorn-based E-step with virtual-node augmentation, likely incurs non-trivial computational overhead. The paper does not report training time or GPU memory consumption.

### Questions
1.Please provide a sensitivity analysis for $\rho$ and the number of Sinkhorn iterations?

2.Please report the original category-level mismatch rate in the used datasets.

3.What is the computational cost of the EM procedure? Specifically, how do the training time and GPU memory usage compare with those of DIVIDE?

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