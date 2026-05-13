# Bilinear MLPs enable weight-based mechanistic interpretability

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
A mechanistic understanding of how MLPs do computation in deep neural networks remains elusive. Current interpretability work can extract features from hidden activations over an input dataset but generally cannot explain how MLP weights construct features. One challenge is that element-wise nonlinearities introduce higher-order interactions and make it difficult to trace computations through the MLP layer. In this paper, we analyze bilinear MLPs, a type of Gated Linear Unit (GLU) without any element-wise nonlinearity that nevertheless achieves competitive performance. Bilinear MLPs can be fully expressed in terms of linear operations using a third-order tensor, allowing flexible analysis of the weights.
Analyzing the spectra of bilinear MLP weights using eigendecomposition reveals interpretable low-rank structure across toy tasks, image classification, and language modeling. We use this understanding to craft adversarial examples, uncover overfitting, and identify small language model circuits directly from the weights alone. Our results demonstrate that bilinear layers serve as an interpretable drop-in replacement for current activation functions and that weight-based interpretability is viable for understanding deep-learning models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work provides an in-depth analysis of Bilinear Multilayer Perceptrons (MLPs). 
Bilinear MLPs use bilinear transformations to achieve nonlinearity for function approximation.
The analysis focuses on the spectral decomposition of the bilinear MLP weights. 
This reveals the low-rank structure of the weights and provides insight into crafting adversarial samples, overfitting, and so on. 
The low-rank structure is interpretable and shows that components corresponding to small eigenvalues can be removed while preserving performance.
The work provides an explainable framework, which would be difficult to achieve without bilinear weights because of the use of nonlinear activation functions.
The paper provides experimental results to support its claims.

### Strengths
ORIGINALITY:
This work distinguishes itself from existing approaches to interpretable neural networks by using a unique characteristic of bilinear MLPs. While previous works have utilized bilinear MLP networks, this paper uniquely demonstrates how to exploit their inherent differences from other MLPs to achieve interpretable neural networks.

SIGNIFICANCE:
Interpretable AI is crucial for understanding how AI models encode information. 
This work offers a new framework for interpretable neural networks, with the potential to significantly advance the field.

QUALITY:
The quality of this work is good. It provides relevant information to support its claims. The experimental results sufficiently support the main claims in this paper.

CLARITY:
This paper is well-written. It provides enough information required to put this work into proper perspective. It is also well organized and provides enough background information needed to understand the main components of this work.

### Weaknesses
This is a minor suggestion:

This paper introduces the use of sparse autoencoders in Section 3.1. 
While the stated limitations offer justification for this approach, a more detailed explanation of the role of sparse autoencoders in Section 3.1 would enhance the clarity and comprehensiveness of the work.

### Questions
Check weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The submission picks up on preliminary ideas developed in “A technical note on bilinear layers for interpretability” (Sharkey, arXiv, 2023) where the idea of using bilinear layers in place of traditional MLPs was promoted to enable forms of interpretability. This is enables by the fact that a bilinear transform of an input vector can be expressed as linear operations with a third-order tensor. This submission follows through by demonstrating several ways in which the tensor can be analyzed with tools from eigen-analysis because input vectors representing features act upon the tensor to yield a matrix (and one can further only consider the symmetric component of this matrix, which has a real eigen-spectrum). 

Examples showcased are: 
* Interpretability for image classification with a shallow feed-forward network with one hidden bilinear layer (MNIST and FMNIST)
    * Eigenvectors of the last layer when projected back into input space visually resemble class prototypes or key features
    * Top eigenvectors are consistent across training runs and model sizes
    * Success on the mechanistic interpretability challenge (Casper, 2023)
    * Successful adversarial masks created from leading eigenvectors for a chosen adversarial class
* Identifying interactions between sparse autoencoder (SAE) based features in a small language transformer model
    * An example of identifying a sentiment negation circuit by projecting input features onto leading (both positive and negative eigenvalues) eigenvectors
    * Pointing out that SAE features tend to be low-rank in terms of the interaction matrix, suggesting promise for future work in circuit discovery in such models

### Strengths
Originality:  While the ideas of using bilinear layers and use of eigenanalysis on the corresponding reduced tensor are borrowed from past work (in particular, “A technical note on bilinear layers for interpretability), the precise demonstrations are new, to my knowledge. 

Clarity: The paper is well-written, making it easy to follow (even for a reader like me, less familiar with this area of work). The Discussion section well-summarizes the contributions, contextualizes the implications, and identifies key limitations.

Quality: The work seems technically sound, with a reasonable span of experiments to make the point that’s being made. 

Significance: The results are certainly intriguing, and help further the case for adoption of bilinear layers in modern models that are heavily MLP-based.

### Weaknesses
The illustrations in the submissions are some fairly reasonable demonstrations of the interpretability-advantages of networks with bilinear layers. However, these ideas may not be mature enough, hence the lack of robust demonstrations at a broader range of tasks, models, and circuits. Being able to showcase such range would significantly strengthen the influence of the work in the nearer future.

Perhaps some of the existing problems can be solved with advances in discovering semantic “output directions” as part of the method. Even if the top eigenvectors may correspond to distributed semantics, further work to enable interpretation of such semantics would also be significant.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper gives several methods to interpret bilinear multilayer perceptron networks (BMLP). BMLP's use a bilinear activation function and produce comparable results to other activation functions. By posing the bilinear leayrs as tensor operations, the author is able to apply direct interaction, eigendecomposition, and SVD analysis. Using these, the author provides an analysis of internal features, construct low-rank approximations of a model, and constructs adversarial examples. Overall, the paper shows the viability of an interpretable BMLPs.

### Strengths
Good exhibition of content in all sections, both setup and presentation of results
Effective choice of experiments with convincing examples and helpful visualization. 
Work is significant: Presents analysis using well understood methods to produce precise, understandable and actionable interpretations of models with competitive performance.

### Weaknesses
I did not notice much analysis using SVD, perhaps I missed it.


Can you justify the use of the HOSVD as used? Two concerns: 1) The tensor represents a non-linear function. 2) If removed all but but the largest singular values of B, would the resulting tensor functionally approximate B? Also, what were the results of the SVD analysis, what section is that in?


Minor Comment:
Giving some dimensions on W,V could help with the presentation.

### Questions
Can you justify the use of the HOSVD as used? Two concerns: 1) The tensor represents a non-linear function. 2) If removed all but but the largest singular values of B, would the resulting tensor functionally approximate B? Also, what were the results of the SVD analysis, what section is that in?


Minor Comment:
Giving some dimensions on W,V could help with the presentation.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to use bilinear MLP as a novel approach for weight-based interpretability. The bilinear MLP and its analysis method are introduced first. Then a handful of experiments are presented to demonstrate the usefulness of this approach, including visual feature interpretation in image classification and feature interactions in language tasks.

### Strengths
- This paper is carefully composed. Though there are places that can be further clarified (as mentioned below), the overall structure and logic is good.
- A variety of experiments are carried out to demonstrate the usefulness of the proposed approach. The bilinear MLP does seem to provide interesting findings and have potential in the realm of mechanistic interpretability.

### Weaknesses
 - I couldn't understand what Figure 2 is demonstrating. Firstly, the caption refers to subfigure A, B while the figures do not have A, B labels. Secondly, do you mean that the input images with "$|$" or "$-" patterns of exactly the same size and position will have high activation? I imagine that when flattening images to vectors, an image with many small "$-" edges isn't well aligned with the eigenvector that is one big "$-" in the middle of the image. If that's the case, why are the "$|$" or "$-" eigenvectors edge detectors?
- I feel that Section 4 and 5 can be clearer if the authors always specify "eigenvectors of *what matrix*" when saying eigenvectors. Section 3 introduced three different methods. So I find the terms like "decomposition" and "eigenvectors" ambiguous, even after I tried to trace back to the concepts introduced in Section 3. The term "eigenvector of a model" is also ambiguous, since models don't really have eigenvectors.
- I'm confused by the $d_{bj}^{in}$ in line 138 and the $d_{in}$ in line 189. Are they the different variables?
- In line 252, I can see that adding dense Gaussian noise to the inputs produces bilinear layers with more intuitively interpretable features. But why is it an effective regularizer?

### Questions
- Could the authors introduce the dimensionality of the variables when defining them? I and perhaps also other readers would find that quite useful for understanding the equations.

- In line 121, is the $W$ in $g(x)=(Wx+b_1)\odot (Vx+b_2)$ supposed to be bold?

- I'm confused by the $d_{bj}^{in}$ in line 138 and the $d_{in}$ in line 189. Are they the different variables?

- In line 252, I can see that adding dense Gaussian noise to the inputs produces bilinear layers with more intuitively interpretable features. But why is it an effective regularizer?

- Is the bilinear MLP related to the gated linear network literature [1]?

  [1] Veness et al (2021). Gated linear networks. https://arxiv.org/abs/1910.01526

### Soundness
3

### Presentation
2

### Contribution
3
