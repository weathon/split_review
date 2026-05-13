# Components Beat Patches: Eigenvector Removal for Robust Masked Image Modelling

- Decision: Reject
- Scores: 8, 3, 8, 3

## Abstract
Masked Image Modeling has gained prominence as a powerful self-supervised learning approach for visual representation learning by reconstructing masked-out patches of images. However, the use of random spatial masking can lead to failure cases in which the learned features are not predictive of downstream labels. In this work, we introduce a novel masking strategy that targets principal components instead of image patches. The learning task then amounts to reconstructing the information of masked-out principal components. The principal components of a dataset contain more global information than patches, such that the information shared between the masked input and the reconstruction target should involve more high-level variables of interest. This property allows principal components to offer a more meaningful masking space, which manifests in improved quality of the learned representations. We provide empirical evidence across natural and medical datasets and demonstrate substantial improvements in image classification tasks. Our method thus offers a simple and robust data-driven alternative to traditional Masked Image Modelling approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the problem of Masked Image Modeling, which classically entails masking out patches of pixels within input images and training a model to reconstruct these missing values based on the visible pixels in a self-supervised fashion. The authors propose a novel alternative to the masking of pixel patches, instead suggesting that the data first be transformed into a latent subspace i.e. projected onto its principal components, and masking operations be done on the component level instead of pixel level. The idea is that because the principal components can represent global correlations, masking individual components still retains information at some level of all pixel locations, as opposed to the masking of entire patches of pixels, which could remove e.g. an entire object. In essence, this allows the model to still be exposed to information from all pixel locations during training, leading to robust representations that are more likely to contain meaningful information needed for downstream tasks, e.g. classification. The approach, termed PMAE, is evaluated against the vanilla Masked Autoencoder in an extensive set of experiments for image classification on multiple natural and medical image sets, showing clear and often significant improvement in nearly all settings.

### Strengths
- Originality

The proposed method is a relatively straightforward combination of previously established approaches, but integrated in a novel, clever, and elegant way. 


- Quality

The authors provide a thorough review of previous research leading to and motivating this work, as well as a nice discussion of the broader context of related research. 

Results support claims made throughout the paper.



- Clarity

The paper is very well written and easy to follow; the foundations are solid and motivation is clear.


- Significance

The proposed method avoids extensive hyperparameter tuning, known to be challenging in established MIM/MAE regimes, as ratio / size of image patches masked strongly influences performance on different  downstream tasks.  Experiments presented using MAEs parameterized with range of masking ratios highlight this -- training models with the standard convention of masking $75$% of image patches often results in poorer classification accuracy, suggesting the necessity of tuning beyond this accepted norm. 
In contrast, PMAE doesn't require much hyperparameter tuning and seems to perform quite well straight off the shelf.


The idea is simple yet solid, even drawing intuitions from early research in image processing / Eigenfaces, which I can imagine inspiring future/new directions in representation learning.

### Weaknesses
I wonder about the scalability of PMAE when applied to larger images, with the potentially prohibitive costs of the eigendecomposition, e.g. $o(pixels^3)$. Could the method still perform well with low-rank approximations?

Some of the presented results are a bit unclear to me, see 'questions'.

### Questions
In the experiments exploring effects of masking ratios, as I understand it in the $PMAE_{rd}$ case, a random percentage of variance between $[10,90]$ is masked. I'm a bit confused as to why in Figure 5, which presents the impact of masking percentage, the classification accuracy results only shown for percentages between $[10, 50]$. What happens when a higher percentage of variance is masked?

How do you anticipate PMAE would perform with nonlinear transformations, e.g. kernelized PCA with an RBF kernel?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposed a new masked strategy based on principal component analysis, in order to capture more global information. The auto-encoder is employed to reconstruct the masked-out components. Experiments are conducted on various datasets.

### Strengths
This paper is well organized and written. The perspective of masking principle components is interesting.

### Weaknesses
It does not make sense to me that we can recover removed principal components from other components. This is because unlike patches, these principal components are orthogonal to each other, meaning they are linearly independent. It is unreasonable to say we can recover a random variable X from another random variable Y when they are orthogonal in the feature space. While non-linear relationships might exist, the authors do not specify the conditions under which such a reconstruction is possible or provide a theoretical justification for why a non-linear autoencoder would be able to reliably reconstruct these masked components. This lack of theoretical grounding is a major concern.

Besides, reporting experimental results on ImageNet would be more convincing.

### Questions
None.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new approach to pre-training neural networks in the context of masked image modelling. Instead of masking out random patches in the image, the authors propose a masking strategy in which the principal components of the image are masked out and the networks are then trained to recover these principal components. The paper empirically demonstrates the advantage of this approach on natural and medical images in the context of image classification.

### Strengths
- The idea for the masked image modelling strategy is simple and intuitive. It is presented in an easy-to-follow fashion.
- The paper is generally well-written and clear (except for the points below).
- The evaluation strategy is solid.
- The use of SOTA baselines is good.

### Weaknesses
 - The idea of using PCA as an invertible transformation into a latent space is sensible, however there many alternative choices for such a transformation (e.g. Fourier or wavelet transforms).
- The evaluation scenario focuses on classification as a downstream task. This is typically a task that relies on global information. However, other downstream tasks, such as object detection or semantic segmentation, require local information, and here, the proposed may perform less well. However, this is not tested.
- The datasets used for evaluation contain very small images (e.g. CIFAR10, MedMNIST)

### Questions
- The method uses a lossless scenario for the PCA. The rationale for this is understandable, but I am wondering if this leads to practical problems (e.g. for very small eigenvalues, their ordering becomes random, etc.)?
- Why not evaluate other similar transforms (e.g. Fourier or wavelet transforms)? 
- How would the pre-training perform on large, high-resolution images?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a variant of the masked autoencoder where instead of masking a subset of image patches, they mask a subset of principal components. They assume that the masked and unmasked principal components are likely to be correlated in a way that is pertinent to the class, which improves downstream classification performance.

### Strengths
The paper is well-written, and provides a clear and agreeable motivation for masking principal components instead of image patches.

### Weaknesses
The main purpose of self-supervised learning is to learn a representation that can be fine-tuned to achieve **strong** downstream performance. This is not demonstrated in this paper. Putting it bluntly, it is not compelling to achieve ~60% accuracy on CIFAR10 and ~20% accuracy on TinyImageNet. Instead of using significant resources to train a vision transformer with this approach, it's more practical to train a small convolutional net to achieve higher performance.

In the original masked autoencoder paper, the authors demonstrate very strong downstream performance on ImageNet1k (not the tiny version), which makes their approach compelling. In light of this, the fact that MAE allegedly performs so poorly on CIFAR10 and TinyImageNet is a bit suspicious. If it is indeed the case that MAE performs poorly on smaller images, we still need to see PMAE do similarly well on ImageNet1k, but these experiments are not in the paper.

### Questions
Can you explain why it makes sense for MAE to achieve near-SOTA performance on ImageNet1k in the original paper, but performs so poorly on the simpler datasets CIFAR10 and TinyImageNet?

As stated in "weaknesses," I think we need to see PMAE's performance on ImageNet1k to reach a conclusion about it's superiority over MAE.

### Soundness
2

### Presentation
3

### Contribution
1
