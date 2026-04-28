# MRFNet: Multi-Receptive Field  Network for Multivariate Time-Series Prediction

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Time series forecasting is a critical topic in machine learning. Although existing deep learning methods have demonstrated outstanding performance and currently dominate this field, the latest state-of-the-art (SOTA) models are increasingly encountering the same limitations: the blockneck of performance. We believe this convergence is due to these models being based on the same mathematical foundations. To address this issue, we draw inspiration from the universal approximation theorem (UAT) and show that most commonly used deep learning models for time series forecasting are specific implementations of UAT. Based on UAT theory and the characteristics of time series data, we propose a new forecasting model called the Multi-Receptive Field Network (MRFNet). This architecture integrates linear, sparse matrix, convolutional, and Fourier transform modules, resulting in an interpretable model with multiple receptive fields that can capture both global and local information. The MRFNet model has been tested extensively on several popular time series forecasting datasets and has achieved superior results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces MRFNET — a new architecture for long sequence time series forecasting, using a mixture of linear, sparse matrix, convolutional, and Fourier blocks. They also express CNNs and transformers in matrix vector form, providing a more direct link to the universal approximation theorem.

### Strengths
While transformer based forecasting models have demonstrated large improvements in Long Sequence Time Series Forecasting (LSTF) tasks, improvements have largely been empirical in nature — with little formal analysis to understand the inner workings of the models.

### Weaknesses
While transformer based forecasting models have demonstrated large improvements in Long Sequence Time Series Forecasting (LSTF) tasks, improvements have largely been empirical in nature — with little formal analysis to understand the inner workings of the models.

However, I do have some fundamental concerns surrounding the motivations of the paper itself.

Firstly, while universal approximation is the cornerstone of function approximation and that building blocks (FFNs, CNNs, transformers) can be expressed in UAT form -- the inductive biases provided through architecture (and how they are aligned with data characteristics) can make a big impact on performance. This has been seen frequently outside of time series datasets (e.g. transformers for LLMs, CNNs for computer vision), and also in the way deep neural networks have evolved beyond simple MLPs (which are also universal function approximators) . As such, the conjecture that performance bottlenecks are due to limitations under UAT would require a lot more evidence than supplied in the paper.

Secondly, assuming this is the case, it is not immediately clear how/why the architecture allows MRFNET to overcome the performance limitations described. Furthermore, the building blocks described have all been utilised in other forecasting architectures, so it would also be important to describe why the current configuration is expected to improve performance.

### Questions
1. Is MRFNet a UAT based, and if not how is it different and how do differences result in performance improvements?
2. Are there any concrete examples of a purely cnn-based time series forecasting model bottle necking at the same performance as a similar transformer-based model? Would we expect the performance of a simple CNN/naive Transformer model to match PatchTST?
3. How significant are performance improvements over PatchTST (e.g. confidence intervals around improvements)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
## Summary of the Paper
The paper introduces MRFNet, a multivariate time-series forecasting model designed to capture patterns by integrating four components: linear, convolutional, sparse matrix, and Fourier transform blocks.

### Strengths
## Strong Points
1.	**Clear Presentation**
The paper is well-organized, making it easy to follow the transition from problem statement to proposed solution. 
2.	**Introduction of UAT to Time-Series Forecasting**
The application of the Universal Approximation Theorem (UAT) in time-series forecasting adds an interesting theoretical perspective.

### Weaknesses
## Weak Points and Concerns
1.	**Insufficient Experiment Details and Missing State-of-the-Art References (Ref 1 and Ref 2 below)**
The experimental setup lacks details, such as the size of weight matrices, learning rates, training epochs, and batch sizes, which are essential for reproducibility. This missing information makes it difficult to replicate the experiments or understand how hyperparameter choices might affect the results. Additionally, comparisons with recent state-of-the-art methods are absent. 
The improvement seems marginal. 

Ref 1 (ICML 2024): SparseTSF: Modeling Long-term Time Series Forecasting with 1k Parameters 
https://arxiv.org/pdf/2405.00946
Ref2 (ICLR 2024) :CARD: Channel Aligned Robust Blend Transformer for Time Series Forecasting
https://openreview.net/pdf?id=MJksrOhurE

2.	**Lack of Motivation for Selecting the Four Specific Blocks**
While MRFNet includes linear, convolutional, sparse matrix, and Fourier transform modules, there is no clear justification of using these four components over others. 

3.	**Limited Theoretical Justification for UAT Application**
Although UAT is referenced as a motivating factor, the paper does not fully explain how each component in MRFNet contributes to leveraging UAT in time-series forecasting. This weakens the theoretical foundation.

### Questions
## Questions for Authors
1.	Can you provide more details on the experiment setup, specifically weight matrix sizes, learning rates, and training epochs?
2.	What motivated the selection of these four specific modules? Could alternative components potentially yield similar or improved results?
3.	How does MRFNet compare with recent state-of-the-art methods in the references?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
MRFNet is a novel multivariable time series prediction model, which is designed based on universal approximation theorem (UAT) and integrates linear, sparse matrix, convolution and Fourier transform modules. The model performs well on multiple popular data sets and achieves better prediction performance. The study also found that current state-of-the-art time series prediction models tend to have similar performance bottlenecks because they share the same mathematical foundation. MRFNet provides a new perspective to understand and improve time series forecasting by capturing both global and local information.

### Strengths
The MRFNet model combines multiple deep learning techniques, including linear, convolution, and Fourier transform, to accommodate the complexity of time series data. The design is based on the general approximation theorem, which ensures that the model can capture global and local information and improve the prediction accuracy.

### Weaknesses
MRFNet's module consolidation, while enhancing model functionality, is limited in innovation and relies primarily on a portfolio of existing technologies. This increases the complexity of the model.

### Questions
1. Capturing global and local features seems to be widely studied, so please identify the innovations in this article
[1] Dai, T., Wu, B., Liu, P., Li, N., Bao, J., Jiang, Y., & Xia, S. T. (2024). Periodicity decoupling framework for long-term series forecasting. In The Twelfth International Conference on Learning Representations.
2.MRFNet has limited performance improvements on some datasets. Do authors think this is mainly due to data characteristics or limitations of the model itself?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is inspired by the universal approximation theorem (UAT) to solve the time-series forecasting problem. It shows that most time-series forecasting models can be expressed in the matrix-vector form thus satisfying the UAT. It also proposes the multi-receptive field network (MRFNet) for time-series forecasting problems. MRFNet consists of four blocks linear, sparse matrix, convolutional and Fourier transform blocks claimed to be interpretable and to capture both global and local information.

### Strengths
1) The problem of time-series forecasting is important because it has many real-world applications.
2) the concept of universal approximation theorem is theoretically sound.

### Weaknesses
Motivation

motivation of this work is rather unclear. It does not point out a specific issue to be addressed in the paper. Rather, the use of UAT is a common issue. In addition, please clarify the fact that neural network is a universal approximator. On the other hand, there is no figures at all justifying the motivation of this paper.

Literature Survey

literature review is rather outdated. There are more recent works uncovered in the literature survey.

Novelty

The novelty of this work might be rather limited because the UAT2LLM has proved the uat of the transformer network.

Experiments

1) Numerical results are not convincing. The performance differences are very small such that it is not conclusive to say that the MRFNET is better than other methods.

2) Statistical tests need to be conducted to understand whether the performance differences are statistically significant or not.

3) Complexity analysis is absent. It is interesting to know the complexity of the proposed method compared to SOTA algorithms.

Conclusion

limitation of this method should be discussed in the conclusion section.

### Questions
1) I wonder the complexity of the proposed method. 
2) I wonder the novelty of this paper provided that the UAT of various modules of neural networks have existed in the literature.

### Soundness
3

### Presentation
2

### Contribution
2
