# On the Fourier analysis in the SO(3) space : the EquiLoPO Network

- Decision: Accept
- Scores: 6, 3, 6, 5, 5

## Abstract
Analyzing volumetric data with rotational invariance or equivariance is an active topic in current research. Existing deep-learning approaches utilize either group convolutional networks limited to discrete rotations or steerable convolutional networks with constrained filter structures. 
This work proposes a novel equivariant neural network architecture that achieves analytical Equivariance to Local Pattern Orientation on the continuous SO(3) group while allowing unconstrained trainable filters - EquiLoPO Network.
Our key innovations are a group convolutional operation leveraging irreducible representations as the Fourier basis and a local activation function in the SO(3) space that provides a well-defined mapping from input to output functions, preserving equivariance. By integrating these operations into a ResNet-style architecture, we propose a model that overcomes the limitations of prior methods. A comprehensive evaluation on diverse 3D medical imaging datasets from MedMNIST3D demonstrates the effectiveness of our approach, which consistently outperforms state of the art. This work suggests the benefits of true rotational equivariance on SO(3) and flexible unconstrained filters enabled by the local activation function,  providing a flexible framework for equivariant deep learning on volumetric data with potential applications across domains. Our code is publicly available at \url{https://gricad-gitlab.univ-grenoble-alpes.fr/GruLab/ILPO/-/tree/main/EquiLoPO}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper describes a class of equivariant group convolution layers based on the steerability paradigm (Wigner-D irreducible representations). Working with such continuious representations of SO(3) signals requires working with feature fields of Fourier coefficients, and one cannot simply take arbitrary activation functions. Hence the authors also propose a new class of activation functions based on polynomial approximations of ReLU, which maintain equivariance exactly. This is an important contribution. Next they show the method works well on 3D volumentric data (Medical MNIST), outperform several state-of-the-art equivariant baselines.

### Strengths
- Being able to build efficient and effective equivariant architectures for 3D volumetric data is still an active field in geometric deep learning. The paper provides a valuable contribution, primarily for the following
- The proposed activation functions are a great contribution, because it is well known that simple norm-based activations (like gating and the "global 2-norm" based one of appendix L) do not work very well. The authors show that the proposed activation function is much more effective.
- The method is sound and well-presented, and the related work section is complete (however, it is mostly absent from the main body as it is in the appendix).

### Weaknesses
## Weaknesses
- Context is missing about where the methods stands relative to the equivariant deep learning literature. Some references should be included in the main body.
- The equivariant convolution layer itself is, in my opinion, not a new contribution as it falls in the steerable class of g-cnns. 
- In the experimental section, an important comparisons for the activation functions is missing, namely comparing to inverse Fourier based activation functions [Fourier o ReLU o InverseFourier]. This is often used to by-pass the constraint of norm-based activations in Fourier space.

## Detailed Comments

### On Group Convolutional Networks Classification
The introduction briefly introduces group convolutional networks into two classes: group conv nets and steerable conv nets. But in my opinion they are both the same as steerable convs (tensor field type) are identical to regular g-convs when expanding the conv kernels in a basis of irreps. So a better separation would be regular vs steerable group convolutions. The first discretizes the group and directly implements equation 1 and 2, the second adopts a fiber bundle viewpoint and talks of steerable feature fields (features that transform via irreps). The kernel constraint becomes more intricate in the latter case, but has the advantage that you maintain exact equivarance (up to the spatial discretization) as you don't need to work with grids over SO(3).

I would say the present work falls into this category, and you have implicitly solved the kernel constraint by deriving the convolution kernels via a Fourier transform from the regular group conv formulation (an approach that is also taking in this lecture [link](https://youtu.be/EBzqL1OXigM?feature=shared) when deriving harmonic networks from regular group convolutions. These two papers make a point of this connection in their appendices:

- Brandstetter, J., Hesselink, R., van der Pol, E., Bekkers, E. J., & Welling, M. Geometric and Physical Quantities improve E(3) Equivariant Message Passing. In International Conference on Learning Representations (2021).
- Bekkers, E. J., Vadgama, S., Hesselink, R., Van der Linden, P. A., & Romero, D. W. Fast, Expressive $\mathrm{SE}(n)$ Equivariant Networks through Weight-Sharing in Position-Orientation Space. In The Twelfth International Conference on Learning Representations (2024)

### Technical Questions and Suggestions
- When mentioning canonicalization, do you mean works like [kaba et al 2023]? Either way, please add cites when discussing it as an option.
- When talking about 3D -> 6D -> 3D (invariant) convolution you cite Zhemchuzhnikov and Grudinin, which is very appropriate, but please also consider including [Andrearczyk and Depeursigne]:

refs:
- Kaba, S. O., Mondal, A. K., Zhang, Y., Bengio, Y., & Ravanbakhsh, S. (2023, July). Equivariance with learned canonicalization functions. In International Conference on Machine Learning (pp. 15546-15566). PMLR.
- Vincent Andrearczyk, Julien Fageot, Valentin Oreiller, Xavier Montet, Adrien Depeursigne Proceedings of The 2nd International Conference on Medical Imaging with Deep Learning, PMLR 102:15-26, 2019.

### Equation Concerns
Could you double check the equations for group convolutions. I have the impression that in Eq. 1 it should read $...w(R^{-1} r_0) …$ instead of $...w(R r_0)$. Same for Equation 2 which I think should read $...w(R^{-1}R_0, R^{-1} R_0)$, here with $R^{-1}$ multiplying on the left of $R$. I could be wrong here but I think there's an inconsistency between group correlation vs convolution where the translation is in convolution form, and rotation in correlation form.

Also in Eq 1 the integration measure is put at the end of the integral, and in 2 they are given up front.

### On Section 3.1
Is my understanding of the derivation of these steerable convolutions—as described above about regular vs steerable g-convs—correct? If so, how does this justify the claim that your method "does not impose constraints on the filter", since having to parametrize the kernels in a basis of wigner-D basis is in a way designing the kernel to automatically satisfy the constraint. But it would then still fall into the class of steerable layers, as described in full generality in:

Cesa, G., Lang, L., & Weiler, M. (2022). A program to build E(N)-equivariant steerable CNNs. In International conference on learning representations.

### On Activation Functions
I like the comment about the need for local activation functions. This could motivate why we typically see that regular group convolutions are more effective than steerable once, because they localize information *and* are compatible with powerful actiation functions like ReLU. This is the main motivation behind works s.a. [Bekkers et al. 2024, see ref above] and extensively tested for in 2D in:

Weiler, M., & Cesa, G. (2019). General e(2)-equivariant steerable cnns. Advances in neural information processing systems, 32.

Sections 4.1 and 4.2 are nice contributions.

### On Experimental Section
I would highly encourage testing these activation functions also in 3D point cloud settings. There should be various benchmarks with models based on e3nn that could serve as a baseline. 

Please improve the experimental sections with explicit conclusions and take-home messages.
There's quite a lot to parse.


### Questions
see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a deep learning network that guarantees rotational equivariance over continuous SO(3). It relies on a Fourier representation of volumetric data. The proposed model follows the well-established ResNet architecture where activations, pooling and normalization layers are adapted to the proposed data representation.

### Strengths
The paper presents an in-depth analytical explanation of the proposed data representation and the components used in the proposed residual model. It also includes detailed analysis of components such as softmax as well as constant and adaptive nonlinear activations.

### Weaknesses
The main paper heavily relies on the appendix for several of the explanations, experimental settings and architectural details. Additionally, the introduction lacks context and references to better understand the motivation and current limitations of state-of-the-art algorithms. Authors should consider adding examples of previous work on group equivariance and the use of steerable filters in SO(3) in the main paper in an organized manner.

Figure 1 is not very informative about the proposed method. For instance, a more detailed diagram might be useful to show the audience how the feature maps in 6D are constructed.

I found the explanation in Section 3 to be hard to follow since:
- h is used to express multiple convolution operations.
- The main paper heavily relies on equations in the appendix to introduce formulation.
- Several equations are contrived and do not comply with the paper's format (e.g. Eq. 5).

The analysis of the proposed layers in the main paper is limited to the activation functions. It may be interesting to ablate most if not all of the components proposed by the paper (normalization, pooling, conv. parameters, etc.) and how each affects accuracy, ROC curves and rotation equivariance.

Evaluations are limited to accuracy and AUC-ROC. The degree of equivariance and how it compares to alternative methods is not evaluated.

It is unclear how to select the architecture to obtain the best performance. Table 1 reports 7 different configurations, each having a significantly different performance across datasets Additionally, Table 1 does not report if the metrics were computed on multiple seeds or a single one, so it is not possible to fully assess which technique is the best and in what case.

There are several grammar and typographical errors (lines 34, 280, 284).

I think the paper requires both additional experiments and a manuscript revision. The way it is currently organized, it is hard to distinguish between the proposed ideas and those of previous work. The experimental section also lacks an ablation study. Since it relies on a single table and no rotational consistency metrics, it is not clear how each component affects the final classification performance.

### Questions
1. Is it possible to compare the degree of rotational equivariance attained by the model with that attained by alternative methods?.

2. If evaluated on a single seed, is it possible to report mean and standard deviation on both ACC and AUC-ROC?

3. Results in Table 1 shows improved results depending on the activations used in the model. Still, it is unclear how to select the model in real applications, particularly since not in all cases the proposed method outperforms alternative methods. How can an end user choose the best model given an arbitrary dataset?

4. How does the 6-D feature map affect memory consumption and training/inference time? Is it possible to report these numbers and compare them to alternative methods?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents an equivariant neural network architecture named EquiLoPO Network, and innovates the design of Fourier basis and a local activation function in SO(3) space. Experiments on various databases along with the comparison with various models are given.

### Strengths
1.	This paper proposes a novel equivariant neural network architecture that combines the strengths of group convolutional networks and steerable convolutional networks by leveraging irreducible representations as the Fourier basis.
2.	This paper presents a local activation function in the rotational space that provides a well-defined mapping from input function values to output function values.
3.	The theoretical derivation is detailed, solid and reasonable.
4.	Qualitative and quantitative experiments demonstrate the advantages of the proposed method on the diverse MedMNIST3D collection of 3D medical imaging datasets, and ablation studies verify the effectiveness of the proposed independent module. 
5.	The presentation is fluent, easy to follow, and understandable, with fewer grammatical and expression errors.

### Weaknesses
1.	The introduction does not detail the research background and related literature, and the research motivation is not sufficient; it only mentions the advantages of combining the two. 
2.	There is a lack of comparison with the latest literature. 
3.	The detailed computational cost of different ResNet-style architectures should be given, including training time, number of model parameters, time and space complexity.

### Questions
1.	Please enrich the related work section, and clarify the motivation.  
2.	Please investigate the latest literature and give comparison. 
3.	Please give more experiments details mentioned in the above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an SO(3) equivariant operator, where filters are unconstrained. The authors introduce various pointwise operations, such as polynomial nonlinearities and pooling that are placed in spherical harmonic space. The main innovation is how the polynomial nonlinearities are constructed, which does not introduce extra higher order harmonics into the spectrum, which would otherwise break a Nyquist-like property. They call their new model the EquiLoPO Architecture. They test there system on regularly-sample 3D volumetric medical imaging data, in particular the MedMNIST v2 dataset.

### Strengths
**Clarity**

The written quality of the paper is good. It is clear at each step what the authors intend.

**Quality**

I read all the math in the main text and as far as I could tell it was correct.

**Originality**

I believe the design of novel pointwise nonlinearities that limit the introduction of higher order harmonics into the spectrum of hidden representations is novel. It is certainly an interesting area.

**Significance**

I believe the introduced nonlinearity could be very interesting to the equivariance community. Good nonlinearities that can be applied in the harmonic space have long been sought after, yet none have been found to suffice. For instance “General E(2)-Equivariant Steerable CNNs” _Weiler & Cesa_ (2019) explores some variants, but found that performing nonlinear operations in the physical domain to be most effective (most likely because locality is maintained). Having to transform back to the physical domain is expensive and an Achilles’ Heel to that class of methods. In this sense, the nonlinearities introduced here are significant.

### Weaknesses
 **Clarity**

I found that the exposition of the paper makes it hard to understand, unless the reader is very acquainted with the area of equivariance. My suggestion to the authors is to streamline the math, improve notation, explain notation/variables in the main text, and explain what the math means in practical terms to the reader.

**Quality**

I have no doubts about the mathematical quality of the paper, that is sound. My major doubt concerns the experiments. It is not clear to me how to judge Table 1 without extra information, which I hope the authors will provide. I would like to know how I should compare models in an apples-to-apples fashion. Are they FLOP-adjusted? Otherwise, improvements of one method over the other cannot be compared. Furthermore, are non-equivariant baselines trained with data augmentation? That would only be fair.

Maybe I have missed it (please correct me if I have), but as far as I can see there are no ablations that corroborate the assertions made that the introduced polynomial activations functions are superior to standard ones (ReLU GeLU, Swish, etc). It would have been useful for the paper to have an ablation of that sort, to strengthen the claims of the authors.

### Questions
Line 34: I would argue that the “increase computational demand” of 3D rotational data augmentation is negligible to the cost of training and running a neural network. Indeed equivariance is useful for its guarantee of symmetry and increased sample efficiency. Indeed, moving to 6D convolutions, with complexity in line 148, would be far more expensive from a computations standpoint.
Line 38: The distinction between group convolutional and steerable networks is somewhat arbitrary. Both classes are types of group convolutional network. The major difference between them is the choice of group representation (regular representation vs. irreducible representation). I would change the naming here to avoid confusion.
Why are there no citations in the Related Work section? Perhaps this section should just be end of the introduction?
Line 90: Please elucidate what you mean by orientation pooling. A diagram or equation would suffice.
Line 94: Why take a direct product of R^3 and SO(3) when SE(3) has a semi-direct product structure?
Section 3.1: I would suggest introducing notation in the body of the paper rather than requiring readers to dip into the Supplement. It is quite hard to follow, unless you already know the area fairly well.
Section 3.1: How is this exposition different from the typical SE(3)-equivariant convolutions with a regular representation on the spatial component and using “steerable” convolutions on the rotational component? Is the derivative needed here?
Line 155: How do you arrive at the statement that linear layers detect probabilities and that activations “selectively amplify these probabilities to form compact representations”. Do you have a citation for this?
Line 157: I think people also use the term “pointwise” as well as local.
Table 1: What measures do you take to make sure that architectures are comparable? They all have vastly differing numbers of parameters. Do you match on, say, FLOPs? Otherwise it is hard to compare numbers on a like-for-like basis.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel equivariant neural network, the **EquiLoPO Network**, designed to achieve analytical equivariance on the continuous SO(3) group. The model utilizes **group convolutional operations** based on irreducible Fourier representations and introduces a local activation function to improve the flexibility and rotational equivariance of filters. Extensive evaluation on 3D datasets, particularly the MedMNIST3D, demonstrates that this approach outperforms existing methods in handling volumetric data.

### Strengths
This work represents a significant advance in multiple areas:
1. **Fundamental**: The introduction of a continuous SO(3) equivariant convolutional model offers a mathematically grounded framework for analyzing volumetric data with rotational invariance.
2. **Methodological**: The combination of group convolutional operations and a novel local activation function is a notable innovation that enhances the robustness and versatility of SO(3)-based neural networks.
3. **Technological**: Implementing this model within a ResNet structure for practical 3D medical imaging tasks positions this work as an innovative tool for advancing medical imaging analysis.
   
This work’s capability for true rotational equivariance without discrete approximation or filter constraints represents a new methodological benchmark in volumetric data analysis. The findings have broad implications for medical imaging and potentially other domains where the rotational orientation of data impacts model performance. By reducing the need for data augmentation and enabling models to operate more efficiently on 3D data, this work could significantly enhance model performance in fields requiring 3D data processing, such as autonomous navigation and robotics.

### Weaknesses
- The model’s computational complexity could be a limitation for deployment in resource-constrained environments. Further analysis of model efficiency in practical scenarios would be beneficial. The authors should provide a more detailed breakdown of the computational cost, specifically in terms of FLOPs and memory usage, and compare it against standard 3D convolutional networks. This should include both training and inference times on various hardware configurations.
- All images are resized to 28×28×28 voxels, which makes this like a toy example. How well does the model generalize to real medical datasets, and are there specific aspects of the activation function that might limit its applicability to other 3D datasets? The authors need to demonstrate the model’s performance on higher-resolution medical imaging data, such as CT or MRI scans, and analyze how the performance scales with increasing input size. It is also unclear if the local activation function is robust to variations in image quality and noise levels, which are common in real-world medical data.
- Clarity on the scaling factor in Equation 9 and its impact on activation function accuracy would improve reproducibility. The authors should provide a more detailed explanation of how the scaling factor is derived and its effect on the polynomial approximation. A sensitivity analysis of the scaling factor would be beneficial to understand its impact on the overall model performance.
- Details on the limitations of the SO(3) continuous convolution relative to discrete methods, such as potential downsides in specific edge cases. The authors should discuss scenarios where the continuous convolution might underperform compared to discrete methods, such as in cases with highly anisotropic features or when dealing with very sparse data. A comparison of the computational cost and accuracy trade-offs between continuous and discrete methods would be useful.
- Clearer explanation of how model parameters were tuned for the MedMNIST3D dataset, especially given class imbalances. The authors should provide details on the specific hyperparameter tuning strategies used, including the learning rate, batch size, and optimization algorithm. They should also discuss how they addressed the class imbalance issue, such as through weighted loss functions or data augmentation techniques.
- Additional insights into the batch normalization adaptations for 6D data would be useful for implementation clarity. The authors should provide a more detailed explanation of how batch normalization is applied to the 6D data, including the specific dimensions over which the mean and variance are calculated. It would be helpful to understand if there are any specific considerations or challenges when applying batch normalization to the Wigner D-matrix coefficients.

### Questions
1. **Computational Efficiency and Practical Applications**:
   - Need the complexity analysis of the computations required for continuous SO(3) convolution, how does the model perform on standard hardware compared to more traditional 3D convolutional networks? 
   - Considering the existence of the current foundation model, like DINOV2, that provides general patterns that works well for multiple tasks, is the new convolution still needed?

2. **Generalization to real clinic Data**:
   - The model is tested on 28×28×28 voxel dataset. Has the EquiLoPO network been tested on datasets outside of the resized MedMNIST3D collection? Especially the high-dimensional clinic data.  What would be the observations, particularly regarding performance on datasets where the continuous rotational symmetry might not be as critical?

3. **Activation Function Details**:
   - Could the authors elaborate on the decision to use local activation functions with trainable polynomial coefficients in the SO(3) space? In particular, what was the rationale for choosing the polynomial degree used, and were there alternative activation functions considered?
   - Are there specific types of data for which the adaptive coefficient approach might be more suitable than the constant coefficients?

4. **Impact of Batch Normalization on 6D Data**:
   - Batch normalization for 6D (3D x SO(3)) data is mentioned as a key feature. Could the authors share more about the challenges or considerations involved in adapting batch normalization for this high-dimensional data? Were there any unique issues encountered when tuning these parameters?

### Soundness
3

### Presentation
3

### Contribution
3
