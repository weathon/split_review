# Beyond Canonicalization: How Tensorial Messages Improve Equivariant Message Passing

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
In numerous applications of geometric deep learning, the studied systems exhibit spatial symmetries and it is desirable to enforce these. For the symmetry of global rotations and reflections, this means that the model should be equivariant with respect to the transformations that form the group of $\mathrm O(d)$.
While many approaches for equivariant message passing require specialized architectures, including non-standard normalization layers or non-linearities, we here present a framework based on local reference frames ("local canonicalization") which can be integrated with any architecture without restrictions.
We enhance equivariant message passing based on local canonicalization by introducing tensorial messages to communicate geometric information consistently between different local coordinate frames.
Our framework applies to message passing on geometric data in Euclidean spaces of arbitrary dimension.
We explicitly show how our approach can be adapted to make a popular existing point cloud architecture equivariant. We demonstrate the superiority of tensorial messages and achieve state-of-the-art results on normal vector regression and competitive results on other standard 3D point cloud tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the equivariant message passing and proposes a formalism which together with local canonicalization enables consistent communication of geometric features between different nodes. This method solves the problem of communicating geometric information between local patches with different coordinate frames and can be combined with other point cloud methods, achieving state-of-the-art results in the experiments.

### Strengths
1. The paper is well-written and technically sound.
2. The paper provides comprehensive theoretical analysis.
3. The experiment results are promising.

### Weaknesses
1. The proposed method relies on point normals to establish local reference frames. However, estimating accurate normals is difficult for *real-world* point clouds due to severe noise. So I expect to see results on real-world tasks rather than only synthetic datasets.
2. An important application of invariance and equivariance is point cloud registration. I expect to see the effectiveness of the proposed method on real-world point cloud registration tasks, such as 3DMatch and 3DLoMatch.
3. In Tab.3, the tensor messages surprisingly outperforms the model with scalar messages under random local frames. The random local frames affect the performance of the model in the form of noise, but these noises help tensor messages perform better. I am very curious about its reason.
4. In Tab.2, I notice refining frames brings marginal improvements, which may indicate that this step fails to obtain better normals. For comparison, I expect to see the results with (1) PCA-based normals and (2) ground-truth normals.

### Questions
Please address the problems in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes an extension of unconstrained message-passing architectures that makes them equivariant by canonicalizing the messages received by each node to its local frame.  It enables local canonicalization of arbitrary types of tensorial messages, which extends previous works that restrict the allowed tensor type of messages (e.g. only allowing for scalars or vectors).  In addition to the local canonicalization methodology, the authors introduce a mechanism for learning the local frame of each node, which is then refined in the later layers of the network.  In the experimental section, the authors evaluate their proposed method on various rotational equivariant point-cloud tasks and provide ablation studies that showcase how the individual parts of the proposed framework affect its performance and generalization.

### Strengths
- The authors describe the proposed framework in detail, providing clear intuition about the specific problems each part of the framework addresses.
- The simplicity of the proposed framework allows it to be easily applied to widely used non-equivariant message-passing architectures with minimal modifications.
- The experimental results demonstrate how the proposed local canonicalization benefits the performance of the baseline model when it is used in tasks with various types of tensorial outputs (e.g.  normal regression or point cloud segmentation).

### Weaknesses
 - The proposed canonicalization procedure assumes that the inferred output vectors $v_{1},v_{2}$  are non-zero. While the authors describe how they resolve ambiguities when $v_{1},v_{2}$ are parallel, they do not explain how they handle the case where the vectors are close to zero, which makes frame selection highly sensitive to small perturbations due to noise. This is a critical issue because if either $v_1$ or $v_2$ approaches zero, the resulting frame becomes ill-defined, and the transformation to this frame can introduce significant numerical instability. The lack of a clear strategy for handling near-zero vectors undermines the robustness of the method, especially in noisy environments or when dealing with highly symmetric local neighborhoods where the predicted vectors might be close to zero.
-  While in Section 2 the authors mention previous works on local-canonicalization during message passing, they do not discuss work on gauge equivariant neural networks, such as the work:  
 [1] Pim De Haan, Maurice Weiler, Taco Cohen, Max Welling, "Gauge Equivariant Mesh CNNs: Anisotropic convolutions on geometric graphs" ICLR (2021)  
which also transforms geometric features from one local frame to another during the message passing, performed in their case during the mesh convolution.

### Questions
- How does the proposed method handle cases where the predicted vectors $v_{1},v_{2}$ are zero or close to zero? Additionally, how sensitive is the frame selection mechanism when different levels of noise are added to the input point clouds? Does this sensitivity change in cases of more symmetric objects?
- An addition of a discussion of gauge equivariant neural networks will benefit the completeness of the related section of this work.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main claim of the paper is that maintaining local equivariant tensor geometric feature in the graph network is better than first canonicalize the feature in local frame and do invariant message passing.  It also proposes a way to pass tensorial features in graph network. The proposed message passing is experimented on toy shape dataset.

### Strengths
- The paper has a smooth and easy-to-flow presentation into equivariance.
- Maintaining local geometric features may be useful in more general settings (but not the examples shown in the paper, see weakness below). Which in the long run may benefit the equivariance community.

### Weaknesses
 - The main concern is that all the experiments are conducted on rigid objects. However, the reviewer believes that the main advantage of the local geometric features preserving throughout the network is to deal with some non-rigid, multi-body, or deformable objects. Indeed there is no strict equivariance in deformation but it is where the local feature should make a difference. Just as shown in Fig.1 in the paper, the geometric feature should help recognize the pattern of the sub-part when it deforms or move. However, the main experiment is conducted on the modelnet rigid object, which we know the performance is quite saturated, and the reviewer believes that a robust global PCA plus any modern large point network will outperform an equivariant network in such an easy setting.
- Again, the comparison does not capture the full equivariant network baselines. We know that there are many more equivariant point networks compared on the same benchmark but they are not included in the table.
- Some more clear discussion of the difference between the proposed message passing with previous ones like TFN or VNN should be highlighted in the paper.

### Questions
The main concern is that the experiments are not convincing for the main claim, some more challenging cases (e.g. multi body objects)  should be included to show the effectiveness of the local geo features

### Soundness
3

### Presentation
3

### Contribution
2
