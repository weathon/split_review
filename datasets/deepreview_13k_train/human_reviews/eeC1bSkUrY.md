# FedPS: Federated data Preprocessing via aggregated Statistics

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Data preprocessing is a crucial step in machine learning that significantly influences model accuracy and performance. In Federated Learning (FL), where multiple entities collaboratively train a model using decentralized data, the importance of preprocessing is often overlooked. This is particularly true in Non-IID settings, where clients hold heterogeneous datasets, requiring aggregated parameter estimates to perform consistent data preprocessing. In this paper, we introduce FedPS, a comprehensive suite of tools for federated data preprocessing. FedPS leverages aggregated statistics, data sketching, and federated machine learning models to address the challenges posed by distributed and diverse datasets in FL. Additionally, we resolve key numerical issues in power transforms by improving numerical stability through log-space computations and constrained optimization. Our proposed Federated Power Transform algorithm, based on Brent’s method, achieves superlinear convergence. Experimental results demonstrate the impact of effective data preprocessing in federated learning, highlighting FedPS as a versatile and robust solution compared to existing frameworks. The implementation of FedPS is open-sourced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the critical yet often overlooked aspect of data preprocessing in Federated Learning (FL), especially in scenarios where data is not identically distributed across clients. The main contribution of the paper is a toolset designed to improve data preprocessing in FL by utilizing combined statistics, data summarization, and federated machine learning techniques. A highlighted contribution is the solution to numerical challenges in power transformations, achieved through computations in logarithmic space and constrained optimization, resulting in a Federated Power Transform algorithm with rapid convergence, inspired by Brent’s method. The authors suggest that FedPS lays a strong groundwork for federated data pre-processing and plan to explore privacy-preserving methods to enhance its privacy features in future work.

### Strengths
- The paper provides a solution for a critical yet often overlooked aspect in Federated Learning.
- The code attached to the paper is overall well-written and of good quality, and I agree with the authors claim that FedPS lays a strong groundwork for federated data pre-processing.
- The paper is overall well-written, and the quality of presentation is good.

### Weaknesses
The main weakness of the paper is the lack of novelty. The paper is a description of a library for federated data pre-processing. Besides the library itself, the only part of the paper that could be considered as a significant contribution is the proposed algorithm for Federated Power-Transforms, which aims at addressing numerical issues in power transform through logarithmic transformation. While the use of logarithmic transformation to handle numerical instability is a known technique, the paper does not sufficiently demonstrate how the specific implementation and constrained optimization within the federated context offers a substantial advancement over existing methods. The paper also lacks a thorough comparison to alternative federated preprocessing techniques, making it difficult to assess the unique benefits of the proposed approach. Specifically, the paper does not explore the trade-offs between the proposed method and other techniques in terms of communication overhead, computational complexity, and convergence speed under various data distributions.

### Questions
N/A

### Soundness
3

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
The paper addresses the often overlooked aspect of data preprocessing in Federated Learning (FL). The authors introduce FedPS, a comprehensive suite of tools designed to enhance the preprocessing of decentralized data, which is essential for improving the accuracy and performance of machine learning models in federated settings.

The paper highlights the challenges posed by Non-IID data distributions across multiple clients, which complicate traditional preprocessing methods. To tackle these issues, the authors propose a novel Federated Power Transform algorithm that improves numerical stability through log-space computations and constrained optimization, achieving superlinear convergence rates.

Additionally, the paper presents experimental results that demonstrate the effectiveness of the proposed preprocessing techniques, showcasing improvements in model performance compared to existing frameworks. The paper contributes valuable insights and tools for enhancing data preprocessing in federated learning environments, emphasizing its importance for robust model training.

### Strengths
1. The paper introduces a robust methodology for federated data preprocessing through the FedPS tool, which leverages aggregated statistics and data sketching techniques.
2. The authors tackle numerical challenges associated with power transforms, which have been a limitation in previous research. By employing log-space computations and constrained optimization, the proposed Federated Power Transform algorithm enhances numerical stability and achieves superlinear convergence rates. 
3. The paper is well-structured and well-written, making it easy to understand.
4. The authors provide an open-source implementation of FedPS. The FedPS tool offers a flexible suite of preprocessing options with customizable parameters, allowing users to adapt the preprocessing techniques to their specific needs and data characteristics.

### Weaknesses
1. The scope of these experiments is limited in terms of the variety of datasets and models tested. very primitive models are tested, where models like resnet family etc should be experimentally tested with the proposed method. 
2. While the paper discusses the necessity of federated data preprocessing in non-IID settings, it does not include detailed experimental results that specifically demonstrate the performance of the proposed methods under non-IID conditions. The paper lacks a rigorous evaluation of how the proposed federated power transform handles varying degrees of non-IID data, such as label skew or feature distribution shifts across clients. This is crucial for demonstrating the practical applicability of the method in realistic federated learning scenarios.
3. A detailed privacy analysis of the preprocessing techniques implemented in FedPS is missing which is very important in a federated setting. The paper does not provide a formal privacy analysis, such as differential privacy guarantees, for the proposed preprocessing methods. This is a significant oversight, as federated learning inherently deals with sensitive user data, and the privacy implications of preprocessing steps must be carefully considered.
4. A more thorough literature review and comparison with federated pre-processing techniques is missing, like Federated One-Hot Encoding, Federated Feature Selection etc. The paper does not adequately position FedPS within the broader landscape of federated preprocessing techniques. Specifically, it lacks a detailed comparison with existing methods like federated one-hot encoding, federated feature selection, and other relevant approaches. This makes it difficult to assess the novelty and practical advantages of FedPS compared to existing solutions.

### Questions
1. Can you elaborate on how FedPS compares with the latest advancements in federated data preprocessing, particularly in terms of efficiency and privacy guarantees?
2. How does FedPS perform in non-IID data distributions among clients? 
3. Can you provide a detailed privacy analysis of the proposed methods in FedPS, and how do you plan to address this important aspect in the context of federated learning?

### Soundness
2

### Presentation
2

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
The paper considers a scenario in federated learning where data preprocessing needed at the clients. It describes some ways of collaboratively estimating some statistics that are needed in such data preprocessing operations. Some experimental results are shown with simple models with and without the scaling preprocessing.

### Strengths
- Data preprocessing is often useful in practice. The consideration of such preprocessing operations in a federated learning scenario can have some practical usefulness.

### Weaknesses
It is not clear what is the main contribution of this paper. It seems to be a straightforward combination of several existing techniques. This is also suggested in the list of main contributions on page 2, which does not include any fundamental technical problem that this paper solves. 
- The main paper does not discuss any unique characteristic of federated learning problems, where the privacy of data at clients, often including their statistics, needs to be preserved. There is some discussion on federated algorithms in the appendix, which still focuses on straightforward aspects and misses key federated learning challenges such as privacy preservation, client dropout, etc. 
- The experiments use simple models and datasets. IID data distribution is assumed, which ignores challenges related to non-IID data that are mentioned in the motivation

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

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
This paper considers data analytics in federated learning. One application of data analytics is data preprocessing, which requires the estimates of certain data statistics. The submission discusses implementation of data statistics estimating algorithms in federated settings, and performs experiments to showcase the importance of data preprocessing.

### Strengths
The problem of data preprocessing/analytics in federated networks is important.

FedPS implements a set of data preprocessing tools, using tools like random sketching.

It considers some numerical issues in one algorithm, and makes the implemented open-sourced as well.

### Weaknesses
Algorithmic contributions of this paper are limited. It centers around implementations of previous algorithms. It uses a known Log-Sum-Exp trick to handle numerical instabilities of power transform, as well as clipping the data when their absolute values are too big.

For lots of the analytics tasks (estimating quantiles, estimating heavy hitters, etc) in federated learning, simply adding or merging local statistics may not be optimal. For instance, averaging local medians wouldn’t give us global medians. Various open problems remain. 

It is not clear what existing algorithms FedPS uses and why it uses them. There are also differences between one-shot methods and interactive methods to estimate the statistics, which are not discussed in detail.


Minor:
power transform is first discussed without explanation.

### Questions
Please see 'weaknesses' for details. It would be good to discuss what is new in FedPS in addition to providing systematic implementations of existing statistics estimators.

### Soundness
2

### Presentation
2

### Contribution
2
