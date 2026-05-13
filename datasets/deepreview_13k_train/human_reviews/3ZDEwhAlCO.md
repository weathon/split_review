# ILPO-NET: convolution network for the recognition of arbitrary volumetric patterns

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Modern spatial data analysis is built on the effective recognition of spatial patterns and learning their hierarchy. Applications to real-world volumetric data require techniques that ensure invariance not only to shifts but also to pattern rotations. While traditional methods can readily achieve translational invariance, rotational invariance possesses multiple challenges and remains an active area of research.
Here, we present ILPO-Net (Invariant to Local Patterns Orientation Network), a novel approach to handling arbitrarily shaped patterns with the convolutional operation inherently invariant to local spatial pattern orientations. Our architecture seamlessly integrates the new convolution operator and, when benchmarked on diverse volumetric datasets such as MedMNIST and CATH, demonstrates superior performance over the baselines with significantly reduced parameter counts—up to 1000 times fewer in the case of MedMNIST. Beyond these demonstrations, ILPO-Net's rotational invariance paves the way for other applications across multiple disciplines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors propose a convolutional neural network equivariant to local 3D rotational deformations. To do this the authors represent filters in their spherical harmonic decomposition. The authors show the proposed approach achieves better performance than baseline models, even with a significant reduction in the number of learnable parameters.

### Strengths
*Originality:* The proposed approach appears novel.

*Quality:* In the experiments, proposed method performs on-par with or better than most baselines.

*Clarity:* (see weakness)

*Significance:* Designing locally equivariant neural network models is a challenging and important problem in the field.

### Weaknesses
 *Quality/Clarity:* The presentation of the related work, and the critiques therein are a bit confusing given the proposed approach.
* The related work is divided into (1) “those based on equivariant operations in the SO(3) space” and (2) “those with learnable filters that are orthogonal to the SO(3).” If I understand correctly, it seems the categories would be better named (1) finite group convolution, and (2) continuous group convolution methods.
* The authors describe the methods in (1) as limited in that they require averaging over the rotations, however, this is a consequence of the definition of convolution. Perhaps this was supposed to be a comment on the pooling layers?
* The authors describe the methods in (2)  as limited in that they require inputs to be centered. My understanding is that inputs to these classes of CNNs are centered by mean subtraction, and that translation offsets do not limit their applicability.
* The authors critique methods in the second class saying “[these methods use] equivariant quantities by design, which prevents them from capturing complex patterns involving multiple point” which is strange since the proposed method requires the filters to be learned as linear combinations of Wigner-D matrices, making them equivariant by design…
* As I understad, one of the claims of the paper is that it can be applied to SE(3) data, but it doesn’t seem like that was tested in the experiments
* It is difficult to evaluate the quality of the model since the experiments are quite sparse. Only one of the related works are compared against and only in a single setting.
* Some notation is introduced without explanation (see questions)

*Possible typos:*
- “architecture” level → ``architecture” level
- In Equation (1 & 2) f(r + \Delta) should be f(\Delta - r)

### Questions
*Questions:*
- What is $\Omega_r$ in eqn (13 & 15)
- It isn’t obvious to me why (16) would be more expressive than averaging especially since it seems like it is the same for all R, can the authors give some intuition here

*Possible typos:*
- “architecture” level → ``architecture” level
- In Equation (1 & 2) f(r + \Delta) should be f(\Delta - r)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper designs a rotation-invariant 3D convolutional neural network architecture. Unlike prior works that rely on data augmentation to learn rotation-invariant representation, the proposed method incorporates such invariance into the model, which leads to a more lightweight and efficient network architecture. Experiments on two volumetric datasets show the effectiveness of the proposed method over several baselines that rely on data augmentation.

### Strengths
1. The proposed method is technically sound to make the 3D ConvNet rotation-invariant by design. 
2. This paper is overall easy to follow.
3. Experiments on two datasets show the proposed method achieves similar or better performance with much less computational cost, in comparison with baselines that rely on data augmentation.

### Weaknesses
My main concern with this work is the lack of comparisons with existing methods. This paper mainly makes comparisons with ResNet variants that learn rotation-invariant representations via data augmentation. How does it compare to prior works that incorporate the rotation-invariance in the network design such as CubeNet? What is the difference between this work and prior works (such as https://arxiv.org/pdf/2003.08890.pdf)? Specifically, the paper does not clearly articulate how its method differs from existing approaches that use group convolutions or steerable filters to achieve rotation invariance. The current comparisons are insufficient to demonstrate the novelty and advantages of the proposed method over these existing techniques. The paper needs to provide a more detailed analysis of how its approach handles continuous rotations compared to methods that discretize the rotation space, and how the specific filter design differs from steerable filters, especially in terms of computational complexity and representational power.

### Questions
See the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new 3D convolution operation that is invariant to the local orientations of the input features in volumetric data. The method considers rotation invariance over a continuous range of rotations spanning all of SO(3) and demonstrates superior performance on two datasets while being extremely parameter efficient.

### Strengths
- The paper is well written, the method is explained comprehensively and is easy to follow.
- The method considers rotation invariance over all of SO(3), and not just a set of discrete rotations as is common in previous work.
- The proposed orientation pooling operation is interesting and leads to expressive filters that not are limited to being radially symmetric.
- The method performs well on the chosen datasets while being extremely parameter efficient.

### Weaknesses
 - The paper only considers two small datasets with relatively low resolution (50^3 and 28^3) volumetric models. It is not clear how the model performance scales as the resolution of the input increases. Specifically, the limited resolution may not fully capture the complexity of real-world 3D data, and it is unclear if the observed performance gains would generalize to higher-resolution datasets where finer details and more complex spatial relationships are present.
- Some analysis on the computational and memory complexity of the proposed convolution operation, compared to standard convolution, is missing. A detailed breakdown of the FLOPs and memory requirements for both training and inference would be beneficial. This should include a discussion of how the computational cost scales with input size, filter size, and the number of channels, which is crucial for assessing the practical applicability of the method.

### Questions
- How does the model perform on datasets with higher resolution data? Considering more diverse geometric datasets like ShapeNet with randomized orientations with higher resolution voxels might help to better demonstrate the generality of the method.
- Does the proposed convolution operation increase the training time compared to standard convolutions? Including some timing or FLOPS comparisons against related work would be helpful.
- Is it possible to achieve rotation sensitivity by making the method equivariant rather than invariant to rotations? Some discussion on this would be useful.
- Typo: Figure 2 x-axis label: sapling -> sampling

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a novel convolutional architecture for processing volumetric data, based on an orientation invariant convolution operation. The authors give a sound introduction to equivariant/invariant convolutions. The authors propose a method where convolutional kernels are constructed using spherical harmonics, which are subsequently applied to the input signal to obtain orientational feature fields expressed in a basis of circular harmonics. The signal is mapped back to a position-orientation scalar feature map, after which the authors then apply (soft-)max pooling over the orientation axis to map back to the original 3D domain. Authors show results on two datasets of 3D data, very clearly showing a significant reduction in the number of trainable parameters compared to baseline methods.

### Strengths
- Good related work section, sketches a clear context for the current work.
- Authors use figures to illustrate their approach.
-The model outperforms baselines significantly with only a fraction of the number of trainable parameters used, indicating the strength of this approach in these experimental settings.

### Weaknesses
My main concern is with regards to the clarity of the proposed method.
First, the manuscript seems to lack motivation for your approach. The authors are very thorough in their literature review, and include references and explanation of a lot of relevant equivariant/invariant approaches to convolutions in multiple domains. However, I’m not sure where this method fits in. What are the specific challenges with previous works in invariant/equivariant convolutions applied to 3D data that this method is proposing to alleviate? And how does it compare to previous works using spherical harmonics (e.g. [1, 2, 3]). You mention the need for avoiding a summation over the rotation axis, but I’m not sure where this follows from. Could you expand on this?

From what I gather your work seems like application of convolutions based on spherical harmonics followed by orientational pooling. Neither of these concepts are novel, nor is their combination.  Where is your contribution exactly, and what is its motivation? It seems this approach is severly limiting in the spatial composition of orientational patterns it is able to express, since architectures invariant to rotation are provably less expressive than equivariant architectures (e.g. see fig 1 in [4])

Second, the experiments are somewhat limited. Authors show results only on two datasets, neither of which is very widely carried in the field of learning on 3D data. I would be interested to see performance of your approach on larger-scale data, e.g. non-aligned ShapeNet, ModelNet, QM9.

### Questions
What is the motivation for your approach compared to equivariant 3D methods?
What exactly is the contribution of your approach? It seems you are simply applying spherical convolutions followed by orientational (soft-)max pooling? Or am I misunderstanding
Could you relate the steps in your derivation on page 5 to parts of figure 1? I am finding the figure itself somewhat hard to interpret.
Could you add references for the baseline methods you’re comparing against in the experimental section?
Are you planning to provide reference code for your implementation?
I am having a hard time interpreting Figure 2 and the corresponding experiment. What exactly are you trying to illustrate here? How does this toy setting relate to real-world data? 
For figure 3, is there any intuition to interpret the visualised filters here? To me, Fig3 and Fig4 show very similar patterns.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
