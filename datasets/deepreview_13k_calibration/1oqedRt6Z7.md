# Convolutional Deep Kernel Machines

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Standard infinite-width limits of neural networks sacrifice the ability for intermediate layers to learn representations from data. Recent work (``A theory of representation learning gives a deep generalisation of kernel methods'', Yang et al. 2023) modified the Neural Network Gaussian Process (NNGP) limit of Bayesian neural networks so that representation learning is retained. Furthermore, they found that applying this modified limit to a deep Gaussian process gives a practical learning algorithm which they dubbed the ``deep kernel machine" (DKM). However, they only considered the simplest possible setting: regression in small, fully connected networks with e.g.\ 10 input features.  Here, we introduce convolutional deep kernel machines. This required us to develop a novel inter-domain inducing point approximation, as well as introducing and experimentally assessing a number of techniques not previously seen in DKMs, including analogues to batch normalisation, different likelihoods, and different types of top-layer. The resulting model trains in roughly 77 GPU hours, achieving around 99\% test accuracy on MNIST, 72\% on CIFAR-100, and 92.7\% on CIFAR-10, which is SOTA for kernel methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an extension of deep kernel machines to leverage convolutions. It is based on the patch-based inter-domain inducing points in the convolutional GP literature. The main difference between convolutional DKMs and convolutional DGPs is that DKMs allow to perform representation learning--the Gram matrix is not fixed as in NNGPs but learnable, while regularized by a NNGP prior. Therefore, the model can have a large number of trainable parameters. Together with the convolutional structure, the model achieves 92% on CIFAR10, which outperforms previous convolutional GP methods and NNGP/NTKs.

### Strengths
* The proposed convolutional DKM model has strong performance on classification benchmarks. 92% accuracy on CIFAR10 is quite impressive if we classify DKM into the broad class of kernel methods. 

* The technical development is sound--the proposed model formulation and training algorithms are sensible and computationally efficient.

### Weaknesses
 * The contribution seems incremental. The proposed method is a combination of DKMs and the inter-domain inducing points used in convolutional (D)GPs.

* The objective for learning parametric gram matrices is regularized by a NNGP prior: $KL(N(0, G^\ell) \| N(0, K(G^{\ell-1}))$ computed from the gram matrix of the previous layer. Although this seems a sensible objective function to enable representation learning, it is unclear what the first principle is behind it. It is mentioned briefly in the paper "Formally, the DKM objective is the evidence lower bound (ELBO) for an infinite-width DGP in the Bayesian representation learning limit." It would be great to see a proof on this.

* The results are quite impressive if we categorize the proposed method into the "kernel method" class. However, I feel more evidences are needed to justify that this is a fair comparison. For example, the number of parameters in DKMs is much larger than NNGPs and convolutional (D)GPs due to the trainable gram matrices. It would be good to report these numbers in experiments and compare to a ResNet with the same number of parameters. Would the regularization bring any advantages over a such a ResNet?

* One big benefit of (D)GPs is that they can produce uncertainty estimates. Do convolutional DKMs exhibit similar capabilities? Are their predictions well-calibrated? Answering these questions could greatly strengthen the paper.

### Questions
Please see above questions.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends the work of deep kernel machines with infinite-width Bayesian NN to convolutional networks. While the extension of the base model to convolutional networks is quite straightforward, making it efficient with inducing points is more challenging and is where the main technical novelty of this paper is.

### Strengths
- The work is a significant contribution to the field of infinite-width NN
- The extension to sparse convolutional DKM is novel
- The method has good results on several standard benchmarks.

### Weaknesses
 - I found the definition of $C^\ell$ in Eq. 18 very confusing and unintuitive. This should be the inducing points equivalent of the BNN convolution operation in Eq. 8. However this involves summing over all of the inducing points in the previous layer. This is unusual and isn't part of any standard convolution.
- Experiments only show accuracy and NLL, and while this is fine for standard machine learning models, the benefit of the Bayesian approach is mostly in the other benefits it adds besides plain accuracy. It would make the paper much better if you show that your VI approximation still holds these properties with additional evaluations on these benchmarks like calibration or out-of-distribution detection.
- The writing needs improvement. English editing is needed to make the paper read like a more coherent text, instead of disjoint sentences.

### Questions
My main question is about Eq. 18 and the reason behind mixing all the previous inducing points.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper formulates the convlutional deep kernel machines based on the framework of a very recent work (Yang et al. 2023), which presents a modified  Neural Network Gaussian Process (NNGP) for retaining a better representation learning. In this work, the authors formulate the convolutional operations in deep kernel machines built upon the convolutional kernel, apply the NNGP framework from (Yang et al. 2023) with an ELBO objective attained, further utilize the sparse GP technique with specific consideration to the convolutional kernel case for yielding a tracble training scheme with the induced points, and conduct experiments mainly mirroring ResNet20 with good results compared to other kernel techniques.

### Strengths
In general, the elements involved in the work and the used technique framework are clear. Despite of the "a bit giant" title, the content presented in the work reflect what the title conveys, so the focus of this work is  well presented.

### Weaknesses
However, for the work itself, I found a bit struggling to appreciate the (both theoretical and practical) benefits of applying the proposed method.

### Major concerns:
1. In the presented content, it does not clearly elaborate or reveal the classical benefits of using kernel method (e.g., more interpretation, primal-dual representation and optimization, analytical results from RKHS, or [1] etc), nor provide practical values of using this method (e.g., varying the architecture besides ResNet20, a possibility of using a simple architecture).

Besides, Would it be possible  that the GP-relied framework in this deep kernel machine shall have advantages in dealing uncertainty in data/images with better robustness or generalization ability. I would suggest the authors to articulate this aspect.

[1] Bohn, B., Rieger, C., & Griebel, M. (2019). A representer theorem for deep kernel learning. The Journal of Machine Learning Research, 20(1), 2302-2333.

2. To my personal experience, the title of this paper looks too "giant", as there exist different lines of work which try to deepen kernel machines w.r.t. different principles, setups and goals. The DKM is basically relying on the NNGP framework (Yang et al. 2023) and the convolution kernel. Besides the cited work in the paper, parts of other work regarding deep kernel machines can involve (**not limited to**):

Mairal, Julien, et al. "Convolutional kernel networks. Advances in neural information processing systems 27 (2014),

Mairal, Julien. "End-to-end kernel learning with supervised convolutional kernel networks." Advances in neural information processing systems 29 (2016),

Chen, Dexiong, Laurent Jacob, and Julien Mairal. "Recurrent kernel networks." Advances in Neural Information Processing Systems 32 (2019), and some other works of Julien Mairal https://lear.inrialpes.fr/people/mairal/resources/pdf/Ohrid_CKN.pdf, where neural networks are involved quite a lot towards a deep architecture.

Suykens, Johan AK. "Deep restricted kernel machines using conjugate feature duality." Neural computation 29.8 (2017),

Tonin, Francesco, et al. "Deep Kernel Principal Component Analysis for Multi-level Feature Learning." arXiv preprint arXiv:2302.11220 (2023),

Achten, Sonny, et al. "Semi-Supervised Classification with Graph Convolutional Kernel Machines." arXiv preprint arXiv:2301.13764 (2023),

and other works of Johan AK Suykens, where the primal-dual framework retaining feature maps (e.g., NNs) in the primal and kernel tricks in the dual is a central idea. I would suggest to have a more comprehensive review on deep kernel machines in related work, though they are designing the model differently. It might also help to distinguish the unique benefits of the proposed method.


### Minor aspects:
1. A configuration figure presenting the convolutional kernel, the deep  architecture and the flow of optimization with sparse GP can be helpful for illustration I suppose.

2. Some typos and non-mathemcatical edits, e.g., the 2nd paragraph under Table 3 on page 8.

3. In the provided codes, there are different variants of nonlinear kernels. But I didn't notice a clear descriptions on how these nonlinear units are chosen or considered.

4. How about the empirical efficiency difference on varying the inducing points setups in Table 2?

5. In Table 1, many factors are investigated, and in different sections mostly the performances did not changge drastically in the compared techniques and were similar to other sections. The evaluation is comprehensive, but the conlusion is less focused, as we would hope to quickly get which factors are the most important ones. I these results don't change much and all attain good results, and then a mild suggestion or a global defaulting setting can be a take-away message.

### Questions
### Major concerns:
1. In the presented content, it does not clearly elaborate or reveal the classical benefits of using kernel method (e.g., more interpretation, primal-dual representation and optimization, analytical results from RKHS, or [1] etc), nor provide practical values of using this method (e.g., varying the architecture besides ResNet20, a possibility of using a simple architecture). 

Besides, Would it be possible  that the GP-relied framework in this deep kernel machine shall have advantages in dealing uncertainty in data/images with better robustness or generalization ability. I would suggest the authors to articulate this aspect.

[1] Bohn, B., Rieger, C., & Griebel, M. (2019). A representer theorem for deep kernel learning. The Journal of Machine Learning Research, 20(1), 2302-2333.

2. To my personal experience, the title of this paper looks too "giant", as there exist different lines of work which try to deepen kernel machines w.r.t. different principles, setups and goals. The DKM is basically relying on the NNGP framework (Yang et al. 2023) and the convolution kernel. Besides the cited work in the paper, parts of other work regarding deep kernel machines can involve (**not limited to**):
 
Mairal, Julien, et al. "Convolutional kernel networks. Advances in neural information processing systems 27 (2014),

Mairal, Julien. "End-to-end kernel learning with supervised convolutional kernel networks." Advances in neural information processing systems 29 (2016), 

Chen, Dexiong, Laurent Jacob, and Julien Mairal. "Recurrent kernel networks." Advances in Neural Information Processing Systems 32 (2019), and some other works of Julien Mairal https://lear.inrialpes.fr/people/mairal/resources/pdf/Ohrid_CKN.pdf, where neural networks are involved quite a lot towards a deep architecture.

Suykens, Johan AK. "Deep restricted kernel machines using conjugate feature duality." Neural computation 29.8 (2017), 

Tonin, Francesco, et al. "Deep Kernel Principal Component Analysis for Multi-level Feature Learning." arXiv preprint arXiv:2302.11220 (2023), 

Achten, Sonny, et al. "Semi-Supervised Classification with Graph Convolutional Kernel Machines." arXiv preprint arXiv:2301.13764 (2023), 

and other works of Johan AK Suykens, where the primal-dual framework retaining feature maps (e.g., NNs) in the primal and kernel tricks in the dual is a central idea. I would suggest to have a more comprehensive review on deep kernel machines in related work, though they are designing the model differently. It might also help to distinguish the unique benefits of the proposed method.


### Minor aspects:
1. A configuration figure presenting the convolutional kernel, the deep  architecture and the flow of optimization with sparse GP can be helpful for illustration I suppose.

2. Some typos and non-mathemcatical edits, e.g., the 2nd paragraph under Table 3 on page 8.

3. In the provided codes, there are different variants of nonlinear kernels. But I didn't notice a clear descriptions on how these nonlinear units are chosen or considered.

4. How about the empirical efficiency difference on varying the inducing points setups in Table 2?

5. In Table 1, many factors are investigated, and in different sections mostly the performances did not changge drastically in the compared techniques and were similar to other sections. The evaluation is comprehensive, but the conlusion is less focused, as we would hope to quickly get which factors are the most important ones. I these results don't change much and all attain good results, and then a mild suggestion or a global defaulting setting can be a take-away message.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes convolutional deep kernel machines (DKMs) which builds upon a previous work of DKM while considers only settings with small-scale and low-dimensional data. The authors first introduce how DKM parameterizes the intermediate kernel matrices in NNGP limit by modifying the objective function. The convolutional DKM is then constructed by incorporating convolutional structure into the kernel function with Gaussian prior on the filter weights. To reduce its computational complexity, the authors leverage the idea of inducing point approach by eliminating spatial structure in inducing points while keeping spatial structure in the remaining data points. The proposed model is tested on several benchmark computer vision datasets with different sets of structures and hyperparameters and compared to other kernel-based models.

### Strengths
•	To my knowledge, the proposed inter-domain inducing point approach seems to be novel and work well in the given context.

•	The authors conduct a comprehensive study of different architectures and hyperparameters of the proposed method.

•	The paper is clearly written and well organized.

### Weaknesses
The scope and applications of convolutional DKM are somewhat limited. From my perspective, a main purpose of kernel-based methods (i.e., NNGP, NTK, DMK, etc.) is to help explain the learning mechanism of Bayesian NNs instead of giving state-of-the-art performance on regression or classification tasks (as can be observed in Table 3). It is thus desirable to briefly discuss how the proposed method contributes to this domain (i.e., explaining the learning scheme of Bayesian convolutional NNs).

It remains unclear how the transition from a feature-based to a kernel-based viewpoint is rigorously justified, particularly when considering the infinite-width limit. The authors mention that the kernel function in Section 4 is calculated based on a finite number of channels ($N_l$), which seems to contradict the infinite-width assumption of DKMs. While the authors state that the features are IID, the specific mathematical steps to move from finite to infinite width in the kernel calculation are not fully transparent. This lack of clarity makes it difficult to assess the theoretical soundness of the proposed approach.

It is also not clear whether the kernel matrix $\textbf{K}_{\text{Conv}}$ is positive-definite by defining $\textbf{F}_{i}^{l}$ using learnable parameter $\textbf{C}^{l}$, or at least a priori (i.e., before training). While the authors claim that the kernel is positive semi-definite because it is the covariance of a random vector, a more detailed explanation of how the specific parameterization using $\textbf{C}^{l}$ ensures this property would be beneficial. The intuition provided is not sufficient to fully understand the positive semi-definiteness under the given parameterization.

### Questions
•	The authors state that DKMs are derived from deep GPs where the width of the intermediate layers goes to infinity, but it seems that the kernel function in Section 4 is calculated based on finite number of channels (i.e., $N_l$ is finite). Can authors provide some clarification?

•	It is not clear whether the kernel matrix $\textbf{K}\_{\text{Conv}}$ is positive-definite by defining $\textbf{F}_{i}^{l}$ using learnable parameter $\textbf{C}^{l}$, or at least a priori (i.e., before training). Can authors give some intuition on this?

•	Why is the convolutional DKM compared with other models only on CIFAR-10 but not CIFAR-100 in Table 3?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
