# Maestro: Uncovering Low-Rank Structures via Trainable Decomposition

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
\red{Deep Neural Networks (DNNs) have been a large driver for AI breakthroughs in recent years.
However, these models have been getting increasingly large as they become more accurate and safe. This means that their training becomes increasingly costly and time-consuming and typically yields a single model to fit all targets.
Various techniques have been proposed in the literature to mitigate this, including pruning, sparsification, or quantization of model weights and updates. While achieving high compression rates, they often incur significant computational overheads at training or lead to non-negligible accuracy penalty. Alternatively, factorization methods have been leveraged for low-rank compression of DNNs. Similarly, such techniques (e.g.,~SVD) frequently rely on heavy iterative decompositions of layers and are potentially sub-optimal for non-linear models, such as DNNs.}
\red{We take a further step in designing efficient low-rank models and propose \tool, a framework for trainable low-rank layers. Instead of iteratively applying a priori decompositions, the low-rank structure is baked into the training process through \technique,
a low-rank ordered decomposition. Not only is this the first time importance ordering via sampling is applied on the decomposed DNN structure, but it also allows selecting ranks at a layer granularity.
Our theoretical analysis demonstrates that in special cases \technique recovers the SVD decomposition 
and PCA 
. Applied to DNNs, \tool enables the extraction of lower footprint models that preserve performance. Simultaneously, it enables the graceful trade-off between accuracy-latency for deployment to even more constrained devices without retraining.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes MAESTRO, which is a trainable low-rank approximation technique for deep neural networks. It proposes a progressive shrinking approach that decomposes the weights of each layer into low-rank components using an extended version of Ordered Dropout. This allows for efficient compression and trade-off between model size and accuracy. The method is evaluated on various models, datasets, and modalities, showing superior performance compared to other compression methods.

### Strengths
- The paper extends the Ordered Dropout technique to handle non-uniformity in the search space by allowing different ranks per layer. 

- It introduces a trainable aspect to the decomposition, which enables the model to reflect the data distribution. 

- It provides a latency-accuracy trade-off mechanism for deploying the network on constrained devices.

### Weaknesses
- The citation style seems not correct. It should include the author's names in place of numerical references.

- Why the method named after "Maestro"? It is never introduced and seems weird to me.

- The proposed technique appears as a logical improvement from Ordered Dropout. Its effectiveness, however, is primarily demonstrated through toy architectures and datasets, such as ResNet18 and Cifar10. For the method to gain practical and impactful validation, I recommend conducting additional experiments on more complex datasets like ImageNet to substantiate its superiority.

- Building on the previous point, there are alternative methods that report better accuracy with more compact architectures. For instance, the OTOv2 framework:

Chen, Tianyi, et al. "Only train once: A one-shot neural network training and pruning framework." Advances in Neural Information Processing Systems 34 (2021): 19637-19651.

It structurally prunes the model during training (hence still training efficient), and it achieves a 93.3% accuracy with only 0.55M parameters on Cifar10 using VGG16. This is in contrast to the 93.10% accuracy with 2.20M parameters reported by the proposed method. This comparison casts doubt on the practical utility and the advantages of the low-rank based method presented.

### Questions
See the weaknesses part above.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a low-rank compression scheme for deep neural networks, which factorizes fully connected, convolutional, and attention layers in the form A=UV, and progressively reduces the rank of the U and V matrices. For convolutional layers the factorization is applied to the unrolled 2D matrix, while for attention layers it is applied to the Q, K, V matrices. They use ordered dropout and hierarchical group-lasso to facilitate the reduction of the rank of U/V matrices.

### Strengths
Unlike unstructured pruning methods, low-rank compression can preserve the dense structure of matrices, which can extract more performance from GPUs. For the training of transformers on the Multi30k dataset shown in Table 3, the proposed method is able to reduce the number of parameters by more than half compared to the baseline (Pufferfish), while also reducing the perplexity.

### Weaknesses
Low-rank compression and Lasso have been around for a very long time, and the only novelty seems to be the use of ordered dropout. The improvement over existing methods is marginal for the experiments with CNNs. The proposed method is obviously very sensitive to the choice of the Lasso coefficient lambda, but there is no theory behind how it can be chosen effectively.

### Questions
How is the initial factorized mapping performed without SVD? How is the initial maximal rank r chosen?

How does the proposed method compare with other structured pruning methods?

Typos
p.4 “multi-head attention (HMA)” > “multi-head attention (MHA)”
p.5 “we one could leverage” > “one could leverage”
p.5 “Singular Value Decomposition (SVD)” Why define this here when it has been repeatedly used in previous sections?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work mainly focuses on incorporating trainable low-rank layer decompositions in deep-learning models. The authors propose MAESTRO, which progressively finds the optimal rank of each layer during the training by imposing importance ordering via the existing Ordered Dropout technique. The redundant ranks are zeroed out by using the hierarchical group lasso term as the regularizer in the loss function. MAESTRO accounts for data distributions and the target function rather than applying SVD on pre-learned model weights.

### Strengths
The novelty of the work lies in applying the existing Ordered Dropout technique from Federated Learning (FjORD) to optimally order the heterogeneous ranks of various layers in DNNs based on importance criterion, which results in discovering layer-wise low-rank decompositions. In contrast to uniform dropout across the width in each layer ( FjORD), MAESTRO independently decomposes each layer to uncover optimal rank. The authors provide applications of MAESTRO to various layer types in CNNs, FC, and Transformers. 

The paper is easy to understand and is well-structured. The experiments are comprehensive and justify theoretical insights.

### Weaknesses
1. The paper suffers from typos. The authors are encouraged to review and proofread the draft.
- Page 1: …*find progressively*…
- Page 2: …*novelly fuse*…
- Page 3: ..*have been proposed*… (multiple instances)
- Page 4: …*HMA*….
- Page 5: ….*orthoghonal*….

2. It is recommended that authors explore a better illustration for Figure 1. For instance, there is not much difference visually in Factorized mapping and Ordered Representation when printed in black/white. It might be helpful to provide a better illustration for the Ordered Dropout process (it is challenging to understand it with symbols without any reference in the figure caption. In current form, it is assumed that the readers will be familiar with OD). Since MAESTRO provides layer-wise decomposition and is generally applicable to various DNN layers, it might be useful to incorporate the various layer types of the DNN network (Sec 3.2) in Figure 1 as an overall summary of the proposed work and its applicability.

### Questions
Suggestions are provided in the above section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce Maestro, a technique designed for efficient layer-wise low-rank factorization during training. This method incorporates an ordered drop strategy combined with group lasso regularization, encouraging the progressive adoption of lower-rank weights during training. The evaluation is conducted on CIFAR10, MNIST, and Multi-30k, comparing Maestro against various low-rank approaches and several pruning and quantization techniques. Furthermore, the paper offers multiple ablation studies and provides theoretical analysis for specific problems.

### Strengths
1. The paper is easy to follow. 
2. The theoretical properties are sound with the proposed method.
3. The algorithm seems reasonable.

### Weaknesses
The algorithm seems reasonable to me. However, for the experiments, ImageNet results are missing. As an important benchmark, ImageNet is often used to compare performance between the compression-related tasks. For instance, Cutterfish presented their ResNet-50 results using the ImageNet dataset. To highlight effectiveness, it would be beneficial to include evaluations based on the ImageNet dataset. Additionally, tests on larger models would enhance the comprehensiveness of the study.

Is the #GMACs the training cost? If not, please show the training cost.

### Questions
How does the proposed method perform on ViT and other larger models using the ImageNet dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
