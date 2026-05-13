# SiT:   Symmetry-invariant Transformers for Generalisation in Reinforcement Learning

- Decision: Reject
- Scores: 6, 8, 3

## Abstract
An open challenge in reinforcement learning~(RL) is the effective deployment of a trained policy to new or slightly different situations as well as semantically-similar environments. 
We introduce {\bf S}ymmetry-{\bf I}nvariant {\bf T}ransformer (SiT), a scalable vision transformer~(ViT) that leverages both local and global data patterns in a self-supervised manner to  improve generalisation. Central to our approach is Graph Symmetric Attention,  which refines the traditional self-attention mechanism to preserve graph symmetries, resulting in invariant and equivariant latent representations. 
We showcase SiT's superior generalization over ViTs on MiniGrid and Procgen RL benchmarks,  and its sample efficiency on Atari 100k and CIFAR10.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Symmetry-Invariant Transformer (SiT), a variant of Vision Transformer that can identify and leverage local and global data patterns. SiT employs Graph Symmetric Attention to maintain graph symmetries, creating invariant and equivariant representations. SiT's contributions involve addressing generalization challenges in RL by utilizing self-attention to handle both local and global symmetries, resulting in better adaptation to out-of-distribution data distributions. It surpasses Vision Transformers (ViTs) and CNNs in RL benchmarks like MiniGrid and Procgen showing improved generalization ability. SiT's contributions include handling symmetries at the pixel level, achieving superior RL performance, and introducing novel methods for employing graph symmetries in self-attention without relying on positional embeddings.

### Strengths
1. This paper provides an interesting way to achieve equivariance to different symmetries in grid data by using graph symmetric attention and different choices of graph topology matrix $G$. To the best of my knowledge, this idea is novel. 

2. SiT achieves impressive generalization performance on MiniGrid and ProcgenRL over ViTs and CNNs.

### Weaknesses
1. Some sections of this paper are not well written leading to confusion while following the paper's arguments. For example in equation 2, symmetric($GV$) assumes that GV is $\mathbb{R}^{P\times P}$ whereas according to the author's definition of $G$ it should be $\mathbb{R}^{P\times d_f}$. This makes it really hard to follow the author's argument and how this formulation is connected to Graph Attention Networks [1] or $E(n)$ Equivariant GNN [2], This also makes following section 3 difficult.

2. As SiT has been built keeping in mind the inductive biases coming from the symmetries of the environment and task, I think just comparing with CNN or ViT baseline is not completely fair. The authors should use an E2 equivariant architecture like E2 Steerable Networks as their baseline for RL experiments [3, 4] or E(n) equivariant GNN [2]. Authors should also expand on the related work on equivariant architectures [5,6] for reinforcement learning. [3, 4, 7]

### Questions
Q1. In Figure 1 (a), what does the bottom right image depict? 


Q2. Can you explain how Equation 2 is connected to GAT and E2GNN?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Symmetry-Invariant Transformer (SiT), a self-attention based network architecture that incorporates planar rotation and reflection symmetries. Central to the architecture is the proposed Graph Symmetric Attention (GSA) layer, which utilizes a graph topology matrix $G$ to control the different symmetries that are allowed in the layer by breaking the full-permutation invariance in the standard attention mechanism. By employing GSA both locally (i.e., each pixel is a token) and globally (i.e., each image patch is a token), SiT efficiently encodes symmetries at various levels. Moreover, by changing the token embedding from invariant features to equivariant features, SiT can be extended to be equivariant (or both invariant and equivariant). The authors apply SiT in both reinforcement learning and supervised learning, showing a solid improvement in both performance and sample efficiency.

### Strengths
1. The proposed architecture is novel. It provides a fresh perspective that connects permutation equivariance and rotation/reflection equivariance by constraining the grid topology matrix. 
2. Utilizing GSA both at local and global levels to preserve symmetries across varying scales is an appealing concept.

### Weaknesses
1. The experiments could benefit from stronger baselines. Given the paper's introduction of a novel equivariant architecture, I think a comparison with existing equivariant architectures is necessary. A possible baseline could be some equivariant architectures that enforce global rotational symmetries like e2cnn[A], or utilizing rotation data augmentation to realize equivariance in CNN or ViT.
2. It would be nice to have an ablation study on only using GSA globally or locally to understand how the two components contribute to the improvement.

### Questions
1. In the first paragraph of page 4, the paper claims, `Notably, GSA reduces to the conventional attention mechanism when the underlying graph topology matrix G only contains self-loops, i.e. G being the identity matrix.` My interpretation of this is that if $G$ is the identity matrix, the output of $\Gamma(Q, K)$ would result in a diagonal matrix, where each token can only attend to itself. This doesn't align with the conventional attention mechanism. I think $G$ should be an all-one matrix here instead of an identity matrix. Please correct me if I am missing something here. 
2. I do not fully understand why $G_{k,v,q}$ are necessary. Would just having $G$ in equation 3 not be enough for maintaining the desired equivariance?
3. How are the sizes of the local patch (5x5) and the global patch (14x14) selected?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a symmetry-invariant transformer (SiT) that learns invariant and equivariant latent representations on images, and applies it in some RL tasks. I think this paper fits better in the CV domain rather than RL, as most of the paper focuses on describing a symmetry-preserving ViT and offers little new insight for RL. Although leveraging symmetry is definitely helpful for promoting generalization, the paper does provide sufficient evidence on the benefits of using the proposed method in solving general RL tasks.

### Strengths
- Leveraging symmetries/invariances is a reasonable direction to improve the generalization performance in RL tasks.
- The paper proposes a method to enforce image-level symmetry-invariant/equivariant on ViT.
- The proposed method shows good performance on some vision-based RL tasks that require image-level generalization capability.

### Weaknesses
 - The majority of the paper is to derive a symmetry-invariant and equivariant ViT model, and there is not much design in the RL part. That's why I think the paper should be treated as a CV paper rather than an RL paper. In that sense, the proposed method should at least first demonstrate its superiority in CV tasks. Unfortunately, the proposed method is only evaluated on the extremely simple CIFAR-10 dataset, and compared with no other CV baselines except for ViT.
- The proposed method is based on ViT, which makes its applicability only restricted to vision-based RL tasks. Moreover, as ViT is quite heavy and costly to learn, it inevitably hurts sample efficiency and usability as compared to other commonly used vision encoders in vision-based RL tasks. No learning curves or results are provided related to the sample efficiency for RL tasks, which is somewhat insufficient to demonstrate the practical value of the proposed method to the RL community.
- The evaluations are only conducted in tasks that particularly rely on image generalization capability, like Procgen and MiniGrid. For some tasks like robotic manipulation, as the sense of orientation is vital, the importance of symmetry-invariant may not be that large.
- There lack of strong baselines in the experiments. The baselines only include ViT, variants of the proposed method, and simple baselines like CNN. As far as I know, there are also some existing works that introduce symmetry-preserving designs in CNN or other image-based models. Such methods should be also compared given their relevance to this paper.
- Minor: the paper reminds me of a recent NeurIPS paper [1] that also uses symmetry to enhance RL performance. This is probably not super related as it enforces symmetry on the temporal aspect, but also worth mentioning.

### Questions
- How will the proposed method perform on more general visual control tasks, like Atari?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
