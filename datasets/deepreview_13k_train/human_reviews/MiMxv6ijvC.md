# CARENET : A NOVEL ARCHITECTURE FOR LOW DATA REGIME MIXING CONVOLUTIONS AND ATTENTION

- Decision: Reject
- Scores: 3, 3, 3, 1

## Abstract
In the rapidly evolving landscape of deep learning for computer vision, var-
ious architectures have been proposed to achieve state-of-the-art performance
in tasks such as object recognition, image segmentation, and classification.
While pretrained models on large datasets like ImageNet have been the corner-
stone for transfer learning in many applications, this paper introduces CAReNet
(Convolutional Attention Residual Network), a novel architecture that was trained
from scratch, in the absence of available pretrained weights. CAReNet incorpo-
rates a unique blend of convolutional layers, attention mechanisms, and residual
connections to offer a holistic approach to feature extraction and representation
learning. Notably, CAReNet closely follows the performance of ResNet50 on
the same training set while utilizing fewer parameters. Training CAReNet from
scratch proved to be necessary, particularly due to architectural differences that
render feature representations incompatible with those from pretrained models.
Furthermore, we highlight that training new models on large, general-purpose
databases to obtain pretrained weights requires time, accurate labels, and pow-
erful machines, which causes significant barriers in many domains. Therefore, the
absence of pretrained weights for CAReNet is not only a constraint but also an op-
portunity for architecture-specific optimization. We also emphasize that in certain
domains, such as space and medical fields, the features learned from ImageNet
images are vastly different and can introduce bias during training, given the gap
that exists between the domains of pretraining and the task of transfer learning.
This work focuses on the importance of architecture-specific training strategies
for optimizing performance and also demonstrates the efficacy of CAReNet in
achieving competitive results with a more compact model architecture. Experi-
ments were carried out on several benchmark datasets, including Tiny ImageNet,
for image classification tasks. Signifying a groundbreaking stride in efficiency
and performance, CAReNet not only outpaces ResNet50 by achieving a lead of
2.61% on Tiny-Imagenet and 1.9% on STL10, but it does so with a model that’s
nearly half the size of ResNet50. This impressive balance between compactness
and elevated accuracy highlights the prowess of CAReNet in the realm of deep
learning architectures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presented aims to integrate the concept of a Convolutional ResNet with an Attention network to attain comparable recognition accuracy using fewer parameters. The proposed layer, referred to as CAReNet, is incorporated into the final convolutional block. Specifically, CAReNet utilizes an Attention block in both grid and window configurations to execute the task. The overall performance of the model is compared with that of ResNet, VGG, Max Vit, and CoatNet in terms of top-1 accuracy using small datasets.

### Strengths
Investigating the convolutional-based attention network might look interesting, but I think the paper is not ready for publication yet. Please see my comments below.

### Weaknesses
While have utmost respect for the work submitted and I hope my comments will assist the authors in fortifying their paper:


- The motivation for integrating Convolution with Attention within the proposed method requires clearer articulation. The current manuscript does not sufficiently convey the intuition or the rationale for this combination. Specifically, how does the proposed CAReNet layer leverage the strengths of both convolutional and attention mechanisms to achieve improved performance or efficiency? What specific limitations of existing architectures does this integration aim to address?

- The literature review appears to be incomplete, lacking references to several pertinent studies. For instance, a notable omission is the Convolutional vision Transformer (CvT). I recommend the authors expand this section to provide a more comprehensive background.

- While it is acknowledged that the addition of an attention layer to convolution blocks can expedite convergence in certain image classification tasks, this does not directly demonstrate the efficiency of the proposed method from a parameter-count perspective. A more detailed analysis is required to substantiate the method's effectiveness. For example, a comparison of the theoretical computational complexity (e.g., FLOPs) of CAReNet against ResNet and other baselines would be beneficial.

- The clarity of the paper's presentation needs improvement. For instance, the captions of figures and tables lack essential details, making it difficult to fully understand the results presented. Figure captions should clearly state what is being depicted, the experimental setup, and the key takeaways. Table captions should provide sufficient context, including the dataset used, the evaluation metric, and a brief description of the models being compared.

- The evaluation of the model on only three small datasets does not provide a robust validation of its capabilities. A more extensive evaluation, including additional and larger datasets, would be more convincing. Specifically, the inclusion of a benchmark dataset like ImageNet-1K is crucial for assessing the scalability and generalizability of the proposed method.

- The current evaluation presented in Table 3 does not convincingly demonstrate the model's effectiveness. For example, the marginal improvement over ResNet18 on the MNIST dataset, despite a higher parameter count, calls into question the practical benefits of the proposed method. A more thorough analysis of the trade-offs between accuracy and parameter count is needed. Furthermore, reporting additional metrics beyond top-1 accuracy, such as top-5 accuracy, precision, recall, and F1-score, would provide a more comprehensive evaluation.

- The paper would benefit greatly from an ablation study, particularly one that investigates the impact of removing the CAReNet block, to discern its actual contribution to the model's performance. This could involve comparing the performance of a model with and without the CAReNet block on the same datasets and under the same experimental conditions.

- For work of this nature, it is crucial to assess performance on larger-scale datasets to ensure the model's effectiveness and generalizability. As mentioned previously, evaluating the model on ImageNet-1K would be a crucial step in this direction.

In the limitations section, numerous questions were raised; however, there still remain some unclear points in the paper. For example, it is quite surprising that VGG16, with ten times the number of parameters, only achieves 10% accuracy on the STL10 dataset. This result is counterintuitive, considering VGG16's established performance on various image recognition tasks. I strongly suggest the authors rigorously investigate this anomaly and discuss whether there might be an error in the reported results or if there are underlying factors that could explain this unexpected outcome. A more detailed explanation would greatly enhance the credibility and scholarly rigor of the work. Specifically, the authors should verify the data preprocessing steps, model implementation, and training procedure for VGG16 on STL10 to rule out any potential errors.

### Questions
In the limitations section, numerous questions were raised; however, there still remain some unclear points in the paper. For example, it is quite surprising that VGG16, with ten times the number of parameters, only achieves 10% accuracy on the STL10 dataset. This result is counterintuitive, considering VGG16's established performance on various image recognition tasks. I strongly suggest the authors rigorously investigate this anomaly and discuss whether there might be an error in the reported results or if there are underlying factors that could explain this unexpected outcome. A more detailed explanation would greatly enhance the credibility and scholarly rigor of the work.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new architecture named CARENet for the tasks of image classification in the low-data regime. They propose an architecture and claim that their architecture design leads to smaller models which are parameter efficient, and perform well when trained from scratch on datasets in the low-data regime.

### Strengths
- The authors have well-framed and well-motivated their problem in the Introduction of making models that work well for low-data regimes. They also partially well-motivate how their problem formulations are important as opposed to pre-training models on large datasets.

### Weaknesses
 - The authors mention that:

> While these Transformer-based models have shown remarkable promise, they are not without their
challenges, particularly when it comes to computational efficiency and the ability to scale.

I believe that the authors start talking about addressing a different problem than what they propose in the introduction. We know that ConvNets scale well especially shown with BiT [1] and other works however it has also been shown that Transformer-based models are comparatively easier to scale, and more memory memory-efficient [2] (especially see Figure 12). Transformer-based models do have their challenges and the authors identify most of them well, however, I think the way they start talking about these problems is a weakness or if this is what they meant, they should also reflect this in their experiments.

- A huge weakness of this paper is that the authors only present a new architecture: this new architecture uses fairly popular and standard methods of building architecture and is not something novel at all. They also introduce a CARENet block which is comprised of a bottleneck block followed by an attention mechanism operating in parallel across both grid and window patterns, however, this is also rather standard, and (shifted) window/local attention has been immensely popularized by [3], and approaches similar to their CARENet block have been used multiple times, popularly in [4]. I believe the construction of their architecture or their method itself is not novel.

- The authors loosely mention these aspects while explaining their architecture:

>  offering enhanced feature extraction capabilities

>  designed to bolster information flow

> empower the model to learn profounder representations

> refine the spatial hierarchy of the feature maps

Not only the benefits they propose are not written down succinctly and clearly but are also not benefits that come with "their" work or their way of putting together these architectures, these are rather fairly popular and standard approaches to building models.

- The method itself might not come across as novel or does not present any important theoretical insight in the formulation of the network. In these cases, one might look toward the paper in this case at the very least explain how such a small change should lead to better properties or in general for applying some method to a unique context, and the only way to show this due to lack of the earlier 2, I feel should be results which in this case should be well compared and contrasted with other methods and not leave questions in the mind of a reader. However, the authors do neither of these.

- I thoroughly disagree with the authors on this,

> In this study, we leverage a diverse set of benchmark datasets to rigorously evaluate the performance and robustness of our proposed models.

Their experiments are not indeed diverse or large in number, they evaluate on STL10, Fashion Mnist, Mnist, and Tiny-Imagenet which is not a diverse set of datasets.

- The authors present that their model is superior or at par with other models trained without extra data however this is not true, and they only reported the performance of some models. For instance, in the case of Tiny Imagenet, there are more than 10 different models [5] trained on the same amount of data that perform better than CARENet but these are not even cited or compared in the paper. Considering this, their results get severely diminished with the lack of clarity around STL-10 results (see questions) and the lack of proper comparisons for Tiny ImageNet. Given this I would also suggest changing,

> The presented results furnish an in-depth comparison among several cutting-edge neural networks
architectures

Maybe parameter efficiency could indeed be something you work toward,

> The Tiny-Imagenet dataset results present an interesting paradigm. MaxVit outperforms other architectures with a 58.28% accuracy but CAReNet, with nearly half the model size of MaxVit, closely
follows with an accuracy of 54.4%

However, still, the results need to be well-explained and compared with SoTA models. The authors should modify or instate a new problem statement if they are indeed trying to work toward parameter efficiency.

- The authors mention that they build a robust architecture,

> Across the board, on datasets such as Fashion Mnist and Mnist, CAReNet maintains an enviable performance, with accuracies nearing 95% and surpassing 99% respectively. Such consistent achievements, despite its smaller model footprint, underscore the robustness of CAReNet’s design.

However, the experiments are not diverse enough and do not span multiple tasks or multiple kinds of dataset settings to state that the model design is in fact robust.

- With multiple modern models to the same means,

> Signifying a groundbreaking stride in efficiency
and performance, CAReNet not only outpaces ResNet50 by achieving a lead of
2.61% on Tiny-Imagenet

I disagree with the authors belief that an improvement over ResNet50 signifies a "groundbreaking stride".

### Questions
- There seems to be some mistake with the title, "CARENET : A NOVEL ARCHITECTURE FOR LOW DATA REGIME MIXING CONVOLUTIONS AND ATTENTION **CONFERENCE SUBMISSIONS**"
- I would recommend the authors follow the problem that they clearly define for the related works, they include SimCLR in their related works section which does present a solution for having less labeled data however this is not the problem that the authors define. However, the authors do not mention how SimCLR or any self-supervised learning algorithms solve a different problem and that their problem formulation is different than these. I think this could be fixed with a rewrite of related works and organizing it better.
- I would recommend the authors reorganize their methods section as well, the components they talk about or fairly common components, and more importantly they should not need to go into such depth into each component in the main text especially when an understanding of these components is not crucial for the reader to understand how your method is novel.
- I do not understand how "Model size (MB)" has anything to do with the problem you define and why it would show up in the main table in the paper?
- Could the authors clarify how they use STL-10, their method indicates that their approach is designed only for labeled data, do they simply use the labeled subset of STL-10 and how are other models compared for STL-10?
- I assume in Table 1 none of the models use extra data?
- I could not help but wonder why authors left out CIFAR-100 from their comparisons while it is supposed to be more challenging than MNISt and Fashion-MNIST?
- I do not think the work shows this aspect

> This work focuses on the importance of architecture-specific training strategies

there is no talk at all about specific new training strategies or training strategies that are modified for this architecture and there are also no experiments to show this?

### Minor formatting issues:

- These

> including VGG Simonyan & Zisserman (2014) and ResNet He et al.
(2015)

> Squeeze-and-Excitation (SE) layers Hu et al. (2018)

> Transformers Vaswani et al. (2017)

among others shouldn't use in-text citations.

- The number of parameters should for this scale of models be in millions for readability.
- There seems to be a typo with "Tiny-Imagenet (ours)" which in this context indicates that this paper introduced TI.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new network design named CAReNet that incorporates convolutional layers, attention mechanisms,, and residual connections. They focus on network-specific training strategies and the conducted experiment results show the relative improvements to some modern network designs.

### Strengths
1. The authors carefully review the different elements of the proposed network and reassemble them into a more compact network.
2. The experiments on STL10, Mnist, Tiny-ImageNet demonstrates the effectiveness and its efficiency in terms of parameters.

### Weaknesses
1.Limited novelty. While the paper brings forward a new model design, its foundation lies in leveraging existing techniques. As a result, its contribution is incremental and not enough for establishing a distinct and well-designed model architecture.

2.The experiment comparisons are not convincing enough. The performances are similar to ResNet18 on most datasets and does not show significant superiority. Moreover, the compared methods do not include more modern architectures, such as Swin-T [1], ResNeXt [2], ConvNext [3].

3.Scaling potential. To comprehensively evaluate the network performance, the experiments should be included to show it can be extended to large-scale dataset, such as ImageNet-1k. Demonstrations of its adaptability to broader downstream vision tasks would also be beneficial.

4.Lacking ablations. The paper could be further strengthened with an ablation study. This would offer clarity on how specific components of the proposed design contribute to performance enhancements.

### Questions
Please consider to answer the above questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors proposes an architecture for computer vision: a self-attention layer on top of a convolutional network. They claim this is novel, and evaluate on MNIST, Fashion MNIST, STL-10 and Tiny-ImageNet. Their network performs roughly on par with a typical ResNet (better on STL, worse on all other datasets), but has less parameters than a ResNet 50.

### Strengths
**Originality**: Putting a Self-Attention Layer on top of a CNN is not novel, and has been proposed many times before (e.g. even in the original Vision Transformer )

**Quality**: The empirical work is poor: Previous work on the same topic is not cited, some prior work is mis-attributed. While the work claims to be targeted towards low-data regimes, it compares only to baselines known to be data-hungry. It does not compare to comparable architectures. There are no error bars even for small scale experiments.

**Clarity:** The work leaves open many questions: the manuscript not explain deviations from standard designs, and talks more about datasets that are well known in the community instead of architectural decisions. Their main contribution is described in a single line short sentence (see "Weaknesses" below).  Numbers in the results are misrepresented to be significant even though they are actually worse.

**Significance:** As far as can be seen from the empirical results, the work is of minor significance.

### Weaknesses
Novelty: Variants of this architecture have been proposed many times over. See e.g. the "Related Work" section in the Vision Transformer paper by Dosovitskiy et al. 2021 for some links

Misleading presentations: Table 1 has all of the results for the proposed method boldened. This is usually done to indicate significantly better results, or at the very least BETTER results as comparable methods. The method proposed here is oftentimes performing worse than the competitors, and the use of boldface is misleading, as it is not in line with the norms of the community. 

Clarity: The architectural decisions are extremely unclear. No time is spent to give intutions, or even ablations for the concrete choices made. For example:
* The bottleneck blocks used in this work seem fairly similar to ResNet Bottlenet blocks, but have an additional Convolution at the end. No explanation is given for this, it would be nice to have one.
* CAReNeT attention is merely described as "an attention mechanism operating in parallel across both grid and window patterns". I do not understand what that means -- What is a window pattern, what does it mean to be parallel across grids and windows? This is the paper's main contribution, so a lot more explanation should be devoted to it.
* The "Residual Blocks" in the Figure 1 seem to always be downsampling. Why is that? It would be nice if Figure 1 could also point out intermediate resolutions to better understand when & by how much the resolution is reduced.

Significance: Variations of this model were proposed many times before. It is unclear if there is anything special about this version. The experiments do not compare to similar architectures from the literature (again: see the ViT paper for references), so it's unclear if it performs better than those. Table 1 show nice results on STL-10, but the paper does not investigate why this is. Why does CAReNeT perform so well here? Is this due to attention, or due to something else in the architecture? What other applications could benefit from this?

Smaller remarks:

"The fusion of Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) Khan et al. (2022) presents a groundbreaking approach to image classification"   ==> Khan et al., did not introduce ViT's, nor the fusion of CNNs and ViTs. Both where done by A. Dosovijtsky et al., (2021) (or references therein), please correct this citation.

### Questions
I have no questions

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
