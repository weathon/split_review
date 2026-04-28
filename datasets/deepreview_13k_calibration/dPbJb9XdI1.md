# Convolution goes higher-order: a biologically inspired mechanism empowers image classification.

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
We propose a novel approach to image classification inspired by complex nonlinear biological visual processing, whereby classical convolutional neural
networks (CNNs) are equipped with learnable higher-order convolutions. Our model incorporates a Volterra-like expansion of the convolution operator, capturing multiplicative interactions akin to those observed in early and advanced stages of biological visual processing. We evaluated this approach on synthetic datasets by measuring sensitivity to testing higher-order correlations and performance in standard benchmarks (MNIST, FashionMNIST, CIFAR10, CIFAR100 and Imagenette). Our architecture outperforms traditional CNN baselines, and achieves optimal performance with expansions up to 3\textsuperscript{rd}/4\textsuperscript{th} order, aligning remarkably well with the distribution of pixel intensities in natural images. Through systematic perturbation analysis, we validate this alignment by isolating the contributions of specific image statistics to model performance, demonstrating how different orders of convolution process distinct aspects of visual information. Furthermore, Representational Similarity Analysis reveals distinct geometries across network layers, indicating qualitatively different modes of visual information processing. Our work bridges neuroscience and deep learning, offering a path towards more effective, biologically inspired computer vision models. It provides insights into visual information processing and lays the groundwork for neural networks that better capture complex visual patterns, particularly in resource-constrained scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel approach to enhance convolutional neural networks (CNNs) by introducing higher-order convolutions (HoConv) inspired by biological visual systems. The method aims to capture complex pixel relationships explicitly by incorporating second-order and higher-order interactions in the convolutional process. The authors validate the effectiveness of HoConv on synthetic datasets and standard benchmarks like CIFAR-10 and CIFAR-100, demonstrating some performance improvements. Representational similarity analysis (RSA) is employed to investigate the representational differences between HoConv and standard convolutional layers.

### Strengths
1.	The introduction of higher-order convolutions is a novel idea, grounded in biological visual processing, which could inspire future work in feature representation.
2.	The theoretical foundation using Volterra series adds rigor to the methodology.
3.	The use of representational similarity analysis (RSA) to explore differences in feature representation provides additional insight into the method’s internal workings.

### Weaknesses
1.	The experimental setup is overly simplistic, relying heavily on toy datasets and limited architectures, making it difficult to assess the method’s effectiveness in real-world scenarios.
2.	There is no exploration of how this method could scale to deeper networks (e.g., ResNet) or more complex tasks (e.g., ImageNet), raising concerns about its applicability to complex tasks.

### Questions
1.	Could the authors provide a more extensive evaluation of HoConv on deeper networks or larger datasets to demonstrate its scalability and generalizability?
2.	How does the explicit modeling of higher-order interactions compare with the traditional method of adding more layers in terms of computational cost and performance improvement?
3.	Can the authors clarify if and how the architectural differences were controlled in the experiments, especially in Table 1, to ensure a fair comparison?

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
In this manuscript, the authors present their new architecture variant HoCNN, which they use as a replacement for the first layer in a simple convolutional neural network architecture. HoCNN adds weights for the higher order terms, i.e. the products of the pixel values, such that the overall function becomes an arbitrary polynomial in the input pixel values for each patch. They find good performance of the network for categorisation of textures from a classical model based on the same correlations HoCNN is build to detect and slight increases in performance for small machine learning datasets (MNIST, FashionMNIST, CIFAR-10, CIFAR-100). Furthermore the authors present some analysis of the distances between stimuli in the network.

### Strengths
Extensions of neural networks to more non-linear behaviour are certainly of interest and the authors do find some improvements with their new architecture.

### Weaknesses
Overall, I do not think this architecture is promising based on the data the authors present and do not think any of the author’s claims about biological inspiration hold up.

First on the biological inspiration: The type of nonlinearity the authors use here is a general purpose approximation for any nonlinear function and was introduced as such originally. Volterra kernels are an early idea to capture non-linear functions at all, but they are not a good way to capture biologically plausible non-linearities. The receptive fields and non-linear interaction over space in early visual processing are well understood and look nothing like the classical polynomial proposed by the authors. And conversely the authors method allows the approximation of any non-linear function including ones very far from biological plausibility.

In terms of raw performance the authors’ model is not very impressive. They only evaluate on small datasets and with the exception of MNIST the performance of both their model and the CNN they compare to is far from the state of the art. Even for these comparisons HoCNN wins by a few percentage points. This is by no means convincing evidence that their HoCNN really improves performance. For example, according to the FashionMNIST website HOG features and a SVM or a vanilla 2 layer convnet without preprocessing both perform better than the networks presented here (at ~92.5%).

The overall number and complexity of the evaluations is lacking. To establish a new architecture the authors should test different scales of their model, different training environments, etc. and show that their advantage is not just a side effect of a slightly better match in training parameters. Also, it would be important to see comparisons to models that perform reasonably well on the tasks to alleviate doubts like: Is the addition helpful because the convnet is too simple in itself? If so, does the advantage go away if you use a deeper network afterwards?

To make the argument the authors are trying to make (i.e. using this particular image processing frontend based loosely on biology helps ML) they would have to compare to models like VOneNet (https://github.com/dicarlolab/vonenet, https://proceedings.neurips.cc/paper/2020/file/98b17f068d5d9b7668e19fb8ae470841-Paper.pdf ).

### Questions
I am still quite uncertain what we can learn from the RSA analyses. What insight is provided by similarities between stimuli are generally lower in HoCNN than in the CNN?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces higher-order 2D convolutions with the objective of capturing higher-order dependencies across pixels in natural images. They show convincing results on synthetic, then standard visual datasets.

### Strengths
It's very common at ICLR to benchmark any visual model with humoungous datasets of millions of images, and paradoxically I find laudable the choice of focusing on synthetic data and "relatively small datasets to allow for comprehensive testing and analysis". This allows to better explain *why* the model brings something to the community, something often missing in papes just exhibiting accuracy results.

### Weaknesses
In figure 6c you use the "Absolute difference between the two RDM" and I would like to question how it brings something qualitative to your analysis... RDMs contains values between 0 and 1 and using a dissimilarity metric based on the distance between probabilities may sound mathematically more justified in comparison to the absolute difference between probability values?

In particular, one main point you mention is "This alignment between model performance and natural image statistics suggests that our approach effectively captures the structure of visual information in the natural world." and I guess it would be more sensible to show how well you capture these statistics instead of using a RDM which focuses on capturing similarities across intermediate representations.

The paper is quite clear and well organized. Minor typos:
Figure 2: indices should start at i=1 not i=0
l 430 "analized"

### Questions
The higher order representation is introduced in the input, but nothing limits from using it in other layers: what do you expect to happen if it introduced at other levels of the hierarchy?

You make a point in section 2.1 about the tied-weight issue. First, this could fit in the intro to justify the use of HO representations. An interesting prospect would be to show how you resolved the problem quantitatively in your model. Could you provide quantitative evidence demonstrating how your model resolves the tied-weight issue? In particular, a receptive field captures some higher-order correlations between neighbouring pixels. Would your results still be valid if you would increase kernels' sizes?



As a perspective, a similar architecture could be applied to signal evolving in the temporal domain. Would the higher-order representation be akin to the different moments in generalized coordinates (speed, acceleration, ...) and be something useful for predictive processing ?

### Soundness
4

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
This paper introduces higher order convolutions in CNNs, citing the importance of higher-order statistics from neuroscience literature. The authors report favorable results in MNIST, F-MNIST, CIFAR-10 and CIFAR100.

### Strengths
The concept is rigorously introduced (I did not know what "Volterra-like" really meant but the equations were clear).

### Weaknesses
 I apologize in advance for my short review, but the paper is actually too light on content for me to have too many opinions. The introductory text goes to page 3, there are a bunch of equations with summations taking up essentially a page, gigantic figures 1 and 2 that basically re-explains the equations, and just like that we are already at page 6. Then, in the experiments section, there are gigantic figures 4 and 5 describing architecture and validation accuracy taking up a whole page. This leaves only 3 pages of real results that I am reviewing. Nonetheless, here are the issues I have with this work:

- The models and datasets are too small to claim improvement over regular CNNs. Even the smallest CNNs widely accepted in literature are trained on ImageNet, and have parameter count in the millions. To be perfectly clear, I am open to small toy networks that illustrate mechanisms or specific interpretations, but that is not the case here. The models here are so small that residual connections (found in basically every "traditional CNN") are not even used, yet they claim to "outperform traditional CNN baselines" as quoted in the abstract. I hope the authors do not think I am gatekeeping computational resources but that their claims are overblown for the parameter count and dataset they are using, especially when there are no indications of this would work when scaled up. 

- There is nothing in the paper about image preprocessing, image augmentations, loss functions, learning rates, dropout probabilities and everything else that should be properly controlled for (and more importantly, stated in the paper). As a reviewer this once again leaves me with doubts but nothing concrete to pinpoint.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
