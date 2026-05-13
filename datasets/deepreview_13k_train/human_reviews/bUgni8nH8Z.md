# Neural Characteristic Activation Value Analysis for Improved ReLU Network Feature Learning

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
This work examines the characteristic activation values of individual ReLU units in neural networks. We refer to the set of input locations corresponding to such characteristic activation values as the characteristic activation set of a ReLU unit. We draw an explicit connection between the characteristic activation set and learned features in ReLU networks. This connection leads to new insights into how various neural network normalization techniques used in modern deep learning architectures regularize and stabilize stochastic gradient optimization. Utilizing these insights, we propose geometric parameterization for ReLU networks to improve feature learning, which decouples the radial and angular parameters in the hyperspherical coordinate system. We empirically verify its usefulness with less carefully chosen initialization schemes and larger learning rates. We report significant improvements in optimization stability, convergence speed, and generalization performance for various models on a variety of datasets, including the ResNet-50 network on ImageNet.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes geometric parameterization (GmP) for ReLU networks.

### Strengths
1. This paper introduced the characteristic activation sets of individual neurons and a geometric connection between such sets and learned features in ReLU networks. 
2. This paper then introduced geometric parameterization (GmP) based on radial-angular decomposition in the hyperspherical coordinate system. It also proves that the change in the angular direction under perturbation $\varepsilon$ is bounded by the magnitude of perturbation $\varepsilon$. This property is not held for standard parameterization and weight normalization.
3. The authors provide some experimental results to show the advantage of the proposed GmP for ReLU networks.

### Weaknesses
1. The Gmp for the ReLU network with IMN in Eq.16 also seems applicable to the weight normalization (WN), i.e. change $u(\theta)$ to $\frac{w}{\||w\|_2}$. I am wondering what the result will look like. The authors should talk more about why they prefer optimization in the angular space instead of the weight normalization space since they are equivalent as shown in Eq. 9 ( $u(\theta):=\frac{w}{\||w\|_2}$). It's not clear why optimizing in the angular space provides an advantage, given the equivalence in Eq. 9. The paper needs to more clearly articulate the specific benefits of the angular parameterization over direct weight normalization, especially concerning stability and optimization behavior.
2. The theoretical proof only shows that the change in the angular direction under perturbation $\varepsilon$ is bounded by the magnitude of perturbation $\varepsilon$. Using $\Delta \phi$ as evidence for generalization is not theoretically justified. I think loss function values should be added as supporting evidence too. The connection between the bound on angular change and generalization is not sufficiently established. While the bound is interesting, it needs to be linked more directly to generalization performance, possibly through empirical loss analysis or other theoretical arguments. The current justification relies too heavily on a single metric, $\Delta \phi$.
3. I found some of the experimental settings unsatisfactory. For example, the training settings of ResNet-50 are very different compared to standard settings. I expect to see a comparison of different methods with standard learning rate decay, i.e. first 30 epochs: 0.1, 30-60 epochs: 0.01, 60-90 epochs: 0.001. Under this setting, BN should achieve around 76.1% top-1 accuracy. Or, the authors should provide a convincing explanation why not use the standard training setting. The deviation from standard training protocols for ResNet-50 raises concerns about the generalizability of the results. It's crucial to demonstrate the performance of the proposed method under commonly used training settings to ensure its practical relevance and comparability with existing methods.

### Questions
1. In Eq.16, only input mean normalization (IMN) is used, why not further normalize the input features with its variance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a geometric parameterization method for ReLU networks to improve their performance. Some experimental results show the performance of the proposed method.

### Strengths
1. This paper proposes a geometric parameterization method for ReLU networks to improve their performance. 
2. Some experimental results show the performance of the proposed method.

### Weaknesses
Although the paper is theoretically and experimental sound, there are still some questions need to be discussed in this paper:
1.	The main contributions of this paper are to propose one geometric parameterization for ReLU networks and input mean normalization. But the input mean normalization proposed in this paper is very similar to the mean-only batch normalization (Salimans & Kingma, 2016). What’s the advantage of the former against the latter?
2.	The experimental results are not convincing. The authors should compare the performance of the proposed algorithm on more models and datasets.
3.	Both the English language and equations in this paper need to be improved.

### Questions
Although the paper is theoretically and experimental sound, there are still some questions need to be discussed in this paper:
1.	The main contributions of this paper are to propose one geometric parameterization for ReLU networks and input mean normalization. But the input mean normalization proposed in this paper is very similar to the mean-only batch normalization (Salimans & Kingma, 2016). What’s the advantage of the former against the latter?
2.	The experimental results are not convincing. The authors should compare the performance of the proposed algorithm on more models and datasets.
3.	Both the English language and equations in this paper need to be improved.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a novel approach to understanding and improving ReLU-based neural networks. The authors delve into the characteristic activation values of individual ReLU units within neural networks and establish a connection between these values and the learned features. They propose a geometric parameterization for ReLU networks based on hyperspherical coordinates, which separates radial and angular parameters. This new parameterization is demonstrated to enhance optimization stability, convergence speed, and generalization performance.

### Strengths
- This paper is written in a clear and easily comprehensible manner, making it easy for readers to follow.
- The paper presents a unique and innovative approach to understanding ReLU networks by exploring the characteristic activation values. This fresh perspective sheds light on the inner workings of these networks, offering insights that were previously unexplored.

### Weaknesses
see questions.

### Questions
- Can the analysis apply to the existing advanced batch normalization improvements like IEBN [1], SwitchNorm [2], layer norm [3]. These missing works should be considered and added to the related works or analysis.

- I am not very familiar with the topics covered in this article, I will consider these clarifications along with feedback from other reviewers in deciding whether to raise my score.

[1] Instance Enhancement Batch Normalization: An Adaptive Regulator of Batch Noise, AAAI

[2] Differentiable Learning-to-Normalize via Switchable Normalization, ICLR

[3] Layer normalization, IJCAI

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
