# Higher Order Transformers: Efficient Attention Mechanism for Tensor Structured Data

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
Transformers are now ubiquitous for sequence modeling tasks, but their extension to multi-dimensional data remains a challenge due the to quadratic cost of the attention mechanism.  In this paper, we propose Higher-Order Transformers (HOT), a novel architecture designed to efficiently process data with more than two axes, i.e. higher order tensors. 
To address the computational challenges associated with high-order tensor attention, we introduce a novel Kronecker factorized attention mechanism that reduces the attention cost to quadratic in each axis' dimension, rather than quadratic in the total size of the input tensor. To further enhance efficiency, HOT leverages kernelized attention, reducing the complexity to linear. This strategy maintains the model's expressiveness while enabling scalable attention computation.
We validate the effectiveness of HOT on two high-dimensional tasks, including long-term time series forecasting, and 3D medical image classification. Experimental results demonstrate that HOT achieves competitive performance while significantly improving computational efficiency, showcasing its potential for tackling a wide range of complex, multi-dimensional data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a new transformer-based model, i.e., Higher-Order Transformers (HOT) which can efficiently process data with more than two axes (i.e., higher order tensors). In addition, the authors propose a novel Kronecker factorized attention mechanism that reduces the attention cost and provide theoretical proof of Kronecker decomposition. The experiments over multivariate time series data and 3D medical images are straightforward and clear.

### Strengths
+ The paper is clear and well written. It is easy to follow and presents a concise idea of Kronecker factorized attention mechanism based on Kronecker decomposition. 
+ The paper also do a good job in describing existing research/roadmap in transformer-based models.
+ For multivariate forecasting tasks, the proposed HOT model always outperforms baselines.

### Weaknesses
 - For multivariate forecasting tasks, the model's effectiveness is assessed only through MAE and MSE. Can the authors also report other metrics, e.g., MAPE? In addition, I am curious about the confidence intervals for prediction of the HOT model compared to other baselines.
- Why Kronecker decomposition: there are also other higher-order structure decomposition approach, e.g., CP decomposition, Tucker decomposition, etc. I wonder if the authors have compared Kronecker decomposition with other tensor decomposition methods?
- Improvements are minor: although the HOT model achieves the best prediction accuracy across all datasets for multivariate forecasting tasks, improvements are not significant. Also, for 3D medical images, the HOT model's performances are less competitive. 
- It would be helpful if the authors could conduct robust experimental comparisons, i.e., if the proposed Kronecker factorized attention mechanism can help improve model's robustness.

### Questions
See my questions from the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel Transformer architecture to extend traditional Transformers for processing higher-order data, while reducing the attention cost to quadratic in each axis' dimension and the complexity to linear.

### Strengths
* Considering the importance of higher-order data, designing specialized Transformer architectures for higher-order data is meaningful.

* The proposed Higher-Order Transformers (HOT) can efficiently capture essential cross-dimensional dependencies with lower complexity, thus overcoming the limitations of previous methods.

* The experimental results also support the superiority of the proposed HOT, both in effectiveness and efficiency.

### Weaknesses
 * Different form previous works which directly flatten the input tensor into a sequence, it's impossible for HOT to use the same architecture process data with different orders, thus limiting its scalability.

* Consideing the high-order feature of HOT, it's necessary to compare the model parameters with its baselines.

* Besides, it's also necessary to conduct more experiments to demonstrate the generality of the proposed method on various kinds of higher-order data, such as typical 2D image datasets and video dataset.

### Questions
Please see the **weaknesses**.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposed a transformer architecture to efficiently deal with higher-order structure data.

### Strengths
1. The research question is important since the attention operator is very computationally expensive on higher-order data.
2. The usage of Kronecker to factorize attention is sound.
3. Empirical studies demonstrate the effectiveness of proposed work on higher-order data.

### Weaknesses
1. The major problem is the novelty. This work is essentially about attention instead of transformer. The Kronecker factorization is applied to attention, which is part of the transformer architecture. Actually, applying Kronecker factorization to attention on higher-order data has been explored in [1]. Currently, the novelty is very marginal from my current understanding. It is important for authors to demonstrate the distinct contributions from [1].

2. Since the proposed attention is not necessarily integrated with the transformer architecture, it would be better to show its effectiveness in other architectures, such as Attention U-Net [2].

3. [Added after discussion with authors] The evaluation is actually conducted on 1D data. The time series data is reshaped into 2D to mimic higher-order data. However, this does not make sense since there is no locality in the feature dimension of 1D data. It does not make sense to apply this on 1D data although it is mathematically correct. To improve, the evaluation on real 2D and 3D data is preferred instead of using 1D data.

### Questions
Please see weakness.

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
The authors propose a high-order Transformer (HOT) for high-order tensor input. The authors apply Kronecker tensor decomposition and kernel attention in Performer to propose a novel Kronecker factorized attention. The experimental results in time-series forecasting and 3D medical image classification illustrate the efficient of HOT.

### Strengths
1. The authors skillfully perform tensor operations.

### Weaknesses
1. This paper demonstrates a limited degree of innovation. The proposed methodology in this paper is merely based on Kronecker tensor decomposition [1] and kernel attention [2].

2. The paper lacks a thorough analysis of the trade-offs between computational complexity and precision when using low-rank approximations via Kronecker decomposition. The authors need to provide more analysis on how the choice of rank R or specific kernels impacts performance, especially in the context of different datasets and application needs. The practical guidance for choosing these parameters is insufficient.

3. The paper does not provide sufficient insight into how the proposed method maintains low complexity when handling datasets with more than 3 dimensions. The authors need to demonstrate how the model scales with increasing dimensionality and whether the Kronecker decomposition remains effective as the dimensionality increases. The current analysis is limited to a general complexity statement without a detailed breakdown of the computational bottlenecks.

### Questions
1. How does the use of low-rank approximation via Kronecker decomposition in Section 4.2 impact the trade-off between computational complexity and precision? The authors need to provide more analysis on this and offer guidelines for choosing the appropriate rank R or kernels to help practitioners adapt the method to different datasets and needs.

2. The authors need to provide more insights or proof on how HOT maintains low complexity when handling datasets with more than 3 dimensions. It would be helpful to understand how the model scales and whether the current complexity reduction techniques, like Kronecker decomposition remain effective as the dimensionality increases.

### Soundness
2

### Presentation
2

### Contribution
1
