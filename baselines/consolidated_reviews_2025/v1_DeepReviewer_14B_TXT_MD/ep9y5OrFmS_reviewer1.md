### Summary

This paper studies the connection between the pruning masks and the Hessian eigenspaces during the training of neural networks. The main contribution of this paper is the empirical finding that the overlap between the top k eigenspace of the Hessian and the pruning mask (i.e., the large magnitude parameters) is well above random chance and can be used to approximate the top Hessian subspace.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. This paper provides a new perspective on connecting the pruning mask and the Hessian eigenspace by casting them as orthonormal matrices and using the Grassmannian metrics. 
2. This paper empirically shows that the overlap between the top k eigenspace of the Hessian and the pruning mask (i.e., the large magnitude parameters) is well above random chance and is stable during the training.

### Weaknesses

#### Some Related Works


#### comment

1. Although this paper provides a new perspective on connecting the pruning mask and the Hessian eigenspace, the contribution of this paper is limited and incremental. The connection between the pruning mask and the Hessian eigenspace has been studied in the literature. 
2. It is not a surprise to see that the overlap between the top k eigenspace of the Hessian and the pruning mask is well above random chance and is stable during the training. This is because the parameters with large magnitudes have a large impact on the output of the DNNs, and the top eigenspace of the Hessian characterizes the direction of the large change of the loss function. 
3. This paper does not provide any new algorithm to leverage the connection between the pruning mask and the Hessian eigenspace. Although the authors mention that we can use the pruning mask to approximate the top Hessian subspace, I did not find any experiment to verify this claim.

### Suggestions

The paper's core argument hinges on the empirical observation of a significant overlap between the top-k Hessian eigenspace and the parameter space defined by large-magnitude weights. While the authors frame this as a novel finding, the connection between parameter magnitude and loss landscape has been explored in prior work, albeit perhaps not with the same specific focus on the Grassmannian metric. To strengthen the contribution, the paper should delve deeper into the theoretical underpinnings of this overlap. For instance, it would be beneficial to investigate the conditions under which this overlap is guaranteed to be high, or conversely, when it might break down. This could involve analyzing the properties of the loss function, the network architecture, or the training dynamics. Furthermore, a more rigorous analysis of the relationship between the parameter space and the Hessian eigenspace, beyond simply measuring their overlap, is needed to provide a more substantial contribution. This could involve exploring the angles between the subspaces or analyzing the distribution of singular values of the projection matrix between them. 

To address the concern that the observed overlap is not surprising, the paper needs to provide a more nuanced analysis of the specific characteristics of this overlap. It is not sufficient to simply show that the overlap is above random chance. The authors should investigate how this overlap evolves during training and how it is affected by different training hyperparameters. For example, does the overlap increase or decrease with the learning rate? Does it vary with the batch size? Does the overlap differ between different optimizers? Furthermore, the paper should explore the practical implications of this overlap. If the overlap is indeed stable, as claimed, then it should be possible to leverage this stability to develop more efficient algorithms for tasks such as network pruning or hyperparameter tuning. The paper should also investigate the limitations of this overlap, and when it might not be a reliable indicator of the top Hessian subspace. 

Finally, the lack of a concrete algorithm leveraging the observed connection is a significant weakness. The paper mentions the potential of using the pruning mask to approximate the top Hessian subspace, but this claim is not supported by any experimental evidence. To address this, the paper should propose and evaluate a specific algorithm that uses the pruning mask to approximate the top Hessian subspace. This could involve, for example, using the large-magnitude weights to construct a basis for the approximate Hessian subspace and then evaluating the quality of this approximation by comparing it to the true top Hessian subspace. The paper should also explore the practical benefits of this approximation, such as reduced computational cost or improved performance in downstream tasks. Without such an algorithm and experimental validation, the paper's contribution remains largely theoretical and lacks practical impact.

### Questions

1. What is the practical benefit of studying the overlap between the top k eigenspace of the Hessian and the pruning mask?
2. The overlap between the top k eigenspace of the Hessian and the pruning mask is well above random chance at the initialization. Is it possible that this high overlap is due to the random initialization? What is the initialization method in the experiments?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
