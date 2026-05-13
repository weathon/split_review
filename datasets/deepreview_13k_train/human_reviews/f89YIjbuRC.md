# Improving Nonlinear Projection Heads using Pretrained Autoencoder Embeddings

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
This empirical study aims at improving the effectiveness of the standard 2-layer MLP projection head $g(\cdot)$ featured in the SimCLR framework through the use of pretrained autoencoder embeddings. Given a contrastive learning task with a largely unlabeled image classification dataset, we first train a shallow autoencoder architecture and extract its compressed representations contained in the encoder's embedding layer. After freezing the weights within this pretrained layer, we use it as a drop-in replacement for the input layer of SimCLR's default projector. Additionally, we also apply further architectural changes to the projector by decreasing its width and changing its activation function. The different projection heads are then used to contrastively train and evaluate a feature extractor $f(\cdot)$ following the SimCLR protocol, while also examining the performance impact of $Z$-score normalized datasets. Our experiments indicate that using a pretrained autoencoder embedding in the projector can not only increase classification accuracy by up to 2.9\,\% or 1.7\,\% on average but can also significantly decrease the dimensionality of the projection space. Our results also suggest, that using the sigmoid and $\tanh$ activation functions within the projector can outperform ReLU in terms of peak and average classification accuracy. When applying our presented projectors, then not applying $Z$-score normalization to datasets often increases peak performance. In contrast, the default projection head can benefit more from normalization. All experiments involving our pretrained projectors are conducted with frozen embeddings, since our test results indicate an advantage compared to using their non-frozen counterparts.

\keywords{Nonlinear Projection Heads \and Multilayer Perceptrons \and Autoencoder Embeddings \and SimCLR Framework \and Contrastive Learning \and Representation Learning}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper improves the projection head in contrastive learning by incorporating pre-trained autoencoder embeddings. The experimental results validate that the pre-trained autoencoder is beneficial for extracting meaningful representations in the embedding layer.

### Strengths
The paper improves the projector by taking advantage of the autoencoder's ability to capture high-quality representations, which improves the performance of the contrastive learning method.

### Weaknesses
1) The biggest problem with this article is the lack of innovation. This article just experimentally verifies that swapping the initialization of the projected head in SimCLR for a pre-trained AE is effective. From this point of view, this article is more like an experimental report than an academic paper. I would suggest that the authors could give more insight or theoretical analysis to prove why this works.
2) The currently listed references only include 9 papers, which is an inadequate number. It is recommended that an in-depth analysis of existing related research be conducted further.
3) Unnecessary symbols in abstract and introduction should be avoided, such as projection head $g(\cdot)$ and feature extractor $f(\cdot)$. It is reasonable to introduce them in the method section to formally explain the concepts.
4) The logical narrative in the introduction section needs adjustment. It is better to first point out the role and limitations of existing projection heads. Subsequently, it is reasonable to propose using pre-trained autoencoder embedding as the initial weights for the projection head. 
5) The contributions in the introduction should be concise. For instance, the proposal of code should not be listed here.
6) In the final paragraph of related work, it is recommended to briefly discuss the differences between your work and the previously mentioned studies.
7) The experimental design provided is insufficient to explain how the projector is capable of generating high-quality representations. When evaluating the overall experiments, relying solely on classification accuracy on classification tasks as the evaluation metric may not provide a comprehensive understanding of the model's performance. To support the conclusions more robustly, it is advisable to incorporate additional evaluation methods such as t-SNE visualization.

### Questions
What is meant by the "high-level structure of the training data" in the discussion section, please give a more detailed description of it.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the impact of using pre-trained autoencoder embeddings within the SimCLR framework’s projection head to improve the quality of learned representations in self-supervised contrastive learning. The authors propose replacing the standard 2-layer MLP projector’s input layer with a trained autoencoder embedding while applying different activation functions and architectural modifications. They evaluate these changes on five well-known image classification datasets.

### Strengths
1. The experiments conducted could be a good reference for industry applications that don't want to fine-tune the whole framework. 
2. The method is very simple and direct.

### Weaknesses
1. Novelty: The paper lacks a deeper theoretical explanation of why pre-trained autoencoder embeddings enhance performance. The observed benefits are primarily justified through empirical evidence.  Also, similar ideas have been applied to many industry scenarios during the last five years. As long as it is a projection layer, is there too much difference between the MLP layer and AE?

2. The experiments are too limited to make such a big claim. The datasets implemented are mostly STL10, CIFAR10, etc, which is too simple and the scale is too limited to support its claim. Some differences will not stand if scaled up to a larger dataset.

### Questions
1. How would your approach scale to larger image datasets or different domains?
2. What are the trade-offs between freezing and fine-tuning the autoencoder embeddings, and could there be scenarios where fine-tuning might be beneficial?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is an empirical study to improve the effectiveness of the standard 2-layer MLP projection head featured in the SimCLR framework by pretrained autoencoder embeddings. The paper’s result show accuracy improvements and dimensionality reductions using the modified nonlinear projection heads in image classification tasks.

### Strengths
- An interesting setting in contrastive learning: optimizing projection head performance.
- Investigated the hypothesis of whether pretrained autoencoder embeddings are able to improve the performance of the standard 2-layer MLP projection head used in the SimCLR framework.
- The paper provided empirical evaluation results on several datasets.

### Weaknesses
 - The background introduction, including SimCLR, autoencoders, pretraining autoencoder embeddings, etc, seems too long in the paper. The author can provide a short summary of this and move the detailed background introduction to the appendix.
- Following the above, the paper lacks a theoretical statement for replacing the SimCLR projection head with autoencoder embeddings. It seems unclear why this approach should theoretically enhance SimCLR's representation quality. The authors reported empirical results in the paper, which is good, but beyond that, it would be good to provide a theoretical analysis.
- The paper included the results on five image datasets. However, it seems unclear why those datasets were selected. The dataset selection could introduce biases, which may impact generalizability.
- It would be good to discuss why SimCLR was selected, as there are more new projection head designs. Or discussions about why the nonlinear nature of the SimCLR projector is beneficial. If SimCLR is not a specific choice, then maybe some ablation study on other projection heads or CL methods can be investigated to see if the findings on SimCLR can be generalized to other models.

### Questions
Please see the comments above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studies in depth about the projection head of SimCLR. The author suggests replacing the conventional projector with a pretrained shallow autoencoder could improve the performance of the trained model.

### Strengths
- The paper is well-written and easy to follow.

- The method is quite simple and easy to implement.

- The improvements are quite good

### Weaknesses
 - First of all, the paper mostly looks like a technical report paper, it lacks the strong idea and results to make it novel.

- The experiments were only conducted with small-scale datasets and lacked a comparison with a large family of self-supervised learning.

- There are no consistent patterns of the number of dimensions, activation function, normalization, etc that could be followed, depending on the dataset, we need to run a bunch of trials to see which combination works best.

- Does the number of layers in the autoencoder affect the performance?

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
