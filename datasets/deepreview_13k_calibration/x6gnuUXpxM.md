# Constructing Sparse Neural Architecture with Deterministic Ramanujan Graphs

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
We present a sparsely connected neural network architecture constructed using the theory of Ramanujan graphs which provide comparable performance to a dense network. The method can be considered as a before-training, deterministic, weight free, pruning at initialization (PaI) technique. The deterministic Ramanujan graphs occur either as Cayley graphs of certain algebraic groups or as Ramanujan $r$-coverings of the full $(k,l)$ bi-regular bipartite graph on $k + l$ vertices. Sparse networks are constructed for bipartite graphs representing both the convolution and the fully connected layers. We experimentally show that the proposed sparse architecture provides comparable accuracy with a lower sparsity ratio than those achieved by previous approaches based on non-deterministic methods for benchmark datasets. In addition, they retain other desirable properties such as path connectivity and symmetricity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use deterministic Ramanujan graphs as a PaI technique for neural architecture sparsification, which can be applied to fully connected and convolutional layers. The proposed method is evaluated on classical architectures for vision tasks.

### Strengths
- The proposed technique is theoretically supported by spectral graph theory.
- The adopted deterministic Ramanujan diagram has desirable properties for sparsification.

### Weaknesses
 - Ramanujan graphs have been well-studied for pruning at initialization [1] and sparse architectures [2]. 
- The experiments are not well designed, especially for the comparison with other PaI methods and the introduction of metric $\delta_{acc}$. Specifically, the comparison in Table 9 is problematic. The PaI baselines are applied to CIFAR-VGG, a smaller network, while the proposed method is evaluated on VGG-base, which is significantly larger. This difference in scale makes it difficult to draw meaningful conclusions about the relative performance of the proposed method. Furthermore, the pruning settings and training procedures for the baselines and the proposed method are not consistent, rendering the comparison using $\delta_{acc}$ inappropriate. The metric $\delta_{acc}$ is presented as a drop in accuracy, but the baseline and proposed methods are evaluated under different conditions, making this metric misleading.

### Questions
- It is very interesting to see that the conclusion here is different from [1], as it claims “not only the Ramanujan property for sparse networks shows no significant relationship to PaI’s relative performance, but maximizing it can also lead to the formation of pseudo-random graphs with no structural meanings”. Can the author elaborate how the property of “deterministic” may mitigate this?
- It seems that Table 9 is not a fair comparison. PaI baselines are applied to CIFAR-VGG, while the proposed method is applied to VGG-base instead, which is 9 times larger than CIFAR-VGG. Meanwhile, the setting adopted for them is also different. The introduced metric $\delta_{acc}$ is inappropriate to evaluate them as the setting and difficulty of pruning are all different.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work empirically studies a deterministic method for constructing sparse networks. The method is based on some known regular and bi-regular Ramanujan graph construction techniques.  Experiments on Cifar10/Cifar100 show the effectiveness of the proposed method compared to baselines.

### Strengths
+ The Ramanujan graph construction techniques are based on recent improvements in graph theory on Ramanujan graphs.
+ Empirical results demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The introduction of the Ramanujan graph construction techniques is too dense and without a good preliminary, which is hard for ML communities to appreciate in general. Actually, the paper, even for its main text has one paper left to fill in. The paper was written in rush. More details on the adopted techniques should be introduced.

- It confuses people when constructing fully connected layers, one adopts Cayley graphs, while to construct convolution layers, one adopts the approach in Sec 4.3.

- The construction seems not to be able to construct layers with arbitrary sizes.

- Empirical evaluation is not based on larger datasets, such as ImageNet. As I am not an expert who works on network pruning, I am not sure if a larger dataset should be used.

- In section 4.4, q should be larger than l. However, in table 9, q is smaller than l.

### Questions
1. Can the authors explain why "In section 4.4, q should be larger than l. However, in table 9, q is smaller than l" ?

2. Can the authors explain why "when constructing fully connected layers, one adopts Cayley graphs, while to construct convolution layers, one adopts the approach in Sec 4.3"?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to prune / sparsify fully connected and convolutional layers in deep nets using deterministic Ramanujan graphs,

### Strengths
Interesting and theoretically well motivated approach.

### Weaknesses
While the conceptual idea on its own is interesting and promising, this paper is lacking deeper theoretical insights (actual novel theoretical contributions) and/or more importantly solid experiments that properly compare the proposed methods with recent baselines.

The paper tries to achieve the latter in Table 9, where the achieved pruning and accuracy is compared with three recent baselines. However, the baselines are evaluated on different variants of the initial neural networks (e.g. different number of parameters, etc.) and hence are not really comparable. Besides, the baselines achieve typically much higher (absolute) accuracy, but as as just said they are not really comparable.

Overall, the fact that Ramanujan graphs were already used for pruning (Hoang et al ICLR 2023) makes this contribution rather iterative (going from random Ramanujan graphs to deterministic ones). I am willing to change my score if authors / other reviewers address my concerns and convince me of the significance of the contribution.

Minor comments:
* Wrong use of \citep vs \citet (e.g."[..] data independent contexts Cheng et al. (2023)" must be (Cheng et al., 2023) and many more such examples)
* Perhaps typo in title "Neural Architecture**s**"?

### Questions
/

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a deterministic method for constructing sparse neural network structures which upon weight initialization can be trained to a high accuracy. The method is based on a Ramanujan graph construction technique. Experimental results show that their methods is able to achieve high sparsity without performances losses.

### Strengths
1. The proposed methods achieve higher sparsity compared to SNIP and GraSP.

2. The method works in pre-training phase and is weight free, which are two main advatanges.

### Weaknesses
1. The experiment is kind of weak. Apart from SNIP and GraSP., there are other pre-training pruning methods as well. Besides, there is also a series of works focused on during-training pruning, such as SET/RigL. I recommend the author give a comprehensive comparison as well.
2. The performance improved compared to existing methods is limited, which means the proposed method only makes a limited contribution.
3. A critical problem of the methods remains that unstructured sparsity is hard for physical acceleration.

### Questions
1. What is the computational complexity of the proposed sparsification method to compute the sparse mask?
2. How the sparse training is implemented in the experiments? Can the authors give a detailed explanation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
