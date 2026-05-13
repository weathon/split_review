# Coloring Deep CNN Layers with Activation Hue Loss

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
This paper proposes a novel hue-like angular parameter to model the structure of deep convolutional neural network (CNN) activation space, referred to as the {\em activation hue}, for the purpose of regularizing models for more effective learning. The activation hue generalizes the notion of color hue angle in standard 3-channel RGB intensity space to $N$-channel activation space. A series of observations based on nearest neighbor indexing of activation vectors with pre-trained networks indicate that class-informative activations are concentrated about an angle $\theta$ in both the $(x,y)$ image plane and in multi-channel activation space. A regularization term in the form of hue-like angular $\theta$ labels is proposed to complement standard one-hot loss. Training from scratch using combined one-hot + activation hue loss improves classification performance modestly for a wide variety of classification tasks, including ImageNet.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced several observations based on the nearest neighbor indexing of feature vectors of pre-trained networks. They show that class-informative activations are connected with a hue-like angular $\theta$. They further propose a regularization term for the training of classification model.

### Strengths
1. The presentation is clear and easy to follow. 
2. The method is well-motivated and novel. The analysis is interesting and insightful. 
3. The evaluation and visualization is extensive and interesting.

### Weaknesses
1. The experiments are conducted with traditional architectures. How about applying the proposed method for training more advanced architecture, such as Vision Transformer?
2. There are already some well-known techniques based on the similarity of activation vectors, such as label smooth. I think the related methods should be compared or discussed. 
3. The extra regularization term seems to introduce extra computation costs. I think the comparison of computation should be presented.

### Questions
See the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel angular parameter, referred to as the activation hue, that models the structure of deep convolutional neural network (CNN) activation space for more effective learning. This activation hue generalizes the concept of the color hue angle in the standard 3-channel RGB intensity space to an N-channel activation space. Based on observations from nearest neighbor indexing of activation vectors with pre-trained networks, the authors suggest that class-informative activations are concentrated about an angle θ in both the (x,y) image plane and in multi-channel activation space. They propose a regularization term using these hue-like angular labels alongside standard one-hot loss. This combined approach modestly improves classification performance across a variety of tasks, including ImageNet.

### Strengths
1. The introduction of the activation hue is an innovative way to regularize the structure of CNN's activation space, which may lead to improved model performance for CNN architecture. The generalization of the notion of color hue to N-channel activation space is an interesting concept that could have broad applications in the field.
2. The combined use of one-hot loss and activation hue loss has been shown to modestly improve classification performance across a variety of classification tasks with ResNet-18 / EfficientNet-B0.

### Weaknesses
1. The paper does not provide evaluation results by properly scaling the employed models, e.g., applying the approach to ResNet-50 or a larger one. Thus, it is difficult to assess the extent of improvement brought by the proposed method. Specifically, the absence of results on larger models leaves open the question of whether the observed improvements are merely a characteristic of the smaller architectures tested, or if the activation hue regularization can provide benefits on more complex models with higher capacity. It's crucial to determine if the method's effectiveness scales with model size, as this directly impacts its practical applicability.
2. The proposed activation hue's properties should be discussed along with experiments. Will it improve the CNN network converge, or make it robust to some perturbations? The paper lacks a thorough analysis of the activation hue's impact on the training dynamics. For example, does the hue-based regularization lead to faster convergence, or does it make the model more resilient to adversarial examples or noisy inputs? These are essential properties that must be investigated to understand the method's behavior and potential limitations.
3. More results about employing the given method to downstream tasks, e.g., detection, and segmentation, will further validate its effectiveness and generality. The current evaluation is limited to classification tasks. To demonstrate the broader applicability of the activation hue, it is necessary to evaluate its performance on tasks such as object detection and semantic segmentation. These tasks involve different types of data and require different network architectures, and testing on these would provide stronger evidence for the method's generalizability.
4. The complexity of the introduction of the novel hue-like parameter to the model architecture and training process should be discussed. The paper should provide a more detailed analysis of the computational overhead introduced by the activation hue. This includes the number of additional parameters, the increase in training time, and the memory requirements. A clear understanding of the computational cost is necessary to assess the practical implications of the proposed method.

Minor issues:
1) There may exist some misuse between \cite and \citep as some citation formats seem improper in the paper.

### Questions
1. Can you explain in more detail how the hue-like parameter was implemented in the model architecture? It would be better to give its code.
2. Table 1 shows that the given method yields better performance in fine-grained classification than that in common ones. Any further explanations for them?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an activation method inspired by concepts found in metric learning, contrastive learning, and image retrieval. Instead of using a straightforward activation function, the proposed approach relies on measuring similarity to the nearest image's activation. The paper further supports this method with four key observations.
However, I have some concerns as follows:

1)	The proposed method relies on the assumption that target objects consistently occupy the center of activated feature maps. This assumption may be overly restrictive and should be thoroughly validated. If this assumption holds true, it suggests that using center-cropping techniques could potentially enhance network performance.

2)	Furthermore, the method also assumes that all objects are small enough to fit within a limited area at the center of the image. It's important to note that these two assumptions may not always hold in real-world scenarios, and there are many cases where objects are not confined to the center or are not small enough to fit within this region. These assumptions might not be universally applicable.
3)	Remarkably, the paper includes only one experiment demonstrating the benefits of the proposed method. However, to provide a more comprehensive understanding and build a convincing case for its adoption, it is essential to include in-depth analyses alongside the reported benefits.

4)	Additionally, the paper primarily focuses on comparisons in few-shot learning scenarios, even though the proposed method isn’t designed for the specific cases. To ensure fair and comprehensive comparisons, it is advisable to evaluate the proposed method against a naïve activation function using the full dataset, not limited to few-shot learning scenarios.

5)	The paper appears to lack sufficient comparisons with prior works, and it seems that the authors may have faced challenges in categorizing the proposed method and identifying relevant prior research. It would enhance the paper's contribution to the field if it included a more extensive comparative analysis with existing methods, even if the proposed approach doesn't neatly fit into existing categories. This would provide a clearer context for evaluating its novelty and effectiveness.

### Strengths
See above

### Weaknesses
1)	The proposed method relies on the assumption that target objects consistently occupy the center of activated feature maps. This assumption may be overly restrictive and should be thoroughly validated. If this assumption holds true, it suggests that using center-cropping techniques could potentially enhance network performance.

2)	Furthermore, the method also assumes that all objects are small enough to fit within a limited area at the center of the image. It's important to note that these two assumptions may not always hold in real-world scenarios, and there are many cases where objects are not confined to the center or are not small enough to fit within this region. These assumptions might not be universally applicable.

3)	Remarkably, the paper includes only one experiment demonstrating the benefits of the proposed method. However, to provide a more comprehensive understanding and build a convincing case for its adoption, it is essential to include in-depth analyses alongside the reported benefits.

4)	Additionally, the paper primarily focuses on comparisons in few-shot learning scenarios, even though the proposed method isn’t designed for the specific cases. To ensure fair and comprehensive comparisons, it is advisable to evaluate the proposed method against a naïve activation function using the full dataset, not limited to few-shot learning scenarios.

5)	The paper appears to lack sufficient comparisons with prior works, and it seems that the authors may have faced challenges in categorizing the proposed method and identifying relevant prior research. It would enhance the paper's contribution to the field if it included a more extensive comparative analysis with existing methods, even if the proposed approach doesn't neatly fit into existing categories. This would provide a clearer context for evaluating its novelty and effectiveness.

### Questions
See above

### Soundness
1 poor

### Presentation
2 fair

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
The paper proposes an angular based distance for regularizing activation maps of neural networks. It starts from a set of observations and significant improvements are claimed on a variety of models and benchmarks.

### Strengths
The idea of regularizing activation maps based on nearest neighbor information is interesting. The structure of the maps will also lead to better understanding of the CNN.

### Weaknesses
1. Results.  The paper proposes an improvement to the current standard of approaching CNN and superior performance is critical in arguing the value of the idea. While results from table 1 show significant improvement, they are arguable. For instance in this paper ( https://arxiv.org/pdf/2110.00476v1.pdf ), there are reports, using the same architectures,  of significantly better results. Given that baseline better results are achievable with known techniques, the improvement is shadowed by the probability that the overall technique used in training CNN is flawed and the proposed idea recover only some of the flaws. 

While I might miss a point and there can be a major difference between this paper and the reference mentioned, thus they are not comparable, this paper must refer to outside sources while establishing baselines. The databases are standard and so are the architectures, therefore other papers should have reported the accuracy for some, if not all the cases.

2. Presentation - is not clear and I have problems understanding the method. A critical aspect is that the proposed loss is not explained clearly. :
 - Page 8 "We thus propose a novel loss function leveraging activation hue, that may be used as a training signal in the (x, y) image plane of arbitrary CNN layers, most notably bottleneck layers with minimal spatial extent". Emphasis on arbitrary.
 - equation (4) and (5) are written for  final layer only!?


3. The paper might benefit from a revision:
 - table 1 Resnet 18 - Cars - huge difference between results

### Questions
1. Please explain better how the proposed loss is implemented
2. The critical questions is about comparison: is the mentioned reference relevant? If not can we find another paper establishing baselines for the tests?  
3. This is more a suggestion but it would be better to focus on a set of architectures and use over the entire paper. Now some models are used in explanations, others in evaluation and the paper is not convincing. "Similar improvements were observed with a variety of different network architectures including VGG, Inception v3, DenseNet" - results could have been shown as additional material.

=======================
Post rebuttal feedback

I have read the author feedback and rebuttal. While some clarification has been added and issues about method details have been dealt with, the relative value of standard methods have not been alleviated. I view this a significant problem and thus I am keeping my initial recommendation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
