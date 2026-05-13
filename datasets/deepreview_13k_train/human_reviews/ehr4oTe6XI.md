# Disentangled Representation Learning with the Gromov-Monge Gap

- Decision: Accept
- Scores: 6, 6, 5, 5

## Abstract
Learning disentangled representations from unlabelled data is a fundamental challenge in machine learning. Solving it may unlock other problems, such as generalization, interpretability, or fairness. Although remarkably challenging to solve in theory, disentanglement is often achieved in practice through prior matching. Furthermore, recent works have shown that prior matching approaches can be enhanced by leveraging geometrical considerations, e.g., by learning representations that preserve geometric features of the data, such as distances or angles between points. However, matching the prior while preserving geometric features is challenging, as a mapping that \textit{fully} preserves these features while aligning the data distribution with the prior does not exist in general. To address these challenges, we introduce a novel approach to disentangled representation learning based on quadratic optimal transport. We formulate the problem using Gromov-Monge maps that transport one distribution onto another with minimal distortion of predefined geometric features, preserving them \textit{as much as can be achieved}. To compute such maps, we propose the Gromov-Monge-Gap (GMG), a regularizer quantifying whether a map moves a reference distribution with minimal geometry distortion. We demonstrate the effectiveness of our approach
for disentanglement across four standard benchmarks, outperforming other methods leveraging geometric considerations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach for unsupervised disentangled representation learning, aiming to balance prior alignment with the preservation of geometric features within latent spaces. Achieving disentangled representations without supervision is difficult; recent studies suggest that maintaining the geometric structure of the data distribution can promote disentanglement. However, aligning data with a prior distribution while fully preserving geometric properties often requires trade-offs. Therefore, the authors introduce the Gromov-Monge Gap (GMG), a regularizer based on optimal transport theory that learns a mapping with minimal distortion.

### Strengths
- The paper is well-organized and clearly written.
- Introducing the Gromov-Monge Gap as a regularizer provides a fresh approach to minimizing geometric feature distortion, presenting a promising advancement for unsupervised disentangled representation learning.
- The authors offer valuable insights, particularly in showing that preserving angles through cosine similarity can enhance disentanglement more effectively than preserving distances.
- The proof demonstrating the GMG as a weakly convex regularizer is a useful contribution for future work in this area.

### Weaknesses
 - The paper provides limited discussion on the scalability of GMG for high-dimensional real world datasets.
- There is an absence of ablation studies on key hyperparameters, such as entropic regularization.

### Questions
- Considering the entropic regularization parameter plays a role in the optimization, how does adjusting the hyperparameter affect the computational efficiency and convergence of the GMG computation? An ablation study of varying hyperparameters would be nice.
- How scalable is GMG to high-dimensional real world datasets for the VAE configuration?

### Soundness
4

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
2

### Summary
This paper introduces a new method for disentangled representation learning based on quadratic optimal transport theory using Gromov-Monge maps. The authors leverage Gromov-Monge Gap (GMG) to measure how well a mapping preserves geometric features while transporting between distributions with minimal distortion. The approach aims to effectively combine geometric constraints with prior matching by finding mappings that optimally balance geometric preservation and distribution alignment. The method is validated on four standard disentanglement benchmarks (Shapes3D, DSprites, SmallNORB, Cars3D) showing consistent improvements over existing disentanglement approaches.

### Strengths
1. This paper provides a fresh perspective on combining geometric constraints with prior matching in disentanglement learning. Different from previous works that use direct penalties for geometric preservation, the authors propose using Gromov-Monge maps to find mappings that optimally preserve geometric features while aligning distributions. The theoretical analysis proves weak convexity of the GMG regularizer and provides precise characterization of convexity constants.

2. The authors have conducted comprehensive experiments across multiple benchmarks and architectural choices. Through thorough ablation studies, they demonstrate that angle preservation outperforms distance preservation, decoder regularization is more effective than encoder regularization, and the GMG shows better gradient stability compared to distortion-based approaches. Additionally, they show the method can be integrated with existing approaches like β-VAE and β-TCVAE to enhance their performance.

### Weaknesses
1. It remains unclear to me why the Gromov-Monge map framework is the optimal choice for combining geometric preservation with distribution alignment. While the authors show empirically that GMG outperforms direct distortion penalties, they don't fully explain why measuring suboptimality in the Gromov-Monge problem provides a better learning signal than other potential optimal transport formulations or geometric metrics. Specifically, the paper lacks a detailed comparison to other optimal transport based approaches that might also be suitable for this task, such as those based on sliced Wasserstein or other variants of optimal transport that could potentially offer similar or better performance with different computational trade-offs. A more thorough justification of why the Gromov-Monge framework is uniquely suited, beyond empirical results, is needed.

2. My another concern is about the practicality of solving Gromov-Wasserstein problems during training. Although the authors provide computational complexity analysis and propose using entropic regularization with scaled costs, they don't thoroughly investigate how different solver parameters affect the trade-off between computational efficiency and accuracy of the approximation. The sensitivity analysis of the entropic regularization parameter $\epsilon_0$ and its impact on training dynamics needs more exploration. The paper should include a more detailed analysis of how the choice of $\epsilon_0$ affects the convergence of the Gromov-Wasserstein solver and the overall training process. It is also unclear how the scaling of the cost matrices interacts with the choice of $\epsilon_0$ and whether this scaling is optimal for all datasets.

### Questions
1. Why does angle preservation work better than distance preservation? Is this finding specific to the datasets tested?

2. How sensitive is the method to the entropic regularization parameter $\epsilon_0$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies learning disentangled representations in an unsupervised setting by introducing Gromov-Wasserstein formulation into the distortion framework. They propose GMG quantifying the difference between the distortion and the Gromov-Wasserstein distance, meanwhile, they show that GMG is weakly convex. They validate the effectiveness of GMG in four 3D datasets.

### Strengths
1. The intuition of this idea is good, it tries to minimize the difference between the previous Distortion and Gromov-Wasserstein distance so that the mapping between source and target should preserve the full features with minimal distortion. 
2. They show that the GMG and its counterpart are weakly convex functions. 
3. The experiments in 3D Shapes dataset and the clustering illustration sound persuasive.

### Weaknesses
 1. The computation of Gromov-Wasserstein distance is very expensive even when entropy regularizer is employed, the time complexity is still around O(N^5). This makes the GMG not practical when involving the method in a large-scale data setting. 
 2. Limited experiments: the datasets in the experiments are all about 3D shapes. How about 2D shapes? I would like to see how it can apply to the MNIST, another simple 2D digit. 
 3. I believe that the robustness should also be important part but this work seems to ignore it. What if the data has out-of-distritbution points? In fact, DST is not robust in the noisy data setting.

### Questions
1. Have you applied the method on datasets other than 3D dataset? For example, MNIST. 

2. Have you tested the method on noisy point clouds? Or any other noisy dataset? 

3. The whole framework is very computational expensive, do you think how it can be applied to large-scale setting? Have you thought about acceleration?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes to learn disentangled representation from the perspective of preserving geometric features. They propose to learn a pair of isometric encoder and decoder, hoping these inductive biases can benefit disentanglement. Based on this motivation, they propose to leverage Gromov-Monge mappings to enforce such an optimal transport (OT) mapping.

### Strengths
1. The empirical performance is good, indicating that adding this neural GM gap can improve the disentanglement score for many architectures.

### Weaknesses
1. The motivation and logical connection is not clear. There are three concerned concepts in the paper: isometry, OT, and disentanglement. The authors claim that adding geometrical constraints (isometry) can help disentanglement, but this connection is not explained well in the paper, which makes it hard to understand how disentanglement connects isometry. Even if there is such a connection, it is not clear why OT is required for isometry. You can just do an isometry mapping. I would expect the authors to explain these two connections more clearly in the revision.

2. The experiments are not set up well to support the main contribution of the paper. If the authors would like to show the benefit of isometry, the authors can follow homeomorphic VAE [1] to show the isometry can hep data on different groups/manifolds. If the authors would like to show the benefit of OT, there is Wasserstein auto-encoder. If the authors want to show the benefit of OT in disentanglement, there are [2] and [3] which learn an OT mapping to model disentangled sequential transformations. I do not see a direct connection between isometric OT mapping and disentanglement.

3. How does the method compare with the vanilla differentiable Sinkhorn algorithm [4]? Will there be any theoretical guarantees? Beyond the vanilla OT problem, there exist other OT solver like entropic OT and unbalanced OT. Do these techniques apply to disentanglement?

4. In a disentanglement paper, it is rare to not see figures about latent traversal which show the exact results of disentanglement. 

5. How does the method work in more scaled settings, i.e., high-resolution disentanglement datasets like Falcol3D and Issac3D [5]?

### Questions
Please refer to the weaknesses.

My main confusion comes from the logical connection of this paper from isometry to disentanglement to OT. Please try to address this issue in the rebuttal.

### Soundness
3

### Presentation
2

### Contribution
1
