# G2Sphere: Learning High-Frequnecy Spherical Signals From Geometric Data

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Many modeling tasks from disparate domains can be framed the same way, computing spherical signals from a geometric input, for example, computing the radar response or aerodynamics drag of different objects, or navigating through an environment. This paper introduces G2Sphere, a general method for mapping object geometries to spherical signals. G2Sphere operates entirely in Fourier space, encoding geometric structure into latent Fourier features using equivariant neural networks and then outputting the Fourier coefficients of the output signal. Combining these coefficients with spherical harmonics enables the simultaneous prediction of all values of the continuous spherical signal at any resolution. We perform experiments on various challenging domains including radar response modeling, aerodynamics drag prediction, and policy learning for manipulation and navigation. We find that G2Sphere significantly outperforms baselines in terms of accuracy and inference time. We also demonstrate that equivariance and Fourier features lead to improved sample efficiency and generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce a novel neural network architecture to learn spherical signals from 3D geometric data. Their network maps geometric inputs to fourier coefficients in an equivariant graph convolutional network. The learned coefficients are used in a spherical neural network decoder amended with a novel frequency up-sampling technique to produce a continuous spherical signal of arbitrary precision. The proposed approach outperforms baselines on radar prediction, drag prediction and policy learning.

### Strengths
The problem considered is interesting and relevant to the community. The paper is well written and organized, and the figures are useful for understanding the proposed approach and its contributions.

### Weaknesses
The architectural contribution appears fairly minimal, much of the architecture is a combination of existing methods; however, the proposed frequency up-sampling method and learned nonlinearity appear novel. Of the novel architectural contributions only the frequency up-sampling method seems to provide consistent empirical benefit.

The application domain appears fairly novel. The authors introduce new datasets for radar prediction and drag prediction which extends their contribution. Their results on these datasets exceed the predictive performance of baseline models considerably; however, it is unclear to me if the selected baselines are the most appropriate for these tasks.

### Questions
Is the model appropriate for weather radar or tornado prediction[1]? There are several existing datasets in these domains and numerous domain specific baselines that could be compared against.

[1] https://arxiv.org/pdf/2401.16437

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present an architecture for mapping geometric datatypes to spherical output maps. To do so they use existing techniques from spherical architectures in combination with an equivariant encoder which maps mesh data to spherical signals. The paper is written clearly and for the most part it is easy to understand. A diverse set of example is provided to understand the efficacy and relevance of the method.

The paper has a few weaknesses in terms of the experimental evaluation of the method and in references made to other works which utilize similar methods already. Moreover some of the claims made in the paper are not supported by experimental data and/or references.

### Strengths
Interesting architecture which uses a mapping from 3d geometries to spherical domain. Diverse set of examples are shown, with seemingly good results over existing baselines

### Weaknesses
The main two weaknesses I see are:
- 125-127: the authors claim that the architectuere caprtures significantly more detail than existing architectures but this is never experimentally shown.
- at some points references to prior works are missing - especially with respect to certain techniques in the architecture which have been utilized in the architecture before (See details)
- The experiments are not-well motivated and it is not clear to me 1) how relevant these are and 2) how difficult and fair they are wrt existing baselines. It is hard to quantify how good the errors reported in Table 1 are. For instance, [1] uses a similar approach to map geometry to spherical signal. Why not compoare wrt. this baseline which seems better suited.
- It is hard to understand the method and the experimental performance with the main text alone. I suggest adding a better explanation of the architecture.

**Detailed:**
- the signals to be learned in FIgure 3 show a high dependence on l and very little variation in m. As such I worry that this example is biased towards a specific architecture. Why not reconstruct other spherical Signals?
- 230-239: **TSNL** -trainable spherical non-linearities are not a new concept as this has also been used in [2]
- 215-229: again, applying non-linearities in spatial domain and then going back to frequency domain has been previously done. See e.g. [1,2,3]
- error is only reported in terms of MSE. As far as I understand the error is not properly integrated over the sphere using the jacobian?
- 100: FNO/SFNO do not entirely operate in Fourier space.
- Table 1 reports numerical errors but it is hard to evaluate how good these errors are. In particular given that Figure 5 suggests that the Equiformer and Transformer break down completely.

### Questions
225-229: While this seems like a substantial improvement, L=40 is not particularly high. For instance in the SFNO work that you cite, SH coefficients are computed up to degrees ~360. Why is this architecture not able to do so?
742: you claim that previos implementations use different derivations of the Spherical Harmonics which makes them a poor fit. Can you elaborate?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents G2Sphere, an approach to model spherical signals by mapping geometric 3D data, such as meshes or point clouds, to spherical representations using Fourier coefficients. The model addresses tasks involving spherical data, which are essential for applications like radar response and aerodynamic drag modeling. The authors propose an architecture composed of an SO(3)-equivariant encoder (using Equiformer v2) to encode 3D geometric data and a spherical CNN decoder to predict Fourier coefficients, allowing the reconstruction of high-resolution spherical signals.

### Strengths
- The paper introduces a Fourier-based approach to represent spherical signals, making it relevant for domains where rotational consistency and high-frequency detail are crucial.
- By adequately modified the exisiting model’s architecture which respects rotational equivariance, the approach maintains input-output alignment under rotations, which is beneficial for tasks that require orientation-aware outputs.

### Weaknesses
 - The paper’s explanation of the model architecture is somewhat ambiguous, particularly regarding the encoder-decoder structure. Specifically, the description of the Equiformer encoder, its output domain, and the role of mean pooling is unclear. For instance, it is not explicitly described how the mesh is encoded into the latent space or how this representation transforms in the decoder to produce Fourier coefficients. From my understanding, G2Sphere applies node-wise spherical representation in Equiformer’s intermediate layer and then combines these node-wise features into a single spherical signal through pooling. However, this flow is difficult to follow based on the paper's explanation alone.
- The proposed method lacks novelty, as modeling the coefficients of spherical signals directly for continuous function representation has been explored in other domains [1]. Specifically, this paper's approach seems to mainly add equivariant GNNs and equivariant convolutions for modeling spherical coefficients, which limits the originality of its contribution. Additionally, a similar frequency up-sampling technique has been used in another spherical harmonics-based convolution method [2].
- While the model is designed to be equivariant, the paper would benefit from a straightforward proof or brief explanation of how this equivariance is ensured within the network architecture. Providing this clarification could help readers better grasp the model's theoretical foundation
- The paper could enhance clarity by including more details on the training process, particularly the training algorithm and loss functions. This would enable readers to understand the optimization approach better and assess the model's robustness.
- Highlighting G2Sphere's uniqueness and distinct purpose would strengthen the paper’s impact. Similar tasks involving spherical signal modeling exist, such as Implicit Neural Networks on spheres [3,4,5] or spherical convolutions for brain imaging [2]. Differentiating G2Sphere from these related approaches would underscore its novelty and relevance.

### Questions
- Could the authors clarify the output domain of the Equiformer encoder and the overall training process? This clarification would greatly enhance the reader’s understanding of the model.

### Soundness
3

### Presentation
2

### Contribution
2
