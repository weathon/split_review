# Learning Invariances via Neural Network Pruning

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Invariance describes transformations that do not alter data's underlying semantics. Neural networks that preserve natural invariance capture good inductive biases and achieve superior performance. Hence, modern networks are handcrafted to handle well-known invariances (ex. translations). We propose a framework to learn novel network architectures that capture data-dependent invariances via pruning. Our learned architectures consistently outperform dense neural networks on both vision and tabular datasets in both efficiency and effectiveness. We demonstrate our framework on multiple deep learning models across 3 vision and 40 tabular datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to prune the original dense network (supernetwork) to find an invariance-preserving subnetwork, called IUNet. 
Toward this, the authors introduce the Invariance Learning Objective (ILO) that helps to learn representation invariant to 
several data transformations and Proactive Initialization (PI).
The authors show that minimizing constrastive learning objective is equivalent to minimizing the distance between
representations of inputs under a set of invariant perturbations, thereby devising ILO.
Through several experiments on vision and tabular tasks, this paper validates the effectiveness of proposed IUNet and
conducted several empirical analysis.

### Strengths
It is novel to me that this paper proposes to obtain invariance-preserving network "via network pruning".
In reality, the experimental results on various tasks show the superior consistency measure, which is much higher than the baselines.
The theoretical insight between the invariant perturbations and the contrastive learning objective is also impressive.

### Weaknesses
Here are my main concerns.

1. The authors try to find the invariance-preserving network "via network pruning", but the proposed ILO could also be applied to just desne networks without network pruning. In this sense, there seems to be a lack of motivation as to why network pruning is necessary for obtaining an invariance-preserving network. Additionally, with magnitude-based one-shot pruning, a method simply based on parameter magnitude will be very sensitive to initialization. To alleviate this, more robust methods for initialization, such as SNIP and GraSP, have been proposed, but in this paper, there is no discussion or experiment on how sensitive to initialization.

2. It seems that many presentations of the paper should be revised. For example, in Section 3.2, the explanation for relations of parameters of supernetwork and subnetwork are quite confusing. Since $\theta_P^{(0)}$ and $\theta_M^{(T)}$ are parameter "vectors", hence the set inclusion operation is not suitable. Also, the expression $|\theta_P^{(0)}| < |\theta_M^{(T)}|$ does not imply that $\theta_P^{(0)}$ is more sparse than $\theta_M^{(T)}$, which does not give any information about the network capacity. Rather, the authors should express the sparsity or network capacity via $\ell_0$-norm (number of non-zeros, nnz). In the same sense, in Section 3.2.1, it seems difficult to say that the higher weight value of criterion (3) is a criterion of network capacity. Even if the parameter value is small, if it is non-zero, it will eventually be counted in the FLOPs calculation, so (for example) the number of non-zeros should be used rather than weight magnitude.

3. In the case of proactive initialization (PI), it is as if only the parameter size was simply adjusted, but looking at the results in Figure 3, the parameters were initialized small with $\kappa = 0.125$. It is natural that the result of $\kappa = 0.125$ has many weights with smaller values. There needs to be some mathematical evidence or experimental results for proactive initialization that can further demonstrate motivation and reasoning about it.

4. It is true that IUNet shows good performance in various experimental results, but it is difficult to interpret Figure 4 that the weights have any pattern. In this sense, I recommend that the authors consider a slightly larger size network parameter or describe more details about which parts are different between the first row and the second row in Figure 4.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to address the issue of pruning neural networks (MLP) which affects the accuracy of the new model, it mainly addresses the issue of invariance during pruning (meaning the weights which might have learned the invariance during the training are dropped) which affects the model accuracy after typical pruning on transformed or original data. It also uses techniques of Initialization of weights and carefully dropping the weights during pruning. They combine Contrastive loss and Maximum likelihood loss to finetune the subnetworks which eventually outperform the original model.

### Strengths
- The paper has a really good notion of using existing work to initialize the weights, dropping the weights and even reinitializing the weights after pruning.

- An automated procedure the construct a completely new sub-network.

- They discover invariance-preserving sub-networks that outperform the invariance-agnostic supernetworks, removing inductive bias in Super net is addressed.

- Paper claims really good improvement on MLP after Pruning when the transformation is performed which fills the gap between CNN and MLP performance.

### Weaknesses
 - Most of the ideas are derived from different papers and combined together.

- Some errors in annotations, missing graph line for different values of K, repetition of the words and techniques throughout the paper.

- The annexure table 7 for tabular data is a bit unclear as it highlights only a few good instances, while the other pruning methods still work better than the proposed method. The reason is not mentioned. While the idea is to capture and preserve the invariance during the pruning, this means somewhere something is still missing in the proposed method, it solves the problem in some of the datasets but not all.

- The paper mentions the encoder-decoder architecture of the proposed method, but throughout the paper, the convention is not followed properly.

- The paper aims to learn an architecture which creates an encoder which represents the same encoding values for all types of transformation.

### Questions
- The authors mention that their method improves compression performance on existing models, how about a completely new model? Does it still work the same? Or do the pre-trained models need to be trained extensively?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a pruning framework called Invariance Unveiling Neural Networks (IUNET) that automatically discovers invariance-preserving subnetworks from deep and dense supernetworks. The framework combines pruning with a novel invariance learning objective to improve the network's inductive bias. In particular, the training objective minimizes the distance between representations of inputs under invariant perturbations for the supernetwork such that the pruned subnetwork architecture captures the invariance. The authors demonstrate that their approach outperforms existing methods in terms of efficiency and effectiveness on both vision and tabular datasets.

### Strengths
The strengths of the paper lie in its comprehensive exploration of invariance in neural network architectures, its demonstration of improved performance on various datasets, and its proposal of a training objective that considers both maximum likelihood and desired invariance properties. The paper also addresses the challenges in designing invariant neural networks for tabular data, which is a valuable contribution to the field.

### Weaknesses
 - As far as I understand, how connectivity models achieve invariance / equivariance does not only rely on the architecture but also on certain constraints on weights (especially weight sharing), for example, the translation invariance / equivariance with convolution. This work only emphasizes on the architecture, but there are no discussions on weights. I am doubtful of the claim (hypothesis) that the subnetwork after retraining "preserves desired invariances and hence improves the inductive bias" and I wonder if this is empirically the case. 

- There lacks a justification or analysis on how pruning of architecture is able to achieve for certain transformation groups. The mechanisms of transformations on the values of input tensors (e.g. colour) should apparently be different from the transformations on the domain (e.g. translation and rotation).

- Rotation, as one of the most explored transformation in the literature of invariant/equivariant deep learning, is however not included in the study of this work.

- A couple of details in the experimental setup are not clear enough, and those will highly affect understanding the effectiveness of the proposed method. See questions.

### Questions
-  After pruning, is ILO or data augmentation used in training the subnetwork?

- In table 3, are the weights of pruned IUNets also re-initialised or re-trained before evaluating the consistency? And if re-trained is ILO or augmentation used in training? As I mentioned, the inductive bias of invariance / equivariance does not only exist in the architecture but also in the shared weights. So if the IUNet weights are re-initialised then the results are too good to be true, otherwise an unfair comparison.

- Also in table 3 and 4, what transformations are used?

- In table 4, what if data augmentation is applied to all models, no matter with and without ILO? I wonder how ILO can improve over simple augmentation (especially with a pruned model trained without ILO)

- Why in fig2(e) ILO is better than IUNet?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
