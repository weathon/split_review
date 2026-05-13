# Manifold Learning via Foliations, and Knowledge Transfer

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Understanding how real data is distributed in high dimensional spaces is the key to many tasks in machine learning. We want to provide a natural geometric structure on the space of data employing a deep ReLU neural network trained as a classifier. Through the data information matrix (DIM), a variation of the Fisher information matrix, the model will 
discern a singular foliation structure on the space of data. We show that the singular points of 
such foliation are contained in a measure zero set, and that a local regular foliation exists almost everywhere. 
Experiments show that the data is correlated with leaves
of such foliation.
Moreover we show the potential of our approach for knowledge transfer by analyzing the %trace and spectral spread of 
spectrum of the DIM to measure distances between datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a manifold learning method based on the foliation structure. Particularly, the eigenvalues of the data information matrix are leveraged to measure the difference between two datasets, which reflects the degree of knowledge transfer from one dataset to another. Several benchmark datasets are used to evaluate the performance of knowledge transfer and its relation with the eigenvalues of the data information matrix.

### Strengths
1. It is interesting to apply the foliation structure for capturing geometric information of data.

2. The paper constructs a relation between the eigenvalues of the data information matrix and the ability of knowledge transfer between datasets.

### Weaknesses
1. Section 1 states that "at least in the cases most relevant for concrete applications, and calls for more sophisticated mathematical modeling". This is too vague to figure out the main point. What kind of concrete applications and challenges are considered here, and what sophisticated mathematical tool is used here for what challenge? More detailed discussions are required to develop this statement.

2. It would be better to re-organize the structure of the submission, especially Section 1. Is it necessary to discuss machine learning and deep learning in Section 1? The connection between this part and the others is unclear. 

3. Section 2 is chaotic without a clear structure. In addition, this part just lists some existing works without further insightful discussions.

4. The formal definitions of some mathematical notations are missing. For example, for Eq. (3), it seems that the gradient vectors are used to construct a subspace, while the definition of "span" is missing.

5. The results regarding singular points and the measure are interesting while difficult to understand. It would be helpful to provide some intuitive examples or visualization results, and discuss more about the physical meanings and potential applications.

6. Is it possible to extend the results to other activation functions?

7. The experiment part is weak. Only several simple datasets are used. An interesting connection between DIM eigenvalue and the ability of knowledge transfer is constructed. Based on this, it would be better to apply this observation to the domain adaptation task, which considers how to effectively transfer knowledge between datasets.

### Questions
1. Section 1 states that "at least in the cases most relevant for concrete applications, and calls for more sophisticated mathematical modeling". This is too vague to figure out the main point. What kind of concrete applications and challenges are considered here, and what sophisticated mathematical tool is used here for what challenge? More detailed discussions are required to develop this statement.

2. For singular points, it would be helpful to provide some intuitive examples or visualization results, and discuss more about the physical meanings and potential applications.

3. Is it possible to extend the results to other activation functions?

4. It would be better to apply this observation to the domain adaptation task, which considers how to effectively transfer knowledge between datasets.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel data information metric (DIM) adapted from the Fisher information matrix. It then illustrates how to use DIM to visualize the structures of datasets and compute distances between datasets. The paper also explains data foliage structure, which splits data into submanifolds. The foliage structure is further separated into regular and singular points, which gives valuable insights into this dataset. The application is to apply knowledge transfer between *NIST datasets. It transfers knowledge of classification from one dataset to other datasets and obtains good accuracies.

### Strengths
1. The foliage structure provides important analysis of datasets, for example, its tangent spaces. Also, the paper visualizes the structures and the eigenvalues comparisons well. 

2. The knowledge transfer experiment shows good results and can show the similarity between many datasets This could extend to large datasets and greatly decrease training time. The experiments of moving data in the direction of tangent space also provide a meaningful way to analyze datasets.

3. The paper provides a theoretical background to DIM and its relation with the established results, like the Frobenius theorem and Fisher information matrix.

### Weaknesses
1. The experiments are limited to *NIST datasets, so it is not clear whether the knowledge transfer can be extended to more complex datasets and manifolds. For example, the classifier is only fine-tuned with the last layer, and there are no more comparisons. Thus, we cannot conclude whether DIM and knowledge transfer are correlated. If Table 2 has more explanations, that will help the readers to understand the conclusion the authors are trying to get.


2. The theoretical results made assumptions about the neural network architecture, so not applicable to other architectures. 

3. Some other papers compute distances between datasets. Reviewer recommends the authors to cite them as well:

Alvarez-Melis, David, and Nicolo Fusi. "Geometric dataset distances via optimal transport." Advances in Neural Information Processing Systems 33 (2020): 21428-21439. 

Hua, Xinru, et al. "Dynamic flows on curved space generated by labeled data." Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence. 2023.

### Questions
1. For Figure 4, what are the possible ways to define singular points with ReLU? Or the method does not work with networks with ReLU?

2. How does Figure 6 connect to the knowledge transfer experiments? What is the conclusion drawn from this visualization?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The submission proposes an information geometry analysis of the data manifold.  In particular, with the “data information matrix” (DIM) -- analogous to the Fisher information matrix but where gradients are taken in data space -- the authors define a distribution over dataspace that can reveal aspects of the data manifold given a trained model.
With this distribution in hand, the authors empirically examine its nature as a foliation (or not, depending on the nonlinear activation in the network) and find that the points in the dataset are different from random points sampled over the dataspace.
From the ability to assess the rank of the distribution at different points in dataspace via the eigenvalues of the DIM, the authors compare the values at points from different datasets for a network trained on MNIST.  Finally, the MNIST-trained network is fine-tuned on the different datasets and the performance of the network is shown to correlate with the smallest non-zero eigenvalues.

### Strengths
The combination of differentiable geometry and information geometry to study the data manifold is interesting, and the authors demonstrate that it can lead to some useful insights on real datasets.  In particular, the comparison of the eigenvalue spectrum of the DIM at data points from different datasets seems a reasonable and principled way to assess the model’s familiarity to different datasets.  The DIM seems like a useful construct, and should generally be more manageable to deal with than the FIM (data space being significantly smaller than parameter space); while it was introduced elsewhere, the authors demonstrate new utility from the DIM.

### Weaknesses
The text is hard to follow at times.  Given the machine learning audience of ICLR, clarity of exposition about differentiable geometry concepts is important, yet explanations are often confusing or absent (see questions below).  I did not get anything from the visualization of Fig 4 (ReLU vs GeLU trained on XOR).  I am skeptical about the claim that points in the training data are identifiable -- perhaps en masse, but not individually.

### Questions
- Why is $D$ used for the dataset in line 113 and then immediately after, for the DIM?  
- What are the blue lines showing in Fig 4, and why are they irregularly spaced?  What is the significance of the coloring of points?
- “Hence, there is no foliation whose leaves fill the data space, naturally associated to it via Frobenius Theorem.” (L227)  --> The foliation does not fill data space, but rather the distribution defined by Eqn 4, correct?  What does the “naturally associated...” clause mean, and what does “it” refer to?
- In Figs. 2 and 3, isn’t the distribution as defined in L193 9-dimensional?  So is there an unambiguous sense of direction “moving tangentially to $\mathcal{D}$”?  What is the “same direction” (L212), just a randomly sampled direction in dataspace?
- What is necessary about integrability when making Figs 2 and 3?  Couldn’t similar directions be found in dataspace using the distribution definition (4) for a network with any arbitrary activation function?  What would change about Figs 2 and 3 for a non integrable distribution?  
- L306, are p and N(x) equivalent, and if so, why are they both included?
- “The points in MNIST, the training dataset, are clearly identifiable by looking at the colored area.” This seems to be one of the main experimental results.  The overlap between the distributions of eigenvalues suggests only a fairly large population of samples can be identified as the training data or not, right?  Additionally, the identifiability is all from the largest couple of eigenvalues, right?  Can you speak to the significance of this, when it’s the *lowest* eigenvalues that correlated best with validation accuracy in the knowledge transfer task (Table 2)?
- “We propose to complement the notion of data manifolds with the more general one of data foliations” -- how are data foliations more general than data manifolds?
- What is the value of Figs 5 and 8?  Why not show e.g. more traversals, perhaps with the starting point an image from a different dataset?
- Can you speak to computing the DIM in practice?  Could the proposed method easily be applied to an imagenet pre-trained ResNet?
- Is there anything noteworthy about the DIM eigenvalue spectrum on points that the model misclassifies?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a geometric analysis of neural networks through the lens of foliation theory. The authors introduced the Data Information Matrix (DIM), a variant of the Fisher Information Matrix applied to data space, to study how neural networks organize high-dimensional data. They developed theoretical proofs showing that neural networks create a foliation structure in the data space, where singular points exist in a measure-zero set. To validate their theory, they conducted experiments using a LeNet-like CNN architecture on MNIST-family datasets, demonstrating how DIM eigenvalues correlate with transfer learning success. They analyzed both ReLU and GeLU networks, showing different properties in terms of foliation structure and investigating the relationship between geometric properties and knowledge transfer capabilities. The experimental validation focused on small-scale problems with 28x28 grayscale images and primarily 10-class classification tasks.

### Strengths
### Theoretical Foundation:
The paper provides rigorous mathematical foundation for understanding neural networks geometrically. Authors prove that singular points of the foliation structure lie in a measure-zero set, giving theoretical guarantees for their geometric framework. This connects deep learning to classical differential geometry in a novel way.

### Interpretable Framework:
The authors demonstrate clear visualization of how neural networks organize data through geometric structures. In their XOR example (Figure 4), they show how different nonlinearities (ReLU vs GeLU) create different foliation patterns, making abstract concepts concrete and visually interpretable.

### Quantitative Metrics:
The work introduces measurable quantities for dataset similarity through DIM eigenvalues. Their experiments show that MNIST transfer to Fashion-MNIST achieves 81% accuracy with λ(d-8) = -8.08, while transfer to CIFARMNIST only achieves 33% with λ(d-8) = -6.90, providing a quantitative relationship between geometric properties and transfer learning success.

### Weaknesses
### Scale Limitations:
The framework faces severe computational challenges with modern-scale problems. For a typical 224x224x3 image, the DIM would require ~85GB memory, making it impractical for real applications. The experiments only deal with 28x28 grayscale images, avoiding these scaling challenges.

### Dataset Constraints:
The validation is limited to simple classification scenarios. While the theory claims generality, experiments only use MNIST-like datasets with 10 classes. This leaves open questions about handling CIFAR100 (100 classes) and ImageNet (1000 classes).

### Architectural Restrictions:
The theoretical analysis mainly focuses on ReLU networks with simple architectures. Modern networks using complex architectures like ResNet (or VGGNet) are not addressed. For example, their transfer learning experiments only retrain the last layer, which is far from contemporary transfer learning practices that often involve partial fine-tuning or adapter modules.

### Questions
I think this paper is trying to contribute theoretically inspired methodology. Thus, would you mind answer the points I mentioned in the weakness?

Please carefully use \citet and \citep in your draft.

### Soundness
3

### Presentation
2

### Contribution
2
