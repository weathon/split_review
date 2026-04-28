# Large-Scale Training Data Attribution with Efficient Influence Functions

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 8, 3, 3

## Abstract
Training data attribution (TDA) quantifies the contribution of individual training examples to model predictions, enabling a range of applications such as data curation, data citation, and model debugging. However, applying existing TDA methods to recent large models and training datasets has been largely limited by prohibitive compute and memory costs. In this work, we focus on influence functions, a popular gradient-based TDA method, and significantly improve its scalability with an efficient gradient projection strategy called LoGra that leverages the gradient structure in backpropagation. We then provide a theoretical motivation of gradient projection approaches to influence functions to promote trust in the TDA process. Lastly, we lower the barrier to implementing TDA systems by introducing LogIX, a software package that can transform existing training code into TDA code with minimal effort. In our TDA experiments, LoGra achieves competitive accuracy against more expensive baselines while showing up to 6,500x improvement in throughput and 5x reduction in GPU memory usage when applied to Llama3-8B-Instruct and the 1B-token dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Training data attribution (TDA) attempt to quantify the contribution of training points to the prediction obtained using a test point. However, these methods do not scale well for large models and datasets. The authors propose an efficient gradient projection strategy that can be adopted with gradient-based TDA methods to scale up these approaches. They show improvements in throughput, reduction in memory usage and applicable to multi-bilion parameter LLMs.

### Strengths
The authors of this paper have really found one of the central problems in TDA methods and addressed them in a neat way. The paper provides sufficient background for gradient-based TDA methods and is really well-written. The key trick seems to be taking the projection operator from gradient to activations and this reduces the memory and storage complexity tremendously.

The authors have also performed several clearly justified experiments with MLP, ResNet and GPT2 models. The results are in line with the original claims - EKFAC seems to be the only method that is close or outperforms the proposed methods but has much lower throughput and higher memory usage during influence computation (from Table 1).

### Weaknesses
I just have a few comments for the authors to consider:

1. The order complexities listed in sections 2 and 3 can be hard to process since the constants are hidden. It is not clear if I can compare two order complexities directly. Is there any way to make this more concrete and easily comparable? For instance, providing a breakdown of the constants in terms of model parameters, batch size, and sequence length would be beneficial. This would allow for a more precise understanding of the practical implications of the theoretical complexities.
2. I would recommend adding compute and memory complexity for the methods compared in Figure 4 to get a more complete picture. Specifically, it would be helpful to see a detailed breakdown of the FLOPs and memory requirements for each method, not just the overall runtime. This should include the cost of both the forward and backward passes, as well as any additional overhead.
3. Please note why quantitative evaluations are not possible for accuracy measures in section 4.2. It's not immediately clear why retraining is necessary for accuracy evaluation. Could the authors clarify if there are alternative evaluation strategies that do not require retraining, such as using held-out datasets or proxy tasks?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a method to scale up the computation of influence functions for large models such as LLMs.
The key idea is to use the gradient structure in backpropagation to perform effective gradient projection without materializing the gradient or projection matrices.
This idea is supported by its link to the effect of the damping factor that is commonly used in influence functions computation: 
the projection can be viewed as a hard way to perform dumping that zeros out influence computations to components in the projection
matrix.
Experiments show that the proposed method can scale up the computation of influence functions for large models, over ~7000x throughput improvement compared to EKFAC while having acceptable accuracy loss and a trade-off in storage (40x more space needed).
In addition, the author(s) also develop a plug-and-play Python package for this method that can easily inject into existing LLMs.

### Strengths
1. The paper addresses a significant practical challenge (scalability) in understanding large language models through influence functions
2. The technical innovation (LoGra) is well-motivated and theoretically grounded by connecting to the damping effect in influence functions
3. Impressive empirical results showing major efficiency gains (7000x throughput) while maintaining accuracy
4. Strong practicality focus with the development of LoGix software that can be easily integrated into existing training pipelines
5. Comprehensive experiments including both quantitative metrics and qualitative analysis of the results

### Weaknesses
1. The failure cases in qualitative analysis (especially with Pythia-1.4B) could be analyzed more thoroughly to better understand the limitations (e.g. is it because of the projection or not). Specifically, the analysis should investigate whether the observed failures are due to the projection step itself, or if they stem from the inherent limitations of influence functions when applied to models with specific architectural or training characteristics. For instance, it would be beneficial to examine the distribution of gradient components before and after projection to quantify the information loss. A more detailed analysis of the specific types of examples where the method fails could also provide insights into the limitations of the approach. Are these examples related to specific token sequences, rare events, or other identifiable patterns?
2. While the theoretical connection to damping is interesting, its practical implications could be explained more clearly. The paper would benefit from a more detailed discussion on how the theoretical connection to damping translates into practical guidance for choosing projection strategies. For example, how does the choice of projection dimension affect the effective damping and what are the trade-offs involved? A more thorough explanation of how the projection affects the influence function calculation would be helpful. It would also be useful to discuss whether the damping effect is uniform across different parts of the model or if it is more pronounced in certain layers or parameter groups.
3. The storage requirement tradeoff (3.5TB for LoGra vs 89GB for EKFAC) deserves more discussion on practical implications. The paper should include a more detailed discussion of the practical implications of the increased storage requirements. For example, what are the implications for researchers with limited storage resources? How does the storage cost scale with model size and how does this compare to the computational cost savings? A more thorough analysis of the cost-benefit trade-off is needed, including the cost of storage, data transfer, and the potential impact on accessibility for different research groups.

### Questions
1. Could you elaborate on why the method performs notably worse on Pythia-1.4B compared to other models? What characteristics of the model might be responsible?
2. The storage requirements are significantly higher for LoGra compared to EKFAC. Could you discuss this tradeoff more explicitly in the draft?
3. The theoretical connection between gradient projection and damping suggests an interpretation of what information is being preserved/discarded. Could this insight be used to make better choices about projection strategies or explain the failure cases?

Overall, the paper makes a clear and significant contribution to scaling up influence functions for large language models, with impressive empirical results and strong practical focus. 
The theoretical grounding adds depth while the open-source implementation increases immediate impact potential. 
Despite some areas that could use additional analysis, this represents is progress in making influence functions practical for modern deep learning.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studies training attribution using influence functions. The authors employ a popular approximation of Gauss-Newton-Hessian called Kronecker Approximate Factorization.

Firstly, the authors introduce the method LoGra, that calculates projected training gradients, with twofold advantages. Firstly, thanks to the Kroneker structure, the projection is orders cheaper to calculate than the usual "dense" projectors. Secondly, the lowered dimension of the gradient allows one to precompute them and store them in a disk. Once the training gradients are precomputed, one can calculate the influences for a given test point in real time.

The second major contribution is a reproducible implementation of LoGra using pytorch's forward/backward hooks. Their codebase allows easy incorporating of gradient projections with existing models.

The authors address the important question of scalability of influence functions and make their application more accessible. Below I mention a few issues.

1. While reading the paper, I often found myself having to refer to the previous papers to clarify some of the formulas. I think an average reader would benefit from self-contained notation: what is Kronecker product, what is Kronecker product of vectors, background for K-FAC approximation of the Hessian, and what is Hessian itself (the Gauss-Newton one).

2. The details of Hessian calculation have been omitted. I do not understand how this calculation was performed, in particular, how do the authors manage to calculate the gradients token-wise.

3. In equation (5), should not $x_t \otimes D x_o $ be a matrix? However, the left-hand side (LHS) is a vector. The same applies to Equation (6). I believe everything would be correct if the vec(⋅) operation were removed—am I right?

4. I believe there are some limitations in the interpretation of Lemma 1 that could be mentioned. First, Assumption 1 mentions a 'prompt,' so I assume the authors had language modeling in mind for this result. In that case, g_{tr} is the mean over tokens in the training set, and g_{te} is the mean over generated tokens. The assumption that they follow the same distribution is impractical, as training and generated texts are typically very different. Additionally, the variance is calculated per token, while g_{tr} and g_{te} are both averages over multiple dependent tokens. The second issue I see may be debatable. The 'cut-off' arises due to the normalization $e_j \mapsto \sqrt{\lambda_j} e_j$. Without this normalization, the cut-off would be the opposite, the top eigenvectors would receive smaller coefficients. Why is one interpretation better than the other? I understand that the motivation was to normalize the coefficients $E c_{j}^{2} = 1$. However, I want to point out that this does not imply all $c_{j}$ are bounded. For example, distribution of c_j could have a heavy-tails. Otherwise, this would mean that the gradients lie in a low-dimensional subspace. As noted in [1] at the end of Section 4.1, this is not always the case, and when it is, it means that the training is slow. See also section 5.5 in [2].


[1] An Investigation into Neural Net Optimization via Hessian Eigenvalue Density

[2] Efficient Sketches for Training Data Attribution and Studying the Loss Landscape https://arxiv.org/pdf/2402.03994

### Strengths
- reproducible codebase
- extensive experiments

### Weaknesses
 - lack of details regarding computation of Hessian
- Lemma 1 has limitations
- choice of k was not addressed (projection dimension)
- While reading the paper, I often found myself having to refer to the previous papers to clarify some of the formulas. I think an average reader would benefit from self-contained notation: what is Kronecker product, what is Kronecker product of vectors, background for K-FAC approximation of the Hessian, and what is Hessian itself (the Gauss-Newton one).

- The details of Hessian calculation have been omitted. I do not understand how this calculation was performed, in particular, how do the authors manage to calculate the gradients token-wise.

- In equation (5), should not $x_t \otimes D x_o $ be a matrix? However, the left-hand side (LHS) is a vector. The same applies to Equation (6). I believe everything would be correct if the vec(⋅) operation were removed—am I right?

- I believe there are some limitations in the interpretation of Lemma 1 that could be mentioned. First, Assumption 1 mentions a 'prompt,' so I assume the authors had language modeling in mind for this result. In that case, g_{tr} is the mean over tokens in the training set, and g_{te} is the mean over generated tokens. The assumption that they follow the same distribution is impractical, as training and generated texts are typically very different. Additionally, the variance is calculated per token, while g_{tr} and g_{te} are both averages over multiple dependent tokens. The second issue I see may be debatable. The 'cut-off' arises due to the normalization $e_j \mapsto \sqrt{\lambda_j} e_j$. Without this normalization, the cut-off would be the opposite, the top eigenvectors would receive smaller coefficients. Why is one interpretation better than the other? I understand that the motivation was to normalize the coefficients $E c_{j}^{2} = 1$. However, I want to point out that this does not imply all $c_{j}$ are bounded. For example, distribution of c_j could have a heavy-tails. Otherwise, this would mean that the gradients lie in a low-dimensional subspace. As noted in [1] at the end of Section 4.1, this is not always the case, and when it is, it means that the training is slow. See also section 5.5 in [2].

### Questions
How does one chose the projection dimension in practice? What was it in the experiments?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel large-scale training data attribution method called LOGRA (Low-Rank Gradient Approximation), which aims to enhance the efficiency of influence functions on large models and datasets. The core contribution of the paper is the use of low-rank projections on input and output activations, significantly reducing the computational complexity and memory overhead of Kronecker product calculations. By performing low-rank projections directly on input and output activations, LOGRA effectively approximates the weight gradients, making influence functions scalable to larger models and datasets. To validate LOGRA's performance, the authors also introduce an open-source software package, LOGIX, and conduct experiments on models like GPT2-XL, Pythia-1.4B, and Llama3-8B-Instruct, demonstrating that LOGRA outperforms existing methods in terms of memory and computational efficiency.

### Strengths
- **Contribution**: The paper introduces an innovative low-rank gradient approximation method, LOGRA, which applies low-rank projections to input and output activations, significantly improving the efficiency of influence functions on large models and datasets. LOGRA’s approach is novel, not only reducing the complexity of Kronecker products but also broadening the applicability of influence functions through low-rank projections. Compared to existing influence function methods like EKFAC and Arnoldi IF, LOGRA's strategy in gradient computation is distinct, enabling more efficient training data attribution on large models and datasets.
- **Comprehensive Experiments**: The authors conduct extensive experiments across various large models, including GPT2-XL, Pythia-1.4B, and Llama3-8B-Instruct. These experiments cover different model scales and datasets, thoroughly demonstrating LOGRA’s advantages in computational and memory efficiency while validating its reliability in influence function attribution accuracy. The experimental design is well-structured, and the results are clear, providing strong evidence of LOGRA's effectiveness.

### Weaknesses
### Weaknesses
- **Limited Applicability to Specific Layer Types**: LOGRA’s low-rank projection mainly applies to linear layers and QKV-generating linear layers, while its effectiveness is limited in other types of layers, such as convolutional layers. It is recommended to explore how the low-rank approximation strategy could be extended to a wider variety of layer types, improving LOGRA's applicability and performance across different models. While the authors mention that most neural network layers can be reduced to matrix multiplication, this does not address the nuances of layers with learnable parameters, such as normalization layers (e.g., LayerNorm and BatchNorm), recurrent layers (e.g., LSTM and GRU), and sparsely connected fully connected layers. For convolutional layers, a more detailed explanation of how LOGRA leverages the unique structural properties, such as sparse connections and shared weights, would be beneficial. Similarly, for normalization layers with learnable scaling and shifting parameters, it would be helpful to clarify if LOGRA can effectively handle them, given their typically small parameter sizes. For recurrent layers, due to the complexity and interdependence of weight matrices, discussing whether LOGRA requires any specialized adaptations, such as block-wise handling, would strengthen the analysis. Sparse fully connected layers, which have unique weight matrix structures, also merit consideration.
- **Potential Impact of Low-Rank Projections on Attribution Accuracy**: The paper lacks a detailed discussion of the potential negative impact of low-rank projections on attribution accuracy, as well as how to balance efficiency with accuracy. It is recommended to include a quantitative analysis of the approximation errors under different low-rank dimensions, which would help readers better understand how LOGRA’s attribution accuracy changes with varying ranks. While the authors claim comparable performance to EKFAC, a more detailed analysis of the trade-offs between Figure 4 and Table 1 metrics across varying projection ranks is needed.
- **Lack of Discussion on Dimensionality Reduction Efficiency**: LOGRA employs PCA and random projection for dimensionality reduction, yet the paper does not discuss the efficiency challenges associated with these methods in detail. While PCA effectively preserves information, its covariance matrix computation and eigen-decomposition can be computationally intensive in high-dimensional scenarios, potentially impacting LOGRA’s overall runtime efficiency. On the other hand, random projection is faster but often requires ensemble techniques to mitigate randomness, introducing additional computational overhead. It is recommended to include a discussion on the efficiency trade-offs of these methods to help readers better understand LOGRA's runtime considerations.

### Questions
### Questions
1. **How can LOGRA's applicability be extended to cover more types of layers?**

2. **How does low-rank projection impact attribution accuracy, and can it be quantified?**

3. **Could you offer the running time and more technology details of PCA and random projection?**

### Soundness
3

### Presentation
1

### Contribution
3
