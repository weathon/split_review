# PLS-based approach for Fair Representation Learning

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
We revisit the problem of fair principal component analysis (PCA), where the 
goal is to learn the 
best 
low-rank 
linear approximation 
of the data that obfuscates 
 demographic information. 
We propose a conceptually 
simple approach that allows for an analytic solution 
similar to standard PCA and can be kernelized.  
Our methods have the same complexity as standard PCA, or kernel PCA,  
and 
run much faster than existing methods for fair PCA 
based on semidefinite programming or manifold optimization, while achieving similar~results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new algorithm for fair representation learning, specifically within the framework of decomposition methods where fairness constraints are imposed over the learned components. The authors address two cases: Where fairness regularization is based on the covariance between the projected data and the sensitive attribute. And, where regularization is based on the Hilbert-Schmidt Independence Criterion (HSIC).
The paper also conducts a thorough evaluation of the resulting representations.

### Strengths
* The paper is well-written with a clear introduction.
* Fair representation is an important problem, particularly in high-dimensional data where many representation learning methods fail.
* The paper utilization of a regularization parameter, that seems to effectively explores the accuracy-fairness front , is a big advantage.
* The method is simple and straightforward.
* The inclusion of the Equality of Odds constraint is a valuable addition.
* The experiments are comprehensive and include evaluation of the representation itself.

### Weaknesses
- My main concern is with the empirical results and the settings. 
  - The learned fair representations in the downstream tasks are evaluated using different target models but are not compared with other baseline methods, which makes the effectiveness of the proposed methods less convincing. The authors need to demonstrate that through PLS, the learned fair representations can achieve better accuracy, fairness, or efficiency compared to other methods (for example, using VAE or other disentanglement methods). Specifically, the lack of direct comparison against methods designed for fair representation learning, such as adversarial training or reweighting techniques, makes it difficult to assess the true value of the proposed approach. The evaluation should include metrics that quantify both the utility of the representation (e.g., classification accuracy) and its fairness (e.g., demographic parity difference or equal opportunity difference) across various sensitive attributes.
  - The chosen datasets are all tabular, and the dimensionality is not very high. Therefore, I am concerned about the proposed method’s performance with high-dimensional data (e.g., image data). The method's reliance on eigenvector computations in each iteration raises concerns about its scalability to high-dimensional feature spaces, which are common in image and text data. It's unclear how the method would perform with datasets that have thousands or millions of features, and the computational cost could become prohibitive.
- The motivation for the proposed method is weak. Although incorporating fairness constraints into PLS is a novel attempt, the justification for using PLS is not strong. In the introduction (lines 121-141), the authors introduce existing fair representation learning methods but do not sufficiently justify the benefits of using PLS. The only comparison made is with PCA, stating that PLS-built features are more accurate than PCA components, which is not enough to fully support the choice of PLS. The authors need to provide a more compelling argument for why PLS is a suitable choice for fair representation learning compared to other dimensionality reduction techniques or methods that directly optimize for fairness, such as those based on information theory or causal inference.
- In the paragraph (lines 274-283), the authors explain why Fair PLS cannot be formulated in closed form. As a result, the algorithm requires iterations to solve for the weight $w_h$ . In each iteration,  it requires the re-computation of the eigenvectors, when the dimension is large, this would increase computation cost and decrease the efficiency. This iterative process, coupled with the need to recompute eigenvectors, could lead to significant computational overhead, especially when dealing with large datasets or high-dimensional feature spaces. The paper lacks a detailed analysis of the computational complexity of the proposed method and how it scales with increasing data size and dimensionality.

### Questions
* In lines 331-333, optimization details are missing. Additionally, it's unclear if this is the algorithm used in the evaluation section

* Does the data contain any preprocessing except normalization?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies fair representation learning. Specifically, it combines Partial Least Squares (PLS) with an additional fair criteria that characterizes the covariance dependence between the new data representation and the the demographic attribute $S$. The linear and non-linear cases are both considered. Finally, the proposed algorithm is tested on different datasets and performs better than the standard fair PCA method.

### Strengths
1. The paper is well-written and easy to follow, with a clearly presented mathematical part. 
2. Interpretations and general thoughts are provided. 
3. A possible relation to fairness in LLM is discussed.

### Weaknesses
Although I appreciate the presentation of the work, I have the following concerns.
1. The empirical comparison to previous fair PCA is only tested on one dataset (Adult Income) and provided in the Appendix. It's not convincing the proposed work will outperform previous work in most cases.
2. Although possible application to fairness in LLM is discussed, it's rather superficial. Unless you have done experiments on LLM to measure fairness, I do not suggest this as a separate section in the main paper. 
3. The experiments are conducted on simple tabular data. Will it be possible to test on more complex and high-dimensional datasets because you are considering dimension reduction? 
4. Several related works in fair representation learning are missing for discussion [1,2,3]. 

[1] Kim, Jin-Young, and Sung-Bae Cho. "Fair representation for safe artificial intelligence via adversarial learning of unbiased information bottleneck." _SafeAI@ AAAI_. 2020.

[2] Shui, Changjian, et al. "Fair representation learning through implicit path alignment." _International Conference on Machine Learning_. PMLR, 2022.

[3] Zamani, Amirreza, Borja Rodríguez-Gálvez, and Mikael Skoglund. "On information theoretic fairness: Compressed representations with perfect demographic parity." _arXiv preprint arXiv:2408.13168_ (2024).

### Questions
See previous section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method for fair representation learning based on Partial Least Squares (PLS). The proposed approach employs supervised learning, requiring input data along with sensitive attributes $S$ and target label $Y$. The goal is to project the input data into a $k$-dimensional subspace that maximizes the covariance with $Y$ while minimizing the covariance with $S$. The method is implemented as a linear projection optimized via gradient descent and is further extended to non-linear kernel projections using Hilbert-Schmidt Independence Criterion (HSIC).

### Strengths
This paper studies an important problem of fair representation learning.

### Weaknesses
I have the following questions and concerns regarding the contribution and evaluation of the work:

1. **Motivation for PLS-based Framework:** It would be helpful for the authors to clarify the motivation behind selecting PLS as the foundation for their framework. There are various types of approaches for fair representation learning, such as adversarial learning [1], disentanglement [2], and distribution alignment [3]. What are the specific advantages of a PLS-based approach in comparison to these methods?

2. **Applicability and Practical Constraints:** The proposed method requires annotations for both the target label $Y$ and the sensitive attribute $S$, which can limit practical applications. Compared to existing approaches in unsupervised fair representation learning or those that do not rely on sensitive attribute annotations (such as [4]), it would be beneficial for the authors to further clarify the unique advantages of their method, potentially in terms of efficiency, theoretical guarantees, or effectiveness.

3. **Evaluation and Comparison:** The evaluation of the proposed method is based on relatively small datasets and lacks comparisons with related approaches. The current experiments seem to focus on applying the learned representations to various classifiers (like in Figure 1) rather than comparing with alternative representation learning methods. The lack of thorough evaluation and comparison makes it challenging to validate the effectiveness of the proposed method. 

4. **Extension to LLMs:** It's helpful that the authors discussed in Section 4.3 about extending their method to Large Language Models (LLMs), where their method could decompose the CLS-embedding from a transformer encoder for fairness constraints. However, it's suggested that the authors could provide a more detailed discussion (with math formulation) in this section and conduct experiments to validate this extension.

5. **Coupling Issue in Fair Representation Learning:** Fair representation learning often involves a trade-off between fairness constraints and downstream task performance. It would be insightful if the authors could discuss how their method might address or mitigate this issue.

6. (Minor point on notations) In the previous context, the authors use x to refer to the input data, but in Section 4.3, x refers to the transformed data in the latent space. The authors may use a different symbol to avoid confusion.


[1] Madras, David, et al. "Learning adversarially fair and transferable representations." International Conference on Machine Learning. PMLR, 2018.

[2] Balunovic, Mislav, Anian Ruoss, and Martin Vechev. "Fair Normalizing Flows." International Conference on Learning Representations. 2022.

[3] Creager, Elliot, et al. "Flexibly fair representation learning by disentanglement." International conference on machine learning. PMLR, 2019.

[4] Chai, Junyi, and Xiaoqian Wang. "Self-supervised fair representation learning without demographics." Advances in Neural Information Processing Systems 35 (2022): 27100-27113.

### Questions
It would be helpful if the authors could clarify my above questions regarding the contribution and evaluation of the work.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a fair representation learning framework by utilizing the technique of PLS with fairness constraint. It leverages the inherent benefits of PLS, such as extracting useful information from the original features in a lower-dimensional space. The paper provides two versions of the framework: linear and non-linear (the latter by applying reproducing kernels, making it more suitable for feature spaces of arbitrarily large dimensionality).

### Strengths
The logic of the paper is clear, and the notations are well-defined. The proposed method is solid in its mathematical formulation. The authors incorporate two different fairness constraints (demographic parity and equalized odds) into the proposed method. The extension of the method to LLMs (though briefly covered), which overcomes the limitations of transforming the linear layer with SVD, is inspiring.

### Weaknesses
- My main concern is with the empirical results and the settings. 
  - The learned fair representations in the downstream tasks are evaluated using different target models but are not compared with other baseline methods, which makes the effectiveness of the proposed methods less convincing. The authors need to demonstrate that through PLS, the learned fair representations can achieve better accuracy, fairness, or efficiency compared to other methods (for example, using VAE or other disentanglement methods).
  - The chosen datasets are all tabular, and the dimensionality is not very high. Therefore, I am concerned about the proposed method’s performance with high-dimensional data (e.g., image data).
- The motivation for the proposed method is weak. Although incorporating fairness constraints into PLS is a novel attempt, the justification for using PLS is not strong. In the introduction (lines 121-141), the authors introduce existing fair representation learning methods but do not sufficiently justify the benefits of using PLS. The only comparison made is with PCA, stating that PLS-built features are more accurate than PCA components, which is not enough to fully support the choice of PLS.
- In the paragraph (lines 274-283), the authors explain why Fair PLS cannot be formulated in closed form. As a result, the algorithm requires iterations to solve for the weight $w_h$ . In each iteration,  it requires the re-computation of the eigenvectors, when the dimension is large, this would increase computation cost and decrease the efficiency.

### Questions
Is there any convergence issue or analysis with the proposed method when the original data has high dimensionality? For example, during the optimization iterations, could the method get stuck in local minima, leading to convergence problems?

### Soundness
2

### Presentation
3

### Contribution
2
