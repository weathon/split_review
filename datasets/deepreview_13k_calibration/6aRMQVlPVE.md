# Rank-adaptive spectral pruning of convolutional layers during training

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
The computing cost and memory demand of deep learning pipelines have grown fast in recent years and thus a variety of techniques have been developed to reduce model parameters. The majority of these techniques focus on reducing inference costs by pruning the network after a pass of full training. A smaller number of methods addresses the reduction of training costs, mostly based on compressing the network via low-rank layer factorizations. Despite their efficiency for linear layers, these methods fail to effectively handle convolutional filters. In this work, we propose a low-parametric training method that factorizes the convolutions into tensor Tucker format and adaptively prunes the Tucker ranks of the convolutional kernel during training. Leveraging fundamental results from geometric integration theory of differential equations on tensor manifolds, we obtain a robust training algorithm that provably approximates the full baseline performance and guarantees loss descent. 
A variety of experiments against the full model and alternative low-rank baselines are implemented, 
showing that the proposed method drastically reduces the training costs, while achieving high performance, comparable to or better than the full baseline, outperforming competing low-rank approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To reduce the cost of training convolutional neural networks, this work proposes a low-parametric training method that combines tensor Tucker format and adaptive pruning of Tucker ranks for convolutional layers. Noticeably, the method allows for the adaptivity of the rank of convolutional filters depending on compression rate and robustness for their condition. The authors verify the method's effectiveness by comparing the proposed method with the full training and baselines and observe the cost is reduced due to the proposed method.

### Strengths
Reducing the training cost of neural networks has attracted much interest, and many papers proposed the method aiming at practical training with less memory consumption. However, most methods focus on the training cost of a fully connected layer and cannot apply to the convolutional layers. Out of all, the proposed method TDLRT gives the efficiency of training convolutional layers.

### Weaknesses
 - TDLRT is complicated compared to vanilla SGD. Indeed, the method needs to compute QR decomposition, the projection, etc, causing significant additional costs. Taking this additional computational cost, it is unclear how computationally efficient TDLRT is. Specifically, the paper lacks a detailed analysis of the computational overhead per iteration, including the cost of QR decompositions and projections, compared to standard SGD. It is not sufficient to only consider the number of iterations to convergence; the cost per iteration must be factored in to make a fair comparison. For example, the cost of computing the Tucker decomposition and its gradient, along with the adaptive rank selection, could be significant and needs to be quantified.

- Theorem 2 does not necessarily indicate the convergence of loss. And there is no comparison with the other method regarding the convergence rate and complexity. The theoretical analysis is limited, and the paper does not provide a rigorous convergence analysis for the proposed method. While the theorem shows that the method stays close to the manifold, it does not guarantee that the loss function will converge to a local minimum. Furthermore, there is no comparison of the convergence rate of TDLRT with other methods, such as standard SGD or other low-rank training approaches. A detailed analysis of the convergence properties, including the rate of convergence and its dependence on hyperparameters, is needed.

### Questions
- It would be nice if the authors could discuss the computational cost per iteration. The computational complexity should also be considered for a fair comparison with SGD and competitors.

- Is it possible to show the convergence of the loss function by training with TDLRT?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an adaptive compression methods for convolution layers using the Tucker decomposition. An interesting feature of the paper is the use of Riemannian geometric approach for tensor decomposition allowing to adaptive rank selection.  Experiments are reasonably good. The motivation to use Tucker decomposition over other methods is not clear. Further, the methods employed may not be the optimal decomposition approach.

### Strengths
1) The problem is useful and relevant.

2) Motivation experimental results.

### Weaknesses
1) The proposed method is incremental work and lack strong novelty.

2) All possible tensor decomposition methods are not considered such as tensor-train. See question 1.

### Questions
1) Though Tucker based decomposition of the convolution layers seems to work well, I wonder if tensor-train is better decomposition [1] for this setting. Tensor-train decomposition  avoids the core tensor, while uses fewer ranks compared to Tucker.  Is there a specific advantage of the proposed method over Tucker? Adaptive rank based learning has also been explored with  Riemannian geometry [2].

2) What are the actual training times compared with the proposed model and baseline methods?

[1] A I. V. Oseledets.  Tensor-Train Decomposition. 2011, SIAM Journal on Scientific Computing, 2295-2317

[2] Michael Steinlechner, Riemannian Optimization for High-Dimensional Tensor Completion,  2016,  SIAM Journal on Scientific Computing

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a dynamic low-rank training method for convolutional neural networks that factorizes convolutions into tensor Tucker format and adaptively prunes the Tucker ranks of the convolutional kernel during training. The proposed method drastically reduces training costs while achieving high performance, outperforming competing low-rank approaches. The paper also includes a discussion of the geometric integration theory of differential equations on tensor manifolds used in this work. Empirical evaluation on CIFAR10 using VGG and Alexnet models also shows the effectiveness of the proposed method.

### Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation and a nice introduction to the problem. 

2. The connection to recent advance in dynamic low-rank approximation is interesting and indeed a nice direction to apply it to dynamic low-rank training. 

3. Strong theoretical understanding on the proposed method. The authors provide a clear derivation of TDLRT and its convergence analysis.

### Weaknesses
1. Concerns on novelty. The proposed TDLRT is clearly an extension of matrix DLRT [1] on Tensor format. Although the authors emphasize this extension is non-trivial as it requires the use of Tucker decomposition and additional techniques for theoretical analysis, I believe the extension is not significant enough to be considered as a novel contribution. The core idea of using a differential equation to dynamically adjust the rank of the low-rank approximation remains largely the same, and the adaptation to tensors, while requiring some modifications, does not fundamentally alter the underlying principle. The use of Tucker decomposition, while a valid approach for tensors, is a standard technique and its application here does not introduce a groundbreaking concept.

2. The paper lacks discussion on computational complexity during training. The authors claim the proposed method drastically reduces the training cost but the empirical results on training cost are missing. In Figure 2, the authors only show the computational footprint of the inference stage. However, for such dynamical compression method I believe training cost is more important to discuss. It would be great to show a figure similar to Figure 2 in [1] to visualize the training cost across different rank values. In Table 1, it also would be great to present the total training cost by different methods for a fair comparison. The absence of training cost analysis makes it difficult to assess the practical benefits of the proposed method, especially given the overhead of performing SVD at each step.

3. More details of proposed method are needed. For example, what initialization on low-rank factors and does it affect the performance? How to choose the threshold? The lack of detail regarding the initialization of the low-rank factors is a concern, as this can significantly impact the convergence and final performance of the network. The choice of the threshold for rank adaptation is also crucial and requires more discussion on how it affects the trade-off between compression and accuracy. Without a clear guideline on this, it is difficult to reproduce the results and apply the method in different scenarios.

4. Evaluation on large-scale datasets and SOTA models are needed. CIFAR-10 is too small to show the effectiveness of the proposed method, and VGG16 and Alexnet are outdated models. It would be great to evaluate methods on ImageNet at least using ResNet50. The current evaluation is insufficient to demonstrate the practical applicability and scalability of the proposed method. The use of small datasets and outdated models raises questions about the method's performance on more complex and realistic scenarios.

### Questions
1. Would be great to provide more details on the training behavior of TDLRT, such as how rank evolves during training, convergence behaviors regarding various compression thresholds, etc.

2. How often do you perform basis augmentation and tucker decomposition using SVD? If it is performed frequently for every step, does the numerical instability affects the convergence? such that, at the later stage of training, the perturbation on $C$ by learning algorithms may be too small compared to the numerical error induced by SVD.    

3. Is there any way to further improve efficiency to make the method practical?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
